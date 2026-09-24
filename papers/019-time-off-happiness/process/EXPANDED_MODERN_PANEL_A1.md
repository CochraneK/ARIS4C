# ARIS4C019 · Expanded modern panel A1 macro-control results

**Date:** 2026-09-24  
**WDI source snapshot:** World Development Indicators mirror, last updated **2026-04-08**.  
**Controls:** WHR log GDP per capita + WDI unemployment (modeled ILO estimate) + WDI CPI inflation.  
**Inference:** country-clustered standard errors.  
**Interpretation:** association models, not causal estimates.

## Complete-case samples

- leave A1: **1885 country-years / 157 countries**
- hours A1: **2000 / 129**
- joint A1: **1629 / 126**

## Exposure coefficients

- leave / TWFE_A1 / leave_per_5_days: beta=0.0455, SE=0.0581, 95% CI [-0.0685, 0.1594], N=1885, countries=157
- leave / FD_A1 / delta_leave_per_5_days: beta=-0.0809, SE=0.0527, 95% CI [-0.1842, 0.0224], N=1588, countries=151
- hours / TWFE_A1 / hours_per_100: beta=0.0130, SE=0.0260, 95% CI [-0.0380, 0.0639], N=2000, countries=129
- hours / FD_A1 / delta_hours_per_100: beta=0.0513, SE=0.0345, 95% CI [-0.0162, 0.1189], N=1733, countries=127
- joint / TWFE_A1 / hours_per_100: beta=0.0147, SE=0.0306, 95% CI [-0.0452, 0.0746], N=1629, countries=126
- joint / TWFE_A1 / leave_per_5_days: beta=0.0591, SE=0.0551, 95% CI [-0.0490, 0.1672], N=1629, countries=126
- joint / FD_A1 / delta_hours_per_100: beta=0.0359, SE=0.0343, 95% CI [-0.0313, 0.1030], N=1387, countries=124
- joint / FD_A1 / delta_leave_per_5_days: beta=-0.0727, SE=0.0629, 95% CI [-0.1959, 0.0504], N=1387, countries=124
- leave_infl_abs_le100 / TWFE_A1 / leave_per_5_days: beta=0.0468, SE=0.0561, 95% CI [-0.0631, 0.1567], N=1879, countries=157
- hours_infl_abs_le100 / TWFE_A1 / hours_per_100: beta=0.0110, SE=0.0263, 95% CI [-0.0406, 0.0625], N=1993, countries=129
- joint_infl_abs_le100 / TWFE_A1 / hours_per_100: beta=0.0117, SE=0.0298, 95% CI [-0.0467, 0.0701], N=1627, countries=126
- joint_infl_abs_le100 / TWFE_A1 / leave_per_5_days: beta=0.0590, SE=0.0534, 95% CI [-0.0456, 0.1636], N=1627, countries=126

## Reading rule

The macro-adjusted coefficients should be compared with A0, not promoted automatically because controls were added. Contemporaneous macro controls can themselves be affected by broader labour reforms and are used here only in the descriptive/association layer.

An explicit `|inflation| <= 100%` sensitivity is reported because extreme crisis inflation can produce high leverage. The primary A1 does **not** silently winsorize or delete those observations.
