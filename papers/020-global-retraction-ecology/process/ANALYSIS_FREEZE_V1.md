# Confirmatory / Exploratory Analysis Freeze · v1

ARIS4C-020 has already observed aggregate RWDB descriptive counts. To avoid converting observed patterns into post-hoc “hypotheses,” this document separates analyses whose direction is **not** pre-specified from tests with falsifiable structural expectations.

## Confirmatory structural checks

### C1 · Denominator necessity
Raw retraction count rankings and publication-normalized incidence rankings are not assumed equivalent.

**Test:** rank correlation and rank changes for field/country/publisher after denominator construction.

**Falsifier:** normalized ordering is effectively identical to raw-count ordering across all major strata.

This is a measurement/interpretation test, not a moral ranking.

### C2 · Mass-event sensitivity
Comparative temporal/entity estimates should be reported with concentrated cleanup events isolated.

**Test:** compare effect estimates under all-data vs pre-frozen cluster exclusions.

**No directional hypothesis:** ARIS4C-020 does not pre-assert that the 2023 spike or any country/publisher effect disappears.

### C3 · Multi-label information loss
Collapsing each Retraction to a single Reason discards native RWDB information.

**Test:** quantify number of labels per work, pairwise co-occurrence, and changes in higher-order summaries under single-label reductions.

**Falsifier:** multi-label structure contributes negligible additional information after work-level deduplication.

### C4 · Cross-database discordance
OpenAlex retraction metadata is treated as a fallible concordance source.

**Test:** among DOI-matched RWDB primary works, quantify OpenAlex false-negative concordance; separately audit OpenAlex multi-candidate/type anomalies.

**No assumption** that discordance favors either database globally.

### C5 · Right-censoring
Recent publication cohorts have less opportunity for formal retraction.

**Test:** compare naive cohort rates with fixed-follow-up / survival-based estimates.

**Falsifier:** censoring-aware estimates are practically indistinguishable across the eligible modern window.

## Confirmatory time-to-event outputs

Pre-freeze before model execution:
- cumulative recorded-retraction incidence at 1, 2, 3, 5 and 10 years;
- primary modern ascertainment window selected from source-coverage diagnostics, not outcome-favorable coefficients;
- mass-event exclusion sensitivities;
- field-level estimates only above a minimum exposure/event threshold.

No country/publisher coefficient is interpreted as misconduct propensity.

## Exploratory analyses

- full observed Reason co-occurrence network;
- six-facet Reason ecology;
- paper-mill / generated-content sub-ecologies;
- journal/source and publisher hierarchy patterns;
- repeated author/institution clusters after identity QA;
- citation-afterlife heterogeneity by field/reason/event cluster;
- citation-context analysis where text/context coverage permits.

Exploratory findings must be labeled as such and should generate future confirmatory studies rather than be back-written as preregistered predictions.

## Locked interpretation constraints

- Retraction ≠ misconduct.
- Affiliation ≠ responsibility.
- Recorded retraction incidence = editorial/database event incidence, not latent misconduct prevalence.
- Citation ≠ endorsement.
- OpenAlex `is_retracted` ≠ ground truth.
- Absence from RWDB ≠ proof a work was never retracted, especially for stealth/unannounced events.
