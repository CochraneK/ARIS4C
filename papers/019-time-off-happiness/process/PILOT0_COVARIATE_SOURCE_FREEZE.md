# ARIS4C019 · Pilot-0 Covariate Source Freeze v0.1

**Frozen:** 2026-09-21  
**Stage:** pre-outcome / no-effect-look

> This file freezes macro-covariate definitions before any post-reform Life Ladder effect is inspected. Covariates are for pre-treatment balance, donor construction, and sensitivity analysis; they are not selected for statistical significance.

## 1. Frozen covariates

| Construct | Frozen variable | Source | Use |
|---|---|---|---|
| Economic level | Log GDP per capita | WHR 2023 historical workbook, field `Log GDP per capita` | Pre-treatment baseline / donor similarity only |
| Labor-market slack | Unemployment, total (% of total labor force), modeled ILO estimate | World Bank WDI `SL.UEM.TOTL.ZS` | Pre-treatment baseline / donor similarity only |
| Price instability | Inflation, consumer prices (annual %) | World Bank WDI `FP.CPI.TOTL.ZG` | Pre-treatment baseline / donor similarity only |

## 2. Source URLs

- WHR historical workbook: https://happiness-report.s3.amazonaws.com/2023/DataForTable2.1WHR2023.xls
- World Bank unemployment indicator: https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS
- World Bank inflation indicator: https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG
- World Bank API base: https://api.worldbank.org/v2/

The existing WHR transport fallback remains a commit-pinned mirror of the same workbook and is recorded by SHA256 in `data/source_inventory.json`.

## 3. Timing freeze

For each focal reform with legal effective year `T`:

- primary baseline covariate summary = mean over observed years `T-4 ... T-1`;
- require at least **2 observed pre-treatment values** for a covariate to be considered available for that event;
- the reference year is `T-1`;
- a mid-year transition year `T` is never included in the baseline;
- no interpolation of missing macro observations;
- post-treatment covariate values are not used for headline adjustment.

## 4. Why no contemporaneous post-treatment controls

GDP, unemployment, and inflation can themselves respond to policy or to macro shocks correlated with policy. Conditioning on post-treatment values could therefore block part of the treatment pathway or introduce post-treatment bias.

Accordingly:

1. headline event estimates are not conditioned on contemporaneous post-treatment macro variables;
2. frozen macro covariates may be used for pre-treatment balance checks, donor weighting/matching, or lagged/baseline sensitivity specifications;
3. no additional covariate may be added because it improves significance.

## 5. Variables explicitly not promoted to primary controls

WHR social support, freedom to make life choices, generosity, perceptions of corruption, positive affect, and negative affect are not headline controls.

- Positive/negative affect are secondary outcomes and remain locked until the Life Ladder analysis is complete.
- Social support/freedom/etc. may be mechanisms or post-treatment variables.

## 6. Gate to outcome unlock

Before `PILOT0_UNLOCK.md` can be created:

- the legal-year event clock must pass;
- all headline events must retain acceptable donor support;
- the frozen three macro covariates must have source definitions recorded;
- pre-treatment coverage diagnostics must be generated without inspecting Life Ladder effects;
- any changes to this freeze after outcome inspection must be logged as explicit deviations.
