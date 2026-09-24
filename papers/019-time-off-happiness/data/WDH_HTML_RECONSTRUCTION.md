# WDH HTML reconstruction contract

ARIS4C019 can reconstruct the long-run World Database of Happiness annual panel from the official public HTML even when the XLSX workbook is unavailable.

Core official equivalent-measure pages:
- 111B → `hl3`
- 111C → `hl4`
- 111D → `hl5`
- 121C → `ls4`
- 121D → `ls5`
- 122F + 122G → `ls10+11`
- 32D → `bw11`

Pipeline:
`official finding rows → transformed 0–10 means → within-country/type/year average → optional 122F/122G family combination`.

The seed validation in `process/WDH_HTML_RECONSTRUCTION_VALIDATION.md` reproduces published USA hl4 and Japan ls4 slopes to <0.001/year using only displayed HTML values. The full scraper lives in `code/rebuild_wdh_html_annual_panel.py`.

Do not discard `finding_measure_code`: a specific Trends-in-Nations registered variable can use a subset of question variants even when the equivalent-measure page contains a broader family.
