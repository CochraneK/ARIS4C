# ARIS4C019 · WDH long-run variable coverage gate v1.0

**Date:** 2026-09-24  
**Effect inspection:** none.

The WDH public “Average Happiness in Nations by Year” registry has now been materialized as a machine-readable coverage table.

## Materialized scale

- long-run variable series: **124**
- distinct nation labels: **61**
- earliest series start: **1946**
- all listed series satisfy the WDH Trends-in-Nations inclusion rule of **>=20 years and >=10 comparable data points**
- source means are transformed by WDH to a 0–10 range, but concept/question/scale identity is retained and must not be ignored.

## Concept-family counts

- happiness: **17** series
- life_satisfaction: **89** series
- life_satisfaction_mixed_4_5: **1** series
- best_worst_possible_life: **16** series
- delighted_terrible_life: **1** series

## Start-decade counts

| start decade | series |
|---:|---:|
| 1940s | 4 |
| 1950s | 6 |
| 1960s | 8 |
| 1970s | 32 |
| 1980s | 21 |
| 1990s | 31 |
| 2000s | 22 |

## Earliest long-run anchors

- United States happiness: 1946/1947 depending on variant;
- France happiness: 1947;
- United Kingdom happiness: 1948;
- Japan life satisfaction: 1958;
- Philippines best-worst possible life: 1959;
- Brazil / Egypt best-worst possible life: 1960;
- India / Japan / Panama / Poland best-worst possible life: 1962;
- Nigeria best-worst possible life: 1963.

This establishes a genuine pre-Gallup/postwar outcome layer rather than treating 2005 as the beginning of cross-national subjective-well-being history.

## Measurement rule

The registry includes happiness, life satisfaction, best-worst possible life and delighted-terrible life, with 2/3/4/5/7/10/11-step scales and mixed variants. The expanded project therefore:
1. models each comparable variable family/variant first;
2. retains WDH variable code and scale;
3. only synthesizes coefficients after bridge/harmonization diagnostics;
4. never treats every transformed 0–10 series as the same raw instrument.

Canonical file: `data/wdh_trends_mean_variable_registry.csv`.
