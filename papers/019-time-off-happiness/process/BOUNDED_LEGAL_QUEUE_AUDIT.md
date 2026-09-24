# ARIS4C019 · Bounded Legal Queue Audit v0.1

**Closed:** 2026-09-24  
**Scope:** final bounded verification pass for Tajikistan, Montenegro and Ecuador

> This audit closes the current expansion round. These candidates were selected from the pre-existing World Bank jump queue based on coverage and statutory-leave change magnitude, not on their Life Ladder outcomes.

## Result

None of the three candidates passes the leave-specific legal-treatment gate.

| Candidate | WB signal | Legal finding | Decision |
|---|---:|---|---|
| Tajikistan 2015 | average leave 21 → 18 days | No matching 2015 annual-leave entitlement cut was verified. The official legal record shows the 1997 Labour Code remained in force until the 2016 replacement; contemporaneous 2014/2015 amendments located in the official database concern holiday law rather than a leave-specific cut. | **Reject as treatment** unless new primary legal evidence appears. |
| Montenegro 2015 | average leave 21 → 20.67 | The 2014 consolidated Labour Law already sets a statutory minimum of **20 working days** in Article 65, and the government published a consolidated Labour Law text again in 2015. | **Reject as treatment**; likely tenure/profile recoding. |
| Ecuador 2013 | average leave 12.33 → 12.0 | Current/continuing Labour Code rule is **15 consecutive days** of annual vacation, with extra tenure days after five years. ILO records a broad 2012 labour-rights law but no verified annual-leave reduction matching the -0.33 standardized average shift. | **Reject as treatment**; likely standardized-case/profile recoding. |

Machine-readable decisions are in `data/bounded_legal_queue_audit.csv`.

## Evidence notes

### Tajikistan

- Official ADLIA record for the 1997 Labour Code contains the annual-leave chapter and remained the operative Labour Code until the new code was adopted in 2016.
- The 2016 adoption record explicitly replaces the prior-code regime.
- Searches of official 2014/2015 legal changes identified amendments to the law on holidays, but did not identify a leave-specific statutory reduction corresponding to the World Bank panel's 21→18 working-day change.

Conclusion: **do not infer a legal reform from the World Bank discontinuity alone**.

### Montenegro

The English 2014 consolidated Labour Law states in Article 65 that annual leave must be **not less than 20 working days**. The government also published a consolidated Labour Law text in November 2015.

The World Bank panel's 2015 movement from 21.0 to 20.67 is too small and too tenure-profile-shaped to count as a treatment without a matching legal entitlement change.

Conclusion: **coding/profile update, not a verified leave reform**.

### Ecuador

The Ministry of Labour describes Article 69 of the Labour Code as providing **15 consecutive days** of annual vacation, plus one extra day for each year beyond five years with the same employer. ILO NATLEX lists the 31 July 2012 Organic Law for Defence of Labour Rights as an amending text, but no annual-leave entitlement change was verified that would explain the World Bank panel's -0.33 average shift.

Conclusion: **do not treat the 2013 World Bank average change as an annual-leave policy shock**.

## Bounded-search stopping rule

This verification round is now **closed**.

Do not continue mining ever-smaller World Bank leave-panel discontinuities merely to enlarge the event count. Re-open legal-event discovery only when at least one of the following occurs:

1. a new authoritative statutory-leave reform database/source is obtained;
2. annual Life Ladder coverage is extended far enough to admit already-clean modern reforms such as Mexico 2023;
3. a specific stand-alone annual-leave reform is independently identified from legal/policy literature.

## Scientific consequence

The scarcity of clean, outcome-covered natural experiments is itself a design result.

ARIS4C019 should now maintain two explicitly different estimands:

- **Track A — leave-specific causal question:** only stand-alone annual-leave reforms that pass the strict legal-isolation and coverage gate. Current viable pool is too small for a pooled manuscript-level causal claim.
- **Track B — broader labour/time-off reform question:** preserve the existing eight-event panel as a transparent exploratory/stress-test analysis, with its policy-bundle, pretrend and shock limitations.

Positive/negative affect remain locked because opening more outcomes does not solve the identification problem.
