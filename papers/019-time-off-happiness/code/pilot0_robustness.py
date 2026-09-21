from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PROCESS = ROOT / "process"


def parse_bool(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def summarize_subset(name: str, frame: pd.DataFrame) -> dict:
    vals = pd.to_numeric(frame["post_mean_gap"], errors="coerce").dropna()
    return {
        "subset": name,
        "n_events": int(len(vals)),
        "mean_post_gap": float(vals.mean()) if len(vals) else float("nan"),
        "median_post_gap": float(vals.median()) if len(vals) else float("nan"),
        "positive_events": int((vals > 0).sum()),
        "negative_events": int((vals < 0).sum()),
    }


def main() -> None:
    summary = pd.read_csv(DATA / "pilot0_life_ladder_event_summary.csv")
    freeze = pd.read_csv(PROCESS / "PILOT0_EVENT_FREEZE.csv")
    macro = pd.read_csv(DATA / "pilot0_macro_pretrend_summary.csv")

    summary = summary.loc[summary["estimable"].map(parse_bool)].copy()
    meta = freeze[["event_id", "macro_window_flags", "scope_flags"]].copy()
    meta["macro_window_flags"] = meta["macro_window_flags"].fillna("")
    meta["scope_flags"] = meta["scope_flags"].fillna("")
    df = summary.merge(meta, on="event_id", how="left")

    macro_small = macro[["event_id", "all_three_covariates_pass2"]].copy()
    macro_small["all_three_covariates_pass2"] = macro_small["all_three_covariates_pass2"].map(parse_bool)
    df = df.merge(macro_small, on="event_id", how="left")

    loo_rows = []
    for event_id, g in df.groupby("event_id"):
        remaining = df.loc[~df["event_id"].eq(event_id)].copy()
        s = summarize_subset(f"leave_out:{event_id}", remaining)
        s.update({
            "left_out_event_id": event_id,
            "left_out_country": str(g.iloc[0]["country"]),
        })
        loo_rows.append(s)
    loo = pd.DataFrame(loo_rows).sort_values("mean_post_gap").reset_index(drop=True)

    masks = {
        "full_primary_8": pd.Series(True, index=df.index),
        "exclude_gfc_overlap": ~df["macro_window_flags"].str.contains("global_financial_crisis_window", regex=False),
        "exclude_covid_overlap": ~df["macro_window_flags"].str.contains("covid_overlap_post_window", regex=False),
        "exclude_jurisdiction_limited": ~df["scope_flags"].str.contains("federal_jurisdiction_only", regex=False),
        "exclude_gfc_and_covid": (
            ~df["macro_window_flags"].str.contains("global_financial_crisis_window", regex=False)
            & ~df["macro_window_flags"].str.contains("covid_overlap_post_window", regex=False)
        ),
        "covariate_complete_only": df["all_three_covariates_pass2"].fillna(False),
    }
    subset = pd.DataFrame([summarize_subset(name, df.loc[mask]) for name, mask in masks.items()])

    loo.to_csv(DATA / "pilot0_leave_one_event_out.csv", index=False)
    subset.to_csv(DATA / "pilot0_prespecified_sensitivities.csv", index=False)

    full_mean = float(df["post_mean_gap"].mean())
    worst = loo.iloc[(loo["mean_post_gap"] - full_mean).abs().argmax()]
    bahrain = df.loc[df["country"].eq("Bahrain")]
    bahrain_pre = float(bahrain.iloc[0]["pre_placebo_rms_gap"]) if len(bahrain) else float("nan")
    bahrain_post = float(bahrain.iloc[0]["post_mean_gap"]) if len(bahrain) else float("nan")

    lines = [
        "# ARIS4C019 · Pilot-0 Robustness Diagnostics",
        "",
        "> Prespecified post-unlock robustness checks on the first equal-weight donor-adjusted Life Ladder diagnostic. These are still not the final causal estimator.",
        "",
        f"- Full 8-event mean full-post gap: **{full_mean:.3f}**.",
        f"- Full 8-event median full-post gap: **{df['post_mean_gap'].median():.3f}**.",
        f"- Most influential leave-one-out case: **{worst['left_out_country']}**; remaining-event mean = **{float(worst['mean_post_gap']):.3f}**.",
        f"- Bahrain pre-placebo RMS gap: **{bahrain_pre:.3f}**; Bahrain full-post mean gap: **{bahrain_post:.3f}**.",
        "",
        "## Prespecified sensitivity subsets",
        "",
        "| Subset | n | Mean post gap | Median post gap | Positive | Negative |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for _, r in subset.iterrows():
        lines.append(
            f"| {r['subset']} | {int(r['n_events'])} | {float(r['mean_post_gap']):.3f} | "
            f"{float(r['median_post_gap']):.3f} | {int(r['positive_events'])} | {int(r['negative_events'])} |"
        )

    lines += [
        "",
        "## Leave-one-event-out",
        "",
        "| Left out | Remaining n | Remaining mean | Remaining median |",
        "|---|---:|---:|---:|",
    ]
    for _, r in loo.iterrows():
        lines.append(
            f"| {r['left_out_country']} | {int(r['n_events'])} | "
            f"{float(r['mean_post_gap']):.3f} | {float(r['median_post_gap']):.3f} |"
        )

    lines += [
        "",
        "## Interpretation boundary",
        "",
        "- A sign change under leave-one-event-out is evidence of event-level fragility, not evidence that the omitted event should be deleted.",
        "- Large pre-placebo gaps weaken a causal interpretation of that event-specific post gap.",
        "- Crisis/scope/covariate subsets were defined before these robustness summaries; they are not selected for significance.",
        "- Positive/negative affect remain locked.",
        "",
    ]
    (PROCESS / "PILOT0_ROBUSTNESS_DIAGNOSTICS.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
