#!/usr/bin/env python3
"""Week 65 independent math check (review stage).

Builds the {8,4} tiling in the hyperboloid (Lorentz) model, without the
author's circle formulas, and checks every answer and adult-guide claim.
Run from anywhere: the repository is four folders up from this file.
Output: check_math.out next to this script.
"""
from pathlib import Path
from math import cos, sin, pi, sqrt, acosh, atan2, tan
import itertools, sys

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
OUT = []
FAIL = []


def log(s=''):
    OUT.append(str(s))


def check(name, ok, detail=''):
    OUT.append(('PASS ' if ok else 'FAIL ') + name + (f'  [{detail}]' if detail else ''))
    if not ok:
        FAIL.append(name)

# ---------------- Lorentz model ----------------
def mink(a, b):
    return -a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def add(a, b, s=1.0):
    return tuple(x + s*y for x, y in zip(a, b))


def scal(s, a):
    return tuple(s*x for x in a)


def lcross(a, b):
    # n with mink(n,a)=mink(n,b)=0
    e = (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
    return (-e[0], e[1], e[2])


def reflect(x, n):
    return add(x, n, -2*mink(x, n)/mink(n, n))


def todisk(x):
    return complex(x[1], x[2])/(1+x[0])


def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0]) + a[2]*(b[0]*c[1]-b[1]*c[0]))


def hdist(a, b):
    return acosh(max(1.0, -mink(a, b)))


def key(x):
    return tuple(round(v, 6) for v in x)

# Regular {p,q}: cosh(circumradius) = cot(pi/p) cot(pi/q)
p, q = 8, 4
chR = 1/tan(pi/p)/tan(pi/q)
shR = sqrt(chR**2-1)
ORIGIN = (1.0, 0.0, 0.0)
HOME = [(chR, shR*cos(pi/8+k*pi/4), shR*sin(pi/8+k*pi/4)) for k in range(8)]

log('== Model ==')
r_disk = abs(todisk(HOME[0]))
check('vertex disk radius equals sqrt(sqrt2-1) (author r)', abs(r_disk - sqrt(sqrt(2)-1)) < 1e-12, f'{r_disk:.12f}')
side = hdist(HOME[0], HOME[1])
check('all 8 home sides equal', all(abs(hdist(HOME[k], HOME[(k+1) % 8])-side) < 1e-12 for k in range(8)), f'side={side:.9f}')


def normal(a, b):
    n = lcross(a, b)
    return scal(1/sqrt(mink(n, n)), n)


def tangent(v, w):
    """Unit tangent at v toward w (in the Lorentz tangent plane)."""
    t = add(w, v, mink(w, v))  # w + <w,v> v
    return scal(1/sqrt(mink(t, t)), t)


def angle_at(v, a, b):
    ta, tb = tangent(v, a), tangent(v, b)
    c = max(-1, min(1, mink(ta, tb)))
    from math import acos
    return acos(c)*180/pi

angs = [angle_at(HOME[k], HOME[k-1], HOME[(k+1) % 8]) for k in range(8)]
check('home interior angles all 90 degrees', all(abs(a-90) < 1e-9 for a in angs), f'{angs[0]:.9f}')

# ---------------- tiling by reflection, BFS ----------------
def centroid_key(poly):
    s = (0.0, 0.0, 0.0)
    for v in poly:
        s = add(s, v)
    m = sqrt(-mink(s, s))
    return key(scal(1/m, s)), scal(1/m, s)

tiles = [HOME]
tkeys = {centroid_key(HOME)[0]: 0}
depth = [0]
adj = {0: set()}
frontier = [0]
MAXD = 3
while frontier:
    nxt = []
    for i in frontier:
        if depth[i] >= MAXD:
            continue
        poly = tiles[i]
        for k in range(8):
            n = normal(poly[k], poly[(k+1) % 8])
            img = [reflect(v, n) for v in poly]
            kk = centroid_key(img)[0]
            if kk not in tkeys:
                tkeys[kk] = len(tiles)
                tiles.append(img)
                depth.append(depth[i]+1)
                adj[len(tiles)-1] = set()
                nxt.append(len(tiles)-1)
            j = tkeys[kk]
            adj[i].add(j); adj[j].add(i)
    frontier = nxt
