"""Recompute every answer printed in the adult guide from the boards on the student pages.

Run from anywhere:  python3 check.py
Reads final/src/figs/*.tex (the figures exactly as printed), rebuilds each board on the
triangle lattice, solves it with the code in lattice.py, prints a report, stops on the
first answer that disagrees with the guide, and writes answer pictures to figs/.
"""
import math
import os
import sys
import time
from collections import Counter
from itertools import combinations

from lattice import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'figs')
os.makedirs(OUT, exist_ok=True)
FAST = '--fast' in sys.argv          # skip the slow 4-by-4 game search

n_ok = 0


def ok(cond, msg):
    global n_ok
    print(('  ok   ' if cond else '  FAIL ') + msg)
    if not cond:
        raise SystemExit('check failed: ' + msg)
    n_ok += 1


def head(s):
    print('\n' + s)


def actual_size(b, what):
    ok(abs(b.frame.unit - 1.0) < 1e-3, f'{what}: small edge {b.frame.unit:.3f} in (actual size)')


def max_yellows(R):
    Y = yellows(R)
    best = 0
    def grow(i, used, k):
        nonlocal best
        best = max(best, k)
        for j in range(i, len(Y)):
            if not (Y[j] & used):
                grow(j + 1, used | Y[j], k + 1)
    grow(0, frozenset(), 0)
    return best


def middle_hex(R):
    pts = set().union(*R)
    c = (round(sum(p[0] for p in pts) / len(pts)), round(sum(p[1] for p in pts) / len(pts)))
    h = frozenset(t for t in R if c in t)
    assert len(h) == 6
    return h


GROUP = [('green', greens), ('blue', blues), ('red', reds), ('yellow', yellows)]


def gbry(R):
    P = []
    for _, f in GROUP:
        P += f(R)
    return P


def mix(T):
    c = Counter(colour(p) for p in T)
    return ', '.join(f'{c[k]} {k}' for k in ('yellow', 'red', 'blue', 'green') if c[k])


# ------------------------------------------------------------------ answer pictures

FILL = {'green': 'pbgreen!55', 'blue': 'pbblue!55', 'red': 'pbred!50', 'yellow': 'pbyellow!75'}


def loop_of(cells):
    """Boundary of a set of triangles as a list of lattice points (one loop)."""
    de = {}
    for t in cells:
        a, b, c = sorted(t)
        pa, pb, pc = cart(a), cart(b), cart(c)
        if (pb[0] - pa[0]) * (pc[1] - pa[1]) - (pb[1] - pa[1]) * (pc[0] - pa[0]) < 0:
            b, c = c, b
        for u, v in ((a, b), (b, c), (c, a)):
            de[(u, v)] = 1
    bnd = {u: v for (u, v) in de if (v, u) not in de}
    s = next(iter(bnd))
    L = [s]
    v = bnd[s]
    while v != s:
        L.append(v)
        v = bnd[v]
    return simplify(L)


class Pic:
    def __init__(self):
        self.cmds = []
        self.box = [1e9, 1e9, -1e9, -1e9]

    def poly(self, pts, style):
        for x, y in pts:
            self.box = [min(self.box[0], x), min(self.box[1], y), max(self.box[2], x), max(self.box[3], y)]
        self.cmds.append(f'\\filldraw[{style}] ' + ' -- '.join(f'({x:.3f},{y:.3f})' for x, y in pts) + ' -- cycle;')

    def text(self, x, y, s, anchor='center'):
        self.cmds.append(f'\\node[anchor={anchor}, inner sep=1pt, font=\\scriptsize] at ({x:.3f},{y:.3f}) {{{s}}};')

    def tex(self):
        return '\\begin{tikzpicture}[x=1in,y=1in, line join=round]\n' + '\n'.join(self.cmds) + '\n\\end{tikzpicture}\n'


def draw_tiling(pic, R, T, rot, unit, dx, dy, mark=None, outline_only=False):
    """Draw tiling T of region R, turned by `rot` degrees, small edge `unit` inches,
    with its lower-left bounding corner at (dx, dy).  Returns the width and height."""
    r = math.radians(rot)

    def P(q):
        X, Y = cart(q)
        return (math.cos(r) * X - math.sin(r) * Y, math.sin(r) * X + math.cos(r) * Y)
    pts = [P(v) for t in R for v in t]
    mx = min(p[0] for p in pts)
    my = min(p[1] for p in pts)
    w = (max(p[0] for p in pts) - mx) * unit
    h = (max(p[1] for p in pts) - my) * unit

    def Q(q):
        X, Y = P(q)
        return (dx + (X - mx) * unit, dy + (Y - my) * unit)
    if T is None:
        pic.poly([Q(q) for q in loop_of(R)], 'fill=white, draw=black, line width=0.5pt')
        for t in R:
            pic.poly([Q(q) for q in sorted(t)], 'fill=none, draw=black!30, line width=0.3pt')
        pic.poly([Q(q) for q in loop_of(R)], 'fill=none, draw=black, line width=0.7pt')
    else:
        for p in T:
            style = 'fill=' + FILL[colour(p)] + ', draw=black, line width=0.45pt'
            pic.poly([Q(q) for q in loop_of(p)], style)
    if mark:
        for p in mark:
            pic.poly([Q(q) for q in loop_of(p)], 'fill=pbblue!60, draw=black, line width=0.6pt')
    return w, h


def row_pic(items, unit, gap=0.22, rot=0, labels=None):
    """items: list of (R, T) or (R, None, mark); drawn left to right, bottoms aligned."""
    pic = Pic()
    x = 0.0
    for i, it in enumerate(items):
        R, T = it[0], it[1]
        mark = it[2] if len(it) > 2 else None
        w, h = draw_tiling(pic, R, T, rot, unit, x, 0.16 if labels else 0.0, mark)
        if labels:
            pic.text(x + w / 2, 0.0, labels[i], 'south')
        x += w + gap
    return pic


