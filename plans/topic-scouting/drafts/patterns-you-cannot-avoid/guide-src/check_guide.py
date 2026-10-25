"""Recompute every answer and number printed in the facilitator guide for "Patterns you cannot avoid".

Run: python3 check_guide.py      (exits with an AssertionError if any printed claim fails)
Checked against the final student pages in plans/topic-scouting/drafts/patterns-you-cannot-avoid/
and, for sizes, the materials file materials.pdf beside the student pages.
The whole run, including Sim's game tree and the general-theorem searches, takes about 5 seconds.
"""
import functools
import itertools
from fractions import Fraction
import sys

sys.setrecursionlimit(10000)
R, B = 'R', 'B'


def swap(s):
    return s.translate(str.maketrans('RBG', 'BRG'))


# ======================================================================= strips (van der Waerden)
def threes(n):
    return [(a, a + d, a + 2 * d) for d in range(1, n) for a in range(1, n + 1) if a + 2 * d <= n]


def mono_threes(c):
    return [t for t in threes(len(c)) if c[t[0] - 1] == c[t[1] - 1] == c[t[2] - 1]]


def good(c):
    return not mono_threes(c)


def good_strips(n):
    return [''.join(p) for p in itertools.product('RB', repeat=n) if good(''.join(p))]


counts = {n: len(good_strips(n)) for n in range(3, 11)}
assert counts == {3: 6, 4: 10, 5: 14, 6: 20, 7: 16, 8: 6, 9: 0, 10: 0}, counts
G8 = good_strips(8)
assert sorted(G8) == sorted(['RRBBRRBB', 'RBRBBRBR', 'RBBRRBBR', 'BBRRBBRR', 'BRBRRBRB', 'BRRBBRRB'])
# reversal: RRBBRRBB reversed is its colour swap; the other two are palindromes
assert 'RRBBRRBB'[::-1] == swap('RRBBRRBB')
assert 'RBRBBRBR'[::-1] == 'RBRBBRBR' and 'RBBRRBBR'[::-1] == 'RBBRRBBR'
# with square 1 red, there is exactly one good 8-strip for each start RR, RBR, RBB
starts = {s: [g for g in G8 if g.startswith(s)] for s in ('RR', 'RBR', 'RBB')}
assert starts == {'RR': ['RRBBRRBB'], 'RBR': ['RBRBBRBR'], 'RBB': ['RBBRRBBR']}, starts
# the combs: spacings 1-4 catch every equally spaced three on 9 squares; strips of 5 need only 1 and 2
assert max(b - a for a, b, _ in threes(9)) == 4 and max(b - a for a, b, _ in threes(5)) == 2
assert len(threes(9)) == 16 and len(threes(8)) == 12 and len(threes(5)) == 4
# square 5 of 9 lies in 8 threes (most of any square)
assert max(sum(1 for t in threes(9) if i in t) for i in range(1, 10)) == 8

# K-1 page 1 rule picture: RRBRBR, comb over 2, 4, 6 shows RRR (its only one-colour three)
assert mono_threes('RRBRBR') == [(2, 4, 6)]

# K-1 Problem 1 examples (strips of 4, 6, 7)
for ex in ('RRBB', 'RRBBRR', 'RRBBRRB'):
    assert good(ex), ex
# alternating colours: good on 4 squares, fails on 6 and 7 at 1, 3, 5
assert good('RBRB') and (1, 3, 5) in mono_threes('RBRBRB') and (1, 3, 5) in mono_threes('RBRBRBR')
# comb positions on 9 squares by spacing: 7, 5, 3, 1
assert [sum(1 for t in threes(9) if t[1] - t[0] == d) for d in (1, 2, 3, 4)] == [7, 5, 3, 1]
print('good strips by length:', counts)


def propagate(n, giv):
    """Unit propagation: repeatedly fill a square whose other colour would complete a one-colour three.
    Returns (colouring dict, list of forced steps (square, colour, reason)) or None on contradiction."""
    col = dict(giv)
    steps = []
    changed = True
    while changed:
        changed = False
        for i in range(1, n + 1):
            if i in col:
                continue
            bad = {}
            for c in 'RB':
                for t in threes(n):
                    if i in t and all(col.get(j) == c for j in t if j != i):
                        bad[c] = t
                        break
            if len(bad) == 2:
                return None
            if len(bad) == 1:
                c0 = next(iter(bad))
                c = 'B' if c0 == 'R' else 'R'
                col[i] = c
                steps.append((i, c, bad[c0]))
                changed = True
    return col, steps


