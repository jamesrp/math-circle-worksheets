"""Shared helpers for the Week 47 math check (Gentle-step landscapes).

Written from scratch for this review. Nothing here imports or reads the
packet's own builders or checkers (make.py, draw.py, examples.py,
check_examples.py, verify*.py, student/verify.py).

Geometry is read from the DELIVERED PDFs with Poppler only:
  * pdftocairo -svg  -> vector paths (lines, circles, rectangles) in PDF points;
  * pdftotext -bbox  -> every printed word with its bounding box.
No PyMuPDF is needed.

Mathematical model taken from the student pages' shared rules:
  * a landscape gives every site a nonnegative whole height;
  * joined sites (neighbours in a row, or joined squares on a graph) differ
    by at most 1;
  * clue sites keep their printed heights.
Heights are NOT capped by the drawing: the enumerations below use a cap that
is provably never binding (max clue + number of sites), and the cap actually
used is printed so a reader can see it is generous.
"""
import os
import re
import subprocess
import tempfile
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
# Committed location: plans/review/checks/week-47/ -> four folders up.
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    # Fallback when run from the scratch run folder (tmp/review-runs/week-47/).
    d = HERE
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
        d = os.path.dirname(d)
    ROOT = d

WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-47')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-47')
BONUS_SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-47-bonus')

PDFS = {
    'k-1': os.path.join(WEEK, 'week-47-k-1.pdf'),
    'grades-2-3': os.path.join(WEEK, 'week-47-grades-2-3.pdf'),
    'grades-4-5': os.path.join(WEEK, 'week-47-grades-4-5.pdf'),
    'guide': os.path.join(WEEK, 'week-47-facilitator.pdf'),
    'bonus': os.path.join(WEEK, 'week-47-bonus.pdf'),
    'bonus-guide': os.path.join(WEEK, 'week-47-bonus-facilitator.pdf'),
}
REFS = {
    'k-1': os.path.join(SRC, 'editable', 'reference-pdfs', 'k-1.pdf'),
    'grades-2-3': os.path.join(SRC, 'editable', 'reference-pdfs', 'grades-2-3.pdf'),
    'grades-4-5': os.path.join(SRC, 'editable', 'reference-pdfs', 'grades-4-5.pdf'),
    'guide': os.path.join(SRC, 'editable', 'reference-pdfs', 'facilitator-guide.pdf'),
    'bonus': os.path.join(BONUS_SRC, 'reference-pdfs', 'week-47-bonus.pdf'),
    'bonus-guide': os.path.join(BONUS_SRC, 'reference-pdfs', 'week-47-bonus-facilitator.pdf'),
}

PT_MM = 25.4 / 72.0


class Log:
    """Collects PASS/FAIL/NOTE lines and prints a summary."""

    def __init__(self, title):
        self.title = title
        self.lines = []
        self.fails = 0
        self.passes = 0

    def check(self, cond, msg):
        if cond:
            self.passes += 1
            self.lines.append('PASS  ' + msg)
        else:
            self.fails += 1
            self.lines.append('FAIL  ' + msg)
        return cond

    def note(self, msg):
        self.lines.append('NOTE  ' + msg)

    def section(self, msg):
        self.lines.append('')
        self.lines.append('== ' + msg)

    def dump(self, path=None):
        out = [self.title, ''] + self.lines + ['', 'Summary: %d checks, %d failures' % (self.passes + self.fails, self.fails)]
        text = '\n'.join(out) + '\n'
        print(text)
        if path:
            with open(path, 'w') as f:
                f.write(text)


# ---------------------------------------------------------------- PDF reading

def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def page_count(pdf):
    m = re.search(r'Pages:\s+(\d+)', run(['pdfinfo', pdf]))
    return int(m.group(1))


def page_text(pdf, page=None, layout=False):
    cmd = ['pdftotext']
    if layout:
        cmd.append('-layout')
    if page is not None:
        cmd += ['-f', str(page), '-l', str(page)]
    cmd += [pdf, '-']
    return run(cmd)


def words(pdf, page):
    """Words on one page: dicts with s, x0, y0, x1, y1, cx, cy (top-left origin, pt)."""
    html = run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), pdf, '-'])
    out = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', html):
        x0, y0, x1, y1 = map(float, m.group(1, 2, 3, 4))
        s = m.group(5).replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
        out.append(dict(s=s, x0=x0, y0=y0, x1=x1, y1=y1, cx=(x0 + x1) / 2, cy=(y0 + y1) / 2))
    return out


_NUM = r'-?\d*\.?\d+(?:e-?\d+)?'


def _parse_color(s):
    if not s or s == 'none':
        return None
    m = re.match(r'rgb\(([\d.]+)%,\s*([\d.]+)%,\s*([\d.]+)%\)', s)
    if not m:
        return s
    return tuple(round(float(v) / 100.0, 3) for v in m.groups())


