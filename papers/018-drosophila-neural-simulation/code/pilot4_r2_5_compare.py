#!/usr/bin/env python3
"""Compare ARIS4C018 Pilot 4 R2.5 legacy/current initial sensory captures."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--legacy", type=Path, required=True)
    ap.add_argument("--current", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    legacy = json.loads(args.legacy.read_text())
    current = json.loads(args.current.read_text())

    lv = legacy["vision"]
    cv = current["vision"]

    result = {
        "schema_version": 1,
        "status": "DIAGNOSTIC_COMPLETE",
        "legacy": legacy,
        "current": current,
        "comparisons": {
            "full_ommatidia_sha_equal": (
                lv["full_sha256_float32"] == cv["full_sha256_float32"]
            ),
            "gray_ommatidia_sha_equal": (
                lv["gray_sha256_float32"] == cv["gray_sha256_float32"]
            ),
            "body_root_position_delta": [
                current["body_root_position"][i] - legacy["body_root_position"][i]
                for i in range(3)
            ],
            "timestep_delta": current["timestep"] - legacy["timestep"],
            "gray_mean_delta": (
                cv["gray_overall"]["mean"] - lv["gray_overall"]["mean"]
            ),
            "gray_std_delta": (
                cv["gray_overall"]["std"] - lv["gray_overall"]["std"]
            ),
            "left_gray_mean_delta": (
                cv["gray_left"]["mean"] - lv["gray_left"]["mean"]
            ),
            "right_gray_mean_delta": (
                cv["gray_right"]["mean"] - lv["gray_right"]["mean"]
            ),
        },
        "interpretation_rule": (
            "If initial ommatidia hashes differ, the matched Pilot4 first-frame "
            "divergence exists before flyvis and must be localized to renderer/"
            "camera/body/scene-reset semantics. If they match, investigate later "
            "neural initialization/temporal-state differences."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print("ARIS4C018 Pilot4 R2.5 comparison PASS")
    print("RESULT_JSON=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