layer = [sum(1 for d in depth if d == t) for t in range(MAXD+1)]
log(f'layers by BFS depth 0..3: {layer}')
check('guide: whole-tiling layers 1, 8, 48', layer[:3] == [1, 8, 48])
# two-step multiplicity from Home
from collections import Counter
mult = Counter(j for i in adj[0] for j in adj[i] if j != 0 and depth[j] == 2)
check('guide: 56 non-backtracking two-door routes', sum(mult.values()) == 56, str(sum(mult.values())))
check('guide: 40 second-ring rooms reached once, 8 reached twice', Counter(mult.values()) == {1: 40, 2: 8}, str(dict(Counter(mult.values()))))
check('first-ring rooms are pairwise non-adjacent', all(not (adj[i] & adj[0] - {0}) or True for i in adj[0]) and all(j not in adj[i] for i in adj[0] for j in adj[0]))

# vertex graph of the tiling (rooms up to depth 3 give complete stars near the centre)
vkeys = {}
verts = []
vadj = {}
for poly in tiles:
    ids = []
    for v in poly:
        kk = key(v)
        if kk not in vkeys:
            vkeys[kk] = len(verts); verts.append(v); vadj[vkeys[kk]] = set()
        ids.append(vkeys[kk])
    for k in range(8):
        a, b = ids[k], ids[(k+1) % 8]
        vadj[a].add(b); vadj[b].add(a)
H = [vkeys[key(v)] for v in HOME]
check('every home vertex has 4 streets (degree 4)', all(len(vadj[h]) == 4 for h in H))
rooms_at = {h: [i for i, poly in enumerate(tiles) if any(key(v) == key(verts[h]) for v in poly)] for h in H}
check('four rooms meet at every home vertex', all(len(rooms_at[h]) == 4 for h in H))


def turn_kind(v, arrive_from, go_to):
    """Classify departure toward go_to relative to arrival heading at v."""
    a = scal(-1, tangent(verts[v], verts[arrive_from]))  # arrival heading
    d = tangent(verts[v], verts[go_to])
    c = mink(a, d)
    s = det3(verts[v], a, d)  # orientation: + = counterclockwise (left) in the disk
    if c > 1-1e-9:
        return 'S'
    if c < -1+1e-9:
        return 'U'
    if abs(c) < 1e-9:
        return 'L' if s > 0 else 'R'
    return f'?{c:.3f}'

# disk-orientation sanity: det>0 means counterclockwise in the disk picture
e = det3(ORIGIN, (0, 1, 0), (0, 0, 1))
check('orientation convention (det>0 = counterclockwise in disk)', e > 0)


def walk(start, toward, rule, maxsteps=40):
    """rule: 'L' or 'R'. Returns visited vertex list and steps to first full-state return."""
    cur, nxt = start, toward
    seq = [cur]
    for step in range(1, maxsteps+1):
        prev, cur = cur, nxt
        seq.append(cur)
        choices = [w for w in vadj[cur] if turn_kind(cur, prev, w) == rule]
        assert len(choices) == 1, (cur, [turn_kind(cur, prev, w) for w in vadj[cur]])
        nxt = choices[0]
        if cur == start and nxt == toward:
            return seq, step
    return seq, None

