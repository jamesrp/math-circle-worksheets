"""Week 50 (staircases and lengths): read every diagram back from the delivered
PDFs and check it against the page text and the intended mathematics.

Reads (with pdfplumber) the current student PDFs for K-1, Grades 2-3, Grades
4-5 and the bonus packet, plus the two adult guides, from
lowell-math-circle-year-2/week-50/. It does not import or run any builder or
checker from the packet's sources.

For each page it reports, in millimetres measured from S (x right, y up):
  * the main rectangle size, the S and F dots and the dotted diagonal;
  * the 100 mm (or 30 mm) calibration bar;
  * every gray strip: its vertices, the signed vertical gap y - (3/4)x of each,
    and whether the polygon equals {|y - 3x/4| <= d} clipped to the rectangle;
  * every printed path: vertices, piece lengths, total length, leftward travel,
    greatest vertical gap from the diagonal and whether it stays in the strip;
  * the opening worked example: piece and bar lengths, and the distance from
    each "X: n" label to its own piece and to the nearest gray outline edge;
  * Grades 4-5 Problem 6: which drawn piece each printed number is nearest to;
  * bonus pages: dot grid size and spacing, strip half-width in units, unit bar;
  * the guide's eight-turn diagram: its route and strip in drawing units.
Run: python3 check_diagrams.py  (writes out_check_diagrams.txt beside itself)
"""
import math
import os
import sys
from fractions import Fraction

import pdfplumber

HERE = os.path.dirname(os.path.abspath(__file__))


def find_repo(start):
    d = start
    while True:
        if os.path.isfile(os.path.join(d, 'AGENTS.md')) and os.path.isdir(
                os.path.join(d, 'lowell-math-circle-year-2')):
            return d
        nd = os.path.dirname(d)
        if nd == d:
            raise SystemExit('repository not found above ' + start)
        d = nd


REPO = find_repo(HERE)
WEEK = os.path.join(REPO, 'lowell-math-circle-year-2', 'week-50')
MM = 25.4 / 72
OUT = []


def say(*a):
    s = ' '.join(str(x) for x in a)
    OUT.append(s)
    print(s)


def r(v, n=2):
    return round(v + 0.0, n)


def seg_point_dist(p, a, b):
    (px, py), (ax, ay), (bx, by) = p, a, b
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = 0 if L2 == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L2))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)


def gap(x, y):
    return y - 0.75 * x


def main_diagram(page):
    """Return (origin_x, origin_y_top) of S in PDF points, using the 160x120 rect."""
    for o in page.rects:
        w, h = (o['x1'] - o['x0']) * MM, (o['bottom'] - o['top']) * MM
        if abs(w - 160) < 1 and abs(h - 120) < 1:
            return o, (o['x0'], o['bottom'])
    return None, None


def to_mm(pt, S):
    return ((pt[0] - S[0]) * MM, (S[1] - pt[1]) * MM)


def expected_strip(d):
    return [(0, 0), (0, d), (160 - 4 * d / 3, 120), (160, 120), (160, 120 - d), (4 * d / 3, 0)]


def same_polygon(P, Q, tol=0.05):
    P = [p for i, p in enumerate(P) if i == 0 or math.dist(p, P[i - 1]) > tol]
    if len(P) > 1 and math.dist(P[0], P[-1]) < tol:
        P = P[:-1]
    if len(P) != len(Q):
        return False
    return all(any(math.dist(p, q) < tol for q in Q) for p in P)


def describe_path(V, strip_d=None):
    pieces = []
    for a, b in zip(V, V[1:]):
        dx, dy = b[0] - a[0], b[1] - a[1]
        if abs(dx) < 0.05 and abs(dy) < 0.05:
            continue
        if abs(dy) < 0.05:
            pieces.append(('R' if dx > 0 else 'L', abs(dx)))
        elif abs(dx) < 0.05:
            pieces.append(('U' if dy > 0 else 'D', abs(dy)))
        else:
            pieces.append(('?', math.hypot(dx, dy)))
    total = sum(p[1] for p in pieces)
    left = sum(p[1] for p in pieces if p[0] == 'L')
    g = max(abs(gap(*v)) for v in V)
    turns = sum(1 for p, q in zip(pieces, pieces[1:]) if p[0] != q[0])
    s = ', '.join(f'{k}{r(v, 1)}' for k, v in pieces)
    say(f'      pieces: {s}')
    say(f'      total {r(total, 2)} mm, leftward {r(left, 2)} mm, turns {turns}, '
        f'greatest |vertical gap| {r(g, 2)} mm (at vertices; gap is linear on pieces)')
    if strip_d is not None:
        bad = [tuple(r(c, 1) for c in v) for v in V if abs(gap(*v)) > strip_d + 0.05]
        say(f'      inside the +-{strip_d} mm strip? {"yes" if not bad else "no; vertices outside: " + str(bad)}')
    return pieces, total, left, g


