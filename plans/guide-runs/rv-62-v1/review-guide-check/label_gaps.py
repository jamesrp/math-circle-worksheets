#!/usr/bin/env python3
"""Measure the gap between allowed-slot labels on the list pages, to see which
labels from neighbouring boards could be read together.
Usage: python3 -I label_gaps.py <student-pdf-folder>"""
import os as _os
_REPO = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))
import sys
import pymupdf as fitz

folder = sys.argv[1] if len(sys.argv) > 1 else \
    _REPO + "/plans/return-visit-drafts/week-62"
for fn, pg in [("k-1.pdf", 0), ("grades-2-3.pdf", 1), ("grades-4-5.pdf", 2)]:
    page = fitz.open(f"{folder}/{fn}")[pg]
    words = [w for w in page.get_text("words")
             if w[4].isdigit() and w[1] > 60 and w[3] < 740]
    words.sort(key=lambda w: (round(w[1]), w[0]))
    groups = []
    for w in words:
        if groups and abs(groups[-1][-1][1] - w[1]) < 2 and w[0] - groups[-1][-1][2] < 8:
            groups[-1].append(w)
        else:
            groups.append([w])
    G = [(" ".join(x[4] for x in g), g[0][0], g[0][1], g[-1][2], g[-1][3]) for g in groups]
    pairs = []
    for i in range(len(G)):
        for j in range(i + 1, len(G)):
            a, b = G[i], G[j]
            dx = max(0, max(a[1], b[1]) - min(a[3], b[3]))
            dy = max(0, max(a[2], b[2]) - min(a[4], b[4]))
            pairs.append(((dx * dx + dy * dy) ** 0.5 * 25.4 / 72, a, b))
    print(f"{fn} page {pg + 1}: closest label pairs (edge gap, positions in pt)")
    for d, a, b in sorted(pairs)[:5]:
        print(f"  {d:5.1f} mm  '{a[0]}' at ({a[1]:.0f},{a[2]:.0f})   '{b[0]}' at ({b[1]:.0f},{b[2]:.0f})")
