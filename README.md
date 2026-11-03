# mama-metrics

**MAMA** (Measuring Automation & Measuring Autonomy) — versioned metric taxonomy and automation/value/impact metric cards.

**Status:** `draft` (v0.1.0) · **License:** CC-BY-4.0 · **Maintainer:** see [MAINTAINERS.md](MAINTAINERS.md)

This repository defines **MAMA automation measurement** — how much eligible work is automated, how well the automated process performs, and what outcomes and effects it produces. These metrics are MAMA's own capability; they are **not** supplied by, and never merged with, the lowercase `mama` autonomy score (see the [framework's interpretation rules](https://github.com/Measuring-Automation-Managing-Autonomy/mama-framework/blob/main/risk-value-interpretation.md)).

## How to use

1. Pick cards from [`cards/`](cards/) for your baseline ([template](https://github.com/Measuring-Automation-Managing-Autonomy/mama-framework/blob/main/templates/baseline-value-hypothesis.md)).
2. Record the card **version** with every value — definitions are versioned and change via ADR.
3. Set your own baseline and target; the library publishes **no universal targets**.
4. Report adverse effects alongside benefits. Label observed / estimate / forecast.

## Metric taxonomy

| Category | Answers |
|---|---|
| `automation-coverage` | What share of work is (or can be) automated, and how much human touch remains? |
| `performance` | Does the automated work get done, correctly, on time, at volume? |
| `quality` | Is the output right the first time? |
| `exceptions-reliability` | What bounces, escalates, breaks, or goes down — and how fast does it recover? |
| `cost-value` | What does a completed outcome cost, and did forecast benefits materialize? |
| `human-customer-impact` | What happens to workers and customers? |
| `distributional` | Who bears the effects — and do they differ across groups? |

## Metric cards (starter library, all `draft`)

| Card | Category | One-line purpose |
|---|---|---|
| [automation-eligibility-share](cards/automation-eligibility-share.yaml) | automation-coverage | Share of assessed work volume that is eligible for automation |
| [automation-coverage](cards/automation-coverage.yaml) | automation-coverage | Share of eligible items actually processed by the automated path |
| [human-touch-ratio](cards/human-touch-ratio.yaml) | automation-coverage | Degree of human involvement remaining in automated-eligible work |
| [straight-through-completion-rate](cards/straight-through-completion-rate.yaml) | performance | Items completed with no manual intervention or rework |
| [task-success-rate](cards/task-success-rate.yaml) | performance | Items completed to the defined success criterion |
| [service-latency](cards/service-latency.yaml) | performance | Time to complete, at percentiles |
| [throughput](cards/throughput.yaml) | performance | Completed outcomes per unit time at sustained load |
| [output-quality-rate](cards/output-quality-rate.yaml) | quality | Outputs meeting quality criteria without correction |
| [rework-rate](cards/rework-rate.yaml) | quality | Outputs requiring correction after completion |
| [exception-rate](cards/exception-rate.yaml) | exceptions-reliability | Items leaving the automated path |
| [escalation-rate](cards/escalation-rate.yaml) | exceptions-reliability | Items needing human authority beyond the process |
| [availability](cards/availability.yaml) | exceptions-reliability | Share of scheduled time the capability is operable |
| [recovery-time](cards/recovery-time.yaml) | exceptions-reliability | Time to restore service after failure |
| [cost-per-completed-outcome](cards/cost-per-completed-outcome.yaml) | cost-value | Fully loaded cost of one completed outcome |
| [realized-vs-forecast-benefit](cards/realized-vs-forecast-benefit.yaml) | cost-value | Actual benefit against the recorded forecast, with attribution status |
| [worker-experience-impact](cards/worker-experience-impact.yaml) | human-customer-impact | Measured change in work quality, workload, and oversight burden |
| [customer-impact](cards/customer-impact.yaml) | human-customer-impact | Measured change in customer outcomes and redress |
| [distributional-effects](cards/distributional-effects.yaml) | distributional | Disparity of outcomes and failures across affected groups |

## Schema & validation

- [`schema/metric-card.schema.json`](schema/metric-card.schema.json) (schema version 1.0.0) — required fields per the CR: definition, formula, unit, denominator, inclusion/exclusion, data source, sampling, time window, owner, baseline, target guidance, uncertainty, limitations, review cadence.
- Validate: `python tools/validate_cards.py cards/` (requires `jsonschema`, `pyyaml`).
- CI validates every card on push (see `.github/workflows/validate.yml`).

## Guidance

| Doc | Covers |
|---|---|
| [guidance/baselining.md](guidance/baselining.md) | Choosing windows, comparability, recording baselines |
| [guidance/attribution.md](guidance/attribution.md) | When you may claim causation; comparison designs |
| [guidance/uncertainty.md](guidance/uncertainty.md) | Observed vs estimate vs forecast; sampling error |
| [guidance/data-quality.md](guidance/data-quality.md) | Data-quality dimensions to record per use |

## Versioning policy

- Cards: semver. Fixing errors without changing meaning = PATCH; additive optional fields = MINOR; changing formula/denominator/inclusions = MAJOR (new card version, migration note, old card marked `deprecated`).
- Schema: semver; additive optional properties = MINOR; new required fields = MAJOR.
- No card ever prescribes a universal target. No card mixes automation measures with `mama` autonomy outputs.

## External references (managed crosswalks)

This library maintains a **managed cross-reference relationship** with the [OpenDEAM Performance Metrics Catalog](https://github.com/technehub-labs/dea-catalog-metrics) — 12 of our cards are mapped to `dea:PerformanceMetric` records (typed `aligns_with`/`narrows`/`broadens` with mandatory meaning notes), and 3 cards are proposed upstream as candidate records.

- Policy & rules: [`external/dea-catalog-metrics.md`](external/dea-catalog-metrics.md) — single source of truth for all cross-references, version-pinned to a catalog commit, CI-validated with drift detection.
- Mapping: [`external/dea-mapping.yaml`](external/dea-mapping.yaml).
- Validate locally: `python tools/validate_external_refs.py --catalog <clone of dea-catalog-metrics>`.

## License

[CC-BY-4.0](LICENSE) for cards, schema, and docs; Apache-2.0 for `tools/` code. See the [license policy](https://github.com/Measuring-Automation-Managing-Autonomy/.github/blob/main/LICENSE-POLICY.md).