def check_main_page(name, pn, page):
    rect, S = main_diagram(page)
    say(f'  p.{pn}:')
    words = page.extract_words()
    if rect is None:
        say('    no 160x120 rectangle on this page')
        return None
    w, h = (rect['x1'] - rect['x0']) * MM, (rect['bottom'] - rect['top']) * MM
    say(f'    rectangle {r(w, 3)} x {r(h, 3)} mm (equal scale: 1 PDF unit = {r(MM, 5)} mm both axes)')
    dots = [o for o in page.curves if o.get('fill') and 2 < (o['x1'] - o['x0']) * MM < 3.5]
    dpos = sorted(to_mm(((o['x0'] + o['x1']) / 2, (o['top'] + o['bottom']) / 2), S) for o in dots)
    say(f'    dots at {[tuple(r(c, 2) for c in p) for p in dpos]} (S expected (0,0), F (160,120))')
    for o in page.lines:
        if o.get('dash') and o['dash'][0] and (o['x1'] - o['x0']) * MM > 100:
            a, b = to_mm(o['pts'][0], S), to_mm(o['pts'][1], S)
            say(f'    dotted diagonal {tuple(r(c, 2) for c in a)} -> {tuple(r(c, 2) for c in b)}, '
                f'length {r(math.dist(a, b), 2)} mm')
    for o in page.lines:
        L = (o['x1'] - o['x0']) * MM
        if abs(o['top'] - o['bottom']) < 0.01 and 99 < L < 101 and o['top'] > rect['bottom']:
            say(f'    calibration bar {r(L, 3)} mm')
    strip_d = None
    for o in page.curves:
        if o.get('fill') and not o.get('stroke') and (o['x1'] - o['x0']) * MM > 100:
            V = [to_mm(p, S) for p in o['pts']]
            gaps = sorted(set(r(gap(*v), 2) for v in V))
            say(f'    gray strip vertices {[tuple(r(c, 2) for c in v) for v in V[:-1]]}')
            say(f'      vertex gaps y-3x/4: {gaps}')
            for d in (15, 8):
                if same_polygon(V, expected_strip(d)):
                    strip_d = d
                    say(f'      = strip |y-3x/4| <= {d} mm clipped by the rectangle: yes')
            if strip_d is None:
                say('      matches neither the 15 mm nor the 8 mm clipped strip!')
    paths = []
    for o in page.curves:
        if o.get('stroke') and not o.get('fill') and (o['x1'] - o['x0']) * MM > 50:
            V = [to_mm(p, S) for p in o['pts']]
            dash = 'dashed' if o.get('dash') and o['dash'][0] else 'solid'
            say(f'    printed {dash} path, line width {r(o["linewidth"], 2)} pt, vertices '
                f'{[tuple(r(c, 2) for c in v) for v in V]}')
            paths.append((V, describe_path(V, strip_d)))
    text = ' '.join(w['text'] for w in words)
    return dict(rect=rect, S=S, words=words, paths=paths, strip=strip_d, text=text)


