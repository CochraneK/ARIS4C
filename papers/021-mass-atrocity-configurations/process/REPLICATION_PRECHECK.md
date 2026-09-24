# ARIS4C021 · Historical Replication Precheck v0.1

Date: 2026-09-24
Status: frozen before case-level reconstruction

## Purpose

Record internal inconsistencies and temporal-design issues in the published historical targets **before** reconstructing the matrix. These are not reasons to discard the prior work; they define what "exact replication" and "design-hardened sensitivity" must mean.

## 1 · Economic autarky count discrepancy in Williams 2016

Williams Table 1 reports:
- genocide E=1: 18;
- non-genocide E=1: 22;
- therefore table-implied total: 40.

The surrounding prose states that 41 cases are economically autarkic.

Rule:
- retain the table-implied 18/22/40 counts as the primary machine-checkable target;
- record the prose value 41 as an internal source discrepancy;
- do not alter a reconstructed case merely to force either total;
- if the recovered original matrix totals 41, investigate whether Table 1 or the prose contains the typo.

## 2 · Published QCA solution does not pass ARIS4C021's prospective robustness threshold

Published intermediate solution:
- solution coverage = 0.750;
- solution consistency = 0.769.

Path A*S*P:
- consistency = 0.741.

ARIS4C021 independently froze a headline sufficiency target of >=0.80 before reconstructing the historical matrix.

Rule:
- reproduce Williams's published solution using the historical conventions;
- do not lower the >=0.80 threshold to make the historical result "pass";
- describe 0.769 as the published fit, not as a robust sufficient relation under ARIS4C021's stricter criterion;
- distinguish exact-replication success from contemporary evidential interpretation.

## 3 · Autocracy is quasi-necessary, not perfectly necessary

Williams:
- 38/40 genocide cases occur with A=1;
- two genocide cases occur with A=0.

Rule:
- label A as quasi-/near-necessary in the historical sample;
- never call it logically necessary without a stated consistency convention;
- test necessity stability under alternative universes and modern data.

## 4 · Temporal leakage risk in political-upheaval coding

Williams states that explanatory values are selected from the first year of the genocide/non-genocidal conflict where possible.

However, political upheaval P is also coded using:
- the difference between highest and lowest polity values **over the whole conflict**, or
- the maximum Harff upheaval value **during the conflict**.

Those rules can use information after the focal onset.

Rule:
- Track R (replication): reconstruct Williams's published coding exactly where possible.
- Track T (time-safe sensitivity): recompute P using only information observable before or at the frozen prediction date.
- never silently substitute Track T for Track R.

## 5 · Temporal leakage risk in war coding

Williams codes W=1 if the case is labelled as war in **any year of the case** in the UCDP/PRIO armed-conflict data.

This can classify an onset using war information occurring later in the same episode.

Rule:
- Track R reproduces the published any-year coding.
- Track T uses only war status observable before/on the prediction date.
- compare whether key configurations survive.

## 6 · Harff and Williams are related but not identical designs

Harff 2003:
- 35 geno-/politicide problem episodes;
- 91 controls;
- predictor timing framed one year prior to geno-/politicide onset.

Williams 2016:
- 40 genocide cases;
- 99 non-genocide instability cases;
- 1955–1998 frame;
- six crisp-set conditions, including newly operationalized W and modified S/E conventions.

Rule:
Do not call Williams a direct reanalysis of the exact Harff 126-row matrix. It is a related extension/reconstruction with a different N and some different operationalization.

## Scientific opportunity

The first publishable contribution may emerge even if the classic configurations reproduce exactly:

**How much of the classic configurational result survives when the same historical cases are recoded under a strict pre-onset information firewall?**

This is a stronger and more falsifiable question than merely rerunning QCA.
