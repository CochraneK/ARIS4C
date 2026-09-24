# Variables & Calibration Scaffold · ARIS4C022

This file is a pre-analysis scaffold, not a frozen preregistration. Thresholds must be justified from theory / natural breakpoints / published criteria before outcome inspection.

## Outcomes

| Outcome | Type | First-pass definition |
|---|---|---|
| PLANET | crisp benchmark | Current IAU Solar-System major-planet label |
| DWARF_PLANET | crisp benchmark | Current IAU dwarf-planet label |
| SATELLITE | crisp | Bound natural body whose primary is a nonstellar body |
| DYN_DOM | fuzzy | Membership in strong dynamical dominance, calibrated from published quantitative discriminants |
| ROUND | fuzzy/crisp sensitivity | Degree of hydrostatic-equilibrium / near-roundness evidence |

QCA runs each outcome separately.

## Condition families

| Family | Candidate variables | QCA role | Warning |
|---|---|---|---|
| ORBITAL_HIERARCHY | primary type, direct stellar orbit, satellite orbit | primary | conceptually prior to many class labels |
| DYNAMICAL_DOMINANCE | Margot Pi/criterion, Soter mu, clearing time | primary | use published formulas / units exactly |
| SELF_GRAVITY | roundness, hydrostatic-equilibrium evidence | primary | observational uncertainty for small bodies |
| BULK_SCALE | mass, radius/diameter | primary + sensitivity | do not enter all derived scale variables together |
| BULK_STRUCTURE | density, moment-of-inertia proxy, differentiation | secondary | data completeness varies |
| ATMOSPHERE | pressure, atmospheric mass, major gases | exploratory | absence may reflect retention + temperature + mass |
| COMPOSITION | rock/metal, ice/volatile, gas-envelope class | exploratory | heterogeneous measurement/model uncertainty |
| THERMAL_GEOLOGY | volcanism, resurfacing, tidal heating, heat flux | exploratory | current activity != formation class |
| STELLAR_ENVIRONMENT | semimajor axis, insolation, T_eq, snow-line-normalized distance | sensitivity | absolute AU is Solar-System-specific |
| EVOLUTION | age, atmospheric loss, differentiation history | exploratory | avoid vague “lifecycle” coding without an operational definition |

## Redundancy map

The following are linked mathematically and cannot be treated as orthogonal evidence:

- mass + radius -> density;
- mass + radius -> surface gravity;
- mass + radius -> escape velocity;
- star mass + semimajor axis -> orbital period (approximately);
- star luminosity + semimajor axis -> insolation;
- mass + host mass + semimajor axis -> Hill radius;
- mass + host mass + orbit -> several dynamical-dominance metrics.

Primary QCA models should select **one representative per tightly coupled family**, then use alternatives in sensitivity runs.

## Calibration plan

### Crisp conditions
Use 0/1 only for genuinely categorical relations such as:
- directly orbits the Sun;
- orbits a planet / dwarf planet;
- official IAU benchmark label.

### Fuzzy conditions
Use theory-anchored full-out / crossover / full-in points.

Candidate examples:
- DYN_DOM: anchor on published planet discriminant values / threshold, not sample quartiles.
- MASSIVE / LARGE: only if a substantively meaningful physical threshold can be defended; otherwise treat as sensitivity.
- ROUND: combine shape measurements + accepted hydrostatic-equilibrium assessments, with uncertainty flags.
- ATMOSPHERE_RICH: calibrate from surface pressure / atmospheric mass only if cross-case comparability is defensible.
- GEO_ACTIVE: use an evidence rubric with explicit present / uncertain / absent states.

## Consistency / coverage

Thresholds are to be frozen before solution inspection. Report:
- necessity consistency + coverage;
- sufficiency consistency;
- PRI;
- raw coverage;
- unique coverage;
- solution coverage / consistency;
- contradictory truth-table rows.

No single universal cutoff will be treated as a law; threshold sensitivity is mandatory.

## Mars check

Mars should satisfy:
- direct orbit around the Sun;
- near-round/self-gravitating;
- strong dynamical dominance under published quantitative criteria.

It is therefore a positive-control PLANET case. Its two moons are separate SATELLITE cases and must not be collapsed into the Mars row.
