#!/usr/bin/env python3
"""Recompute every answer printed in the Week 7 adult guide.

The positions (piles, starts, track lengths, rules) are read from the final
student sources in ../src/*.tex where they appear as macro arguments, and
the rest are copied from the problem text with the page noted.  Every
answer is computed from the game rules alone (no closed forms are assumed),
then compared with EXPECTED, which mirrors what the guide prints.

Run:  python3 check.py        (exits non-zero on any mismatch)
"""
import itertools
import os
import re
import sys
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src")

FAIL = []


def check(name, got, want):
    ok = got == want
    print(("ok   " if ok else "FAIL ") + name + ": " + str(got))
    if not ok:
        print("       expected: " + str(want))
        FAIL.append(name)


# ---------------------------------------------------------------------------
# Game engine: one pile, allowed moves S.  A player who cannot move loses.
# Normal play: taking the last counter wins (so the player facing 0 loses).
# Misere: taking the last counter loses (the player facing 0 wins).
# win(n) is True when the player about to move from n can force a win.
# ---------------------------------------------------------------------------
def make_win(S, misere=False):
    S = tuple(sorted(S))

    @lru_cache(maxsize=None)
    def win(n):
        if n == 0:
            return misere  # normal: no move, mover lost; misere: mover won
        moves = [n - s for s in S if s <= n]
        if not moves:
            return False  # counters left but no legal move: mover loses
        return any(not win(m) for m in moves)

    return win


def losing(S, upto, misere=False):
    """Squares you want to leave for your opponent (mover loses there)."""
    w = make_win(S, misere)
    return [n for n in range(upto + 1) if not w(n)]


def winning_takes(S, n, misere=False):
    w = make_win(S, misere)
    return [s for s in sorted(S) if s <= n and not w(n - s)]


def choice(S, n, misere=False):
    """('first', [takes]) or ('second', [])."""
    t = winning_takes(S, n, misere)
    return ("first", t) if t else ("second", [])


# Two piles, move in one pile, last counter on the table wins (normal play).
# Brute force, independent of Grundy theory.
def make_win2(S):
    S = tuple(sorted(S))

    @lru_cache(maxsize=None)
    def win2(a, b):
        a, b = min(a, b), max(a, b)
        nxt = [(a - s, b) for s in S if s <= a] + [(a, b - s) for s in S if s <= b]
        if not nxt:
            return False
        return any(not win2(x, y) for x, y in nxt)

    return win2


def choice2(S, a, b):
    w2 = make_win2(S)
    if not w2(a, b):
        return ("second", [])
    good = []
    for s in sorted(S):
        if s <= a and not w2(a - s, b):
            good.append((a - s, b))
        if s <= b and not w2(a, b - s):
            good.append((a, b - s))
    return ("first", good)


def grundy(S, upto):
    g = []
    for n in range(upto + 1):
        opts = {g[n - s] for s in S if s <= n}
        m = 0
        while m in opts:
            m += 1
        g.append(m)
    return g


