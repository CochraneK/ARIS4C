# Motif-Family Source Bundle Contract · v0.1

## Why this layer exists
Surviving ancient corpora rarely justify the universal claim that a whole tradition lacks a motif. ARIS4C-023 therefore separates the historical tradition-time unit from a frozen motif-family source bundle.

## Semantics
Within a bundle marked negative_closed=true:
- present = motif occurs in at least one eligible frozen passage;
- absent = every eligible frozen passage in the bundle was assessed absent;
- uncertain = at least one eligible passage is uncertain and none is present;
- not_observed = evidence is unavailable/excluded.

An absent bundle cell means only 'absent from this frozen source bundle'. It must never be paraphrased as 'this civilization/tradition never had the motif'.

## Bundle types
- closed_frozen_bundle: a bounded focal narrative/passage is the explicit unit.
- closed_selected_bundle: multiple predeclared passages form the bundle; inference is limited to that selection.
- partial_fragmentary / partial_philological: positives may be used, negatives remain not_observed.
- later_comparator: excluded from in-window confirmatory analysis.

## Similarity pilot
Pairwise Jaccard is allowed only among bundles in the same motif family with negative_closed=true. This is descriptive source-bundle similarity, not civilization similarity and not evidence of borrowing.
