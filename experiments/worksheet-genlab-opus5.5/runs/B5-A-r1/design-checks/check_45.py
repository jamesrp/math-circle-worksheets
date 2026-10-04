"""Checks for the grades 4-5 pages. Run: python3 check_45.py"""
import sys
from math import comb
from collections import Counter, deque
import tri
import lozenge as L
import instances as I

ok = True


def claim(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg)
    ok = ok and cond


print('=== Grades 4-5 Problem 1: all blue coverings of the three tall hexagons ===')
for k, abc, want in [('45-P1a', (1, 1, 1), 2), ('45-P1b', (1, 2, 1), 3), ('45-P1c', (1, 2, 2), 6)]:
    R, ts = L.tilings(*abc)
    kinds = Counter(L.kind(r) for r in ts[0])
    claim(len(ts) == want, '%s hexagon with sides %s (bottom, lower right, upper right): %d ways; each way uses %d blues (%d leaning right, %d leaning left, %d standing)'
          % (k, abc, len(ts), len(ts[0]), kinds['R'], kinds['L'], kinds['S']))

print('\n=== Grades 4-5 Problem 2: the flip map of the 1,2,2 hexagon ===')
R, ts, idx, adj = L.flip_graph(1, 2, 2)
words = {k: L.ribbons(t, 1, 2, 2)[0] for k, t in enumerate(ts)}
edges = sorted({tuple(sorted((words[u], words[v]))) for u in adj for v in adj[u]})
claim(len(ts) == 6 and len(edges) == 6, 'map has 6 ways (dots) and %d one-flip lines: %s' % (len(edges), ', '.join('%s-%s' % e for e in edges)))
deg = {words[k]: len(adj[k]) for k in adj}
print('INFO number of flips possible from each way (by its chain letters): %s' % deg)
D = {words[s]: {words[t]: d for t, d in L.bfs(adj, s).items()} for s in adj}
far = max((D[a][b], a, b) for a in D for b in D[a])
pairs = sorted({tuple(sorted((a, b))) for a in D for b in D[a] if D[a][b] == far[0]})
claim(far[0] == 4 and pairs == [('LLRR', 'RRLL')], 'farthest-apart pair needs %d flips: %s (the only pair that far apart)' % (far[0], pairs))
# the map has exactly one closed loop, a square
cyc = len(edges) - len(ts) + 1
claim(cyc == 1, 'the map has exactly one loop (edges - dots + 1 = %d): the square RLRL-RLLR-LRLR-LRRL' % cyc)

print('\n=== Grades 4-5 Problem 3: chains (ribbons) in the 1,2,2 hexagon ===')
ws = sorted(words.values())
allw = sorted(''.join(p) for p in set(__import__('itertools').permutations('LLRR')))
claim(ws == allw, 'the six ways have six different chains, and they are exactly the six orders of L, L, R, R: %s' % ws)
good = True
for u in adj:
    for v in adj[u]:
        a, b = words[u], words[v]
        diff = [i for i in range(4) if a[i] != b[i]]
        good &= len(diff) == 2 and diff[1] == diff[0] + 1 and a[diff[0]] == b[diff[1]] and a[diff[1]] == b[diff[0]]
claim(good, 'every flip swaps one neighbouring L and R in the chain (LR <-> RL), and nothing else in the chain changes')

print('\n=== Grades 4-5 Problem 4: counting with chains ===')
for k, abc in [('45-P4a', (1, 3, 2)), ('45-P4b', (1, 3, 3)), ('45-P4c', (1, 4, 4))]:
    a, b, c = abc
    R, ts = L.tilings(*abc)
    wset = {L.ribbons(t, *abc)[0] for t in ts}
    claim(len(ts) == comb(b + c, b) and len(wset) == len(ts) and all(w.count('R') == b and w.count('L') == c for w in wset),
          '%s hexagon %s: %d ways = number of orders of %d R and %d L = C(%d,%d); every way has a different chain'
          % (k, abc, len(ts), b, c, b + c, b))
# Pascal check, the kind of counting a child may invent
claim(comb(5, 2) == comb(4, 1) + comb(4, 2) and comb(6, 3) == comb(5, 2) + comb(5, 3) and comb(8, 4) == 70,
      'Pascal pattern: 10 = 4 + 6, 20 = 10 + 10, and the 1,4,4 hexagon has 70 ways')

