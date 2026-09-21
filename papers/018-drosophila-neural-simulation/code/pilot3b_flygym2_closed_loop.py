#!/usr/bin/env python3
"""ARIS4C018 Pilot 3B: current FlyGym 2.x + current flyvis full-chain smoke.

Engineering migration gate:
walking baseline -> current Retina -> current pretrained flyvis -> frozen official
decoder math -> current HybridTurningController -> current FlyGym body.

The target is a simple static visible sphere. This is NOT a reproduction of the
legacy moving-fly paper condition and makes no biological decoder claim.
"""

from __future__ import annotations

import json
import time

import mujoco as mj
import numpy as np
import torch
from flyvis.utils.activity_utils import LayerActivity

from flygym.compose import FlatGroundWorld
from flygym.simulation import Simulation
from flygym.utils.math import Rotation3D
from flygym_demo.complex_terrain import (
    HybridControllerObservation,
    HybridTurningController,
    PreprogrammedSteps,
    apply_locomotion_action,
    make_locomotion_fly,
)

from flygym2_flyvis_adapter import (
    FlyGym2RetinaMapper,
    initialize_from_flygym_readouts,
    load_pretrained_stepwise_network,
)
from official_legacy_decoder import object_mask_from_zscores, turning_from_object_mask


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


def build_sim(*, target=False):
    fly = make_locomotion_fly(name="nmf", add_adhesion=True)
    fly.add_vision(draw_sensor_markers=False)

    world = FlatGroundWorld()
    if target:
        world.mjcf_root.worldbody.add_geom(
            type=mj.mjtGeom.mjGEOM_SPHERE,
            name="aris_visual_target",
            pos=[5.0, 2.2, 1.5],
            size=[1.25],
            rgba=[0.0, 0.0, 0.0, 1.0],
            contype=0,
            conaffinity=0,
        )

    world.add_fly(
        fly,
        spawn_position=[0, 0, 1.0],
        spawn_rotation=Rotation3D("quat", [1, 0, 0, 0]),
    )

    sim = Simulation(world)
    sim.reset()
    controller = HybridTurningController(
        timestep=sim.mj_model.opt.timestep,
        preprogrammed_steps=PreprogrammedSteps(),
    )
    return sim, fly, controller


def get_visual_activity(sim, fly, network, mapper):
    retinal = sim.get_ommatidia_readouts(fly.name)
    visual = mapper.flygym_to_flyvis(retinal.max(axis=-1))
    activity_arr = network.forward_one_step(
        torch.as_tensor(visual, dtype=torch.float32)
    ).detach().cpu().numpy()
    layer = LayerActivity(
        activity_arr,
        network.connectome,
        keepref=True,
        use_central=False,
    )
    return retinal, activity_arr, layer


def run_baseline():
    sim, fly, controller = build_sim(target=False)
    retinal0 = sim.get_ommatidia_readouts(fly.name)
    mapper = FlyGym2RetinaMapper(sim.retina)
    network = load_pretrained_stepwise_network()
    initialize_from_flygym_readouts(
        network, mapper, retinal0, dt=1 / VISION_HZ, fade_in_s=1.0
    )

    visual_every = max(1, round((1 / VISION_HZ) / sim.mj_model.opt.timestep))
    n_steps = round(BASELINE_S / sim.mj_model.opt.timestep)
    samples = {cell: [] for cell in TRACKING_CELLS}
    updates = 0

    drive = np.array([1.0, 1.0])
    for step in range(n_steps):
        obs = HybridControllerObservation.from_sim(sim, fly.name)
        action = controller.step(drive, obs)
        apply_locomotion_action(sim, fly.name, action)
        sim.step()

        if step % visual_every == 0:
            _, _, layer = get_visual_activity(sim, fly, network, mapper)
            for cell in TRACKING_CELLS:
                arr = mapper.flyvis_to_flygym(np.asarray(layer[cell]))
                samples[cell].append(np.asarray(arr, dtype=float))
            updates += 1

    baseline = {}
    zero = total = 0
    for cell, vals in samples.items():
        stack = np.stack(vals)
        mu = stack.mean(axis=0)
        sd = stack.std(axis=0)
        zero += int(np.count_nonzero(sd <= 0))
        total += int(sd.size)
        baseline[cell] = {"mean": mu, "std": sd}

    positions = sim.get_body_positions(fly.name)
    root_idx = fly.get_bodysegs_order().index(fly.root_segment)
    end_xy = positions[root_idx, :2].astype(float)

    network.cleanup_step_by_step_simulation()
    return baseline, {
        "vision_updates": updates,
        "zero_std_fraction": zero / total,
        "end_xy": end_xy.tolist(),
    }


