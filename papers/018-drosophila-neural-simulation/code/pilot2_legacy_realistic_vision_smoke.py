#!/usr/bin/env python3
"""ARIS4C018 Pilot 2A: legacy RealisticVisionFly embodied-neural interface smoke.

This uses the official FlyGym 1.x + pretrained flyvis integration. To keep the
clean CPU CI gate tractable, only the initial steady-state fade-in duration is
shortened. The neural model, pretrained weights, retinal rendering, body model,
and FlyGym<->flyvis mapping remain the upstream implementation.

PASS here is an engineering interface gate, not reproduction of the paper's
full-duration baseline or closed-loop behavioural result.
"""

import numpy as np
import flyvis
from torch import Tensor

from flygym_gymnasium import SingleFlySimulation
from flygym_gymnasium.arena import FlatTerrain
from flygym_gymnasium.examples.vision import RealisticVisionFly


CONTACTS = [
    f"{leg}{segment}"
    for leg in ["LF", "LM", "LH", "RF", "RM", "RH"]
    for segment in ["Tibia", "Tarsus1", "Tarsus2", "Tarsus3", "Tarsus4", "Tarsus5"]
]


class FastSmokeRealisticVisionFly(RealisticVisionFly):
    """Official interface with a short CI-only neural fade-in."""

    smoke_fade_in_s = 0.02

    def _initialize_vision_network(self, vision_obs):
        vision_obs_grayscale = vision_obs.max(axis=-1)
        visual_input = self.retina_mapper.flygym_to_flyvis(vision_obs_grayscale)
        visual_input = Tensor(visual_input).to(flyvis.device)

        initial_state = self.vision_network.fade_in_state(
            t_fade_in=self.smoke_fade_in_s,
            dt=1 / self.vision_refresh_rate,
            initial_frames=visual_input.unsqueeze(1),
        )
        self.vision_network.setup_step_by_step_simulation(
            dt=1 / self.vision_refresh_rate,
            initial_state=initial_state,
            as_states=False,
            num_samples=2,
        )
        self._initial_state = initial_state
        self._vision_network_initialized = True


def main():
    fly = FastSmokeRealisticVisionFly(
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
    assert np.isfinite(neural0).all()

    pos0 = np.asarray(obs["fly"])[0, :3].copy()

    vision_updates = 0
    for _ in range(40):
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
    assert np.isfinite(neural1).all()
    assert all(np.isfinite(v) for v in summaries.values())
    assert vision_updates >= 1

    print("ARIS4C018 legacy RealisticVisionFly smoke PASS")
    print("smoke_fade_in_s=0.02")
    print("official_full_fade_in_s=1.0")
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
