# Metric Taxonomy

**Status:** draft (v0.1.0)

MAMA's automation measurement is organized into seven categories. A card belongs to exactly one category. Categories describe *what question* a metric answers — never a target, maturity stage, or rank.

| Category | Question | Starter cards |
|---|---|---|
| **automation-coverage** | What share of work is (or can be) automated, and how much human touch remains? | automation-eligibility-share, automation-coverage, human-touch-ratio |
| **performance** | Does the automated work get done — correctly, on time, at volume? | straight-through-completion-rate, task-success-rate, service-latency, throughput |
| **quality** | Is the output right the first time? | output-quality-rate, rework-rate |
| **exceptions-reliability** | What bounces, escalates, breaks, or goes down — and how fast does it recover? | exception-rate, escalation-rate, availability, recovery-time |
| **cost-value** | What does a completed outcome cost, and did forecast benefits materialize? | cost-per-completed-outcome, realized-vs-forecast-benefit |
| **human-customer-impact** | What happens to workers and customers? | worker-experience-impact, customer-impact |
| **distributional** | Do outcomes and failures differ across affected groups? | distributional-effects |

## Practice-indicator cards

Two cards (`guardrail-drill-adherence`, `incident-learning-closure`) exist as
evidence hooks for the framework's [practice maturity
model](https://github.com/Measuring-Automation-Managing-Autonomy/mama-framework/blob/main/maturity-model.md)
([ADR-004](https://github.com/Measuring-Automation-Managing-Autonomy/mama-framework/blob/main/decisions/adr-004-practice-maturity-model.md)).
They are ordinary cards — not ladder rungs; the maturity model describes
operating practice and never turns these (or any card) into a target or score.

## Rules

1. **Categories are not a maturity ladder.** Moving work "down the list" is not progress; a use case may need distributional and impact measures from day one.
2. **Balanced sets.** A use-case baseline should draw from at least three categories, always including at least one of `human-customer-impact` or `distributional` for medium/high risk tiers (see the [risk/impact review](https://github.com/Measuring-Automation-Managing-Autonomy/mama-framework/blob/main/templates/risk-impact-review.md)).
3. **Cross-category caution.** Coverage without quality is volume without value; performance without distributional checks hides unequal effects. Never present a category subset as "the picture".
4. **No category mixes with autonomy outputs.** `mama` autonomy profiles (levels, dimensions, contracts) are a separate display — linked by use-case ID, never averaged or scored together (ADR-003).

## Extending the taxonomy

Propose new categories or cards via a [Metric Proposal issue](https://github.com/Measuring-Automation-Managing-Autonomy/mama-metrics/issues/new?template=metric-proposal.yml). Sector profiles (networks, software delivery, industrial robotics, public services, business operations) may map cards to sector KPIs but must not redefine card formulas — that would break cross-use comparability.
