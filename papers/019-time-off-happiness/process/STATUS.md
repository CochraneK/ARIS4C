# ARIS4C019 · Process status

- Stage: Historical expansion · Coverage Gate v0.3 · legal/measurement materialization
- Activity: active
- Progress: 66%
- Scope correction: the previous 98% state referred to the narrow leave-specific Pilot-0/publication package, not the user's original broad question. The project-level scope remains reopened.
- Pilot-0: **PASS / frozen sub-study**. Eight-event WHR2024 refresh + independent Israel holdout + legal isolation audit + bilingual/SIR package remain preserved and must not be retroactively rewritten.
- Canonical historical availability master: **8,579 coverage-only rows / 11 materialized source IDs** in `data/historical_country_source_coverage_v1.csv`; all rows explicitly record `value_inspected=no`.
- Materialized depth: OWID working-hours availability **5,063 country-years / 130 entities / 1870–2023**; WDH comparable long-series metadata **105 rows / 56 normalized country labels / earliest 1946**; Eurobarometer **809 entity-years / 1973–2016**; WVS visible Waves 1–6 **229 rows / 96 country codes**; WHR2024 **2,363 country-years / 165 entities / 2005–2023**; Cantril **10 historical countries/entities**.
- Outcome-blind overlap: WHR × hours **1,951 country-years / 125 countries**; WVS visible Waves 1–6 × hours **89 country codes**; WDH comparable-series × hours **51 countries**; WDH × WHR **55 countries**.
- No-effect coverage dashboard: `figures/historical_coverage_timeline.svg`.
- ILO: official current counts remain C052 **54 ratifications / 17 not in force** and C132 **39 ratifications**; bounded parser committed in `code/historical_ilo_ratification_ingest.py`, row materialization pending a networked execution surface.
- Immediate gate: materialize ILO rows; reconcile WVS Wave 7 + EVS country-wave coverage; replace/extend Eurobarometer transport with official GESIS/EC metadata; build national primary-law chronology; then ingest numeric historical hours and WDH observation/question data under explicit comparability flags.
- Expanded effect estimation remains locked.
- Existing PDF-publication runner issue remains an engineering issue for the frozen Pilot-0 snapshot only and is not the project-level blocker.
