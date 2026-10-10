#!/usr/bin/env python3
"""Week 68 independent math check (review stage).

Models each printed map as an infinite graph truncated far beyond the printed
window.  Blockers are only placed on printed dots, so outside the window the
graph is an intact tail/exterior; a component is counted as a "forever piece"
iff it reaches the truncation boundary.  (That the exterior of a box is one
connected infinite piece is the tail / enclosing-square argument; it is not
proved by this code.)
"""
from itertools import combinations
from collections import deque
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]


def components(vertices, nbrs, blocked):
    seen, comps = set(), []
    for v in vertices:
        if v in blocked or v in seen:
            continue
        comp, q = [v], deque([v])
        seen.add(v)
        while q:
            u = q.popleft()
            for w in nbrs(u):
                if w in vertices and w not in blocked and w not in seen:
                    seen.add(w); comp.append(w); q.append(w)
        comps.append(comp)
    return comps


def classify(vertices, nbrs, blocked, is_far):
    comps = components(vertices, nbrs, blocked)
    forever = [c for c in comps if any(is_far(v) for v in c)]
    trapped = [c for c in comps if not any(is_far(v) for v in c)]
    return forever, trapped


out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

# ---------------- Line (problems 1, 2) ----------------
L = 30
line_V = set(range(-L, L + 1))
line_n = lambda v: (v - 1, v + 1)
line_far = lambda v: abs(v) == L
window = list(range(-4, 5))  # 9 printed dots, numbered 1..9 left to right
say('== Line: 9 printed dots')
for k in (1, 2, 4):
    fset, tset = set(), set()
    for B in combinations(window, k):
        f, t = classify(line_V, line_n, set(B), line_far)
        fset.add(len(f)); tset.add(len(t))
    say(f'P1 k={k}: forever-piece counts over all {len(list(combinations(window,k)))} placements = {sorted(fset)}; trapped counts = {sorted(tset)}')
cnt2 = 0
for B in combinations(window, 4):
    f, t = classify(line_V, line_n, set(B), line_far)
    if len(t) == 2:
        cnt2 += 1
say(f'P2: placements of 4 blockers on 9 dots with exactly 2 trapped pieces = {cnt2} of 126')
B = {d - 5 for d in (2, 4, 5, 7)}
f, t = classify(line_V, line_n, B, line_far)
say('P2 guide example block 2,4,5,7: forever', len(f), 'trapped dots', sorted(sorted(x + 5 for x in c) for c in t))

# ---------------- Ladder (problems 3, 4) ----------------
L = 30
lad_V = {(x, y) for x in range(-L, L + 1) for y in (0, 1)}
lad_n = lambda v: ((v[0] - 1, v[1]), (v[0] + 1, v[1]), (v[0], 1 - v[1]))
lad_far = lambda v: abs(v[0]) == L
lwin = [(x, y) for x in range(-4, 5) for y in (0, 1)]
say('== Ladder: 9 printed columns, 18 dots')
res1 = {(len(f), len(t)) for B in combinations(lwin, 1) for f, t in [classify(lad_V, lad_n, set(B), lad_far)]}
say('P3 one blocker: (forever, trapped) outcomes =', sorted(res1))
sep, together, trap2 = [], 0, 0
for B in combinations(lwin, 2):
    f, t = classify(lad_V, lad_n, set(B), lad_far)
    if t: trap2 += 1
    if len(f) == 2: sep.append(B)
    else: together += 1
same_rung = [b for b in sep if b[0][0] == b[1][0]]
diag = [b for b in sep if abs(b[0][0] - b[1][0]) == 1 and b[0][1] != b[1][1]]
say(f'P3 two blockers: {len(sep)} separating placements ({len(same_rung)} same rung, {len(diag)} diagonal in adjacent columns, {len(sep)-len(same_rung)-len(diag)} other); {together} stay connected; placements with a trapped pocket: {trap2}')
say('   example diagonal separation:', diag[0])
f, t = classify(lad_V, lad_n, {(0, 0), (1, 0)}, lad_far)
say('   guide contrast (two adjacent dots same rail): forever', len(f), 'trapped', len(t))
mf, mc, three = 0, 0, None
for B in combinations(lwin, 4):
    f, t = classify(lad_V, lad_n, set(B), lad_far)
    mf = max(mf, len(f));
    if len(f) + len(t) > mc: mc, three = len(f) + len(t), B
say(f'P4 four blockers (all 3060 placements): max forever pieces = {mf}; max total components = {mc}')
f, t = classify(lad_V, lad_n, {(0, 0), (0, 1), (2, 0), (2, 1)}, lad_far)
say('P4 guide example (rungs 0 and 2 blocked): forever', len(f), 'trapped', [sorted(c) for c in t])

