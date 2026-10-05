"""Independent game solver for the Week 7 math check (take-away games).

Written from scratch for the review; it does not import or read the
packet's own check.py.  Everything is computed by direct game-tree search
(memoised), not from remainder formulas, so the formulas the pages and the
guide state can be tested against it.

Conventions (from the student pages' opening rules):
  normal play: whoever takes the last counter (puts the token on 0) wins;
               a player who cannot move while counters are left loses
               (4-5 opening rule).
  misere play: whoever takes the last counter loses; a player who cannot
               move while counters are left still loses.
"""
import os, sys
from functools import lru_cache
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    # Fallback when run from the scratch run folder rather than checks/week-07/.
    d = HERE
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
        d = os.path.dirname(d)
    ROOT = d


sys.setrecursionlimit(20000)


@lru_cache(maxsize=None)
def _win(state, S, misere):
    """state: sorted tuple of piles; S: sorted tuple of moves."""
    if sum(state) == 0:
        # The previous player took the last counter.
        return misere  # misere: previous player lost, so the mover has won
    for i, a in enumerate(state):
        for s in S:
            if s <= a:
                nxt = list(state)
                nxt[i] -= s
                if not _win(tuple(sorted(nxt)), S, misere):
                    return True
    return False  # every move loses, or no move with counters left


def mover_wins_piles(piles, S, misere=False):
    """True if the player to move wins (best play) from a tuple of piles.
    A move takes s in S counters from one pile with at least s counters."""
    S = tuple(sorted(S))
    state = tuple(sorted(piles))
    if len(state) == 1 and state[0] > 1000:
        raise ValueError('too large')
    # warm the cache bottom-up for single piles to keep recursion shallow
    if len(state) == 1:
        for m in range(0, state[0], 200):
            _win((m,), S, misere)
    return _win(state, S, misere)


def P_positions(S, upto, misere=False):
    """Single-pile squares you want to leave for the opponent (mover loses)."""
    return [n for n in range(upto + 1) if not mover_wins_piles((n,), S, misere)]


def winning_takes(n, S, misere=False):
    """All first takes from a single pile n that leave a losing pile."""
    return [s for s in sorted(S) if s <= n and not mover_wins_piles((n - s,), S, misere)]


def winning_two_pile_moves(a, b, S):
    out = []
    for which, (x, y) in (('first pile', (a, b)), ('second pile', (b, a))):
        for s in sorted(S):
            if s <= x and not mover_wins_piles((x - s, y), S):
                out.append((which, s, (x - s, y) if which == 'first pile' else (y, x - s)))
    return out


def grundy(S, upto):
    g = []
    for n in range(upto + 1):
        opts = {g[n - s] for s in S if s <= n}
        m = 0
        while m in opts:
            m += 1
        g.append(m)
    return g


def greedy_take(n, S):
    allowed = [s for s in S if s <= n]
    return max(allowed) if allowed else None


def greedy_all_game_wins(n, S):
    """True if a player who always takes the most allowed counters wins from
    n (he moves first) against EVERY reply of the opponent."""
    @lru_cache(maxsize=None)
    def kai_to_move(m):
        t = greedy_take(m, S)
        if t is None:
            return False
        r = m - t
        if r == 0:
            return True
        return opp_to_move(r)

    @lru_cache(maxsize=None)
    def opp_to_move(m):
        replies = [s for s in S if s <= m]
        if not replies:
            return True  # opponent stuck
        for s in replies:
            if m - s == 0:
                return False  # opponent takes the last counter
            if not kai_to_move(m - s):
                return False
        return True
    return kai_to_move(n)


def outcome_sequence(S, length, misere=False):
    return ''.join('P' if not mover_wins_piles((n,), S, misere) else 'N' for n in range(length))


def pre_period(S, length=400):
    """(preperiod, period) of the normal-play outcome sequence, found by
    searching the computed prefix."""
    seq = outcome_sequence(S, length)
    best = None
    for p in range(1, length // 4):
        # smallest start t such that seq[n] == seq[n+p] for all n >= t in range
        t = length - p
        while t > 0 and seq[t - 1] == seq[t - 1 + p]:
            t -= 1
        if t < length // 2:
            cand = (t, p)
            if best is None or cand[1] < best[1]:
                best = cand
                break
    return best