# K-1 Problem 2: each strip has exactly one good completion
P2 = [(7, {2: R, 3: R}, 'BRRBBRR'), (8, {1: R, 2: R}, 'RRBBRRBB'),
      (8, {2: B, 4: B}, 'RBRBBRBR'), (8, {5: R, 8: R}, 'RBBRRBBR')]
for n, giv, ans in P2:
    comp = [g for g in good_strips(n) if all(g[p - 1] == c for p, c in giv.items())]
    assert comp == [ans], (n, giv, comp)
    col, steps = propagate(n, giv)
    print(f'K-1 P2 strip {n} {giv}: answer {ans}; forced by the combs alone: '
          f'{"".join(col.get(i, ".") for i in range(1, n + 1))}; steps {steps}')
# what the guide prints: the 7-strip is forced square by square; each 8-strip needs one trial
c, steps = propagate(7, {2: R, 3: R})
assert ''.join(c[i] for i in range(1, 8)) == 'BRRBBRR'
assert [s[:2] for s in steps] == [(1, B), (4, B), (7, R), (5, B), (6, R)]
assert propagate(8, {1: R, 2: R})[0] == {1: R, 2: R, 3: B}
assert propagate(8, {2: B, 4: B})[0] == {2: B, 4: B, 3: R, 6: R}
assert propagate(8, {5: R, 8: R})[0] == {5: R, 8: R, 2: B}
# the single trials that settle them: 4 red fails on RRB....., 1 blue fails on .BRB.R.., 1 blue fails on .B..R..R
assert propagate(8, {1: R, 2: R, 3: B, 4: R}) is None
assert ''.join(propagate(8, {1: R, 2: R, 3: B, 4: B})[0][i] for i in range(1, 9)) == 'RRBBRRBB'
assert propagate(8, {2: B, 4: B, 3: R, 6: R, 1: B}) is None
assert ''.join(propagate(8, {2: B, 4: B, 3: R, 6: R, 1: R})[0][i] for i in range(1, 9)) == 'RBRBBRBR'
assert propagate(8, {5: R, 8: R, 2: B, 1: B}) is None
assert ''.join(propagate(8, {5: R, 8: R, 2: B, 1: R})[0][i] for i in range(1, 9)) == 'RBBRRBBR'

# Grades 2-3 / 4-5 Problem 3: each good 8-strip fails at square 9 in both colours.
kill = {}
for g in G8:
    kill[g] = {c: mono_threes(g + c)[0] for c in 'RB' if mono_threes(g + c)}
    assert len(kill[g]) == 2, g
print('9th square kills:', kill)
# printed table, colour-swap representatives
assert (1, 5, 9) in mono_threes('RRBBRRBB' + 'R') and (7, 8, 9) in mono_threes('RRBBRRBB' + 'B')
assert (3, 6, 9) in mono_threes('RBRBBRBR' + 'R') and (5, 7, 9) in mono_threes('RBRBBRBR' + 'B')
assert (1, 5, 9) in mono_threes('RBBRRBBR' + 'R') and (3, 6, 9) in mono_threes('RBBRRBBR' + 'B')
for g in G8:
    print('   ', g, {c: mono_threes(g + c) for c in 'RB'})


# Hand proof for 9 squares (outline): check every forced step mechanically.
def bad_colours(col, i, n=9):
    """Colours that square i cannot take without completing a one-colour three (with the triple)."""
    out = {}
    for c in 'RB':
        for t in threes(n):
            if i in t and all(col.get(j) == c for j in t if j != i):
                out[c] = t
                break
    return out


# Case 1: 4 and 6 match (red): 5 (4,5,6), 2 (2,4,6) and 8 (4,6,8) cannot be red, but 2, 5, 8 cannot all be blue
col = {4: R, 6: R}
assert bad_colours(col, 5) == {R: (4, 5, 6)} and bad_colours(col, 2) == {R: (2, 4, 6)}
assert bad_colours(col, 8) == {R: (4, 6, 8)}
assert (2, 5, 8) in threes(9)
# Case 2: 4, 5 red and 6 blue: 3 B, 9 R, 7 B, 8 R, 1 B, then square 2 can be neither colour
col = {4: R, 5: R, 6: B}
for sq, c, t in ((3, B, (3, 4, 5)), (9, R, (3, 6, 9)), (7, B, (5, 7, 9)), (8, R, (6, 7, 8)), (1, B, (1, 5, 9))):
    other = R if c == B else B
    assert bad_colours(col, sq) == {other: t}, (sq, bad_colours(col, sq))
    col[sq] = c
