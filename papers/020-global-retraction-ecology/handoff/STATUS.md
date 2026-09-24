# Status

## State
Active · 48%

## Current stage
Executable pre-confirmatory package · networked denominator gate.

## Evidence
- Full RWDB snapshot frozen: 72,606 rows / 67,197 Retractions / 61,155 unique usable original DOI.
- OpenAlex feasibility: 996/1,000 pilot = 99.6%; historical shard 0 = 15,146/15,255 = 99.2855%.
- Production OpenAlex format is one query DOI → 0/1/N candidates; all four shards must be rerun in this format.
- OpenAlex `is_retracted` is concordance only; recent literature independently documents false OpenAlex retraction markings.
- OpenAlex API key is sent only in the Authorization header; `corpus=core` is explicit; transient retry/backoff implemented.
- Reason reference ontology now has 111/111 Appendix-B labels mapped and 0 unclassified; observed 110-label snapshot reconciliation/manual audit remains.
- Core work table, full/fractional counting, reason network, lag profile, mass-event screen, work-type QA, match summarizer and one-command pipeline runner are implemented.
- 3 descriptive SVG figures, 2 preliminary tables and EN/ZH working-paper drafts are committed.

## Next gate
Run `RUNBOOK.md` on a networked execution surface: candidate-safe OpenAlex shards 0–3 → match summary → work-type QA → year × field denominators → observed Reason reconciliation → eligible-type freeze.

## Blocker
No scientific-design blocker. Firecrawl credits are exhausted and private-repo GitHub Actions still fail before any job step starts; the remaining network-dependent work is fully scripted and resumable.
