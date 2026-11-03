# Attribution Guidance

**Status:** draft (v0.1.0)

Attribution is the defensible link between an observed outcome and the automation/autonomy change. Without it, you may report *change* — never *caused* ([interpretation rules](https://github.com/Measuring-Automation-Managing-Autonomy/mama-framework/blob/main/risk-value-interpretation.md) §3).

## The claim ladder

| Claim | Requires |
|---|---|
| "X changed after deployment" | A baseline and the after-measurement. Nothing more. |
| "X changed, consistent with the deployment" | Above + a stated mechanism + no obvious confound yet unexamined |
| "The deployment caused X" | A recorded **attribution design** (below), executed as stated, with confounds addressed and sensitivity checks reported |
| "The deployment will cause X" (forecast) | Above, ideally, or an explicitly labeled forecast with assumptions — never blended with observed results |

## Attribution designs, in ascending strength

1. **Before/after, confounds listed** — weakest. Acceptable only where nothing else changed; enumerate plausible confounds and argue each is absent or immaterial. Most real environments fail this test; say so.
2. **Before/after with adjustment** — control for documented confounds (seasonality, volume mix, staffing) with stated methods (e.g., matched windows, mix-adjusted rates). State what was *not* adjustable.
3. **Matched comparison** — a comparable unit/process without the change (another team, another region, another product line) measured over the same window. Disclose matching criteria and their weaknesses.
4. **Staged/controlled rollout** — the change is introduced gradually (by region, cohort, item class) with held-out comparison groups. Strongest common design; requires rollout authority to accept staged pacing.

## Recording the attribution

Every benefit claim in a review pack names: design used, confounds considered and their handling, data quality of the comparison, sensitivity result (does the claim survive a reasonable alternative assumption?), and the attribution status: **established / partially established / not established**. Unestablished attribution is a normal, publishable state — hiding it is not.

## Autonomy decisions are not attribution conclusions

Automation metrics (even well-attributed) are *context a grantor may consider* in the upstream `mama` review — they never mechanically expand or revoke autonomy grants ([integration contract](https://github.com/Measuring-Automation-Managing-Autonomy/mama-framework/blob/main/integration-contract.md) rule 4). Correlation is the interface; the governance loop decides.
