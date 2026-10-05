"""Solve every Week 13 problem (base packet and return visit) from graphs.py.

Writes solve.out next to this script.  All answers come from exhaustive search
in routes.py; nothing from the packet's own checkers is used.
"""
import os, sys
from itertools import combinations, product
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from graphs import BOARDS, CAPACITY, R1, RD, RS, RB
from routes import *

OUT = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s); OUT.append(s)


def ed(name):
    return BOARDS[name][0]


def verts(name):
    return sorted({v for e in ed(name) for v in e})


def summary(name):
    E = ed(name)
    P = simple_paths(E)
    k, cols = packings(E)
    c, cuts = min_cuts(E)
    log(f'  {name}: {len(P)} routes; max packing {k} ({len(cols)} maximum collections); min closure {c} ({len(cuts)} minimum closures); equal: {k == c}')
    return k, cols, c, cuts


log('== Basic data for every board')
for n in ['diamond', 'greedy', 'bowtie', 'doubletrap', 'funnel', 'threetwo', 'three', 'bottleneck', 'endpoint_two', 'backward', 'staircase']:
    summary(n)

log('\n== K-1 P1 (greedy, bowtie): largest collections')
for n in ['greedy', 'bowtie']:
    k, cols = packings(ed(n))
    log(f'  {n}: max {k}; collections:', '; '.join('{' + ', '.join(fmt_path(p) for p in c) + '}' for c in cols))
log('  stuck single route on greedy? s-A-B-t blocks all others:',
    not simple_paths(ed('greedy'), closed=frozenset(R1)))

log('\n== K-1 P2 (diamond, funnel): minimum closures')
for n in ['diamond', 'funnel']:
    c, cuts = min_cuts(ed(n))
    log(f'  {n}: min {c}:', ' '.join(fmt_edges(x) for x in cuts))

log('\n== K-1 P3 (threetwo, three)')
for n in ['threetwo', 'three']:
    k, cols = packings(ed(n)); c, cuts = min_cuts(ed(n))
    log(f'  {n}: max {k}, min {c}; minimum closures:', ' '.join(fmt_edges(x) for x in cuts))

log('\n== K-1 P4: single closures that still allow two routes')
for n in ['threetwo', 'greedy']:
    E = ed(n)
    keep = [e for e in E if packings([x for x in E if x != e])[0] >= 2]
    log(f'  {n}: {len(keep)} arrows:', fmt_edges(keep))

log('\n== K-1 P5 / 2-3 P3: every pair of arrows that stops all travel on the bowtie')
E = ed('bowtie')
pairs = [c for c in combinations(E, 2) if blocks(E, set(c))]
log(f'  {len(pairs)} pairs:', ' '.join(fmt_edges(p) for p in pairs))
singles = [e for e in E if blocks(E, {e})]
log('  single arrows that block:', singles)

log('\n== K-1 P6 / 2-3 P6: closing game (move that leaves no route wins)')
for n in ['diamond', 'greedy']:
    first, good = game(ed(n))
    log(f'  {n}: first player wins: {first}; winning first moves: {fmt_edges(good)}')
# guide claim: every other first closure on greedy leaves surviving routes sharing one arrow
E = ed('greedy')
for e in E:
    rem = simple_paths(E, closed=frozenset([e]))
    common = set(rem[0]).intersection(*map(set, rem)) if rem else set()
    log(f'    greedy after closing {e[0]+e[1]}: routes {[fmt_path(p) for p in rem]}; common arrows {fmt_edges(sorted(common))}')

log('\n== 2-3 P1')
for n in ['bowtie', 'greedy']:
    k, _ = packings(ed(n)); c, cuts = min_cuts(ed(n))
    log(f'  {n}: max {k}, min {c}; {{sA,sB}} blocks: {blocks(ed(n), {("s","A"),("s","B")})}')

log('\n== 2-3 P2 / 4-5 P2 (bottleneck)')
E = ed('bottleneck')
k, cols = packings(E); c, cuts = min_cuts(E)
log(f'  routes {len(simple_paths(E))}; max {k}; unordered maximum collections {len(cols)}; min {c}; minimum closures:',
    ' '.join(fmt_edges(x) for x in cuts))
S = ['s', 'A', 'B', 'C', 'D']
log('  out-arrows of {s,A,B,C,D}:', fmt_edges([e for e in E if e[0] in S and e[1] not in S]),
    ' in-arrows:', fmt_edges([e for e in E if e[1] in S and e[0] not in S]))
guide_pair = [(('s', 'A'), ('A', 'D'), ('D', 'E'), ('E', 'G'), ('G', 'H'), ('H', 't')),
              (('s', 'C'), ('C', 'D'), ('D', 'F'), ('F', 'G'), ('G', 'J'), ('J', 't'))]
