#!/usr/bin/env python3
"""Compare frozen Pilot 4 legacy/current engineering metrics without ranking."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


METRICS = {
    "mask_detection_rate": ("target", "mask_detection_rate"),
    "turning_bias_mean_abs": ("target", "turning_bias_mean_abs"),
    "drive_diff_mean_abs": ("target", "drive_diff_mean_abs"),
    "displacement": ("target", "displacement"),
    "runtime_s": ("elapsed_s",),
    "zero_std_fraction": ("baseline", "zero_std_fraction"),
}


def get(x, path):
    for key in path:
        x = x[key]
    return float(x)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--legacy", type=Path, required=True)
    ap.add_argument("--current", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    legacy = json.loads(args.legacy.read_text())
    current = json.loads(args.current.read_text())

    # Freeze-condition parity before comparing outputs.
    assert legacy["condition"] == current["condition"], {
        "legacy": legacy["condition"],
        "current": current["condition"],
    }

    comparison = {}
    for name, path in METRICS.items():
        lv = get(legacy, path)
        cv = get(current, path)
        comparison[name] = {
            "legacy": lv,
            "current": cv,
            "current_minus_legacy": cv - lv,
            "current_over_legacy": (cv / lv) if lv != 0 else None,
        }

    out = {
        "schema_version": 1,
        "status": "DIAGNOSTIC_COMPLETE",
        "condition": legacy["condition"],
        "stacks": {
            "legacy": legacy["model_stack"],
            "current": current["model_stack"],
        },
        "pre_frozen_metrics": comparison,
        "interpretation_rule": (
            "This first matched run is diagnostic. No post-hoc equivalence threshold, "
            "winner, biological interpretation, or version-quality ranking is allowed."
        ),
        "next_localization_order": [
            "R1 retina geometry/order",
            "R2 frozen retinal stimulus -> flyvis",
            "R3 pure decoder (already unit-tested)",
            "R4 controller semantics",
            "R5 embodied trajectory",
        ],
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print("ARIS4C018 Pilot4 matched cross-version diagnostic PASS")
    for name, vals in comparison.items():
        print(
            f"{name}: legacy={vals['legacy']:.9g} "
            f"current={vals['current']:.9g} "
            f"delta={vals['current_minus_legacy']:.9g}"
        )


if __name__ == "__main__":
    main()
