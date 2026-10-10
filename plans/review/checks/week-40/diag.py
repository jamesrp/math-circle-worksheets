#!/usr/bin/env python3
"""Week 40 math check: shared helpers.

Reads the DELIVERED student PDFs with pdfplumber (vector paths and characters,
not the generator source), converts everything to millimetres with a top-left
origin, and rebuilds knot/tangle diagrams from the drawn cord outlines:

  * each wide black outline stroke is a drawn piece of cord; pieces whose ends
    touch are merged, so each polyline is one gap-to-gap arc;
  * two arc ends facing each other across a gap form an underpass when the
    straight segment joining them crosses exactly one other drawn arc (the
    overstrand) exactly once;
  * unmatched ends are open ends (end dots, machine inputs/outputs);
  * no two drawn arcs may intersect anywhere (that would be a crossing with no
    gap, i.e. undetermined over/under).

Colourings are then counted by brute force over R/B/G with the rule "the three
colours at a crossing are all equal or all different".  Standard library plus
pdfplumber only.

The committed copy lives in plans/review/checks/week-40/; the repository is
four folders up from that folder (HERE.parents[3]).  When run from the scratch
run folder the script searches upward instead.
"""
import itertools
import math
import sys
from pathlib import Path

import pdfplumber

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
WEEK = REPO / "lowell-math-circle-year-2" / "week-40"
PT = 25.4 / 72.0  # mm per point

FAIL = []


def ok(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)
    return cond


def summary():
    print()
    if FAIL:
        print(f"{len(FAIL)} FAILED CHECK(S):")
        for m in FAIL:
            print("   -", m)
    else:
        print("ALL CHECKS PASSED")


# ---------------------------------------------------------------- geometry
def bez(p0, p1, p2, p3, n=24):
    out = []
    for i in range(1, n + 1):
        t = i / n
        a = (1 - t) ** 3
        b = 3 * (1 - t) ** 2 * t
        c = 3 * (1 - t) * t * t
        d = t ** 3
        out.append((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0],
                    a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]))
    return out


def flatten(path):
    """pdfplumber path (top-origin points) -> list of (polyline_mm, closed)."""
    subs = []
    cur = None
    start = None
    for cmd in path:
        op = cmd[0]
        if op == "m":
            if cur and len(cur) > 1:
                subs.append([cur, False])
            cur = [cmd[1]]
            start = cmd[1]
        elif op == "l":
            cur.append(cmd[1])
        elif op == "c":
            cur.extend(bez(cur[-1], cmd[1], cmd[2], cmd[3]))
        elif op == "v":  # first control point = current point
            cur.extend(bez(cur[-1], cur[-1], cmd[1], cmd[2]))
        elif op == "y":  # second control point = end point
            cur.extend(bez(cur[-1], cmd[1], cmd[2], cmd[2]))
        elif op == "h":
            if cur and (cur[-1] != start):
                cur.append(start)
            if cur and len(cur) > 1:
                subs.append([cur, True])
            cur = None
        else:
            raise ValueError(op)
    if cur and len(cur) > 1:
        subs.append([cur, False])
    out = []
    for pts, closed in subs:
        mm = [(x * PT, y * PT) for x, y in pts]
        if math.dist(mm[0], mm[-1]) < 1e-3:
            closed = True
        out.append((mm, closed))
    return out


def colour_of(c):
    if c is None:
        return None
    if isinstance(c, (int, float)):
        return (float(c),) * 3
    c = tuple(float(v) for v in c)
    if len(c) == 1:
        return c * 3
    if len(c) == 4:  # cmyk
        k = c[3]
        return tuple((1 - v) * (1 - k) for v in c[:3])
    return c


def colour_name(rgb):
    """Classify an RGB stroke/fill colour as R, B, G, black, white, grey."""
    if rgb is None:
        return None
    r, g, b = rgb
    if max(rgb) - min(rgb) < 0.05:
        if r < 0.15:
            return "black"
        if r > 0.95:
            return "white"
        return "grey"
    if r > g + 0.2 and r > b + 0.2:
        return "R"
    if b > r + 0.2 and b > g + 0.1:
        return "B"
    if g > r + 0.1 and g > b + 0.1:
        return "G"
    return "other" + str(rgb)


