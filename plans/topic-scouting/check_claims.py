#!/usr/bin/env python3
"""Checks every computed claim in the topic-scouting outlines (October 24, 2026).

Standard library only. Run: python3 plans/topic-scouting/check_claims.py
Each section prints the numbers the outlines quote and asserts them.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, ceil, log2


def section(title):
    print(f"\n== {title}")


# ---------------------------------------------------------------- towers from either end
section("Towers from either end")


@lru_cache(None)
def margin(t):
    """Most the player to move can win by (their cubes minus the other's)."""
    if not t:
        return 0
    return max(t[0] - margin(t[1:]), t[-1] - margin(t[:-1]))


even_losses = sum(1 for n in (2, 4, 6) for t in product(range(1, 5), repeat=n) if margin(t) < 0)
assert even_losses == 0
print("even rows (heights 1-4, 2, 4 or 6 towers) the first player loses:", even_losses)
assert margin((2, 1, 2, 3)) == 2 and sum((2, 2)) == sum((1, 3))
print("2,1,2,3: colour totals 4 and 4 (colour plan only ties); best play wins by", margin((2, 1, 2, 3)))
assert margin((1, 5, 1)) == -3
print("1,5,1: the first player loses by", -margin((1, 5, 1)))
five = Counter((margin(t) > 0) - (margin(t) < 0) for t in product(range(1, 5), repeat=5))
assert (five[-1], five[0]) == (143, 147)
print("five towers of heights 1-4: first player loses", five[-1], "ties", five[0], "of 1024")

# ---------------------------------------------------------------- games decided before they start
section("Games decided before they start")
for m, n in ((2, 3), (3, 3), (2, 4)):
    print(f"{m}x{n} bar: {m * n - 1} breaks, last break by the", "first" if (m * n - 1) % 2 else "second", "player")
print("Brussels Sprouts 5n-2 for n = 1..4:", [5 * n - 2 for n in range(1, 5)])
print("Sprouts bounds [2n, 3n-1] for n = 1..4:", [(2 * n, 3 * n - 1) for n in range(1, 5)])

# ---------------------------------------------------------------- chomp
section("Poisoned cookie (Chomp)")


def chomp_moves(p):
    """p = row lengths from the poison row up. Yields (row, col, result), 0-based from the poison corner."""
    for r in range(len(p)):
        for c in range(p[r]):
            if r == 0 and c == 0:
                continue
            q = tuple(x for x in list(p[:r]) + [min(x, c) for x in p[r:]] if x > 0)
            yield r, c, q


@lru_cache(None)
def chomp_win(p):
    if p == (1,):
        return False  # only the poison is left: the mover must eat it
    return any(not chomp_win(q) for _, _, q in chomp_moves(p))


for rows in range(1, 5):
    for cols in range(1, 7):
        if rows * cols > 1:
            assert chomp_win(tuple([cols] * rows))
print("first player wins every rectangle up to 4x6 except 1x1: True")
assert all(not chomp_win(tuple(x for x in (a, a - 1) if x)) for a in range(1, 9))
print("two rows: (a, a-1) loses for the mover, a = 1..8: True")
assert all(not chomp_win(tuple([n] + [1] * (n - 1))) for n in range(1, 8))
print("equal-armed L shapes lose for the mover: True")
for rows, cols, expect in ((3, 4, [(1, 2)]), (3, 5, [(2, 3)]), (4, 5, [(2, 2)])):
    wins = [(r, c) for r, c, q in chomp_moves(tuple([cols] * rows)) if not chomp_win(q)]
    assert wins == expect
    print(f"{rows} rows x {cols} columns: only winning bite at row {wins[0][0] + 1}, column {wins[0][1] + 1} (counting from the poison)")

# ---------------------------------------------------------------- who beat whom
section("Who beat whom (tournaments)")


def ham_paths(n, beat):
    """Number of line-ups in which each player beat the next (DP over subsets)."""
    dp = [[0] * n for _ in range(1 << n)]
    for v in range(n):
        dp[1 << v][v] = 1
    for mask in range(1 << n):
        for v in range(n):
            if dp[mask][v]:
                for w in range(n):
                    if not mask >> w & 1 and beat[v][w]:
                        dp[mask | 1 << w][w] += dp[mask][v]
    return sum(dp[(1 << n) - 1])


for n in range(2, 7):
    pairs = list(combinations(range(n), 2))
    king_numbers, scores = set(), set()
    for bits in product((0, 1), repeat=len(pairs)):
        beat = [[False] * n for _ in range(n)]
        for (i, j), b in zip(pairs, bits):
            beat[i][j], beat[j][i] = bool(b), not b
        assert ham_paths(n, beat) % 2 == 1
        s = [sum(row) for row in beat]
        king = [all(u == v or beat[v][u] or any(beat[v][w] and beat[w][u] for w in range(n)) for u in range(n)) for v in range(n)]
        assert all(king[v] for v in range(n) if s[v] == max(s))
        king_numbers.add(sum(king))
        scores.add(tuple(sorted(s)))
    landau = {s for s in product(range(n), repeat=n) if list(s) == sorted(s) and sum(s) == comb(n, 2)
              and all(sum(s[:k]) >= comb(k, 2) for k in range(1, n + 1))}
    assert scores == landau
    print(f"{n} players: every tournament has an odd number of line-ups; top scorers are kings; "
          f"numbers of kings {sorted(king_numbers)}; {len(scores)} sorted win lists = Landau's count")

# ---------------------------------------------------------------- hidden armies
section("Hidden armies (Blotto, three hills)")


def splits(n):
    return [(a, b, n - a - b) for a in range(n + 1) for b in range(n + 1 - a)]


def beats(x, y):
    return sum(p > q for p, q in zip(x, y)) > sum(p < q for p, q in zip(x, y))


for n in range(1, 13):
    unbeaten = [s for s in splits(n) if not any(beats(t, s) for t in splits(n))]
    assert (n >= 4) == (not unbeaten)
    if n <= 4:
        print(f"{n} soldiers: never-beaten splits {unbeaten}")
print("4 to 12 soldiers: every split is beaten by another")
S6 = splits(6)
assert len(S6) == 28 and beats((0, 1, 5), (2, 0, 4)) and beats((2, 0, 4), (1, 2, 3)) and beats((1, 2, 3), (0, 1, 5))
print("6 soldiers: 28 splits; cycle (0,1,5) > (2,0,4) > (1,2,3) > (0,1,5)")
for s, lost, won in (((2, 2, 2), 3, 12), ((6, 0, 0), 15, 0)):
    assert (sum(beats(t, s) for t in S6), sum(beats(s, t) for t in S6)) == (lost, won)
    print(f"{s}: beaten by {lost}, beats {won}")

# ---------------------------------------------------------------- patterns you cannot avoid
section("Patterns you cannot avoid")


def has_ap(col):
    n = len(col)
    return any(col[a] == col[a + d] == col[a + 2 * d] for a in range(n) for d in range(1, n) if a + 2 * d < n)


counts = [sum(1 for c in product("RB", repeat=n) if not has_ap(c)) for n in range(3, 10)]
assert counts == [6, 10, 14, 20, 16, 6, 0]
print("strips of 3..9 squares with no equally spaced one-colour three:", counts)
print("the six of length 8:", ["".join(c) for c in product("RB", repeat=8) if not has_ap(c)])


def sum_free(col):
    n = len(col)
    return not any(col[x - 1] == col[y - 1] == col[x + y - 1] for x in range(1, n + 1) for y in range(x, n + 1) if x + y <= n)


schur = {n: ["".join(c) for c in product("RB", repeat=n) if sum_free(c)] for n in (4, 5)}
assert schur[4] == ["RBBR", "BRRB"] and schur[5] == []
print("numbers 1-4 with no same-colour x+y=z (x=y allowed):", schur[4], "; 1-5: none")
for n, free, least in ((5, 12, 0), (6, 0, 2)):
    E = list(combinations(range(n), 2))
    tri = []
    for col in product((0, 1), repeat=len(E)):
        c = dict(zip(E, col))
        tri.append(sum(c[(a, b)] == c[(a, d)] == c[(b, d)] for a, b, d in combinations(range(n), 3)))
    assert (tri.count(0), min(tri)) == (free, least)
    print(f"{n} dots: {free} of {len(tri)} colourings avoid a one-colour triangle; fewest one-colour triangles {least}")

# ---------------------------------------------------------------- pancake flips
section("Pancake flips")


def bfs(start, step):
    dist, dq = {start: 0}, deque([start])
    while dq:
        x = dq.popleft()
        for y in step(x):
            if y not in dist:
                dist[y] = dist[x] + 1
                dq.append(y)
    return dist


def flips(s):
    return [tuple(reversed(s[:k])) + s[k:] for k in range(2, len(s) + 1)]


def burnt_flips(s):
    return [tuple(-x for x in reversed(s[:k])) + s[k:] for k in range(1, len(s) + 1)]


worst = []
for n in range(1, 8):
    d = bfs(tuple(range(1, n + 1)), flips)  # stacks listed top first; flips are their own inverses
    worst.append(max(d.values()))
    breaks = lambda s: sum(abs(s[i] - s[i + 1]) != 1 for i in range(n - 1)) + (s[-1] != n)
    assert all(d[s] >= breaks(s) for s in d) and all(d[s] <= max(2 * n - 3, 0) for s in d if n >= 2)
    if n == 3:
        assert [s for s in d if d[s] == 3] == [(1, 3, 2)]
    if n == 4:
        assert sorted(s for s in d if d[s] == 4) == [(2, 4, 1, 3), (3, 1, 4, 2), (4, 2, 3, 1)]
    if n == 6:
        assert sum(v == 7 for v in d.values()) == 2
assert worst == [0, 1, 3, 4, 5, 7, 8]
print("worst stacks need", worst, "flips for 1..7 pancakes; breaks lower bound and 2n-3 upper bound hold")
bw = [max(bfs(tuple(range(1, n + 1)), burnt_flips).values()) for n in range(1, 6)]
assert bw == [1, 4, 6, 8, 10]
print("burnt pancakes, worst cases for 1..5:", bw)

# ---------------------------------------------------------------- train-yard sorting
section("Train-yard sorting")


def siding_sorts(order):
    siding, need = [], 1
    for car in order:
        siding.append(car)
        while siding and siding[-1] == need:
            siding.pop()
            need += 1
    return not siding


def has_231(p):
    return any(p[k] < p[i] < p[j] for i, j, k in combinations(range(len(p)), 3))


for n in range(1, 9):
    P = list(permutations(range(1, n + 1)))
    assert all(siding_sorts(p) == (not has_231(p)) for p in P)
    good = sum(map(siding_sorts, P))
    assert good == comb(2 * n, n) // (n + 1)
print("sortable arrival orders = Catalan numbers 1, 2, 5, 14, 42, 132, 429, 1430; exactly the orders with no 2-3-1")
assert [p for p in permutations((1, 2, 3)) if not siding_sorts(p)] == [(2, 3, 1)]


def two_sidings(order):
    n = len(order)
    start = (tuple(order), (), (), 1)
    seen, dq = {start}, deque([start])
    while dq:
        inp, a, b, need = dq.popleft()
        if need == n + 1:
            return True
        nxt = []
        if inp:
            nxt.append((inp[1:], a + (inp[0],), b, need))
        if a:
            nxt.append((inp, a[:-1], b + (a[-1],), need))
        if b and b[-1] == need:
            nxt.append((inp, a, b[:-1], need + 1))
        for s in nxt:
            if s not in seen:
                seen.add(s)
                dq.append(s)
    return False


assert all(two_sidings(p) for p in permutations(range(1, 7)))
bad7 = sum(not two_sidings(p) for p in permutations(range(1, 8)))
assert bad7 == 22
print("two sidings in a row: all 720 six-car orders sort; 22 of 5040 seven-car orders do not")

# ---------------------------------------------------------------- counting-out circles
section("Counting-out circles")


def survivor(n, k=2):
    people, i = list(range(1, n + 1)), 0
    while len(people) > 1:
        i = (i + k - 1) % len(people)
        people.pop(i)
    return people[0]


for n in range(1, 257):
    m = 1 << (n.bit_length() - 1)
    assert survivor(n) == 2 * (n - m) + 1
print("every second person: survivors for 1..16:", [survivor(n) for n in range(1, 17)], "; J(2^m+L) = 2L+1 checked to 256")
third = [survivor(n, 3) for n in range(1, 17)]
assert third == [1, 2, 2, 1, 4, 1, 4, 7, 1, 4, 7, 10, 13, 2, 5, 8]
print("every third person:", third)

# ---------------------------------------------------------------- untangling networks
section("Untangling networks")
for name, v, e, bound in (("K5", 5, 10, 3 * 5 - 6), ("K3,3", 6, 9, 2 * 6 - 4)):
    assert e > bound
    print(f"{name}: {e} links but a crossing-free drawing allows at most {bound}")

# ---------------------------------------------------------------- hex
section("Hex")


def hex_nbrs(n):
    return {(r, c): [(r + dr, c + dc) for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1))
                     if 0 <= r + dr < n and 0 <= c + dc < n] for r in range(n) for c in range(n)}