print('\n=== Grades 4-5 Problems 5-7: the regular hexagon with 2 on each side ===')
R, ts, idx, adj = L.flip_graph(2, 2, 2)
W = {k: L.ribbons(t, 2, 2, 2) for k, t in enumerate(ts)}
byw = {v: k for k, v in W.items()}
nedges = sum(len(v) for v in adj.values()) // 2
claim(len(ts) == 20 and len(L.bfs(adj, 0)) == 20, 'regular hexagon: 20 ways, %d one-flip connections, and every way can be reached from every other by flips' % nedges)

# every flip changes exactly one of the two chains, by swapping one neighbouring LR pair
good = True
for u in adj:
    for v in adj[u]:
        changed = [i for i in range(2) if W[u][i] != W[v][i]]
        if len(changed) != 1:
            good = False
            continue
        a, b = W[u][changed[0]], W[v][changed[0]]
        diff = [i for i in range(4) if a[i] != b[i]]
        good &= len(diff) == 2 and diff[1] == diff[0] + 1
claim(good, 'every flip changes exactly one of the two chains, by swapping one neighbouring L and R')


def score(k):
    """sum over both chains of the number of (R before L) pairs = 'how far the Ls have sunk'"""
    return sum(L.inversions(w) for w in W[k])


claim(all(abs(score(u) - score(v)) == 1 for u in adj for v in adj[u]), 'every flip changes the score (pairs R-before-L, summed over both chains) by exactly 1')

for part, (s, t) in I.P5_PAIRS.items():
    a, b = byw[s], byw[t]
    d = L.bfs(adj, a)[b]
    lb = abs(score(a) - score(b))
    want = {'a': 2, 'b': 6, 'c': 8}[part]
    claim(d == want and lb == d, 'P5%s: start chains %s, finish chains %s: fewest flips = %d; score %d -> %d, so no route can be shorter'
          % (part, s, t, d, score(a), score(b)))

# the finish picture is the start picture turned a sixth of a turn
cx, cy = 0, 2


def rot_t(tt, k=1):
    u, v = tri.centroid3(tt)
    u -= 3 * cx
    v -= 3 * cy
    for _ in range(k):
        u, v = -v, u + v
    return tri.from_centroid3((u + 3 * cx, v + 3 * cy))


def rot_tiling(T, k=1):
    return frozenset(frozenset(rot_t(x, k) for x in rh) for rh in T)


for part, (s, t) in I.P5_PAIRS.items():
    T = ts[byw[s]]
    claim(idx[rot_tiling(T, 1)] == byw[t], 'P5%s: the finish is the start turned 1/6 of a turn counterclockwise' % part)
diam = max(max(L.bfs(adj, s).values()) for s in adj)
far_pairs = {tuple(sorted((W[u], W[v]))) for u in adj for v, d in L.bfs(adj, u).items() if d == diam}
claim(diam == 8 and far_pairs == {tuple(sorted(I.P5_PAIRS['c']))}, 'the largest number of flips ever needed between two ways of the regular hexagon is %d, and only the P5c pair is that far apart' % diam)

# Problem 6: round trips from the start way
s = byw[I.P6_START]
claim(len(adj[s]) == 6 and len(adj[s]) == max(len(v) for v in adj.values()), 'P6 start %s: 6 different flips are possible (the most of any way)' % (I.P6_START,))
# bipartite: colour by parity of score
claim(all((score(u) + score(v)) % 2 == 1 for u in adj for v in adj[u]), 'flip map is two-coloured by the parity of the score, so every round trip has an even number of flips')


def nonbacktracking_cycles(start, length):
    found = []

    def rec(path):
        if len(path) == length + 1:
            if path[-1] == start:
                found.append(list(path))
            return
        for nb in adj[path[-1]]:
            if len(path) >= 2 and nb == path[-2]:
                continue  # never undo the flip just made
            rec(path + [nb])
    rec([start])
    return found


for n in range(1, 9):
    c = nonbacktracking_cycles(s, n)
    if n % 2 == 1:
        claim(len(c) == 0, 'P6: no round trip of %d flip(s) from the start that never undoes the previous flip' % n) if n <= 7 else None
    else:
        ex = c[0] if c else None
        if n in (4, 6):
            claim(len(c) > 0, 'P6: round trips of %d flips that never undo the previous flip exist (%d of them), e.g. %s'
                  % (n, len(c), ' -> '.join('|'.join(W[k]) for k in ex)))
# also: any closed walk at all (with undo) of odd length is impossible - follows from bipartite; check directly up to 9
reach = {s: 1}
odd_back = False
cur = {s}
for step in range(1, 10):
    cur = {v for u in cur for v in adj[u]}
    if step % 2 == 1 and s in cur:
        odd_back = True
claim(not odd_back, 'P6: brute force: no sequence of 1, 3, 5, 7 or 9 flips (even with undoing) returns to the start')

