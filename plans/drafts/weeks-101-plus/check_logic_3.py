#!/usr/bin/env python3
"""Checks for the draft plans of weeks 189-195 (logic, third group).

Every small number quoted in the week-189 to week-195 drafts is computed here.
Standard library only. Run: python3 plans/drafts/weeks-101-plus/check_logic_3.py
One function per week; each asserts the facts its draft quotes and prints "ok".
"""

import itertools
import math
from fractions import Fraction as F
from functools import lru_cache


# ---------------------------------------------------------------- week 189
def hat_outcomes(n, strategy):
    """strategy(i, hats) -> 'R', 'B' or None (pass); player i ignores hats[i].
    Returns (wins, correct guesses, wrong guesses) over all 2^n hat rows."""
    wins = right = wrong = 0
    for hats in itertools.product("RB", repeat=n):
        r = w = 0
        for i in range(n):
            g = strategy(i, hats)
            if g is None:
                continue
            if g == hats[i]:
                r += 1
            else:
                w += 1
        right += r
        wrong += w
        if r >= 1 and w == 0:
            wins += 1
    return wins, right, wrong


def three_player_rule(i, hats):
    others = [hats[j] for j in range(3) if j != i]
    if others[0] != others[1]:
        return None
    return "B" if others[0] == "R" else "R"


def hamming_rule(i, hats):
    """7 players numbered 1..7; codewords are rows whose red positions XOR to 0."""
    n = len(hats)
    def syndrome(row):
        s = 0
        for k in range(n):
            if row[k] == "R":
                s ^= k + 1
        return s
    rows = {}
    for c in "RB":
        row = list(hats)
        row[i] = c
        rows[c] = syndrome(row)
    # If one choice of my hat would make the row a codeword, guess the other colour.
    if rows["R"] == 0:
        return "B"
    if rows["B"] == 0:
        return "R"
    return None


def best_hat_strategy(n):
    """Exhaustive search over all deterministic guess-or-pass strategies."""
    views = list(itertools.product("RB", repeat=n - 1))
    choices = ["R", "B", None]
    per_player = list(itertools.product(choices, repeat=len(views)))
    rows = list(itertools.product("RB", repeat=n))
    best = 0
    balanced = True
    vidx = {(hats, i): views.index(hats[:i] + hats[i + 1:]) for hats in rows for i in range(n)}
    for combo in itertools.product(per_player, repeat=n):
        wins = right = wrong = 0
        for hats in rows:
            r = w = 0
            for i in range(n):
                g = combo[i][vidx[(hats, i)]]
                if g is None:
                    continue
                if g == hats[i]:
                    r += 1
                else:
                    w += 1
            right += r
            wrong += w
            if r and not w:
                wins += 1
        balanced = balanced and right == wrong
        best = max(best, wins)
    return best, balanced


def check_week_189():
    # Three players: win 6 of 8 rows; 6 right and 6 wrong guesses, wrong ones packed into 2 rows.
    wins, right, wrong = hat_outcomes(3, three_player_rule)
    assert (wins, right, wrong) == (6, 6, 6)
    assert F(wins, 8) == F(3, 4)
    # Two players: nothing beats 1/2. Three players: nothing beats 3/4.
    # In every strategy, right guesses equal wrong guesses over all rows.
    best2, bal2 = best_hat_strategy(2)
    assert best2 == 2 and bal2
    best3, bal3 = best_hat_strategy(3)
    assert best3 == 6 and bal3
    # Seven players with the Hamming rule: 112 of 128 rows, 7/8.
    wins7, right7, wrong7 = hat_outcomes(7, hamming_rule)
    assert wins7 == 112 and F(wins7, 128) == F(7, 8) and right7 == wrong7 == 112
    # Bound: a losing row holds at most n wrong guesses, so wins <= n * losses, i.e. P <= n/(n+1).
    for n, w in ((3, 6), (7, 112)):
        assert w <= n * (2 ** n - w) and F(w, 2 ** n) == F(n, n + 1)
    # 1 - 1/2^k for 2^k - 1 players: 3/4, 7/8, 15/16.
    assert [1 - F(1, 2 ** k) for k in (2, 3, 4)] == [F(3, 4), F(7, 8), F(15, 16)]
    # Everyone guessing at random (or one fixed guesser) wins half the time; all three guessing wins 1/8.
    assert F(1, 2) ** 3 == F(1, 8)


