# Closest Competitor Gap Analysis · 2026-09-24

## Why this document exists

A 2026 preprint substantially overlaps the original ARIS4C-020 motivation:

**Venturini S, Urbinati A, Gallo P. _The Retraction Epidemic in Science Across Publishers, Fields, and Countries._ arXiv:2604.02302.**

It is close enough that ARIS4C-020 must treat denominator-normalized global retraction incidence as **prior art**, not as its standalone novelty claim.

## What Venturini et al. already do

Based on the inspected full text:

- OpenAlex October-2025 snapshot;
- >107 million works, publication years 1992–2021;
- ~31,000 works marked retracted through the OpenAlex boolean flag;
- publication-cohort incidence rather than retraction-year raw counts;
- per-paper and per-active-author incidence;
- field/domain comparisons;
- fractional country attribution;
- publisher comparisons;
- negative-binomial exposure-adjusted GLMs;
- constant / linear / exponential incidence model comparison;
- publication-to-retraction lag analysis;
- pre-2021 cutoff to reduce right censoring;
- concentration/Gini analyses across countries and publishers;
- explicit discussion of detection, metadata, conference-coverage and retraction-flag limitations.

Therefore the following are **not sufficient novelty claims** for ARIS4C-020:

- “we normalize retractions by publication volume”;
- “we compare countries/fields/publishers”;
- “we use fractional country weights”;
- “we model temporal retraction incidence”;
- “we study publication-to-retraction lag”;
- “we note that raw counts are misleading.”

## What ARIS4C-020 must add

### 1. Direct event-spine reconstruction instead of OpenAlex-flag-defined cases

ARIS4C-020 begins with the complete frozen RWDB event file:
- 72,606 total rows;
- 67,197 primary Retraction events;
- 61,155 unique usable original DOI.

OpenAlex is an enrichment/denominator layer, never the authority defining the primary outcome.

This matters because:
- Hauschke & Nazarovets (2025; DOI 10.1177/01655515251322478) independently found incorrect OpenAlex retraction markings;
- our own shard-0 feasibility run contains RWDB-linked works with `OpenAlex.is_retracted=false`;
- OpenAlex can return multiple Work candidates for one DOI.

Primary contribution: quantify and propagate **cross-database concordance/discordance** rather than silently accepting one database flag.

### 2. Event → work provenance

RWDB is event-oriented. ARIS4C-020 retains all Record IDs while building a unique scholarly-work layer.

This permits:
- multiple notices for one original work;
- earliest formal Retraction event;
- union of reasons/subjects/countries with source-row provenance;
- no inflation of publication-risk numerators by repeated event records.

The frozen snapshot already contains repeated original DOI values with maximum multiplicity 145.

### 3. Native multi-label Reason ecology

RWDB's reason vocabulary is not a mutually exclusive cause variable.

ARIS4C-020 preserves:
- atomic official labels;
- label prevalence;
- co-occurrence network;
- six orthogonal analytical facets;
- vocabulary drift between observed snapshot and Appendix-B reference;
- procedural/notice labels separately from substantive failure mechanisms.

This is central rather than a descriptive appendix.

### 4. Mass-event decomposition as an interpretation guard

Headline estimates are repeated under pre-frozen leave-cluster-out sensitivity sets:
- largest publisher-year cluster excluded;
- all threshold-defined mass clusters excluded;
- Paper Mill excluded;
- Paper Mill + peer-review-compromise labels excluded;
- publisher-year contribution caps.

The target is not merely to measure concentration, but to ask whether comparative conclusions survive concentrated editorial events.

### 5. Explicit time-to-event framework

Rather than relying only on a historical publication-year cutoff, ARIS4C-020 builds the non-retracted publication universe and treats unretracted works as administratively right-censored.

Primary options:
- cumulative incidence at fixed horizons;
- piecewise/discrete hazard;
- Cox only if proportionality is defensible;
- fixed-follow-up/mature-cohort sensitivity.

The pre-2021-style cutoff remains a sensitivity benchmark, not the sole censoring solution.

### 6. All-field citation afterlife in the same work spine

The same deduplicated work IDs are used to estimate:
- pre/post-retraction citation rates;
- share of lifetime citations after retraction;
- first post-retraction citation delay;
- persistence at fixed horizons;
- matched non-retracted control trajectories.

The incidence paper mentions continuing citations as motivation but citation afterlife is not its primary empirical package.

### 7. Auditability across database versions

ARIS4C-020 freezes:
- RWDB file hash and generation date;
- OpenAlex corpus choice (`core`);
- 0/1/N DOI match candidates;
- unmatched/ambiguous cases;
- ontology version;
- denominator definition;
- mass-event sensitivity set.

The result should be a reproducible data/audit system, not only a one-shot bibliometric estimate.

## Other close prior work

### Oppenlaender 2026 · arXiv:2602.19197
**How Ten Publishers Retract Research**
- 46,087 RWDB retractions across ten major publishers;
- rates, reasons, temporal and geographic comparisons;
- further removes “publisher-normalized rates/reasons” as a standalone novelty claim.

### Fletcher & Stevenson 2025 · DOI 10.1186/s41073-025-00168-w
- RWDB × OpenAlex case-control construction;
- matched non-retracted works and explicit eligibility filters;
- useful precedent for controls, but prediction is the target rather than global event ecology.

### Hauschke & Nazarovets 2025 · DOI 10.1177/01655515251322478
- directly demonstrates that OpenAlex retraction marking is not perfectly reliable;
- motivates the concordance layer.

## Revised novelty statement

The working novelty claim is **not** “the first global normalized study of retractions.”

A defensible target is:

> A versioned, event-to-work reconstruction of the complete current Retraction Watch corpus that explicitly audits cross-database retraction concordance, models the native multi-label reason ecology and concentrated cleanup events, handles retraction timing through a true right-censored publication universe, and links the same work spine to post-retraction citation trajectories.

This claim remains provisional until the formal literature screen is complete.
