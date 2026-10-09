"""Read every shuffle-machine mat straight from the vector drawings of the Week 3 PDFs.

Independent of the packet's own generators and checkers: it uses only the final PDFs.
A mat is a row of slot squares (light-grey fill) with a matching row directly below it.
An arrow is a black stroked path whose first point sits on the bottom edge of a top slot;
its target is the bottom slot under its last point (the end of the final vertical stub),
and an arrowhead (black filled polygon) must sit just below that point.

Repository root: four folders up from plans/review/checks/week-03/ (the committed copy),
or three up from tmp/review-runs/week-03/ (the run folder).
"""
import math
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent


def repo_root():
    for up in HERE.parents:
        if (up / "lowell-math-circle-year-2").is_dir():
            return up
    raise SystemExit("repository not found")


REPO = repo_root()
WEEK = REPO / "lowell-math-circle-year-2" / "week-03"

COL = {
    "green": (0x3F, 0xAE, 0x4A), "blue": (0x2F, 0x6F, 0xD6), "red": (0xD8, 0x34, 0x3C), "yellow": (0xF5, 0xC5, 0x18),
    "purple": (0x7D, 0x46, 0xA8), "pink": (0xF0, 0x7A, 0xB4), "teal": (0x1E, 0xA5, 0x9B), "gray": (0x8C, 0x90, 0x99),
}


def colour_name(fill):
    if fill is None:
        return None
    rgb = tuple(round(255 * c) for c in fill)
    best = min(COL, key=lambda k: sum((a - b) ** 2 for a, b in zip(COL[k], rgb)))
    return best if sum((a - b) ** 2 for a, b in zip(COL[best], rgb)) < 300 else None


def is_slotfill(fill):
    return fill is not None and all(abs(c - 0.975) < 0.01 for c in fill)


def pts_of(d):
    out = []
    for it in d["items"]:
        for p in it[1:]:
            if hasattr(p, "x"):
                out.append((p.x, p.y))
    return out


class Mat:
    def __init__(self, top, bot):
        self.top, self.bot = top, bot  # lists of Rect, left to right
        self.n = len(top)
        self.targets = [None] * self.n
        self.pictures = [None] * self.n
        self.heads = []          # (slot index, tip x offset from slot centre / slot width)
        self.paths = [None] * self.n
        self.labels = []

    @property
    def perm(self):
        return None if None in self.targets else [t + 1 for t in self.targets]

    @property
    def bbox(self):
        return pymupdf.Rect(self.top[0].x0, self.top[0].y0, self.bot[-1].x1, self.bot[-1].y1)


def slot_index(row, x, tol=0.6):
    for i, r in enumerate(row):
        if r.x0 - tol <= x <= r.x1 + tol:
            return i
    return None


def is_guide_slot(d):
    r = d["rect"]
    return (d["type"] == "s" and abs((d.get("width") or 0) - 0.5) < 0.01 and len(d["items"]) == 4
            and all(it[0] == "l" for it in d["items"]) and abs(r.width - r.height) < 0.5 and 8 < r.width < 30)


