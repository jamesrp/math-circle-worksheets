#!/usr/bin/env python3
"""Checks the small numbers quoted in the draft plans for Weeks 176-181 (games, third group).

Standard library only. Run: python3 plans/drafts/weeks-101-plus/check_games_3.py
One function per week; each asserts the facts its draft quotes and prints "ok".
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product


# ---------------------------------------------------------------- week 176
def solve_2x2(m):
    """Zero-sum 2x2 game, payoffs to Row. Returns (p, q, value) with p = P(row 0), q = P(col 0),
    assuming no saddle point (the mixed solution equalises both rows and both columns)."""
    (a, b), (c, d) = [[F(x) for x in row] for row in m]
    den = a - b - c + d
    p = (d - c) / den
    q = (d - b) / den
    v = (a * d - b * c) / den
    return p, q, v


def certify(m, p, q, v):
    """Minimax certificate: Row's mix earns >= v against each column, Column's mix holds each row to <= v."""
    rows = len(m)
    cols = len(m[0])
    for j in range(cols):
        assert sum(p[i] * m[i][j] for i in range(rows)) >= v
    for i in range(rows):
        assert sum(q[j] * m[i][j] for j in range(cols)) <= v
    return True


def pure_gap(m):
    """Best guaranteed pure payoff for Row, and best pure cap for Column."""
    lower = max(min(row) for row in m)
    upper = min(max(m[i][j] for i in range(len(m))) for j in range(len(m[0])))
    return lower, upper


def check_week_176():
    # Hide the bean: seeker scores 1 for finding it under red, 2 under blue, 0 for a miss.
    # Rows: seeker guesses red, blue. Columns: hider hides red, blue. Payoff to seeker.
    bean = [[1, 0], [0, 2]]
    p, q, v = solve_2x2(bean)
    assert (p, q, v) == (F(2, 3), F(2, 3), F(2, 3))
    assert certify(bean, [p, 1 - p], [q, 1 - q], v)
    assert pure_gap(bean) == (0, 1)              # no pure choice is safe for either side
    # A die: red on 1-4, blue on 5-6 gives exactly 2/3.
    assert F(4, 6) == F(2, 3)
    # Predictable hiders lose: always red lets the seeker take 1 every round, always blue 2.
    assert max(bean[i][0] for i in range(2)) == 1 and max(bean[i][1] for i in range(2)) == 2
    # Variant 1 and 3 (blue pays 3): both sides use red 3/4, value 3/4.
    assert solve_2x2([[1, 0], [0, 3]]) == (F(3, 4), F(3, 4), F(3, 4))
    # General a, b: red with chance b/(a+b), value ab/(a+b).
    for a in range(1, 7):
        for b in range(1, 7):
            assert solve_2x2([[a, 0], [0, b]]) == (F(b, a + b), F(b, a + b), F(a * b, a + b))

    # Professor Swindle (Princeton Friends School problem): Louie gets 9 for two heads, 1 for two
    # tails, pays 5 for a mismatch. Looks fair (9 + 1 = 5 + 5) but favours the professor.
    prof = [[9, -5], [-5, 1]]
    p, q, v = solve_2x2(prof)
    assert (p, q, v) == (F(3, 10), F(3, 10), F(-4, 5))
    assert certify(prof, [p, 1 - p], [q, 1 - q], v)
    # Each playing heads half the time gives 0: the 50-50 habit hides the edge.
    assert sum(F(1, 4) * prof[i][j] for i in range(2) for j in range(2)) == 0
    # Against a professor who plays 3/10 heads, every Louie plan averages -4/5.
    for h in range(0, 11):
        ph = F(h, 10)
        assert ph * (F(3, 10) * 9 + F(7, 10) * -5) + (1 - ph) * (F(3, 10) * -5 + F(7, 10) * 1) == F(-4, 5)

    # Baez's lopsided matching pennies: A gets 10 for HH, 20 for TT, pays 10 for a mismatch.
    baez = [[10, -10], [-10, 20]]
    p, q, v = solve_2x2(baez)
    assert (p, q, v) == (F(3, 5), F(3, 5), F(2))

    # Odds and evens Morra: show 1 or 2 fingers, the total is paid to Evens if even, to Odds if odd.
    morra = [[2, -3], [-3, 4]]                  # rows Evens shows 1, 2; columns Odds shows 1, 2
    p, q, v = solve_2x2(morra)
    assert (p, q, v) == (F(7, 12), F(7, 12), F(-1, 12))
    assert certify(morra, [p, 1 - p], [q, 1 - q], v)
    # Both showing 1 or 2 equally often: Evens averages (2 - 3 - 3 + 4) / 4 = 0, so it looks fair.
    assert sum(F(1, 4) * morra[i][j] for i in range(2) for j in range(2)) == 0
    # A 12-card deck (7 cards "one", 5 cards "two") is the optimal randomiser for either side.
    assert F(7, 12) + F(5, 12) == 1
    # If Odds plays 7/12 "one", Evens loses 1/12 per round whatever it does; 12 rounds lose 1 point.
    for e in range(13):
        pe = F(e, 12)
        assert pe * (2 * F(7, 12) - 3 * F(5, 12)) + (1 - pe) * (-3 * F(7, 12) + 4 * F(5, 12)) == F(-1, 12)

    # Pattern predictors. Against a fair die (each move independent, 1/2 each) every guessing rule
    # that looks at the last two moves finds the coin exactly half the time on average.
    rules = list(product("LR", repeat=4))          # a guess for each of LL, LR, RL, RR
    keys = ["LL", "LR", "RL", "RR"]
    n = 8
    for rule in rules:
        hits = 0
        for seq in product("LR", repeat=n):
            hits += sum(1 for t in range(2, n) if dict(zip(keys, rule))[seq[t - 2] + seq[t - 1]] == seq[t])
        assert F(hits, 2 ** n * (n - 2)) == F(1, 2)
    # A hider who alternates is caught every time by "guess the opposite of last time".
    alt = "LRLRLRLRLRLR"
    assert all(("R" if alt[t - 1] == "L" else "L") == alt[t] for t in range(1, len(alt)))


# ---------------------------------------------------------------- week 177
def pirate_outcome(k, gold, strict=False):
    """Pirate game with k pirates (pirate k most senior proposes), `gold` coins.
    A plan passes with yes votes >= k/2 (proposer breaks ties), or > k/2 when strict.
    Voters accept only if strictly better off than after rejection; a pirate who would die on
    rejection accepts any plan. Returns a tuple of coins (None = thrown overboard) for pirates
    1..k, or 'ambiguous' if the proposer has a tie among cheapest voters."""
    if k == 1:
        return (gold,)
    need = k // 2 + 1 if strict else (k + 1) // 2      # yes votes needed, proposer included
    fallback = pirate_outcome(k - 1, gold, strict)
    if fallback == "ambiguous":
        return "ambiguous"
    # price of each other pirate's vote
    prices = []
    for i in range(k - 1):
        f = fallback[i]
        prices.append((0 if f is None else f + 1, i))
    prices.sort()
    others = need - 1
    if others == 0:
        plan = [0] * (k - 1) + [gold]
        return tuple(plan)
    chosen = prices[:others]
    cost = sum(c for c, _ in chosen)
    if cost > gold:
        # proposer cannot win; proposer is thrown overboard and the rest play the k-1 game
        return tuple(list(fallback) + [None])
    cutoff = chosen[-1][0]
    if others < len(prices) and prices[others][0] == cutoff:
        return "ambiguous"
    plan = [0] * k
    for c, i in chosen:
        plan[i] = c
    plan[k - 1] = gold - cost
    return tuple(plan)


def stewart_survivors(gold, n_max):
    """Counting recursion behind the many-pirate pattern (assuming, as Stewart's account does,
    that every proposer up to 2G survives and that a proposer can always buy `gold` votes at one
    coin each). Pirate k survives as proposer iff (k - m) + gold >= k/2, where m is the last
    surviving proposer below k (pirates m+1..k-1 would die, so they vote yes for nothing)."""
    surv = list(range(1, 2 * gold + 1))
    m = 2 * gold
    for k in range(2 * gold + 1, n_max + 1):
        if 2 * ((k - m) + gold) >= k:
            surv.append(k)
            m = k
    return surv


def check_week_177():
    # Ten gems, casting-vote rule. Pirates listed from most junior to most senior (the proposer).
    assert pirate_outcome(1, 10) == (10,)
    assert pirate_outcome(2, 10) == (0, 10)
    assert pirate_outcome(3, 10) == (1, 0, 9)
    assert pirate_outcome(4, 10) == (0, 1, 0, 9)
    assert pirate_outcome(5, 10) == (1, 0, 1, 0, 8)
    assert pirate_outcome(6, 10) == (0, 1, 0, 1, 0, 8)
    assert pirate_outcome(7, 10) == (1, 0, 1, 0, 1, 0, 7)
    # Classic five pirates and 100 coins: A 98, B 0, C 1, D 0, E 1 (A most senior).
    assert tuple(reversed(pirate_outcome(5, 100))) == (98, 0, 1, 0, 1)
    # With k <= 2G pirates the proposer keeps G - floor((k-1)/2), and the bribed pirates
    # alternate with the proposer's parity.
    for g in (10, 100):
        for k in range(1, 2 * g + 1):
            out = pirate_outcome(k, g)
            assert out[-1] == g - (k - 1) // 2
            assert sum(out) == g
            assert all(out[i] == (1 if (k - 1 - i) % 2 == 0 else 0) for i in range(k - 1))
    # Strict-majority variant (the Waterloo handout): two pirates means the senior one is
    # thrown overboard, so in the three-pirate game the middle pirate votes yes for nothing.
    assert pirate_outcome(2, 10, strict=True) == (10, None)
    assert pirate_outcome(3, 10, strict=True) == (0, 0, 10)
    assert pirate_outcome(4, 10, strict=True) == (1, 1, 0, 8)
    # Five pirates, strict majority: the proposer must choose which of two pirates gets 2,
    # matching the handout's "97 for A, 1 to C, 2 to D or E".
    assert pirate_outcome(5, 100, strict=True) == "ambiguous"
    fb = pirate_outcome(4, 100, strict=True)      # (1, 1, 0, 98): E, D, C, B
    assert fb == (1, 1, 0, 98)
    assert 100 - (fb[2] + 1) - (fb[0] + 1) == 97

    # Many pirates, 100 coins: surviving proposers above 200 are 201, 202, 204, 208, 216, 232,
    # 264, 328, 456, i.e. 2G + (a power of 2).
    surv = [s for s in stewart_survivors(100, 500) if s > 200]
    assert surv == [201, 202, 204, 208, 216, 232, 264, 328, 456]
    assert all((s - 200) & (s - 201) == 0 for s in surv)          # s - 200 is a power of 2
    # With 500 pirates, pirates 457 to 500 (44 of them) are thrown overboard.
    assert 500 - 456 == 44
    # Pirate 456 counts 128 free votes (329 to 456) plus 100 bought votes: 228 = 456 / 2.
    assert 456 - 328 == 128 and 128 + 100 == 228 and 2 * 228 == 456
    # Small-coin check of the same recursion: one coin, survivors 1, 2, 3, 4, 6, 10, 18, 34.
    assert [s for s in stewart_survivors(1, 40)] == [1, 2, 3, 4, 6, 10, 18, 34]


# ---------------------------------------------------------------- week 178
@lru_cache(None)
def random_turn(i, j):
    """Chance that A wins a race where A needs i steps, B needs j, and a fair coin picks the mover."""
    if i == 0:
        return F(1)
    if j == 0:
        return F(0)
    return (random_turn(i - 1, j) + random_turn(i, j - 1)) / 2


@lru_cache(None)
def richman(i, j):
    """Richman cost: the share of all the money A needs (A wins above it, loses below)."""
    if i == 0:
        return F(0)
    if j == 0:
        return F(1)
    return (richman(i - 1, j) + richman(i, j - 1)) / 2


LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def won(board, c):
    return any(all(board[k] == c for k in line) for line in LINES)


@lru_cache(None)
def richman_ttt(board):
    """Richman cost of tic-tac-toe for X when the bid winner places their own mark; a draw counts
    as a loss for X. Average of X's best and O's best next position."""
    if won(board, "X"):
        return F(0)
    if won(board, "O"):
        return F(1)
    empty = [k for k in range(9) if board[k] == "."]
    if not empty:
        return F(1)
    best_x = min(richman_ttt(board[:k] + "X" + board[k + 1:]) for k in empty)
    best_o = max(richman_ttt(board[:k] + "O" + board[k + 1:]) for k in empty)
    return (best_x + best_o) / 2


def discrete_race(total):
    """Develin-Payne discrete bidding on the race: both bid whole chips up to what they hold;
    the higher bid pays the other player and steps. On a tie the star holder either takes the bid
    (pays it, steps, and passes the star) or gives it (the other pays the holder and steps).
    Returns (a_wins, b_wins) functions of (i, j, a_chips, star)."""

    @lru_cache(None)
    def a_wins(i, j, a, star):
        if i == 0:
            return True
        if j == 0:
            return False
        b = total - a

        def res(x, y):
            if x > y:
                return a_wins(i - 1, j, a - x, star)
            if y > x:
                return a_wins(i, j - 1, a + y, star)
            if star == "A":
                return a_wins(i - 1, j, a - x, "B") or a_wins(i, j - 1, a + x, "A")
            return a_wins(i, j - 1, a + x, "A") and a_wins(i - 1, j, a - x, "B")

        return any(all(res(x, y) for y in range(b + 1)) for x in range(a + 1))

    @lru_cache(None)
    def b_wins(i, j, a, star):
        if i == 0:
            return False
        if j == 0:
            return True
        b = total - a

        def res(x, y):
            if x > y:
                return b_wins(i - 1, j, a - x, star)
            if y > x:
                return b_wins(i, j - 1, a + y, star)
            if star == "A":
                return b_wins(i - 1, j, a - x, "B") and b_wins(i, j - 1, a + x, "A")
            return b_wins(i, j - 1, a + x, "A") or b_wins(i - 1, j, a - x, "B")

        return any(all(res(x, y) for x in range(a + 1)) for y in range(b + 1))

    return a_wins, b_wins


def check_week_178():
    # Richman's theorem on the race grid: the share A needs is B's chance in the coin-flip game.
    for i in range(0, 6):
        for j in range(0, 6):
            if i == 0 and j == 0:
                continue
            assert richman(i, j) == 1 - random_turn(i, j)
    assert richman(1, 1) == F(1, 2)
    assert richman(1, 3) == F(1, 8) and random_turn(1, 3) == F(7, 8)
    assert richman(2, 3) == F(5, 16)
    assert richman(3, 3) == F(1, 2)
    # One step against j steps: each extra step the opponent needs halves the share you need.
    assert [richman(1, j) for j in range(1, 5)] == [F(1, 2), F(1, 4), F(1, 8), F(1, 16)]
    # Tic-tac-toe under Richman bidding: X needs more than 133/256 of the money (draws lose).
    assert richman_ttt("." * 9) == F(133, 256)
    assert F(133, 256) > F(1, 2)
    # Discrete chips with a tie-breaking star (Develin and Payne). Every position is won by
    # exactly one player.
    for total in (6, 8, 10):
        aw, bw = discrete_race(total)
        for i in range(1, 4):
            for j in range(1, 4):
                for a in range(total + 1):
                    for star in "AB":
                        assert aw(i, j, a, star) != bw(i, j, a, star)
    # Equal chips in an equal race: the star decides. 5 each, 2 steps each; 4 each, 3 steps each.
    aw, bw = discrete_race(10)
    assert aw(2, 2, 5, "A") and not aw(2, 2, 5, "B")
    assert min(a for a in range(11) if aw(2, 2, a, "A")) == 5
    assert min(a for a in range(11) if aw(2, 2, a, "B")) == 6
    aw8, _ = discrete_race(8)
    assert aw8(3, 3, 4, "A") and not aw8(3, 3, 4, "B")
    # One step against three, 10 chips in all: a single chip is enough, with or without the star.
    assert aw(1, 3, 1, "A") and aw(1, 3, 1, "B") and not aw(1, 3, 0, "B")
    # Two steps against three, 10 chips: 3 chips are enough (Richman share 5/16 of 10 is 3.125).
    assert min(a for a in range(11) if aw(2, 3, a, "A")) == 3
    assert min(a for a in range(11) if aw(2, 3, a, "B")) == 3
    assert F(5, 16) * 10 == F(25, 8)


# ---------------------------------------------------------------- week 179
def shapley(players, cost):
    """Average marginal cost over all arrival orders."""
    n = len(players)
    share = {p: F(0) for p in players}
    orders = list(permutations(players))
    for order in orders:
        seen = []
        for p in order:
            share[p] += cost(seen + [p]) - cost(seen)
            seen.append(p)
    return {p: share[p] / len(orders) for p in players}


def taxi_cost(dist):
    return lambda group: max((dist[p] for p in group), default=0)


def sequential_rule(dist):
    """Split each stretch of road equally among the riders still in the taxi (Littlechild-Owen)."""
    stops = sorted(set(dist.values()))
    share = {p: F(0) for p in dist}
    prev = 0
    for s in stops:
        riders = [p for p in dist if dist[p] >= s]
        for p in riders:
            share[p] += F(s - prev, len(riders))
        prev = s
    return share


def in_core(dist, share):
    players = list(dist)
    for r in range(1, len(players) + 1):
        for group in combinations(players, r):
            if sum(share[p] for p in group) > max(dist[p] for p in group):
                return False
    return True


def check_week_179():
    examples = [
        ({"A": 3, "B": 5, "C": 6}, {"A": 1, "B": 2, "C": 3}),
        ({"A": 6, "B": 8, "C": 9}, {"A": 2, "B": 3, "C": 4}),
        ({"A": 6, "B": 12, "C": 42}, {"A": 2, "B": 5, "C": 35}),            # Knight's taxi game
        ({"a": 12, "b": 24, "c": 36, "d": 40}, {"a": 3, "b": 7, "c": 13, "d": 17}),  # Amano et al.
    ]
    for dist, expect in examples:
        sh = shapley(list(dist), taxi_cost(dist))
        assert sh == {p: F(v) for p, v in expect.items()}
        assert sh == sequential_rule(dist)
        assert sum(sh.values()) == max(dist.values())                       # efficiency
        assert in_core(dist, sh)                                            # no group overpays
    # Equal split charges a friend who never rides: stops (0, 3, 5, 6) split 6 equally is 3/2 each,
    # while the Shapley share of the friend at 0 is 0.
    d0 = {"A": 0, "B": 3, "C": 5, "D": 6}
    assert shapley(list(d0), taxi_cost(d0))["A"] == 0 and F(6, 4) == F(3, 2)
    # Symmetry: two friends at the same stop pay the same. Null player: a friend at 0 pays 0.
    sh = shapley(["A", "B", "C", "D"], taxi_cost({"A": 4, "B": 4, "C": 7, "D": 0}))
    assert sh["A"] == sh["B"] == F(4, 3) and sh["D"] == 0 and sh["C"] == F(13, 3)
    # Six arrival orders for three friends; the friend at 6 pays extra only when last of all
    # who ride beyond 5: C's marginal cost is 6, 1, 1, ... averaging 3.
    dist = {"A": 3, "B": 5, "C": 6}
    marg_c = []
    for order in permutations("ABC"):
        before = order[:order.index("C")]
        marg_c.append(6 - max((dist[p] for p in before), default=0))
    assert sorted(marg_c) == [1, 1, 1, 3, 6, 6] and F(sum(marg_c), 6) == 3
    # Alternatives. Equal split of 6 for friends at 1, 5, 6: the friend at 1 pays 2 > 1 alone.
    d2 = {"A": 1, "B": 5, "C": 6}
    eq = {p: F(2) for p in d2}
    assert not in_core(d2, eq)
    assert shapley(list(d2), taxi_cost(d2)) == {"A": F(1, 3), "B": F(1, 3) + 2, "C": F(1, 3) + 2 + 1}
    # Split in proportion to distance, (3,5,6): 18/14, 30/14, 36/14; it is in the core here but
    # differs from the Shapley shares.
    prop = {p: F(6 * v, 14) for p, v in dist.items()}
    assert prop == {"A": F(9, 7), "B": F(15, 7), "C": F(18, 7)} and in_core(dist, prop)
    # Pay-for-your-own-extra in one fixed order (nearest first) is efficient but not symmetric:
    # A pays 3, B 2, C 1 for (3, 5, 6); farthest-first makes C pay all 6.
    assert [3, 5 - 3, 6 - 5] == [3, 2, 1]


# ---------------------------------------------------------------- week 180
def wins(group, weights, quota):
    return sum(weights[i] for i in group) >= quota


def banzhaf(weights, quota):
    n = len(weights)
    count = [0] * n
    for r in range(1, n + 1):
        for group in combinations(range(n), r):
            if wins(group, weights, quota):
                for i in group:
                    if not wins([j for j in group if j != i], weights, quota):
                        count[i] += 1
    return count


def shapley_shubik(weights, quota):
    n = len(weights)
    count = [0] * n
    total = 0
    for order in permutations(range(n)):
        s = 0
        for i in order:
            s += weights[i]
            if s >= quota:
                count[i] += 1
                break
        total += 1
    return [F(c, total) for c in count]


def check_week_180():
    # Nassau County Board, [16: 9, 9, 7, 3, 1, 1]: the 7 has as much power as each 9, and the
    # members with 3, 1 and 1 votes never change any result.
    w, q = [9, 9, 7, 3, 1, 1], 16
    bz = banzhaf(w, q)
    assert bz[0] == bz[1] == bz[2] > 0 and bz[3] == bz[4] == bz[5] == 0
    assert bz == [16, 16, 16, 0, 0, 0]
    assert shapley_shubik(w, q) == [F(1, 3)] * 3 + [F(0)] * 3
    assert sum(w) == 30 and 16 / 30 > 0.5
    # 1958 EEC Council, [12: 4, 4, 4, 2, 2, 1]: Luxembourg (1 vote) is a dummy.
    w, q = [4, 4, 4, 2, 2, 1], 12
    bz = banzhaf(w, q)
    assert bz == [10, 10, 10, 6, 6, 0]
    ss = shapley_shubik(w, q)
    assert ss == [F(7, 30)] * 3 + [F(3, 20)] * 2 + [F(0)]
    assert sum(w) == 17
    # Three parties [51: 49, 48, 3]: very different weights, equal power (any two win).
    assert banzhaf([49, 48, 3], 51) == [2, 2, 2]
    assert shapley_shubik([49, 48, 3], 51) == [F(1, 3)] * 3
    # Wellesley examples: [10: 7, 6, 2] has a dummy; [15: 9, 6, 3, 3, 3] Shapley-Shubik 45%, 20%, 7/60 each.
    assert banzhaf([7, 6, 2], 10) == [2, 2, 0]
    assert shapley_shubik([9, 6, 3, 3, 3], 15) == [F(54, 120), F(24, 120)] + [F(14, 120)] * 3
    # Kid table: three children with 4, 3, 2 cubes and a line at 5: any two reach it, equal power.
    assert banzhaf([4, 3, 2], 5) == [2, 2, 2]
    assert banzhaf([4, 3, 2], 6) == [3, 1, 1]       # raise the line to 6 and the 4 becomes strongest
    # Four children with 3, 2, 1, 1 cubes; move the line from 4 to 7.
    assert banzhaf([3, 2, 1, 1], 4) == [6, 2, 2, 2]  # line 4: the 2 is no stronger than a 1
    assert banzhaf([3, 2, 1, 1], 5) == [5, 3, 1, 1]
    assert banzhaf([3, 2, 1, 1], 6) == [3, 3, 1, 1]  # line 6: the 2 is as strong as the 3
    assert banzhaf([3, 2, 1, 1], 7) == [1, 1, 1, 1]  # everyone needed: equal power
    assert shapley_shubik([3, 2, 1, 1], 4) == [F(1, 2), F(1, 6), F(1, 6), F(1, 6)]
    assert shapley_shubik([3, 2, 1, 1], 6) == [F(5, 12), F(5, 12), F(1, 12), F(1, 12)]
    # Adding a vote can lower your power share: [8: 5, 3, 1, 1, 1] versus [8: 4, 4, 1, 1, 1].
    a = banzhaf([5, 3, 1, 1, 1], 8)
    b = banzhaf([4, 4, 1, 1, 1], 8)
    assert a == [9, 7, 1, 1, 1] and b == [8, 8, 0, 0, 0]
    # A 1-vote member has power in the first and none in the second.
    # The two indices can give different shares: [4: 2, 1, 1, 1].
    bz = banzhaf([2, 1, 1, 1], 4)
    assert [F(x, sum(bz)) for x in bz] == [F(2, 5)] + [F(1, 5)] * 3
    assert shapley_shubik([2, 1, 1, 1], 4) == [F(1, 2)] + [F(1, 6)] * 3
    # Dummy test: a voter is a dummy exactly when their Banzhaf count is 0, and then also their
    # Shapley-Shubik share is 0 (checked on all weight lists from 1..4 for 4 voters, all quotas).
    for ws in product(range(1, 5), repeat=4):
        for qq in range(sum(ws) // 2 + 1, sum(ws) + 1):
            bz = banzhaf(list(ws), qq)
            ss = shapley_shubik(list(ws), qq)
            assert all((bz[i] == 0) == (ss[i] == 0) for i in range(4))
            # more weight never means less power (monotone): heavier voter count >= lighter
            for i in range(4):
                for j in range(4):
                    if ws[i] >= ws[j]:
                        assert bz[i] >= bz[j]


# ---------------------------------------------------------------- week 181
def equilibria(n, paths, cost_fns):
    """All splits of n identical drivers over paths (tuples of edge names) where no driver can
    strictly lower their own time by switching path. Returns list of (split, times)."""
    out = []

    def splits(k, parts):
        if parts == 1:
            yield (k,)
            return
        for first in range(k + 1):
            for rest in splits(k - first, parts - 1):
                yield (first,) + rest

    for split in splits(n, len(paths)):
        load = {}
        for count, path in zip(split, paths):
            for e in path:
                load[e] = load.get(e, 0) + count

        def time(path, ld):
            return sum(cost_fns[e](ld.get(e, 0)) for e in path)

        times = [time(p, load) for p in paths]
        stable = True
        for a, pa in enumerate(paths):
            if split[a] == 0:
                continue
            for b, pb in enumerate(paths):
                if a == b:
                    continue
                ld = dict(load)
                for e in pa:
                    ld[e] -= 1
                for e in pb:
                    ld[e] = ld.get(e, 0) + 1
                if time(pb, ld) < times[a]:
                    stable = False
        if stable:
            out.append((split, times))
    return out


def total_time(split, paths, cost_fns):
    load = {}
    for count, path in zip(split, paths):
        for e in path:
            load[e] = load.get(e, 0) + count
    return sum(count * sum(cost_fns[e](load.get(e, 0)) for e in path) for count, path in zip(split, paths))


def check_week_181():
    # Floor map with 4 cars. Crowded roads take as many minutes as cars on them; long roads 5.
    kid = {"SA": lambda x: x, "AE": lambda x: 5, "SB": lambda x: 5, "BE": lambda x: x, "AB": lambda x: 0}
    two = [("SA", "AE"), ("SB", "BE")]
    three = two + [("SA", "AB", "BE")]
    eq_before = equilibria(4, two, kid)
    assert eq_before == [((2, 2), [7, 7])]
    eq_after = equilibria(4, three, kid)
    assert eq_after == [((0, 0, 4), [9, 9, 8])]       # everyone takes the shortcut, 8 minutes each
    # Best total with the shortcut open is still the 2-2 split (28 minutes); equilibrium costs 32.
    best = min(total_time(s, three, kid) for s in [(a, b, 4 - a - b) for a in range(5) for b in range(5 - a)])
    assert best == 28 and total_time((0, 0, 4), three, kid) == 32
    assert F(32, 28) == F(8, 7)
    # With the shortcut a lone car on S-A-E would take 4 + 5 = 9 > 8, so nobody leaves it.
    # Group totals (minutes summed over cars) at equilibrium, without and with the shortcut:
    # the shortcut helps 1, 2 or 3 cars, hurts 4 to 7 (at every equilibrium), and with 8 cars
    # the best equilibrium ties (72) while others are worse.
    def eq_totals(n, paths):
        return sorted(set(total_time(s, paths, kid) for s, _ in equilibria(n, paths, kid)))
    table = {n: (eq_totals(n, two), eq_totals(n, three)) for n in range(1, 9)}
    assert table == {1: ([6], [2]), 2: ([12], [8]), 3: ([20], [18]), 4: ([28], [32]),
                     5: ([38], [42, 46, 50]), 6: ([48], [52, 56, 60]), 7: ([60], [62, 66, 70]),
                     8: ([72], [72, 76, 80])}
    assert [s for s, _ in equilibria(3, three, kid)] == [(0, 0, 3)]     # 3 cars: 6 minutes each

    # Braess's own numbers (Nagurney's page): 6 travellers, a = 10f, b = f + 50, c = f + 50,
    # d = 10f, new link e = f + 10. Before 83 each; after 92 each.
    br = {"a": lambda f: 10 * f, "b": lambda f: f + 50, "c": lambda f: f + 50,
          "d": lambda f: 10 * f, "e": lambda f: f + 10}
    p_two = [("a", "c"), ("b", "d")]
    p_three = p_two + [("a", "e", "d")]
    assert equilibria(6, p_two, br) == [((3, 3), [83, 83])]
    assert ((2, 2, 2), [92, 92, 92]) in equilibria(6, p_three, br)
    assert [s for s, _ in equilibria(6, p_three, br)] == [(2, 2, 2)]
    # At the old 3-3 split the new path would take 30 + 10 + 30 = 70.
    assert 10 * 3 + (0 + 10) + 10 * 3 == 70

    # Divisible traffic (Roughgarden's lecture). Pigou: one unit, top road 1, bottom road x.
    # Equilibrium: all on the bottom, average 1. Best split puts half on each: 1/2 + 1/4 = 3/4.
    grid = [F(k, 100) for k in range(101)]
    avg = lambda x: (1 - x) * 1 + x * x            # x = share on the bottom road
    assert min(avg(x) for x in grid) == F(3, 4) and avg(F(1)) == 1
    assert F(1) / F(3, 4) == F(4, 3)
    # Braess, divisible: roads x, 1, 1, x and a free shortcut; 3/2 before, 2 after.
    assert F(1, 2) + 1 == F(3, 2)
    assert 1 + 1 == 2 and F(2) / F(3, 2) == F(4, 3)


def main():
    for name in ("check_week_176", "check_week_177", "check_week_178",
                 "check_week_179", "check_week_180", "check_week_181"):
        globals()[name]()
        print(name.replace("check_", ""), "ok")


if __name__ == "__main__":
    main()
