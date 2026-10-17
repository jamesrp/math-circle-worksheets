#!/usr/bin/env python3
"""Exact finite planning examples for Weeks 86/87; no classroom/physical claims.

Game classification uses the least capture attractor in visible alternating
one-cop states. This is independent of the folding certificate used in the key.
The universal mathematical statements have separate written proofs.
"""
from itertools import combinations, combinations_with_replacement
import json
from math import inf


def graph(n, edges):
    moves = [set([i]) for i in range(n)]
    for a, b in edges:
        moves[a].add(b)
        moves[b].add(a)
    return moves


def cop_starts(moves):
    n = len(moves)
    states = {(c, r, t) for c in range(n) for r in range(n) for t in (0, 1)}
    winning = {(c, c, t) for c in range(n) for t in (0, 1)}
    while True:
        added = set()
        for c, r, t in states - winning:
            if t == 0:
                if any((cc, r, 1) in winning for cc in moves[c]):
                    added.add((c, r, t))
            elif all((c, rr, 0) in winning for rr in moves[r]):
                added.add((c, r, t))
        if not added:
            break
        winning |= added
    return [c for c in range(n) if all((c, r, 0) in winning for r in range(n))]


def path(n):
    return [(i, i + 1) for i in range(n - 1)]


def worst_cop_move_counts(moves):
    """Minimax count of future cop turns; a stay consumes one cop turn."""
    n = len(moves)
    cost = {(c, r, t): 0 if c == r else inf
            for c in range(n) for r in range(n) for t in (0, 1)}
    while True:
        updated = dict(cost)
        for (c, r, t), current in cost.items():
            if c == r:
                continue
            value = (1 + min(cost[cc,r,1] for cc in moves[c]) if t == 0
                     else max(cost[c,rr,0] for rr in moves[r]))
            updated[c,r,t] = min(current, value)
        if updated == cost:
            return [max(cost[c,r,0] for r in range(n)) for c in range(n)]
        cost = updated


def ring(n):
    return path(n) + [(n - 1, 0)]


def assert_class(n, edges, expected):
    starts = cop_starts(graph(n, edges))
    assert bool(starts) is expected, (n, edges, starts)
    return starts


def folds(moves):
    return [(v, u) for v in range(len(moves)) for u in moves[v] - {v}
            if moves[v] <= moves[u]]


def pair(profile, a, b):
    score_a = sum(row.index(a) < row.index(b) for row in profile)
    score_b = len(profile) - score_a
    assert score_a != score_b
    return a if score_a > score_b else b


def agendas(profile):
    out = {}
    for bye in "ABC":
        first = [x for x in "ABC" if x != bye]
        finalist = pair(profile, *first)
        out[bye] = pair(profile, finalist, bye)
    return out


def line_vote(favorites, x, y):
    tally = [0, 0, 0]
    for p in favorites:
        a, b = abs(p - x), abs(p - y)
        tally[0 if a < b else 1 if b < a else 2] += 1
    return tally


games = {}
for n in (5, 7):
    games[f"path{n}"] = assert_class(n, path(n), True)
tree1 = [(0,1),(1,2),(0,3),(3,4),(0,5),(5,6)]
tree2 = [(0,1),(1,2),(2,3),(3,4),(2,5),(5,6),(5,7)]
games["T1"] = assert_class(7, tree1, True)
games["T2"] = assert_class(8, tree2, True)
for n in (4,5,6,8):
    games[f"C{n}"] = assert_class(n, ring(n), False)
games["C3"] = assert_class(3, ring(3), True)
chords4 = set(combinations(range(4),2)) - {tuple(sorted(e)) for e in ring(4)}
chords5 = set(combinations(range(5),2)) - {tuple(sorted(e)) for e in ring(5)}
for chord in chords4:
    assert_class(4, ring(4) + [chord], True)
for chord in chords5:
    assert_class(5, ring(5) + [chord], False)
