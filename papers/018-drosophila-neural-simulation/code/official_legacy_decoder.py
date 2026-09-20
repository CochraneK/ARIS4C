"""Pure implementation of the official legacy FlyGym fly-following decoder.

Source logic:
NeLy-EPFL/flygym-gymnasium
flygym_gymnasium/examples/vision/follow_fly_closed_loop.py

This module contains only the engineered readout math. It deliberately contains
no flyvis or MuJoCo code so that decoder behavior can be tested independently.
"""
from __future__ import annotations

import numpy as np


def object_mask_from_zscores(
    zscores: np.ndarray,
    threshold: float = 5.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Average selected-cell absolute z-scores and threshold into an object mask."""
    zscores = np.asarray(zscores, dtype=float)
    mean_zscore = np.nanmean(zscores, axis=0)
    mean_zscore = np.nan_to_num(mean_zscore, nan=0.0, posinf=0.0, neginf=0.0)
    return mean_zscore > threshold, mean_zscore


def turning_from_object_mask(
    obj_mask: np.ndarray,
    ommatidia_coms: np.ndarray,
    *,
    retina_nrows: int,
    retina_ncols: int,
    tracking_gain: float = 6.0,
) -> dict:
    """Apply the official mask -> turning bias -> 2-D descending-drive equations."""
    obj_mask = np.asarray(obj_mask, dtype=bool)
    ommatidia_coms = np.asarray(ommatidia_coms, dtype=float)

    if obj_mask.ndim != 2 or obj_mask.shape[0] != 2:
        raise ValueError("obj_mask must have shape (2, n_ommatidia)")
    if ommatidia_coms.shape != (obj_mask.shape[1], 2):
        raise ValueError("ommatidia_coms must have shape (n_ommatidia, 2)")

    size_per_eye = obj_mask.sum(axis=1).astype(float)
    com_per_eye = np.full((2, 2), np.nan)

    for eye_idx in range(2):
        if size_per_eye[eye_idx] > 0:
            masked_xy_coords = ommatidia_coms[obj_mask[eye_idx], :]
            com_per_eye[eye_idx, :] = masked_xy_coords.mean(axis=0)

    com_per_eye /= np.array([retina_nrows, retina_ncols], dtype=float)
    size_per_eye /= obj_mask.shape[1]

    center_deviation = com_per_eye[:, 1].copy()
    center_deviation[0] = 1 - center_deviation[0]

    weighted_deviation = center_deviation.copy()
    weighted_deviation[size_per_eye == 0] = 1e9

    if size_per_eye.sum() == 0:
        turning_bias = 0.0
    else:
        turning_bias = float(
            (
                -size_per_eye[0] * weighted_deviation[0]
                + size_per_eye[1] * weighted_deviation[1]
            )
            / size_per_eye.sum()
        )

    dn_inner = max(0.4, 1 - abs(turning_bias * tracking_gain) * 0.6)
    dn_outer = min(1.2, 1 + abs(turning_bias * tracking_gain) * 0.2)

    if turning_bias < 0:
        dn_drive = np.array([dn_inner, dn_outer], dtype=float)
    else:
        dn_drive = np.array([dn_outer, dn_inner], dtype=float)

    return {
        "turning_bias": turning_bias,
        "dn_drive": dn_drive,
        "size_per_eye": size_per_eye,
        "com_per_eye": com_per_eye,
        "center_deviation": center_deviation,
    }
