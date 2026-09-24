# M2 primary-condition freeze · ARIS4C022

Version 0.1 · 2026-09-24

This freeze occurs **before any fsQCA calibration, truth table, consistency/coverage statistic, or solution term is inspected**.

## Outcome

Primary M2 outcome: `PLANET` = current IAU major-planet label.

The purpose is descriptive/taxonomic stress-testing: ask whether a compact set of **non-definitional physical traits** reproduces the official label. It is not a causal model of why a body became a planet.

## Frozen five-condition primary specification

| Family | Primary representative | Why this representative | Current substantive coverage |
|---|---|---|---:|
| SCALE | `escape_velocity_m_s` | integrates mass and radius into a physically meaningful scale/retention quantity; avoids entering mass, radius, surface gravity together | 34/50 |
| BULK_MATERIAL | `density_from_mass_radius_g_cm3` | quantitative bulk-material proxy available across rocky/icy/gas bodies; **not** treated as literal composition | 34/50 |
| ATMOSPHERE_RETENTION | evidence-coded `atmosphere_value` | staged retention state is more comparable than heterogeneous pressure measurements | 25/50 substantive values |
| INTERNAL_ORGANIZATION | evidence-coded `differentiation_value` | cross-class internal-structure construct; preferred over geology because geology lacks measurement equivalence between gas giants and solid worlds | 32/50 substantive values |
| SOLAR_ENERGY | `insolation_rel_earth` | physically interpretable stellar-energy environment; use one energy/distance representative only | 34/50 |

Current complete cases on all five: **19/50**:
Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Ceres, Pluto, Moon, Io, Europa, Ganymede, Callisto, Dione, Rhea, Titan, Triton.

Current complete-case strata: 8 planets, 2 dwarf planets, 9 satellites, 0 small/boundary bodies.

Therefore **M2 is not calibration-ready**.

## Why INTERNAL_ACTIVITY was moved out of the primary five

Pilot-0 proposed INTERNAL_ACTIVITY. Evidence review showed that `geologic_activity` does not have stable measurement semantics across the full case universe: volcanism/resurfacing is meaningful for solid bodies, while giant planets have intrinsic heat and convective/atmospheric dynamics rather than comparable surface geology.

Before result inspection, the primary family is therefore revised to **INTERNAL_ORGANIZATION / differentiation**. Geology, ocean evidence and tidal heating remain scientifically important but enter sensitivity / M4 analyses rather than the primary M2 specification.

## Composition handling

The categorical composition ontology is **not converted into an arbitrary single ordinal fuzzy scale**.

Primary M2 uses bulk density as a material-state proxy. The evidence-coded composition classes remain for:
- mvQCA sensitivity,
- stratified interpretation,
- alternative specifications,
- periodic-table-style visualization.

This prevents an unjustified ordering such as ROCK_METAL < CARBONACEOUS_HYDRATED < ROCK_ICE_MIXED < H_HE_ENVELOPE.

## Explicitly prohibited M2 conditions

The following may not enter M2 as conditions:

- `official_class` or any recoding of PLANET except as the outcome;
- `direct_sun_orbit`;
- `is_satellite`;
- `primary_body` or orbital-hierarchy labels;
- IAU cleared-neighborhood labels;
- Margot Pi / membership;
- Soter mu / membership;
- ROUND / hydrostatic-equilibrium classification;
- `boundary_tag`;
- any variable directly constructed from the outcome label.

These belong to M0/M1/M3 or descriptive metadata, not anti-circularity M2.

## Redundancy rule

Never enter algebraically coupled representatives together in the primary model.

Examples:
- escape velocity excludes simultaneous mass + radius + surface gravity;
- density excludes a second density reconstructed from the same mass/radius inputs;
- insolation excludes simultaneous heliocentric distance or equilibrium temperature in the same primary specification.

Alternatives may appear in sensitivity runs one-at-a-time.

## Pre-calibration readiness gates

No primary M2 calibration is allowed until all of the following are true:

1. each primary condition has **>=40/50 substantive, non-missing case values**;
2. the five-condition complete-case set has **>=35/50 cases**;
3. all 8 major planets remain complete;
4. complete non-planet coverage includes at least:
   - 4/5 dwarf planets,
   - 12/21 satellites,
   - 10/16 small/boundary bodies;
5. remaining missingness is audited by scientific reason, not silently imputed;
6. calibration anchors are justified from theory/physics or explicit evidence rubrics before solution inspection.

If these gates cannot be met, M2 is reported as exploratory/incomplete; the model is not rescued by post-hoc condition deletion after seeing results.

## Sensitivity families frozen in advance

Allowed substitutions, one family at a time:

- SCALE: mass or mean radius instead of escape velocity.
- BULK_MATERIAL: evidence-coded composition via mvQCA or class contrasts instead of density.
- ATMOSPHERE_RETENTION: comparable surface pressure where valid instead of staged evidence.
- INTERNAL_ORGANIZATION: geologic activity, ocean evidence, or tidal heating as separate sensitivity models; do not merge them post hoc to improve fit.
- SOLAR_ENERGY: heliocentric/host distance or equilibrium-temperature proxy instead of insolation.

## Anti-circularity state

At freeze time:
- QCA solutions inspected: **0**
- calibration anchors inspected/tuned: **0**
- truth-table rows inspected: **0**
- outcome-fit statistics inspected: **0**
