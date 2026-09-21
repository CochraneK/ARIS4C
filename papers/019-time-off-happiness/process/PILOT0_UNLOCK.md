# ARIS4C019 · Pilot-0 Outcome Unlock v1

**Unlocked:** 2026-09-21  
**Scope unlocked:** annual WHR/Gallup **Life Ladder only**  
**Still locked:** Positive affect and Negative affect

> This manifest marks the first permitted inspection of post-reform Life Ladder values. No post-reform Life Ladder effect was printed, plotted, ranked, regressed, summarized, or compared before this unlock.

## 1. Frozen scientific state at unlock

### Treatment/event clock

- Legal effective year is the event clock.
- Pre = legal year T-4 through T-1.
- Reference = T-1.
- January-1 reforms may enter post at k=0.
- Reforms effective after January 1 have transition year T excluded from event estimation and first full post at k=+1.
- No outcome interpolation.

Relevant commits:
- `03984a7ee90add9236b1facde4c71de3b70713a2` — exclude partial-exposure years from pre window.
- `29c634edb4ceaf4216c195186808c3492d4ec6e6` — align donor diagnostics to legal-year event clock.
- `10875f1f1a9560c18fb8657a698c07e483f09f14` — align analysis freeze wording to legal-year event clock.

### Headline primary event pool

Exactly **8 Tier-A events** are unlocked for the headline Pilot-0 pool:

1. China — 2008-01-01
2. Croatia — 2010-01-01
3. Kosovo — 2010-12-16
4. Kuwait — 2010-02-21
5. Bahrain — 2012-09-02
6. Taiwan, China — 2017-01-01
7. Luxembourg — 2019-01-01
8. Canada — 2019-09-01

No event may be promoted, demoted, added, or removed based on its observed Life Ladder effect.

Lithuania remains a non-headline design sensitivity.  
United Kingdom remains Tier-B legal-only sensitivity.

### Donor support

At the last outcome-blind diagnostic:

- headline primary events with >=10 clean donors: **8/8**;
- headline primary events with >=20 clean donors: **8/8**;
- clean-donor counts range from **80 to 124**.

The donor screen uses outcome availability and treatment/leave contamination only; it does not use post-treatment Life Ladder values.

### Macro covariates

Frozen variables:

- WHR `Log GDP per capita`;
- WDI `SL.UEM.TOTL.ZS` unemployment, modeled ILO estimate;
- WDI `FP.CPI.TOTL.ZG` CPI inflation.

All use pre-treatment T-4...T-1 summaries only for balance/donor/sensitivity work.

Coverage gate:

- **6/8** headline events have >=2 pre observations for all three frozen covariates.
- Taiwan has no matched WDI unemployment or inflation in this gate.
- Kosovo has no matched WDI unemployment in this gate.
- These missing covariates do **not** justify dropping the events after outcome inspection; instead, analyses requiring all three covariates form a prespecified covariate-limited sensitivity subset.

Relevant commits:
- `5c42da51b3966253f8b103e5285c0ae791be0dc3` — covariate source freeze.
- `def0681321a257da05b6aaa8c45434a5c45c47df` — outcome-blind covariate gate.
- `f0184fb0acd5d08414a9c0089296f791e5a8eec8` — CI integration.
- `66e91862c62d9af0b0c6ae455d9323646bd55550` — generated gate artifacts.

## 2. First permitted outcome look

The first outcome script may:

1. read annual Life Ladder values;
2. construct event-specific trajectories using the frozen legal-year clock;
3. compare treated-country change from T-1 with the same-calendar-year change among the already frozen clean donor pool;
4. show pre-period placebo/event-time gaps and full-post gaps;
5. pool event-time estimates descriptively across the eight frozen headline events.

The first outcome look is a **diagnostic Pilot-0**, not the final causal estimator.

It must not:

- change the event pool based on effects;
- choose covariates based on significance;
- unlock positive/negative affect;
- describe a descriptive donor-adjusted gap as definitive causal evidence;
- hide null, adverse, or heterogeneous event estimates.

## 3. Next inferential gate

Before a manuscript-level causal claim:

- implement modern staggered-adoption/group-time ATT where support permits;
- implement a heterogeneous-treatment event-study robustness specification;
- report TWFE only as a comparator;
- run leave-one-event-out;
- report Tier-A-only vs Tier-A+Tier-B sensitivity;
- report prespecified GFC, COVID, jurisdiction-limited, broad-code, and multistage sensitivities;
- inspect pre-treatment trajectory compatibility and one-event dominance.

Null or heterogeneous findings remain valid outcomes.
