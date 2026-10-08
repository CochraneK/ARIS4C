"""Gate E T0: environment probe — interpreter imports + pointer file existence.

stdout budget: <= 15 lines.
"""
import importlib
import os
import sys

PY = sys.executable
print("python:", PY)

mods = ["pandas", "numpy", "networkx", "scipy"]
for m in mods:
    try:
        mod = importlib.import_module(m)
        ver = getattr(mod, "__version__", "?")
        print(f"import {m}: OK {ver}")
    except Exception as e:
        print(f"import {m}: MISSING ({type(e).__name__})")

pointers = [
    "RESEARCH_BRIEF.md",
    "stage3b_summary.md",
    "data/exposure_protocol.md",
    "data/exposure_queue.csv",
    "data/queue_summary.json",
    "data/stage3/pilot_focals.csv",
    "data/stage3/cpe_results.csv",
    "data/stage3/m0_results.csv",
    "data/stage3/m1_results.csv",
    "data/stage3/m1s_results.csv",
    "data/stage3/m2_results.csv",
    "data/stage3/m3_results.csv",
    "data/stage3/benchmark_results.csv",
    "data/stage3/benchmark_report.md",
    "data/stage3/graph_cache.pkl",
    "code/sim_m1s.py",
    "code/sim_m3.py",
    "code/cpe_pilot.py",
]
missing = []
for p in pointers:
    if not os.path.exists(p):
        missing.append(p)
print("pointers checked:", len(pointers), "missing:", len(missing))
if missing:
    for m in missing[:8]:
        print("  MISSING:", m)
