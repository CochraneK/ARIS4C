# Blinded Calibration Packet · v0.1

This directory contains the first reliability packet for ARIS4C-023.

## Files

- `motifs_v0.1.csv`: 24 frozen calibration motifs.
- `packet_template.csv`: 15 passages × 8 family-specific motifs = 120 judgments.
- `coder_A.csv` and `coder_B.csv`: byte-identical blank copies at freeze.
- `score_calibration.py`: dependency-free scorer.

## Allowed states

- `present`
- `absent`
- `uncertain`
- `not_observed`

Blank means **not yet coded** and is not a state.

## Blinding

Coder A and B must not see:
- controller seed judgments;
- each other's responses;
- similarity/clustering output;
- hypothesized transmission path for the coded item.

## Release blocker

`P_ANTH_ATRA` is not coder-ready until an exact scholarly-edition passage locator is inserted. The row remains in the packet to make the missing requirement explicit.

## Scoring

Run:

```bash
python code/score_calibration.py \
  --a data/calibration/coder_A.csv \
  --b data/calibration/coder_B.csv \
  --out data/calibration/reliability.json
```

The scorer reports:
- number of common completed judgments;
- four-state raw agreement;
- four-state Cohen kappa;
- four-state Gwet AC1;
- binary present/absent subset agreement, kappa and AC1;
- confusion matrix.

Reliability is a gate, not a target to game. If a motif repeatedly generates disagreement, revise the ontology and rerun a new frozen calibration version.
