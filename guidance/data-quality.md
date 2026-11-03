# Data-Quality Guidance

**Status:** draft (v0.1.0)

Every metric value published under MAMA carries a data-quality note. This page defines the dimensions to record and the minimum honesty thresholds.

## Dimensions to record per measure

| Dimension | Question to answer |
|---|---|
| **Completeness** | What share of in-scope events does the source actually capture? (log loss, unmetered channels, offline work) |
| **Accuracy** | Do recorded events match reality? (timestamps, path classification, join integrity across systems) |
| **Attribution integrity** | Can events be assigned to items/users/groups correctly? (shared accounts, swivel-chair work, missing identity) |
| **Timeliness** | How fresh is the data at reporting time; does late-arriving data revise published values? |
| **Consistency** | Are definitions, taxonomies, and group attributes stable over the window? |
| **Provenance** | Which system, which extraction, which transformation, which version — can a third party reconstruct the number? |

## Minimum honesty thresholds

1. **Every published metric states its capture method and known gaps.** A metric without a data-quality note is not publishable in a review pack.
2. **Revisions are versioned.** If late data changes a published value, republish with the revision marked and the old value retained — silent revision is forbidden.
3. **Detection limits are disclosed** where the metric depends on detection (interventions, defects, exceptions): "we can only see what the logs record" belongs next to the number.
4. **Join integrity is tested** whenever a metric spans systems (entry-to-completion joins): report join-completeness.
5. **Log-integrity checks** for metrics that are gameable by suppressing records (STP, rework): periodic audit that suppression is not occurring.

## Known traps in automation measurement

- **Shadow tooling** — humans quietly fixing things outside the system (spreadsheets, chat requests) makes automation look cleaner than it is. Detect via sampling of worker journals and QA reconciliation.
- **Boundary games** — defining the process boundary to exclude the ugly parts. Boundary definitions are versioned records; changes require a note.
- **Definition drift** — downstream systems changing their own taxonomies mid-study. Freeze or map versions explicitly.
- **Survey/contact bias** — measuring experience only through channels the unhappy avoid.

## Privacy & minimization interface

Data quality never overrides data protection: minimization, pseudonymization, and small-cell suppression apply **before** analytics where feasible, and their effect on measurement (if material) is itself part of the data-quality note. Local-first processing is the default posture for MAMA tooling.
