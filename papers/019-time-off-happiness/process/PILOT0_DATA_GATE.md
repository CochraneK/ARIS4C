# ARIS4C019 · Pilot-0 Data Gate

> Auto-generated from official source downloads. This reports feasibility only; it does not estimate a treatment effect.

- WHR annual panel: **2199 country-year observations**, **165 countries/territories**, 2005–2022.
- Leave-reform candidates registered: **30**.
- Candidates with >=2 observed pre and >=2 observed post WHR years in a ±4-year window: **17**.
- Of those, candidates whose treatment year is already verified: **0**.
- World Bank statutory-leave panel: **3434 rows**, **202 economies**, EW2004–EW2020.
- Reform candidates whose World Bank panel change matches the registered direction and WHR coverage passes: **12**.
- Freeze-eligible legal events (verified timing + WHR coverage): **0**.
- Tier A, additionally corroborated by the World Bank panel: **0**.
- Tier B, legally verified but not corroborated by the World Bank historical panel: **0**.
- All World Bank annual-leave jumps discovered: **44**; unregistered jumps with usable WHR coverage awaiting legal verification: **11**.

## Interpretation

Coverage PASS means an event is empirically inspectable. It does **not** establish parallel trends, no anticipation, clean treatment isolation, or causality.

## Verified-year candidates that pass coverage

None yet. Verify exact legal effective dates before causal estimation.

## Next gate

1. continue exact-date verification for Tier-C candidates with good WHR coverage;
2. keep Tier A as the primary candidate pool and Tier B as legally verified sensitivity evidence;
3. freeze estimator/control rules without inspecting post-treatment Life Ladder changes;
4. only then run event-study / staggered-DiD diagnostics.
