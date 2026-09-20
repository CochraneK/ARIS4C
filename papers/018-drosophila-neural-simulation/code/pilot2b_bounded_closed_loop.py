#!/usr/bin/env python3
"""ARIS4C018 Pilot 2B: bounded reproduction of the official legacy fly-following decoder.

This script uses:
- the official legacy RealisticVisionFly;
- pretrained flyvis visual dynamics;
- real retinal rendering;
- a real MovingFlyArena target;
- the decoder equations from follow_fly_closed_loop.py.

To keep CI bounded, baseline and closed-loop durations are much shorter than the
published 3 s condition. This is an engineering reproduction gate, not a paper-result
replication.
"""

from __future__ import annotations

import json
import math
import numpy as np

from flygym_gymnasium import SingleFlySimulation
from flygym_gymnasium.arena import FlatTerrain
from flygym_gymnasium.examples.vision import MovingFlyArena, RealisticVisionFly


CONTACTS = [
    f"{leg}{segment}"
    for leg in ["LF", "LM", "LH", "RF", "RM", "RH"]
    for segment in ["Tibia", "Tarsus1", "Tarsus2", "Tarsus3", "Tarsus4", "Tarsus5"]
]

# Exact upstream LC9/LC10-input selection.
TRACKING_CELLS = [
    "T2", "T2a", "T3",
    "Tm1", "Tm2", "Tm3", "Tm4", "Tm5Y", "Tm5a", "Tm5b", "Tm5c",
    "Tm9", "Tm16", "Tm20", "Tm28", "Tm30",
    "TmY3", "TmY4", "TmY5a", "TmY9", "TmY10", "TmY13", "TmY14",
    "TmY15", "TmY18",
]

VISION_REFRESH_RATE = 500
Z_SCORE_THRESHOLD = 5.0
TRACKING_GAIN = 6.0
BASELINE_RUN_TIME_S = 0.20
CLOSED_LOOP_RUN_TIME_S = 0.20


def make_fly(*, spawn_pos=None):
    kwargs = dict(
        contact_sensor_placements=CONTACTS,
        enable_adhesion=True,
        vision_refresh_rate=VISION_REFRESH_RATE,
        neck_kp=500,
        head_stabilization_model=None,
    )
    if spawn_pos is not None:
        kwargs["spawn_pos"] = spawn_pos
    return RealisticVisionFly(**kwargs)


def collect_baseline():
    fly = make_fly()
    sim = SingleFlySimulation(fly=fly, arena=FlatTerrain())
    obs, info = sim.reset(seed=0)

    samples = {cell: [] for cell in TRACKING_CELLS}
    n_steps = int(BASELINE_RUN_TIME_S / sim.timestep)
    vision_updates = 0

    for _ in range(n_steps):
        obs, _, _, _, info = sim.step(action=np.array([1.0, 1.0]))
        if info.get("vision_updated", False):
            vision_updates += 1
            nn_activities = info["nn_activities"]
            for cell in TRACKING_CELLS:
                arr = fly.retina_mapper.flyvis_to_flygym(nn_activities[cell])
                samples[cell].append(np.asarray(arr, dtype=np.float64))

    stats = {}
    zero_std_total = 0
    std_total = 0
    for cell, values in samples.items():
        stack = np.stack(values, axis=0)
        mean = stack.mean(axis=0)
        std = stack.std(axis=0)
        zero_std_total += int(np.count_nonzero(std <= 0))
        std_total += int(std.size)
        stats[cell] = {"mean": mean, "std": std}

    sim.close()

    assert vision_updates >= 20
    return stats, {
        "steps": n_steps,
        "vision_updates": vision_updates,
        "zero_std_fraction": zero_std_total / std_total,
    }


