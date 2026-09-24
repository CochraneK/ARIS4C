# Agent Handoff

## Cold start

Read in this order:

1. `STATUS.md`
2. `TODO.md`
3. `../RUNBOOK.md`
4. `../process/EXECUTION_PACKAGE_QA_2026-09-24.md`
5. `../process/ANALYSIS_FREEZE_V1.md`

Do not redesign the study before reading these files.


Continue ARIS4C-020 without re-planning from scratch.

1. Read `papers/020-global-retraction-ecology/process/RESEARCH_PLAN.md`.
2. Run `python papers/020-global-retraction-ecology/code/acquire_rwdb.py`.
3. Verify the generated provenance manifest and never commit the raw CSV.
4. Build a deterministic data-audit script before producing substantive rankings.
5. Freeze Retraction-only inclusion criteria and multi-valued parsing rules.
6. Do not compare fields/countries on raw counts as if they were risks; construct Crossref/OpenAlex denominators first.
7. Keep reason labels multi-label and preserve uncertainty around author/institution identity.
8. Commit each bounded analysis unit and update this handoff plus `papers/dashboard.json`.


## Runtime gate order · 2026-09-24

Before any network-dependent execution:

```bash
python papers/020-global-retraction-ecology/code/smoke_offline.py
```

Required transition:

`PASS_STATIC_CONTRACT → PASS_OFFLINE_SMOKE → PASS_NETWORK_MATCH → PASS_DENOMINATOR`

Do not skip directly from static QA to scientific interpretation.

## Immediate next action

Adjudicate the 158 anomalous rows in `data/derived/openalex_work_type_qa.csv` using the six allowed buckets, freeze the eligible work-type list and the right-censoring/mature-cohort rule, then unlock comparative country/field/publisher risk results and refresh the EN/ZH manuscript with the frozen numbers. The networked chain — PASS_OFFLINE_SMOKE, candidate-safe shards 0–3, bidirectional concordance, core `is_retracted` snapshot, year×field/type denominators and the censoring-aware hazard panel — was executed and frozen 2026-09-24 (see STATUS.md and `data/derived/pipeline_run_manifest.json`).
