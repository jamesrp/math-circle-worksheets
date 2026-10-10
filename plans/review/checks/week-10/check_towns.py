"""Week 10 base packets: read every town from the three student PDFs and solve every town
problem by exhaustive walk search (graphs.py). Also checks every town answer, example walk,
count and claim the adult guide gives for these problems.
Run: python3 check_towns.py > check_towns.out
"""
import os
import sys
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfread as R
from graphs import Town, edge_game, additions, extra_counters, fewest

FAILS = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + str(detail) if detail != '' else ''))
    if not ok:
        FAILS.append(name)


CACHE = {}


def towns_on(key, page):
    if (key, page) not in CACHE:
        towns, probs, rects, words = R.read_towns(key, page)
        check(f'{key} p{page} reader: every band ends at two island centres, no band over another island', not probs, probs)
        CACHE[(key, page)] = towns
    return CACHE[(key, page)]


def get(key, page, sig, degseq=None):
    """Town on the page whose (islands, bridges) count is sig (and sorted degree sequence degseq, if given);
    also returns island positions."""
    hits = []
    for t in towns_on(key, page):
        names, edges, pos = R.town_graph(t)
        if (len(names), len(edges)) == sig:
            T_ = Town(names, edges)
            if degseq is None or sorted(T_.degrees().values()) == sorted(degseq):
                hits.append((T_, pos))
    assert len(hits) == 1, (key, page, sig, len(hits))
    return hits[0]


def describe(pos, vs):
    """Describe unlabelled islands by position: (x, y) in points."""
    return [f'{v}@({pos[v][0]:.0f},{pos[v][1]:.0f})' for v in sorted(vs)]


def fmt(se):
    return '; '.join(f'{s}->{"".join(sorted(e))}' for s, e in sorted(se.items())) or 'none'


def degs(t):
    d = t.degrees()
    return ' '.join(f'{v}{d[v]}' for v in t.V)


def rank(pos, v, axis):
    return sorted(pos[w][axis] for w in pos).index(pos[v][axis])


print('==== K-1 ====')
# P1 page 1: four towns
tri, ptri = get('k1', 1, (3, 3))
bow, pbow = get('k1', 1, (5, 6), [2, 2, 2, 2, 4])
hs, phs = get('k1', 1, (5, 6), [2, 2, 2, 3, 3])
dia, pdia = get('k1', 1, (4, 5))
for nm, t, pos in [('triangle', tri, ptri), ('bowtie', bow, pbow), ('house', hs, phs), ('diamond', dia, pdia)]:
    se = t.start_end()
    print(f'  K-1 P1 {nm}: degrees {degs(t)}; starts->ends {fmt(se)}')
    check(f'K-1 P1 {nm}: a walk picking up every counter exists', bool(se))
check('K-1 P1 triangle/bowtie: start anywhere (guide)', set(tri.start_end()) == set(tri.V) and set(bow.start_end()) == set(bow.V))
# diamond: starts are the two middle islands (equal y, not top or bottom)
ds = tri_s = set(dia.start_end())
mid = {v for v in dia.V if 0 < rank(pdia, v, 1) < 3}
check('K-1 P1 diamond: starts are exactly the two middle islands (guide picture)', ds == mid, describe(pdia, ds))
hss = set(hs.start_end())
top_sq = sorted(hs.V, key=lambda v: phs[v][1])[1:3]
check('K-1 P1 house: starts are exactly the two upper corners of the square (guide picture)', hss == set(top_sq), describe(phs, hss))

# P2 page 2
lad, plad = get('k1', 2, (6, 7))
trf, ptrf = get('k1', 2, (6, 9))
ls = set(lad.start_end())
midcol = {v for v in lad.V if abs(plad[v][0] - sorted(p[0] for p in plad.values())[2]) < 1}
check('K-1 P2 two squares: starts are exactly the two middle islands', ls == midcol, describe(plad, ls))
check('K-1 P2 two squares: walk from one middle island ends at the other', all(lad.start_end()[s] == midcol - {s} for s in ls))
check('K-1 P2 big triangle: every island, ending where it started', set(trf.start_end()) == set(trf.V) and all(trf.start_end()[s] == {s} for s in trf.V))

