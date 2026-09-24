# G5 INDEPENDENT VALIDATION PROTOCOL · v0.2

## Frozen packet

Primary validation packet: **190 judgments**
- flood: 7 bundles × 9 motifs = 63
- anthropogony: 5 × 11 = 55
- divine conflict: 8 × 9 = 72

The two blank coder CSVs are byte-identical at freeze.

## Required independent streams

### H · human / domain-informed coder
A genuinely independent human coder trained on the written codebook, not on Pilot answers.
Target: all 190 judgments.

If one person cannot responsibly assess source-language/translation issues across all traditions, use:
- one trained general coder for the full packet;
- source-domain spot reviewers for high-risk bundles (Hurrian/Hittite, Ugaritic, Egyptian, Vedic, Chinese) before final adjudication.

### M · external model coder
A genuinely separate provider/model/session with no project memory.
Target: all 190 judgments.

This is a robustness stream, not a substitute for H.

## Minimum completeness
- H: 100% states or explicit `not_observed` where evidence is inaccessible.
- M: 100% states or explicit `not_observed`.
- blanks are not valid completed responses.

## Reliability gate

Before adjudication:
- four-state raw agreement >= 0.80 overall;
- binary present/absent Cohen kappa >= 0.70;
- binary Gwet AC1 >= 0.75;
- each primary family raw agreement >= 0.75;
- no single unresolved definition boundary accounts for >10% of all packet rows.

Because prevalence may distort kappa, all coefficients are reported; none is silently discarded.

## Failure rule

If the gate fails:
- do not adjudicate labels into agreement;
- diagnose disagreement;
- version ontology/source rules to v0.2.1;
- construct a new blinded packet for affected motifs/bundles;
- revalidate.

## Domain-source audit

Any disagreement that depends on:
- source-language semantics,
- fragment reconstruction,
- text-critical/source-layer assignment,
- translation ambiguity,
triggers domain-source review before confirmatory coding freezes.

## Adjudication

Adjudication happens only after H and M files are frozen.
The adjudicator sees:
- both responses,
- rationales,
- source packet,
- codebook,
but not similarity/contact/model outcomes.

All label changes are recorded; original H/M files remain immutable.

## Gate output

G5 PASS requires:
- frozen H file;
- frozen M file;
- reliability JSON;
- disagreement taxonomy;
- domain-source review record for high-risk disagreements;
- adjudicated v0.2 coding table;
- explicit pass/fail decision.
