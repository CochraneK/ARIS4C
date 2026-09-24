# Session Log

## 2026-09-24 · Project registration
- Verified official full-dataset access through Crossref / Retraction Watch.
- Registered paper 020 and dashboard state.
- Added acquisition script with SHA-256 provenance manifest.
- Added data-handling boundary and comprehensive research plan.
- Added continuity package.

## 2026-09-24 · First full-database audit
- Retrieved the official Crossref/Retraction Watch CSV generated 2026-09-23.
- Snapshot size 66,881,479 bytes; SHA-256 `da61a30cd4b01b681d1b42ad43cae7ae9eca2213a4f33ff7e762b7942c93f663`.
- Audited 72,606 rows; 67,197 are Retractions.
- 61,155 unique usable original-paper DOIs; DOI coverage 91.25%.
- All Retraction rows have parseable publication/retraction dates; median lag 490 days; 0 negative lags.
- Confirmed strongly multi-label reason structure: 110 reason labels, mean 3.96 labels per Retraction.
- Froze novelty boundary against recent 2026 paper-mill, OA-rate, medical-rate and citation-afterlife studies.

## 2026-09-24 · OpenAlex matching gate
- Deterministic 1,000-DOI pilot matched 996/1,000 (99.6%), with zero API errors.
- Sharded full-match design frozen as int(SHA256(doi)[:8],16) % 4.
- Shard 0 completed: 15,146/15,255 unique DOI matched (99.2855%); 109 unmatched; zero API errors.
- External browser credits were exhausted before shards 1–3. This is an execution-surface limitation, not a scientific/data blocker.
- Added resumable OpenAlex enrichment and grouped denominator scripts.
- Froze event-vs-work identity, RWDB semicolon parsing, and denominator contracts.

## 2026-09-24 · Executable pre-confirmatory package
- Added literature-positioning checks for Hauschke & Nazarovets (OpenAlex retraction-status discordance), Fletcher & Stevenson (RWDB×OpenAlex case-control pipeline), and Rawlins (RWDB×OpenAlex access-model work).
- Upgraded production OpenAlex matching to rerun all four shards in 0/1/N candidate-safe format; historical shard 0 remains feasibility evidence only.
- Pinned OpenAlex `corpus=core` for reproducibility after the expansion-corpus change.
- Moved optional OpenAlex API-key authentication to Authorization Bearer headers and added exponential retry/backoff for 429/5xx.
- Added deterministic anomalous work-type QA materializer and a one-command `RUNBOOK.md` / `run_pipeline.py`.
- Frozen Appendix-B reference ontology now covers 111/111 labels with 0 unclassified; observed snapshot has 110 and remains under reconciliation/manual audit.
- Added two preliminary audit tables. Current package is scientifically gated at networked full match + denominator execution, not at method design.
