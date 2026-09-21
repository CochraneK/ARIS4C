from __future__ import annotations

import io
import math
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PROCESS = ROOT / "process"
FIGURES = ROOT / "figures"
DATA.mkdir(parents=True, exist_ok=True)
PROCESS.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

UNLOCK = PROCESS / "PILOT0_UNLOCK.md"
WHR_URL = "https://happiness-report.s3.amazonaws.com/2023/DataForTable2.1WHR2023.xls"
WHR_MIRROR_URL = "https://raw.githubusercontent.com/dgbrizan/2024-01-cs663-a1/d7d7255fe00108aa15335286599658ab5365c2b3/DataForTable2.1WHR2023.xls"
HEADERS = {"User-Agent": "ARIS4C019-research/0.1 (+https://github.com/CochraneK/ARIS4C)"}


def require_unlock() -> None:
    if not UNLOCK.exists():
        raise RuntimeError("Outcome firewall active: PILOT0_UNLOCK.md is missing.")
    text = UNLOCK.read_text(encoding="utf-8")
    if "Life Ladder only" not in text:
        raise RuntimeError("Outcome unlock does not explicitly permit Life Ladder analysis.")


def download_whr() -> bytes:
    errors = []
    for url in (WHR_URL, WHR_MIRROR_URL):
        try:
            r = requests.get(url, headers=HEADERS, timeout=120)
            r.raise_for_status()
            return r.content
        except Exception as exc:
            errors.append(f"{url}: {exc!r}")
    raise RuntimeError("WHR download failed:\n" + "\n".join(errors))


