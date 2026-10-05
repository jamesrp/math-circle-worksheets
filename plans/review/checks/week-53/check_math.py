"""Independent exhaustive check of every Week 53 problem and every finite claim
in the adult guide. Uses only the hand transcription in check_diagrams.T (which
check_diagrams.py verifies against the delivered PDF). Imports no writer code.

Run: python3 check_math.py   (writes out_check_math.txt beside itself)
"""
import itertools
import os as _os
import random
import sys
from collections import Counter

HERE = _os.path.dirname(_os.path.abspath(__file__))
sys.path.insert(0, HERE)
from check_diagrams import T  # noqa: E402

out = []


def say(*a):
    s = ' '.join(str(x) for x in a)
    out.append(s)


def places(edges):
    return sorted(set(''.join(edges)))


def connected(vs, es):
    par = {v: v for v in vs}

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for e in es:
        par[f(e[0])] = f(e[1])
    return len({f(v) for v in vs}) == 1


def acyclic(vs, es):
    par = {v: v for v in vs}

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for e in es:
        a, b = f(e[0]), f(e[1])
        if a == b:
            return False
        par[a] = b
    return True


def catalog(price):
    """All connected spanning purchases, trees, minimum and optimal purchases."""
    E = sorted(price)
    V = places(E)
    conn, trees = [], []
    for r in range(len(E) + 1):
        for S in itertools.combinations(E, r):
            if connected(V, S):
                conn.append(S)
                if acyclic(V, S):
                    trees.append(S)
    cost = lambda S: sum(price[e] for e in S)
    m = min(cost(S) for S in conn)
    opt = [S for S in conn if cost(S) == m]
    return {'V': V, 'E': E, 'subsets': 2 ** len(E), 'conn': conn, 'trees': trees, 'min': m, 'opt': opt,
            'cost': cost}


def swaps(price, bought):
    """All legal one-link swaps (buy unused, return bought, result connected) from a fixed input."""
    V = places(price)
    base = sum(price[e] for e in bought)
    res = []
    for buy in sorted(set(price) - set(bought)):
        for ret in sorted(bought):
            S = (set(bought) - {ret}) | {buy}
            ok = connected(V, S)
            res.append((ret, buy, base - price[ret] + price[buy], ok))
    return base, res


def fmt(S):
    return '/'.join(S)


g = {}
for page, diags in T.items():
    for name, pr, bought in diags:
        if all(isinstance(v, int) for v in pr.values()):
            g[name] = (pr, bought)

say('=== Fixed priced maps: complete catalogs ===')
cov = {}
for name in ['convention available', 'P1 left', 'P1 right', 'P2', 'P3', 'P4', 'P5 demo before', 'P5 left', 'P6', 'P9']:
    pr, _ = g[name]
    c = catalog(pr)
    cov[name] = c
    assert all(acyclic(c['V'], S) for S in c['opt']), name
    say('%-22s subsets %4d connected %4d trees %3d  min %2d  optima %d: %s  (sum of all prices %d, links %d)' % (
        name, c['subsets'], len(c['conn']), len(c['trees']), c['min'], len(c['opt']),
        '; '.join(fmt(S) for S in c['opt']), sum(pr.values()), len(pr)))
say('Total trees over the ten fixed weighted maps listed in the guide:', sum(len(c['trees']) for c in cov.values()))

say('\n=== P1 ===')
for n in ('P1 left', 'P1 right'):
    c = cov[n]
    say(n, 'two-link purchases:', ', '.join('%s=%d' % (fmt(S), c['cost'](S)) for S in c['trees']))

say('\n=== P3 trap ===')
pr = g['P3'][0]
cheap3 = sorted(pr, key=lambda e: pr[e])[:3]
say('three cheapest links', cheap3, 'cost', sum(pr[e] for e in cheap3), 'connected?', connected('ABCD', cheap3))
say('cheapest connected purchase costing < 7 exists?', any(cov['P3']['cost'](S) < 7 for S in cov['P3']['conn']))
say('second-cheapest connected purchase cost:', sorted({cov['P3']['cost'](S) for S in cov['P3']['conn']})[:3])

say('\n=== P4: greedy-by-price failure ===')
pr = g['P4'][0]
cheap = sorted(pr, key=lambda e: pr[e])
say('price order', [(e, pr[e]) for e in cheap])
say('four cheapest AB/AC/BC/CD connect all five?', connected('ABCDE', ['AB', 'AC', 'BC', 'CD']))

say('\n=== P5 swap demo ===')
pr, b = g['P5 demo before']
base, res = swaps(pr, b)
say('demo before', sorted(b), 'cost', base, '; after buy UW', base + pr['UW'], '; after return VW', base + pr['UW'] - pr['VW'])

for n in ('P5 left', 'P5 right', 'P8 top', 'P8 bottom'):
    pr, b = g[n]
    base, res = swaps(pr, b)
    better = [r for r in res if r[3] and r[2] < base]
    illegal_cheaper = [r for r in res if not r[3] and r[2] < base]
    say('\n=== %s: input %s cost %d ===' % (n, fmt(sorted(b)), base))
    say('cheaper legal swaps (%d):' % len(better), '; '.join('return %s buy %s -> %d' % r[:3] for r in better) or 'none')
    say('cheaper-total but disconnected swaps:', '; '.join('return %s buy %s -> %d' % r[:3] for r in illegal_cheaper) or 'none')
    c = catalog(pr)
    say('input is optimal?', base == c['min'], '(min %d)' % c['min'])

