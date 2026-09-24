# ARIS4C-019 · Time Off × Happiness · Long Run

**Expanded working title:** Time Off and Happiness Across Countries: Long-Run Institutional Change, Comparative Well-Being Panels, and Policy-Reform Evidence

ARIS4C019 studies how statutory paid annual leave and realized working time changed across countries over the long twentieth century and early twenty-first century, and how those changes relate to subjective well-being.

The project is deliberately multi-resolution:

1. **institutional history** — paid-leave standards, national laws, work-week/rest rules and policy diffusion;
2. **realized time use** — historical and modern annual working hours;
3. **subjective well-being history** — WDH, Cantril, Eurobarometer, WVS/EVS and Gallup/WHR;
4. **modern country-year association panels** — broad coverage with explicit non-causal interpretation;
5. **verified reform causal studies** — exact legal timing, treatment-isolation and donor/pretrend gates.

The original eight-event + Israel study is preserved as **Pilot-0**, a narrow causal-identification module rather than the whole project.

## Current scale

### Modern annual panel

- statutory leave × WHR availability: **161 countries / 1,934 country-years**
- median linked support: **14 years**
- **127 countries** with >=10 linked years
- **57 countries** with >=15 linked years
- WHR2024 annual source through 2023

### Actual working hours

- **130 countries / 5,063 observations / 1870–2023**
- 14-country historical segment already present from **1870**
- country coverage rises from 14 in 1870/1900/1913/1938 to 130 in 2005/2010
- all 14 earliest hours countries also occur in the WDH long-run registry

### Historical well-being

- WDH public long-run mean registry materialized: **124 variable series / 61 nation labels**, earliest **1946**
- Cantril historical comparative data: 1957–1963
- Eurobarometer general life satisfaction: **1973–2026** measurement chain; Mannheim harmonized trend file = 86 waves / >1M respondent cases through 2002
- WVS Waves 1–7 country registry: **295 country-wave rows / 107 distinct codes**

### Legal/institutional history

- ILO C052 (1936): current official register = **54 ratifications**
- ILO C132 (1970): current official register = **39 ratifications**
- complete C132 39-country diffusion seed materialized; 14 ratifications occurred in the 1970s
- national implementation law is kept separate from ILO ratification

## Modern statistical result

The expanded modern analysis now includes:

- country + year fixed effects;
- within-between decomposition;
- first differences;
- log GDP / unemployment / inflation adjustment;
- >=10 / >=15-year support checks;
- country-specific linear trends;
- frozen nonlinear spline knots at 12 / 20 / 26 leave days;
- 0–3-year report-year lag diagnostics;
- leave-one-changing-country-out influence analysis;
- legal-credibility restriction;
- legal-year vs World-Bank-report-year timing falsification;
- joint statutory-leave + actual-hours models.

### Modern interpretation lock

The modern broad panel does **not** establish a stable positive or negative aggregate Life Ladder response.

For statutory leave, the timing audit is decisive: verified legal changes appear in the World Bank panel on average **1.22 years later** than their actual legal effective year. In the same verified-changer macro-adjusted sample, the first-difference estimate is strongly negative when the WB report-year step is used but flips positive when the same leave step is aligned to the verified legal year. Neither sign is promoted as causal.

For actual working hours, the familiar negative between-country association does not reproduce as a stable negative within-country annual coefficient after fixed effects / macro controls / country trends.

See [Expanded modern interpretation lock](process/EXPANDED_MODERN_INTERPRETATION_LOCK.md).

## What remains

The modern panel is now a substantive completed module, but the full project is not finished. Priority work is:

- numeric WDH long-run observations;
- Eurobarometer and EVS/WVS outcome aggregation;
- complete C052/C132 primary rows + national paid-leave legal chronology;
- historical instrument-specific hours × well-being models;
- cross-instrument coefficient synthesis / meta-analysis;
- expanded verified-reform/event-effect synthesis;
- a new bilingual manuscript integrating the full long-run evidence.

## Construct boundary

Never silently substitute:

1. statutory paid annual leave;
2. public holidays;
3. weekly rest / work-week rules;
4. actual annual working hours;
5. actual leave utilization.

## Canonical entry points

- [Expanded research plan](process/HISTORICAL_EXPANSION_PLAN.md)
- [Historical source matrix](process/HISTORICAL_SOURCE_MATRIX.md)
- [Historical coverage gate](process/HISTORICAL_COVERAGE_GATE.md)
- [Modern panel overlap gate](process/MODERN_PANEL_OVERLAP_GATE.md)
- [Expanded statistical freeze](process/EXPANDED_STATISTICAL_FREEZE.md)
- [Expanded modern interpretation lock](process/EXPANDED_MODERN_INTERPRETATION_LOCK.md)
- [Long-run hours coverage gate](process/WORKING_HOURS_LONGRUN_COVERAGE_GATE.md)
- [WDH variable coverage gate](process/WDH_VARIABLE_COVERAGE_GATE.md)
- [Current status](process/STATUS.md)
- [Agent handoff](handoff/AGENT_HANDOFF.md)

## Pilot-0 archive

The prior leave-specific manuscript remains reproducible and scientifically frozen:

- [Pilot-0 interpretation lock](process/PILOT0_INTERPRETATION_LOCK.md)
- [Israel holdout results](process/ISRAEL_HOLDOUT_RESULTS.md)
- [English Pilot-0 working paper](manuscript/WORKING_PAPER_EN.md)
- [中文 Pilot-0 工作稿](manuscript/WORKING_PAPER_ZH.md)

Its locked conclusion remains: **no robust positive or negative population Life Ladder effect of statutory annual leave is established from that causal-identification module.**

Positive/negative affect remain locked for Pilot-0 and are not opened to repair identification problems.
