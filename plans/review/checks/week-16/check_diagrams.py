"""Read every diagram in the delivered Week 16 base PDFs back from their
content streams and check it against the mathematics.

Student PDFs (K-1, Grades 2-3, Grades 4-5): for every board, the dots and
lines are matched to a lattice board of side 2, 3 or 4 or to the fan board
(exact bijection of dots, exact edge set, no extra or missing line), the
triangle is checked to be equilateral with equal x/y scaling, printed letters
are read at their dots, side-rule labels are located on the correct side, the
star is located under the right dot, the Problem 3 local triangles and the
Problem 4 rows are measured, and the door example is checked.
Adult guide: every board figure is read the same way, together with its
letters, cell numbers, shaded cells and door bars, and compared with the
mathematics and with the row codes the guide prints.
Run: python3 check_diagrams.py   (writes out_check_diagrams.txt beside itself)
"""
import collections
import itertools
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfgeom16 as G  # noqa: E402
from sperner16 import lattice, fan2, row_code  # noqa: E402

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


BOARDS = {'side2': lattice(2), 'side3': lattice(3), 'side4': lattice(4), 'fan': fan2()}


def fit(dots, segs, tol=0.6):
    """Match dot centres to one of the candidate boards.  Returns
    (name, board, vertex->centre, scale) or None."""
    if len(dots) < 3:
        return None
    ys = sorted(d[1] for d in dots)
    bottom = [d for d in dots if abs(d[1] - ys[0]) < tol]
    top = [d for d in dots if abs(d[1] - ys[-1]) < tol]
    if len(top) != 1 or len(bottom) < 2:
        return None
    R = min(bottom)
    B = max(bottom)
    side = B[0] - R[0]
    for name, b in BOARDS.items():
        if len(b.xy) != len(dots):
            continue
        place = {v: (R[0] + x * side, R[1] + y * side) for v, (x, y) in b.xy.items()}
        match = {}
        for v, p in place.items():
            near = [d for d in dots if dist(d, p) < tol]
            if len(near) != 1:
                break
            match[v] = near[0]
        else:
            if len(set(match.values())) == len(dots):
                return name, b, match, side
    return None


def edge_set_ok(b, match, segs, tol=0.6):
    """Every board edge drawn, and every drawn segment is a board edge."""
    inv = {}
    for v, p in match.items():
        inv[p] = v

    def at(p):
        near = [q for q in match.values() if dist(p, q) < tol]
        return inv[near[0]] if len(near) == 1 else None
    drawn = set()
    extra = []
    for a, c, path in segs:
        va, vc = at(a), at(c)
        if va is None or vc is None or va == vc:
            extra.append((a, c))
        else:
            drawn.add(frozenset((va, vc)))
    want = set(b.edge_cells)
    return drawn == want and not extra, len(drawn), len(want), extra


def letters_at(words, match, radius, allowed='RBY'):
    lab = {}
    for w, x, y, ww, hh in words:
        if len(w) == 1 and w in allowed:
            near = [v for v, p in match.items() if dist((x, y), p) < radius]
            if len(near) == 1:
                lab[near[0]] = w
    return lab


def equilateral(match, b, tol=0.05):
    R, B, Y = (match[b.corners[k]] for k in 'RBY')
    s1, s2, s3 = dist(R, B), dist(B, Y), dist(Y, R)
    return abs(s1 - s2) < tol and abs(s1 - s3) < tol and abs(R[1] - B[1]) < tol, (s1, s2, s3)


# ====================================================================== students
EXPECT = {
    # (band, page): (board, printed letters as row code with '.' for blank or None, kind)
    ('K-1', 1): ('side2', None), ('K-1', 2): ('side3', None), ('K-1', 3): ('side3', None),
    ('K-1', 4): ('fan', {(0, 0): 'R', (1, 0): 'R', (2, 0): 'B', (0, 1): 'Y', (1, 1): 'B', (0, 2): 'Y'}),
    ('K-1', 5): ('side4', None), ('K-1', 6): ('side3', None),
    ('2-3', 1): ('side3', None), ('2-3', 2): ('side3', None), ('2-3', 3): ('side3', 'RBRB/RRB/RB/Y'),
    ('2-3', 6): ('side4', None), ('2-3', 7): ('fan', None),
    ('4-5', 1): ('side3', None), ('4-5', 2): ('side3', None), ('4-5', 3): ('side4', 'RRBRB/YBRB/RBB/RB/Y'),
    ('4-5', 6): ('fan', None), ('4-5', 7): ('side4', None),
}
BOTTOM_LABEL = {('K-1', 6): 'R or B or Y', ('4-5', 7): 'R or B, except'}

