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

## Prior-method comparison

Fletcher & Stevenson (2025; DOI 10.1186/s41073-025-00168-w) used a prediction-oriented RWDB × OpenAlex case-control design with narrower eligibility rules, including selected RWDB article types and OpenAlex journal/conference plus article/review constraints. Those rules are useful as a sensitivity benchmark but are **not adopted automatically** here because ARIS4C-020 estimates all-discipline retraction ecology rather than classifier performance.

Hauschke & Nazarovets (2025; DOI 10.1177/01655515251322478) further shows that OpenAlex's retraction marking can disagree with true retraction status. Consequently, work-type and retraction-status QA are separate gates.

## Deterministic anomaly QA protocol

For every candidate non-primary type (`retraction`, `erratum`, `reference-entry`, `supplementary-materials`, `paratext`, `other`):

1. sort query DOI by `SHA256("ARIS4C020-WORKTYPE:" + doi)`;
2. inspect up to 50 DOI per type, or all if fewer;
3. compare RWDB original title/date/DOI with every OpenAlex candidate title/date/type;
4. label outcome as `ORIGINAL_CORRECT_TYPE`, `OPENALEX_TYPE_MISCLASSIFICATION`, `NOTICE_ORIGINAL_CONFUSION`, `MULTI_CANDIDATE_AMBIGUOUS`, `RWDB_IDENTITY_ISSUE`, or `OTHER_LEGITIMATE_TYPE`;
5. freeze eligible types only after the audit table is complete.

No anomalous type is excluded solely because its string looks non-research-like.
