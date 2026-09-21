#!/usr/bin/env python3
"""Semantic parity checks for ARIS4C018 legacy/current real-model traces."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRACE_PATHS = {
    "legacy": ROOT / "data/pilot2c_synchronized_trace.json",
    "current": ROOT / "data/pilot3c_current_synchronized_trace.json",
}
FRAME_KEYS = {"t_s", "body", "target", "decoder", "neural"}
DECODER_KEYS = {
    "turning_bias",
    "dn_left",
    "dn_right",
    "object_fraction_left",
    "object_fraction_right",
    "mean_zscore_max",
}


def finite(x):
    return isinstance(x, (int, float)) and math.isfinite(x)


def validate(name, path):
    x = json.loads(path.read_text(encoding="utf-8"))
    assert x["schema_version"] == 1
    assert isinstance(x["provenance"]["model_stack"], str)
    assert x["provenance"]["model_stack"]
    assert isinstance(x["provenance"]["scientific_boundary"], str)
    assert x["provenance"]["scientific_boundary"]
    assert len(x["cell_order"]) == 25
    assert len(set(x["cell_order"])) == 25
    assert len(x["frames"]) > 0

    for i, frame in enumerate(x["frames"]):
        assert FRAME_KEYS <= set(frame), (name, i, "frame keys")
        assert finite(frame["t_s"])
        assert finite(frame["body"]["x"])
        assert finite(frame["body"]["y"])
        assert finite(frame["target"]["x"])
        assert finite(frame["target"]["y"])

        decoder = frame["decoder"]
        assert DECODER_KEYS <= set(decoder), (name, i, "decoder keys")
        for key in DECODER_KEYS:
            assert finite(decoder[key]), (name, i, key)

        neural = frame["neural"]
        assert neural["source_layer"] == "BIO"
        assert len(neural["cell_mean_left"]) == 25
        assert len(neural["cell_mean_right"]) == 25
        assert all(finite(v) for v in neural["cell_mean_left"])
        assert all(finite(v) for v in neural["cell_mean_right"])
        assert all(finite(v) for v in neural["summary"].values())

    return x


def main():
    traces = {name: validate(name, path) for name, path in TRACE_PATHS.items()}

    # Data-contract parity does NOT imply matched experimental conditions.
    assert traces["legacy"]["provenance"]["model_stack"] != traces["current"]["provenance"]["model_stack"]

    print("ARIS4C018 legacy/current trace semantic parity PASS")
    print(f"legacy_frames={len(traces['legacy']['frames'])}")
    print(f"current_frames={len(traces['current']['frames'])}")


if __name__ == "__main__":
    main()
