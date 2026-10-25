"""Check every mathematical fact the three packets rely on.

Run: python3 verify.py   (exits with an error if any check fails)
"""
import functools
import itertools


# ---------- equally spaced threes on a strip ----------
def threes(n):
    return [(a, a + d, a + 2 * d) for d in range(1, n) for a in range(1, n + 1) if a + 2 * d <= n]


def good_strip(c):
    return all(not (c[a - 1] == c[b - 1] == c[e - 1]) for a, b, e in threes(len(c)))


def good_strips(n):
    return [''.join(p) for p in itertools.product('RB', repeat=n) if good_strip(''.join(p))]


counts = {n: len(good_strips(n)) for n in range(3, 10)}
assert counts == {3: 6, 4: 10, 5: 14, 6: 20, 7: 16, 8: 6, 9: 0}, counts
assert sorted(good_strips(8)) == sorted(['RRBBRRBB', 'RBRBBRBR', 'RBBRRBBR',
                                         'BBRRBBRR', 'BRBRRBRB', 'BRRBBRRB'])
# the combs (spacings 1 to 4) cover every equally spaced three on strips up to 9
assert max(b - a for a, b, _ in threes(9)) == 4

# K-1 puzzles: (length, givens) -> unique good completion
puzzles = [
    (7, {2: 'R', 3: 'R'}, 'BRRBBRR'),
    (8, {1: 'R', 2: 'R'}, 'RRBBRRBB'),
    (8, {2: 'B', 4: 'B'}, 'RBRBBRBR'),
    (8, {5: 'R', 8: 'R'}, 'RBBRRBBR'),
]
for n, giv, ans in puzzles:
    comp = [g for g in good_strips(n) if all(g[p - 1] == c for p, c in giv.items())]
    assert comp == [ans], (n, giv, comp)


# ---------- the strip game (K-1) ----------
# Players take turns putting a red or a blue counter on an empty square.
# The player who completes a one-colour equally spaced three loses.
def strip_game_value(n):
    T = [tuple(i - 1 for i in t) for t in threes(n)]

    @functools.lru_cache(None)
    def val(state):  # value for the player to move: +1 win, 0 draw, -1 loss
        empt = [i for i, s in enumerate(state) if s == '.']
        if not empt:
            return 0
        best = -2
        for i in empt:
            for c in 'RB':
                lose = any(i in t and all(state[j] == c for j in t if j != i) for t in T)
                v = -1 if lose else -val(state[:i] + c + state[i + 1:])
                best = max(best, v)
        return best
    return val('.' * n)


assert strip_game_value(8) == 0      # perfect play on 8 squares is a draw
assert strip_game_value(9) == -1     # on 9 squares the second player wins
# a full strip of 9 always contains a one-colour three, so no game on 9 is a draw
assert counts[9] == 0


# ---------- sums (Schur) ----------
def sum_free_extend_ok(col, allow_equal):
    n = len(col)
    c = col[-1]
    for x in range(1, n):
        y = n - x
        if y < x:
            break
        if not allow_equal and x == y:
            continue
        if col[x - 1] == col[y - 1] == c:
            return False
    return True


def longest(k, allow_equal):
    best = [0]

    def dfs(col):
        best[0] = max(best[0], len(col))
        for c in range(k):
            nc = col + [c]
            if sum_free_extend_ok(nc, allow_equal):
                dfs(nc)
    dfs([])
    return best[0]


def all_colourings(n, k, allow_equal):
    out = []
    for p in itertools.product(range(k), repeat=n):
        if all(sum_free_extend_ok(list(p[:m]), allow_equal) for m in range(1, n + 1)):
            out.append(p)
    return out


assert longest(2, True) == 4
assert [''.join('RB'[x] for x in p) for p in all_colourings(4, 2, True)] == ['RBBR', 'BRRB']
assert all_colourings(5, 2, True) == []
assert longest(2, False) == 8          # Problem 8 (grades 4-5): 2 + 2 = 4 does not count
assert [''.join('RB'[x] for x in p) for p in all_colourings(8, 2, False)] == ['RRBRBBBR', 'BBRBRRRB']
assert longest(3, True) == 13          # three colours, 2 + 2 = 4 counts


# ---------- triangles (Ramsey) ----------
def mono_triangles(n, colouring):
    E = list(itertools.combinations(range(n), 2))
    col = dict(zip(E, colouring))
    return sum(1 for a, b, c in itertools.combinations(range(n), 3)
               if col[(a, b)] == col[(a, c)] == col[(b, c)])


def stats(n):
    m = n * (n - 1) // 2
    dist = {}
    for p in itertools.product((0, 1), repeat=m):
        t = mono_triangles(n, p)
        dist[t] = dist.get(t, 0) + 1
    return dist


d5 = stats(5)
assert d5[0] == 12 and sum(d5.values()) == 1024
d6 = stats(6)
assert 0 not in d6 and 1 not in d6 and d6[2] > 0   # every 6-dot colouring has at least 2

# an example with exactly two (for adults): red = two disjoint triangles' complement
E6 = list(itertools.combinations(range(6), 2))
red = {(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5)}
ex = [1 if e in red else 0 for e in E6]
assert mono_triangles(6, ex) == 2

# ---------- pictures and wording on the revised pages ----------
# K-1 rule picture: the full strip RRBRBR under a comb at 2, 4, 6 shows three reds, and that is its only
# one-colour three, so the picture shows exactly one reason the strip is not good.
pic = 'RRBRBR'
mono = [t for t in threes(6) if pic[t[0] - 1] == pic[t[1] - 1] == pic[t[2] - 1]]
assert mono == [(2, 4, 6)], mono

# Five dots (grades 4-5 "find every way"): all 12 good colourings make each colour a loop through all
# five dots.
E5 = list(itertools.combinations(range(5), 2))


def is_five_cycle(edges):
    deg = {v: 0 for v in range(5)}
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    if any(d != 2 for d in deg.values()):
        return False
    # connected?
    seen, stack = {0}, [0]
    while stack:
        v = stack.pop()
        for a, b in edges:
            for x, y in ((a, b), (b, a)):
                if x == v and y not in seen:
                    seen.add(y)
                    stack.append(y)
    return len(seen) == 5


good5 = [p for p in itertools.product((0, 1), repeat=10) if mono_triangles(5, p) == 0]
assert len(good5) == 12
for p in good5:
    red = [e for e, c in zip(E5, p) if c == 1]
    blue = [e for e, c in zip(E5, p) if c == 0]
    assert is_five_cycle(red) and is_five_cycle(blue)

# Sim: a full board has 8 lines of the first player's colour and 7 of the second's; none of those
# colourings avoids a one-colour triangle, so Sim never ends in a draw.
assert all(mono_triangles(6, p) > 0 for p in itertools.product((0, 1), repeat=15) if sum(p) == 8)
print('picture and five-dot checks passed')

print('all checks passed')
print('good strips by length:', counts)
print('strip game on 8:', strip_game_value(8), ' on 9:', strip_game_value(9))
print('six dots, number of colourings by count of one-colour triangles:', sorted(d6.items())[:3])