log('  guide routes s-A-D-E-G-H-t, s-C-D-F-G-J-t are routes and edge-disjoint:',
    all(p in simple_paths(E) for p in guide_pair) and edge_disjoint(guide_pair))

log('\n== 2-3 P4: one new arrow between inside dots (not s or t) giving three routes')
for n in ['bottleneck', 'endpoint_two']:
    E = ed(n); inner = [v for v in verts(n) if v not in ('s', 't')]
    good = []
    for u in inner:
        for v in inner:
            if u != v:
                E2 = E + [(u, v)]  # a duplicate of an existing arrow is a parallel arrow
                # packings treats identical tuples as one edge; handle a parallel copy by renaming
                if (u, v) in E:
                    E2 = E + [(u, v + "'"), (v + "'", v)]
                if packings(E2)[0] >= 3:
                    good.append(u + v)
    log(f'  {n}: {len(good)} working arrows:', ' '.join(good))
E = ed('bottleneck') + [('D', 'G')]
three = [(('s', 'A'), ('A', 'D'), ('D', 'E'), ('E', 'G'), ('G', 'H'), ('H', 't')),
         (('s', 'B'), ('B', 'D'), ('D', 'G'), ('G', 'I'), ('I', 't')),
         (('s', 'C'), ('C', 'D'), ('D', 'F'), ('F', 'G'), ('G', 'J'), ('J', 't'))]
log('  guide DG routes valid and disjoint:', all(p in simple_paths(E) for p in three) and edge_disjoint(three))
E = ed('bottleneck') + [('A', 'H')]
log('  e.g. AH: max', packings(E)[0], 'with', [fmt_path(p) for p in packings(E)[1][0]])

log('\n== 2-3 P5 / 4-5 P1: reserved routes, stuck?, largest collections, change-walks')
for n, R in [('greedy', R1), ('doubletrap', RD)]:
    E = ed(n)
    stuck = not simple_paths(E, closed=frozenset(R))
    k, cols = packings(E)
    W = change_walks(E, R)
    log(f'  {n}: reserved {fmt_edges(sorted(R))}; no route fits beside: {stuck}; max {k}; {len(cols)} maximum collections:',
        '; '.join('{' + ', '.join(fmt_path(p) for p in c) + '}' for c in cols))
    log(f'    routes on board: {len(simple_paths(E))}; simple change-walks: {len(W)}')
    for w in W:
        R2 = toggle(R, w); rts, rest = decompose(R2)
        log('     ', '-'.join(['s'] + [a[1] for a in w]), ' cancels', [a[2][0] + a[2][1] for a in w if a[3] == 'cancel'],
            ' reserves', [a[2][0] + a[2][1] for a in w if a[3] == 'reserve'], ' -> routes', [fmt_path(p) for p in rts],
            'disjoint simple:', edge_disjoint(rts) and all(p in simple_paths(E) for p in rts), 'leftover', rest)

log('\n== 4-5 P3 (backward): splits with exactly two cut arrows and at least one arrow back into the Start side')
E = ed('backward')
for S, o, i in splits(E, verts('backward')):
    if len(o) == 2 and i:
        log(f'  S={{{",".join(S)}}} out {fmt_edges(o)} in {fmt_edges(i)}; closing out blocks: {blocks(E, set(o))}')
log('  all splits by out-count:', sorted(len(o) for S, o, i in splits(E, verts('backward'))))
log('  max packing', packings(E)[0])

log('\n== 4-5 P4 (backward): minimum closures and routes using two of their arrows')
k, cols = packings(E); c, cuts = min_cuts(E)
P = simple_paths(E)
log(f'  routes {len(P)}: {[fmt_path(p) for p in P]}')
for cut in cuts:
    two = [p for p in P if len(set(p) & set(cut)) >= 2]
    best_with = {fmt_path(p): max(len(col) for col in [[p]] + [list(cc) for kk in range(1, 3) for cc in combinations(P, kk) if p in cc and edge_disjoint(cc)]) for p in two}
    log(f'  minimum closure {fmt_edges(cut)}: routes using two of its arrows {list(best_with)}; largest collection containing each: {list(best_with.values())}')

log('\n== 4-5 P5 (staircase)')
E = ed('staircase')
log('  no route fits beside the reserved routes:', not simple_paths(E, closed=frozenset(RS)))
W = change_walks(E, RS)
log(f'  simple change-walks: {len(W)}')
for w in W:
    R2 = toggle(RS, w); rts, rest = decompose(R2)
    log('   ', '-'.join(['s'] + [a[1] for a in w]), ' cancels', [a[2][0] + a[2][1] for a in w if a[3] == 'cancel'],
        ' -> routes', [fmt_path(p) for p in rts], 'valid:', edge_disjoint(rts) and all(p in simple_paths(E) for p in rts))
