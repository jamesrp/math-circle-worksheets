"""Recompute every answer printed in the adult guide from the student pages themselves.

Towns, pictures and the Konigsberg map are read back out of final/src/*.tex by parse_pages.py
(island centres, band paths, stroke segments, land shapes); nothing is taken from the
author's Python objects, comments or check output, or from the reviews.  Walks are found by
exhaustive search (euler.py), not by the parity rule, so the rule itself is being checked.

Run:  python3 check_answers.py      (writes check-output.txt next to this file and stops with an
                                       AssertionError if any answer printed in the guide is wrong)
"""

import itertools
import math
import os
import re
import sys
from functools import lru_cache

from parse_pages import load, land_at, poly_dist, poly_len, point_at_len, SRC
from euler import start_end, degrees, one_walk, count_walks, has_walk, fewest_extra, connected
from pictures_graph import analyse

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s=''):
    OUT.append(s)


def names(t, xs):
    return sorted(t.name(x) for x in xs)


def walk_str(t, w):
    return ' '.join(t.name(x) for x in w)


def summary(t):
    E = t.edges()
    d = degrees(t.n, E)
    se = start_end(t.n, E)
    starts = {t.name(s): ''.join(sorted(t.name(e) for e in es)) for s, es in se.items()}
    odd = [i for i in range(t.n) if d[i] % 2]
    return d, se, starts, odd


def all_pairs(t):
    return [(u, v) for u, v in itertools.combinations(range(t.n), 2)]


def pair_str(t, pr):
    return '-'.join(sorted([t.name(pr[0]), t.name(pr[1])]))


# ------------------------------------------------------------------ geometry: room for a counter

BAND_W = float(re.search(r'bandout/.style=\{line width=([0-9.]+)cm', open(os.path.join(SRC, 'k-1.tex')).read()).group(1))


def counter_room(t):
    """For each bridge: (visible length between island edges, clearance from the bridge's midpoint
    to the nearest other band edge or other island edge), in cm."""
    out = []
    for i, b in enumerate(t.br):
        L = poly_len(b['pts'])
        m = point_at_len(b['pts'], L / 2)
        ru, rv = t.isl[b['u']]['r'], t.isl[b['v']]['r']
        vis = L - ru - rv
        clr = 99.0
        for j, b2 in enumerate(t.br):
            if j != i:
                clr = min(clr, poly_dist(m, b2['pts']) - BAND_W / 2)
        for k, d in enumerate(t.isl):
            if k not in (b['u'], b['v']):
                clr = min(clr, math.dist(m, d['c']) - d['r'])
        out.append((vis, clr))
    return out


# ------------------------------------------------------------------ two-player fallback game

def game_first_player_wins(t, start):
    """Players take turns moving one shared token across a bridge that still has its counter, and
    take the counter.  A player who cannot move loses.  True if the first player wins."""
    E = t.edges()

    @lru_cache(maxsize=None)
    def win(x, mask):
        for i, (u, v) in enumerate(E):
            if not mask >> i & 1 and x in (u, v):
                y = v if x == u else u
                if not win(y, mask | 1 << i):
                    return True
        return False

    return win(start, 0)


# ------------------------------------------------------------------ small-town searches (2-3 P8, P9; 4-5 P6)

def multigraphs(n, m):
    pairs = list(itertools.combinations(range(n), 2))
    for combo in itertools.combinations_with_replacement(range(len(pairs)), m):
        E = [pairs[i] for i in combo]
        if connected(n, E):
            yield E


def start_set(n, E):
    return set(start_end(n, E))


