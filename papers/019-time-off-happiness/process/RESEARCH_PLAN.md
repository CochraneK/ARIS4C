# ARIS4C019 · Research Plan v0.2

> **2026-09-24 scope correction:** Historical expansion supersedes the narrow Pilot-0 scope as the project-level research plan. The completed leave-specific Life Ladder study remains a frozen causal sub-study; it is not the whole ARIS4C019. Canonical expansion details: `HISTORICAL_EXPANSION_PLAN.md` and `HISTORICAL_SOURCE_MATRIX.md`.

## Expanded project question

How did statutory and realized time off evolve across countries over the long twentieth century and early twenty-first century, and how are those changes associated with — and, where quasi-experimental identification is credible, causally related to — subjective well-being?

The project now targets: institutional/legal history from the early twentieth century with systematic ILO anchors from 1936 onward; subjective-well-being evidence from 1945 onward; Eurobarometer from 1973; WVS/EVS from 1981; and annual Gallup-era analysis from the mid-2000s onward. Modern cross-sectional legal coverage should target all 193 UN member states where source licenses/coverage permit.

---

## Preserved Pilot-0 plan

## Working question

When countries expand or reduce legally guaranteed time off, or when actual working time changes materially, does population subjective well-being change afterward?

## Why longitudinal change is primary

A raw cross-country association between vacation entitlement and happiness is heavily confounded by income, institutions, labor-market quality, welfare states, culture, health, inequality and measurement differences.

Therefore the design hierarchy is:

1. within-country longitudinal change;
2. policy-reform event studies / staggered difference-in-differences where identifying assumptions are defensible;
3. matched or synthetic-control case studies for large reforms;
4. cross-sectional comparisons only as descriptive context.

## Exposure hierarchy

### E1 · Statutory paid annual leave — primary policy exposure

Measure legally guaranteed paid annual-leave days under comparable worker/tenure assumptions. Preserve eligibility rules and whether entitlements depend on tenure.

### E2 · Actual annual working hours — primary realized-time exposure

Use within-country trends rather than naïve level comparisons when source definitions differ.

### E3 · Statutory public holidays — secondary

Keep separate from annual leave. Public holidays may be fixed, substitute, moved, clustered or not universally observed.

### E4 · Leave utilization / effective time off — tertiary

Where surveys or administrative data allow, measure days actually taken. Do not infer use from legal entitlement.

## Outcome hierarchy

### O1 · Life evaluation / life satisfaction — primary

Prefer harmonized 0–10 measures with known survey methodology and adequate country-year coverage.

### O2 · Positive/negative affect — secondary

Use only where harmonization is defensible.

### O3 · Mental/physical health and burnout — mechanism/supplement

Useful for triangulation but not interchangeable with population happiness.

## Main hypotheses

**H1. Policy time-off hypothesis:** increases in guaranteed paid leave are followed by higher life evaluation on average, conditional on macroeconomic and institutional shocks.

**H2. Realized-time hypothesis:** reductions in actual working time predict well-being gains more strongly than nominal entitlement alone.

**H3. Implementation hypothesis:** effects are larger where entitlement is more likely to be used/enforced.

**H4. Nonlinearity hypothesis:** marginal gains may be larger when starting from very long working time / low leave entitlement than at already-high time-off levels.

These are hypotheses, not assumed truths. Null, heterogeneous or adverse results remain informative.

## Identification strategy

### Stage A · Coverage and measurement freeze

Build a country-year matrix before examining outcome relationships:

- statutory annual leave;
- public holidays where reliable;
- actual hours worked;
- life satisfaction;
- GDP per capita;
- unemployment;
- inflation;
- labor-force structure;
- social expenditure / welfare-state controls where available;
- population and major crisis indicators.

Freeze source priority and transformations.

### Stage B · Descriptive decomposition

Estimate how much change in total work-year exposure comes from:

- statutory leave reforms;
- public-holiday reforms;
- weekly-hours reforms;
- changes in actual hours / part-time composition.

### Stage C · Within-country panel

Country and year fixed effects, clustered inference, lag structures and pre-trend diagnostics. Avoid interpreting two-way fixed-effects coefficients causally when treatment timing/heterogeneity invalidates the estimator.

### Stage D · Policy-event design

Identify discrete reforms in paid leave or standard working time. Use modern staggered-adoption/event-study estimators where appropriate, explicitly inspect pre-trends and anticipation.

### Stage E · Robustness

- leave-one-country-out;
- region-specific estimates;
- alternative happiness sources;
- alternative time-off definitions;
- placebo reform years;
- leads/lags;
- major-crisis exclusions;
- weighting vs unweighted country estimands;
- sensitivity to GDP/unemployment/inflation controls.

## Key threats

- richer and better-governed countries both mandate more leave and report higher well-being;
- statutory leave may not be taken;
- happiness surveys differ in sampling and timing;
- reforms may be responses to political/economic conditions that also alter well-being;
- labor-market composition changes can reduce aggregate hours without increasing leisure for the same workers;
- public holidays are not equivalent to annual leave;
- simultaneity and slow adaptation may blur timing.

## First bounded unit

1. build a source-by-country-by-year coverage matrix;
2. freeze the definition of statutory paid annual leave;
3. enumerate policy changes with exact effective dates;
4. select a primary happiness series based on annual coverage;
5. produce a pre-analysis table of feasible reform events before estimating any treatment effect.