assert bad_colours(col, 2) == {B: (1, 2, 3), R: (2, 5, 8)}
# reversing the strip (i -> 10 - i) fixes 5 and swaps 4 with 6, so "5 matches 6" becomes "5 matches 4"
assert {4: 6, 5: 5, 6: 4} == {i: 10 - i for i in (4, 5, 6)}

# Launch strip of 5 (not a task length in any band; printed on Materials page 3). The figure's run
# (review M1: no alternating colours): RRBBB fails only under Comb 1 at 3, 4, 5; changing square 3
# gives RRRBB, which fails only under Comb 1 at 1, 2, 3; the children's good strip RRBRR passes Combs 1
# and 2 everywhere and, with BBRBB, is the only good 5-strip not inside a good 8-strip.
G5 = good_strips(5)
inside8 = {g[i:i + 5] for g in G8 for i in range(4)}
assert sorted(set(G5) - inside8) == ['BBRBB', 'RRBRR']
assert mono_threes('RRBBB') == [(3, 4, 5)]
assert mono_threes('RRRBB') == [(1, 2, 3)]
assert 'RRBBB'[:2] + 'R' + 'RRBBB'[3:] == 'RRRBB'
assert good('RRBRR')
# a strip of 5 whose only one-colour three is 1, 3, 5 must alternate: why the figure avoids Comb 2 failures
assert sorted(c for c in (''.join(p) for p in itertools.product('RB', repeat=5)) if mono_threes(c) == [(1, 3, 5)]) \
    == ['BRBRB', 'RBRBR']
# on 5 squares only Combs 1 and 2 fit (spacing 2 at most)
assert sorted({t[1] - t[0] for t in threes(5)}) == [1, 2]


# K-1 Problem 6 (and 2-3 / 4-5 Problem 2): completeness by start, each start needs at most one try (review S2)
def steps_ok(col, steps, n=8):
    """Each (square, colour, three) step is forced: the other colour completes that three."""
    col = dict(col)
    for sq, c, t in steps:
        other = R if c == B else B
        assert sq not in col
        assert t in threes(n) and sq in t and all(col.get(j) == other for j in t if j != sq), (sq, c, t, col)
        col[sq] = c
    return col


def stuck(col, sq, why_r, why_b, n=8):
    """Square sq can take neither colour: red completes why_r, blue completes why_b."""
    assert all(col.get(j) == R for j in why_r if j != sq) and sq in why_r and why_r in threes(n)
    assert all(col.get(j) == B for j in why_b if j != sq) and sq in why_b and why_b in threes(n)


def finish(col, n=8):
    c, _ = propagate(n, col)
    return ''.join(c.get(i, '.') for i in range(1, n + 1))


# RR: 3 blue (1,2,3). Try 4 red: 6 blue (2,4,6), 7 blue (1,4,7), 5 red (5,6,7); 8 stuck (2,5,8 / 6,7,8).
c = steps_ok({1: R, 2: R}, [(3, B, (1, 2, 3))])
c4 = steps_ok({**c, 4: R}, [(6, B, (2, 4, 6)), (7, B, (1, 4, 7)), (5, R, (5, 6, 7))])
stuck(c4, 8, (2, 5, 8), (6, 7, 8))
assert finish({**c, 4: B}) == 'RRBBRRBB'
# RBR: 5 blue (1,3,5), 8 red (2,5,8). Try 4 red: 6 blue (4,6,8); 7 stuck (1,4,7 / 5,6,7).
c = steps_ok({1: R, 2: B, 3: R}, [(5, B, (1, 3, 5)), (8, R, (2, 5, 8))])
c4 = steps_ok({**c, 4: R}, [(6, B, (4, 6, 8))])
stuck(c4, 7, (1, 4, 7), (5, 6, 7))
assert finish({**c, 4: B}) == 'RBRBBRBR'
# RBB: all forced: 4 red (2,3,4), 7 blue (1,4,7), 5 red (3,5,7), 6 blue (4,5,6), 8 red (6,7,8).
c = steps_ok({1: R, 2: B, 3: B}, [(4, R, (2, 3, 4)), (7, B, (1, 4, 7)), (5, R, (3, 5, 7)), (6, B, (4, 5, 6)),
                                  (8, R, (6, 7, 8))])
assert ''.join(c[i] for i in range(1, 9)) == 'RBBRRBBR' and good('RBBRRBBR')
# the three starts cover every strip whose square 1 is red
assert sorted(g for g in G8 if g[0] == R) == ['RBBRRBBR', 'RBRBBRBR', 'RRBBRRBB']

