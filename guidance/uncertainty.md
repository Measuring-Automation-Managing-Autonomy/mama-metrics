# Uncertainty Guidance

**Status:** draft (v0.1.0)

MAMA numbers travel from dashboards into investment decisions. Uncertainty is not decoration — it is part of the measurement.

## The three measurement modes

| Mode | Meaning | Label required as |
|---|---|---|
| **Observed** | Directly measured from data in the stated window | `observed` + data-quality note |
| **Estimate** | Inferred: sampled, modeled, allocated, or otherwise mediated | `estimate` + method + uncertainty |
| **Forecast** | Projected before knowing the outcome | `forecast` + assumptions + date of forecast |

Rules: never blend modes in one chart element; never present a forecast where a decision expects an observation; never restate a forecast after results are known (that belongs to [realized-vs-forecast-benefit](../cards/realized-vs-forecast-benefit.yaml)).

## Expressing uncertainty

- **Percentages on finite counts** carry binomial noise: report counts (e.g., "82% of 3,400" not "82%"). Where groups are compared, show intervals; a gap smaller than its interval is **indeterminate**, not zero.
- **Percentiles** need the event count behind them: "p95 (n=214)".
- **Allocations and models** (unit cost, benefit lines): sensitivity-check the dominant assumption and report the range, not a false-precision point.
- **Surveys**: report response rate and distribution, not just means; anonymity design bounds validity.
- **Rare events** (outages, severe defects): absence in a window is weak evidence — report the window's event count and cumulative history.

## Honest vocabulary

| Instead of… | Say… |
|---|---|
| "Improved by 23%" | "Observed 23% change; attribution not established (before/after only)" |
| "No impact" | "No detectable difference; interval spans ±X" |
| "Accurate to 99%" | "Observed defect rate 1.0% (n=…); detection method: …" |
| "We expect savings of…" | "Forecast: … under assumptions …, made on …" |

## Small numbers, small groups

Distributional cuts on small groups produce unstable estimates. Use confidence intervals, aggregate where honest, and apply small-cell suppression for privacy — but never let suppression erase a documented affected group from the record; state what was suppressed and why ([distributional-effects](../cards/distributional-effects.yaml)).