def save(name, pic):
    with open(os.path.join(OUT, name + '.tex'), 'w') as fh:
        fh.write(pic.tex())


t0 = time.time()

# ------------------------------------------------------------------ K-1
head('K-1 Problem 1 (figure k1): bigger copies')
b = boards_of('k1', 'line width=1.6pt')
names = ['2x triangle', '2x rhombus', '2x hexagon', '2x trapezoid']
want_sides = [[2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2, 2, 2], [2, 2, 2, 4]]
pieces_for = {'2x triangle': greens, '2x rhombus': blues, '2x trapezoid': reds, '2x hexagon': yellows}
size = {greens: 1, blues: 2, reds: 3, yellows: 6}
for B, nm, ws in zip(b, names, want_sides):
    actual_size(B, nm)
    ok(sorted(B.sides) == sorted(ws), f'{nm}: sides {B.sides}')
    f = pieces_for[nm]
    n = Tiler(B.R, f(B.R)).count()
    k = len(B.R) // size[f]
    print(f'      {nm}: {len(B.R)} small triangles, {n} filling(s) with small {f.__name__}')
    if nm == '2x hexagon':
        ok(n == 0 and max_yellows(B.R) == 3, '2x hexagon: no filling with small yellows (answer X); at most 3 yellows fit')
    else:
        ok(n >= 1 and k == 4, f'{nm}: 4 small pieces')
    if nm == '2x trapezoid':
        ok(n == 1, '2x trapezoid: exactly one way with 4 reds')
loops, segs, pieces, fills, texts = read_fig('k1')
small = [s for s in reading_order(loops) if 'line width=0.9pt' in s.style]
three = []
for s in small:
    shortest = min(math.dist(s.pts[i], s.pts[(i + 1) % len(s.pts)]) for i in range(len(s.pts)))
    B = Board(s, shortest / 3)
    three.append(B)
