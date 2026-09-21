#!/usr/bin/env python3
"""ARIS4C018 Pilot 4: legacy side of a matched static-target regression.

This deliberately mirrors the current Pilot 3B engineering condition:
- static black sphere at [5.0, 2.2, 1.5], radius 1.25
- observer spawn [0, 0, 1.0]
- 0.08 s walking baseline
- 0.08 s closed loop
- 500 Hz vision
- z threshold 5
- tracking gain 6
- the same 25 tracking cell types
- the same pure decoder implementation

The goal is version-regression diagnosis, not biological inference.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from flygym_gymnasium import SingleFlySimulation
from flygym_gymnasium.arena import FlatTerrain
from flygym_gymnasium.examples.vision import RealisticVisionFly

from official_legacy_decoder import object_mask_from_zscores, turning_from_object_mask


CONTACTS = [
    f"{leg}{segment}"
    for leg in ["LF", "LM", "LH", "RF", "RM", "RH"]
    for segment in ["Tibia", "Tarsus1", "Tarsus2", "Tarsus3", "Tarsus4", "Tarsus5"]
]
TRACKING_CELLS = [
    "T2", "T2a", "T3",
    "Tm1", "Tm2", "Tm3", "Tm4", "Tm5Y", "Tm5a", "Tm5b", "Tm5c",
    "Tm9", "Tm16", "Tm20", "Tm28", "Tm30",
    "TmY3", "TmY4", "TmY5a", "TmY9", "TmY10", "TmY13", "TmY14",
    "TmY15", "TmY18",
]

VISION_HZ = 500
BASELINE_S = 0.08
CLOSED_LOOP_S = 0.08
Z_THRESHOLD = 5.0
TRACKING_GAIN = 6.0
TARGET_POS = np.array([5.0, 2.2, 1.5], dtype=float)
TARGET_RADIUS = 1.25
SPAWN_POS = (0.0, 0.0, 1.0)


class StaticSphereArena(FlatTerrain):
    def __init__(self, *, with_target: bool):
        super().__init__()
        if with_target:
            self.root_element.worldbody.add(
                "geom",
                type="sphere",
                name="aris_visual_target",
                pos=TARGET_POS,
                size=(TARGET_RADIUS,),
                rgba=(0.0, 0.0, 0.0, 1.0),
                contype=0,
                conaffinity=0,
            )


def make_fly():
    return RealisticVisionFly(
        contact_sensor_placements=CONTACTS,
        enable_adhesion=True,
        vision_refresh_rate=VISION_HZ,
        neck_kp=500,
        head_stabilization_model=None,
        spawn_pos=SPAWN_POS,
    )


def collect_baseline():
    fly = make_fly()
    sim = SingleFlySimulation(fly=fly, arena=StaticSphereArena(with_target=False))
    obs, info = sim.reset(seed=0)

    samples = {cell: [] for cell in TRACKING_CELLS}
    n_steps = int(BASELINE_S / sim.timestep)
    updates = 0

    for _ in range(n_steps):
        obs, _, _, _, info = sim.step(action=np.array([1.0, 1.0]))
        if info.get("vision_updated", False):
            updates += 1
            layer = info["nn_activities"]
            for cell in TRACKING_CELLS:
                arr = fly.retina_mapper.flyvis_to_flygym(layer[cell])
                samples[cell].append(np.asarray(arr, dtype=float))

    baseline = {}
    zero = total = 0
    for cell, values in samples.items():
        stack = np.stack(values)
        mu = stack.mean(axis=0)
        sd = stack.std(axis=0)
        zero += int(np.count_nonzero(sd <= 0))
        total += int(sd.size)
        baseline[cell] = {"mean": mu, "std": sd}

    end_xy = np.asarray(obs["fly"])[0, :2].astype(float)
    sim.close()

    assert updates == 40, f"Expected 40 baseline visual updates, got {updates}"
    return baseline, {
        "vision_updates": updates,
        "zero_std_fraction": zero / total,
        "end_xy": end_xy.tolist(),
    }


def run_target(baseline):
    fly = make_fly()
    arena = StaticSphereArena(with_target=True)
    sim = SingleFlySimulation(fly=fly, arena=arena)

    ommatidia_coms = np.empty((fly.retina.num_ommatidia_per_eye, 2))
    for i in range(fly.retina.num_ommatidia_per_eye):
        mask = fly.retina.ommatidia_id_map == i + 1
        ommatidia_coms[i] = np.argwhere(mask).mean(axis=0)

    obs, info = sim.reset(seed=0)
    start_xy = np.asarray(obs["fly"])[0, :2].astype(float).copy()

    drive = np.array([1.0, 1.0])
    n_steps = int(CLOSED_LOOP_S / sim.timestep)
    traces = []
    zero_hits = 0

    for step in range(n_steps):
        if info.get("vision_updated", False):
            layer = info["nn_activities"]
            zscores = []

            for cell in TRACKING_CELLS:
                arr = np.asarray(
                    fly.retina_mapper.flyvis_to_flygym(layer[cell]),
                    dtype=float,
                )
                mu = baseline[cell]["mean"]
                sd = baseline[cell]["std"]
                zero_mask = sd <= 0
                zero_hits += int(np.count_nonzero(zero_mask))
                safe_sd = np.where(zero_mask, np.nan, sd)
                with np.errstate(divide="ignore", invalid="ignore"):
                    zscores.append(np.abs((arr - mu) / safe_sd))

            obj_mask, mean_z = object_mask_from_zscores(
                np.asarray(zscores), threshold=Z_THRESHOLD
            )
            decoded = turning_from_object_mask(
                obj_mask,
                ommatidia_coms,
                retina_nrows=fly.retina.nrows,
                retina_ncols=fly.retina.ncols,
                tracking_gain=TRACKING_GAIN,
            )
            drive = decoded["dn_drive"]
            traces.append({
                "step": step,
                "turning_bias": float(decoded["turning_bias"]),
                "dn_left": float(drive[0]),
                "dn_right": float(drive[1]),
                "object_left": float(decoded["size_per_eye"][0]),
                "object_right": float(decoded["size_per_eye"][1]),
                "max_z": float(np.max(mean_z)),
            })

        obs, _, _, _, info = sim.step(action=drive)

    end_xy = np.asarray(obs["fly"])[0, :2].astype(float).copy()
    sim.close()

    assert len(traces) == 40, f"Expected 40 decoder updates, got {len(traces)}"
    bias = np.array([x["turning_bias"] for x in traces], dtype=float)
    dd = np.array([x["dn_right"] - x["dn_left"] for x in traces], dtype=float)
    masks = np.array([x["object_left"] + x["object_right"] for x in traces], dtype=float)
    assert np.isfinite(bias).all()
    assert np.isfinite(dd).all()

    frames_with_mask = int(np.count_nonzero(masks > 0))
    return {
        "decoder_updates": len(traces),
        "frames_with_object_mask": frames_with_mask,
        "mask_detection_rate": frames_with_mask / len(traces),
        "turning_bias_mean_abs": float(np.mean(np.abs(bias))),
        "turning_bias_max_abs": float(np.max(np.abs(bias))),
        "drive_diff_mean_abs": float(np.mean(np.abs(dd))),
        "drive_diff_max_abs": float(np.max(np.abs(dd))),
        "start_xy": start_xy.tolist(),
        "end_xy": end_xy.tolist(),
        "displacement": float(np.linalg.norm(end_xy - start_xy)),
        "zero_std_positions_encountered": zero_hits,
        "first_trace": traces[0],
        "last_trace": traces[-1],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    t0 = time.perf_counter()
    baseline, baseline_meta = collect_baseline()
    target = run_target(baseline)
    elapsed = time.perf_counter() - t0

    result = {
        "schema_version": 1,
        "side": "legacy",
        "model_stack": "legacy FlyGym 1.3.2 + flyvis 1.1.2",
        "condition": {
            "baseline_s": BASELINE_S,
            "closed_loop_s": CLOSED_LOOP_S,
            "vision_hz": VISION_HZ,
            "spawn_pos": list(SPAWN_POS),
            "target_pos": TARGET_POS.tolist(),
            "target_radius": TARGET_RADIUS,
            "z_score_threshold": Z_THRESHOLD,
            "tracking_gain": TRACKING_GAIN,
            "tracking_cells": TRACKING_CELLS,
        },
        "baseline": baseline_meta,
        "target": target,
        "elapsed_s": elapsed,
        "scientific_boundary": (
            "Matched cross-version engineering diagnostic. Target and decoder settings "
            "are matched, but simulator/body/rendering/flyvis versions remain the "
            "variables under diagnosis. Not a biological effect test."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("ARIS4C018 Pilot4 legacy matched-static PASS")
    print("RESULT_JSON=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