def run_target(baseline):
    sim, fly, controller = build_sim(target=True)
    retinal0 = sim.get_ommatidia_readouts(fly.name)
    mapper = FlyGym2RetinaMapper(sim.retina)
    network = load_pretrained_stepwise_network()
    initialize_from_flygym_readouts(
        network, mapper, retinal0, dt=1 / VISION_HZ, fade_in_s=1.0
    )

    ommatidia_coms = np.empty((sim.retina.num_ommatidia_per_eye, 2))
    for i in range(sim.retina.num_ommatidia_per_eye):
        mask = sim.retina.ommatidia_id_map == i + 1
        ommatidia_coms[i] = np.argwhere(mask).mean(axis=0)

    visual_every = max(1, round((1 / VISION_HZ) / sim.mj_model.opt.timestep))
    n_steps = round(CLOSED_LOOP_S / sim.mj_model.opt.timestep)

    root_idx = fly.get_bodysegs_order().index(fly.root_segment)
    start_xy = sim.get_body_positions(fly.name)[root_idx, :2].astype(float).copy()

    drive = np.array([1.0, 1.0])
    traces = []
    zero_hits = 0

    for step in range(n_steps):
        if step % visual_every == 0:
            _, _, layer = get_visual_activity(sim, fly, network, mapper)
            zscores = []
            for cell in TRACKING_CELLS:
                arr = mapper.flyvis_to_flygym(np.asarray(layer[cell]))
                mu, sd = baseline[cell]["mean"], baseline[cell]["std"]
                zero_mask = sd <= 0
                zero_hits += int(np.count_nonzero(zero_mask))
                safe_sd = np.where(zero_mask, np.nan, sd)
                with np.errstate(divide="ignore", invalid="ignore"):
                    zscores.append(np.abs((arr - mu) / safe_sd))

            mask, mean_z = object_mask_from_zscores(
                np.asarray(zscores), threshold=Z_THRESHOLD
            )
            decoded = turning_from_object_mask(
                mask,
                ommatidia_coms,
                retina_nrows=sim.retina.nrows,
                retina_ncols=sim.retina.ncols,
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

        obs = HybridControllerObservation.from_sim(sim, fly.name)
        action = controller.step(drive, obs)
        apply_locomotion_action(sim, fly.name, action)
        sim.step()

    end_xy = sim.get_body_positions(fly.name)[root_idx, :2].astype(float).copy()
    network.cleanup_step_by_step_simulation()

    bias = np.array([x["turning_bias"] for x in traces])
    dd = np.array([x["dn_right"] - x["dn_left"] for x in traces])
    masks = np.array([x["object_left"] + x["object_right"] for x in traces])

    assert len(traces) >= 10
    assert np.isfinite(bias).all()
    assert np.isfinite(dd).all()

    frames_with_object_mask = int(np.count_nonzero(masks > 0))
    drive_diff_max_abs = float(np.max(np.abs(dd)))

    # A full-chain migration PASS requires a real visual target to survive the
    # neural readout and decoder, not merely finite values.
    assert frames_with_object_mask >= 1, "No decoder object mask detected"
    assert drive_diff_max_abs > 1e-6, "Decoder never produced asymmetric drive"

    return {
        "decoder_updates": len(traces),
        "frames_with_object_mask": frames_with_object_mask,
        "turning_bias_mean_abs": float(np.mean(np.abs(bias))),
        "turning_bias_max_abs": float(np.max(np.abs(bias))),
        "drive_diff_mean_abs": float(np.mean(np.abs(dd))),
        "drive_diff_max_abs": drive_diff_max_abs,
        "start_xy": start_xy.tolist(),
        "end_xy": end_xy.tolist(),
        "displacement": float(np.linalg.norm(end_xy - start_xy)),
        "zero_std_positions_encountered": zero_hits,
        "first_trace": traces[0],
        "last_trace": traces[-1],
    }


def main():
    t0 = time.perf_counter()
    baseline, baseline_meta = run_baseline()
    target = run_target(baseline)
    elapsed = time.perf_counter() - t0

    result = {
        "status": "PASS",
        "stack": "current FlyGym 2.x + current flyvis",
        "baseline_s": BASELINE_S,
        "closed_loop_s": CLOSED_LOOP_S,
        "vision_hz": VISION_HZ,
        "baseline": baseline_meta,
        "target": target,
        "elapsed_s": elapsed,
        "scientific_boundary": (
            "Current-stack migration engineering test with a synthetic static visual "
            "target. The decoder remains engineered and this is not the legacy moving-"
            "fly publication condition."
        ),
    }

    print("ARIS4C018 Pilot3B current-stack closed-loop PASS")
    print("RESULT_JSON=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
