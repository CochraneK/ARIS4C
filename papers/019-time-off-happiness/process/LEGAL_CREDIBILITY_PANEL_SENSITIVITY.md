# ARIS4C019 · Legal-credibility restricted panel sensitivity v1.0

**Date:** 2026-09-24  
**Purpose:** determine whether broad-panel leave coefficients are driven by unverified World Bank discontinuities.  
**Status:** association sensitivity, not causal identification.

## Changer structure

- observed leave-value changer countries in the WHR-linked WB panel: **26**
- changer countries with a matching panel change plus verified/verified-derived legal date and legal-timing coverage in the existing reform-validation registry: **8**
- unverified / mismatched / coding-sensitive changers removed in the restricted sensitivity: **18**

Verified changer set:
- Bahrain
- Canada
- China
- Croatia
- Kosovo
- Kuwait
- Lithuania
- Taiwan Province of China

Removed changer set:
- Bangladesh
- Bosnia and Herzegovina
- Ecuador
- Estonia
- Eswatini
- India
- Iraq
- Kazakhstan
- Liberia
- Malta
- Montenegro
- Namibia
- North Macedonia
- Saudi Arabia
- Slovenia
- Syria
- Tajikistan
- Uganda

## Results

- all_observed_changers / TWFE: beta=0.0420, cluster SE=0.0605, 95% CI [-0.0766, 0.1606], N=1934, countries=161
- all_observed_changers / FD: beta=-0.0941, cluster SE=0.0400, 95% CI [-0.1724, -0.0158], N=1628, countries=155
- all_observed_changers / LAG2: beta=0.1020, cluster SE=0.0492, 95% CI [0.0055, 0.1985], N=1540, countries=154
- all_observed_changers / LAG3: beta=0.1107, cluster SE=0.0500, 95% CI [0.0127, 0.2087], N=1409, countries=152
- verified_panel_change_changers_only / TWFE: beta=0.1314, cluster SE=0.1211, 95% CI [-0.1060, 0.3688], N=1714, countries=143
- verified_panel_change_changers_only / FD: beta=-0.1593, cluster SE=0.0840, 95% CI [-0.3239, 0.0054], N=1439, countries=137
- verified_panel_change_changers_only / LAG2: beta=0.2106, cluster SE=0.0951, 95% CI [0.0242, 0.3969], N=1363, countries=137
- verified_panel_change_changers_only / LAG3: beta=0.1223, cluster SE=0.1197, 95% CI [-0.1123, 0.3570], N=1247, countries=135
- china_only_plus_never_changers / TWFE: beta=0.1885, cluster SE=0.0303, 95% CI [0.1291, 0.2479], N=1622, countries=136
- china_only_plus_never_changers / FD: beta=-0.3593, cluster SE=0.0455, 95% CI [-0.4485, -0.2702], N=1361, countries=130
- china_only_plus_never_changers / LAG2: beta=0.4178, cluster SE=0.0300, 95% CI [0.3589, 0.4766], N=1287, countries=130
- china_only_plus_never_changers / LAG3: beta=0.4134, cluster SE=0.0309, 95% CI [0.3527, 0.4740], N=1177, countries=128
- china_lux_plus_never_changers / TWFE: beta=0.1885, cluster SE=0.0303, 95% CI [0.1291, 0.2479], N=1622, countries=136
- china_lux_plus_never_changers / FD: beta=-0.3593, cluster SE=0.0455, 95% CI [-0.4485, -0.2702], N=1361, countries=130
- china_lux_plus_never_changers / LAG2: beta=0.4178, cluster SE=0.0300, 95% CI [0.3589, 0.4766], N=1287, countries=130
- china_lux_plus_never_changers / LAG3: beta=0.4134, cluster SE=0.0309, 95% CI [0.3527, 0.4740], N=1177, countries=128

## Interpretation

The restricted panel is deliberately conservative: countries with an observed but unverified leave jump are removed entirely, while never-changing countries remain available to absorb common year shocks. This prevents a suspicious coding discontinuity from contributing within-country leave variation.

The China-only and China+Luxembourg variants are **diagnostic lower-dimensional checks**, not substitutes for the separately frozen event-study/holdout analyses. China is the cleanest leave-specific WB event in the original isolation audit; Luxembourg is closer to leave-specific but bundled with an added public holiday.

A stable coefficient across these restrictions would support measurement robustness, not causal identification. Direction changes or large magnitude changes indicate that the broad WB panel is sensitive to which legal discontinuities are trusted.
