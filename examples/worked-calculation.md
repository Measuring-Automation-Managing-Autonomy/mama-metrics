# Worked Calculation Example

**Status:** draft (v0.1.0) · Synthetic data throughout.

A miniature end-to-end example showing how card definitions, denominators, and uncertainty notes work together. Scenario: an invoice-processing use case (`usecase-ap-invoices`, synthetic) where 2,000 invoices/month were handled by a team of 6; an automated path was introduced; one quarter has elapsed.

## Step 1 — Baseline (recorded before deployment)

| Card (version) | Baseline | Mode | Notes |
|---|---|---|---|
| task-success-rate v0.1.0 | 96.2% (observed; n=6,038) | observed | Manual process; criterion: invoice approved & paid correctly per vendor confirmation |
| output-quality-rate v0.1.0 | 98.9% (observed; QA sample n=600) | observed | Defects mostly late-discovered (vendor statements) |
| service-latency v0.1.0 | p50 4.1 days, p95 9.3 days (end-to-end) | observed | Business-hours clock |
| cost-per-completed-outcome v0.1.0 | $14.80 (estimate; loading model v2) | estimate | Allocation sensitivity ±$1.10 |
| worker-experience-impact v0.1.0 | baseline wave recorded (response rate 83%) | observed | Instrument v3 |

## Step 2 — After one quarter (Q3 window, 5,850 invoices)

| Card | Value | Reading |
|---|---|---|
| automation-coverage v0.1.0 | 71% (observed; 4,154 of 5,850) | Eligibility criteria v1.2; denominator = assessed-eligible items |
| straight-through-completion-rate v0.1.0 | 64% (observed; n=5,850) | Strict intervention definition v1 |
| task-success-rate v0.1.0 | 96.6% (observed; n=5,850) | Same criterion version as baseline |
| output-quality-rate v0.1.0 | 98.1% (observed; automated QA + sample) | Late-discovery share fell 40%→22% |
| exception-rate v0.1.0 | 29% by class: input data 44%, rule gap 31%, review trigger 25% | Volume: 1,192 items to humans |
| service-latency v0.1.0 | p50 0.4 days, p95 2.2 days | Same clock definition |
| cost-per-completed-outcome v0.1.0 | $11.20 (estimate; loading model v2; sensitivity ±$0.90) | Amortization included per model |
| worker-experience-impact v0.1.0 | escalation burden 3.1→11.4 per worker-day; survey mean 3.4→3.1 (5-pt scale) | Response rate 61% ⚠ non-response bias assessed |

## Step 3 — Interpretation, under the rules

- **Coverage is not success.** 71% coverage coexists with a 29% exception rate — consistent, since coverage counts *entry* to the automated path and exceptions measure *exits*. Both reported.
- **Quality moved, in both directions.** Output quality dipped 0.8pp while late-discovery share fell — the automated QA layer catches defects earlier. Reported as a trade-off, not a headline.
- **The cost claim needs attribution discipline.** Unit cost fell $14.80 → $11.20 (−24%). Design: before/after with adjustment for volume mix; confounds: two senior staff rotated out mid-quarter. Status: **partially established** — the claim in the review pack reads "observed −24% (−$3.60); attribution partially established; sensitivity ±$0.90".
- **The workforce signal is adverse and reported.** Escalation burden more than tripled. This is a finding, not a footnote — the review must address staffing/oversight design before any scope expansion.
- **Distributional check (required, medium risk tier).** Success rate by vendor segment: large 97.1%, small 94.8% (n=412; interval ±2.1pp) — the gap is **indeterminate** at this sample size; reported as such, with a plan to re-check at 2 quarters.
- **No composite.** No "MAMA score" is computed; the pack shows the table above plus the linked `mama` autonomy profile for the delegated exception-approval domain — imported as issued (ruleset 2.0.0), never averaged with this table.

## What this example demonstrates

1. Baseline and after on identical card versions.
2. Adverse effects in the same view as benefits.
3. Attribution status stated, not implied.
4. Uncertainty carried through (counts, intervals, sensitivity).
5. Mode labels (observed/estimate) on every row.
