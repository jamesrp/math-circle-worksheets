"""Independent lattice-visibility mathematics for the Week 31 check.

Everything here is computed by brute force over lattice points (no gcd is used
for the basic notions), so that the gcd rule printed in the packet can be
checked against it rather than assumed.
"""
from fractions import Fraction
from math import gcd


def between(P, T):
    """All lattice points strictly between P and T on segment PT (brute force)."""
    (px, py), (tx, ty) = P, T
    out = []
    for x in range(min(px, tx), max(px, tx) + 1):
        for y in range(min(py, ty), max(py, ty) + 1):
            if (x, y) in (P, T):
                continue
            # collinear and strictly between
            if (x - px) * (ty - py) - (y - py) * (tx - px) != 0:
                continue
            out.append((x, y))
    out.sort(key=lambda q: abs(q[0] - px) + abs(q[1] - py))
    return out


def visible(T, P=(0, 0)):
    return T != P and not between(P, T)


def first_point(T, P=(0, 0)):
    """First lattice point after P on ray PT (brute force)."""
    b = between(P, T)
    return b[0] if b else T


def hides(F, n, P=(0, 0)):
    """Dots of the 0..n square grid lying beyond F on the ray from P through F."""
    out = []
    for x in range(0, n + 1):
        for y in range(0, n + 1):
            if (x, y) in (P, F):
                continue
            if F in between(P, (x, y)):
                out.append((x, y))
    return out


def grid(n, m=None):
    m = n if m is None else m
    return [(x, y) for y in range(m + 1) for x in range(n + 1) if (x, y) != (0, 0)]


def same_ray_group(D, n, lo=0):
    """All dots (x, y) with lo <= x, y <= n on the ray from O through D, D included."""
    out = []
    for x in range(lo, n + 1):
        for y in range(lo, n + 1):
            if (x, y) == (0, 0):
                continue
            if x * D[1] - y * D[0] == 0 and x * D[0] + y * D[1] > 0:
                out.append((x, y))
    return sorted(out, key=lambda q: q[0] + q[1])


# ---------- triangles ----------

def area2(A, B, C):
    return abs((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]))


def classify_triangle(A, B, C, pts):
    """Return (side_dots, interior_dots) among pts (excluding corners)."""
    side, inside = [], []
    s = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    for P in pts:
        if P in (A, B, C):
            continue
        d = []
        for U, V in ((A, B), (B, C), (C, A)):
            d.append(((V[0] - U[0]) * (P[1] - U[1]) - (V[1] - U[1]) * (P[0] - U[0])) * (1 if s > 0 else -1))
        if min(d) < 0:
            continue
        if min(d) == 0:
            side.append(P)
        else:
            inside.append(P)
    return side, inside


def classify_triangle_float(A, B, C, pts, eps=1e-6):
    side, inside = [], []
    s = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    for P in pts:
        if any(abs(P[0] - Q[0]) < 0.05 and abs(P[1] - Q[1]) < 0.05 for Q in (A, B, C)):
            continue
        d = []
        for U, V in ((A, B), (B, C), (C, A)):
            L = ((V[0] - U[0]) ** 2 + (V[1] - U[1]) ** 2) ** .5
            d.append(((V[0] - U[0]) * (P[1] - U[1]) - (V[1] - U[1]) * (P[0] - U[0])) * (1 if s > 0 else -1) / L)
        if min(d) < -eps:
            continue
        if min(d) <= eps:
            side.append(P)
        else:
            inside.append(P)
    return side, inside


def shape_key(A, B, C):
    return tuple(sorted(((P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2) for P, Q in ((A, B), (B, C), (C, A))))


# ---------- direction cards (mediant insertion) ----------

def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def insertions_to_contain(targets, start=((1, 0), (0, 1)), max_depth=12):
    """Breadth-first search over ordered rows built by inserting neighbour sums;
    returns the fewest insertions after which every target is present, with one
    such row.  Rows are kept as tuples."""
    from collections import deque
    start = tuple(start)
    seen = {start}
    q = deque([(start, 0)])
    while q:
        row, k = q.popleft()
        if all(t in row for t in targets):
            return k, row
        if k >= max_depth:
            continue
        for i in range(len(row) - 1):
            u, v = row[i], row[i + 1]
            w = (u[0] + v[0], u[1] + v[1])
            # pruning: never build a card larger than the largest target coordinate
            if max(w) > max(max(t) for t in targets):
                continue
            nr = row[:i + 1] + (w,) + row[i + 1:]
            if nr not in seen:
                seen.add(nr)
                q.append((nr, k + 1))
    return None, None


def all_cards(depth):
    """Every card any row can contain after at most `depth` levels of insertion
    (the full binary insertion tree between (1,0) and (0,1))."""
    cards = set()

    def rec(u, v, d):
        if d == 0:
            return
        w = (u[0] + v[0], u[1] + v[1])
        cards.add((w, u, v))
        rec(u, w, d - 1)
        rec(w, v, d - 1)
    rec((1, 0), (0, 1), depth)
    return cards


def wedge_search(T):
    """The insertion procedure the bonus guide describes: keep the neighbour pair
    whose wedge contains T, insert the sum, keep the smaller wedge with T."""
    u, v = (1, 0), (0, 1)
    row = [u, v]
    steps = []
    while True:
        w = (u[0] + v[0], u[1] + v[1])
        i = row.index(u)
        row.insert(i + 1, w)
        steps.append(w)
        if w == T:
            return steps, row
        # which side of ray w is T on?  det(w, T) > 0 means T is anticlockwise (towards v)
        if det(w, T) > 0:
            u = w
        else:
            v = w
        if len(steps) > 100:
            return None, row
