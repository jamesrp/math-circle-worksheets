"""Board shapes used in the three packets."""
from tri import *


def rot_about(tris, c, k=1):
    """rotate triangle set by k*60 degrees about lattice vertex c"""
    out = set(tris)
    for _ in range(k):
        out = {identify([(rot60((v[0] - c[0], v[1] - c[1]))[0] + c[0],
                          rot60((v[0] - c[0], v[1] - c[1]))[1] + c[1]) for v in verts(t)]) for t in out}
    return frozenset(out)


def poly_region(*pts):
    return region_from_lattice_poly(list(pts))


# ---- grades 2-3, problem 1 boards
star = big_triangle(3) | poly_region((-1, 2), (2, 2), (2, -1))
trap2 = poly_region((0, 0), (4, 0), (2, 2), (0, 2))          # 2x red trapezoid
chev2 = frozenset(('%s' % k, 2 * i + a, 2 * j + b) for (k, i, j) in [])  # placeholder


def scale2(tris):
    """scale a set of triangles by 2 about the origin"""
    out = set()
    for (k, i, j) in tris:
        if k == 'U':
            # big up triangle with corners (2i,2j),(2i+2,2j),(2i,2j+2)
            out |= big_triangle(2, 2 * i, 2 * j)
        else:
            # big down triangle with corners (2i+2,2j),(2i+2,2j+2),(2i,2j+2)
            out |= {D(2 * i + 1, 2 * j), U(2 * i + 1, 2 * j + 1), D(2 * i, 2 * j + 1), D(2 * i + 1, 2 * j + 1)}
    return frozenset(out)


chev2 = scale2(PIECES['P'])
boat = poly_region((0, 0), (3, 0), (3, 2), (-2, 2))
_hexc = hex_around(2, 2)
_trap = frozenset([U(2, 0), D(2, 0), U(3, 0)])
pinwheel = _hexc | _trap | rot_about(_trap, (2, 2), 2) | rot_about(_trap, (2, 2), 4)

# ---- grades 2-3, hexagon with holes
HEX2, HEX2POLY = hexagon(2, 2, 2)

# ---- grades 2-3, corridor board (balanced, not coverable)
upT2 = big_triangle(2)                       # U00 D00 U10 U01 ; right corner U(1,0)
corridor = frozenset([D(1, 0), U(2, 0), D(2, 0), U(3, 0)])
# down T2 whose left corner D touches U(3,0) through edge (4,0)-(4,1)? find by search below

def inv_T2(a, b):
    return frozenset([D(a, b + 1), U(a + 1, b + 1), D(a + 1, b + 1), D(a + 1, b)])

corridor = frozenset([D(1, 0), U(2, 0), D(2, 0), U(3, 0), D(3, 0), U(4, 0)])
dumbbell = upT2 | corridor | inv_T2(3, 0)
