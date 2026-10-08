# Host-side (orchestrator) helper, 2026-09-30.
# Dumps the frozen ChineseNames 2025.8 RDA datasets to CSV so that
# pilot acceptance #5 (reproducible expected initial-letter shares)
# can be evaluated without R installed.
# Frozen source: data/chinenames_pkg.tar.gz (CRAN, 359498 bytes, v2025.8, 2025-08-15).
import os
import pyreadr

BASE = os.path.join("data", "chinenames_pkg", "ChineseNames", "data")
OUT = os.path.join("data", "chinenames_pkg")
os.makedirs(OUT, exist_ok=True)

FILES = ["familyname", "population", "top100name.year", "givenname",
         "top50char.year", "top1000name.prov"]

for f in FILES:
    src = os.path.join(BASE, f + ".rda")
    try:
        res = pyreadr.read_r(src)
    except Exception as e:
        print("FAIL", f, str(e)[:150])
        continue
    import pandas as _pd
    if isinstance(res, _pd.DataFrame):
        res = {f.replace(".", "_"): res}
    for name, df in res.items():
        p = os.path.join(OUT, name + ".csv")
        df.to_csv(p, index=False)
        print("DUMPED", name, "shape=", df.shape, "cols=", list(df.columns)[:12])
print("DUMP-DONE")
