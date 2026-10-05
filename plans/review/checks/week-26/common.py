"""Shared helpers for the Week 26 math check (polyomino perimeter and shared edges).

Written independently of the packet's own builders and checkers.  Nothing here
imports from lowell-math-circle-year-2/source/.

Cells are (x, y) pairs with x = column (to the right) and y = row (downward),
matching the page orientation of the PDFs.
"""
import os
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))


def find_root():
    # Committed copy lives in plans/review/checks/week-26/: four folders up.
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')):
        return cand
    # Fallback for the scratch run folder (tmp/review-runs/week-26/).
    d = HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository root not found')


ROOT = find_root()
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-26')
PT_MM = 25.4 / 72

N4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
N8 = N4 + ((1, 1), (1, -1), (-1, 1), (-1, -1))


class Log:
    def __init__(self):
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

    def save(self, path):
        self.out(f'== {self.fails} FAIL line(s)')
        with open(path, 'w') as f:
            f.write('\n'.join(self.lines) + '\n')


# ------------------------------------------------------------- basic counts

def perimeter(cells):
    """Exposed unit edges, counted directly side by side (hole edges included)."""
    s = set(cells)
    return sum((x + dx, y + dy) not in s for x, y in s for dx, dy in N4)


def shared(cells):
    """Number of full shared sides (each meeting counted once)."""
    s = set(cells)
    return sum((x + 1, y) in s for x, y in s) + sum((x, y + 1) in s for x, y in s)


def connected(cells):
    s = set(cells)
    if not s:
        return False
    start = next(iter(s))
    seen = {start}
    todo = [start]
    while todo:
        x, y = todo.pop()
        for dx, dy in N4:
            q = (x + dx, y + dy)
            if q in s and q not in seen:
                seen.add(q)
                todo.append(q)
    return seen == s


def rows_cols(cells):
    return len({y for _, y in cells}), len({x for x, _ in cells})


def bbox(cells):
    xs = [x for x, _ in cells]
    ys = [y for _, y in cells]
    return max(xs) - min(xs) + 1, max(ys) - min(ys) + 1  # width, height


def intervals(cells):
    """Total number of maximal runs in rows plus in columns."""
    s = set(cells)
    runs = 0
    for x, y in s:
        if (x - 1, y) not in s:
            runs += 1
        if (x, y - 1) not in s:
            runs += 1
    return runs


def has_block(cells):
    s = set(cells)
    return any({(x + 1, y), (x, y + 1), (x + 1, y + 1)} <= s for x, y in s)


def longest_run(cells):
    s = set(cells)
    best = 0
    for x, y in s:
        if (x - 1, y) not in s:
            k = 0
            while (x + k, y) in s:
                k += 1
            best = max(best, k)
        if (x, y - 1) not in s:
            k = 0
            while (x, y + k) in s:
                k += 1
            best = max(best, k)
    return best


def holes(cells, eight=False):
    """Bounded components of empty cells.

    eight=False: empty cells connect only through shared sides.  This is the
    complement of the union of closed squares, so a diagonal tile contact seals.
    eight=True: empty cells also connect through corners (a diagonal contact
    leaks), i.e. the stricter 'holes need a side-sealed ring' convention.
    """
    s = set(cells)
    xs = [x for x, _ in s]
    ys = [y for _, y in s]
    x0, x1, y0, y1 = min(xs) - 1, max(xs) + 1, min(ys) - 1, max(ys) + 1
    nb = N8 if eight else N4
    empty = {(x, y) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1)} - s
    seen = set()
    count = 0
    for e in empty:
        if e in seen:
            continue
        comp = {e}
        todo = [e]
        seen.add(e)
        border = False
        while todo:
            x, y = todo.pop()
            if x in (x0, x1) or y in (y0, y1):
                border = True
            for dx, dy in nb:
                q = (x + dx, y + dy)
                if q in empty and q not in seen:
                    seen.add(q)
                    comp.add(q)
                    todo.append(q)
        if not border:
            count += 1
    return count


