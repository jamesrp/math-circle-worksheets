#!/usr/bin/env python3
"""Check every claim, key and count changed by the October 23, 2026 card fixes (W65 v3).

Run from anywhere: python3 review/verify_card_fixes_2026_10_23.py [students.pdf facilitator.pdf]
It rebuilds the {8,4} tiling to depth 3 by reflection (its own construction, using only the
seed octagon from student/geometry.py), then checks:
  - the guide's turning rule: left minus right quarter-turns around n rooms is 4 + 4n on the
    octagon floor and 4 on squares, for every connected cluster of up to 4 rooms containing
    Home whose outside is one simple closed walk; the named cases (17/1, 5/1);
  - Problem 2's ready-pair answer: no full return (position and facing) in fewer than 8 moves
    with any turns, and no odd return, since the corner graph is two-colourable;
  - Problem 6's key: 48 rooms first reached in 2 crossings on octagons, 8 on squares,
    and 56 routes with 8 rooms reached twice;
  - the moved R label is nearer R than any other drawn street;
  - the printed wording and numbering in the generated TeX and the guide source, and, when
    the two PDFs are given, in the PDFs.
"""
import cmath, re, sys
from collections import Counter, deque
from itertools import combinations
from math import sqrt, pi
from pathlib import Path

WEEK = Path(__file__).resolve().parent.parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(WEEK/'student'))
from geometry import V, reflect, full_ends, circle  # noqa: E402

_points = {}
def key(z, tol=1e-9):
    """One id per point: points within tol share an id, even across a rounding boundary."""
    gx, gy = round(z.real*1e6), round(z.imag*1e6)
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for w, ident in _points.get((gx+dx, gy+dy), []):
                if abs(w - z) < tol: return ident
    ident = len(_points.setdefault('all', [])); _points['all'].append(z)
    _points.setdefault((gx, gy), []).append((z, ident)); return ident

# ---- the tiling to depth 3, with tile adjacency by shared edge
tiles = [(0j, list(V), 0)]; index = {key(0j): 0}
for i in range(10**6):
    if i >= len(tiles): break
    c, poly, d = tiles[i]
    if d >= 3: continue
    for k in range(8):
        p, q = poly[k], poly[(k+1) % 8]
        z = reflect(c, p, q)
        if key(z) not in index:
            index[key(z)] = len(tiles); tiles.append((z, [reflect(w, p, q) for w in poly], d+1))
assert Counter(d for _, _, d in tiles) == {0: 1, 1: 8, 2: 48, 3: 280}   # 280 = 6*48 - 8
edge_tiles = {}
for i, (_, poly, _) in enumerate(tiles):
    for k in range(8):
        edge_tiles.setdefault(frozenset((key(poly[k]), key(poly[(k+1) % 8]))), set()).add(i)
adj = {i: set() for i in range(len(tiles))}
for e, ts in edge_tiles.items():
    assert len(ts) <= 2
    for a, b in combinations(sorted(ts), 2): adj[a].add(b); adj[b].add(a)
assert all(len(adj[i]) == 8 for i, t in enumerate(tiles) if t[2] <= 2)

# ---- Problem 6: rooms first reached in exactly 2 crossings
dist = {0: 0}; dq = deque([0])
while dq:
    u = dq.popleft()
    if dist[u] == 2: continue
    for v in adj[u]:
        if v not in dist: dist[v] = dist[u]+1; dq.append(v)
