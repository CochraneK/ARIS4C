# ARIS4C019 · Historical trend interpretation lock

**Locked:** 2026-09-24  
**Layer:** published WDH long-run trend coefficients × same-window annual working-hours trends  
**Status:** exploratory ecological association only; not causal annual-leave evidence.

## Canonical evidence base

- WDH Table 2 displayed rows: **200**.
- Exact unique trend rows after preserving then deterministically removing one exact source duplicate: **199**.
- Exact duplicate in the HTML source: **UK · ls4 · 1990–2020 · +0.025**, displayed twice.
- Unique WDH trend rows with >=10 annual-hours observations spanning >=10 years in the same calendar window: **190**.
- Countries represented in the matched hours–well-being bridge: **46**.
- Deterministic one-longest-series-per-country sensitivity: **46 rows / 46 countries**.

## Locked descriptive associations

Using pre-COVID WDH trend coefficients:

| analysis | Pearson r | Spearman rho |
|---|---:|---:|
| all 190 unique matched series (non-independent) | +0.101 | +0.094 |
| one longest series per country (46 countries) | -0.057 | -0.045 |
| happiness-question family | -0.225 | +0.110 |
| life-satisfaction family | +0.188 | +0.122 |
| best-worst-life family | -0.246 | +0.103 |

The pre-1990-start subset had produced a substantially more negative Pearson correlation. Once the full 1940s–2000s Table-2 frame is materialized, that pattern disappears. Therefore the earlier negative historical correlation is treated as **subset-selection sensitive and superseded for overall historical inference**.

## Interpretation lock

> Across the full published WDH long-run trend frame that can be aligned to annual working-hours histories, there is no stable monotonic ecological relationship between the rate of change in annual working hours and the rate of change in national subjective well-being. Direction and magnitude vary by measure family, era, duplicate handling and correlation metric. The historical trend bridge therefore does not establish that falling work hours cause rising happiness, nor the reverse.

This is compatible with the separate expanded-modern interpretation lock: the modern country-year panel likewise does not establish a stable positive or negative aggregate association after timing, macro and specification stress tests.

## Boundaries

- Do not treat repeated WDH instruments/windows within a country as independent country observations.
- Do not convert ecological trend correlation into an individual-level vacation effect.
- Do not infer the effect of statutory annual leave from actual-hours trends.
- Do not treat a 0–10 transformation as proof that distinct happiness/life-satisfaction instruments are identical.
- Do not replace the still-pending yearly WDH workbook with these published regression slopes; they are a valuable historical layer, not the raw panel.
- The project can still find effects in well-identified legal reforms or worker-level outcomes; this lock only constrains interpretation of this historical aggregate trend layer.

## Canonical machine-readable files

- `data/wdh_published_trends_table2.csv`
- `data/wdh_hours_window_matched_trends_full.csv`
- `data/wdh_hours_longest_series_per_country_full.csv`
- `data/wdh_hours_trend_association_summary_full.csv`
- `process/WDH_TABLE2_MATERIALIZATION_AUDIT.md`
