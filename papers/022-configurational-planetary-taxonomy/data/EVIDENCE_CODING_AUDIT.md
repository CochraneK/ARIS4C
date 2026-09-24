# Evidence coding audit · Anchor batch 01

Date: 2026-09-24

## Scope

The first blinded evidence-coding batch covers **10 anchor bodies**:

Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Ceres, Pluto.

No QCA truth table, solution term, calibration score, or model fit was inspected before or during coding.

## Coding completed

- Composition: 10/50
- Atmosphere: 10/50
- Differentiation: 10/50
- Geological activity: 1/50 (Mars only; the NASA page explicitly describes extinct volcanoes)
- Tidal heating: 10/50 coded `NA_NOT_APPLICABLE` under the frozen direct-Sun default
- Ocean evidence: 0/50; deliberately deferred because "ocean" requires a more precise operational distinction between surface liquid reservoirs, subsurface liquid-water oceans, and deep high-pressure planetary fluids.

Total non-pending state cells in this batch: **41 / 300**.

## Source policy

Each populated scientific value points to an agency facts page rather than a generic secondary summary. The anchor batch intentionally favors conservative coding:

- Mercury's "atmosphere" is coded as `EXOSPHERE_TRACE`, not as a conventional atmosphere.
- Ceres' water-vapor evidence is coded `EXOSPHERE_TRACE` with `STRONGLY_CONSTRAINED`, not `DIRECT_MEASURED/SUBSTANTIAL`.
- Jupiter's internal differentiation remains `PARTIAL_OR_UNCERTAIN` / `MODEL_INFERRED` because NASA still describes core structure as uncertain.
- Earth-like solid/liquid "ocean" and giant-planet deep fluid layers are not collapsed into one construct.

## Anti-circularity firewall

All 50 rows retain `review_status=UNEXPOSED_TO_QCA_RESULT`. The remaining cells stay `PENDING_REVIEW`; they are not converted to absence or zero.
