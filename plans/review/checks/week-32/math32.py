"""Independent mathematics for the Week 32 check (squares inside rectangles).

Nothing here imports or reads the packet's own checkers.  The biggest-square
rule is simulated literally on a cell grid and cross-checked against plain
repeated subtraction; tilings are found by exhaustive search.
"""
from functools import lru_cache
from itertools import product


# ------------------------------------------------------------ biggest-square rule

def greedy_cells(w, h):
    """Literal simulation on a w-by-h cell grid.

    At each step the uncovered cells must form one rectangle; cover the
    largest square that fits at its left (or top) end.  Returns the list of
    square sides in removal order and checks every remainder is a rectangle.
    """
    covered = [[False]*w for _ in range(h)]
    sides = []
    while True:
        cells = [(x, y) for y in range(h) for x in range(w) if not covered[y][x]]
        if not cells:
            return sides
        xs = [c[0] for c in cells]; ys = [c[1] for c in cells]
        x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
        rw, rh = x1 - x0 + 1, y1 - y0 + 1
        assert rw * rh == len(cells), 'remainder is not a rectangle'
        s = min(rw, rh)
        # largest square that fits: try every size, keep the biggest that fits at the end
        best = max(t for t in range(1, max(rw, rh) + 1) if t <= rw and t <= rh)
        assert best == s
        for y in range(y0, y0 + s):
            for x in range(x0, x0 + s):
                assert not covered[y][x]
                covered[y][x] = True
        sides.append(s)


def greedy_sub(a, b):
    """Repeated subtraction version (no division)."""
    out = []
    while a and b:
        if a < b:
            a, b = b, a
        out.append(b)
        a -= b
    return out


def greedy(a, b):
    g1 = greedy_cells(a, b)
    g2 = greedy_sub(a, b)
    assert g1 == g2, (a, b, g1, g2)
    return g1


def recipe(a, b):
    seq = greedy(a, b)
    out = []
    for s in seq:
        if out and out[-1][0] == s:
            out[-1][1] += 1
        else:
            out.append([s, 1])
    return [c for _, c in out]


def distinct_sizes(a, b):
    return len(set(greedy(a, b)))


def common_divisors(a, b):
    return [d for d in range(1, min(a, b) + 1) if a % d == 0 and b % d == 0]


def gcd_brute(a, b):
    return max(common_divisors(a, b))


# ------------------------------------------------------------ tilings by search

def equal_square_tiles(w, h, s):
    """Can identical s-by-s grid squares tile w-by-h?  First-empty-cell search."""
    grid = [[False]*w for _ in range(h)]

    def first():
        for y in range(h):
            for x in range(w):
                if not grid[y][x]:
                    return x, y
        return None

    def rec():
        f = first()
        if f is None:
            return True
        x, y = f
        if x + s > w or y + s > h:
            return False
        if any(grid[yy][xx] for yy in range(y, y+s) for xx in range(x, x+s)):
            return False
        for yy in range(y, y+s):
            for xx in range(x, x+s):
                grid[yy][xx] = True
        ok = rec()
        for yy in range(y, y+s):
            for xx in range(x, x+s):
                grid[yy][xx] = False
        return ok
    return rec()


def _search(w, h, sizes):
    """Exhaustive min-count square tiling of w-by-h with grid squares whose
    sides are in `sizes` (None = any).  Returns (min count or None, witness)."""
    full = (1 << (w*h)) - 1

    @lru_cache(maxsize=None)
    def best(mask):
        if mask == full:
            return (0, ())
        # first empty cell in row-major order
        i = 0
        while mask >> i & 1:
            i += 1
        x, y = i % w, i // w
        res = None
        maxs = min(w - x, h - y)
        for s in range(maxs, 0, -1):
            if sizes is not None and s not in sizes:
                continue
            m = 0; ok = True
            for yy in range(y, y+s):
                for xx in range(x, x+s):
                    bit = 1 << (yy*w + xx)
                    if mask & bit:
                        ok = False; break
                    m |= bit
                if not ok:
                    break
            if not ok:
                continue
            sub = best(mask | m)
            if sub is not None and (res is None or sub[0] + 1 < res[0]):
                res = (sub[0] + 1, ((x, y, s),) + sub[1])
        return res
    r = best(0)
    best.cache_clear()
    return (None, ()) if r is None else r


def min_squares(w, h, sizes=None):
    return _search(w, h, None if sizes is None else frozenset(sizes))


def count_tilings_by_size_multiset(w, h, k, sizes=None):
    """All multisets of k square sides that tile w-by-h (exhaustive)."""
    full = (1 << (w*h)) - 1
    found = set()

    def rec(mask, used):
        if len(used) > k:
            return
        if mask == full:
            if len(used) == k:
                found.add(tuple(sorted(used, reverse=True)))
            return
        i = 0
        while mask >> i & 1:
            i += 1
        x, y = i % w, i // w
        for s in range(min(w-x, h-y), 0, -1):
            if sizes is not None and s not in sizes:
                continue
            m = 0; ok = True
            for yy in range(y, y+s):
                for xx in range(x, x+s):
                    bit = 1 << (yy*w + xx)
                    if mask & bit:
                        ok = False
                    m |= bit
            if ok:
                rec(mask | m, used + [s])
    rec(0, [])
    return found


def rect_shapes_from_squares(n, s):
    """Rectangles (up to turning) that n identical s-by-s squares tile exactly."""
    area = n * s * s
    out = []
    for w in range(1, area + 1):
        if area % w:
            continue
        h = area // w
        if w > h:
            continue
        if equal_square_tiles(w, h, s):
            out.append((w, h))
    return out


def can_pack(W, H, rects):
    """Can the given rectangles (each may be turned) be drawn disjointly on a
    W-by-H grid with edges on grid lines?  Exhaustive."""
    rects = sorted(rects, key=lambda r: -r[0]*r[1])
    occ = [[False]*W for _ in range(H)]

    def rec(i):
        if i == len(rects):
            return True
        a, b = rects[i]
        for (w, h) in {(a, b), (b, a)}:
            for y in range(H - h + 1):
                for x in range(W - w + 1):
                    if any(occ[yy][xx] for yy in range(y, y+h) for xx in range(x, x+w)):
                        continue
                    for yy in range(y, y+h):
                        for xx in range(x, x+w):
                            occ[yy][xx] = True
                    if rec(i + 1):
                        return True
                    for yy in range(y, y+h):
                        for xx in range(x, x+w):
                            occ[yy][xx] = False
        return False
    return rec(0)


def cf_value(qs):
    """q1 + 1/(q2 + 1/(... + 1/qk)) as a reduced fraction (num, den)."""
    from fractions import Fraction
    v = Fraction(qs[-1])
    for q in reversed(qs[:-1]):
        v = q + 1 / v
    return v.numerator, v.denominator


def rebuild_from_recipe(qs):
    """The guide's backward reconstruction: start with a qk-by-1 strip, then
    each preceding count q turns (long s, short t) into (q*s + t, s)."""
    s, t = qs[-1], 1
    steps = [(s, t)]
    for q in reversed(qs[:-1]):
        s, t = q*s + t, s
        steps.append((s, t))
    return steps
