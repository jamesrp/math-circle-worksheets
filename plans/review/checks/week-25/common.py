"""Shared helpers for the Week 25 math check (row and column shadows).

Written independently of the packet's own builders and checkers.  Nothing here
imports from lowell-math-circle-year-2/source/.
"""
import os
from itertools import combinations, product
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))


def find_root():
    # Committed copy lives in plans/review/checks/week-25/: four folders up.
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')):
        return cand
    # Fallback for the scratch run folder (tmp/review-runs/week-25/).
    d = HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository root not found')


ROOT = find_root()
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-25')


# ---------------------------------------------------------------- pictures
# A picture is a tuple of row strings, e.g. ('110', '001').

def parse(s):
    return tuple(s.split('/'))


def fmt(p):
    return '/'.join(p)


def margins(p):
    rows = tuple(r.count('1') for r in p)
    cols = tuple(sum(r[j] == '1' for r in p) for j in range(len(p[0])))
    return rows, cols


def solutions(rows, cols):
    """All 0/1 pictures with the given row and column counts (row-subset search)."""
    c = len(cols)
    out = []

    def rec(i, rem, acc):
        if i == len(rows):
            if all(x == 0 for x in rem):
                out.append(tuple(acc))
            return
        for S in combinations(range(c), rows[i]):
            if all(rem[j] > 0 for j in S):
                nrem = list(rem)
                for j in S:
                    nrem[j] -= 1
                rec(i + 1, nrem, acc + [''.join('1' if j in S else '0' for j in range(c))])
    rec(0, list(cols), [])
    return out


def switches(p):
    """Every legal switch: (row i, row k, col j, col l, result) with
    (i,j),(k,l) occupied and (i,l),(k,j) empty."""
    r, c = len(p), len(p[0])
    out = []
    for i, k in combinations(range(r), 2):
        for j in range(c):
            for l in range(c):
                if j == l:
                    continue
                if p[i][j] == '1' and p[k][l] == '1' and p[i][l] == '0' and p[k][j] == '0':
                    q = [list(x) for x in p]
                    q[i][j], q[k][l], q[i][l], q[k][j] = '0', '0', '1', '1'
                    out.append((i, k, j, l, tuple(''.join(x) for x in q)))
    return out


def bfs(start):
    dist = {start: 0}
    dq = deque([start])
    while dq:
        x = dq.popleft()
        for *_, y in switches(x):
            if y not in dist:
                dist[y] = dist[x] + 1
                dq.append(y)
    return dist


def distance(a, b):
    return bfs(a).get(b)


def all_pictures(r, c, k=None):
    for bits in product('01', repeat=r * c):
        if k is not None and bits.count('1') != k:
            continue
        yield tuple(''.join(bits[i * c:(i + 1) * c]) for i in range(r))


def cell_name(i, j):
    return 'ABCDEF'[i] + str(j + 1)
