#!/usr/bin/env python3
"""ARIS4C018 Pilot 3C: current-stack synchronized trace capture.

Keeps Pilot 3B's strict current-stack condition unchanged and adds only
data-contract capture. Produces the same semantic frame structure as legacy
Pilot 2C so one replay UI can consume both traces.

This is an engineering migration artifact, not a novel biological experiment.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import numpy as np
import torch

import pilot3b_flygym2_closed_loop as p3b
from official_legacy_decoder import object_mask_from_zscores, turning_from_object_mask
from flygym_demo.complex_terrain import (
    HybridControllerObservation,
    apply_locomotion_action,
)


TARGET_XY = (5.0, 2.2)


def capture_current_trace(baseline):
    sim, fly, controller = p3b.build_sim(target=True)
    retinal0 = sim.get_ommatidia_readouts(fly.name)
    mapper = p3b.FlyGym2RetinaMapper(sim.retina)
    network = p3b.load_pretrained_stepwise_network()
    p3b.initialize_from_flygym_readouts(
        network,
        mapper,
        retinal0,
        dt=1 / p3b.VISION_HZ,
        fade_in_s=1.0,
    )

    ommatidia_coms = np.empty((sim.retina.num_ommatidia_per_eye, 2))
    for i in range(sim.retina.num_ommatidia_per_eye):
        mask = sim.retina.ommatidia_id_map == i + 1
        ommatidia_coms[i] = np.argwhere(mask).mean(axis=0)

    visual_every = max(
        1, round((1 / p3b.VISION_HZ) / sim.mj_model.opt.timestep)
    )
    n_steps = round(p3b.CLOSED_LOOP_S / sim.mj_model.opt.timestep)

    root_idx = fly.get_bodysegs_order().index(fly.root_segment)
    drive = np.array([1.0, 1.0])
    frames = []
    zero_hits = 0

    for step in range(n_steps):
        if step % visual_every == 0:
            _, _, layer = p3b.get_visual_activity(
                sim, fly, network, mapper
            )

            zscores = []
            cell_mean_left = []
            cell_mean_right = []

            for cell in p3b.TRACKING_CELLS:
                arr = np.asarray(
                    mapper.flyvis_to_flygym(np.asarray(layer[cell])),
                    dtype=float,
                )
                cell_mean_left.append(float(np.mean(arr[0])))
                cell_mean_right.append(float(np.mean(arr[1])))

                mu = baseline[cell]["mean"]
                sd = baseline[cell]["std"]
                zero_mask = sd <= 0
                zero_hits += int(np.count_nonzero(zero_mask))
                safe_sd = np.where(zero_mask, np.nan, sd)

                with np.errstate(divide="ignore", invalid="ignore"):
                    zscores.append(np.abs((arr - mu) / safe_sd))

            obj_mask, mean_z = object_mask_from_zscores(
                np.asarray(zscores),
                threshold=p3b.Z_THRESHOLD,
            )
            decoded = turning_from_object_mask(
                obj_mask,
                ommatidia_coms,
                retina_nrows=sim.retina.nrows,
                retina_ncols=sim.retina.ncols,
                tracking_gain=p3b.TRACKING_GAIN,
            )
            drive = decoded["dn_drive"]

            body_xy = (
                sim.get_body_positions(fly.name)[root_idx, :2]
                .astype(float)
                .copy()
            )

            frames.append({
                "t_s": float(step * sim.mj_model.opt.timestep),
                "body": {
                    "x": float(body_xy[0]),
                    "y": float(body_xy[1]),
                    "heading": None,
                },
                "target": {
                    "x": TARGET_XY[0],
                    "y": TARGET_XY[1],
                },
                "decoder": {
                    "turning_bias": float(decoded["turning_bias"]),
                    "dn_left": float(drive[0]),
                    "dn_right": float(drive[1]),
                    "object_fraction_left": float(decoded["size_per_eye"][0]),
                    "object_fraction_right": float(decoded["size_per_eye"][1]),
                    "mean_zscore_max": float(np.max(mean_z)),
                },
                "neural": {
                    "source_layer": "BIO",
                    "summary": {
                        "selected_mean_left": float(np.mean(cell_mean_left)),
                        "selected_mean_right": float(np.mean(cell_mean_right)),
                        "selected_mean_abs": float(np.mean(
                            np.abs(cell_mean_left + cell_mean_right)
                        )),
                    },
                    "cell_mean_left": cell_mean_left,
                    "cell_mean_right": cell_mean_right,
                },
            })

        obs = HybridControllerObservation.from_sim(sim, fly.name)
        action = controller.step(drive, obs)
        apply_locomotion_action(sim, fly.name, action)
        sim.step()

    network.cleanup_step_by_step_simulation()

    assert len(frames) == 40, f"Expected 40 frames, got {len(frames)}"
    masks = [
        f["decoder"]["object_fraction_left"]
        + f["decoder"]["object_fraction_right"]
        for f in frames
    ]
    drive_diff = [
        f["decoder"]["dn_right"] - f["decoder"]["dn_left"]
        for f in frames
    ]
    assert sum(v > 0 for v in masks) >= 1, "No target mask in current trace"
    assert max(abs(v) for v in drive_diff) > 1e-6, "No asymmetric drive"

    return frames, zero_hits


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "papers/018-drosophila-neural-simulation/data/"
            "pilot3c_current_synchronized_trace.json"
        ),
    )
    args = parser.parse_args()

    baseline, baseline_meta = p3b.run_baseline()
    frames, zero_hits = capture_current_trace(baseline)

    payload = {
        "schema_version": 1,
        "provenance": {
            "model_stack": "current FlyGym 2.x + current flyvis",
            "source": "ARIS4C018 Pilot 3C current-stack migration trace",
            "upstream_commit": (
                "FlyGym 38c8ec61034cd59bc5ba0de20688d4a3c0000d60; "
                "flyvis 92b3845cc426dd309a1a0e1b3890156c42e14021"
            ),
            "aris_commit": os.environ.get("GITHUB_SHA", ""),
            "workflow_run_id": os.environ.get("GITHUB_RUN_ID", ""),
            "scientific_boundary": (
                "BIO neural activity uses current FlyGym Retina plus current "
                "pretrained flyvis. DECODER remains engineered. The target is a "
                "synthetic static sphere; this is migration/replay evidence, not "
                "the legacy moving-fly publication condition."
            ),
        },
        "configuration": {
            "baseline_run_time_s": p3b.BASELINE_S,
            "closed_loop_run_time_s": p3b.CLOSED_LOOP_S,
            "vision_refresh_rate_hz": p3b.VISION_HZ,
            "tracking_gain": p3b.TRACKING_GAIN,
            "z_score_threshold": p3b.Z_THRESHOLD,
            "tracking_cells": p3b.TRACKING_CELLS,
            "target_kind": "static_sphere",
            "target_xy": list(TARGET_XY),
        },
        "baseline": baseline_meta,
        "zero_std_positions_encountered": zero_hits,
        "cell_order": p3b.TRACKING_CELLS,
        "frames": frames,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )

    print("ARIS4C018 Pilot3C current synchronized trace PASS")
    print(f"trace_frames={len(frames)}")
    print(f"object_mask_frames={sum((f['decoder']['object_fraction_left'] + f['decoder']['object_fraction_right']) > 0 for f in frames)}")
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
