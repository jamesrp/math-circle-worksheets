"""Checks for the K-1 pages. Run: python3 check_k1.py"""
import sys
from functools import lru_cache
from collections import Counter
import tri
import lozenge as L
import instances as I

B = I.boards()
ok = True


def claim(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg)
    ok = ok and cond


def blue_tilings(R):
    return tri.count_tilings(R, ['B'])


print('=== K-1 Problem 1: cover with blue blocks only ===')
expect = {'K1-P1a': True, 'K1-P1b': False, 'K1-P1c': True, 'K1-P1d': False}
for k, want in expect.items():
    R = B[k]
    m, _ = tri.max_matching(R)
    n = blue_tilings(R)
    claim((n > 0) == want, '%s: %d small triangles (%d up, %d down); most blues that fit = %d; blue-only coverings = %d -> %s'
          % (k, len(R), *tri.counts(R), m, n, 'POSSIBLE' if n else 'IMPOSSIBLE'))

print('\n=== K-1 Problem 2: blues plus as few greens as possible (big triangles) ===')
for k, n in [('K1-P2a', 2), ('K1-P2b', 3), ('K1-P2c', 4)]:
    R = B[k]
    m, match = tri.max_matching(R)
    g = len(R) - 2 * m
    up, dn = tri.counts(R)
    claim(g == n and g == up - dn, '%s (triangle side %d): fewest greens = %d (= up %d - down %d); blues used = %d' % (k, n, g, up, dn, m))

print('\n=== K-1 Problem 3: all the ways to cover the long hexagons with blues ===')
for k, abc, n in [('K1-P3a', (1, 1, 1), 2), ('K1-P3b', (2, 1, 1), 3), ('K1-P3c', (3, 1, 1), 4)]:
    R, ts = L.tilings(*abc)
    assert R == B[k]
    standing_positions = []
    all_one = True
    for t in ts:
        kinds = Counter(L.kind(r) for r in t)
        if kinds['S'] != 1:
            all_one = False
        s = [r for r in t if L.kind(r) == 'S'][0]
        cx = sum(x for x, y in L.rhombus_cart(s)) / 4
        standing_positions.append(round(cx, 2))
    claim(len(ts) == n and all_one and len(set(standing_positions)) == n,
          '%s hexagon %s: %d ways; every way has exactly one standing blue; its centre x-positions (inches from the bottom-left corner of the bottom edge) are %s'
          % (k, abc, len(ts), sorted(standing_positions)))



def all_min(R, pieces, k):
    """every covering of R that uses exactly k blocks (k = the fewest possible)"""
    R = frozenset(R)
    cells = sorted(R, key=tri.order_key)
    by = {c: [] for c in cells}
    for p in pieces:
        for pl in tri.placements(R, p):
            for c in pl:
                by[c].append((p, pl))
    sols = []

    def rec(cov, ch):
        first = next((c for c in cells if c not in cov), None)
        if first is None:
            sols.append(list(ch))
            return
        if len(ch) == k:
            return
        for p, pl in by[first]:
            if pl.isdisjoint(cov):
                ch.append((p, pl))
                rec(cov | pl, ch)
                ch.pop()
    rec(frozenset(), [])
    return sols

print('\n=== K-1 Problem 4: fewest blocks (yellow, red, blue, green) ===')


def min_pieces_forced(R, pieces, forced):
    """fewest pieces when the placement 'forced' must be used."""
    k, ex = tri.min_pieces(R - forced, pieces)
    return k + 1, ex


for k, want in [('K1-P4a', 3), ('K1-P4b', 6), ('K1-P4c', 5)]:
    R = B[k]
    m4, ex4 = tri.min_pieces(R, ['Y', 'R', 'B', 'G'])
    m5, ex5 = tri.min_pieces(R, ['Y', 'P', 'R', 'B', 'G'])
    claim(m4 == want and m5 == want, '%s: fewest blocks = %d (example: %s); allowing purple chevrons too still gives %d'
          % (k, m4, dict(Counter(p for p, _ in ex4)), m5))
    sols = all_min(R, ['Y', 'R', 'B', 'G'], want)
    kinds = Counter(tuple(sorted(Counter(p for p, _ in s_).items())) for s_ in sols)
    print('INFO %s: there are only %d fewest-block coverings, by kind of block: %s' % (k, len(sols), dict(kinds)))
# number of fewest-block solutions and the "obvious first move" traps
R = B['K1-P4a']
centre_yellow = frozenset(tri.around_point((1, 1)))
assert centre_yellow <= R
k, ex = min_pieces_forced(R, ['Y', 'R', 'B', 'G'], centre_yellow)
claim(k == 4, 'K1-P4a: if the yellow goes in the middle (the only place it fits), the best possible is %d blocks (yellow + 3 greens); three reds give 3' % k)
claim(len([pl for pl in tri.placements(R, 'Y')]) == 1, 'K1-P4a: a yellow fits in exactly one place on the size-3 triangle')
R = B['K1-P4b']
centre_yellow = frozenset(tri.around_point((0, 2)))
assert centre_yellow <= R
k, ex = min_pieces_forced(R, ['Y', 'R', 'B', 'G'], centre_yellow)
claim(k == 7, 'K1-P4b: with a yellow in the very middle of the big hexagon the best possible is %d blocks (e.g. %s + yellow); the true fewest is 6'
      % (k, dict(Counter(p for p, _ in ex))))
