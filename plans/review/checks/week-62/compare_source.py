#!/usr/bin/env python3
"""Week 62 math check: confirm the editable source data (student/graphs.json)
describes the same networks as the delivered PDF (extracted.json from extract.py):
same vertices, same edges, and the same relative positions (cm -> pt, y flipped).
Standard library only.  Run: python3 compare_source.py > out_compare_source.txt
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand and (cand / "lowell-math-circle-year-2").is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    sys.exit("repository not found above " + str(HERE))


REPO = find_repo()
SRC = json.loads((REPO / "lowell-math-circle-year-2/source/week-62/student/graphs.json").read_text())
PDF = json.loads((HERE / "extracted.json").read_text())
PT_PER_CM = 72 / 2.54

pdf_nets = [(p["page"], n) for p in PDF["pages"] for n in p["networks"]]
src_nets = list(SRC.items())  # insertion order = page order in the builder
print(f"source networks: {len(src_nets)}; PDF networks: {len(pdf_nets)}")
bad = 0
for (name, s), (page, n) in zip(src_nets, pdf_nets):
    se = sorted("".join(sorted(e)) for e in s["edges"])
    pe = sorted("".join(e) for e in n["edges"])
    same_v = sorted(s["vertices"]) == n["vertices"]
    same_e = se == pe
    ref = sorted(s["vertices"])[0]
    sx, sy = s["coordinates_cm"][ref]
    px, py = n["geometry"][ref]["center_pt"]
    err = 0.0
    for v in s["vertices"]:
        x, y = s["coordinates_cm"][v]
        qx, qy = n["geometry"][v]["center_pt"]
        ex = (x - sx) * PT_PER_CM - (qx - px)
        ey = -(y - sy) * PT_PER_CM - (qy - py)
        err = max(err, abs(ex), abs(ey))
    good = same_v and same_e and err < 0.2
    bad += not good
    print(f"{'ok  ' if good else 'FAIL'} {name:22s} -> PDF p{page}: vertices {same_v}, edges {same_e},"
          f" max position error {err:.3f} pt")
print("mismatches:", bad)