for band in ('K-1', '2-3', '4-5'):
    pdf = G.PDFFile(G.PDF[band])
    npg = len(pdf.pages)
    say('== %s: %d pages' % (band, npg))
    for pg in range(1, npg + 1):
        pl = G.paths(pdf, pg)
        circ = G.circles(pl, rmin=4, rmax=14)
        segs = [s for s in G.segments(pl) if abs(s[2].lw - 0.8) < 0.05]
        words = G.words(G.PDF[band], pg)
        key = (band, pg)
        if key in EXPECT:
            want_board, want_lab = EXPECT[key]
            dots = [(c[0], c[1]) for c in circ]
            f = fit(dots, segs)
            if f is None:
                check(False, '%s p.%d: dots do not fit any board' % key)
                continue
            name, b, match, side = f
            check(name == want_board, '%s p.%d: board is %s (%d dots), side %.2f pt = %.4f in' % (band, pg, name, len(match), side, side / 72))
            ok, nd, nw, extra = edge_set_ok(b, match, segs)
            check(ok, '%s p.%d: drawn lines are exactly the %d board edges (drawn %d, extra %d)' % (band, pg, nw, nd, len(extra)))
            eq, sides = equilateral(match, b)
            check(eq, '%s p.%d: big triangle equilateral with equal x/y scale, sides %.3f %.3f %.3f pt' % ((band, pg) + sides))
            radii = {v: [c[2] for c in circ if (c[0], c[1]) == p][0] for v, p in match.items()}
            lab = letters_at(words, match, 9)
            exp = {b.corners[k]: k for k in 'RBY'}
            if isinstance(want_lab, str):
                rows = want_lab.split('/')
                exp = {(i, j): ch for j, r in enumerate(rows) for i, ch in enumerate(r)}
            elif isinstance(want_lab, dict):
                exp = dict(want_lab)
            check(lab == exp, '%s p.%d: printed letters %s' % (band, pg, row_code(b.n, lab) if hasattr(b, 'n') and len(lab) == len(b.xy) else sorted(lab.items(), key=str)))
            # fill colour of lettered dots matches the letter, blank dots white
            col = {'R': (0.984, 0.890, 0.882), 'B': (0.875, 0.922, 0.984), 'Y': (1.0, 0.969, 0.796)}
            fills_ok = True
            for v, p in match.items():
                cpath = [c[3] for c in circ if (c[0], c[1]) == p][0]
                want_col = col.get(lab.get(v), (1.0, 1.0, 1.0))
                if max(abs(a - bb) for a, bb in zip(cpath.fill, want_col)) > 0.01:
                    fills_ok = False
            check(fills_ok, '%s p.%d: lettered dots tinted by letter, blank dots white' % key)
            if band == 'K-1':
                spac = min(dist(match[a], match[c]) for e in b.edge_cells for a, c in [tuple(e)])
                say('     tightest dot spacing on this board %.4f in; blank dot diameter %.3f in' %
                    (spac / 72, 2 * min(radii.values()) / 72))
            # side-rule labels: rotated words give fragments; locate them
            R, Bc, Y = (match[b.corners[k]] for k in 'RBY')
            midL = ((R[0] + Y[0]) / 2, (R[1] + Y[1]) / 2)
            midR = ((Bc[0] + Y[0]) / 2, (Bc[1] + Y[1]) / 2)
            fr = [w for w in words if w[0] in ('Ro', 'rY', 'Bo', 'B', 'or', 'Y', 'R')
                  and not any(dist((w[1], w[2]), p) < 12 for p in match.values())]
            leftw = [w for w in fr if dist((w[1], w[2]), midL) < 45 and w[1] < midL[0]]
            rightw = [w for w in fr if dist((w[1], w[2]), midR) < 45 and w[1] > midR[0]]
            lt = ''.join(sorted(''.join(w[0] for w in leftw)))
            rt = ''.join(sorted(''.join(w[0] for w in rightw)))
            check(lt == ''.join(sorted('RorY')) and rt == ''.join(sorted('BorY')),
                  '%s p.%d: "R or Y" outside the left side, "B or Y" outside the right side' % key)
            below = sorted([w for w in words if R[1] - 45 < w[2] < R[1] - 5 and R[0] < w[1] < Bc[0]], key=lambda w: w[1])
            bt = ' '.join(w[0] for w in below if w[0] != '∗' or w[2] < R[1] - 25)
            wantb = BOTTOM_LABEL.get(key, 'R or B')
            check(bt.startswith(wantb), '%s p.%d: bottom label "%s"' % (band, pg, bt))
            if key == ('4-5', 7):
                stars = [w for w in words if w[0] == '∗' and abs(w[2] - R[1]) < 25]
                near = [v for v, p in match.items() if stars and abs(p[0] - stars[0][1]) < 1 and stars[0][2] < p[1]]
                check(len(stars) == 1 and near and min(near, key=lambda v: abs(match[v][1] - stars[0][2])) == (2, 0),
                      '4-5 p.7: the star sits directly under bottom dot (2,0), the middle of five')
            if name == 'fan':
                # inserted dots at centroids of the four side-2 cells
                cent_ok = True
                for nm, c in b.original.items():
                    cx = sum(match[v][0] for v in c) / 3
                    cy = sum(match[v][1] for v in c) / 3
                    if dist((cx, cy), match[nm]) > 0.3:
                        cent_ok = False
                check(cent_ok, '%s p.%d: the four inserted dots sit at the centroids of the four side-2 cells' % key)
        elif band != 'K-1' and pg in (4,) or (band == '2-3' and pg == 4):
            # local triangles
            tri = [s for s in G.segments(pl) if abs(s[2].lw - 0.8) < 0.05]
            dots = [(c[0], c[1]) for c in circ]
            closed = [p for p in pl if p.stroked and any(cl for _, cu, cl in p.subpaths if not cu)]
            tris = []
            for p in closed:
                for pts, cu, cl in p.subpaths:
                    if not cu and cl and len(pts) in (3, 4):
                        q = pts[:3]
                        tris.append(q)
            okt = len(tris) == 12
            for q in tris:
                s = [dist(q[0], q[1]), dist(q[1], q[2]), dist(q[2], q[0])]
                if max(s) - min(s) > 0.05:
                    okt = False
                if sum(1 for v in q if any(dist(v, d) < 0.3 for d in dots)) != 3:
                    okt = False
            check(okt and len(dots) == 36, '%s p.%d (Problem 3): 12 equilateral triangles, side %.3f in, a dot at each of 36 corners' %
                  (band, pg, dist(tris[0][0], tris[0][1]) / 72 if tris else 0))
        elif pg == 5:
            dots = sorted(circ, key=lambda c: (-c[1], c[0]))
            rows = collections.defaultdict(list)
            for c in dots:
                rows[round(c[1], 1)].append(c)
            rowlist = [sorted(rows[y], key=lambda c: c[0]) for y in sorted(rows, reverse=True)]
            lab_words = [w for w in words if w[0] in ('R', 'B')]
            desc = []
            okr = True
            for r in rowlist:
                xs = [c[0] for c in r]
                gaps = [b_ - a for a, b_ in zip(xs, xs[1:])]
                if max(gaps) - min(gaps) > 0.05:
                    okr = False
                ends = []
                for c in (r[0], r[-1]):
                    near = [w[0] for w in lab_words if dist((w[1], w[2]), (c[0], c[1])) < 9]
                    ends.append(near[0] if near else '?')
                inner_white = all(max(abs(1 - t) for t in c[3].fill) < 0.01 for c in r[1:-1])
                okr = okr and inner_white
                desc.append('%s%s:%d edges' % (ends[0], ends[1], len(r) - 1))
            want = {'2-3': ['RB:2 edges', 'RB:3 edges', 'RB:4 edges', 'RB:5 edges', 'RB:6 edges'],
                    '4-5': ['RB:3 edges', 'RR:4 edges', 'RB:5 edges', 'RR:6 edges', 'RB:7 edges']}[band]
            check(okr and desc == want, '%s p.5 (Problem 4) rows, top to bottom: %s; dots equally spaced' % (band, desc))
        else:
            say('     %s p.%d: no board expected; %d dots' % (band, pg, len(circ)))
        # door example (2-3 p.3, 4-5 p.3)
        if pg == 3 and band != 'K-1':
            thick = [s for s in G.segments(pl) if s[2].lw > 2.5]
            thin = [s for s in G.segments(pl) if 0.3 < s[2].lw < 0.5 and not s[2].filled]
            # the example triangle: three thin segments forming a closed triangle
            tri_pts = None
            for p in pl:
                for pts, cu, cl in p.subpaths:
                    if cl and not cu and len(pts) == 3 and p.stroked and abs(p.lw - 0.4) < 0.05:
                        tri_pts = pts
            check(tri_pts is not None and len(thick) == 2, '%s p.3: door example triangle found with two thick door bars' % band)
            if tri_pts:
                labs = {}
                for v in tri_pts:
                    near = sorted([w for w in words if w[0] in 'RBY' and len(w[0]) == 1], key=lambda w: dist((w[1], w[2]), v))
                    labs[v] = near[0][0]
                on = []
                for a, c, _ in thick:
                    for e in itertools.combinations(tri_pts, 2):
                        p0, p1 = e
                        L = dist(p0, p1)
                        dd = [abs((p1[0] - p0[0]) * (q[1] - p0[1]) - (p1[1] - p0[1]) * (q[0] - p0[0])) / L for q in (a, c)]
                        if max(dd) < 0.3:
                            on.append(''.join(sorted(labs[p0] + labs[p1])))
                rb_edges = sorted(''.join(sorted(labs[p] + labs[q])) for p, q in itertools.combinations(tri_pts, 2) if {labs[p], labs[q]} == {'R', 'B'})
                check(sorted(on) == rb_edges == ['BR', 'BR'], '%s p.3: example labels %s; thick bars lie on exactly its two R-B edges' %
                      (band, ''.join(sorted(labs.values()))))
                s = sorted(dist(p, q) for p, q in itertools.combinations(tri_pts, 2))
                say('     %s p.3: example triangle side lengths %.1f, %.1f, %.1f pt (not equilateral: %s)' %
                    (band, s[0], s[1], s[2], abs(s[0] - s[2]) > 1))

