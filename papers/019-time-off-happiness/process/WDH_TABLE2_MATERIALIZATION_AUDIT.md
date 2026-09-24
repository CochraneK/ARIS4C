# ARIS4C019 · WDH Table 2 materialization audit

**Date:** 2026-09-24  
**Source:** Veenhoven & Kegel (2024), Table 2.

- source-declared trends: **200**
- materialized rows: **200**
- exact unique trend rows after deterministic duplicate check: **199**
- exact duplicate rows: **1**
- duplicate identified: **UK · ls4 · 1990–2020 · slope +0.025**, appearing twice in the HTML table.
- cohort counts in the verbatim materialization: 1940s=3, 1950s=6, 1960s=12, 1970s=35, 1980s=39, 1990s=64, 2000s=41.

The 200-row file preserves the source table faithfully. Analytical reuse must deduplicate exact repeated rows before weighting, which yields **199 unique trend rows**.

The source itself reports, across the 200 displayed trends up to 2019, 62 significant rises, 19 significant declines and 119 non-significant changes. These are source-reported summary counts, not re-estimated from the rounded CI strings in this repository.
