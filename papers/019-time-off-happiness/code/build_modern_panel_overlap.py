#!/usr/bin/env python3
"""Build ARIS4C019 modern statutory-leave × WHR availability overlap.

Coverage only: this script never reads Life Ladder values.
"""

from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

ALIASES = {
    "egypt": "EGY",
    "kyrgyzstan": "KGZ",
    "russia": "RUS",
    "south korea": "KOR",
    "venezuela": "VEN",
    "turkiye": "TUR",
    "iran": "IRN",
    "taiwan province of china": "TWN",
    "czechia": "CZE",
    "slovakia": "SVK",
    "hong kong s a r of china": "HKG",
    "yemen": "YEM",
    "ivory coast": "CIV",
    "laos": "LAO",
    "congo brazzaville": "COG",
    "congo kinshasa": "ZAR",  # legacy code in this WB historical file
    "syria": "SYR",
    "bangladesh": "BGD",
    "brazil": "BRA",
    "india": "IND",
    "indonesia": "IDN",
    "japan": "JPN",
    "mexico": "MEX",
    "united states": "USA",
    "china": "CHN",
    "pakistan": "PAK",
    "nigeria": "NGA",
    "gambia": "GMB",
}

def norm(s: str) -> str:
    import unicodedata, re
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("&", "and")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s)).strip()

def read_csv(name: str):
    with (DATA / name).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))

def write_csv(name: str, rows: list[dict], fields: list[str]):
    with (DATA / name).open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

def main() -> int:
    cal = read_csv("whr_observation_calendar.csv")
    wb = read_csv("worldbank_statutory_leave_panel.csv")
    national = [r for r in wb if "_" not in r["economy_code"]]

    by_name = {}
    for r in national:
        by_name.setdefault(norm(r["economy"]), r["economy_code"])

    countries = sorted({r["country"] for r in cal})
    cross = []
    for country in countries:
        key = norm(country)
        code = ALIASES.get(key) or by_name.get(key, "")
        labels = sorted({r["economy"] for r in national if r["economy_code"] == code})
        cross.append({
            "whr_country": country,
            "wb_code": code,
            "wb_economy_label": labels[0] if labels else "",
            "match_status": "matched" if code else "unmatched",
            "match_method": (
                "curated_alias_or_base_code" if key in ALIASES and key != "congo kinshasa"
                else "curated_legacy_wb_code" if key == "congo kinshasa"
                else "normalized_name" if code else "unmatched"
            ),
        })

    wb_by_code_year = {(r["economy_code"], r["ew_year"]): r for r in national}
    code_by_country = {r["whr_country"]: r["wb_code"] for r in cross}
    overlap = []
    for r in cal:
        code = code_by_country.get(r["country"], "")
        wr = wb_by_code_year.get((code, r["year"]))
        if not wr:
            continue
        overlap.append({
            "country": r["country"],
            "year": r["year"],
            "wb_code": code,
            "wb_economy_label": wr["economy"],
            "leave_1y": wr["leave_1y"],
            "leave_5y": wr["leave_5y"],
            "leave_10y": wr["leave_10y"],
            "leave_avg": wr["leave_avg"],
        })

    by_country = {}
    for r in overlap:
        by_country.setdefault(r["country"], []).append(int(r["year"]))
    summary = []
    for country, years in by_country.items():
        summary.append({
            "country": country,
            "n_overlap_years": len(years),
            "first_overlap_year": min(years),
            "last_overlap_year": max(years),
        })
    summary.sort(key=lambda r: (-r["n_overlap_years"], r["country"]))

    write_csv("modern_wb_whr_country_crosswalk.csv", cross,
              ["whr_country","wb_code","wb_economy_label","match_status","match_method"])
    write_csv("modern_wb_whr_overlap.csv", overlap,
              ["country","year","wb_code","wb_economy_label","leave_1y","leave_5y","leave_10y","leave_avg"])
    write_csv("modern_wb_whr_overlap_summary.csv", summary,
              ["country","n_overlap_years","first_overlap_year","last_overlap_year"])

    unmatched = [r["whr_country"] for r in cross if r["match_status"] == "unmatched"]
    assert len(cross) == 165
    assert len(cross) - len(unmatched) == 161
    assert len(summary) == 161
    assert len(overlap) == 1934
    assert unmatched == ["Cuba", "Somaliland region", "State of Palestine", "Turkmenistan"]

    print("PASS modern overlap: 161 countries / 1934 country-years")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
