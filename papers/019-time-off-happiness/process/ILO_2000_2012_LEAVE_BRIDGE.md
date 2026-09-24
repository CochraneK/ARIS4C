# ARIS4C019 · ILO 2000→2012 statutory-leave bridge

**Date:** 2026-09-24  
**Purpose:** convert the late-1990s NATLEX snapshot and 2012 TRAVAIL cross-section into a conservative cross-time legal-change screen.

## Overlap

- 2000/NATLEX frame: 41 countries
- matched to 2012 ILO/TRAVAIL: **37**
- unmatched: **4** — Albania, Azerbaijan, Kazakhstan, Poland
- matched rows with **high-confidence** five-day approximation in 2000 and exact 2012 value: **15**

## Three-week threshold transitions

- >=3weeks->>=3weeks: **21**
- <3weeks->>=3weeks: **3**
- not_specified-><3weeks: **1**
- <3weeks-><3weeks: **11**
- >=3weeks-><3weeks: **1**

### Upgrades across the three-week threshold
- Bulgaria: 14 working days → 20 (2012 five-day-workweek basis)
- El Salvador: 15 days → 15 (2012 five-day-workweek basis)
- Sudan: 20 days → 17 (2012 five-day-workweek basis)

### Apparent downward threshold crossing — rejected after primary-law QA
- Nicaragua: 15 consecutive days every six months (30 days/year) → ILO-2012 standardized value 10.
- **Disposition: source_conflict_not_reform.** NORMLEX/CEACR documents Labour Code Article 76 as 15 paid days per six months in both 1998 and 2005, so no legal decrease is accepted. citeturn121965search1turn121965search0

Threshold crossings are only screening candidates; primary national law controls reform acceptance. The two ILO snapshots differ in reference date and harmonization method; primary national law is required before treatment timing.

## High-confidence approximate changes >=3 days

| country | approx 2000 (5-day) | 2012 | delta |
|---|---:|---:|---:|
| Nicaragua | 21 | 10 | -11 · **REJECT source conflict** |
| United Kingdom | 20 | 28 | +8 |
| Slovakia | 15 | 20 | +5 |
| Algeria | 21 corrected | 21 | 0 · **REJECT harmonization artifact** |
| Mali | 21 corrected | 21 | 0 · **REJECT harmonization artifact** |
| Namibia | 17 | 20 | +3 · **VERIFIED reform, effective 2008-11-01** |

These are a **primary-law verification queue**. They are not outcome-tested selections.

## Interpretation rule

This bridge is superior to comparing arbitrary cross-source numbers because:
1. both endpoints come from ILO legal-data products;
2. the 2000 source preserves the original legal expression;
3. the 2012 source provides a standardized five-day-workweek measure;
4. approximation confidence is explicit.

But it is still not a causal panel. A country enters the reform inventory only after the national statute/amendment and effective date confirm the entitlement change.

Canonical file: `data/ilo_2000_2012_leave_bridge.csv`.


## Primary-law adjudication

- **Bulgaria 2001:** verified; 14 working days → minimum 20 working days, effective 31 Mar 2001. citeturn115033search1
- **Slovakia 2002:** verified; basic minimum 3 weeks → at least 4 weeks, effective 1 Apr 2002. citeturn673653search1turn163090view0
- **Great Britain 2007/2009:** verified staged increase 4 → 4.8 → 5.6 weeks / max 28 days, but explicitly public-holiday-linked. citeturn397223view1turn298580search1
- **Nicaragua:** rejected as a source inconsistency rather than a reform. citeturn121965search1turn121965search0

See `process/HISTORICAL_REFORM_VERIFICATION_GATE_V1.md`.


## Algeria/Mali approximation correction

The original screening bridge incorrectly converted both 30-day rules as if they were six-day-workweek working days.

- Algeria's underlying law specifies up to **30 calendar days**; five-day equivalent ≈21.
- Mali L.151 specifies **30 days including non-working days**; five-day equivalent ≈21.

The machine bridge has been corrected from 25→21 for both. Their apparent -4-day changes are deleted from the reform queue.

Namibia remains a true legal change: 24 consecutive days under the 1992 Act → four consecutive weeks under the 2007 Act, effective 1 Nov 2008.
