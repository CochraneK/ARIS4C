#!/usr/bin/env python3
"""Compare Pilot4 R2 frozen-retinal outputs without an equivalence verdict."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--legacy",type=Path,required=True)
    ap.add_argument("--current",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=json.loads(ap.parse_args().legacy.read_text()) if False else None

    args=ap.parse_args()
    legacy=json.loads(args.legacy.read_text())
    current=json.loads(args.current.read_text())

    assert legacy["dt"] == current["dt"]
    assert legacy["neutral_fade_in_s"] == current["neutral_fade_in_s"]
    assert set(legacy["stimuli"]) == set(current["stimuli"])

    comparison={}
    all_mapping_equal=True
    for name in legacy["stimuli"]:
        l=legacy["stimuli"][name]
        c=current["stimuli"][name]
        mapping_equal=l["mapped_sha256"] == c["mapped_sha256"]
        all_mapping_equal &= mapping_equal

        la=np.asarray(l["tracking_flat"],dtype=float)
        ca=np.asarray(c["tracking_flat"],dtype=float)
        comparison[name]={
            "retinal_sha_equal": l["retinal_sha256"] == c["retinal_sha256"],
            "mapped_sha_equal": mapping_equal,
            "neural_sha_equal": l["neural_sha256_float32"] == c["neural_sha256_float32"],
            "neural_mean": {
                "legacy": l["neural_mean"],
                "current": c["neural_mean"],
                "delta": c["neural_mean"]-l["neural_mean"],
            },
            "neural_std": {
                "legacy": l["neural_std"],
                "current": c["neural_std"],
                "delta": c["neural_std"]-l["neural_std"],
            },
            "neural_l2": {
                "legacy": l["neural_l2"],
                "current": c["neural_l2"],
                "delta": c["neural_l2"]-l["neural_l2"],
            },
            "tracking_cell_mean_mae": float(np.mean(np.abs(ca-la))),
            "tracking_cell_mean_max_abs_diff": float(np.max(np.abs(ca-la))),
        }

    out={
        "schema_version":1,
        "status":"DIAGNOSTIC_COMPLETE",
        "r2a_all_mapped_vectors_equal":bool(all_mapping_equal),
        "r2b_neural_hashes_all_equal":all(
            x["neural_sha_equal"] for x in comparison.values()
        ),
        "stimuli":comparison,
        "interpretation_rule":(
            "Exact R2a equality excludes mapper output for these frozen vectors. "
            "R2b numerical differences then localize to flyvis model/version/dynamics "
            "or numerical stack, not renderer/body/decoder/controller."
        ),
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2)+"\n")
    print("ARIS4C018 Pilot4 R2 comparison PASS")
    print(json.dumps(out,sort_keys=True))


if __name__=="__main__":
    main()
