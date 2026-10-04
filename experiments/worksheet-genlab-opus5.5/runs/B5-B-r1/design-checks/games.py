"""Shared helpers for checking the Week 7 take-away game designs.

Conventions used everywhere:
  * A rule S is a tuple of allowed take-amounts. Every rule used on the pages contains 1,
    so every non-empty position has a legal move and "whoever takes the last counter wins"
    is exactly normal play (the player with no move loses).
  * "L" (losing pile) = the player ABOUT TO MOVE loses against best play
    ("you'd rather go second").  "W" = the player about to move can force a win.
  * Everything below is computed by brute-force backward induction on the actual game
    positions; nothing relies on Sprague-Grundy theory unless a function says so
    (the Grundy helpers are used only to compare against brute force).
"""
from functools import lru_cache


def moves(S, n):
    return [n - s for s in S if s <= n]


def losing_table(S, N, misere=False):
    """lose[n] is True when the player to move from a pile of n loses with best play.
    Normal play: taking the last counter wins.  Misere: taking the last counter loses."""
    lose = []
    for n in range(N + 1):
        if n == 0:
            # normal: the previous player took the last counter and won -> mover has lost.
            # misere: the previous player took the last counter and lost -> mover has won.
            lose.append(not misere)
            continue
        lose.append(all(not lose[m] for m in moves(S, n)))
    return lose


def losing_piles(S, lo, hi, misere=False):
    t = losing_table(S, hi, misere)
    return [n for n in range(lo, hi + 1) if t[n]]


def winning_takes(S, n, misere=False):
    """All take-amounts from pile n that leave a losing pile for the opponent."""
    t = losing_table(S, n, misere)
    return [s for s in S if s <= n and t[n - s]]


def grundy_table(S, N):
    g = []
    for n in range(N + 1):
        vals = {g[m] for m in moves(S, n)}
        v = 0
        while v in vals:
            v += 1
        g.append(v)
    return g


def eventual_period(seq, max_pre=None):
    """Smallest (preperiod, period) such that seq[i] == seq[i+p] for all i >= pre in range,
    requiring at least 3 full periods of evidence.  Returns None if not found."""
    N = len(seq)
    if max_pre is None:
        max_pre = N // 3
    for pre in range(max_pre):
        for p in range(1, (N - pre) // 3 + 1):
            if all(seq[i] == seq[i + p] for i in range(pre, N - p)):
                return pre, p
    return None


def multi_pile_lose(rules, piles, misere=False):
    """Brute-force outcome of a sum of take-away piles.
    rules: tuple of rules, one per pile; piles: tuple of sizes.
    A turn = take an allowed amount from exactly one pile.  Returns True if the player to
    move loses with best play."""
    rules = tuple(tuple(r) for r in rules)

    @lru_cache(maxsize=None)
    def lose(pos):
        if sum(pos) == 0:
            return not misere
        for i, (S, n) in enumerate(zip(rules, pos)):
            for s in S:
                if s <= n:
                    nxt = list(pos)
                    nxt[i] = n - s
                    if lose(tuple(nxt)):
                        return False
        return True

    return lose(tuple(piles))


def multi_pile_winning_moves(rules, piles):
    """List of (pile index, amount) moves that leave a losing position."""
    out = []
    for i, (S, n) in enumerate(zip(rules, piles)):
        for s in S:
            if s <= n:
                nxt = list(piles)
                nxt[i] = n - s
                if multi_pile_lose(rules, tuple(nxt)):
                    out.append((i, s))
    return out


def fmt_set(xs):
    return ", ".join(str(x) for x in xs)
