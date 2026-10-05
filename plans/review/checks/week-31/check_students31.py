"""Week 31 (hidden orchard): read every student diagram back from the delivered
PDFs and solve every student problem independently.

Covers week-31-k-1.pdf, week-31-grades-2-3.pdf, week-31-grades-4-5.pdf and the
bonus companion week-31-bonus.pdf.  Diagram facts (dot lattices, rings, lines,
labels) come from the PDFs' vector content via pdf31.py; answers come from the
brute-force lattice functions in orchard31.py.
Run: python3 check_students31.py   (writes out_check_students31.txt beside itself)
"""
import os as _os
import re
import sys
from math import gcd

HERE = _os.path.dirname(_os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdf31 as P  # noqa: E402
import orchard31 as M  # noqa: E402

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


CM = P.PT_PER_CM
SPACINGS = [s * CM for s in (0.9, 2.0, 0.7, 0.65)]
PAGES = {}
for band, path in P.PDFS.items():
    doc = P.open_pdf(path)
    PAGES[band] = []
    for page in doc:
        S = P.read_page(page)
        S['grids'] = P.grids(S['dots'], SPACINGS)
        S['fulltext'] = ' '.join(page.get_text().split())
        PAGES[band].append(S)
    say(f'{band}: {len(PAGES[band])} pages read from {_os.path.relpath(path, P.ROOT)}')


def ring_points(S, gi):
    g = S['grids'][gi]
    pts = []
    for r in S['rings']:
        if P.in_grid(g, r['x'], r['y']):
            (a, b), err = P.lattice_of(g, r['x'], r['y'])
            if err < 0.02:
                pts.append((a, b))
    return sorted(pts)


def grid_ok(S, gi, n, spacing_cm, what):
    g = S['grids'][gi]
    sx = sorted(set(round(v, 2) for v in g['sx']))
    sy = sorted(set(round(v, 2) for v in g['sy']))
    check(g['cols'] == n + 1 and g['rows'] == n + 1 and g['n'] == (n + 1) ** 2,
          f'{what}: {n + 1} x {n + 1} dots (found {g["cols"]} x {g["rows"]}, {g["n"]} dots)')
    check(all(abs(v - spacing_cm * CM) < 0.1 for v in sx + sy),
          f'{what}: equal spacing {spacing_cm} cm across and up (found x {sorted(sx)} pt, y {sorted(sy)} pt)')


def axis_labels_ok(S, gi, n, what):
    g = S['grids'][gi]
    s = g['sx'][0]
    xs_found, ys_found, o_found = [], [], False
    for t in S['texts']:
        if t['t'].isdigit():
            # below the bottom row, under a column
            if 0 < t['y'] - g['y0'] < 0.5 * s + 6:
                (a, b), err = P.lattice_of(g, t['x'], g['y0'])
                if 0 <= a <= n and abs(t['x'] - (g['x0'] + a * s)) < 2:
                    xs_found.append((a, int(t['t'])))
            if 0 < g['x0'] - t['x'] < 0.5 * s + 8:
                (a, b), err = P.lattice_of(g, g['x0'], t['y'])
                if 0 <= b <= n and abs(t['y'] - (g['y0'] - b * s)) < 2:
                    ys_found.append((b, int(t['t'])))
        if t['t'] == 'O' and abs(t['y'] - g['y0']) < 4 and 0 < g['x0'] - t['x'] < 20:
            o_found = True
    check(sorted(xs_found) == [(a, a) for a in range(n + 1)], f'{what}: across labels 0..{n} under their columns')
    want_y = [(b, b) for b in range(1, n + 1)]
    check(sorted(v for v in ys_found if v[0] > 0) == want_y, f'{what}: up labels 1..{n} beside their rows')
    return o_found


def pts_str(L):
    return ', '.join(f'({a},{b})' for a, b in L) if L else 'none'


def parse_pairs(s):
    return [(int(a), int(b)) for a, b in re.findall(r'\((\d+), (\d+)\)', s)]


# ------------------------------------------------------------------ shared start
def check_start(band, S):
    say(f'-- {band} p. 1 launch examples')
    g0, g1 = S['grids'][0], S['grids'][1]
    for gi in (0, 1):
        grid_ok(S, gi, 4, 0.9, f'{band} p1 example {gi + 1}')
        o = axis_labels_ok(S, gi, 4, f'{band} p1 example {gi + 1}')
        check(o, f'{band} p1 example {gi + 1}: O label at the origin')
    check(ring_points(S, 0) == [(2, 1), (4, 2)], f'{band} p1 "hidden" example rings at (2,1) and (4,2)')
    check(ring_points(S, 1) == [(3, 2)], f'{band} p1 "visible" example ring at (3,2)')
    seg = {}
    for l in S['lines']:
        for gi in (0, 1):
            g = S['grids'][gi]
            if P.in_grid(g, l['x0'], l['y0']) and P.in_grid(g, l['x1'], l['y1']):
                a, ea = P.lattice_of(g, l['x0'], l['y0'])
                b, eb = P.lattice_of(g, l['x1'], l['y1'])
                if ea < .01 and eb < .01 and a != b:
                    seg[gi] = (a, b)
    check(seg.get(0) == ((0, 0), (4, 2)), f'{band} p1 hidden thread runs exactly O->(4,2): {seg.get(0)}')
    check(seg.get(1) == ((0, 0), (3, 2)), f'{band} p1 visible thread runs exactly O->(3,2): {seg.get(1)}')
    check(M.between((0, 0), (4, 2)) == [(2, 1)], 'hidden example: the only dot between O and (4,2) is (2,1) = B')
    check(M.between((0, 0), (3, 2)) == [], 'visible example: no dot between O and (3,2)')
    # labels T and B next to the right rings
    for lab, gi, target in (('T', 0, (4, 2)), ('B', 0, (2, 1)), ('T', 1, (3, 2))):
        g = S['grids'][gi]
        cands = [t for t in S['texts'] if t['t'] == lab and P.in_grid(g, t['x'], t['y'])]
        best = None
        for t in cands:
            (a, b), _ = P.lattice_of(g, t['x'], t['y'])
            tx = g['x0'] + target[0] * g['sx'][0]
            ty = g['y0'] - target[1] * g['sx'][0]
            d = ((t['x'] - tx) ** 2 + (t['y'] - ty) ** 2) ** .5 / g['sx'][0]
            best = d if best is None else min(best, d)
        check(best is not None and best < 0.5, f'{band} p1 label {lab} within half a spacing of its ring {target} (distance {best and round(best, 2)} spacings)')


def check_coord(band, S):
    say(f'-- {band} p. 2 coordinate example')
    grid_ok(S, 0, 4, 0.7, f'{band} p2 coordinate example')
    check(ring_points(S, 0) == [(4, 2)], f'{band} p2 coordinate example: ring at (4,2)')
    g = S['grids'][0]
    segs = []
    for l in S['lines']:
        if P.in_grid(g, l['x0'], l['y0']) and P.in_grid(g, l['x1'], l['y1']):
            a, ea = P.lattice_of(g, l['x0'], l['y0'])
            b, eb = P.lattice_of(g, l['x1'], l['y1'])
            if a != b and max(ea, eb) < .1:
                segs.append((a, b))
    check(((0, 0), (4, 0)) in segs and ((4, 0), (4, 2)) in segs,
          f'{band} p2 arrows O->(4,0) ("4 across") then (4,0)->(4,2) ("2 up"): {segs}')
    s = g['sx'][0]
    lab = [t for t in S['texts'] if t['t'] == '(4, 2)'][0]
    row_level = (g['y0'] - lab['y']) / s
    dist = ((lab['x'] - (g['x0'] + 4 * s)) ** 2 + (lab['y'] - (g['y0'] - 2 * s)) ** 2) ** .5 / s
    say(f'info {band} p2 label "(4, 2)" sits level with up = {row_level:.2f} '
        f'(ring is at up = 2) and {dist:.2f} spacings ({dist * s / CM:.1f} cm) from the ring')
    check(abs(row_level - 2) < 0.4, f'{band} p2 label "(4, 2)" level with the ringed row 2 (it is level with {row_level:.2f})')


# ------------------------------------------------------------------ K-1
K = PAGES['K-1']
say('\n== K-1')
check_start('K-1', K[0])
say('-- K-1 P1 (p. 1)')
grid_ok(K[0], 2, 4, 2.0, 'K-1 P1 board')
axis_labels_ok(K[0], 2, 4, 'K-1 P1 board')
vis4 = [T for T in M.grid(4) if M.visible(T)]
say(f'K-1 P1 answer: {len(vis4)} visible dots on the 0..4 board: {pts_str(vis4)}')
check(len(vis4) == 13, 'K-1 P1: 13 visible dots')

say('-- K-1 P2 (p. 2)')
for gi in (0, 1):
    grid_ok(K[1], gi, 4, 2.0, f'K-1 P2 board {gi + 1}')
    axis_labels_ok(K[1], gi, 4, f'K-1 P2 board {gi + 1}')
    rp = ring_points(K[1], gi)
    say(f'K-1 P2 board {gi + 1} circled targets: {pts_str(rp)}')
    for T in rp:
        b = M.between((0, 0), T)
        say(f'   {T}: ' + (f'hidden, nearest blocker {b[0]}, all blockers {pts_str(b)}' if b else 'visible'))
K2 = {gi: ring_points(K[1], gi) for gi in (0, 1)}
check(K2[0] == sorted([(4, 4), (4, 2), (2, 4), (3, 3)]), 'K-1 P2 board 1 targets (4,4),(4,2),(2,4),(3,3)')
check(K2[1] == sorted([(4, 0), (0, 4), (2, 2), (4, 3)]), 'K-1 P2 board 2 targets (4,0),(0,4),(2,2),(4,3)')
check(sum(1 for T in K2[0] + K2[1] if M.visible(T)) == 1, 'K-1 P2: exactly one circled target, (4,3), is visible')

say('-- K-1 P3 (p. 3)')
grid_ok(K[2], 0, 6, 2.0, 'K-1 P3 board')
axis_labels_ok(K[2], 0, 6, 'K-1 P3 board')
one = [T for T in M.grid(6) if len(M.between((0, 0), T)) == 1]
two = [T for T in M.grid(6) if len(M.between((0, 0), T)) == 2]
say(f'K-1 P3 exactly one dot between: {len(one)}: {pts_str(sorted(one))}')
say(f'K-1 P3 exactly two dots between: {len(two)}: {pts_str(sorted(two))}')
check(len(one) == 9 and len(two) == 5, 'K-1 P3: 9 targets with one dot between, 5 with two')
check(all(gcd(*T) == 2 for T in one) and all(gcd(*T) == 3 for T in two), 'K-1 P3: these are gcd 2 and gcd 3')

say('-- K-1 P4 (p. 4)')
grid_ok(K[3], 0, 6, 2.0, 'K-1 P4 board')
for y in range(0, 7):
    row = [(x, y) for x in range(7) if (x, y) != (0, 0)]
    v = [T for T in row if M.visible(T)]
    h = [T for T in row if not M.visible(T)]
    say(f'   row {y}: visible x = {[T[0] for T in v]}, hidden x = {[T[0] for T in h]}')
allvis = [y for y in range(7) if all(M.visible((x, y)) for x in range(7) if (x, y) != (0, 0))]
nohidden = [y for y in range(7) if not any(not M.visible((x, y)) for x in range(7) if (x, y) != (0, 0))]
check(all(M.visible((1, y)) for y in range(1, 7)), 'K-1 P4: (1,y) is visible in every row above O')
check(allvis == [1], f'K-1 P4: the only all-visible row is row 1 (found {allvis})')
check(nohidden == [1], 'K-1 P4: so "a hidden dot in every row" fails exactly at row 1 (answer: no)')

say('-- K-1 P5 (p. 5)')
grid_ok(K[4], 0, 6, 2.0, 'K-1 P5 board')
firsts = [F for F in M.grid(6) if M.visible(F)]
hc = {F: len(M.hides(F, 6)) for F in firsts}
best = max(hc.values())
tie = sorted(F for F in firsts if hc[F] == best)
say(f'K-1 P5: hide counts by first dot (only nonzero): ' + ', '.join(f'{F}:{c}' for F, c in sorted(hc.items()) if c))
check(best == 5 and tie == [(0, 1), (1, 0), (1, 1)], f'K-1 P5: max {best} hidden, tie {tie}')
check(sorted(set(hc.values())) == [0, 1, 2, 5], 'K-1 P5: any other first dot hides at most 2')

# ------------------------------------------------------------------ 2-3
G = PAGES['2-3']
say('\n== Grades 2-3')
check_start('2-3', G[0])
say('-- 2-3 P1 (p. 1)')
grid_ok(G[0], 2, 6, 2.0, '2-3 P1 board')
axis_labels_ok(G[0], 2, 6, '2-3 P1 board')
vis6 = [T for T in M.grid(6) if M.visible(T)]
say(f'2-3 P1: {len(vis6)} visible on 0..6: {pts_str(vis6)}')
check(len(vis6) == 25, '2-3 P1: 25 visible dots')
check_coord('2-3', G[1])
say('-- 2-3 P2 (p. 2)')
grid_ok(G[1], 1, 6, 2.0, '2-3 P2 board')
m = re.search(r'Problem 2: Test these targets: (.*?)\. Find', G[1]['fulltext'])
T2 = parse_pairs(m.group(1))
check(T2 == [(6, 4), (6, 3), (5, 3), (5, 2), (4, 4), (4, 1)], f'2-3 P2 targets read from page: {T2}')
for T in T2:
    say(f'   {T}: between = {pts_str(M.between((0, 0), T))}')
check(all(max(T) <= 6 for T in T2), '2-3 P2: every target is on the printed 0..6 board')
say('-- 2-3 P3 (p. 3)')
grid_ok(G[2], 0, 6, 2.0, '2-3 P3 board')
say(f'2-3 P3 = K-1 P3 lists on the same 0..6 board: one blocker {len(one)}, two blockers {len(two)}')
say('-- 2-3 P4 (p. 4)')
grid_ok(G[3], 0, 6, 2.0, '2-3 P4 board')
m = re.search(r'Make groups for (.*?)\.', G[3]['fulltext'])
D4 = parse_pairs(m.group(1))
check(D4 == [(1, 1), (2, 1), (3, 2), (1, 2), (1, 0)], f'2-3 P4 named directions: {D4}')
for D in D4:
    say(f'   group {D}: {pts_str(M.same_ray_group(D, 6))}')
check(all(M.visible(D) for D in D4), '2-3 P4: every named direction is the first dot of its ray')
say('-- 2-3 P5 (p. 5)')
m = re.search(r'Use it to predict (.*?)\. Explain', G[4]['fulltext'])
T5 = parse_pairs(m.group(1))
check(T5 == [(12, 8), (10, 7), (15, 5), (11, 1)], f'2-3 P5 targets: {T5}')
for T in T5:
    b = M.between((0, 0), T)
    say(f'   {T}: ' + (f'hidden, first {b[0]}, {len(b)} blockers' if b else 'visible'))
rule_ok = all(M.visible(T) == (gcd(*T) == 1) for T in M.grid(25))
check(rule_ok, '2-3 P5: on 0..25, visible exactly when the coordinates share no factor > 1 (axes included)')
say('-- 2-3 P6 (p. 5)')
check(all(M.visible((x, 1)) for x in range(0, 300)), '2-3 P6: row 1 visible for x = 0..299')
for y in range(2, 7):
    check(sum(M.visible((x, y)) for x in range(0, 60)) >= 10, f'2-3 P6: row {y} also has many visible dots (x = 0..59)')
check(sum(M.visible((x, 0)) for x in range(1, 60)) == 1, '2-3 P6: row 0 has only one visible dot, so it is the one wrong answer')

# ------------------------------------------------------------------ 4-5
U = PAGES['4-5']
say('\n== Grades 4-5')
check_start('4-5', U[0])
say('-- 4-5 P1 (p. 1)')
grid_ok(U[0], 2, 6, 2.0, '4-5 P1 board')
counts = sorted(set(len(M.between((0, 0), T)) for T in M.grid(6)))
say(f'4-5 P1: blocker counts that occur on 0..6: {counts}')
check(counts == [0, 1, 2, 3, 4, 5], '4-5 P1: hidden targets with three different counts exist (1..5 available)')
check(len(set(len(M.between((0, 0), T)) for T in M.grid(6) if M.visible(T))) == 1,
      '4-5 P1: every visible target has 0 blockers, so "different numbers of blockers" can only apply to the hidden three')
check_coord('4-5', U[1])
say('-- 4-5 P2 (p. 2)')
grid_ok(U[1], 1, 6, 2.0, '4-5 P2 board')
m = re.search(r'every blocker: (.*?)\.', U[1]['fulltext'])
T2u = parse_pairs(m.group(1))
check(T2u == [(6, 4), (6, 3), (5, 3), (6, 6), (6, 0), (0, 6)], f'4-5 P2 targets: {T2u}')
for T in T2u:
    say(f'   {T}: first {M.first_point(T)}, blockers {pts_str(M.between((0, 0), T))}')
say('-- 4-5 P3 (p. 3)')
m = re.search(r'blockers for (.*?)\. Explain', U[2]['fulltext'])
T3u = parse_pairs(m.group(1))
check(T3u == [(12, 8), (15, 10), (21, 14), (25, 15), (13, 8)], f'4-5 P3 targets: {T3u}')
for T in T3u:
    say(f'   {T}: first {M.first_point(T)}, {len(M.between((0, 0), T))} blockers, gcd {gcd(*T)}')
say('-- 4-5 P4 (p. 3)')
both = True
for a in range(1, 41):
    for b in range(1, 41):
        bl = M.between((0, 0), (a, b))
        cd = [q for q in range(2, min(a, b) + 1) if a % q == 0 and b % q == 0]
        if bool(bl) != bool(cd):
            both = False
        for (u, v) in bl:
            from fractions import Fraction
            t = Fraction(u, a)
            if t.denominator == 1 or a % t.denominator or b % t.denominator:
                both = False
            if Fraction(v, b) != t:
                both = False
        for q in cd:
            if (a // q, b // q) not in bl:
                both = False
check(both, '4-5 P4: for 1 <= a, b <= 40, a common divisor q > 1 gives blocker (a/q, b/q), and every blocker t(a,b) has a denominator > 1 dividing a and b (answer: yes)')
say('-- 4-5 P5 (p. 4)')
grid_ok(U[3], 0, 6, 2.0, '4-5 P5 board')
for T in ((6, 4), (6, 3), (6, 6)):
    F = M.first_point(T)
    grp = [Q for Q in M.grid(6) if Q[0] >= 1 and Q[1] >= 1 and M.first_point(Q) == F]
    say(f'   same first visible dot as {T} (= {F}): {pts_str(sorted(grp))}')
part = {}
for Q in M.grid(6):
    part.setdefault(M.first_point(Q), []).append(Q)
check(sum(len(v) for v in part.values()) == len(M.grid(6)), '4-5 P5: first-dot groups partition the board (no target in two groups)')
say('-- 4-5 P6 (p. 5)')
ok6 = all(M.first_point(T) == (T[0] // gcd(*T), T[1] // gcd(*T)) and len(M.between((0, 0), T)) == gcd(*T) - 1
          for T in M.grid(30))
check(ok6, '4-5 P6: on 0..30 (axes included), first dot = (a/d, b/d) and blockers = d - 1')
ok6b = all(M.between((0, 0), T) == [(k * T[0] // gcd(*T), k * T[1] // gcd(*T)) for k in range(1, gcd(*T))]
           for T in M.grid(20))
check(ok6b, '4-5 P6: on 0..20 the blockers are exactly k(a/d, b/d), k = 1..d-1 (no extra dots)')
say('-- 4-5 P7 (p. 5)')
check(all(M.visible((x, 1)) for x in range(0, 200)), '4-5 P7: row 1 entirely visible (x = 0..199)')
check(all(not M.visible((n, n)) for n in range(2, 60)), '4-5 P7: (n,n), n >= 2, all hidden')
check(len(M.between((0, 0), (100, 100))) == 99 and len(M.between((0, 0), (100, 0))) == 99,
      '4-5 P7: (100,100) and (100,0) have exactly 99 blockers')
check([y for y in range(0, 13) if all(M.visible((x, y)) for x in range(0, 40) if (x, y) != (0, 0))] == [1],
      '4-5 P7: row 1 is the only entirely visible row among rows 0..12')

# ------------------------------------------------------------------ bonus
B = PAGES['bonus']
say('\n== Bonus (Grades 2-5)')
say('-- bonus P1 (p. 1)')
S = B[0]
grid_ok(S, 0, 6, 2.0, 'bonus P1 board')
g = S['grids'][0]
L = [P.lattice_of(g, q['x'], q['y']) for q in S['squares']]
check([l[0] for l in L] == [(0, 0)], f'bonus P1: lookout L (filled square) at (0,0): {L}')
big = [r for r in S['rings'] if r['r'] > 2.8]
small = [r for r in S['rings'] if r['r'] <= 2.8]
Rl = [P.lattice_of(g, r['x'], r['y'])[0] for r in big]
check(Rl == [(1, 0)], f'bonus P1: lookout R (heavier ring) at (1,0): {Rl}')
tg = sorted(P.lattice_of(g, r['x'], r['y'])[0] for r in small)
check(tg == sorted([(x, y) for x in range(7) for y in (3, 6)]), 'bonus P1: target rings on every dot of rows 3 and 6')
lab = {t['t']: t for t in S['texts'] if t['t'] in ('lookout L', 'lookout R')}
check(abs(lab['lookout L']['x'] - g['x0']) < abs(lab['lookout L']['x'] - (g['x0'] + g['sx'][0])),
      'bonus P1: "lookout L" label is nearer x = 0 than x = 1')
check(abs(lab['lookout R']['x'] - (g['x0'] + g['sx'][0])) < 30, 'bonus P1: "lookout R" label starts at x = 1')
Lk, Rk = (0, 0), (1, 0)


def code(T):
    v = M.visible(T, Lk) + M.visible(T, Rk)
    return {2: 'B', 1: '1', 0: '0'}[v]


for y in (3, 6):
    say(f'   row {y} (across 0..6): ' + ','.join(code((x, y)) for x in range(7)))
check([y for y in (3, 6) for x in range(7) if code((x, y)) == '0'] == [6, 6], 'bonus P1: only (3,6),(4,6) are hidden from both')
say('-- bonus P2 (p. 1)')
dbl4 = [x for x in range(-300, 301) if code((x, 4)) == '0']
check(dbl4 == [], 'bonus P2: no target (x,4), -300 <= x <= 300, is hidden from both lookouts')
rows_dbl = [y for y in range(1, 31) if any(code((x, y)) == '0' for x in range(-60, 61))]
say(f'   rows 1..30 that have a doubly hidden target: {rows_dbl}')
pp = [y for y in range(2, 31) if len({p for p in range(2, y + 1) if y % p == 0 and all(p % q for q in range(2, p))}) == 1]
check(set(rows_dbl).isdisjoint(pp) and all(y in rows_dbl for y in range(2, 31) if y not in pp),
      'bonus P2 (guide claim): a row is doubly hidden somewhere exactly when its height is not a prime power')
check(sorted({x % 6 for x in range(-60, 61) if code((x, 6)) == '0'}) == [3, 4], 'bonus guide: on row 6, doubly hidden exactly at across = 3 or 4 mod 6')

say('-- bonus P3 (p. 2)')
S = B[1]
names = ['A', 'B', 'C', 'D']
check(len(S['grids']) == 4 and all(gr['cols'] == 4 and gr['rows'] == 4 for gr in S['grids']), 'bonus P3: four 4 x 4 grids')
tri = {}
for gi, gr in enumerate(S['grids']):
    grid_ok(S, gi, 3, 2.0, f'bonus P3 grid {names[gi]}')
    lab = [t for t in S['texts'] if t['t'] == names[gi]][0]
    check(abs(lab['x'] - gr['x0']) < 20 and 0 < lab['y'] - gr['y0'] < 40, f'bonus P3: label {names[gi]} under grid {gi + 1}')
    rp = []
    for r in S['rings']:
        (a, b), err = P.lattice_of(gr, r['x'], r['y'])
        if err < 0.02 and 0 <= a <= 3 and 0 <= b <= 3:
            rp.append((a, b))
    tri[names[gi]] = sorted(rp)
pts4 = [(x, y) for x in range(4) for y in range(4)]
for nm in names:
    A_, B_, C_ = tri[nm]
    side, inside = M.classify_triangle(A_, B_, C_, pts4)
    say(f'   {nm}: corners {pts_str(tri[nm])}, area {M.area2(A_, B_, C_) / 2}, side dots {pts_str(side)}, inside dots {pts_str(inside)}')
check(tri['A'] == [(0, 0), (0, 1), (1, 0)] and tri['B'] == [(0, 0), (1, 2), (3, 1)]
      and tri['C'] == [(0, 0), (0, 2), (2, 0)] and tri['D'] == [(0, 0), (1, 1), (2, 1)],
      'bonus P3: corners read from the rings')
# do other grids' dots fall inside any printed triangle?  (absolute page coordinates)
alldots = [(d['x'], -d['y']) for d in S['dots']]
for gi, nm in enumerate(names):
    gr = S['grids'][gi]
    s = gr['sx'][0]
    cs = [(gr['x0'] + a * s, -(gr['y0'] - b * s)) for a, b in tri[nm]]
    side, inside = M.classify_triangle_float(*cs, alldots, eps=0.05)
    own_side, own_inside = M.classify_triangle(*tri[nm], pts4)
    check(len(side) == len(own_side) and len(inside) == len(own_inside),
          f'bonus P3 {nm}: no dot of another grid lies on or inside the printed triangle')

say('-- bonus P4 (p. 3)')
S = B[2]
check(len(S['grids']) == 3 and all(gr['cols'] == 4 and gr['rows'] == 4 for gr in S['grids']), 'bonus P4: three 4 x 4 grids')
for gi in range(3):
    grid_ok(S, gi, 3, 2.0, f'bonus P4 grid {gi + 1}')
empt = []
for i in range(16):
    for j in range(i + 1, 16):
        for k in range(j + 1, 16):
            A_, B_, C_ = pts4[i], pts4[j], pts4[k]
            if M.area2(A_, B_, C_) == 0:
                continue
            side, inside = M.classify_triangle(A_, B_, C_, pts4)
            if not side and not inside:
                empt.append((A_, B_, C_))
areas = sorted(set(M.area2(*t) for t in empt))
shapes = sorted(set(M.shape_key(*t) for t in empt))
say(f'   empty triangles in a 4 x 4 grid: {len(empt)}, doubled areas {areas}, {len(shapes)} congruence shapes (squared sides): {shapes}')
check(areas == [1], 'bonus P4: every empty triangle in the printed grid has area 1/2 (no area larger than 1/2)')
check(len(shapes) >= 3, 'bonus P4: at least three different empty shapes fit')

say('-- bonus layout: gaps between neighbouring printed grids (pp. 2-3)')
for pn in (1, 2):
    S = B[pn]
    gs = S['grids']
    for i in range(len(gs)):
        for j in range(i + 1, len(gs)):
            a, b = gs[i], gs[j]
            s = a['sx'][0]
            # horizontal gap between facing columns when the row bands overlap
            ya = (a['ys'][-1], a['ys'][0]); yb = (b['ys'][-1], b['ys'][0])
            xa = (a['xs'][0], a['xs'][-1]); xb = (b['xs'][0], b['xs'][-1])
            if min(ya[1], yb[1]) - max(ya[0], yb[0]) > -1:
                gap = max(xb[0] - xa[1], xa[0] - xb[1])
                say(f'info p{pn + 1} grids {i + 1}-{j + 1} side by side: facing columns {gap / CM * 10:.1f} mm apart '
                    f'(dot spacing {s / CM * 10:.1f} mm, ratio {gap / s:.2f}); row offset {abs(a["y0"] - b["y0"]) / CM * 10:.1f} mm')
            elif min(xa[1], xb[1]) - max(xa[0], xb[0]) > -1:
                gap = max(yb[0] - ya[1], ya[0] - yb[1])
                off = (b['x0'] - a['x0']) / s
                say(f'info p{pn + 1} grids {i + 1}-{j + 1} one above the other: facing rows {abs(gap) / CM * 10:.1f} mm apart '
                    f'(dot spacing {s / CM * 10:.1f} mm, ratio {abs(gap) / s:.2f}); column offset {off:.2f} spacings')

say('-- bonus worked direction card example and P5 (p. 4)')
S = B[3]
ft = S['fulltext']
check('(2 , 1)' in ft or '(2,1)' in ft.replace(' ', ''), 'bonus p4 example cards present')
g = S['grids'][0]
check(g['cols'] == 4 and g['rows'] == 3 and all(abs(v - 0.65 * CM) < 0.1 for v in g['sx'] + g['sy']),
      'bonus p4 example dot grid 4 x 3 at 0.65 cm both ways')
rp = [P.lattice_of(g, r['x'], r['y'])[0] for r in S['rings']]
check(rp == [(3, 2)], f'bonus p4 example ring at (3,2) = 3 across, 2 up: {rp}')
longest = max([l for l in S['lines'] if P.in_grid(g, l['x0'], l['y0']) and P.in_grid(g, l['x1'], l['y1'])], key=lambda l: (l['x1'] - l['x0']) ** 2 + (l['y1'] - l['y0']) ** 2)
a0, e0 = P.lattice_of(g, longest['x0'], longest['y0'])
a1, e1 = P.lattice_of(g, longest['x1'], longest['y1'])
check(a0 == (0, 0) and a1 == (3, 2), f'bonus p4 example arrow O -> (3,2) (shaft ends {e1:.2f} spacing short for the head)')
check(M.det((2, 1), (1, 1)) in (1, -1), 'bonus p4 example: (2,1),(1,1) are a legal neighbour pair (|det| = 1)')
k, row = M.insertions_to_contain([(4, 3), (3, 4)])
say(f'bonus P5: fewest insertions to contain (4,3) and (3,4): {k}; a row: {row}')
boxes = [b for b in S['boxes'] if 60 < b['x1'] - b['x0'] < 75]
say(f'bonus P5: blank recording boxes on the page: {len(boxes)}')
check(k == 7 and len(boxes) >= k, 'bonus P5: 7 new cards needed, at least 7 blank boxes printed')
cards = M.all_cards(14)
check(all(gcd(*w) == 1 and abs(M.det(u, w)) == 1 and abs(M.det(w, v)) == 1 for w, u, v in cards),
      f'bonus P5: all {len(cards)} cards producible within 14 levels are coprime and keep |det| = 1 with both neighbours')
check(all(w != (4, 2) for w, u, v in cards), 'bonus P5: (4,2) never appears (14 levels)')
say('-- bonus P6 (p. 4)')
cop = [(a, b) for a in range(1, 7) for b in range(1, 7) if gcd(a, b) == 1]
okp6 = True
for T in cop:
    steps, row = M.wedge_search(T)
    if steps is None or steps[-1] != T or max(max(s) for s in steps) > 6:
        okp6 = False
check(okp6 and len(cop) == 23, f'bonus P6: the wedge procedure reaches all {len(cop)} coprime targets with 1 <= a, b <= 6, never building a card above 6')
reach6 = {w for w, u, v in cards if max(w) <= 6}
check(reach6 == set(cop), 'bonus P6: the cards with coordinates <= 6 are exactly the 23 coprime targets, each once')

say('')
say(f'{len(FAIL)} failures')
for f in FAIL:
    say('FAILED: ' + f)
with open(_os.path.join(HERE, 'out_check_students31.txt'), 'w') as fh:
    fh.write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
