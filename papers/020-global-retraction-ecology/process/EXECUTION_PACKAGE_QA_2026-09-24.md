# Execution Package QA · 2026-09-24

## Result

**STATIC / CONTRACT QA: PASS**

This gate does not claim that network-dependent jobs have executed. It verifies that the current ARIS4C-020 package is internally wired for execution when a networked runner becomes available.

## Runner dependency check

`code/run_pipeline.py` references 21 executable/support scripts in the 020 code directory.

Result:
- missing referenced scripts: **0**
- runner references to nonexistent files: **0**

Core helper files (`pipeline_core.py`, `run_pipeline.py`) are present separately.

## CLI contract check

The runner call signatures were compared against each child script's current `argparse` contract.

Checked interfaces include:
- RWDB acquisition: `--out`
- RWDB audit: positional CSV + `--out`
- work table / reason network / ontology / vocabulary reconciliation
- lag profile / mass-event screen / audit figures
- OpenAlex enrichment: positional CSV + `--shard --shards`
- match summary / concordance
- OpenAlex retracted snapshot
- bidirectional concordance
- anomalous work-type QA
- field/type grouped denominators
- aggregated hazard panel
- optional citation-edge acquisition + citation-afterlife summary

No runner/CLI argument mismatch was found in the 2026-09-24 static inspection.

## OpenAlex live API contract check

Re-checked against current OpenAlex documentation on 2026-09-24:

- Bearer-token authentication is supported.
- Work queries support explicit `corpus=core`.
- OR batch retrieval supports up to 100 IDs.
- `group_by` supports cursor paging for >200 groups.
- `filter=cites:W...` returns incoming citing works.
- citing Works expose `referenced_works`, enabling batched target→citer edge reconstruction.

See:
- `OPENALEX_API_CONTRACT_2026-09-24.md`

## Offline smoke gate

`code/smoke_offline.py` now checks, without network or raw RWDB download:

1. Python compilation for every 020 code file;
2. `--help` startup for executable CLIs;
3. synthetic core identity/counting regression tests;
4. Appendix-B reference ontology QA.

`run_pipeline.py` invokes this smoke gate before acquisition/analysis.

## What remains unverified in this execution environment

Because the available runner surfaces currently cannot execute the private repository with outbound network access:

- the newly added offline smoke script has not yet been executed on the canonical Git checkout;
- production candidate-safe OpenAlex shards have not run;
- bidirectional concordance snapshot has not run;
- grouped denominators / hazard panel have not run;
- citation-afterlife edge acquisition has not run.

These are execution gates, not missing method/code design.

## Public-surface consistency check

Manually verified after Actions failed pre-runner:

- repository Chinese README: 020 appears exactly once at **52%**;
- English README: 020 = **52%**;
- Command Center showcase card: **52%**, current stage/title;
- Command Center detailed card: **52%**, current evidence/next gate/blocker;
- EN/ZH working-paper buttons are active;
- Chinese and English `portfolio-maturity.svg`: 020 = **52%**;
- corrupted Chinese README literal `\\n` row was removed.

## Gate

**PASS_STATIC_CONTRACT**

Next state transition requires actual execution:
`PASS_OFFLINE_SMOKE` → `PASS_NETWORK_MATCH` → `PASS_DENOMINATOR`.
