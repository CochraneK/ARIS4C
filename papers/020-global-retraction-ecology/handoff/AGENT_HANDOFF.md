# Agent Handoff

Continue ARIS4C-020 without re-planning from scratch.

## Canonical starting point

1. Read `STATUS.md`, `TODO.md`, and `../RUNBOOK.md`.
2. Read `../process/OPENALEX_MATCH_GATE.md`, `DENOMINATOR_SPEC.md`, `EVENT_WORK_IDENTITY_CONTRACT.md`, and `REASON_ONTOLOGY_SPEC.md`.
3. Treat the frozen RWDB 2026-09-23 snapshot SHA-256 `da61a30cd4b01b681d1b42ad43cae7ae9eca2213a4f33ff7e762b7942c93f663` as the current event-source snapshot.

## Do not redo

- Full RWDB acquisition feasibility and first data audit are complete.
- Retraction-only primary event population is frozen.
- Event-vs-work identity and full/fractional counting rules are frozen.
- OpenAlex feasibility is established: 99.6% deterministic 1,000-DOI pilot and 99.2855% historical shard-0 unique-DOI match.
- Reason reference ontology QA covers 111/111 Appendix-B reference labels.
- Time-to-retraction, mass-event, work-type and citation-afterlife analysis specifications already exist.
- Bilingual working manuscripts and preliminary figures/tables already exist.

## Next execution

On a networked runner:

```bash
python papers/020-global-retraction-ecology/code/run_pipeline.py
```

Production OpenAlex matching must rerun **all four shards 0–3** because the historical shard-0 feasibility run predates the candidate-safe 0/1/N wrapper format.

If an OpenAlex API key is available, set `OPENALEX_API_KEY` in the environment. Never paste or commit it; scripts send it through `Authorization: Bearer`.

## Hard scientific locks

- RWDB, not OpenAlex `is_retracted`, defines the primary Retraction population.
- Do not compare country/field/publisher “risk” using raw counts.
- Do not select one OpenAlex candidate silently when a DOI has multiple candidates.
- Do not force RWDB Reason into one mutually exclusive cause.
- Do not interpret affiliation as responsibility or citation as endorsement.
- Do not call the 490-day descriptive lag a population survival estimate.
- Do not unlock comparative Results until full match, denominator, right-censoring, work-type QA, mass-event and Reason-reconciliation gates pass.

Commit every bounded substantive work unit and update `papers/dashboard.json` plus this handoff.
