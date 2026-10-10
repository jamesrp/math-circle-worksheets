"""Exact frieze-symmetry engine for the Week 35 check (standard library only).

A motif is a list of points (polygon vertices in order, then the arrow tail and
tip).  A placement is (sx, sy, tx, ty): p -> (sx*px + tx, sy*py + ty) with
sx, sy = +-1, so the four forms are A (1,1), H A (1,-1), V A (-1,1), R A (-1,-1).
A border is a period P and the placements in one period; it repeats by P.

Because the motif's own symmetry group is trivial (checked separately), every
symmetry of a border is fixed by where it sends one motif.  So the candidates
t_{kP} g_j g_0^{-1} are all the symmetries there are; each is verified
geometrically by transforming the actual point sets.
"""
from fractions import Fraction as F
from itertools import product

FORMS = {"A": (1, 1), "HA": (1, -1), "VA": (-1, 1), "RA": (-1, -1)}


def fr(x):
    return F(x).limit_denominator(1000) if not isinstance(x, F) else x


def apply(g, p):
    sx, sy, tx, ty = g
    return (sx * p[0] + tx, sy * p[1] + ty)


def compose(f, g):  # f after g
    fsx, fsy, ftx, fty = f
    gsx, gsy, gtx, gty = g
    return (fsx * gsx, fsy * gsy, fsx * gtx + ftx, fsy * gty + fty)


def inverse(g):
    sx, sy, tx, ty = g
    return (sx, sy, -sx * tx, -sy * ty)


def placed(motif, g):
    return frozenset(apply(g, p) for p in motif)


class Border:
    def __init__(self, name, period, items):
        """items: list of (form, x, y) with x, y the anchor (motif centre)."""
        self.name = name
        self.P = fr(period)
        self.items = [(f, fr(x), fr(y)) for f, x, y in items]
        self.g = [(FORMS[f][0], FORMS[f][1], x, y) for f, x, y in self.items]

    def window(self, motif, K=4):
        s = set()
        for k in range(-K, K + 1):
            for sx, sy, tx, ty in self.g:
                s.add(placed(motif, (sx, sy, tx + k * self.P, ty)))
        return s

    def symmetries(self, motif, K=2):
        """All symmetries f whose image of motif 0 lies within K periods."""
        win = self.window(motif, K + 3)
        g0inv = inverse(self.g[0])
        found = []
        for k in range(-K, K + 1):
            for gj in self.g:
                target = (gj[0], gj[1], gj[2] + k * self.P, gj[3])
                f = compose(target, g0inv)
                ok = all(placed(motif, compose(f, gi)) in win for gi in self.g)
                finv = inverse(f)
                ok = ok and all(placed(motif, compose(finv, gi)) in win for gi in self.g)
                if ok:
                    found.append(f)
        return sorted(set(found))


def classify(f):
    sx, sy, tx, ty = f
    if (sx, sy) == (1, 1):
        if tx == 0 and ty == 0:
            return ("identity",)
        return ("slide", tx, ty)
    if (sx, sy) == (1, -1):
        if tx == 0:
            return ("hflip", ty / 2)          # reflection in y = ty/2
        return ("glide", ty / 2, tx)          # glide along y = ty/2 by tx
    if (sx, sy) == (-1, 1):
        if ty == 0:
            return ("vflip", tx / 2)          # reflection in x = tx/2
        return ("vglide", tx / 2, ty)
    return ("halfturn", tx / 2, ty / 2)       # centre


def summary(border, motif, K=2):
    syms = [classify(f) for f in border.symmetries(motif, K)]
    out = {"slide": [], "hflip": [], "glide": [], "vflip": [], "vglide": [], "halfturn": []}
    for s in syms:
        if s[0] == "identity":
            continue
        out[s[0]].append(s[1:])
    return out


def fmt(v):
    v = F(v)
    return str(v.numerator) if v.denominator == 1 else f"{float(v):g}"


def describe(border, motif, K=2):
    s = summary(border, motif, K)
    parts = []
    parts.append("slides " + ",".join(fmt(t[0]) for t in s["slide"] if t[1] == 0))
    if any(t[1] != 0 for t in s["slide"]):
        parts.append("NONHORIZONTAL SLIDES!")
    parts.append("hflips y=" + ",".join(fmt(t[0]) for t in s["hflip"]) if s["hflip"] else "no hflip")
    parts.append("glides " + ",".join(f"y={fmt(c)}:{fmt(a)}" for c, a in s["glide"]) if s["glide"] else "no glide")
    parts.append("vflips x=" + ",".join(fmt(t[0]) for t in s["vflip"]) if s["vflip"] else "no vflip")
    parts.append("halfturns " + ",".join(f"({fmt(a)},{fmt(b)})" for a, b in s["halfturn"]) if s["halfturn"] else "no halfturn")
    if s["vglide"]:
        parts.append("VERTICAL GLIDES!")
    return "; ".join(parts)


# ---------- polygon helpers ----------

def polygon_isometries(pts, tol=1e-6):
    """All isometries of the plane mapping the vertex list onto itself as a set."""
    import math
    n = len(pts)
    res = []
    a, b = pts[0], pts[1]
    dab = math.dist(a, b)
    for i, j in product(range(n), repeat=2):
        if i == j or abs(math.dist(pts[i], pts[j]) - dab) > tol:
            continue
        for refl in (False, True):
            # map a->pts[i], b->pts[j]
            ux, uy = (b[0] - a[0]) / dab, (b[1] - a[1]) / dab
            vx, vy = (pts[j][0] - pts[i][0]) / dab, (pts[j][1] - pts[i][1]) / dab

            def T(p, ux=ux, uy=uy, vx=vx, vy=vy, i=i, refl=refl):
                dx, dy = p[0] - a[0], p[1] - a[1]
                s, t = dx * ux + dy * uy, -dx * uy + dy * ux
                if refl:
                    t = -t
                return (pts[i][0] + s * vx - t * vy, pts[i][1] + s * vy + t * vx)
            img = [T(p) for p in pts]
            if all(min(math.dist(q, p) for p in pts) < tol for q in img):
                res.append((i, j, refl))
    return res


def point_in_poly(x, y, poly):
    inside = False
    n = len(poly)
    for k in range(n):
        x1, y1 = poly[k]
        x2, y2 = poly[(k + 1) % n]
        if (y1 > y) != (y2 > y):
            xc = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < xc:
                inside = not inside
    return inside
