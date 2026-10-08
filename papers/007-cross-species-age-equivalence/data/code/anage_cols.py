# -*- coding: utf-8 -*-
"""Show all AnAge snapshot column names + rows for candidate target species."""
import csv

f = open("data/suppl/anage_lu2023_snapshot.csv", encoding="utf-8")
r = csv.reader(f)
title = next(r)          # row0: table title
hdr = next(r)            # row1: column names
rows = [row for row in r]
print("cols:", len(hdr), "rows:", len(rows))
print("COLS:")
for i, h in enumerate(hdr):
    print(i, repr(h))
