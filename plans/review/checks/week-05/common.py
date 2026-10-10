"""Shared helpers for the Week 5 (Tower cities) math check.

Written independently of the packet's own towers.py / check.py.  The repository is
found from this file's location (walk up until a folder holds lowell-math-circle-year-2),
so the scripts run both from the run folder and from plans/review/checks/week-05/.
"""
from itertools import permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent


def repo_root():
    for up in [HERE, *HERE.parents]:
        if (up / "lowell-math-circle-year-2").is_dir():
            return up
    raise SystemExit("repository not found")


REPO = repo_root()
WEEK = REPO / "lowell-math-circle-year-2" / "week-05"
PDF = {
    "K": WEEK / "week-05-k-1.pdf",
    "M": WEEK / "week-05-grades-2-3.pdf",
    "U": WEEK / "week-05-grades-4-5.pdf",
    "G": WEEK / "week-05-facilitator.pdf",
    "RV": WEEK / "week-05-return-visit.pdf",
    "RVG": WEEK / "week-05-return-visit-facilitator.pdf",
}


def seen(row):
    """Number of towers seen looking along `row` from its first entry:
    a tower is seen when it is taller than every tower in front of it."""
    best = 0
    count = 0
    for h in row:
        if h > best:
            count += 1
            best = h
    return count


def views(row):
    row = tuple(row)
    return seen(row), seen(row[::-1])


def latin_squares(n):
    """All n-by-n Latin squares on 1..n, by plain backtracking over cells."""
    out = []
    grid = [[0] * n for _ in range(n)]

    def rec(k):
        if k == n * n:
            out.append(tuple(tuple(r) for r in grid))
            return
        r, c = divmod(k, n)
        used = set(grid[r][:c]) | {grid[i][c] for i in range(r)}
        for v in range(1, n + 1):
            if v not in used:
                grid[r][c] = v
                rec(k + 1)
        grid[r][c] = 0

    rec(0)
    return out


def count_latin(n):
    """Count n-by-n Latin squares (row-by-row backtracking with bitmasks)."""
    full = (1 << n) - 1
    rows = list(permutations(range(n)))
    cnt = 0

    def rec(r, colmask):
        nonlocal cnt
        if r == n:
            cnt += 1
            return
        for p in rows:
            ok = True
            for c in range(n):
                if colmask[c] >> p[c] & 1:
                    ok = False
                    break
            if ok:
                rec(r + 1, [colmask[c] | (1 << p[c]) for c in range(n)])

    rec(0, [0] * n)
    return cnt


# Edge places: ('T', c) above column c, ('B', c) below column c,
# ('L', r) left of row r, ('R', r) right of row r; rows/cols numbered from 1.
def edge_numbers(sq):
    n = len(sq)
    d = {}
    for c in range(n):
        col = [sq[r][c] for r in range(n)]
        d[("T", c + 1)] = seen(col)
        d[("B", c + 1)] = seen(col[::-1])
    for r in range(n):
        d[("L", r + 1)] = seen(sq[r])
        d[("R", r + 1)] = seen(sq[r][::-1])
    return d


def places(n):
    return [(s, i) for s in "TBLR" for i in range(1, n + 1)]


def fits(sq_edges, clues):
    return all(sq_edges[k] == v for k, v in clues.items())


def name(place):
    s, i = place
    return {"T": f"above column {i}", "B": f"below column {i}",
            "L": f"left of row {i}", "R": f"right of row {i}"}[s]


def rowstr(sq):
    return "/".join("".join(map(str, r)) for r in sq)
