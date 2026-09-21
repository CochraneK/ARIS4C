"""ARIS4C018 adapter: current FlyGym 2.x Retina -> current flyvis stepwise network.

The mapping and stepwise-network logic are ported from the official legacy
FlyGym advanced-vision implementation, but target the current FlyGym 2.x
Simulation.get_ommatidia_readouts API.

Scientific boundary:
- Retina + flyvis neural state: biologically/connectome-constrained model layer.
- No neural-to-motor decoder is implemented here.
"""

from __future__ import annotations

import warnings
from typing import Optional, Union

import flyvis
import numpy as np
import torch
from flyvis.datasets.rendering import BoxEye
from flyvis.network.network import Network, IntegrationWarning
from flyvis.utils.tensor_utils import AutoDeref
from flygym.vision.retina import Retina


class FlyGym2RetinaMapper:
    """Map current FlyGym 2.x ommatidia ordering to flyvis BoxEye ordering."""

    def __init__(self, retina: Optional[Retina] = None, boxeye: Optional[BoxEye] = None):
        retina = retina or Retina()
        boxeye = boxeye or BoxEye(extent=15)

        receptor_centers = boxeye.receptor_centers.cpu().numpy()
        horiz = sorted(np.unique(receptor_centers[:, 1]))
        col_min, col_max = horiz[0], horiz[-1]
        left = receptor_centers[receptor_centers[:, 1] == col_min]
        right = receptor_centers[receptor_centers[:, 1] == col_max]
        flyvis_a = np.array([left[:, 0].min(), col_min])
        flyvis_b = np.array([right[:, 0].max(), col_max])

        a_rows, a_cols = np.where(retina.ommatidia_id_map == 1)
        flygym_a = np.array([a_rows.mean(), a_cols.mean()])
        max_id = retina.ommatidia_id_map.max()
        b_rows, b_cols = np.where(retina.ommatidia_id_map == max_id)
        flygym_b = np.array([b_rows.mean(), b_cols.mean()])

        row_k = (flygym_b[0] - flygym_a[0]) / (flyvis_b[0] - flyvis_a[0])
        row_b = flygym_a[0] - row_k * flyvis_a[0]
        col_k = (flygym_b[1] - flygym_a[1]) / (flyvis_b[1] - flyvis_a[1])
        col_b = flygym_a[1] - col_k * flyvis_a[1]

        centers = np.empty_like(receptor_centers)
        centers[:, 0] = row_k * receptor_centers[:, 0] + row_b
        centers[:, 1] = col_k * receptor_centers[:, 1] + col_b
        centers = np.rint(centers).astype(int)

        idx_flyvis_to_flygym = np.array(
            [retina.ommatidia_id_map[r, c] for r, c in centers], dtype=int
        ) - 1

        if len(np.unique(idx_flyvis_to_flygym)) != retina.num_ommatidia_per_eye:
            raise RuntimeError("FlyGym2<->flyvis retinal mapping is not one-to-one")

        self._idx_flyvis_to_flygym = idx_flyvis_to_flygym
        self._idx_flygym_to_flyvis = np.argsort(idx_flyvis_to_flygym)
        self.num_ommatidia = retina.num_ommatidia_per_eye

    def flygym_to_flyvis(self, stimulus: np.ndarray) -> np.ndarray:
        stimulus = np.asarray(stimulus)
        if stimulus.shape[-1] != self.num_ommatidia:
            raise ValueError(
                f"Expected last dimension {self.num_ommatidia}, got {stimulus.shape[-1]}"
            )
        return stimulus[..., self._idx_flyvis_to_flygym]

    def flyvis_to_flygym(self, stimulus: np.ndarray) -> np.ndarray:
        stimulus = np.asarray(stimulus)
        if stimulus.shape[-1] != self.num_ommatidia:
            raise ValueError(
                f"Expected last dimension {self.num_ommatidia}, got {stimulus.shape[-1]}"
            )
        return stimulus[..., self._idx_flygym_to_flyvis]


