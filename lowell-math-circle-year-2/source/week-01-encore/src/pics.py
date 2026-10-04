"""Named regions used in the packets (sets of small triangles)."""
from tri import *


def P(start, steps):
    return region_from_poly(path_poly(start, steps))


def tri_up(x, y, n):
    """Up-pointing triangle with n small edges per side, bottom-left vertex (x, y)."""
    return P((x, y), [(0, n), (2, n), (4, n)])


def tri_down(x, y, n):
    """Down-pointing triangle with n small edges per side, top-left vertex (x, y)."""
    return P((x, y), [(0, n), (4, n), (2, n)])


def trap(x, y, bottom, top):
    """Upright trapezoid: long side `bottom` at the bottom, short side `top`."""
    h = bottom - top
    return P((x, y), [(0, bottom), (2, h), (3, top), (4, h)])


def rhomb(n):
    return P((0, 0), [(0, n), (1, n), (3, n), (4, n)])


def hexR(a, b, c):
    return region_from_poly(hexagon(a, b, c))


def parR(a, b):
    return region_from_poly(parallelogram(a, b))


def triR(n):
    return tri_up(0, 0, n)


def outside_neighbors(R, pred):
    out = set()
    for t in R:
        for o in neighbors(t):
            if o not in R and pred(centroid(o)):
                out.add(o)
    return out


# K-1 picture outlines
STAR = tri_up(0, 0, 3) | tri_down(-1, 2, 3)                      # 12 small triangles
_body = hexR(2, 1, 1)
FISH = _body | outside_neighbors(_body, lambda c: c[0] < 0)       # 12 small triangles
BOAT = P((0, 0), [(0, 2), (1, 2), (3, 4), (5, 2)]) | tri_up(-1, 2, 2)  # 16 small triangles
HEX2 = hexR(2, 2, 2)                                             # 24 small triangles
