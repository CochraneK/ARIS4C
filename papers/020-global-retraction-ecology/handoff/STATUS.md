# Status

## State
Active · 52%

## Current stage
Executable event-to-work / concordance package · networked confirmatory gate.

## Evidence
- Frozen RWDB snapshot: 72,606 rows / 67,197 primary Retractions / 61,155 unique usable original DOI.
- OpenAlex feasibility: 996/1,000 pilot = 99.6%; historical shard 0 = 15,146/15,255 = 99.2855%.
- Production matching preserves 0/1/N candidates and reruns all four shards.
- RWDB→OpenAlex concordance and a bidirectional OpenAlex `is_retracted=true` snapshot/comparison are fully scripted; the latter records retrieval time and SHA-256.
- 111/111 Appendix-B reference Reason labels map to orthogonal facets; observed snapshot has 110 labels pending exact reconciliation/manual audit.
- Closest 2026 competitor already covers global denominator-normalized incidence, field/country/publisher comparisons, lag and concentration; 020 has been explicitly repositioned away from those as standalone novelty claims.
- Aggregated cohort×field×age hazard construction is implemented, avoiding a 100M+ individual-control table.
- Citation-afterlife edge acquisition and work-level summary are implemented as an opt-in heavy run.
- 3 preliminary figures, 2 preliminary tables, bilingual working drafts, prior-art matrix, analysis freeze and one-command runbook are committed.

## Next gate
On a networked runner execute the runbook: candidate-safe shards 0–3 → match summary → RWDB↔OpenAlex concordance → anomalous work-type QA → year×field/type denominators → aggregated hazard panel → observed Reason reconciliation. Then freeze eligible work types and unlock confirmatory incidence/sensitivity models.

## Blocker
No scientific-design blocker. Current remaining blocker is network execution: Firecrawl credits are exhausted and private-repo GitHub Actions still fail before any job step starts. The full network-dependent chain is scripted, resumable, and provenance-aware.
