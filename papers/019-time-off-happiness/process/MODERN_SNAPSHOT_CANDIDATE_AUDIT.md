# ARIS4C019 · Modern Snapshot-Difference Candidate Audit v0.1

**Frozen:** 2026-09-21  
**Purpose:** outcome-blind discovery of possible statutory annual-leave changes between WORLD 2015/16 and Equal Futures 2026 snapshots.

## Source snapshots

- WORLD old map: all 193 UN states, law review as of April 2015, with OECD detail supplemented to September 2016.
- Equal Futures 2026 map/data: all 193 UN states, law review as of January 2026.
- Both maps use the same substantive construct: the **lowest amount of paid annual leave guaranteed to a worker with at least one year of tenure**.
- 2026 public-use ZIP SHA256 observed during audit: `a8b58bc009c810c8e2b88dfd385f8429594562300d8bcc9c994a3954d49d1f05`.
- 2026 `paid_anlv` coding from its data dictionary: 1=no leave; 2=5–9; 3=10–14; 4=15–20; 5=20+.

The snapshot difference is a **candidate-discovery screen only**. A category change is never itself treated as proof of a legal reform.

## Cross-category candidates and triage

| Country | 2015/16 snapshot | 2026 snapshot | Legal/coverage triage | Track-A decision |
|---|---|---|---|---|
| **Israel** | 10–14 | 15–19 | Knesset Annual Leave Law Amendment No.15 is leave-specific; +1 day from 2016-07-01 and second +1 from 2017-01-01; WHR has 4 pre + 4 full-post in frozen window | **ADMIT clean holdout** |
| Mexico | 5–9 | 10–14 | leave-specific 2023 vacation reform; WHR annual panel through 2023 gives only one post year | future holdout |
| Ethiopia | 10–14 | 15–19 | 2019 Labour Proclamation raises first-year annual leave 14→16 working days but is a comprehensive Labour Code | reject leave-specific holdout |
| Pakistan | none | 10–14 | identifiable 2016 leave guarantees are provincial (e.g. Sindh) and embedded in broader shops/employment legislation | reject national clean holdout |
| India | none | 15–19 | four Labour Codes became effective 2025-11-21; broad reform and no usable post-outcome window | future/non-clean |
| Mozambique | 10–14 | 20+ | 2023 Labour Law took effect in 2024; broad labour code and no annual post outcome in WHR2024 | reject current holdout |
| Bosnia and Herzegovina | 15–19 | 20+ | Federation labour code is broad and subnational/entity-specific | reject population-wide clean holdout |
| Uzbekistan | 15–19 | 20+ | new Labour Code effective 2023-04-30, broad reform; transition year is the last available annual outcome year | reject current holdout |
| Egypt | 20+ | 15–19 | comprehensive Labour Law No.14/2025 effective 2025-09-01; no usable annual post outcome | reject current holdout |
| Kiribati | none | 20+ | possible legal introduction but no WHR annual coverage | reject on outcome coverage |
| Tuvalu | none | 10–14 | no WHR annual coverage | reject on outcome coverage |
| Burundi | 15–19 | 20+ | WHR modern coverage too sparse | reject on outcome coverage |
| Somalia | 15–19 | 20+ | WHR observations stop before a usable modern post window | reject on outcome coverage |

Bolivia and Nepal were absent/data-unavailable in the old snapshot but appear in 2026, so they are kept outside the legal-change queue unless an independently dated reform is verified. Namibia remains 20+ in the 2026 raw CSV and is not treated as a change despite crawler/map rendering inconsistency.

## Israel legal identification

Official Knesset materials document that Amendment No.15 directly amended the **Annual Leave Law, 1951**. For workers with up to four years of tenure, the amendment adds two annual-leave days:

- first additional day from **2016-07-01**;
- second additional day from **2017-01-01**.

This is one leave-specific statute with staged implementation, not a broad labour-code rewrite.

### Frozen event clock

- event clock: **2016**
- reference year: **2015**
- 2016: partial-exposure transition year, excluded
- first full treatment: **2017**
- pre: 2012–2015
- post: 2017–2020

No Israel Life Ladder value was inspected to make this admission decision.

## Outcome-blind support gate

Using the original Pilot-0 donor rules:

- raw donors with >=2 observed pre and >=2 observed post: **137**
- clean after nearby World Bank leave-jump and verified-treatment screens: **120**
- stricter clean set after additionally excluding every 2015→2026 snapshot-change country: **115**
- clean-donor >=20 gate: **PASS**

The strict 115-donor list is frozen in `data/israel_holdout_donors.csv`.

## Source anchors

- WORLD 2015/16 annual-leave map: https://www.worldpolicycenter.org/policies/is-paid-annual-leave-available-to-workers
- Equal Futures 2026 annual-leave map: https://equalfutures.org/policies/is-paid-annual-leave-available-to-workers
- Equal Futures 2026 download page/data dictionary: https://equalfutures.org/maps-data/data-download/annual-leave-and-weekly-rest-data-download
- Israel Knesset Amendment No.15: https://main.knesset.gov.il/apps/legislation/main/bills/563603
- Knesset final-approval notice: https://main.knesset.gov.il/News/PressReleases/pages/press080216-0mq.aspx

## Interpretation boundary

Israel is an **independent post-unlock holdout discovery**, not an addition to the original eight-event primary pool. Its effect must be reported separately. It can test whether a cleaner leave-specific reform is directionally compatible with the exploratory eight-event package analysis; it cannot retroactively repair that panel's pretrend or treatment-isolation problems.
