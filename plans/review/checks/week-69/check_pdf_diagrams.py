#!/usr/bin/env python3
"""Check the delivered student PDF's diagrams against the intended mathematics:
dot lattices on each page (counts, equal x/y spacing) and tree dot/road counts."""
from pathlib import Path
from collections import Counter
import pymupdf as fitz

REPO = Path(__file__).resolve().parents[4]
pdf = fitz.open(REPO / "lowell-math-circle-year-2/week-69/week-69-students.pdf")
for pno, page in enumerate(pdf, 1):
    dots, segs = [], []
    for d in page.get_drawings():
        r = d["rect"]
        if d.get("fill") is not None and r.width < 8 and abs(r.width - r.height) < 0.5:
            dots.append((round((r.x0 + r.x1) / 2, 1), round((r.y0 + r.y1) / 2, 1), round(r.width, 1)))
        for it in d["items"]:
            if it[0] == "l" and d.get("color") == (0.0, 0.0, 0.0) and (d.get("width") or 0) > 1:
                segs.append(it)
    # cluster dots by size and by vertical bands
    print(f"page {pno}: {len(dots)} small filled dots; sizes {Counter(s for *_, s in dots)}")
    if pno in (2, 3):
        # group into lattices: split by large gaps in x or y
        groups = []
        for x, y, s in sorted(dots):
            for g in groups:
                if any(abs(x - gx) < 60 and abs(y - gy) < 60 for gx, gy in g):
                    g.append((x, y)); break
            else:
                groups.append([(x, y)])
        # merge groups transitively
        merged = True
        while merged:
            merged = False
            for i in range(len(groups)):
                for j in range(i + 1, len(groups)):
                    if any(abs(a[0]-b[0]) < 60 and abs(a[1]-b[1]) < 60 for a in groups[i] for b in groups[j]):
                        groups[i] += groups.pop(j); merged = True; break
                if merged: break
        for g in groups:
            xs = sorted({x for x, _ in g}); ys = sorted({y for _, y in g})
            dx = {round(b - a, 1) for a, b in zip(xs, xs[1:])}; dy = {round(b - a, 1) for a, b in zip(ys, ys[1:])}
            print(f"   lattice {len(xs)}x{len(ys)} = {len(g)} dots; x-steps {sorted(dx)}; y-steps {sorted(dy)}")
