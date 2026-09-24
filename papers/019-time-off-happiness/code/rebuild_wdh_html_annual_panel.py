from __future__ import annotations

"""Rebuild WDH long-run annual happiness panels from official HTML.

Rationale
---------
The public TrendsInNations XLSX is not always transferable in constrained
runtimes, but the World Database of Happiness publishes the underlying
distributional findings in server-rendered HTML. This script reconstructs:
  1. individual finding rows;
  2. nation x equivalent-measure-type x year means on the WDH 0-10 scale;
  3. Table-2 measure families used by ARIS4C019.

Important
---------
- Preserve individual rows before averaging.
- Average transformed 0-10 means within nation / measure type / year.
- Do not collapse distinct measure types before the family rule explicitly says
  to do so. Only 122F + 122G are combined into the historical 'ls10+11' family.
- A specific Trends-in-Nations variable may use a subset of question variants;
  finding_measure_code is therefore retained for later variable-level filtering.
"""

import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
HEADERS = {
    "User-Agent": "ARIS4C019-research/0.11 (+https://github.com/CochraneK/ARIS4C)"
}

@dataclass(frozen=True)
class MeasurePage:
    measure_type: str
    table2_family: str
    url: str

PAGES = [
    MeasurePage("111B", "hl3", "https://worlddatabaseofhappiness.eur.nl/equivalent-measures/3-step-verbal-happiness-1/"),
    MeasurePage("111C", "hl4", "https://worlddatabaseofhappiness.eur.nl/equivalent-measures/4-step-verbal-happiness-2/"),
    MeasurePage("111D", "hl5", "https://worlddatabaseofhappiness.eur.nl/equivalent-measures/5-step-verbal-happiness-3/"),
    MeasurePage("121C", "ls4", "https://worlddatabaseofhappiness.eur.nl/equivalent-measures/4-step-verbal-lifesatisfaction-5/"),
    MeasurePage("121D", "ls5", "https://worlddatabaseofhappiness.eur.nl/equivalent-measures/5-step-verbal-lifesatisfaction-6/"),
    MeasurePage("122F", "ls10+11", "https://worlddatabaseofhappiness.eur.nl/equivalent-measures/10-step-numeral-lifesatisfaction-7/"),
    MeasurePage("122G", "ls10+11", "https://worlddatabaseofhappiness.eur.nl/equivalent-measures/11-step-numeral-lifesatisfaction-8/"),
    MeasurePage("32D", "bw11", "https://worlddatabaseofhappiness.eur.nl/equivalent-measures/11-step-numeral-best-worst-possible-life-9/"),
]

YEAR_RE = re.compile(r"^(?:18|19|20)\d{2}$")


def get_html(url: str) -> str:
    r = requests.get(url, headers=HEADERS, timeout=120)
    r.raise_for_status()
    return r.text


def number(text: str) -> float:
    text = text.strip().replace(",", ".")
    if text in {"", "*", "-", "—"}:
        return np.nan
    m = re.search(r"[-+]?\d+(?:\.\d+)?", text)
    return float(m.group()) if m else np.nan


