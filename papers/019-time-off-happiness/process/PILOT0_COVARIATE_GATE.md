# ARIS4C019 · Pilot-0 Macro Covariate Gate

> Outcome-blind macro coverage diagnostic. This script never reads Life Ladder values.

- WHR country-year macro rows: **2199**.
- WHR countries/territories: **165**.
- WHR names matched to WDI names: **161**.
- Non-missing WHR Log GDP per capita rows: **2179**.
- Non-missing WDI unemployment rows: **2153**.
- Non-missing WDI inflation rows: **2111**.
- Headline primary events with >=2 pre observations for all three frozen covariates: **6/8**.

## Event-level pre-treatment coverage

| Event | Legal year | Primary | GDP n | Unemployment n | Inflation n | All 3 pass |
|---|---:|---:|---:|---:|---:|---:|
| Bahrain | 2012 | True | 3 | 3 | 3 | True |
| Canada | 2019 | True | 4 | 4 | 4 | True |
| China | 2008 | True | 2 | 2 | 2 | True |
| Croatia | 2010 | True | 2 | 2 | 2 | True |
| Kuwait | 2010 | True | 2 | 2 | 2 | True |
| Luxembourg | 2019 | True | 4 | 4 | 4 | True |
| Taiwan, China | 2017 | True | 4 | 0 | 0 | False |
| Kosovo | 2010 | True | 2 | 0 | 3 | False |
| United Kingdom | 2009 | False | 3 | 3 | 3 | True |
| Lithuania | 2017 | False | 4 | 4 | 4 | True |

## Frozen use

- Baselines use legal-year T-4 through T-1 only.
- Mid-year transition year T is excluded.
- No interpolation.
- Post-treatment macro values are not used as headline controls.
- Missing macro coverage does not justify dropping a treatment event after outcome inspection; it triggers a prespecified covariate-limited sensitivity instead.
