# Research Plan · ARIS4C022

## 1. Research object

The unit is a **planetary body**, not a galaxy. The user’s motivating examples concern Mars, planets, moons, composition, distance from the Sun, and physical formulas; therefore the relevant level is planetary-system taxonomy.

## 2. Primary framing

This project transfers QCA from its usual causal/configurational use into a **set-theoretic taxonomy audit**.

That distinction is frozen:

- If outcome = official IAU class, the analysis evaluates configurational correspondence with a classification rule.
- It does **not** prove that a category label was physically caused by the conditions.
- Physical mechanism claims require independent planetary-science theory and evidence.

## 3. Research questions

### RQ1 · Necessary conditions
Which conditions are empirically necessary for membership in the Solar-System “planet” set?

Candidate families:
- direct orbit around the Sun / central star;
- hydrostatic-equilibrium / near-roundness;
- dynamical dominance / orbital clearing;
- mass-size regime;
- composition / differentiation;
- atmosphere / volatile retention;
- thermal-geological state.

### RQ2 · Sufficient configurations
Which conjunctions are sufficient for:
- PLANET,
- DWARF_PLANET,
- SATELLITE,
- SMALL_BODY?

Each outcome is analysed separately; QCA is not intrinsically multinomial.

### RQ3 · Intuitive vs defining features
Do intuitive features such as mass, diameter, density, atmosphere, mineral/gas composition, or geological activity retain discriminative value once orbital hierarchy and dynamical dominance are included?

### RQ4 · Quantitative dynamics
How well do quantitative dynamical criteria reproduce the observed planet/non-planet separation?

Primary candidates:
- Margot planet discriminant / orbit-clearing criterion;
- Soter planetary discriminant;
- Hill-sphere and host/primary relations.

### RQ5 · Boundary cases
Which cases expose classification tensions or non-intuitive boundaries?
Examples include large moons, dwarf planets, and nearly round asteroids.

Mars is a **positive-control planet**, not an unresolved planet-vs-satellite case.

## 4. Case frame · Phase 1

Target N: roughly 40–60 Solar-System bodies.

Strata:
1. 8 major planets;
2. 5 officially recognized dwarf planets;
3. large and medium natural satellites;
4. representative main-belt / trans-Neptunian / other small bodies;
5. explicit boundary cases.

Sampling must not be “largest bodies only”; otherwise size is structurally biased toward the outcome.

## 5. Data layers

### A. Orbital hierarchy
- primary orbited;
- direct stellar orbit vs satellite orbit;
- semimajor axis;
- eccentricity;
- inclination;
- orbital period;
- Hill relation / barycentric context where relevant.

### B. Dynamical dominance
- Margot-style discriminant;
- Soter-style discriminant where data permit;
- clearing-time or neighborhood-dominance proxies.

### C. Bulk physics
- mass;
- mean / equatorial radius;
- density;
- surface gravity;
- escape velocity;
- rotation.

### D. Composition
- rock/metal fraction where estimable;
- ice/volatile indicators;
- gas-envelope status;
- atmospheric pressure and major constituents;
- differentiation / core evidence.

### E. Evolution / activity
- geological activity;
- tidal heating;
- atmosphere retention/loss;
- inferred formation/evolutionary class;
- age only when meaningfully comparable.

### F. Stellar environment
- distance / semimajor axis;
- insolation;
- equilibrium temperature;
- physically normalized distance (e.g. relative to snow line) for later extrasolar extension.

## 6. Formula registry

Use derived variables transparently and never treat mathematically redundant measures as independent evidence.

- Mean density: `rho = M / ((4/3) pi R^3)`
- Surface gravity: `g = GM / R^2`
- Escape speed: `v_esc = sqrt(2GM/R)`
- Kepler period: `P^2 = 4 pi^2 a^3 / (G(M_* + M_p))`
- Hill radius: `r_H ≈ a (M_p/(3M_*))^(1/3)`
- Insolation: `S ∝ L_*/a^2`
- Equilibrium temperature (simplified): `T_eq ≈ T_* sqrt(R_*/(2a)) (1-A)^(1/4)`
- Soter discriminant: `mu = M / m` where `m` is the mass sharing the orbital zone.
- Margot-style dynamical discriminant: compute from the published criterion with pinned units and constants; do not reimplement from memory.

## 7. Anti-circularity rules

1. Do not include a condition that is merely a restatement of the outcome.
2. For IAU-label replication, label-defining variables are explicitly marked “definitional benchmark”.
3. Discovery analyses must separate benchmark conditions from exploratory physical features.
4. Mass, radius, density, gravity, escape velocity and related terms are strongly dependent; they are grouped into a condition family and not all entered simultaneously as if independent.
5. Distance from the Sun is not interpreted as a universal planet criterion.
6. Composition/lifecycle variables are not forced into a planet definition merely because they are scientifically interesting.

## 8. QCA workflow

1. Freeze case frame.
2. Freeze raw-variable dictionary and provenance.
3. Pre-register calibration anchors.
4. Produce raw + calibrated matrix.
5. Test necessity for Y and ~Y.
6. Build truth tables with declared frequency / consistency / PRI thresholds.
7. Report complex, intermediate and parsimonious solutions.
8. Report raw and unique coverage.
9. Inspect contradictory rows and deviant cases.
10. Run calibration perturbation and leave-one-case-out sensitivity.
11. Compare with a non-QCA descriptive companion: clustering / PCA or UMAP only as exploratory geometry.
12. Interpret configurations using planetary-science mechanisms, not QCA metrics alone.

## 9. First falsification gates

The study is weakened if:
- QCA merely reproduces an outcome because its exact definition was entered as conditions;
- alternative calibrations change all substantive pathways;
- only size/mass sampling creates the planet/non-planet split;
- dynamical dominance does not separate known benchmark cases;
- missing composition/activity data systematically remove small bodies or satellites;
- claims use causal verbs when only taxonomic set relations were tested.

## 10. Primary sources

- IAU Resolution B5/B6 and current IAU FAQ on the Solar-System planet definition.
- NASA/NSSDC Planetary Fact Sheets.
- NASA Solar System Exploration / planet and dwarf-planet resources.
- JPL Solar System Dynamics.
- Margot (2015), *A Quantitative Criterion for Defining Planets*, AJ 150:185.
- Margot, Gladman & Yang (2024), *Quantitative Criteria for Defining Planets*.
- Soter (2006), *What Is a Planet?*
- R package **QCA** methodology paper and COMPASSS QCA guidance.

See `../data/SOURCE_REGISTRY.md`.
