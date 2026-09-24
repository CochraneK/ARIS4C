# TODO

- [x] Retrieve and hash the official full RWDB snapshot.
- [x] Commit source manifest, not the raw CSV.
- [x] Audit row count, identifiers, dates, duplicate DOI patterns and multi-label structure.
- [x] Freeze Retraction-only primary inclusion criteria.
- [x] Freeze multi-valued parsing rules for Subject/Country/Author/Institution/Reason.
- [~] Join DOI-linked records to OpenAlex: 1,000-DOI pilot PASS; shard 0/4 complete; shards 1–3 pending execution.
- [~] Build publication denominators by year × field: denominator contract + executable grouped-count script frozen; execution pending full match coverage.
- [~] Freeze retraction-reason ontology and co-occurrence representation: six-facet ontology rules cover 111/111 Appendix-B reference labels in local dry-run; observed 110-label snapshot reconciliation + manual audit pending.
- [x] Design lag/survival models.
- [x] Design post-retraction citation afterlife analysis.
- [~] Stress-test mass-retraction/paper-mill episode sensitivity: screen + leave-cluster-out specification implemented; full-data execution pending.

- [ ] Complete OpenAlex work-type concordance QA before freezing denominator eligibility.

- [x] Create bilingual working paper and preliminary descriptive figures.
- [x] Add core work-level dedup / fractional-counting / reason-network pipeline and regression tests.
