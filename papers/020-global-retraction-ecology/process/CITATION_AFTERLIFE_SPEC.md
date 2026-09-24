# Citation Afterlife Specification · v1

## Question

How much scholarly attention persists after a work is formally retracted, and how does that persistence differ by field, retraction reason, publication age, journal/source, and mass-retraction episode?

## Event time

For each unique retracted work:
- t = 0 is the earliest valid RWDB RetractionDate;
- citing works are assigned relative time from the retraction date;
- pre- and post-retraction citation windows are kept separate.

## Primary outcomes

- citations before retraction;
- citations after retraction;
- proportion of lifetime citations received after retraction;
- time to first post-retraction citation;
- annual/monthly post-retraction citation rate;
- citation decay half-life where estimable;
- persistence at 1, 2, 3 and 5 years after retraction.

## Matched control design

For each DOI-linked retracted work, select non-retracted OpenAlex controls matched/coarsened on:
- publication year;
- primary field/topic;
- work type;
- source/journal when feasible;
- pre-event citation level or age-specific citation trajectory.

Controls receive a pseudo-event date matched on publication age.

## Models

Primary options:
- self-controlled pre/post rate model;
- negative-binomial count model with exposure time;
- event-study / interrupted trajectory;
- matched retracted-vs-control difference in citation trajectory.

The model family is chosen after examining overdispersion, zero inflation and time granularity.

## Confounding / censoring

Explicitly handle:
- varying publication-to-retraction lag;
- database indexing delay;
- right censoring for recent retractions;
- highly cited outliers;
- field-specific citation density;
- mass-retraction episodes;
- self-citation sensitivity when authorship data permit.

## Interpretation

A citation is evidence of scholarly attention, not endorsement. Without full citation-context text, “continued citation” must not be described as continued acceptance of the retracted claim.

## Novelty boundary

Recent work has modeled post-retraction citation persistence in restricted disciplinary or national subsets. ARIS4C-020's target is an all-field RWDB-linked citation-afterlife analysis using the shared full-data spine and the same denominator/identity contracts as the rest of the project.

## Acquisition implementation

The OpenAlex Works API supports `filter=cites:<work_id>` for incoming citations and OR filters with `|`. ARIS4C-020 therefore queries batches of retracted target Work IDs and requests each citing work's `referenced_works`, allowing a returned citing work to be assigned back to every target it cites.

Production files:
- `code/openalex_citation_edges.py`: resumable batched edge acquisition;
- `code/summarize_citation_afterlife.py`: target-work pre/post summary.

Only uniquely matched OpenAlex target works enter the first pass. Ambiguous multi-candidate DOI matches remain excluded until identity adjudication.

### Event-time precision

The citing work's publication date is used as the observable bibliographic time of the citation. It is not the date the manuscript was written or submitted.

Primary sensitivity around the retraction boundary:
- same-day citations separated;
- 0–90 days after retraction;
- 91–180 days;
- >180 days.

This prevents a paper already in production when the retraction occurred from being interpreted too strongly as evidence of avoidable post-retraction propagation.