assert_class(5, ring(5) + [(0,2),(0,3)], True)
designed = [(0,1),(1,2),(2,0),(2,3),(3,4),(4,5)]
games["six_dot_cop_design"] = assert_class(6, designed, True)
fold1 = [(0,1),(1,2),(2,0),(2,3),(3,4),(0,5)]
fold2 = ring(5) + [(0,2)]
games["F1"] = assert_class(6, fold1, True)
games["F2"] = assert_class(5, fold2, False)
assert folds(graph(5, fold2)) == [(1,0),(1,2)]
assert folds(graph(4, ring(4))) == []
capture_counts = {"path5":worst_cop_move_counts(graph(5,path(5))),
                  "path7":worst_cop_move_counts(graph(7,path(7))),
                  "T1":worst_cop_move_counts(graph(7,tree1)),
                  "T2":worst_cop_move_counts(graph(8,tree2))}
assert capture_counts["path5"] == [4,3,2,3,4]
assert capture_counts["path7"] == [6,5,4,3,4,5,6]
assert capture_counts["T1"][0] == 2
assert capture_counts["T2"][2] == 2 and capture_counts["T2"][5] == 3
# Check the actual F1 fold sequence without relabelling surviving vertices.
remaining = set(range(6))
edges = {frozenset(e) for e in fold1}
for v,u in [(4,3),(3,2),(5,0),(0,1),(1,2)]:
    def neighborhood(w):
        return {w} | {next(iter(e-{w})) for e in edges if w in e}
    assert v in remaining and u in neighborhood(v)
    assert neighborhood(v) <= neighborhood(u), (v,u)
    remaining.remove(v)
    edges = {e for e in edges if v not in e}
assert remaining == {2}

# Check the local evasion invariant against every legal cop response, all
# pre-cop safe positions, and all supplied ring lengths (including an odd ring).
invariant_states = 0
for n in (4,5,6,8):
    moves = graph(n, ring(n))
    for c in range(n):
        for r in set(range(n)) - moves[c]:
            for cc in moves[c]:
                assert cc != r
                assert moves[r] - moves[cc]
                invariant_states += 1

cycle = ["ABC", "BCA", "CAB"]
assert {a+b:pair(cycle,a,b) for a,b in ("AB","BC","CA")} == {
    "AB":"A", "BC":"B", "CA":"C"}
assert agendas(cycle) == {"A":"A","B":"B","C":"C"}
fixed = ["ABC", "ACB", "BAC"]
assert agendas(fixed) == {"A":"A","B":"A","C":"A"}
reverse = ["ACB", "CBA", "BAC"]
assert len(set(agendas(reverse).values())) == 3

favorites = [0,2,4,7,10]
counts = {q:line_vote(favorites,4,q) for q in range(11) if q != 4}
assert all(row[0] >= 3 for row in counts.values())
assert counts[0] == [3,1,1]
assert counts[8] == [3,2,0]
assert all(line_vote([1,4,4,4,9],4,q)[0] >= 3
           for q in range(11) if q != 4)
five_profiles = 0
for favorite_set in combinations_with_replacement(range(11),5):
    median = favorite_set[2]
    assert all(line_vote(favorite_set,median,q)[0] >= 3
               for q in range(11) if q != median)
    five_profiles += 1
even_favorites = [1,3,7,9]
weak = [x for x in range(11)
        if all((lambda s:s[0] >= s[1])(line_vote(even_favorites,x,y))
               for y in range(11) if x != y)]
strict = [x for x in range(11)
          if all((lambda s:s[0] > s[1])(line_vote(even_favorites,x,y))
                 for y in range(11) if x != y)]
assert weak == [3,4,5,6,7] and strict == []
assert all(line_vote(even_favorites,x,y) == [2,2,0]
           for x,y in combinations(range(3,8),2))
print(json.dumps({
    "status":"pass",
    "game_cop_starts":games,
    "worst_case_cop_move_counts_by_start":capture_counts,
    "cycle_safe_reply_cases":invariant_states,
    "C4_single_diagonals_checked":len(chords4),
    "C5_single_chords_checked":len(chords5),
    "cycle_agendas":agendas(cycle),
    "fixed_winner_agendas":agendas(fixed),
    "reverse_cycle_agendas":agendas(reverse),
    "five_favorites_counts":counts,
    "five_favorite_profiles_with_repetitions_checked":five_profiles,
    "even_voter_weak_locations":weak,
    "even_voter_strict_locations":strict,
    "scope":"Exact finite examples; written universal proofs separately reviewed. No PDF, physical rehearsal or classroom validation."
}, indent=2))
