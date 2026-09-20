# ARIS4C019 · Pilot-0 Data Gate

> Auto-generated from official source downloads. This reports feasibility only; it does not estimate a treatment effect.

- WHR annual panel: **2199 country-year observations**, **165 countries/territories**, 2005–2022.
- Leave-reform candidates registered: **30**.
- Candidates with >=2 observed pre and >=2 observed post WHR years in a ±4-year window: **17**.
- Of those, candidates whose treatment year is already verified: **10**.
- World Bank statutory-leave panel: **3434 rows**, **202 economies**, EW2004–EW2020.
- Reform candidates whose World Bank panel change matches the registered direction and WHR coverage passes: **13**.
- Freeze-eligible legal events (verified timing + WHR coverage): **10**.
- Tier A, additionally corroborated by the World Bank panel: **9**.
- Tier B, legally verified but not corroborated by the World Bank historical panel: **1**.
- All World Bank annual-leave jumps discovered: **44**; unregistered jumps with usable WHR coverage awaiting legal verification: **11**.

## Interpretation

Coverage PASS means an event is empirically inspectable. It does **not** establish parallel trends, no anticipation, clean treatment isolation, or causality.

## Verified legal events that pass coverage

| Tier | Country | Legal effective date | First full post year | Direction | WB Δ avg leave | n pre | n post | Primary | Flags |
|---|---|---|---:|---|---:|---:|---:|---|---|
| A_corroborated | China | 2008-01-01 | 2008 | introduced | 6.67 | 2 | 5 | True | global_financial_crisis_window |
| A_corroborated | Croatia | 2010-01-01 | 2010 | increase | 2.00 | 2 | 5 | True | global_financial_crisis_window |
| A_corroborated | Kosovo | 2010-12-16 | 2011 | increase | 5.00 | 3 | 4 | True |  |
| A_corroborated | Kuwait | 2010-02-21 | 2011 | increase | 11.33 | 2 | 4 | True |  |
| A_corroborated | Bahrain | 2012-09-02 | 2013 | increase | 11.67 | 3 | 4 | True |  |
| A_corroborated | Taiwan, China | 2017-01-01 | 2017 | increase | 0.67 | 4 | 5 | True |  |
| A_corroborated | Lithuania | 2017-07-01 | 2018 | changed_unspecified | 0.33 | 4 | 4 | False | broad_labour_code_package |
| A_corroborated | Luxembourg | 2019-01-01 | 2019 | increase | 1.00 | 4 | 2 | True | covid_overlap_post_window |
| A_corroborated | Canada | 2019-09-01 | 2020 | increase | 3.33 | 4 | 3 | True | covid_overlap_post_window;federal_jurisdiction_only |
| B_legal_only | United Kingdom | 2009-04-01 | 2010 | increase | 0.00 | 3 | 4 | False | global_financial_crisis_window;multi_stage_reform |

## Next gate

1. continue exact-date verification for Tier-C candidates with good WHR coverage;
2. keep Tier A as the primary candidate pool and Tier B as legally verified sensitivity evidence;
3. freeze estimator/control rules without inspecting post-treatment Life Ladder changes;
4. only then run event-study / staggered-DiD diagnostics.
