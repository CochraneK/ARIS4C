# ARIS4C021 · Control-Frame Reconstruction Gate v0.2

Date: 2026-09-24
Status: **99 control identities reconstructed; exact source-vintage dates still under audit**

## Published Williams target

Williams 2016 uses:
- 40 genocide episodes;
- 99 non-genocide political-instability events;
- 139 total analytic cases;
- a historical frame ending in 1998.

The two outcome groups are not a simple binary split of one later consolidated table. The positive side is a genocide-episode list; the negative side is the set of other qualifying PITF political-instability events.

## Why the PITF 2018 row count was misleading

A first mechanical pass over the later PITF 2018 consolidated table produced 103 pre-1999 rows without a GEN marker. That comparison was useful as a warning about source drift, but it was not the correct reconstruction rule because Williams's 40 positives are episode-level genocide cases rather than one-to-one consolidated rows.

The reconstruction therefore moved back toward the source generation Williams actually used.

## Williams-era reconstruction

The old George Mason / SCIP consolidated-event page reflects the PITF source generation current through roughly 2006 and exposes the historical adverse-regime-change / ethnic-war / revolutionary-war frame used by the later Williams analysis.

After:
1. retaining qualifying 1955–1998 political-instability events;
2. excluding events used as genocide positives;
3. correcting the page's duplicated Jordan/Kenya rendering artifact; and
4. restoring Djibouti 1991–1994 from PITF 2010-era evidence,

the reconstructed control universe contains **exactly 99 unique identities**.

Canonical identity file:
`data/WILLIAMS_CONTROL_IDENTITIES_V1.csv`

## Important source artefacts / uncertainties

### Jordan / Kenya HTML artefact

The old web rendering places the Jordan 1970–1971 Revolutionary War description under Kenya as well. Later official PITF tables show this second row is a continuation of Jordan with a blank country cell, followed by Kenya's actual 1964 and 1991 events.

Rule: do not create a fictitious "Kenya 1970" control.

### Djibouti 1991–1994

Djibouti is not visible in the currently rendered old SCIP page, but contemporaneous literature citing the PITF **2010** Consolidated Problem Set lists Djibouti 11/1991–6/1994, and later PITF releases preserve the event.

Rule: include Djibouti in the 99-control identity universe and keep its provenance explicit.

### Cross-version date drift

At least these identities show begin-date differences across PITF vintages:
- Colombia second Revolutionary War;
- Jordan 1957 Regime Change;
- Nicaragua 1978 Complex;
- Peru 1962 Regime Change.

Identity is stable, but the Williams-era first-year date can matter for condition coding.

Rule: identity membership is frozen; exact timing remains provisional until the closest source snapshot is recovered.

## Hard gate

The 139-case identity frame can now be frozen, but the **six-condition matrix cannot yet be called an exact Williams reconstruction**.

Before CONDITION_MATRIX_V1 is frozen:
- reconcile the flagged source-vintage dates;
- recover or reconstruct A/P/W/I/S/E with field-level provenance;
- pass published marginal-count checks;
- pass published path-coverage / consistency checks;
- preserve exact-replication versus pre-onset/time-safe coding separately.

No case may be removed or recoded because it improves model fit.


## 2026-09-24 · Cuba vs Djibouti boundary audit

This membership ambiguity is now resolved for the v1 identity frame.

Evidence:
- a 2012 publication explicitly cites the PITF Consolidated Problem Set **version 2010** and lists Djibouti as an Ethnic War from 11/1991 to 6/1994;
- later official PITF tables list both Cuba (Complex, 3/1952–12/1961) and Djibouti (Ethnic War, 11/1991–6/1994);
- Williams defines the analytic material as PITF cases in the 1955–1998 frame and states that independent-condition values are selected from the first year of the focal genocide/non-genocide conflict where possible.

Decision:
- retain DJI_1991;
- exclude Cuba's 1952-start consolidated episode from the Williams v1 control identity universe;
- do not treat Cuba's post-1955 subcomponents as a new standalone control unless an exact Williams-era row-level source proves that Williams split the consolidated episode.

This decision is based on source-frame reconstruction, not on whether either choice improves QCA fit.
