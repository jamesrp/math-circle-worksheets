#!/usr/bin/env python3
"""Check the Week 67 critic follow-up (Critic C could 13) in the print guide.

Usage: python3 plans/review/checks/week-67/check_critic_fixes.py   (from the repository root)

K-1's "Put a counter on every dot where the walk can stop and still be shortest" for A and B on
Problem 1's left board marks every dot on some shortest A-B route; the guide's key says ten. The
tree's meeting dot is two roads below C (C - t - v in the card-fix verifier's tree).
"""
from pathlib import Path
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
P = ROOT / 'lowell-math-circle-year-2/week-67'


def N(s):
    return re.sub(r'\s+', ' ', s).strip()


g = pymupdf.open(P / 'week-67-facilitator.pdf')
old = pymupdf.open(P / 'archive-before-critic-fixes-2026-10-23/week-67-facilitator.pdf')
assert len(g) == len(old) == 3 and all('GGT67-FAC-v3' in p.get_text() for p in g)
t = N(' '.join(p.get_text() for p in g))
assert 'a smaller meeting counter (about ten for a K–1 pair)' in t
assert 'on the tree, the junction two roads below C.' in t and 'junction just below C' not in t
assert 'for A and B alone, the ten dots in the two bottom rows' in t
diff = [i + 1 for i, (a, b) in enumerate(zip(g, old)) if N(a.get_text()).replace('FAC-v3', 'FAC-v2') != N(b.get_text())]
assert diff == [1], diff
print('PASS guide: three pages, GGT67-FAC-v3; materials give a K-1 pair about ten counters for the key\'s ten dots; '
      'the tree key says "two roads below C"; only page 1 changed apart from footers.')
