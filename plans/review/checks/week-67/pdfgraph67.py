"""Rebuild the road maps of the delivered Week 67 student PDF as graphs.

Reads vector drawings with pymupdf: filled black discs are plain dots,
white-filled stroked circles are labelled dots (homes, P/Q/M, cube labels),
and stroked straight segments are roads.  Two dots are joined by a road when
one drawn segment passes through both centres with no other dot strictly
between them.  Nothing is taken from the LaTeX source.
"""
from pathlib import Path
import math

import pymupdf

REPO = Path(__file__).resolve().parents[4]
STUDENT = REPO / "lowell-math-circle-year-2/week-67/week-67-students.pdf"
GUIDE = REPO / "lowell-math-circle-year-2/week-67/week-67-facilitator.pdf"

TOL = 0.6  # points


def _circle(d):
    r = d["rect"]
    return ((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2, (r.x1 - r.x0) / 2, (r.y1 - r.y0) / 2)


def page_objects(pno):
    doc = pymupdf.open(STUDENT)
    page = doc[pno]
    verts, segs = [], []
    words = page.get_text("words")
    for d in page.get_drawings():
        kinds = {it[0] for it in d["items"]}
        if kinds == {"c"}:
            cx, cy, rx, ry = _circle(d)
            if d["type"] == "f" and d.get("fill") == (0.0, 0.0, 0.0) and rx < 3:
                verts.append({"x": cx, "y": cy, "r": rx, "label": None})
            elif d["type"] == "fs" and d.get("fill") == (1.0, 1.0, 1.0):
                lab = " ".join(w[4] for w in words
                               if abs((w[0] + w[2]) / 2 - cx) < rx and abs((w[1] + w[3]) / 2 - cy) < ry)
                verts.append({"x": cx, "y": cy, "r": rx, "label": lab, "ry": ry})
        elif d["type"] == "s":
            for it in d["items"]:
                if it[0] == "l":
                    segs.append(((it[1].x, it[1].y), (it[2].x, it[2].y), d["width"], d["color"]))
                elif it[0] == "re":  # a closed rectangle path = four roads
                    r = it[1]
                    cs = [(r.x0, r.y0), (r.x1, r.y0), (r.x1, r.y1), (r.x0, r.y1)]
                    for k in range(4):
                        segs.append((cs[k], cs[(k + 1) % 4], d["width"], d["color"]))
                elif it[0] == "qu":
                    q = it[1]
                    cs = [(q.ul.x, q.ul.y), (q.ur.x, q.ur.y), (q.lr.x, q.lr.y), (q.ll.x, q.ll.y)]
                    for k in range(4):
                        segs.append((cs[k], cs[(k + 1) % 4], d["width"], d["color"]))
    # a labelled circle drawn on top of a dot replaces it
    merged = []
    for v in verts:
        if v["label"] is None and any(w["label"] is not None and math.hypot(w["x"] - v["x"], w["y"] - v["y"]) < TOL
                                      for w in verts):
            continue
        merged.append(v)
    return merged, segs, words


def _on_seg(p, a, b):
    (px, py), (ax, ay), (bx, by) = p, a, b
    L = math.hypot(bx - ax, by - ay)
    if L < 1e-9:
        return None
    cross = abs((bx - ax) * (py - ay) - (by - ay) * (px - ax)) / L
    t = ((px - ax) * (bx - ax) + (py - ay) * (by - ay)) / (L * L)
    if cross < TOL and -TOL / L <= t <= 1 + TOL / L:
        return t
    return None


def build_graph(verts, segs, min_width=0.0):
    n = len(verts)
    adj = {i: set() for i in range(n)}
    used = []
    for a, b, w, col in segs:
        if w < min_width:
            continue
        on = []
        for i, v in enumerate(verts):
            t = _on_seg((v["x"], v["y"]), a, b)
            if t is not None:
                on.append((t, i))
        on.sort()
        for (t1, i), (t2, j) in zip(on, on[1:]):
            adj[i].add(j)
            adj[j].add(i)
            used.append((i, j, w, col))
    return adj, used


def components(adj):
    seen, comps = set(), []
    for s in adj:
        if s in seen:
            continue
        stack, comp = [s], []
        seen.add(s)
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        comps.append(sorted(comp))
    return comps


def bfs(adj, s):
    dist = {s: 0}
    q = [s]
    for u in q:
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def all_dist(adj, nodes):
    return {u: bfs(adj, u) for u in nodes}


def meeting_set(D, homes, nodes):
    a, b, c = homes
    out = []
    for m in nodes:
        if (D[a][m] + D[m][b] == D[a][b] and D[a][m] + D[m][c] == D[a][c]
                and D[b][m] + D[m][c] == D[b][c]):
            out.append(m)
    return out