# how many yellows fit at most in the big hexagon?
def max_disjoint(R, piece):
    pls = tri.placements(R, piece)
    best = 0
    def rec(i, used, cnt):
        nonlocal best
        best = max(best, cnt)
        for j in range(i, len(pls)):
            if pls[j].isdisjoint(used):
                rec(j + 1, used | pls[j], cnt + 1)
    rec(0, frozenset(), 0)
    return best
claim(max_disjoint(B['K1-P4b'], 'Y') == 3, 'K1-P4b: at most 3 yellows fit in the big hexagon (so 4 blocks is impossible; 5 blocks would have to be 3 yellows + 2 reds, which the search rules out)')
R = B['K1-P4c']
k_noY, ex = tri.min_pieces(R, ['R', 'B', 'G'])
claim(k_noY == 6, 'K1-P4c: without a yellow (or purple) the fewest is %d (e.g. 5 reds + 1 green); with one yellow it is 5' % k_noY)
claim(max_disjoint(R, 'Y') == 1, 'K1-P4c: only one yellow fits at a time in the size-4 triangle')

print('\n=== K-1 Problem 5: big shapes from small blocks of the same colour ===')
for k, piece, want, name in [('K1-P5a', 'G', True, 'big green from greens'), ('K1-P5b', 'R', True, 'big red from reds'),
                             ('K1-P5c', 'Y', False, 'big yellow from yellows'), ('K1-P5d', 'P', False, 'big purple from purples')]:
    R = B[k]
    n = tri.count_tilings(R, [piece])
    md = max_disjoint(R, piece)
    claim((n > 0) == want, '%s (%s): %d small triangles = %d blocks by area; coverings = %d; most that fit without overlap = %d'
          % (k, name, len(R), len(R) // tri.AREA[piece], n, md))

print('\n=== K-1 Problem 6: blue-block game, last block wins ===')


def game(R):
    R = frozenset(R)
    pls = tri.placements(R, 'B')

    @lru_cache(maxsize=None)
    def win(covered):
        for pl in pls:
            if pl.isdisjoint(covered):
                if not win(covered | pl):
                    return True
        return False

    first_wins = win(frozenset())
    winning = [pl for pl in pls if not win(pl)]
    return first_wins, winning, pls, win


def strip_index(t):
    i, j, o = t
    return 2 * i + o + 1  # 1-based position along the strip


for k, want_first in [('K1-P6a', False), ('K1-P6b', True), ('K1-P6c', True)]:
    R = B[k]
    fw, winning, pls, win = game(R)
    if k == 'K1-P6a':
        desc = 'all %d first moves lose' % len(pls) if not winning else str(winning)
    else:
        desc = 'winning first moves cover triangles ' + ', '.join(
            '%s' % sorted(strip_index(t) for t in pl) for pl in winning)
    claim(fw == want_first, '%s (%d triangles): %s player wins with best play; %s' % (k, len(R), 'FIRST' if fw else 'SECOND', desc))

# hexagon: second player's reply must be the middle pair of the remaining four
R = frozenset(B['K1-P6a'])
fw, winning, pls, win = game(R)
good = True
for p1 in pls:
    rest = R - p1
    replies = [p2 for p2 in pls if p2 <= rest]
    win_replies = [p2 for p2 in replies if not win(p1 | p2)]
    # remaining 4 triangles form a path; the winning reply is the middle two, which leaves two triangles that do not touch
    left = rest - win_replies[0]
    a, b = list(left)
    good &= (len(win_replies) == 1 and b not in tri.neighbors(a))
claim(good, 'K1-P6a: after any first move, the second player has exactly one winning reply: cover the middle two of the four triangles left, leaving two triangles that do not touch')

# strip of 10: after the middle move, copying wins
R = frozenset(B['K1-P6c'])
fw, winning, pls, win = game(R)
mid = [pl for pl in pls if sorted(strip_index(t) for t in pl) == [5, 6]][0]
claim(not win(mid), 'K1-P6c: covering triangles 5 and 6 (the middle) leaves 4 + 4, a second-player win: the first player then copies on the other side')
# general table for strips
tab = []
for n in range(2, 13):
    fw, winning, pls, win = game(I.strip(n))
    tab.append('%d:%s' % (n, 'first' if fw else 'second'))
print('INFO strip of n triangles, who wins with best play: ' + ', '.join(tab))

print('\nALL K-1 CHECKS PASSED' if ok else '\nSOME K-1 CHECKS FAILED')
sys.exit(0 if ok else 1)
