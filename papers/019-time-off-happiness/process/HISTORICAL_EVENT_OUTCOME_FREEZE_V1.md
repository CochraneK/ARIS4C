# ARIS4C019 · Historical verified-event outcome freeze v1.0

**Frozen:** 2026-09-24  
**Outcome inspection after this file:** permitted only under the rules below.  
**Registry:** `data/historical_verified_leave_reform_registry_v1.csv`

## Purpose

The historical legal audit produced four pre-outcome verified candidates:

| event | tier | legal clock | treatment structure |
|---|---|---|---|
| Bulgaria | A | 2001-03-31 | 14 working days → 20 working days |
| Slovakia | A | 2002-04-01 | 3 weeks → at least 4 weeks |
| Great Britain | B | 2007-10-01 and 2009-04-01 | 4 → 4.8 → 5.6 weeks / max 28 days |
| Namibia | B | 2008-11-01 | 24 consecutive days → 4 consecutive weeks |

A-tier means stronger treatment isolation, not a claim that all causal assumptions are satisfied. B-tier events remain useful robustness/illustration cases but carry explicit policy-bundle or broad-code concerns.

## Frozen event-time rules

### Bulgaria 2001
- legal effective date: 2001-03-31
- transition year: **2001**
- clean pre: **<=2000**
- full post: **>=2002**

### Slovakia 2002
- legal effective date: 2002-04-01
- transition year: **2002**
- clean pre: **<=2001**
- full post: **>=2003**

### Great Britain staged 2007/2009
- stage 1: 2007-10-01, +0.8 weeks
- stage 2: 2009-04-01, another +0.8 weeks
- baseline clean pre: **<=2006**
- transition/staged window: **2007–2009**
- full-treatment post: **>=2010**
- preferred modeling: staged dose / separate transition indicators; a binary fully-treated sensitivity may compare <=2006 vs >=2010 while excluding 2007–2009.
- scope flag: reform explicitly connected to bank/public holidays; never describe it as a pure vacation-only shock.

### Namibia 2008
- legal effective date: 2008-11-01
- clean pre: **<=2007**
- transition year: **2008**
- full post: **>=2009**
- scope flag: comprehensive Labour Act replacement; annual-leave provision is explicit but treatment isolation is weaker.

## Outcome-source hierarchy

The outcome source is chosen by pre-existing comparability/support, **not by effect sign**.

1. **Official WDH annual findings**, preserving equivalent-measure type and finding code. Use only same/instrument-compatible series; no blind pooling of all 0–10 transforms.
2. **Eurobarometer / Candidate Countries Eurobarometer** life satisfaction where country and pre/post coverage exist; preserve survey wave/date and question coding.
3. **EVS/WVS** life satisfaction / happiness at country-wave level as lower-frequency corroboration.
4. **Gallup/WHR annual Life Ladder** only when sufficient pre-treatment support exists. It cannot retroactively supply pre-2005 data for Bulgaria/Slovakia.

No source may be selected because it yields a stronger or more favorable estimate.

## Minimum support gates

### Annual-source event study
- at least **3 distinct pre-treatment annual observations** in the chosen compatible outcome series;
- at least **3 distinct full-post annual observations**;
- no single transition-year observation counted as pre or post;
- report actual calendar gaps; sparse WDH years are not interpolated.

### Wave-source corroboration
- at least **2 pre-treatment waves** and **2 post-treatment waves** if claiming a within-country directional contrast;
- otherwise the result is descriptive only.

### Donor / comparative analysis
- donor countries must use the same outcome source and compatible instrument family;
- donors with a verified leave reform within the focal event window are excluded or censored;
- donor composition is frozen before focal post-treatment outcomes are summarized;
- report leave-one-donor/region sensitivity where donor count permits.

## Estimator hierarchy

1. transparent within-country event-time plot/table;
2. donor-adjusted or matched comparative trajectory if support allows;
3. source-specific country/year FE on the broader legal panel;
4. stacked/event-study synthesis only after enough verified events share compatible outcomes;
5. event-level meta-analysis after event-specific estimates are frozen.

No pooled historical causal coefficient is computed by combining incompatible survey instruments.

## Confounding / falsification requirements

For each event:
- record contemporaneous major labour-code/policy changes;
- preserve crisis years (e.g. financial crisis) but run explicit sensitivity rather than silently deleting;
- test pre-trend/support before interpreting post patterns;
- separate statutory entitlement from public holidays and actual hours;
- B-tier events cannot be promoted to clean leave-specific causal evidence.

## Stopping rule

If an event lacks minimum comparable outcome support, label it **outcome-support insufficient**. Do not broaden the measure, change the event year, or search alternative baselines after seeing the outcome merely to rescue the event.
