# Execution Runbook · ARIS4C-020

This is the cold-start execution path for any networked machine or agent.

## Prerequisites

- Python 3.10+.
- Network access to the official Crossref/Retraction Watch GitLab raw CSV and `api.openalex.org`.
- No third-party Python packages are required for the current pipeline.
- Optional but recommended: set `OPENALEX_API_KEY` in the environment. The key is sent only as an `Authorization: Bearer` header and must never be committed.

The OpenAlex analysis is pinned to **`corpus=core`**. OpenAlex added an opt-in expansion corpus in 2025/2026; relying on the implicit default would make long-term reproduction less explicit.

## One command

From repository root:

```bash
python papers/020-global-retraction-ecology/code/run_pipeline.py
```

This will:

1. acquire RWDB if the raw CSV is missing;
2. audit source rows/hash/schema;
3. create the unique-work table;
4. build Reason prevalence/co-occurrence;
5. reconcile observed Reason vocabulary with Appendix B;
6. build descriptive lag and mass-event screens;
7. run local regression/ontology QA;
8. rerun **all four** OpenAlex DOI shards in the candidate-safe 0/1/N format;
9. summarize full DOI match coverage;
10. quantify RWDB→OpenAlex `is_retracted` concordance;
11. snapshot OpenAlex core `is_retracted=true` works with timestamp + SHA-256 and classify original-DOI / notice-DOI / absent-both concordance;
12. materialize anomalous OpenAlex work-type QA cases;
13. create year×field and year×type denominator tables;
14. build the compact cohort×field×age hazard panel from grouped denominators.

## Offline/local-only validation

```bash
python papers/020-global-retraction-ecology/code/run_pipeline.py --skip-network --skip-download
```

This assumes `data/raw/retraction_watch.csv` already exists.

## Why shard 0 is rerun

The historical feasibility run for shard 0 established 15,146/15,255 unique DOI matches (99.2855%), but it was performed before we discovered that OpenAlex can return multiple Work candidates for one DOI. Production enrichment therefore reruns **0–3** using one wrapper row per query DOI:

```json
{
  "query_doi": "10.x/...",
  "candidate_count": 0,
  "candidates": []
}
```

This prevents one-to-many OpenAlex candidates from inflating work counts.

## Required gates before comparative risk results

Do not unlock country/field/publisher risk results until:

- four candidate-safe OpenAlex shards complete;
- full match summary is frozen;
- anomalous work-type QA is adjudicated;
- eligible work types are frozen;
- year×field denominator table exists;
- right-censoring/mature-cohort rule is frozen;
- mass-event sensitivity is executed.

## Files that stay out of Git

- `data/raw/`
- `data/interim/`
- large API caches

Only compact manifests, QA tables, derived aggregate tables, code and final figures belong in Git.

## Citation-afterlife run

Citation acquisition is intentionally **not** part of the default network run because the incoming-citation edge set can be much larger than the matching/denominator jobs.

Run it explicitly:

```bash
python papers/020-global-retraction-ecology/code/run_pipeline.py --with-citations
```

The citation fetcher batches multiple target OpenAlex Work IDs with the `cites:` OR filter, then uses each citing work's `referenced_works` list to recover target→citer edges. Completed batches are written atomically under gitignored `data/interim/openalex_citation_batches/`, so a failed run resumes without restarting finished batches.

The resulting work-level summary distinguishes citations published before, on, and after the earliest formal RWDB RetractionDate. Citing-work publication date is a bibliographic event-time proxy, not proof that the citing authors saw or endorsed the retracted claim.