# ---------------------------------------------------------------- week 190
def cycles(perm):
    seen, out = set(), []
    for s in range(len(perm)):
        if s in seen:
            continue
        length, x = 0, s
        while x not in seen:
            seen.add(x)
            x = perm[x]
            length += 1
        out.append(length)
    return out


def loop_success(n):
    """Exact chance that every prisoner succeeds opening n/2 of n boxes with the loop rule."""
    half = n // 2
    return 1 - sum(F(1, k) for k in range(half + 1, n + 1))


def check_week_190():
    # Brute force agrees with 1 - (H_n - H_{n/2}) for 4, 6 and 8 boxes.
    for n in (4, 6, 8):
        good = sum(1 for p in itertools.permutations(range(n)) if max(cycles(p)) <= n // 2)
        assert F(good, math.factorial(n)) == loop_success(n)
    assert loop_success(4) == F(10, 24) == F(5, 12)          # about 42%
    assert loop_success(6) == F(23, 60)                      # about 38%
    assert round(float(loop_success(10)), 3) == 0.354
    p100 = loop_success(100)
    assert round(float(p100), 4) == 0.3118
    assert abs((1 - math.log(2)) - 0.30685) < 1e-5
    # The chance falls as n grows (checked for even n up to 100) and stays above 1 - ln 2.
    vals = [loop_success(n) for n in range(2, 101, 2)]
    assert all(a > b for a, b in zip(vals, vals[1:])) and float(vals[-1]) > 1 - math.log(2)
    # Cycle types of the 24 shuffles of 4: 1 identity, 6 swaps, 3 double swaps, 8 three-loops, 6 four-loops.
    from collections import Counter
    types = Counter(tuple(sorted(cycles(p))) for p in itertools.permutations(range(4)))
    assert types == Counter({(1, 1, 1, 1): 1, (1, 1, 2): 6, (2, 2): 3, (1, 3): 8, (4,): 6})
    # Chance of a loop of exact length L > n/2 is 1/L (n = 6).
    for L in (4, 5, 6):
        c = sum(1 for p in itertools.permutations(range(6)) if L in cycles(p))
        assert F(c, 720) == F(1, L)
    # Independent random choices: (1/2)^n; for 4 prisoners 1/16.
    assert F(1, 2) ** 4 == F(1, 16)
    assert 7e-31 < 0.5 ** 100 < 8e-31
    # One swap by a helper who sees every box always fixes a long loop (n = 6, 8).
    for n in (6, 8):
        for p in itertools.permutations(range(n)):
            if max(cycles(p)) <= n // 2:
                continue
            ok = False
            for a, b in itertools.combinations(range(n), 2):
                q = list(p)
                q[a], q[b] = q[b], q[a]
                if max(cycles(q)) <= n // 2:
                    ok = True
                    break
            assert ok
    # A ten-card deck: probability no loop longer than 5 is 1 - (1/6+...+1/10).
    assert loop_success(10) == 1 - (F(1, 6) + F(1, 7) + F(1, 8) + F(1, 9) + F(1, 10))


# ---------------------------------------------------------------- week 191
def say(s):
    out, i = [], 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out.append(str(j - i) + s[i])
        i = j
    return "".join(out)


def has_parent(s):
    """True if s is the reading of some row: even length, nonzero counts, neighbouring digits differ."""
    if len(s) % 2:
        return False
    pairs = [(s[k], s[k + 1]) for k in range(0, len(s), 2)]
    if any(c == "0" for c, _ in pairs):
        return False
    return all(pairs[k][1] != pairs[k + 1][1] for k in range(len(pairs) - 1))


def check_week_191():
    rows = ["1"]
    for _ in range(54):
        rows.append(say(rows[-1]))
    assert rows[:8] == ["1", "11", "21", "1211", "111221", "312211", "13112221", "1113213211"]
    lengths = [len(r) for r in rows]
    assert lengths[:12] == [1, 2, 2, 4, 6, 6, 8, 10, 14, 20, 26, 34]
    # Only the digits 1, 2, 3; never four equal digits in a row; never 333 (checked on 55 rows).
    for r in rows:
        assert set(r) <= set("123")
        assert "1111" not in r and "2222" not in r and "3333" not in r
        assert "333" not in r
    # Every row ends in 1; rows after the first have even length.
    assert all(r.endswith("1") for r in rows)
    assert all(len(r) % 2 == 0 for r in rows[1:])
    # Growth ratio settles near Conway's constant 1.3036 (row 55 against row 54).
    assert abs(lengths[-1] / lengths[-2] - 1.3036) < 0.01
    # Other starts: 22 never changes; a start d keeps d at the end; 4 survives only as the last digit.
    assert say("22") == "22"
    r = "4"
    for _ in range(12):
        r = say(r)
        assert r.endswith("4") and r.count("4") == 1
    assert [say("3"), say(say("3"))] == ["13", "1113"]
    # Which strings can be readings of an earlier row?
    assert not has_parent("1111")      # "one 1, one 1" would have been read as 21
    assert not has_parent("111")       # odd length
    assert has_parent("1211") and has_parent("3112")
    assert not has_parent("0211")      # a count of zero
    assert all(has_parent(r) for r in rows[1:])


# ---------------------------------------------------------------- week 192
def huffman_cost(weights):
    """Total length of the Huffman code = sum of all merge weights."""
    ws = sorted(weights)
    total = 0
    while len(ws) > 1:
        a, b = ws[0], ws[1]
        ws = sorted(ws[2:] + [a + b])
        total += a + b
    return total


def best_prefix_cost(weights, max_len=6):
    """Brute force over code lengths that satisfy Kraft (sum 2^-l <= 1)."""
    best = None
    for ls in itertools.product(range(1, max_len + 1), repeat=len(weights)):
        if sum(F(1, 2 ** l) for l in ls) <= 1:
            c = sum(w * l for w, l in zip(weights, ls))
            best = c if best is None else min(best, c)
    return best


def is_prefix_free(code):
    words = list(code.values())
    return not any(a != b and b.startswith(a) for a in words for b in words)


def decodings(bits, code):
    if not bits:
        return 1
    return sum(decodings(bits[len(w):], code) for w in code.values() if bits.startswith(w))


def check_week_192():
    msg = "ABRACADABRA"
    counts = {c: msg.count(c) for c in set(msg)}
    assert counts == {"A": 5, "B": 2, "R": 2, "C": 1, "D": 1}
    assert huffman_cost(counts.values()) == 23 == best_prefix_cost(list(counts.values()))
    assert 3 * len(msg) == 33                       # five letters need 3 bits each if all equal
    code = {"A": "0", "B": "100", "R": "101", "C": "110", "D": "111"}
    assert is_prefix_free(code)
    assert sum(len(code[c]) for c in msg) == 23
    bits = "".join(code[c] for c in msg)
    assert decodings(bits, code) == 1
    # Kraft: lengths 1,1,2 impossible; the code above uses the whole budget exactly.
    assert sum(F(1, 2 ** l) for l in (1, 1, 2)) > 1
    assert sum(F(1, 2 ** len(w)) for w in code.values()) == 1
    # Atlas AP-29's counts 4, 2, 1, 1: lengths 1, 2, 3, 3 send 14 bits, against 16 with 2 bits each.
    assert huffman_cost([4, 2, 1, 1]) == 14 == best_prefix_cost([4, 2, 1, 1])
    assert huffman_cost([1, 1, 1, 1]) == 8                # equal counts: the balanced tree
    # Morse without gaps is not prefix-free: E = . is the start of I = .. and S = ...
    morse = {"E": ".", "I": "..", "S": "...", "T": "-", "A": ".-", "N": "-.", "M": "--"}
    assert not is_prefix_free(morse)
    assert decodings("...", morse) == 4                  # EEE, EI, IE, S
    # MISSISSIPPI: Huffman 21 bits against 22 with two bits per letter.
    assert huffman_cost([4, 4, 2, 1]) == 21 and 2 * 11 == 22


# ---------------------------------------------------------------- week 193
def run_ant(steps):
    """Langton's ant on an all-white grid: on white turn right, on black turn left,
    flip the cell, step forward. Returns list of positions and the set of black cells."""
    black = set()
    x = y = 0
    dx, dy = 0, 1                     # facing up
    pos = [(0, 0)]
    for _ in range(steps):
        if (x, y) in black:
            dx, dy = -dy, dx          # left turn
            black.remove((x, y))
        else:
            dx, dy = dy, -dx          # right turn
            black.add((x, y))
        x, y = x + dx, y + dy
        pos.append((x, y))
    return pos, black


def check_week_193():
    pos, black = run_ant(12000)
    # First steps: the first four moves go round a square and come back to the start, all four cells black.
    p4, b4 = run_ant(4)
    assert p4[4] == (0, 0) and len(b4) == 4
    # Moves alternate horizontal and vertical.
    for (a, b), (c, d), (e, f) in zip(pos, pos[1:], pos[2:]):
        assert (a == c) != (c == e)
    # Highway: from some step on, the position 104 steps later is shifted by a fixed diagonal (2 cells each way).
    def shift(t):
        return (pos[t + 104][0] - pos[t][0], pos[t + 104][1] - pos[t][1])
    end = 12000 - 104
    target = shift(end)
    assert abs(target[0]) == 2 and abs(target[1]) == 2
    start = end
    while start > 0 and shift(start - 1) == target:
        start -= 1
    assert start == 9976                 # the 104-step repeat holds from step 9,976 on (sources: 9,977)
    # Reversibility: running the rule backward from step 500 recovers the empty start.
    p500, b500 = run_ant(500)
    x, y = p500[-1]
    dx, dy = x - p500[-2][0], y - p500[-2][1]
    b = set(b500)
    for _ in range(500):
        x, y = x - dx, y - dy               # step back
        if (x, y) in b:                     # cell is black now, so it was white and we turned right
            b.remove((x, y))
            dx, dy = -dy, dx                # undo right turn
        else:
            b.add((x, y))
            dx, dy = dy, -dx                # undo left turn
    assert (x, y) == (0, 0) and not b and (dx, dy) == (0, 1)
    # Twenty steps for the floor launch: how many black cells, and where the ant is.
    p20, b20 = run_ant(20)
    assert len(b20) == 6
    assert len(set(p20)) == 11        # cells visited in the first 20 steps (start included)


# ---------------------------------------------------------------- week 194
def check_week_194():
    # Pairings shown on the corridor: n -> n + 1 frees room 1; n -> 2n frees the odd rooms.
    rooms = range(1, 1001)
    assert sorted(n + 1 for n in rooms)[0] == 2
    evens = [2 * n for n in rooms]
    assert len(set(evens)) == len(evens) and all(e % 2 == 0 for e in evens)
    # Zigzag listing of all whole numbers 0, 1, -1, 2, -2, ... hits each once.
    zig = [0] + [s * k for k in range(1, 51) for s in (1, -1)]
    assert sorted(zig) == list(range(-50, 51))
    # Diagonal flip: for every list of k strips of length k (k = 1..4), the flipped diagonal is new.
    for k in range(1, 5):
        strips = list(itertools.product("RB", repeat=k))
        assert len(strips) == 2 ** k > k
        for lst in itertools.product(strips, repeat=k):
            diag = tuple("B" if lst[i][i] == "R" else "R" for i in range(k))
            assert all(diag != row for row in lst)
            assert all(diag[i] != lst[i][i] for i in range(k))
    # Three-cell strips: 8 in all, so a list of 3 rows misses at least 5.
    assert 2 ** 3 - 3 == 5
    # A list of 8 three-cell rows can hold every strip: finite strips can be listed in full.
    assert len(set(itertools.product("RB", repeat=3))) == 8
    # Fractions are listable: the diagonals of the grid list every p/q with p, q <= 6.
    seen = []
    for s in range(2, 13):
        for p in range(1, s):
            q = s - p
            if p <= 6 and q <= 6 and math.gcd(p, q) == 1:
                seen.append(F(p, q))
    assert len(seen) == len(set(seen)) == len({F(p, q) for p in range(1, 7) for q in range(1, 7)})


# ---------------------------------------------------------------- week 195
def fewest_weighings(n):
    """Exact fewest comparisons that sort n items in the worst case (adversary search)."""
    perms = frozenset(itertools.permutations(range(n)))
    pairs = list(itertools.combinations(range(n), 2))

    @lru_cache(maxsize=None)
    def solvable(state, d):
        if len(state) <= 1:
            return True
        if len(state) > 2 ** d:
            return False
        for a, b in pairs:
            left = frozenset(p for p in state if p[a] < p[b])
            right = state - left
            if not left or not right:
                continue
            if solvable(left, d - 1) and solvable(right, d - 1):
                return True
        return False

    d = 0
    while not solvable(perms, d):
        d += 1
    return d


def ford_johnson(n):
    return sum(math.ceil(math.log2(3 * k / 4)) for k in range(1, n + 1))


def info_bound(n):
    return math.ceil(math.log2(math.factorial(n)))


def binary_insertion_worst(n):
    return sum(math.ceil(math.log2(k + 1)) for k in range(1, n))


def merge_sort_worst(items):
    count = 0
    def ms(xs):
        nonlocal count
        if len(xs) <= 1:
            return xs
        m = len(xs) // 2
        a, b = ms(xs[:m]), ms(xs[m:])
        out = []
        while a and b:
            count += 1
            out.append(a.pop(0) if a[0] < b[0] else b.pop(0))
        return out + a + b
    ms(list(items))
    return count


def check_week_195():
    assert [info_bound(n) for n in range(1, 13)] == [0, 1, 3, 5, 7, 10, 13, 16, 19, 22, 26, 29]
    assert [ford_johnson(n) for n in range(1, 13)] == [0, 1, 3, 5, 7, 10, 13, 16, 19, 22, 26, 30]
    assert all(ford_johnson(n) == info_bound(n) for n in range(1, 12))
    assert ford_johnson(12) == 30 and info_bound(12) == 29
    # Exhaustive adversary search: 3 stones need 3, 4 need 5, 5 need 7.
    assert [fewest_weighings(n) for n in (2, 3, 4, 5)] == [1, 3, 5, 7]
    assert math.factorial(5) == 120 and 2 ** 6 == 64 < 120 <= 128 == 2 ** 7
    assert math.factorial(4) == 24 and 2 ** 4 == 16 < 24 <= 32
    # Ordinary methods use 8 for five stones: binary insertion and merge sort.
    assert binary_insertion_worst(5) == 8
    assert max(merge_sort_worst(p) for p in itertools.permutations(range(5))) == 8
    # Three stones, compare A with B, then the heavier with C: two weighings settle it 1 time in 3.
    two = 0
    for p in itertools.permutations(range(3)):
        a, b, c = p
        hi = max(a, b)
        if c > hi:
            two += 1
    assert F(two, 6) == F(1, 3)
    # The heaviest of n stones takes n - 1 weighings (a knockout): 4 for five stones.
    assert 5 - 1 == 4


def main():
    for name in ("check_week_189", "check_week_190", "check_week_191", "check_week_192",
                 "check_week_193", "check_week_194", "check_week_195"):
        globals()[name]()
        print(name.replace("check_", ""), "ok")


if __name__ == "__main__":
    main()
