# Evidence coding audit · Batch 02 moon/boundary set

Date: 2026-09-24

## Scope

Batch 02 codes nine high-information satellite/boundary cases:

Moon, Io, Europa, Ganymede, Callisto, Enceladus, Titan, Triton, Charon.

They are deliberately chosen because several are physically planet-like while remaining satellites, making them critical M2/M3 counterexamples.

## New methodological clarification

The canonical `ocean_value` now refers to **evidence for a present-day or plausibly persistent subsurface liquid ocean**, not merely evidence that an ocean existed in the distant past.

Therefore:
- Europa / Ganymede / Enceladus / Titan can receive current-ocean evidence codes.
- Callisto remains uncertain/candidate.
- Charon's evidence for a long-past water-ice ocean is preserved in notes and source registry, but does **not** populate `ocean_value`.

This prevents paleogeologic evidence from being collapsed into current habitability/geophysics.

## Coverage after batches 01 + 02

| Dimension | non-pending / 50 |
|---|---:|
| composition | 19 |
| atmosphere | 18 |
| differentiation | 18 |
| geological activity | 9 |
| present/persistent ocean evidence | 5 |
| tidal heating | 13 |

Total: **82/300** evidence-state cells non-pending.

Batch 02 advanced **41** additional cells.

## Conservative decisions

- Europa current geological activity is `NA_UNCERTAIN / UNCERTAIN`: NASA reports possible active venting, not a settled detection.
- Callisto ocean is `NA_UNCERTAIN / CANDIDATE`: NASA explicitly notes it may exist or may not.
- Enceladus atmosphere remains pending because a plume/gaseous envelope is not automatically equivalent to a stable gravitationally bound atmosphere.
- Titan geological activity is coded current/recent only for NASA-described tectonic forces/processes; cryovolcanism itself remains uncertain and is not separately asserted.
- Charon is `PAST_ONLY` geologically; NASA/NTRS synthesis says it is not currently active but experienced ancient tectonism/resurfacing.

## Firewall

Every row remains `UNEXPOSED_TO_QCA_RESULT`. No calibration anchors, truth table, consistency score, coverage score, or solution term was inspected.
