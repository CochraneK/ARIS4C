# ARIS4C019 · Expanded statistical analysis freeze v1.0

**Freeze date:** 2026-09-24  
**Status:** frozen before opening new expanded-panel happiness effects

This plan supersedes the former practice of treating a small event set as the whole analysis. It preserves the original Pilot-0 event study as one causal module.

## Analysis populations

### P-A · historical descriptive universe
All source-valid legal/working-time observations and all source-valid well-being observations. No requirement that every country-year be complete.

### P-B · instrument-specific linked panels
Separate panels for:
- WDH comparable-question subsets;
- Cantril historical surveys;
- Eurobarometer life satisfaction;
- WVS / EVS;
- Gallup / WHR.

Do not pool raw scores across instruments before bridge diagnostics.

### P-C · modern WB × WHR panel
Current availability gate: 161 countries / 1,934 linked country-years in the 2004–2020 WB exposure window.

### P-D · verified causal reform events
Only exact-date, legally verified treatment changes that pass isolation/support gates. Database jumps alone are not treatments.

## S0 · Descriptive statistics

Report by decade / region / source:
- N countries and N country-years/waves;
- mean, SD, median, IQR, P10/P90;
- minimum/maximum with explicit extreme-cell audit;
- fraction at zero statutory entitlement;
- within-country SD and between-country SD;
- number / size / direction of observed changes;
- exposure transition matrices;
- source missingness heatmaps;
- country coverage and overlap heatmaps.

For happiness outcomes:
- preserve native scale first;
- report distributional statistics separately by instrument;
- where WDH dispersion is available, analyze both mean and SD/inequality descriptively.

## S1 · Long-run institutional diffusion

For first adoption / major upgrade of paid annual leave:
- Kaplan-Meier style diffusion curves (descriptive);
- Cox / discrete-time event-history models only where covariates have coherent historical timing;
- region × decade adoption matrices;
- competing coding for first national law vs ILO ratification;
- never equate ratification with national implementation.

## S2 · Modern association panel

Headline association model:

`Y_it = beta L_it + alpha_i + gamma_t + epsilon_it`

where:
- Y = instrument-specific life evaluation;
- L = statutory annual leave entitlement;
- alpha_i = country fixed effects;
- gamma_t = year fixed effects;
- inference clustered by country.

This coefficient is an **association**, not automatically causal.

Prespecified variants:
1. unweighted country estimand;
2. population-weighted sensitivity;
3. country linear trends;
4. first-difference model;
5. within-between / Mundlak decomposition;
6. balanced-support subset (>=10 linked years);
7. high-support subset (>=15 linked years).

## S3 · Nonlinearity

No outcome-driven knot selection.

Primary nonlinear representation:
- restricted cubic spline using exposure-only distribution knots at approximately P10 / P50 / P90 = **12 / 20 / 26 days**.

Sensitivity:
- categorical bands: 0; 1-9; 10-14; 15-19; 20-24; 25-29; >=30 days.
- exclude/flag source-extreme cells without silently recoding them.

## S4 · Lag / adaptation structure

Prespecified annual exposure lags:
- contemporaneous L(t)
- L(t-1)
- L(t-2)
- L(t-3)

Because statutory leave often changes slowly, distributed-lag estimates are reported jointly and with cumulative contrasts. No post-hoc lag chosen because it gives the largest effect.

## S5 · Covariate hierarchy

Association models report sequential specifications:
- A0: country + year FE only;
- A1: + log GDP per capita, unemployment, inflation;
- A2: + labor-force participation / employment composition where coverage permits;
- A3: + social expenditure / welfare-regime proxies where coherent.

For causal reform models, contemporaneous post-treatment covariates are not mechanically included; pre-treatment design and shock controls follow the causal protocol.

## S6 · Instrument bridging

For Eurobarometer / WVS-EVS / WDH / Gallup overlap:
1. estimate within-instrument effects first;
2. preserve native question wording and response scale;
3. produce country-time overlap matrix;
4. compare standardized within-instrument coefficients;
5. estimate multilevel/random-effects synthesis of coefficients, not naive pooled raw scores;
6. leave-one-instrument-out analysis;
7. report heterogeneity tau² / I² where meta-analytic synthesis is appropriate.

## S7 · Verified reform causal layer

Estimator hierarchy:
1. transparent event-specific before/after + donor diagnostics;
2. stacked event study;
3. Callaway-Sant'Anna group-time ATT;
4. Sun-Abraham interaction-weighted event study;
5. synthetic control / synthetic DiD for suitable large reforms;
6. matrix-completion sensitivity when support is adequate.

Mandatory:
- treatment isolation;
- exact effective date;
- partial-exposure transition-year handling;
- >=2 pre and >=2 post observations for minimal event eligibility;
- pretrend / placebo diagnostics;
- contamination screen;
- crisis/concurrent-policy audit;
- leave-one-event-out.

Conventional TWFE is never the sole causal headline under heterogeneous staggered treatment.

## S8 · Event-effect meta-analysis

For event estimates sharing a sufficiently comparable estimand:
- random-effects meta-analysis;
- prediction interval;
- influence / Baujat-style diagnostics;
- leave-one-event-out;
- meta-regression only when event count supports it.

Candidate moderators are frozen before expanded result inspection:
- reform magnitude;
- baseline leave;
- baseline actual hours;
- GDP/income level;
- region;
- informality;
- labor-force participation;
- gender employment composition;
- collective-bargaining / union proxy;
- welfare/social expenditure;
- crisis/conflict overlap.

## S9 · Robustness / falsification

- placebo reform years;
- negative-control timing where possible;
- alternative legal exposure definition (1y / 5y / 10y tenure vs average);
- source-version sensitivity;
- exclude coding-extreme cells;
- exclude broad bundled reforms;
- exclude crisis years;
- leave-one-country / region / instrument / event out;
- randomization/permutation inference for small event sets where defensible;
- multiple-testing control for prespecified secondary families.

## Reporting rule

The project will report:
- scale and coverage first;
- descriptive history second;
- association estimates third;
- causal estimates only where identification gates pass.

A large N does not upgrade an association into a causal result, and a small clean event set does not define the entire historical project.
