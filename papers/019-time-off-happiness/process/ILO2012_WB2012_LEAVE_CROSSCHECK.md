# ARIS4C019 · ILO TRAVAIL 2012 × World Bank leave QA

**Date:** 2026-09-24  
**Purpose:** use an independent ILO legal cross-section to audit the World Bank standardized-case leave panel.

## Correct comparison

ILO's 2012 field is the minimum statutory entitlement for a worker in the **first year of service**, normalized to a five-day workweek. Therefore the closest World Bank comparator is `leave_1y`, **not** `leave_avg` across 1/5/10 years.

## Overlap

- ILO rows: **155**
- World Bank 2012 base-economy rows: **191**
- name-matched rows: **151**
- exact numeric ILO×WB first-year pairs: **143**
- unmatched ILO labels: **4**

## Agreement among exact numeric pairs

- Pearson correlation: **0.832**
- mean WB(1y) − ILO difference: **1.62 days**
- median difference: **1.00 days**
- mean absolute difference: **2.17 days**
- exact equality: **62/143**
- within 1 day: **75/143**
- within 2 days: **96/143**
- priority review (absolute gap >=5 days): **22**

## Largest gaps requiring legal/source review

| country | ILO first-year 5-day | WB first-year | difference |
|---|---:|---:|---:|
| Nicaragua | 10 | 30 | +20.0 |
| San Marino | 10 | 26 | +16.0 |
| Finland | 20 | 30 | +10.0 |
| Syria | 24 | 14 | -10.0 |
| Cameroon | 15 | 24 | +9.0 |
| Guinea | 21 | 30 | +9.0 |
| Togo | 21 | 30 | +9.0 |
| Peru | 21 | 13 | -8.0 |
| Zambia | 17 | 24 | +7.0 |
| Bangladesh | 10 | 17 | +7.0 |
| Tunisia | 12 | 18 | +6.0 |
| Uganda | 15 | 21 | +6.0 |
| Nepal | 12 | 18 | +6.0 |
| Italy | 20 | 26 | +6.0 |
| Bahrain | 21 | 15 | -6.0 |
| Djibouti | 25 | 30 | +5.0 |
| Libya | 25 | 30 | +5.0 |
| Sao Tome and Principe | 21 | 26 | +5.0 |
| France | 25 | 30 | +5.0 |
| Brazil | 21 | 26 | +5.0 |

A large gap is **not automatically a World Bank error**. Potential causes include sector/coverage differences, standardized-case assumptions, law interpretation, database vintage, public-holiday treatment, or an actual legal change around the reference period. These rows are a bounded legal-audit queue.

## No-universal-minimum cases

ILO's `no_universal_minimum` is a scope statement, not zero days. A positive World Bank value for the same country can reflect the World Bank's standardized worker/business scenario or sector-specific law and must not be averaged with ILO as if both measured the same construct.

## Decision

Use ILO 2012 as an **independent legal anchor and QA source**, not a silent replacement for the World Bank panel. For historical/legal synthesis:
- preserve both measures;
- prefer national primary law for treatment timing;
- use discrepancies >=5 days as priority verification cases;
- do not pool cross-source values until the measurement scope is reconciled.
