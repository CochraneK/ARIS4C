# ARIS4C019 · Historical statutory-leave reform verification gate v1.0

**Frozen:** 2026-09-24  
**Outcome firewall:** no happiness outcome was inspected to select or accept these events.

The ILO 2000→2012 legal bridge generated a bounded primary-law audit queue. Primary-law review yields **three verified reform candidates** and **one rejected source-conflict case**.

## Verified A-tier candidates

### Bulgaria — 31 March 2001

The late-1990s ILO/NATLEX snapshot reports a 14-working-day basic entitlement. The Bulgarian Labour Code now preserves the amendment history in Article 155(4): State Gazette no. 25/2001, effective **31 March 2001**, raised the basic paid annual leave floor to **not less than 20 working days**. citeturn115033search1

**Freeze:** single-step statutory annual-leave reform; provisional magnitude +6 working days. No public-holiday bundle has been identified in the current legal evidence.

### Slovakia — 1 April 2002

The pre-reform Slovak Labour Code set basic annual leave at **three weeks**. citeturn673653search1turn673653search4

Act 311/2001 took effect on **1 April 2002**; its earliest effective version already states in §103(1) that basic annual leave is **at least four weeks**. citeturn551982view0turn163090view0

**Freeze:** single-step +1-week basic statutory minimum effective 2002-04-01.

## Verified B-tier staged candidate

### Great Britain — 1 October 2007 and 1 April 2009

The 2007 Working Time amendment added **0.8 weeks from 1 October 2007** and a second **0.8 weeks from 1 April 2009**, bringing the total from four weeks to 5.6 weeks, capped at 28 days. citeturn397223view1turn397223view2

The policy rationale explicitly linked the extra entitlement to bank/public holidays, so this is not coded as a clean leave-only shock. citeturn298580search1

**Freeze:** verified two-stage statutory-entitlement reform, **public-holiday-linked scope flag**, Great Britain scope. Analyze separately from A-tier leave-specific candidates.

## Rejected case: Nicaragua

The 2012 ILO Annex reports 10 standardized days, but NORMLEX/CEACR records that Labour Code Article 76 granted **15 paid days per six months**, i.e. 30 days per year, in 1998 and again in 2005. citeturn121965search1turn121965search0

Therefore the apparent 2000→2012 drop is treated as **source inconsistency / scope mismatch, not a legal reform**. It must not enter an event study.

## Next legal audit queue

The remaining high-confidence cross-snapshot differences — Algeria, Mali and Namibia — remain **unverified**. They should be audited only against national primary legislation before entering this registry.

## Canonical file

`data/historical_verified_leave_reform_registry_v1.csv`


## Second audit wave: Algeria / Mali / Namibia

### Algeria — reject as harmonization artifact

Law 90-11 provides paid annual leave at 2.5 days per month, capped at **30 calendar days per year**. The ILO supervisory record explicitly describes the 30-day ceiling as calendar days. citeturn448988search0turn448988search1

Under the 2012 ILO five-day-workweek method, 30 calendar days map to about **21 working days** (`30 × 5/7`). The prior 25-day screening value was a harmonization error. No 2000→2012 reform is accepted.

### Mali — reject as harmonization artifact

Labour Code Article L.151 provides 2.5 days per month, **30 days per year including non-working days**. citeturn448988search8turn242103search19

Thus a five-day-workweek equivalent is about **21 days**, matching the 2012 ILO snapshot. The prior 25-day approximation was incorrect. No reform is accepted.

### Namibia — verified B-tier reform, 1 November 2008

The 1992 Labour Act §39 provided **24 consecutive days** of paid annual leave. citeturn997205search12

The 2004 Labour Act proposed a different rule but **never came into force**; the 1992 Act remained operative until replaced. citeturn296718search0

The 2007 Labour Act §23 provides **four consecutive weeks**; for a five-day workweek it explicitly equals **20 working days**. NATLEX records general entry into force on **1 November 2008**. citeturn588501search12turn588501search0

**Freeze:** verified statutory annual-leave increase, but B-tier for causal isolation because it arrived in a comprehensive Labour Act that altered many employment conditions.

## V1 reform inventory after two audit waves

Accepted pre-outcome candidates:
- **A-tier:** Bulgaria 2001; Slovakia 2002.
- **B-tier / bundled or broad-code:** Great Britain 2007/2009 staged; Namibia 2008.

Rejected:
- Nicaragua — source conflict;
- Algeria — unit-harmonization artifact;
- Mali — unit-harmonization artifact.

No happiness outcome was used in these adjudications.