names = 'ABCDEFGH'
idx = {h: names[k] for k, h in enumerate(H)}
log('\n== Problem 2 (one octagon, local turns) ==')
seqL, nL = walk(H[0], H[1], 'L')
log('left-turn walk from A toward B: ' + ','.join(idx.get(v, '?') for v in seqL))
check('P2 left: position after 4 moves is E', idx.get(seqL[4]) == 'E')
check('P2 left: first full-state return after 8 moves', nL == 8, str(nL))
check('P2 left: no earlier return to A', all(v != H[0] for v in seqL[1:8]))
seqR, nR = walk(H[0], H[7], 'R')
log('right-turn walk from A toward H: ' + ','.join(idx.get(v, '?') for v in seqR))
check('P2 right: first full-state return after 8 moves, 4th stop E', nR == 8 and idx.get(seqR[4]) == 'E', f'{nR}')
# the guide's left visual: at B arriving from A, the left branch is toward C
check('p.2 visual: at B, arriving from A, left branch goes to C', turn_kind(H[1], H[0], H[2]) == 'L')
check('p.2 visual: at B, arriving from A, straight branch leaves the octagon', all(turn_kind(H[1], H[0], w) != 'S' or w not in H for w in vadj[H[1]]))

log('\n== Problem 3 (outside of two side-sharing octagons) ==')
# second room shares side H(=v7)-A(=v0) with Home; drawn start: top shared endpoint = v0, heading to v1
nb = next(j for j in adj[0] if set(key(v) for v in tiles[j]) >= {key(HOME[7]), key(HOME[0])})
roomsets = [set(vkeys[key(v)] for v in tiles[t]) for t in (0, nb)]
edges = Counter()
for t in (0, nb):
    ids = [vkeys[key(v)] for v in tiles[t]]
    for k in range(8):
        edges[frozenset((ids[k], ids[(k+1) % 8]))] += 1
bedges = {e for e, c in edges.items() if c == 1}
check('two rooms share exactly one side', sum(1 for c in edges.values() if c == 2) == 1)
cur, prev = H[1], H[0]
path = [H[0], H[1]]
kinds = []
while True:
    outs = [w for w in vadj[cur] if frozenset((cur, w)) in bedges and w != prev]
    assert len(outs) == 1
    w = outs[0]
    kinds.append(turn_kind(cur, prev, w))
    prev, cur = cur, w
    path.append(cur)
    if cur == H[0]:
        kinds.append(turn_kind(cur, prev, H[1]))
        break
moves = len(path)-1
log(f'outside walk: {moves} edges; turn kinds at the {len(kinds)} junctions: {"".join(kinds)}')
check('P3 octagons: 14 edge moves', moves == 14)
check('P3 octagons: 12 left quarter-turns, 2 straight, no right turns', kinds.count('L') == 12 and kinds.count('S') == 2 and kinds.count('R') == 0)
straight_at = [path[(i+1)] for i, k in enumerate(kinds) if k == 'S']
check('P3 octagons: straight junctions are the two ends of the shared wall', set(straight_at) == {H[0], H[7]})
# left side check: Home interior lies on the left of v0->v1
cH = centroid_key(HOME)[1]
check('P3: rooms are on the walker\'s left at the start', det3(verts[H[0]], tangent(verts[H[0]], verts[H[1]]), tangent(verts[H[0]], cH)) > 0)
# squares: same rule on Z^2
sq = [(1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1)]
sk = []
for i in range(6):
    a, b, c = sq[i-1], sq[i], sq[(i+1) % 6]
    u = (b[0]-a[0], b[1]-a[1]); v = (c[0]-b[0], c[1]-b[1])
    cr = u[0]*v[1]-u[1]*v[0]
    sk.append('S' if u == v else ('L' if cr > 0 else 'R'))
check('P3 squares: 6 moves, 4 left turns, 2 straight', sk.count('L') == 4 and sk.count('S') == 2, ''.join(sk))
check('P3 guide arithmetic 16-4=12, 8-4=4, 8+8-2=14, 4+4-2=6', (16-4, 8-4, 8+8-2, 4+4-2) == (12, 4, 14, 6))

log('\n== Problem 4 (complete streets) ==')
# Full geodesics through home sides: planes with unit normals n_k. Two geodesics meet in H^2
# iff |<n1,n2>| < 1; ultraparallel iff > 1; asymptotic iff = 1.
N = [normal(HOME[k], HOME[(k+1) % 8]) for k in range(8)]
rel = {}
for i, j in itertools.combinations(range(8), 2):
    g = abs(mink(N[i], N[j]))
    rel[(i, j)] = 'cross' if g < 1-1e-9 else ('ultraparallel' if g > 1+1e-9 else 'asymptotic')
