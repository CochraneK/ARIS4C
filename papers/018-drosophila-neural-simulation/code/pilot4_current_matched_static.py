#!/usr/bin/env python3
"""ARIS4C018 Pilot 4: current side of the matched static-target regression."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import pilot3b_flygym2_closed_loop as p3b


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    t0 = time.perf_counter()
    baseline, baseline_meta = p3b.run_baseline()
    target = p3b.run_target(baseline)
    elapsed = time.perf_counter() - t0

    target = dict(target)
    target["mask_detection_rate"] = (
        target["frames_with_object_mask"] / target["decoder_updates"]
    )

    result = {
        "schema_version": 1,
        "side": "current",
        "model_stack": "current FlyGym 2.x + current flyvis",
        "condition": {
            "baseline_s": p3b.BASELINE_S,
            "closed_loop_s": p3b.CLOSED_LOOP_S,
            "vision_hz": p3b.VISION_HZ,
            "spawn_pos": [0.0, 0.0, 1.0],
            "target_pos": [5.0, 2.2, 1.5],
            "target_radius": 1.25,
            "z_score_threshold": p3b.Z_THRESHOLD,
            "tracking_gain": p3b.TRACKING_GAIN,
            "tracking_cells": p3b.TRACKING_CELLS,
        },
        "baseline": baseline_meta,
        "target": target,
        "elapsed_s": elapsed,
        "scientific_boundary": (
            "Matched cross-version engineering diagnostic. Target and decoder settings "
            "are matched, but simulator/body/rendering/flyvis versions remain the "
            "variables under diagnosis. Not a biological effect test."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("ARIS4C018 Pilot4 current matched-static PASS")
    print("RESULT_JSON=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
