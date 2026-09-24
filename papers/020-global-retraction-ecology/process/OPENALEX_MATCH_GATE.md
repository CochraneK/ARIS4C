# OpenAlex DOI Match Gate · 2026-09-24

## Deterministic 1,000-DOI pilot

A reproducible sample of 1,000 unique RWDB Retraction original-paper DOIs was selected by sorting on `SHA256("aris4c020:" + normalized_doi)`.

- matched: **996 / 1,000**
- match rate: **99.6%**
- API errors: **0**
- median current OpenAlex cited-by count: **4**
- mean current cited-by count: **14.79**

## Full-match shard 0

Full matching is resumably partitioned by:

`int(SHA256(doi)[:8], 16) % 4`

Shard 0:
- input: **15,255 unique DOI**
- matched: **15,146**
- unmatched: **109**
- match rate: **99.2855%**
- API errors: **0**

The external browser runner exhausted credits before shards 1–3. This is an execution-surface limitation, not an OpenAlex/data failure.

OpenAlex `is_retracted` is treated only as a concordance signal. RWDB remains the authority for membership in the primary Retraction population.

**Gate: PASS for full DOI enrichment.** Comparative rate claims remain locked until denominator and full-match coverage gates are complete.
