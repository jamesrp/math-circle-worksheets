"""Read the drawn towns, pictures and boxes straight out of the delivered Week 10 PDFs.

Written for this review. It uses pdfplumber only to read path operators, colours,
line widths and words. It imports nothing from the packet's own builders or checkers.
Coordinates are PDF points, y measured downward from the top of the page.
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
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-10')
PDFS = {
    'k1': os.path.join(WEEK, 'week-10-k-1.pdf'),
    'g23': os.path.join(WEEK, 'week-10-grades-2-3.pdf'),
    'g45': os.path.join(WEEK, 'week-10-grades-4-5.pdf'),
    'fac': os.path.join(WEEK, 'week-10-facilitator.pdf'),
    'rv': os.path.join(WEEK, 'week-10-return-visit.pdf'),
    'rvfac': os.path.join(WEEK, 'week-10-return-visit-facilitator.pdf'),
}
CM = 72 / 2.54


def endpoints(o):
    path = o.get('path')
    if path:
        pts = [cmd[-1] for cmd in path if cmd[0] in ('m', 'l', 'c')]
        return pts[0], pts[-1]
    return o['pts'][0], o['pts'][-1]


def circle_of(o):
    """(cx, cy, r) if the curve is a closed 4-Bezier circle, else None."""
    path = o.get('path') or []
    if len(path) < 5 or path[0][0] != 'm':
        return None
    if sum(1 for c in path if c[0] == 'c') != 4:
        return None
    w = o['x1'] - o['x0']
    h = o['bottom'] - o['top']
    if abs(w - h) > 0.05 * max(w, h):
        return None
    return ((o['x0'] + o['x1']) / 2, (o['top'] + o['bottom']) / 2, (w + h) / 4)


def bezier_points(o, n=40):
    """Polyline approximation of a (line or curve) path."""
    path = o.get('path')
    if not path:
        return list(o['pts'])
    out = []
    cur = None
    for cmd in path:
        if cmd[0] == 'm':
            cur = cmd[1]
            out.append(cur)
        elif cmd[0] == 'l':
            cur = cmd[1]
            out.append(cur)
        elif cmd[0] == 'c':
            p0, p1, p2, p3 = cur, cmd[1], cmd[2], cmd[3]
            for k in range(1, n + 1):
                t = k / n
                a, b, c, d = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3
                out.append((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0],
                            a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]))
            cur = p3
    return out


def page_objects(key, pno):
    pdf = pdfplumber.open(PDFS[key])
    p = pdf.pages[pno - 1]
    objs = list(p.lines) + list(p.curves) + list(p.rects)
    words = p.extract_words(x_tolerance=1.5)
    return p, objs, words


def read_towns(key, pno):
    """Return a list of towns on the page. Each town: dict with islands {id: (x, y)},
    labels {id: letter or None}, bridges [(id1, id2, kind, polyline)], and boxes near it."""
    p, objs, words = page_objects(key, pno)
    islands = []
    for o in objs:
        if o['object_type'] != 'curve' or not o.get('fill'):
            continue
        c = circle_of(o)
        if c and abs(c[2] - 27.0) < 1.0 and str(o.get('non_stroking_color')) in ('1.0', '(1.0,)', '[1.0]', '1'):
            islands.append(c)
    bands = [o for o in objs if abs((o.get('linewidth') or 0) - 1.6 * CM) < 0.3]
    fills = [o for o in objs if abs((o.get('linewidth') or 0) - (1.6 - 0.12) * CM) < 0.3]
    bridges = []
    problems = []
    if not islands:
        return [], ([('bands without islands', len(bands))] if bands else []), [], words
    for o in bands:
        a, b = endpoints(o)
        ia = min(range(len(islands)), key=lambda i: math.hypot(islands[i][0] - a[0], islands[i][1] - a[1]))
        ib = min(range(len(islands)), key=lambda i: math.hypot(islands[i][0] - b[0], islands[i][1] - b[1]))
        da = math.hypot(islands[ia][0] - a[0], islands[ia][1] - a[1])
        db = math.hypot(islands[ib][0] - b[0], islands[ib][1] - b[1])
        if da > 0.5 or db > 0.5 or ia == ib:
            problems.append(('band end not at an island centre', a, b, da, db))
        bridges.append((ia, ib, o['object_type'], bezier_points(o)))
    # check every band has its matching grey fill drawn on top of it
    fill_keys = sorted((tuple(round(v, 1) for v in endpoints(o)[0]), tuple(round(v, 1) for v in endpoints(o)[1])) for o in fills)
    band_keys = sorted((tuple(round(v, 1) for v in endpoints(o)[0]), tuple(round(v, 1) for v in endpoints(o)[1])) for o in bands)
    if fill_keys != band_keys:
        problems.append(('band outlines and fills differ',))
    # band passes over a non-endpoint island?
    for ia, ib, kind, pts in bridges:
        for k, (x, y, r) in enumerate(islands):
            if k in (ia, ib):
                continue
            dmin = min(math.hypot(px - x, py - y) for px, py in pts)
            if dmin < r + 0.8 * CM:
                problems.append(('band touches another island', ia, ib, k, round(dmin, 1)))
    # group into towns (connected components)
    parent = list(range(len(islands)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for ia, ib, _, _ in bridges:
        parent[find(ia)] = find(ib)
    comps = {}
    for i in range(len(islands)):
        comps.setdefault(find(i), []).append(i)
    # labels: single-letter words whose centre is inside an island
    lab = {}
    for w in words:
        cx, cy = (w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2
        for k, (x, y, r) in enumerate(islands):
            if math.hypot(cx - x, cy - y) < r * 0.7:
                lab.setdefault(k, []).append(w['text'])
    rects = [o for o in objs if o['object_type'] == 'rect']
    towns = []
    for root, members in comps.items():
        xs = [islands[i][0] for i in members]
        ys = [islands[i][1] for i in members]
        bb = (min(xs), min(ys), max(xs), max(ys))
        t = {
            'islands': {i: (round(islands[i][0], 2), round(islands[i][1], 2)) for i in members},
            'labels': {i: ''.join(lab.get(i, [])) or None for i in members},
            'bridges': [(ia, ib, kind) for ia, ib, kind, _ in bridges if ia in members],
            'polylines': [(ia, ib, pts) for ia, ib, kind, pts in bridges if ia in members],
            'bbox': bb,
        }
        towns.append(t)
    towns.sort(key=lambda t: (round(t['bbox'][1] / 60), t['bbox'][0]))
    return towns, problems, rects, words


def town_graph(t):
    """Map a read town to (letters list, edge list of letter pairs). Unlabelled islands get
    names by reading order: top to bottom, left to right, as i1, i2, ..."""
    ids = sorted(t['islands'], key=lambda i: (round(t['islands'][i][1]), t['islands'][i][0]))
    name = {}
    for k, i in enumerate(ids):
        name[i] = t['labels'][i] or f'i{k + 1}'
    edges = [(name[a], name[b]) for a, b, _ in t['bridges']]
    pos = {name[i]: t['islands'][i] for i in ids}
    return [name[i] for i in ids], edges, pos


def read_strokes(key, pno, lw=1.4, tol=0.15):
    """Picture strokes: straight segments and circles of the given line width."""
    p, objs, words = page_objects(key, pno)
    segs, circles = [], []
    for o in objs:
        if abs((o.get('linewidth') or 0) - lw) > tol:
            continue
        c = circle_of(o) if o['object_type'] == 'curve' else None
        if c:
            circles.append(c)
            continue
        path = o.get('path')
        if o['object_type'] == 'rect':
            x0, y0, x1, y1 = o['x0'], o['top'], o['x1'], o['bottom']
            corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
            for k in range(4):
                segs.append((corners[k], corners[(k + 1) % 4]))
            continue
        pts = [cmd[-1] for cmd in path if cmd[0] in ('m', 'l')] if path else list(o['pts'])
        if path and any(cmd[0] == 'c' for cmd in path):
            raise ValueError('unexpected curved stroke')
        closed = path and path[-1][0] == 'h'
        for k in range(len(pts) - 1):
            segs.append((pts[k], pts[k + 1]))
        if closed:
            segs.append((pts[-1], pts[0]))
    return segs, circles, words
