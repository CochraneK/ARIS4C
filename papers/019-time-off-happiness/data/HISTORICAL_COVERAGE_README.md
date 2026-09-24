# ARIS4C019 · Historical coverage data map

This directory deliberately separates **coverage metadata** from scientific values/effects.

## Canonical coverage files

- `historical_source_coverage.csv` — source-level registry and provenance.
- `historical_country_source_coverage_v1.csv` — single canonical country/entity × source × year/wave availability master (**8,579 rows** at Gate v0.3).
- `historical_coverage_overlap_summary.csv` — availability intersections only.
- `historical_wvs_wave_registry.csv` — WVS wave QA/count registry.
- `historical_wvs_country_visible_registry.csv` — visible Waves 1–6 country rows; mismatches vs reported counts remain explicit.
- `historical_wdh_trends_comparable_seed.csv` — WDH series satisfying the source's >=20-year / >=10-comparable-point rule; metadata only.
- `historical_eurobarometer_coverage.csv` — 1973–2016 availability; values omitted.
- `historical_working_hours_coverage.csv` — 1870–2023 availability with source-era flags; values omitted.
- `historical_early_wellbeing_country_seed.csv` — Cantril and early WVS seed metadata.

## Not yet materialized

- `ilo_c052_c132_ratifications.csv` — generated only after the NORMLEX parser passes the frozen 54+39 row gate.
- full WDH observation/question table;
- WVS Wave 7 and EVS country-wave release inventory;
- post-2016 Eurobarometer official machine inventory;
- national primary-law chronology;
- numeric historical working-hours panel.

## Firewall

Coverage scripts/tables may inspect whether a source contains a country/year/wave. They must not compute a time-off × well-being association, treatment sign, ranking, correlation, regression or event-study result before the expanded historical analysis unlock.
