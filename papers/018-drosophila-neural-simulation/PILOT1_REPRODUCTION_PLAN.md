# ARIS4C018 · Pilot 1 Reproduction Plan

## Goal

Move from a toy pipeline to maintained, published Drosophila modelling components without prematurely inventing a new biological claim.

Pilot 1 has two independent smoke tracks.

## Track A · flyvis connectome smoke

Pinned upstream snapshot:

- repository: https://github.com/TuragaLab/flyvis
- commit: `92b3845cc426dd309a1a0e1b3890156c42e14021`
- Python constraint from upstream: >=3.9,<3.13
- ARIS runner: Python 3.11

Minimal reproduction:

1. install the pinned upstream package;
2. import the packaged connectome resource;
3. compile `ConnectomeFromAvgFilters` at extent=1;
4. report node/edge table sizes and cell-type count.

This is intentionally smaller than the paper/tutorial default extent=15.

## Track B · FlyGym compile smoke

Pinned upstream snapshot:

- repository: https://github.com/NeLy-EPFL/flygym
- commit: `38c8ec61034cd59bc5ba0de20688d4a3c0000d60`
- upstream package version at inspection: 2.1.0
- Python constraint from upstream: >=3.12,<3.15
- ARIS runner: Python 3.12

Minimal reproduction follows the current upstream interactive-viewer construction pattern but stops before GUI launch:

1. create a `Fly`;
2. add biological joints and leg actuators;
3. add the fly to `FlatGroundWorld`;
4. compile the MuJoCo model;
5. report basic model dimensions.

## Gate

Pilot 1 passes only if each track:

- installs from the pinned upstream commit;
- constructs the intended model object;
- executes without relying on a local manual environment;
- records its output in GitHub Actions logs.

A package import alone does not count as a reproduction.

## After the gate

If both tracks pass, design the smallest bridge between neural state and embodied behaviour. Do not yet claim that flyvis activity causally controls FlyGym behaviour.

## Practical usability fields

For each track, record alongside PASS/FAIL:

- Python version;
- pinned upstream commit;
- clean-install time on GitHub-hosted Ubuntu;
- whether GPU/display is required for the smoke path;
- whether network downloads beyond package installation are required at runtime;
- model/object size indicators produced by the smoke script;
- whether a newcomer can reach the same state from one documented command.

The point is not only "can ARIS run it?" but also "can another user reasonably reproduce it?"
