# ARIS4C019 · Bounded Legal Queue Audit

**Frozen:** 2026-09-23  
**Scope:** final bounded review of Tajikistan, Montenegro, and Ecuador World Bank leave-panel jumps  
**Rule:** no candidate is promoted because its happiness outcome is favorable; candidate-specific Life Ladder effects were not inspected during this legal review.

## Bottom line

None of the final three queue items qualifies as a new clean annual-leave treatment event.

| Queue item | Finding | Decision |
|---|---|---|
| Tajikistan EW2015 | Official legal history does not show a 2015 annual-leave reform. The 1997 Labour Code's listed amendments stop in 2013 before replacement by the 2016 Code. | Reject the 2015 World Bank jump as a treatment event; treat as likely coding/measurement discontinuity absent contrary legal evidence. |
| Montenegro EW2010 | There is evidence of a genuine historical increase from the older 18-working-day floor to at least 20 days, but the legally traceable reform is tied to the broad 2011 Labour Law amendment rather than the EW2010 +1 panel jump. | Reject the queue jump as a clean event. Do not create a new leave-specific treatment from it. |
| Montenegro EW2015 | The statutory floor was already at least 20 working days by this period; no matching 2015 leave-entitlement decrease was found. | Reject as legal treatment; likely tenure-profile/panel coding movement. |
| Ecuador EW2013 | The Labour Code amendment history contains a 2012 labour-rights law but no matching 2013 annual-leave entitlement change. Article 69's 15-day annual-vacation rule persists. | Reject as a legal annual-leave event. |

Machine-readable decisions: `data/legal_queue_bounded_audit.csv`.

## Evidence notes

### Tajikistan

The official ADLIA consolidated 1997 Labour Code lists amendments through **22 July 2013** and states that it was repealed by the new Labour Code adopted in **2016**. A separate ADLIA record confirms the 2016 adoption. No 2015 leave-entitlement amendment was identified in this bounded search.

- https://mmih.adlia.tj/SEARCH/DocumentView?DocumentId=20398&compareid=162419
- https://mmih.adlia.tj/Search/DocumentView?DocumentId=127597

Therefore the World Bank EW2015 fall from 21 to 18 average working days should not be interpreted as a statutory reform without new contrary legal evidence.

### Montenegro

ILO NORMLEX records Montenegro's older annual-holiday specification at **18 working days**. ILO EPLex records Labour Law Act No. 49/08 as amended by Act No. 59/2011 of **14 December 2011**. Contemporary EU screening material subsequently describes annual leave as at least **20 working days**.

- https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB%3A11300%3A0%3A%3ANO%3A%3AP11300_INSTRUMENT_ID%3A312277
- https://eplex.ilo.org/en/country-detail?code=MNE&yr=2012
- https://enlargement.ec.europa.eu/document/download/b7191b23-7320-4ec2-97b7-1a8461889986_en?filename=screening_report_montenegro_ch19.pdf&prefLang=hr
- Montenegro Government 2011 amendment context: https://www.gov.me/clanak/106946--s-a-o-p-s-t-e-nj-e

So a real historical entitlement increase plausibly exists, but the queue's **EW2010 +1** and **EW2015 −0.33** observations are not cleanly aligned legal shocks. The 2011 amendment was also a broad labour-law package, so it does not meet the leave-specific holdout criterion.

### Ecuador

ILO NATLEX's Labour Code record lists the **31 July 2012** labour-rights amendment and later amendments, but no 2013 annual-leave reform matching the EW2013 −0.33 panel movement. Ecuador's National Assembly described the 2012 law as addressing enforcement of workers' claims, social-security affiliation, lactation and domestic-worker rest, not a change to the standard annual-vacation entitlement.

- https://natlex.ilo.org/dyn/natlex2/r/natlex/fe/details?p3_isn=47812
- https://www.asambleanacional.gob.ec/es/noticia/8387-pleno-aprobo-proyecto-de-ley-de-defensa-de-los-derechos
- current Ministry guidance on Article 69: https://www.trabajo.gob.ec/27-cuantos-dias-de-vacaciones-le-corresponden-al-trabajador-que-ha-suscrito-un-contrato-de-jornada-parcial-permanente/

Accordingly EW2013 is not promoted to a treatment event.

## Bounded-search stop rule

This closes the current World Bank-jump expansion round.

- Do **not** continue harvesting small panel discontinuities merely to increase event count.
- Future additions must come from a **law-first** search for stand-alone annual-leave reforms, then pass outcome-availability and donor-support gates.
- The existing 8-event frozen panel remains a transparent broad labour/time-off-policy stress test.
- The leave-specific holdout remains separate; Mexico 2023 remains the strongest currently identified future candidate but requires >=2 full-post annual Life Ladder observations from a validated annual source.
- Positive and negative affect remain locked.

## Scientific consequence

The project bottleneck is now explicitly **identification quality**, not event discovery volume. More World Bank jumps are not useful unless a primary legal source establishes a distinct, correctly timed statutory annual-leave intervention.
