#!/usr/bin/env python3
"""ARIS4C018 Pilot4 R1: deterministic Retina/indexing signature."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


def sha(arr):
    arr = np.ascontiguousarray(arr)
    return hashlib.sha256(arr.tobytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stack", choices=["legacy", "current"], required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    if args.stack == "legacy":
        from flygym_gymnasium.vision import Retina
        from flygym_gymnasium.examples.vision import RetinaMapper
        model_stack = "legacy FlyGym 1.3.2 + flyvis 1.1.2"
    else:
        from flygym.vision.retina import Retina
        from flygym2_flyvis_adapter import FlyGym2RetinaMapper as RetinaMapper
        model_stack = "current FlyGym 2.x + current flyvis"

    retina = Retina()
    mapper = RetinaMapper(retina=retina)

    id_map = np.asarray(retina.ommatidia_id_map)
    ids = np.unique(id_map[id_map > 0])
    idx = np.asarray(mapper._idx_flyvis_to_flygym, dtype=np.int64)

    pale = getattr(retina, "pale_type_mask", None)
    pale_summary = None
    if pale is not None:
        pale = np.asarray(pale)
        pale_summary = {
            "count": int(pale.size),
            "true_or_one": int(np.count_nonzero(pale)),
            "false_or_zero": int(pale.size - np.count_nonzero(pale)),
            "sha256": sha(pale.astype(np.uint8)),
        }

    result = {
        "schema_version": 1,
        "side": args.stack,
        "model_stack": model_stack,
        "retina": {
            "nrows": int(retina.nrows),
            "ncols": int(retina.ncols),
            "num_ommatidia_per_eye": int(retina.num_ommatidia_per_eye),
            "id_map_shape": list(id_map.shape),
            "id_map_dtype": str(id_map.dtype),
            "id_map_max": int(id_map.max()),
            "unique_nonzero_ids": int(ids.size),
            "covered_pixels": int(np.count_nonzero(id_map > 0)),
            "id_map_sha256": sha(id_map),
            "pale_type": pale_summary,
        },
        "mapper": {
            "length": int(idx.size),
            "min": int(idx.min()),
            "max": int(idx.max()),
            "unique": int(np.unique(idx).size),
            "bijection_0_to_n_minus_1": bool(
                np.array_equal(np.sort(idx), np.arange(idx.size))
            ),
            "flyvis_to_flygym_sha256": sha(idx),
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("ARIS4C018 Pilot4 R1 retina signature PASS")
    print("RESULT_JSON=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
