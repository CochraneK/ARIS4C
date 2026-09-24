# ARIS4C019 · A0→A1 sample-composition decomposition

**Date:** 2026-09-24  
**Purpose:** separate coefficient movement caused by complete-case sample restriction from movement caused by adding macro controls.

For each exposure:
- **A0 full:** exposure + country FE + year FE on all available rows;
- **A0 on A1 sample:** same model, but restricted to rows with complete GDP/unemployment/inflation;
- **A1:** same complete-case sample plus the three macro controls.

## Key coefficients
- hours / TWFE_A0_FULL / hours_per_100: beta=0.0350, SE=0.0296, CI [-0.0230, 0.0929], N=2015, countries=130
- hours / TWFE_A0_A1SAMPLE / hours_per_100: beta=0.0349, SE=0.0295, CI [-0.0230, 0.0928], N=2000, countries=129
- hours / TWFE_A1 / hours_per_100: beta=0.0130, SE=0.0260, CI [-0.0380, 0.0639], N=2000, countries=129
- hours / FD_A0_FULL / delta_hours_per_100: beta=0.0615, SE=0.0350, CI [-0.0070, 0.1301], N=1744, countries=128
- hours / FD_A0_A1SAMPLE / delta_hours_per_100: beta=0.0608, SE=0.0350, CI [-0.0077, 0.1294], N=1733, countries=127
- hours / FD_A1 / delta_hours_per_100: beta=0.0513, SE=0.0345, CI [-0.0162, 0.1189], N=1733, countries=127
- leave / TWFE_A0_FULL / leave_per_5_days: beta=0.0420, SE=0.0605, CI [-0.0766, 0.1606], N=1934, countries=161
- leave / TWFE_A0_A1SAMPLE / leave_per_5_days: beta=0.0273, SE=0.0619, CI [-0.0940, 0.1486], N=1885, countries=157
- leave / TWFE_A1 / leave_per_5_days: beta=0.0455, SE=0.0581, CI [-0.0685, 0.1594], N=1885, countries=157
- leave / FD_A0_FULL / delta_leave_per_5_days: beta=-0.0941, SE=0.0400, CI [-0.1724, -0.0158], N=1628, countries=155
- leave / FD_A0_A1SAMPLE / delta_leave_per_5_days: beta=-0.1179, SE=0.0373, CI [-0.1911, -0.0448], N=1588, countries=151
- leave / FD_A1 / delta_leave_per_5_days: beta=-0.0809, SE=0.0527, CI [-0.1842, 0.0224], N=1588, countries=151
- joint / TWFE_A0_FULL / hours_per_100: beta=0.0625, SE=0.0347, CI [-0.0055, 0.1305], N=1663, countries=129
- joint / TWFE_A0_FULL / leave_per_5_days: beta=0.0380, SE=0.0590, CI [-0.0776, 0.1537], N=1663, countries=129
- joint / TWFE_A0_A1SAMPLE / hours_per_100: beta=0.0623, SE=0.0345, CI [-0.0053, 0.1300], N=1629, countries=126
- joint / TWFE_A0_A1SAMPLE / leave_per_5_days: beta=0.0397, SE=0.0592, CI [-0.0762, 0.1557], N=1629, countries=126
- joint / TWFE_A1 / hours_per_100: beta=0.0147, SE=0.0306, CI [-0.0452, 0.0746], N=1629, countries=126
- joint / TWFE_A1 / leave_per_5_days: beta=0.0591, SE=0.0551, CI [-0.0490, 0.1672], N=1629, countries=126
- joint / FD_A0_FULL / delta_hours_per_100: beta=0.0622, SE=0.0367, CI [-0.0097, 0.1341], N=1412, countries=127
- joint / FD_A0_FULL / delta_leave_per_5_days: beta=-0.1111, SE=0.0462, CI [-0.2015, -0.0206], N=1412, countries=127
- joint / FD_A0_A1SAMPLE / delta_hours_per_100: beta=0.0618, SE=0.0367, CI [-0.0101, 0.1336], N=1387, countries=124
- joint / FD_A0_A1SAMPLE / delta_leave_per_5_days: beta=-0.1111, SE=0.0460, CI [-0.2013, -0.0209], N=1387, countries=124
- joint / FD_A1 / delta_hours_per_100: beta=0.0359, SE=0.0343, CI [-0.0313, 0.1030], N=1387, countries=124
- joint / FD_A1 / delta_leave_per_5_days: beta=-0.0727, SE=0.0629, CI [-0.1959, 0.0504], N=1387, countries=124

This file is the canonical decomposition for deciding whether A0→A1 movement is a sample-composition artifact or a control-adjustment effect.
