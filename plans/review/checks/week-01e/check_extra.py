"""Extra checks for statements in the adult guide: the 0,1,2 numbering of the ring in the
4-5 Problem 7 explanation, and the game on the 1,3,3 hexagon ("the second player wins by
copying").  Writes check_extra.out."""
import os, sys, time
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import *
from fastgame import Board

log = Log(os.path.join(HERE, 'check_extra.out'))
big4 = stroked_boards('grades-4-5', 4, min_lw=1.5)[0]
R = big4.R
pts = Counter(v for c in R for v in c)
cx = sum(centroid(c)[0] for c in R) / len(R)
cy = sum(centroid(c)[1] for c in R) / len(R)
mid = min(pts, key=lambda p: (lcart(p)[0] - cx) ** 2 + (lcart(p)[1] - cy) ** 2)
H = unit_hex(mid)
ring = R - H
deg = Counter(len([d for d in ring if adjacent(c, d)]) for c in ring)
log(f'ring of the 2x hexagon: {len(ring)} cells; degrees inside the ring: {dict(deg)} (a single loop needs all 2)')
# walk the loop
start = next(iter(ring))
order = [start]
prev = None
cur = start
while True:
    nxt = [d for d in ring if adjacent(cur, d) and d != prev]
    nxt = [d for d in nxt if d not in order] or [d for d in nxt]
    d = nxt[0]
    if d == start:
        break
    order.append(d)
    prev, cur = cur, d
log(f'loop length {len(order)} (one loop through all ring cells: {len(order) == len(ring)})')
touch = [k for k, c in enumerate(order) if any(adjacent(c, h) for h in H)]
log(f'positions of the cells touching the middle along the loop: {touch}; differences mod 18: '
    f'{sorted(set((touch[(i + 1) % len(touch)] - touch[i]) % 18 for i in range(len(touch))))} (every third: all 3)')
# trapezoids that reach into the middle: what ring cells can they cover?
num = {}
r0 = touch[0] % 3
for k, c in enumerate(order):
    num[c] = (k - r0 + 2) % 3   # touching cells numbered 2
reach = [p for p in reds(R) if (p & H) and (p & ring)]
log(f'trapezoids reaching from the ring into the middle: {len(reach)}; ring numbers they cover: '
    f'{sorted(Counter(tuple(sorted(num[c] for c in p & ring)) for p in reach).items())}')
inside_ring = [p for p in reds(R) if p <= ring]
log(f'trapezoids inside the ring: {len(inside_ring)}; each covers one 0, one 1 and one 2: '
    f'{all(sorted(num[c] for c in p) == [0, 1, 2] for p in inside_ring)}')

o = stroked_boards('grades-4-5', 6, min_lw=1.5)[0]
t = time.time()
Bd = Board(o.R)
w, good, moves = Bd.solve()
ht = half_turn_centre(o.R)
log(f'game on the 1,3,3 hexagon (page 6 of grades 4-5): {describe(o.R)}; half-turn centre: {ht[1] if ht else None}; '
    f'winner {w}; {len(moves)} first moves; {time.time() - t:.1f} s')
log.save()
