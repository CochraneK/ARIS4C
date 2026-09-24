# ARIS4C019 · Country-trend and nonlinear sensitivity v1.1

**Corrected:** 2026-09-24 after Taiwan working-hours join repair.

## Country-specific linear trend sensitivity

- leave / COUNTRY_TREND_A0 / leave_per_day: beta=-0.02025, SE=0.00616, CI [-0.03233, -0.00817], N=1934, countries=161
- leave / COUNTRY_TREND_A1 / leave_per_day: beta=-0.01036, SE=0.00642, CI [-0.02295, 0.00223], N=1885, countries=157
- hours / COUNTRY_TREND_A0 / hours_per_100: beta=0.05706, SE=0.02811, CI [0.00197, 0.11214], N=2015, countries=130
- hours / COUNTRY_TREND_A1 / hours_per_100: beta=0.02994, SE=0.02542, CI [-0.01988, 0.07976], N=2000, countries=129

The A0 hours model now includes Taiwan; the earlier 2000/129 A0 line is superseded. A1 remains 2000/129 because macro complete-case coverage removes one country, not because of the Taiwan join.

Country-specific linear trends absorb slow-moving national trajectories. The macro-adjusted A1 versions again cross zero for both leave and working hours, so these demanding trend specifications do not establish a stable directional association.

## Frozen restricted cubic spline

The pre-written exposure-only knots remain **12, 20 and 26 statutory leave days**. The RCS results are leave-only and are unaffected by the Taiwan working-hours fix.

- RCS A0 nonlinear term: beta=0.00116, SE=0.02672, CI [-0.05121, 0.05353]
- RCS A1 nonlinear term: beta=0.00655, SE=0.02433, CI [-0.04113, 0.05422]

Machine-readable contrasts relative to 20 leave days remain in `data/expanded_leave_rcs_contrasts.csv`.
