from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PROCESS = ROOT / "process"


def as_bool(s: pd.Series) -> pd.Series:
    return s.astype(str).str.lower().eq("true")


def main() -> None:
    freeze = pd.read_csv(PROCESS / "PILOT0_EVENT_FREEZE.csv")
    calendar = pd.read_csv(DATA / "whr_observation_calendar.csv")
    jumps = pd.read_csv(DATA / "worldbank_leave_jumps.csv")

    calendar["year"] = pd.to_numeric(calendar["year"], errors="coerce").astype("Int64")
    freeze["candidate_treatment_year"] = pd.to_numeric(
        freeze["candidate_treatment_year"], errors="coerce"
    ).astype("Int64")
    freeze["primary_pool"] = as_bool(freeze["primary_pool"])

    treated_by_country: dict[str, list[int]] = {}
    for _, r in freeze.dropna(subset=["whr_country", "candidate_treatment_year"]).iterrows():
        treated_by_country.setdefault(str(r["whr_country"]), []).append(
            int(r["candidate_treatment_year"])
        )

    jump_years: dict[str, list[int]] = {}
    for _, r in jumps.dropna(subset=["whr_country", "ew_year"]).iterrows():
        c = str(r["whr_country"])
        if not c:
            continue
        jump_years.setdefault(c, []).append(int(r["ew_year"]))

    countries = sorted(calendar["country"].dropna().astype(str).unique())
    rows = []

    for _, e in freeze.iterrows():
        ty = int(e["candidate_treatment_year"])
        focal = str(e["whr_country"])
        pre_years = set(range(ty - 4, ty))
        post_years = set(range(ty, ty + 5))
        full_window = set(range(ty - 4, ty + 5))

        raw_donors = []
        clean_donors = []
        excluded_jump = []
        excluded_treatment = []

        for country in countries:
            if country == focal:
                continue
            obs = set(
                calendar.loc[calendar["country"].eq(country), "year"]
                .dropna().astype(int).tolist()
            )
            if len(obs & pre_years) < 2 or len(obs & post_years) < 2:
                continue
            raw_donors.append(country)

            # EW reporting may lag legal effective dates. Screen one extra year
            # on either side so a nearby statutory discontinuity cannot quietly
            # contaminate the donor pool.
            has_jump = any((ty - 5) <= jy <= (ty + 5) for jy in jump_years.get(country, []))
            has_verified_treatment = any(
                other_ty in full_window for other_ty in treated_by_country.get(country, [])
            )

            if has_jump:
                excluded_jump.append(country)
                continue
            if has_verified_treatment:
                excluded_treatment.append(country)
                continue
            clean_donors.append(country)

        rows.append({
            "event_id": e["event_id"],
            "country": e["country"],
            "whr_country": focal,
            "event_tier": e["event_tier"],
            "primary_pool": bool(e["primary_pool"]),
            "first_full_post_year": ty,
            "n_pre_observed": int(e["n_pre"]),
            "n_post_observed": int(e["n_post"]),
            "raw_donor_count": len(raw_donors),
            "clean_donor_count": len(clean_donors),
            "excluded_for_nearby_wb_jump": len(excluded_jump),
            "excluded_for_verified_treatment": len(excluded_treatment),
            "clean_donor_pass_10": len(clean_donors) >= 10,
            "clean_donor_pass_20": len(clean_donors) >= 20,
            "clean_donors": ";".join(clean_donors),
        })

    out = pd.DataFrame(rows).sort_values(
        ["primary_pool", "clean_donor_count", "event_id"],
        ascending=[False, False, True],
    )
    out.to_csv(DATA / "pilot0_donor_diagnostics.csv", index=False)

    primary = out.loc[out["primary_pool"]]
    lines = [
        "# ARIS4C019 · Outcome-blind design diagnostics",
        "",
        "> This file uses only survey-observation availability, treatment timing, and statutory-leave jump metadata. It does not read Life Ladder values.",
        "",
        f"- Frozen events: **{len(out)}**",
        f"- Headline primary events: **{len(primary)}**",
        f"- Primary events with >=10 clean donors: **{int(primary['clean_donor_pass_10'].sum())}/{len(primary)}**",
        f"- Primary events with >=20 clean donors: **{int(primary['clean_donor_pass_20'].sum())}/{len(primary)}**",
        "",
        "## Event support",
        "",
        "| Event | First full post | Tier | Primary | Pre obs | Post obs | Raw donors | Clean donors |",
        "|---|---:|---|---:|---:|---:|---:|---:|",
    ]
    for _, r in out.iterrows():
        lines.append(
            f"| {r['country']} | {int(r['first_full_post_year'])} | {r['event_tier']} | "
            f"{bool(r['primary_pool'])} | {int(r['n_pre_observed'])} | {int(r['n_post_observed'])} | "
            f"{int(r['raw_donor_count'])} | {int(r['clean_donor_count'])} |"
        )
    lines += [
        "",
        "## Gate rule",
        "",
        "A primary event is not automatically discarded for having fewer donors, but <10 clean donors triggers an identification warning and requires event-specific support review before outcome unlock.",
        "",
        "No post-treatment happiness effect has been inspected in producing this diagnostic.",
        "",
    ]
    (PROCESS / "PILOT0_DESIGN_DIAGNOSTICS.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
