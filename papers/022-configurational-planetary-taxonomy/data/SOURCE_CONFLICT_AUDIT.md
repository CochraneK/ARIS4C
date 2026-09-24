# Source-conflict audit · v0.2

Date: 2026-09-24

This audit distinguishes unresolved conflict from ordinary scientific updating, different constructs, and model-vs-observation differences.

| ID | Body | Variable | Sources | Type | Adjudication | Status |
|---|---|---|---|---|---|---|
| C001 | Mimas | present subsurface ocean | NASA_MIMAS_FACTS vs NATURE_MIMAS_OCEAN_2024 | temporal supersession | Use 2024 Nature orbital-dynamics result for current ocean evidence; retain older frozen/inert surface description as valid surface context. | RESOLVED |
| C002 | Quaoar | atmosphere | earlier non-detections / upper limits vs QUAOAR_APJ_2026 | constraint refinement | 2026 occultation synthesis tightens CH4 surface-pressure upper limit to 0.65 nbar at 3σ; this is consistent with, not contradictory to, previous non-detections. | NOT_A_CONFLICT |
| C003 | Hygiea | differentiation | hydrated-mineral evidence vs nearly spherical post-impact shape | construct mismatch | Hydration and sphericity do not establish internal differentiation. Keep differentiation `NA_UNCERTAIN / PARTIAL_OR_UNCERTAIN`. | RESOLVED_BY_CONSTRUCT_SEPARATION |
| C004 | Sedna/Gonggong | composition | rich surface ice/organic spectra vs unknown bulk interior | measurement-target mismatch | Do not promote surface spectroscopy to bulk composition. Keep `NA_UNCERTAIN / MIXED_UNCERTAIN`. | RESOLVED_BY_TARGET_SEPARATION |

## Batch-05 scan result

No new **unresolved** source conflict requiring `NA_SOURCE_CONFLICT` was identified. The dominant issue is measurement-target mismatch: surface spectroscopy is much better constrained than bulk interiors for distant TNOs.

## Rule

Use `NA_SOURCE_CONFLICT` only when credible sources remain materially incompatible after considering:
1. publication date,
2. measurement target,
3. direct observation vs model inference,
4. operational definition.

Do not manufacture a conflict when newer evidence merely tightens a bound or when two sources describe different layers of the same body.

## Readiness-targeted scan · Batch 06

| ID | Body | Variable | Sources | Type | Adjudication | Status |
|---|---|---|---|---|---|---|
| C005 | Haumea | differentiation | HAUMEA_OCCULTATION_2017 vs HAUMEA_STRUCTURE_APJ_2019 | observation vs model refinement | The occultation rules out a simple homogeneous hydrostatic interpretation; the later ApJ model shows a differentiated triaxial solution can fit the shape. Code MODEL_INFERRED / DIFFERENTIATED, not direct measurement. | RESOLVED_BY_EVIDENCE_LEVEL |
| C006 | Enceladus | atmosphere | plume descriptions vs NASA_ENCELADUS_LOCAL_ATMOSPHERE | construct clarification | Earlier protocol intentionally avoided equating a plume with an atmosphere. Cassini UVIS stellar occultation independently detected localized water-vapor atmosphere; code DIRECT_MEASURED / EXOSPHERE_TRACE. | RESOLVED_BY_DIRECT_DETECTION |
| C007 | Tethys | differentiation | TETHYS_SHAPE_1991 | model ambiguity | Shape analysis permits differentiation with a small rocky core but also discusses historical mass uncertainty. Keep MODEL_INFERRED / DIFFERENTIATED rather than STRONGLY_CONSTRAINED. | RESOLVED_BY_EVIDENCE_LEVEL |

Unresolved source conflicts requiring `NA_SOURCE_CONFLICT`: **0**.

## Readiness-targeted scan · Batch 07

| ID | Body | Variable | Sources | Type | Adjudication | Status |
|---|---|---|---|---|---|---|
| C008 | Phobos/Deimos | atmosphere | NASA_PHOBOS_AIRLESS / NASA_MARS_MOONS_AIRLESS | direct agency synthesis | Airless-body statements support `EVIDENCE_OF_ABSENCE / NONE_OR_NEGLIGIBLE`; no atmosphere is inferred from size alone. | RESOLVED |
| C009 | Ariel/Umbriel/Titania/Oberon | differentiation | URANUS_MOONS_INTERIORS_2023 | model-based interior layering | Ocean + ice-shell + rocky-layer models imply internal differentiation, but remain model inference rather than direct gravity-field measurement. | RESOLVED_BY_EVIDENCE_LEVEL |

Unresolved source conflicts requiring `NA_SOURCE_CONFLICT`: **0**.
