"""Shared helpers for the Week 48 math check (Inside and outside covers).

Written from scratch for this review. Nothing here imports or reads the
packet's own builders or checkers (make.py, draw.py, verify*.py,
student/verify.py, facilitator-src/verify_math.py).

Geometry is read from the DELIVERED PDFs with Poppler only:
  * pdftocairo -svg  -> vector paths (lines, polygons, fills) in PDF points;
  * pdftotext        -> page text.

Mathematical model (from the shared rules on every student page):
  * a grid cell is WHOLE when the gray polygon covers all of its area;
  * a cell is in the COVER when it contains positive gray area;
  * a cell that only touches the gray shape along an edge or at a corner is
    OUTSIDE (adds nothing);
  * PARTIAL = in the cover but not whole.
All area computations are exact (fractions.Fraction): a simple polygon is
clipped against each closed axis-aligned cell (Sutherland-Hodgman, valid for
area even when the polygon is not convex) and the shoelace area is compared
with 0 and with the cell area.
"""
import os
import re
import subprocess
import tempfile
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
# Committed location: plans/review/checks/week-48/ -> four folders up.
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    # Fallback when run from the scratch run folder (tmp/review-runs/week-48/).
    d = HERE
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
        d = os.path.dirname(d)
    ROOT = d

WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-48')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-48')
BONUS_SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-48-bonus')

PDFS = {
    'k-1': os.path.join(WEEK, 'week-48-k-1.pdf'),
    'grades-2-3': os.path.join(WEEK, 'week-48-grades-2-3.pdf'),
    'grades-4-5': os.path.join(WEEK, 'week-48-grades-4-5.pdf'),
    'guide': os.path.join(WEEK, 'week-48-facilitator.pdf'),
    'bonus': os.path.join(WEEK, 'week-48-bonus.pdf'),
    'bonus-guide': os.path.join(WEEK, 'week-48-bonus-facilitator.pdf'),
}
REFS = {
    'k-1': os.path.join(SRC, 'editable', 'reference-pdfs', 'k-1.pdf'),
    'grades-2-3': os.path.join(SRC, 'editable', 'reference-pdfs', 'grades-2-3.pdf'),
    'grades-4-5': os.path.join(SRC, 'editable', 'reference-pdfs', 'grades-4-5.pdf'),
    'guide': os.path.join(SRC, 'editable', 'reference-pdfs', 'facilitator-guide.pdf'),
    'bonus': os.path.join(BONUS_SRC, 'reference-pdfs', 'week-48-bonus.pdf'),
    'bonus-guide': os.path.join(BONUS_SRC, 'reference-pdfs', 'week-48-bonus-facilitator.pdf'),
}
TEX = {
    'k-1': os.path.join(SRC, 'editable', 'src', 'k-1.tex'),
    'grades-2-3': os.path.join(SRC, 'editable', 'src', 'grades-2-3.tex'),
    'grades-4-5': os.path.join(SRC, 'editable', 'src', 'grades-4-5.tex'),
}

PT_MM = 25.4 / 72.0


class Log:
    """Collects PASS/FAIL/INFO lines and writes them to <name>.out."""

    def __init__(self, title):
        self.lines = [title, '=' * len(title)]
        self.fails = 0
        self.checks = 0

    def check(self, ok, msg):
        self.checks += 1
        if not ok:
            self.fails += 1
        self.lines.append(('PASS  ' if ok else 'FAIL  ') + msg)
        return ok

    def info(self, msg):
        self.lines.append('INFO  ' + msg)

    def head(self, msg):
        self.lines.append('')
        self.lines.append('## ' + msg)

    def write(self, name):
        self.lines.append('')
        self.lines.append(f'{self.checks} checks, {self.fails} failures')
        out = '\n'.join(self.lines) + '\n'
        with open(os.path.join(HERE, name), 'w') as fh:
            fh.write(out)
        print(out)


# ----------------------------------------------------------------- PDF access

def npages(pdf):
    out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True, check=True).stdout
    return int(re.search(r'Pages:\s+(\d+)', out).group(1))


