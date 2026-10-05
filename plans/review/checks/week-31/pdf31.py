"""Read the delivered Week 31 PDFs back into dots, rings, lines, boxes and text.

Shared by the Week 31 math-check scripts.  Uses PyMuPDF only to read vector
drawings and text positions from the delivered student PDFs; nothing from the
packet's own sources, verifiers or answer files is imported.
"""
import os as _os
import math

HERE = _os.path.dirname(_os.path.abspath(__file__))
# Committed copy lives in plans/review/checks/week-31/ (four folders up);
# the working copy lives in tmp/review-runs/week-31/ (three folders up).
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
if not _os.path.isdir(_os.path.join(ROOT, 'lowell-math-circle-year-2')):
    ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..'))
WEEK = _os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-31')
PDFS = {
    'K-1': _os.path.join(WEEK, 'week-31-k-1.pdf'),
    '2-3': _os.path.join(WEEK, 'week-31-grades-2-3.pdf'),
    '4-5': _os.path.join(WEEK, 'week-31-grades-4-5.pdf'),
    'bonus': _os.path.join(WEEK, 'week-31-bonus.pdf'),
}
GUIDES = {
    'base': _os.path.join(WEEK, 'week-31-facilitator.pdf'),
    'bonus': _os.path.join(WEEK, 'week-31-bonus-facilitator.pdf'),
}
PT_PER_CM = 72 / 2.54


def _items_kind(d):
    return tuple(it[0] for it in d['items'])


def read_page(page):
    """Return a dict of primitive shapes on one page (PDF points, y downward)."""
    import pymupdf  # noqa: F401  (imported lazily so callers can report absence)
    dots, rings, squares, lines, boxes = [], [], [], [], []
    for d in page.get_drawings():
        kind = _items_kind(d)
        r = d['rect']
        cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
        if kind == ('c', 'c', 'c', 'c'):
            rad = (r.width + r.height) / 4
            if d['type'] == 'f':
                dots.append({'x': cx, 'y': cy, 'r': rad, 'w': r.width, 'h': r.height,
                             'fill': d['fill']})
            else:
                rings.append({'x': cx, 'y': cy, 'r': rad, 'w': r.width, 'h': r.height,
                              'lw': d['width']})
        elif kind == ('l', 'l', 'l', 'l') and d['type'] == 'f' and r.width < 10:
            squares.append({'x': cx, 'y': cy, 'w': r.width, 'h': r.height})
        elif kind == ('re',) or (kind == ('l', 'l', 'l', 'l') and r.width > 20):
            boxes.append({'x0': r.x0, 'y0': r.y0, 'x1': r.x1, 'y1': r.y1, 'type': d['type']})
        elif all(k == 'l' for k in kind):
            for it in d['items']:
                p, q = it[1], it[2]
                lines.append({'x0': p.x, 'y0': p.y, 'x1': q.x, 'y1': q.y,
                              'lw': d['width'], 'color': d['color']})
    texts = []
    for b in page.get_text('dict')['blocks']:
        for ln in b.get('lines', []):
            for sp in ln['spans']:
                t = sp['text'].strip()
                if t:
                    x0, y0, x1, y1 = sp['bbox']
                    texts.append({'t': t, 'x': (x0 + x1) / 2, 'y': (y0 + y1) / 2,
                                  'bbox': [x0, y0, x1, y1], 'size': sp['size']})
    return {'dots': dots, 'rings': rings, 'squares': squares, 'lines': lines,
            'boxes': boxes, 'texts': texts}


def grids(dots, spacings, tol=0.015):
    """Group dots into lattices: dots joined by axis-aligned steps of one of the
    given spacings (in points).  Returns a list of grids with lattice indices."""
    n = len(dots)
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i in range(n):
        for j in range(i + 1, n):
            dx = abs(dots[i]['x'] - dots[j]['x'])
            dy = abs(dots[i]['y'] - dots[j]['y'])
            for s in spacings:
                if (abs(dx - s) < tol * s and dy < 0.3) or (abs(dy - s) < tol * s and dx < 0.3):
                    parent[find(i)] = find(j)
    comps = {}
    for i in range(n):
        comps.setdefault(find(i), []).append(dots[i])
    out = []
    for members in comps.values():
        xs = sorted(set(round(d['x'], 2) for d in members))
        ys = sorted(set(round(d['y'], 2) for d in members), reverse=True)  # bottom first
        gx = [b - a for a, b in zip(xs, xs[1:])]
        gy = [a - b for a, b in zip(ys, ys[1:])]
        out.append({'n': len(members), 'cols': len(xs), 'rows': len(ys),
                    'x0': xs[0], 'y0': ys[0], 'xs': xs, 'ys': ys,
                    'sx': gx, 'sy': gy,
                    'radius': sorted(set(round(d['r'], 3) for d in members))})
    out.sort(key=lambda g: (round(g['ys'][-1]), g['x0']))
    return out


def lattice_of(g, x, y):
    """Lattice coordinates (a, b) of point (x, y) in grid g (b upward), plus error."""
    sx = (g['xs'][-1] - g['xs'][0]) / max(1, g['cols'] - 1)
    sy = (g['ys'][0] - g['ys'][-1]) / max(1, g['rows'] - 1)
    a = (x - g['x0']) / sx
    b = (g['y0'] - y) / sy
    A, B = round(a), round(b)
    return (A, B), math.hypot(a - A, b - B)


def in_grid(g, x, y, margin=0.6):
    sx = (g['xs'][-1] - g['xs'][0]) / max(1, g['cols'] - 1)
    sy = (g['ys'][0] - g['ys'][-1]) / max(1, g['rows'] - 1)
    return (g['xs'][0] - margin * sx <= x <= g['xs'][-1] + margin * sx and
            g['ys'][-1] - margin * sy <= y <= g['ys'][0] + margin * sy)


def open_pdf(path):
    import pymupdf
    return pymupdf.open(path)
