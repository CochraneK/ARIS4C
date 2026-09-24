# Status

## State
Active · 75%

## Current stage
WB network run CONDITIONAL PASS · post-run QA rerun + work-type adjudication.

## Evidence
- Networked RUNBOOK execution is real and substantially successful: PASS_OFFLINE_SMOKE; 61,155 DOI queried; 60,773 matched (99.375%); 30 ambiguous; 382 unmatched.
- RWDB→OpenAlex single-candidate `is_retracted` concordance remains valid: 60,208 true / 535 false = 99.12%.
- OpenAlex core snapshot contained 136,000 Work rows; field/type denominators 1990–2025 and the 12,246-row hazard panel were produced.
- Post-run controller QA found two bounded reporting/diagnostic contract defects:
  1. pre-fix hazard coverage sidecar mixed RWDB-year and OpenAlex-year bases, allowing impossible coverage >1;
  2. pre-fix bidirectional class counts were Work-row counts (n=134,923), but STATUS described them as unique-DOI classification (n=134,890).
- Both scripts are fixed; the old derived files are explicitly marked invalid/provisional pending rerun.
- Observed Reason ontology gap is closed: `Miscommunication with/by Third Party` now maps to `miscommunication_third_party`; observed unmapped count = 0.
- Work-type QA is not complete: 158 rows are sampled but adjudication cells remain blank.

## Next gate
Rerun the corrected hazard coverage sidecar and bidirectional concordance summary; commit a tracked full OpenAlex snapshot manifest; adjudicate the 158 work-type QA rows; freeze eligible work types and the mature/right-censoring rule; then unlock comparative country/field/publisher models and refresh the EN/ZH manuscript.

## Blocker
No design blocker. A small network/local rerun is required because the corrected summaries depend on ignored raw/interim files that are not committed to Git. Use the WB/local checkout if its interim files remain; otherwise rerun the network acquisition chain.
