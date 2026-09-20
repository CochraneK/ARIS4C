# ARIS4C019 · Pilot-0 Data Gate

> Auto-generated from official source downloads. This reports feasibility only; it does not estimate a treatment effect.

- WHR annual panel: **2199 country-year observations**, **165 countries/territories**, 2005–2022.
- Leave-reform candidates registered: **30**.
- Candidates with >=2 observed pre and >=2 observed post WHR years in a ±4-year window: **17**.
- Of those, candidates whose treatment year is already verified: **4**.

## Interpretation

Coverage PASS means an event is empirically inspectable. It does **not** establish parallel trends, no anticipation, clean treatment isolation, or causality.

## Verified-year candidates that pass coverage

| Country | Effective year | Direction | n pre | n post |
|---|---:|---|---:|---:|
| China | 2008 | introduced | 2 | 5 |
| United Kingdom | 2009 | increase | 3 | 5 |
| Taiwan, China | 2017 | increase | 4 | 5 |
| Canada | 2019 | increase | 4 | 4 |

## Next gate

1. materialize World Bank annual-leave country-year values;
2. verify exact legal effective dates for every retained event;
3. freeze event inclusion without reference to post-treatment happiness changes;
4. only then run event-study / staggered-DiD diagnostics.
