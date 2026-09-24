# Post-WB Audit · ARIS4C-020 · 2026-09-24

## Verdict

**CONDITIONAL PASS**

The WorkBuddy/networked run is substantively real and useful. It successfully executed the previously blocked network chain and produced reproducible derived artifacts. It is **not yet a final/frozen confirmatory package**, because post-run QA found two measurement-contract defects and one incomplete adjudication gate.

## What passed

- RWDB snapshot reproduced exactly: 72,606 rows / 67,197 Retractions / 61,155 unique usable original-paper DOI.
- Offline smoke executed successfully after fixing the recursion bug.
- Candidate-safe OpenAlex matching executed for all four shards:
  - queried unique DOI: 61,155
  - matched at least once: 60,773 (99.375%)
  - single candidate: 60,743
  - ambiguous multi-candidate: 30
  - unmatched: 382
- RWDB → OpenAlex `is_retracted` concordance is internally coherent:
  - 60,208 true
  - 535 false
  - 60,743 unique single-candidate matches
  - true share = 99.119%
- OpenAlex core `is_retracted=true` snapshot actually contained 136,000 Work rows:
  - 134,923 rows with DOI
  - 1,077 rows without DOI
  - 134,890 unique DOI
- Year × field and year × type denominator files exist for 1990–2025.
- Hazard panel contains 12,246 cohort×field×age rows, no negative risk sets and no hazard values outside [0,1].
- Work-type QA sample exists: 158 anomalous rows across six types.
- Full-data lag, mass-event, Reason-network and ontology outputs exist.
- Raw/interim large files were not committed; compact derived artifacts were committed.

## Post-run issues found by controller audit

### A. Hazard coverage diagnostic mixed publication-year systems

The pre-fix `discrete_hazard_coverage.json` compared:
- denominator diagnostic grouped by **RWDB earliest publication year**
- matched numerator grouped by **OpenAlex publication_year**

This created impossible coverage ratios >1 (for example 1966=18.0 and 2022≈1.006).

The **hazard event panel itself uses OpenAlex publication_year aligned to the OpenAlex denominator**, so this does not automatically invalidate the panel. The coverage sidecar, however, is invalid until regenerated.

Fix committed:
- `build_discrete_hazard_panel.py` schema v2 now uses RWDB year on both sides of the coverage diagnostic;
- it separately records OpenAlex event-year counts and OpenAlex−RWDB publication-year disagreement.

Current committed pre-fix coverage JSON is explicitly marked `INVALID_PRE_RERUN`.

### B. Bidirectional concordance mixed Work-row counts with unique DOI language

The pre-fix result has:
- 134,923 DOI-bearing OpenAlex Work rows
- 134,890 unique DOI
- row-level class counts: 60,299 + 41,152 + 33,472 = 134,923

The STATUS text incorrectly described those class counts as classification of 134,890 unique DOI.

Fix committed:
- `compare_bidirectional_concordance.py` now emits both unique-DOI and Work-row classifications;
- duplicate DOI Work rows are reported explicitly.

Current pre-fix derived JSON is retained for provenance but labeled `PROVISIONAL_ROW_LEVEL_CLASSIFICATION` and requires rerun for the unique-DOI classification.

### C. One observed Reason label was left unclassified

Observed label:
`Miscommunication with/by Third Party`

Fix committed:
- maps to `process_actor = miscommunication_third_party`
- evidence specificity = `procedural_or_lifecycle`
- observed ontology now has 0 unclassified labels.

This closes the machine mapping gap; manual scientific review of the whole facet ontology is still recommended before headline facet claims.

## Remaining scientific gate

The 158 anomalous OpenAlex work-type rows are only **sampled**, not adjudicated. Their `adjudication` field is blank.

Therefore:
- eligible OpenAlex work types are not yet frozen;
- hazard/rate outputs remain pre-eligibility/provisional;
- comparative country/field/publisher results remain locked.

## Reproducibility note

The OpenAlex 136,000-Work snapshot was stored in ignored interim data with a local SHA-256 sidecar. The Git history currently records only the hash prefix in STATUS/SESSION, not a committed full snapshot manifest. The snapshot script should emit a small tracked manifest on the next rerun.

## Required next actions

1. Rerun corrected hazard coverage generation.
2. Rerun corrected bidirectional concordance summary.
3. Commit the full OpenAlex snapshot manifest (timestamp, bytes, full SHA-256, corpus/filter).
4. Adjudicate the 158 work-type QA rows.
5. Freeze eligible work types and mature/right-censoring rule.
6. Only then unlock comparative incidence/risk models and manuscript result refresh.

## Acceptance boundary

WB network execution: **PASS**.

WB claim of a fully frozen confirmatory chain: **NOT YET**.

Overall handoff status: **CONDITIONAL PASS — small targeted rerun + adjudication required, no redesign required.**
