# ARIS4C018 · Trace Analysis Rules

## What the current 100-frame trace can support

- deterministic replay;
- engineering debugging;
- provenance-aware visualization;
- descriptive time-series inspection;
- selection of candidate diagnostics for future experiments.

## What it cannot support

Do not use the trace alone for:

- inferential p-values based on 100 frames;
- treating frames as independent replicates;
- cell-type discovery claims;
- causal claims from correlation;
- successful-following claims;
- biological validation of the engineered decoder.

## Unit of replication for future science

A future confirmatory analysis should define independent runs/trials/seeds or perturbation instances as the replication unit, not visual-update frames.

## Decoder-induced dependence

`turning_bias -> descending_drive` is an engineered deterministic mapping.

Any strong correlation between these quantities is implementation validation, not biological evidence.

## Neural summaries

The replay UI stores mean left/right activity per selected cell type for visual interpretability.

The published decoder instead uses:

```
cell-wise spatial activity
 -> baseline z-score maps
 -> average across selected cell types
 -> thresholded spatial object mask
```

Therefore mean cell-type activity is a visualization summary only.

## Future trace extension

For a hypothesis-testing run, add:

- perturbation identity;
- independent trial/seed ID;
- intact/null/control identity;
- selected spatial neural-map summaries or hashes;
- decoder saturation flags;
- observer-target distance;
- body heading;
- exact upstream/model commit;
- baseline provenance.
