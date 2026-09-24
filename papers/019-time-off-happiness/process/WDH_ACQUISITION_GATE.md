# ARIS4C019 · WDH historical happiness acquisition gate

**Date:** 2026-09-24

## Confirmed source

World Database of Happiness (WDH) provides an open-source Excel data file:

- **file:** `TrendsInNations-2023e.xlsx`
- **canonical URL:** `https://worlddatabaseofhappiness.eur.nl/wp-content/uploads/TrendsInNations-2023e.xlsx`
- purpose: longitudinal analysis of societal conditions and happiness;
- inclusion rule: national general-population happiness series spanning at least **20 years** and at least **10 comparable observations**;
- variables include mean happiness (M), happiness inequality (SD), happy-life-years (HLY), inequality-adjusted happiness (IAH), life expectancy and GDP growth.

The WDH site reports the following long-run cohort counts as of 2023:
- since 1940s: 2 nations;
- since 1950s: 3;
- since 1960s: 8;
- since 1970s: 16;
- since 1980s: 18;
- since 1990s: 42;
- since 2000s: 41.

A 2024 analysis using the 2022/2023 Trends in Nations material reports **200 qualifying time series in 70 nations over 1945–2021**.

## Acquisition state

The exact binary URL is pinned and the file is explicitly documented as open source. The current execution surface can read the web documentation but could not transfer the binary XLSX into the runtime. This is recorded as a **transport limitation**, not a data-availability limitation.

Do not substitute scraped chart values or reconstructed values while the official XLSX is unavailable.

## Analysis contract once acquired

1. preserve nation, year, happiness-measure variant and native/0–10 transformation metadata;
2. materialize mean happiness and SD separately;
3. never average distinct question variants into one series without the WDH equivalence rule;
4. classify each time series by first decade and observation count;
5. produce a country × year × measure coverage table before joining any time-off exposure;
6. estimate long-run association models separately from the Gallup/WHR annual model;
7. use happiness inequality as an additional descriptive/secondary outcome, not a substitute for mean happiness.
