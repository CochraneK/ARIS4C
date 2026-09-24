# Blinded Calibration Packet · v0.1

This directory contains the first reliability packet for ARIS4C-023.

## Files

- `motifs_v0.1.csv`: 24 frozen calibration motifs.
- `packet_template.csv`: 15 passages × 8 family-specific motifs = 120 judgments.
- `coder_A.csv` and `coder_B.csv`: byte-identical blank copies at freeze.
- `score_calibration.py`: dependency-free scorer.
- `../../process/CALIBRATION_PACKET_QA.md`: controller-side locator QA.

## Allowed states

`present`, `absent`, `uncertain`, `not_observed`. Blank means not yet coded.

## Blinding

Coder A and B must not see controller seed judgments, each other's responses, similarity/clustering output, or hypothesized transmission paths.

## Scoring

```bash
python code/score_calibration.py \
  --a data/calibration/coder_A.csv \
  --b data/calibration/coder_B.csv \
  --out data/calibration/reliability.json
```

The scorer reports four-state raw agreement, Cohen kappa, Gwet AC1, the binary present/absent subset, and a confusion matrix.

Reliability is a gate, not a target to game. Recurrent disagreement triggers ontology revision and a newly versioned packet.