def page_text(pdf, page=None, layout=False):
    args = ['pdftotext']
    if layout:
        args.append('-layout')
    if page is not None:
        args += ['-f', str(page), '-l', str(page)]
    args += [pdf, '-']
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def _parse_d(d):
    """Parse an SVG path d attribute containing only M/L/Z (TikZ and ReportLab
    straight-line output). Returns a list of subpaths (lists of points) and a
    flag telling whether any curve command was seen."""
    toks = re.findall(r'[MLZCmlzc]|-?\d*\.?\d+(?:e-?\d+)?', d)
    subs, cur, curve, i, cmd = [], [], False, 0, None
    while i < len(toks):
        t = toks[i]
        if t in 'MLZCmlzc':
            cmd = t
            i += 1
            if cmd in 'Zz':
                if cur:
                    subs.append(cur)
                cur = []
            continue
        if cmd == 'M':
            if cur:
                subs.append(cur)
            cur = [(float(toks[i]), float(toks[i + 1]))]
            i += 2
            cmd = 'L'
        elif cmd == 'L':
            cur.append((float(toks[i]), float(toks[i + 1])))
            i += 2
        elif cmd == 'C':
            curve = True
            cur.append((float(toks[i + 4]), float(toks[i + 5])))
            i += 6
        else:
            raise ValueError('unsupported path command ' + str(cmd))
    if cur:
        subs.append(cur)
    # drop the duplicate trailing "M x y" that cairo writes after Z
    subs = [s for s in subs if len(s) > 1]
    return subs, curve


def _rgb(attr):
    if attr is None or attr == 'none':
        return None
    m = re.match(r'rgb\(([\d.]+)%,\s*([\d.]+)%,\s*([\d.]+)%\)', attr)
    if not m:
        return attr
    return tuple(round(float(v) / 100, 4) for v in m.groups())


def svg_items(pdf, page):
    """Return the vector items of one page in page points, y measured DOWN from
    the top edge (SVG convention). Glyph outlines (inside <defs>) are skipped.
    Each item: dict(fill, stroke, width, subpaths, curve, clip) where clip is
    the bounding box (x0,y0,x1,y1) of the clip path applied to it, if any."""
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, 'p.svg')
        subprocess.run(['pdftocairo', '-svg', '-f', str(page), '-l', str(page), pdf, out], check=True)
        s = open(out).read()
    defs_end = s.find('</defs>')
    defs, body = (s[:defs_end], s[defs_end:]) if defs_end >= 0 else ('', s)
    clips = {}
    for m in re.finditer(r'<clipPath id="([^"]+)">\s*<path[^>]*d="([^"]+)"', defs):
        subs, _ = _parse_d(m.group(2))
        pts = [p for sp in subs for p in sp]
        clips[m.group(1)] = (min(p[0] for p in pts), min(p[1] for p in pts),
                             max(p[0] for p in pts), max(p[1] for p in pts))
    items = []
    clip_re = re.compile(r'<g clip-path="url\(#([^)]+)\)"[^>]*>\s*$')
    for m in re.finditer(r'<path ([^>]*)/>', body):
        attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        if 'd' not in attrs:
            continue
        subs, curve = _parse_d(attrs['d'])
        tr = attrs.get('transform')
        if tr:
            a, b, c, dd, e, f = [float(v) for v in re.match(r'matrix\(([^)]*)\)', tr).group(1).split(',')]
            subs = [[(a * x + c * y + e, b * x + dd * y + f) for x, y in sp] for sp in subs]
        before = body[max(0, m.start() - 200):m.start()]
        cm = clip_re.search(before)
        items.append({
            'fill': _rgb(attrs.get('fill')),
            'stroke': _rgb(attrs.get('stroke')),
            'width': float(attrs.get('stroke-width', '0')) if attrs.get('stroke') not in (None, 'none') else 0.0,
            'subpaths': subs,
            'curve': curve,
            'clip': clips.get(cm.group(1)) if cm else None,
        })
    return items


# ------------------------------------------------------------- exact geometry

def area(poly):
    """Signed shoelace area of a polygon given as a list of Fraction points."""
    s = 0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return s / 2


