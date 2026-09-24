# ARIS4C019 · Legal-year vs World Bank report-year timing audit

**Date:** 2026-09-24

Among panel changes that already have verified/verified-derived legal timing and pass the legal-timing coverage gate:

- events audited: **9**
- mean WB jump-year minus legal-effective-year offset: **1.22 years**
- median offset: **1.0 years**
- range: **0 to 2 years**

| event | legal year | WB jump year | offset |
|---|---:|---:|---:|
| Bahrain (BHR_EW2014) | 2012 | 2014 | +2 |
| Canada (CAN_EW2019) | 2019 | 2019 | +0 |
| China (CHN_EW2009) | 2008 | 2009 | +1 |
| Croatia (HRV_EW2011) | 2010 | 2011 | +1 |
| Kosovo (XKX_EW2012) | 2010 | 2012 | +2 |
| Kuwait (KWT_EW2011) | 2010 | 2011 | +1 |
| Lithuania (LTU_EW2019) | 2017 | 2019 | +2 |
| Luxembourg (LUX_EW2020) | 2019 | 2020 | +1 |
| Taiwan Province of China (TWN_EW2018) | 2017 | 2018 | +1 |

## Consequence

The WB panel's reporting year cannot be interpreted as the legal treatment clock.

This directly affects the expanded-panel lag diagnostics: a positive coefficient at WB lag 1–3 can partly or wholly reflect delayed coding/reporting of a law that became effective earlier. Therefore the initial lag-2/lag-3 positive associations are **timing-sensitive diagnostics**, not evidence that statutory leave improves Life Ladder only after two or three years.

For causal/event-time work, use verified legal effective dates. For broad descriptive FE work using WB annual values, describe the exposure as the WB standardized-case legal measure observed in that report year, not as a precisely timed reform indicator.