log('  max packing', packings(E)[0], 'min closure', min_cuts(E)[0])

log('\n== 4-5 P6 (bottleneck with two reserved routes)')
E = ed('bottleneck')
reach = residual_reach(E, RB)
o = [e for e in E if e[0] in reach and e[1] not in reach]
i = [e for e in E if e[1] in reach and e[0] not in reach]
log(f'  reachable {sorted(reach)}; out-arrows {fmt_edges(o)} (all reserved: {all(e in RB for e in o)}); in-arrows {fmt_edges(i)}')
log('  reserved routes valid:', all(p in simple_paths(E) for p in guide_pair), ' change-walk exists:', bool(change_walks(E, RB)))
log('  any route fits beside the reserved routes:', bool(simple_paths(E, closed=frozenset(RB))))

# ---------------- return visit ----------------
log('\n== Return visit P1: shared dots vs one route per middle dot')


def vertex_disjoint_max(E, s='s', t='t'):
    P = simple_paths(E, s, t); best = 0
    for k in range(1, len(P) + 1):
        for c in combinations(P, k):
            inner = [e[1] for p in c for e in p if e[1] != t]
            if len(inner) == len(set(inner)) and edge_disjoint(c):
                best = k
    return best


for n in ['hub', 'hub_bypass']:
    E = ed(n)
    log(f'  {n}: edge-disjoint max {packings(E)[0]}; internally vertex-disjoint max {vertex_disjoint_max(E)}; '
        f'min arrow closure {min_cuts(E)[0]}; dots on every route: {sorted(set.intersection(*[set(e[1] for e in p[:-1]) for p in simple_paths(E)]))}')
# guide extension: three-branch hub
E3 = [('s', a) for a in 'abc'] + [(a, 'H') for a in 'abc'] + [('H', x) for x in 'xyz'] + [(x, 't') for x in 'xyz']
log(f'  three-branch hub extension: edge-disjoint max {packings(E3)[0]}, min arrow closure {min_cuts(E3)[0]}, vertex max {vertex_disjoint_max(E3)}')

log('\n== Return visit P2: assigned pairs')
E = ed('pairs')


def pair_fits(E, assign):
    (p, x), (q, y) = assign
    A = simple_paths(E, p, x); B = simple_paths(E, q, y)
    return [(a, b) for a in A for b in B if not set(a) & set(b)], A, B


for assign in [(('P', 'X'), ('Q', 'Y')), (('P', 'Y'), ('Q', 'X'))]:
    fits, A, B = pair_fits(E, assign)
    log(f'  {assign[0][0]}->{assign[0][1]}, {assign[1][0]}->{assign[1][1]}: routes {[fmt_path(a) for a in A]} / {[fmt_path(b) for b in B]}; '
        f'fitting pairs {[(fmt_path(a), fmt_path(b)) for a, b in fits]}')
log('  third map, two different finishes from {X,Y}: only (P->X, Q->Y) and (P->Y, Q->X) exist; the first is map 1.')
# any-dot reading of "finishes"
dots = sorted({v for e in E for v in e} - {'P', 'Q'})
anyfit = [(x, y) for x in dots for y in dots if x != y and pair_fits(E, (('P', x), ('Q', y)))[0]]
log(f'  if a finish may be any dot: {len(anyfit)} ordered choices fit, e.g. {anyfit[:6]}')
adds = []
V = sorted({v for e in E for v in e})
for u in V:
    for v in V:
        if u != v and (u, v) not in E:
            if pair_fits(E + [(u, v)], (('P', 'Y'), ('Q', 'X')))[0]:
                adds.append(u + v)
log(f'  one-arrow additions allowing P->Y and Q->X: {adds}')

log('\n== Return visit P3: lane capacities')
for n in ['capacity3', 'capacity4']:
    E = ed(n); cap = CAPACITY[n]
    P = simple_paths(E)
    best = 0; bestx = []
    for x in product(*[range(6) for _ in P]):
        use = {e: 0 for e in E}
        for p, m in zip(P, x):
            for e in p:
                use[e] += m
        if all(use[e] <= cap[e] for e in E):
            if sum(x) > best:
                best, bestx = sum(x), [x]
            elif sum(x) == best:
                bestx.append(x)
    cuts = sorted((sum(cap[e] for e in o), S) for S, o, i in splits(E, verts(n)))
    log(f'  {n}: route types {[fmt_path(p) for p in P]}; max {best}; optimal multiplicities {bestx}; '
        f'min cut {cuts[0][0]}; cuts of that value: {[S for v, S in cuts if v == cuts[0][0]]}')

open(os.path.join(HERE, 'solve.out'), 'w').write('\n'.join(OUT) + '\n')
