# ARIS4C019 · Historical happiness-trend × working-hours-trend bridge

**Date:** 2026-09-24  
**Design:** exploratory ecological trend-to-trend association, not causal.

For each published WDH happiness trend row, annual working hours are restricted to the **same calendar window** before an OLS hours slope is estimated. A row is analysis-eligible only with >=10 working-hours observations spanning >=10 years.

## Coverage

- published WDH rows: **95**
- exact-window rows with usable hours trend: **94**
- represented countries: **27**
- deterministic one-row-per-country longest-series set: **27**

## Association summaries

| analysis | N | countries | Pearson r | Spearman rho | mean hours slope (h/year) | mean happiness slope (0–10/year) |
|---|---:|---:|---:|---:|---:|---:|
| all_series_nonindependent | 94 | 27 | -0.229 | -0.058 | -5.83 | 0.0053 |
| one_longest_series_per_country | 27 | 27 | -0.458 | -0.222 | -6.51 | 0.0070 |
| family_happiness | 18 | 8 | -0.436 | 0.181 | -5.44 | 0.0012 |
| family_life_satisfaction | 57 | 19 | -0.016 | -0.028 | -6.20 | 0.0045 |
| family_best_worst_life | 19 | 13 | -0.467 | -0.133 | -5.13 | 0.0117 |

## Non-independence guardrail

The full-series correlation is descriptive only because WDH publishes multiple instruments and nested start-windows for some countries. The one-row-per-country check uses a frozen deterministic rule: **earliest start year → longest span → lexical measure code**. It is not selected on coefficient sign.

Even the one-row-per-country result remains an ecological correlation between two long-run trends. It does not isolate annual leave, does not establish direction of causation, and can reflect modernization, productivity, income, labor-force composition, survey-instrument differences and other secular changes.

Machine-readable inputs/outputs:
- `data/wdh_hours_window_matched_trends.csv`
- `data/wdh_hours_longest_series_per_country.csv`
- `data/wdh_hours_trend_association_summary.csv`