say('\n=== P6: every / some / none ===')
pr = g['P6'][0]
c = cov['P6']
for e in sorted(pr):
    k = sum(1 for S in c['opt'] if e in S)
    say('  %s=%d in %d of %d optima -> %s' % (e, pr[e], k, len(c['opt']),
                                          'every' if k == len(c['opt']) else ('none' if k == 0 else 'some')))
V = c['V']
bridges = [e for e in pr if not connected(V, [f for f in pr if f != e])]
say('bridges:', bridges or 'none')
# cut certificates
for side in ['A', 'AB', 'ABC', 'E', 'F']:
    cross = sorted((pr[e], e) for e in pr if (e[0] in side) != (e[1] in side))
    uniq = cross[0][0] < cross[1][0]
    say('  cut {%s}: %s -> uniquely cheapest %s' % (','.join(side), cross, cross[0][1] if uniq else 'TIE'))
for cyc in [('AB', 'BC', 'AC'), ('DE', 'EF', 'DF'), ('BC', 'CD', 'BD'), ('CD', 'DE', 'CE')]:
    ps = sorted((pr[e], e) for e in cyc)
    say('  cycle %s: %s -> uniquely dearest %s' % ('-'.join(cyc), ps, ps[-1][1] if ps[-1][0] > ps[-2][0] else 'TIE'))
# Is every excluded link certified by some cycle where it is uniquely dearest, every forced by some cut?
say('Second-best purchases on P6 (cost, count):', sorted(Counter(c['cost'](S) for S in c['trees']).items())[:3])

say('\n=== P7: all 4^6 price assignments on the K4 map ===')
E7 = ['AB', 'BC', 'AC', 'AD', 'BD', 'CD']
trees7 = [S for r in (3,) for S in itertools.combinations(E7, r) if connected('ABCD', S)]
conn7 = [S for r in range(7) for S in itertools.combinations(E7, r) if connected('ABCD', S)]
say('K4: subsets 64, connected', len(conn7), 'trees', len(trees7))
dist = Counter()
for ps in itertools.product([1, 2, 3, 4], repeat=6):
    pr = dict(zip(E7, ps))
    costs = [sum(pr[e] for e in S) for S in conn7]
    m = min(costs)
    nopt = sum(1 for x in costs if x == m)
    dist[nopt] += 1
say('optimum-count distribution:', dict(sorted(dist.items())))
say('unique:', dist[1], 'several:', sum(v for k, v in dist.items() if k > 1))
for label, ps in [('unique witness', (1, 1, 3, 2, 3, 4)), ('multiple witness', (1, 2, 2, 1, 4, 4))]:
    pr = dict(zip(E7, ps))
    c = catalog(pr)
    say(label, pr, '-> min', c['min'], 'optima', [fmt(S) for S in c['opt']])

say('\n=== P8 general claims (finite sanity checks; the proof is in the guide) ===')
# (a) local optimality of a spanning tree <=> global, over every tree of every fixed map
def local_opt(pr, T):
    base, res = swaps(pr, T)
    return not any(ok and nc < base for _, _, nc, ok in res)

bad = 0; checked = 0
for name, c in cov.items():
    pr = g[name][0]
    for Tt in c['trees']:
        checked += 1
        if local_opt(pr, Tt) != (c['cost'](Tt) == c['min']):
            bad += 1
say('fixed maps: %d trees checked, local/global mismatches %d' % (checked, bad))
# random small graphs with positive integer prices incl. ties
random.seed(53)
bad = 0; checked = 0
for trial in range(3000):
    n = random.randint(3, 6)
    V = 'ABCDEF'[:n]
    allE = [a + b for a, b in itertools.combinations(V, 2)]
    E = [e for e in allE if random.random() < 0.6]
    if not connected(V, E):
        continue
    pr = {e: random.randint(1, 4) for e in E}
    c = catalog(pr)
    for Tt in c['trees']:
        checked += 1
        if local_opt(pr, Tt) != (c['cost'](Tt) == c['min']):
            bad += 1
say('random graphs: %d trees checked, local/global mismatches %d' % (checked, bad))
# (b) loopy counterexample: triangle of price-1 links
pr = {'AB': 1, 'BC': 1, 'AC': 1}
base, res = swaps(pr, ['AB', 'BC', 'AC'])
say('triangle all bought: cost', base, 'swaps available', len(res), 'min', catalog(pr)['min'])

say('\n=== P9 and distinct-price uniqueness ===')
say('P9 optimum', [fmt(S) for S in cov['P9']['opt']], 'cost', cov['P9']['min'])
bad = 0; checked = 0
for trial in range(3000):
    n = random.randint(3, 6)
    V = 'ABCDEF'[:n]
    allE = [a + b for a, b in itertools.combinations(V, 2)]
    E = [e for e in allE if random.random() < 0.6]
    if not connected(V, E):
        continue
    ps = random.sample(range(1, 30), len(E))
    pr = dict(zip(E, ps))
    checked += 1
    if len(catalog(pr)['opt']) != 1:
        bad += 1
say('random distinct-price graphs: %d checked, non-unique %d' % (checked, bad))

say('\n=== Guide p.6 bottom-input data ===')
pr, b = g['P8 bottom']
say('bottom input links/prices:', [(e, pr[e]) for e in sorted(b)], 'unused:', [(e, pr[e]) for e in sorted(set(pr) - set(b))])

txt = '\n'.join(out)
print(txt)
open(_os.path.join(HERE, 'out_check_math.txt'), 'w').write(txt + '\n')
