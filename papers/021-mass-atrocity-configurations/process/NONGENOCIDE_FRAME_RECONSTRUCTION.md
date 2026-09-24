# ARIS4C021 · Williams Non-Genocide Frame Reconstruction v0.1

Date: 2026-09-24
Status: candidate reconstruction; count parity achieved

## Published rule

Williams states that non-genocides are:
- other cases in the PITF consolidated list;
- adverse regime changes, ethnic wars or revolutions / consolidated political-instability cases;
- not coded as genocide;
- in the 1955–1998 study window.

The paper reports **99 non-genocide events** in the analytic table, although the introduction once says “100 non-genocidal incidents.” The abstract and Table 1 use 139 total cases = 40 genocide + 99 non-genocide.

## Reconstruction

Using the official PITF Consolidated Case List 2018 and selecting the pre-modern historical events that:
1. begin in 1955–1998 inclusive;
2. are political-instability events represented as adverse regime change, ethnic war, revolutionary war, or consolidated/complex cases;
3. do not contain a GEN-coded episode in the focal consolidated event;

produces exactly **99 candidate non-genocide cases**.

The candidate rows are frozen in:

data/WILLIAMS_NONGENOCIDE_CANDIDATE_V0.csv

## Why this is promising

The exact 99-case count is independently implied by:
- Williams Table 1;
- Williams's case-selection prose;
- the 40 + 99 = 139 total stated throughout the article.

The reconstructed frame also retains high-risk political-instability controls rather than substituting peaceful country-years.

## Why this is not yet called exact replication

Williams worked from an earlier PITF consolidated list available by 2013 / updated through 2006, while the public official list used here is the 2018 revision.

The 2018 codebook notes that historical cases have been reviewed and some cases have been added, deleted or modified over time.

Therefore the 99-count match is a **strong candidate reconstruction**, not proof that every case boundary is byte-for-byte identical to Williams's original input.

## Exact-replication gate

Upgrade V0 -> V1 only after:
- recovering the historical PITF list/version closest to Williams's coding date, or an original Williams case matrix;
- comparing every case ID and episode boundary;
- resolving any version differences;
- reproducing Williams's six marginal condition counts and published QCA solution.

## Internal paper discrepancy

Williams introduction: 40 genocide + 100 non-genocidal incidents.
Williams Table 1 / analysis: 40 genocide + 99 non-genocide = 139.

ARIS4C021 treats 99 as the analytic target because it is consistent with Table 1 and the repeated 139 total.
