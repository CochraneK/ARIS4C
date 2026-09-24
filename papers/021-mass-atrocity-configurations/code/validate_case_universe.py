#!/usr/bin/env python3
"""Validate ARIS4C021 case-universe reconstruction contracts."""

from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ROOT / "data" / "PUBLISHED_REPLICATION_TARGETS_V1.json"

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("case_universe", type=Path)
    args = ap.parse_args()

    with args.case_universe.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit("empty case universe")

    required = {"case_id","outcome_genocide","analysis_included"}
    missing = required.difference(rows[0])
    if missing:
        raise SystemExit(f"missing columns: {sorted(missing)}")

    included=[r for r in rows if str(r["analysis_included"]).strip()=="1"]
    pos=[r for r in included if str(r["outcome_genocide"]).strip()=="1"]
    neg=[r for r in included if str(r["outcome_genocide"]).strip()=="0"]

    target=json.loads(TARGETS.read_text(encoding="utf-8"))["williams_2016"]["analysis_universe"]
    failures=[]
    if len(included)!=target["total"]:
        failures.append(f"total included {len(included)} != {target['total']}")
    if len(pos)!=target["genocide"]:
        failures.append(f"positive {len(pos)} != {target['genocide']}")
    if len(neg)!=target["non_genocide"]:
        failures.append(f"controls {len(neg)} != {target['non_genocide']}")
    if len({r["case_id"] for r in included})!=len(included):
        failures.append("duplicate included case_id")

    status="PASS" if not failures else "FAIL"
    print(json.dumps({
      "status":status,
      "included":len(included),
      "positive":len(pos),
      "controls":len(neg),
      "failures":failures
    }, indent=2))
    return 0 if not failures else 2

if __name__ == "__main__":
    raise SystemExit(main())
