# ARIS4C018 · Pilot 4 Mismatch Localization Protocol

Status: frozen before Pilot 4 matched outputs are inspected.

## Trigger

Use this protocol only if the first matched cross-version diagnostic shows a material numerical difference in any pre-frozen engineering metric.

The first matched run itself does not define an equivalence threshold.

## R1 · Retina geometry / indexing

Record separately for legacy and current stacks:

- `nrows`;
- `ncols`;
- `num_ommatidia_per_eye`;
- maximum ommatidium ID;
- number of unique nonzero ommatidium IDs;
- pixel count covered by ommatidia;
- pale/yellow type counts where exposed;
- deterministic SHA-256 of the integer `ommatidia_id_map`;
- deterministic SHA-256 of the FlyGym→flyvis index vector;
- whether the mapping is a bijection over 721 ommatidia.

Interpretation:

- identical counts but different hashes = ordering/geometry implementation difference;
- non-bijective mapping = migration bug;
- different ommatidia count = model/interface change requiring explicit adaptation.

## R2 · Frozen retinal-vector → neural state

Do not use rendered scenes.

Construct deterministic left/right retinal vectors directly:

1. uniform 0.5;
2. left-eye horizontal gradient / mirrored right-eye gradient;
3. single-ommatidium impulse at three fixed IDs;
4. seeded random vector with seed 1804.

For each stack, record:

- mapped flyvis input hash;
- neural state shape;
- finite-value check;
- per-cell mean for the 25 tracking cell types;
- whole-state mean / SD / L2 norm.

Two localization passes:

### R2a · mapping-only

Compare mapped flyvis vectors before neural dynamics.

### R2b · neural-model-inclusive

Run each stack's pinned flyvis model.

A difference in R2b with R2a agreement implicates flyvis version/checkpoint/dynamics rather than retinal ordering.

## R3 · Pure decoder

Already frozen in `official_legacy_decoder.py`.

For identical z-score maps, require identical:

- object mask;
- center of mass;
- object fractions;
- turning bias;
- two-value drive.

Any difference here is an ARIS implementation regression, not a simulator-version effect.

## R4 · Controller semantics

Feed a frozen descending-drive sequence:

```
[1.0, 1.0]
[0.8, 1.1]
[1.1, 0.8]
[0.4, 1.2]
[1.2, 0.4]
```

Record before stepping body physics:

- joint target vector;
- adhesion state;
- controller-side intrinsic amplitudes;
- intrinsic-frequency signs.

Do not require legacy/current internal controller classes to have identical private representations. Compare only semantically corresponding public/control outputs.

## R5 · Embodied trajectory

Only after R1–R4.

Use the matched Pilot 4 scene and compare:

- body x/y trajectory;
- displacement;
- target-mask time series;
- turning-bias time series;
- drive time series.

Do not attribute R5 differences to neural biology if R1–R4 already differ.

## Reporting rule

For each first divergence, report:

```
earliest divergent layer
observable
legacy value
current value
known implementation difference
remaining uncertainty
```

Do not compress the result to “v1 better” or “v2 better”.
