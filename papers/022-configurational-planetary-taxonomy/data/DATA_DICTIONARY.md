# Data Dictionary · Pilot-0

Version: 0.2 · 2026-09-24

One row is one named Solar-System body in the frozen Pilot-0 case frame. Raw/catalogued values stay separate from derived values. Every nontrivial numeric field requires source, retrieval date, unit, and uncertainty/provenance.

## Identity and outcome fields

- case_id: stable study-local identifier
- name: canonical English body name
- official_class: planet / dwarf_planet / satellite / small_body
- primary_body: direct dynamical primary
- direct_sun_orbit: binary direct Solar orbit
- is_satellite: binary natural-satellite indicator
- boundary_tag: why the case is scientifically useful near a classification boundary

## Provenance / ingestion fields

- source_key: controlled source route such as JPL_PLANET_PHYS / JPL_SAT_PHYS / JPL_SBDB_API
- retrieved_date: retrieval date in YYYY-MM-DD
- ingestion_status: INGESTED_CORE / NA_NOT_INGESTED / explicit scientific missingness state
- mass_value_type: DIRECT_TABLE / DERIVED_FROM_GM_CODATA2018 / later controlled values
- gm_ref: JPL ephemeris/reference identifier when GM is the source quantity
- notes: deterministic conversion or source caveat, never a substitute for machine-readable source metadata

## Raw physical fields

Canonical target fields:
- mass_kg
- mass_sigma_kg
- gm_km3_s2
- gm_sigma_km3_s2
- mean_radius_km
- radius_sigma_km
- diameter_km
- density_kg_m3
- rotation_period_h
- surface_pressure_pa
- albedo_bond

Current v0.1 physical snapshot preserves JPL-native `density_g_cm3` and `geometric_albedo`; the analysis matrix will normalize density to kg/m3 and must not silently relabel geometric albedo as Bond albedo.

For satellites, JPL often supplies GM as the primary dynamical measurement. Where `mass_kg` is present with `mass_value_type=DERIVED_FROM_GM_CODATA2018`, it is deterministically derived using:

`M = GM / G`, with `G = 6.67430e-20 km^3 kg^-1 s^-2`.

## Orbital hierarchy fields

- heliocentric_semimajor_axis_au: direct-Sun orbit scale
- primary_orbit_semimajor_axis_km: satellite-to-primary scale
- orbital_period_days
- eccentricity
- inclination_deg
- primary_mass_kg
- host_solar_distance_au: inherited stellar environment for satellites

Never mix planetocentric and heliocentric semimajor axes into one condition.

## Composition, atmosphere, and evolution

- composition_class
- rock_metal_fraction_est
- ice_volatile_fraction_est
- h_he_envelope
- atmosphere_present
- atmosphere_major_species
- differentiated
- current_geologic_activity
- tidal_heating_relevant
- subsurface_ocean_evidence

Model-estimated interior fractions must be labeled as estimates, not direct measurements.

## Derived physics

- density_derived = M / ((4/3) pi R^3)
- surface_gravity_derived = G M / R^2
- escape_velocity_m_s = sqrt(2 G M / R)
- hill_radius_m approximately equals a (M/(3 M_primary))^(1/3)
- insolation_rel_earth = (L_star/L_sun) / a_AU^2
- equilibrium_temperature_K only with explicit albedo and redistribution assumptions

Raw source columns and normalized/derived columns must remain separable.

## Dynamical dominance

Keep each published criterion separately:
- margot_discriminant_raw
- margot_threshold
- margot_member
- soter_mu

Implementation is pinned in `code/dynamics_metrics.py`:
- Margot (2015) Eq. 8, Eq. 9, Eq. 10
- Soter (2006) mu = M / m

Soter mu additionally requires an explicit orbital-zone mass census; it must not be synthesized from the focal body's own physical fields.

## Fuzzy-set calibration

Raw values and calibrated memberships live in separate tables. Each fuzzy set requires explicit full-out, crossover, and full-in anchors. Sample quantiles alone are not the default scientific justification.

## Missingness

Use explicit states:
- NA_NOT_APPLICABLE
- NA_NOT_MEASURED
- NA_UNCERTAIN
- NA_SOURCE_CONFLICT
- NA_NOT_INGESTED

Never coerce these to zero.