# P3 pages 3-4
claw, _ = get('k1', 3, (4, 3))
trip, _ = get('k1', 3, (2, 3))
lol, plol = get('k1', 3, (4, 4))
theta, ptheta = get('k1', 4, (5, 6))
k4, pk4 = get('k1', 4, (4, 6))
exp = [('three-arm star', claw, False), ('two islands, three bridges', trip, True), ('triangle with tail', lol, True),
       ('square with centre, one diagonal', theta, True), ('arc town', k4, False)]
for nm, t, e in exp:
    check(f'K-1 P3 {nm}: walk exists = {e} (guide: {"check" if e else "X"})', t.has_walk() == e, f'degrees {degs(t)}; {fmt(t.start_end())}')
check('K-1 P3 two islands: both islands are starts ("any island")', set(trip.start_end()) == set(trip.V))
d = lol.degrees()
check('K-1 P3 triangle with tail: starts are the 3-bridge corner and the tail tip', set(lol.start_end()) == {v for v in lol.V if d[v] % 2}, describe(plol, set(lol.start_end())))
d = theta.degrees()
ts = set(theta.start_end())
check('K-1 P3 square with centre: starts are the two corners on the diagonal (top right, bottom left in guide)',
      ts == {v for v in theta.V if d[v] == 3} and len(ts) == 2, describe(ptheta, ts))

# P4 pages 5-6
rd, _ = get('k1', 5, (3, 4))
ds_, _ = get('k1', 5, (3, 3))
sq2, psq2 = get('k1', 5, (4, 5))
flw, _ = get('k1', 6, (7, 9))
ldr, _ = get('k1', 6, (6, 8))
for nm, t, e in [('row of two double bridges', rd, True), ('double then single', ds_, False), ('square, doubled bottom', sq2, False),
                 ('three triangles (flower)', flw, True), ('two squares, doubled middle rung', ldr, True)]:
    check(f'K-1 P4 {nm}: closed walk = {e}', t.has_closed() == e, f'degrees {degs(t)}; {fmt(t.start_end())}')
    if not e:
        check(f'K-1 P4 {nm}: every counter can still be picked up, ending elsewhere (guide "ends elsewhere")', t.has_walk())
sqs = set(sq2.start_end())
check('K-1 P4 square with doubled bottom: filled islands are the two bottom corners (guide picture)',
      sqs == set(sorted(sq2.V, key=lambda v: -psq2[v][1])[:2]), describe(psq2, sqs))

# P6 pages 9-10
for nm, sig, pg in [('three-arm star', (4, 3), 9), ('square with centre and both diagonals', (5, 8), 9), ('square with two tails', (6, 6), 10)]:
    t, pos = get('k1', pg, sig)
    check(f'K-1 P6 {nm}: nobody can pick up every counter (as the page says)', not t.has_walk())
    adds = additions(t, 1)
    odd = t.odd()
    check(f'K-1 P6 {nm}: exactly 6 single new bridges work, = the pairs of odd islands (guide)',
          sorted(tuple(sorted(a[0])) for a in adds) == sorted(itertools.combinations(odd, 2)), f'{len(adds)} work; odd {describe(pos, odd)}')
    ok = all(set(t.plus(a).start_end()) == set(odd) - set(a[0]) for a in adds)
    check(f'K-1 P6 {nm}: afterwards the starts are the two odd islands not joined (guide)', ok)

# P8 pages 11-12
for nm, sig, pg, want in [('arc town', (4, 6), 11, 'all'), ('square with two tails', (6, 6), 11, 'tails'),
                          ('square with centre and both diagonals', (5, 8), 12, 'sides')]:
    t, pos = get('k1', pg, sig)
    works = [i for i in range(len(t.E)) if t.doubled([i]).has_walk()]
    d = t.degrees()
    if want == 'all':
        ok = len(works) == len(t.E)
    elif want == 'tails':
        ok = sorted(works) == sorted(i for i, (a, b) in enumerate(t.E) if min(d[a], d[b]) == 1)
    else:
        ok = sorted(works) == sorted(i for i, (a, b) in enumerate(t.E) if d[a] == 3 and d[b] == 3)
    check(f'K-1 P8 {nm}: bridges where two counters work = {want} (guide)', ok,
          f'{len(works)} of {len(t.E)}: ' + ', '.join(f'{t.E[i][0]}-{t.E[i][1]}' for i in works))