# Problem 7: count via two chains
from itertools import permutations
words6 = sorted({''.join(p) for p in permutations('LLRR')})


def prefix_L(w, j):
    return w[:j].count('L')


compat = [(x, y) for x in words6 for y in words6 if all(prefix_L(x, j) >= prefix_L(y, j) for j in range(5))]
claim(len(compat) == 20 and set(compat) == set(W.values()),
      'P7: the ways match exactly the pairs (left chain, right chain) where the left chain has at least as many Ls as the right chain at every height: %d pairs' % len(compat))
byleft = Counter(x for x, y in compat)
print('INFO P7 breakdown by left chain: %s' % dict(sorted(byleft.items())))
byright = Counter(y for x, y in compat)
print('INFO P7 breakdown by right chain: %s' % dict(sorted(byright.items())))

# extra: MacMahon / box formula for adults
from fractions import Fraction


def macmahon(a, b, c):
    r = Fraction(1)
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                r *= Fraction(i + j + k - 1, i + j + k - 2)
    return r


for abc in [(1, 1, 1), (1, 2, 1), (1, 2, 2), (1, 3, 2), (1, 3, 3), (1, 4, 4), (2, 2, 2), (3, 3, 3)]:
    n = tri.count_tilings(tri.hexagon_region(*abc), ['B'])
    claim(n == macmahon(*abc), 'hexagon %s: %d ways by direct search = MacMahon box formula' % (abc, n))


print('\n=== Flip spots lettered A-G (for the key picture on the P5/P6 pages) and example routes ===')
LETTER = {(0, 2): 'A', (1, 2): 'B', (0, 3): 'C', (-1, 3): 'D', (-1, 2): 'E', (0, 1): 'F', (1, 1): 'G'}
claim(set(LETTER) == set(L.interior_points(I.H222)), 'the 7 inner grid points of the regular hexagon are the only places a flip can happen; lettered A (centre), B (right), C (upper right), D (upper left), E (left), F (lower left), G (lower right)')


def route(a, b):
    """one shortest route from tiling a to b, as flip-spot letters"""
    prev = {a: None}
    q = deque([a])
    while q:
        u = q.popleft()
        if u == b:
            break
        for pnt, nt in L.flips(u, I.H222):
            if nt not in prev:
                prev[nt] = (u, pnt)
                q.append(nt)
    out = []
    cur = b
    while prev[cur] is not None:
        u, pnt = prev[cur]
        out.append(LETTER[pnt])
        cur = u
    return out[::-1]


for part, (s_, t_) in I.P5_PAIRS.items():
    r = route(ts[byw[s_]], ts[byw[t_]])
    print('INFO P5%s one shortest route (flip spots in order): %s  (%d flips)' % (part, ' '.join(r), len(r)))
start = ts[byw[I.P6_START]]
print('INFO P6 start: flips possible at %s' % ' '.join(sorted(LETTER[pnt] for pnt, _ in L.flips(start, I.H222))))


def letter_round_trips(T0, length, distinct=False):
    """round trips from T0 of the given length, as letter strings, never flipping the same spot twice in a row
    (that would just undo the last flip). With distinct=True, all ways passed through must be different."""
    found = []

    def rec(T, seq, seen):
        if len(seq) == length:
            if T == T0:
                found.append(''.join(seq))
            return
        for pnt, nt in L.flips(T, I.H222):
            ch = LETTER[pnt]
            if seq and seq[-1] == ch:
                continue
            if distinct and nt in seen and not (len(seq) == length - 1 and nt == T0):
                continue
            rec(nt, seq + [ch], seen | {nt})
    rec(T0, [], {T0})
    return found


for n in (4, 6):
    trips = letter_round_trips(start, n)
    claim(len(trips) > 0, 'P6: %d round trips of %d flips from the start that never flip the same spot twice in a row; examples: %s'
          % (len(trips), n, ', '.join(sorted(trips)[:4])))
claim('BEBE' in letter_round_trips(start, 4), 'P6: e.g. B E B E is a 4-flip round trip (flip B, flip E, flip B back, flip E back)')
cyc6 = letter_round_trips(start, 6, distinct=True)
print('INFO P6: %d of the 6-flip round trips pass through 6 different ways (a true loop), e.g. %s' % (len(cyc6), ', '.join(sorted(cyc6)[:6])))
for n in (1, 3, 5, 7):
    claim(len(letter_round_trips(start, n)) == 0, 'P6: no %d-flip round trip from the start' % n)

print('\nALL GRADES 4-5 CHECKS PASSED' if ok else '\nSOME GRADES 4-5 CHECKS FAILED')
sys.exit(0 if ok else 1)
