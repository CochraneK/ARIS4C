# Status

## State
Active · 38%

## Current stage
RWDB audited · OpenAlex match gate PASS · analysis contracts frozen.

## Evidence
- 72,606 RWDB rows; 67,197 primary Retraction records.
- 61,155 unique usable original-paper DOIs.
- OpenAlex deterministic 1,000-DOI pilot: **99.6%** matched.
- OpenAlex full-match shard 0: **15,146/15,255 = 99.2855%** matched; 0 API errors.
- Event/work identity, semicolon parsing and denominator contracts frozen.
- Reason analysis uses atomic RW labels + orthogonal facets + co-occurrence rather than a single forced cause.
- Citation-afterlife matched-control design and OpenAlex work-type concordance gate specified.

## Next gate
Execute OpenAlex shards 1–3 and year × field denominators; complete the 110-label reason mapping; QA anomalous OpenAlex work types before freezing eligible denominator types.

## Blocker
No scientific blocker. External browser credits are exhausted; remaining matching/denominator jobs require another networked execution surface. GitHub Actions currently fail before runner steps start.
