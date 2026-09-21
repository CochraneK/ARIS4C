# ARIS4C019 · Outcome Source Freshness Audit v0.2

**Audit date:** 2026-09-21  
**Stage:** post-unlock source audit

> Any newer outcome source is a post-unlock robustness update. It may not silently replace the frozen WHR2023 first-look source.

## 1. Frozen first-look source

- World Happiness Report 2023 historical annual workbook: `DataForTable2.1WHR2023.xls`
- annual national mean Life Ladder
- 2005–2022
- 2,199 country-year observations
- 165 countries/territories
- frozen SHA256 recorded in `data/source_inventory.json`

The first outcome look and its initial robustness layers remain tied to this source.

## 2. WHR2024 annual panel · validated post-unlock refresh

A pinned public transport mirror of the WHR2024 annual panel was validated before refreshed treatment estimates were produced:

- repository: `ahmedlubis/world-happiness-panel-analysis`
- pinned commit: `ba44f791215334b43e99b16bf6b83ac38de213bb`
- Git blob: `8440054da65290bbe318be8c3bd28892ba7e128c`
- 2,363 Life Ladder country-years
- 2005–2023
- published WHR2024 rounded summary statistics reproduced
- Israel 2023 cross-check reproduced

An independent WHR2023 CSV transcription contains 2,199 rows. All **2,199/2,199** overlapping WHR2023 country-year Life Ladder values equal the WHR2024 mirror at published three-decimal precision.

WHR2024 adds:

- **26** observations dated 2022 that were absent from the WHR2023 release;
- **138** observations dated 2023.

See:

- `process/WHR2024_MIRROR_VALIDATION.md`
- `process/WHR2024_OVERLAP_CROSSCHECK.md`
- `process/WHR2024_SOURCE_REFRESH_FREEZE.md`
- `process/WHR2024_SOURCE_REFRESH_RESULTS.md`
- `process/WHR2024_SOURCE_REFRESH_ROBUSTNESS.md`

## 3. Source-refresh result

The pre-written comparison separated:

- A-proxy: WHR2024 values restricted to the original WHR2023 country-year keys;
- B: WHR2024 through 2022, adding newly available 2022 observations;
- C: WHR2024 through 2023.

Pooled donor-adjusted event means:

- frozen exact-float WHR2023: **+0.110**, median **-0.099**;
- A-proxy: **+0.110**, median **-0.099**;
- B: **+0.108**, median **-0.099**;
- C: **+0.088**, median **-0.099**.

The 2023 extension does not stabilize a positive finding: Luxembourg flips negative and the C panel has 2 positive versus 6 negative event means. Leaving Bahrain out gives **-0.117**.

## 4. WHR2025 / WHR2026 boundary

The underlying Gallup World Poll research releases extend through 2024/2025, but the currently public Figure 2.1 downloads are **three-year-average life-evaluation series**, not annual country-year national means.

The WHR2025 Figure 2.1 workbook explicitly labels the outcome `Life evaluation (3-year average)`. Current Our World in Data Cantril-Ladder redistribution follows the same rolling three-year semantics for these newer rankings.

Therefore:

- do not treat WHR2025/WHR2026 Figure 2.1 rows as annual Life Ladder observations;
- do not algebraically invert overlapping three-year averages to manufacture annual 2024/2025 values;
- do not mix annual WHR2024 and rolling-average WHR2025/2026 observations in the event study;
- an annual extension through 2024/2025 requires an official or verifiably exact annual panel / Gallup access.

## 5. Scientific consequence

The openly reproducible annual panel is currently defensible through **2023**.

This is enough to lengthen Canada/Luxembourg follow-up, but not enough to admit Mexico 2023 under the frozen requirement of at least two full post-treatment annual observations.

Mexico remains a future holdout rather than an analyzed event.

## 6. Source anchors

- WHR Data Sharing: https://www.worldhappiness.report/data-sharing/
- WHR2024 chapter / appendix: https://www.worldhappiness.report/ed/2024/happiness-of-the-younger-the-older-and-those-in-between/
- WHR2024 statistical appendix: https://files.worldhappiness.report/WHR24_Statistical_Appendix.pdf
- WHR2025 Figure 2.1 workbook: https://files.worldhappiness.report/WHR25_Data_Figure_2.1v3.xlsx
- WHR2025 statistical appendix: https://files.worldhappiness.report/WHR25_Ch02_Appendix_B.pdf
- WHR2026 statistical appendix: https://files.worldhappiness.report/WHR26_Statistical_Appendix.pdf

## 7. Next source gate

Do not spend further effort searching unaudited mirrors unless they contain genuine annual 2024/2025 observations and can be independently validated against an official release. Source expansion is no longer the immediate bottleneck; legal-treatment isolation is.
