#!/usr/bin/env python3
"""Checks carried over from the old student builder (make.py, archived in the
repository's source/week-50/archive-before-problem-files-2026-10-23/). checks.txt,
which make.py wrote, records what they establish."""


def stairs(n):
    pts = [(0, 0)]
    for i in range(n):
        pts.extend([((i+1)*160/n, i*120/n), ((i+1)*160/n, (i+1)*120/n)])
    return pts


for n in [1, 2, 4, 8]:
    ps = stairs(n)
    length = sum(abs(a-c)+abs(b-d) for (a, b), (c, d) in zip(ps, ps[1:]))
    assert length == 280
assert 120**2+160**2 == 200**2
# An eight-horizontal-piece centered staircase fits the narrow 8 mm corridor.
ps = [(0, 0), (0, 7.5)]
for i in range(1, 9):
    ps.append((20*i, 15*i-7.5)); ps.append((20*i, min(120, 15*i+7.5)))
assert ps[-1] == (160, 120) and max(abs(b-.75*a) for a, b in ps) == 7.5
print('PASS student checks: staircases of 1, 2, 4 and 8 steps are 280 mm; the diagonal is 200 mm; an '
      '8-horizontal-piece staircase fits the 8 mm strip with greatest gap 7.5 mm.')
