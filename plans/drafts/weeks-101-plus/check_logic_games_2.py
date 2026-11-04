#!/usr/bin/env python3
"""Checks for the draft plans of weeks 143-149 (logic and games, second group).

Every small number quoted in the week-143 to week-149 drafts is computed here.
Standard library only. Run: python3 plans/drafts/weeks-101-plus/check_logic_games_2.py
One function per week; each asserts the facts its draft quotes and prints "ok".
"""

import itertools
from collections import deque
from fractions import Fraction as F
from functools import lru_cache


# ---------------------------------------------------------------- week 143
# Two-input signals as 4-bit truth tables; bit i is the output when 2a + b = i.
A_SIG, B_SIG = 0b1100, 0b1010


def nand(x, y):
    return ~(x & y) & 0b1111


def fewest_nands(targets, max_gates=5):
    """Fewest NAND gates (inputs A, B only, no constants) whose signals include all targets."""
    best = None

    def grow(signals, used):
        nonlocal best
        if all(t in signals for t in targets):
            if best is None or used < best:
                best = used
            return
        if used == max_gates or (best is not None and used + 1 >= best):
            return
        for i in range(len(signals)):
            for j in range(i, len(signals)):
                new = nand(signals[i], signals[j])
                if new not in signals:
                    grow(signals + [new], used + 1)

    grow([A_SIG, B_SIG], 0)
    return best


def half_adder(a, b):
    return a ^ b, a & b  # (sum, carry)


def full_adder(a, b, c):
    s1, c1 = half_adder(a, b)
    s2, c2 = half_adder(s1, c)
    return s2, c1 | c2


def check_week_143():
    NOT_A, AND, OR, XOR = 0b0011, 0b1000, 0b1110, 0b0110
    # Truth tables built from NAND alone.
    assert nand(A_SIG, A_SIG) == NOT_A
    assert nand(nand(A_SIG, B_SIG), nand(A_SIG, B_SIG)) == AND
    assert nand(nand(A_SIG, A_SIG), nand(B_SIG, B_SIG)) == OR
    # Fewest NAND gates: NOT 1, AND 2, OR 3, XOR 4, half adder (XOR and AND together) 5.
    assert fewest_nands([NOT_A]) == 1
    assert fewest_nands([AND]) == 2
    assert fewest_nands([OR]) == 3
    assert fewest_nands([XOR]) == 4
    assert fewest_nands([XOR, AND]) == 5
    # There are 2^4 = 16 two-input truth tables, and NAND circuits make every one
    # (closure of {A, B} under NAND, plus constants from A NAND NOT A).
    sigs = {A_SIG, B_SIG}
    while True:
        new = {nand(x, y) for x in sigs for y in sigs} | sigs
        if new == sigs:
            break
        sigs = new
    assert len(sigs) == 16
    # A half adder counts how many of its two inputs are on: 00, 01, 01, 10.
    assert [half_adder(a, b)[::-1] for a in (0, 1) for b in (0, 1)] == [(0, 0), (0, 1), (0, 1), (1, 0)]
    # A full adder counts three inputs.
    for a, b, c in itertools.product((0, 1), repeat=3):
        s, carry = full_adder(a, b, c)
        assert 2 * carry + s == a + b + c
    # Parker's layout: one half adder and two full adders add any two 3-bit numbers (64 pairs).
    for x in range(8):
        for y in range(8):
            xb = [(x >> i) & 1 for i in range(3)]
            yb = [(y >> i) & 1 for i in range(3)]
            s0, c = half_adder(xb[0], yb[0])
            s1, c = full_adder(xb[1], yb[1], c)
            s2, c = full_adder(xb[2], yb[2], c)
            assert s0 + 2 * s1 + 4 * s2 + 8 * c == x + y
    # A domino OR (two lines merging) falls when either input falls: table 0, 1, 1, 1.
    assert [int(a or b) for a in (0, 1) for b in (0, 1)] == [0, 1, 1, 1]


