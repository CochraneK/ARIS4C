# Status

## State
Active · 36%

## Current stage
RWDB audited · OpenAlex match gate PASS · denominator contract frozen.

## Evidence
- 72,606 RWDB rows; 67,197 primary Retraction records.
- 61,155 unique usable original-paper DOIs.
- Deterministic 1,000-DOI OpenAlex pilot: **996/1,000 = 99.6%** matched.
- Full-match shard 0: **15,146/15,255 = 99.2855%** unique DOI matched; 0 API errors.
- Event/work identity contract prevents multi-record DOI inflation.
- RWDB semicolon-list parsing and OpenAlex denominator contracts are frozen.

## Next gate
Run deterministic OpenAlex shards 1–3, aggregate full match coverage, then generate year × field denominators and freeze eligible OpenAlex work types.

## Blocker
No scientific blocker. Firecrawl credits were exhausted after shard 0; remaining shards are executable with the committed networked enrichment script. GitHub Actions are currently failing before runner steps start.
