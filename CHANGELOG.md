# Changelog — mama-metrics

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); semver.

## [0.1.1] — 2026-11-04

### Added

- Managed cross-reference relationship with the OpenDEAM Performance Metrics Catalog (`technehub-labs/dea-catalog-metrics`):
  - `external/dea-catalog-metrics.md` — reference & meaning policy (single source of truth, version-pinned, typed relationships, drift = review trigger)
  - `external/dea-mapping.yaml` — 15-row crosswalk (12 mapped cards ↔ `dea:PerformanceMetric` records; 3 cards proposed upstream) pinned to catalog commit `c2a2951`
  - `tools/validate_external_refs.py` — crosswalk validator (structure, card citations, catalog existence + lifecycle drift at the pinned commit)
  - CI job `dea-crosswalk` cloning the catalog at the pinned commit
  - DEA citations appended to the 15 cards' `references`

## [0.1.0] — 2026-11-04

### Added (initial scaffold, CR MAMA-ORG-CR-001)

- Metric taxonomy (7 categories)
- Metric-card schema v1.0.0 (JSON Schema draft 2020-12)
- 18 starter metric cards across automation coverage, performance, quality, exceptions/reliability, cost/value, human/customer impact, and distributional effects — all `draft` status
- Guidance: baselining, attribution, uncertainty, data quality
- Worked calculation example
- Card validator (`tools/validate_cards.py`) + CI workflow

[0.1.0]: https://github.com/Measuring-Automation-Managing-Autonomy/mama-metrics/releases/tag/v0.1.0
