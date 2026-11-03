# Managed Reference: OpenDEAM Performance Metrics Catalog

**Status:** draft (v1.0.0) · **License:** CC-BY-4.0 (this document)

This library maintains a managed cross-reference relationship with the [OpenDEAM Performance Metrics Catalog](https://github.com/technehub-labs/dea-catalog-metrics) (`technehub-labs/dea-catalog-metrics`) — the canonical catalog of Performance Metric records for the `dea:PerformanceMetric` entity of the OpenDEAM metamodel (v0.2.1), Apache-2.0 licensed.

## What each side owns

| | OpenDEAM catalog (DEA) | mama-metrics (MAMA) |
|---|---|---|
| Defines | General enterprise Performance Metric records (4,400+), classified on 5 axes + directionality, MECE-unique | Automation-measurement **use**: metric cards with automation denominators, adverse-effect pairing, attribution and uncertainty rules |
| Authority for | The general semantics and identity of a performance metric | The automation-measurement operationalization: what counts in the denominator, what is reported alongside, what claims are allowed |
| License | Apache-2.0 | CC-BY-4.0 (cards/docs), Apache-2.0 (tools) |

**Neither side redefines the other.** A MAMA card referencing a DEA record does not import DEA's formula wholesale, and a DEA record referencing a MAMA card does not adopt MAMA's automation context as general semantics. Meanings stay distinct; the mapping carries the differences.

## The relationship is managed, not casual

1. **Single source of truth.** All cross-references live in [`dea-mapping.yaml`](dea-mapping.yaml). Cards cite DEA records only through it; DEA records cite MAMA cards only through the rows below. No free-floating references in either direction.
2. **Version-pinned.** The mapping pins the catalog commit (`reference.pinned_commit`). CI validates every `dea_record` against the catalog **at that commit** — references never float against a moving main branch.
3. **Typed relationships.** `relationship` is stated from the MAMA card's perspective:
   - `aligns_with` — same underlying construct and scope; local formula/denominator emphasis may differ.
   - `narrows` — the MAMA card is the DEA construct restricted to the automation-measurement context.
   - `broadens` — the MAMA card covers a wider construct than the (narrower) DEA record.
   - `proposes_upstream` — no adequate DEA record exists; the card is proposed as a future candidate record (see the upstream change request).
4. **Meaning notes are mandatory.** Every row carries a `meaning_note` stating where the two definitions agree, where they diverge, and what is *not* interchangeable (denominators, reporting obligations, pairing requirements).
5. **Drift is a review trigger, not a silent event.** If a referenced record's `lifecycle_status` or meaning changes upstream, CI fails the cross-reference check; a maintainer updates the row (or re-pins with justification) before merging anything else. Re-pinning is recorded in the mapping file's `revision_history`.
6. **Changes go through both processes.** Adding/changing a row requires a [Metric Proposal](https://github.com/Measuring-Automation-Managing-Autonomy/mama-metrics/issues/new?template=metric-proposal.yml) on the MAMA side, and — where the upstream record must gain or change its back-reference — a change request in the DEA catalog's own `change-requests/` process (currently CR-MET-021).

## Current state (2026-11-04)

- 15 rows: 12 mapped (`aligns_with`/`narrows`/`broadens`), 3 `proposes_upstream` (automation-eligibility-share, worker-experience-impact, distributional-effects).
- Upstream side: CR-MET-021 documents the relationship, defines the `external_references` item shape, and seeds back-references on the 12 mapped records.
- Validation: `python tools/validate_external_refs.py --catalog <local clone of the catalog>`; CI runs it against the pinned commit.

## Boundaries

- This relationship is **not** an equivalence, endorsement, or conformance claim in either direction (see [mama-framework external mappings](https://github.com/Measuring-Automation-Managing-Autonomy/mama-framework/blob/main/external-mappings.md)).
- MAMA metric-card validation (schema, MECE of meaning, adverse-effect pairing) is governed here; DEA record admission/classification is governed upstream. Neither CI gates the other's *content*, only the *references between them*.
- The lowercase `mama` autonomy method and its outputs are unrelated to this crosswalk and remain governed by [mama-integrations](https://github.com/Measuring-Automation-Managing-Autonomy/mama-integrations).