print('==== Grades 2-3 and 4-5 ====')
for band in ('g23', 'g45'):
    B = '2-3' if band == 'g23' else '4-5'
    house, _ = get(band, 1, (5, 6))
    tail, _ = get(band, 1, (4, 4))
    dbl, _ = get(band, 1, (3, 4))
    check(f'{B} P1 house: starts B or C, ending at the other', house.start_end() == {'B': {'C'}, 'C': {'B'}}, fmt(house.start_end()))
    check(f'{B} P1 triangle with tail: starts A or C, ending at the other', tail.start_end() == {'A': {'C'}, 'C': {'A'}}, fmt(tail.start_end()))
    check(f'{B} P1 two double bridges: any island, closed', dbl.start_end() == {v: {v} for v in dbl.V}, fmt(dbl.start_end()))
    for w in ['BACBDEC']:
        check(f'{B} guide P1 example {" ".join(w)} is a walk in the house', house.is_walk(w))
    check(f'{B} guide P1 example A C B D C is a walk in the tail town', tail.is_walk('ACBDC'))
    check(f'{B} guide P1 example A B C B A is a walk in the doubles town', dbl.is_walk('ABCBA'))
    t1, _ = get(band, 2, (6, 6))
    t2, _ = get(band, 2, (6, 7))
    t3, _ = get(band, 3, (6, 8))
    t4, _ = get(band, 3, (7, 9))
    check(f'{B} P2 town 1: none (D has 5 bridges; A, C, F have 1)', not t1.has_walk() and t1.degrees()['D'] == 5
          and [v for v in t1.V if t1.degrees()[v] == 1] == ['A', 'C', 'F'], degs(t1))
    check(f'{B} P2 town 2: start A or D, end at the other', t2.start_end() == {'A': {'D'}, 'D': {'A'}}, fmt(t2.start_end()))
    check(f'{B} P2 town 3: start D or F, end at the other', t3.start_end() == {'D': {'F'}, 'F': {'D'}}, fmt(t3.start_end()))
    check(f'{B} P2 town 4: any island, closed', t4.start_end() == {v: {v} for v in t4.V}, fmt(t4.start_end()))
    # fallback game on the house (guide p. 2)
    res = {s: edge_game(house, s) for s in house.V}
    check(f'{B} house bridge game: first player wins from A, D, E; second from B, C (guide p. 2)',
          res == {'A': True, 'B': False, 'C': False, 'D': True, 'E': True}, res)

# Grades 2-3 only
trf, _ = get('g23', 4, (6, 9))
dtri, _ = get('g23', 4, (3, 4))
arc, _ = get('g23', 5, (4, 6))
spk, _ = get('g23', 5, (5, 7))
check('2-3 P3 big triangle: every island', set(trf.start_end()) == set(trf.V))
check('2-3 P3 triangle with a double bridge: A and C', set(dtri.start_end()) == {'A', 'C'}, fmt(dtri.start_end()))
check('2-3 P3 arc town: none, all four odd', not arc.has_walk() and arc.odd() == ['A', 'B', 'C', 'D'], degs(arc))
check('2-3 P3 square with three spokes: none, B C D E odd', not spk.has_walk() and spk.odd() == ['B', 'C', 'D', 'E'], degs(spk))
star, _ = get('g23', 6, (4, 3))
tails, _ = get('g23', 6, (6, 6))
lad4, _ = get('g23', 7, (8, 10))
for nm, t, odd, add, walk in [('star', star, 'ABCD', ('C', 'D'), 'ABCDB'), ('square with tails', tails, 'BCDE', ('B', 'E'), 'CBEABFED'),
                              ('ladder', lad4, 'BCFG', ('B', 'G'), 'CBGCDHGFEABF')]:
    check(f'2-3 P4 {nm}: no walk as printed; odd islands {odd}', not t.has_walk() and ''.join(t.odd()) == odd, degs(t))
    adds = additions(t, 1)
    check(f'2-3 P4 {nm}: exactly the 6 bridges joining two odd islands work', sorted(tuple(sorted(a[0])) for a in adds) == sorted(itertools.combinations(odd, 2)), len(adds))
    check(f'2-3 P4 {nm}: walk then runs between the other two odd islands', all(
        set(t.plus(a).start_end()) == set(odd) - set(a[0]) for a in adds))
    check(f'2-3 guide P4 {nm}: add {add[0]}-{add[1]}, walk {" ".join(walk)} is valid', t.plus([add]).is_walk(walk))
