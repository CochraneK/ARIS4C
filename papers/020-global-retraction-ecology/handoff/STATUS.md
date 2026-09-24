# Status

## State
Active · 45%

## Current stage
Preliminary results + bilingual working paper · confirmatory denominator gate.

## Evidence
- Full RWDB snapshot frozen: 72,606 rows / 67,197 primary Retractions / 61,155 unique usable original DOI.
- Median publication→retraction lag: 490 days; descriptive only until survival denominator is available.
- OpenAlex pilot: 996/1,000 = 99.6%; shard 0: 15,146/15,255 = 99.2855%.
- OpenAlex enrichment now preserves 0/1/N candidates per query DOI, preventing one-to-many candidate inflation.
- Event/work identity, parsing, denominator, time-to-retraction, mass-event, citation-afterlife, work-type and reason-ontology gates frozen.
- Official Appendix-B reference has 111 reason names; observed snapshot has 110 unique labels, now handled as an explicit vocabulary-drift gate.
- 3 preliminary descriptive SVG figures and bilingual EN/ZH working-paper drafts committed.
- Core synthetic regression test for DOI collapse and fractional counting passed locally.

## Next gate
Complete OpenAlex shards 1–3 using the 0/1/N candidate-safe format; aggregate full DOI coverage; execute year × field denominators; reconcile observed 110 vs reference 111 Reason vocabulary; then freeze eligible OpenAlex work types.

## Blocker
No scientific-design blocker. Remaining confirmatory execution requires a networked runner. External browser credits are exhausted and private-repo GitHub Actions still fail before any job step starts (confirmed again after an explicit re-run).
