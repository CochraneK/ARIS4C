# ARIS4C019 · 1962→2000→2012 statutory-leave bridge v1.1

**Corrected:** 2026-09-24  
**Design:** historical legal-category bridge; descriptive, not causal.

## Critical correction

The first implementation let empty 2012 numeric cells pass through JavaScript's `Number("") = 0`, which incorrectly coded India and Sri Lanka/Ceylon's `no_universal_minimum` status as less-than-two-weeks. This is fixed.

Nicaragua is also excluded from change statistics because primary-law QA already classifies its 2012 ten-day value as a source conflict rather than a legal retrenchment.

## Harmonized category scale

1. `less_than_two_weeks`
2. `about_two_weeks`
3. `three_weeks_or_more`

1962 uses ILO's own source-defined groups.  
2012 uses only `exact_annex` numeric values: <10, 10–14, >=15 five-day-workweek days.  
2000 enters the three-node subset only when the project's approximation confidence is high or medium.

## State-continuity firewall

Excluded from naive longitudinal mapping:
- Byelorussia: unsafe_soviet_republic_to_belarus
- Czechoslovakia: unsafe_split_state
- Germany, Democratic Republic: unsafe_reunification
- Germany, Federal Republic: unsafe_reunification_territorial_change
- Ukraine: unsafe_soviet_republic_to_independent_ukraine
- United Arab Republic: unsafe_historical_state_identity
- U.S.S.R.: unsafe_dissolved_state
- Viet-Nam: unsafe_partition_reunification
- Yugoslavia: unsafe_dissolved_state

Safe renames remain explicit (e.g. Burma→Myanmar, Ceylon→Sri Lanka, Malagasy Republic→Madagascar, Rumania→Romania, Republic of Togo→Togo).

## Valid 1962→2012 comparison

After requiring:
- safe state continuity,
- exact numeric 2012 ILO value,
- no already-adjudicated source conflict,

the comparable set contains **58 countries**.

- upward movement: **34**
- unchanged category: **24**
- downward movement: **0**

Transition matrix:
- three_weeks_or_more->three_weeks_or_more: **10**
- about_two_weeks->three_weeks_or_more: **23**
- about_two_weeks->about_two_weeks: **10**
- less_than_two_weeks->about_two_weeks: **5**
- less_than_two_weeks->less_than_two_weeks: **4**
- less_than_two_weeks->three_weeks_or_more: **6**

**No valid downward category movement remains** after the missing-value and Nicaragua source-conflict corrections.

## Three-node 1962→2000→2012 subset

High/medium-confidence 2000 numeric bridge + valid endpoints: **9 countries**.

Patterns:
- about_two_weeks->three_weeks_or_more->three_weeks_or_more: **3**
- about_two_weeks->about_two_weeks->about_two_weeks: **2**
- less_than_two_weeks->less_than_two_weeks->less_than_two_weeks: **2**
- about_two_weeks->about_two_weeks->three_weeks_or_more: **1**
- less_than_two_weeks->less_than_two_weeks->about_two_weeks: **1**

The 2000 frame is selected, so these counts are not global prevalence estimates.

## Interpretation

Among countries that can be linked safely and measured comparably, the source record shows **long-run stability or upward movement in statutory paid annual leave, not verified downward movement**. This describes legal-policy diffusion/expansion; it does not imply a corresponding monotonic increase in national happiness.

Canonical file: `data/ilo_1962_2000_2012_leave_bridge.csv`.
