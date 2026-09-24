# ARIS4C019 · Expanded modern panel first statistics v1.1

**Corrected:** 2026-09-24 after auditing the hours-country join.  
**Join fix:** `Taiwan` (working-hours source) → `Taiwan Province of China` (WHR2024).  
**Interpretation:** descriptive association layer; not causal.

## Corrected sample sizes
- actual working hours × Life Ladder: **2015 country-years / 130 countries**
- statutory leave × Life Ladder: **1934 / 161**
- joint overlap: **1663 / 129**

## Key exposure coefficients
- TWFE_A0 / hours / hours_per_100: beta=0.0350, SE=0.0296, 95% CI [-0.0230, 0.0929], N=2015, countries=130
- WITHIN_BETWEEN_YEARFE / hours / hours_per_100_within: beta=0.0422, SE=0.0314, 95% CI [-0.0193, 0.1037], N=2015, countries=130
- WITHIN_BETWEEN_YEARFE / hours / hours_per_100_between: beta=-0.1411, SE=0.0301, 95% CI [-0.2002, -0.0821], N=2015, countries=130
- FD_YEARFE / hours / delta_hours_per_100: beta=0.0615, SE=0.0350, 95% CI [-0.0070, 0.1301], N=1744, countries=128
- TWFE_LAG1 / hours / hours_per_100_lag1: beta=0.0233, SE=0.0284, 95% CI [-0.0324, 0.0790], N=1744, countries=128
- TWFE_LAG2 / hours / hours_per_100_lag2: beta=0.0278, SE=0.0286, 95% CI [-0.0283, 0.0839], N=1670, countries=129
- TWFE_LAG3 / hours / hours_per_100_lag3: beta=0.0219, SE=0.0265, 95% CI [-0.0300, 0.0738], N=1564, countries=129
- TWFE_A0 / leave / leave_per_5_days: beta=0.0420, SE=0.0605, 95% CI [-0.0766, 0.1606], N=1934, countries=161
- WITHIN_BETWEEN_YEARFE / leave / leave_per_5_days_within: beta=0.0417, SE=0.0605, 95% CI [-0.0768, 0.1602], N=1934, countries=161
- WITHIN_BETWEEN_YEARFE / leave / leave_per_5_days_between: beta=-0.0390, SE=0.0686, 95% CI [-0.1733, 0.0954], N=1934, countries=161
- FD_YEARFE / leave / delta_leave_per_5_days: beta=-0.0941, SE=0.0400, 95% CI [-0.1724, -0.0158], N=1628, countries=155
- TWFE_LAG1 / leave / leave_per_5_days_lag1: beta=0.0623, SE=0.0463, 95% CI [-0.0283, 0.1530], N=1628, countries=155
- TWFE_LAG2 / leave / leave_per_5_days_lag2: beta=0.1020, SE=0.0492, 95% CI [0.0055, 0.1985], N=1540, countries=154
- TWFE_LAG3 / leave / leave_per_5_days_lag3: beta=0.1107, SE=0.0500, 95% CI [0.0127, 0.2087], N=1409, countries=152
- TWFE_JOINT / joint / hours_per_100: beta=0.0625, SE=0.0347, 95% CI [-0.0055, 0.1305], N=1663, countries=129
- TWFE_JOINT / joint / leave_per_5_days: beta=0.0380, SE=0.0590, 95% CI [-0.0776, 0.1537], N=1663, countries=129
- FD_JOINT / joint / delta_hours_per_100: beta=0.0622, SE=0.0367, 95% CI [-0.0097, 0.1341], N=1412, countries=127
- FD_JOINT / joint / delta_leave_per_5_days: beta=-0.1111, SE=0.0462, 95% CI [-0.2015, -0.0206], N=1412, countries=127

The earlier 129-country hours outputs are superseded. No scientific claim should cite them.
