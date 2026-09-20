# ARIS4C019 · Data Source Audit v0.1

_Last checked: 2026-09-21._

## 1. Paid annual leave legislation

### ILO

- Global legislative trends on paid annual leave (2026-07-27)
- https://www.ilo.org/publications/global-legislative-trends-paid-annual-leave
- Strength: current global legal-policy framing and standardized concepts.
- Limitation: the research brief itself is not automatically a complete annual country-year panel.

### ILO TRAVAIL / Conditions of Work and Employment Laws

- https://www.ilo.org/resource/other/database-conditions-work-and-employment-laws
- Strength: comparative legal information across 100+ countries and some historical comparisons.
- Limitation: legacy database; last general update was 2009, so it is mainly useful for historical reconstruction and validation.

### World Bank Employing Workers / historical Doing Business

- Current working-hours table: https://www.worldbank.org/en/research/employing-workers/data/working-hours
- Historical Doing Business catalog: https://datacatalog.worldbank.org/search/dataset/0038564/doing-business
- Strength: harmonized fields include paid annual leave for workers with 1, 5 and 10 years of tenure; Doing Business historical data span 2004–2019 and are public.
- Limitation: hypothetical-worker assumptions and discontinued Doing Business framework require careful interpretation. Preserve original definitions and never present the measure as realized vacation use.

## 2. Actual working time

### OECD

- Average annual hours actually worked per worker.
- Strength: current harmonized trend series with long historical coverage for many OECD members.
- Critical caveat from OECD: use is intended for comparison of trends over time; level comparisons across countries can be misleading because source methods differ.

### Our World in Data / Penn World Table + historical reconstruction

- https://ourworldindata.org/grapher/annual-working-hours-per-worker
- Strength: long-run annual-hours series (historical reconstruction plus PWT), useful for sensitivity and long-range context.
- Limitation: source definitions differ across eras; not a direct legal-leave measure.

## 3. Subjective well-being

### World Happiness Report / Gallup World Poll

- https://www.worldhappiness.report/data-sharing/
- Strength: Gallup World Poll has comparable surveys across more than 160 countries/territories since 2005.
- Current access limitation: free WHR downloads emphasize published aggregates such as three-year average life evaluations; finer Gallup data can require researcher institutional access or subscription.
- Consequence: annual country-year coverage must be audited before the confirmatory design is frozen.

### OECD Current Well-being

- Life satisfaction, 0–10 scale.
- Strength: official national-statistics ecosystem and SDMX API.
- Limitation: country-year coverage is uneven and relatively recent for many countries.

## 4. Pilot source strategy

Preferred first-pass panel:

1. World Bank historical paid annual leave, 2004–2019;
2. OECD/PWT actual hours as realized-time checks;
3. the densest defensible annual life-satisfaction source that can be lawfully accessed;
4. macro controls from standard international sources.

If annual global happiness coverage is too sparse, narrow the confirmatory scope rather than filling years by interpolation.

## 5. Non-negotiable measurement rules

- annual leave != public holidays;
- statutory entitlement != leave taken;
- annual hours != vacation days;
- three-year average happiness != single-year outcome;
- do not interpolate policy changes or happiness simply to create a balanced panel;
- retain source/definition/version metadata for every country-year cell.