for B, nm, f in zip(three, ['3x triangle', '3x rhombus', '3x trapezoid', '3x hexagon'],
                    [greens, blues, reds, yellows]):
    n = Tiler(B.R, f(B.R)).count()
    print(f'      {nm} (picture of the Upscale block, sides {B.sides}): {len(B.R)} triangles, {n} filling(s)')
    if nm == '3x hexagon':
        ok(n == 0 and max_yellows(B.R) == 7, '3x hexagon: no filling with small yellows (X); at most 7 fit')
    else:
        ok(n >= 1 and len(B.R) // size[f] == 9, f'{nm}: 9 small pieces')

GAME_LOG = []


def game_report(B, label, expect, show_moves=False):
    w, win, moves = game(B.R)
    c, kind, selfs = half_turn(B.R)
    sym = 'no half-turn symmetry' if c is None else f'half-turn centre at a {kind}, {len(selfs)} placement(s) on the centre'
    ok(w == expect, f'{label} (sides {B.sides}, {len(B.R)} triangles): {w} player wins; '
       f'{len(win)} of {len(moves)} first moves win; {sym}')
    GAME_LOG.append((label, w, len(win), len(moves), sym))
    return win, selfs


head('K-1 Problem 2 (figure k2): game boards, reading order')
b = boards_of('k2')
for B in b:
    actual_size(B, 'board')
win_strip = None
for B, lab, e in zip(b, ['hexagon 1,1,1', '2-by-2 board', '3-by-1 strip'], ['second', 'second', 'first']):
    win, _ = game_report(B, 'K-1 P2 ' + lab, e)
    if lab == '3-by-1 strip':
        win_strip = (B, win)
B, win = win_strip
mids = [m for m in win]
ok(len(mids) == 1, '3-by-1 strip: the only winning first move is the middle one (covers triangles 3 and 4 of 6)')

head('K-1 Problem 3 (figure k3): fewest / most')
b = boards_of('k3')
k3pics = []
for B, nm, few in zip(b, ['triangle side 3', 'six-point star'], [3, 6]):
    actual_size(B, nm)
    T = Tiler(B.R, gbry(B.R))
    n, ex = T.fewest()
    most = T.most()
    ok(n == few and most == len(B.R), f'{nm}: fewest {n} (e.g. {mix(ex)}), most {most} (all green)')
    k3pics.append((B.R, ex))
tri3 = b[0]
Yt = yellows(tri3.R)
rest = tri3.R - Yt[0]
ok(len(Yt) == 1 and Tiler(rest, gbry(rest)).fewest()[0] == 3, 'triangle 3: a yellow fits in one place only, and then 3 greens are needed (4 pieces)')
# star: every point needs its own piece
B = b[1]
nb = neighbours_in(B.R)
points = [t for t in B.R if len(nb[t]) == 1]
ok(len(points) == 6 and all(not any(t in p and u in p for p in gbry(B.R)) for t, u in combinations(points, 2)),
   'star: 6 points, no piece can cover two points, so at least 6 pieces')
T = Tiler(B.R, gbry(B.R))
print('      star: fillings with 6 pieces use', sorted({mix(x) for x in T.all_with(6)}))
save('k3ans', row_pic(k3pics, 0.22, labels=['triangle: 3', 'star: 6']))

head('K-1 Problem 4 (figure k4): game boards, reading order')
b = boards_of('k4')
for B, lab, e in zip(b, ['3-by-2 board', 'triangle side 3', '4-by-2 board'], ['first', 'first', 'second']):
    actual_size(B, lab)
    win, selfs = game_report(B, 'K-1 P4 ' + lab, e)
    if lab == '3-by-2 board':
        ok(len(win) == 1 and set(win) == set(selfs), '3-by-2: the only winning first move is the centre rhombus')
        K32 = (B.R, win)
    if lab == 'triangle side 3':
        ok(len(win) == len(blues(B.R)), 'triangle 3: every first move wins')

head('K-1 Problem 5 (figure k5): only red, then only blue')
b = boards_of('k5', 'line width=1.6pt')
k5pics = []
for B, nm, red, blue in zip(b, ['arrow (sides 1,1,3,1,1,3)', 'trapezoid 4 along the bottom, 1 on top', 'hexagon 2,1,2'],
                            [4, 5, None], [6, None, 8]):
    actual_size(B, nm)
    tr = Tiler(B.R, reds(B.R)).all()
    tb = Tiler(B.R, blues(B.R)).all()
    u, d = B.updown
    ok((len(tr) > 0) == (red is not None) and (not tr or len(tr[0]) == red),
       f'{nm}: {len(B.R)} triangles; red: ' + (f'{red} pieces, {len(tr)} way(s)' if tr else 'X'))
    ok((len(tb) > 0) == (blue is not None) and (not tb or len(tb[0]) == blue),
       f'{nm}: up {u} / down {d}; blue: ' + (f'{blue} pieces, {len(tb)} way(s)' if tb else 'X'))
    if tr:
        k5pics.append((B.R, tr[0]))
    if tb:
        k5pics.append((B.R, tb[0]))
save('k5ans', row_pic(k5pics, 0.19, labels=['4 red', '6 blue', '5 red', '8 blue']))

head('K-1 Problem 6 (figure k6): fewest / most')
b = boards_of('k6')
k6pics = []
for B, nm, few in zip(b, ['boat', '2x hexagon'], [5, 6]):
    actual_size(B, nm)
    T = Tiler(B.R, gbry(B.R))
    n, ex = T.fewest()
    ok(n == few and T.most() == len(B.R), f'{nm}: fewest {n} (e.g. {mix(ex)}), most {len(B.R)} (all green)')
    k6pics.append((B.R, ex))
    if nm == 'boat':
        print('      boat: 5-piece fillings use', sorted({mix(x) for x in T.all_with(5)}), len(T.all_with(5)), 'fillings')
save('k6ans', row_pic(k6pics, 0.22, labels=['boat: 5', 'hexagon: 6']))

head('K-1 Problem 7 (figure k7): the 1-inch hexagon')
b = boards_of('k7', skip_icons=True)
H = b[0]
actual_size(H, 'yellow hexagon outline')
ok(H.sides == [1] * 6, 'outline is one yellow hexagon')
tr = Tiler(H.R, reds(H.R)).all()
tb = Tiler(H.R, blues(H.R)).all()
ok(len(tr) == 3 and all(len(x) == 2 for x in tr), 'two reds: 3 ways (cut across each of the 3 long diagonals)')
ok(len(tb) == 2 and all(len(x) == 3 for x in tb), 'three blues: 2 ways')
copies = [B for B in b[1:]]
rows = Counter(round(B.shape.bbox[1], 2) for B in copies)
ok(sorted(rows.values()) == [2, 3], f'recording hexagons per row: {sorted(rows.values(), reverse=True)} (red row 3, blue row 2)')
save('k7ans', row_pic([(H.R, x) for x in tr] + [(H.R, x) for x in tb], 0.24, gap=0.15))

# ------------------------------------------------------------------ games for 2-3 and 4-5
head('Grades 2-3 and 4-5 Problem 1 (figure game1)')
b = boards_of('game1')
for B, lab, e in zip(b, ['hexagon 1,1,1', '2-by-2 board', '3-by-2 board', 'hexagon 1,1,2'],
                     ['second', 'second', 'first', 'first']):
    actual_size(B, lab)
    win, selfs = game_report(B, 'P1 ' + lab, e)
    if e == 'first':
        ok(set(selfs) <= set(win) and len(selfs) == 1, f'{lab}: the centre rhombus is a winning first move')
    if lab == 'hexagon 1,1,2':
        H112 = (B.R, win)
        ok(len(win) == 1, 'hexagon 1,1,2: the centre rhombus is the only winning first move')

head('Grades 2-3 Problem 2 (figure tri3-4-par)')
b = boards_of('tri3-4-par')
for B, lab, e in zip(b, ['triangle side 3', 'triangle side 4', '4-by-2 board'], ['first', 'second', 'second']):
    actual_size(B, lab)
    game_report(B, '2-3 P2 ' + lab, e)

def game_lengths(R):
    lens = set()

    def play(free, k):
        moves = [m for m in blues(free)]
        if not moves:
            lens.add(k)
            return
        for m in moves:
            play(free - m, k + 1)
    play(frozenset(R), 0)
    return lens


T3 = boards_of('tri3-4-par')[0]
nb3 = neighbours_in(T3.R)
downs = [t for t in T3.R if not is_up(t)]
ok(game_lengths(T3.R) == {3} and all(any(len(nb3[u]) == 1 for u in nb3[d]) for d in downs),
   'triangle 3: every game lasts exactly 3 moves (each of the 3 down-triangles has a corner partner no other can use)')

head('Grades 4-5 Problem 3 (figure tri3-4)')
b = boards_of('tri3-4')
for B, lab, e in zip(b, ['triangle side 3', 'triangle side 4'], ['first', 'second']):
    actual_size(B, lab)
    game_report(B, '4-5 P3 ' + lab, e)

head('Strategy boards: 2-3 Problem 5 and 4-5 Problem 2 (figure game2)')
b = boards_of('game2')
for B, lab, e in zip(b, ['hexagon 2,2,2', '3-by-3 board'], ['second', 'first']):
    actual_size(B, lab)
    win, selfs = game_report(B, 'strategy ' + lab, e)
    if e == 'second':
        ok(len(selfs) == 0, f'{lab}: centre is a grid point and no placement is its own image, so copying works')
    else:
        ok(len(selfs) == 1 and selfs[0] in win, f'{lab}: one placement covers the centre; take it, then copy')
        S33 = (B.R, selfs)

head('Grades 4-5 Problem 9 (figure u9): drawn small')
b = boards_of('u9')
for B, lab, e in zip(b, ['hexagon 3,3,3', 'hexagon 1,2,3', '4-by-4 board', '5-by-2 board'],
                     ['second', 'first', 'second', 'first']):
    c, kind, selfs = half_turn(B.R)
    want_kind = 'grid point' if e == 'second' else 'edge midpoint'
    ok(kind == want_kind and len(selfs) == (0 if e == 'second' else 1),
       f'4-5 P9 {lab} (sides {B.sides}, {len(B.R)} triangles): centre at a {kind}, '
       f'{len(selfs)} placement(s) on the centre -> {e} player wins by copying')
    if lab in ('hexagon 1,2,3', '5-by-2 board') or (lab == '4-by-4 board' and not FAST):
        tt = time.time()
        win, _ = game_report(B, f'4-5 P9 {lab} (full search)', e)
        print(f'      search took {time.time() - tt:.0f} s')

# parity rule for centres, over many boards
head('Centre rule (where the half-turn centre sits)')
for a in range(1, 6):
    for bb in range(1, 6):
        lp = [(0, 0), (a, 0), (a, bb), (0, bb)]
        R = region_of_lattice_poly(lp)
        c, kind, selfs = half_turn(R)
        assert (kind == 'grid point') == (a % 2 == 0 and bb % 2 == 0)
        assert len(selfs) == (0 if kind == 'grid point' else 1)
for a in range(1, 5):
    for bb in range(1, 5):
        for cc in range(1, 5):
            pts = [(0, 0)]
            for (dx, dy), n in zip([(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)], [a, bb, cc, a, bb, cc]):
                x, y = pts[-1]
                pts.append((x + dx * n, y + dy * n))
            R = region_of_lattice_poly(pts[:-1])
            c, kind, selfs = half_turn(R)
            assert (kind == 'grid point') == (a % 2 == bb % 2 == cc % 2)
            assert len(selfs) == (0 if kind == 'grid point' else 1)
ok(True, 'a-by-b board: centre is a grid point exactly when a and b are both even (a, b <= 5); '
   'hexagon a,b,c: exactly when a, b, c are all even or all odd (<= 4); otherwise exactly one placement covers the centre')

# ------------------------------------------------------------------ fewest pieces, 2-3 and 4-5
head('Grades 2-3 Problem 3 (figure m3): fewest pieces')
b = boards_of('m3', 'line width=1.6pt')
m3pics = []
for B, nm, few in zip(b, ['2x hexagon', 'triangle side 4'], [6, 5]):
    actual_size(B, nm)
    T = Tiler(B.R, gbry(B.R))
    n, ex = T.fewest()
    ok(n == few, f'{nm}: fewest {n} (e.g. {mix(ex)})')
    allbest = {mix(x) for x in T.all_with(few)}
    print(f'      {nm}: every {few}-piece filling uses one of {sorted(allbest)}')
    m3pics.append((B.R, ex))
    Y = yellows(B.R)
    sets = [s for k in range(1, 8) for s in combinations(Y, k) if all(not (p & q) for p, q in combinations(s, 2))]
    maxy = max(len(s) for s in sets)
    print(f'      {nm}: {len(Y)} places for a yellow, at most {maxy} fit together')
    if nm == '2x hexagon':
        ok(maxy == 3, '2x hexagon: at most 3 yellows fit')
        mid = middle_hex(B.R)
        ok(all(len(h & mid) >= 2 for h in Y), '2x hexagon: every yellow covers at least 2 of the 6 middle triangles')
        threes = [s for s in sets if len(s) == 3]
        for s in threes:
            rest = B.R - set().union(*s)
            comps = components(rest, neighbours_in(rest))
            ok(sorted(len(c) for c in comps) == [2, 2, 2],
               '2x hexagon: 3 yellows leave three separate 2-triangle holes, so 3 more pieces: 6 in all')
        print(f'      ({len(threes)} ways to place 3 yellows)')
    if nm == 'triangle side 4':
        ok(maxy == 1, 'triangle 4: only one yellow fits; 1 yellow + 4 others >= 16 needs reds: 6+3+3+3 = 15 < 16 for 4 pieces')
save('m3ans', row_pic(m3pics, 0.2, labels=['hexagon: 6', 'triangle: 5']))

head('Big hexagon: 2-3 Problem 6 and 4-5 Problem 10 (figure bighex)')
B = boards_of('bighex', 'line width=1.6pt')[0]
actual_size(B, '3x hexagon')
ok(B.sides == [3] * 6 and len(B.R) == 54, '3x hexagon, 54 small triangles')
tt = time.time()
T = Tiler(B.R, gbry(B.R))
n, ex = T.fewest()
ok(n == 12, f'3x hexagon: fewest {n} (e.g. {mix(ex)}); search {time.time() - tt:.0f} s')
Y = yellows(B.R)
best = {}


def grow(start, chosen, used):
    k = len(chosen)
    best.setdefault(k, []).append(tuple(chosen))
    for i in range(start, len(Y)):
        if not (Y[i] & used):
            chosen.append(Y[i])
            grow(i + 1, chosen, used | Y[i])
            chosen.pop()


grow(0, [], frozenset())
maxy = max(best)
ok(maxy == 7, f'3x hexagon: {len(Y)} places for a yellow, at most {maxy} fit')
worst = None
for s in best[7]:
    rest = B.R - set().union(*s)
    m, _ = Tiler(rest, greens(rest) + blues(rest) + reds(rest)).fewest()
    comps = components(rest, neighbours_in(rest))
    worst = m if worst is None else min(worst, m)
ok(worst == 6, f'3x hexagon: {len(best[7])} ways to fit 7 yellows; each leaves holes needing >= 6 more pieces (7+6 = 13)')
print('      7-yellow leftovers: hole sizes', sorted({tuple(sorted(len(c) for c in components(B.R - set().union(*s), neighbours_in(B.R - set().union(*s))))) for s in best[7]}))
twelve = T.all_with(12)
pts54 = set().union(*B.R)
cx2 = sum(2 * p[0] for p in pts54) // len(pts54)
cy2 = sum(2 * p[1] for p in pts54) // len(pts54)
ctr = (cx2 // 2, cy2 // 2)


def img_tiling(T, f):
    return frozenset(frozenset(frozenset(f(v) for v in t) for t in p) for p in T)


def rot60(v):
    x, y = v[0] - ctr[0], v[1] - ctr[1]
    return (-y + ctr[0], x + y + ctr[1])


def refl(v):
    x, y = v[0] - ctr[0], v[1] - ctr[1]
    return (y + ctr[0], x + ctr[1])


a12, b12 = twelve
rots = []
cur = a12
for k in range(6):
    rots.append(cur)
    cur = img_tiling(cur, rot60)
ok(len(twelve) == 2 and all(mix(x) == '6 yellow, 6 red' for x in twelve) and rots[1] == b12
   and img_tiling(a12, refl) == b12,
   '3x hexagon: exactly two 12-piece fillings, 6 yellows + 6 reds; each is the other turned a sixth of a turn (or mirrored)')
six = {mix(x) for x in [ex]}
print('      a 12-piece filling:', six)
save('bighexans', row_pic([(B.R, ex)], 0.2))

# ------------------------------------------------------------------ trapezoids, 2-3
head('Grades 2-3 Problem 4 (figure m4): trapezoid fillings, two-up and two-down')
b = boards_of('m4')
tri3 = b[0]
actual_size(tri3, 'triangle 3')


def kinds(T):
    up = sum(1 for p in T if sum(1 for t in p if is_up(t)) == 2)
    return up, len(T) - up


tt = Tiler(tri3.R, reds(tri3.R)).all()
ok(len(tt) == 2 and all(kinds(x) == (3, 0) for x in tt), 'triangle 3: exactly 2 fillings, each 3 two-up and 0 two-down')
ok(sum(1 for B in b[1:] if len(B.R) == 9) == 2, 'two small triangle copies on the page')
ptsT = set().union(*tri3.R)
# mirror in the triangle's vertical axis and a third of a turn, in lattice coordinates


def mapT(T, f):
    return frozenset(frozenset(frozenset(f(v) for v in tri) for tri in p) for p in T)
x0 = min(p[0] for p in ptsT); y0 = min(p[1] for p in ptsT)
mir = lambda v: (x0 + 3 - (v[0] - x0) - (v[1] - y0), v[1])
rot120 = lambda v: (x0 + 3 - (v[0] - x0) - (v[1] - y0), v[0] - x0 + y0)
ok(all(t_ in tri3.R for p in mapT(tt[0], mir) for t_ in p) and mapT(tt[0], mir) == tt[1]
   and mapT(tt[0], rot120) == tt[0], 'triangle 3: the 2 fillings are mirror images; each is unchanged by a third of a turn')
save('m4tri', row_pic([(tri3.R, x) for x in tt], 0.22))
hexb = boards_of('m3', 'line width=1.6pt')[0]
th = Tiler(hexb.R, reds(hexb.R)).all()
ok(len(th) == 9 and all(kinds(x) == (4, 4) for x in th), '2x hexagon (as drawn in Problem 3): 9 fillings, each 4 two-up and 4 two-down')
ok(sum(1 for B in b[1:] if len(B.R) == 24) == 8, 'eight small hexagon copies on the page')

head('Grades 2-3 Problem 7 (figure m7): triangle with 6 small edges per side')
B = boards_of('m7', 'line width=1.6pt')[0]
actual_size(B, 'triangle 6')
u, d = B.updown
ok((u, d) == (21, 15), f'triangle 6: {u} up-triangles and {d} down-triangles')
tt = Tiler(B.R, reds(B.R)).all()
ok(len(tt) == 220 and all(kinds(x) == (9, 3) for x in tt), f'triangle 6: {len(tt)} fillings, every one 9 two-up and 3 two-down')
ok((u - d) == 6 and (u + d) // 3 == 12, 'two-up minus two-down = 21 - 15 = 6; two-up plus two-down = 36/3 = 12; so 9 and 3')
for n in range(1, 7):
    R = region_of_lattice_poly([(0, 0), (n, 0), (0, n)])
    uu = sum(1 for t in R if is_up(t))
    assert len(R) == n * n and uu == n * (n + 1) // 2 and len(R) - uu == n * (n - 1) // 2
ok(True, 'triangle with n small edges per side: n*n triangles, 1+..+n up and 1+..+(n-1) down (n <= 6)')

# ------------------------------------------------------------------ cubes, 4-5
head('Grades 4-5 Problems 4-6: blue fillings as piles of cubes')
DIR3 = {90: (0, 0, 1), 270: (0, 0, -1), 210: (1, 0, 0), 30: (-1, 0, 0), 330: (0, 1, 0), 150: (0, -1, 0)}


def page_angle(frame, a, b):
    pa, pb = frame.to_page(a), frame.to_page(b)
    return round(math.degrees(math.atan2(pb[1] - pa[1], pb[0] - pa[0]))) % 360


def diag_class(frame, p):
    t, u = list(p)
    a = list(t - u)[0]
    c = list(u - t)[0]
    ang = page_angle(frame, a, c) % 180
    return {0: 'flat', 60: 'diag60', 120: 'diag120'}[ang]


def lift(frame, T, anchor):
    """3D positions of the tiling's vertices, walking along rhombus sides from `anchor`."""
    adj = {}
    for p in T:
        t, u = list(p)
        sides = [frozenset(e) for tri in p for e in combinations(sorted(tri), 2) if frozenset(e) != (t & u)]
        for e in sides:
            a, c = list(e)
            adj.setdefault(a, set()).add(c)
            adj.setdefault(c, set()).add(a)
    pos = {anchor: (0, 0, 0)}
    q = [anchor]
    while q:
        a = q.pop()
        for c in adj[a]:
            v = DIR3[page_angle(frame, a, c)]
            pc = tuple(x + y for x, y in zip(pos[a], v))
            if c in pos:
                assert pos[c] == pc, 'lift not consistent'
            else:
                pos[c] = pc
                q.append(c)
    return pos


def cubes(frame, R, T):
    pts = set().union(*R)
    anchor = min(pts, key=lambda q: frame.to_page(q)[1])          # bottom corner of the picture
    pos = lift(frame, T, anchor)
    tot = 0
    for p in T:
        if diag_class(frame, p) == 'flat':
            zs = {pos[v][2] for v in set().union(*p)}
            assert len(zs) == 1
            tot += zs.pop()
    return tot


def heights(frame, R, T):
    """Stack heights of the pile: {cell: height}, cells counted from the back corner."""
    pts = set().union(*R)
    anchor = min(pts, key=lambda q: frame.to_page(q)[1])
    pos = lift(frame, T, anchor)
    cells = {}
    for p in T:
        if diag_class(frame, p) == 'flat':
            cs = [pos[v] for v in set().union(*p)]
            cells[(min(q[0] for q in cs), min(q[1] for q in cs))] = cs[0][2]
    mx = min(k[0] for k in cells)
    my = min(k[1] for k in cells)
    return {(k[0] - mx, k[1] - my): v for k, v in cells.items()}


def shaded_pictures(name):
    """Pictures drawn as filled pieces in figure `name`, keyed by the letter printed to their
    left: label -> (frame, region, tiling, fill of each piece)."""
    loops, segs, pieces, fills, texts = read_fig(name)
    labels = [(x, y, t.split()[-1]) for x, y, t in texts if t.split()[-1] in ('A', 'B', 'C', 'D')]
    # cluster pieces into pictures by horizontal overlap
    pcs = sorted(pieces, key=lambda pc: pc.bbox[0])
    clusters = []
    for pc in pcs:
        if clusters and pc.bbox[0] <= max(q.bbox[2] for q in clusters[-1]) + 1e-6:
            clusters[-1].append(pc)
        else:
            clusters.append([pc])
    out = {}
    for cl in clusters:
        x0 = min(q.bbox[0] for q in cl)
        lab = min((L for L in labels if L[0] < x0), key=lambda L: x0 - L[0])[2]
        unit = min(math.dist(pc.pts[i], pc.pts[(i + 1) % len(pc.pts)]) for pc in cl for i in range(len(pc.pts)))
        fr = Frame(cl[0].pts, unit)
        T, shade = [], {}
        for pc in cl:
            p = region_of_lattice_poly([fr.to_lat(q) for q in pc.pts])
            T.append(p)
            shade[p] = pc.kind
        out[lab] = (fr, frozenset().union(*T), frozenset(T), shade)
    return out


key = None
for fig in ('u4', 'u5'):
    pics = shaded_pictures(fig)
    ok(sorted(pics) == ['A', 'B'], f'{fig}: pictures A and B found')
    for lab in 'AB':
        fr, R, T, shade = pics[lab]
        ok(sorted(sides(loop_of(R))) == [2] * 6 and all(len(p) == 2 for p in T) and sum(len(p) for p in T) == len(R) == 24,
           f'{fig} {lab}: a filling of the 2,2,2 hexagon by 12 blue rhombi')
        m = {}
        for p in T:
            m.setdefault(diag_class(fr, p), set()).add(shade[p])
        ok(all(len(v) == 1 for v in m.values()), f'{fig} {lab}: one shade per direction {dict((k, v.pop()) for k, v in m.items())}')
        mm = {}
        for p in T:
            mm[diag_class(fr, p)] = shade[p]
        if key is None:
            key = mm
        ok(all(key[k] == v for k, v in mm.items()), f'{fig} {lab}: same shading key as before')
        c = cubes(fr, R, T)
        ok(c == {'A': 0, 'B': 8}[lab], f'{fig} {lab}: picture shows {c} cubes (page says {"0" if lab == "A" else "8"} on Problem 4)')
ok(key['flat'] == 'shadeL', 'flat (horizontal) faces are the light shade')
HEXU = boards_of('u4', 'line width=1.6pt')[0]
actual_size(HEXU, '4-5 P4 hexagon')
R = HEXU.R
Ts = Tiler(R, blues(R)).all()
G = rhombus_flip_graph(R, Ts)
cnt = {T: cubes(HEXU.frame, R, T) for T in Ts}
dist = Counter(cnt.values())
ok(len(Ts) == 20 and sorted(dist.items()) == [(0, 1), (1, 1), (2, 3), (3, 3), (4, 4), (5, 3), (6, 3), (7, 1), (8, 1)],
   f'4-5 P4: 20 fillings; number of fillings with 0..8 cubes: {[dist[i] for i in range(9)]}')
ok(all(abs(cnt[T] - cnt[S]) == 1 for T in Ts for S in G[T]), 'every flip adds or removes exactly one cube')
ok(is_bipartite(G), 'flip graph has no odd cycle (so no route returns after an odd number of flips)')
empty = [T for T in Ts if cnt[T] == 0][0]
full = [T for T in Ts if cnt[T] == 8][0]
d = bfs(G, empty)
ok(d[full] == 8 and all(d[T] == cnt[T] for T in Ts), 'fewest flips from A (0 cubes) to B (8 cubes) is 8; distance from A = cube count')
ok(all(len(G[T]) >= 1 for T in Ts) and sorted(len(G[T]) for T in Ts)[:2] == [1, 1], 'A and B are the only fillings with a single possible flip')
ok(Counter(len(G[T]) for T in Ts)[1] == 2, 'exactly two fillings allow just one flip')
piles = {}
for T in Ts:
    h = heights(HEXU.frame, R, T)
    assert sorted(h) == [(0, 0), (0, 1), (1, 0), (1, 1)] and sum(h.values()) == cnt[T]
    piles[T] = (h[(0, 0)], h[(1, 0)], h[(0, 1)], h[(1, 1)])          # back, left, right, front
pp = sorted(piles.values(), key=lambda v: (sum(v), [-x for x in v]))
allpp = [(a, b, c_, d) for a in range(3) for b in range(3) for c_ in range(3) for d in range(3)
         if a >= b and a >= c_ and b >= d and c_ >= d]
ok(sorted(pp) == sorted(allpp) and len(set(pp)) == 20,
   '4-5 P4: the 20 fillings are exactly the 20 piles (back >= left, right >= front, heights 0-2)')
byc = {}
for v in pp:
    byc.setdefault(sum(v), []).append(''.join(map(str, v)))
print('      piles (back left right front) by cube count:', byc)
with open(os.path.join(OUT, 'piles.tex'), 'w') as fh:
    fh.write(' \\\\\n'.join(f'{k} & ' + ', '.join(byc[k]) for k in sorted(byc)) + '\n')
ok(piles[[T for T in Ts if cnt[T] == 0][0]] == (0, 0, 0, 0), 'A is the empty corner 0000; B is 2222')
for T in Ts:
    c = Counter(diag_class(HEXU.frame, p) for p in T)
    assert c == Counter({'flat': 4, 'diag60': 4, 'diag120': 4})
ok(True, '2,2,2 hexagon: every filling has 4 rhombi of each shade')

U6 = boards_of('u6', 'line width=1.6pt')[0]
actual_size(U6, '4-5 P6 hexagon')
R = U6.R
Ts6 = Tiler(R, blues(R)).all()
G6 = rhombus_flip_graph(R, Ts6)
c6 = {T: cubes(U6.frame, R, T) for T in Ts6}
SH = {k: {'shadeL': 'light', 'shadeM': 'medium', 'shadeD': 'dark'}[v] for k, v in key.items()}
counts = {tuple(sorted(Counter(SH[diag_class(U6.frame, p)] for p in T).items())) for T in Ts6}
ok(len(Ts6) == 20, f'4-5 P6 hexagon (sides {U6.sides}): 20 fillings')
ok(len(counts) == 1, f'4-5 P6: every filling has the same shades: {counts}')
e6 = [T for T in Ts6 if c6[T] == 0]
f6 = [T for T in Ts6 if c6[T] == max(c6.values())]
ok(len(e6) == 1 and len(f6) == 1 and max(c6.values()) == 9 and bfs(G6, e6[0])[f6[0]] == 9,
   '4-5 P6: no cubes to most cubes (9 = 1 x 3 x 3) takes 9 flips')
print('      P6 cube counts 0..9:', [Counter(c6.values())[i] for i in range(10)])
ok(all(abs(c6[T] - c6[S]) == 1 for T in Ts6 for S in G6[T]) and is_bipartite(G6), '4-5 P6: flips change the count by one; no odd routes')
ok(len(bfs(G6, e6[0])) == 20 and len(bfs(G, empty)) == 20, 'flips connect all 20 fillings of each hexagon')
c6s, kind6, selfs6 = half_turn(U6.R)
ok(kind6 == 'grid point' and not selfs6, '4-5 page 6 hexagon 1,3,3 as a game board (fallback): centre is a grid point, second player wins by copying')


def macmahon(a, b, cc):
    from fractions import Fraction
    p = Fraction(1)
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, cc + 1):
                p *= Fraction(i + j + k - 1, i + j + k - 2)
    return p


def hexagon_region(a, b, cc):
    pts = [(0, 0)]
    for (dx, dy), n in zip([(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)], [a, b, cc, a, b, cc]):
        x, y = pts[-1]
        pts.append((x + dx * n, y + dy * n))
    return region_of_lattice_poly(pts[:-1])


R122 = hexagon_region(1, 2, 2)
T122 = Tiler(R122, blues(R122)).all()
G122 = rhombus_flip_graph(R122, T122)
ends = [T for T in T122 if len(G122[T]) == 1]
ok(len(T122) == 6 and len(ends) == 2 and bfs(G122, ends[0])[ends[1]] == 4, 'hexagon 1,2,2: 6 blue fillings, 4 flips from emptiest to fullest')
ok(macmahon(2, 2, 2) == 20 and macmahon(1, 3, 3) == 20 and macmahon(1, 2, 2) == 6, "MacMahon's product gives 20, 20 and 6")
sides6 = U6.sides
print('      P6 hexagon page sides (from lowest-left corner):', sides6)

# ------------------------------------------------------------------ trapezoids, 4-5
head('Grades 4-5 Problems 7-8: red fillings of the 2,2,2 hexagon')
R = HEXU.R
Tt = Tiler(R, reds(R)).all()
ok(len(Tt) == 9, '4-5 P7: 9 fillings with small reds')
mid = middle_hex(R)
ok(all(sum(1 for p in T if p <= mid) == 2 for T in Tt), 'every filling covers the middle small hexagon with 2 reds')
ring = R - mid
nbr = neighbours_in(ring)
inner = [t for t in ring if any(adjacent(t, m) for m in mid)]
loop = [inner[0]]
prev = None
while True:
    nxt = [u for u in nbr[loop[-1]] if u != prev]
    prev = loop[-1]
    if nxt[0] == loop[0]:
        break
    loop.append(nxt[0])
ok(all(len(v) == 2 for v in nbr.values()) and len(loop) == 18 and len(inner) == 6
   and all((loop.index(t) % 3) == 0 for t in inner),
   'the ring is a loop of 18 triangles; the 6 touching the middle hexagon are every third one')
rings = Tiler(ring, reds(ring)).all()
middles = Tiler(mid, reds(mid)).all()
ok(len(rings) == 3 and len(middles) == 3, 'the ring (18 triangles) has 3 fillings; the middle has 3: 3 x 3 = 9')
ok(all(not (set(a) & set(bb)) for a, bb in combinations(rings, 2)), 'two different ring fillings share no trapezoid')
cm = [v for v in set().union(*R) if all(v in t_ for t_ in mid)][0]
reflc = lambda v: (cm[0] + (v[1] - cm[1]), cm[1] + (v[0] - cm[0]))
rf = lambda T: frozenset(frozenset(frozenset(reflc(v) for v in t_) for t_ in p) for p in T)
# Put the rings in the order the guide describes (pinwheel, frame, mirror pinwheel),
# independent of set iteration order, which can differ from one build to another.
_frame = [r for r in rings if rf(r) == frozenset(r)]
_pin = sorted((r for r in rings if rf(r) != frozenset(r)), key=lambda r: repr(sorted(repr(sorted(map(sorted, p))) for p in r)))
if len(_frame) == 1 and len(_pin) == 2:
    rings = [_pin[0], _frame[0], _pin[1]]
TT = {(i, j): frozenset(set(rings[i]) | set(middles[j])) for i in range(3) for j in range(3)}
ok(rf(rings[1]) == frozenset(rings[1]) and rf(rings[0]) == frozenset(rings[2]),
   'rings in drawing order: pinwheel, frame (unchanged by a mirror), pinwheel the other way (the mirror of the first)')
ok(set(TT.values()) == set(Tt), 'the 9 fillings are exactly ring x middle')
pics = shaded_pictures('u8')
C = pics['C'][2]
D = pics['D'][2]
frC = pics['C'][0]


def as_hexu(lab):
    """Re-express picture lab in HEXU's lattice by matching outlines up to translation."""
    fr, RR, T, _ = pics[lab]
    # both frames are rotated by 30 degrees; shift by matching the lowest-leftmost corners
    a = min(set().union(*RR))
    bb = min(set().union(*R))
    dx, dy = bb[0] - a[0], bb[1] - a[1]
    return frozenset(frozenset(frozenset((v[0] + dx, v[1] + dy) for v in t) for t in p) for p in T)


Cm, Dm = as_hexu('C'), as_hexu('D')
ok(Cm in set(Tt) and Dm in set(Tt), 'pictures C and D are valid red fillings of the hexagon')
ri = {T: i for (i, j), T in TT.items()}
mj = {T: j for (i, j), T in TT.items()}
ok(mj[Cm] == mj[Dm] and ri[Cm] != ri[Dm] and len(Cm - Dm) == 6, 'C and D: same middle, different ring; they differ in 6 trapezoids')
E5 = {T: [S for S in Tt if S != T and len(T - S) <= 5] for T in Tt}
comp = bfs(E5, Cm)
ok(len(comp) == 3 and Dm not in comp, 'moves of 5 or fewer trapezoids reach only the 3 fillings with C\'s ring; D is not among them')
E2 = {T: [S for S in Tt if len(T - S) == 2] for T in Tt}
tri = [(a, bb, c) for a, bb, c in combinations(Tt, 3) if bb in E2[a] and c in E2[bb] and a in E2[c]]
ok(len(tri) == 3 and not is_bipartite(E2), 'two-trapezoid moves: turning the middle pair gives a 3-move round trip (3 such triangles)')
ok(all(set(E2[T]) == {S for S in Tt if ri[S] == ri[T] and S != T} for T in Tt), 'a two-trapezoid move only ever turns the middle pair')
# the 9 fillings, rings as rows, middles as columns
pic = Pic()
for (i, j), T in TT.items():
    draw_tiling(pic, R, T, 30, 0.2, j * 0.9, (2 - i) * 0.95)
save('u7ans', pic)
which = {lab: (ri[T] + 1, mj[T] + 1) for lab, T in (('C', Cm), ('D', Dm))}
print('      C is ring', which['C'][0], 'middle', which['C'][1], '; D is ring', which['D'][0], 'middle', which['D'][1])
with open(os.path.join(OUT, 'cdpos.tex'), 'w') as fh:
    fh.write(f'\\newcommand{{\\Cring}}{{{which["C"][0]}}}\\newcommand{{\\Dring}}{{{which["D"][0]}}}'
             f'\\newcommand{{\\CDmid}}{{{which["C"][1]}}}\n')

# ------------------------------------------------------------------ winning first moves to show
save('firstK', row_pic([(win_strip[0].R, None, win_strip[1]), (K32[0], None, K32[1])], 0.22, gap=0.3,
                      labels=['3-by-1 strip (P2)', '3-by-2 board (P4)']))
save('firstM', row_pic([(K32[0], None, K32[1]), (H112[0], None, H112[1]), (S33[0], None, S33[1])], 0.2, gap=0.3,
                      labels=['3-by-2', 'hexagon 1,1,2', '3-by-3']))

# ------------------------------------------------------------------ pieces needed (materials)
head('Pieces needed at once for the largest task on each page')
ok(len(boards_of('k6')[1].R) == 24, 'K-1 most on the 2x hexagon: 24 greens per pair')
ok(len(boards_of('m7', 'line width=1.6pt')[0].R) // 3 == 12, '2-3 P7: 12 reds per pair')
ok(len(U6.R) // 2 == 15, '4-5 P6: 15 blues for one filling')
ok(54 // 3 == 18, '3x hexagon all in reds: 18; fewest filling: 6 yellows + 6 reds')

print(f'\nall {n_ok} checks passed in {time.time() - t0:.0f} s; answer pictures in {OUT}')
