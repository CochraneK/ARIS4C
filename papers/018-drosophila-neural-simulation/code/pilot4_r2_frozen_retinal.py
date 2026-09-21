#!/usr/bin/env python3
"""ARIS4C018 Pilot4 R2: frozen retinal vectors -> mapper -> pinned flyvis.

No MuJoCo scene, renderer, body, target geom, decoder or controller is used.
This localizes cross-version differences between:
R2a FlyGym retinal ordering mapper
R2b flyvis model/version/dynamics
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch
from flyvis.utils.activity_utils import LayerActivity


TRACKING_CELLS = [
    "T2", "T2a", "T3",
    "Tm1", "Tm2", "Tm3", "Tm4", "Tm5Y", "Tm5a", "Tm5b", "Tm5c",
    "Tm9", "Tm16", "Tm20", "Tm28", "Tm30",
    "TmY3", "TmY4", "TmY5a", "TmY9", "TmY10", "TmY13", "TmY14",
    "TmY15", "TmY18",
]
N = 721
DT = 1 / 500
FADE_IN_S = 1.0


def digest(arr):
    x = np.ascontiguousarray(np.asarray(arr, dtype=np.float32))
    return hashlib.sha256(x.tobytes()).hexdigest()


def stimuli():
    g = np.linspace(0.0, 1.0, N, dtype=np.float32)
    rng = np.random.RandomState(1804)
    out = {
        "uniform_0p5": np.full((2, N), 0.5, dtype=np.float32),
        "gradient_mirror": np.stack([g, g[::-1]], axis=0),
        "random_seed1804": rng.random_sample((2, N)).astype(np.float32),
    }
    for idx in [0, 360, 720]:
        x = np.zeros((2, N), dtype=np.float32)
        x[0, idx] = 1.0
        x[1, N - 1 - idx] = 1.0
        out[f"mirror_impulse_{idx}"] = x
    return out


def load(stack):
    if stack == "legacy":
        import flyvis
        from flygym_gymnasium.examples.vision import (
            RealTimeVisionNetworkView,
            RetinaMapper,
        )
        mapper = RetinaMapper()
        view = RealTimeVisionNetworkView(flyvis.results_dir / "flow/0000/000")
        network = view.init_network(chkpt="best_chkpt")
        label = "legacy FlyGym 1.3.2 + flyvis 1.1.2"
    else:
        from flygym2_flyvis_adapter import (
            FlyGym2RetinaMapper,
            load_pretrained_stepwise_network,
        )
        mapper = FlyGym2RetinaMapper()
        network = load_pretrained_stepwise_network()
        label = "current FlyGym 2.x + current flyvis"
    return mapper, network, label


def setup_neutral(network, mapper):
    neutral = np.full((2, N), 0.5, dtype=np.float32)
    mapped = mapper.flygym_to_flyvis(neutral)
    x = torch.as_tensor(mapped, dtype=torch.float32, device="cpu")
    initial_state = network.fade_in_state(
        t_fade_in=FADE_IN_S,
        dt=DT,
        initial_frames=x.unsqueeze(1),
    )
    network.setup_step_by_step_simulation(
        dt=DT,
        initial_state=initial_state,
        as_states=False,
        num_samples=2,
    )


def summarize(stack):
    mapper, network, label = load(stack)
    results = {}

    for name, retinal in stimuli().items():
        mapped = np.asarray(mapper.flygym_to_flyvis(retinal), dtype=np.float32)

        setup_neutral(network, mapper)
        x = torch.as_tensor(mapped, dtype=torch.float32, device="cpu")
        activity = network.forward_one_step(x).detach().cpu().numpy()
        network.cleanup_step_by_step_simulation()

        assert activity.shape == (2, 45669)
        assert np.isfinite(activity).all()

        layer = LayerActivity(
            activity,
            network.connectome,
            keepref=True,
            use_central=False,
        )
        cell_means = {}
        flat = []
        for cell in TRACKING_CELLS:
            arr = np.asarray(layer[cell], dtype=float)
            lr = [float(np.mean(arr[0])), float(np.mean(arr[1]))]
            cell_means[cell] = lr
            flat.extend(lr)

        results[name] = {
            "retinal_sha256": digest(retinal),
            "mapped_sha256": digest(mapped),
            "mapped_mean": float(np.mean(mapped)),
            "mapped_std": float(np.std(mapped)),
            "neural_sha256_float32": digest(activity),
            "neural_shape": list(activity.shape),
            "neural_mean": float(np.mean(activity)),
            "neural_std": float(np.std(activity)),
            "neural_l2": float(np.linalg.norm(activity)),
            "tracking_cell_means": cell_means,
            "tracking_flat": flat,
        }

    return {
        "schema_version": 1,
        "side": stack,
        "model_stack": label,
        "dt": DT,
        "neutral_fade_in_s": FADE_IN_S,
        "stimulus_definition": (
            "Deterministic vectors in FlyGym ommatidium order; each test resets "
            "flyvis from a 1s uniform-0.5 neutral fade-in before one frozen step."
        ),
        "stimuli": results,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stack", choices=["legacy", "current"], required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    result = summarize(args.stack)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("ARIS4C018 Pilot4 R2 frozen-retinal PASS")
    print("RESULT_JSON=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
