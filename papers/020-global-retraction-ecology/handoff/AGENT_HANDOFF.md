# ARIS4C020 · Agent takeover brief

## What this project is

**The Global Ecology of Scientific Retractions: Event-to-Work Reconstruction, Reason Ecology, Timing, and Citation Afterlife**

WB completed the formerly blocked network run and produced real full-match, denominator, concordance and hazard artifacts. Post-run controller QA gives a conditional pass: two bounded summary/coverage contract defects were identified and fixed in code, their pre-fix derived outputs are marked provisional pending rerun, and 158 anomalous OpenAlex work-type rows remain to be adjudicated before confirmatory comparative results unlock.

## Current state

- Activity: **active**
- Progress: **75%**
- Stage: **WB network run CONDITIONAL PASS · post-run QA rerun + work-type adjudication**
- Evidence: Network execution is real: PASS_OFFLINE_SMOKE; 61,155 DOI queried, 60,773 matched (99.375%); RWDB→OpenAlex is_retracted concordance 99.12%; 1990–2025 field/type denominators, mass-event outputs and a 12,246-row hazard panel exist. Controller post-run audit found two bounded QA contract defects: hazard coverage sidecar mixed RWDB/OpenAlex publication-year bases, and bidirectional concordance described Work-row class counts as unique-DOI counts. Both scripts are fixed; pre-fix derived files are explicitly marked provisional/invalid pending rerun. The single observed unmapped Reason label is now mapped. 158 anomalous work-type rows remain unadjudicated.

## Immediate next action

**Rerun corrected hazard coverage and bidirectional concordance, commit a tracked full OpenAlex snapshot manifest, adjudicate the 158 work-type QA rows, freeze eligible types + censoring rule, then unlock comparative models/manuscript refresh.**

## Current blocker / gate

No design blocker. A small network/local rerun is required for two corrected QA summaries; the ignored OpenAlex/RWDB intermediates are not in Git, so rerun needs the WB/local checkout or another networked executor.

## Canonical files / entry points

- **paper.json:** paper.json
- **English paper:** manuscript/working_paper_en.md
- **Chinese paper:** manuscript/working_paper_zh.md
- **source:** https://github.com/CochraneK/ARIS4C/tree/main/papers/020-global-retraction-ecology

## Before changing anything

1. Read `TODO.md`, `DECISIONS.md`, and the newest entries in `CHATLOG.md` and `SESSION_LOG.md`.
2. Preserve frozen/preregistered design decisions unless the repository explicitly records an authorized amendment.
3. Do not broaden claims beyond the evidence state recorded in the manuscript/process files.
4. Use **Cochrane Kang** for visible author naming.
5. Do not commit secrets, private credentials, hidden chain-of-thought, or unnecessary sensitive personal data.
6. After a material change, update canonical research files first, then continuity files.

## Handoff completion rule

Before ending a substantial session:
- update `TODO.md`;
- append any material research decision to `DECISIONS.md`;
- append a public-safe conversation summary to `CHATLOG.md`;
- append what was executed/validated to `SESSION_LOG.md`.