def check_example(page):
    """Opening worked example (identical on all three base bands)."""
    blacks = [o for o in page.lines if (o['x1'] - o['x0']) * MM < 50 and o['linewidth'] > 0.9]
    outline = [o for o in page.rects if not o.get('fill') and (o['x1'] - o['x0']) * MM < 50]
    bars = [o for o in page.rects if o.get('fill')]
    ol = outline[0]
    S = (ol['x0'], ol['bottom'])
    say(f'    gray outline {r((ol["x1"] - ol["x0"]) * MM, 2)} x {r((ol["bottom"] - ol["top"]) * MM, 2)} mm')
    pieces = []
    for o in blacks:
        a, b = to_mm(o['pts'][0], S), to_mm(o['pts'][1], S)
        pieces.append((a, b))
        say(f'    black piece {tuple(r(c, 1) for c in a)} -> {tuple(r(c, 1) for c in b)}: '
            f'{r(math.dist(a, b), 2)} mm')
    for o in bars:
        say(f'    bar cell {r((o["x1"] - o["x0"]) * MM, 2)} mm wide at x={r((o["x0"] - S[0]) * MM, 1)}')
    W, Hh = (ol['x1'] - ol['x0']) * MM, (ol['bottom'] - ol['top']) * MM
    edges = {'outline bottom (40 mm)': ((0, 0), (W, 0)), 'outline left (30 mm)': ((0, 0), (0, Hh)),
             'outline top (40 mm)': ((0, Hh), (W, Hh)), 'outline right (30 mm)': ((W, 0), (W, Hh))}
    words = page.extract_words()
    for i, w in enumerate(words):
        if w['text'] in ('A:', 'B:', 'C:', 'D:') and w['top'] < 250:
            num = words[i + 1]
            cx = ((w['x0'] + num['x1']) / 2 - S[0]) * MM
            cy = (S[1] - (w['top'] + w['bottom']) / 2) * MM
            x0, x1 = (w['x0'] - S[0]) * MM, (num['x1'] - S[0]) * MM
            dpiece = sorted((r(seg_point_dist((cx, cy), a, b), 1), f'{r(math.dist(a, b), 0)} mm piece')
                            for a, b in pieces)
            dedge = sorted((r(seg_point_dist((cx, cy), a, b), 1), k) for k, (a, b) in edges.items()
                           if math.dist(a, b) > 0)
            say(f'    label "{w["text"]} {num["text"]}" spans x {r(x0, 1)}..{r(x1, 1)}, centre '
                f'({r(cx, 1)},{r(cy, 1)}); nearest black pieces {dpiece[:2]}; nearest outline edges {dedge[:2]}')
            if w['text'] == 'C:':
                # proposed fix: draw the label at make.py (31,46) instead of (17,45),
                # i.e. 14 mm right and 1 mm lower, inside the outline to the right of C
                px, py = cx + 14, cy - 1
                half = (x1 - x0) / 2
                dpiece = sorted((r(seg_point_dist((px, py), a, b), 1), f'{r(math.dist(a, b), 0)} mm piece')
                                for a, b in pieces)
                dedge = sorted((r(seg_point_dist((px, py), a, b), 1), k) for k, (a, b) in edges.items())
                say(f'      proposed "C: 20" centre ({r(px, 1)},{r(py, 1)}), text x {r(px - half, 1)}..{r(px + half, 1)}: '
                    f'nearest black pieces {dpiece[:2]}; nearest outline edges {dedge[:2]}')


