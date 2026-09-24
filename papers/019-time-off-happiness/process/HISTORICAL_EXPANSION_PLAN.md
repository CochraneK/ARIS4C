# ARIS4C019 · Historical expansion plan v1.0

## Why the scope is reopened

The completed leave-specific Pilot-0 is scientifically useful but too narrow to answer the original project question: how time off changed across countries over the long run and how those changes relate to subjective well-being.

Pilot-0 therefore remains frozen as a causal-identification module rather than the whole project. The expanded ARIS4C019 becomes a multi-resolution historical study with three linked but non-interchangeable layers:

1. **global institutional history** of paid annual leave / weekly rest / public holidays / working time;
2. **long-run comparative well-being panels** using multiple survey families;
3. **clean policy-reform causal studies** where exact legal timing and donor support allow.

The project must not force sparse early history into a fake annual balanced panel. Resolution changes by period and source.

## Expanded temporal frame

### Era H0 · pre-standardization / institutional origins (c. 1900–1935)

Goal: document major national adoption milestones and pre-ILO antecedents where primary legal sources are recoverable.

- No claim of globally comparable annual happiness coverage.
- Treat this as legal/institutional history, not a causal happiness panel.
- Selected historical working-time series may extend earlier than 1900 where established datasets permit.

### Era H1 · international standardization and early survey era (1936–1972)

Core exposure anchors:
- ILO Holidays with Pay Convention, 1936 (C052);
- ratification / denunciation dates;
- national implementing laws and entitlement levels where primary legal evidence can be reconstructed;
- ILO Holidays with Pay Convention (Revised), 1970 (C132);
- historical actual working-time series.

Well-being:
- World Database of Happiness historical surveys from 1945 onward;
- Cantril Pattern of Human Concerns 1957–1963 for the available countries;
- other clearly documented national/general-population survey series.

### Era H2 · European repeated life-satisfaction era (1973–1980)

- Eurobarometer life-satisfaction series beginning in 1973.
- Continue legal leave / working-time reconstruction.
- Do not extrapolate European estimates globally.

### Era H3 · global values-survey era (1981–2004)

- World Values Survey / European Values Study life satisfaction and happiness;
- retain exact survey wave/year and question wording;
- expand country coverage and repeated cross-sections;
- combine only after explicit measurement bridging.

### Era H4 · Gallup annual era (2005–present)

- Gallup World Poll / World Happiness Report annual Life Ladder where genuine annual country-year data are available;
- modern WORLD / Equal Futures legal snapshots;
- World Bank historical screening fields;
- clean exact-date legal reforms;
- current Pilot-0 and future Mexico-style prospective holdouts.

## Exposure system

Keep five exposure families separate and analyze them jointly only in explicitly defined models:

| code | exposure | role |
|---|---|---|
| E1 | statutory paid annual leave entitlement | core legal exposure |
| E2 | statutory weekly rest / standard workweek | complementary legal exposure |
| E3 | statutory public holidays | distinct calendar exposure |
| E4 | actual annual / weekly hours worked | realized work-time exposure |
| E5 | actual leave utilization / vacation taken | realized leave exposure |

Create derived measures only after the raw components are preserved:
- minimum guaranteed annual paid days;
- total statutory non-work days where defensible;
- annual work-time burden;
- change in entitlement;
- change in realized hours;
- policy-package flags;
- coverage / eligibility / tenure conditions.

## Outcome system

Never treat all happiness questions as identical.

| family | approximate era | primary use |
|---|---|---|
| World Database of Happiness | 1945 onward | historical descriptive / comparable-question subsets |
| Cantril historical surveys | 1957–1963 | early cross-national bridge |
| Eurobarometer | 1973 onward | European repeated life satisfaction |
| WVS / EVS | 1981 onward | multi-country wave panel |
| Gallup / WHR | 2005 onward | annual global Life Ladder |

Primary rule:
- estimate within instrument first;
- preserve wording/scale/sample metadata;
- build overlap-country bridge diagnostics;
- use harmonized z/0–10 transformations only as sensitivity, never as the sole headline series;
- pool instrument-specific estimates through hierarchical/meta-analytic synthesis rather than pretending the raw scores are one homogeneous scale.

