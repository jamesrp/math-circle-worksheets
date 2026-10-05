"""Independent solutions for every Week 14 base-packet problem and guide claim.

Starting fillings are read from extracted_figures.json (the delivered PDFs, via
extract_figures.py), not typed from the sources.  Guide claims are typed from
the guide text (week-14-facilitator.pdf) and each one is checked.
Writes solve.out next to this script.
"""
import os, sys, json, itertools
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tri import *

OUT = []
FAIL = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    OUT.append(s)


def check(cond, msg):
    log(('  ok   ' if cond else '  FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


FIG = json.load(open(os.path.join(HERE, 'extracted_figures.json')))


def page(f, p):
    return FIG[f'{f}#{p}']


def fillings_on(f, p, n=None):
    labs = '123456789' if f.endswith('-k-1.pdf') else LET
    out = []
    for r in page(f, p):
        if n and r['n'] != n:
            continue
        out.append((r['n'], parse(' '.join(r['diagonals']), labs) if r['diagonals'] else frozenset(), r))
    return out


K, M, U, GD = 'week-14-k-1.pdf', 'week-14-grades-2-3.pdf', 'week-14-grades-4-5.pdf', 'week-14-facilitator.pdf'
N = '123456789'

# ------------------------------------------------------------------ foundations
log('== Foundations')
T = {}
for n in range(3, 10):
    a = set(by_root(n))
    if n <= 8:
        b = set(by_subsets(n))
        check(a == b, f'n={n}: subset enumeration and root-edge recursion agree ({len(a)})')
    T[n] = sorted(a, key=lambda t: sorted(t))
log('  counts n=3..9:', [len(T[n]) for n in range(3, 10)])
check([len(T[n]) for n in range(3, 9)] == [1, 2, 5, 14, 42, 132], 'guide table: 1, 2, 5, 14, 42, 132 labeled fillings for 3..8 corners')
for n in range(3, 10):
    ok = all(len(triangles(n, t)) == n - 2 and len(t) == n - 3 for t in T[n])
    check(ok, f'n={n}: every filling has n-2={n-2} triangles and n-3={n-3} diagonals')

# Any noncrossing chord set whose faces are all triangles is a full triangulation
for n in range(4, 9):
    D = diagonals(n)
    allsets = []

    def grow(i, cur):
        allsets.append(list(cur))
        for j in range(i, len(D)):
            if all(not cross(D[j], e) for e in cur):
                cur.append(D[j]); grow(j + 1, cur); cur.pop()
    grow(0, [])
    tri_only = [s for s in allsets if all(len(f) == 3 for f in faces(n, s))]
    sizes = Counter(len(s) for s in tri_only)
    check(set(sizes) == {n - 3} and len(tri_only) == len(T[n]),
          f'n={n}: of {len(allsets)} noncrossing chord sets, exactly the {len(T[n])} of size n-3 cut the polygon into triangles only (so 3 triangles in a hexagon is impossible)')

G = {n: graph(n, T[n]) for n in range(3, 10)}
for n in range(4, 10):
    check(all(len(set(G[n][t])) == n - 3 and all(v in G[n] for v in G[n][t]) for t in T[n]),
          f'n={n}: every filling has exactly n-3={n-3} distinct flip neighbours (overview)')
    # flip neighbours are exactly fillings sharing n-4 diagonals (guide p.7 "Check the actual move")
    ok = all(set(G[n][t]) == {s for s in T[n] if len(t & s) == n - 4} for t in T[n])
    check(ok, f'n={n}: two fillings are flip neighbours iff they share exactly n-4 diagonals')
    check(len(bfs(G[n], T[n][0])) == len(T[n]), f'n={n}: flip graph connected')

# pentagon: two diagonals with no common endpoint cross
p5 = diagonals(5)
check(all(cross(e, f) for e, f in itertools.combinations(p5, 2) if not set(e) & set(f)),
      'pentagon: any two diagonals without a common endpoint cross (guide p.3 proof)')
check(set(T[5]) == {fan(5, v) for v in range(5)}, 'pentagon: the five fillings are exactly the five fans')

# ------------------------------------------------------------------ K-1
log('\n== K-1')
# P1
for n, d, r in fillings_on(K, 1):
    pass
log('  P1: pentagon has', len(T[5]), 'fillings, hexagon', len(T[6]), '-> two different ways exist; triangles 3 and 4')
check(parse('13 14', N) in T[5] and parse('24 25', N) in T[5] and parse('13 14 15', N) in T[6] and parse('24 25 26', N) in T[6],
      'guide K-1 P1 examples {13,14},{24,25},{13,14,15},{24,25,26} are fillings')
# P2
blanks = sum(1 for n, d, r in fillings_on(K, 2) if not d) - 1
log(f'  P2: {len(T[5])} fillings; page has {blanks} small blank copies + 1 large')
check(set(parse(s, N) for s in ['13 14', '24 25', '13 35', '14 24', '25 35']) == set(T[5]), 'guide K-1 P2 list = all five fillings')
# P3
log('  P3: hexagon fillings all have 4 triangles (see foundations); 3 is impossible')
# P4
(_, pent_line, _), = [x for x in fillings_on(K, 4, 5) if x[2]['width_in'] > 2]
(_, hex_line, _), = [x for x in fillings_on(K, 4, 6) if x[2]['width_in'] > 2]
cp = [t for t in T[5] if pent_line <= t]
ch = [t for t in T[6] if hex_line <= t]
copies5 = sum(1 for x in fillings_on(K, 4, 5) if x[2]['width_in'] < 2)
copies6 = sum(1 for x in fillings_on(K, 4, 6) if x[2]['width_in'] < 2)
log(f'  P4: printed lines {name(pent_line, N)} / {name(hex_line, N)}; completions {len(cp)} / {len(ch)};'
    f' recording copies with the line printed: {copies5} / {copies6}')
log('      pentagon completions:', [name(t, N) for t in cp])
log('      hexagon completions :', [name(t, N) for t in ch])
check(len(cp) == 2 and len(ch) == 4, 'K-1 P4: 2 pentagon and 4 hexagon completions')
check(set(cp) == {parse('13 35', N), parse('13 14', N)} and
      set(ch) == {parse(s, N) for s in ['14 24 46', '13 14 46', '14 15 24', '13 14 15']}, 'guide K-1 P4 catalog complete and correct')
if copies5 != len(cp):
    log(f'  NOTE K-1 P4: the pentagon has {copies5} pre-lined copies but only {len(cp)} answers')
# P5
starts = [d for n, d, r in fillings_on(K, 5, 6) if d]
for s in starts:
    nb = G[6][s]
    log(f'  P5: start {name(s, N)} -> {len(nb)} results: {[name(t, N) for t in nb]}')
check([set(G[6][s]) for s in starts] == [{parse(x, N) for x in ['13 14 46', '13 15 35', '14 15 24']},
                                         {parse(x, N) for x in ['13 35 36', '15 25 35', '13 14 15']}],
      'guide K-1 P5 neighbour lists (both starts) correct')
log('      blank copies per start:', sum(1 for x in fillings_on(K, 5, 6) if not x[1]) // 2)
# P6
(s6,) = [d for n, d, r in fillings_on(K, 6, 5) if d]
log('  P6: start', name(s6, N))


def ham_cycles(Gn, s):
    out = []
    nodes = list(Gn)

    def go(path):
        if len(path) == len(nodes):
            if s in Gn[path[-1]]:
                out.append(path + [s])
            return
        for v in Gn[path[-1]]:
            if v not in path:
                go(path + [v])
    go([s])
    return out


hc = ham_cycles(G[5], s6)
log('      Hamiltonian cycles from start:', len(hc), [' -> '.join(LET[[v for v in range(5) if fan(5, v) == t][0]] for t in c) for c in hc])
check(len(hc) == 2, 'K-1 P6: yes, 2 loops (one each direction)')
route = [parse(x, N) for x in ['13 14', '13 35', '25 35', '24 25', '14 24', '13 14']]
check(all(b in G[5][a] for a, b in zip(route, route[1:])) and len(set(route[:-1])) == 5, 'guide K-1 P6 route legal, visits all five')

# ------------------------------------------------------------------ grades 2-3
log('\n== Grades 2-3')
check(parse('AC AD AE') in T[6] and parse('BD BE BF') in T[6] and parse('AC AD AE AF') in T[7] and parse('BD BE BF BG') in T[7],
      'guide 2-3 P1 examples are fillings (hexagon, heptagon)')
log('  P2: 5 fillings; small copies:', sum(1 for x in fillings_on(M, 2) if not x[1]) - 1)
st = [d for n, d, r in fillings_on(M, 3, 6) if d]
for s in st:
    log(f'  P3: start {name(s)} -> {[name(t) for t in G[6][s]]}')
check([set(G[6][s]) for s in st] == [{parse(x) for x in ['AC AD DF', 'AC AE CE', 'AD AE BD']},
                                     {parse(x) for x in ['AC CE CF', 'AE BE CE', 'AC AD AE']}], 'guide 2-3 P3 neighbour lists correct')
# P4 map
maps = [d for n, d, r in fillings_on(M, 4, 5)]
check(len(maps) == 5 and set(maps) == set(T[5]), 'P4: the five printed pentagons are the five different fillings')
quad = [d for n, d, r in fillings_on(M, 4, 4)]
check(quad == [parse('AC'), parse('BD')], 'P4 example: AC then BD (one flip of the quadrilateral)')
joins = {frozenset((a, b)) for a in maps for b in G[5][a]}
fanname = {fan(5, v): 'F' + LET[v] for v in range(5)}
log('  P4: joins', sorted('-'.join(sorted(fanname[t] for t in j)) for j in joins), f'({len(joins)})')
guide_joins = {frozenset((fan(5, LET.index(a)), fan(5, LET.index(b)))) for a, b in ['AC', 'CE', 'EB', 'BD', 'DA']}
check(joins == guide_joins, 'guide 2-3 P4: exactly five joins FA-FC, FC-FE, FE-FB, FB-FD, FD-FA')
# layout: are joined drawings neighbours around the page?
pos = {d: r['center'] for n, d, r in fillings_on(M, 4, 5)}
import math
cx = sum(p[0] for p in pos.values()) / 5; cy = sum(p[1] for p in pos.values()) / 5
order = sorted(pos, key=lambda d: -math.atan2(pos[d][1] - cy, pos[d][0] - cx))
log('  P4 layout clockwise:', [fanname[d] for d in order])
check(all(frozenset((order[i], order[(i + 1) % 5])) in joins for i in range(5)), 'P4: the page places the drawings in their cycle order (no crossing joins needed)')
# P5 odd return


def odd_closed_walk_min(Gn, s, maxlen=11):
    best = None
    frontier = {s}
    for L in range(1, maxlen + 1):
        frontier = {v for u in frontier for v in Gn[u]}
        if L % 2 == 1 and s in frontier:
            return L
    return None


(s5,) = [d for n, d, r in fillings_on(M, 5, 5) if d]
check(s5 == fan(5, 0), 'P5 start = FA')
L = odd_closed_walk_min(G[5], s5)
log('  P5: shortest odd return =', L)
check(L == 5, 'guide 2-3 P5: shortest odd return is 5 flips')
check(odd_closed_walk_min(G[4], T[4][0]) is None, 'guide extension: quadrilateral has no odd return')
# P6
(s6a, t6a) = [d for n, d, r in fillings_on(M, 6, 6) if d]
D6 = bfs(G[6], s6a)
log(f'  P6: start {name(s6a)}, target {name(t6a)}, distance {D6[t6a]}')
check(D6[t6a] == 3, 'P6 minimum 3')
lens = set()


def simple_paths(Gn, s, t):
    stack = [(s, [s])]
    while stack:
        u, p = stack.pop()
        if u == t:
            lens.add(len(p) - 1)
            continue
        for v in Gn[u]:
            if v not in p:
                stack.append((v, p + [v]))


simple_paths(G[6], s6a, t6a)
log('  P6: simple-route lengths possible:', sorted(lens))
r1 = [parse(x) for x in ['BD BE BF', 'AE BD BE', 'AD AE BD', 'AC AD AE']]
r2 = [parse(x) for x in ['BD BE BF', 'BE BF CE', 'AE BE CE', 'AC AE CE', 'AC AD AE']]
for r, k in [(r1, 3), (r2, 4)]:
    check(all(b in G[6][a] for a, b in zip(r, r[1:])) and len(set(r)) == len(r) and len(r) - 1 == k,
          f'guide 2-3 P6 {k}-flip route legal and repeat-free')
log('  P6 recording copies:', sum(1 for x in fillings_on(M, 6, 6) if not x[1]) - 1, '(+1 large board)')
# P7
c7 = sum(1 for x in fillings_on(M, 7, 6) if not x[1]) - 1 + sum(1 for x in fillings_on(M, 8, 6) if not x[1])
log(f'  P7: {len(T[6])} fillings; recording outlines on pp.7-8: {c7}')
groups = Counter()
for t in T[6]:
    (tr,) = [x for x in triangles(6, t) if 0 in x and 5 in x]
    groups[LET[[v for v in tr if v not in (0, 5)][0]]] += 1
log('  P7: by third corner of the triangle on AF:', dict(sorted(groups.items())))
check(dict(groups) == {'B': 5, 'C': 2, 'D': 2, 'E': 5}, 'guide 2-3 P7: 5+2+2+5 by triangle on AF')
cat = {'B': ['BF CF DF', 'BF CE CF', 'BD BF DF', 'BE BF CE', 'BD BE BF'], 'C': ['AC CF DF', 'AC CE CF'],
       'D': ['AD BD DF', 'AC AD DF'], 'E': ['AE BE CE', 'AE BD BE', 'AC AE CE', 'AD AE BD', 'AC AD AE']}
allc = [parse(x) for v in cat.values() for x in v]
check(len(set(allc)) == 14 and set(allc) == set(T[6]), 'guide 2-3 P7 catalog = all 14, no repeats')
for g, lst in cat.items():
    check(all(any(set(tr) == {0, 5, LET.index(g)} for tr in triangles(6, parse(x))) for x in lst), f'guide catalog group {g} correctly grouped')

# ------------------------------------------------------------------ grades 4-5
log('\n== Grades 4-5')
st = [d for n, d, r in fillings_on(U, 2, 6) if d]
check(st == [parse('AC AD AE'), parse('AC AE CE')], 'P2 starts = 2-3 P3 starts')
maps = [d for n, d, r in fillings_on(U, 3, 5)]
check(set(maps) == set(T[5]), 'P3: five printed pentagons = all fillings; odd return of 5 exists (see 2-3 P5)')
# bipartite?
col = {T[5][0]: 0}
bip = True
for u in bfs(G[5], T[5][0]):
    for v in G[5][u]:
        if v in col and col[v] == col[u]:
            bip = False
        col.setdefault(v, 1 - col[u])
check(not bip, 'P3: pentagon flip graph is not bipartite')
p4 = [(r['center'], d) for n, d, r in fillings_on(U, 4, 6) if d]
p4.sort(key=lambda x: (-round(x[0][1]), x[0][0]))
starts, target = [d for c, d in p4[:3]], p4[3][1]
log('  P4: starts', [name(s) for s in starts], 'target', name(target))
check(target == fan(6, 0), 'P4 fourth filling = fan at A')
D = bfs(G[6], target)
dists = [D[s] for s in starts]
missing = [len(target - s) for s in starts]
log('  P4: distances', dists, 'missing target diagonals', missing)
check(dists == [3, 1, 2] and dists == missing, 'guide 4-5 P4: 3, 1, 2, each equal to the missing-diagonal bound')
rr = [parse(x) for x in ['AD BD DF', 'AC AD DF', 'AC AD AE']]
check(all(b in G[6][a] for a, b in zip(rr, rr[1:])), 'guide 4-5 P4 right-start route legal')
check(parse('AC AD AE') in G[6][parse('AC AE CE')], 'guide 4-5 P4 middle-start flip legal')
log('  P4 recording copies:', sum(1 for x in fillings_on(U, 4, 6) if not x[1]) - 1)
(s5,) = [d for n, d, r in fillings_on(U, 5, 8) if d]
D8 = bfs(G[8], s5)
log(f'  P5: start {name(s5)}; to fan A {D8[fan(8, 0)]}, to fan E {D8[fan(8, 4)]}; degrees A={deg(s5, 0)}, E={deg(s5, 4)}')
check((D8[fan(8, 0)], D8[fan(8, 4)]) == (3, 5), 'guide 4-5 P5: 3 and 5')
rA = [parse(x) for x in ['AC AD DF DG DH', 'AC AD AG DF DG', 'AC AD AF AG DF', 'AC AD AE AF AG']]
rE = [parse(x) for x in ['AC AD DF DG DH', 'AC AD DG DH EG', 'AC AD DH EG EH', 'AC AD AE EG EH', 'AC AE CE EG EH', 'AE BE CE EG EH']]
for r, k in [(rA, 'A'), (rE, 'E')]:
    check(all(b in G[8][a] for a, b in zip(r, r[1:])) and r[-1] == fan(8, LET.index(k)), f'guide 4-5 P5 route to fan {k} legal')
check(parse('AC AD AE AF AG') == fan(8, 0) and parse('AE BE CE EG EH') == fan(8, 4), 'guide fan lists correct')
log('  P5 recording copies:', sum(1 for x in fillings_on(U, 5, 8) if not x[1]), '(guide routes need 3+5=8 new pictures)')
# P6 rule
for n in range(3, 10):
    ok = True
    for v in range(n):
        Dv = bfs(G[n], fan(n, v))
        ok &= all(Dv[t] == n - 3 - deg(t, v) for t in T[n])
    check(ok, f'n={n}: distance to the fan at any corner v = n-3-d_v for all {len(T[n])} fillings')
# greedy procedure from guide p.11 always finds an A-increasing flip
for n in range(4, 10):
    ok = all(any(deg(flip(n, t, d), 0) == deg(t, 0) + 1 for d in t if 0 not in d) for t in T[n] if t != fan(n, 0))
    check(ok, f'n={n}: every non-fan filling has a flip that adds a diagonal at A (guide p.11 construction)')
# P7
(sS, sT, _) = [d for n, d, r in fillings_on(U, 7, 8)]
log(f'  P7: S={name(sS)} T={name(sT)} distance {D8[sT]} shared diagonals {len(sS & sT)}')
check(D8[sT] == 5, 'P7 distance 5 (guide: five-flip route is shortest)')
r7 = [parse(x) for x in ['AC AD DF DG DH', 'AD BD DF DG DH', 'AD BD DG DH EG', 'AD BD DH EG EH', 'AD AE BD EG EH', 'AE BD BE EG EH']]
check(all(b in G[8][a] for a, b in zip(r7, r7[1:])) and r7[-1] == sT, 'guide 4-5 P7 route legal')
via = {LET[v]: (5 - deg(sS, v)) + (5 - deg(sT, v)) for v in range(8)}
log('  P7: route length through each fan:', via)
check(via['A'] == 7, 'guide: through the A fan 3+4=7')

# ------------------------------------------------------------------ guide extensions
log('\n== Guide extensions')
cnt7 = Counter()
for t in T[7]:
    (tr,) = [x for x in triangles(7, t) if 0 in x and 6 in x]
    cnt7[[v for v in tr if v not in (0, 6)][0]] += 1
log('  heptagon by third corner on root side:', [cnt7[k] for k in range(1, 6)])
check([cnt7[k] for k in range(1, 6)] == [14, 5, 4, 5, 14], 'guide: 14+5+4+5+14=42')
Tn = {2: 1, **{n: len(T[n]) for n in range(3, 10)}}
check(all(Tn[n] == sum(Tn[k + 1] * Tn[n - k] for k in range(1, n - 1)) for n in range(3, 10)), 'guide recursion T_n = sum T_{k+1} T_{n-k}')
a, b = parse('BF CE CF'), parse('AD AE BD')
log('  nonfan example: first flips add', sorted(name(t - a) for t in G[6][a]), 'distance', bfs(G[6], a)[b])
check(sorted(name(t - a) for t in G[6][a]) == ['AC', 'BE', 'DF'] and bfs(G[6], a)[b] == 4, 'guide nonfan example: first flip adds AC/BE/DF only; distance 4')
rn = [parse(x) for x in ['BF CE CF', 'BF CF DF', 'BD BF DF', 'AD BD DF', 'AD AE BD']]
check(all(y in G[6][x] for x, y in zip(rn, rn[1:])), 'guide nonfan 4-flip route legal')
gaps = Counter()
for t in T[6]:
    for s in T[6]:
        gaps[bfs(G[6], t)[s] - len(s - t)] += 1
log('  hexagon: (distance - missing diagonals) over all ordered pairs:', dict(gaps))

log('\nFAILED CHECKS:', len(FAIL))
for f in FAIL:
    log('  ', f)
open(os.path.join(HERE, 'solve.out'), 'w').write('\n'.join(OUT) + '\n')
