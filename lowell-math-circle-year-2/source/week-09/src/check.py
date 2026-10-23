#!/usr/bin/env python3
"""Week 9 (Bouncing paths): the old builder's checks (src/gen.py's __main__), run on the
drawing code in ../figures.py and the problem files in ../problems/.

- the step-by-step simulation agrees with the lcm rule on every table up to 60 by 60,
  and the ball never stops at the starting corner;
- each unfolding sheet: thick lines crossed = bounces, and the panels the line passes
  through (the layers when folded) stay few;
- K-1 Problem 5: each circled corner can be made on a 3 by 3 grid;
- Grades 2-3 Problem 4: the tables on a 6 by 6 grid for each printed outcome (the last
  has none), and the problem file prints exactly these outcomes;
- Grades 4-5 Problem 6: the first three outcomes fit the 14 by 12 grid and the last has
  no table at all, and the problem file prints exactly these outcomes.
Prints ALL CHECKS PASSED, or stops at the first failure.
"""
import os
import sys

WEEK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, WEEK)
from figures import (ball_path, rule, unfold, tables_with, M23_TARGETS, M23_EXPECT,  # noqa: E402
                     M23_LABEL, U45_TARGETS)


def problem(name):
    with open(os.path.join(WEEK, 'problems', name)) as fh:
        return fh.read()


# sanity: simulation agrees with the lcm rule for every table used or asked about
for w in range(1, 61):
    for h in range(1, 61):
        _, c, b = ball_path(w, h)
        assert (c, b) == rule(w, h), (w, h)
        assert c != "bottom left"
print("simulation = lcm rule on every table up to 60 by 60; never the starting corner")
# unfolding sheets: crossings equal bounces; folded layers stay small
for cols, rows, w, h, layers in [(2, 1, 1, 2, 2), (3, 1, 1, 3, 3), (2, 1, 2, 4, 2),  # K-1
                                 (3, 2, 2, 3, 4), (3, 1, 1, 3, 3),                    # 2-3
                                 (4, 3, 2, 3, 4), (3, 4, 4, 3, 6)]:                   # 4-5
    end, crossed, n = unfold(cols, rows, w, h)
    assert crossed == rule(w, h)[1] and n == layers, (cols, rows, w, h, end, crossed, n)
print("unfolding sheets: crossings = bounces, layers 2 to 6")
# K-1 Problem 5: each target can be made on a 3 x 3 grid
for t in ("top left", "bottom right", "top right"):
    assert any(rule(w, h)[0] == t for w in range(1, 4) for h in range(1, 4))
print("K-1 Problem 5: every circled corner fits a 3 by 3 grid")
# Grades 2-3 Problem 4 targets on 6 x 6 grids, as printed
for t in M23_TARGETS:
    assert tables_with(t[0], t[1], 6, 6) == M23_EXPECT[t], (t, tables_with(t[0], t[1], 6, 6))
text = problem('12-m-draw-to-order.md')
assert all(text.count(M23_LABEL[t]) == 1 for t in M23_TARGETS) and text.count('label=') == 4
print("Grades 2-3 Problem 4: printed outcomes", M23_TARGETS, "-> tables", [M23_EXPECT[t] for t in M23_TARGETS])
# Grades 4-5 Problem 6: first three fit the 14 x 12 grid; the last has no table at all
for c, b in U45_TARGETS[:3]:
    assert tables_with(c, b, 14, 12), (c, b)
assert not tables_with("bottom right", 10, 60, 60)
text = problem('21-u-find-a-table.md')
assert [l for l in text.splitlines() if l.startswith('\\item')] == [
    f"\\item The ball stops at the {c} corner after {b} bounces." for c, b in U45_TARGETS]
print("Grades 4-5 Problem 6: printed outcomes", U45_TARGETS, "; the last is impossible")
print("ALL CHECKS PASSED")
