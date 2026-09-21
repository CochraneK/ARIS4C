# ARIS4C019 · Bounded Legal-Jump Isolation Audit

**Frozen audit date:** 2026-09-21  
**Input queue:** `process/LEGAL_VERIFICATION_QUEUE.csv`  
**Rule:** verify the pre-existing 11 World Bank annual-leave discontinuities; do not expand the search indefinitely and do not inspect candidate-specific Life Ladder effects.

## Result

- Queue rows reviewed: **11 / 11**
- New clean annual-leave holdouts admitted: **0**
- Queue rows rejected from a leave-specific causal holdout: **11**
- Reason families:
  - broad labour/employment code rather than leave-only intervention;
  - legal effective date does not match the World Bank jump year;
  - scope is entity/jurisdiction limited rather than population-wide;
  - no legal entitlement change could be verified, suggesting coding/unit/profile revision.

This is an **identification-feasibility result**. It is not a reason to relax the holdout rules.

## Case audit

| Queue event | Finding | Decision |
|---|---|---|
| Estonia EW2009 +24 | A real Employment Contracts Act entered into force 2009-07-01 and §55 sets 28 calendar days, but it is a comprehensive employment code; the WB 0→24 working-day discontinuity cannot be interpreted as a clean isolated +24-day leave shock. | Reject clean holdout |
| Tajikistan EW2015 −3 | Contemporaneous 2015 material still reports a minimum of 24 **calendar** days; later Labour Code also retains 24 calendar days. No 2015 statutory cut matching 21→18 working days was verified. | Reject; likely unit/coding revision |
| Bangladesh EW2008 +3 | Labour Act 2006 §117 already sets the annual-leave formula. The broad Act predates the WB jump. | Reject timing/bundle |
| Uganda EW2008 +3 | Employment Act 2006 §54 already grants seven paid days per four months of continuous service (21/year). | Reject timing/bundle |
| Saudi Arabia EW2010 +2.67 | The WB change is mainly a tenure-profile change. The bounded search did not verify a stand-alone 2010 annual-leave-only amendment. | Reject clean holdout |
| Bosnia and Herzegovina EW2017 +2 | Relevant labour rules are broad and entity-level; the bounded search did not identify a clean population-wide leave-only national shock. | Reject scope/bundle |
| Slovenia EW2015 +1 | ZDR-1 was adopted in 2013 and sets a minimum of four weeks; the previous regime also specified four weeks. No matching national 2015 statutory entitlement step was verified. | Reject; likely profile/coding change |
| Iraq EW2017 +1 | Comprehensive Labour Law No. 37 of 2015 contains the annual-leave provisions and predates the 2017 WB discontinuity. | Reject timing/bundle |
| Montenegro EW2010 +1 | ILO records a relevant Labour Law amendment in 2011 providing at least 20 working days, not the 2010 18→19 queue jump. | Reject timing mismatch |
| Ecuador EW2013 −0.33 | Article 69 still provides the long-standing 15-day annual-vacation rule plus seniority days; no 2013 national statutory cut was verified. | Reject; likely profile/coding change |
| Montenegro EW2015 −0.33 | Government consolidated Labour Law materials do not establish a leave-only 2015 national cut matching the tiny WB average shift. | Reject; likely profile/coding change |

Machine-readable audit: `data/legal_jump_isolation_audit.csv`.

## Source anchors

- Estonia Employment Contracts Act, official Riigi Teataja: https://www.riigiteataja.ee/en/eli/529062018003/consolide
- Tajikistan 2015 business-law guide (contemporaneous leave rule): https://www.rsm.global/tajikistan/sites/default/files/media/Guide%20To%20Doing%20Business%20in%20Tajikistan.pdf
- Bangladesh Labour Act 2006, ILO NATLEX: https://natlex.ilo.org/dyn/natlex2/natlex2/files/download/76402/BGD76402%20Eng.pdf
- Uganda Employment Act 2006, ILO NATLEX: https://natlex.ilo.org/dyn/natlex2/natlex2/files/download/74416/UGA74416.pdf
- Slovenia ZDR-1, official PISRS: https://pisrs.si/Pis.web/pregledPredpisa?sop=2013-01-0784
- Iraq Labour Law 2015, ILO NATLEX: https://natlex.ilo.org/dyn/natlex2/natlex2/files/download/96652/IRQ96652%20Eng.pdf
- Montenegro Labour Law / ILO NORMLEX comment on 2011 amendment: https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:13101:0::NO::P13101_COMMENT_ID:3134153
- Montenegro consolidated Labour Law, Government: https://www.gov.me/en/documents/505ff512-502c-4960-a96d-091de0ad0a03
- Ecuador 2013 Labour Code application, National Court: https://www.cortenacional.gob.ec/cnj/images/pdf/sentencias/laboral/2013/R21-2013-J423-2011.pdf

## Locked consequence

The bounded World Bank jump queue yields **zero new legally clean leave-specific holdouts**. The project must therefore not promote a measurement discontinuity into a treatment merely to increase event count.

The annual-leave-specific track remains underidentified with the currently open, reproducible annual Life Ladder data. Mexico 2023 remains the highest-priority future holdout once a verifiable annual panel provides at least two full post-treatment survey years.

The original eight-event panel remains useful only as a transparent stress test of heterogeneous labour/time-off reforms in which annual leave changed.

Positive and negative affect remain locked.
