#!/usr/bin/env python3
"""Week 62 math check: extract every printed network from the delivered student PDF.

Independent of the packet's own builders and checkers: it reads only the final
PDF (lowell-math-circle-year-2/week-62/week-62-students.pdf), finds the drawn
circles, the single-segment conflict lines and the letters, and rebuilds each
graph from geometry.  Output: extracted.json next to this script.

Run: python3 extract.py   (needs PyMuPDF: python3 -m pip install pymupdf)
"""
import json
import math
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent


def find_repo():
    # Committed location: <repo>/plans/review/checks/week-62/<this file>
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand and (cand / "lowell-math-circle-year-2").is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):  # fallback: run folder under tmp/
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    sys.exit("repository not found above " + str(HERE))


REPO = find_repo()
PDF = REPO / "lowell-math-circle-year-2" / "week-62" / "week-62-students.pdf"
PT_PER_MM = 72 / 25.4


def circles_and_segments(page):
    circles, segs = [], []
    for order, d in enumerate(page.get_drawings()):
        kinds = [it[0] for it in d["items"]]
        r = d["rect"]
        if kinds == ["c"] * 4:
            circles.append({
                "order": order,
                "cx": (r.x0 + r.x1) / 2, "cy": (r.y0 + r.y1) / 2,
                "w": r.width, "h": r.height,
                "stroke": d.get("width") or 0,
            })
        elif kinds and all(k == "l" for k in kinds) and d["type"] == "s":
            for it in d["items"]:
                p, q = it[1], it[2]
                segs.append({"order": order, "p": [p.x, p.y], "q": [q.x, q.y],
                             "width": d.get("width") or 0})
    return circles, segs


def inside(c, x, y, slack=0.5):
    return math.hypot(x - c["cx"], y - c["cy"]) <= max(c["w"], c["h"]) / 2 + slack


def label_circles(page, circles):
    words = page.get_text("words")
    for c in circles:
        c["labels"] = []
    for w in words:
        x0, y0, x1, y1, txt = w[:5]
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        hits = [c for c in circles if inside(c, mx, my, slack=-1)]
        if len(hits) == 1:
            hits[0]["labels"].append(txt)


def endpoint_circle(circles, x, y, loose=False):
    """Circle whose centre is this endpoint (full-size networks are drawn centre to
    centre); with loose=True (small worked figures), any circle containing it."""
    best = None
    for i, c in enumerate(circles):
        d = math.hypot(x - c["cx"], y - c["cy"])
        rad = c["w"] / 2
        if d < 0.6 or (loose and d < rad + 1.5):  # centre, or anywhere inside (small figures)
            if best is None or d < best[1]:
                best = (i, d)
    return best[0] if best else None


def group_graphs(circles, segs):
    """Split a page's full-size circles into separate networks using drawing order:
    each TikZ picture draws its conflict lines, then its circles."""
    big = [c for c in circles if c["w"] > 40]
    groups, cur, seen_circle = [], [], False
    items = sorted([("c", c["order"], c) for c in big] +
                   [("s", s["order"], s) for s in segs if 1.0 < s["width"] < 2.0],
                   key=lambda t: t[1])
    cur_labels = set()
    for kind, _, obj in items:
        if kind == "s":
            if seen_circle:
                groups.append(cur)
                cur, cur_labels, seen_circle = [], set(), False
            cur.append(("s", obj))
        else:
            lab = "".join(obj["labels"])
            if lab in cur_labels:
                groups.append(cur)
                cur, cur_labels = [], set()
            cur.append(("c", obj))
            cur_labels.add(lab)
            seen_circle = True
    if cur:
        groups.append(cur)
    return groups


def main():
    doc = pymupdf.open(PDF)
    out = {"pdf": str(PDF.relative_to(REPO)), "pages": []}
    for pno, page in enumerate(doc, start=1):
        circles, segs = circles_and_segments(page)
        label_circles(page, circles)
        page_rec = {"page": pno, "networks": [], "small_figures": None,
                    "header": page.get_text().splitlines()[0]}
        for g in group_graphs(circles, segs):
            cs = [o for k, o in g if k == "c"]
            ss = [o for k, o in g if k == "s"]
            verts = {}
            for c in cs:
                lab = "".join(c["labels"])
                verts[lab] = {"center_pt": [round(c["cx"], 2), round(c["cy"], 2)],
                              "w_mm": round(c["w"] / PT_PER_MM, 2),
                              "h_mm": round(c["h"] / PT_PER_MM, 2)}
            edges, bad = [], []
            for s in ss:
                a = endpoint_circle(cs, *s["p"])
                b = endpoint_circle(cs, *s["q"])
                if a is None or b is None or a == b:
                    bad.append(s)
                    continue
                e = sorted(["".join(cs[a]["labels"]), "".join(cs[b]["labels"])])
                edges.append(e)
            page_rec["networks"].append({
                "vertices": sorted(verts), "geometry": verts,
                "edges": sorted(edges), "unattached_segments": bad,
                "segments_pt": [[s["p"], s["q"]] for s in ss],
            })
        # small worked-example figures (circles narrower than 40 pt)
        small = [c for c in circles if c["w"] <= 40]
        if small:
            sedges = []
            for s in segs:
                if s["width"] > 1.0 and s["width"] < 2:  # full-size conflict lines
                    continue
                a = endpoint_circle(small, *s["p"], loose=True)
                b = endpoint_circle(small, *s["q"], loose=True)
                if a is not None and b is not None and a != b:
                    sedges.append({"ends": sorted([" ".join(small[a]["labels"]),
                                                   " ".join(small[b]["labels"])]),
                                   "width": round(s["width"], 3),
                                   "x": round((s["p"][0] + s["q"][0]) / 2, 1)})
            page_rec["small_figures"] = {
                "circles": [{"labels": c["labels"], "center_pt": [round(c["cx"], 1), round(c["cy"], 1)],
                             "w_mm": round(c["w"] / PT_PER_MM, 2), "h_mm": round(c["h"] / PT_PER_MM, 2)}
                            for c in small],
                "edges": sedges,
            }
        out["pages"].append(page_rec)
    (HERE / "extracted.json").write_text(json.dumps(out, indent=1))
    for p in out["pages"]:
        print(f"page {p['page']}: {p['header']}")
        for i, n in enumerate(p["networks"], 1):
            sizes = {(v["w_mm"], v["h_mm"]) for v in n["geometry"].values()}
            print(f"  network {i}: V={''.join(n['vertices'])} E={' '.join(a + b for a, b in n['edges'])}"
                  f" circle sizes(mm)={sorted(sizes)} unattached={len(n['unattached_segments'])}")
        if p["small_figures"]:
            sf = p["small_figures"]
            print("  worked-example circles:", [(" ".join(c["labels"]), c["w_mm"]) for c in sf["circles"]])
            print("  worked-example lines:", [("-".join(e["ends"]), e["width"], e["x"]) for e in sf["edges"]])


if __name__ == "__main__":
    main()
