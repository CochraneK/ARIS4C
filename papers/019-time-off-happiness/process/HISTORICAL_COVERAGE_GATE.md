# ARIS4C019 · Historical coverage gate v0.2

**Gate date:** 2026-09-24  
**Effect inspection:** prohibited / none performed in this gate

## What is now materially available

The historical expansion now has executable coverage rather than only source plans.

| layer | materialized coverage | status |
|---|---:|---|
| WHR2024 annual Life Ladder availability | **2,363 country-years / 165 countries or territories / 2005–2023** | country-year coverage complete for the validated release |
| OWID annual working-hours availability | **5,063 country-years / 130 countries or territories / 1870–2023** | coverage-only panel materialized; numeric hours withheld from this gate |
| WVS visible Waves 1–6 | **229 wave-country rows / 96 unique codes** | seed materialized; Waves 3–6 catalogue-count mismatches remain explicit |
| WDH Trends in Nations comparable series | **105 measure-country long-series rows / 56 normalized country labels** | metadata materialized; series values not opened |
| Cantril ICPSR 7023 | **10 historical countries/entities / 1957–1963** | country seed materialized |
| Eurobarometer ECS73 | **9 countries / 1973** | first country-survey seed materialized |
| ILO C052/C132 | **54 + 39 ratifications source-count verified** | row-level bounded ingest code committed; live row materialization still pending |
| World Bank Employing Workers | **202 economies / 3,434 rows / EW2004–2020** | already materialized from Pilot-0 |
| WORLD 2015 | **193 UN member states target** | source verified; redistribution/license constraints retained |

## Cross-layer overlap before any effect inspection

| overlap | count |
|---|---:|
| WHR × actual-hours country-years | **1951** |
| WHR × actual-hours countries | **125** |
| WVS visible Waves 1–6 × actual-hours country codes | **89** |
| WDH comparable-series countries × actual-hours countries | **51** |
| WDH comparable-series countries × WHR countries | **55** |

These are availability intersections only. No happiness–hours or happiness–leave coefficient, correlation, ranking, sign or graph was computed.

## WDH comparability rule

The WDH Trends in Nations seed uses only series that WDH itself describes as spanning at least **20 years** and containing at least **10 comparable data points**. Measure family, response scale, WDH variable code and starting year are preserved. Apparent source-code anomalies are flagged rather than silently corrected. cite placeholder removed in repository artifact: source URL stored per row.

This seed is a bridge/coverage layer, not permission to pool 3-step happiness, 4-step life satisfaction, 10-step life satisfaction and 11-step life satisfaction as one raw outcome.

## Working-hours comparability rule

The materialized 1870–2023 availability derives from the OWID annual-working-hours series. Historical Huberman–Minns-era observations and later Penn World Table-era observations remain source-era separated. A numeric historical panel may be ingested next, but source changes must remain explicit.

## WVS QA lock

Current source metadata report more countries/societies than appear in visible catalogue country tables for Waves 3–6. No missing countries are guessed. Wave 7 remains pending official/current release-country inventory.

## ILO lock

NORMLEX currently reports **54 C052 ratifications (17 denounced/not in force)** and **39 C132 ratifications**. A bounded parser is committed at code/historical_ilo_ratification_ingest.py and hard-fails on count drift. Ratification remains an institutional anchor only; it is not silently treated as national statutory-entitlement adoption.

## Still closed before expanded effect estimation

1. materialize ILO C052/C132 country rows;
2. reconcile WVS Waves 3–7 against downloadable release/DDI metadata;
3. expand Eurobarometer country × survey coverage beyond the 1973 seed;
4. build WDH observation/question metadata beyond the long-series seed;
5. build national paid-leave primary-law chronology separately from ILO ratification;
6. ingest numeric actual-hours values with source-era/comparability flags;
7. create an instrument bridge manifest before harmonizing subjective-well-being scales.

Until these are satisfied, the expanded statistical ladder remains locked.
