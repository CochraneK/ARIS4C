# Time-to-Retraction Specification · v1

## Estimand

Estimate the distribution and covariate structure of **time from original publication to formal retraction**, using the eligible publication universe rather than only eventually retracted works.

The current 490-day median is descriptive **conditional on eventual recorded retraction** and is not a population survival estimate.

## Cohort construction

For each eligible OpenAlex work:
- time origin: original publication date;
- event = 1 if the work maps to a primary RWDB Retraction event;
- event date = earliest valid RetractionDate linked to the work;
- event = 0 otherwise;
- administrative censoring date = frozen RWDB snapshot date / analysis cutoff.

Works with event date before publication date fail identity/date QA rather than being coerced.

## Primary time scale

Days since publication.

Calendar year and publication cohort are modeled separately because detection/editorial practices change over historical time.

## Descriptive survival outputs

- Kaplan–Meier-style retraction-free survival;
- cumulative incidence of recorded retraction at 1, 2, 3, 5 and 10 years;
- cohort-stratified curves;
- field-stratified curves only after denominator/match coverage passes.

Because retraction is rare, plots also report cumulative events per 10,000 works to avoid visually flat survival curves.

## Regression strategy

Model family is chosen after diagnostics, not pre-selected for convenience.

Candidate primary models:
1. piecewise-exponential / discrete-time hazard with publication-age intervals;
2. Cox proportional-hazards model if proportionality diagnostics are acceptable;
3. flexible parametric survival as sensitivity when baseline hazard shape is complex.

Calendar period can enter as time-varying or stratification structure where justified.

## Right censoring

Recent cohorts have shorter observation windows. A 2025 publication cannot be compared naively with a 2010 publication on eventual retraction probability.

Headline cross-field/country comparisons must either:
- use a common fixed follow-up horizon;
- restrict to sufficiently mature cohorts; or
- use the full survival model with explicit censoring.

## Ascertainment era

RWDB historical capture and modern detection practices are not assumed stable over centuries.

Before confirmatory modeling:
- plot event and publication coverage by calendar year;
- identify a defensible modern ascertainment window;
- run at least one broader-window sensitivity analysis.

The confirmatory lower-year cutoff is not chosen from outcome-favorable results.

## EOC / Correction

Expressions of concern and corrections are not population-complete in RWDB and do not enter the primary event definition.

Where available, EOC may be explored as a precursor/time-varying process in a secondary pathway analysis. It is not treated as a competing event that prevents later retraction.

## Covariates

Candidate covariates after data-quality gates:
- OpenAlex field / topic;
- publication year / calendar period;
- work type;
- OA status;
- collaboration/country structure;
- journal/source;
- publisher hierarchy;
- citation exposure only when temporally defined to avoid post-event leakage.

No author/institution risk coefficient is interpreted before entity-resolution and denominator gates.

## Falsification / robustness

- fixed 3-year and 5-year follow-up cohorts;
- exclusion of mass-retraction clusters;
- DOI-linked only vs broader identity tiers;
- alternate field mappings;
- publication-date precision sensitivity;
- publisher/journal random or fixed effects as appropriate;
- proportional-hazards diagnostics where Cox models are used.
