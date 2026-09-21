from __future__ import annotations

import hashlib
import io
import json
import unicodedata
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PROCESS = ROOT / "process"
DATA.mkdir(parents=True, exist_ok=True)
PROCESS.mkdir(parents=True, exist_ok=True)

# Frozen WHR 2023 transport used by Pilot-0.
WHR2023_PINNED = (
    "https://raw.githubusercontent.com/dgbrizan/2024-01-cs663-a1/"
    "d7d7255fe00108aa15335286599658ab5365c2b3/DataForTable2.1WHR2023.xls"
)
WHR2023_EXPECTED_SHA256 = "1ef5eb637815b74f161359fea7516278f53d81847d2d2973890ac036103d8cbd"

# Post-unlock WHR 2024 annual-panel transport candidate.
WHR2024_REPO = "ahmedlubis/world-happiness-panel-analysis"
WHR2024_COMMIT = "ba44f791215334b43e99b16bf6b83ac38de213bb"
WHR2024_GIT_BLOB_SHA = "8440054da65290bbe318be8c3bd28892ba7e128c"
WHR2024_PINNED = (
    "https://raw.githubusercontent.com/ahmedlubis/world-happiness-panel-analysis/"
    f"{WHR2024_COMMIT}/World-happiness-report-updated_2024.csv"
)

REQUIRED = [
    "Country name",
    "year",
    "Life Ladder",
    "Log GDP per capita",
    "Social support",
    "Healthy life expectancy at birth",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of corruption",
    "Positive affect",
    "Negative affect",
]

# Official comparison anchors: WHR24 Statistical Appendix Table 6
# (N=2363; mean=5.48; SD=1.13; min=1.28; max=8.02) and
# WHR24 Chapter 2 note reporting Israel 2023 annual ladder ~= 6.78.
OFFICIAL_2024 = {
    "life_ladder_n": 2363,
    "life_ladder_mean_2dp": 5.48,
    "life_ladder_sd_2dp": 1.13,
    "life_ladder_min_2dp": 1.28,
    "life_ladder_max_2dp": 8.02,
    "year_min": 2005,
    "year_max": 2023,
    "israel_2023_approx": 6.78,
}

HEADERS = {"User-Agent": "ARIS4C019-source-validator/0.1 (+https://github.com/CochraneK/ARIS4C)"}


def fetch(url: str) -> bytes:
    r = requests.get(url, headers=HEADERS, timeout=120)
    r.raise_for_status()
    return r.content


def sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def norm_country(value: object) -> str:
    s = str(value).strip()
    # Match Türkiye/Turkiye and harmless typography differences without
    # inventing political/geographic equivalences.
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    return " ".join(s.split()).casefold()


def load_2023(content: bytes) -> pd.DataFrame:
    df = pd.read_excel(io.BytesIO(content), sheet_name="Sheet1", engine="xlrd")
    out = df[["Country name", "year", "Life Ladder"]].copy()
    out.columns = ["country", "year", "life_ladder_2023_release"]
    out["year"] = pd.to_numeric(out["year"], errors="coerce").astype("Int64")
    out["life_ladder_2023_release"] = pd.to_numeric(
        out["life_ladder_2023_release"], errors="coerce"
    )
    return out.dropna(subset=["country", "year", "life_ladder_2023_release"]).copy()


def load_2024(content: bytes) -> pd.DataFrame:
    df = pd.read_csv(io.BytesIO(content))
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise RuntimeError(f"WHR2024 mirror missing required columns: {missing}")
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    df["Life Ladder"] = pd.to_numeric(df["Life Ladder"], errors="coerce")
    return df


