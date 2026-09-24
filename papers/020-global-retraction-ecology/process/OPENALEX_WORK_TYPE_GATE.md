# OpenAlex Work-Type Concordance Gate · v1

## Why this gate exists

OpenAlex work type and RWDB ArticleType are different vocabularies. In the completed full-match shard 0, OpenAlex classified the matched DOI records as:

- article: 11,589
- conference-paper: 2,563
- retraction: 563
- reference-entry: 147
- review: 130
- book-chapter: 93
- preprint: 18
- erratum: 13
- conference-abstract: 13
- editorial: 11
- book-review: 8
- letter: 4
- book: 3
- other: 2
- supplementary-materials: 1
- paratext: 1

The presence of `type=retraction` among RWDB **OriginalPaperDOI** matches is a concordance signal that must be investigated, not silently filtered.

OpenAlex itself distinguishes a work whose type is a *retraction notice* from the separate `is_retracted` status of a work.

## Freeze

Do not define denominator eligibility from OpenAlex type until all shards complete and anomalous-type QA is run.

### Candidate scholarly denominator set
Likely candidates include:
- article
- review
- conference-paper
- conference-abstract
- book-chapter
- preprint
- letter
- editorial

### Candidate non-primary denominator objects
Require explicit review before exclusion:
- retraction
- erratum
- reference-entry
- supplementary-materials
- paratext
- other

## QA gate

For each anomalous type:
1. draw a deterministic sample;
2. compare RWDB original DOI/title/date with OpenAlex DOI/title/type;
3. determine whether the mismatch is RWDB identity, DOI normalization, OpenAlex classification, notice-vs-original confusion, or legitimate object type;
4. freeze inclusion/exclusion rule only after this audit.

No field/country rate is final before this gate passes.
