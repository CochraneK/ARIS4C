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
