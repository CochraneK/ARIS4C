import csv, datetime, pathlib, sys, urllib.request

BASE = pathlib.Path(r"D:\Software\ARIS4C-local\007-cross-species-age-equivalence")
URL = "https://www.ssa.gov/oact/STATS/t4c6data.csv"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
OUT = BASE / "data" / "raw" / "ssa_life_table.csv"

def progress(msg):
    with (BASE / "stage3b_progress.md").open("a", encoding="utf-8") as f:
        f.write(msg + "\n")

def parse(text):
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        age_s = parts[0]
        if age_s.lower() == "age":
            continue
        age = int(float(age_s[:-1])) if age_s.endswith("+") else int(float(age_s))
        rows.append((age, float(parts[2]), float(parts[-1])))  # age, lx, e0
    if len(rows) < 100:
        raise ValueError("too few rows: %d" % len(rows))
    return rows

last_err = ""
for attempt in (1, 2):
    try:
        req = urllib.request.Request(URL, headers=UA)
        with urllib.request.urlopen(req, timeout=40) as r:
            text = r.read().decode("utf-8", "replace")
        rows = parse(text)
        l0 = rows[0][1]
        OUT.parent.mkdir(parents=True, exist_ok=True)
        with OUT.open("w", encoding="utf-8", newline="") as f:
            f.write("# source: %s (SSA US period life table), fetched %s; age 120 = 120+ open interval; S = lx/l0; e0=%.4f\n" % (URL, datetime.date.today().isoformat(), rows[0][2]))
            f.write("age,S\n")
            for a, lx, _ in rows:
                f.write("%d,%.12g\n" % (a, lx / l0))
        print("OK rows=%d e0=%.4f S_last=%.6g" % (len(rows), rows[0][2], rows[-1][1] / l0))
        progress("T2 ssa_life_table.csv OK rows=%d e0=%.4f" % (len(rows), rows[0][2]))
        sys.exit(0)
    except Exception as e:
        last_err = repr(e)
        print("attempt %d fail: %s" % (attempt, str(e)[:140]))
progress("T2 ssa fetch FAIL: " + last_err[:120])
print("FAIL " + last_err[:160])
sys.exit(2)
