# Baselining Guidance

**Status:** draft (v0.1.0)

A baseline is the recorded before-picture that makes after-claims checkable. Every MAMA use case records baselines **before** deployment scale-up ([template](https://github.com/Measuring-Automation-Managing-Autonomy/mama-framework/blob/main/templates/baseline-value-hypothesis.md)).

## What a valid baseline requires

1. **Same definition, different time.** Baseline and after-values must come from the same metric card version — formula, denominator, inclusions. If you change the card, you re-baseline and say so.
2. **A defensible window.** Long enough to cover the work's natural cycle (weekly rhythms, month-end peaks, seasonal events); short enough to be relevant. Record why the window is representative and what it might miss.
3. **The whole denominator.** The baseline counts failures, exceptions, and rework as they were — not the process as wished. A flattering baseline is a lie with a timestamp.
4. **Recorded provenance.** Window, data source, extraction method, card versions, known data-quality caveats, and who recorded it. A baseline nobody can reconstruct is not a baseline.
5. **Measurement mode labels.** State which baseline values are observed vs estimated (modeled). Estimates carry their method and uncertainty.

## Common failure modes

| Failure | Consequence | Prevention |
|---|---|---|
| Baseline from a different definition ("we used a broader success rule before") | After-comparison is meaningless | Card-version discipline; re-baseline on change |
| Cherry-picked window (quiet period before, peak after) | Manufactured improvement | Window rationale recorded; sensitivity check with a second window |
| No baseline ("we'll measure once it's running") | Benefits unclaimable; decisions uninformed | Stage gate 2 in the lifecycle — no scale-up without baseline |
| Baseline includes work that automation excludes | Denominator shift masquerading as improvement | Same inclusion/exclusion rules both sides, stated |
| Baseline invalidated silently (process reorg mid-study) | Confounded series | Record context changes in the evidence register |

## Multi-wave baselines

Where the process changes repeatedly, use rolling re-baselines: each material change closes the previous series (documented, kept for audit) and opens a new one with its own baseline. Comparing across series is a disclosure-laden exercise — describe the joins or don't draw the trend line.
