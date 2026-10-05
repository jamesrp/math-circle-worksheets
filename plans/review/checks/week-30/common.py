"""Shared helpers for the Week 30 math check (two-pan weight kits).

Written independently of the packet's own builders and checkers; nothing here
imports from lowell-math-circle-year-2/source/.

Convention (from the student pages): the target stays on the left pan, each
weight goes on the left (beside the target), on the right (opposite) or off.
A placement is a tuple of coefficients c_i in {-1, 0, +1}; +1 = opposite the
target, -1 = beside it.  The placement balances target t exactly when
t + (sum of left weights) = (sum of right weights), i.e. t = sum c_i w_i.
"""
import os
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))


def find_root():
    # Committed copy lives in plans/review/checks/week-30/: four folders up.
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')):
        return cand
    # Fallback for the scratch run folder (tmp/review-runs/week-30/).
    d = HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository root not found')


ROOT = find_root()
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-30')
PDF = {
    'K': os.path.join(WEEK, 'week-30-k-1.pdf'),
    '23': os.path.join(WEEK, 'week-30-grades-2-3.pdf'),
    '45': os.path.join(WEEK, 'week-30-grades-4-5.pdf'),
    'BON': os.path.join(WEEK, 'week-30-bonus.pdf'),
    'GUIDE': os.path.join(WEEK, 'week-30-facilitator.pdf'),
    'BGUIDE': os.path.join(WEEK, 'week-30-bonus-facilitator.pdf'),
}


def placements(weights):
    """All 3^m placements as (coeffs, value)."""
    for cs in product((-1, 0, 1), repeat=len(weights)):
        yield cs, sum(c * w for c, w in zip(cs, weights))


def reachable(weights):
    """Positive targets the kit can balance."""
    return sorted({v for _, v in placements(weights) if v > 0})


def ways(weights, t):
    """Every placement balancing target t, as (left list, right list)."""
    out = []
    for cs, v in placements(weights):
        if v == t:
            left = [w for c, w in zip(cs, weights) if c == -1]
            right = [w for c, w in zip(cs, weights) if c == 1]
            out.append((left, right))
    return out


def run_length(weights):
    """Largest n such that every target 1..n balances (0 if 1 fails)."""
    r = set(reachable(weights))
    n = 0
    while n + 1 in r:
        n += 1
    return n


def first_miss(weights):
    return run_length(weights) + 1


def show_way(t, left, right):
    l = ' + '.join(str(x) for x in [t] + left)
    r = ' + '.join(str(x) for x in right) or '(empty)'
    return f'{l} = {r}'


class Log:
    def __init__(self, name):
        self.name = name
        self.lines = []
        self.fails = 0

    def out(self, *a):
        s = ' '.join(str(x) for x in a)
        print(s)
        self.lines.append(s)

    def ok(self, cond, msg):
        if not cond:
            self.fails += 1
        self.out(('PASS ' if cond else 'FAIL ') + msg)
        return cond

    def save(self):
        self.out(f'-- {self.fails} FAIL line(s)')
        with open(os.path.join(HERE, self.name), 'w') as f:
            f.write('\n'.join(self.lines) + '\n')
