from __future__ import annotations

import hashlib
import io
import json
import math
import unicodedata
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PROCESS = ROOT / "process"

VALIDATION = DATA / "whr2024_source_validation.json"
FROZEN_SUMMARY = DATA / "pilot0_life_ladder_event_summary.csv"

WHR2023_PINNED = (
    "https://raw.githubusercontent.com/dgbrizan/2024-01-cs663-a1/"
    "d7d7255fe00108aa15335286599658ab5365c2b3/DataForTable2.1WHR2023.xls"
)
WHR2024_COMMIT = "ba44f791215334b43e99b16bf6b83ac38de213bb"
WHR2024_PINNED = (
    "https://raw.githubusercontent.com/ahmedlubis/world-happiness-panel-analysis/"
    f"{WHR2024_COMMIT}/World-happiness-report-updated_2024.csv"
)
HEADERS = {"User-Agent": "ARIS4C019-source-refresh/0.1 (+https://github.com/CochraneK/ARIS4C)"}


def parse_bool(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def norm_country(value: object) -> str:
    s = unicodedata.normalize("NFKD", str(value).strip())
    s = s.encode("ascii", "ignore").decode("ascii")
    return " ".join(s.split()).casefold()


def fetch(url: str) -> bytes:
    r = requests.get(url, headers=HEADERS, timeout=120)
    r.raise_for_status()
    return r.content


def require_validated_source() -> dict:
    if not VALIDATION.exists():
        raise RuntimeError("WHR2024 source refresh locked: validation JSON is missing.")
    v = json.loads(VALIDATION.read_text(encoding="utf-8"))
    if v.get("status") != "PASS":
        raise RuntimeError("WHR2024 source refresh locked: validator did not PASS.")
    if v.get("transport", {}).get("whr2024_commit") != WHR2024_COMMIT:
        raise RuntimeError("WHR2024 validator commit differs from refresh-script pin.")
    return v


def read_2023() -> pd.DataFrame:
    raw = fetch(WHR2023_PINNED)
    df = pd.read_excel(io.BytesIO(raw), sheet_name="Sheet1", engine="xlrd")
    out = df[["Country name", "year", "Life Ladder"]].copy()
    out.columns = ["country", "year", "life_ladder"]
    out["year"] = pd.to_numeric(out["year"], errors="coerce").astype("Int64")
    out["life_ladder"] = pd.to_numeric(out["life_ladder"], errors="coerce")
    return out.dropna(subset=["country", "year", "life_ladder"]).copy()


def read_2024(validation: dict) -> pd.DataFrame:
    raw = fetch(WHR2024_PINNED)
    got_sha = hashlib.sha256(raw).hexdigest()
    expected_sha = validation["transport"]["whr2024_sha256"]
    if got_sha != expected_sha:
        raise RuntimeError(f"WHR2024 bytes changed: {got_sha} != {expected_sha}")
    df = pd.read_csv(io.BytesIO(raw))
    out = df[["Country name", "year", "Life Ladder"]].copy()
    out.columns = ["country", "year", "life_ladder"]
    out["year"] = pd.to_numeric(out["year"], errors="coerce").astype("Int64")
    out["life_ladder"] = pd.to_numeric(out["life_ladder"], errors="coerce")
    return out.dropna(subset=["country", "year", "life_ladder"]).copy()


def value_lookup(whr: pd.DataFrame) -> dict[tuple[str, int], float]:
    return {
        (norm_country(r.country), int(r.year)): float(r.life_ladder)
        for r in whr.itertuples(index=False)
    }


def estimate_panel(whr: pd.DataFrame, panel_name: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    events = pd.read_csv(PROCESS / "PILOT0_EVENT_FREEZE.csv")
    events = events.loc[events["primary_pool"].map(parse_bool)].copy()
    donors = pd.read_csv(DATA / "pilot0_donor_diagnostics.csv")
    donor_by_event = donors.set_index("event_id")["clean_donors"].fillna("").to_dict()
    lookup = value_lookup(whr)

    long_rows = []
    summary_rows = []

    for _, e in events.iterrows():
        event_id = str(e["event_id"])
        focal = str(e["whr_country"])
        display = str(e["country"])
        T = int(e["legal_effective_year"])
        ref = int(e["reference_year"])
        transition = None if pd.isna(e["transition_year_excluded"]) else int(e["transition_year_excluded"])
        clean = [x for x in str(donor_by_event.get(event_id, "")).split(";") if x]

        y_ref = lookup.get((norm_country(focal), ref))
        if y_ref is None:
            summary_rows.append({
                "panel": panel_name, "event_id": event_id, "country": display,
                "estimable": False, "reason": f"missing treated reference {ref}",
            })
            continue

        erows = []
        for k in range(-4, 5):
            year = T + k
            if transition is not None and year == transition:
                continue
            y = lookup.get((norm_country(focal), year))
            if y is None:
                continue

            donor_changes = []
            for donor in clean:
                dr = lookup.get((norm_country(donor), ref))
                dy = lookup.get((norm_country(donor), year))
                if dr is not None and dy is not None:
                    donor_changes.append(dy - dr)
            if not donor_changes:
                continue

            gap = (y - y_ref) - float(sum(donor_changes) / len(donor_changes))
            row = {
                "panel": panel_name,
                "event_id": event_id,
                "country": display,
                "legal_effective_year": T,
                "event_time": k,
                "calendar_year": year,
                "donor_adjusted_gap": gap,
                "donor_n": len(donor_changes),
                "period": "pre" if k < 0 else "post",
            }
            long_rows.append(row)
            erows.append(row)

        er = pd.DataFrame(erows)
        post = er.loc[er["period"].eq("post")] if not er.empty else er
        pre = er.loc[er["event_time"].le(-2)] if not er.empty else er
        summary_rows.append({
            "panel": panel_name,
            "event_id": event_id,
            "country": display,
            "legal_effective_year": T,
            "estimable": bool(len(post)),
            "reason": "",
            "n_pre_placebo_points": int(len(pre)),
            "n_post_points": int(len(post)),
            "pre_placebo_rms_gap": (
                float(math.sqrt((pre["donor_adjusted_gap"] ** 2).mean()))
                if len(pre) else math.nan
            ),
            "post_mean_gap": float(post["donor_adjusted_gap"].mean()) if len(post) else math.nan,
            "post_median_gap": float(post["donor_adjusted_gap"].median()) if len(post) else math.nan,
            "min_donor_n": int(er["donor_n"].min()) if len(er) else 0,
        })

    return pd.DataFrame(long_rows), pd.DataFrame(summary_rows)


def pooled_row(summary: pd.DataFrame, panel: str) -> dict:
    s = summary.loc[summary["estimable"].map(parse_bool)].copy()
    vals = pd.to_numeric(s["post_mean_gap"], errors="coerce").dropna()
    return {
        "panel": panel,
        "n_events": int(len(vals)),
        "mean_post_gap": float(vals.mean()),
        "median_post_gap": float(vals.median()),
        "positive_events": int((vals > 0).sum()),
        "negative_events": int((vals < 0).sum()),
    }


def main() -> None:
    validation = require_validated_source()

    old = read_2023()
    new = read_2024(validation)

    long_a, sum_a = estimate_panel(old, "A_WHR2023_frozen")
    long_b, sum_b = estimate_panel(new.loc[new["year"].le(2022)].copy(), "B_WHR2024_common_horizon")
    long_c, sum_c = estimate_panel(new.loc[new["year"].le(2023)].copy(), "C_WHR2024_extended_2023")

    # Guard that A exactly reproduces the already-published frozen benchmark.
    frozen = pd.read_csv(FROZEN_SUMMARY)[["event_id", "post_mean_gap"]].copy()
    chk = sum_a[["event_id", "post_mean_gap"]].merge(
        frozen, on="event_id", suffixes=("_recomputed", "_frozen"), how="inner"
    )
    chk["abs_diff"] = (
        chk["post_mean_gap_recomputed"] - chk["post_mean_gap_frozen"]
    ).abs()
    max_repro_diff = float(chk["abs_diff"].max()) if len(chk) else math.inf
    if len(chk) != 8 or max_repro_diff > 1e-10:
        raise RuntimeError(
            f"Frozen A benchmark failed exact reproduction: n={len(chk)}, maxdiff={max_repro_diff}"
        )

    all_long = pd.concat([long_a, long_b, long_c], ignore_index=True)
    all_summary = pd.concat([sum_a, sum_b, sum_c], ignore_index=True)

    wide = (
        all_summary.pivot(index=["event_id", "country"], columns="panel",
                          values=["post_mean_gap", "n_post_points", "pre_placebo_rms_gap"])
        .reset_index()
    )
    wide.columns = [
        "_".join([str(x) for x in col if str(x)])
        if isinstance(col, tuple) else str(col)
        for col in wide.columns
    ]

    a = "post_mean_gap_A_WHR2023_frozen"
    b = "post_mean_gap_B_WHR2024_common_horizon"
    c = "post_mean_gap_C_WHR2024_extended_2023"
    wide["B_minus_A_release_revision"] = wide[b] - wide[a]
    wide["C_minus_B_added_2023"] = wide[c] - wide[b]

    pooled = pd.DataFrame([
        pooled_row(sum_a, "A_WHR2023_frozen"),
        pooled_row(sum_b, "B_WHR2024_common_horizon"),
        pooled_row(sum_c, "C_WHR2024_extended_2023"),
    ])
    pa = pooled.set_index("panel").loc["A_WHR2023_frozen"]
    pb = pooled.set_index("panel").loc["B_WHR2024_common_horizon"]
    pc = pooled.set_index("panel").loc["C_WHR2024_extended_2023"]
    pooled["vs_A_mean_delta"] = pooled["mean_post_gap"] - float(pa["mean_post_gap"])

    all_long.to_csv(DATA / "whr2024_refresh_event_time.csv", index=False)
    wide.to_csv(DATA / "whr2024_refresh_event_summary.csv", index=False)
    pooled.to_csv(DATA / "whr2024_refresh_pooled.csv", index=False)

    lines = [
        "# ARIS4C019 · WHR 2024 Source-Refresh Results",
        "",
        "> Post-unlock source-refresh robustness under the pre-written WHR2024 source-refresh freeze. This is not an independent replication and does not open the new holdout candidates.",
        "",
        f"- Frozen benchmark reproduction max |difference|: **{max_repro_diff:.12f}**.",
        f"- A · WHR2023 frozen mean / median: **{float(pa['mean_post_gap']):.3f} / {float(pa['median_post_gap']):.3f}**.",
        f"- B · WHR2024 release restricted to <=2022 mean / median: **{float(pb['mean_post_gap']):.3f} / {float(pb['median_post_gap']):.3f}**.",
        f"- C · WHR2024 release extended through 2023 mean / median: **{float(pc['mean_post_gap']):.3f} / {float(pc['median_post_gap']):.3f}**.",
        f"- Pooled B-A release-revision shift: **{float(pb['mean_post_gap'] - pa['mean_post_gap']):+.3f}**.",
        f"- Pooled C-B added-2023 shift: **{float(pc['mean_post_gap'] - pb['mean_post_gap']):+.3f}**.",
        "",
        "## Event-level decomposition",
        "",
        "| Event | A frozen | B common horizon | C +2023 | B-A revision | C-B 2023 | Post n A/B/C |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for _, r in wide.sort_values("country").iterrows():
        na = int(r.get("n_post_points_A_WHR2023_frozen", 0))
        nb = int(r.get("n_post_points_B_WHR2024_common_horizon", 0))
        nc = int(r.get("n_post_points_C_WHR2024_extended_2023", 0))
        lines.append(
            f"| {r['country']} | {r[a]:.3f} | {r[b]:.3f} | {r[c]:.3f} | "
            f"{r['B_minus_A_release_revision']:+.3f} | {r['C_minus_B_added_2023']:+.3f} | "
            f"{na}/{nb}/{nc} |"
        )

    sign_a = dict(zip(wide["event_id"], wide[a].apply(lambda x: 0 if pd.isna(x) else (1 if x > 0 else -1 if x < 0 else 0))))
    sign_b = dict(zip(wide["event_id"], wide[b].apply(lambda x: 0 if pd.isna(x) else (1 if x > 0 else -1 if x < 0 else 0))))
    sign_c = dict(zip(wide["event_id"], wide[c].apply(lambda x: 0 if pd.isna(x) else (1 if x > 0 else -1 if x < 0 else 0))))
    flips_ab = [eid for eid in sign_a if sign_a[eid] != sign_b.get(eid)]
    flips_bc = [eid for eid in sign_b if sign_b[eid] != sign_c.get(eid)]

    lines += [
        "",
        "## Stability flags",
        "",
        f"- Event sign changes A→B: **{len(flips_ab)}** ({'; '.join(flips_ab) if flips_ab else 'none'}).",
        f"- Event sign changes B→C: **{len(flips_bc)}** ({'; '.join(flips_bc) if flips_bc else 'none'}).",
        "",
        "## Interpretation boundary",
        "",
        "- A→B differences are source-release/history-revision effects, not new follow-up.",
        "- B→C differences isolate the addition of 2023 within the already frozen legal T-4…T+4 window.",
        "- The existing treatment-isolation and pretrend problems remain binding even if A/B/C are numerically stable.",
        "- Mexico/New Zealand/Malta and other stand-alone candidates remain behind the holdout firewall.",
        "- Positive and negative affect remain locked.",
        "",
    ]
    (PROCESS / "WHR2024_SOURCE_REFRESH_RESULTS.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