def _clip_half(poly, inside, inter):
    out = []
    n = len(poly)
    for i in range(n):
        cur, prev = poly[i], poly[i - 1]
        ci, pi = inside(cur), inside(prev)
        if ci:
            if not pi:
                out.append(inter(prev, cur))
            out.append(cur)
        elif pi:
            out.append(inter(prev, cur))
    return out


def clip_rect(poly, x0, y0, x1, y1):
    """Sutherland-Hodgman clip of polygon against the closed rectangle; exact."""
    def ix(xc):
        def f(p, q):
            t = (xc - p[0]) / (q[0] - p[0])
            return (xc, p[1] + t * (q[1] - p[1]))
        return f

    def iy(yc):
        def f(p, q):
            t = (yc - p[1]) / (q[1] - p[1])
            return (p[0] + t * (q[0] - p[0]), yc)
        return f
    for inside, inter in [(lambda p: p[0] >= x0, ix(x0)), (lambda p: p[0] <= x1, ix(x1)),
                          (lambda p: p[1] >= y0, iy(y0)), (lambda p: p[1] <= y1, iy(y1))]:
        if not poly:
            return []
        poly = _clip_half(poly, inside, inter)
    return poly


def cell_area(poly, x0, y0, x1, y1):
    c = clip_rect(poly, x0, y0, x1, y1)
    return abs(area(c)) if len(c) >= 3 else F(0)


def classify(poly, x0, y0, side):
    a = cell_area(poly, x0, y0, x0 + side, y0 + side)
    if a == 0:
        return 'O', a
    if a == side * side:
        return 'W', a
    return 'P', a


def grid_status(poly, n, side=F(1), ox=F(0), oy=F(0), cols=None, rows=None):
    """Status of every cell of an n-by-n grid (or cols x rows) of the given cell
    side whose top-left corner is (ox, oy). Returns dict (col,row)->(status, area)."""
    cols = n if cols is None else cols
    rows = n if rows is None else rows
    return {(i, j): classify(poly, ox + i * side, oy + j * side, side)
            for i in range(cols) for j in range(rows)}


def bounds(status, side=F(1)):
    """(inside bound, cover bound) in units where a side-1 cell has area 1."""
    w = sum(1 for s, _ in status.values() if s == 'W')
    c = sum(1 for s, _ in status.values() if s != 'O')
    return w * side * side, c * side * side, w, c


def snap(v, den=240, tol=1e-3):
    """Snap a float (in grid units) to the nearest multiple of 1/den; return the
    Fraction and the rounding error."""
    f = F(round(v * den), den)
    return f, abs(float(f) - v)


def segments_intersect_properly(p1, p2, p3, p4):
    """True if open segments p1p2 and p3p4 cross or overlap (exact)."""
    def orient(a, b, c):
        v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        return (v > 0) - (v < 0)

    def on_seg(a, b, c):
        return min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= c[1] <= max(a[1], b[1])
    o1, o2, o3, o4 = orient(p1, p2, p3), orient(p1, p2, p4), orient(p3, p4, p1), orient(p3, p4, p2)
    if o1 != o2 and o3 != o4 and 0 not in (o1, o2, o3, o4):
        return True
    # collinear overlap counts as a problem for a simple polygon
    if o1 == o2 == 0 and (on_seg(p1, p2, p3) or on_seg(p1, p2, p4)):
        return True
    return False


def is_simple(poly):
    n = len(poly)
    for i in range(n):
        a, b = poly[i], poly[(i + 1) % n]
        for j in range(i + 1, n):
            if j == i or (j + 1) % n == i or j == (i + 1) % n:
                continue
            c, d = poly[j], poly[(j + 1) % n]
            if segments_intersect_properly(a, b, c, d):
                return False
    return True


def perimeter_sq_terms(poly):
    """List of squared edge lengths (exact)."""
    n = len(poly)
    return [(poly[(i + 1) % n][0] - poly[i][0]) ** 2 + (poly[(i + 1) % n][1] - poly[i][1]) ** 2 for i in range(n)]


def fmt(x):
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'
    return str(x)
