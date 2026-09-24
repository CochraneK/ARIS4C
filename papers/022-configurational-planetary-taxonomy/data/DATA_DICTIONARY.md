# Data Dictionary · Pilot-0

Version: 0.1 · 2026-09-24

One row is one named Solar-System body in the frozen Pilot-0 case frame. Raw/catalogued values stay separate from derived values. Every nontrivial numeric field requires source, retrieval date, unit, and uncertainty/provenance.

## Identity and outcome fields

- case_id: stable study-local identifier
- name: canonical English body name
- official_class: planet / dwarf_planet / satellite / small_body
- primary_body: direct dynamical primary
- direct_sun_orbit: binary direct Solar orbit
- is_satellite: binary natural-satellite indicator
- boundary_tag: why the case is scientifically useful near a classification boundary

## Raw physical fields

- mass_kg
- mean_radius_km
- diameter_km
- density_kg_m3
- rotation_period_h
- surface_pressure_pa
- albedo_bond

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

## Dynamical dominance

Keep each published criterion separately:
- margot_discriminant_raw
- margot_threshold
- margot_member
- soter_mu

Published equations and units must be implemented from source papers, never reconstructed from memory.

## Fuzzy-set calibration

Raw values and calibrated memberships live in separate tables. Each fuzzy set requires explicit full-out, crossover, and full-in anchors. Sample quantiles alone are not the default scientific justification.

## Missingness

Use explicit states:
- NA_NOT_APPLICABLE
- NA_NOT_MEASURED
- NA_UNCERTAIN
- NA_SOURCE_CONFLICT

Never coerce these to zero.
