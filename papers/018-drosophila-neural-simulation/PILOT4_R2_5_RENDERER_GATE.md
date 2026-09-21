# ARIS4C018 · Pilot 4 R2.5 Renderer / Initial-Scene Gate

Status: frozen before R2 frozen-retinal neural outputs are inspected.

## Trigger

Run R2.5 if:

- R1 Retina geometry/order matches; and
- R2 deterministic retinal-vector mapping/neural response does not explain the matched Pilot 4 first-frame divergence.

## Purpose

The matched Pilot 4 result diverges at the first target decoder frame:

- legacy immediately detects the target strongly;
- current is below the frozen z=5 threshold.

Before invoking locomotion/body dynamics, test whether the two stacks already present different **rendered sensory inputs** at the initial scene.

## Frozen scene

Use the same Pilot 4 geometry:

- static black sphere [5.0, 2.2, 1.5];
- radius 1.25;
- observer requested spawn [0, 0, 1.0];
- flat checkerboard ground;
- no controller-driven locomotion before the first capture;
- no decoder.

## Capture at reset / first available visual frame

For each stack record:

### BODY / camera context

- requested spawn;
- observed root/body x/y/z;
- body quaternion/orientation if exposed;
- eye-camera pose/orientation if exposed;
- MuJoCo timestep.

### Raw rendered eye input

- left/right raw or fisheye-corrected image shape;
- per-eye mean/std/min/max;
- deterministic image hash if raw arrays are exposed comparably.

### Ommatidia

- full `(2, 721, channels)` readout;
- per-eye/channel mean/std/min/max;
- deterministic float32 hash;
- scalar/grayscale vector used for flyvis;
- mapped flyvis-input hash.

## Interpretation

### If ommatidia/readout hashes differ

The first divergence exists before flyvis.

Candidate causes include:

- eye camera pose/orientation;
- renderer implementation;
- body geometry/self-occlusion;
- scene material/light differences;
- reset/spawn semantics.

### If ommatidia/readouts match

The first divergence lies at or after flyvis dynamics despite the same Retina geometry and rendered sensory vector.

## No forced pixel equivalence

Raw rendered images may differ in implementation-specific formatting. The primary comparison is the actual ommatidia vector delivered to the neural model.

## Body-motion firewall

Do not step the locomotor controller before the diagnostic visual capture.

R2.5 is a sensory-input test, not a trajectory test.