def connected(board, n, nb, player):
    start = [(0, c) for c in range(n)] if player == 1 else [(r, 0) for r in range(n)]
    goal = (lambda x: x[0] == n - 1) if player == 1 else (lambda x: x[1] == n - 1)
    seen = {s for s in start if board[s] == player}
    dq = deque(seen)
    while dq:
        x = dq.popleft()
        if goal(x):
            return True
        for y in nb[x]:
            if y not in seen and board[y] == player:
                seen.add(y)
                dq.append(y)
    return False


for n in (3, 4):
    nb = hex_nbrs(n)
    cells = list(nb)
    tally = Counter()
    for col in product((1, 2), repeat=n * n):
        b = dict(zip(cells, col))
        tally[(connected(b, n, nb, 1), connected(b, n, nb, 2))] += 1
    assert set(tally) == {(True, False), (False, True)}
    print(f"{n}x{n}: all {2 ** (n * n)} full boards have exactly one winner ({dict(tally)})")
nb3 = hex_nbrs(3)
cells3 = list(nb3)


@lru_cache(None)
def hex_mover_wins(state, mover):
    for i, v in enumerate(state):
        if v == 0:
            s = state[:i] + (mover,) + state[i + 1:]
            if connected(dict(zip(cells3, s)), 3, nb3, mover) or not hex_mover_wins(s, 3 - mover):
                return True
    return False


