# ARIS4C021 · Condition Matrix v0 Contract

## Separation of layers

CASE_UNIVERSE_IDENTITY_V1.csv answers only: **which 139 cases belong to the historical Williams frame?**

CONDITION_MATRIX_V0.csv answers: **what evidence do we currently have for the six conditions under two coding tracks?**

The two layers must not be conflated.

## Tracks

### R · replication
Reconstruct Williams 2016 as actually coded:
- historical source vintages;
- retrospective whole-case rules where Williams used them;
- documented qualitative/manual judgments.

### M · modern reproducible
Recode the same historical cases using:
- version-pinned machine-readable inputs;
- deterministic transformations;
- explicit pre-onset timing wherever possible.

R and M may disagree. That disagreement is an intended robustness result.

## Cell contract

Each condition/track has:
- value: 0 / 1 / blank;
- status;
- source;
- note.

Allowed status:
- SOURCE_EXACT
- SOURCE_DERIVED
- AUTHOR_RECONSTRUCTED
- PUBLISHED_CASE_CLUE
- UNRESOLVED
- NOT_APPLICABLE

## Anti-circularity rule

Published Williams:
- condition margins;
- QCA solution formulas;
- case coverage;
- false positives/negatives

are **validation targets, not imputation sources**.

A missing A/P/W/I/S/E cell may not be filled merely because doing so would make the published formula or marginal totals match.

Published case-level discussion may be stored separately as a clue and used to prioritize source recovery. If later used as a cell value, it must be explicitly labelled PUBLISHED_CASE_CLUE and excluded from any supposedly independent replication validation.

## Freeze rule

CONDITION_MATRIX_V1.csv may be created only after:
1. the 139 identities remain stable;
2. Williams coding protocol is frozen;
3. each nonblank R cell has provenance;
4. each nonblank M cell is reproducible from version-pinned inputs;
5. unresolved cells and manual judgments are quantified;
6. condition margins are compared with published targets without tuning values to force agreement.
