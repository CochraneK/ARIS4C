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

## 2026-09-24 · Competitor repositioning + concordance/survival/citation engineering
- Closest competitor arXiv:2604.02302 inspected in full text; global denominator-normalized incidence, fractional country weighting, field/publisher comparisons, lag and concentration are now treated as prior art rather than ARIS4C-020 standalone novelty.
- Added closest-competitor gap analysis, confirmatory/exploratory analysis freeze, prior-art screening protocol and evidence matrix.
- Working title revised to emphasize event-to-work reconstruction, Reason ecology, timing and citation afterlife rather than causal “Causes.”
- Added aggregated cohort×field×age hazard construction from grouped OpenAlex denominators, avoiding materialization of the complete non-retracted work universe.
- Added batched OpenAlex incoming-citation acquisition using cites-filter OR batches and referenced-work back-mapping; citation afterlife remains an explicit heavy run.
- Added RWDB→OpenAlex concordance report and bidirectional OpenAlex is_retracted snapshot/comparison, including original-DOI vs notice-DOI separation.
- OpenAlex retracted snapshot now records retrieval timestamp and SHA-256 provenance.

## 2026-09-24 · Static execution-contract gate
- Repaired stale public surfaces: Chinese README duplicate/escaped rows removed; 019–023 table segment rebuilt from canonical dashboard; 020 Command Center cards and bilingual manuscript links synchronized.
- Forced both EN/ZH portfolio-maturity SVG entries for 020 from stale 28% to canonical progress.
- Re-verified current OpenAlex API contracts against 2026 documentation: Bearer authentication, explicit core corpus, up-to-100 OR batching, group_by cursor paging, and cites incoming-citation semantics.
- Added OPENALEX_API_CONTRACT_2026-09-24.md.
- Added smoke_offline.py and wired it as the first run_pipeline.py gate.
- Static QA: all 21 runner-referenced scripts exist and their argparse interfaces align with runner calls.
- Added EXECUTION_PACKAGE_QA_2026-09-24.md. Static contract PASS; actual offline/network execution still pending.


## 2026-09-24 · Networked confirmatory chain EXECUTED (GLM sandbox agent)
- Resolved the former execution-surface blocker: direct network access from the local sandbox reached both the GitLab RWDB source and api.openalex.org; OPENALEX_API_KEY picked up from env.
- Full RUNBOOK run (run_pipeline.py) completed end-to-end in ~45 min; manifest PASS.
- Offline smoke gate PASS (21/21 CLI help, 2/2 tests). Two bugs found and fixed during the run:
  1. smoke_offline.py had no argparse, so `--help` recursively re-ran the entire suite; guard added.
  2. audit_rwdb.py no longer emitted the `dates` block consumed by build_audit_figures.py (contract drift vs the committed 2026-09-23 audit JSON); block restored including recent_retraction_counts, year ranges, median lag years.
- Fresh RWDB snapshot identical hash to 2026-09-23 freeze: 72,606 rows / 67,197 Retractions / 61,155 unique original DOIs (sha256 da61a30c...).
- OpenAlex candidate-safe shards 0-3: 61,155 DOIs queried, 60,773 matched (99.375%), 30 ambiguous, 382 unmatched, 0 malformed.
- RWDB-to-OpenAlex is_retracted concordance: 99.12% true (60,208/60,743 single-candidate).
- OpenAlex core is_retracted=true snapshot: 136,000 works frozen with timestamp+sha256 sidecar (a7d20372...).
- Bidirectional DOI concordance: 60,299 original-DOI matches, 41,152 notice-DOI-only, 33,472 absent from RWDB; only 880 RWDB original DOIs absent from OpenAlex.
- Work-type QA: 158 anomalous rows materialized (reference-entry 50, retraction 50, erratum 42, paratext 8, other 6, supplementary 2).
- Denominators 1990-2025 (year x field, year x type) + censoring-aware hazard panel frozen (936 denominator cells, 4,664 event cells).
- Dashboard 020: 55 -> 75 (active). Next gate: work-type QA adjudication -> freeze eligible types + censoring rule -> comparative risk results -> manuscript refresh.
- Large regenerable intermediates (work_table.jsonl 63MB, openalex_retracted_not_rwdb_original.csv 15MB) added to .gitignore per RUNBOOK boundary.

## 2026-09-24 · Controller post-WB audit
- Verdict: CONDITIONAL PASS. WB network execution is real and valuable; no redesign required.
- Verified 61,155 DOI queries, 60,773 matched (99.375%), 60,743 single-candidate, 30 ambiguous, 382 unmatched.
- Verified RWDB→OpenAlex is_retracted concordance 60,208/60,743 = 99.12%.
- Found hazard coverage diagnostic year-basis bug: RWDB-year denominator vs OpenAlex-year numerator; pre-fix sidecar can exceed 1. Fixed build_discrete_hazard_panel.py; old sidecar marked INVALID_PRE_RERUN.
- Found bidirectional classification unit bug: class counts summed to 134,923 DOI-bearing Work rows while text called them 134,890 unique DOI. Fixed compare_bidirectional_concordance.py to emit both units; old output relabeled provisional row-level.
- Closed observed Reason mapping gap for Miscommunication with/by Third Party.
- Work-type QA remains sample-only: 158 adjudication cells blank. Comparative models remain locked.
- OpenAlex snapshot local SHA sidecar was not committed as a tracked manifest; add on rerun.