def corner_counts(cells):
    """(convex C, concave R, pinch vertices) over all lattice vertices."""
    s = set(cells)
    verts = {(x + a, y + b) for x, y in s for a in (0, 1) for b in (0, 1)}
    C = R = pinch = 0
    for vx, vy in verts:
        around = [(vx - 1, vy - 1), (vx, vy - 1), (vx - 1, vy), (vx, vy)]
        occ = [q in s for q in around]
        k = sum(occ)
        if k == 1:
            C += 1
        elif k == 3:
            R += 1
        elif k == 2 and occ[0] == occ[3]:
            pinch += 1
    return C, R, pinch


# ------------------------------------------------------------- shape classes

def norm(cells):
    mx = min(x for x, _ in cells)
    my = min(y for _, y in cells)
    return tuple(sorted((x - mx, y - my) for x, y in cells))


SYMS = [lambda x, y: (x, y), lambda x, y: (-x, y), lambda x, y: (x, -y),
        lambda x, y: (-x, -y), lambda x, y: (y, x), lambda x, y: (-y, x),
        lambda x, y: (y, -x), lambda x, y: (-y, -x)]


def canon(cells):
    """Free (turns and flips) canonical form."""
    return min(norm([f(x, y) for x, y in cells]) for f in SYMS)


def fixed_polyominoes(nmax):
    """Dict n -> set of fixed (translation-normalized) polyominoes, n <= nmax."""
    out = {1: {((0, 0),)}}
    for n in range(2, nmax + 1):
        nxt = set()
        for q in out[n - 1]:
            s = set(q)
            for x, y in q:
                for dx, dy in N4:
                    p = (x + dx, y + dy)
                    if p not in s:
                        nxt.add(norm(s | {p}))
        out[n] = nxt
    return out


def free_polyominoes(fixed):
    return {n: {canon(q) for q in v} for n, v in fixed.items()}


def neighbors_empty(cells):
    s = set(cells)
    return {(x + dx, y + dy) for x, y in s for dx, dy in N4} - s


def show(cells):
    w, h = bbox(cells)
    c = norm(cells)
    s = set(c)
    return '/'.join(''.join('#' if (x, y) in s else '.' for x in range(w)) for y in range(h))


def from_rows(rows, left_aligned=True):
    return [(x, y) for y, k in enumerate(rows) for x in range(k)]


# ------------------------------------------------------------- enumeration

def redelmeier(nmax, callback):
    """Call callback(cells) once for every fixed polyomino with <= nmax cells
    (Redelmeier's method; each fixed polyomino is produced exactly once)."""
    poly = []
    seen = {(0, 0)}

    def ok(c):
        return c[1] > 0 or (c[1] == 0 and c[0] >= 0)

    def rec(untried):
        untried = list(untried)
        while untried:
            c = untried.pop()
            poly.append(c)
            callback(poly)
            if len(poly) < nmax:
                new = []
                for dx, dy in N4:
                    nb = (c[0] + dx, c[1] + dy)
                    if ok(nb) and nb not in seen:
                        new.append(nb)
                for nb in new:
                    seen.add(nb)
                rec(untried + new)
                for nb in new:
                    seen.discard(nb)
            poly.pop()
    rec([(0, 0)])


def box_subsets(w, h, n=None):
    """All connected subsets of a w-by-h box that touch every row and column
    of the box (so the box is the bounding box), optionally with n cells."""
    from itertools import combinations
    cells = [(x, y) for y in range(h) for x in range(w)]
    if n is not None:
        for comb in combinations(cells, n):
            if len({x for x, _ in comb}) == w and len({y for _, y in comb}) == h \
                    and connected(comb):
                yield comb
        return
    N = w * h
    for mask in range(1, 1 << N):
        comb = [cells[i] for i in range(N) if mask >> i & 1]
        if len({x for x, _ in comb}) == w and len({y for _, y in comb}) == h \
                and connected(comb):
            yield comb


def load_extracted(path):
    import json
    X = json.load(open(path))

    def fix(o):
        if isinstance(o, dict):
            return {k: ([tuple(c) for c in v] if k in ('cells', 'added') else fix(v)) for k, v in o.items()}
        if isinstance(o, list):
            return [fix(v) for v in o]
        return o
    return fix(X)
