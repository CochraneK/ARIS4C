#!/usr/bin/env python3
"""ARIS4C018 Pilot 2A: official legacy RealisticVisionFly interface smoke.

This exercises the published FlyGym 1.x + flyvis integration without rendering.
It is a reproduction/engineering gate, not a new biological experiment.
"""

import numpy as np

from flygym_gymnasium import SingleFlySimulation
from flygym_gymnasium.arena import FlatTerrain
from flygym_gymnasium.examples.vision import RealisticVisionFly


CONTACTS = [
    f"{leg}{segment}"
    for leg in ["LF", "LM", "LH", "RF", "RM", "RH"]
    for segment in ["Tibia", "Tarsus1", "Tarsus2", "Tarsus3", "Tarsus4", "Tarsus5"]
]


def main():
    fly = RealisticVisionFly(
        contact_sensor_placements=CONTACTS,
        enable_adhesion=True,
        vision_refresh_rate=500,
        neck_kp=500,
    )
    sim = SingleFlySimulation(fly=fly, arena=FlatTerrain())

    obs, info = sim.reset(seed=0)

    neural0 = np.asarray(obs["nn_activities_arr"])
    assert neural0.ndim == 2
    assert neural0.shape[0] == 2
    assert neural0.shape[1] > 10000
    assert "nn_activities" in info

    pos0 = np.asarray(obs["fly"])[0, :3].copy()

    vision_updates = 0
    for _ in range(100):
        obs, _, _, _, info = sim.step(action=np.array([1.0, 1.0]))
        vision_updates += int(bool(info.get("vision_updated", False)))

    pos1 = np.asarray(obs["fly"])[0, :3].copy()
    neural1 = np.asarray(obs["nn_activities_arr"])

    named = info["nn_activities"]
    cells = ["T4a", "T4b", "T4c", "T4d", "T5a", "T5b", "T5c", "T5d"]
    summaries = {}
    for cell in cells:
        arr = np.asarray(named[cell])
        summaries[cell] = float(np.mean(arr))

    assert neural1.shape == neural0.shape
    assert all(np.isfinite(v) for v in summaries.values())

    print("ARIS4C018 legacy RealisticVisionFly smoke PASS")
    print(f"neural_shape={tuple(neural1.shape)}")
    print(f"vision_updates={vision_updates}")
    print(f"body_position_start={pos0.tolist()}")
    print(f"body_position_end={pos1.tolist()}")
    print(f"body_displacement={float(np.linalg.norm(pos1 - pos0))}")
    for cell in cells:
        print(f"{cell}_mean={summaries[cell]:.9g}")

    sim.close()


if __name__ == "__main__":
    main()
