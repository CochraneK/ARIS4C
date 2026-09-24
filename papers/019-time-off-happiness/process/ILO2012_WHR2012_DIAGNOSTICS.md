# ARIS4C019 · 2012 cross-section heterogeneity / nonlinearity / influence diagnostics

**Date:** 2026-09-24  
**Base sample:** 114 countries with exact ILO/TRAVAIL 2012 statutory-leave value, WHR2012 Life Ladder and log GDP per capita.

## Nonlinearity

GDP + ILO-region adjusted quadratic model:
- linear term: **-0.174**, 95% CI [-0.549, 0.202]
- squared term: **0.035**, 95% CI [-0.023, 0.092]

No stable quadratic/U-shaped relationship is established.

## Leave-category descriptive means

| statutory leave | N | mean leave | mean Life Ladder | mean log GDP pc |
|---|---:|---:|---:|---:|
| <10 | 13 | 4.1 | 5.48 | 9.24 |
| 10-14 | 21 | 11.4 | 5.53 | 9.12 |
| 15-19 | 22 | 16.0 | 4.84 | 8.82 |
| 20-23 | 42 | 20.4 | 5.58 | 9.67 |
| 24-25 | 13 | 24.8 | 5.92 | 10.07 |
| 26+ | 3 | 29.3 | 6.05 | 9.95 |

The raw category means strongly mix income and region composition and are not interpreted causally.

## Region-specific GDP-adjusted slopes

| region | N | beta per +5 days | 95% CI |
|---|---:|---:|---:|
| Africa | 31 | -0.220 | [-0.486, 0.046] |
| Asia and Pacific | 20 | -0.029 | [-0.303, 0.245] |
| Europe and CIS | 32 | 0.235 | [-0.106, 0.577] |
| Americas and Caribbean | 21 | 0.055 | [-0.176, 0.285] |
| Middle East (Arab States) | 10 | 0.189 | [-0.272, 0.649] |

Excluding Europe entirely, the adjusted coefficient is **-0.015**, 95% CI [-0.153, 0.124], N=82.

## Leave-one-country-out influence

Across 114 leave-one-country-out refits of the adjusted linear model:
- minimum beta: **0.006** when dropping Sri Lanka
- maximum beta: **0.062** when dropping Iran
- positive beta in **114/114** refits; negative beta in **0/114**

No single country creates a hidden strong positive association; the coefficient stays small.

## Lock

The 2012 cross-section does not reveal a robust linear, quadratic, or region-general positive association between statutory paid annual leave and national Life Ladder after basic macro/geographic adjustment. This is an aggregate association result, not evidence that individual vacations lack wellbeing benefits.
