# TODO

- [x] Retrieve and hash the official full RWDB snapshot.
- [x] Commit source manifest, not the raw CSV.
- [x] Audit row count, identifiers, dates, duplicate DOI patterns and multi-label structure.
- [x] Freeze Retraction-only primary inclusion criteria.
- [x] Freeze multi-valued parsing rules for Subject/Country/Author/Institution/Reason.
- [~] Join DOI-linked records to OpenAlex: feasibility PASS; production candidate-safe shards 0–3 pending network execution.
- [~] Build publication denominators by year × field: denominator contract + executable grouped-count script frozen; execution pending full match coverage.
- [~] Freeze retraction-reason ontology and co-occurrence representation: six-facet ontology rules cover 111/111 Appendix-B reference labels in local dry-run; observed 110-label snapshot reconciliation + manual audit pending.
- [x] Design lag/survival models.
- [x] Design post-retraction citation afterlife analysis.
- [~] Stress-test mass-retraction/paper-mill episode sensitivity: screen + leave-cluster-out specification implemented; full-data execution pending.

- [ ] Complete OpenAlex work-type concordance QA before freezing denominator eligibility.

- [x] Create bilingual working paper and preliminary descriptive figures.
- [x] Add core work-level dedup / fractional-counting / reason-network pipeline and regression tests.

- [x] Implement RWDB→OpenAlex and bidirectional RWDB↔OpenAlex retraction-status concordance pipelines.
- [x] Add OpenAlex is_retracted snapshot timestamp/SHA-256 provenance sidecar.
- [x] Build aggregated cohort×field×age censoring-aware hazard pipeline.
- [x] Implement batched OpenAlex citation-afterlife edge acquisition and summary.
- [x] Freeze closest-competitor gap, analysis freeze, prior-art protocol and evidence matrix.
- [ ] Execute the full networked concordance/denominator/hazard chain and freeze results.

- [x] Static execution-package QA: runner dependencies + CLI contracts + current OpenAlex API contract.
- [x] Add offline compile/CLI/synthetic smoke gate before full pipeline.
- [x] Repair/sync 020 README, Command Center and EN/ZH maturity SVG public surfaces.
- [ ] Execute offline smoke on a canonical checkout and record PASS_OFFLINE_SMOKE.
