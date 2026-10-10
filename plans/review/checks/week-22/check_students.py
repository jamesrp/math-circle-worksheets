"""Recompute every Week 22 student answer from the printed geometry.

Reads extracted.json (written by extract.py from the delivered PDFs), converts
the printed board coordinates to exact fractions and, for every fixed board,
lists every unordered split whose closed convex hulls meet, with the exact
shared point or segment. It also measures how far each failing split misses
(at actual print size), to flag near-misses a pencil drawing could blur.

Output: out_check_students.txt
"""
import json
import math
import os
import sys
from fractions import Fraction as Fr
from itertools import combinations, product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from geom import (P, hull, orient, successes, two_splits, fmt, fmt_shared, shared_set,  # noqa: E402
                  dist_to_segment, dist_to_line)

LINES = []


def say(s=''):
    LINES.append(s)
    print(s)


data = json.load(open(os.path.join(HERE, 'extracted.json')))


def pts_of(board, extra=None):
    out = {}
    for d in board['dots']:
        for lab in d['label'].replace(' ', '').split(','):
            out[lab] = P(d['x'], d['y'])
    if extra:
        out.update(extra)
    return out


def gap(pts, g1, g2):
    """Float distance between the hulls of two groups (0 if they meet)."""
    h1, h2 = hull([pts[x] for x in g1]), hull([pts[x] for x in g2])
    if shared_set(h1, h2) is not None:
        return 0.0

    def segs(h):
        if len(h) == 1:
            return [(h[0], h[0])]
        if len(h) == 2:
            return [(h[0], h[1])]
        return [(h[i], h[(i + 1) % len(h)]) for i in range(len(h))]
    best = math.inf
    for a, b in segs(h1):
        for c, d in segs(h2):
            best = min(best, dist_to_segment(a, c, d), dist_to_segment(b, c, d),
                       dist_to_segment(c, a, b), dist_to_segment(d, a, b))
    return best


def report(name, pts, scale_cm=1.0, expect=None):
    s = successes(pts)
    say(f'  {name}: ' + ', '.join(f"{k} [{fmt_shared(v)}]" for k, v in s.items()) + f'  -> {len(s)} successful')
    fails = []
    for g1, g2 in two_splits(sorted(pts)):
        k = g1 + '|' + g2
        if k not in s:
            fails.append((gap(pts, g1, g2) * scale_cm, k))
    fails.sort()
    if fails:
        say(f'      closest failing split: {fails[0][1]} misses by {fails[0][0] * 10:.1f} mm at print size')
    # collinearity / near-collinearity of distinct triples
    locs = sorted(set(pts.values()))
    near = []
    for a, b, c in combinations(locs, 3):
        for p, q, r in ((a, b, c), (b, c, a), (c, a, b)):
            near.append((dist_to_line(p, q, r) * scale_cm, p, q, r))
    near = [t for t in near if t[0] > 0]
    near.sort(key=lambda t: t[0])
    exact = sum(1 for a, b, c in combinations(locs, 3) if orient(a, b, c) == 0)
    if exact:
        say(f'      exactly collinear triples of locations: {exact}')
    if near:
        d, p, q, r = near[0]
        names = {v: k for k, v in pts.items()}
        say(f'      nearest non-collinear point-to-line among triples: {names[p]} to line {names[q]}{names[r]} = {d * 10:.2f} mm')
    if expect is not None:
        ok = set(s) == set(expect)
        say(f'      expected {sorted(expect)} -> {"OK" if ok else "MISMATCH"}')
    return s


def board(band, page, idx=0):
    bs = [b for b in data[band] if b['page'] == page]
    return bs[idx]


# --------------------------------------------------------------------------
say('K-1')
b = board('k-1', 1)
say(f" P1 (p1): A, B, C fixed; crosses {b['crosses']}")
for x, y in b['crosses']:
    report(f'D=({x:g},{y:g})', pts_of(b, {'D': P(x, y)}))
b = board('k-1', 2)
say(f" P2 (p2): crosses {b['crosses']}")
for x, y in b['crosses']:
    report(f'D=({x:g},{y:g})', pts_of(b, {'D': P(x, y)}))
rec = [bb for bb in data['k-1'] if bb['page'] == 3]
from collections import Counter  # noqa: E402
cnt = Counter(tuple(next(d for d in bb['dots'] if d['label'] == 'D').values())[1:3] for bb in rec)
say(f'  record page p3: {len(rec)} small boards; copies per D position: {dict(cnt)}')
b = board('k-1', 4)
say(' P3 (p4):')
report('line A D C B', pts_of(b))
say(f"  record page p5: {len([bb for bb in data['k-1'] if bb['page'] == 5])} small boards (+1 large = 7 = number of candidate splits)")
b = board('k-1', 6)
say(' P4 (p6): A, B, C fixed, D anywhere in the box')
base = pts_of(b)
N = 63   # every point of the 0.2 cm lattice in the 12.6 cm box, plus lines through the dots
minimum, worst = 9, None
counts = Counter()
for i in range(N + 1):
    for j in range(N + 1):
        D = (Fr(i, 5), Fr(j, 5))
        s = successes(dict(base, D=D))
        counts[len(s)] += 1
        if len(s) < minimum:
            minimum, worst = len(s), D