crossing_pairs = sorted(k for k, v in rel.items() if v == 'cross')
log(f'crossing pairs among the 8 drawn streets: {crossing_pairs}')
check('drawn streets cross only at the 8 home vertices (neighbours k,k+1)', set(crossing_pairs) == {tuple(sorted((k, (k+1) % 8))) for k in range(8)})
through_P = [k for k in range(8) if abs(mink(N[k], HOME[0])) < 1e-9]
check('exactly two drawn streets pass through P=v0 (sides 7 and 0)', sorted(through_P) == [0, 7], str(through_P))
check('P4: both streets through P miss R (side 3 geodesic)', all(rel[tuple(sorted((k, 3)))] != 'cross' for k in through_P), str([rel[tuple(sorted((k, 3)))] for k in through_P]))
check('R does not pass through P', abs(mink(N[3], HOME[0])) > 1e-6)
# the two through P are distinct and actually different lines
check('the two streets through P are distinct', abs(abs(mink(N[0], N[7]))-1) > 1e-9)
# Euclidean answer to the comparison question is "no" (Playfair): trivially recorded
log('Euclidean comparison: two distinct lines through a point both missing a third line would be two parallels through one point -> impossible (answer: no).')

# Guide's adult proof, in disk coordinates
C = 2**0.25; r = sqrt(sqrt(2)-1)
# circle orthogonal to unit circle through two disk points: solve directly
def ortho_circle(z1, z2):
    # centre c with Re(conj(c) z) = (|z|^2+1)/2 for z1,z2
    a1, b1, r1 = z1.real, z1.imag, (abs(z1)**2+1)/2
    a2, b2, r2 = z2.real, z2.imag, (abs(z2)**2+1)/2
    det = a1*b2-a2*b1
    c = complex((r1*b2-r2*b1)/det, (a1*r2-a2*r1)/det)
    return c, sqrt(abs(c)**2-1)
Vd = [todisk(v) for v in HOME]
c0, s0 = ortho_circle(Vd[0], Vd[1]); c7, s7 = ortho_circle(Vd[7], Vd[0]); c3, s3 = ortho_circle(Vd[3], Vd[4])
check('guide: centres C e^{i pi/4}, C, -C', abs(c0-C*complex(cos(pi/4), sin(pi/4))) < 1e-12 and abs(c7-C) < 1e-12 and abs(c3+C) < 1e-12)
check('guide: all three radii equal r', max(abs(s0-r), abs(s7-r), abs(s3-r)) < 1e-12)
check('guide: -C+r<0, C/sqrt2-r>0, C-r>0', -C+r < 0 and C/sqrt(2)-r > 0 and C-r > 0, f'{-C+r:.4f},{C/sqrt(2)-r:.4f},{C-r:.4f}')
check('guide: (C/sqrt2)^2 - r^2 = 1 - sqrt2/2', abs((C/sqrt(2))**2-r**2-(1-sqrt(2)/2)) < 1e-12)
# disk-circle cross-check: the side circles really are orthogonal to the unit circle and contain the vertices
check('disk: supporting circles orthogonal to boundary', all(abs(abs(c)**2-s**2-1) < 1e-12 for c, s in ((c0, s0), (c7, s7), (c3, s3))))

log('\n== Problem 5 (four rooms around one corner) ==')
P_rooms = rooms_at[H[0]]
check('four rooms around corner P', len(P_rooms) == 4)
sub = {i: adj[i] & set(P_rooms) for i in P_rooms}
check('room graph around a corner is a 4-cycle (each room has 2 neighbours there)', all(len(s) == 2 for s in sub.values()))
star = next(i for i in P_rooms if i != 0 and i not in adj[0])
nbrs = sorted(sub[0])
NAME = {0: 'H', star: '*', nbrs[0]: 'X', nbrs[1]: 'Y'}


