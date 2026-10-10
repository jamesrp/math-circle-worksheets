"""Read every diagram in the delivered Week 57 student PDF (and the adult
guide's compact proof figure) back from the PDF content streams and check it
against the text and the guide's keys.

For each page: dot boards (count, rows x columns, 20 mm spacing in both axes),
every authored outline (vertices converted to lattice coordinates), dashed
seams, the counting panel's circle/box marks, and the shaded/white fills.
The read-back coordinates are then counted with lattice57 (I, B, area) and
compared with the records the guide prints.

Run: python3 check_diagrams.py   (writes out_check_diagrams.txt beside itself)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, HERE)
import lattice57 as L  # noqa: E402
import pdfgeom57 as G  # noqa: E402

ROOT = L.repo_root()
STUDENT = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-57', 'week-57-students.pdf')
GUIDE = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-57', 'week-57-facilitator.pdf')
STEP = 20 * G.MM
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def same_cycle(a, b):
    a, b = list(a), list(b)
    if len(a) != len(b):
        return False
    n = len(a)
    for seq in (b, b[::-1]):
        for r in range(n):
            if seq[r:] + seq[:r] == a:
                return True
    return False


def boards_of(page):
    out = []
    for g in G.cluster_boards(page['dots'], STEP):
        def levels(vals):
            vals = sorted(vals)
            groups = [[vals[0]]]
            for v in vals[1:]:
                if v - groups[-1][-1] < 1.0:
                    groups[-1].append(v)
                else:
                    groups.append([v])
            return [sum(gr) / len(gr) for gr in groups]
        xs = levels([p[0] for p in g])
        ys = levels([p[1] for p in g])
        x0, y0 = min(p[0] for p in g), min(p[1] for p in g)
        # spacing checks in both axes
        dx = [b - a for a, b in zip(xs, xs[1:])]
        dy = [b - a for a, b in zip(ys, ys[1:])]
        out.append(dict(dots=g, cols=len(xs), rows=len(ys), x0=x0, y0=y0,
                        dx=dx, dy=dy,
                        w_mm=(max(p[0] for p in g) - x0) / G.MM,
                        h_mm=(max(p[1] for p in g) - y0) / G.MM))
    # rows of boards (overlapping vertical ranges) top-to-bottom, then left-to-right
    out.sort(key=lambda b: -(b['y0'] + (b['rows'] - 1) * STEP))
    rows = []
    for b in out:
        top = b['y0'] + (b['rows'] - 1) * STEP
        if rows and top >= rows[-1][0]['y0'] - 1:
            rows[-1].append(b)
        else:
            rows.append([b])
    return [b for r in rows for b in sorted(r, key=lambda b: b['x0'])]


def to_lattice(b, p, tol=0.05):
    u = (p[0] - b['x0']) / STEP
    v = (p[1] - b['y0']) / STEP
    ru, rv = round(u), round(v)
    ok = abs(u - ru) < tol and abs(v - rv) < tol
    return (ru, rv), ok


def in_board(b, p):
    return (b['x0'] - 5 <= p[0] <= b['x0'] + (b['cols'] - 1) * STEP + 5 and
            b['y0'] - 5 <= p[1] <= b['y0'] + (b['rows'] - 1) * STEP + 5)


def outlines_on(page, b, rgb=(0.12, 0.16, 0.2)):
    res = []
    for s in page['strokes']:
        if s['rgb'] != rgb or not s['closed']:
            continue
        if all(in_board(b, p) for p in s['pts']):
            pts, oks = zip(*(to_lattice(b, p) for p in s['pts']))
            res.append((list(pts), all(oks)))
    return res


def seams_on(page, b):
    res = []
    for s in page['strokes']:
        if s['dash'] and all(in_board(b, p) for p in s['pts']):
            pts, oks = zip(*(to_lattice(b, p) for p in s['pts']))
            res.append((list(pts), all(oks)))
    return res


S = G.read(STUDENT)
check(len(S) == 10, 'student PDF has 10 pages (found %d)' % len(S))

# Expected content, typed from the guide's adult keys (pp. 4-9)
EXPECT = {
    1: [dict(dots=(3, 2), polys=[[(0, 0), (2, 0), (0, 1)]], rec=[(0, 4, '1')], name='panel input'),
        dict(dots=(3, 2), polys=[[(0, 0), (2, 0), (2, 1), (0, 1)]], seams=[[(2, 0), (0, 1)]],
             rec=[(0, 6, '2')], name='panel two copies joined'),
        dict(dots=(5, 5), polys=[[(0, 1), (3, 1), (3, 3), (0, 3)]], rec=[(2, 10, '6')], name='P1 rectangle'),
        dict(dots=(5, 5), polys=[[(0, 0), (2, 0), (3, 3), (1, 3)]], rec=[(4, 6, '6')], name='P1 slanted')],
    2: [dict(dots=(3, 3), polys=[[(0, 0), (2, 0), (2, 2), (0, 2)]], rec=[(1, 8, '4')], name='count input'),
        dict(dots=(3, 3), polys=[[(0, 0), (2, 0), (2, 2), (0, 2)]], rec=[(1, 8, '4')], name='count marked',
             marks=True),
        dict(dots=(5, 5), polys=[[(0, 0), (3, 0), (3, 1), (1, 1), (1, 3), (0, 3)]], rec=[(0, 12, '5')],
             name='P2 L-shape'),
        dict(dots=(5, 5), polys=[[(0, 0), (3, 0), (1, 3)]], rec=[(3, 5, '9/2')], name='P2 triangle')],
    3: [dict(dots=(5, 5), polys=[], name='P3 left board'), dict(dots=(5, 5), polys=[], name='P3 right board')],
    4: [dict(dots=(7, 7), polys=[], name='P4 board')],
    5: [dict(dots=(7, 7), polys=[], name='P5 board')],
    6: [dict(dots=(5, 4), polys=[[(0, 0), (4, 0), (4, 2), (0, 2)]], seams=[[(2, 0), (2, 2)]],
             rec=[(3, 12, '8')], name='P6 rectangle'),
        dict(dots=(5, 4), polys=[[(0, 0), (2, 0), (3, 3), (1, 3)]], seams=[[(0, 0), (3, 3)]],
             rec=[(4, 6, '6')], name='P6 slanted')],
    7: [dict(dots=(7, 7), polys=[], name='P7 board')],
    8: [dict(dots=(5, 4), polys=[[(0, 0), (4, 1), (1, 3)]], rec=[(5, 3, '11/2')], name='P8 triangle'),
        dict(dots=(5, 4), polys=[[(0, 0), (4, 0), (4, 3), (2, 2), (0, 3)]], rec=[(5, 12, '10')],
             name='P8 pentagon')],
    9: [dict(dots=(5, 5), polys=[[(0, 0), (4, 0), (4, 4), (0, 4)], [(1, 1), (3, 1), (3, 3), (1, 3)]],
             hole=True, rec=[(0, 24, '12')], name='P9 ring'),
        dict(dots=(7, 4), polys=[], name='P9 extra board')],
    10: [dict(dots=(7, 7), polys=[], name='P10 board')],
}

for pg in range(1, 11):
    page = S[pg - 1]
    bs = boards_of(page)
    exp = EXPECT[pg]
    check(len(bs) == len(exp), 'p.%d: %d dot boards (expected %d)' % (pg, len(bs), len(exp)))
    for b, e in zip(bs, exp):
        tag = 'p.%d %s' % (pg, e['name'])
        check((b['cols'], b['rows']) == e['dots'],
              '%s: %dx%d dots (expected %dx%d)' % (tag, b['cols'], b['rows'], *e['dots']))
        check(len(b['dots']) == e['dots'][0] * e['dots'][1], '%s: full rectangular dot set' % tag)
        if b['dx'] and b['dy']:
            sp = b['dx'] + b['dy']
            check(all(abs(d - STEP) < 0.05 for d in sp),
                  '%s: every dot interval is 20 mm in x and y (%.3f..%.3f mm)'
                  % (tag, min(sp) / G.MM, max(sp) / G.MM))
        say('     %s board size %.1f x %.1f mm' % (tag, b['w_mm'], b['h_mm']))
        found = outlines_on(page, b)
        check(len(found) == len(e['polys']), '%s: %d outline(s) drawn (expected %d)'
              % (tag, len(found), len(e['polys'])))
        for (pts, ok), want in zip(found, e['polys']):
            check(ok, '%s: every outline vertex sits on a dot' % tag)
            check(same_cycle(pts, want), '%s: outline %s matches guide %s' % (tag, pts, want))
            check(L.is_simple(pts), '%s: outline is a simple polygon with %d sides' % (tag, len(pts)))
        for (pts, ok), want in zip(seams_on(page, b), e.get('seams', [])):
            check(ok and sorted(pts) == sorted(want), '%s: dashed seam %s matches %s' % (tag, pts, want))
        check(len(seams_on(page, b)) == len(e.get('seams', [])), '%s: number of dashed seams' % tag)
        if e.get('rec'):
            polys = [p for p, _ in found]
            if e.get('hole'):
                outer, hole = polys
                I, B = L.counts(outer, [hole])
                A = L.area_cells(outer, [hole])
            else:
                I, B = L.counts(polys[0])
                A = L.area_cells(polys[0])
            want = e['rec'][0]
            check((I, B, str(A)) == want, '%s: read-back record (I,B,A)=(%d,%d,%s), guide %s'
                  % (tag, I, B, A, want))
        if e.get('marks'):
            poly = e['polys'][0]
            rings = [to_lattice(b, (r[0], r[1])) for r in page['rings'] if in_board(b, r)]
            ring_pts = sorted(p for p, ok in rings if ok)
            ins, bd = L.dot_sets(poly)
            check(ring_pts == bd, '%s: circles mark exactly the boundary dots %s' % (tag, bd))
            boxes = [s for s in page['strokes'] if s['closed'] and s['rgb'] == (0.0, 0.0, 0.0)
                     and len(s['pts']) == 4 and all(in_board(b, p) for p in s['pts'])]
            centres = []
            for s in boxes:
                cx = sum(p[0] for p in s['pts']) / 4
                cy = sum(p[1] for p in s['pts']) / 4
                centres.append(to_lattice(b, (cx, cy))[0])
            check(sorted(centres) == ins, '%s: boxes mark exactly the inside dots %s' % (tag, ins))
        if e.get('hole'):
            fills = [f for f in page['fills'] if all(in_board(b, p) for p in f['pts'])]
            greys = [f for f in fills if f['gray'] == 0.95]
            whites = [f for f in fills if f['gray'] == 1]
            check(len(greys) == 1 and len(whites) == 1,
                  '%s: one shaded outer fill and one white hole fill' % tag)
            if whites:
                wp = [to_lattice(b, p)[0] for p in whites[0]['pts']]
                check(same_cycle(wp, e['polys'][1]), '%s: white fill is exactly the hole %s' % (tag, wp))

# Guide p. 8 compact proof figure: A=(0,0), B=(2,1), C=(6,6), D=(2,6)
GD = G.read(GUIDE)
check(len(GD) == 10, 'guide PDF has 10 pages')
gp = GD[7]
step7 = 7 * G.MM
grp = G.cluster_boards(gp['dots'], step7, tol=0.3)
big = max(grp, key=len)
check(len(big) == 49, 'guide p.8 figure: 7x7 dots at 7 mm (found %d)' % len(big))
x0 = min(p[0] for p in big)
y0 = min(p[1] for p in big)
quad = None
dashed = []
for s in gp['strokes']:
    pts = [(round((p[0] - x0) / step7, 3), round((p[1] - y0) / step7, 3)) for p in s['pts']]
    if s['dash']:
        dashed.append(sorted(pts))
    elif s['closed'] and len(pts) == 4:
        quad = pts
check(quad is not None and same_cycle([(int(round(x)), int(round(y))) for x, y in quad],
                                      [(0, 0), (2, 1), (6, 6), (2, 6)]),
      'guide p.8 figure: outline is A(0,0) B(2,1) C(6,6) D(2,6): %s' % quad)
want_d = [sorted([(0.0, 0.0), (6.0, 6.0)]), sorted([(2.0, 1.0), (2.0, 6.0)])]
check(sorted(dashed) == sorted(want_d), 'guide p.8 figure: dashed diagonals AC and BD: %s' % dashed)

say('')
say('%d checks, %d failures' % (sum(1 for l in OUT if l.startswith(('ok', 'FAIL'))), len(FAIL)))
open(os.path.join(HERE, 'out_check_diagrams.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
sys.exit(1 if FAIL else 0)