def read_life_ladder() -> pd.DataFrame:
    content = download_whr()
    df = pd.read_excel(io.BytesIO(content), sheet_name="Sheet1", engine="xlrd")
    required = ["Country name", "year", "Life Ladder"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise RuntimeError(f"WHR Life Ladder fields missing: {missing}")
    out = df[required].copy()
    out.columns = ["country", "year", "life_ladder"]
    out["year"] = pd.to_numeric(out["year"], errors="coerce").astype("Int64")
    out["life_ladder"] = pd.to_numeric(out["life_ladder"], errors="coerce")
    return out.dropna(subset=["country", "year", "life_ladder"]).copy()


def value_lookup(whr: pd.DataFrame) -> dict[tuple[str, int], float]:
    return {
        (str(r.country), int(r.year)): float(r.life_ladder)
        for r in whr.itertuples(index=False)
    }


def parse_bool(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def build_event_time(whr: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    events = pd.read_csv(PROCESS / "PILOT0_EVENT_FREEZE.csv")
    donors = pd.read_csv(DATA / "pilot0_donor_diagnostics.csv")

    events = events.loc[events["primary_pool"].map(parse_bool)].copy()
    donor_by_event = donors.set_index("event_id")["clean_donors"].fillna("").to_dict()
    lookup = value_lookup(whr)

    rows = []
    event_summaries = []

    for _, e in events.iterrows():
        event_id = str(e["event_id"])
        focal = str(e["whr_country"])
        display_country = str(e["country"])
        T = int(e["legal_effective_year"])
        ref_year = int(e["reference_year"])
        transition = None if pd.isna(e["transition_year_excluded"]) else int(e["transition_year_excluded"])
        clean_donors = [x for x in str(donor_by_event.get(event_id, "")).split(";") if x]

        ref_treated = lookup.get((focal, ref_year))
        if ref_treated is None:
            event_summaries.append({
                "event_id": event_id,
                "country": display_country,
                "legal_effective_year": T,
                "estimable": False,
                "reason": f"treated reference year {ref_year} missing",
            })
            continue

        event_rows = []
        for k in range(-4, 5):
            year = T + k
            if transition is not None and year == transition:
                continue
            treated = lookup.get((focal, year))
            if treated is None:
                continue

            donor_changes = []
            for donor in clean_donors:
                y_ref = lookup.get((donor, ref_year))
                y_now = lookup.get((donor, year))
                if y_ref is None or y_now is None:
                    continue
                donor_changes.append(y_now - y_ref)

            if not donor_changes:
                continue

            treated_change = treated - ref_treated
            donor_mean_change = float(sum(donor_changes) / len(donor_changes))
            gap = treated_change - donor_mean_change
            r = {
                "event_id": event_id,
                "country": display_country,
                "whr_country": focal,
                "legal_effective_year": T,
                "reference_year": ref_year,
                "transition_year_excluded": "" if transition is None else transition,
                "event_time": k,
                "calendar_year": year,
                "life_ladder": treated,
                "treated_change_from_ref": treated_change,
                "donor_mean_change_from_ref": donor_mean_change,
                "donor_adjusted_gap": gap,
                "donor_n": len(donor_changes),
                "period": "pre" if k < 0 else "post",
            }
            rows.append(r)
            event_rows.append(r)

        er = pd.DataFrame(event_rows)
        post = er.loc[er["period"].eq("post")] if not er.empty else er
        pre_placebo = er.loc[er["event_time"] <= -2] if not er.empty else er
        event_summaries.append({
            "event_id": event_id,
            "country": display_country,
            "legal_effective_year": T,
            "estimable": not er.empty and not post.empty,
            "reason": "",
            "n_pre_placebo_points": int(len(pre_placebo)),
            "n_post_points": int(len(post)),
            "pre_placebo_mean_gap": float(pre_placebo["donor_adjusted_gap"].mean()) if len(pre_placebo) else math.nan,
            "pre_placebo_rms_gap": float(math.sqrt((pre_placebo["donor_adjusted_gap"] ** 2).mean())) if len(pre_placebo) else math.nan,
            "post_mean_gap": float(post["donor_adjusted_gap"].mean()) if len(post) else math.nan,
            "post_median_gap": float(post["donor_adjusted_gap"].median()) if len(post) else math.nan,
            "min_donor_n": int(er["donor_n"].min()) if len(er) else 0,
        })

    long = pd.DataFrame(rows)
    summary = pd.DataFrame(event_summaries)

    if long.empty:
        raise RuntimeError("No event-time Life Ladder estimates were generated.")

    pooled_rows = []
    for k, g in long.groupby("event_time", sort=True):
        vals = g["donor_adjusted_gap"].dropna()
        pooled_rows.append({
            "event_time": int(k),
            "event_n": int(len(vals)),
            "mean_gap": float(vals.mean()) if len(vals) else math.nan,
            "median_gap": float(vals.median()) if len(vals) else math.nan,
            "min_gap": float(vals.min()) if len(vals) else math.nan,
            "max_gap": float(vals.max()) if len(vals) else math.nan,
        })
    pooled = pd.DataFrame(pooled_rows).sort_values("event_time").reset_index(drop=True)
    return long, summary, pooled


def write_outputs(long: pd.DataFrame, summary: pd.DataFrame, pooled: pd.DataFrame) -> None:
    long.to_csv(DATA / "pilot0_life_ladder_event_time.csv", index=False)
    summary.to_csv(DATA / "pilot0_life_ladder_event_summary.csv", index=False)
    pooled.to_csv(DATA / "pilot0_life_ladder_pooled_event_time.csv", index=False)

    estimable = summary.loc[summary["estimable"].map(parse_bool)].copy()
    post_vals = estimable["post_mean_gap"].dropna()
    pos = int((post_vals > 0).sum())
    neg = int((post_vals < 0).sum())
    zero = int((post_vals == 0).sum())

    lines = [
        "# ARIS4C019 · Pilot-0 First Life Ladder Outcome Look",
        "",
        "> First post-unlock outcome diagnostic. These are equal-weight clean-donor adjusted changes, not the final causal estimator.",
        "",
        f"- Frozen headline events: **{len(summary)}**.",
        f"- Events estimable with frozen T-1 reference and >=1 full-post point: **{len(estimable)}/{len(summary)}**.",
        f"- Event-level mean full-post gap > 0: **{pos}**; < 0: **{neg}**; = 0: **{zero}**.",
        f"- Mean of event-level full-post gaps: **{post_vals.mean():.3f} Life Ladder points**." if len(post_vals) else "- Mean full-post gap unavailable.",
        f"- Median of event-level full-post gaps: **{post_vals.median():.3f} Life Ladder points**." if len(post_vals) else "- Median full-post gap unavailable.",
        "",
        "## Event-level diagnostic",
        "",
        "| Event | Legal year | Estimable | Pre placebo mean | Pre placebo RMS | Full-post mean gap | Post points | Min donors |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for _, r in summary.iterrows():
        def fmt(x):
            return "" if pd.isna(x) else f"{float(x):.3f}"
        lines.append(
            f"| {r['country']} | {int(r['legal_effective_year'])} | {bool(r['estimable'])} | "
            f"{fmt(r.get('pre_placebo_mean_gap'))} | {fmt(r.get('pre_placebo_rms_gap'))} | "
            f"{fmt(r.get('post_mean_gap'))} | {int(r.get('n_post_points', 0) or 0)} | "
            f"{int(r.get('min_donor_n', 0) or 0)} |"
        )

    lines += [
        "",
        "## Interpretation boundary",
        "",
        "- A positive gap means the treated country's Life Ladder rose more (or fell less) than the equal-weight clean-donor mean relative to T-1.",
        "- A negative gap means it rose less (or fell more) than the donor mean.",
        "- Pre-period gaps are design diagnostics, not treatment effects.",
        "- This first look does not establish parallel trends or causal identification.",
        "- Do not promote, drop, or reweight events because of these observed outcome signs.",
        "- Positive/negative affect remain locked.",
        "",
        "## Next",
        "",
        "Implement the frozen modern staggered-adoption / heterogeneous event-study estimators and prespecified leave-one-event-out plus crisis/scope sensitivities before manuscript-level interpretation.",
        "",
    ]
    (PROCESS / "PILOT0_FIRST_OUTCOME_LOOK.md").write_text("\n".join(lines), encoding="utf-8")

    try:
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(7.2, 4.6))
        for country, g in long.groupby("country"):
            g = g.sort_values("event_time")
            ax.plot(g["event_time"], g["donor_adjusted_gap"], alpha=0.25, linewidth=1)

        pg = pooled.sort_values("event_time")
        ax.plot(pg["event_time"], pg["mean_gap"], marker="o", linewidth=2.5, label="Pooled mean")
        ax.axhline(0, linewidth=1)
        ax.axvline(0, linewidth=1, linestyle="--")
        ax.set_xlabel("Event time relative to legal effective year")
        ax.set_ylabel("Donor-adjusted Life Ladder change")
        ax.set_title("ARIS4C019 Pilot-0: first outcome diagnostic")
        ax.legend(frameon=False)
        fig.tight_layout()
        fig.savefig(FIGURES / "pilot0_life_ladder_event_time.png", dpi=180)
        plt.close(fig)
    except Exception as exc:
        (PROCESS / "PILOT0_FIGURE_ERROR.txt").write_text(repr(exc), encoding="utf-8")


def main() -> None:
    require_unlock()
    whr = read_life_ladder()
    long, summary, pooled = build_event_time(whr)
    write_outputs(long, summary, pooled)


if __name__ == "__main__":
    main()
