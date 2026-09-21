#!/usr/bin/env python3
"""ARIS4C018 Pilot 3A: current FlyGym 2.x Retina -> current flyvis neural state."""

from __future__ import annotations

import time

import numpy as np

from flygym.anatomy import ActuatedDOFPreset, AxisOrder, JointPreset, Skeleton
from flygym.compose.fly import ActuatorType, NeuroMechFly
from flygym.compose.pose import KinematicPosePreset
from flygym.compose.world import TetheredWorld
from flygym.simulation import Simulation
from flygym.utils.math import Rotation3D

from flygym2_flyvis_adapter import (
    FlyGym2RetinaMapper,
    initialize_from_flygym_readouts,
    load_pretrained_stepwise_network,
)


def main():
    t0 = time.perf_counter()

    fly = NeuroMechFly(name="fly")
    skeleton = Skeleton(
        joint_preset=JointPreset.ALL_BIOLOGICAL,
        axis_order=AxisOrder.YAW_PITCH_ROLL,
    )
    neutral_pose = KinematicPosePreset.NEUTRAL
    fly.add_joints(skeleton, neutral_pose=neutral_pose)

    actuated_dofs = skeleton.get_actuated_dofs_from_preset(
        ActuatedDOFPreset.LEGS_ACTIVE_ONLY
    )
    fly.add_actuators(
        actuated_dofs,
        ActuatorType.POSITION,
        neutral_input=neutral_pose,
        kp=50.0,
    )
    fly.add_vision(draw_sensor_markers=False)

    world = TetheredWorld(name="vision_world")
    world.add_fly(
        fly,
        spawn_position=[0, 0, 1.5],
        spawn_rotation=Rotation3D("quat", [1, 0, 0, 0]),
    )

    sim = Simulation(world)
    sim.reset()

    retinal = sim.get_ommatidia_readouts(fly.name)
    assert retinal.shape[0] == 2
    assert retinal.shape[1] == 721
    assert retinal.shape[2] == 2
    assert np.isfinite(retinal).all()

    mapper = FlyGym2RetinaMapper(sim.retina)
    network = load_pretrained_stepwise_network()

    visual_input = initialize_from_flygym_readouts(
        network,
        mapper,
        retinal,
        dt=1 / 500,
        fade_in_s=1.0,
    )
    activity0 = network.forward_one_step(visual_input).detach().cpu().numpy()

    # Advance physics, render current eyes again, and take a second neural step.
    for _ in range(20):
        sim.step()
    retinal1 = sim.get_ommatidia_readouts(fly.name)
    visual_input1 = mapper.flygym_to_flyvis(retinal1.max(axis=-1))
    import torch
    activity1 = network.forward_one_step(
        torch.as_tensor(visual_input1, dtype=torch.float32)
    ).detach().cpu().numpy()

    assert activity0.shape == (2, 45669)
    assert activity1.shape == (2, 45669)
    assert np.isfinite(activity0).all()
    assert np.isfinite(activity1).all()

    elapsed = time.perf_counter() - t0
    delta = float(np.mean(np.abs(activity1 - activity0)))

    print("ARIS4C018 FlyGym2->flyvis migration smoke PASS")
    print(f"retinal_shape={tuple(retinal.shape)}")
    print(f"neural_shape={tuple(activity1.shape)}")
    print(f"mean_abs_neural_delta={delta:.9g}")
    print(f"elapsed_s={elapsed:.3f}")

    network.cleanup_step_by_step_simulation()


if __name__ == "__main__":
    main()