openings = [cells3[i] for i in range(9) if not hex_mover_wins(tuple(1 if j == i else 0 for j in range(9)), 2)]
assert len(openings) == 5 and (1, 1) in openings and (0, 0) not in openings and (2, 2) not in openings
print("3x3: winning first moves", openings, "(centre wins; the two acute corners lose)")

# ---------------------------------------------------------------- graceful labels
section("Graceful labels")


def graceful(n, edges):
    m = len(edges)
    adj = {v: [] for v in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    order = sorted(range(n), key=lambda v: -len(adj[v]))
    lab, used, diffs = [-1] * n, set(), set()

    def bt(k):
        if k == n:
            return True
        v = order[k]
        for x in range(m + 1):
            if x in used:
                continue
            nd = [abs(x - lab[u]) for u in adj[v] if lab[u] >= 0]
            if 0 in nd or len(set(nd)) < len(nd) or any(d in diffs for d in nd):
                continue
            lab[v] = x
            used.add(x)
            diffs.update(nd)
            if bt(k + 1):
                return True
            lab[v] = -1
            used.discard(x)
            diffs.difference_update(nd)
        return False

    return bt(0)


for n in range(3, 11):
    ok = graceful(n, [(i, (i + 1) % n) for i in range(n)])
    assert ok == (n % 4 in (0, 3))
print("cycles with 3..10 links graceful exactly when the count leaves 0 or 3 on division by 4: True")
assert graceful(4, list(combinations(range(4), 2))) and not graceful(5, list(combinations(range(5), 2)))
print("K4 graceful (0, 1, 4, 6); K5 not")


def canon(n, edges):
    adj = {v: [] for v in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    def enc(v, parent):
        return "(" + "".join(sorted(enc(u, v) for u in adj[v] if u != parent)) + ")"

    return min(enc(r, -1) for r in range(n))


def prufer_edges(code, n):
    deg = [1] * n
    for x in code:
        deg[x] += 1
    edges = []
    for x in code:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, x))
        deg[leaf] -= 1
        deg[x] -= 1
    u, v = [i for i in range(n) if deg[i] == 1]
    return edges + [(u, v)]


