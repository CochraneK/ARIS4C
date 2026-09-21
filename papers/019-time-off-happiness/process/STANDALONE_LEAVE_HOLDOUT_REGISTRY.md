# ARIS4C019 · Stand-alone Annual-Leave Reform Holdout Registry v0.1

**Frozen candidate-selection date:** 2026-09-21  
**Stage:** post-unlock identification rescue  
**Selection basis:** legal specificity + calendar timing + outcome *availability*, not candidate Life Ladder sign or magnitude.

> This is a post-outcome registry. It does not alter the original eight-event freeze. The purpose is to define a legally cleaner holdout track without selecting candidates because their happiness outcomes look favorable.

## Admission rule for a future leave-specific holdout

A candidate can enter the leave-specific holdout only if all of the following are satisfied **before inspecting its candidate-specific treatment effect**:

1. exact legal effective date is verified;
2. the statutory change is specifically about paid annual leave, rather than a broad Labour Code / working-time package;
3. entitlement direction and magnitude are interpretable;
4. at least 2 observed Life Ladder years exist in legal T-4…T-1;
5. at least 2 full-exposure Life Ladder years exist in the frozen post window;
6. no overlapping leave reform makes the event intrinsically multistage unless a multistage estimator is frozen first;
7. major macro/reference-year shocks are flagged before outcome estimation;
8. donor contamination/support is checked using the same outcome-blind logic as Pilot-0.

## Current candidates

| Candidate | Legal cleanliness | Coverage | Decision |
|---|---|---|---|
| New Zealand 2007 | Strong. Holidays Act explicitly scheduled the move to four weeks from 1 April 2007. | Only one observed pre year in the available WHR annual panel. | **Do not estimate as primary holdout** under the frozen >=2-pre rule. |
| Mexico 2023 | Strong. The federal decree specifically reforms Labour Law Articles 76 and 78 “en materia de vacaciones” and raises the first-year minimum to 12 working days. | Four pre years are available, but a panel ending in 2023 provides only one post year. | **Highest-priority future holdout** if a validated annual 2024/2025 outcome panel supplies >=2 post years. |
| Malta 2018/2019/2020 | Leave-focused, but annual entitlement rose in serial +8-hour stages. | Strong annual survey coverage. | **Sensitivity only** unless a multistage design is frozen; not a single clean shock. |
| UK 2007/2009 | Leave-specific regulations, but two staged increases. | 2007 stage lacks >=2 pre years; 2009 stage has prior treatment in its pre-period. | **Sensitivity only**; also GFC overlap. |
| Zambia 2007 | Leave provision appears inside a broad Employment Act. | Outcome coverage is limited around the event. | **Reject from leave-specific holdout** unless legal review overturns the bundle classification. |

Machine-readable registry: `data/standalone_leave_reform_candidates.csv`.

## Source anchors

- New Zealand Holidays Act 2003, version around 2007: https://www.legislation.govt.nz/act/public/2003/129/en/2007-05-17/
- Mexico DOF decree, 27 Dec 2022: https://www.dof.gob.mx/nota_detalle.php?codigo=5675889&fecha=27/12/2022
- Malta DIER Resource Pack 2020: https://dier.gov.mt/en/About-DIER/Publications-and-Archives/Other%20Publications/Documents/Resource%20Pack%202020.pdf
- UK working-time regulation evidence review: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/389676/bis-14-1287-the-impact-of-the-working-time-regulations-on-the-UK-labour-market-a-review-of-evidence.pdf
- Zambia Employment Act / ILO NATLEX: https://natlex.ilo.org/dyn/natlex2/r/natlex/fe/details?p3_isn=76114

## Locked interpretation

The absence of an immediately usable clean holdout is a scientific result about design feasibility, not a reason to relax the rules. The next priority is to extend/validate annual Life Ladder outcome coverage and continue a bounded legal search, while keeping the current eight-event panel as a broader policy-package stress test.