## Target country universe

- Modern legal cross-section target: all **193 UN member states** where WORLD / Equal Futures coverage permits.
- Historical legal panel: expand as far as primary-source reconstruction allows; every country-year carries provenance and confidence.
- Historical well-being universe: all countries with valid observations in WDH / Cantril / Eurobarometer / WVS-EVS / Gallup.
- Causal event set: all legally verified reforms meeting design gates, not an arbitrary eight-event cap.

## Statistical analysis ladder

### S0 · descriptive historical atlas
- country-year / country-wave heatmaps;
- regional diffusion curves;
- distribution of legal leave days by decade;
- adoption / reform timelines;
- working-time trajectories;
- happiness trajectories with source identity visible;
- inequality/dispersion of happiness where available.

### S1 · policy diffusion / historical change
- event-history / survival models for first adoption and major upgrades;
- decade × region transition matrices;
- change-point detection for large entitlement / hours shifts;
- clustering of national time-off regimes.

### S2 · long-run association models
- country fixed effects + time fixed effects;
- within-between decomposition;
- country-specific or region-specific trends as robustness;
- clustered / Driscoll–Kraay style inference where appropriate;
- lagged exposure models;
- nonlinear dose-response / spline models;
- alternative weighting (country vs population).

These are association models unless identification assumptions justify more.

### S3 · multi-instrument well-being synthesis
- run instrument-specific models;
- estimate bridge consistency in overlapping countries/years;
- random-effects / multilevel meta-analysis of comparable coefficients;
- heterogeneity by survey family;
- leave-one-instrument-out sensitivity.

### S4 · modern causal policy-reform layer
- stacked event studies;
- Callaway–Sant'Anna style group-time ATT;
- Sun–Abraham style interaction-weighted event study where appropriate;
- synthetic control / synthetic DiD / matrix-completion sensitivity for large reforms;
- explicit anticipation, transition-year, pretrend and contamination rules;
- no conventional TWFE headline when staggered heterogeneous treatment invalidates interpretation.

### S5 · event-effect synthesis
- derive event-level treatment estimates under a common estimand where possible;
- random-effects meta-analysis;
- influence diagnostics;
- meta-regression by reform size, baseline entitlement, enforcement proxy, region, income, informality and labor-force exposure;
- publication-style forest plots rather than a single pooled mean.

### S6 · mechanism / heterogeneity
Prespecified candidate moderators:
- baseline leave entitlement;
- reform size;
- actual working hours;
- income level / GDP per capita;
- unemployment / inflation shocks;
- labor-force participation;
- informality;
- union / collective-bargaining environment when available;
- social expenditure / welfare regime;
- gender employment composition;
- crisis / conflict years.

## Missingness and comparability

The historical design is explicitly **multi-resolution**:
- early periods may be decade/event-level for laws and sparse-wave for happiness;
- later periods become country-wave;
- Gallup era becomes country-year.

Do not interpolate missing happiness years merely to create a visually complete panel.
Do not treat ILO ratification as identical to the first national entitlement law.
Do not infer leave taken from leave guaranteed.
Do not combine annual leave and public holidays without showing components.

## Deliverables

1. machine-readable country × year/time-source legal history table;
2. survey-source × country × year/wave happiness table;
3. historical source/provenance ledger;
4. 1900s/1936–2026 global time-off atlas;
5. 1945–present subjective-well-being atlas;
6. harmonization/bridge report;
7. descriptive and panel-statistics notebook;
8. expanded legally verified reform inventory;
9. modern causal event-study suite;
10. event-level meta-analysis / heterogeneity synthesis;
11. revised bilingual manuscript where Pilot-0 is one module, not the entire paper.

## Immediate execution order

1. freeze this expanded design before adding new effect estimates;
2. inventory historical source coverage by era;
3. ingest ILO C052/C132 ratification histories as **candidate institutional anchors**, not automatic treatments;
4. inventory WDH / Cantril / Eurobarometer / WVS-EVS / Gallup outcome coverage;
5. construct historical working-hours source map;
6. produce a no-effect-inspection coverage dashboard;
7. only then run the expanded statistical ladder.
