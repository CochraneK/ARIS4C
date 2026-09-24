# ARIS4C019 · Historical coverage gate v0.1

**Gate date:** 2026-09-24  
**Effect inspection:** prohibited / none performed in this gate

## What is now materialized

The first historical coverage layer is no longer only a plan.

- source-level registry: **11 source families** spanning legal institutions, historical working time and subjective well-being;
- WVS wave metadata registry: **7 waves** scaffolded;
- WVS visible country registry: **229 source-wave-country rows** across Waves 1–6;
- unique WVS country/territory codes visible across those rows: **96**;
- Cantril 1957–1963 early-country seed: **10 historical countries/entities**;
- WVS Wave 1 early-country seed: **10 countries**;
- modern WORLD legal snapshot target: **193 UN member states**;
- existing World Bank legal panel: **202 economies / 3,434 rows / EW 2004–2020**;
- existing WHR annual panel in repository: **165 countries / 2,199 country-years through 2022**, with the WHR2024 refresh separately extending the frozen Pilot-0 source through 2023.

## Historical time depth now supported by concrete sources

| layer | earliest verified anchor | current role |
|---|---:|---|
| historical days/hours literature | 1870 | pre-modern working-time context / extraction pending |
| ILO paid annual leave standard | 1936 | international institutional diffusion |
| WDH happiness distributions | 1945 | postwar historical well-being backbone |
| Cantril self-anchoring ladder | 1957 | early cross-national bridge |
| Eurobarometer | 1973 | repeated European life satisfaction |
| WVS | 1981 | multi-wave global happiness / life satisfaction |
| World Bank Employing Workers | 2004 | annual statutory-leave screening |
| Gallup / WHR | 2005 | modern annual Life Ladder |
| WORLD global legal snapshot | 2015 | 193-country legal cross-section |

## WVS metadata inconsistency discovered

The IHSN catalogue pages report more countries/societies than are present in the currently visible country tables for several waves:

| wave | reported | visible rows | gap |
|---:|---:|---:|---:|
| 1 | 10 | 10 | 0 |
| 2 | 18 | 18 | 0 |
| 3 | 56 | 49 | 7 |
| 4 | 41 | 39 | 2 |
| 5 | 58 | 54 | 4 |
| 6 | 60 | 59 | 1 |

This is a **QA finding**, not a reason to guess missing countries. The expanded panel must reconcile each wave against the downloadable release/DDI before country-wave coverage is frozen.

## Interpretation of scale

The project is now materially broader than the Pilot-0:

- the modern legal universe can reach 193 countries;
- postwar happiness evidence begins in 1945 rather than 2005;
- WVS Waves 1–6 alone already expose 96 unique visible country/territory codes in the seed registry;
- causal reform events remain a separate, stricter subset and are not allowed to determine descriptive/global coverage.

## Next coverage gates

1. reconcile WVS Wave 3–7 release-country counts from downloadable metadata;
2. enumerate Eurobarometer country × survey-year life-satisfaction coverage;
3. acquire/export WDH Trends in Nations / comparable-question subsets where license and interface permit;
4. materialize ILO C052/C132 ratification rows with status and declared leave length;
5. add historical national-law effective dates separately from ILO ratification;
6. extend working-time country coverage using OECD 1970–2019 plus the historical 1870–2000 literature;
7. compute overlap cells among legal leave, realized hours and each well-being instrument before any expanded effect estimation.