# ====================================================================== guide
say('')
say('== Adult guide figures')
gpdf = G.PDFFile(G.PDF['guide'])
SHADE = (0.929, 0.941, 0.945)
DOORC = (0.133, 0.357, 0.478)


def figures_on(pg):
    pl = G.paths(gpdf, pg)
    circ = G.circles(pl, rmin=3, rmax=8)
    segs = [s for s in G.segments(pl) if abs(s[2].lw - 0.7) < 0.05 and max(abs(a - b) for a, b in zip(s[2].stroke, (0, 0, 0))) < 0.01]
    bars = [s for s in G.segments(pl) if abs(s[2].lw - 2.5) < 0.05]
    shades = []
    for p in pl:
        if p.filled and not p.stroked and max(abs(a - b) for a, b in zip(p.fill, SHADE)) < 0.01:
            for pts, cu, cl in p.subpaths:
                shades.append(pts)
    words = G.words(G.PDF['guide'], pg)
    dots = [(c[0], c[1]) for c in circ]
    # components of dots joined by black segments
    parent = {d: d for d in dots}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, c, _ in segs:
        da = [d for d in dots if dist(d, a) < 0.6]
        dc = [d for d in dots if dist(d, c) < 0.6]
        if da and dc:
            parent[find(da[0])] = find(dc[0])
    groups = collections.defaultdict(list)
    for d in dots:
        groups[find(d)].append(d)
    figs = []
    for g in groups.values():
        f = fit(g, segs)
        if f is None:
            say('     guide p.%d: a group of %d dots fits no board' % (pg, len(g)))
            continue
        name, b, match, side = f
        mysegs = [s for s in segs if any(dist(s[0], d) < 0.6 for d in g)]
        ok, nd, nw, extra = edge_set_ok(b, match, mysegs)
        rad = [c[2] for c in circ if (c[0], c[1]) in g][0]
        lab = letters_at(words, match, rad + 1.5)
        # cell numbers
        nums = {}
        for w, x, y, ww, hh in words:
            if w.isdigit():
                for k, c in enumerate(b.cells):
                    cx = sum(match[v][0] for v in c) / 3
                    cy = sum(match[v][1] for v in c) / 3
                    if dist((x, y), (cx, cy)) < 4:
                        nums[k] = int(w)
        sh = set()
        for pts in shades:
            cx = sum(p[0] for p in pts) / len(pts)
            cy = sum(p[1] for p in pts) / len(pts)
            for k, c in enumerate(b.cells):
                if dist((cx, cy), (sum(match[v][0] for v in c) / 3, sum(match[v][1] for v in c) / 3)) < 1 and len(pts) == 3:
                    sh.add(k)
        dr = set()
        for a, c, p in bars:
            mid = ((a[0] + c[0]) / 2, (a[1] + c[1]) / 2)
            for e in b.edge_cells:
                u, v = tuple(e)
                if dist(mid, ((match[u][0] + match[v][0]) / 2, (match[u][1] + match[v][1]) / 2)) < 0.8:
                    dr.add(e)
        cx0 = min(p[0] for p in match.values())
        cy0 = max(p[1] for p in match.values())
        figs.append(dict(name=name, b=b, match=match, side=side, edges_ok=ok, lab=lab, nums=nums, shaded=sh,
                         bars=dr, nbars=len(bars), eq=equilateral(match, b)[0], x=cx0, ytop=cy0))
    figs.sort(key=lambda f: (-round(f['ytop'] / 40), f['x']))
    return figs


