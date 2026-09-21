# ARIS4C019 · Outcome Source Freshness Audit v0.1

**Audit date:** 2026-09-21  
**Stage:** post-unlock source audit

> This audit evaluates whether the annual Life Ladder panel can be extended beyond the frozen WHR 2023 historical workbook without silently changing provenance. Any newer outcome source is a post-unlock data update and must be reported as such.

## 1. Frozen source used for the first outcome look

Current frozen Pilot-0 source:

- World Happiness Report 2023 historical annual workbook
- file name: `DataForTable2.1WHR2023.xls`
- coverage in the current pipeline: 2005–2022
- 2,199 country-year observations
- 165 countries/territories
- primary outcome: annual national mean Life Ladder
- transport: official WHR URL first; commit-pinned public mirror only if automated retrieval of the official object fails
- SHA256 is recorded in `data/source_inventory.json`

The first outcome look, robustness diagnostics, Callaway–Sant'Anna-style analysis, and Sun–Abraham-style robustness remain tied to this frozen source.

## 2. WHR 2024 annual panel

World Happiness Report 2024 explicitly states that:

- its Gallup World Poll release covers 2005/06 through 2023;
- Table 2.1 uses annual national average Life Ladder observations;
- actual average values for each survey year were available in an online data file accompanying the chapter.

The official 2024 statistical appendix reports **2,363** country-year observations with valid Life Ladder values.

A public GitHub mirror named `World-happiness-report-updated_2024.csv` contains:

- 2,363 data rows plus header;
- years 2005–2023;
- the same variable family used by the WHR annual panel: Country name, year, Life Ladder, Log GDP per capita, Social support, Healthy life expectancy, Freedom, Generosity, Corruption, Positive affect, Negative affect.

The mirror's row count and published summary statistics match the official WHR 2024 statistical appendix. It is therefore a strong transport candidate, but it is still a **mirror**, not the current official download endpoint.

### Decision

Do **not** silently replace the frozen WHR 2023 source.

Treat WHR 2024 annual data as a **post-unlock source-refresh robustness layer** only after:

1. the mirror is pinned to an immutable Git commit/blob;
2. SHA256 is recorded;
3. official WHR 2024 appendix summary statistics are reproduced exactly or within published rounding;
4. known published annual values (for example Israel 2023) are cross-checked;
5. the original WHR 2023 results remain preserved and reported.

## 3. WHR 2025 and WHR 2026

Official statistical appendices document annual GWP coverage through:

- WHR 2025: 2005/06–2024;
- WHR 2026: 2005/06–2025.

However, the current WHR Data Sharing page states that the freely downloadable Figure 2.1 data contain **three-year averages** of life evaluation, confidence intervals, and explanatory-factor contributions. Additional Gallup World Poll data require institutional request, journalist request, or Gallup Analytics access.

Therefore:

- do not treat WHR 2025/2026 Figure 2.1 downloads as annual country-year Life Ladder observations;
- do not reverse-engineer annual values from rolling three-year averages;
- do not use an unaudited Kaggle/third-party 2025/2026 file as the primary outcome source;
- a later annual extension to 2024/2025 is permitted only if an official or verifiably exact historical annual file is recovered.

## 4. Scientific consequence

The currently reproducible public annual panel can be safely extended to **2023 only as a post-unlock robustness update**, using the WHR 2024 annual-data mirror after exact validation.

This matters because:

- Luxembourg 2019 and Canada 2019 gain their legal-event-year +4 observation in 2023 if surveyed;
- newer reforms such as Mexico 2023 still have only one post-treatment year in a panel ending in 2023, so they do not pass the frozen >=2-post-years gate;
- an annual panel through 2024 or 2025 would materially expand the clean-reform holdout candidate set.

## 5. Source anchors

- WHR data-sharing page: https://www.worldhappiness.report/data-sharing/
- WHR 2024 Chapter 2: https://www.worldhappiness.report/ed/2024/happiness-of-the-younger-the-older-and-those-in-between/
- WHR 2024 statistical appendix: https://files.worldhappiness.report/WHR24_Statistical_Appendix.pdf
- WHR 2025 statistical appendix: https://files.worldhappiness.report/WHR25_Ch02_Appendix_B.pdf
- WHR 2026 statistical appendix: https://files.worldhappiness.report/WHR26_Statistical_Appendix.pdf
- candidate 2024 annual-data mirror: https://github.com/ahmedlubis/world-happiness-panel-analysis/blob/main/World-happiness-report-updated_2024.csv

## 6. Next gate

Build a deterministic validator for the WHR 2024 mirror. The validator must compare row count, year range, variable names, published summary statistics, and selected published annual values before any refreshed outcome estimate is run.
