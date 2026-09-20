# ARIS4C019 · Pilot-0 Data Gate

> Auto-generated from official source downloads. This reports feasibility only; it does not estimate a treatment effect.

- WHR annual panel: **2199 country-year observations**, **165 countries/territories**, 2005–2022.
- Leave-reform candidates registered: **30**.
- Candidates with >=2 observed pre and >=2 observed post WHR years in a ±4-year window: **17**.
- Of those, candidates whose treatment year is already verified: **10**.
- World Bank statutory-leave panel: **3434 rows**, **202 economies**, EW2004–EW2020.
- Reform candidates whose World Bank panel change matches the registered direction and WHR coverage passes: **11**.
- Freeze-eligible legal events (verified timing + WHR coverage): **10**.
- Tier A, additionally corroborated by the World Bank panel: **8**.
- Tier B, legally verified but not corroborated by the World Bank historical panel: **2**.

## Interpretation

Coverage PASS means an event is empirically inspectable. It does **not** establish parallel trends, no anticipation, clean treatment isolation, or causality.

## Verified-year candidates that pass coverage

| Tier | Country | Effective year | Direction | WB Δ avg leave | n pre | n post | Flags |
|---|---|---:|---|---:|---:|---:|---|
| A_corroborated | Croatia | 2010 | increase | 2.00 | 2 | 5 | global_financial_crisis_window |
| A_corroborated | Kosovo | 2010 | increase | 5.00 | 3 | 5 | global_financial_crisis_window |
| A_corroborated | Kuwait | 2010 | increase | 11.33 | 2 | 5 | global_financial_crisis_window |
| A_corroborated | Bahrain | 2012 | increase | 11.67 | 3 | 5 |  |
| A_corroborated | Lithuania | 2017 | changed_unspecified | 0.33 | 4 | 5 | broad_labour_code_package |
| A_corroborated | Taiwan, China | 2017 | increase | 0.67 | 4 | 5 |  |
| A_corroborated | Canada | 2019 | increase | 3.33 | 4 | 4 | covid_overlap_post_window;federal_jurisdiction_only |
| A_corroborated | Luxembourg | 2019 | increase | 1.00 | 4 | 2 | covid_overlap_post_window |
| B_legal_only | China | 2008 | introduced |  | 2 | 5 | world_bank_name_match_missing |
| B_legal_only | United Kingdom | 2009 | increase | 0.00 | 3 | 5 | global_financial_crisis_window;multi_stage_reform |

## Next gate

1. continue exact-date verification for Tier-C candidates with good WHR coverage;
2. keep Tier A as the primary candidate pool and Tier B as legally verified sensitivity evidence;
3. freeze estimator/control rules without inspecting post-treatment Life Ladder changes;
4. only then run event-study / staggered-DiD diagnostics.
