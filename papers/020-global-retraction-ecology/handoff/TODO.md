# TODO

- [x] Retrieve and hash the official full RWDB snapshot.
- [x] Commit source manifest, not the raw CSV.
- [x] Audit row count, identifiers, dates, duplicate DOI patterns and multi-label structure.
- [x] Freeze Retraction-only primary inclusion criteria.
- [x] Freeze multi-valued parsing rules for Subject/Country/Author/Institution/Reason.
- [x] Join DOI-linked records to OpenAlex: candidate-safe shards 0–3 executed 2026-09-24 (60,773/61,155 = 99.375% match; 30 ambiguous; 382 unmatched).
- [x] Build publication denominators by year × field (and × type): executed for 1990–2025.
- [x] Freeze retraction-reason ontology and co-occurrence representation: 110 observed labels reconciled against 111 reference labels (1 observed-only label `Miscommunication with/by Third Party` remains unmapped — document or extend ontology).
- [x] Design lag/survival models.
- [x] Design post-retraction citation afterlife analysis.
- [x] Stress-test mass-retraction/paper-mill episode sensitivity: screen + leave-cluster-out executed on full data (152 publisher clusters, 566 reason clusters, 58 years).
- [x] Execute offline smoke on a canonical checkout and record PASS_OFFLINE_SMOKE (2026-09-24; smoke_offline.py --help recursion bug fixed during the run).
- [x] Execute the full networked concordance/denominator/hazard chain and freeze results (pipeline manifest PASS 2026-09-24).
- [x] Complete OpenAlex work-type concordance QA *sampling* — 158 anomalous rows materialized with adjudication buckets.

Remaining:

- [ ] Adjudicate the 158 rows in `data/derived/openalex_work_type_qa.csv` and freeze the eligible work-type list.
- [ ] Freeze the right-censoring / mature-cohort rule for hazard interpretation.
- [ ] Decide the 1 unmapped reason label (`Miscommunication with/by Third Party`): extend ontology or map.
- [ ] Unlock comparative country/field/publisher risk results; refresh EN/ZH manuscript + figures with frozen numbers.
- [ ] Optional: citation-afterlife run (`run_pipeline.py --with-citations`) — large edge set, opt-in.
