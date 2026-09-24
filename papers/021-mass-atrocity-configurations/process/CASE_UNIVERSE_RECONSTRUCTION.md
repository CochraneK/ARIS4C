# ARIS4C021 · Case-universe reconstruction v0.2

## What is now reproduced

Williams 2016 reports **40 genocide cases + 99 non-genocide PITF instability cases = 139**.

A public PITF-2014 transformation in the Early Warning Project replication repository reproduces **exactly 40 geno-/politicide onset country-years for 1955–1998**, matching the Williams positive-case count and onset list.

Using the PITF consolidation rule — merge overlapping instability events, or events separated by no more than five years — on the same public panel gives **102 non-genocide consolidated episodes beginning 1955–1998**.

Therefore:

- published Williams controls: **99**
- PITF-2014-lineage reconstructed candidates: **102**
- unresolved difference: **3 cases**

## Interpretation

This is now a **version-lineage gap**, not a free modeling choice.

Williams cites PITF/Harff data accessed on **2012-11-12**. The available public machine-readable reconstruction is PITF 2014. Cases may have been added, re-dated, retyped or retrospectively consolidated between the 2012-era source and 2014.

ARIS4C021 will **not delete three cases merely to force N=99**.

## Current canonical statuses

- Williams 40 positive seed: literature-derived and independently cross-checked.
- 102 negative candidates: **candidate_not_canonical**.
- Final 99 negative controls: **not frozen**.
- CONDITION_MATRIX_V1.csv: **not frozen**.

## Resolution strategy

1. locate a 2012-era PITF consolidated case list / problem-set snapshot;
2. compare it directly with the 102 candidate list;
3. identify the exact three version-added/reclassified cases;
4. record case-level provenance;
5. only then freeze CASE_UNIVERSE_V1.

If an exact 2012 snapshot cannot be recovered, the paper will keep:
- a published-N reconstruction track;
- a transparent PITF-2014 sensitivity track;
rather than pretending the historical list is known exactly.

## Strong validation clue

Williams's nine published false-positive cases all correspond to episodes in the 102-case candidate universe. This supports, but does not prove, the reconstruction lineage.
