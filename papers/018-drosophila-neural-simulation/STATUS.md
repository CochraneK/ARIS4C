# ARIS4C018 Status

## Current

- Progress: 46%
- Activity: active
- Stage: Pilot 2A embodied-neural interface PASS · Pilot 2B official closed-loop reproduction

## Completed

- Mapped research/model infrastructure and user/community projects separately.
- Built and tested the behaviour-left / neural-activity-right Pilot 0 sandbox.
- Completed deterministic toy perturbation sweeps.
- Pilot 1 clean-CI reproduction PASS:
  - flyvis connectome construction: 443 nodes / 8,174 edges / 65 cell types at extent=1;
  - FlyGym 2.1.0 NeuroMechFly compilation: 70 bodies / 127 joints / 42 controls.
- Pilot 2A official legacy advanced-vision interface PASS:
  - pretrained flyvis weights downloaded with upstream checksum verification;
  - headless retinal rendering operational through EGL;
  - upstream 1.0 s neural fade-in completed;
  - same run exposed FlyGym body state plus a **2 × 45,669** neural activity array;
  - five real vision updates observed in the bounded smoke;
  - named T4/T5 activity outputs were finite.

Pilot 2A workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35528654776

## Key conceptual correction

The published legacy FlyGym path already implements most of the visual-to-behaviour integration we initially considered building ourselves.

Its chain must be split into:

```
BIOLOGICALLY CONSTRAINED
retina -> pretrained flyvis -> named visual neural activity

ENGINEERED
neural activity -> baseline z-score -> object mask
-> turning bias -> 2-D descending drive -> hybrid locomotor controller
```

018 must not collapse those layers into one "brain controls body" claim.

## Community comparators

The landscape now includes recent closed-loop community projects that expose real/engineered boundaries, negative results, ablations and readout artefacts. These are treated as scientific comparators and failure-mode sources, not merely UI inspiration.

## Next gates

1. Reproduce a bounded official baseline-response calibration.
2. Reproduce the exact official z-score/object-mask/turning-bias decoder.
3. Run one bounded real closed-loop fly-following trial.
4. Export synchronized body, retina, neural-state and decoder traces.
5. Audit whether a new question remains after published and 2026 community work.
6. Only then freeze an ARIS hypothesis.

## Scientific boundary

Pilot 2A demonstrates a real embodied-neural software interface. It does not yet reproduce closed-loop following and does not establish a biological visual-to-descending-neuron circuit.