for n in range(2, 9):
    shapes = {}
    for code in product(range(n), repeat=n - 2):
        e = prufer_edges(code, n)
        shapes.setdefault(canon(n, e), e)
    assert all(graceful(n, e) for e in shapes.values())
    print(f"all {len(shapes)} tree shapes on {n} dots are graceful")

# ---------------------------------------------------------------- close-behind candidates (README lines)
section("Close-behind candidates quoted in the README")
print("champion n-1, champion and runner-up n+ceil(log2 n)-2 for n = 8:", 8 - 1, 8 + ceil(log2(8)) - 2)


def unsow(b):
    b = list(b)
    k = next((i for i, x in enumerate(b) if x == 0), len(b))
    if k == len(b):
        b.append(0)
    for i in range(k):
        b[i] -= 1
    b[k] = k + 1
    return b


boards = [[]]
for _ in range(10):
    boards.append(unsow(boards[-1]))
assert boards[10] == [0, 1, 1, 3, 5]
print("Tchoukaillon winning boards for 1..6 beans:", boards[1:7])


def tilted_squares(n):
    pts = set(product(range(n), repeat=2))
    return sum(1 for (x, y) in pts for dx in range(n) for dy in range(1, n)
               if {(x + dx, y + dy), (x + dx - dy, y + dy + dx), (x - dy, y + dx)} <= pts)