layers = Counter(dist.values())
assert layers == {0: 1, 1: 8, 2: 48}, layers
routes = Counter(w for v in adj[0] for w in adj[v] if w != 0)
assert sum(routes.values()) == 56 and Counter(routes.values()) == {1: 40, 2: 8}
sq = lambda x, y: [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
sq_routes = Counter(w for v in sq(0, 0) for w in sq(*v) if w != (0, 0))
assert sum(sq_routes.values()) == 12 and Counter(sq_routes.values()) == {1: 4, 2: 4}
assert len(sq_routes) == 8 and all(abs(x)+abs(y) == 2 for x, y in sq_routes)
assert all(max(abs(x), abs(y)) <= 2 for x, y in sq_routes)   # all fit the printed 5 x 5 floor

# ---- turning around clusters: a corner vertex with k cluster corners turns 2 - k quarter-turns
def outside(corner_lists, edges_of):
    corners = Counter(key(z) for poly in corner_lists for z in poly)
    count = Counter(e for poly in corner_lists for e in edges_of(poly))
    bd = [e for e, m in count.items() if m == 1]
    deg = Counter(v for e in bd for v in e)
    if any(m != 2 for m in deg.values()): return None          # outside touches itself
    nbr = {}
    for e in bd:
        a, b = tuple(e); nbr.setdefault(a, []).append(b); nbr.setdefault(b, []).append(a)
    start = next(iter(nbr)); seen = {start}; prev, cur = None, start
    while True:
        nxt = next(v for v in nbr[cur] if v != prev)
        if nxt == start: break
        seen.add(nxt); prev, cur = cur, nxt
    if len(seen) != len(nbr): return None                       # more than one outside walk
    turns = Counter(2 - corners[v] for v in nbr)
    return turns[1], turns[0], turns[-1]                        # left, straight, right

oct_edges = lambda poly: [frozenset((key(poly[k]), key(poly[(k+1) % 8]))) for k in range(8)]
def oct_cluster(ids): return outside([tiles[i][1] for i in ids], oct_edges)
def sq_poly(c): x, y = c; return [complex(x, y), complex(x+1, y), complex(x+1, y+1), complex(x, y+1)]
sq_edges = lambda poly: [frozenset((key(poly[k]), key(poly[(k+1) % 4]))) for k in range(4)]
def sq_cluster(cells): return outside([sq_poly(c) for c in cells], sq_edges)

def connected_clusters(start, nbrs, size):
    found = {frozenset([start])}; frontier = set(found)
    for _ in range(size-1):
        frontier = {c | {w} for c in frontier for v in c for w in nbrs(v) if w not in c}
        found |= frontier
    return found
checked = Counter()
for cl in connected_clusters(0, lambda i: adj[i], 4):
    t = oct_cluster(cl)
    if t is None: continue
    assert t[0] - t[2] == 4 + 4*len(cl), (sorted(cl), t); checked[('oct', len(cl))] += 1
for cl in connected_clusters((0, 0), lambda c: sq(*c), 4):
    t = sq_cluster(cl)
    if t is None: continue
    assert t[0] - t[2] == 4, (sorted(cl), t); checked[('sq', len(cl))] += 1
assert checked[('oct', 4)] > 0 and checked[('sq', 4)] > 0

# The named cases: four rooms at the corner P = V[0], as on the Problem 5 board.
P = V[0]
four = [i for i, t in enumerate(tiles) if any(abs(z-P) < 1e-9 for z in t[1])]
assert len(four) == 4 and 0 in four
nbrs0 = [i for i in four if i in adj[0]]; star = next(i for i in four if i != 0 and i not in adj[0])
assert len(nbrs0) == 2
A = nbrs0[0]
assert oct_cluster([0]) == (8, 0, 0)
assert oct_cluster([0, A]) == (12, 2, 0)                  # Problem 3: 12 left, 2 straight
assert oct_cluster([0, A, star]) == (17, 2, 1)            # guide: 17 left and 1 right
assert oct_cluster(four) == (20, 4, 0)                    # n = 4: 20 = 4 + 16
assert sq_cluster([(0, 0)]) == (4, 0, 0) and sq_cluster([(0, 0), (1, 0)]) == (4, 2, 0)
assert sq_cluster([(0, 0), (1, 0), (0, 1)]) == (5, 2, 1)  # guide: L of three squares, 5 left and 1 right
# Gauss-Bonnet in quarter-turns: each octagon has area 6*pi - 8*(pi/2) = 2*pi = 4 quarter-turns.
assert abs((6*pi - 8*pi/2) - 2*pi) < 1e-12

# ---- Problem 2 ready pair: shortest full return is 8; never odd
# Recentre at the corner A = V[0] and grow four rings of rooms around its four rooms, so every
# corner within 4 roads of A has all four of its roads (checked below).
phi = lambda z: (z - V[0])/(1 - V[0].conjugate()*z)
ctiles = [(phi(tiles[i][0]), [phi(z) for z in tiles[i][1]], 0) for i in four]
cindex = {key(c): j for j, (c, _, _) in enumerate(ctiles)}
for i in range(10**6):
    if i >= len(ctiles): break
    c, poly, d = ctiles[i]
    if d >= 4: continue
    for k in range(8):
        p, q = poly[k], poly[(k+1) % 8]
        z = reflect(c, p, q)
        if key(z) not in cindex:
            cindex[key(z)] = len(ctiles); ctiles.append((z, [reflect(w, p, q) for w in poly], d+1))
vadj = {}
for _, poly, _ in ctiles:
    for k in range(8):
        a, b = key(poly[k]), key(poly[(k+1) % 8]); vadj.setdefault(a, set()).add(b); vadj.setdefault(b, set()).add(a)
A0, B0 = key(phi(V[0])), key(phi(V[1]))
vd = {A0: 0}; dq = deque([A0])
while dq:
    u = dq.popleft()
    for v in vadj[u]:
        if v not in vd: vd[v] = vd[u]+1; dq.append(v)
assert all(len(vadj[v]) == 4 for v, d in vd.items() if d <= 4)   # complete degree-4 graph near A
state = {(A0, B0)}; returns = []
for L in range(1, 10):   # a closed walk of length <= 9 visits only corners within distance 4 of A
    state = {(v, w) for (u, v) in state for w in vadj[v] if w != u}
    if (A0, B0) in state: returns.append(L)
assert returns == [8], returns
# Two colours by distance from A: no road joins two corners at the same distance, so every
# closed walk in this region is even. (Far out, near the map's edge, floating point is too
# coarse to join corners reliably, so the check covers the corners within 10 roads of A.)
colour = {v: d % 2 for v, d in vd.items() if d <= 10}
assert all(colour[u] != colour[v] for u in colour for v in vadj[u] if v in colour)

# ---- the R label (Problem 4 board): nearer R than any other drawn street
def dist_to_line(z, p, q):
    cr = circle(p, q)
    if cr is None:
        e = (q-p)/abs(q-p); return abs((z.conjugate()*e).imag)
    c, r2 = cr; return abs(abs(z-c) - sqrt(r2))
label = complex(-0.66, 0); old = complex(-0.77, 0.08); scale_mm = 2.92*25.4
dR = dist_to_line(label, V[3], V[4])*scale_mm
others = min(dist_to_line(label, V[k], V[(k+1) % 8]) for k in range(8) if k != 3)*scale_mm
assert dR < others and abs(label) < 1, (dR, others)
old_R = dist_to_line(old, V[3], V[4])*scale_mm; old_23 = dist_to_line(old, V[2], V[3])*scale_mm
assert old_23 < old_R            # the card's finding about the old position

# ---- printed wording and numbering
tex = (WEEK/'student'/'students.tex').read_text()
assert tex.count('W65-S-v4') == 7 and 'W65-S-v3' not in tex  # v4 since the critic follow-up
assert re.findall(r'\\textbf\{Problem (\d)[:\s]', tex) == ['1', '2', '3', '4', '5', '5', '6']
for s in ['return to your starting place, facing the same way?', 'two different ordinary straight lines',
          r'\textbf{Problem 5 (continued)}', 'at (-0.66,0) {R}', r'scale=2.2] at', 'in 2 door crossings but not fewer',
          'Octagon floor:', 'Square floor:']:
    assert s in tex, s
for s in ['Mark dots where you go straight.', 'Extra workspace', 'starting place and heading']:
    assert s not in tex, s
guide = (WEEK/'guide'/'facilitator.tex').read_text()
for s in ['W65-FAC-v4', r'\(4+4n\)', 'Week~56', 'Week~61', 'K--1, adult-led on these pages',
          'fewer than 8 moves', 'two alternating colors', '17 left turns and 1 right', '5 left and 1 right',
          r'\(56-8=48\)', r'\(12-4=8\)', 'seven pages', '35 sheets', 'Problems 4--6',
          'corner of an index card']:
    assert s in guide, s
assert 'A general formula for larger clusters is not required' not in guide

if len(sys.argv) == 3:
    import pymupdf
    st = pymupdf.open(sys.argv[1]); gd = pymupdf.open(sys.argv[2])
    assert len(st) == 7 and len(gd) == 7
    text = [p.get_text() for p in st]
    assert all('W65-S-v4' in t and 'Week 65 / Hyperbolic octagon streets / Grades 3' in t for t in text)
    assert 'Problem 5 (continued)' in text[5] and 'Problem 6:' in text[6]
    assert all('W65-FAC-v4' in p.get_text() for p in gd)
    print('PDFs: 7 student pages and 7 guide pages, v4 footers, P5 continued on p. 6, P6 on p. 7.')

print('Clusters checked:', dict(sorted(checked.items())))
print('Layers 1, 8, 48; routes 56 = 40 once + 8 twice; squares 12 routes, 8 rooms.')
print('Full returns up to 9 moves:', returns, '- corner graph two-coloured,', len(colour), 'corners.')
print(f'R label: {dR:.1f} mm from R, {others:.1f} mm from the nearest other street '
      f'(old position: {old_R:.1f} mm from R, {old_23:.1f} mm from the v2v3 street).')
print('Wording, numbering and footers checked. All card-fix checks passed.')