def load(pdfname, page):
    """Strokes, fills and characters of one page, in mm, top-left origin."""
    with pdfplumber.open(WEEK / pdfname) as pdf:
        pg = pdf.pages[page - 1]
        strokes, fills = [], []
        for o in pg.curves + pg.lines + pg.rects:
            path = o.get("path")
            if not path:
                x0, x1, t, b = o["x0"], o["x1"], o["top"], o["bottom"]
                path = [("m", (x0, t)), ("l", (x1, t)), ("l", (x1, b)), ("l", (x0, b)), ("h",)]
            for pts, closed in flatten(path):
                rec = dict(pts=pts, closed=closed, width=o["linewidth"] * PT,
                           stroke=colour_of(o["stroking_color"]) if o["stroke"] else None,
                           fill=colour_of(o["non_stroking_color"]) if o["fill"] else None,
                           kind=o["object_type"], dash=o.get("dash"))
                if o["stroke"]:
                    strokes.append(rec)
                if o["fill"]:
                    fills.append(rec)
        chars = [dict(text=c["text"], x=(c["x0"] + c["x1"]) / 2 * PT,
                      y=(c["top"] + c["bottom"]) / 2 * PT, size=c["size"])
                 for c in pg.chars]
        text = pg.extract_text()
    return dict(strokes=strokes, fills=fills, chars=chars, text=text)


def seg_inter(p, q, r, s):
    """Proper intersection parameter (t,u) of segments pq and rs, or None."""
    d1 = (q[0] - p[0], q[1] - p[1])
    d2 = (s[0] - r[0], s[1] - r[1])
    den = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(den) < 1e-12:
        return None
    w = (r[0] - p[0], r[1] - p[1])
    t = (w[0] * d2[1] - w[1] * d2[0]) / den
    u = (w[0] * d1[1] - w[1] * d1[0]) / den
    if 0 <= t <= 1 and 0 <= u <= 1:
        return t, u
    return None


def pt_seg_dist(p, a, b):
    vx, vy = b[0] - a[0], b[1] - a[1]
    L2 = vx * vx + vy * vy
    if L2 == 0:
        return math.dist(p, a), 0.0
    t = max(0.0, min(1.0, ((p[0] - a[0]) * vx + (p[1] - a[1]) * vy) / L2))
    return math.dist(p, (a[0] + t * vx, a[1] + t * vy)), t


def poly_dist(p, poly):
    """Distance from p to polyline, plus index of nearest segment."""
    best = (1e18, -1, 0.0)
    for i in range(len(poly) - 1):
        d, t = pt_seg_dist(p, poly[i], poly[i + 1])
        if d < best[0]:
            best = (d, i, t)
    return best


def poly_len(poly):
    return sum(math.dist(poly[i], poly[i + 1]) for i in range(len(poly) - 1))


def bbox(poly):
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    return min(xs), min(ys), max(xs), max(ys)


def in_box(poly, box):
    x0, y0, x1, y1 = bbox(poly)
    return x0 >= box[0] and y0 >= box[1] and x1 <= box[2] and y1 <= box[3]


def merge_pieces(polys, tol=0.05):
    """Join polylines whose endpoints coincide (end-to-end continuation)."""
    polys = [list(p) for p in polys]
    changed = True
    while changed:
        changed = False
        for i in range(len(polys)):
            for j in range(len(polys)):
                if i == j or polys[i] is None or polys[j] is None:
                    continue
                a, b = polys[i], polys[j]
                if math.dist(a[0], a[-1]) < tol or math.dist(b[0], b[-1]) < tol:
                    continue
                for ra in (False, True):
                    for rb in (False, True):
                        A = a[::-1] if ra else a
                        B = b[::-1] if rb else b
                        if math.dist(A[-1], B[0]) < tol:
                            polys[i] = A + B[1:]
                            polys[j] = None
                            changed = True
                            break
                    if changed:
                        break
                if changed:
                    break
            if changed:
                break
        polys = [p for p in polys if p is not None]
    return polys


