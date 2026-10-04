"""Blue-rhombus tilings of hexagons as cube pictures, flips, and red-trapezoid tilings."""
from collections import deque
import itertools
from math import atan2, degrees, cos, sin, radians
from tri import *


def unit_hex_at(x, y):
    return frozenset([('U', x, y), ('D', x - 1, y), ('U', x - 1, y), ('D', x - 1, y - 1),
                      ('U', x, y - 1), ('D', x, y - 1)])


def flip_neighbors(T, R):
    T = set(T)
    out = []
    pts = set()
    for t in R:
        pts.update(verts(t))
    for (x, y) in pts:
        H = unit_hex_at(x, y)
        if not H <= R:
            continue
        inside = [p for p in T if p <= H]
        if len(inside) == 3:
            for s in itertools.combinations(rhombi(H), 3):
                ss = set(s)
                if set().union(*ss) == set(H) and ss != set(inside):
                    out.append(frozenset((T - set(inside)) | ss))
    return out


def shade_class(p, rot=90):
    """'L' (lying flat: tops/floor), 'M' (left faces), 'D' (right faces) after rotating the
    picture by `rot` degrees.  Uses the rhombus's long diagonal."""
    t, u = list(p)
    vt, vu = set(verts(t)), set(verts(u))
    shared = vt & vu
    a = list(vt - shared)[0]
    b = list(vu - shared)[0]
    (ax, ay), (bx, by) = cart(a), cart(b)
    dx, dy = bx - ax, by - ay
    r = radians(rot)
    dx, dy = cos(r) * dx - sin(r) * dy, sin(r) * dx + cos(r) * dy
    ang = degrees(atan2(dy, dx)) % 180
    if ang < 15 or ang > 165:
        return 'L'
    if abs(ang - 120) < 15:
        return 'M'
    if abs(ang - 60) < 15:
        return 'D'
    raise ValueError(ang)


def rhombus_tilings(R):
    R = frozenset(R)
    return [frozenset(t) for t in tilings(R, rhombi(R))]


def flip_graph(R):
    R = frozenset(R)
    Ts = rhombus_tilings(R)
    G = {T: flip_neighbors(T, R) for T in Ts}
    return Ts, G


def bfs(G, s):
    d = {s: 0}
    q = deque([s])
    while q:
        u = q.popleft()
        for v in G[u]:
            if v not in d:
                d[v] = d[u] + 1
                q.append(v)
    return d


def empty_and_full(R, rot=90):
    """The two tilings with a single flip available; 'empty' has its flat (L) rhombi lowest."""
    Ts, G = flip_graph(R)
    frozen = [T for T in Ts if len(G[T]) == 1]
    assert len(frozen) == 2

    def mean_flat_y(T):
        ys = []
        r = radians(rot)
        for p in T:
            if shade_class(p, rot) == 'L':
                cx = sum(centroid(t)[0] for t in p) / 2
                cy = sum(centroid(t)[1] for t in p) / 2
                ys.append(sin(r) * cx + cos(r) * cy)
        return sum(ys) / len(ys)
    frozen.sort(key=mean_flat_y)
    return frozen[0], frozen[1], Ts, G
