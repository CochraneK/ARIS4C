# ARIS4C020 · Current status

- **Title:** The Global Ecology of Scientific Retractions: Event-to-Work Reconstruction, Reason Ecology, Timing, and Citation Afterlife
- **Project status:** wb-network-run-conditional-pass-postrun-qa
- **Activity:** active
- **Portfolio progress:** 75%
- **Current stage:** WB network run CONDITIONAL PASS · post-run QA rerun + work-type adjudication
- **Evidence established:** Network execution is real: PASS_OFFLINE_SMOKE; 61,155 DOI queried, 60,773 matched (99.375%); RWDB→OpenAlex is_retracted concordance 99.12%; 1990–2025 field/type denominators, mass-event outputs and a 12,246-row hazard panel exist. Controller post-run audit found two bounded QA contract defects: hazard coverage sidecar mixed RWDB/OpenAlex publication-year bases, and bidirectional concordance described Work-row class counts as unique-DOI counts. Both scripts are fixed; pre-fix derived files are explicitly marked provisional/invalid pending rerun. The single observed unmapped Reason label is now mapped. 158 anomalous work-type rows remain unadjudicated.
- **Next gate:** Rerun corrected hazard coverage and bidirectional concordance, commit a tracked full OpenAlex snapshot manifest, adjudicate the 158 work-type QA rows, freeze eligible types + censoring rule, then unlock comparative models/manuscript refresh.
- **Blocker:** No design blocker. A small network/local rerun is required for two corrected QA summaries; the ignored OpenAlex/RWDB intermediates are not in Git, so rerun needs the WB/local checkout or another networked executor.

## Source of truth

This snapshot is synchronized from `paper.json` and `papers/dashboard.json`. Study-specific `process/` files may contain finer-grained status and frozen design details.
