# ARIS4C019 · Legal-time aligned panel falsification

**Date:** 2026-09-24  
**Purpose:** test whether the negative WB-year first-difference coefficient survives when verified leave steps are moved to legal time.

The sample retains never-changing countries and only the already verified changer events. Two deterministic exposure clocks are compared:

1. **legal effective year:** new leave level begins in the legal effective calendar year;
2. **first full year:** if the law starts after January 1, the new level begins in T+1.

Both use the verified pre/post leave levels already stored in `reform_panel_validation.csv`.

## Exposure coefficients

- legal_effective_year / TWFE_A1: beta=0.1582, SE=0.1015, CI [-0.0406, 0.3571], N=1665, countries=139
- legal_effective_year / FD_A1: beta=0.0925, SE=0.0208, CI [0.0518, 0.1332], N=1399, countries=133
- full_year / TWFE_A1: beta=0.1863, SE=0.1650, CI [-0.1370, 0.5097], N=1665, countries=139
- full_year / FD_A1: beta=0.2464, SE=0.2725, CI [-0.2878, 0.7805], N=1399, countries=133

## Interpretation boundary

This is a falsification/sensitivity analysis, not a new causal estimator. It demonstrates how much a broad panel coefficient depends on whether the exposure step is timestamped by a database reporting year or by verified legal timing. The separately frozen event-study/holdout design remains the proper causal layer.
