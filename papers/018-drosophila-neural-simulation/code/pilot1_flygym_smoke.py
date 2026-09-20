#!/usr/bin/env python3
"""ARIS4C018 Pilot 1B: minimal pinned FlyGym / NeuroMechFly compile smoke."""

from flygym.anatomy import (
    ActuatedDOFPreset,
    AxisOrder,
    ContactBodiesPreset,
    JointPreset,
    Skeleton,
)
from flygym.compose import ActuatorType, FlatGroundWorld, Fly, KinematicPosePreset
from flygym.utils.math import Rotation3D


def main():
    fly = Fly()

    skeleton = Skeleton(
        joint_preset=JointPreset.ALL_BIOLOGICAL,
        axis_order=AxisOrder.YAW_PITCH_ROLL,
    )
    neutral_pose = KinematicPosePreset.NEUTRAL
    fly.add_joints(skeleton, neutral_pose)

    actuated_dofs = skeleton.get_actuated_dofs_from_preset(
        ActuatedDOFPreset.LEGS_ACTIVE_ONLY
    )
    fly.add_actuators(
        actuated_dofs,
        ActuatorType.POSITION,
        neutral_input=neutral_pose,
        kp=50.0,
        ctrlrange=(-3.14, 3.14),
    )
    fly.add_joint_sites(JointPreset.LEGS_ONLY.to_joint_list())

    world = FlatGroundWorld()
    world.add_fly(
        fly,
        (0, 0, 0.8),
        Rotation3D("quat", (1, 0, 0, 0)),
        bodysegs_with_ground_contact=ContactBodiesPreset.LEGS_THORAX_ABDOMEN_HEAD,
    )

    mj_model, mj_data = world.compile()

    assert mj_model.nbody > 0
    assert mj_model.njnt > 0
    assert mj_data.qpos.size > 0

    print("ARIS4C018 FlyGym smoke PASS")
    print(f"nbody={mj_model.nbody}")
    print(f"njnt={mj_model.njnt}")
    print(f"nq={mj_model.nq}")
    print(f"nv={mj_model.nv}")
    print(f"nu={mj_model.nu}")


if __name__ == "__main__":
    main()