house5, _ = get('g23', 7, (5, 6))
arc5, _ = get('g23', 7, (4, 6))
H, _ = get('g23', 8, (6, 5))
for nm, t, k, n in [('house', house5, 1, 1), ('arc town', arc5, 2, 3), ('H town', H, 3, 15)]:
    kk, sols = fewest(lambda k: additions(t, k, closed=True))
    check(f'2-3 P5 {nm}: fewest new bridges for a closed walk = {k}, in {n} ways (guide)', kk == k and len(sols) == n,
          f'{kk}, {len(sols)} ways: ' + '; '.join('+'.join(a + b for a, b in s) for s in sols[:15]))
arc10, _ = get('g23', 12, (4, 6))
claw10, _ = get('g23', 12, (4, 3))
for nm, t, k, n in [('arc town', arc10, 2, 3), ('three-arm star', claw10, 3, 1)]:
    sols = None
    for kk in range(len(t.E) + 1):
        s = [c for c in itertools.combinations(range(len(t.E)), kk) if t.doubled(c).has_closed()]
        if s:
            sols = (kk, s)
            break
    check(f'2-3 P10 {nm}: fewest bridges with a second counter = {k}, in {n} ways (guide)', sols[0] == k and len(sols[1]) == n,
          f'{sols[0]}: ' + '; '.join('+'.join(t.E[i][0] + t.E[i][1] for i in c) for c in sols[1]))
    if nm == 'arc town':
        check('2-3 P10 arc town: the solutions are exactly the pairs of bridges with no island in common',
              all(not (set(t.E[c[0]]) & set(t.E[c[1]])) for c in sols[1]))

# Grades 4-5 only
lad, _ = get('g45', 4, (8, 10))
bowt, _ = get('g45', 4, (5, 6))
grd, _ = get('g45', 5, (9, 13))
check('4-5 P3 2 by 4 ladder: none (B, C, F, G have 3)', not lad.has_walk() and lad.odd() == ['B', 'C', 'F', 'G'], degs(lad))
check('4-5 P3 bowtie: anywhere, ending where it started', bowt.start_end() == {v: {v} for v in bowt.V}, fmt(bowt.start_end()))
check('4-5 P3 3 by 3 grid with B-D: F to H or H to F only', grd.start_end() == {'F': {'H'}, 'H': {'F'}}, fmt(grd.start_end()))
check('4-5 P3 grid: the diagonal joins B and D', ('B', 'D') in grd.E or ('D', 'B') in grd.E)

