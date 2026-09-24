#!/usr/bin/env python3
"""Cross-check Williams positive episodes against IBM transformed PITF annual data.

Episode membership is evaluated by interval overlap with positive annual
DEATHMAG, not by requiring every year of the interval to be positive.
"""

from __future__ import annotations
import argparse, csv, json
from pathlib import Path

ALIASES = {
    "Bosnia": "Bosnia and Herzegovina",
    "DR Congo": "Congo (Democratic Republic of the)",
    "Iran": "Iran (Islamic Republic of)",
    "Myanmar (Burma)": "Myanmar",
    "Pakistan (now Bangladesh)": "Pakistan",
    "Syria": "Syrian Arab Republic",
    "Vietnam South": "Viet Nam",
}

def load_seed(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return [r for r in rows if r["analysis_included"] == "1"]

def load_ibm(path: Path) -> dict[str, set[int]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    out: dict[str, set[int]] = {}
    for r in rows:
        if r.get("Indicator Code") != "SP.GE.MAG.DEATH":
            continue
        try:
            value = float(r.get("value") or 0)
            year = int(float(r.get("year") or 0))
        except ValueError:
            continue
        if value > 0:
            out.setdefault(r.get("Country Name", ""), set()).add(year)
    return out

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("seed", type=Path)
    ap.add_argument("ibm_filtered", type=Path)
    ap.add_argument("--json-out", type=Path)
    args = ap.parse_args()

    seed = load_seed(args.seed)
    ibm = load_ibm(args.ibm_filtered)
    rows = []
    for case in seed:
        country = case["country"]
        ibm_country = ALIASES.get(country, country)
        start, end = int(case["start_year"]), int(case["end_year"])
        expected = list(range(start, end + 1))
        positive = sorted(y for y in expected if y in ibm.get(ibm_country, set()))
        missing = sorted(set(expected).difference(positive))
        rows.append({
            "case_id": case["case_id"], "country": country, "ibm_country": ibm_country,
            "start": start, "end": end, "expected_years": len(expected),
            "positive_years": len(positive),
            "coverage": round(len(positive) / len(expected), 3),
            "first_positive": positive[0] if positive else None,
            "last_positive": positive[-1] if positive else None,
            "missing_positive_years": missing,
            "any_overlap": bool(positive),
        })

    report = {
        "included_cases": len(rows),
        "any_overlap": sum(r["any_overlap"] for r in rows),
        "full_year_coverage": sum(r["coverage"] == 1.0 for r in rows),
        "partial_year_coverage": sum(r["any_overlap"] and r["coverage"] < 1.0 for r in rows),
        "no_overlap": sum(not r["any_overlap"] for r in rows),
        "cases": rows,
        "status": "PASS" if len(rows) == 40 and all(r["any_overlap"] for r in rows) else "FAIL",
        "interpretation": "Episode identity requires overlap, not annual continuity of DEATHMAG>0."
    }
    text = json.dumps(report, indent=2, ensure_ascii=False)
    print(text)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text + "\n", encoding="utf-8")
    return 0 if report["status"] == "PASS" else 2

if __name__ == "__main__":
    raise SystemExit(main())