def validate() -> tuple[dict, pd.DataFrame]:
    old_bytes = fetch(WHR2023_PINNED)
    new_bytes = fetch(WHR2024_PINNED)

    old_sha = sha256(old_bytes)
    new_sha = sha256(new_bytes)
    if old_sha != WHR2023_EXPECTED_SHA256:
        raise RuntimeError(
            f"Frozen WHR2023 transport hash changed: {old_sha} != {WHR2023_EXPECTED_SHA256}"
        )

    old = load_2023(old_bytes)
    new = load_2024(new_bytes)

    ladder = new["Life Ladder"].dropna()
    stats = {
        "rows": int(len(new)),
        "life_ladder_n": int(ladder.shape[0]),
        "year_min": int(new["year"].min()),
        "year_max": int(new["year"].max()),
        "life_ladder_mean": float(ladder.mean()),
        "life_ladder_sd": float(ladder.std(ddof=1)),
        "life_ladder_min": float(ladder.min()),
        "life_ladder_max": float(ladder.max()),
    }

    official_checks = {
        "n_2363": stats["life_ladder_n"] == OFFICIAL_2024["life_ladder_n"],
        "year_2005_2023": (
            stats["year_min"] == OFFICIAL_2024["year_min"]
            and stats["year_max"] == OFFICIAL_2024["year_max"]
        ),
        "mean_matches_official_2dp": round(stats["life_ladder_mean"], 2)
        == OFFICIAL_2024["life_ladder_mean_2dp"],
        "sd_matches_official_2dp": round(stats["life_ladder_sd"], 2)
        == OFFICIAL_2024["life_ladder_sd_2dp"],
        "min_matches_official_2dp": round(stats["life_ladder_min"], 2)
        == OFFICIAL_2024["life_ladder_min_2dp"],
        "max_matches_official_2dp": round(stats["life_ladder_max"], 2)
        == OFFICIAL_2024["life_ladder_max_2dp"],
    }

    israel = new.loc[
        new["Country name"].astype(str).str.strip().eq("Israel") & new["year"].eq(2023),
        "Life Ladder",
    ].dropna()
    israel_value = None if israel.empty else float(israel.iloc[0])
    official_checks["israel_2023_matches_report"] = bool(
        israel_value is not None
        and abs(israel_value - OFFICIAL_2024["israel_2023_approx"]) <= 0.005
    )

    old["country_key"] = old["country"].map(norm_country)
    new_overlap = new.loc[new["year"].le(2022), ["Country name", "year", "Life Ladder"]].copy()
    new_overlap["country_key"] = new_overlap["Country name"].map(norm_country)

    merged = old.merge(
        new_overlap,
        on=["country_key", "year"],
        how="outer",
        indicator=True,
    )
    both = merged.loc[merged["_merge"].eq("both")].copy()
    both["abs_diff"] = (
        both["life_ladder_2023_release"] - both["Life Ladder"]
    ).abs()
    both["old_round3"] = both["life_ladder_2023_release"].round(3)
    both["new_round3"] = both["Life Ladder"].round(3)
    both["same_at_3dp"] = both["old_round3"].eq(both["new_round3"])

    overlap = {
        "frozen_2023_rows": int(len(old)),
        "matched_country_years": int(len(both)),
        "old_keys_missing_from_2024_mirror": int((merged["_merge"] == "left_only").sum()),
        "new_pre2023_keys_not_in_frozen_2023": int((merged["_merge"] == "right_only").sum()),
        "same_at_3dp": int(both["same_at_3dp"].sum()),
        "different_at_3dp": int((~both["same_at_3dp"]).sum()),
        "mean_abs_diff": float(both["abs_diff"].mean()) if len(both) else None,
        "max_abs_diff": float(both["abs_diff"].max()) if len(both) else None,
        "n_abs_diff_gt_0_001": int((both["abs_diff"] > 0.001).sum()),
        "n_abs_diff_gt_0_01": int((both["abs_diff"] > 0.01).sum()),
        "n_abs_diff_gt_0_05": int((both["abs_diff"] > 0.05).sum()),
    }

    # Save only aggregate overlap diagnostics. Candidate-specific new outcomes
    # are deliberately not surfaced by this source-validation gate.
    result = {
        "status": "PASS" if all(official_checks.values()) else "FAIL",
        "transport": {
            "whr2023_url": WHR2023_PINNED,
            "whr2023_sha256": old_sha,
            "whr2024_repository": WHR2024_REPO,
            "whr2024_commit": WHR2024_COMMIT,
            "whr2024_git_blob_sha": WHR2024_GIT_BLOB_SHA,
            "whr2024_url": WHR2024_PINNED,
            "whr2024_sha256": new_sha,
        },
        "official_2024_checks": official_checks,
        "official_2024_stats": stats,
        "israel_2023": israel_value,
        "overlap_with_frozen_whr2023": overlap,
    }

    if result["status"] != "PASS":
        raise RuntimeError("WHR2024 candidate mirror failed official-statistics validation")

    return result, both