assert [tilted_squares(n) for n in range(2, 7)] == [n * n * (n * n - 1) // 12 for n in range(2, 7)] == [1, 6, 20, 50, 105]
print("squares on n-by-n dot grids, n = 2..6: 1, 6, 20, 50, 105 = n^2(n^2-1)/12")
print("circle regions for 1..7 points:", [1 + comb(n, 2) + comb(n, 4) for n in range(1, 8)])


def hanoi_steps(state):
    """state[d] = peg of disk d (0 = smallest); legal moves of a top disk onto an empty peg or a larger disk."""
    tops = {}
    for d, peg in enumerate(state):
        tops.setdefault(peg, d)
    for peg, d in tops.items():
        for q in range(3):
            if q != peg and (q not in tops or tops[q] > d):
                yield state[:d] + (q,) + state[d + 1:]


for n in range(1, 5):
    d = bfs(tuple([0] * n), lambda s: list(hanoi_steps(s)))
    assert len(d) == 3 ** n and d[tuple([2] * n)] == 2 ** n - 1 == max(d.values())
moves = []


def solve(n, a, b, c):
    if n:
        solve(n - 1, a, c, b)
        moves.append(n)
        solve(n - 1, c, b, a)


solve(4, 0, 2, 1)
ruler = [(k & -k).bit_length() for k in range(1, 16)]
gray = [((k ^ (k >> 1)) ^ ((k - 1) ^ ((k - 1) >> 1))).bit_length() for k in range(1, 16)]
assert moves == ruler == gray
print("Tower of Hanoi: 3^n states, 2^n - 1 moves (n = 1..4); disk moved at each step = Gray-code position flipped:", ruler)


def slide_reach(nodes, edges, hole):
    """Arrangements with the hole back home, sliding one token at a time into the empty dot."""
    adj = {v: [] for v in nodes}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    idx = {v: i for i, v in enumerate(nodes)}
    start = tuple(None if v == hole else v for v in nodes)
    seen, dq = {start}, deque([start])
    while dq:
        s = dq.popleft()
        h = s.index(None)
        for u in adj[nodes[h]]:
            t = list(s)
            t[h], t[idx[u]] = t[idx[u]], None
            t = tuple(t)
            if t not in seen:
                seen.add(t)
                dq.append(t)
    return sum(1 for s in seen if s[idx[hole]] is None)


grid = [(r, c) for r in range(2) for c in range(3)]
grid_links = [(a, b) for a, b in combinations(grid, 2) if abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1]
loop = list(range(6))
counts = (slide_reach(grid, grid_links, (0, 0)), slide_reach(loop, [(i, (i + 1) % 6) for i in loop], 0),
          slide_reach(grid, grid_links + [((0, 0), (1, 1))], (0, 0)))
assert counts == (60, 5, 120)
print("sliding tokens, hole home: 2-by-3 grid 60, six-dot loop 5 (rotations), grid plus a diagonal 120, of 120")


def frogs(m, n):
    start, goal = "F" * m + "_" + "T" * n, "T" * n + "_" + "F" * m
    dist, dq = {start: 0}, deque([start])
    while dq:
        s = dq.popleft()
        if s == goal:
            return dist[s]
        h = s.index("_")
        for src, kind in ((h - 1, "F"), (h - 2, "F"), (h + 1, "T"), (h + 2, "T")):
            if 0 <= src < len(s) and s[src] == kind and not (abs(src - h) == 2 and s[(src + h) // 2] == "_"):
                t = list(s)
                t[h], t[src] = t[src], "_"
                t = "".join(t)
                if t not in dist:
                    dist[t] = dist[s] + 1
                    dq.append(t)


assert all(frogs(m, n) == m * n + m + n for m in range(1, 5) for n in range(1, 5))
print("frogs and toads: fewest moves m*n + m + n for m, n up to 4")


def set_partitions(n):
    if n == 0:
        return [[]]
    out = []
    for p in set_partitions(n - 1):
        out += [p[:i] + [p[i] + [n]] + p[i + 1:] for i in range(len(p))] + [p + [[n]]]
    return out


assert [len(set_partitions(n)) for n in range(1, 6)] == [1, 2, 5, 15, 52]
print("ways to split 1..5 children into teams: 1, 2, 5, 15, 52")
print("\nAll assertions passed.")
