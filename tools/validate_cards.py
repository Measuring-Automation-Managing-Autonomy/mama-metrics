#!/usr/bin/env python3
"""Validate MAMA metric cards against the metric-card schema.

Usage:
    python tools/validate_cards.py [CARDS_DIR] [--schema SCHEMA_PATH]

Defaults: CARDS_DIR=<repo>/cards, SCHEMA_PATH=<repo>/schema/metric-card.schema.json.

Checks, per card:
  1. Valid YAML
  2. Valid against schema/metric-card.schema.json (draft 2020-12)
  3. Cross-checks: `status` matches the README index table; card `version`
     parses as semver; `related_metrics` reference existing card ids.

Exit code 0 iff all cards pass. Requires: pyyaml, jsonschema.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("error: pyyaml is required (pip install pyyaml)")

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover
    sys.exit("error: jsonschema is required (pip install jsonschema)")

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
CARD_STATUSES = {"draft", "pilot", "reviewed", "stable", "deprecated", "archived"}


def load_schema(schema_path: Path) -> dict:
    with schema_path.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_card(path: Path) -> tuple[dict | None, str | None]:
    try:
        with path.open(encoding="utf-8") as fh:
            card = yaml.safe_load(fh)
    except yaml.YAMLError as exc:
        return None, f"invalid YAML: {exc}"
    if not isinstance(card, dict):
        return None, "card must be a YAML mapping"
    return card, None


def cross_check(card: dict, known_ids: set[str]) -> list[str]:
    """Checks the JSON schema cannot express."""
    problems: list[str] = []
    if not SEMVER.match(str(card.get("version", ""))):
        problems.append(f"version {card.get('version')!r} is not semver")
    if card.get("status") not in CARD_STATUSES:
        problems.append(f"status {card.get('status')!r} is not a valid artifact label")
    target = str(card.get("target_guidance", "")).lower()
    for phrase in ("every organization should", "universal target is", "target is 9"):
        if phrase in target:
            problems.append(f"target_guidance looks like a universal target ({phrase!r})")
    for rel in card.get("related_metrics", []) or []:
        if rel not in known_ids:
            problems.append(f"related_metrics references unknown card id {rel!r}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cards_dir", nargs="?", default=str(REPO_ROOT / "cards"))
    parser.add_argument("--schema", default=str(REPO_ROOT / "schema" / "metric-card.schema.json"))
    args = parser.parse_args()

    cards_dir = Path(args.cards_dir)
    schema_path = Path(args.schema)
    schema = load_schema(schema_path)
    validator = Draft202012Validator(schema)

    paths = sorted(cards_dir.glob("*.yaml"))
    if not paths:
        print(f"error: no cards found in {cards_dir}")
        return 2

    # First pass: collect ids for cross-reference checks.
    loaded: dict[Path, dict] = {}
    failures = 0
    for path in paths:
        card, err = load_card(path)
        if err:
            print(f"FAIL {path.name}: {err}")
            failures += 1
        else:
            loaded[path] = card
    known_ids = {c["id"] for c in loaded.values() if c and "id" in c}

    for path, card in loaded.items():
        errors = sorted(validator.iter_errors(card), key=lambda e: list(e.path))
        for err in errors:
            where = "/".join(str(p) for p in err.absolute_path) or "<root>"
            print(f"FAIL {path.name}: schema error at {where}: {err.message}")
            failures += 1
        for problem in cross_check(card, known_ids):
            print(f"FAIL {path.name}: {problem}")
            failures += 1
        if not errors and not cross_check(card, known_ids):
            print(f"ok   {path.name}  (id={card['id']} v{card['version']} {card['status']})")

    total = len(paths)
    print(f"\n{total - failures}/{total} cards valid ({failures} failure(s))")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
