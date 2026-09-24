# Status

## State
Active · 75%

## Current stage
Networked confirmatory chain EXECUTED · work-type adjudication gate.

## Evidence
- 2026-09-24: full RUNBOOK executed end-to-end on a networked checkout (sandboxed agent, direct network, OPENALEX_API_KEY from env). `pipeline_run_manifest.json` = PASS.
- Offline smoke gate: PASS_OFFLINE_SMOKE (compile ok; 21/21 CLI `--help`; 2/2 test suites; 111/111 ontology QA). Bug found+fixed: `smoke_offline.py` had no argparse, so `--help` recursively re-ran the whole suite; a guard was added.
- Bug found+fixed: `audit_rwdb.py` no longer emitted the `dates` block consumed by `build_audit_figures.py` (contract drift vs the committed 2026-09-23 audit JSON); the block was restored (retraction-year histogram, year ranges, median lag years).
- Fresh RWDB snapshot: 72,606 rows / 67,197 Retraction / 61,155 unique usable original DOI (sha256 `da61a30c…`, GitLab ETag `c6e074fe…`).
- Candidate-safe OpenAlex shards 0–3 complete: 61,155 unique DOIs queried → 60,773 matched (99.375%), 30 ambiguous multi-candidate, 382 unmatched, 0 malformed rows.
- RWDB→OpenAlex `is_retracted` concordance: 60,208 true / 535 false / 0 unknown = 99.12% of single-candidate DOI matches.
- OpenAlex core `is_retracted=true` snapshot frozen: 136,000 works, 44.1 MB jsonl + timestamp/SHA-256 sidecar (`a7d20372…`).
- Bidirectional RWDB↔OpenAlex DOI concordance: of 134,890 unique is_retracted OpenAlex DOIs — 60,299 match RWDB original DOI, 41,152 match notice DOI only, 33,472 absent from RWDB both ways; only 880 RWDB original DOIs absent from OpenAlex.
- Work-type QA sample materialized: 158 anomalous rows across 6 types (reference-entry 50, retraction 50, erratum 42, paratext 8, other 6, supplementary 2) with the 6 allowed adjudication buckets.
- Denominators built: year×field and year×type, 1990–2025.
- Aggregated censoring-aware hazard panel frozen: 936 denominator cells, 4,664 matched event cells (`discrete_hazard_field_panel.csv` + coverage sidecar).

## Next gate
Adjudicate the 158 rows in `data/derived/openalex_work_type_qa.csv` (buckets: ORIGINAL_CORRECT_TYPE / OPENALEX_TYPE_MISCLASSIFICATION / NOTICE_ORIGINAL_CONFUSION / MULTI_CANDIDATE_AMBIGUOUS / RWDB_IDENTITY_ISSUE / OTHER_LEGITIMATE_TYPE), freeze the eligible work-type list, freeze the right-censoring/mature-cohort rule, then unlock comparative country/field/publisher risk results and refresh the EN/ZH manuscript with frozen numbers.

## Blocker
None. The former "no networked execution surface" blocker is resolved — direct network access from the local sandbox sufficed (Firecrawl/GitHub Actions no longer needed).
