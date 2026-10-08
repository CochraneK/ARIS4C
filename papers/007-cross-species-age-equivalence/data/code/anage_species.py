# -*- coding: utf-8 -*-
"""Print key AnAge fields for candidate target species."""
import csv

COLS = [2, 3, 8, 9, 13, 14, 15, 16, 20, 24, 25, 26, 28, 30, 83, 84, 85, 87, 89, 92]
f = open("data/suppl/anage_lu2023_snapshot.csv", encoding="utf-8")
r = csv.reader(f)
next(r); hdr = next(r)
rows = [row for row in r]

CAND = ["Homo sapiens", "Mus musculus", "Felis catus", "Canis lupus familiaris",
        "Canis familiaris", "Pan troglodytes", "Gorilla gorilla", "Bos taurus",
        "Equus caballus", "Loxodonta africana", "Sus scrofa", "Macaca mulatta",
        "Cavia porcellus", "Oryctolagus cuniculus", "Mustela putorius furo",
        "Papio anubis", "Ovis aries", "Meles meles", "Pteropus vampyrus",
        "Pteropus poliocephalus", "Pteropus alecto", "Bats", "Chimpanzee",
        "Cat", "Dog", "Rhesus", "Guinea", "Rabbit", "Ferret"]

seen = set()
for row in rows:
    name = row[2] if len(row) > 2 else ""
    common = row[3] if len(row) > 3 else ""
    for c in CAND:
        if c.lower() in name.lower() or c.lower() in common.lower():
            key = name
            if key in seen:
                continue
            seen.add(key)
            vals = [row[i] if i < len(row) else "" for i in COLS]
            print(" | ".join(str(v)[:28] for v in vals))
            break
print("matched:", len(seen))
