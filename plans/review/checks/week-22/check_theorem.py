"""General facts behind Week 22, checked exhaustively on finite grids.

These finite checks support (they cannot replace) the planar Radon proof:
 1. every placement of 4 labels on a 5 x 5 grid (coincidences allowed) has a
    successful split; success counts by kind of placement;
 2. general position <=> exactly one success (4-5 P5's "exactly one");
 3. the shared set never has positive area, and a positive-length shared
    segment happens only when all four labels are collinear (2-3 P3);
 4. three labels succeed iff their locations are collinear (incl. coincident);
    two labels iff they coincide; on a line three labels always succeed;
 5. random rational placements with small denominators (degenerate-heavy).

Output: out_check_theorem.txt
"""
import os
import random
import sys
from collections import Counter
from fractions import Fraction as Fr
from itertools import combinations, product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from geom import orient, successes, two_splits  # noqa: E402

LINES = []


def say(s=''):
    LINES.append(s)
    print(s)


def kind(pts):
    locs = list(pts.values())
    if len(set(locs)) < len(locs):
        return 'all coincide' if len(set(locs)) == 1 else 'some coincide'
    tri = sum(1 for a, b, c in combinations(locs, 3) if orient(a, b, c) == 0)
    if tri == 0:
        return 'general position'
    if tri == 4:
        return 'all four collinear'
    return 'one collinear triple'


grid = [(Fr(x), Fr(y)) for x in range(5) for y in range(5)]
stats = {}
violations = Counter()
for quad in product(grid, repeat=4):
    pts = dict(zip('ABCD', quad))
    s = successes(pts)
    k = kind(pts)
    stats.setdefault(k, Counter())[len(s)] += 1
    if not s:
        violations['no success'] += 1
    if any(v[0] == 'area' for v in s.values()):
        violations['positive-area overlap'] += 1
    if any(v[0] == 'segment' for v in s.values()) and k != 'all four collinear' and k != 'some coincide' and k != 'all coincide':
        violations['segment overlap without four collinear'] += 1
    if any(v[0] == 'segment' for v in s.values()):
        locs = list(pts.values())
        if not all(orient(a, b, c) == 0 for a, b, c in combinations(locs, 3)):
            violations['segment overlap with a non-collinear triple'] += 1
    # coincident pair: all four splits separating them succeed
    for x, y in combinations('ABCD', 2):
        if pts[x] == pts[y]:
            for g1, g2 in two_splits('ABCD'):
                if (x in g1) != (y in g1) and g1 + '|' + g2 not in s:
                    violations['coincident pair separated but failing'] += 1
say(f'1. 4 labels on the 5 x 5 grid: {25 ** 4} placements')
for k in ['general position', 'one collinear triple', 'all four collinear', 'some coincide', 'all coincide']:
    say(f'   {k:22s}: success counts {dict(sorted(stats[k].items()))}')
say(f'   violations (no success; positive-area overlap; shared segment with a non-collinear triple;')
say(f'   coincident pair separated but failing): {dict(violations) or "none"}')
say('3. so a shared segment of positive length needs all four locations collinear, and no overlap has area')
seven = sum(c for k, cc in stats.items() for n, c in cc.items() if n == 7)
say(f'   placements with all 7 splits successful: {seven} (all-coincide placements: {sum(stats["all coincide"].values())})')
ones = sum(stats['general position'].values())
say(f'2. exactly one success <=> general position: '
    f'{stats["general position"] == Counter({1: ones}) and all(n >= 2 for k, cc in stats.items() if k != "general position" for n in cc)}')

# three and two labels
c3 = Counter()
bad3 = 0
for tri in product(grid, repeat=3):
    pts = dict(zip('ABC', tri))
    ok = bool(successes(pts))
    col = orient(*tri) == 0
    c3[(col, ok)] += 1
    bad3 += ok != col
say(f'4. 3 labels on the grid ({25 ** 3}): success iff collinear-or-coincident: {bad3 == 0}  {dict(c3)}')
bad2 = sum(bool(successes(dict(zip('AB', pr)))) != (pr[0] == pr[1]) for pr in product(grid, repeat=2))
say(f'   2 labels: success iff coincident: {bad2 == 0}')
line = [(Fr(x), Fr(0)) for x in range(7)]
bad1 = sum(not successes(dict(zip('ABC', t))) for t in product(line, repeat=3))
say(f'   3 labels on a line (all {7 ** 3} placements on 7 positions): all succeed: {bad1 == 0}')
bad1b = sum(bool(successes(dict(zip('AB', t)))) != (t[0] == t[1]) for t in product(line, repeat=2))
say(f'   2 labels on a line: success iff coincident: {bad1b == 0}')

random.seed(22)
vals = [Fr(k, 3) for k in range(0, 13)]
fails = 0
cnt = Counter()
for _ in range(30000):
    pts = {l: (random.choice(vals), random.choice(vals)) for l in 'ABCD'}
    s = successes(pts)
    fails += not s
    cnt[(kind(pts), len(s))] += 1
say(f'5. 30000 random placements on a thirds lattice: placements with no success: {fails}')

# 4-5 P5 / 2-3 P4: there are general-position placements with different unique splits
say('   unique split realised as: ' + ', '.join(sorted({next(iter(successes(dict(zip("ABCD", q)))))
                                                        for q in product(grid[:9:2] + grid[10:20:3], repeat=4)
                                                        if kind(dict(zip("ABCD", q))) == "general position"})))

open(os.path.join(HERE, 'out_check_theorem.txt'), 'w').write('\n'.join(LINES) + '\n')