def country_from_heading(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_table_rows(table, country: str, page: MeasurePage) -> list[dict]:
    out = []
    for tr in table.find_all("tr"):
        cells = [re.sub(r"\s+", " ", c.get_text(" ", strip=True)) for c in tr.find_all(["td", "th"])]
        if not cells or cells[0].lower().startswith("finding measure"):
            continue
        if cells[0].lower().startswith("average"):
            continue

        # Expected semantic order:
        # finding code | year | original mean | original SD | transformed mean | transformed SD
        # Some WDH rows have missing SD cells. Anchor on the 4-digit year.
        year_i = next((i for i, x in enumerate(cells) if YEAR_RE.match(x)), None)
        if year_i is None or year_i == 0:
            continue

        code = cells[year_i - 1]
        year = int(cells[year_i])
        tail = cells[year_i + 1:]
        nums = [number(x) for x in tail]

        # When all six columns are present, transformed mean is nums[2].
        # With a missing original SD, it is typically nums[1].
        # Prefer the cell explicitly aligned to the second "mean" header when
        # column count permits; otherwise use the last numeric pair heuristic.
        original_mean = nums[0] if nums else np.nan
        original_sd = nums[1] if len(nums) >= 4 else np.nan
        scale_mean = nums[2] if len(nums) >= 3 else (nums[-1] if nums else np.nan)
        scale_sd = nums[3] if len(nums) >= 4 else np.nan

        if not np.isfinite(scale_mean):
            continue
        out.append({
            "country": country,
            "measure_type": page.measure_type,
            "table2_family": page.table2_family,
            "finding_measure_code": code,
            "year": year,
            "original_mean": original_mean,
            "original_sd": original_sd,
            "scale_0_10_mean": scale_mean,
            "scale_0_10_sd": scale_sd,
            "source_url": page.url,
        })
    return out


def parse_page(html: str, page: MeasurePage) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    out = []

    # Primary path: country heading followed by an HTML table.
    for h3 in soup.find_all("h3"):
        country = country_from_heading(h3.get_text(" ", strip=True))
        if not country or country.lower() in {"measure types"}:
            continue
        table = h3.find_next("table")
        if table is None:
            continue
        # Guard against accidentally crossing into the next country section.
        next_h3 = h3.find_next("h3")
        if next_h3 is not None and table.sourceline and next_h3.sourceline:
            if table.sourceline > next_h3.sourceline:
                continue
        out.extend(parse_table_rows(table, country, page))

    if out:
        return out

    raise RuntimeError(
        f"No WDH finding rows parsed from {page.url}. "
        "Inspect current DOM before changing parsing rules."
    )


def build() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    rows = []
    for page in PAGES:
        rows.extend(parse_page(get_html(page.url), page))

    findings = pd.DataFrame(rows).sort_values(
        ["measure_type", "country", "year", "finding_measure_code"]
    ).reset_index(drop=True)

    annual = (
        findings.groupby(
            ["country", "measure_type", "table2_family", "year", "source_url"],
            as_index=False,
        )
        .agg(
            annual_mean_0_10=("scale_0_10_mean", "mean"),
            n_findings=("scale_0_10_mean", "size"),
            annual_sd_mean=("scale_0_10_sd", "mean"),
        )
        .sort_values(["table2_family", "country", "year"])
        .reset_index(drop=True)
    )

    # Historical paper convention: 10- and 11-step numerical life-satisfaction
    # are treated as equivalent. Do this only after type-level annual averaging.
    family_annual = (
        annual.groupby(["country", "table2_family", "year"], as_index=False)
        .agg(
            annual_mean_0_10=("annual_mean_0_10", "mean"),
            contributing_measure_types=("measure_type", lambda x: ";".join(sorted(set(x)))),
            n_type_year_cells=("measure_type", "size"),
            n_underlying_findings=("n_findings", "sum"),
        )
        .sort_values(["table2_family", "country", "year"])
        .reset_index(drop=True)
    )
    return findings, annual, family_annual


def main() -> int:
    findings, annual, family = build()
    findings.to_csv(DATA / "wdh_html_findings_core8.csv", index=False)
    annual.to_csv(DATA / "wdh_html_annual_core8_by_type.csv", index=False)
    family.to_csv(DATA / "wdh_html_annual_table2_families.csv", index=False)

    assert set(findings["measure_type"]) == {p.measure_type for p in PAGES}
    assert findings["year"].between(1900, 2030).all()
    assert findings["scale_0_10_mean"].between(0, 10).all()
    assert not annual.duplicated(["country", "measure_type", "year"]).any()
    assert not family.duplicated(["country", "table2_family", "year"]).any()

    print(
        f"PASS: {len(findings)} finding rows -> {len(annual)} type-year cells "
        f"-> {len(family)} Table-2 family-year cells"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
