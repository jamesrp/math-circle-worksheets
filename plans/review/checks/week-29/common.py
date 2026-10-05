"""Shared helpers for the Week 29 math check.

The repository is found from this file's location: four folders up from
plans/review/checks/week-29/ (its committed home).  When run from another
folder (such as tmp/review-runs/week-29/), we walk upward until we find the
folder that holds lowell-math-circle-year-2/.
"""
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None  # four folders up from week-29/
    if cand and (cand / 'lowell-math-circle-year-2').is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):
        if (p / 'lowell-math-circle-year-2').is_dir() and (p / 'AGENTS.md').is_file():
            return p
    sys.exit('cannot find repository from ' + str(HERE))


REPO = find_repo()
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-29'
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-29'
BONUS_SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-29-bonus'
PDFS = {
    'k-1': WEEK / 'week-29-k-1.pdf',
    'grades-2-3': WEEK / 'week-29-grades-2-3.pdf',
    'grades-4-5': WEEK / 'week-29-grades-4-5.pdf',
    'guide': WEEK / 'week-29-facilitator.pdf',
    'bonus': WEEK / 'week-29-bonus.pdf',
    'bonus-guide': WEEK / 'week-29-bonus-facilitator.pdf',
}
CM = 72 / 2.54  # points per centimetre


class Log:
    def __init__(self):
        self.n = 0
        self.fail = 0

    def check(self, ok, msg):
        self.n += 1
        if not ok:
            self.fail += 1
        print(('PASS ' if ok else 'FAIL ') + msg)
        return ok

    def info(self, msg):
        print('     ' + msg)

    def done(self):
        print(f'\n{self.n} checks, {self.fail} failures')


def reachable(rods, limit, stock=None):
    """Set of totals 0..limit buildable from the given rod lengths.
    stock: optional dict length -> max copies (finite box)."""
    if stock is None:
        ok = [False] * (limit + 1)
        ok[0] = True
        for n in range(1, limit + 1):
            ok[n] = any(n >= r and ok[n - r] for r in rods)
        return {n for n in range(limit + 1) if ok[n]}
    tots = {0}
    for r in rods:
        tots = {t + k * r for t in tots for k in range(stock[r] + 1)}
    return {t for t in tots if t <= limit}


def multisets(rods, n):
    """All count vectors (one count per rod length) with sum count*len == n."""
    rods = list(rods)
    out = []

    def rec(i, rem, acc):
        if i == len(rods) - 1:
            if rem % rods[i] == 0:
                out.append(tuple(acc + [rem // rods[i]]))
            return
        for k in range(rem // rods[i] + 1):
            rec(i + 1, rem - k * rods[i], acc + [k])
    rec(0, n, [])
    return out


def words(rods, n):
    """All ordered sequences of rod lengths totalling n."""
    if n == 0:
        return [()]
    out = []
    for r in rods:
        if r <= n:
            out += [w + (r,) for w in words(rods, n - r)]
    return out


def gaps(rods, upto):
    R = reachable(rods, upto)
    return [n for n in range(1, upto + 1) if n not in R]
