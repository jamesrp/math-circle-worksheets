"""Enumerate shapes made of halves (right isosceles triangles with unit legs) on the
square dot lattice, and compute outline dots B and inside dots I directly from the
eight 45-degree sectors around each dot (Pick's rule is not assumed).

A shape is a frozenset of quarters (x, y, d): the four triangles cut from cell
[x,x+1]x[y,y+1] by both diagonals; d in 'SENW' names the side that is the base.
A half is two adjacent quarters of one cell: SW, SE, NE, NW.
"""
from collections import defaultdict
import itertools, json, sys

HALVES = ['SW', 'SE', 'NE', 'NW']
OPP_HALF = {'SW': 'NE', 'NE': 'SW', 'SE': 'NW', 'NW': 'SE'}
ACROSS = {'S': (0, -1, 'N'), 'N': (0, 1, 'S'), 'E': (1, 0, 'W'), 'W': (-1, 0, 'E')}


def half_quarters(x, y, h):
    return [(x, y, h[0]), (x, y, h[1])]


def centroid6(q):
    x, y, d = q
    return {'S': (6*x+3, 6*y+1), 'N': (6*x+3, 6*y+5),
            'W': (6*x+1, 6*y+3), 'E': (6*x+5, 6*y+3)}[d]


def from_centroid6(a, b):
    x, y = a // 6, b // 6
    ra, rb = a - 6*x, b - 6*y
    d = {(3, 1): 'S', (3, 5): 'N', (1, 3): 'W', (5, 3): 'E'}[(ra, rb)]
    return (x, y, d)


SYMS = [lambda a, b: (a, b), lambda a, b: (-b, a), lambda a, b: (-a, -b), lambda a, b: (b, -a),
        lambda a, b: (-a, b), lambda a, b: (b, a), lambda a, b: (a, -b), lambda a, b: (-b, -a)]


def normalize(qs):
    qs = list(qs)
    mx = min(q[0] for q in qs)
    my = min(q[1] for q in qs)
    return tuple(sorted((x-mx, y-my, d) for x, y, d in qs))


def transform(qs, s):
    out = []
    for q in qs:
        a, b = centroid6(q)
        a2, b2 = s(a, b)
        out.append(from_centroid6(a2, b2))
    return out


def canon(qs, flips=True):
    syms = SYMS if flips else SYMS[:4]
    return min(normalize(transform(qs, s)) for s in syms)


def cells(qs):
    c = defaultdict(set)
    for x, y, d in qs:
        c[(x, y)].add(d)
    return c


def sectors(qs, X, Y):
    S = set(qs)
    seq = [(X, Y, 'S'), (X, Y, 'W'), (X-1, Y, 'E'), (X-1, Y, 'S'),
           (X-1, Y-1, 'N'), (X-1, Y-1, 'E'), (X, Y-1, 'W'), (X, Y-1, 'N')]
    return [q in S for q in seq]


def dot_status(qs):
    """Return (B, I, pinch, inside_dots, outline_dots)."""
    xs = [q[0] for q in qs]; ys = [q[1] for q in qs]
    B = I = 0
    pinch = False
    ins, outl = [], []
    for X in range(min(xs), max(xs)+2):
        for Y in range(min(ys), max(ys)+2):
            s = sectors(qs, X, Y)
            c = sum(s)
            if c == 8:
                I += 1; ins.append((X, Y))
            elif c > 0:
                B += 1; outl.append((X, Y))
                runs = sum(1 for i in range(8) if s[i] and not s[i-1])
                if runs != 1:
                    pinch = True
    return B, I, pinch, ins, outl


def has_hole(qs):
    S = set(qs)
    xs = [q[0] for q in qs]; ys = [q[1] for q in qs]
    x0, x1, y0, y1 = min(xs)-1, max(xs)+1, min(ys)-1, max(ys)+1
    allq = {(x, y, d) for x in range(x0, x1+1) for y in range(y0, y1+1) for d in 'SENW'}
    free = allq - S
    inner = {'S': 'EW', 'E': 'SN', 'N': 'EW', 'W': 'SN'}
    start = (x0, y0, 'S')
    seen = {start}; stack = [start]
    while stack:
        x, y, d = stack.pop()
        nb = [(x, y, e) for e in inner[d]]
        dx, dy, e = ACROSS[d]
        nb.append((x+dx, y+dy, e))
        for n in nb:
            if n in free and n not in seen:
                seen.add(n); stack.append(n)
    return len(seen) != len(free)


def can_add(S, x, y, h):
    qs = half_quarters(x, y, h)
    if any(q in S for q in qs):
        return False
    # hypotenuse
    if all(q in S for q in half_quarters(x, y, OPP_HALF[h])):
        return True
    for (cx, cy, d) in qs:
        dx, dy, e = ACROSS[d]
        if (cx+dx, cy+dy, e) in S:
            return True
    return False


def children(shape):
    S = set(shape)
    xs = [q[0] for q in S]; ys = [q[1] for q in S]
    for x in range(min(xs)-1, max(xs)+2):
        for y in range(min(ys)-1, max(ys)+2):
            for h in HALVES:
                if can_add(S, x, y, h):
                    yield frozenset(S | set(half_quarters(x, y, h)))


def enumerate_shapes(nmax):
    gens = {1: {canon(half_quarters(0, 0, 'SW'))}}
    for n in range(2, nmax+1):
        nxt = set()
        for c in gens[n-1]:
            for ch in children(c):
                nxt.add(canon(ch))
        gens[n] = nxt
    return gens


def pieces(qs):
    c = cells(qs)
    full = sum(1 for v in c.values() if len(v) == 4)
    half = sum(1 for v in c.values() if len(v) == 2)
    return full, half


def bbox(qs):
    xs = [q[0] for q in qs]; ys = [q[1] for q in qs]
    return (max(xs)-min(xs)+1, max(ys)-min(ys)+1)


def vertices_outline(qs):
    return dot_status(qs)[4]


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    gens = enumerate_shapes(N)
    total_allowed = 0
    for n in range(1, N+1):
        shapes = gens[n]
        allowed = []
        for s in shapes:
            B, I, pinch, _, _ = dot_status(s)
            if pinch or has_hole(s):
                continue
            allowed.append(s)
            assert B + 2*I == n + 2, (s, B, I)
        total_allowed += len(allowed)
        stats = defaultdict(int)
        for s in allowed:
            B, I, *_ = dot_status(s)
            stats[(B, I)] += 1
        print(n, 'polyaboloes', len(shapes), 'allowed', len(allowed), dict(stats))
    print('total allowed', total_allowed)
