#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Validate the managed crosswalk to the OpenDEAM dea-catalog-metrics catalog.

Usage:
    python tools/validate_external_refs.py [--mapping external/dea-mapping.yaml]
                                           [--catalog PATH_TO_CLONE]

Checks the mapping file's structure and, when --catalog is given (a clone of
technehub-labs/dea-catalog-metrics at the pinned commit), verifies that every
referenced record exists there with the recorded lifecycle status. A mismatch
is a DRIFT: the row must be reviewed and re-pinned by a maintainer (see
external/dea-catalog-metrics.md rule 5) — this tool never auto-updates.

Exit code 0 iff the crosswalk is consistent. Requires: pyyaml (and nothing else).
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("error: pyyaml is required (pip install pyyaml)")

RELATIONSHIPS = {"aligns_with", "narrows", "broadens", "proposes_upstream"}
DEA_LIFECYCLE = {"candidate", "admitted", "active", "deprecated", "retired"}
DEA_ID_RE = re.compile(r"^dea:metric-[a-z0-9][a-z0-9-]*$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")

REQUIRED_REFERENCE = (
    "catalog_repo",
    "catalog_entity",
    "metamodel",
    "catalog_license",
    "pinned_commit",
    "pinned_at",
    "upstream_change_request",
)


def fail(msg: str) -> None:
    print(f"FAIL {msg}")


def ok(msg: str) -> None:
    print(f"ok   {msg}")


def load_mapping(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise SystemExit(f"error: {path} must be a YAML mapping")
    return data


def check_reference_block(mapping: dict, errors: int) -> int:
    ref = mapping.get("reference") or {}
    for key in REQUIRED_REFERENCE:
        if not ref.get(key):
            fail(f"reference.{key} missing/empty")
            errors += 1
    if not SHA_RE.match(str(ref.get("pinned_commit", ""))):
        fail(f"reference.pinned_commit {ref.get('pinned_commit')!r} is not a 40-hex commit SHA")
        errors += 1
    try:
        datetime.date.fromisoformat(str(ref.get("pinned_at", "")))
    except ValueError:
        fail(f"reference.pinned_at {ref.get('pinned_at')!r} is not an ISO date")
        errors += 1
    return errors


def check_rows(mapping: dict, errors: int) -> tuple[int, dict]:
    rows = mapping.get("mappings")
    if not isinstance(rows, list) or not rows:
        fail("mappings must be a non-empty list")
        return errors + 1, {}

    seen: set[tuple[str, str]] = set()
    valid_rows: dict[str, dict] = {}
    for i, row in enumerate(rows):
        label = f"mappings[{i}]"
        card = row.get("mama_card")
        rel = row.get("relationship")
        if rel not in RELATIONSHIPS:
            fail(f"{label}: relationship {rel!r} not in {sorted(RELATIONSHIPS)}")
            errors += 1
            continue
        if rel == "proposes_upstream":
            if row.get("dea_record") is not None:
                fail(f"{label}: proposes_upstream rows must have dea_record: null")
                errors += 1
            if not row.get("cr_ref"):
                fail(f"{label}: proposes_upstream rows must name cr_ref (the upstream CR)")
                errors += 1
            if card:
                valid_rows[card] = row
            continue

        if not isinstance(card, str) or not card:
            fail(f"{label}: mama_card missing")
            errors += 1
            continue
        if not (REPO_ROOT / "cards" / f"{card}.yaml").exists():
            fail(f"{label}: card file cards/{card}.yaml does not exist")
            errors += 1
            continue
        dea_id = row.get("dea_record")
        if not isinstance(dea_id, str) or not DEA_ID_RE.match(dea_id):
            fail(f"{label}: dea_record {dea_id!r} does not match dea:metric-<slug>")
            errors += 1
            continue
        if not row.get("dea_name"):
            fail(f"{label}: dea_name missing")
            errors += 1
        if row.get("dea_lifecycle") not in DEA_LIFECYCLE:
            fail(f"{label}: dea_lifecycle {row.get('dea_lifecycle')!r} invalid")
            errors += 1
        if "meaning_note" not in row or not str(row.get("meaning_note", "")).strip():
            fail(f"{label}: meaning_note is mandatory (policy rule 4)")
            errors += 1
        if not isinstance(row.get("upstream_reference_added"), bool):
            fail(f"{label}: upstream_reference_added must be a boolean")
            errors += 1
        key = (card, dea_id)
        if key in seen:
            fail(f"{label}: duplicate mapping {key}")
            errors += 1
        seen.add(key)
        valid_rows[card] = row
    return errors, valid_rows


def check_card_citations(valid_rows: dict, errors: int) -> int:
    for card, row in valid_rows.items():
        card_path = REPO_ROOT / "cards" / f"{card}.yaml"
        text = card_path.read_text(encoding="utf-8")
        marker = (
            row["dea_record"]
            if row["relationship"] != "proposes_upstream"
            else str(row.get("cr_ref", "CR-MET-?"))
        )
        if marker not in text:
            fail(f"cards/{card}.yaml does not cite {marker} — cards must cite through the crosswalk")
            errors += 1
    return errors


def check_catalog(valid_rows: dict, catalog_dir: Path, errors: int) -> int:
    registry = catalog_dir / "CATALOG.yaml"
    if not registry.exists():
        fail(f"--catalog {catalog_dir} has no CATALOG.yaml (clone at the pinned commit)")
        return errors + 1
    with registry.open(encoding="utf-8") as fh:
        catalog = yaml.safe_load(fh)
    entities = {e["id"]: e for e in catalog["catalog"]["entities"]}
    for card, row in valid_rows.items():
        if row["relationship"] == "proposes_upstream":
            continue
        dea_id = row["dea_record"]
        ent = entities.get(dea_id)
        if ent is None:
            fail(f"DRIFT: {dea_id} (mapped from {card}) not found in catalog at pinned commit")
            errors += 1
            continue
        actual = ent.get("lifecycle_status")
        if actual != row["dea_lifecycle"]:
            fail(
                f"DRIFT: {dea_id} lifecycle changed: mapping says {row['dea_lifecycle']!r}, "
                f"catalog says {actual!r} — review the row and re-pin (policy rule 5)"
            )
            errors += 1
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mapping", default=str(REPO_ROOT / "external" / "dea-mapping.yaml"))
    parser.add_argument("--catalog", default=None, help="clone of dea-catalog-metrics at pinned_commit")
    args = parser.parse_args()

    mapping = load_mapping(Path(args.mapping))
    errors = 0
    errors = check_reference_block(mapping, errors)
    errors, valid_rows = check_rows(mapping, errors)
    errors = check_card_citations(valid_rows, errors)
    if args.catalog:
        errors = check_catalog(valid_rows, Path(args.catalog), errors)

    total = len(mapping.get("mappings", []))
    if errors:
        print(f"\ncrosswalk INVALID: {errors} error(s) across {total} rows")
        return 1
    print(f"\ncrosswalk valid: {total} rows"
          + (f" (verified against catalog at pinned commit)" if args.catalog else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
