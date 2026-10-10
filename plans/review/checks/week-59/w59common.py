"""Shared helpers for the independent Week 59 math check (constant width).

Nothing here is imported from the packet's own builders or checkers
(make_assets.py, geometry.py, verify_math.py are not used).

* find_repo(): the repository root, from this file's own location.  The
  committed copy lives in <repo>/plans/review/checks/week-59/ (four folders up
  from the file); the working copy lives in <repo>/tmp/review-runs/week-59/.
* page_paths(pdf, page): every vector path that the delivered PDF draws on a
  page, read by converting that page with poppler's `pdftocairo -svg` and
  parsing the SVG path data (M/L/C/Z) with its transform.  Coordinates are
  returned in millimetres with the origin at the bottom-left page corner and
  y pointing up.  Glyph outlines (text) are excluded.
* page_text(pdf, page): `pdftotext -layout` text of one page.
* Exact support-function tools for line and cubic Bezier segments, so widths
  of the compiled outlines are computed from the actual curves rather than
  from control-point boxes.
"""
import math
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PT = 25.4 / 72.0  # mm per PostScript point


def find_repo():
    cands = []
    if len(HERE.parents) > 3:
        cands.append(HERE.parents[3])   # plans/review/checks/week-59 -> repo
    if len(HERE.parents) > 2:
        cands.append(HERE.parents[2])   # tmp/review-runs/week-59 -> repo
    for c in cands:
        if (c / "lowell-math-circle-year-2" / "week-59").is_dir():
            return c
    for p in [HERE] + list(HERE.parents):
        if (p / "lowell-math-circle-year-2" / "week-59").is_dir():
            return p
    sys.exit("repository not found above " + str(HERE))


REPO = find_repo()
WEEK = REPO / "lowell-math-circle-year-2" / "week-59"
SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-59"
STUDENT_PDF = WEEK / "week-59-students.pdf"
MATERIALS_PDF = WEEK / "week-59-materials.pdf"
GUIDE_PDF = WEEK / "week-59-facilitator.pdf"


class Log:
    def __init__(self):
        self.lines, self.fails, self.oks = [], 0, 0

    def say(self, s=""):
        print(s)
        self.lines.append(s)

    def check(self, cond, msg):
        if cond:
            self.oks += 1
            self.say("ok    " + msg)
        else:
            self.fails += 1
            self.say("FAIL  " + msg)
        return cond

    def note(self, msg):
        self.say("note  " + msg)

    def save(self, path):
        self.say("")
        self.say(f"summary: {self.oks} ok, {self.fails} FAIL")
        Path(path).write_text("\n".join(self.lines) + "\n")


def page_text(pdf, page):
    out = subprocess.run(["pdftotext", "-layout", "-f", str(page), "-l", str(page),
                          str(pdf), "-"], capture_output=True, text=True, check=True)
    return out.stdout


def all_text(pdf):
    out = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True,
                         text=True, check=True)
    return " ".join(out.stdout.split())


# ---------------------------------------------------------------- SVG parsing
_NUM = r"-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?"


def _attr(tag, name):
    m = re.search(r'\s' + name + r'="([^"]*)"', tag)
    return m.group(1) if m else None


def page_paths(pdf, page):
    """Vector paths of one page as dicts:
    {'subpaths': [[seg,...],...], 'stroke':str|None, 'fill':str|None,
     'width':float(mm)|None, 'dash':str|None, 'closed':[bool,...]}
    seg = ('L', p0, p1) or ('C', p0, c1, c2, p3), points in mm, y up."""
    with tempfile.TemporaryDirectory() as td:
        svg = Path(td) / "p.svg"
        subprocess.run(["pdftocairo", "-svg", "-f", str(page), "-l", str(page),
                        str(pdf), str(svg)], check=True)
        s = svg.read_text()
    m = re.search(r'<svg[^>]*height="([\d.]+)(pt)?"', s)
    H = float(m.group(1))
    body = s[s.find("</defs>"):] if "</defs>" in s else s
    out = []
    for tag in re.findall(r"<path\b[^>]*>", body):
        d = _attr(tag, "d")
        if d is None:
            continue
        tr = _attr(tag, "transform")
        a, b, c, dd, e, f = 1, 0, 0, 1, 0, 0
        if tr:
            mm = re.match(r"matrix\(([^)]*)\)", tr)
            a, b, c, dd, e, f = [float(v) for v in re.split(r"[ ,]+", mm.group(1).strip())]

        def T(x, y):
            X, Y = a * x + c * y + e, b * x + dd * y + f
            return (X * PT, (H - Y) * PT)

        toks = re.findall(r"[MLCZ]|" + _NUM, d)
        subpaths, closed, cur, start, pos, i = [], [], None, None, None, 0
        while i < len(toks):
            t = toks[i]
            if t == "M":
                if cur:
                    subpaths.append(cur); closed.append(False)
                p = T(float(toks[i + 1]), float(toks[i + 2])); i += 3
                cur, start, pos = [], p, p
            elif t == "L":
                p = T(float(toks[i + 1]), float(toks[i + 2])); i += 3
                cur.append(("L", pos, p)); pos = p
            elif t == "C":
                q = [T(float(toks[i + 1 + 2 * k]), float(toks[i + 2 + 2 * k])) for k in range(3)]
                i += 7
                cur.append(("C", pos, q[0], q[1], q[2])); pos = q[2]
            elif t == "Z":
                i += 1
                if cur is not None:
                    if math.dist(pos, start) > 1e-6:
                        cur.append(("L", pos, start))
                    pos = start
                    if cur:
                        subpaths.append(cur); closed.append(True)
                    cur = []
            else:
                raise ValueError("unexpected token " + t)
        if cur:
            subpaths.append(cur); closed.append(False)
        subpaths2, closed2 = [], []
        for sp, cl in zip(subpaths, closed):
            if sp:
                subpaths2.append(sp); closed2.append(cl)
        sw = _attr(tag, "stroke-width")
        out.append(dict(subpaths=subpaths2, closed=closed2,
                        stroke=_attr(tag, "stroke"), fill=_attr(tag, "fill"),
                        width=float(sw) * PT if sw else None,
                        dash=_attr(tag, "stroke-dasharray")))
    return out


