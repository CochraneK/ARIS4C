#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

import pilot0_ring_attractor as mod

baseline = mod.summarize([0.0], seeds=10)[0]
lesioned = mod.summarize([0.4], seeds=10)[0]

assert baseline["mean_heading_error_deg"] < 1.0
assert lesioned["mean_heading_error_deg"] > baseline["mean_heading_error_deg"]
assert 0.0 <= baseline["recovery_success_rate"] <= 1.0
assert 0.0 <= lesioned["recovery_success_rate"] <= 1.0

print("ARIS4C018 Pilot0 smoke PASS")
