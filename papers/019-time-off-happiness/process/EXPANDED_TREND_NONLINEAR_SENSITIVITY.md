# ARIS4C019 · Country-trend and nonlinear sensitivity

**Date:** 2026-09-24

## Country-specific linear trend sensitivity

- leave / COUNTRY_TREND_A0 / leave_per_day: beta=-0.02117, SE=0.00618, CI [-0.03329, -0.00905], N=1885, countries=157
- leave / COUNTRY_TREND_A1 / leave_per_day: beta=-0.01036, SE=0.00642, CI [-0.02295, 0.00223], N=1885, countries=157
- hours / COUNTRY_TREND_A0 / hours_per_100: beta=0.05689, SE=0.02812, CI [0.00178, 0.11200], N=2000, countries=129
- hours / COUNTRY_TREND_A1 / hours_per_100: beta=0.02994, SE=0.02542, CI [-0.01988, 0.07976], N=2000, countries=129

Country-specific linear trends absorb slow-moving national trajectories that could otherwise correlate with gradual work-time or leave changes. Because statutory leave changes sparsely, this is intentionally a demanding sensitivity and can be noisy.

## Frozen restricted cubic spline

The pre-written exposure-only knots are **12, 20 and 26 statutory leave days**. With three knots, the restricted cubic spline has a linear term plus one nonlinear basis term.

Nonlinearity terms:
- RCS_A0_KNOTS_12_20_26: beta=0.00116, SE=0.02672, CI [-0.05121, 0.05353]
- RCS_A1_KNOTS_12_20_26: beta=0.00655, SE=0.02433, CI [-0.04113, 0.05422]

Machine-readable contrasts relative to **20 leave days** are stored in `data/expanded_leave_rcs_contrasts.csv`. These are association contrasts within the FE specification, not causal dose-response effects.
