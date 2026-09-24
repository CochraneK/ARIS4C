# ARIS4C-020 · Global Retraction Ecology

## Current state · 2026-09-24

**Active · 48%**

- full RWDB snapshot frozen: 72,606 rows / 67,197 Retractions / 61,155 unique usable original-paper DOI;
- median publication→retraction lag: 490 days (descriptive among eventually retracted works);
- deterministic OpenAlex pilot: 996/1,000 = 99.6%; historical shard-0 feasibility: 15,146/15,255 = 99.2855%;
- production OpenAlex matching now uses one query DOI → 0/1/N candidates and reruns **all four shards**;
- OpenAlex requests pin `corpus=core`, use Bearer-header API-key auth, and retry 429/5xx safely;
- 111/111 Appendix-B reference Reason labels have explicit orthogonal-facet mappings; observed snapshot has 110 labels and remains under reconciliation/manual audit;
- 3 preliminary SVG figures, 2 compact tables, EN/ZH working drafts, regression tests, and a one-command execution runbook are committed;
- next gate: run `RUNBOOK.md` on a networked execution surface to finish full match + year×field denominators.

Key gates: [first data audit](process/FIRST_DATA_AUDIT.md) · [OpenAlex match](process/OPENALEX_MATCH_GATE.md) · [denominator spec](process/DENOMINATOR_SPEC.md) · [reason ontology](process/REASON_ONTOLOGY_SPEC.md) · [citation afterlife](process/CITATION_AFTERLIFE_SPEC.md) · [execution runbook](RUNBOOK.md)

## Question

What does the global retraction system actually look like when we use the full Retraction Watch database, normalize by the underlying publication universe, preserve multi-label retraction reasons, model publication-to-retraction time, and follow citations after retraction?

## Why this is not another “top countries / journals” paper

Absolute retraction counts confound publication volume, database coverage, editorial detection, publisher policy, field composition, time, and mass events such as paper-mill cleanups. The primary analyses therefore separate:

1. **Counts** — what Retraction Watch records.
2. **Rates** — retractions per eligible publication denominator.
3. **Detection / policy process** — when and how records are retracted.
4. **Reason structure** — multi-label causes and co-occurrence.
5. **Afterlife** — citations before and after the retraction notice.

## Data spine

- **Retraction Watch / Crossref bulk CSV** — canonical retraction-event source.
- **Crossref REST / public metadata** — DOI metadata and update relations.
- **OpenAlex** — discipline/topic assignment, publication denominators, institutions and citation graph.
- Optional sensitivity sources: OpenCitations, PubMed for domain-specific validation.

The raw bulk snapshot belongs in `data/raw/` and is intentionally gitignored. A compact provenance manifest with URL, retrieval timestamp, hash, bytes, row count and columns is committed under `data/manifests/`.

## Primary analysis families

- time trends and publication-cohort retraction rates;
- field-normalized and year-normalized retraction risk;
- country / institution / journal / publisher rates with exposure denominators;
- publication-to-retraction lag and survival/hazard models;
- controlled-vocabulary reason prevalence and reason co-occurrence networks;
- reason × field × time heterogeneity;
- repeated-author / repeated-institution clusters with explicit identity uncertainty;
- mass-retraction and paper-mill episode detection;
- pre/post-retraction citation trajectories and post-retraction persistence;
- notice accessibility / paywall patterns;
- robustness to DOI availability, multi-country counting rules, field mapping and high-volume event exclusions.

## Non-negotiable interpretation rules

- Retraction ≠ proven misconduct.
- Country/institution affiliation ≠ responsibility.
- A citation ≠ endorsement.
- Retraction counts ≠ retraction rates.
- RWDB correction / expression-of-concern records are not treated as population-complete.
- Multi-label reasons are not forced into a single “main cause” unless a separately validated rule is frozen first.

See `process/RESEARCH_PLAN.md`.
