# ARIS4C019 · Full WDH Table-2 happiness × working-hours trend bridge

**Date:** 2026-09-24  
**Scope:** published WDH trend coefficients, 1946–2021, matched to actual-hours slopes in the same calendar windows.

## Coverage

- verbatim source rows: **200**
- exact unique rows used analytically: **199**
- unique rows with >=10 hours observations spanning >=10 years: **190**
- countries in matched analytical set: **46**
- one deterministic longest-series row per country: **46**

Rows failing the hours-window support gate: **9**.

## Association summaries

| analysis | N | countries | Pearson r | Spearman rho | mean hours slope (h/year) | mean happiness slope (0–10/year) |
|---|---:|---:|---:|---:|---:|---:|
| all_unique_series | 190 | 46 | 0.101 | 0.094 | -6.11 | 0.0068 |
| one_longest_series_per_country | 46 | 46 | -0.057 | -0.045 | -7.49 | 0.0093 |
| family_happiness | 25 | 10 | -0.225 | 0.110 | -5.11 | 0.0034 |
| family_life_satisfaction | 139 | 40 | 0.188 | 0.122 | -6.57 | 0.0065 |
| family_best_worst_life | 26 | 14 | -0.246 | 0.103 | -4.65 | 0.0117 |
| cohort_1940s | 3 | 2 | -1.000 | -1.000 | -9.50 | 0.0163 |
| cohort_1950s | 6 | 3 | -0.161 | -0.543 | -4.59 | 0.0033 |
| cohort_1960s | 11 | 9 | 0.085 | 0.082 | -5.42 | 0.0057 |
| cohort_1970s | 35 | 16 | -0.030 | -0.122 | -5.73 | 0.0050 |
| cohort_1980s | 39 | 18 | -0.254 | -0.032 | -5.96 | 0.0050 |
| cohort_1990s | 59 | 38 | 0.283 | 0.195 | -5.96 | 0.0064 |
| cohort_2000s | 37 | 37 | 0.241 | 0.202 | -7.07 | 0.0113 |

## Interpretation lock for this historical bridge

This is an **ecological trend-to-trend exploration**, not a causal annual-leave estimate.

The source contains multiple instruments and nested time windows per nation, so the full-series correlation is non-independent. The one-row-per-country version is a sensitivity, not a preferred causal model. Correlations may absorb productivity, income, labor-force composition, survey-instrument changes, post-socialist transitions, crises, welfare institutions and other secular changes.

Do not convert a negative Pearson coefficient into the claim “fewer hours cause greater happiness.” The discrepancy between Pearson and Spearman coefficients, measure-family results and decade-specific results is itself evidence that the relation is not a simple universal linear law.
