#!/usr/bin/env python3
"""Week 5 (Tower cities): the old builder's checks (src/build.py's check()), run on the
puzzles named in ../figures.py, which the problem files draw. Every printed puzzle is
solved by brute force (how many cities fit), and every count the pages rely on is
recomputed. Prints the report that src/answers-check.txt holds; stops on the first
failed assertion. build.sh compares the report with answers-check.txt.
"""
import os
import sys
from collections import Counter
from itertools import combinations, permutations

WEEK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, WEEK)
from figures import (lr, solutions, show, view, all_with_clues, P23, P23_EXPECT, P23_MANY,  # noqa: E402
                     LADDER, TWO_FOURS, K_ROWS_P1, K_EYE_ROW, K_CARDS3, K_CARDS4, U_CARDS4)


def rows_for(n, pair):
    return [p for p in permutations(range(1, n + 1)) if lr(p) == pair]


def unique_puzzles(n, k):
    """Number of k-number clue sets (taken from some city) that fit exactly one city."""
    data = all_with_clues(n)
    keys = sorted(data[0][1].keys())
    count = 0
    for sub in combinations(keys, k):
        groups = Counter(tuple(cl[x] for x in sub) for sq, cl in data)
        count += sum(1 for v in groups.values() if v == 1)
    return count


def check():
    report = []
    # K-1
    shown = set(K_ROWS_P1) | {K_EYE_ROW}
    for row in K_ROWS_P1:
        report.append(f"K P1 row {row}: views {lr(row)}")
    report.append(f"K P1 + eye picture show {len(shown)} of the 6 orders: {sorted(shown)}")
    for pair in K_CARDS3:
        report.append(f"K P3 card {pair}: {rows_for(3, pair)}")
    left1 = [p for p in permutations(range(1, 5)) if lr(p)[0] == 1]
    assert len(left1) == 6 and all(p[0] == 4 for p in left1)
    report.append(f"K P5 left view 1, four towers: {left1}")
    r22 = rows_for(4, (2, 2))
    assert len(r22) == 6
    report.append(f"K P6 (2,2) rows of four: {r22}")
    report.append(f"K P5/P6 cubes for towers 1-4: {sum(range(1, 5))} (a pair has 12)")
    for pair in K_CARDS4:
        report.append(f"K P7 card {pair}: {len(rows_for(4, pair))} rows {rows_for(4, pair)[:3]}")
    # 2-3
    pairs3 = sorted({lr(p) for p in permutations((1, 2, 3))})
    report.append(f"23 P1 pairs that occur: {pairs3}")
    assert all(sum(sum(r) for r in sq) == 18 for sq, cl in all_with_clues(3))
    report.append("23 P2: every 3-by-3 city uses 18 cubes")
    for i, (pz, ex) in enumerate(zip(P23, P23_EXPECT)):
        s = solutions(3, pz)
        assert len(s) == ex, (i, len(s))
        report.append(f"23 P3 puzzle {i+1}: {len(s)} solution(s) {[show(x).replace(chr(10), '/') for x in s]}")
    s = solutions(3, P23_MANY)
    assert len(s) == 3
    report.append(f"23 P4: {len(s)} cities {[show(x).replace(chr(10), '/') for x in s]}")
    adds = []
    for key in [(sd, k) for sd in 'TBLR' for k in range(3)]:
        if key in P23_MANY:
            continue
        for v in (1, 2, 3):
            t = dict(P23_MANY); t[key] = v
            if len(solutions(3, t)) == 1:
                adds.append((key, v))
    assert adds
    report.append(f"23 P4 single added clues that work: {adds}")
    # 2-3 P5: fewest numbers is 2
    for key in [(sd, k) for sd in 'TBLR' for k in range(3)]:
        for v in (1, 2, 3):
            assert len(solutions(3, {key: v})) > 1
    u2 = unique_puzzles(3, 2)
    assert u2 > 0
    report.append(f"23 P5: every one-number puzzle has at least 2 cities; "
                  f"{u2} two-number puzzles have one city, so the fewest is 2")
    tot = sorted({sum(cl.values()) for sq, cl in all_with_clues(3)})
    report.append(f"23 P6 number of cities (turned/flipped count as different): {len(all_with_clues(3))}")
    report.append(f"23 P7 totals: {tot}")
    # 4-5
    for pair in U_CARDS4:
        report.append(f"45 P1 card {pair}: {len(rows_for(4, pair))} rows")
    assert all(sum(sum(r) for r in sq) == 40 for sq, cl in all_with_clues(4))
    report.append("45 P2: every 4-by-4 city uses exactly 40 cubes")
    for name, pz in zip(['E1', 'E2', 'M1', 'M2', 'H1', 'H2'], LADDER):
        s = solutions(4, pz)
        assert len(s) == 1, name
        report.append(f"45 P3 ladder {name} ({len(pz)} clues): {show(s[0]).replace(chr(10), '/')}")
    s = solutions(4, TWO_FOURS)
    assert len(s) == 4
    report.append(f"45 P4 two fours: {[show(x).replace(chr(10), '/') for x in s]}")
    adds = []
    for key in [(sd, k) for sd in 'TBLR' for k in range(4)]:
        if key in TWO_FOURS:
            continue
        for v in (1, 2, 3, 4):
            t = dict(TWO_FOURS); t[key] = v
            if len(solutions(4, t)) == 1:
                adds.append((key, v))
    assert adds
    report.append(f"45 P4 single added clues that work: {adds}")
    assert unique_puzzles(4, 2) == 0 and unique_puzzles(4, 3) > 0
    report.append("45 P5: fewest numbers for one city is 3 (no two-number puzzle has one city)")
    # 4-5 P6: a three-number puzzle with no 4
    keys4 = [(sd, k) for sd in 'TBLR' for k in range(4)]
    ex = None
    for sq, cl in all_with_clues(4):
        for sub in combinations(keys4, 3):
            cs = {k: cl[k] for k in sub}
            if 4 not in cs.values() and len(solutions(4, cs)) == 1:
                ex = cs; break
        if ex: break
    assert ex
    report.append(f"45 P6 example: {ex}")
    c4 = Counter(lr(p) for p in permutations(range(1, 5)))
    report.append(f"45 P7 table: {sorted(c4.items())}")
    c5 = Counter(view(p) for p in permutations(range(1, 6)))
    report.append(f"45 P8 rows of five by left view: {sorted(c5.items())}")
    groups = {}
    for sq, cl in all_with_clues(4):
        groups.setdefault(tuple(sorted(cl.items())), []).append(sq)
    same = [v for v in groups.values() if len(v) > 1]
    report.append(f"45 P9: {len(same)} clue sets shared by 2+ cities, e.g. {[show(x).replace(chr(10), '/') for x in same[0][:2]]}")
    print("\n".join(report))


if __name__ == "__main__":
    check()