def main():
    P = {stem: {pr['num']: pr for pr in load(stem)} for stem in ['k-1', 'grades-2-3', 'grades-4-5']}
    K, M, U = P['k-1'], P['grades-2-3'], P['grades-4-5']
    ok = []

    def check(cond, what):
        ok.append((bool(cond), what))
        if not cond:
            say('   *** MISMATCH: ' + what)

    # ============================================================ K-1
    say('K-1 (islands are not lettered; names give the place in the town)')
    # P1
    t1 = K[1]['towns']
    say('P1 (page %s)' % K[1]['pages'])
    for t, kind in zip(t1, ['triangle', 'bowtie', 'diamond', 'house']):
        d, se, starts, odd = summary(t)
        say(f'  {kind}: {t.n} islands {len(t.br)} bridges, degrees {d}; possible starts {sorted(starts)}')
    check([len(summary(t)[1]) for t in t1] == [3, 5, 2, 2], 'K-1 P1: triangle and bowtie start anywhere, diamond and house from 2 islands')
    check(sorted(summary(t1[2])[2]) == ['left', 'right'], 'K-1 P1 diamond: start at the left or right middle island')
    check(sorted(summary(t1[3])[2]) == ['left', 'right'], 'K-1 P1 house: start where the roof meets the walls')
    # P2
    say('P2 (page %s)' % K[2]['pages'])
    a, b = K[2]['towns']
    for t in (a, b):
        d, se, starts, odd = summary(t)
        say(f'  {t.n} islands {len(t.br)} bridges: starts {starts}')
    check(summary(a)[2] == {'bottom': 'top', 'top': 'bottom'}, 'K-1 P2 ladder: only the two middle islands, ending at the other')
    check(len(summary(b)[1]) == 6 and all(s in e for s, e in summary(b)[1].items()), 'K-1 P2 big triangle: all six, back to start')
    # P3: check or X (any walk)
    res = []
    for t in K[3]['towns']:
        res.append('yes' if summary(t)[1] else 'X')
        say(f'  P3 town p{t.page}: {t.n} islands, {len(t.br)} bridges, degrees {summary(t)[0]}: {res[-1]}; starts {sorted(summary(t)[2])}')
    check(res == ['X', 'yes', 'yes', 'yes', 'X'], 'K-1 P3: X, yes, yes, yes, X')
    # P4: closed walk
    res = []
    for t in K[4]['towns']:
        se = summary(t)[1]
        closed = any(s in e for s, e in se.items())
        res.append('yes' if closed else ('X (open walk only)' if se else 'X'))
        say(f'  P4 town p{t.page}: {t.n} islands, {len(t.br)} bridges, degrees {summary(t)[0]}: {res[-1]}')
    check(res == ['yes', 'X (open walk only)', 'X (open walk only)', 'yes', 'yes'], 'K-1 P4: yes, X, X, yes, yes')
    # P5 pictures (pairs of copies)
    pics = K[5]['pictures']
    res = []
    for p in pics[::2]:
        a_ = analyse(p)
        res.append(a_['strokes'])
        say(f'  P5 picture p{p.page}: odd points {a_["odd"]}, fewest strokes {a_["strokes"]}')
    check(res == [1, 1, 2, 1, 2, 1], 'K-1 P5: cross out the envelope (3rd) and the circle with a plus (5th)')
    check(all(analyse(pics[2 * i])['odd'] == analyse(pics[2 * i + 1])['odd'] for i in range(6)), 'K-1 P5: both copies alike')
    # P6: one new bridge
    say('P6 one new bridge (any start allowed):')
    for t in K[6]['towns']:
        good = [pr for pr in all_pairs(t) if has_walk(t.n, t.edges() + [pr])]
        odd = summary(t)[3]
        say(f'  town p{t.page}: odd islands {names(t, odd)}; working new bridges {[pair_str(t, g) for g in good]}')
        check(sorted(good) == sorted(itertools.combinations(sorted(odd), 2)) and len(odd) == 4,
              'K-1 P6: works exactly for a bridge joining two of the four odd islands')
    # P8: double one bridge
    say('P8 doubled bridge:')
    res = []
    for t in K[8]['towns']:
        E = t.edges()
        good = [i for i in range(len(E)) if has_walk(t.n, E + [E[i]])]
        res.append(len(good))
        say(f'  town p{t.page}: {len(good)} of {len(E)} bridges work: {[pair_str(t, E[i]) for i in good]}')
    check(res == [6, 2, 4], 'K-1 P8: all 6; the 2 tail bridges; the 4 sides')
    t8 = K[8]['towns']
    E = t8[1].edges(); d = summary(t8[1])[0]
    check(all(min(d[u], d[v]) == 1 for u, v in [E[i] for i in range(len(E)) if has_walk(t8[1].n, E + [E[i]])]),
          'K-1 P8 town 2: the working bridges are the tails')
    E = t8[2].edges(); d = summary(t8[2])[0]
    check(all(d[u] == 3 and d[v] == 3 for u, v in [E[i] for i in range(len(E)) if has_walk(t8[2].n, E + [E[i]])]),
          'K-1 P8 town 3: the working bridges are the sides (corner to corner)')
    # P7: example towns of 4 hexagons
    can = [[(0, 1), (1, 2), (2, 3), (3, 0)], [(0, 1), (1, 2), (2, 3)]]
    cannot = [[(0, 1), (0, 2), (0, 3)], [(0, 1), (1, 2), (2, 0), (0, 3), (1, 3), (2, 3)]]
    check(all(has_walk(4, E) for E in can) and not any(has_walk(4, E) for E in cannot),
          'K-1 P7 examples: square and row of 4 can; star of 3 sticks and triangle-with-centre cannot')

    # ============================================================ grades 2-3
    say()
    say('GRADES 2-3')
    m1 = M[1]['towns']
    ex = {0: 'B A C B D E C', 1: 'A C B D C', 2: 'A B C B A'}
    for k, t in enumerate(m1):
        d, se, starts, odd = summary(t)
        say(f'  P1 town {k + 1}: starts {starts}')
    check(summary(m1[0])[2] == {'B': 'C', 'C': 'B'}, '2-3 P1 house: B to C')
    check(summary(m1[1])[2] == {'A': 'C', 'C': 'A'}, '2-3 P1 lollipop: A to C')
    check(summary(m1[2])[2] == {'A': 'A', 'B': 'B', 'C': 'C'}, '2-3 P1 doubles: anywhere, closed')
    for k, t in enumerate(m1):
        check(is_walk(t, ex[k]), f'2-3/4-5 P1 example walk {ex[k]}')
    exp2 = [{}, {'A': 'D', 'D': 'A'}, {'D': 'F', 'F': 'D'}, {c: c for c in 'ABCDEFG'}]
    for k, t in enumerate(M[2]['towns']):
        d, se, starts, odd = summary(t)
        say(f'  P2 town {k + 1}: degrees {dict((t.name(i), d[i]) for i in range(t.n))}; starts {starts}')
        check(starts == exp2[k], f'2-3 P2 town {k + 1}: {exp2[k] or "none"}')
    exp3 = [set('ABCDEF'), {'A', 'C'}, set(), set()]
    for k, t in enumerate(M[3]['towns']):
        d, se, starts, odd = summary(t)
        say(f'  P3 town {k + 1}: degrees {dict((t.name(i), d[i]) for i in range(t.n))}; starts {starts}')
        check(set(starts) == exp3[k], f'2-3 P3 town {k + 1}: circle {sorted(exp3[k]) or "none"}')
    # P4: one new bridge
    ex4 = [('C', 'D', 'A B C D B'), ('B', 'E', 'C B E A B F E D'), ('B', 'G', 'C B G C D H G F E A B F')]
    for k, t in enumerate(M[4]['towns']):
        good = [pr for pr in all_pairs(t) if has_walk(t.n, t.edges() + [pr])]
        odd = summary(t)[3]
        say(f'  P4 town {k + 1}: odd {names(t, odd)}; working new bridges {[pair_str(t, g) for g in good]}')
        check(sorted(good) == sorted(itertools.combinations(sorted(odd), 2)) and len(odd) == 4,
              f'2-3 P4 town {k + 1}: any bridge joining two of {names(t, odd)}')
        u, v, w = ex4[k]
        check(is_walk(t, w, extra=[(u, v)]), f'2-3 P4 town {k + 1}: example new bridge {u}-{v}, walk {w}')
    # P5: fewest new bridges, closed walk
    exp5 = [1, 2, 3]
    for k, t in enumerate(M[5]['towns']):
        kk, sols = fewest_extra(t.n, t.edges(), all_pairs(t), closed=True)
        say(f'  P5 town {k + 1}: fewest {kk}, {len(sols)} ways, e.g. {[pair_str(t, p) for p in sols[0]]}')
        check(kk == exp5[k], f'2-3 P5 town {k + 1}: {exp5[k]} new bridges')
        if k == 0:
            check([[pair_str(t, p) for p in s] for s in sols] == [['B-C']], '2-3 P5 house: only a second B-C bridge')
        if k == 1:
            check(len(sols) == 3, '2-3 P5 arc town: 3 ways (pair up A, B, C, D)')
        if k == 2:
            check(len(sols) == 15, '2-3 P5 H town: 15 ways')
            check(any(sorted(pair_str(t, p) for p in s) == ['A-D', 'B-E', 'C-F'] for s in sols), '2-3 P5 H town: A-D, B-E, C-F works')
    # P7 pictures
    res = [analyse(p)['strokes'] for p in M[7]['pictures'][::2]]
    say(f'  P7 fewest strokes by picture: {res}')
    check(res == [1, 2, 1, 2, 1, 1], '2-3 P7: house yes, window no, star yes, envelope no, rings yes, square+diamond yes')
    near = min(analyse(p)['near_miss_cm'] for p in M[7]['pictures'][8:10])
    say(f'  P7 rings: closest pair of rings that do not cross are {near:.2f} cm apart (centre lines)')
    # P8: specs
    say('  P8 specs (connected towns; parallel bridges allowed):')
    specs = [(4, 6, lambda n, E: start_set(n, E) == set(range(n))),
             (5, 5, lambda n, E: not start_set(n, E)),
             (6, 8, lambda n, E: start_set(n, E) == {0, 5}),
             (3, 5, lambda n, E: start_set(n, E) == {0, 1})]
    examples = [[(0, 1), (0, 1), (1, 2), (1, 2), (2, 3), (2, 3)],          # A=B=C=D, every bridge doubled
                [(0, 1), (1, 2), (2, 0), (0, 3), (1, 4)],                  # triangle with two tails
                [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 2), (2, 5)],   # ring A..F plus A-C and C-F
                [(0, 1), (0, 2), (0, 2), (1, 2), (1, 2)]]                  # A-B, A=C, B=C
    for k, (n, m, ok_) in enumerate(specs):
        sols = [E for E in multigraphs(n, m) if ok_(n, E)]
        simple = [E for E in sols if len(set(E)) == len(E)]
        maxmult = min(max(E.count(x) for x in E) for E in sols) if sols else None
        say(f'   spec {k + 1}: {len(sols)} labelled towns, {len(simple)} without parallel bridges; '
            f'fewest parallel needed: {maxmult}')
        check(ok_(n, examples[k]) and connected(n, examples[k]) and len(examples[k]) == m, f'2-3 P8 example {k + 1}')
        if k == 0:
            check(len(simple) == 0 and maxmult == 2, '2-3 P8 spec 1 needs a double bridge (K4 is the only simple one, all odd)')
        if k == 3:
            check(maxmult == 2, '2-3 P8 spec 4 can be built with double bridges, no triple needed')
            check(sorted(sorted(E) for E in sols if max(E.count(x) for x in E) == 2) == [sorted(examples[3])],
                  '2-3 P8 spec 4: A-B single with A=C and B=C doubled is the only way without a triple')
    # P9: no town with exactly one start (small exhaustive search)
    found = []
    for n in range(2, 5):
        for m in range(1, 7):
            for E in multigraphs(n, m):
                if len(start_set(n, E)) == 1:
                    found.append(E)
    say(f'  P9: towns with 2-4 islands and 1-6 bridges with exactly one start island: {len(found)}')
    check(not found, '2-3 P9: impossible')
    # P10: second counters
    exp10 = [2, 3]
    for k, t in enumerate(M[10]['towns']):
        kk, sols = fewest_extra(t.n, t.edges(), t.edges(), closed=True)
        say(f'  P10 town {k + 1}: fewest second counters {kk}, ways {[[pair_str(t, p) for p in s] for s in sols]}')
        check(kk == exp10[k], f'2-3 P10 town {k + 1}: {exp10[k]}')
    t = M[10]['towns'][0]
    kk, sols = fewest_extra(t.n, t.edges(), t.edges(), closed=True)
    check(sorted(sorted(pair_str(t, p) for p in s) for s in sols) == [['A-B', 'C-D'], ['A-C', 'B-D'], ['A-D', 'B-C']],
          '2-3 P10 arc town: two bridges with no island in common, 3 ways')

    # ============================================================ grades 4-5
    say()
    say('GRADES 4-5')
    for k, (tm, tu) in enumerate(zip(M[1]['towns'], U[1]['towns'])):
        check(summary(tm)[2] == summary(tu)[2] and sorted(tm.edges()) == sorted(tu.edges()), f'4-5 P1 town {k + 1} same as 2-3')
    for k, (tm, tu) in enumerate(zip(M[2]['towns'], U[2]['towns'])):
        check(summary(tm)[2] == summary(tu)[2], f'4-5 P2 town {k + 1} same as 2-3')
    exp3 = [{}, {c: c for c in 'ABCDE'}, {'F': 'H', 'H': 'F'}]
    for k, t in enumerate(U[3]['towns']):
        d, se, starts, odd = summary(t)
        say(f'  P3 town {k + 1}: degrees {dict((t.name(i), d[i]) for i in range(t.n))}; starts {starts}')
        check(starts == exp3[k], f'4-5 P3 town {k + 1}: {exp3[k] or "none"}')
    # P5 Konigsberg from the map
    mp = U[5]['maps'][0]
    kb = []
    for a_, b_ in mp.bands:
        la, lb = land_at(mp, a_), land_at(mp, b_)
        mid = ((a_[0] + b_[0]) / 2, (a_[1] + b_[1]) / 2)
        check(len(la) == 1 and len(lb) == 1 and la != lb and not land_at(mp, mid), f'4-5 P5 bridge {a_}-{b_} joins two lands over water')
        kb.append((la[0], lb[0]))
    lands = sorted({x for e in kb for x in e})
    idx = {x: i for i, x in enumerate(lands)}
    KE = [(idx[a_], idx[b_]) for a_, b_ in kb]
    d = degrees(4, KE)
    say(f'  P5 bridges {sorted("".join(sorted(e)) for e in kb)}; degrees {dict(zip(lands, d))}')
    check(dict(zip(lands, d)) == {'A': 5, 'B': 3, 'C': 3, 'D': 3}, '4-5 P5: A 5, B 3, C 3, D 3')
    check(not start_end(4, KE), '4-5 P5: no walk')
    pairs = list(itertools.combinations(range(4), 2))
    one = [p for p in pairs if has_walk(4, KE + [p])]
    check(len(one) == 6, '4-5 P5: one new bridge between any two land areas works')
    for p in one:
        se = start_end(4, KE + [p])
        rest = sorted(set(range(4)) - set(p))
        check(set(se) == set(rest), f'4-5 P5: with new bridge {lands[p[0]]}{lands[p[1]]} the walk runs between the other two')
    # a new B-C bridge has room: a straight crossing west of island A runs over water only
    west = [(1.3, 10.3), (1.3, 1.7)]
    pts = [(1.3, 1.7 + k * (8.6 / 200)) for k in range(201)]
    on = [tuple(land_at(mp, q)) for q in pts]
    check(land_at(mp, west[0]) == ['B'] and land_at(mp, west[1]) == ['C'] and
          all(o in ((), ('B',), ('C',)) for o in on) and sum(1 for o in on if o == ()) > 150,
          '4-5 P5: a B-C bridge fits across the river west of A')
    kk, sols = fewest_extra(4, KE, pairs, closed=True)
    say(f'  P5 closed: fewest new bridges {kk}; ways {[["".join(lands[i] for i in p) for p in s] for s in sols]}')
    check(kk == 2, '4-5 P5: 2 new bridges for a closed walk')
    # P7 pictures
    res = [analyse(p)['strokes'] for p in U[7]['pictures'][::2]]
    say(f'  P7 fewest strokes by picture: {res}')
    check(res == [1, 2, 4, 4, 1, 1], '4-5 P7: house 1, window 2, cube 4, grid 4, rings 1, star 1')
    # P8 Lee
    t = U[8]['towns'][0]
    lee = 'A B C D E F G H I A'.split()
    nm = {t.name(i): i for i in range(t.n)}
    E = t.edges()
    outer = []
    for a_, b_ in zip(lee, lee[1:]):
        ids = [i for i, (u, v) in enumerate(E) if {u, v} == {nm[a_], nm[b_]}]
        check(len(ids) == 1, f'4-5 P8: Lee bridge {a_}{b_} exists once')
        outer.append((ids[0], nm[a_], nm[b_]))
    d = degrees(t.n, E)
    say(f'  P8 degrees {dict((t.name(i), d[i]) for i in range(t.n))}; {len(E)} bridges')
    lee_count = {}
    for directed in (True, False):
        @lru_cache(maxsize=None)
        def cnt(x, mask, k):
            if mask == (1 << len(E)) - 1:
                return 1 if (x == nm['A'] and k == 9) else 0
            tot = 0
            for i, (u, v) in enumerate(E):
                if mask >> i & 1 or x not in (u, v):
                    continue
                y = v if x == u else u
                kk = k
                if any(i == o[0] for o in outer):
                    if k == 9 or outer[k][0] != i or (directed and (outer[k][1], outer[k][2]) != (x, y)):
                        continue
                    kk = k + 1
                tot += cnt(y, mask | 1 << i, kk)
            return tot
        lee_count[directed] = cnt(nm['A'], 0, 0)
    say(f'  P8 walks keeping Lee\'s order: {lee_count[True]} (same directions), {lee_count[False]} (any directions)')
    lee_ex = 'A B J I B C J E C D E F J H F G H I A'
    check(is_walk(t, lee_ex, closed=True), '4-5 P8 example walk')
    check(lee_count[True] == 352, '4-5 P8: 352 walks keep Lee\'s bridges in order and direction')
    check(lee_count[False] == 448, '4-5 P8: 448 if Lee\'s bridges may be crossed in either direction')
    inner = [pair_str(t, E[i]) for i in range(len(E)) if i not in [o[0] for o in outer]]
    say(f'  P8 inside bridges: {sorted(inner)}')
    check(sorted(inner) == sorted(['B-I', 'B-J', 'I-J', 'C-E', 'C-J', 'E-J', 'F-H', 'F-J', 'H-J']),
          '4-5 P8: inside bridges are three triangles BIJ, CEJ, FHJ')
    # P10, P11 delivery routes
    exp10 = [(2, 1), (3, 1), (2, 0)]
    for k, t in enumerate(U[10]['towns']):
        c, _ = fewest_extra(t.n, t.edges(), t.edges(), closed=True)
        o, _ = fewest_extra(t.n, t.edges(), t.edges(), closed=False)
        _, cs = fewest_extra(t.n, t.edges(), t.edges(), closed=True)
        _, os_ = fewest_extra(t.n, t.edges(), t.edges(), closed=False)
        say(f'  P10 town {k + 1}: closed {c} {[[pair_str(t, p) for p in s] for s in cs]}, '
            f'open {o} {[[pair_str(t, p) for p in s] for s in os_]}')
        check((c, o) == exp10[k], f'4-5 P10 town {k + 1}: {exp10[k]}')
    # P6: no town with exactly one or three odd islands (small search)
    bad = 0
    for n in range(2, 6):
        for m in range(1, 7 if n < 5 else 6):
            for E in multigraphs(n, m):
                odd = sum(1 for x in degrees(n, E) if x % 2)
                bad += odd in (1, 3)
    check(bad == 0, '4-5 P6: no town (2-5 islands, up to 6 bridges) has 1 or 3 odd islands')

    # ============================================================ where the odd points of the drawings are
    def odd_places(p):
        a = analyse(p)
        x0, y0, x1, y1 = p.bbox()
        def where(q):
            fx = (q[0] - x0) / (x1 - x0); fy = (q[1] - y0) / (y1 - y0)
            col = 'l' if fx < 0.02 else ('r' if fx > 0.98 else ('m' if abs(fx - 0.5) < 0.02 else 'x'))
            row = 'b' if fy < 0.02 else ('t' if fy > 0.98 else ('m' if abs(fy - 0.5) < 0.02 else 'x'))
            return row + col
        return sorted(where(q) for q in a['odd_pts']), sorted(a['deg'].values())
    kp = K[5]['pictures'][::2]
    check(odd_places(kp[0])[0] == ['bl', 'br'], 'K-1 P5 house: start at a bottom corner')
    check(odd_places(kp[2])[0] == ['bl', 'br', 'tl', 'tr'], 'K-1 P5 envelope: the 4 corners are odd')
    check(odd_places(kp[3])[0] == ['ml', 'mr'], 'K-1 P5 circle with a line: start at an end of the line')
    check(odd_places(kp[4])[0] == ['bm', 'ml', 'mr', 'tm'], 'K-1 P5 circle with plus: the 4 rim points are odd')
    mp_ = M[7]['pictures'][::2]
    check(odd_places(mp_[0])[0] == ['bl', 'br'], '2-3 P7 house: start at a bottom corner')
    check(odd_places(mp_[1])[0] == ['bm', 'ml', 'mr', 'tm'], '2-3 P7 window: the middles of the 4 sides are odd')
    check(odd_places(mp_[3])[0] == ['bl', 'br', 'tl', 'tr'], '2-3 P7 envelope: the 4 corners are odd')
    check(odd_places(mp_[4])[1] == [4] * 8, '2-3 P7 rings: 8 crossings with 4 lines each')
    up = U[7]['pictures'][::2]
    check(odd_places(up[2])[1] == [3] * 8 + [4] * 2, '4-5 P7 cube: 8 corners with 3 lines, 2 crossings with 4')
    check(odd_places(up[3])[1].count(3) == 8 and all('x' in w or w[0] in 'tb' and w[1] == 'x' or w[1] in 'lr' and w[0] == 'x'
                                                    for w in odd_places(up[3])[0]), '4-5 P7 grid: the 8 odd points are on the edges, not corners')
    # odd islands named in the guide
    def odd_names(t):
        return sorted(t.name(i) for i in summary(t)[3])
    check(odd_names(M[2]['towns'][0]) == ['A', 'C', 'D', 'F'], '2-3/4-5 P2 town 1: A, C, D, F odd (D has 5)')
    check(summary(M[2]['towns'][0])[0][[t_ for t_ in range(M[2]['towns'][0].n) if M[2]['towns'][0].name(t_) == 'D'][0]] == 5, 'D has 5')
    check(odd_names(M[3]['towns'][3]) == ['B', 'C', 'D', 'E'], '2-3 P3 town 4: B, C, D, E odd')
    check(odd_names(U[3]['towns'][0]) == ['B', 'C', 'F', 'G'], '4-5 P3 town 1: B, C, F, G odd')
    check(sorted(summary(K[2]['towns'][0])[0]) == [2, 2, 2, 2, 3, 3], 'K-1 P2 two squares: the two middle islands have 3 bridges')

    # ============================================================ materials: counters per page, room for counters
    say()
    say('COUNTERS PER PAGE (one counter per printed bridge; extras noted)')
    extra = {('k-1', 6): 1, ('k-1', 8): 1, ('grades-2-3', 4): 1, ('grades-2-3', 5): None, ('grades-2-3', 10): None,
             ('grades-4-5', 10): None}
    busiest = {}
    for stem, probs in P.items():
        per_page = {}
        add_page = {}
        for num, pr in probs.items():
            for t in pr['towns']:
                per_page[t.page] = per_page.get(t.page, 0) + len(t.br)
                # bridges the children add on this page (new bridges or second counters)
                if (stem, num) in extra:
                    k = extra[(stem, num)]
                    if k is None:
                        pool = all_pairs(t) if num == 5 else t.edges()
                        k, _ = fewest_extra(t.n, t.edges(), pool, closed=True)
                    add_page[t.page] = add_page.get(t.page, 0) + k
            for mp in pr['maps']:
                per_page[mp.page] = per_page.get(mp.page, 0) + len(mp.bands)
        tot = {p: per_page[p] + add_page.get(p, 0) for p in per_page}
        say(f'  {stem}: printed bridges by page {dict(sorted(per_page.items()))}')
        say(f'  {stem}: with added bridges/counters {dict(sorted(tot.items()))}')
        bp = max(tot, key=lambda p: (tot[p], -p))
        busiest[stem] = (bp, tot[bp], per_page[bp])
        say(f'  {stem}: busiest page {bp}: {tot[bp]} counters ({per_page[bp]} printed bridges)')
    check(busiest['k-1'] == (1, 20, 20), 'K-1 busiest page: page 1, 20 counters')
    check(busiest['grades-2-3'] == (7, 26, 22), '2-3 busiest page: page 7, 26 counters (22 printed + 4 added)')
    check(busiest['grades-4-5'] == (9, 18, 18), '4-5 busiest page: page 9, 18 counters')

    say()
    say(f'ROOM FOR A COUNTER (band width {BAND_W} cm; counter radius 1.27 cm for 1 inch, 0.95 cm for 3/4 inch)')
    worst = []
    for stem, probs in P.items():
        vis_min, clr_min = 99, 99
        n1 = n34 = nb = 0
        for num, pr in probs.items():
            for k, t in enumerate(pr['towns']):
                for (vis, clr) in counter_room(t):
                    nb += 1
                    vis_min = min(vis_min, vis)
                    clr_min = min(clr_min, clr)
                    n1 += clr < 1.27
                    n34 += clr < 0.9525
                    worst.append((clr, stem, num, t.page))
        say(f'  {stem}: {nb} bridges; shortest visible bridge {vis_min:.2f} cm; smallest clearance {clr_min:.2f} cm; '
            f'bridges where a 1-inch counter would touch another band or island: {n1}; 3/4-inch: {n34}')
        check(n1 == 0, f'{stem}: a 1-inch counter fits on every bridge')
    worst.sort()
    check(any(s_ == 'k-1' and p_ == 9 and c_ < 1.31 for c_, s_, n_, p_ in worst),
          'K-1 page 9 is one of the tightest pages for counters (test there)')
    say('  tightest bridges: ' + '; '.join(f'{s} P{n} p{p} {c:.2f} cm' for c, s, n, p in worst[:6]))

    # ============================================================ fallback game
    say()
    say('FALLBACK GAME (shared token, take turns crossing a bridge and taking its counter; no move = lose)')
    for label, t in [('house (2-3/4-5 P1 town 1)', M[1]['towns'][0]), ('lollipop (2-3/4-5 P1 town 2)', M[1]['towns'][1]),
                     ('arc town (2-3 P3 town 3)', M[3]['towns'][2]), ('big triangle (2-3 P3 town 1)', M[3]['towns'][0])]:
        w = {t.name(s): ('first' if game_first_player_wins(t, s) else 'second') for s in range(t.n)}
        say(f'  {label}: winner by start island {dict(sorted(w.items()))}')
    t = M[1]['towns'][0]
    gw = {t.name(s): game_first_player_wins(t, s) for s in range(t.n)}
    check(gw == {'A': True, 'B': False, 'C': False, 'D': True, 'E': True},
          'game on the house: second player wins from B or C, first player from A, D or E')
    t = M[3]['towns'][0]
    gw = {t.name(s): game_first_player_wins(t, s) for s in range(t.n)}
    check(gw == {'A': False, 'B': True, 'C': True, 'D': False, 'E': True, 'F': False},
          'game on the big triangle: second player wins from a corner, first player from a middle island')

    say()
    bad = [w for c, w in ok if not c]
    say(f'{len(ok)} checks, {len(bad)} mismatches')
    open(os.path.join(HERE, 'check-output.txt'), 'w').write('\n'.join(OUT) + '\n')
    print('\n'.join(OUT))
    assert not bad, bad


def is_walk(t, w, extra=(), closed=False):
    """True if the walk w (island names separated by spaces) crosses every bridge of t, plus the
    extra bridges (pairs of names), exactly once."""
    nm = {t.name(i): i for i in range(t.n)}
    E = [tuple(sorted(e)) for e in t.edges()] + [tuple(sorted((nm[a], nm[b]))) for a, b in extra]
    seq = [nm[x] for x in w.split()]
    used = []
    for a, b in zip(seq, seq[1:]):
        e = tuple(sorted((a, b)))
        if E.count(e) <= used.count(e):
            return False
        used.append(e)
    return len(used) == len(E) and (not closed or seq[0] == seq[-1])


if __name__ == '__main__':
    main()
