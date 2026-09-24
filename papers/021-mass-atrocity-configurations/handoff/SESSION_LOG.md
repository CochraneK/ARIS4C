# ARIS4C021 · Session log

## 2026-09-24 · Bootstrap

Created the project scaffold, literature position, research plan, condition ontology, source inventory and continuity package. No empirical outcome analysis has been run.


## 2026-09-24 · Multimethod + Phase-1 source freeze

- Reframed 021 from QCA-centered to method-neutral multimethod research.
- Frozen Phase-1 Harff-style baseline + QCA + CNA on the same historical matrix.
- Deferred NCA to continuous/ordinal modern indicators; reserved event-history, rare-event prediction and process tracing for later layers.
- Verified official PITF 2018 landing page, codebook, consolidated case list and GenoPoliticide XLS endpoint.
- Recorded the historical-series limitation: PITF GenoPoliticide is a replication source, not a continuously updated modern outcome.
- Added deterministic PITF acquisition/hash script and Phase-1 analytic matrix contract.
- Current runtime could not retrieve the legacy XLS binary; no unofficial mirror was substituted.


## 2026-09-24 · Positive-case cross-check

- Recovered IBM's transformed SystemicPeace genocide indicators from a pinned public commit.
- Verified all 40/40 Williams positive analysis cases have overlapping annual DEATHMAG>0 observations.
- 33/40 match the full published episode span year-by-year; 7/40 contain zero years inside a broader episode.
- Frozen the rule that episode boundaries must come from published/source case definitions rather than naïve runs of positive annual death-magnitude values.


## 2026-09-24 · Candidate 139-case universe and condition-recovery gate

- Materialized CASE_UNIVERSE_CANDIDATE_V0.csv: 40 Williams positive cases + 99 high-risk PITF non-genocide controls = 139.
- Positive-case cross-check: 40/40 overlap transformed PITF annual DEATHMAG; 33/40 have full annual positive coverage, confirming episode boundaries must remain distinct from annual severity.
- Reconstructed 99 controls from the published Williams rule and official PITF consolidated case list; exact count parity achieved, but historical-list version reconciliation remains required.
- Frozen machine-readable Harff/Williams replication targets and validators.
- Located the exact official UCDP/PRIO v4-2012 download endpoint used by Williams for W.
- Located an independent 2014 USHMM/Jay Ulfelder replication script using p4v2012.xls and defining the Harff autocracy indicator as Polity <= 0 (valid -10..10 range).
- Added CONDITION_SOURCE_CROSSWALK.md and acquisition tooling for A/W/E.

## 2026-09-24 · 139-case identity lock + coding protocol

- Resolved the 102-vs-99 control discrepancy without outcome/condition tuning.
- Identified three left-truncation artifacts: Colombia began 1948, Cuba 1952, Iran 1953; the 1955 annual-panel boundary falsely made them appear as new controls.
- Frozen WILLIAMS_NEGATIVE_CASES_IDENTITY_V1.csv and combined CASE_UNIVERSE_IDENTITY_V1.csv at 40 positives + 99 controls.
- Recovered Williams's published coding rules for A/P/W/I/S/E from the full article.
- Explicitly marked the A threshold/override rule as under-specified in the paper rather than inventing a cutoff.
- Confirmed P and W use whole-case information in the historical procedure, motivating separate replication and time-safe tracks.
- Confirmed I includes Williams qualitative coding and E uses a 33% trade-openness threshold.
- Preserved the E count inconsistency: Table cells 18+22=40 while prose reports 41.
- Materialized CONDITION_MATRIX_V0.csv with R/M tracks; all unsupported condition values remain blank + UNRESOLVED.
- Added an anti-circularity rule preventing published margins/QCA solutions from being used to impute missing input cells.