def read_page(page, guide=False):
    drs = page.get_drawings()
    if guide:
        slots = [d["rect"] for d in drs if is_guide_slot(d)]
    else:
        slots = [d["rect"] for d in drs if d["type"] == "fs" and is_slotfill(d.get("fill"))]
    if not slots:
        return []
    # group into rows: same y0, y1; split on large x gaps
    rows = {}
    for r in slots:
        rows.setdefault((round(r.y0, 1), round(r.y1, 1)), []).append(r)
    rowlist = []
    for key, rs in rows.items():
        rs.sort(key=lambda r: r.x0)
        cur = [rs[0]]
        for a, b in zip(rs, rs[1:]):
            if b.x0 - a.x1 > 0.5 * a.width:
                rowlist.append(cur)
                cur = []
            cur.append(b)
        rowlist.append(cur)
    # pair each row with the nearest row below with identical x positions
    used, mats = set(), []
    rowlist.sort(key=lambda rs: rs[0].y0)
    for i, r in enumerate(rowlist):
        if i in used:
            continue
        cands = [j for j, s in enumerate(rowlist) if j not in used and j != i and s[0].y0 > r[0].y1
                 and len(s) == len(r) and all(abs(a.x0 - b.x0) < 0.5 and abs(a.width - b.width) < 0.5 for a, b in zip(r, s))]
        if not cands:
            continue
        j = min(cands, key=lambda j: rowlist[j][0].y0)
        # the row below must be closer than any other row with the same x positions that is above it
        used |= {i, j}
        mats.append(Mat(r, rowlist[j]))
    heads = []
    for d in drs:
        if d["type"] == "fs" and d.get("fill") and all(c < 0.05 for c in d["fill"]) and len(d["items"]) in (3, 4):
            p = pts_of(d)
            tip = max(p, key=lambda q: q[1])
            heads.append(tip)
    for d in drs:
        if d["type"] != "s" or not d.get("color") or any(c > 0.05 for c in d["color"]):
            continue
        if guide and is_guide_slot(d):
            continue
        p = pts_of(d)
        if len(p) < 2:
            continue
        x0, y0 = p[0]
        x1, y1 = p[-1]
        hit = None
        for m in mats:
            ytopbot = m.top[0].y1
            if abs(y0 - ytopbot) < 0.6 and slot_index(m.top, x0, 0.0) is not None and y1 > y0 + 5 and y1 < m.bot[0].y0 + 0.5:
                hit = m
        if hit is None:
            continue
        a = slot_index(hit.top, x0, 0.0)
        b = slot_index(hit.bot, x1, 0.0)
        assert b is not None, ("arrow end outside every bottom slot", x1)
        assert hit.targets[a] is None, "two arrows leave one top slot"
        hit.targets[a] = b
        hit.paths[a] = p
        # arrowhead: tip below the path end, at the bottom row's top edge
        tips = sorted(heads, key=lambda t: math.hypot(t[0] - x1, t[1] - y1))
        tip = tips[0]
        assert math.hypot(tip[0] - x1, tip[1] - y1) < 12, ("arrowhead not found", x1, y1)
        assert len(tips) == 1 or math.hypot(tips[1][0] - x1, tips[1][1] - y1) > math.hypot(tip[0] - x1, tip[1] - y1) + 2
        # the arrowhead tip, not only the path end, must sit over the target slot
        assert slot_index(hit.bot, tip[0], 0.0) == b, ("arrowhead over a different slot", tip, b)
        assert abs(tip[1] - hit.bot[0].y0) < 3.5, ("arrowhead does not touch the bottom slot", tip, hit.bot[0].y0)
        r = hit.bot[b]
        hit.heads.append((b, (tip[0] - (r.x0 + r.x1) / 2) / r.width))
    # pictures above the top slots
    for d in drs:
        name = colour_name(d.get("fill"))
        if not name:
            continue
        rr = d["rect"]
        cx = (rr.x0 + rr.x1) / 2
        for m in mats:
            if 0 <= m.top[0].y0 - rr.y1 < 12 and rr.height > 2.5:
                k = slot_index(m.top, cx, 2.0)
                if k is not None:
                    m.pictures[k] = name
    # text labels near each mat
    words = page.get_text("words")
    for m in mats:
        bb = m.bbox
        for w in words:
            wx, wy = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
            if bb.x0 - 60 <= wx <= bb.x1 + 60 and bb.y0 - 40 <= wy <= bb.y1 + 20:
                m.labels.append(w[4])
    mats.sort(key=lambda m: (round(m.top[0].y0 / 20), m.top[0].x0))
    return mats


def read_pdf(name):
    doc = pymupdf.open(WEEK / name)
    guide = "facilitator" in name
    return [(pno + 1, read_page(page, guide)) for pno, page in enumerate(doc)]


def crossings(m):
    """Every pair of arrow paths that cross: (i, j, angle in degrees, distance from crossing to nearest bend)."""
    def segs(p):
        return [(p[k], p[k + 1]) for k in range(len(p) - 1)]

    def inter(a, b, c, d):
        (x1, y1), (x2, y2), (x3, y3), (x4, y4) = a, b, c, d
        den = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
        if abs(den) < 1e-9:
            return None
        t = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / den
        u = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / den
        if 0 < t < 1 and 0 < u < 1:
            return (x1 + t * (x2 - x1), y1 + t * (y2 - y1)), t, u
        return None

    out = []
    for i in range(m.n):
        for j in range(i + 1, m.n):
            for a, b in segs(m.paths[i]):
                for c, d in segs(m.paths[j]):
                    X = inter(a, b, c, d)
                    if X:
                        v1 = (b[0] - a[0], b[1] - a[1])
                        v2 = (d[0] - c[0], d[1] - c[1])
                        cosv = abs(v1[0] * v2[0] + v1[1] * v2[1]) / (math.hypot(*v1) * math.hypot(*v2))
                        out.append((i + 1, j + 1, math.degrees(math.acos(min(1, cosv))), X[0]))
    return out