def code_of(f):
    b = f['b']
    if f['name'] == 'fan':
        base = '/'.join(''.join(f['lab'].get((i, j), '.') for i in range(3 - j)) for j in range(3))
        return base + ' centres ' + ''.join(f['lab'].get(k, '.') for k in ('lowerleft', 'central', 'lowerright', 'top'))
    return '/'.join(''.join(f['lab'].get((i, j), '.') for i in range(b.n + 1 - j)) for j in range(b.n + 1))


def report(pg, f, want_code=None, want_shaded=None, numbering=True, doors=False):
    b = f['b']
    code = code_of(f)
    check(f['edges_ok'] and f['eq'], 'guide p.%d %s figure: edges exact, equilateral' % (pg, f['name']))
    if want_code is not None:
        check(code == want_code, 'guide p.%d: figure letters read %s (expected %s)' % (pg, code, want_code))
    if len(f['lab']) == len(b.xy):
        rb = set(b.rainbow(f['lab']))
        check(f['shaded'] == rb, 'guide p.%d %s: shaded cells are exactly the all-three cells (%d)' % (pg, code, len(rb)))
        if want_shaded is not None:
            check(len(rb) == want_shaded, 'guide p.%d %s: %d all-three cells (expected %d)' % (pg, code, len(rb), want_shaded))
        if doors:
            dd = set(b.doors(f['lab']))
            check(f['bars'] == dd and f['nbars'] == len(dd), 'guide p.%d: %d door bars, exactly on the %d R-B edges' % (pg, f['nbars'], len(dd)))
    if numbering and f['nums']:
        if f['name'] == 'fan':
            say('     guide p.%d fan numbering (number: region, corner letters): %s' %
                (pg, ', '.join('%d:%s' % (f['nums'][k], b.region[b.cells[k]]) for k in sorted(f['nums'], key=lambda k: f['nums'][k]))))
        else:
            check(all(f['nums'][k] == k + 1 for k in f['nums']) and len(f['nums']) == len(b.cells),
                  'guide p.%d: cell numbers follow strip-by-strip, left-to-right order (%d numbers)' % (pg, len(f['nums'])))
    return code


