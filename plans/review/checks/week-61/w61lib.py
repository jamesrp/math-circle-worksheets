"""Shared helpers for the Week 61 math check (independent of the packet's code).

Spherical geometry on the unit sphere with numpy, plus tools to read figures
out of extracted.json (made by extract.py from the delivered student PDF).
"""
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
INK = [33, 39, 45]
BALL = [249, 250, 250]
BLUE = [32, 91, 137]


def unit(v):
    v = np.asarray(v, float)
    return v / np.linalg.norm(v)


def tangent(a, b):
    """Unit tangent at a of the minor great-circle arc from a toward b."""
    a, b = unit(a), unit(b)
    return unit(b - np.dot(a, b) * a)


def corner(a, b, c):
    """Surface angle at a of triangle abc, degrees (between tangent directions)."""
    return math.degrees(math.acos(np.clip(np.dot(tangent(a, b), tangent(a, c)), -1, 1)))


def dist(a, b):
    return math.degrees(math.acos(np.clip(np.dot(unit(a), unit(b)), -1, 1)))


def solid_angle(a, b, c):
    """Van Oosterom-Strackee: area of the minor-arc triangle abc on the unit sphere."""
    a, b, c = unit(a), unit(b), unit(c)
    num = abs(np.dot(a, np.cross(b, c)))
    den = 1 + np.dot(a, b) + np.dot(b, c) + np.dot(c, a)
    return 2 * math.atan2(num, den)


def signs(x, verts):
    """Sign triple of x in the basis of the three vertex vectors (= side half-spaces)."""
    M = np.column_stack([unit(v) for v in verts])
    coef = np.linalg.solve(M, np.asarray(x, float))
    return tuple(int(np.sign(c)) for c in coef), coef


def sign_str(s):
    return "".join("+" if t > 0 else "-" for t in s)


def plane_fit(points, zmin=0.15):
    """Best plane through the origin for 3D points: (unit normal, max |n.p|).

    Points lifted from within zmin of the limb carry large depth errors from
    the sqrt, so they are left out of the fit when enough others remain.
    """
    P = np.asarray(points, float)
    if len(P) > 6:
        Q = P[np.abs(P[:, 2]) >= zmin]
        if len(Q) >= 0.3 * len(P) and len(Q) >= 3:
            P = Q
    _, _, vt = np.linalg.svd(P)
    n = vt[-1]
    return n, float(np.max(np.abs(P @ n)))


def kabsch(src, dst):
    """Orthogonal R minimising |R src - dst|; returns R, det, max residual."""
    S, D = np.asarray(src, float), np.asarray(dst, float)
    u, _, vt = np.linalg.svd(D.T @ S)
    d = np.sign(np.linalg.det(u @ vt))
    R = u @ np.diag([1, 1, d]) @ vt
    res = float(np.max(np.linalg.norm((R @ S.T).T - D, axis=1)))
    return R, d, res


# ---------------------------------------------------------------- PDF figures
def load_pages():
    return json.loads((HERE / "extracted.json").read_text())["pages"]


def pts_of(path):
    return [q for s in path["subpaths"] for q in s if q != "Z"]


def bbox(path):
    P = pts_of(path)
    xs, ys = [p[0] for p in P], [p[1] for p in P]
    return min(xs), min(ys), max(xs), max(ys)


def is_small_disc(path, color=INK):
    x0, y0, x1, y1 = bbox(path)
    return path["fill"] == color and (x1 - x0) < 6 and abs((x1 - x0) - (y1 - y0)) < 0.05 and len(pts_of(path)) > 20


