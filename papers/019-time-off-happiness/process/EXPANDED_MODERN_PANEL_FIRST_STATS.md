# ARIS4C019 · Expanded modern panel first statistics v1.0

**Analysis date:** 2026-09-24  
**Design status:** prespecified association layer; not causal.

## Data

### Actual working hours × Life Ladder
- 2015 country-years
- 130 countries
- 2005–2023
- exposure unit in models: +100 annual working hours

### Statutory leave × Life Ladder
- 1919 country-years
- 160 countries
- 2005–2020
- exposure unit in models: +5 statutory leave days

### Joint overlap
- 1648 country-years
- 128 countries
- 2005–2020

## Estimator

Two-way fixed effects models absorb country and year effects. Standard errors are clustered by country with a finite-sample cluster adjustment. First-difference models use exact consecutive-year pairs and year fixed effects. Within-between models separate within-country deviation from the country mean from between-country mean differences.

These estimates are **associations**. They do not convert the broad panel into a natural experiment.

## Main numerical results

- TWFE_A0 / hours_per_100: beta=0.0350, cluster SE=0.0296, 95% CI [-0.0230, 0.0929], N=2015, countries=130
- WITHIN_BETWEEN_YEARFE / hours_per_100_within: beta=0.0422, cluster SE=0.0314, 95% CI [-0.0193, 0.1037], N=2015, countries=130
- WITHIN_BETWEEN_YEARFE / hours_per_100_between: beta=-0.1411, cluster SE=0.0301, 95% CI [-0.2002, -0.0821], N=2015, countries=130
- FIRST_DIFF_YEARFE / delta_hours_per_100: beta=0.0615, cluster SE=0.0350, 95% CI [-0.0070, 0.1301], N=1744, countries=128
- TWFE_A0 / leave_per_5_days: beta=0.0417, cluster SE=0.0605, 95% CI [-0.0770, 0.1603], N=1919, countries=160
- WITHIN_BETWEEN_YEARFE / leave_per_5_days_within: beta=0.0415, cluster SE=0.0605, 95% CI [-0.0771, 0.1600], N=1919, countries=160
- WITHIN_BETWEEN_YEARFE / leave_per_5_days_between: beta=-0.0396, cluster SE=0.0685, 95% CI [-0.1738, 0.0946], N=1919, countries=160
- FIRST_DIFF_YEARFE / delta_leave_per_5_days: beta=-0.0941, cluster SE=0.0399, 95% CI [-0.1723, -0.0160], N=1615, countries=154
- TWFE_SUPPORT_GE10 / leave_per_5_days: beta=0.0720, cluster SE=0.0558, 95% CI [-0.0373, 0.1814], N=1734, countries=126
- TWFE_SUPPORT_GE15 / leave_per_5_days: beta=-0.0646, cluster SE=0.2281, 95% CI [-0.5117, 0.3825], N=840, countries=56
- TWFE_EXCLUDE_LEAVE_GT40 / leave_per_5_days: beta=0.0417, cluster SE=0.0605, 95% CI [-0.0769, 0.1603], N=1916, countries=159
- TWFE_JOINT / hours_per_100: beta=0.0617, cluster SE=0.0350, 95% CI [-0.0070, 0.1304], N=1648, countries=128
- TWFE_JOINT / leave_per_5_days: beta=0.0377, cluster SE=0.0590, 95% CI [-0.0779, 0.1534], N=1648, countries=128
- FIRST_DIFF_JOINT / delta_hours_per_100: beta=0.0610, cluster SE=0.0367, 95% CI [-0.0110, 0.1330], N=1399, countries=126
- FIRST_DIFF_JOINT / delta_leave_per_5_days: beta=-0.1112, cluster SE=0.0461, 95% CI [-0.2016, -0.0209], N=1399, countries=126

## Interpretation rule

- Working-hours coefficients are Life Ladder points per +100 annual work hours.
- Leave coefficients are Life Ladder points per +5 statutory leave days.
- A negative hours coefficient means higher annual work time is associated with lower life evaluation within the specified model.
- A positive leave coefficient means higher statutory entitlement is associated with higher life evaluation within the specified model.
- The joint model asks whether each exposure retains a within-country association when both are included; it remains non-causal.

## Lag models

All prespecified lag 0–3 estimates are stored machine-readably in `data/expanded_modern_panel_first_statistics.csv`. No lag is selected post hoc as the preferred result.

## Source caution

Working-hours transport currently uses a public GitHub mirror whose 1870–2023 structure matches the current OWID indicator description. It is a transport fallback, not a replacement for an official OWID re-download. Statutory leave uses the repository's frozen World Bank Employing Workers panel. WHR2024 annual Life Ladder uses the already validated annual source mirror.