def period(seq, start_max=20):
    """Smallest (preperiod, period) with seq[i] == seq[i+p] for all i >= pre."""
    L = len(seq)
    for p in range(1, L // 3):
        for pre in range(0, start_max):
            if all(seq[i] == seq[i + p] for i in range(pre, L - p)):
                return pre, p
    return None


# ---------------------------------------------------------------------------
# Read the positions from the student sources.
# ---------------------------------------------------------------------------
def src(name):
    with open(os.path.join(SRC, name)) as f:
        return f.read()


K1, M23, U45 = src("k-1.tex"), src("grades-2-3.tex"), src("grades-4-5.tex")


def body(tex):
    return tex.split(r"\begin{document}", 1)[1]


def macro_args(tex, macro):
    """All argument lists of \\macro{...} or \\macro[..]{...} in the body."""
    out = []
    for m in re.finditer(r"\\" + macro + r"(?:\[[^\]]*\])?\{([^}]*)\}", body(tex)):
        out.append(m.group(1))
    return out


def ints(s):
    return [int(x) for x in re.split(r"\s*,\s*", s.strip())]


def pairs(s):
    return [tuple(int(y) for y in x.split("/")) for x in s.split(",")]


k1_choice = macro_args(K1, "pilechoice")     # P1, P9
k1_rows = macro_args(K1, "pilerows")         # P4
k1_two = macro_args(K1, "twopilechoice")     # P8
m_choice = macro_args(M23, "pilechoice")     # P1, P8
m_two = macro_args(M23, "twopiles")          # P7
u_rec = macro_args(U45, "pilerecord")        # P1, P3, P10
u_chart = macro_args(U45, "pilechart")       # P13

print("Positions read from the student sources")
print("  K-1  pilechoice:", k1_choice, " pilerows:", k1_rows, " twopilechoice:", k1_two)
print("  2-3  pilechoice:", m_choice, " twopiles:", m_two)
print("  4-5  pilerecord:", u_rec, " pilechart:", u_chart)
print()

K1_P1, K1_P9 = ints(k1_choice[0]), ints(k1_choice[1])
K1_P4 = ints(k1_rows[0])
K1_P8 = pairs(k1_two[0])
M_P1, M_P8 = ints(m_choice[0]), ints(m_choice[1])
M_P7 = pairs(m_two[0])
U_P1, U_P3, U_P10 = ints(u_rec[0]), ints(u_rec[1]), ints(u_rec[2])
U_P13_N = int(u_chart[0])

# Sanity: the text of the problems that we copy by hand.
assert "take 1 or 2 counters" in body(K1)
assert "1, 2 or 3 squares, starting on 10" in K1
assert "1 or 4 squares, starting on 8" in K1
assert "starts on 9 and moves 1, 3 or 4" in M23
assert "pile of 13" in M23
assert "pile\nof 50" in M23 and "pile of 100" in M23
assert "Play piles of 7 and 7" in U45
assert "piles of 20 and 11" in U45
assert "Take 2, 5 or 6 counters" in U45

# ---------------------------------------------------------------------------
# Expected values: exactly what the guide prints.
# ---------------------------------------------------------------------------
EXPECTED = {
    # K-1, moves 1 or 2
    "K1 P1": {2: ("first", [2]), 3: ("second", []), 4: ("first", [1]),
              5: ("first", [2]), 6: ("second", []), 7: ("first", [1]),
              8: ("first", [2])},
    "K1 P2 grown-up squares from 10": [9, 6, 3, 0],
    "K1 P4": {5: [2], 7: [1], 8: [2], 10: [1]},
    "K1 P5 go second on": [3, 6, 9],
    "K1 P6 first player's squares {1,2,3} from 10": [[8, 4, 0]],
    "K1 P7 first player's squares {1,4} from 8": [[7, 2, 0], [7, 5, 0]],
    "K1 P7 greedy 8->4 loses": True,
    "K1 P8": {(2, 2): ("second", []), (1, 2): ("first", [(1, 1)]),
              (3, 3): ("second", []), (2, 4): ("first", [(1, 4), (2, 2)]),
              (4, 4): ("second", [])},
    "K1 P9 misere": {1: ("second", []), 2: ("first", [1]), 3: ("first", [2]),
                     4: ("second", []), 5: ("first", [1]), 6: ("first", [2])},
    # 2-3, moves 1, 3 or 4 unless stated
    "M P1": {2: ("second", []), 5: ("first", [3]), 6: ("first", [4]),
             7: ("second", []), 8: ("first", [1])},
    "M P2 squares to leave 0-20": [0, 2, 7, 9, 14, 16],
    "M P3 starts 10-20": {10: ("first", [1, 3]), 11: ("first", [4]),
                          12: ("first", [3]), 13: ("first", [4]),
                          14: ("second", []), 15: ("first", [1]),
                          16: ("second", []), 17: ("first", [1, 3]),
                          18: ("first", [4]), 19: ("first", [3]),
                          20: ("first", [4])},
    "M P4 Lena right": True,
    "M P4 Lena reply table": {9: {8: [7], 6: [2], 5: [2]},
                              7: {6: [2], 4: [0], 3: [0, 2]}, 2: {1: [0]}},
    "M P5 Omar wins whatever": False,
    "M P5 Omar losing lines": [[13, 9, 5, 1, 0], [13, 9, 8, 4, 0]],
    "M P5 winning first take from 13": [4],
    "M P6 50": ("first", [1]),
    "M P6 100": ("second", []),
    "M P7": {(5, 5): ("second", []), (5, 6): ("first", [(4, 6), (5, 5)])},
    "M P8 {1,4}": {5: ("second", []), 6: ("first", [1, 4]), 8: ("first", [1]),
                   9: ("first", [4]), 10: ("second", [])},
    "M P9 {1,4}": [0, 2, 5, 7, 10, 12, 15, 17, 20],
    "M P9 {1,3,5}": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
    # 4-5
    "U P1 {1,2}": {7: ("first", [1]), 9: ("second", []), 11: ("first", [2]),
                   12: ("second", []), 16: ("first", [1])},
    "U P2 {1,2}": [0, 3, 6, 9, 12, 15, 18],
    "U P2 {1,2,3}": [0, 4, 8, 12, 16, 20],
    "U P3 {1,3,4}": {5: ("first", [3]), 8: ("first", [1]), 9: ("second", []),
                     11: ("first", [4]), 14: ("second", [])},
    "U P4 {1,3,4} 0-30": [0, 2, 7, 9, 14, 16, 21, 23, 28, 30],
    "U P5 Kai (first move wrong)": [5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29],
    "U P5 Kai greedy every turn beaten": [5, 8, 10, 12, 13, 15, 17, 18, 19,
                                          20, 22, 24, 25, 26, 27, 29],
    "U P5 greedy every turn always wins": [1, 3, 4, 6, 11],
    "U P6 100 {1,2}": ("first", [1]),
    "U P6 100 {1,2,3}": ("second", []),
    "U P6 100 {1,3,4}": ("second", []),
    "U P6 reply {1,3,4} by remainder": {1: [1], 3: [1, 3], 4: [4], 5: [3],
                                        6: [4]},
    "U P7 {1,4}": [0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30],
    "U P7 {2,3}": [0, 1, 5, 6, 10, 11, 15, 16, 20, 21, 25, 26, 30],
    "U P7 {1,3,5}": list(range(0, 31, 2)),
    "U P8 period {1,3,4}": (0, 7),
    "U P9 multiples of 5 rule": "contains 1,2,3,4 and no multiple of 5",
    "U P9 multiples of 3 rule": "contains 1,2 and no multiple of 3",
    "U P9 sample sets for 0,3,6": [[1, 2], [1, 2, 4], [1, 2, 5], [1, 2, 4, 5],
                                   [1, 2, 7], [1, 2, 4, 7], [1, 2, 8]],
    "U P10 misere {1,2}": {1: ("second", []), 3: ("first", [2]),
                           5: ("first", [1]), 7: ("second", []),
                           8: ("first", [1])},
    "U P11 misere {1,2}": [1, 4, 7, 10, 13, 16, 19],
    "U P11 misere {1,2,3}": [1, 5, 9, 13, 17],
    "U P12 7 and 7": ("second", []),
    "U P13 chart squares coloured": 34,
    "U P13 chart rule": "same remainder mod 3",
    "U P13 20 and 11": ("second", []),
    "U P14 {2,5,6}": [0, 1, 4, 8, 11, 12, 15, 19, 22, 23, 26, 30],
    "U P14 period": (0, 11),
    # playing to win: squares to leave as remainders, and the take(s) that
    # work from every pile with each other remainder
    "cheat {1,2}": (3, [0], {1: [1], 2: [2]}),
    "cheat {1,2,3}": (4, [0], {1: [1], 2: [2], 3: [3]}),
    "cheat {1,4}": (5, [0, 2], {1: [1], 3: [1], 4: [4]}),
    "cheat {1,3,4}": (7, [0, 2], {1: [1], 3: [1, 3], 4: [4], 5: [3], 6: [4]}),
    "cheat {2,3}": (5, [0, 1], {2: [2], 3: [2, 3], 4: [3]}),
    "cheat {1,3,5}": (2, [0], {1: [1]}),
    "cheat misere {1,2}": (3, [1], {0: [2], 2: [1]}),
    "cheat misere {1,2,3}": (4, [1], {0: [3], 2: [1], 3: [2]}),
    "K1 P5 first take by start": {1: [1], 2: [2], 4: [1], 5: [2], 7: [1],
                                  8: [2], 10: [1]},
    "launch pile of 7, first take": [1],
    "race to 10 by 1 or 2: totals to say": [1, 4, 7, 10],
    "race to 21 by 1, 2 or 3: totals to say": [1, 5, 9, 13, 17, 21],
    "race to 100 adding 1 to 10: totals to say": [1, 12, 23, 34, 45, 56, 67,
                                                  78, 89, 100],
    "U P5 Kai's move right for n>=4 exactly when remainder": [4, 6],
    "P8 window 7-10 equals 0-3 for {1,3,4}": True,
    # materials and printing
    "materials totals (counters, tokens, col. pencils, pencils, boards, paper)":
        [96, 8, 22, 14, 7, 10],
    "student page counts K-1, 2-3, 4-5": [6, 5, 8],
    "printed sheets K-1, 2-3, 4-5": [36, 30, 40],
    "0-10 tracks on K-1 page 2; 0-20 tracks on 2-3 page 1": [6, 2],
    # mathematics page
    "Grundy {1,2}": [0, 1, 2, 0, 1, 2, 0, 1, 2, 0],
    "Grundy {1,3,4}": [0, 1, 0, 1, 2, 3, 2, 0, 1, 0, 1, 2, 3, 2],
    "K1 P8 1 and 4 is a loss for the mover": True,
    # materials
    "largest single pile on a K-1 page": 10,
    "largest two-pile total on a K-1 page": 8,
    "largest pile or two-pile total on a 2-3 page (built)": 11,
    "largest pile or two-pile total on a 4-5 page (built)": 16,
}

# ---------------------------------------------------------------------------
# K-1
# ---------------------------------------------------------------------------
S12, S123, S134, S14, S23, S135 = (1, 2), (1, 2, 3), (1, 3, 4), (1, 4), (2, 3), (1, 3, 5)
check("K1 P1", {n: choice(S12, n) for n in K1_P1}, EXPECTED["K1 P1"])


def winner_paths(S, start, misere=False):
    """All games where the first player always makes a winning move (any of
    them) and the second player tries every legal move.  Returns the sorted
    list of distinct lists of squares the first player lands on."""
    w = make_win(S, misere)
    out = set()

    def rec(n, mine, first_to_move):
        if n == 0:
            out.add(tuple(mine))
            return
        if first_to_move:
            for s in winning_takes(S, n, misere):
                rec(n - s, mine + [n - s], False)
        else:
            for s in S:
                if s <= n:
                    rec(n - s, mine, True)

    assert w(start)
    rec(start, [], True)
    return sorted(list(p) for p in out)


paths = winner_paths(S12, 10)
check("K1 P2 grown-up squares from 10", sorted({x for p in paths for x in p}, reverse=True),
      EXPECTED["K1 P2 grown-up squares from 10"])
assert all(p == [9, 6, 3, 0] for p in paths)

check("K1 P4", {n: winning_takes(S12, n) for n in K1_P4}, EXPECTED["K1 P4"])
check("K1 P5 go second on", [n for n in range(1, 11) if choice(S12, n)[0] == "second"],
      EXPECTED["K1 P5 go second on"])
check("K1 P6 first player's squares {1,2,3} from 10", winner_paths(S123, 10),
      EXPECTED["K1 P6 first player's squares {1,2,3} from 10"])
check("K1 P7 first player's squares {1,4} from 8", winner_paths(S14, 8),
      EXPECTED["K1 P7 first player's squares {1,4} from 8"])
check("K1 P7 greedy 8->4 loses", make_win(S14)(4), EXPECTED["K1 P7 greedy 8->4 loses"])
check("K1 P8", {(a, b): choice2(S12, a, b) for a, b in K1_P8}, EXPECTED["K1 P8"])
check("K1 P9 misere", {n: choice(S12, n, True) for n in K1_P9}, EXPECTED["K1 P9 misere"])
check("K1 P8 1 and 4 is a loss for the mover", not make_win2(S12)(1, 4),
      EXPECTED["K1 P8 1 and 4 is a loss for the mover"])

# ---------------------------------------------------------------------------
# Grades 2-3
# ---------------------------------------------------------------------------
check("M P1", {n: choice(S134, n) for n in M_P1}, EXPECTED["M P1"])
check("M P2 squares to leave 0-20", losing(S134, 20), EXPECTED["M P2 squares to leave 0-20"])
check("M P3 starts 10-20", {n: choice(S134, n) for n in range(10, 21)},
      EXPECTED["M P3 starts 10-20"])


def second_player_reply_table(S, start):
    """For a losing start, the replies that keep the opponent on losing
    squares: {square before opponent: {square after opponent: my reply}}."""
    w = make_win(S)
    table = {}
    frontier = [start]
    seen = set()
    while frontier:
        n = frontier.pop()
        if n in seen or n == 0:
            continue
        seen.add(n)
        row = {}
        for s in S:
            if s <= n:
                m = n - s
                good = sorted(m - t for t in S if t <= m and not w(m - t))
                assert good, "no reply from %d" % m
                row[m] = good
                frontier.extend(good)
        table[n] = row
    return table


lena = second_player_reply_table(S134, 9)
check("M P4 Lena right", not make_win(S134)(9), EXPECTED["M P4 Lena right"])
check("M P4 Lena reply table", lena, EXPECTED["M P4 Lena reply table"])


def greedy_take(S, n):
    return max(s for s in S if s <= n)


def greedy_beaten_lines(S, start):
    """Greedy player moves first from start every turn; opponent tries every
    move.  Return the lines in which the opponent can force a win (opponent
    plays any move from which it then has a forced win)."""
    w = make_win(S)
    lines = []

    @lru_cache(maxsize=None)
    def opp_can_force(n):
        # opponent to move at n, greedy player replies greedily
        if n == 0:
            return False  # greedy player took the last counter
        for s in S:
            if s <= n:
                m = n - s
                if m == 0:
                    return True
                if not greedy_safe(m):
                    return True
        return False

    @lru_cache(maxsize=None)
    def greedy_safe(n):
        # greedy player to move at n: True if greedy wins against every reply
        m = n - greedy_take(S, n)
        return not opp_can_force(m)

    def rec(n, line, greedy_turn):
        if n == 0:
            if not greedy_turn:  # greedy took the last counter
                return
            lines.append(line)  # opponent took the last counter
            return
        if greedy_turn:
            rec(n - greedy_take(S, n), line + [n - greedy_take(S, n)], False)
        else:
            for s in S:
                if s <= n:
                    rec(n - s, line + [n - s], True)

    rec(start, [start], True)
    return sorted(lines), greedy_safe(start)


omar_lines, omar_safe = greedy_beaten_lines(S134, 13)
check("M P5 Omar wins whatever", omar_safe, EXPECTED["M P5 Omar wins whatever"])
check("M P5 Omar losing lines", omar_lines, EXPECTED["M P5 Omar losing lines"])
check("M P5 winning first take from 13", winning_takes(S134, 13),
      EXPECTED["M P5 winning first take from 13"])
check("M P6 50", choice(S134, 50), EXPECTED["M P6 50"])
check("M P6 100", choice(S134, 100), EXPECTED["M P6 100"])
check("M P7", {(a, b): choice2(S134, a, b) for a, b in M_P7}, EXPECTED["M P7"])
check("M P8 {1,4}", {n: choice(S14, n) for n in M_P8}, EXPECTED["M P8 {1,4}"])
check("M P9 {1,4}", losing(S14, 20), EXPECTED["M P9 {1,4}"])
check("M P9 {1,3,5}", losing(S135, 20), EXPECTED["M P9 {1,3,5}"])

# ---------------------------------------------------------------------------
# Grades 4-5
# ---------------------------------------------------------------------------
check("U P1 {1,2}", {n: choice(S12, n) for n in U_P1}, EXPECTED["U P1 {1,2}"])
check("U P2 {1,2}", losing(S12, 20), EXPECTED["U P2 {1,2}"])
check("U P2 {1,2,3}", losing(S123, 20), EXPECTED["U P2 {1,2,3}"])
check("U P3 {1,3,4}", {n: choice(S134, n) for n in U_P3}, EXPECTED["U P3 {1,3,4}"])
check("U P4 {1,3,4} 0-30", losing(S134, 30), EXPECTED["U P4 {1,3,4} 0-30"])

w134 = make_win(S134)
kai = [n for n in range(1, 31) if w134(n) and w134(n - greedy_take(S134, n))]
check("U P5 Kai (first move wrong)", kai, EXPECTED["U P5 Kai (first move wrong)"])
beaten = [n for n in range(1, 31) if w134(n) and not greedy_beaten_lines(S134, n)[1]]
check("U P5 Kai greedy every turn beaten", beaten, EXPECTED["U P5 Kai greedy every turn beaten"])
check("U P5 greedy every turn always wins",
      [n for n in range(1, 31) if greedy_beaten_lines(S134, n)[1]],
      EXPECTED["U P5 greedy every turn always wins"])

check("U P6 100 {1,2}", choice(S12, 100), EXPECTED["U P6 100 {1,2}"])
check("U P6 100 {1,2,3}", choice(S123, 100), EXPECTED["U P6 100 {1,2,3}"])
check("U P6 100 {1,3,4}", choice(S134, 100), EXPECTED["U P6 100 {1,3,4}"])
# The adult's reply to the pile the opponent leaves, by remainder mod 7;
# checked on every pile from 1 to 200 with that remainder.
rep = {}
for r in (1, 3, 4, 5, 6):
    sets = {tuple(winning_takes(S134, n)) for n in range(1, 201) if n % 7 == r}
    assert len(sets) == 1, (r, sets)
    rep[r] = list(sets.pop())
check("U P6 reply {1,3,4} by remainder", rep, EXPECTED["U P6 reply {1,3,4} by remainder"])
# Complement strategies: reply 3-k (moves 1,2) and 4-k (moves 1,2,3) always
# lands on a losing pile.
for S, m in ((S12, 3), (S123, 4)):
    for n in range(0, 200, m):
        for k in S:
            if k <= n:
                assert not make_win(S)(n - m), (S, n, k)
                assert (m - k) in S

check("U P7 {1,4}", losing(S14, 30), EXPECTED["U P7 {1,4}"])
check("U P7 {2,3}", losing(S23, 30), EXPECTED["U P7 {2,3}"])
check("U P7 {1,3,5}", losing(S135, 30), EXPECTED["U P7 {1,3,5}"])
w_seq = [make_win(S134)(n) for n in range(400)]
check("U P8 period {1,3,4}", period(w_seq), EXPECTED["U P8 period {1,3,4}"])

# P9: every move set from {1..12} of size at most 7, losing squares to 100.
N = 120
works5, works3 = [], []
for k in range(1, 8):
    for S in itertools.combinations(range(1, 13), k):
        L = losing(S, N)
        if L == list(range(0, N + 1, 5)):
            works5.append(S)
        if L == list(range(0, N + 1, 3)):
            works3.append(S)
rule5 = all(({1, 2, 3, 4} <= set(S) and not any(s % 5 == 0 for s in S)) == (S in works5)
            for k in range(1, 8) for S in itertools.combinations(range(1, 13), k))
rule3 = all(({1, 2} <= set(S) and not any(s % 3 == 0 for s in S)) == (S in works3)
            for k in range(1, 8) for S in itertools.combinations(range(1, 13), k))
check("U P9 multiples of 5 rule",
      "contains 1,2,3,4 and no multiple of 5" if rule5 else "rule fails",
      EXPECTED["U P9 multiples of 5 rule"])
check("U P9 multiples of 3 rule",
      "contains 1,2 and no multiple of 3" if rule3 else "rule fails",
      EXPECTED["U P9 multiples of 3 rule"])
check("U P9 sample sets for 0,3,6",
      [list(S) for S in EXPECTED["U P9 sample sets for 0,3,6"] if tuple(S) in works3],
      EXPECTED["U P9 sample sets for 0,3,6"])
assert (1, 2, 3, 4) in works5

check("U P10 misere {1,2}", {n: choice(S12, n, True) for n in U_P10},
      EXPECTED["U P10 misere {1,2}"])
check("U P11 misere {1,2}", losing(S12, 20, True), EXPECTED["U P11 misere {1,2}"])
check("U P11 misere {1,2,3}", losing(S123, 20, True), EXPECTED["U P11 misere {1,2,3}"])
check("U P12 7 and 7", choice2(S12, 7, 7), EXPECTED["U P12 7 and 7"])
w2 = make_win2(S12)
chart = [(a, b) for a in range(U_P13_N + 1) for b in range(U_P13_N + 1) if not w2(a, b)]
check("U P13 chart squares coloured", len(chart), EXPECTED["U P13 chart squares coloured"])
check("U P13 chart rule",
      "same remainder mod 3" if all((a % 3 == b % 3) == ((a, b) in chart)
                                    for a in range(U_P13_N + 1)
                                    for b in range(U_P13_N + 1)) else "other",
      EXPECTED["U P13 chart rule"])
check("U P13 20 and 11", choice2(S12, 20, 11), EXPECTED["U P13 20 and 11"])
S256 = (2, 5, 6)
check("U P14 {2,5,6}", losing(S256, 30), EXPECTED["U P14 {2,5,6}"])
check("U P14 period", period([make_win(S256)(n) for n in range(400)]),
      EXPECTED["U P14 period"])

# Playing-to-win table: period m, losing remainders, and the takes that
# work from EVERY pile n >= 1 (n <= 300) with each other remainder.
def cheat(S, misere=False):
    w = make_win(S, misere)
    seq = [w(n) for n in range(1, 400)]
    pre, m = period(seq)
    assert pre == 0
    lose = sorted({n % m for n in range(1, 300) if not w(n)} |
                  ({0} if not misere else set()))
    assert all((not w(n)) == (n % m in lose) for n in range(0 if not misere else 1, 300))
    takes = {}
    for r in range(m):
        if r in lose:
            continue
        ok = [s for s in sorted(S)
              if all(s <= n and not w(n - s) for n in range(1, 300) if n % m == r)]
        assert ok, (S, r)
        takes[r] = ok
    return (m, lose, takes)


for name, S, mis in (("cheat {1,2}", S12, False), ("cheat {1,2,3}", S123, False),
                     ("cheat {1,4}", S14, False), ("cheat {1,3,4}", S134, False),
                     ("cheat {2,3}", S23, False), ("cheat {1,3,5}", S135, False),
                     ("cheat misere {1,2}", S12, True),
                     ("cheat misere {1,2,3}", S123, True)):
    check(name, cheat(S, mis), EXPECTED[name])

check("K1 P5 first take by start",
      {n: winning_takes(S12, n) for n in range(1, 11) if make_win(S12)(n)},
      EXPECTED["K1 P5 first take by start"])
check("launch pile of 7, first take", winning_takes(S12, 7),
      EXPECTED["launch pile of 7, first take"])


def race_totals(T, S):
    """Counting up to T, adding an allowed amount each turn; whoever says T
    wins.  Saying total t leaves a pile of T - t, so the totals to say are
    those whose leftover is a losing pile."""
    w = make_win(S)
    return [t for t in range(1, T + 1) if not w(T - t)]


check("race to 10 by 1 or 2: totals to say", race_totals(10, S12),
      EXPECTED["race to 10 by 1 or 2: totals to say"])
check("race to 21 by 1, 2 or 3: totals to say", race_totals(21, S123),
      EXPECTED["race to 21 by 1, 2 or 3: totals to say"])
check("race to 100 adding 1 to 10: totals to say", race_totals(100, tuple(range(1, 11))),
      EXPECTED["race to 100 adding 1 to 10: totals to say"])

kai_rem = sorted({n % 7 for n in range(4, 300) if not w134(n - 4)})
assert all((not w134(n - 4)) == (n % 7 in (4, 6)) for n in range(4, 300))
check("U P5 Kai's move right for n>=4 exactly when remainder", kai_rem,
      EXPECTED["U P5 Kai's move right for n>=4 exactly when remainder"])
check("P8 window 7-10 equals 0-3 for {1,3,4}",
      [w134(n) for n in range(7, 11)] == [w134(n) for n in range(0, 4)],
      EXPECTED["P8 window 7-10 equals 0-3 for {1,3,4}"])

# Materials: per-table counts as printed in the guide, and their totals.
kids = {"K1": 4, "M": 4, "U": 3}
pairs_ = {"K1": 2, "M": 2, "U": 1}
counters = {"K1": 12 * 2 + 6, "M": 12 * 2 + 6, "U": 20 + 12 + 4}
assert 12 >= max(K1_P1 + K1_P4 + K1_P9) and 12 >= max(M_P1 + M_P8 + [a + b for a, b in M_P7])
assert 20 >= max(U_P1 + U_P3 + U_P10 + [14]) and 20 + 12 >= 20 + 11
tokens = {k: pairs_[k] + 1 for k in kids}
cpencils = {k: 2 * kids[k] for k in kids}
pencils = {k: kids[k] + 1 for k in kids}
boards = {"K1": 0, "M": pairs_["M"] + 1, "U": kids["U"] + 1}
paper = {"K1": 0, "M": 4, "U": 6}
check("materials totals (counters, tokens, col. pencils, pencils, boards, paper)",
      [sum(d.values()) for d in (counters, tokens, cpencils, pencils, boards, paper)],
      EXPECTED["materials totals (counters, tokens, col. pencils, pencils, boards, paper)"])
import subprocess
npages = []
for f in ("k-1.pdf", "grades-2-3.pdf", "grades-4-5.pdf"):
    out = subprocess.run(["pdfinfo", os.path.join(HERE, "..", f)], capture_output=True,
                         text=True).stdout
    npages.append(int(re.search(r"Pages:\s+(\d+)", out).group(1)))
check("student page counts K-1, 2-3, 4-5", npages, EXPECTED["student page counts K-1, 2-3, 4-5"])
check("printed sheets K-1, 2-3, 4-5", [npages[0] * 6, npages[1] * 6, npages[2] * 5],
      EXPECTED["printed sheets K-1, 2-3, 4-5"])
k1_page2 = body(K1).split(r"\newpage")[1]
m_page1 = body(M23).split(r"\newpage")[0]
check("0-10 tracks on K-1 page 2; 0-20 tracks on 2-3 page 1",
      [3 * k1_page2.count(r"\threetracks") + 2 * k1_page2.count(r"\twotracks")
       + k1_page2.count(r"\track{10}"),
       m_page1.count(r"\track{20}")],
      EXPECTED["0-10 tracks on K-1 page 2; 0-20 tracks on 2-3 page 1"])

check("Grundy {1,2}", grundy(S12, 9), EXPECTED["Grundy {1,2}"])
check("Grundy {1,3,4}", grundy(S134, 13), EXPECTED["Grundy {1,3,4}"])
# Grundy rule for the two-pile games on the pages: loss iff values equal.
for S in (S12, S134):
    g, w2s = grundy(S, 30), make_win2(S)
    assert all((g[a] == g[b]) == (not w2s(a, b)) for a in range(31) for b in range(31))

# Materials: the largest piles children build (not the 50/100/20+11 paper ones).
check("largest single pile on a K-1 page", max(K1_P1 + K1_P4 + K1_P9),
      EXPECTED["largest single pile on a K-1 page"])
check("largest two-pile total on a K-1 page", max(a + b for a, b in K1_P8),
      EXPECTED["largest two-pile total on a K-1 page"])
check("largest pile or two-pile total on a 2-3 page (built)",
      max(M_P1 + M_P8 + [a + b for a, b in M_P7]),
      EXPECTED["largest pile or two-pile total on a 2-3 page (built)"])
check("largest pile or two-pile total on a 4-5 page (built)",
      max(U_P1 + U_P3 + U_P10 + [14]),
      EXPECTED["largest pile or two-pile total on a 4-5 page (built)"])

print()
if FAIL:
    print("%d mismatches: %s" % (len(FAIL), ", ".join(FAIL)))
    sys.exit(1)
print("All %d checks agree with the guide." % len(EXPECTED))
