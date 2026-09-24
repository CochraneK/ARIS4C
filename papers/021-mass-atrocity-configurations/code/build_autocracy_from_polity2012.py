#!/usr/bin/env python3
"""Build the Polity-only precursor for Williams autocracy condition A.

This script is deliberately target-blind. It does not use the published
107/38/69 A margins to fill or correct any case.
"""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path

ALIASES = {
    "DR Congo": "Congo Kinshasa",
    "Congo-Kinshasa": "Congo Kinshasa",
    "Congo-Brazzaville": "Congo Brazzaville",
    "Pakistan (now Bangladesh)": "Pakistan",
    "The Gambia": "Gambia",
    "Korea, South": "Korea South",
    "Dominican Republic": "Dominican Rep",
    "USSR (Soviet Union)": "USSR",
    "Yemen, North": "Yemen North",
    "Yemen, South": "Yemen South",
}
SPECIAL = {-66, -77, -88}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--polity", type=Path, required=True)
    ap.add_argument("--cases", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--summary", type=Path)
    args = ap.parse_args()

    with args.polity.open(encoding="utf-8-sig", newline="") as f:
        polity = list(csv.DictReader(f))
    with args.cases.open(encoding="utf-8-sig", newline="") as f:
        cases = list(csv.DictReader(f))

    names = {r["country"] for r in polity}
    idx = {(r["country"], r["year"]): r for r in polity}
    out = []
    for case in cases:
        pc = case["country"] if case["country"] in names else ALIASES.get(case["country"], "")
        src = idx.get((pc, case["start_year"])) if pc else None
        row = {
            "case_id": case["case_id"],
            "country": case["country"],
            "outcome_genocide": case["outcome_genocide"],
            "start_year": case["start_year"],
            "polity_country": pc,
            "polity_start_raw": "",
            "polity2_start_raw": "",
            "democ_start_raw": "",
            "autoc_start_raw": "",
            "A_polity_only": "",
            "A_status": "",
            "source_ref": "p4v2012.csv",
        }
        if not pc:
            row["A_status"] = "country_unresolved"
        elif src is None or src.get("polity", "") == "":
            row["A_status"] = "missing_start_year"
        else:
            val = int(float(src["polity"]))
            row["polity_start_raw"] = src.get("polity", "")
            row["polity2_start_raw"] = src.get("polity2", "")
            row["democ_start_raw"] = src.get("democ", "")
            row["autoc_start_raw"] = src.get("autoc", "")
            if val in SPECIAL:
                row["A_status"] = f"special_{val}_requires_FH"
            else:
                row["A_polity_only"] = "1" if -10 <= val <= 0 else "0"
                row["A_status"] = "direct_polity"
        out.append(row)

    fields = list(out[0])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(out)

    summary = {
        "rows": len(out),
        "direct_polity": sum(r["A_status"] == "direct_polity" for r in out),
        "special_requires_FH": sum(r["A_status"].startswith("special_") for r in out),
        "direct_A1_total": sum(r["A_polity_only"] == "1" for r in out),
        "direct_A1_genocide": sum(r["A_polity_only"] == "1" and r["outcome_genocide"] == "1" for r in out),
        "direct_A1_control": sum(r["A_polity_only"] == "1" and r["outcome_genocide"] == "0" for r in out),
    }
    print(json.dumps(summary, indent=2))
    if args.summary:
        args.summary.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