arcU, _ = get('g45', 11, (4, 6))
clawU, _ = get('g45', 11, (4, 3))
diagU, _ = get('g45', 12, (6, 8))
for nm, t, want in [('arc town', arcU, (2, 1)), ('three-arm star', clawU, (3, 1)), ('diagonals town', diagU, (2, 0))]:
    kc, sc = fewest(lambda k: extra_counters(t, k, closed=True))
    ko, so = fewest(lambda k: extra_counters(t, k, closed=False))
    lab = lambda c: '+'.join(t.E[i][0] + t.E[i][1] for i in c) or '(none)'
    check(f'4-5 P10 {nm}: (closed, open) = {want} (guide)', (kc, ko) == want,
          f'closed {kc}: {"; ".join(lab(c) for c in sc)} | open {ko}: {"; ".join(lab(c) for c in so)}')
    if nm == 'arc town':
        check('4-5 P10 arc town closed: exactly the 3 pairs of bridges with no island in common', len(sc) == 3 and all(len(set(c)) == 2 and not (set(t.E[c[0]]) & set(t.E[c[1]])) for c in sc))
        check('4-5 P10 arc town open: any one bridge', len(so) == 6)
    if nm == 'three-arm star':
        check('4-5 P10 star closed: all three bridges, the only way', len(sc) == 1 and sorted(sc[0]) == [0, 1, 2])
        check('4-5 P10 star open: any one bridge', len(so) == 3)
    if nm == 'diagonals town':
        got = set(frozenset(frozenset(t.E[i]) for i in c) for c in sc)
        want_set = {frozenset([frozenset('DE'), frozenset('EF')]), frozenset([frozenset('BD'), frozenset('BF')])}
        check('4-5 P10 diagonals town closed: D-E and E-F, or D-B and B-F, only', got == want_set and len(sc) == 2)
check('4-5 P11: arc town has four odd islands and no closed route with 1 extra counter', arcU.odd() == ['A', 'B', 'C', 'D'] and not extra_counters(arcU, 1, True))

# Lee (P8)
lee, ppos = get('g45', 9, (10, 18))
outside = 'ABCDEFGHIA'
check('4-5 P8 Lee\'s walk A B C D E F G H I A uses 9 distinct drawn bridges', lee.is_walk(outside) is False and all(
    (a, b) in lee.E or (b, a) in lee.E for a, b in zip(outside, outside[1:])))
inner = [e for e in lee.E if frozenset(e) not in {frozenset(p) for p in zip(outside, outside[1:])}]
check('4-5 P8 the 9 inside bridges form triangles B I J, C E J, F H J', set(frozenset(e) for e in inner) == set(
    frozenset(e) for e in [('B', 'I'), ('I', 'J'), ('J', 'B'), ('C', 'E'), ('E', 'J'), ('J', 'C'), ('F', 'H'), ('H', 'J'), ('J', 'F')]) and len(inner) == 9, inner)
check('4-5 P8 guide walk A B J I B C J E C D E F J H F G H I A crosses every bridge once', lee.is_walk('ABJIBCJECDEFJHFGHIA'))


def lee_count(directional):
    lee_edges = [frozenset(p) for p in zip(outside, outside[1:])]
    lee_dir = list(zip(outside, outside[1:]))
    idx_of = {}
    for i, e in enumerate(lee.E):
        idx_of.setdefault(frozenset(e), []).append(i)
    lee_idx = [idx_of[e][0] for e in lee_edges]
    pos_in_lee = {i: k for k, i in enumerate(lee_idx)}
    n = 0
    seqs = []

    def rec(v, mask, nextk, path):
        nonlocal n
        if mask == lee.full:
            if v == 'A':
                n += 1
                seqs.append(path)
            return
        for i, w in lee.inc[v]:
            if mask >> i & 1:
                continue
            if i in pos_in_lee:
                if pos_in_lee[i] != nextk:
                    continue
                if directional and (v, w) != lee_dir[nextk]:
                    continue
                rec(w, mask | 1 << i, nextk + 1, path + w)
            else:
                rec(w, mask | 1 << i, nextk, path + w)
    rec('A', 0, 0, 'A')
    return n, seqs


n_dir, seqs = lee_count(True)
n_any, _ = lee_count(False)
check('4-5 P8 guide: 352 walks keep Lee\'s order and direction', n_dir == 352, f'{n_dir} with direction kept, {n_any} with order only')
check('4-5 P8 guide example is among them', 'ABJIBCJECDEFJHFGHIA' in seqs)
print('  Euler circuits of Lee\'s town from A (all):', lee.count_trails('A', closed=True))

print()
print('FAILURES:', FAILS if FAILS else 'none')
