# ARIS4C019 · WHR2023↔WHR2024 Independent Overlap Cross-check

**Checked:** 2026-09-21  
**Purpose:** independent source-level corroboration before running the WHR2024 treatment-effect refresh.

## Inputs

### WHR2023 CSV transcription

- Repository: `jamesinjune/Epidemiology_of_Suicide`
- Path: `raw_data/DataForTable2.1WHR2023.csv`
- Git blob SHA: `4d12b77068fe3c084318c9d6c600d3ced794e18b`
- Rows: **2,199**

This is a CSV transcription of the WHR2023 Table 2.1 annual workbook used by the frozen Pilot-0.

### WHR2024 annual mirror

- Repository: `ahmedlubis/world-happiness-panel-analysis`
- Path: `World-happiness-report-updated_2024.csv`
- Pinned commit: `ba44f791215334b43e99b16bf6b83ac38de213bb`
- Git blob SHA: `8440054da65290bbe318be8c3bd28892ba7e128c`
- Rows: **2,363**

## Result

Country names were Unicode-normalized only for matching (for example Türkiye/Turkiye); no substantive geographic recoding was introduced.

For the **2,199 country-years already present in WHR2023**:

- matched in WHR2024: **2,199 / 2,199**
- missing from WHR2024: **0**
- Life Ladder differences at the published 3-decimal precision: **0 / 2,199**
- mean absolute Life Ladder difference: **0**
- maximum absolute Life Ladder difference: **0**

Therefore the WHR2024 mirror does **not** revise the published 3-decimal Life Ladder values for any country-year already present in the WHR2023 transcription.

WHR2024 additionally contains:

- **26** new observations dated 2022 that were absent from WHR2023;
- **138** observations dated 2023.

The 26 newly covered 2022 country-years are listed in `data/whr2024_new_2022_coverage.csv`. No Life Ladder values are stored in that coverage-only file.

## Consequence for the frozen source-refresh decomposition

This sharply narrows what A→B can mean:

- it cannot be driven by changed Life Ladder values among the 2,199 overlapping observations;
- any A→B difference can arise only because WHR2024 supplies additional **2022 survey observations** that were absent from the WHR2023 release;
- under the frozen legal T−4…T+4 event window, those extra 2022 observations can materially affect only the later 2019 reform windows, principally by changing available treated/donor observations;
- C→B then isolates the addition of 2023 observations.

This cross-check does not estimate any treatment effect and does not open the post-unlock holdout candidates.

## Caveat

The CSV-to-CSV overlap check validates the released 3-decimal annual values. The deterministic validator in `code/validate_whr2024_mirror.py` separately checks the pinned WHR2024 mirror against official WHR2024 published summary statistics and against the exact frozen WHR2023 workbook transport.