# --------------------------------------------------------- curve geometry
def bez(seg, t):
    p0, c1, c2, p3 = seg[1:]
    s = 1 - t
    return (s**3 * p0[0] + 3 * s * s * t * c1[0] + 3 * s * t * t * c2[0] + t**3 * p3[0],
            s**3 * p0[1] + 3 * s * s * t * c1[1] + 3 * s * t * t * c2[1] + t**3 * p3[1])


def seg_points(seg, n=64):
    if seg[0] == "L":
        return [seg[1], seg[2]]
    return [bez(seg, k / n) for k in range(n + 1)]


def seg_support(seg, u):
    """Exact max of p.u over a line or cubic segment."""
    if seg[0] == "L":
        return max(seg[1][0] * u[0] + seg[1][1] * u[1], seg[2][0] * u[0] + seg[2][1] * u[1])
    p = [q[0] * u[0] + q[1] * u[1] for q in seg[1:]]
    # derivative of cubic Bernstein: 3[(p1-p0)s^2 + 2(p2-p1)st + (p3-p2)t^2]
    a0, a1, a2 = p[1] - p[0], p[2] - p[1], p[3] - p[2]
    A = a0 - 2 * a1 + a2
    B = 2 * (a1 - a0)
    C = a0
    ts = [0.0, 1.0]
    if abs(A) > 1e-15:
        disc = B * B - 4 * A * C
        if disc >= 0:
            r = math.sqrt(disc)
            ts += [(-B + r) / (2 * A), (-B - r) / (2 * A)]
    elif abs(B) > 1e-15:
        ts.append(-C / B)
    best = -1e18
    for t in ts:
        if 0 <= t <= 1:
            s = 1 - t
            v = s**3 * p[0] + 3 * s * s * t * p[1] + 3 * s * t * t * p[2] + t**3 * p[3]
            best = max(best, v)
    return best


def support(segs, u):
    return max(seg_support(s, u) for s in segs)


def width(segs, theta_deg):
    th = math.radians(theta_deg)
    u = (math.cos(th), math.sin(th))
    return support(segs, u) + support(segs, (-u[0], -u[1]))


def width_range(segs, n=3600):
    ws = [width(segs, 180.0 * k / n) for k in range(n)]
    return min(ws), max(ws), ws


def bbox(segs):
    pts = [q for s in segs for q in seg_points(s, 32)]
    xs, ys = [q[0] for q in pts], [q[1] for q in pts]
    return min(xs), min(ys), max(xs), max(ys)


def arc_fit(seg):
    """Circle through start, middle and end of one cubic; returns center, radius,
    and the max deviation of 65 sample points from that circle."""
    p0, pm, p1 = bez(seg, 0), bez(seg, 0.5), bez(seg, 1)
    c, r = circle3(p0, pm, p1)
    dev = max(abs(math.dist(q, c) - r) for q in seg_points(seg, 64))
    return c, r, dev


def circle3(a, b, c):
    ax, ay = a; bx, by = b; cx, cy = c
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / d
    uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / d
    return (ux, uy), math.dist((ux, uy), a)


def length(segs, n=2000):
    tot = 0.0
    for s in segs:
        if s[0] == "L":
            tot += math.dist(s[1], s[2])
        else:
            pts = seg_points(s, n)
            tot += sum(math.dist(pts[k], pts[k + 1]) for k in range(n))
    return tot


def dot_centers(paths, max_r=1.0):
    """Small filled circles (TikZ \\fill ... circle), returned as (center, radius)."""
    res = []
    for p in paths:
        if p["stroke"] is None and p["fill"] and p["fill"] != "none" and len(p["subpaths"]) == 1:
            segs = p["subpaths"][0]
            if all(s[0] == "C" for s in segs) and len(segs) == 4:
                x0, y0, x1, y1 = bbox(segs)
                r = (x1 - x0 + y1 - y0) / 4
                if r <= max_r:
                    res.append((((x0 + x1) / 2, (y0 + y1) / 2), r))
    return res


def words(pdf, page):
    """Words of one page with their box centres in mm (y up): [(text, x, y)]."""
    out = subprocess.run(["pdftotext", "-bbox", "-f", str(page), "-l", str(page),
                          str(pdf), "-"], capture_output=True, text=True, check=True).stdout
    H = 792.0
    m = re.search(r'<page width="([\d.]+)" height="([\d.]+)"', out)
    if m:
        H = float(m.group(2))
    res = []
    for x0, y0, x1, y1, t in re.findall(
            r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', out):
        x0, y0, x1, y1 = map(float, (x0, y0, x1, y1))
        res.append((t, (x0 + x1) / 2 * PT, (H - (y0 + y1) / 2) * PT))
    return res


def nearest_word(ws, text, p):
    c = [(math.dist((x, y), p), (x, y)) for t, x, y in ws if t == text]
    return min(c) if c else (float("inf"), None)