class Figure:
    """One drawn ball: orthographic disc of centre (cx, cy) and radius r in PDF points."""

    def __init__(self, page, ballpath):
        x0, y0, x1, y1 = bbox(ballpath)
        self.cx, self.cy, self.r = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2
        self.box = (x0, y0, x1, y1)
        self.page = page
        pad = 0.30 * self.r
        inside = lambda b: (b[0] >= x0 - pad and b[2] <= x1 + pad and b[1] >= y0 - pad and b[3] <= y1 + pad)
        self.paths = [p for p in page["paths"] if inside(bbox(p)) and p is not ballpath]
        self.dots = [p for p in self.paths if is_small_disc(p)]
        self.bluedots = [p for p in self.paths if is_small_disc(p, BLUE)]
        self.arcs = [p for p in self.paths if p["stroke"] is not None and p["fill"] is None and len(pts_of(p)) >= 2
                     and not self._is_outline(p) and not self._is_small_ring(p)]
        self.fills = [p for p in self.paths if p["fill"] not in (None, INK, BALL, [255, 255, 255], BLUE)]
        self.words = merge_stars([w for w in page["words"] if inside((w["x0"], w["y0"], w["x1"], w["y1"]))])

    def _is_small_ring(self, p):
        b = bbox(p)
        return (b[2] - b[0]) < 6 and (b[3] - b[1]) < 6

    def _is_outline(self, p):
        b = bbox(p)
        return abs((b[2] - b[0]) / 2 - self.r) < 0.5 and abs((b[0] + b[2]) / 2 - self.cx) < 0.5

    def xy(self, p):
        return ((p[0] - self.cx) / self.r, (self.cy - p[1]) / self.r)

    def lift(self, p, back=False):
        x, y = self.xy(p)
        z2 = 1 - x * x - y * y
        if z2 < -2e-3:
            raise ValueError(f"point outside disc: {x:.4f},{y:.4f}")
        z = math.sqrt(max(0.0, z2))
        return np.array([x, y, -z if back else z])

    def dot_centre(self, path):
        x0, y0, x1, y1 = bbox(path)
        return ((x0 + x1) / 2, (y0 + y1) / 2)

    def labelled_dots(self):
        """Map label text -> dot centre (PDF pts). Each dot takes the nearest word."""
        out = {}
        for d in self.dots:
            c = self.dot_centre(d)
            best = min(self.words, key=lambda w: rect_dist(c, w))
            out.setdefault(best["text"], []).append(c)
        return out

    def word_centre(self, text):
        ws = [w for w in self.words if w["text"] == text]
        return [((w["x0"] + w["x1"]) / 2, (w["y0"] + w["y1"]) / 2) for w in ws]


def rect_dist(c, w):
    dx = max(w["x0"] - c[0], 0, c[0] - w["x1"])
    dy = max(w["y0"] - c[1], 0, c[1] - w["y1"])
    return math.hypot(dx, dy)


def merge_stars(ws):
    """Join a superscript star to the letter just left of it: 'B' + '∗' -> 'B*'."""
    letters = [dict(w) for w in ws if w["text"] != "∗"]
    for st in [w for w in ws if w["text"] == "∗"]:
        cands = [w for w in letters if abs(w["x1"] - st["x0"]) < 1.5 and abs(w["y1"] - st["y1"]) < 8]
        if cands:
            w = cands[0]
            w["text"] += "*"
            w["x1"] = st["x1"]
        else:
            letters.append(dict(st))
    return letters


def figures(page):
    balls = [p for p in page["paths"] if p["fill"] == BALL]
    figs = [Figure(page, b) for b in balls]
    return sorted(figs, key=lambda f: (round(f.cy / 50), f.cx))


def point_in_poly(pt, poly):
    x, y = pt
    inside = False
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            inside = not inside
    return inside


def interior_point(path):
    """A point well inside a filled region (first subpath), found on a grid."""
    poly = [tuple(q) for q in path["subpaths"][0] if q != "Z"]
    xs, ys = [p[0] for p in poly], [p[1] for p in poly]
    best, bd = None, -1
    for i in range(1, 40):
        for j in range(1, 40):
            q = (min(xs) + (max(xs) - min(xs)) * i / 40, min(ys) + (max(ys) - min(ys)) * j / 40)
            if point_in_poly(q, poly):
                d = min(math.hypot(q[0] - a[0], q[1] - a[1]) for a in poly)
                if d > bd:
                    best, bd = q, d
    return best
