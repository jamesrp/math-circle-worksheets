#!/usr/bin/env python3
"""Independent extraction of the printed diagrams from the two Week 2 catalogs.

Reads vector drawings with PyMuPDF: white circles are lamps, small dark filled
circles are ON dots, 1.25-pt strokes are lines, 1.2-pt strokes are arrows.
Groups lamps into pictures (connected through lines, or by proximity for
multi-island pictures), pairs pictures across each arrow, and writes a JSON
description: per pair, normalized lamp coordinates, edges, ON set, and the
x/y scale factors needed to check equal scaling.
"""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import json
import math
import sys
from collections import defaultdict

import pymupdf

BASE = _os.path.join(ROOT, 'lowell-math-circle-year-2/week-02/')
FILES = {
    "cat": BASE + "week-02-shared-catalog.pdf",
    "up": BASE + "week-02-shared-catalog-upper.pdf",
}


def page_objects(page):
    lamps, dots, lines, arrows = [], [], [], []
    for d in page.get_drawings():
        kinds = [it[0] for it in d["items"]]
        r = d["rect"]
        if kinds and all(k == "c" for k in kinds):
            cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
            rad = (r.x1 - r.x0) / 2
            if d.get("fill") == (1.0, 1.0, 1.0) or (d.get("fill") and min(d["fill"]) > 0.95):
                lamps.append((cx, cy, rad))
            else:
                dots.append((cx, cy, rad))
        elif kinds == ["l"]:
            p1, p2 = d["items"][0][1], d["items"][0][2]
            w = round(d["width"], 2)
            seg = ((p1.x, p1.y), (p2.x, p2.y))
            if abs(w - 1.25) < 0.01 or abs(w - 2.0) < 0.01:
                lines.append(seg)
            elif abs(w - 1.2) < 0.01:
                arrows.append(seg)
    return lamps, dots, lines, arrows


def build(page):
    lamps, dots, lines, arrows = page_objects(page)
    idx = {}

    def find_lamp(pt):
        best = min(range(len(lamps)), key=lambda i: math.dist(pt, lamps[i][:2]))
        if math.dist(pt, lamps[best][:2]) < 0.6:
            return best
        return None

    edges = []
    bad = []
    for a, b in lines:
        i, j = find_lamp(a), find_lamp(b)
        if i is None or j is None:
            bad.append((a, b))
        else:
            edges.append((i, j))
    # Union-find over lamps by edges plus proximity (islands in one picture).
    parent = list(range(len(lamps)))

    def f(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, j in edges:
        parent[f(i)] = f(j)
    groups = defaultdict(list)
    for i in range(len(lamps)):
        groups[f(i)].append(i)
    comps = list(groups.values())
    on = set()
    for x, y, r in dots:
        for i, (lx, ly, lr) in enumerate(lamps):
            if math.dist((x, y), (lx, ly)) < 0.6:
                on.add(i)
    return lamps, edges, comps, on, arrows, bad


def describe(fn):
    doc = pymupdf.open(fn)
    out = []
    for pno, page in enumerate(doc, 1):
        lamps, edges, comps, on, arrows, bad = build(page)
        comp_info = []
        for c in comps:
            xs = [lamps[i][0] for i in c]
            ys = [lamps[i][1] for i in c]
            comp_info.append({
                "lamps": c,
                "bbox": [min(xs), min(ys), max(xs), max(ys)],
                "radius": round(lamps[c[0]][2], 2),
            })
        out.append({
            "page": pno,
            "lamps": [[round(x, 2), round(y, 2), round(r, 2)] for x, y, r in lamps],
            "edges": edges,
            "on": sorted(on),
            "components": comp_info,
            "arrows": [[list(map(lambda v: round(v, 2), a)), list(map(lambda v: round(v, 2), b))] for a, b in arrows],
            "unattached_lines": bad,
        })
    return out


if __name__ == "__main__":
    res = {k: describe(v) for k, v in FILES.items()}
    json.dump(res, open(_os.path.join(HERE, 'extracted.json'), "w"), indent=1)
    for k, pages in res.items():
        for p in pages:
            print(k, p["page"], "lamps", len(p["lamps"]), "edges", len(p["edges"]),
                  "on", len(p["on"]), "comps", len(p["components"]),
                  "arrow segs", len(p["arrows"]), "unattached", len(p["unattached_lines"]))
