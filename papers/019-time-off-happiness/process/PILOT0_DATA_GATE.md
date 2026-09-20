# ARIS4C019 · Pilot-0 Data Gate

> Auto-generated from official source downloads. This reports feasibility only; it does not estimate a treatment effect.

- WHR annual panel: **2199 country-year observations**, **165 countries/territories**, 2005–2022.
- Leave-reform candidates registered: **30**.
- Candidates with >=2 observed pre and >=2 observed post WHR years in a ±4-year window: **17**.
- Of those, candidates whose treatment year is already verified: **4**.
- World Bank statutory-leave panel: **3434 rows**, **202 economies**, EW2004–EW2020.
- Reform candidates whose World Bank panel change matches the registered direction and WHR coverage passes: **11**.
- Candidates passing WHR coverage + verified timing + World Bank direction validation: **2**.

## Interpretation

Coverage PASS means an event is empirically inspectable. It does **not** establish parallel trends, no anticipation, clean treatment isolation, or causality.

## Verified-year candidates that pass coverage

| Country | Effective year | Direction | WB Δ avg leave | n pre | n post |
|---|---:|---|---:|---:|---:|
| Taiwan, China | 2017 | increase | 0.67 | 4 | 5 |
| Canada | 2019 | increase | 3.33 | 4 | 4 |

## Next gate

1. verify exact legal effective dates for structurally valid events still marked provisional;
2. freeze event inclusion and crisis/scope flags without reference to post-treatment happiness changes;
3. create the no-outcome-look event-study design manifest;
4. only then run event-study / staggered-DiD diagnostics.