# ---------------------------------------------------------------- week 144
def miu_moves(s):
    out = set()
    if s.endswith('I'):
        out.add(s + 'U')                      # rule 1
    out.add('M' + s[1:] * 2)                  # rule 2
    for i in range(1, len(s) - 2):            # rule 3
        if s[i:i + 3] == 'III':
            out.add(s[:i] + 'U' + s[i + 3:])
    for i in range(1, len(s) - 1):            # rule 4
        if s[i:i + 2] == 'UU':
            out.add(s[:i] + s[i + 2:])
    return out


def miu_bfs(cap):
    dist = {'MI': 0}
    q = deque(['MI'])
    while q:
        s = q.popleft()
        for t in miu_moves(s):
            if len(t) <= cap and t not in dist:
                dist[t] = dist[s] + 1
                q.append(t)
    return dist


def check_week_144():
    dist = miu_bfs(16)
    # The invariant: the number of I's is never a multiple of 3, so MU never appears.
    assert all(s.count('I') % 3 != 0 for s in dist)
    assert 'MU' not in dist
    # With strings up to 16 letters allowed along the way, every M-string of up to
    # 6 letters whose I count is not a multiple of 3 is reached (the characterisation).
    for k in range(1, 6):
        for w in itertools.product('IU', repeat=k):
            s = 'M' + ''.join(w)
            assert (s in dist) == (s.count('I') % 3 != 0)
    # With a cap of 12 letters some short theorems are missed (e.g. MIUUUI): detours can be long.
    small = miu_bfs(12)
    assert 'MIUUUI' not in small and 'MIUUUI' in dist
    # Fewest steps (cap 22 gives the same values).
    big = miu_bfs(22)
    want = {'MIU': 1, 'MII': 1, 'MIIU': 2, 'MIIII': 2, 'MIUIU': 2, 'MUI': 3, 'MUIU': 4}
    for s, n in want.items():
        assert dist[s] == n and big[s] == n
    # Cube-pile version: start with 1 cube; double the pile, or remove 3 cubes.
    seen = {1: 0}
    q = deque([1])
    while q:
        n = q.popleft()
        for m in (2 * n, n - 3):
            if 0 <= m <= 60 and m not in seen:
                seen[m] = seen[n] + 1
                q.append(m)
    assert sorted(m for m in seen if m <= 30) == [m for m in range(1, 31) if m % 3]
    assert 0 not in seen and 3 not in seen
    assert seen[5] == 4  # 1, 2, 4, 8, 5
    assert seen[7] == 6  # 1, 2, 4, 8, 5, 10, 7


# ---------------------------------------------------------------- week 145
GCAP = 14


@lru_cache(maxsize=None)
def weigh_solve(a, h, l, g, k, mode):
    """Can k weighings finish? a: coins that may be heavy or light; h: may only be heavy;
    l: may only be light; g: known genuine. mode 'type' must name the coin and heavy/light,
    mode 'coin' only the coin. Pans must hold equal numbers of coins."""
    hyp = 2 * a + h + l
    if mode == 'type' and hyp <= 1:
        return True
    if mode == 'coin' and a + h + l <= 1:
        return True
    if k == 0 or (mode == 'type' and hyp > 3 ** k):
        return False
    n = a + h + l + g
    for a1 in range(a + 1):
        for a2 in range(a - a1 + 1):
            for h1 in range(h + 1):
                for h2 in range(h - h1 + 1):
                    for l1 in range(l + 1):
                        for l2 in range(l - l1 + 1):
                            s1, s2 = a1 + h1 + l1, a2 + h2 + l2
                            if s1 + s2 == 0 or abs(s1 - s2) > g:
                                continue  # genuine coins fill the lighter-count pan
                            outcomes = [(0, a1 + h1, a2 + l2), (0, a2 + h2, a1 + l1),
                                        (a - a1 - a2, h - h1 - h2, l - l1 - l2)]
                            if all(weigh_solve(A, H, L, min(GCAP, n - A - H - L), k - 1, mode)
                                   for A, H, L in outcomes):
                                return True
    return False


