# Takeover (window A): peek Oxman 2026 xlsx structure -> results/s2_oxman_peek.txt
import json
import pandas as pd

BASE = r"D:/Software/ARIS4C-local/001-gca-bees/data/oxman2026"
FILES = [
    "Focal bee totals by entrance.xlsx",
    "Mean Circuits Followed Per Stage.xlsx",
    "Raw Follower Data.xlsx",
]
out = []
for fn in FILES:
    path = f"{BASE}/{fn}"
    xl = pd.ExcelFile(path)
    out.append(f"### {fn}  sheets={xl.sheet_names}")
    for sh in xl.sheet_names:
        df = xl.parse(sh)
        out.append(f"  [{sh}] shape={df.shape}")
        out.append("  cols: " + " | ".join(str(c) for c in df.columns))
        out.append("  head:")
        for _, row in df.head(5).iterrows():
            out.append("    " + " | ".join(str(v)[:24] for v in row.values))
        if len(df) > 5:
            out.append(f"    ... ({len(df)} rows total)")
    out.append("")
# record.json meta
try:
    with open(f"{BASE}/record.json", encoding="utf-8") as f:
        rec = json.load(f)
    out.append("### record.json (truncated)")
    out.append(json.dumps(rec, ensure_ascii=False)[:1500])
except Exception as e:
    out.append(f"record.json read error: {e}")

text = "\n".join(out)
with open(r"D:/Software/ARIS4C-local/001-gca-bees/results/s2_oxman_peek.txt", "w", encoding="utf-8") as f:
    f.write(text)
print(f"wrote {len(out)} lines")
print("\n".join(out[:40]))
