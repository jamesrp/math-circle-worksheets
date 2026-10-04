"""
Single source of truth for every board used in the design.
Each board is a set of small triangles (see tri.py for coordinates).
"""
import tri
import lozenge as L

UP, DN = tri.UP, tri.DN


def scale(cells, k):
    out = set()
    for t in cells:
        cs = [(c[0] * k, c[1] * k) for c in tri.corners(t)]
        out |= tri.region_from_lattice_polygon(cs)
    return out


def strip(n):
    """One row of n small triangles, starting with an up-triangle at the left."""
    cells = []
    for k in range(n):
        cells.append((k // 2, 0, UP if k % 2 == 0 else DN))
    return set(cells)


TRI = {n: tri.triangle_region(n) for n in range(1, 8)}
HEX = lambda a, b, c: tri.hexagon_region(a, b, c)

BIG_GREEN = scale(tri.GREEN, 2)    # = triangle with 2 on each side
BIG_BLUE = scale(tri.BLUE, 2)      # rhombus with 2 on each side
BIG_RED = scale(tri.RED, 2)        # trapezoid, bottom 4, top 2, slant sides 2
BIG_YELLOW = scale(tri.YELLOW, 2)  # regular hexagon with 2 on each side
BIG_PURPLE = scale(tri.PURPLE, 2)  # chevron at double size

# ---- grades 2-3, problem 3: big hexagon (2,2,2) with two small triangles removed ----
H222 = HEX(2, 2, 2)
LEFT_CORNER_UP = (-2, 2, UP)     # upper half of the left corner
LEFT_CORNER_DN = (-2, 1, DN)     # lower half of the left corner
RIGHT_CORNER_UP = (1, 2, UP)     # upper half of the right corner
RIGHT_CORNER_DN = (1, 1, DN)     # lower half of the right corner
CENTER_SIX = tri.around_point((0, 2))   # counterclockwise, starting with the up-triangle just right of center, above the middle line
UPPER_RIGHT_INNER_DN = (0, 2, DN)   # interior down-triangle, centroid (2.00, 2.31)
LOWER_LEFT_INNER_UP = (-1, 1, UP)    # interior up-triangle, centroid (0.00, 1.15): 180-degree image of the one above
UPPER_LEFT_INNER_DN = (-2, 2, DN)    # interior down-triangle, centroid (0.00, 2.31): mirror image (left-right) of the first
MUT = {
    'a': {LEFT_CORNER_UP, RIGHT_CORNER_DN},              # point-symmetric pair: one up, one down
    'b': {LEFT_CORNER_UP, RIGHT_CORNER_UP},              # mirror pair: two ups
    'c': {UPPER_RIGHT_INNER_DN, LOWER_LEFT_INNER_UP},    # point-symmetric pair: one up, one down
    'd': {UPPER_RIGHT_INNER_DN, UPPER_LEFT_INNER_DN},    # mirror pair: two downs
}

# ---- grades 2-3, problem 6: "hourglass" boards: up-triangle side 3 + down-triangle side 3 ----
HOURGLASS_NECK2 = TRI[3] | tri.down_triangle_region(3, (0, 1))
HOURGLASS_NECK1 = TRI[3] | tri.down_triangle_region(3, (0, 2))

# ---- grades 2-3, problem 7 answer: triangle side 3 minus a corner blue ----
SMALLEST_3GAP = TRI[3] - {(2, 0, UP), (1, 0, DN)}


def boards():
    B = {}
    # K-1
    B['K1-P1a'] = HEX(1, 1, 1)
    B['K1-P1b'] = BIG_GREEN
    B['K1-P1c'] = BIG_BLUE
    B['K1-P1d'] = BIG_RED
    B['K1-P2a'] = TRI[2]
    B['K1-P2b'] = TRI[3]
    B['K1-P2c'] = TRI[4]
    B['K1-P3a'] = HEX(1, 1, 1)
    B['K1-P3b'] = HEX(2, 1, 1)
    B['K1-P3c'] = HEX(3, 1, 1)
    B['K1-P4a'] = TRI[3]
    B['K1-P4b'] = H222
    B['K1-P4c'] = TRI[4]
    B['K1-P5a'] = BIG_GREEN
    B['K1-P5b'] = BIG_RED
    B['K1-P5c'] = BIG_YELLOW
    B['K1-P5d'] = BIG_PURPLE
    B['K1-P6a'] = HEX(1, 1, 1)
    B['K1-P6b'] = strip(8)
    B['K1-P6c'] = strip(10)
    # 2-3
    B['23-P1a'] = H222
    B['23-P1b'] = TRI[3]
    B['23-P1c'] = TRI[4]
    B['23-P1d'] = BIG_PURPLE
    B['23-P2a'] = TRI[3]
    B['23-P2b'] = TRI[4]
    B['23-P2c'] = TRI[5]
    for k, holes in MUT.items():
        B['23-P3' + k] = H222 - holes
    B['23-P4'] = TRI[7]
    B['23-P5a'] = TRI[3]
    B['23-P5b'] = TRI[4]
    B['23-P5c'] = TRI[6]
    B['23-P6a'] = HOURGLASS_NECK2
    B['23-P6b'] = HOURGLASS_NECK1
    # 4-5
    B['45-P1a'] = HEX(1, 1, 1)
    B['45-P1b'] = HEX(1, 2, 1)
    B['45-P1c'] = HEX(1, 2, 2)
    B['45-P4a'] = HEX(1, 3, 2)
    B['45-P4b'] = HEX(1, 3, 3)
    B['45-P4c'] = HEX(1, 4, 4)
    B['45-P5'] = H222
    return B


HOLES = {'23-P3' + k: v for k, v in MUT.items()}
HOLE_BASE = {'23-P3' + k: H222 for k in MUT}


# ---- grades 4-5: named tilings of the (2,2,2) hexagon by their two chain words ----
def tiling_by_words(a, b, c, words):
    R, ts = L.tilings(a, b, c)
    for t in ts:
        if L.ribbons(t, a, b, c) == tuple(words):
            return t
    raise KeyError(words)


P5_PAIRS = {
    'a': (('RLLR', 'RLRL'), ('LRLR', 'LRRL')),
    'b': (('RLRL', 'RRLL'), ('LLRR', 'LRLR')),
    'c': (('RRLL', 'RRLL'), ('LLRR', 'LLRR')),
}
P6_START = ('LRLR', 'RLRL')
