"""Read drawn geometry and words from the delivered Week 12 PDFs.

Written for this review; it uses pdfplumber only to read path operators and
words, and does not use the packet's own builders or checkers.  Coordinates are
PDF points with y measured downward from the top of the page.
"""
import os
import math
import pdfplumber

HERE = os.path.dirname(os.path.abspath(__file__))


def find_root():
    # Committed copy lives in plans/review/checks/week-NN/: four folders up.
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')) and os.path.exists(os.path.join(cand, 'AGENTS.md')):
        return cand
    # Fallback for the scratch run folder (tmp/review-runs/week-NN/).
    d = HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')) and os.path.exists(os.path.join(d, 'AGENTS.md')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository not found')


ROOT = find_root()
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-12')
MM = 72 / 25.4


def pdf_path(name):
    return os.path.join(WEEK, name)


def _gray(c):
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


def _subpaths(path):
    cur = []
    for seg in path:
        if seg[0] == 'm':
            if cur:
                yield cur
            cur = [seg]
        else:
            cur.append(seg)
    if cur:
        yield cur


class Page:
    def __init__(self, ppage):
        self.circles = []      # dict(cx, cy, r, fill, stroke, scolor, fcolor, lw)
        self.polylines = []    # dict(pts, closed, lw, scolor, fill, dash)
        self.beziers = []      # dict(p0, p1, p2, p3, lw, scolor)
        self.width = ppage.width
        self.height = ppage.height
        objs = list(ppage.curves) + list(ppage.lines) + list(ppage.rects)
        for o in objs:
            path = o.get('path')
            if not path:
                path = [('m', o['pts'][0])] + [('l', p) for p in o['pts'][1:]]
            for sp in _subpaths(path):
                kinds = [s[0] for s in sp]
                base = dict(lw=o.get('linewidth'), scolor=_gray(o.get('stroking_color')),
                            fcolor=_gray(o.get('non_stroking_color')), fill=bool(o.get('fill')),
                            stroke=bool(o.get('stroke', True)), dash=o.get('dash'))
                if kinds[:5] == ['m', 'c', 'c', 'c', 'c'] and all(k in 'h' for k in kinds[5:]):
                    pts = [sp[0][1]] + [p for s in sp[1:5] for p in s[1:]]
                    xs = [p[0] for p in pts]
                    ys = [p[1] for p in pts]
                    w, h = max(xs) - min(xs), max(ys) - min(ys)
                    if abs(w - h) < 0.02 * max(w, h) + 0.05:
                        d = dict(base, cx=(max(xs) + min(xs)) / 2, cy=(max(ys) + min(ys)) / 2, r=(w + h) / 4)
                        self.circles.append(d)
                        continue
                if kinds == ['m', 'c']:
                    p0 = sp[0][1]
                    p1, p2, p3 = sp[1][1], sp[1][2], sp[1][3]
                    self.beziers.append(dict(base, p0=p0, p1=p1, p2=p2, p3=p3))
                    continue
                if all(k in ('m', 'l', 'h') for k in kinds):
                    pts = [s[1] for s in sp if s[0] in ('m', 'l')]
                    closed = kinds[-1] == 'h'
                    self.polylines.append(dict(base, pts=pts, closed=closed))
                    continue
                # anything else is kept as a polyline of its anchor points
                pts = [s[-1] for s in sp if len(s) > 1]
                self.polylines.append(dict(base, pts=pts, closed=False, other=kinds))
        self.words = [dict(text=w['text'], x0=w['x0'], x1=w['x1'], top=w['top'], bottom=w['bottom'],
                           font=w.get('fontname', ''), size=w.get('size', 0),
                           cx=(w['x0'] + w['x1']) / 2, cy=(w['top'] + w['bottom']) / 2)
                      for w in ppage.extract_words(extra_attrs=['fontname', 'size'], keep_blank_chars=False)]
        self.chars = [dict(text=c['text'], cx=(c['x0'] + c['x1']) / 2, cy=(c['top'] + c['bottom']) / 2,
                           font=c.get('fontname', ''), size=c.get('size', 0), x0=c['x0'], x1=c['x1'],
                           top=c['top'], bottom=c['bottom'])
                      for c in ppage.chars]
        self.text = ppage.extract_text() or ''

    def segments(self, minlen=0.0):
        """All straight segments from open/closed polylines."""
        out = []
        for pl in self.polylines:
            pts = pl['pts'] + ([pl['pts'][0]] if pl['closed'] else [])
            for a, b in zip(pts, pts[1:]):
                if math.dist(a, b) >= minlen:
                    out.append(dict(pl, a=a, b=b))
        return out


def load(name):
    with pdfplumber.open(pdf_path(name)) as pdf:
        return [Page(p) for p in pdf.pages]


def near(p, q, tol=0.6):
    return math.dist(p, q) <= tol


def clockwise_angle(cx, cy, x, y):
    """Angle in degrees clockwise from straight up (y grows downward)."""
    a = math.degrees(math.atan2(x - cx, -(y - cy))) % 360
    return 0.0 if a > 359.9 else a


def word_from_polyline(pts, step=None, tol=0.05):
    """Read a U/D word from a polyline of equal diagonal steps.  Returns (word, step) or (None, reason)."""
    if len(pts) < 2:
        return None, 'too short'
    steps = [(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])]
    if step is None:
        step = abs(steps[0][0])
    w = ''
    for dx, dy in steps:
        if abs(dx - step) > tol * step or abs(abs(dy) - step) > tol * step:
            return None, f'step ({dx:.2f},{dy:.2f}) not a unit diagonal of {step:.2f}'
        w += 'U' if dy < 0 else 'D'
    return w, step


def heights(w):
    h = [0]
    for c in w:
        h.append(h[-1] + (1 if c == 'U' else -1))
    return h


def code_of_pairs(pairs, n):
    first = {min(p) for p in pairs}
    return ''.join('U' if i in first else 'D' for i in range(1, n + 1))


def tree_code(nodes, edges, root):
    """nodes: list of (x, y); edges: list of (i, j).  Parent is the higher end (smaller y).
    Returns (code, problems)."""
    problems = []
    children = {i: [] for i in range(len(nodes))}
    parent = {}
    for i, j in edges:
        a, b = (i, j) if nodes[i][1] < nodes[j][1] else (j, i)
        if abs(nodes[i][1] - nodes[j][1]) < 0.5:
            problems.append(f'horizontal edge {i}-{j}')
        if b in parent:
            problems.append(f'node {b} has two parents')
        parent[b] = a
        children[a].append(b)
    for i in range(len(nodes)):
        if i != root and i not in parent:
            problems.append(f'node {i} has no parent')
    if root in parent:
        problems.append('root has a parent')

    def rec(v, seen):
        if v in seen:
            problems.append('cycle')
            return ''
        seen.add(v)
        kids = sorted(children[v], key=lambda k: nodes[k][0])
        xs = [nodes[k][0] for k in kids]
        if len(set(round(x, 1) for x in xs)) != len(xs):
            problems.append(f'children of {v} share an x position')
        return ''.join('U' + rec(k, seen) + 'D' for k in kids)

    seen = set()
    code = rec(root, seen)
    if len(seen) != len(nodes):
        problems.append('not all nodes reachable')
    return code, problems
