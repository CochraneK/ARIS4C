# Evidence coding audit · Batch 03 mid-moons + remaining dwarf planets

Date: 2026-09-24

## Scope

Primary Batch-03 cases:
Phobos, Deimos, Mimas, Tethys, Dione, Rhea, Iapetus, Miranda, Ariel, Umbriel, Titania, Oberon, Haumea, Makemake, Eris.

Two previously coded cases also receive newly sourced ocean/geology updates:
Pluto and Triton.

## Coverage after Batch 03

| Dimension | non-pending / 50 |
|---|---:|
| composition | 34 |
| atmosphere | 24 |
| differentiation | 24 |
| geological activity | 23 |
| present/persistent ocean evidence | 14 |
| tidal heating | 20 |

Total: **139/300** non-pending cells. Batch 03 advanced **57** cells.

## Important decisions

- **Mimas:** 2024 Nature orbital-dynamics work is treated as a substantive update over older "frozen solid" expectations. Ocean = `STRONG_EVIDENCE`; the discrepancy is logged as temporal supersession rather than hidden.
- **Dione:** subsurface ocean remains `MODEL_INFERRED / CANDIDATE`, not near-consensus.
- **Rhea:** homogeneous ice-rock mixture supports an undifferentiated coding; its oxygen/CO2 exosphere is directly detected.
- **Uranian moons:** 2023 JPL modeling gives Ariel/Umbriel/Titania/Oberon candidate oceans; Miranda receives model-based no-current-ocean evidence. These are not promoted to direct measurements.
- **Haumea/Makemake/Eris:** explicit NASA statements of limited structural knowledge are encoded as `NA_NOT_MEASURED` rather than guessed values.
- **Makemake atmosphere:** possible thin perihelion atmosphere remains `NA_UNCERTAIN`.
- **Pluto/Triton:** NASA Ocean Worlds supports candidate-ocean coding; Triton stays uncertain.

## Firewall

All 50 rows remain `UNEXPOSED_TO_QCA_RESULT`. No fsQCA calibration anchor, truth table, consistency, PRI, coverage, or solution term has been inspected.
