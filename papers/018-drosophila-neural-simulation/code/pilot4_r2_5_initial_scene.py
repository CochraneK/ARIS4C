#!/usr/bin/env python3
"""ARIS4C018 Pilot 4 R2.5: initial-scene sensory capture.

This test removes flyvis, decoder, controller stepping, and trajectory effects.
It asks one question only:

Given the same requested spawn and static target geometry, do legacy FlyGym 1.x
and current FlyGym 2.x deliver the same ommatidia vector BEFORE locomotion?

The script is run separately under each pinned stack and emits a compact JSON
signature for later comparison.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


TARGET_POS = [5.0, 2.2, 1.5]
TARGET_RADIUS = 1.25
SPAWN_POS = [0.0, 0.0, 1.0]


def digest(arr) -> str:
    x = np.ascontiguousarray(np.asarray(arr, dtype=np.float32))
    return hashlib.sha256(x.tobytes()).hexdigest()


def stats(arr):
    x = np.asarray(arr, dtype=np.float64)
    return {
        "shape": list(x.shape),
        "mean": float(np.mean(x)),
        "std": float(np.std(x)),
        "min": float(np.min(x)),
        "max": float(np.max(x)),
    }


def summarize_vision(vision):
    x = np.asarray(vision, dtype=np.float32)
    assert x.shape[0] == 2
    assert x.shape[1] == 721
    assert x.shape[2] == 2
    gray = x.max(axis=-1)

    return {
        "full_shape": list(x.shape),
        "full_sha256_float32": digest(x),
        "gray_shape": list(gray.shape),
        "gray_sha256_float32": digest(gray),
        "overall": stats(x),
        "left": stats(x[0]),
        "right": stats(x[1]),
        "channel_0": stats(x[..., 0]),
        "channel_1": stats(x[..., 1]),
        "gray_overall": stats(gray),
        "gray_left": stats(gray[0]),
        "gray_right": stats(gray[1]),
    }


def run_legacy():
    from flygym_gymnasium import SingleFlySimulation
    from flygym_gymnasium.arena import FlatTerrain
    from flygym_gymnasium.examples.locomotion import HybridTurningFly

    contacts = [
        f"{leg}{segment}"
        for leg in ["LF", "LM", "LH", "RF", "RM", "RH"]
        for segment in ["Tibia", "Tarsus1", "Tarsus2", "Tarsus3", "Tarsus4", "Tarsus5"]
    ]

    class StaticSphereArena(FlatTerrain):
        def __init__(self):
            super().__init__()
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

    fly = HybridTurningFly(
        contact_sensor_placements=contacts,
        enable_adhesion=True,
        enable_vision=True,
        vision_refresh_rate=500,
        neck_kp=500,
        head_stabilization_model=None,
        spawn_pos=tuple(SPAWN_POS),
    )
    sim = SingleFlySimulation(fly=fly, arena=StaticSphereArena())
    obs, info = sim.reset(seed=0)

    vision = np.asarray(obs["vision"], dtype=np.float32)
    root = np.asarray(obs["fly"])[0]
    body_position = [float(v) for v in root[:3]]

    out = {
        "schema_version": 1,
        "side": "legacy",
        "model_stack": "legacy FlyGym 1.3.2",
        "requested_spawn": SPAWN_POS,
        "target_pos": TARGET_POS,
        "target_radius": TARGET_RADIUS,
        "timestep": float(sim.timestep),
        "body_root_position": body_position,
        "vision": summarize_vision(vision),
    }
    sim.close()
    return out


def run_current():
    import mujoco as mj

    from flygym.compose import FlatGroundWorld
    from flygym.simulation import Simulation
    from flygym.utils.math import Rotation3D
    from flygym_demo.complex_terrain import make_locomotion_fly

    fly = make_locomotion_fly(name="nmf", add_adhesion=True)
    fly.add_vision(draw_sensor_markers=False)

    world = FlatGroundWorld()
    world.mjcf_root.worldbody.add_geom(
        type=mj.mjtGeom.mjGEOM_SPHERE,
        name="aris_visual_target",
        pos=TARGET_POS,
        size=[TARGET_RADIUS],
        rgba=[0.0, 0.0, 0.0, 1.0],
        contype=0,
        conaffinity=0,
    )
    world.add_fly(
        fly,
        spawn_position=SPAWN_POS,
        spawn_rotation=Rotation3D("quat", [1, 0, 0, 0]),
    )
    sim = Simulation(world)
    sim.reset()

    vision = np.asarray(sim.get_ommatidia_readouts(fly.name), dtype=np.float32)
    root_idx = fly.get_bodysegs_order().index(fly.root_segment)
    body_position = [
        float(v) for v in sim.get_body_positions(fly.name)[root_idx, :3]
    ]

    out = {
        "schema_version": 1,
        "side": "current",
        "model_stack": "current FlyGym 2.x",
        "requested_spawn": SPAWN_POS,
        "target_pos": TARGET_POS,
        "target_radius": TARGET_RADIUS,
        "timestep": float(sim.mj_model.opt.timestep),
        "body_root_position": body_position,
        "vision": summarize_vision(vision),
    }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stack", choices=["legacy", "current"], required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    result = run_legacy() if args.stack == "legacy" else run_current()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print("ARIS4C018 Pilot4 R2.5 initial-scene capture PASS")
    print("RESULT_JSON=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
