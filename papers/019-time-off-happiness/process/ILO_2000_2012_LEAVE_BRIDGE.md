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

### Apparent downward threshold crossings
- Nicaragua: 15 consecutive days every six months (30 days per year) → 10

Any threshold crossing is a **candidate**, not yet an accepted reform. The two ILO snapshots differ in reference date and harmonization method; primary national law is required before treatment timing.

## High-confidence approximate changes >=3 days

| country | approx 2000 (5-day) | 2012 | delta |
|---|---:|---:|---:|
| Nicaragua | 21 | 10 | -11 |
| United Kingdom | 20 | 28 | +8 |
| Slovakia | 15 | 20 | +5 |
| Algeria | 25 | 21 | -4 |
| Mali | 25 | 21 | -4 |
| Namibia | 17 | 20 | +3 |

These are a **primary-law verification queue**. They are not outcome-tested selections.

## Interpretation rule

This bridge is superior to comparing arbitrary cross-source numbers because:
1. both endpoints come from ILO legal-data products;
2. the 2000 source preserves the original legal expression;
3. the 2012 source provides a standardized five-day-workweek measure;
4. approximation confidence is explicit.

But it is still not a causal panel. A country enters the reform inventory only after the national statute/amendment and effective date confirm the entitlement change.

Canonical file: `data/ilo_2000_2012_leave_bridge.csv`.
