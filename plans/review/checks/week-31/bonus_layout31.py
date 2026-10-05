"""Week 31 bonus pp. 2-3: what happens if a child treats the printed 4 x 4 grids
that sit close together as one dot field.

Reads every printed dot from week-31-bonus.pdf (page coordinates), then lists
triangles whose corners are printed dots in two different grids and that have
no other printed dot on a side or inside -- "empty" by the page's own
definition.  For each such triangle it reports the area in grid squares
(20 mm x 20 mm).  Within one grid every empty triangle has area 1/2; across
grids the areas differ, so the pages' layout lets the P4 question
("Can an empty triangle have area larger than half a grid square?") get a
misleading answer.
Run: python3 bonus_layout31.py   (writes out_bonus_layout31.txt beside itself)
"""
import os as _os
import sys
from itertools import combinations

HERE = _os.path.dirname(_os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdf31 as P  # noqa: E402
import orchard31 as M  # noqa: E402

OUT = []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


CM = P.PT_PER_CM
doc = P.open_pdf(P.PDFS['bonus'])
for pn in (1, 2):  # 0-based: page 2 (P3) and page 3 (P4)
    S = P.read_page(doc[pn])
    gs = P.grids(S['dots'], [2.0 * CM])
    s = 2.0 * CM
    dots = []
    for gi, g in enumerate(gs):
        for d in S['dots']:
            if P.in_grid(g, d['x'], d['y'], margin=0.1):
                (a, b), err = P.lattice_of(g, d['x'], d['y'])
                dots.append((gi, (a, b), (d['x'] / s, -d['y'] / s)))
    say(f'== bonus page {pn + 1}: {len(gs)} grids, {len(dots)} dots (coordinates in grid units)')
    pts = [p for _, _, p in dots]
    found = []
    for i, j, k in combinations(range(len(dots)), 3):
        gset = {dots[i][0], dots[j][0], dots[k][0]}
        if len(gset) < 2:
            continue
        A, B, C = dots[i][2], dots[j][2], dots[k][2]
        ar = abs((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])) / 2
        if ar < 0.02:
            continue
        side, inside = M.classify_triangle_float(A, B, C, pts, eps=0.002)
        if side or inside:
            continue
        found.append((ar, [(dots[t][0] + 1, dots[t][1]) for t in (i, j, k)]))
    found.sort(reverse=True)
    big = [f for f in found if f[0] > 0.5 + 1e-3]
    small = [f for f in found if f[0] < 0.5 - 1e-3]
    say(f'cross-grid "empty" triangles: {len(found)}; area > 1/2: {len(big)}; area < 1/2: {len(small)}')
    for ar, cs in found[:6]:
        say(f'   area {ar:.3f} grid squares: corners ' + ', '.join(f'grid {g} {c}' for g, c in cs))
    for ar, cs in small[-3:]:
        say(f'   area {ar:.3f} grid squares: corners ' + ', '.join(f'grid {g} {c}' for g, c in cs))
    # the side-by-side pair only (grids 1 and 2 on each page)
    pair = [f for f in found if {g for g, _ in f[1]} == {1, 2}]
    pb = [f for f in pair if f[0] > 0.5 + 1e-3]
    say(f'side-by-side grids 1 and 2 only: {len(pair)} cross-grid empty triangles, {len(pb)} with area > 1/2, '
        f'areas from {min(f[0] for f in pair):.3f} to {max(f[0] for f in pair):.3f}')
    for ar, cs in pb[:3]:
        say(f'   area {ar:.3f}: corners ' + ', '.join(f'grid {g} {c}' for g, c in cs))
    # triangles that stay near the narrow gap: grid 1 columns 2-3 and grid 2 columns 0-1
    near = [f for f in pair if all((g == 1 and c[0] >= 2) or (g == 2 and c[0] <= 1) for g, c in f[1])]
    nb_ = [f for f in near if f[0] > 0.5 + 1e-3]
    say(f'   of these, using only the two columns each side of the gap: {len(near)}, {len(nb_)} with area > 1/2')
    for ar, cs in sorted(nb_, key=lambda f: (-f[0]))[:3]:
        say(f'   area {ar:.3f}: corners ' + ', '.join(f'grid {g} {c}' for g, c in cs))
    # the simplest sliver: last column of grid 1, first column of grid 2
    want = [(1, (3, 0)), (2, (0, 0)), (1, (3, 1))]
    for ar, cs in found:
        if sorted(cs) == sorted(want):
            say(f'   sliver grid 1 (3,0), grid 2 (0,0), grid 1 (3,1): empty by the page definition, area {ar:.3f} grid squares')

with open(_os.path.join(HERE, 'out_bonus_layout31.txt'), 'w') as fh:
    fh.write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
