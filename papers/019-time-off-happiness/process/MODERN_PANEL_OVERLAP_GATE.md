# ARIS4C019 · Modern WB × WHR overlap gate v1.0

**Freeze date:** 2026-09-24  
**Outcome-effect inspection:** NONE. This gate uses WHR availability only, not Life Ladder values.

## Canonical modern overlap

After explicit country-name/code reconciliation between the repository's World Bank Employing Workers statutory-leave panel and WHR annual observation calendar:

- WHR countries in availability calendar: **165**
- WB base/national economy codes in the historical panel: **191**
- WHR countries mapped to WB exposure records: **161 / 165**
- exact linked WB-leave × WHR-availability countries: **161**
- exact linked country-years: **1,934**
- median linked years per country: **14**
- countries with >=10 linked years: **127**
- countries with >=15 linked years: **57**
- maximum linked years in the current 2004-2020 WB window: **15**

WHR countries not linkable to this WB source are:
- Cuba
- Somaliland region
- State of Palestine
- Turkmenistan

These four are **source-coverage gaps**, not exclusions from the broader historical project.

## Crosswalk QA

Several World Bank records use a city-labelled standardized case while retaining the national/base code, for example:

- Bangladesh Dhaka -> BGD
- Brazil Sao Paulo -> BRA
- India Mumbai -> IND
- Indonesia Jakarta -> IDN
- Japan Tokyo -> JPN
- Mexico Mexico City -> MEX
- Russian Federation Moscow -> RUS
- United States New York City -> USA
- China Shanghai -> CHN
- Pakistan Karachi -> PAK
- Nigeria Lagos -> NGA

The Democratic Republic of the Congo uses the legacy World Bank code **ZAR** in this historical file rather than modern ISO **COD**. Using COD silently loses all DRC years; the crosswalk therefore explicitly preserves ZAR for this source.

## Exposure-only variation audit

Within the **1,934** linked country-years, without opening any happiness values:

- **26** countries show at least one observed change in WB `leave_avg`;
- **28** adjacent observed-value transitions occur;
- **24** transitions are increases;
- **4** transitions are decreases;
- median absolute transition size = **2.33 days**.

These are database discontinuities, **not automatically legal reforms**.

Examples demanding treatment-verification rather than automatic admission include:
- Estonia: observed 0 -> 24;
- China: observed 0 -> 6.67;
- Somalia: `leave_avg=80` because tenure-specific fields are 15 / 75 / 150;
- small negative jumps in Ecuador and Montenegro.

Therefore the modern panel supports broad association / descriptive statistics, while causal event studies remain restricted to independently verified legal changes.

## Exposure distribution in linked country-years

Raw WB average-leave distribution:

- N = **1,934**
- mean = **19.42**
- SD = **6.13**
- P10 = **12**
- Q1 = **16.08**
- median = **20**
- Q3 = **22.33**
- P90 = **26**
- min = **0**
- max = **80**
- distinct numeric values = **64**

The 0 and 80 extremes prove that raw WB values require legal/source QA and robust/winsor-free sensitivity analyses; they must not be silently cleaned after viewing happiness outcomes.

## Files

- `data/modern_wb_whr_country_crosswalk.csv`
- `data/modern_wb_whr_overlap.csv`
- `data/modern_wb_whr_overlap_summary.csv`
- `data/modern_overlap_leave_change_events.csv`
- `data/modern_overlap_country_exposure_summary.csv`

## Gate decision

The statement that ARIS4C019 has "too few countries" is no longer true for the modern descriptive panel: the current legal-leave × annual-happiness availability intersection already reaches **161 countries and 1,934 country-years**.

However, broad panel size does **not** imply 161 clean natural experiments. The causal reform layer remains a much smaller verified subset by design.
