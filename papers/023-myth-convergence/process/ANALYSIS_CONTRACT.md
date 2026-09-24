# Analysis Contract · ARIS4C-023

## Purpose

Predefine what happens **after** the coding-reliability gate so exploratory choices do not silently become confirmatory evidence.

## 1. Input freeze

No headline similarity/network/phylogenetic result is interpreted until:
- calibration reliability is scored;
- ontology version is frozen;
- source-backed coding table passes `validate_coding.py`;
- all analysis rows record witness scope;
- a dated data manifest/hash is committed.

## 2. Similarity estimand

Primary descriptive pairwise similarity is **Jaccard similarity on PRESENT motifs**, computed only among motifs that are explicitly scorable as PRESENT or ABSENT in both traditions.

Unknown, uncertain and not-observed values are **excluded from the denominator**, never coerced to absence.

Report alongside every similarity:
- number of comparable motifs;
- both-present count;
- asymmetric present/absent counts;
- both-absent count;
- secondary simple-matching similarity.

Pairs below a preregistered minimum comparable-item threshold are not ranked/interpreted.

## 3. Why simple matching is secondary

A sparse motif matrix can make two poorly observed traditions look similar simply because both contain many absences. Jaccard avoids rewarding joint absences, but it still depends on observation quality; therefore coverage diagnostics accompany every heatmap/network edge.

## 4. Contact data

Contact is its own evidence table, not inferred from myth similarity.

Allowed relation families initially:
- direct political incorporation;
- conquest/occupation;
- documented trade;
- migration/settlement;
- bilingual scribal/literary transmission;
- translation/adaptation;
- diplomatic contact;
- geographic adjacency only.

Each edge needs:
- time interval;
- direction if known;
- evidence grade;
- source;
- status: confirmed / plausible / hypothesis / rejected.

**Geographic adjacency alone is never promoted to documented cultural transmission.**

## 5. Temporal overlap

Maintain at least three distinct intervals:
1. cultural/tradition activity;
2. source composition/witness;
3. contact opportunity.

Do not reduce interval uncertainty to a single midpoint for primary inference.

## 6. Analysis order

1. coverage/missingness;
2. motif prevalence;
3. pairwise Jaccard + comparable-N;
4. clustering/MDS as descriptive;
5. phylogenetic signal where tree assumptions fit;
6. contact/dyadic model;
7. temporal diffusion analysis where dates fit;
8. process tracing of selected high-information cases;
9. optional QCA only after all above clarify what a “case” and “outcome” mean.

## 7. QCA trigger

QCA is enabled only if:
- there is a calibrated set-valued outcome with substantive meaning;
- case count/dependence are defensible;
- conditions are not algebraic restatements of the outcome;
- calibration thresholds have external justification;
- sensitivity to thresholds and contradictory rows is reported.

Otherwise the paper remains non-QCA.

## 8. No “most similar civilizations” leaderboard

The project can visualize pairwise similarities, but it will not turn them into a simplistic civilization ranking. Similarity is conditional on corpus, time slice, ontology and observability.
