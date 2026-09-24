# TODO

- [x] Retrieve and hash the official full RWDB snapshot.
- [x] Commit source manifest, not the raw CSV.
- [x] Audit row count, identifiers, dates, duplicate DOI patterns and multi-label structure.
- [x] Freeze Retraction-only primary inclusion criteria.
- [x] Freeze multi-valued parsing rules for Subject/Country/Author/Institution/Reason.
- [~] Join DOI-linked records to OpenAlex: feasibility pilot + historical shard-0 PASS; production run must rerun candidate-safe shards 0–3.
- [~] Build publication denominators by year × field: denominator contract + executable grouped-count script frozen; execution pending full match coverage.
- [~] Freeze retraction-reason ontology and co-occurrence representation: 111/111 Appendix-B reference labels mapped with 0 unclassified; observed 110-label reconciliation + manual audit pending.
- [x] Design lag/survival models.
- [x] Design post-retraction citation afterlife analysis.
- [~] Stress-test mass-retraction/paper-mill episode sensitivity: screen + leave-cluster-out specification implemented; full-data execution pending.

- [ ] Complete OpenAlex work-type concordance QA before freezing denominator eligibility.

- [x] Create bilingual working paper and preliminary descriptive figures.
- [x] Add core work-level dedup / fractional-counting / reason-network pipeline and regression tests.

- [x] Harden OpenAlex secret/auth/retry handling and pin corpus=core.
- [x] Add one-command networked runbook and candidate-safe work-type QA materializer.
- [x] Freeze 2 preliminary audit tables alongside 3 descriptive figures.