say(f'  {(N + 1) ** 2} lattice positions for D: fewest successes {minimum}; distribution {dict(sorted(counts.items()))}')
# guide p8: "if D is far enough beyond A, A may lie inside BCD" -- inside the box?
cands = []
for i in range(0, 64):
    for j in range(0, 64):
        D = (Fr(i, 5), Fr(j, 5))
        s = successes(dict(base, D=D))
        if list(s) == ['A|BCD']:
            cands.append(D)
say(f'  positions in the box where A|BCD is the only success: {len(cands)}, e.g. {[(fmt(x), fmt(y)) for x, y in cands[:3]]}')
b = board('k-1', 7)
say(f" P5 (p7): A, B fixed; crosses {b['crosses']}")
base = pts_of(b)
for x, y in b['crosses']:
    report(f'C=({x:g},{y:g})', dict(base, C=P(x, y)))
on_line, off_line, bad = 0, 0, []
for i in range(0, 127):
    for j in range(0, 127):
        C = (Fr(i, 10), Fr(j, 10))
        ok = bool(successes(dict(base, C=C)))
        if ok != (C[1] == base['A'][1]):
            bad.append(C)
        on_line += ok
say(f'  0.1 cm lattice (127 x 127): successful positions exactly those with y = {fmt(base["A"][1])}: {"yes" if not bad else bad[:5]}; count {on_line}')
for C in [base['A'], base['B']]:
    say(f'  C at {fmt(C[0])},{fmt(C[1])}: ' + ', '.join(successes(dict(base, C=C))))
say(' P6 (p8): free placement -- see check_theorem.py')

# --------------------------------------------------------------------------
say()
say('Grades 2-3')
b = board('grades-2-3', 1)
say(f" P1 (p1): crosses {b['crosses']}")
for x, y in b['crosses']:
    report(f'D=({x:g},{y:g})', pts_of(b, {'D': P(x, y)}))
b = board('grades-2-3', 2)
say(' P2 (p2):')
report('line A D B C', pts_of(b))
say(f"  record page p3: {len([bb for bb in data['grades-2-3'] if bb['page'] == 3])} small boards")
say(' P3 (p4): construction -- see check_theorem.py (positive-length overlap needs four collinear labels)')
say(' P4 (p5-6): construction -- guide witnesses checked in check_guide.py')
b = board('grades-2-3', 7)
say(' P5 (p7): printed three dots')
pts = pts_of(b)
report('A B C', pts)
A, B = pts['A'], pts['B']
slope = (B[1] - A[1]) / (B[0] - A[0])
y0 = A[1] - slope * A[0]
say(f'  locus: line y = {fmt(y0)} + ({fmt(slope)}) x; at x=0 y={fmt(y0)}, at x=63/5 y={fmt(y0 + slope * Fr(63, 5))}')
bad = []
for i in range(0, 127):
    for j in range(0, 127):
        C = (Fr(i, 10), Fr(j, 10))
        ok = bool(successes({'A': A, 'B': B, 'C': C}))
        if ok != (orient(A, B, C) == 0):
            bad.append(C)
say(f'  0.1 cm lattice: success exactly on line AB: {"yes" if not bad else bad[:5]}')
say(' P6 (p8): free placement -- see check_theorem.py')

# --------------------------------------------------------------------------
say()
say('Grades 4-5')
b = board('grades-4-5', 1)
say(f" P1 (p1): crosses {b['crosses']}")
for x, y in b['crosses']:
    report(f'D=({x:g},{y:g})', pts_of(b, {'D': P(x, y)}))
b = board('grades-4-5', 2)
say(' P2 (p2): sloping line')
pts = pts_of(b)
say(f"  collinear: {all(orient(pts['A'], pts['D'], pts[x]) == 0 for x in 'BC')}; order along line: "
    + ''.join(sorted(pts, key=lambda k: pts[k])))
report('A C B D', pts)
say(' P3 (p4): free placement -- see check_theorem.py')
b = board('grades-4-5', 5)
say(' P4 (p5): A and D share a location')
pts = pts_of(b)
report('A=D', pts)
say(' P5 (p7-9): constructions -- see check_theorem.py and check_guide.py')
say(' P6 (p10): theorem -- see check_theorem.py')
b = board('grades-4-5', 11)
say(' P7 (p11): printed three dots')
pts = pts_of(b)
report('A B C', pts)
say(f"  orientation (B-A) x (C-A) = {fmt(orient(pts['A'], pts['B'], pts['C']))}")

open(os.path.join(HERE, 'out_check_students.txt'), 'w').write('\n'.join(LINES) + '\n')