# ---------------- Grid (problems 5, 6) ----------------
say('== Grid: 7x7 printed window, coordinates -3..3')
R = 5  # board [-5,5]^2: window plus two-ring exterior
W = 2 * R + 1
idx = lambda x, y: (y + R) * W + (x + R)
FULL = (1 << (W * W)) - 1
COLMASK_L = sum(1 << idx(-R, y) for y in range(-R, R + 1))
COLMASK_R = sum(1 << idx(R, y) for y in range(-R, R + 1))
OUTER = sum(1 << idx(x, y) for x in range(-R, R + 1) for y in range(-R, R + 1) if max(abs(x), abs(y)) == R)

def flood(seed, openm):
    reach = seed & openm
    while True:
        nb = reach | ((reach << 1) & ~COLMASK_L) | ((reach >> 1) & ~COLMASK_R) | (reach << W) | (reach >> W)
        nb &= openm & FULL
        if nb == reach: return reach
        reach = nb

gwin = [(x, y) for x in range(-3, 4) for y in range(-3, 4)]
trapping = []
for B in combinations(gwin, 4):
    bm = sum(1 << idx(*b) for b in B)
    openm = FULL & ~bm
    if flood(OUTER, openm) != openm:
        trapping.append(B)
centers = []
for B in trapping:
    S = set(B)
    c = [(x, y) for (x, y) in gwin if (x, y) not in S and S == {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}]
    centers.append(c[0] if c else None)
say(f'P5 left: 4-blocker placements in the window that trap something = {len(trapping)}; all are the 4 neighbours of one dot: {all(centers)}; trapped dots are the {len(set(centers))} interior dots (|x|,|y|<=2): {all(max(abs(a),abs(b))<=2 for a,b in centers)}')

X = {(0, y) for y in range(-2, 3)}
P, Q = (-2, 0), (2, 0)
def bfs(start, goal, allowed):
    dist = {start: 0}; q = deque([start])
    while q:
        u = q.popleft()
        for d in ((1,0),(-1,0),(0,1),(0,-1)):
            w = (u[0]+d[0], u[1]+d[1])
            if w in allowed and w not in dist:
                dist[w] = dist[u] + 1; q.append(w)
    return dist.get(goal)
win_open = {v for v in gwin if v not in X}
big_open = {(x, y) for x in range(-12, 13) for y in range(-12, 13)} - X
say('P5 right: shortest P-Q route inside printed window =', bfs(P, Q, win_open), '; on a large board =', bfs(P, Q, big_open))
route = [P]
for step in ['U']*3 + ['R']*4 + ['D']*3:
    x, y = route[-1]
    route.append({'U': (x, y+1), 'R': (x+1, y), 'D': (x, y-1)}[step])
say('   guide route 3 up/4 right/3 down: ends at Q', route[-1] == Q, '; avoids X', not (set(route) & X), '; stays in window', all(max(abs(a), abs(b)) <= 3 for a, b in route), '; steps', len(route) - 1)
bm = sum(1 << idx(*b) for b in X); openm = FULL & ~bm
say('   right map: every open dot reaches the far exterior (no pocket):', flood(OUTER, openm) == openm)
# Exterior-connectivity lemma for the P6 proof: annulus [-M,M]^2 \ [-N,N]^2 connected
ok = True
for N in range(0, 6):
    for M in range(N + 1, N + 5):
        A = {(x, y) for x in range(-M, M+1) for y in range(-M, M+1) if max(abs(x), abs(y)) > N}
        a0 = next(iter(A))
        comps = components(A, lambda v: ((v[0]+1,v[1]),(v[0]-1,v[1]),(v[0],v[1]+1),(v[0],v[1]-1)), set())
        ok &= len(comps) == 1
say('P6 lemma check: every annulus [-M,M]^2 minus [-N,N]^2 (N<=5, M<=N+4) is connected:', ok)

# ---------------- 3-regular tree (problems 7, 8) ----------------
say('== 3-regular tree')
D = 10
children = {(): [(i,) for i in range(3)]}
nodes = [()]
frontier = [(i,) for i in range(3)]
for depth in range(1, D + 1):
    nxt = []
    for v in frontier:
        nodes.append(v)
        if depth < D:
            children[v] = [v + (j,) for j in range(2)]
            nxt.extend(children[v])
    frontier = nxt
parent = {c: p for p, cs in children.items() for c in cs}
tV = set(nodes)
tn = lambda v: tuple(children.get(v, [])) + ((parent[v],) if v in parent else ())
deg_ok = all(len(tn(v)) == 3 for v in nodes if len(v) < D)
say('tree truncated at depth', D, '; internal degrees all 3:', deg_ok)
for r in range(0, 5):
    ball = {v for v in nodes if len(v) <= r}
    f, t = classify(tV, tn, ball, lambda v: len(v) == D)
    say(f'P7/P8 radius {r}: blockers {len(ball)}, forever pieces {len(f)}, trapped {len(t)}, 3*2^r = {3*2**r}')

(Path(__file__).with_suffix('.out')).write_text('\n'.join(out) + '\n')
