#!/usr/bin/env python3
"""ARIS4C018 Pilot 0: transparent toy ring-attractor robustness sandbox.

This is NOT a validated Drosophila central-complex model. It is a deliberately
small rate-network toy used to validate the experiment/visualization pipeline
before substituting published circuit models.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import numpy as np


def wrap_angle(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


@dataclass
class Result:
    heading_error_deg: float
    bump_concentration: float
    recovery_s: float | None


def simulate(seed=0, lesion_fraction=0.0, weight_noise=0.05, steps=800, dt=0.05, n_units=32):
    rng = np.random.default_rng(seed)
    pref = np.linspace(-np.pi, np.pi, n_units, endpoint=False)

    w = (1.8 * np.cos(pref[:, None] - pref[None, :]) - 0.5) / n_units
    w *= 1 + rng.normal(0, weight_noise, w.shape)

    alive = np.ones(n_units, dtype=bool)
    n_dead = int(round(n_units * lesion_fraction))
    if n_dead:
        dead = rng.choice(n_units, n_dead, replace=False)
        alive[dead] = False
        w[~alive, :] = 0
        w[:, ~alive] = 0

    rates = np.maximum(0, 0.3 + 0.05 * rng.normal(size=n_units))
    headings, targets, concentrations = [], [], []
    tau = 0.15

    for t in range(steps):
        target = 0.0 if t < steps // 2 else np.pi / 2
        sensory = 1.2 * np.maximum(0, np.cos(pref - target))
        sensory[~alive] = 0

        drive = w @ rates + sensory + 0.02 * rng.normal(size=n_units)
        rates += dt / tau * (-rates + np.maximum(0, drive))
        rates[~alive] = 0

        population_vector = np.sum(rates * np.exp(1j * pref))
        heading = np.angle(population_vector) if abs(population_vector) > 1e-12 else 0.0
        concentration = abs(population_vector) / (rates.sum() + 1e-9)

        headings.append(heading)
        targets.append(target)
        concentrations.append(concentration)

    error = np.abs(wrap_angle(np.asarray(headings) - np.asarray(targets)))

    mask = np.ones(steps, dtype=bool)
    mask[:100] = False
    mask[steps // 2: steps // 2 + 100] = False

    heading_error_deg = float(np.degrees(np.mean(error[mask])))
    bump_concentration = float(np.mean(np.asarray(concentrations)[mask]))

    threshold = np.deg2rad(15)
    after_switch = error[steps // 2:]
    recovery_s = None
    for i in range(max(0, len(after_switch) - 20)):
        if np.all(after_switch[i:i + 20] < threshold):
            recovery_s = float(i * dt)
            break

    return Result(heading_error_deg, bump_concentration, recovery_s)


def summarize(lesion_levels, seeds):
    rows = []
    for lesion in lesion_levels:
        results = [simulate(seed, lesion) for seed in range(seeds)]
        errors = np.asarray([x.heading_error_deg for x in results])
        concentrations = np.asarray([x.bump_concentration for x in results])
        recovery = np.asarray(
            [np.nan if x.recovery_s is None else x.recovery_s for x in results],
            dtype=float,
        )
        rows.append({
            "lesion_fraction": lesion,
            "n_seeds": seeds,
            "mean_heading_error_deg": float(errors.mean()),
            "sd_heading_error_deg": float(errors.std(ddof=1)),
            "mean_bump_concentration": float(concentrations.mean()),
            "mean_recovery_s": float(np.nanmean(recovery)),
            "recovery_success_rate": float(np.isfinite(recovery).mean()),
        })
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=50)
    parser.add_argument("--output", type=Path, default=Path("data/pilot0_summary.csv"))
    args = parser.parse_args()

    rows = summarize([0.0, 0.1, 0.2, 0.3, 0.4], args.seeds)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    for row in rows:
        print(
            f"lesion={row['lesion_fraction']:.1f} "
            f"error={row['mean_heading_error_deg']:.3f}deg "
            f"recovery_success={row['recovery_success_rate']:.2f}"
        )


if __name__ == "__main__":
    main()
