#!/usr/bin/env python3
"""ARIS4C018 Pilot 2C: capture synchronized neural/decoder/body/target trace.

Uses the same bounded configuration as Pilot 2B. The output is a JSON trace for
scientific auditing and the user-facing replay prototype. It is not a new
biological experiment.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import numpy as np

import pilot2b_bounded_closed_loop as p2b
from official_legacy_decoder import (
    object_mask_from_zscores,
    turning_from_object_mask,
)
from flygym_gymnasium import SingleFlySimulation
from flygym_gymnasium.examples.vision import MovingFlyArena


def capture_trace(baseline):
    arena = MovingFlyArena(move_speed=15, radius=10, terrain_type="flat")
    fly = p2b.make_fly(spawn_pos=(-5, 10, 0.3))
    sim = SingleFlySimulation(fly=fly, arena=arena)

    ommatidia_coms = np.empty((fly.retina.num_ommatidia_per_eye, 2))
    for i in range(fly.retina.num_ommatidia_per_eye):
        mask = fly.retina.ommatidia_id_map == i + 1
        ommatidia_coms[i, :] = np.argwhere(mask).mean(axis=0)

    obs, info = sim.reset(seed=0)
    dn_drive = np.array([1.0, 1.0])
    n_steps = int(p2b.CLOSED_LOOP_RUN_TIME_S / sim.timestep)
    frames = []
    zero_std_hits = 0

    for step in range(n_steps):
        if info.get("vision_updated", False):
            nn_activities = info["nn_activities"]
            zscores = []
            cell_mean_left = []
            cell_mean_right = []

            for cell in p2b.TRACKING_CELLS:
                activities = np.asarray(
                    fly.retina_mapper.flyvis_to_flygym(nn_activities[cell]),
                    dtype=float,
                )
                cell_mean_left.append(float(np.mean(activities[0])))
                cell_mean_right.append(float(np.mean(activities[1])))

                response_mean = baseline[cell]["mean"]
                response_std = baseline[cell]["std"]
                zero_mask = response_std <= 0
                zero_std_hits += int(np.count_nonzero(zero_mask))
                safe_std = np.where(zero_mask, np.nan, response_std)

                with np.errstate(divide="ignore", invalid="ignore"):
                    zscores.append(np.abs((activities - response_mean) / safe_std))

            obj_mask, mean_zscore = object_mask_from_zscores(np.asarray(zscores))
            decoded = turning_from_object_mask(
                obj_mask,
                ommatidia_coms,
                retina_nrows=fly.retina.nrows,
                retina_ncols=fly.retina.ncols,
                tracking_gain=p2b.TRACKING_GAIN,
            )
            dn_drive = decoded["dn_drive"]

            body_xy = np.asarray(obs["fly"])[0, :2].astype(float)
            target_xy = np.asarray(arena.fly_pos[:2], dtype=float)

            frames.append({
                "t_s": float(step * sim.timestep),
                "body": {
                    "x": float(body_xy[0]),
                    "y": float(body_xy[1]),
                    "heading": None,
                },
                "target": {
                    "x": float(target_xy[0]),
                    "y": float(target_xy[1]),
                },
                "decoder": {
                    "turning_bias": float(decoded["turning_bias"]),
                    "dn_left": float(dn_drive[0]),
                    "dn_right": float(dn_drive[1]),
                    "object_fraction_left": float(decoded["size_per_eye"][0]),
                    "object_fraction_right": float(decoded["size_per_eye"][1]),
                    "mean_zscore_max": float(np.max(mean_zscore)),
                },
                "neural": {
                    "source_layer": "BIO",
                    "summary": {
                        "selected_mean_left": float(np.mean(cell_mean_left)),
                        "selected_mean_right": float(np.mean(cell_mean_right)),
                        "selected_mean_abs": float(
                            np.mean(np.abs(cell_mean_left + cell_mean_right))
                        ),
                    },
                    "cell_mean_left": cell_mean_left,
                    "cell_mean_right": cell_mean_right,
                },
            })

        obs, _, _, _, info = sim.step(action=dn_drive)

    sim.close()
    assert len(frames) >= 20

    return frames, zero_std_hits


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "papers/018-drosophila-neural-simulation/data/pilot2c_synchronized_trace.json"
        ),
    )
    args = parser.parse_args()

    baseline, baseline_meta = p2b.collect_baseline()
    frames, zero_std_hits = capture_trace(baseline)

    payload = {
        "schema_version": 1,
        "provenance": {
            "model_stack": "legacy FlyGym 1.3.2 + flyvis 1.1.2",
            "source": (
                "ARIS4C018 bounded reproduction of "
                "NeLy-EPFL/flygym-gymnasium advanced vision"
            ),
            "upstream_commit": "d285260a1c8a7b3494150cd1590f2c9fe4b5e06b",
            "aris_commit": os.environ.get("GITHUB_SHA", ""),
            "workflow_run_id": os.environ.get("GITHUB_RUN_ID", ""),
            "scientific_boundary": (
                "BIO neural activity is connectome-constrained flyvis output; "
                "DECODER z-score/object-mask/turning mapping is engineered. "
                "Bounded trace is not evidence of successful following."
            ),
        },
        "configuration": {
            "baseline_run_time_s": p2b.BASELINE_RUN_TIME_S,
            "closed_loop_run_time_s": p2b.CLOSED_LOOP_RUN_TIME_S,
            "vision_refresh_rate_hz": p2b.VISION_REFRESH_RATE,
            "tracking_gain": p2b.TRACKING_GAIN,
            "z_score_threshold": p2b.Z_SCORE_THRESHOLD,
            "tracking_cells": p2b.TRACKING_CELLS,
        },
        "baseline": baseline_meta,
        "zero_std_positions_encountered": zero_std_hits,
        "cell_order": p2b.TRACKING_CELLS,
        "frames": frames,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )

    print("ARIS4C018 Pilot2C synchronized trace PASS")
    print(f"trace_frames={len(frames)}")
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