def shapes(pdf, page):
    """Vector paths on one page, in top-left-origin PDF points.

    Each shape: dict(kind, pts, fill, stroke, bbox, ncurves, nlines).
    kind is 'line' (single straight segment), 'circle' (closed, only curves,
    square bbox), 'rrect' (rounded rectangle: 4 curves + straight sides),
    'rect' (4 straight sides) or 'other'.
    """
    with tempfile.TemporaryDirectory() as td:
        svg = os.path.join(td, 'p.svg')
        subprocess.run(['pdftocairo', '-svg', '-f', str(page), '-l', str(page), pdf, svg], check=True)
        data = open(svg).read()
    body = data.split('</defs>', 1)[1]
    out = []
    for m in re.finditer(r'<path ([^>]*?)/>', body):
        attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        d = attrs.get('d', '')
        tr = attrs.get('transform')
        a, b, c, dd, e, f = 1, 0, 0, 1, 0, 0
        if tr:
            mm = re.match(r'matrix\(([^)]*)\)', tr)
            a, b, c, dd, e, f = [float(v) for v in mm.group(1).split(',')]
        toks = re.findall(r'[MLCZ]|' + _NUM, d)
        pts = []
        ncurves = nlines = 0
        i = 0
        cur = None
        while i < len(toks):
            t = toks[i]
            if t == 'M':
                cur = (float(toks[i + 1]), float(toks[i + 2]))
                pts.append(cur)
                i += 3
            elif t == 'L':
                cur = (float(toks[i + 1]), float(toks[i + 2]))
                pts.append(cur)
                nlines += 1
                i += 3
            elif t == 'C':
                cps = [(float(toks[i + 1 + 2 * k]), float(toks[i + 2 + 2 * k])) for k in range(3)]
                pts.extend(cps)
                cur = cps[-1]
                ncurves += 1
                i += 7
            elif t == 'Z':
                i += 1
            else:
                i += 1
        tp = [(a * x + c * y + e, b * x + dd * y + f) for x, y in pts]
        if not tp:
            continue
        xs = [p[0] for p in tp]
        ys = [p[1] for p in tp]
        bbox = (min(xs), min(ys), max(xs), max(ys))
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        closed = 'Z' in d
        if ncurves == 0 and nlines == 1:
            kind = 'line'
        elif ncurves >= 4 and nlines <= 1 and abs(w - h) < 0.05 * max(w, h, 1e-9):
            kind = 'circle'
        elif ncurves == 4 and nlines >= 3:
            kind = 'rrect'
        elif ncurves == 0 and closed and nlines in (3, 4):
            kind = 'rect'
        else:
            kind = 'other'
        out.append(dict(kind=kind, pts=tp, fill=_parse_color(attrs.get('fill')),
                        stroke=_parse_color(attrs.get('stroke')), bbox=bbox,
                        cx=(bbox[0] + bbox[2]) / 2, cy=(bbox[1] + bbox[3]) / 2,
                        w=w, h=h, ncurves=ncurves, nlines=nlines))
    return out


# ---------------------------------------------------------------- mathematics

def legal(heights, edges):
    return all(h >= 0 for h in heights) and all(abs(heights[u] - heights[v]) <= 1 for u, v in edges)


def path_edges(n):
    return [(i, i + 1) for i in range(n - 1)]


def ring_edges(n):
    return [(i, (i + 1) % n) for i in range(n)]


def completions(n, edges, clues, cap=None):
    """All legal completions.

    cap: largest height tried. Default max(clues)+n, which can never bind on a
    connected graph with n sites (any legal height is within n-1 of a clue).
    For a row (edges == path_edges(n)) the sites are filled left to right,
    trying every height 0..cap at the first site and h-1, h, h+1 after it
    (exactly the rows obeying the rule); otherwise every assignment of the
    free sites is tried by brute force.
    """
    if cap is None:
        cap = (max(clues.values()) if clues else 0) + n
    if list(edges) == path_edges(n):
        out = []

        def grow(prefix):
            i = len(prefix)
            if i == n:
                out.append(tuple(prefix))
                return
            cand = range(cap + 1) if i == 0 else (prefix[-1] - 1, prefix[-1], prefix[-1] + 1)
            for h in cand:
                if h < 0 or h > cap:
                    continue
                if i in clues and clues[i] != h:
                    continue
                grow(prefix + [h])
        grow([])
        return sorted(out)
    free = [i for i in range(n) if i not in clues]
    out = []
    for hs in product(range(cap + 1), repeat=len(free)):
        v = [0] * n
        for i, h in clues.items():
            v[i] = h
        for i, h in zip(free, hs):
            v[i] = h
        if legal(v, edges):
            out.append(tuple(v))
    return out


def shortest_moves(start, target, n, edges, fixed, cap):
    """BFS over legal landscapes; a move changes one non-fixed site by +-1."""
    from collections import deque
    start, target = tuple(start), tuple(target)
    seen = {start: None}
    q = deque([start])
    while q:
        s = q.popleft()
        if s == target:
            break
        for i in range(n):
            if i in fixed:
                continue
            for dlt in (-1, 1):
                v = list(s)
                v[i] += dlt
                if v[i] < 0 or v[i] > cap:
                    continue
                v = tuple(v)
                if v not in seen and legal(v, edges):
                    seen[v] = s
                    q.append(v)
    if target not in seen:
        return None, None
    path = [target]
    while seen[path[-1]] is not None:
        path.append(seen[path[-1]])
    return len(path) - 1, path[::-1]
