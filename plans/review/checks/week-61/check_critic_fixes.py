#!/usr/bin/env python3
"""Check the Week 61 critic follow-up (Critic C could 6) in the print guide.

Usage: python3 plans/review/checks/week-61/check_critic_fixes.py   (from the repository root)

The K-1 kit is two plain balls, so the K-1 key's triangle with three square corners must not
assume a marked top or middle line. Any point can be the top: down a quarter of a great circle,
a quarter along the circle a quarter of the way around from it, and back up is the octant
triangle, with three 90-degree corners. Only that sentence and the version id changed.
"""
from pathlib import Path
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
P = ROOT / 'lowell-math-circle-year-2/week-61'


def N(s):
    return re.sub(r'\s+', ' ', s).strip()


# The octant from any top T: unit vectors T, D (a quarter down), E (a quarter across); all corners 90 degrees.
T, D, E = (0, 0, 1), (1, 0, 0), (0, 1, 0)
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
assert dot(T, D) == dot(D, E) == dot(E, T) == 0       # each side a quarter of a great circle, each corner 90 degrees
print('PASS math: from any top, down a quarter, across a quarter and back up a quarter closes with three square corners.')

new, old = pymupdf.open(P / 'week-61-facilitator.pdf'), pymupdf.open(P / 'archive-before-critic-fixes-2026-10-23/week-61-facilitator.pdf')
assert len(new) == len(old) == 9
assert all('W61-F-v4' in p.get_text() for p in new)
t = N(' '.join(p.get_text() for p in new))
assert ('On the ball three square corners work: pick any dot as the top and go down, across and back up, each a '
        'quarter of the way around.') in t
assert 'down to the middle line' not in t
changed = [i + 1 for i, (a, b) in enumerate(zip(new, old))
           if N(a.get_text()).replace('W61-F-v4', 'W61-F-v3') != N(b.get_text())]
assert changed == [3, 9], changed       # p. 3 the key; p. 9 the version note
print('PASS guide: nine pages, W61-F-v4; the K-1 key starts from "any dot as the top"; only p. 3 (the key) and p. 9 '
      '(the version note) changed apart from footers.')