# ---------------------------------------------------------------- diagrams
class Diagram:
    """Arcs (polylines), crossings (over, under_end_1, under_end_2), open ends.

    An end is (arc index, 0 for polyline start or 1 for polyline end)."""

    def __init__(self, arcs, gap_max=25.0, width=None):
        self.arcs = arcs
        self.width = width
        self.closed = [math.dist(a[0], a[-1]) < 0.05 for a in arcs]
        ends = []
        for i, a in enumerate(arcs):
            if not self.closed[i]:
                ends += [(i, 0), (i, 1)]
        self.ends = ends
        cands = []
        for e1, e2 in itertools.combinations(ends, 2):
            p, q = self.endpt(e1), self.endpt(e2)
            d = math.dist(p, q)
            if d > gap_max:
                continue
            # The two ends must face each other: each end's outward tangent
            # points roughly toward the other end.
            if self.facing(e1, q) < 0.8 or self.facing(e2, p) < 0.8:
                continue
            hits = self.hits(p, q, exclude_ends=(e1, e2))
            if len(hits) == 1:
                cands.append((d, e1, e2, hits[0]))
        cands.sort(key=lambda c: c[0])
        used = set()
        self.crossings = []
        for d, e1, e2, (arc, pt) in cands:
            if e1 in used or e2 in used:
                continue
            used |= {e1, e2}
            self.crossings.append(dict(over=arc, u=(e1, e2), point=pt, gap=d))
        self.open_ends = [e for e in ends if e not in used]

    def endpt(self, e):
        a = self.arcs[e[0]]
        return a[0] if e[1] == 0 else a[-1]

    def out_dir(self, e, back=1.5):
        """Unit outward tangent at an end (from a point ~back mm inside)."""
        a = self.arcs[e[0]]
        seq = a if e[1] == 1 else a[::-1]
        end = seq[-1]
        k = len(seq) - 2
        while k > 0 and math.dist(seq[k], end) < back:
            k -= 1
        v = (end[0] - seq[k][0], end[1] - seq[k][1])
        n = math.hypot(*v)
        return (v[0] / n, v[1] / n)

    def facing(self, e, target):
        p = self.endpt(e)
        v = (target[0] - p[0], target[1] - p[1])
        n = math.hypot(*v)
        if n == 0:
            return 1
        o = self.out_dir(e)
        return (o[0] * v[0] + o[1] * v[1]) / n

    def hits(self, p, q, exclude_ends=()):
        out = []
        for i, a in enumerate(self.arcs):
            for k in range(len(a) - 1):
                r = seg_inter(p, q, a[k], a[k + 1])
                if r is None:
                    continue
                t, u = r
                if t < 1e-6 or t > 1 - 1e-6:
                    continue  # touching at the ends themselves
                out.append((i, (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))))
        # collapse duplicate hits at a shared polyline vertex
        uniq = []
        for h in out:
            if not any(h[0] == g[0] and math.dist(h[1], g[1]) < 1e-6 for g in uniq):
                uniq.append(h)
        return uniq

    def arc_intersections(self):
        """All intersections between drawn arcs (should be none)."""
        res = []
        n = len(self.arcs)
        boxes = [bbox(a) for a in self.arcs]
        for i in range(n):
            for j in range(i, n):
                bi, bj = boxes[i], boxes[j]
                if bi[2] < bj[0] or bj[2] < bi[0] or bi[3] < bj[1] or bj[3] < bi[1]:
                    continue
                A, B = self.arcs[i], self.arcs[j]
                for k in range(len(A) - 1):
                    for m in range(len(B) - 1):
                        if i == j and abs(k - m) <= 1:
                            continue
                        if i == j and self.closed[i] and {k, m} == {0, len(A) - 2}:
                            continue
                        if seg_inter(A[k], A[k + 1], B[m], B[m + 1]):
                            res.append((i, j, A[k]))
        return res

    def min_clearance(self):
        """Smallest distance between centerlines of two different arcs, minus
        the outline width (= cap radius + half width of the other strand).
        Positive means a white gap is visible between different arcs."""
        best = 1e9
        n = len(self.arcs)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for p in self.arcs[i][:: max(1, len(self.arcs[i]) // 400)] + [self.arcs[i][-1]]:
                    d = poly_dist(p, self.arcs[j])[0]
                    best = min(best, d)
        return best - (self.width or 0)

    def components(self):
        parent = list(range(len(self.arcs)))

        def f(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for c in self.crossings:
            (a, _), (b, _) = c["u"]
            parent[f(a)] = f(b)
        return len({f(i) for i in range(len(self.arcs))})

    def colourings(self, fixed=None):
        """All valid R/B/G colourings (tuples by arc index); fixed: {arc: colour}."""
        fixed = fixed or {}
        n = len(self.arcs)
        out = []
        for c in itertools.product("RBG", repeat=n):
            if any(c[k] != v for k, v in fixed.items()):
                continue
            if all(len({c[x["over"]], c[x["u"][0][0]], c[x["u"][1][0]]}) in (1, 3)
                   for x in self.crossings):
                out.append(c)
        return out

    def traverse(self, start_arc=0):
        """Walk one component: list of (arc, reversed?) in order, plus the
        sequence of crossing events ('O' or 'U', crossing index, direction)."""
        seq = []
        arc, rev = start_arc, False
        while True:
            seq.append((arc, rev))
            end = (arc, 0 if rev else 1)
            nxt = None
            for ci, c in enumerate(self.crossings):
                if end in c["u"]:
                    other = c["u"][1] if c["u"][0] == end else c["u"][0]
                    nxt = (other[0], other[1] == 1)  # entering at end 1 -> reversed
                    break
            if nxt is None:
                return seq, False  # open
            arc, rev = nxt
            if (arc, rev) == seq[0]:
                return seq, True
            if len(seq) > 4 * len(self.arcs):
                raise RuntimeError("traversal loop")

    def crossing_events(self, start_arc=0):
        """For a closed single component: ordered O/U events and crossing signs."""
        seq, closed = self.traverse(start_arc)
        orient = {a: r for a, r in seq}
        events = []
        for arc, rev in seq:
            poly = self.arcs[arc][::-1] if rev else self.arcs[arc]
            # overpasses along this arc, in order of position along the arc
            overs = []
            for ci, c in enumerate(self.crossings):
                if c["over"] == arc:
                    d, k, t = poly_dist(c["point"], poly)
                    overs.append((k + t, ci))
            for _, ci in sorted(overs):
                events.append(("O", ci))
            # the underpass at the end of this arc
            end = (arc, 0 if rev else 1)
            for ci, c in enumerate(self.crossings):
                if end in c["u"]:
                    events.append(("U", ci))
        signs = {}
        for ci, c in enumerate(self.crossings):
            e1, e2 = c["u"]
            # direction of travel through the underpass
            if orient.get(e1[0]) is None or orient.get(e2[0]) is None:
                continue
            # incoming end is the end at which its arc (as oriented) finishes
            inc = e1 if (e1[1] == (0 if orient[e1[0]] else 1)) else e2
            outg = e2 if inc == e1 else e1
            p, q = self.endpt(inc), self.endpt(outg)
            du = (q[0] - p[0], q[1] - p[1])
            ov = c["over"]
            poly = self.arcs[ov][::-1] if orient.get(ov) else self.arcs[ov]
            d, k, t = poly_dist(c["point"], poly)
            do = (poly[k + 1][0] - poly[k][0], poly[k + 1][1] - poly[k][1])
            signs[ci] = 1 if do[0] * du[1] - do[1] * du[0] > 0 else -1
        return events, signs, closed


def rope_arcs(page, width_mm, box=None, colour="black", tol=0.05):
    polys = [s["pts"] for s in page["strokes"]
             if abs(s["width"] - width_mm) < 0.02 and colour_name(s["stroke"]) == colour
             and (box is None or in_box(s["pts"], box))]
    return merge_pieces(polys, tol)


def chars_in(page, box, texts=None):
    return [c for c in page["chars"] if box[0] <= c["x"] <= box[2] and box[1] <= c["y"] <= box[3]
            and (texts is None or c["text"] in texts)]


def fox_count(n_arcs, crossings, p=3):
    """Number of Fox p-colourings for an abstract diagram (over, u1, u2)."""
    cnt = 0
    for c in itertools.product(range(p), repeat=n_arcs):
        if all((2 * c[o] - c[a] - c[b]) % p == 0 for o, a, b in crossings):
            cnt += 1
    return cnt
