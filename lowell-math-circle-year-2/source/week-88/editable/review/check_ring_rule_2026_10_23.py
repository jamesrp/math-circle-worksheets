#!/usr/bin/env python3
"""Week 88, Problem 11: the tempting rule "3 x (ratio + 1), rounded down" against the true ring maximum.

With middle radius R and outside radius r (ratio R/r), the largest ring of equal outside disks is
floor(pi / arcsin(1 / (ratio + 1))) (guide p. 6). The rule matches it at every ratio the kit can make
(1/2, 1, 3/2, 2, 3: rings of 4, 6, 7, 9, 12) but is false in general; among half-step ratios it first
fails at 3.5 (14 fit, not 13), and at 7 (25, not 24). Also checks that the guide source and the kit
say what this check supports. Standard library only. Run from the package folder:

    python3 review/check_ring_rule_2026_10_23.py
"""
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def ring(rho):
    return math.floor(math.pi / math.asin(1 / (rho + 1)) + 1e-12)


def rule(rho):
    return math.floor(3 * (rho + 1) + 1e-12)


fails = []
def check(ok, label):
    print(('ok   ' if ok else 'FAIL ') + label)
    if not ok:
        fails.append(label)


kit = {0.5: 4, 1: 6, 1.5: 7, 2: 9, 3: 12}
check(all(ring(r) == n == rule(r) for r, n in kit.items()), 'kit ratios 1/2, 1, 3/2, 2, 3: ring and rule both give 4, 6, 7, 9, 12')
halves = [(k / 2, ring(k / 2), rule(k / 2)) for k in range(1, 41)]
first = next(h for h in halves if h[1] != h[2])
check(first == (3.5, 14, 13), f'first half-step failure: ratio {first[0]}, {first[1]} fit, rule says {first[2]}')
check((7.0, 25, 24) in halves, 'ratio 7: 25 fit, rule says 24')
guide = (ROOT / 'guide' / 'facilitator.tex').read_text()
check('fits every ring the kit makes but fails at ratio 3.5 (14 fit, not 13)' in guide, 'guide p. 6 names the rule and where it fails')
check('so cut printed disks just inside the line' in guide, 'guide p. 2: cut just inside the line')
check('Cut just inside the line.' in (ROOT / 'student' / 'materials.tex').read_text(), 'materials p. 1: cut just inside the line')
print(f'{len(fails)} failure(s)')
sys.exit(1 if fails else 0)
