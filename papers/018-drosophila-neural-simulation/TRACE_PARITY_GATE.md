# ARIS4C018 · Legacy / Current Trace Parity Gate

## Purpose

Pilot 2C and Pilot 3C are not matched experiments, but they must be interchangeable **data contracts**.

This gate defines what "same trace schema" means before any cross-version scientific comparison.

## Allowed differences

The two traces may differ in:

- number of frames;
- duration;
- target type;
- target trajectory;
- body trajectory;
- model-stack provenance;
- numerical neural activity;
- decoder outputs;
- runtime;
- baseline diagnostics.

These are data/content differences.

## Required semantic parity

Both traces must provide:

### Top level

- `schema_version == 1`
- `provenance`
- `configuration`
- `baseline`
- `cell_order`
- `frames`

### Cell identity

- exactly 25 selected tracking cell types for the current replay contract;
- stable order within a trace;
- per-frame left/right arrays aligned to `cell_order`.

### Per frame

- `t_s`
- `body.x`, `body.y`
- `target.x`, `target.y`
- `decoder.turning_bias`
- `decoder.dn_left`
- `decoder.dn_right`
- `decoder.object_fraction_left`
- `decoder.object_fraction_right`
- `decoder.mean_zscore_max`
- `neural.source_layer == "BIO"`
- `neural.summary`
- `neural.cell_mean_left`
- `neural.cell_mean_right`

## Provenance must remain visible

The viewer must display enough metadata to prevent users from confusing:

- legacy FlyGym 1.x moving-target reproduction;
- current FlyGym 2.x static-target migration condition.

A shared viewer is a UI/data-contract achievement, not evidence that these conditions are scientifically comparable.

## Automated parity checks after Pilot 3C

The repository should automatically verify:

1. both traces parse as JSON;
2. both conform to the same semantic required fields;
3. both have 25-cell neural summary arrays;
4. all displayed decoder/neural/body numbers are finite;
5. each trace identifies its model stack and scientific boundary.

## Matched comparison is a separate gate

Only `CROSS_VERSION_REGRESSION_PLAN.md` can authorize a matched version comparison.

Trace parity alone must never be described as model equivalence.
