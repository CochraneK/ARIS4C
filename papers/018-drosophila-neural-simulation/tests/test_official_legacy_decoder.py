#!/usr/bin/env python3
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from official_legacy_decoder import object_mask_from_zscores, turning_from_object_mask


def main():
    # 4 synthetic ommatidia at two horizontal positions.
    coms = np.array([
        [1, 1],
        [1, 3],
        [3, 1],
        [3, 3],
    ], dtype=float)

    # No detected object -> symmetric unit drive.
    empty = np.zeros((2, 4), dtype=bool)
    out = turning_from_object_mask(
        empty, coms, retina_nrows=4, retina_ncols=4, tracking_gain=6
    )
    assert out["turning_bias"] == 0
    assert np.allclose(out["dn_drive"], [1, 1])

    # Mirrored one-eye masks must generate opposite biases and mirrored drives.
    left_eye = np.zeros((2, 4), dtype=bool)
    right_eye = np.zeros((2, 4), dtype=bool)
    left_eye[0, [0, 2]] = True
    right_eye[1, [1, 3]] = True

    a = turning_from_object_mask(
        left_eye, coms, retina_nrows=4, retina_ncols=4, tracking_gain=6
    )
    b = turning_from_object_mask(
        right_eye, coms, retina_nrows=4, retina_ncols=4, tracking_gain=6
    )
    assert np.isclose(a["turning_bias"], -b["turning_bias"])
    assert np.allclose(a["dn_drive"], b["dn_drive"][::-1])

    # Saturation limits are part of the upstream engineering decoder.
    for x in [a, b]:
        assert np.all(x["dn_drive"] >= 0.4)
        assert np.all(x["dn_drive"] <= 1.2)

    # z-score aggregation / thresholding.
    z = np.zeros((3, 2, 4), dtype=float)
    z[:, 1, 2] = 6
    mask, mean = object_mask_from_zscores(z, threshold=5)
    assert mask.sum() == 1
    assert mask[1, 2]
    assert mean[1, 2] == 6

    print("ARIS4C018 official legacy decoder unit tests PASS")


if __name__ == "__main__":
    main()