def run_closed_loop(baseline):
    arena = MovingFlyArena(
        move_speed=15,
        radius=10,
        terrain_type="flat",
    )
    fly = make_fly(spawn_pos=(-5, 10, 0.3))
    sim = SingleFlySimulation(fly=fly, arena=arena)

    ommatidia_coms = np.empty((fly.retina.num_ommatidia_per_eye, 2))
    for i in range(fly.retina.num_ommatidia_per_eye):
        mask = fly.retina.ommatidia_id_map == i + 1
        ommatidia_coms[i, :] = np.argwhere(mask).mean(axis=0)

    obs, info = sim.reset(seed=0)
    start_xy = np.asarray(obs["fly"])[0, :2].astype(float).copy()
    target_start_xy = np.asarray(arena.fly_pos[:2], dtype=float).copy()

    dn_drive = np.array([1.0, 1.0])
    n_steps = int(CLOSED_LOOP_RUN_TIME_S / sim.timestep)
    traces = []
    zero_std_hits = 0
    decoder_updates = 0

    for step in range(n_steps):
        if info.get("vision_updated", False):
            nn_activities = info["nn_activities"]
            zscores = []

            for cell in TRACKING_CELLS:
                activities = fly.retina_mapper.flyvis_to_flygym(nn_activities[cell])
                response_mean = baseline[cell]["mean"]
                response_std = baseline[cell]["std"]

                zero_mask = response_std <= 0
                zero_std_hits += int(np.count_nonzero(zero_mask))

                # Exact official decoder is undefined at zero baseline SD. Keep those
                # positions out of the bounded smoke rather than silently inventing signal.
                safe_std = np.where(zero_mask, np.nan, response_std)
                with np.errstate(divide="ignore", invalid="ignore"):
                    abs_zscore = np.abs((activities - response_mean) / safe_std)
                zscores.append(abs_zscore)

            zscores = np.asarray(zscores, dtype=float)
            mean_zscore = np.nanmean(zscores, axis=0)
            mean_zscore = np.nan_to_num(mean_zscore, nan=0.0, posinf=0.0, neginf=0.0)
            obj_mask = mean_zscore > Z_SCORE_THRESHOLD

            size_per_eye = obj_mask.sum(axis=1)
            com_per_eye = np.full((2, 2), np.nan)
            for eye_idx in range(2):
                if size_per_eye[eye_idx] > 0:
                    masked_xy_coords = ommatidia_coms[obj_mask[eye_idx], :]
                    com_per_eye[eye_idx, :] = masked_xy_coords.mean(axis=0)

            com_per_eye /= np.array([fly.retina.nrows, fly.retina.ncols])
            size_per_eye = size_per_eye / fly.retina.num_ommatidia_per_eye

            center_deviation = com_per_eye[:, 1].copy()
            center_deviation[0] = 1 - center_deviation[0]
            weighted_deviation = center_deviation.copy()
            weighted_deviation[size_per_eye == 0] = 1e9

            if size_per_eye.sum() == 0:
                turning_bias = 0.0
            else:
                turning_bias = float(
                    (
                        -size_per_eye[0] * weighted_deviation[0]
                        + size_per_eye[1] * weighted_deviation[1]
                    )
                    / size_per_eye.sum()
                )

            dn_inner = max(0.4, 1 - abs(turning_bias * TRACKING_GAIN) * 0.6)
            dn_outer = min(1.2, 1 + abs(turning_bias * TRACKING_GAIN) * 0.2)
            if turning_bias < 0:
                dn_drive = np.array([dn_inner, dn_outer])
            else:
                dn_drive = np.array([dn_outer, dn_inner])

            decoder_updates += 1
            traces.append({
                "step": step,
                "turning_bias": turning_bias,
                "dn_left": float(dn_drive[0]),
                "dn_right": float(dn_drive[1]),
                "object_fraction_left": float(size_per_eye[0]),
                "object_fraction_right": float(size_per_eye[1]),
                "mean_zscore_max": float(np.max(mean_zscore)),
            })

        obs, _, _, _, info = sim.step(action=dn_drive)

    end_xy = np.asarray(obs["fly"])[0, :2].astype(float).copy()
    target_end_xy = np.asarray(arena.fly_pos[:2], dtype=float).copy()
    sim.close()

    biases = np.array([x["turning_bias"] for x in traces], dtype=float)
    drive_diff = np.array([x["dn_right"] - x["dn_left"] for x in traces], dtype=float)
    object_fraction = np.array([
        x["object_fraction_left"] + x["object_fraction_right"] for x in traces
    ], dtype=float)

    assert decoder_updates >= 20
    assert np.isfinite(biases).all()
    assert np.isfinite(drive_diff).all()

    return {
        "steps": n_steps,
        "decoder_updates": decoder_updates,
        "observer_start_xy": start_xy.tolist(),
        "observer_end_xy": end_xy.tolist(),
        "observer_displacement": float(np.linalg.norm(end_xy - start_xy)),
        "target_start_xy": target_start_xy.tolist(),
        "target_end_xy": target_end_xy.tolist(),
        "turning_bias_mean_abs": float(np.mean(np.abs(biases))),
        "turning_bias_max_abs": float(np.max(np.abs(biases))),
        "dn_drive_difference_mean_abs": float(np.mean(np.abs(drive_diff))),
        "dn_drive_difference_max_abs": float(np.max(np.abs(drive_diff))),
        "frames_with_object_mask": int(np.count_nonzero(object_fraction > 0)),
        "zero_std_positions_encountered": int(zero_std_hits),
        "first_trace": traces[0] if traces else None,
        "last_trace": traces[-1] if traces else None,
    }


def main():
    baseline, baseline_meta = collect_baseline()
    closed_loop = run_closed_loop(baseline)

    result = {
        "status": "PASS",
        "baseline_run_time_s": BASELINE_RUN_TIME_S,
        "closed_loop_run_time_s": CLOSED_LOOP_RUN_TIME_S,
        "vision_refresh_rate_hz": VISION_REFRESH_RATE,
        "tracking_cells": TRACKING_CELLS,
        "decoder": {
            "z_score_threshold": Z_SCORE_THRESHOLD,
            "tracking_gain": TRACKING_GAIN,
            "source": "official legacy follow_fly_closed_loop.py equations",
            "zero_std_policy_for_bounded_smoke": "exclude zero-SD positions from z-score aggregation",
        },
        "baseline": baseline_meta,
        "closed_loop": closed_loop,
        "scientific_boundary": (
            "Engineering reproduction of the published legacy decoder path at short duration. "
            "Not a replication of the 3 s paper condition and not evidence that the engineered "
            "decoder is a biological descending circuit."
        ),
    }

    print("ARIS4C018 Pilot2B bounded closed-loop PASS")
    print("RESULT_JSON=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