def check_week_145():
    # One heavy coin: 3^k coins in k weighings, and not one more.
    for k in (1, 2, 3):
        assert weigh_solve(0, 3 ** k, 0, 0, k, 'type')
        assert not weigh_solve(0, 3 ** k + 1, 0, 0, k, 'type')
    assert weigh_solve(0, 9, 0, 0, 2, 'type') and not weigh_solve(0, 10, 0, 0, 2, 'type')
    # Heavier or lighter, name the coin and which: Dyson's range 3 <= n <= (3^k - 3)/2.
    for k in (2, 3):
        ok = [n for n in range(1, 16) if weigh_solve(n, 0, 0, 0, k, 'type')]
        assert ok == list(range(3, (3 ** k - 3) // 2 + 1))
    assert weigh_solve(12, 0, 0, 0, 3, 'type') and not weigh_solve(13, 0, 0, 0, 3, 'type')
    # Counting alone does not rule out 13: 26 cases fit in 27 outcomes.
    assert 2 * 13 <= 27 and 2 * 12 == 27 - 3
    # The first-weighing argument: j coins a pan; a tilt leaves 2j cases, a level result
    # 2(13 - 2j); no j keeps both at most 9.
    assert not any(2 * j <= 9 and 2 * (13 - 2 * j) <= 9 for j in range(1, 7))
    # (3^k - 3)/2 for k = 3, 4: 12 and 39.
    assert [(3 ** k - 3) // 2 for k in (3, 4)] == [12, 39]
    # Name the coin only: 13 coins in 3 weighings (but 2 coins never).
    ok = [n for n in range(1, 16) if weigh_solve(n, 0, 0, 0, 3, 'coin')]
    assert ok == [1] + list(range(3, 14))
    # With one extra coin known to be genuine: (3^k - 1)/2 coins, named with direction.
    for k in (2, 3):
        ok = [n for n in range(1, 16) if weigh_solve(n, 0, 0, 1, k, 'type')]
        assert ok == list(range(1, (3 ** k - 1) // 2 + 1))
    # Two-outcome questions would allow only 2^2 = 4 cases in two answers; three outcomes allow 9.
    assert 2 ** 2 == 4 and 3 ** 2 == 9


# ---------------------------------------------------------------- week 146
def equal_splits(ws):
    """Splits into two equal-total piles, counted once (the pile holding item 0 is listed)."""
    total = sum(ws)
    if total % 2:
        return []
    out = []
    for r in range(1, len(ws) + 1):
        for c in itertools.combinations(range(len(ws)), r):
            if 0 in c and sum(ws[i] for i in c) == total // 2 and r < len(ws):
                out.append(sorted(ws[i] for i in c))
    return out


def greedy_gap(ws):
    a = b = 0
    for w in sorted(ws, reverse=True):
        if a <= b:
            a += w
        else:
            b += w
    return abs(a - b)


def reachable_sums(ws):
    sums = {0}
    for w in ws:
        sums |= {s + w for s in sums}
    return sums


def check_week_146():
    # Greedy (biggest stick to the shorter row) can fail: 3 3 2 2 2 splits 6 | 6, greedy leaves a gap of 2.
    assert equal_splits([3, 3, 2, 2, 2]) == [[3, 3]]
    assert greedy_gap([3, 3, 2, 2, 2]) == 2
    # The seven-stick bag 2, 3, 5, 7, 8, 10, 13 (total 48) has exactly one equal split.
    bag = [2, 3, 5, 7, 8, 10, 13]
    assert sum(bag) == 48
    assert equal_splits(bag) == [[2, 5, 7, 10]]  # the other row is 3, 8, 13
    # Greedy on this bag: rows 13, 7, 3, 2 (25) and 10, 8, 5 (23), 2 apart.
    assert greedy_gap(bag) == 2
    # 2^7 = 128 ways to share 7 sticks between two rows, 64 if the rows are not told apart.
    assert 2 ** 7 == 128 and 2 ** 6 == 64
    # The bag 1, 3, 4, 7, 8, 11 (total 34) has no equal split, though no stick is over half
    # and the total is even.
    nobag = [1, 3, 4, 7, 8, 11]
    assert sum(nobag) == 34 and max(nobag) <= 17 and equal_splits(nobag) == []
    assert 17 not in reachable_sums(nobag)
    # Parity and too-big certificates for "no": 2 2 2 8 (all even, half 7); 1 1 1 7 (7 > half of 10).
    assert equal_splits([2, 2, 2, 8]) == [] and (sum([2, 2, 2, 8]) // 2) % 2 == 1
    assert equal_splits([1, 1, 1, 7]) == [] and 7 > 10 // 2
    # Doubling: 10 sticks give 512 splits, 20 give 524,288, 40 about 5.5 * 10^11.
    assert 2 ** 9 == 512 and 2 ** 19 == 524288 and 5.4e11 < 2 ** 39 < 5.6e11
    # Small whole-number lengths are easy by the running list of reachable totals:
    # for the 7-stick bag the list never holds more than 49 totals (0 to 48).
    assert len(reachable_sums(bag)) <= 49
    # Checking a 3-colouring of the Petersen graph means looking at 15 edges; there are 3^10 = 59049
    # colourings to search, of which 120 are proper.
    outer = [(i, (i + 1) % 5) for i in range(5)]
    spokes = [(i, i + 5) for i in range(5)]
    inner = [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    edges = outer + spokes + inner
    assert len(edges) == 15
    proper = sum(1 for col in itertools.product(range(3), repeat=10)
                 if all(col[u] != col[v] for u, v in edges))
    assert 3 ** 10 == 59049 and proper == 120


# ---------------------------------------------------------------- week 147
def lines_grid(n):
    L = [[(r, c) for c in range(n)] for r in range(n)]
    L += [[(r, c) for r in range(n)] for c in range(n)]
    L.append([(i, i) for i in range(n)])
    L.append([(i, n - 1 - i) for i in range(n)])
    return [frozenset(x) for x in L]


def maker_breaker(cells, lines, maker_first=True):
    """True if Maker (who only needs one whole line) wins with perfect play."""
    cells = tuple(cells)
    idx = {c: i for i, c in enumerate(cells)}
    masks = [sum(1 << idx[c] for c in line) for line in lines]

    @lru_cache(maxsize=None)
    def win(maker, breaker, maker_to_move):
        if any(m & maker == m for m in masks):
            return True
        live = [m for m in masks if m & breaker == 0]
        if not live:
            return False
        free = [i for i in range(len(cells)) if not (maker | breaker) >> i & 1]
        if not free:
            return False
        if maker_to_move:
            return any(win(maker | 1 << i, breaker, False) for i in free)
        return all(win(maker, breaker | 1 << i, True) for i in free)

    return win(0, 0, maker_first)


def ttt_value():
    lines = lines_grid(3)
    cells = [(r, c) for r in range(3) for c in range(3)]

    @lru_cache(maxsize=None)
    def val(xs, os, x_to_move):
        for line in lines:
            if line <= xs:
                return 1
            if line <= os:
                return -1
        free = [c for c in cells if c not in xs and c not in os]
        if not free:
            return 0
        if x_to_move:
            return max(val(xs | {c}, os, False) for c in free)
        return min(val(xs, os | {c}, True) for c in free)

    return val(frozenset(), frozenset(), True)


def find_pairing(n_cells_lines):
    """Backtracking: give each line two of its own cells, no cell used twice."""
    lines = n_cells_lines
    used = set()
    choice = []

    def go(i):
        if i == len(lines):
            return True
        cells = sorted(lines[i])
        for p, q in itertools.combinations(cells, 2):
            if p not in used and q not in used:
                used.update((p, q))
                choice.append((p, q))
                if go(i + 1):
                    return True
                choice.pop()
                used.difference_update((p, q))
        return False

    return choice if go(0) else None


def check_week_147():
    # Ordinary tic-tac-toe is a draw.
    assert ttt_value() == 0
    # Full drawn boards: 5 X, 4 O, no line for either.
    lines = lines_grid(3)
    cells = [(r, c) for r in range(3) for c in range(3)]
    draws = 0
    for xs in itertools.combinations(cells, 5):
        X = frozenset(xs)
        O = frozenset(cells) - X
        if not any(l <= X or l <= O for l in lines):
            draws += 1
    assert draws == 16
    assert len(lines) == 8
    # Maker-Breaker on 3x3: Maker wins moving first; moving second, Maker loses.
    assert maker_breaker(cells, lines, True)
    assert not maker_breaker(cells, lines, False)
    # Strip games (Maker first, Maker needs k neighbouring cells of a strip of n).
    for n in range(2, 13):
        strip = list(range(n))
        two = [frozenset((i, i + 1)) for i in range(n - 1)]
        three = [frozenset((i, i + 1, i + 2)) for i in range(n - 2)]
        assert maker_breaker(strip, two) == (n >= 3)
        if three:
            assert not maker_breaker(strip, three)
        # Pairing cells (0,1), (2,3), ...: every run of three contains a whole pair.
        pairs = [frozenset((2 * i, 2 * i + 1)) for i in range(n // 2)]
        assert all(any(p <= t for p in pairs) for t in three)
    # Line counts ((n+2)^k - n^k)/2: 3x3 has 8, 4x4 has 10, 5x5 has 12, 3x3x3 has 49.
    assert [((n + 2) ** k - n ** k) // 2 for n, k in ((3, 2), (4, 2), (5, 2), (3, 3))] == [8, 10, 12, 49]
    # A pairing needs two cells per line: 4x4 has 16 cells < 20; 5x5 has 25 >= 24, and one exists.
    assert 2 * 10 > 16 and 2 * 12 <= 25
    pairing = find_pairing(lines_grid(5))
    assert pairing is not None and len(pairing) == 12
    flat = [c for pq in pairing for c in pq]
    assert len(flat) == len(set(flat)) == 24
    # Golomb-Hales threshold n >= 2 / (2^(1/k) - 1): smallest n is 5, 8, 11, 14 for k = 2, 3, 4, 5.
    thresholds = []
    for k in (2, 3, 4, 5):
        n = 1
        while 2 * n ** k < (n + 2) ** k:
            n += 1
        thresholds.append(n)
    assert thresholds == [5, 8, 11, 14]


# ---------------------------------------------------------------- week 148
def best_reply_ties(guesses, p):
    """Payoffs (share of the prize) for a list of guesses: closest to p * mean wins, ties split."""
    target = p * F(sum(guesses), len(guesses))
    dists = [abs(g - target) for g in guesses]
    m = min(dists)
    winners = [i for i, d in enumerate(dists) if d == m]
    return [F(1, len(winners)) if i in winners else F(0) for i in range(len(guesses))]


def symmetric_equilibrium(n, value, p, top=100):
    base = best_reply_ties([value] * n, p)[0]
    for dev in range(top + 1):
        if dev == value:
            continue
        pay = best_reply_ties([dev] + [value] * (n - 1), p)[0]
        if pay > base:
            return False
    return True


def check_week_148():
    p = F(2, 3)
    # Levels of reasoning starting from 50: 33.3, 22.2, 14.8, 9.9.
    levels = [round(float(50 * p ** k), 1) for k in range(1, 5)]
    assert levels == [33.3, 22.2, 14.8, 9.9]
    # Upper bounds after rounds of crossing out: 66.7, 44.4, 29.6, 19.8; below 1 after 12 rounds.
    assert [round(float(100 * p ** k), 1) for k in range(1, 5)] == [66.7, 44.4, 29.6, 19.8]
    assert 100 * p ** 11 > 1 > 100 * p ** 12
    # Reported results: Nagel's first-round mean 36.73 gives target 24.49; ChessBase's 32.215
    # gives 21.48; Thaler's FT target 12.61 means an average of about 18.9.
    assert round(36.73 * 2 / 3, 2) == 24.49
    assert round(32.21539 * 2 / 3, 2) == 21.48
    assert round(12.61 * 3 / 2, 1) == 18.9
    # Whole numbers 0-100: everyone choosing 0 is an equilibrium for any group size;
    # everyone choosing 1 is one exactly when the group has at least 4 players;
    # everyone choosing 2 to 100 never is.
    for n in range(2, 16):
        assert symmetric_equilibrium(n, 0, p)
        assert symmetric_equilibrium(n, 1, p) == (n >= 4)
        for v in (2, 3, 10, 33, 50, 100):
            assert not symmetric_equilibrium(n, v, p)
    # K-1 version: towers of 0 to 10 cubes, target half the levelled tower.
    half = F(1, 2)
    for n in range(2, 12):
        assert symmetric_equilibrium(n, 0, half, top=10)
        for v in range(1, 11):
            assert not symmetric_equilibrium(n, v, half, top=10)
    # Practice round: towers 2, 4, 9 level to 5 each; half is 5/2, so the tower of 2 wins alone.
    towers = [2, 4, 9]
    assert F(sum(towers), 3) == 5 and half * 5 == F(5, 2)
    assert best_reply_ties(towers, half) == [1, 0, 0]


# ---------------------------------------------------------------- week 149
def u_track_inside(x, y):
    """The U track: a 20 by 12 rectangle of squares with a wall filling x < 15, 4 < y < 8."""
    if not (0 <= x <= 20 and 0 <= y <= 12):
        return False
    return not (x < 15 and 4 < y < 8)


def move_ok(x0, y0, x1, y1):
    steps = max(abs(x1 - x0), abs(y1 - y0)) * 4 + 1
    return all(u_track_inside(x0 + (x1 - x0) * F(i, steps), y0 + (y1 - y0) * F(i, steps))
               for i in range(steps + 1))


def fastest_u():
    start = (2, 2, 0, 0)
    dist = {start: 0}
    q = deque([start])
    while q:
        x, y, vx, vy = s = q.popleft()
        for ax in (-1, 0, 1):
            for ay in (-1, 0, 1):
                nvx, nvy = vx + ax, vy + ay
                nx, ny = x + nvx, y + nvy
                t = (nx, ny, nvx, nvy)
                if t in dist or not move_ok(x, y, nx, ny):
                    continue
                dist[t] = dist[s] + 1
                if ny >= 8 and nx <= 2:
                    return dist[t]
                q.append(t)
    return None


def park_moves(d):
    """Fewest moves along a line from rest to land on square d with a last move of length 1."""
    seen = {(0, 0): 0}
    q = deque([(0, 0)])
    while q:
        x, v = q.popleft()
        for nv in (v - 1, v, v + 1):
            nx = x + nv
            if nv <= 0 or nx > d or (nx, nv) in seen:
                continue
            seen[(nx, nv)] = seen[(x, v)] + 1
            q.append((nx, nv))
    return seen.get((d, 1))


def check_week_149():
    # Nine choices each turn: each coordinate of the move changes by -1, 0 or +1.
    assert len(list(itertools.product((-1, 0, 1), repeat=2))) == 9
    # Drag race from rest at full throttle: positions 1, 3, 6, 10, 15 (triangular numbers).
    pos, v, out = 0, 0, []
    for _ in range(5):
        v += 1
        pos += v
        out.append(pos)
    assert out == [1, 3, 6, 10, 15]
    # Parking: fewest moves to land on square d with a last move of length 1.
    parks = [park_moves(d) for d in range(1, 21)]
    assert parks == [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8]
    # The rule: m moves can park at most floor((m + 1)^2 / 4) squares away (1, 2, 4, 6, 9, 12, 16, 20).
    assert [(m + 1) ** 2 // 4 for m in range(1, 9)] == [1, 2, 4, 6, 9, 12, 16, 20]
    for d in range(1, 21):
        m = parks[d - 1]
        assert (m + 1) ** 2 // 4 >= d > m ** 2 // 4
    # The U track: fastest from rest at (2, 2) to the top-left finish box is 13 moves.
    assert fastest_u() == 13
    # Full throttle to the right from (2, 2) crashes into the far wall on move 6 (17 -> 23).
    x, v, crash = 2, 0, None
    for move in range(1, 10):
        v += 1
        if not move_ok(x, 2, x + v, 2):
            crash = (move, x, x + v)
            break
        x += v
    assert crash == (6, 17, 23)


def main():
    for name in ("check_week_143", "check_week_144", "check_week_145", "check_week_146",
                 "check_week_147", "check_week_148", "check_week_149"):
        globals()[name]()
        print(name.replace("check_", ""), "ok")


if __name__ == "__main__":
    main()
