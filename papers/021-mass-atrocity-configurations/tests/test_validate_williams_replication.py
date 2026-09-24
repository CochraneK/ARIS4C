#!/usr/bin/env python3
"""Unit tests for Williams published-solution evaluator."""

from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE = HERE.parent / "code" / "validate_williams_replication.py"
spec = importlib.util.spec_from_file_location("rep", MODULE)
rep = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(rep)


def row(**kw):
    base = {"outcome_genocide": 0, "A": 0, "P": 0, "W": 0, "I": 0, "S": 0, "E": 0}
    base.update(kw)
    return base


def test_path_match_positive_and_negated_literals():
    r = row(A=1, I=1, E=1, P=1, W=0)
    assert rep.path_match(r, "A*I*E*P*~W")
    assert not rep.path_match(r, "A*I*E*~P*W")


def test_solution_union_not_double_counted():
    rows = [
        row(outcome_genocide=1, A=1, S=1, I=1, P=1),
        row(outcome_genocide=0, A=1, S=1, I=1),
        row(outcome_genocide=0),
    ]
    out = rep.solution_stats(rows, ["A*S*I", "A*S*P"])
    assert out["predicted_n"] == 2
    assert out["true_positive"] == 1
    assert out["false_positive"] == 1
    assert out["coverage"] == 1.0
    assert out["consistency"] == 0.5


if __name__ == "__main__":
    test_path_match_positive_and_negated_literals()
    test_solution_union_not_double_counted()
    print("PASS")
