# ARIS4C019 · Pilot-0 Analysis Freeze v0.1

**Frozen:** 2026-09-21  
**Stage:** pre-outcome / no-effect-look

> This file freezes the first inferential design before any post-reform Life Ladder effect is inspected. Changes after outcome inspection must be versioned as deviations, never silently overwritten.

## 1. Research target

Estimate whether verified increases in statutory paid annual leave are followed by changes in population life evaluation within countries over time.

This is not a cross-country “vacation days vs happiness” ranking.

## 2. Unit and outcome

- Unit: country-year.
- Primary outcome: annual Gallup/World Happiness Report **Life Ladder**.
- No interpolation of missing Life Ladder years.
- Positive/negative affect are secondary and remain locked until the Life Ladder analysis is complete.
- WHR variables such as social support, freedom, generosity and corruption are **not** primary controls because they may be mediators or post-treatment variables.

## 3. Exposure

Primary exposure is a **verified statutory paid annual-leave reform**.

Keep separate:
- paid annual leave;
- public holidays;
- actual annual/weekly working hours;
- actual leave utilization.

The World Bank Employing Workers panel is a corroborating measurement source, not the legal authority for a reform date.

## 4. Event-time rule

Because the outcome is annual and interview month is not available, the **event clock is the verified legal effective year**, not the first full post year.

- Pre-period: legal effective year **−4 through −1**.
- Reference period: **k = −1**, always the last full untreated calendar year.
- Reform effective on **January 1** → legal effective year is fully exposed and enters post-treatment at **k = 0**.
- Reform effective after January 1 → legal effective year is a **transition year (k = 0) and is excluded** from event estimation; the following calendar year is the first full post year (**k = +1**).
- Verified year without an exact day → conservatively treat that legal year as a transition year and begin full post exposure at **k = +1**.
- Post window ends at legal effective year **+4**.
- Missing survey years remain missing; no outcome interpolation is permitted.

This rule prevents a partly exposed reform year from being misclassified as a pre-treatment observation and keeps event time anchored to the legal intervention itself.

## 5. Event tiers

- **Tier A — corroborated:** legal timing verified, WHR coverage passes, and the World Bank leave panel records a directionally compatible discontinuity.
- **Tier B — legal-only:** legal timing verified and WHR coverage passes, but the historical World Bank panel does not independently show the discontinuity.
- **Tier C — provisional:** legal timing remains unverified.

Headline primary pool:
- Tier A only;
- direction must be explicitly increase / introduced / decrease;
- no event is promoted or demoted based on observed happiness changes.

Current special handling:
- Lithuania remains design sensitivity until the annual-leave direction is independently isolated from the broader Labour Code package.
- United Kingdom stages remain Tier-B sensitivity because the World Bank historical panel is backfilled at a constant 28 days and cannot corroborate the legal step changes.

## 6. Donor / control eligibility

For each event, a candidate donor must:

1. have at least 2 observed pre and 2 observed post Life Ladder years inside the frozen window;
2. not be the focal treated country;
3. have no World Bank annual-leave jump inside the focal event window (conservative contamination screen);
4. have no verified paid-leave treatment inside the focal event window;
5. not require interpolated outcome values.

Not-yet-treated countries may serve as donors outside their own treatment window.

## 7. Estimation hierarchy

Because the treated-country count is small, no single pooled coefficient will carry the scientific claim.

**Primary evidence**
1. event-specific treatment estimates against clean donor pools;
2. pooled modern staggered-adoption group-time ATT / event-time aggregation.

**Required robustness**
- Callaway–Sant'Anna style group-time ATT;
- Sun–Abraham style heterogeneous event-study specification;
- ordinary TWFE event study only as a descriptive comparator, never the headline estimator;
- leave-one-event-out pooled estimates;
- Tier-A-only vs Tier-A+Tier-B sensitivity.

## 8. Predefined macro/scope sensitivities

Report the full frozen primary pool, then prespecified sensitivity sets excluding:

- events whose legal/treatment window overlaps the 2008–2010 global financial crisis;
- events whose post window overlaps 2020–2021 COVID disruption;
- jurisdiction-limited reforms (e.g. Canada federal jurisdiction);
- broad labour-code packages;
- multistage reforms;
- Tier-B events.

These exclusions are not chosen using effect sizes.

## 9. Covariates

Preferred pre-specified macro covariates, subject to source/coverage freeze before effect estimation:

- log GDP per capita;
- unemployment rate;
- inflation.

Use **pre-treatment / lagged baseline summaries for adjustment or donor construction**. Do not condition the headline effect on contemporaneous post-treatment macro variables that could themselves respond to the reform.

Do not add controls because they improve statistical significance.

## 10. Falsification / failure conditions

The strong interpretation must be weakened if:

- pre-treatment trajectories are incompatible with the identifying design;
- donor/common support is inadequate;
- estimates are dominated by one event;
- results reverse under prespecified crisis/scope sensitivities;
- legal timing or entitlement direction cannot be independently verified;
- outcome coverage is too sparse for the declared event window.

Null and heterogeneous results are valid outcomes.

## 11. Outcome firewall

Before the design gate is explicitly unlocked:

- scripts may inspect country/year availability;
- scripts may inspect leave-law values, reform dates and donor contamination;
- scripts must **not** print, plot, rank, regress, summarize or compare post-treatment Life Ladder values.

The next executable gate is therefore an **outcome-blind donor/support diagnostic**.