# p.3: K-1 P1 four witnesses
figs = figures_on(3)
check(len(figs) == 4, 'guide p.3: four side-2 figures')
for k, f in enumerate(figs, 1):
    code = report(3, f)
    rb = [c + 1 for c in f['b'].rainbow(f['lab'])]
    check(rb == [k], 'guide p.3 "Cell %d" figure %s: its only all-three cell is cell %s' % (k, code, rb))
# p.4: K-1 P3 max and P4 max
figs = figures_on(4)
check(len(figs) == 2, 'guide p.4: two figures')
report(4, figs[0], 'RBRB/RYB/RB/Y', 5)
report(4, figs[1], 'RRB/YB/Y centres BRYR', 7)
# p.5: three witnesses
figs = figures_on(5)
for f, (c, n) in zip(figs, [('RRRB/RRB/RB/Y', 1), ('RRRB/RRY/RB/Y', 3), ('RBRB/RYB/RB/Y', 5)]):
    report(5, f, c, n)
check(len(figs) == 3, 'guide p.5: three figures')
# p.6: numbered side-4 board
figs = figures_on(6)
check(len(figs) == 1 and figs[0]['name'] == 'side4' and not figs[0]['lab'], 'guide p.6: one unlettered side-4 board')
report(6, figs[0])
# p.7: K-1 P6 four fillings and 4-5 P6 witness
figs = figures_on(7)
check(len(figs) == 5, 'guide p.7: five figures')
for f, c in zip(figs[:4], ['RRYB/RRY/RY/Y', 'RRYB/RRY/YY/Y', 'RRYB/RYB/RY/Y', 'RRYB/RYB/YB/Y']):
    report(7, f, c, 0)
report(7, figs[4], 'RRYBB/RRYB/RRY/RY/Y', 0)
# p.8: 2-3 P2 with doors
figs = figures_on(8)
report(8, figs[0], 'RBRB/RRB/RB/Y', 1, doors=True)
# p.9: 4-5 P2 with doors
figs = figures_on(9)
report(9, figs[0], 'RRBRB/YBRB/RBB/RB/Y', 3, doors=True)

say('')
say('%d failures' % len(FAIL))
for f in FAIL:
    say('FAILED: ' + f)
open(os.path.join(HERE, 'out_check_diagrams.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
