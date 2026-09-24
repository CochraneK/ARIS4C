# ARIS4C021 · Harff Case-Level Replication Route v0.1

Date: 2026-09-24

## Why this route matters

Hainmueller & Hazlett (Political Analysis, 2014; DOI 10.1093/pan/mpt019) reanalyzed the Harff 2003 structural genocide model using the same N=126 political-instability events.

Their paper states that the Harff replication data contain:
- outcome: genocide onset;
- PriorUpheaval: continuous prior upheaval;
- PriorGen: prior genocide dummy;
- IdeologicalChar: ideological character of ruling elite;
- Autoc: autocracy dummy;
- EthnicChar: ethnic character of ruling elite;
- TradeOpen: trade openness, logged in the replication model.

This is potentially a much better route to the Harff case-level matrix than manually reconstructing P/I/S.

## Replication-data provenance

The paper explicitly states that replication materials were deposited in the Political Analysis Dataverse.

Historical landing reference from the paper:
http://dvn.iq.harvard.edu/dvn/dv/pan

The old Dataverse interface has moved/changed, and a stable modern dataset DOI has not yet been recovered in the current search session.

## Important substantive result

Hainmueller & Hazlett report that:
- the original linear/logit-style specification finds a positive prior-upheaval association;
- the continuous PriorUpheaval variable is strongly right-skewed;
- after logging prior upheaval, that apparent effect essentially disappears in their flexible analysis.

This does not automatically invalidate Harff. It does show that the political-upheaval result is sensitive to functional-form assumptions.

## Consequence for ARIS4C021

Add a function-form replication layer before calling a condition robust:

1. exact Harff/Williams coding;
2. continuous-variable reconstruction where source data permit;
3. skew-aware transformations specified before outcome comparison;
4. flexible nonlinear benchmark (e.g. spline/GAM/KRLS-like model);
5. compare whether a condition is:
   - set-theoretically important;
   - statistically associated under the original form;
   - robust to continuous/nonlinear specification.

## Recovery priority

1. Recover Hainmueller/Hazlett Political Analysis replication archive.
2. Inspect variable names, row IDs, and source provenance.
3. Compare its 126 Harff rows against ARIS4C021's reconstructed historical case universe.
4. Use it as a Harff replication source only after verifying it is the authors' deposited replication data, not a derivative copy.
5. Never silently map the 126-row Harff frame onto the 139-row Williams frame; preserve both universes and crosswalk them.

## New scientific opportunity

Paper 021 can distinguish three kinds of “importance” that earlier work often mixes:

- **configurational importance**: QCA/CNA necessity/sufficiency;
- **functional-form robustness**: whether regression/nonlinear models retain the association;
- **temporal validity**: whether the condition is observable before onset.

A condition should not receive a strong “periodic-table” role merely because it succeeds on one of these dimensions.