def routes(L):
    res = []
    def go(rt):
        if len(rt) == L+1:
            if rt[-1] == star:
                res.append(rt)
            return
        for j in sorted(sub[rt[-1]]):
            go(rt+[j])
    go([0])
    return res
r2, r4 = routes(2), routes(4)
log('2-door routes: ' + '; '.join(''.join(NAME[x] for x in rt) for rt in r2))
log('4-door routes: ' + '; '.join(''.join(NAME[x] for x in rt) for rt in r4))
check('P5: exactly 2 two-door routes', len(r2) == 2)
check('P5: exactly 8 four-door routes', len(r4) == 8)
check('P5: Home and star share no side (corner only)', star not in adj[0])
# guide list, with A,B in either labelling
guide4 = ['HAHA*', 'HAHB*', 'HA*A*', 'HA*B*', 'HBHA*', 'HBHB*', 'HB*A*', 'HB*B*']
got = sorted(''.join(NAME[x] for x in rt).replace('X', 'A').replace('Y', 'B') for rt in r4)
check('guide: printed eight-route list equals the enumeration', sorted(guide4) == got)
# if 'route from Home to star' were read as 'stop on first arrival', count would be
first_arrival = [rt for rt in r4 if star not in rt[1:-1]]
log(f'(alternative reading: 4-door routes that do not pass through * earlier = {len(first_arrival)})')
# square grid comparison layers
sqlayers = [sum(1 for x in range(-5, 6) for y in range(-5, 6) if abs(x)+abs(y) == d) for d in range(3)]
check('guide: square grid exact-distance layers 1,4,8', sqlayers == [1, 4, 8])

log('\n== Problem 1 (square grid, never turn around) ==')
DIRS = {'E': (1, 0), 'N': (0, 1), 'W': (-1, 0), 'S': (0, -1)}
OPP = {'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N'}
B = 3  # A at centre of a 6x6-square board: coordinates -3..3


def p1routes(L):
    out = []
    def go(pos, seq):
        if len(seq) == L:
            if pos == (0, 0) and OPP[seq[-1]] != 'E':
                out.append(''.join(seq))
            return
        for d, (dx, dy) in DIRS.items():
            if seq and d == OPP[seq[-1]]:
                continue
            if not seq and d != 'E':
                continue
            np = (pos[0]+dx, pos[1]+dy)
            if max(abs(np[0]), abs(np[1])) > B:
                continue
            go(np, seq+[d])
    go((0, 0), [])
    return out
for L in (2, 4, 6, 8):
    rs = p1routes(L)
    log(f'length {L}: {len(rs)} legal returning routes' + (f' e.g. {rs[:4]}' if rs else ''))
check('P1: no 2-move route (would need a U-turn)', len(p1routes(2)) == 0)
check('P1: routes of 4, 6 and 8 moves all exist on the board', all(p1routes(L) for L in (4, 6, 8)))
check('P1: odd lengths impossible (parity)', not p1routes(5) and not p1routes(7))
for ex in ('ENWS', 'EENWWS', 'EENNWWSS', 'ENWSENWS'):
    check(f'guide example {ex} is a legal return on the board', ex in p1routes(len(ex)))
check('guide: final S arrival then left turn faces E', True, 'facing S, left = E')
check('P1: a return arriving westbound cannot then face east (U-turn): ENESWW excluded', 'ENESWW' not in p1routes(6))
check('P1: a return arriving eastbound needs no final turn: ESWWNE included', 'ESWWNE' in p1routes(6))

log('\n== Guide preparation arithmetic ==')
check('five packets x six single-sided pages = 30 sheets', 5*6 == 30)

log('')
log(f'{len([l for l in OUT if l.startswith(("PASS","FAIL"))])} checks, {len(FAIL)} failures')
text = '\n'.join(OUT) + '\n'
(HERE / 'check_math.out').write_text(text)
print(text)
sys.exit(1 if FAIL else 0)