# 4-5 Problem 3, the mirrored case by hand (review M7): 4 red, 5 and 6 blue:
# 7 red (5,6,7), 1 blue (1,4,7), 3 red (1,3,5), 2 blue (2,3,4), 9 red (1,5,9); 8 stuck (7,8,9 / 2,5,8).
c = steps_ok({4: R, 5: B, 6: B}, [(7, R, (5, 6, 7)), (1, B, (1, 4, 7)), (3, R, (1, 3, 5)), (2, B, (2, 3, 4)),
                                  (9, R, (1, 5, 9))], n=9)
stuck(c, 8, (7, 8, 9), (2, 5, 8), n=9)

# ======================================================================= the strip game (K-1)
def strip_game(n):
    T = [tuple(i - 1 for i in t) for t in threes(n)]

    @functools.lru_cache(None)
    def val(state):
        """(value, length): value +1 win / 0 draw / -1 loss for the player to move;
        length = moves still to be played (including the losing move) with the winner hurrying and
        the loser delaying."""
        empt = [i for i, s in enumerate(state) if s == '.']
        if not empt:
            return (0, 0)
        best = None
        for i in empt:
            for c in 'RB':
                lose = any(i in t and all(state[j] == c for j in t if j != i) for t in T)
                if lose:
                    v = (-1, 1)
                else:
                    w, ln = val(state[:i] + c + state[i + 1:])
                    v = (-w, ln + 1)
                key = (v[0], -v[1] if v[0] == 1 else v[1])
                if best is None or key > best[0]:
                    best = (key, v)
        return best[1]
    return val('.' * n), val


game = {n: strip_game(n)[0] for n in range(3, 10)}
print('strip game (value for first player, length):', game)
assert all(game[n][0] == 0 for n in range(3, 9))     # draws up to 8
assert game[9][0] == -1                               # second player wins on 9
assert game[9][1] == 9                                # the first player can hold out to the ninth move
assert game[8][1] == 8


def random_safe_exact(n):
    """Exact outcome distribution when the mover picks uniformly among safe (square, colour) moves;
    a mover with no safe move loses on that move. Keys: 'full', or the move number of the loss."""
    T = threes(n)

    @functools.lru_cache(None)
    def dist(state):
        k = n - state.count('.')
        if k == n:
            return {'full': Fraction(1)}
        safe = []
        for i in range(n):
            if state[i] != '.':
                continue
            for col in 'RB':
                if not any((i + 1) in t and all(state[j - 1] == col for j in t if j != i + 1) for t in T):
                    safe.append(state[:i] + col + state[i + 1:])
        if not safe:
            return {k + 1: Fraction(1)}
        out = {}
        for st in safe:
            for key, p in dist(st).items():
                out[key] = out.get(key, 0) + p / len(safe)
        return out
    return dist('.' * n)


d9 = random_safe_exact(9)
first_loses = float(sum(p for m, p in d9.items() if m != 'full' and m % 2 == 1))
reach9 = float(d9.get(9, 0))
second_on8 = float(d9.get(8, 0))
print(f'random safe play on 9 (exact): first player loses {first_loses:.4f}; on move 9 {reach9:.4f}; '
      f'second player stuck on move 8 {second_on8:.4f}; distribution { {k: round(float(v), 4) for k, v in d9.items()} }')
assert 'full' not in d9
assert 0.55 < first_loses < 0.57 and first_loses - reach9 < 0.01      # printed: "a little over half", "almost always on the ninth"
assert 0.43 < second_on8 < 0.45                                        # "otherwise the second player is stuck on the eighth"
# no simple mirror strategy: the second player's winning replies to an opening red counter
def winning_replies(n, state):
    _, val = strip_game(n)
    T = [tuple(i - 1 for i in t) for t in threes(n)]
    out = []
    for i, s in enumerate(state):
        if s != '.':
            continue
        for c in 'RB':
            lose = any(i in t and all(state[j] == c for j in t if j != i) for t in T)
            if not lose and val(state[:i] + c + state[i + 1:])[0] == -1:
                out.append((i + 1, c))
    return out
assert winning_replies(9, 'R........') == [(2, R), (4, B), (5, B), (7, B), (8, R), (9, R)]
assert winning_replies(9, '.R.......') == [(1, R), (3, B), (4, B), (6, R), (8, B), (9, R)]
assert winning_replies(9, '....R....') == [(1, B), (4, R), (6, R), (9, B)]
d8 = random_safe_exact(8)
full8 = float(d8['full'])
print(f'random safe play on 8 (exact): fills with nobody losing {full8:.4f}')
assert 0.17 < full8 < 0.20                                  # printed as "about one game in five"