def write_outputs(result: dict) -> None:
    (DATA / "whr2024_source_validation.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    s = result["official_2024_stats"]
    o = result["overlap_with_frozen_whr2023"]
    checks = result["official_2024_checks"]
    t = result["transport"]

    lines = [
        "# ARIS4C019 · WHR 2024 Annual-Mirror Validation",
        "",
        "> Post-unlock source validation only. This gate does not estimate any treatment effect and does not surface candidate-event Life Ladder values.",
        "",
        f"- Gate: **{result['status']}**.",
        f"- Pinned mirror commit: `{t['whr2024_commit']}`.",
        f"- Git blob SHA: `{t['whr2024_git_blob_sha']}`.",
        f"- Download SHA256: `{t['whr2024_sha256']}`.",
        f"- Rows with Life Ladder: **{s['life_ladder_n']}**.",
        f"- Year range: **{s['year_min']}–{s['year_max']}**.",
        f"- Life Ladder mean / SD: **{s['life_ladder_mean']:.6f} / {s['life_ladder_sd']:.6f}**.",
        f"- Life Ladder min / max: **{s['life_ladder_min']:.3f} / {s['life_ladder_max']:.3f}**.",
        f"- Israel 2023 cross-check: **{result['israel_2023']:.3f}** (WHR text reports 6.78).",
        "",
        "## Official-statistics checks",
        "",
    ]
    for key, value in checks.items():
        lines.append(f"- {key}: **{'PASS' if value else 'FAIL'}**")

    lines += [
        "",
        "## Overlap with frozen WHR 2023 annual panel",
        "",
        f"- Frozen WHR2023 rows: **{o['frozen_2023_rows']}**.",
        f"- Matched country-years: **{o['matched_country_years']}**.",
        f"- Old keys missing from 2024 mirror: **{o['old_keys_missing_from_2024_mirror']}**.",
        f"- New pre-2023 keys absent from frozen WHR2023: **{o['new_pre2023_keys_not_in_frozen_2023']}**.",
        f"- Same after rounding both Life Ladder values to 3 decimals: **{o['same_at_3dp']}**.",
        f"- Different at 3 decimals: **{o['different_at_3dp']}**.",
        f"- Mean absolute difference: **{o['mean_abs_diff']:.6f}**.",
        f"- Maximum absolute difference: **{o['max_abs_diff']:.6f}**.",
        f"- |difference| > .001 / .01 / .05: **{o['n_abs_diff_gt_0_001']} / {o['n_abs_diff_gt_0_01']} / {o['n_abs_diff_gt_0_05']}**.",
        "",
        "## Interpretation",
        "",
        "- Passing the official summary-statistics checks supports treating this pinned file as a validated transport mirror of the WHR 2024 annual analysis panel.",
        "- It remains a post-unlock source refresh, not a replacement for the frozen WHR2023 analysis.",
        "- Historical-overlap differences must be reported before any refreshed treatment estimate is compared with the frozen result.",
        "- No 2024-mirror candidate-event treatment effect is opened by this gate.",
        "",
    ]
    (PROCESS / "WHR2024_MIRROR_VALIDATION.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def main() -> None:
    result, _ = validate()
    write_outputs(result)


if __name__ == "__main__":
    main()