class StepwiseFlyvisNetwork(Network):
    """Current flyvis Network with the official legacy one-frame-at-a-time API."""

    def setup_step_by_step_simulation(
        self,
        dt: float,
        initial_state: Union[str, AutoDeref, None] = "auto",
        as_states: bool = False,
        num_samples: int = 1,
    ) -> None:
        if dt > 1 / 50:
            with warnings.catch_warnings():
                warnings.simplefilter("always")
                warnings.warn(
                    f"dt={dt} is large for integration; prefer <= 1/50",
                    IntegrationWarning,
                    stacklevel=2,
                )

        is_training = self.training
        self.training = False
        params_requiring_grad = {}
        for name, params in self.named_parameters():
            params_requiring_grad[name] = params.requires_grad
            params.requires_grad = False

        self.clamp()
        params = self._param_api()

        if initial_state is None:
            initial_state = self._initial_state(params=params, batch_size=1)
        elif initial_state == "auto":
            initial_state = self.steady_state(t_pre=1.0, dt=dt, batch_size=1)
        self._current_step_by_step_sim_state = initial_state

        layer_index = {
            cell_type: index[:]
            for cell_type, index in self.connectome.nodes.layer_index.items()
        }
        input_node_index = np.array(
            [
                layer_index[cell_type.decode()]
                for cell_type in self.connectome.input_cell_types[:]
            ]
        )

        self._step_by_step_sim_params = {
            "dt": dt,
            "is_training": is_training,
            "params_requiring_grad": params_requiring_grad,
            "as_states": as_states,
            "sim_params": params,
            "num_nodes": len(self.connectome.nodes.type),
            "num_samples": num_samples,
            "input_node_index": input_node_index,
        }

    def cleanup_step_by_step_simulation(self) -> None:
        self._check_step_by_step_simulation_setup()
        self.training = self._step_by_step_sim_params["is_training"]
        for name, params in self.named_parameters():
            params.requires_grad = self._step_by_step_sim_params[
                "params_requiring_grad"
            ][name]
        del self._step_by_step_sim_params
        del self._current_step_by_step_sim_state

    def forward_one_step(self, curr_visual_input: torch.Tensor):
        self._check_step_by_step_simulation_setup()

        p = self._step_by_step_sim_params
        stimulus_buffer = torch.zeros(
            (p["num_samples"], p["num_nodes"]),
            device=curr_visual_input.device,
        )
        for i in range(p["num_samples"]):
            stimulus_buffer[i, p["input_node_index"]] += curr_visual_input[i]

        self._current_step_by_step_sim_state = self._next_state(
            params=p["sim_params"],
            state=self._current_step_by_step_sim_state,
            x_t=stimulus_buffer,
            dt=p["dt"],
        )

        if p["as_states"]:
            return self._current_step_by_step_sim_state
        return self._current_step_by_step_sim_state.nodes.activity

    def _check_step_by_step_simulation_setup(self) -> None:
        if not hasattr(self, "_step_by_step_sim_params"):
            raise RuntimeError("Call setup_step_by_step_simulation() first")


def load_pretrained_stepwise_network(
    network_dir=None,
) -> StepwiseFlyvisNetwork:
    """Load current flyvis pretrained flow model 0000/000 into stepwise subclass."""
    flyvis.device = torch.device("cpu")
    if network_dir is None:
        network_dir = flyvis.results_dir / "flow/0000/000"

    view = flyvis.NetworkView(network_dir)
    network = StepwiseFlyvisNetwork(**view.dir.config.network)
    return view.init_network(network=network)


def initialize_from_flygym_readouts(
    network: StepwiseFlyvisNetwork,
    mapper: FlyGym2RetinaMapper,
    ommatidia_readouts: np.ndarray,
    *,
    dt: float = 1 / 500,
    fade_in_s: float = 1.0,
) -> torch.Tensor:
    """Initialize with a frozen current FlyGym retinal frame for both eyes."""
    gray = np.asarray(ommatidia_readouts).max(axis=-1)
    visual_input = mapper.flygym_to_flyvis(gray)
    visual_input_t = torch.as_tensor(visual_input, dtype=torch.float32, device="cpu")

    initial_state = network.fade_in_state(
        t_fade_in=fade_in_s,
        dt=dt,
        initial_frames=visual_input_t.unsqueeze(1),
    )
    network.setup_step_by_step_simulation(
        dt=dt,
        initial_state=initial_state,
        as_states=False,
        num_samples=2,
    )
    return visual_input_t
