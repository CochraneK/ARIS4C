# Israel original-rule 120-donor reconstruction

**Reconstructed:** 2026-09-23  
**Purpose:** close the reproducibility gap for the pre-frozen `original120_mean` sensitivity reported in the manuscript.

## Rule

The original Pilot-0 donor rule was frozen before Israel's outcome was opened:

1. at least 2 observed Life Ladder years in 2012–2015;
2. at least 2 observed Life Ladder years in 2017–2020;
3. no World Bank annual-leave jump in EW2011–EW2021;
4. no already verified leave treatment in the focal 2012–2020 window;
5. Israel excluded as the treated country.

Applying these rules to the same validated WHR2024 annual panel yields **120 donors**.

The later strict snapshot-clean rule removes five additional countries whose annual-leave category changed between the legacy WORLD snapshot and Equal Futures 2026:

- Egypt
- Ethiopia
- Mexico
- Pakistan
- Uzbekistan

Therefore:

- original-rule pool: **120**
- strict snapshot-clean pool: **115**
- difference: exactly the five countries above

The apparent `Türkiye` / `Turkiye` discrepancy is only Unicode/name normalization and does not change membership.

## Outcome firewall note

This file is a **post-outcome reconstruction of a pre-frozen rule**, not a new donor-selection decision. Membership is derived only from outcome availability and previously frozen legal-contamination rules; no Life Ladder sign or magnitude is used.

Machine-readable list: `data/israel_holdout_donors_original120.csv`.