def check_p6_labels(info):
    V = info['paths'][0][0]
    S = info['S']
    segs = [(V[i], V[i + 1]) for i in range(len(V) - 1)]
    for w in info['words']:
        if w['text'].isdigit() and w.get('upright', True) and w['top'] < info['rect']['bottom'] and w['top'] > info['rect']['top'] - 10:
            c = to_mm(((w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2), S)
            ds = sorted((seg_point_dist(c, a, b), i) for i, (a, b) in enumerate(segs))
            (d0, i0), (d1, i1) = ds[0], ds[1]
            a, b = segs[i0]
            L = math.dist(a, b)
            dg = abs(gap(*c)) * 0.8  # perpendicular distance to the diagonal
            say(f'    label "{w["text"]}" at ({r(c[0], 1)},{r(c[1], 1)}): nearest piece #{i0 + 1} '
                f'{tuple(r(t, 0) for t in a)}->{tuple(r(t, 0) for t in b)} (length {r(L, 1)}) at {r(d0, 1)} mm; '
                f'next piece #{i1 + 1} at {r(d1, 1)} mm; dotted diagonal at {r(dg, 1)} mm; '
                f'{"MATCH" if abs(L - int(w["text"])) < 0.3 else "MISMATCH"}')


def bonus(pdfpath):
    pdf = pdfplumber.open(pdfpath)
    for pn, page in enumerate(pdf.pages, 1):
        say(f'  p.{pn}:')
        dots = [((o['x0'] + o['x1']) / 2, (o['top'] + o['bottom']) / 2) for o in page.curves
                if o.get('fill') and (o['x1'] - o['x0']) < 7]
        if pn in (1, 2):
            big = [d for d in dots if not (d[1] > 130 and d[1] < 200)] if pn == 1 else dots
            xs = sorted(set(round(d[0], 2) for d in big))
            ys = sorted(set(round(d[1], 2) for d in big))
            sx = [r(b - a, 2) for a, b in zip(xs, xs[1:])]
            sy = [r(b - a, 2) for a, b in zip(ys, ys[1:])]
            say(f'    route grid dots: {len(big)} = {len(xs)} columns x {len(ys)} rows; '
                f'spacing x {sx} pt, y {sy} pt ({r(sx[0] * MM, 2)} mm)')
            say(f'    so S->F needs {len(xs) - 1} right and {len(ys) - 1} up steps')
            ws = page.extract_words()
            for t in ('S', 'F'):
                # the endpoint label is the lone "S"/"F" word closest to a grid dot
                cands = [((w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2) for w in ws if w['text'] == t]
                c = min(cands, key=lambda c: min(math.dist(d, c) for d in big))
                near = min(big, key=lambda d: math.dist(d, c))
                say(f'    label {t} nearest dot at column {xs.index(round(near[0], 2))}, '
                    f'row-from-bottom {len(ys) - 1 - ys.index(round(near[1], 2))}, {r(math.dist(near, c) * MM, 1)} mm away')
        if pn == 3:
            grid = [o for o in page.lines if abs(o['x0'] - o['x1']) < 0.01 and (o['bottom'] - o['top']) > 300]
            xs = sorted(o['x0'] for o in grid)
            unit = (xs[1] - xs[0])
            say(f'    grid: {len(xs)} vertical lines, unit {r(unit, 3)} pt = {r(unit * MM, 3)} mm; '
                f'square side {r((xs[-1] - xs[0]) * MM, 2)} mm')
            bar = [o for o in page.lines if abs(o['top'] - o['bottom']) < 0.01 and o['top'] > 680 and
                   (o['x1'] - o['x0']) > 50]
            for o in bar:
                say(f'    unit bar {r((o["x1"] - o["x0"]) * MM, 3)} mm')
            S = (xs[0], max(o['bottom'] for o in grid))
            poly = [o for o in page.curves if (o['x1'] - o['x0']) > 300][0]
            V = [((p[0] - S[0]) / unit, (S[1] - p[1]) / unit) for p in poly['pts']]
            say(f'    strip vertices (units) {[tuple(r(c, 3) for c in v) for v in V[:-1]]}')
            say(f'    vertex gaps y-x: {sorted(set(r(v[1] - v[0], 3) for v in V))}')
            exp = [(0, 0), (0.25, 0), (4, 3.75), (4, 4), (3.75, 4), (0, 0.25)]
            say(f'    equals |y-x| <= 1/4 clipped by the 4x4 square: {same_polygon(V, exp, 0.002)}')
            dots = [((o['x0'] + o['x1']) / 2, (o['top'] + o['bottom']) / 2) for o in page.curves
                    if o.get('fill') and (o['x1'] - o['x0']) < 7]
            say(f'    S/F dots (units): {[tuple(r(c, 3) for c in ((d[0] - S[0]) / unit, (S[1] - d[1]) / unit)) for d in dots]}')
            diag = [o for o in page.lines if abs((o['x1'] - o['x0']) - (o['bottom'] - o['top'])) < 0.1 and (o['x1'] - o['x0']) > 300]
            for o in diag:
                say(f'    diagonal from ({r((o["x0"] - S[0]) / unit, 3)},0) to ({r((o["x1"] - S[0]) / unit, 3)},'
                    f'{r((S[1] - o["top"]) / unit, 3)})')


def guide_diagram(pdfpath):
    pdf = pdfplumber.open(pdfpath)
    page = pdf.pages[1]
    rect = page.rects[0]
    sx = (rect['x1'] - rect['x0']) / 160
    sy = (rect['bottom'] - rect['top']) / 120
    say(f'  guide p.2 diagram: scale x {r(sx, 4)} pt/mm, y {r(sy, 4)} pt/mm (equal: {abs(sx - sy) < 1e-3})')
    S = (rect['x0'], rect['bottom'])
    route = [o for o in page.lines if o['linewidth'] > 1]
    V = [((route[0]['pts'][0][0] - S[0]) / sx, (S[1] - route[0]['pts'][0][1]) / sy)]
    for o in route:
        V.append(((o['pts'][1][0] - S[0]) / sx, (S[1] - o['pts'][1][1]) / sy))
    say(f'    route {[tuple(r(c, 1) for c in v) for v in V]}')
    witness = [(0, 0), (20, 0), (20, 30), (60, 30), (60, 60), (100, 60), (100, 90), (140, 90), (140, 120), (160, 120)]
    say(f'    equals the printed eight-turn witness: {all(math.dist(a, b) < 0.1 for a, b in zip(V, witness)) and len(V) == len(witness)}')
    poly = page.curves[0]
    P = [((p[0] - S[0]) / sx, (S[1] - p[1]) / sy) for p in poly['pts']]
    say(f'    strip = |y-3x/4| <= 15 clipped: {same_polygon(P, expected_strip(15), 0.1)}')
    describe_path(V, 15)


def main():
    for band, fn in [('K-1', 'week-50-k-1.pdf'), ('Grades 2-3', 'week-50-grades-2-3.pdf'),
                     ('Grades 4-5', 'week-50-grades-4-5.pdf')]:
        say(f'=== {band}: {fn}')
        pdf = pdfplumber.open(os.path.join(WEEK, fn))
        for pn, page in enumerate(pdf.pages, 1):
            info = check_main_page(band, pn, page)
            if pn == 1:
                say('    opening worked example:')
                check_example(page)
            if band == 'Grades 4-5' and pn == 6:
                say('    Problem 6 length labels:')
                check_p6_labels(info)
    say('=== Bonus: week-50-bonus.pdf')
    bonus(os.path.join(WEEK, 'week-50-bonus.pdf'))
    say('=== Base adult guide: week-50-facilitator.pdf')
    guide_diagram(os.path.join(WEEK, 'week-50-facilitator.pdf'))
    with open(os.path.join(HERE, 'out_check_diagrams.txt'), 'w') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