# ======================================================================= sums (Schur)
def ok_last(col, allow_equal):
    """col is a list of colours of 1..n; check sums equal to n."""
    n = len(col)
    for x in range(1, n // 2 + 1):
        y = n - x
        if x == y and not allow_equal:
            continue
        if col[x - 1] == col[y - 1] == col[n - 1]:
            return False
    return True


def colourings(n, k, allow_equal):
    out = []

    def dfs(col):
        if len(col) == n:
            out.append(tuple(col))
            return
        for c in range(k):
            if ok_last(col + [c], allow_equal):
                dfs(col + [c])
    dfs([])
    return out


def longest(k, allow_equal):
    n = 1
    while colourings(n + 1, k, allow_equal):
        n += 1
    return n


def name(p, letters='RBG'):
    return ''.join(letters[x] for x in p)


assert longest(2, True) == 4
assert sorted(name(p) for p in colourings(4, 2, True)) == ['BRRB', 'RBBR']
assert colourings(5, 2, True) == []
# forced chain: 1 R -> 2 B (1+1) -> 4 R (2+2) -> 3 B (1+3) -> 5 neither (1+4, 2+3)
# dead end in order: R B R is good for 1..3 but cannot reach 4
assert ok_last([0, 1, 0], True) and not ok_last([0, 1, 0, 0], True) and not ok_last([0, 1, 0, 1], True)
assert longest(2, False) == 8
assert sorted(name(p) for p in colourings(8, 2, False)) == ['BBRBRRRB', 'RRBRBBBR']
assert colourings(9, 2, False) == []
assert longest(3, True) == 13
C13 = colourings(13, 3, True)
assert len(C13) == 18


def canon(p):
    # rename colours in order of first appearance
    m = {}
    return tuple(m.setdefault(x, len(m)) for x in p)


reps = sorted({canon(p) for p in C13})
assert len(reps) == 3
print('three-colour 1..13 up to renaming:', [name(p) for p in reps])
classes = [sorted({i + 1 for i, x in enumerate(p) if x == c}) for p in reps for c in range(3)]
print('colour classes:', classes)
EX13 = {1: 'R', 4: 'R', 10: 'R', 13: 'R', 2: 'B', 3: 'B', 11: 'B', 12: 'B',
        5: 'G', 6: 'G', 7: 'G', 8: 'G', 9: 'G'}
ex = tuple('RBG'.index(EX13[i]) for i in range(1, 14))
assert ex in C13
assert max(len(c) for c in classes) == 5          # never more than 5 of one colour: 6 counters of each is enough
assert max(len([x for x in p if x == c]) for p in C13 for c in range(3)) == 5
# a 2-3 / 4-5 route to 13: it extends 1..4 = R B B R
assert name(ex[:4]) == 'RBBR' and name(ex[9:]) == 'RBBR' and set(ex[4:9]) == {2}

# in-order play with three colours: greedy (first allowed colour) stops at 7
g = []
while True:
    for c in range(3):
        if ok_last(g + [c], True):
            g.append(c)
            break
    else:
        break
assert len(g) == 7 and name(g) == 'RBRGRBR', name(g)


# all maximal in-order runs with 1 red (never going back)
def maximal_runs(k, allow_equal):
    lens = []

    def dfs(col):
        ext = [c for c in range(k) if ok_last(col + [c], allow_equal)]
        if not ext:
            lens.append(len(col))
        for c in ext:
            dfs(col + [c])
    dfs([0])
    return lens


L3 = maximal_runs(3, True)
dist3 = {m: L3.count(m) for m in sorted(set(L3))}
print('three colours, never going back, 1 red: dead-end lengths', dist3, 'total', len(L3))
assert max(dist3) == 13 and dist3[13] == 6 and len(L3) == 278
assert dist3[9] + dist3[10] == 170
L2 = maximal_runs(2, True)
assert sorted(L2) == [3, 4]                     # R B R stops at 3, R B B R reaches 4
L2b = maximal_runs(2, False)
print('two colours, a number cannot be added to itself, never going back: dead ends', sorted(set(L2b)))


# 4-5 Problem 9 (x != y): a hand route to 8 and why 9 fails
# with 1 R: 2 can be R (1+1 does not count).  The answer RRBRBBBR = red {1, 2, 4, 8}, blue {3, 5, 6, 7}.
def sumfree(S, allow_equal):
    return not any(x + y in S for x in S for y in S if (x < y or (allow_equal and x == y)))


assert sumfree({1, 2, 4, 8}, False) and sumfree({3, 5, 6, 7}, False)
assert not sumfree({1, 2, 4, 8}, True)          # 1 + 1 = 2, so the doubled rule would forbid it
assert sumfree({1, 4, 10, 13}, True) and sumfree({2, 3, 11, 12}, True) and sumfree({5, 6, 7, 8, 9}, True)


# why no colouring of 1..9 works when a number cannot be added to itself: short case check
def forced_chain_x_ne_y(n):
    """All colourings of 1..n with 1 red, as a search tree size."""
    return [p for p in colourings(n, 2, False) if p[0] == 0]


assert [name(p) for p in forced_chain_x_ne_y(8)] == ['RRBRBBBR']


def bad_sum_colours(col, v, n=9, allow_equal=False):
    out = {}
    trip = [(x, y, x + y) for x in range(1, n) for y in range(x, n) if x + y <= n and (allow_equal or x < y)]
    for c in 'RB':
        for t in trip:
            if v in t and all(col.get(u) == c for u in t if u != v):
                out[c] = t
                break
    return out


def run_chain(col, steps, final):
    col = dict(col)
    for v, c, t in steps:
        other = R if c == B else B
        assert bad_sum_colours(col, v).get(other) == t, (v, c, t, bad_sum_colours(col, v))
        col[v] = c
    x, y, z = final
    assert col[x] == col[y] == col[z], (final, col)


# 1..9, a number cannot be added to itself; take 1 red
run_chain({1: R, 3: R}, [(2, B, (1, 2, 3)), (4, B, (1, 3, 4)), (6, R, (2, 4, 6)), (9, B, (3, 6, 9)),
                         (5, R, (4, 5, 9))], (1, 5, 6))
run_chain({1: R, 3: B, 4: R}, [(5, B, (1, 4, 5)), (2, R, (2, 3, 5)), (6, B, (2, 4, 6)), (8, R, (3, 5, 8)),
                               (9, R, (3, 6, 9))], (1, 8, 9))     # 7 is not needed (review M10)
run_chain({1: R, 3: B, 4: B}, [(7, R, (3, 4, 7)), (6, B, (1, 6, 7)), (8, B, (1, 7, 8)), (2, R, (2, 4, 6)),
                               (5, B, (2, 5, 7))], (3, 5, 8))
# 1..5 with doubling allowed: 1 R -> 2 B -> 4 R -> 3 B, then 5 can be neither
col = {1: R}
for v, c, t in ((2, B, (1, 1, 2)), (4, R, (2, 2, 4)), (3, B, (1, 3, 4))):
    other = R if c == B else B
    assert bad_sum_colours(col, v, 5, True).get(other) == t
    col[v] = c
assert bad_sum_colours(col, 5, 5, True) == {R: (1, 4, 5), B: (2, 3, 5)}


# ======================================================================= triangles (Ramsey)
def edges(n):
    return list(itertools.combinations(range(n), 2))


def mono_triangles(n, colouring):
    col = dict(zip(edges(n), colouring))
    return sum(1 for a, b, c in itertools.combinations(range(n), 3) if col[(a, b)] == col[(a, c)] == col[(b, c)])


E5 = edges(5)
good5 = [p for p in itertools.product((0, 1), repeat=10) if mono_triangles(5, p) == 0]
assert len(good5) == 12 and 2 ** 10 == 1024


def degrees(es, n):
    d = [0] * n
    for a, b in es:
        d[a] += 1
        d[b] += 1
    return d


sides5 = {(i, (i + 1) % 5) if i < (i + 1) % 5 else ((i + 1) % 5, i) for i in range(5)}
shape = {}
for p in good5:
    red = [e for e, c in zip(E5, p) if c == 1]
    assert degrees(red, 5) == [2] * 5            # every dot: two red and two blue lines
    k = len(set(red) & sides5)
    shape[k] = shape.get(k, 0) + 1
assert shape == {5: 1, 0: 1, 3: 5, 2: 5}, shape
# 12 = number of loops through five labelled dots = 4!/2 = (choose dot A's 2 neighbours: 6) x 2
assert 12 == 24 // 2 == 6 * 2
# the inset on 2-3 P6 / 4-5 P5: red triangle top, lower-left, lower-right = dots 0, 2, 3 (two diagonals, one side)
assert (0, 2) not in sides5 and (0, 3) not in sides5 and (2, 3) in sides5

E6 = edges(6)
dist6 = {}
for p in itertools.product((0, 1), repeat=15):
    t = mono_triangles(6, p)
    dist6[t] = dist6.get(t, 0) + 1
assert min(dist6) == 2 and dist6[2] == 1760 and sum(dist6.values()) == 32768
print('six dots, colourings by number of one-colour triangles:', sorted(dist6.items()))
# example with exactly 2: red = two separate triangles (alternate dots 0,2,4 and 1,3,5), blue = the rest
red = {(0, 2), (2, 4), (0, 4), (1, 3), (3, 5), (1, 5)}
assert mono_triangles(6, [1 if e in red else 0 for e in E6]) == 2
# another: red = one triangle 0,1,2 and blue elsewhere? count it for the hints
red2 = {(0, 1), (1, 2), (0, 2)}
print('one red triangle on dots 0,1,2, rest blue:', mono_triangles(6, [1 if e in red2 else 0 for e in E6]))


# Goodman's counting: mono >= 20 - (1/2) sum_v r_v (5 - r_v) >= 20 - 18 = 2
def goodman_ok(p):
    red = [e for e, c in zip(E6, p) if c == 1]
    d = degrees(red, 6)
    mixed = sum(r * (5 - r) for r in d)          # two-colour corners
    return mono_triangles(6, p) == 20 - mixed // 2 and mixed % 2 == 0


assert all(goodman_ok(p) for p in itertools.product((0, 1), repeat=15))
assert max(r * (5 - r) for r in range(6)) == 6 and 20 - 6 * 6 // 2 == 2
# exactly two needs every dot to have 2 or 3 red lines
for p in itertools.product((0, 1), repeat=15):
    if mono_triangles(6, p) == 2:
        red = [e for e, c in zip(E6, p) if c == 1]
        assert all(r in (2, 3) for r in degrees(red, 6))
        break

# Sim: full board has 8 red (first player) and 7 blue; none avoids a one-colour triangle
assert all(mono_triangles(6, p) > 0 for p in itertools.product((0, 1), repeat=15) if sum(p) == 8)

# Sim game tree: first player colours red. Whoever completes a triangle of their own colour loses.
TRI = [tuple(E6.index(e) for e in ((a, b), (a, c), (b, c))) for a, b, c in itertools.combinations(range(6), 3)]
TRI_OF = [[[j for j in t if j != i] for t in TRI if i in t] for i in range(15)]


@functools.lru_cache(maxsize=None)
def sim(red, blue):
    """+1 if the player to move wins with perfect play, -1 if they lose (no draws possible)."""
    turn_red = bin(red).count('1') == bin(blue).count('1')
    mine = red if turn_red else blue
    used = red | blue
    any_safe = False
    for i in range(15):
        if used >> i & 1:
            continue
        if any((mine >> a & 1) and (mine >> b & 1) for a, b in TRI_OF[i]):
            continue                                   # this line would complete my own triangle
        any_safe = True
        nr, nb = (red | 1 << i, blue) if turn_red else (red, blue | 1 << i)
        if sim(nr, nb) == -1:
            return 1
    return -1                                          # every move loses (or none is safe)


sim_value = sim(0, 0)
print('Sim: first player', 'wins' if sim_value == 1 else 'loses', 'with perfect play; positions', sim.cache_info().currsize)
assert sim_value == -1

print('all guide checks passed')

# figures in the guide (figs.py): the two five-dot types have no one-colour triangle; the six-dot one has two
pent = {(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)}
bent = {(0, 1), (1, 2), (3, 4), (2, 4), (0, 3)}
for red in (pent, bent):
    assert mono_triangles(5, [1 if e in red else 0 for e in E5]) == 0
assert len(bent & sides5) == 3
print('figure checks passed')

# ======================================================================= additions for the revised guide
# 4-5 Problem 5, which counts to accept (review M8): 12 on labelled dots; up to turning, flipping, swapping.
def orbit_count(cols, group):
    seen, orbits = set(), 0
    for p in cols:
        if p in seen:
            continue
        orbits += 1
        for g in group:
            seen.add(g(p))
    return orbits


def perm_edges(perm):
    def act(p):
        col = dict(zip(E5, p))
        return tuple(col[tuple(sorted((perm[a], perm[b])))] for a, b in E5)
    return act


rots = [tuple((i + k) % 5 for i in range(5)) for k in range(5)]
flips = [tuple((k - i) % 5 for i in range(5)) for k in range(5)]
G_rot = [perm_edges(r) for r in rots]
G_dih = [perm_edges(r) for r in rots + flips]
swap5 = lambda p: tuple(1 - x for x in p)
G_rot_swap = G_rot + [lambda p, g=g: swap5(g(p)) for g in G_rot]
G_all = G_dih + [lambda p, g=g: swap5(g(p)) for g in G_dih]
good5t = [tuple(p) for p in good5]
counts5 = (len(good5t), orbit_count(good5t, G_rot), orbit_count(good5t, G_dih),
           orbit_count(good5t, G_rot_swap), orbit_count(good5t, G_all))
print('five dots: labelled, up to turning, turning and flipping, turning and swapping, all:', counts5)
assert counts5 == (12, 4, 4, 2, 2)

# 4-5 Problem 8, the referee's routine (review M9): at each dot, each pair of same-colour lines whose third
# line has that colour too; every one-colour triangle is found once at each of its three corners.
def corner_count(p):
    col = dict(zip(E6, p))
    e = lambda a, b: col[tuple(sorted((a, b)))]
    return sum(1 for v in range(6) for a, b in itertools.combinations([u for u in range(6) if u != v], 2)
               if e(v, a) == e(v, b) == e(a, b))


rng_cols = list(itertools.islice(itertools.product((0, 1), repeat=15), 0, 32768, 97))
assert all(corner_count(p) == 3 * mono_triangles(6, p) for p in rng_cols)


# Overview, the general theorems (review S1). Searched here: 26 squares in three colours avoid a one-colour
# three and 27 do not (W(3;3) = 27); 34 squares in two colours avoid four equally spaced of one colour and
# 35 do not (W(4;2) = 35). Checked here: a four-colouring of 1..44 with no one-colour x + y = z (x = y
# allowed), and the 17-dot Paley colouring with no four dots joined in one colour. That 1..45 and 18 dots
# cannot be done is quoted from the literature (Baumert 1965; Greenwood and Gleason 1955), not re-searched.
def vdw_first(n, k, L):
    col = [None] * (n + 1)

    def ok(v, c):
        return not any(all(col[v - j * d] == c for j in range(1, L)) for d in range(1, (v - 1) // (L - 1) + 1))

    def dfs(v, used):
        if v > n:
            return True
        for c in range(min(used + 1, k)):
            if ok(v, c):
                col[v] = c
                if dfs(v + 1, max(used, c + 1)):
                    return True
                col[v] = None
        return False
    return dfs(1, 0)


assert vdw_first(26, 3, 3) and not vdw_first(27, 3, 3)
assert vdw_first(34, 2, 4) and not vdw_first(35, 2, 4)
S44 = [[1, 3, 5, 15, 17, 19, 26, 28, 40, 42, 44], [2, 7, 8, 18, 21, 24, 27, 33, 37, 38, 43],
       [4, 6, 13, 20, 22, 23, 25, 30, 32, 39, 41], [9, 10, 11, 12, 14, 16, 29, 31, 34, 35, 36]]
assert sorted(sum(S44, [])) == list(range(1, 45)) and all(sumfree(set(S), True) for S in S44)
QR17 = {(x * x) % 17 for x in range(1, 17)}
assert not any(len({(a - b) % 17 in QR17 for a, b in itertools.combinations(q, 2)}) == 1
               for q in itertools.combinations(range(17), 4))
print('general theorems: W(3;3) = 27 and W(4;2) = 35 searched; 1..44 in four colours and 17 dots checked')

# Materials file (materials.pdf beside the student pages), as the guide cites it:
# Comb d has windows over squares 1, 1 + d, 1 + 2d, so on a strip of n squares it fits n - 2d places.
assert [sum(1 for t in threes(9) if t[1] - t[0] == d) for d in (1, 2, 3, 4)] == [9 - 2 * d for d in (1, 2, 3, 4)]
# Materials sizes quoted in the guide (measured in the materials file by its own check_materials.py):
# 34 mm combs with 27 mm notches over 25 mm squares reach 9 mm above the strip they check, 2 mm short of the
# strip above on K-1 page 1 (strips 11 mm apart); counters of 22 mm fit the 23 mm windows and 26 mm circles.
COMB_H, SQ, K1_GAP, COUNTER = 34, 25, 11, 22
assert COMB_H - SQ == 9 and K1_GAP - (COMB_H - SQ) == 2 and COUNTER < 23 < 26

# K-1 Problem 6: each good 8-strip uses four counters of each colour, so ten of each hold two strips at once
assert all(g.count(R) == 4 and g.count(B) == 4 for g in G8) and 10 // 4 == 2
print('revision checks passed')
