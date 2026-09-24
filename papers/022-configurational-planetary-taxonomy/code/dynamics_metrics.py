"""Published dynamical-dominance metrics used by ARIS4C022.

Equations are implemented from the source papers, not reconstructed as labels.

Margot (2015), arXiv:1507.06300:
- Eq. 8: general minimum orbit-clearing mass.
- Eq. 9: main-sequence-lifetime specialization.
- Eq. 10: Pi = M_body / M_clear.

Soter (2006), arXiv:astro-ph/0608359:
- mu = M / m, where m is the aggregate mass of other bodies sharing the orbital zone.
"""

from __future__ import annotations

import math

DEFAULT_C = 2.0 * math.sqrt(3.0)


def margot_mclear_general_earth_masses(
    semimajor_axis_au: float,
    host_mass_solar: float = 1.0,
    characteristic_time_years: float = 1.0e10,
    c_hill: float = DEFAULT_C,
) -> float:
    """Margot 2015 Eq. 8, returned in Earth masses."""
    if min(semimajor_axis_au, host_mass_solar, characteristic_time_years, c_hill) <= 0:
        raise ValueError("all inputs must be positive")
    return (
        c_hill ** 1.5
        * host_mass_solar ** (5.0 / 8.0)
        * (characteristic_time_years / 1.1e5) ** (-3.0 / 4.0)
        * semimajor_axis_au ** (9.0 / 8.0)
    )


def margot_mclear_main_sequence_earth_masses(
    semimajor_axis_au: float,
    host_mass_solar: float = 1.0,
    c_hill: float = DEFAULT_C,
) -> float:
    """Margot 2015 Eq. 9, returned in Earth masses."""
    if min(semimajor_axis_au, host_mass_solar, c_hill) <= 0:
        raise ValueError("all inputs must be positive")
    return (
        1.9e-4
        * c_hill ** 1.5
        * host_mass_solar ** 2.5
        * semimajor_axis_au ** (9.0 / 8.0)
    )


def margot_pi(
    body_mass_earth: float,
    semimajor_axis_au: float,
    host_mass_solar: float = 1.0,
    c_hill: float = DEFAULT_C,
) -> float:
    """Margot 2015 Eq. 10 using the Eq. 9 main-sequence clearing mass."""
    if body_mass_earth <= 0:
        raise ValueError("body_mass_earth must be positive")
    return body_mass_earth / margot_mclear_main_sequence_earth_masses(
        semimajor_axis_au=semimajor_axis_au,
        host_mass_solar=host_mass_solar,
        c_hill=c_hill,
    )


def soter_mu(body_mass: float, other_orbital_zone_mass: float) -> float:
    """Soter 2006 planetary discriminant mu = M / m.

    Inputs can use any common mass unit. The result is dimensionless.
    """
    if body_mass <= 0 or other_orbital_zone_mass <= 0:
        raise ValueError("masses must be positive")
    return body_mass / other_orbital_zone_mass


if __name__ == "__main__":
    # Published Margot table gives Earth Pi about 8.1e2 and Mars about 5.4e1.
    earth = margot_pi(1.0, 1.0)
    mars = margot_pi(0.107, 1.523679)
    print(f"Earth Pi ~ {earth:.1f}")
    print(f"Mars Pi  ~ {mars:.1f}")
