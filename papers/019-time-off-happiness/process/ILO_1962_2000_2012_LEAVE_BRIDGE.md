# ARIS4C019 · 1962→2000→2012 statutory-leave bridge

**Date:** 2026-09-24  
**Design:** historical legal-category bridge; descriptive, not causal.

## Harmonized category scale

For longitudinal screening only:

1. `less_than_two_weeks`
2. `about_two_weeks`
3. `three_weeks_or_more`

1962 uses the ILO article's own source-defined groups.  
2012 uses the standardized five-day-workweek value: <10 days, 10–14 days, >=15 days.  
2000 is used only where the project's five-day approximation has **high or medium** confidence.

This does not erase raw legal wording; all source-specific raw fields remain in the bridge.

## State-continuity firewall

The following 1962 entities are **not** naively linked longitudinally:
- Byelorussia: unsafe_soviet_republic_to_belarus
- Czechoslovakia: unsafe_split_state
- Germany, Democratic Republic: unsafe_reunification
- Germany, Federal Republic: unsafe_reunification_territorial_change
- Ukraine: unsafe_soviet_republic_to_independent_ukraine
- United Arab Republic: unsafe_historical_state_identity
- U.S.S.R.: unsafe_dissolved_state
- Viet-Nam: unsafe_partition_reunification
- Yugoslavia: unsafe_dissolved_state

Safe historical renames such as Burma→Myanmar, Ceylon→Sri Lanka, Malagasy Republic→Madagascar, Rumania→Romania and Republic of Togo→Togo are retained with explicit mapping.

## 1962→2012 comparable pair

- safe one-to-one/rename countries with a numeric 2012 category: **63**
- upward category movement: **34**
- same category: **26**
- downward movement: **3**

Transition matrix:
- three_weeks_or_more->three_weeks_or_more: **10**
- three_weeks_or_more->about_two_weeks: **1**
- about_two_weeks->three_weeks_or_more: **23**
- about_two_weeks->less_than_two_weeks: **2**
- about_two_weeks->about_two_weeks: **10**
- less_than_two_weeks->about_two_weeks: **5**
- less_than_two_weeks->less_than_two_weeks: **6**
- less_than_two_weeks->three_weeks_or_more: **6**

The dominant historical movement is upward into the three-weeks-or-more category, but country-level “downward” cells must be audited before being interpreted as legal retrenchment because definitions and coverage changed substantially between 1962 and 2012.

## Three-node comparable subset

Countries with:
- safe 1962 identity continuity,
- high/medium-confidence numeric 2000 approximation,
- exact numeric 2012 value:

**10 countries**

Patterns:
- about_two_weeks->three_weeks_or_more->three_weeks_or_more: **3**
- about_two_weeks->about_two_weeks->about_two_weeks: **2**
- less_than_two_weeks->less_than_two_weeks->less_than_two_weeks: **2**
- three_weeks_or_more->three_weeks_or_more->about_two_weeks: **1**
- about_two_weeks->about_two_weeks->three_weeks_or_more: **1**
- less_than_two_weeks->less_than_two_weeks->about_two_weeks: **1**

The 2000 frame is selected rather than global, so this three-node subset is not used to estimate global prevalence. It is a candidate generator for primary-law reconstruction.

## Interpretation

This bridge now gives 019 a genuine **mid-century → late-20th-century → 2012** legal-policy structure. It supports historical transition analysis without pretending all historical units, calendars, worker coverage rules or states are identical.

Canonical file: `data/ilo_1962_2000_2012_leave_bridge.csv`.
