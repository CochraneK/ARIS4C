#!/usr/bin/env python3
"""Validate a reconstructed Williams 2016 crisp-set matrix against published targets."""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ROOT / "data" / "PUBLISHED_REPLICATION_TARGETS_V1.json"

COLS = ["A", "P", "W", "I", "S", "E"]
TARGET_KEYS = {
    "A": "A_autocracy",
    "P": "P_political_upheaval",
    "W": "W_war",
    "I": "I_exclusionary_ideology",
    "S": "S_elite_ethnicity_salient",
    "E": "E_economic_autarky",
}


def load_rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    required = {"case_id", "outcome_genocide", *COLS}
    missing = required.difference(rows[0].keys() if rows else [])
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    for row in rows:
        for col in ["outcome_genocide", *COLS]:
            value = str(row[col]).strip()
            if value not in {"0", "1"}:
                raise ValueError(f"{row.get('case_id')}: {col} must be 0/1, got {value!r}")
            row[col] = int(value)
    return rows


def path_match(row: dict, formula: str) -> bool:
    for literal in formula.split("*"):
        literal = literal.strip()
        neg = literal.startswith("~")
        key = literal[1:] if neg else literal
        value = row[key]
        if (value == 1) == neg:
            return False
    return True


def path_stats(rows: list[dict], formula: str) -> dict:
    positives = sum(r["outcome_genocide"] for r in rows)
    matched = [r for r in rows if path_match(r, formula)]
    matched_pos = sum(r["outcome_genocide"] for r in matched)
    return {
        "formula": formula,
        "matched_n": len(matched),
        "matched_positive_n": matched_pos,
        "raw_coverage": matched_pos / positives if positives else math.nan,
        "consistency": matched_pos / len(matched) if matched else math.nan,
    }


def solution_stats(rows: list[dict], formulas: list[str]) -> dict:
    positives = sum(r["outcome_genocide"] for r in rows)
    predicted = [r for r in rows if any(path_match(r, f) for f in formulas)]
    tp = sum(r["outcome_genocide"] for r in predicted)
    fp = len(predicted) - tp
    return {
        "predicted_n": len(predicted),
        "true_positive": tp,
        "false_positive": fp,
        "coverage": tp / positives if positives else math.nan,
        "consistency": tp / len(predicted) if predicted else math.nan,
    }


def close(a: float, b: float, tol: float = 0.002) -> bool:
    return abs(a - b) <= tol


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("matrix", type=Path)
    ap.add_argument("--json-out", type=Path)
    args = ap.parse_args()

    target = json.loads(TARGETS.read_text(encoding="utf-8"))["williams_2016"]
    rows = load_rows(args.matrix)
    failures: list[str] = []

    n_pos = sum(r["outcome_genocide"] for r in rows)
    n_neg = len(rows) - n_pos
    exp_u = target["analysis_universe"]
    for label, got, exp in [
        ("total", len(rows), exp_u["total"]),
        ("genocide", n_pos, exp_u["genocide"]),
        ("non_genocide", n_neg, exp_u["non_genocide"]),
    ]:
        if got != exp:
            failures.append(f"{label}: got {got}, expected {exp}")

    margins = {}
    for col in COLS:
        pos = sum(r[col] for r in rows if r["outcome_genocide"] == 1)
        neg = sum(r[col] for r in rows if r["outcome_genocide"] == 0)
        total = pos + neg
        margins[col] = {"genocide_present": pos, "non_genocide_present": neg, "total_present": total}
        exp = target["conditions"][TARGET_KEYS[col]]
        for field, got in margins[col].items():
            if got != exp[field]:
                failures.append(f"{col}.{field}: got {got}, expected {exp[field]}")

    formulas = [p["formula"] for p in target["published_intermediate_solution"]["paths"]]
    paths = [path_stats(rows, f) for f in formulas]
    sol = solution_stats(rows, formulas)
    exp_sol = target["published_intermediate_solution"]

    for field, got, exp in [
        ("solution.predicted_n", sol["predicted_n"], exp_sol["predicted_genocide_total"]),
        ("solution.true_positive", sol["true_positive"], exp_sol["true_positive"]),
        ("solution.false_positive", sol["false_positive"], exp_sol["false_positive"]),
    ]:
        if got != exp:
            failures.append(f"{field}: got {got}, expected {exp}")

    for field, got, exp in [
        ("solution.coverage", sol["coverage"], exp_sol["solution_coverage"]),
        ("solution.consistency", sol["consistency"], exp_sol["solution_consistency"]),
    ]:
        if not close(got, exp):
            failures.append(f"{field}: got {got:.4f}, expected {exp:.4f}")

    for got, exp in zip(paths, exp_sol["paths"]):
        for field in ["raw_coverage", "consistency"]:
            if not close(got[field], exp[field]):
                failures.append(
                    f"{got['formula']}.{field}: got {got[field]:.4f}, expected {exp[field]:.4f}"
                )

    report = {
        "matrix": str(args.matrix),
        "rows": len(rows),
        "outcome_counts": {"genocide": n_pos, "non_genocide": n_neg},
        "margins": margins,
        "paths": paths,
        "solution": sol,
        "failures": failures,
        "status": "PASS" if not failures else "FAIL",
        "note": "Unique coverage is not validated here because it requires path-overlap attribution; add after exact matrix reconstruction is stable.",
    }

    text = json.dumps(report, indent=2, ensure_ascii=False)
    print(text)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text + "\n", encoding="utf-8")
    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
