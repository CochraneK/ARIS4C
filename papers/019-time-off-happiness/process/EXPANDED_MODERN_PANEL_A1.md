# ARIS4C019 · Expanded modern panel A1 macro-control results v1.1

**Corrected:** 2026-09-24 after Taiwan join repair.  
**Controls:** WHR log GDP per capita + WDI unemployment + WDI CPI inflation.  
**Inference:** country-clustered SE. Association models only.

## Complete-case samples
- hours: **2000 / 129 countries**
- leave: **1885 / 157**
- joint: **1629 / 126**

## Key exposure coefficients
- TWFE_A1 / hours / hours_per_100: beta=0.0130, SE=0.0260, 95% CI [-0.0380, 0.0639], N=2000, countries=129
- FD_A1 / hours / delta_hours_per_100: beta=0.0513, SE=0.0345, 95% CI [-0.0162, 0.1189], N=1733, countries=127
- TWFE_A1 / leave / leave_per_5_days: beta=0.0455, SE=0.0581, 95% CI [-0.0685, 0.1594], N=1885, countries=157
- FD_A1 / leave / delta_leave_per_5_days: beta=-0.0809, SE=0.0527, 95% CI [-0.1842, 0.0224], N=1588, countries=151
- TWFE_A1 / joint / hours_per_100: beta=0.0147, SE=0.0306, 95% CI [-0.0452, 0.0746], N=1629, countries=126
- TWFE_A1 / joint / leave_per_5_days: beta=0.0591, SE=0.0551, 95% CI [-0.0490, 0.1672], N=1629, countries=126
- FD_A1 / joint / delta_hours_per_100: beta=0.0359, SE=0.0343, 95% CI [-0.0313, 0.1030], N=1387, countries=124
- FD_A1 / joint / delta_leave_per_5_days: beta=-0.0727, SE=0.0629, 95% CI [-0.1959, 0.0504], N=1387, countries=124
