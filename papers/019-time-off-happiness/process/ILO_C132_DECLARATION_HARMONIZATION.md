# ARIS4C019 · C132 declared-holiday-length harmonization guardrail

**Date:** 2026-09-24

NORMLEX records a holiday length declared at C132 ratification for all **39** current ratifiers, but the units are heterogeneous.

| declaration unit | countries |
|---|---:|
| unspecified_days | 3 |
| calendar_days | 6 |
| working_days | 17 |
| calendar_month | 2 |
| weeks | 10 |
| mixed_groups | 1 |

## Rule

The raw NORMLEX wording is canonical. This file adds only a lossless unit classification and a numeric value **within that unit**.

Do **not** convert automatically:
- 3/4/5 weeks to working days;
- a calendar month to 30 working days;
- calendar days to working days;
- Yemen's worker/employee split to one scalar.

Such conversions require assumptions about the workweek and national legal definitions and would create false precision.

## Analytical use

The declarations can support descriptive institutional-intensity summaries or stratified candidate screening. They are not assumed to equal the country's current statutory entitlement and are not a causal exposure without national-law verification.

Canonical file: `data/ilo_c132_ratification_harmonized.csv`.
