#!/usr/bin/env python3
"""Checks for the draft plans of weeks 196-201 (symmetry and number, third set).

Standard library only. Run: python3 plans/drafts/weeks-101-plus/check_symmetry_number_3.py
Every small number quoted in the week-196 ... week-201 drafts is asserted here.
"""

from itertools import permutations
from math import gcd, cos, sin, pi, sqrt, isclose


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


# ---------------------------------------------------------------- week 196
def apply_change(row, swaps):
    """swaps: list of 0-based positions p meaning 'swap places p and p+1'."""
    r = list(row)
    for p in swaps:
        r[p], r[p + 1] = r[p + 1], r[p]
    return tuple(r)


def all_changes(n):
    """Every nonempty set of disjoint neighbour swaps on n bells."""
    out = []

    def grow(start, chosen):
        if chosen:
            out.append(tuple(chosen))
        for p in range(start, n - 1):
            grow(p + 2, chosen + [p])

    grow(0, [])
    return out


def plain_hunt(n):
    cross = list(range(0, n - 1, 2))          # swap 12, 34, ...
    inner = list(range(1, n - 1, 2))          # swap 23, 45, ...
    rows = [tuple(range(1, n + 1))]
    k = 0
    while True:
        rows.append(apply_change(rows[-1], cross if k % 2 == 0 else inner))
        k += 1
        if rows[-1] == rows[0]:
            return rows


def sjt(n):
    """Steinhaus-Johnson-Trotter order of the permutations of 1..n."""
    if n == 1:
        return [(1,)]
    out = []
    for i, p in enumerate(sjt(n - 1)):
        spots = range(n - 1, -1, -1) if i % 2 == 0 else range(n)
        for s in spots:
            out.append(p[:s] + (n,) + p[s:])
    return out


def count_ham_cycles(vertices, nbrs):
    """Undirected Hamiltonian cycles (each counted once)."""
    start = vertices[0]
    n = len(vertices)
    count = 0
    seen = {start}

    def dfs(v, depth):
        nonlocal count
        if depth == n:
            if start in nbrs[v]:
                count += 1
            return
        for w in nbrs[v]:
            if w not in seen:
                seen.add(w)
                dfs(w, depth + 1)
                seen.discard(w)

    dfs(start, 1)
    return count // 2


def change_graph(n, changes):
    verts = list(permutations(range(1, n + 1)))
    nbrs = {v: {apply_change(v, c) for c in changes} for v in verts}
    return verts, nbrs


def parity(p):
    inv = sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])
    return inv % 2


def check_week_196():
    # Kinds of change: 2 on 3 bells, 4 on 4, 7 on 5.
    assert [len(all_changes(n)) for n in (3, 4, 5)] == [2, 4, 7]
    # Plain hunt returns after 2n changes, visiting 2n different rows.
    for n in (3, 4, 5, 6):
        rows = plain_hunt(n)
        assert len(rows) - 1 == 2 * n and len(set(rows)) == 2 * n
    # On 3 bells plain hunt rings all 6 orders; on 4 only 8 of 24, on 5 only 10 of 120.
    assert len(set(plain_hunt(3))) == 6
    ph4 = set(plain_hunt(4))
    assert ph4 == {(1, 2, 3, 4), (2, 1, 4, 3), (2, 4, 1, 3), (4, 2, 3, 1),
                   (4, 3, 2, 1), (3, 4, 1, 2), (3, 1, 4, 2), (1, 3, 2, 4)}
    # Plain Bob Minimus: x 14 x 14 x 14 x 12, three times: 24 different rows, then rounds.
    x, p14, p12 = [0, 2], [1], [2]
    lead = [x, p14, x, p14, x, p14, x, p12]
    rows = [(1, 2, 3, 4)]
    for _ in range(3):
        for c in lead:
            rows.append(apply_change(rows[-1], c))
    assert rows[-1] == rows[0] and len(set(rows[:-1])) == 24
    # Each lead of 8 rows is the lead head with the 8 plain-hunt shapes applied.
    hunt_shapes = []
    r = tuple(range(4))
    for c in lead[:-1]:
        hunt_shapes.append(r)
        r = apply_change(r, c)
    hunt_shapes.append(r)
    assert len(set(hunt_shapes)) == 8
    for j in range(3):
        head = rows[8 * j]
        assert set(rows[8 * j: 8 * j + 8]) == {tuple(head[i] for i in h) for h in hunt_shapes}
    # Bell 1 hunts (positions 1,2,3,4,4,3,2,1) in every lead; bells 2,3,4 take turns dodging.
    assert [rows[k].index(1) + 1 for k in range(8)] == [1, 2, 3, 4, 4, 3, 2, 1]
    # Steinhaus-Johnson-Trotter: all n! orders, consecutive rows (and last to first)
    # differ by one neighbour swap.
    for n in (3, 4, 5):
        order = sjt(n)
        assert len(set(order)) == len(order) == [1, 1, 2, 6, 24, 120][n]
        for a, b in zip(order, order[1:] + order[:1]):
            diff = [i for i in range(n) if a[i] != b[i]]
            assert len(diff) == 2 and diff[1] == diff[0] + 1
    assert sjt(3) == [(1, 2, 3), (1, 3, 2), (3, 1, 2), (3, 2, 1), (2, 3, 1), (2, 1, 3)]
    # Permutohedron of order 4: 24 corners, 36 edges.
    verts, nbrs = change_graph(4, [(0,), (1,), (2,)])
    assert len(verts) == 24 and sum(len(s) for s in nbrs.values()) // 2 == 36
    # Single swaps change parity, so rows alternate even and odd.
    for v in verts:
        for w in nbrs[v]:
            assert parity(v) != parity(w)
    # 3 bells: the only round trip through all 6 orders is plain hunt (one cycle).
    v3, n3 = change_graph(3, all_changes(3))
    assert count_ham_cycles(v3, n3) == 1
    # Counts of round trips through all 24 orders on 4 bells.
    # (each cycle counted once, whatever its start and direction).
    assert count_ham_cycles(verts, nbrs) == 44          # single neighbour swaps only
    v4, n4 = change_graph(4, all_changes(4))
    assert count_ham_cycles(v4, n4) == 5396             # any of the 4 kinds of change


# ---------------------------------------------------------------- week 197
def midpoint(n, i, apothem=1.0):
    a = 2 * pi * i / n
    return (apothem * cos(a), apothem * sin(a))


def hankin_line_hits(n, i, theta_deg):
    """Line through edge-midpoint M_i at contact angle theta (towards increasing i).
    Return the index j of another midpoint the line passes through, or None."""
    mx, my = midpoint(n, i)
    a = 2 * pi * i / n
    # edge direction at M_i (tangent, counterclockwise) and inward normal
    tx, ty = -sin(a), cos(a)
    nx, ny = -cos(a), -sin(a)
    t = theta_deg * pi / 180
    dx, dy = cos(t) * tx + sin(t) * nx, cos(t) * ty + sin(t) * ny
    for j in range(n):
        if j == i:
            continue
        px, py = midpoint(n, j)
        cross = (px - mx) * dy - (py - my) * dx
        if abs(cross) < 1e-9:
            return j
    return None


def star_pieces(n, k):
    seen, pieces = set(), 0
    for s in range(n):
        if s in seen:
            continue
        pieces += 1
        v = s
        while v not in seen:
            seen.add(v)
            v = (v + k) % n
    return pieces


def star_symmetries(n, k):
    edges = {frozenset((i, (i + k) % n)) for i in range(n)}
    count = 0
    for r in range(n):
        for flip in (False, True):
            f = (lambda v: (r - v) % n) if flip else (lambda v: (v + r) % n)
            if {frozenset(map(f, e)) for e in edges} == edges:
                count += 1
    return count


def grid_meeting(h, dx, dy):
    """Square cell [0, 2h]^2.  Ray from bottom midpoint (h, 0) with direction (-dx, dy)
    meets its mirror ray from the left midpoint (0, h) on the diagonal x = y."""
    # (h - t dx, t dy) on x = y  ->  t = h / (dx + dy)
    t = h / (dx + dy)
    return (h - t * dx, t * dy)


def segments_square_grid(h, dx, dy, span=3):
    """Hankin segments for the square grid of side 2h, rule direction (dx, dy)."""
    px, py = grid_meeting(h, dx, dy)
    base = []
    # in cell [0,2h]^2: each midpoint joins the two meeting points beside it
    corners_p = [(px, py), (2 * h - px, py), (2 * h - px, 2 * h - py), (px, 2 * h - py)]
    mids = [(h, 0), (2 * h, h), (h, 2 * h), (0, h)]
    for k, m in enumerate(mids):
        for q in (corners_p[k], corners_p[(k + 1) % 4]):
            base.append((m, q))
    segs = set()
    for a in range(-span, span + 1):
        for b in range(-span, span + 1):
            for (m, q) in base:
                p1 = (round(m[0] + 2 * h * a, 6), round(m[1] + 2 * h * b, 6))
                p2 = (round(q[0] + 2 * h * a, 6), round(q[1] + 2 * h * b, 6))
                segs.add(frozenset((p1, p2)))
    return segs


def transform_segs(segs, f, window):
    out = set()
    for s in segs:
        p1, p2 = tuple(s)
        q1, q2 = f(p1), f(p2)
        q1 = (round(q1[0], 6), round(q1[1], 6))
        q2 = (round(q2[0], 6), round(q2[1], 6))
        out.add(frozenset((q1, q2)))
    inside = lambda s: all(abs(c) <= window for p in s for c in p)
    return {s for s in out if inside(s)}


def check_week_197():
    # Hankin in a regular n-gon: contact angle 180k/n gives lines M_i M_{i+k},
    # the star polygon {n/k} on the edge midpoints.
    for n in (5, 6, 8, 10, 12):
        for k in range(1, (n + 1) // 2):
            for i in range(n):
                assert hankin_line_hits(n, i, 180 * k / n) == (i + k) % n
    # A contact angle not of that form hits no other midpoint in the octagon.
    assert hankin_line_hits(8, 0, 50) is None
    # {8/2} is two squares, {8/3} one star, {6/2} two triangles, {5/2} one star.
    assert [star_pieces(8, 2), star_pieces(8, 3), star_pieces(6, 2), star_pieces(5, 2)] == [2, 1, 2, 1]
    assert all(star_pieces(n, k) == gcd(n, k) for n in range(3, 13) for k in range(1, n))
    # A regular star has 2n symmetries (n turns, n mirrors).
    assert star_symmetries(8, 3) == 16 and star_symmetries(8, 2) == 16 and star_symmetries(6, 2) == 12
    # Dot-grid rules in a 6-by-6 cell (h = 3): "1 across, 2 up" meets at (2, 2),
    # "2 across, 1 up" at (1, 1), "1 across, 1 up" at (1.5, 1.5) on the line joining midpoints.
    assert grid_meeting(3, 1, 2) == (2, 2)
    assert grid_meeting(3, 2, 1) == (1, 1)
    assert grid_meeting(3, 1, 1) == (1.5, 1.5)
    # Every drawn segment has length sqrt(5) for both steep and shallow rules.
    assert isclose(sqrt((3 - 2) ** 2 + 2 ** 2), sqrt(5)) and isclose(sqrt((3 - 1) ** 2 + 1 ** 2), sqrt(5))
    # Steep rule: around a grid corner the 8-gon (2,2),(3,0),(2,-2),(0,-3),... is convex;
    # inside a cell the 8-gon (3,0),(4,2),(6,3),... is a four-pointed star (not convex).
    def convex(poly):
        signs = set()
        for i in range(len(poly)):
            a, b, c = poly[i], poly[(i + 1) % len(poly)], poly[(i + 2) % len(poly)]
            cr = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
            signs.add(cr > 0)
        return len(signs) == 1
    corner_steep = [(2, 2), (0, 3), (-2, 2), (-3, 0), (-2, -2), (0, -3), (2, -2), (3, 0)]
    cell_steep = [(3, 0), (4, 2), (6, 3), (4, 4), (3, 6), (2, 4), (0, 3), (2, 2)]
    assert convex(corner_steep) and not convex(cell_steep)
    # Shallow rule swaps them: the star sits round the grid corner.
    corner_shallow = [(1, 1), (0, 3), (-1, 1), (-3, 0), (-1, -1), (0, -3), (1, -1), (3, 0)]
    cell_shallow = [(3, 0), (5, 1), (6, 3), (5, 5), (3, 6), (1, 5), (0, 3), (1, 1)]
    assert not convex(corner_shallow) and convex(cell_shallow)
    # The whole pattern keeps quarter turns about a cell centre and a grid corner,
    # and mirrors, but not an eighth turn.
    for (dx, dy) in ((1, 2), (2, 1)):
        segs = segments_square_grid(3, dx, dy)
        W = 9
        ref = transform_segs(segs, lambda p: p, W)
        quarter_corner = transform_segs(segs, lambda p: (-p[1], p[0]), W)
        mirror = transform_segs(segs, lambda p: (-p[0], p[1]), W)
        diag = transform_segs(segs, lambda p: (p[1], p[0]), W)
        c = 1 / sqrt(2)
        eighth = transform_segs(segs, lambda p: (c * (p[0] - p[1]), c * (p[0] + p[1])), W)
        assert ref == quarter_corner == mirror == diag
        assert eighth != ref
        # quarter turn about the cell centre (3, 3)
        about = transform_segs(segs, lambda p: (6 - p[1], p[0]), W)
        assert about == ref
    # 4.8.8 tiling: an eighth turn about an octagon centre fixes that octagon but moves
    # the neighbouring octagon centre (L, 0) to (L/sqrt2, L/sqrt2), not a centre.
    L = 1 + sqrt(2)
    q = L / sqrt(2)
    assert not isclose(q / L, round(q / L))


# ---------------------------------------------------------------- week 198
def normalize(cells):
    mx = min(x for x, y in cells)
    my = min(y for x, y in cells)
    return frozenset((x - mx, y - my) for x, y in cells)


def orientations(cells):
    out = []
    c = list(cells)
    for _ in range(4):
        c = [(y, -x) for x, y in c]
        out.append(normalize(c))
        out.append(normalize([(-x, y) for x, y in c]))
    return out


def free_polyominoes(n):
    shapes = {normalize([(0, 0)])}
    for _ in range(n - 1):
        new = set()
        for s in shapes:
            for (x, y) in s:
                for (a, b) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if (x + a, y + b) not in s:
                        t = normalize(set(s) | {(x + a, y + b)})
                        new.add(min(orientations(t), key=lambda z: sorted(z)))
        shapes = new
    return shapes


def lattice_tiles(cells):
    """Tiles by translations of a lattice (Hermite normal form search)."""
    n = len(cells)
    for a in range(1, n + 1):
        if n % a:
            continue
        c = n // a
        for b in range(a):
            res = set()
            for (x, y) in cells:
                q, ry = divmod(y, c)
                res.add(((x - q * b) % a, ry))
            if len(res) == n:
                return True
    return False


def boundary_word(cells):
    """Counterclockwise boundary word in letters r, u, l, d of a simply connected polyomino."""
    # Build directed boundary edges with the cell on the left.
    out = {}
    for (x, y) in cells:
        if (x, y - 1) not in cells:
            out.setdefault((x, y), []).append(((x + 1, y), 'r'))
        if (x + 1, y) not in cells:
            out.setdefault((x + 1, y), []).append(((x + 1, y + 1), 'u'))
        if (x, y + 1) not in cells:
            out.setdefault((x + 1, y + 1), []).append(((x, y + 1), 'l'))
        if (x - 1, y) not in cells:
            out.setdefault((x, y + 1), []).append(((x, y), 'd'))
    total = sum(len(v) for v in out.values())
    start = min(out)
    word, p, prev = [], start, None
    turn_pref = {'r': 'urd', 'u': 'lur', 'l': 'dlu', 'd': 'rdl'}
    while True:
        opts = out[p]
        if len(opts) == 1:
            q, ch = opts[0]
        else:
            q, ch = next(o for t in turn_pref[prev] for o in opts if o[1] == t)
        word.append(ch)
        p, prev = q, ch
        if p == start and len(word) == total:
            break
    return ''.join(word)


COMP = {'r': 'l', 'l': 'r', 'u': 'd', 'd': 'u'}


def hat(w):
    return ''.join(COMP[c] for c in reversed(w))


def bn_factorization(word):
    """Beauquier-Nivat: some rotation equals A B C hat(A) hat(B) hat(C), at most one empty."""
    n = len(word)
    if n % 2:
        return False
    half = n // 2
    for s in range(n):
        w = word[s:] + word[:s]
        first, second = w[:half], w[half:]
        for i in range(half + 1):
            for j in range(i, half + 1):
                A, B, C = first[:i], first[i:j], first[j:]
                if sum(1 for z in (A, B, C) if z == '') > 1:
                    continue
                if second == hat(A) + hat(B) + hat(C):
                    return True
    return False


PENTOMINOES = {
    'F': [(1, 0), (2, 0), (0, 1), (1, 1), (1, 2)],
    'I': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
    'L': [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0)],
    'N': [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3)],
    'P': [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)],
    'T': [(0, 2), (1, 2), (2, 2), (1, 1), (1, 0)],
    'U': [(0, 0), (2, 0), (0, 1), (1, 1), (2, 1)],
    'V': [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)],
    'W': [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)],
    'X': [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    'Y': [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1)],
    'Z': [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)],
}


def check_week_198():
    counts = [len(free_polyominoes(n)) for n in range(1, 7)]
    assert counts == [1, 1, 2, 5, 12, 35]
    # Beauquier-Nivat (boundary factorization) agrees with a direct lattice search
    # for every polyomino up to 6 cells (none of these has a hole).
    tile_counts = []
    for n in range(1, 7):
        k = 0
        for s in free_polyominoes(n):
            w = boundary_word(set(s))
            bn = bn_factorization(w)
            lt = lattice_tiles(set(s))
            assert bn == lt
            k += bn
        tile_counts.append(k)
    assert tile_counts == [1, 1, 2, 5, 9, 24]
    # Which pentominoes tile by translation alone.
    trans = sorted(name for name, c in PENTOMINOES.items() if lattice_tiles(set(c)))
    assert trans == ['I', 'L', 'N', 'P', 'V', 'W', 'X', 'Y', 'Z']   # not F, T, U
    # Every tetromino tiles by translation alone.
    assert tile_counts[3] == 5
    # Nibble examples on a 4-by-4 square (cells (x, y), 0 <= x, y <= 3).
    sq = {(x, y) for x in range(4) for y in range(4)}
    # A one-cell nibble from the top edge (column 1), stuck anywhere under the bottom
    # edge, tiles by translation (directly below: square lattice; elsewhere: rows slide).
    for x in range(4):
        t = (sq - {(1, 3)}) | {(x, -1)}
        assert lattice_tiles(t) and bn_factorization(boundary_word(t))
    good = (sq - {(1, 3)}) | {(1, -1)}
    # Stuck on the left or right side instead, it never tiles by translation.
    for y in range(4):
        for side in (-1, 4):
            t = (sq - {(1, 3)}) | {(side, y)}
            assert not lattice_tiles(t) and not bn_factorization(boundary_word(t))
    # An L-shaped three-cell nibble slid to the bottom tiles; flipped over, it does not.
    nib = {(1, 3), (2, 3), (2, 2)}
    slid = (sq - nib) | {(x, y - 4) for x, y in nib}
    flipped = (sq - nib) | {(3 - x, y - 4) for x, y in nib}
    assert lattice_tiles(slid) and not lattice_tiles(flipped)
    assert bn_factorization(boundary_word(slid)) and not bn_factorization(boundary_word(flipped))
    # Two nibbles (top to bottom and left to right) still tile by translation.
    two = (good - {(0, 1)}) | {(4, 1)}
    assert lattice_tiles(two)



# ---------------------------------------------------------------- week 199
def out_shuffle(deck):
    n = len(deck) // 2
    top, bot = deck[:n], deck[n:]
    return tuple(c for pair in zip(top, bot) for c in pair)


def in_shuffle(deck):
    n = len(deck) // 2
    top, bot = deck[:n], deck[n:]
    return tuple(c for pair in zip(bot, top) for c in pair)


def order(f, m):
    d = tuple(range(m))
    e, k = f(d), 1
    while e != d:
        e, k = f(e), k + 1
    return k


def mult_order(a, m):
    x, k = a % m, 1
    while x != 1:
        x, k = x * a % m, k + 1
    return k


def shuffle_group_size(m):
    start = tuple(range(m))
    seen, frontier = {start}, [start]
    while frontier:
        nxt = []
        for d in frontier:
            for f in (in_shuffle, out_shuffle):
                e = f(d)
                if e not in seen:
                    seen.add(e)
                    nxt.append(e)
        frontier = nxt
    return len(seen)


def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def check_week_199():
    # Out-shuffle orders: 4, 6, 8, 10, 12 cards take 2, 4, 3, 6, 10; 52 takes 8;
    # 50 takes 21; 54 takes 52.  The order is the order of 2 mod (cards - 1).
    want = {4: 2, 6: 4, 8: 3, 10: 6, 12: 10, 50: 21, 52: 8, 54: 52}
    for m, k in want.items():
        assert order(out_shuffle, m) == k == mult_order(2, m - 1)
    # In-shuffle orders: order of 2 mod (cards + 1); 52 cards need 52,
    # and 26 in-shuffles turn the deck upside down.
    for m in range(2, 60, 2):
        assert order(in_shuffle, m) == mult_order(2, m + 1)
    assert order(in_shuffle, 52) == 52
    d = tuple(range(52))
    for _ in range(26):
        d = in_shuffle(d)
    assert d == tuple(range(51, -1, -1))
    # Elmsley: to send the top card to place k (counting from 0), write k in binary and
    # do in for 1, out for 0, left to right.  Checked for 8, 16 and 52 cards.
    for m in (8, 16, 52):
        for k in range(m):
            deck = tuple(range(m))
            for bit in (bin(k)[2:] if k else ''):
                deck = in_shuffle(deck) if bit == '1' else out_shuffle(deck)
            assert deck.index(0) == k
    assert [b for b in bin(6)[2:]] == ['1', '1', '0']
    assert bin(13)[2:] == '1101'
    # Mirror partners (places i and m-1-i) stay mirror partners under both shuffles.
    for m in range(2, 30, 2):
        for f in (in_shuffle, out_shuffle):
            e = f(tuple(range(m)))
            for i in range(m):
                assert e.index(m - 1 - e[i]) == m - 1 - i
    # How many orders the two shuffles reach together.
    sizes = {m: shuffle_group_size(m) for m in range(2, 17, 2)}
    assert sizes[4] == 8 and sizes[8] == 24 and sizes[16] == 64      # k * 2^k for 2^k cards
    assert sizes[12] == 64 * 120                                      # 2^6 times PGL(2,5)
    assert sizes[14] == fact(7) * 2 ** 6                               # D_7, n = 7
    assert sizes[6] == fact(3) * 2 ** 2                                # D_3, n = 3
    assert sizes[10] == fact(5) * 2 ** 5 // 2                          # index 2, n = 5
    assert sizes == {2: 2, 4: 8, 6: 24, 8: 24, 10: 1920, 12: 7680, 14: 322560, 16: 64}
    # Mirror-pair bound n! 2^n; 8 cards reach 24 of 40320 orders.
    assert fact(8) == 40320 and fact(4) * 2 ** 4 == 384



# ---------------------------------------------------------------- week 200
def kaprekar_step(s):
    digits = sorted(s)
    lo = int(''.join(digits))
    hi = int(''.join(reversed(digits)))
    return str(hi - lo).zfill(len(s))


def kaprekar_steps(s, target):
    k = 0
    seen = set()
    while s != target:
        if s in seen:
            return None
        seen.add(s)
        s = kaprekar_step(s)
        k += 1
    return k


def happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(c) ** 2 for c in str(n))
    return n == 1


def check_week_200():
    # Four digits: every string 0000-9999 with two different digits reaches 6174
    # within 7 steps; 7 is needed.
    dist = {}
    for v in range(10000):
        s = str(v).zfill(4)
        if len(set(s)) == 1:
            continue
        k = kaprekar_steps(s, '6174')
        assert k is not None and k <= 7
        dist[k] = dist.get(k, 0) + 1
    assert sum(dist.values()) == 9990 and max(dist) == 7
    # Restricting to 1000-9999 (as Nishiyama counts): 8991 starts.
    four = [str(v) for v in range(1000, 10000) if len(set(str(v))) > 1]
    assert len(four) == 8991
    d2 = {}
    for s in four:
        k = kaprekar_steps(s, '6174')
        d2[k] = d2.get(k, 0) + 1
    assert d2[0] == 1 and d2[7] == 1980 and max(d2) == 7
    assert [d2[k] for k in range(8)] == [1, 356, 519, 2124, 1124, 1379, 1508, 1980]
    # 6174 is the only fixed point with two different digits.
    assert [s for s in (str(v).zfill(4) for v in range(10000))
            if len(set(s)) > 1 and kaprekar_step(s) == s] == ['6174']
    # Example chains.
    assert kaprekar_step('3524') == '3087' and kaprekar_step('3087') == '8352' and kaprekar_step('8352') == '6174'
    assert kaprekar_step('2111') == '0999' and kaprekar_step('0999') == '8991'
    # The first step depends only on the gaps: big - small = 999(a-d) + 90(b-c).
    for v in range(10000):
        s = str(v).zfill(4)
        a, b, c, d = sorted(map(int, s), reverse=True)
        assert int(kaprekar_step(s)) == 999 * (a - d) + 90 * (b - c)
    firsts = {999 * x + 90 * y for x in range(1, 10) for y in range(0, x + 1)}
    assert len(firsts) == 54
    assert all(kaprekar_steps(str(f).zfill(4), '6174') <= 6 for f in firsts)
    # Three digits: big - small = 99(a - c), so only 9 first results 099 ... 891,
    # and every start with two different digits reaches 495 within 6 steps.
    three_firsts = sorted({int(kaprekar_step(str(v).zfill(3))) for v in range(1000) if len(set(str(v).zfill(3))) > 1})
    assert three_firsts == [99 * g for g in range(1, 10)]
    steps3 = [kaprekar_steps(str(v).zfill(3), '495') for v in range(1000) if len(set(str(v).zfill(3))) > 1]
    assert None not in steps3 and max(steps3) == 6
    # Two digits: 9 times the gap; the loop 09 -> 81 -> 63 -> 27 -> 45 -> 09.
    s = '09'
    loop = [s]
    for _ in range(5):
        s = kaprekar_step(s)
        loop.append(s)
    assert loop == ['09', '81', '63', '27', '45', '09']
    # The gaps go round 9, 7, 3, 5, 1.
    assert [abs(int(x[0]) - int(x[1])) for x in loop[:5]] == [9, 7, 3, 5, 1]
    # Happy numbers below 50 and the eight-number loop.
    assert [n for n in range(1, 50) if happy(n)] == [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49]
    cyc = {4, 16, 37, 58, 89, 145, 42, 20}
    for n in range(1, 1001):
        m, seen = n, set()
        while m != 1 and m not in cyc:
            m = sum(int(c) ** 2 for c in str(m))
        assert m == 1 or m in cyc
    assert sum(int(c) ** 2 for c in '7') == 49 and 4 ** 2 + 9 ** 2 == 97



# ---------------------------------------------------------------- week 201
LIMIT = 10001
SIEVE = [False, False] + [True] * (LIMIT - 1)
for _i in range(2, int(LIMIT ** 0.5) + 1):
    if SIEVE[_i]:
        for _j in range(_i * _i, LIMIT + 1, _i):
            SIEVE[_j] = False


def goldbach_ways(n):
    return [(p, n - p) for p in range(2, n // 2 + 1) if SIEVE[p] and SIEVE[n - p]]


def check_week_201():
    # Every even number from 4 to 10000 is a sum of two primes.
    for n in range(4, 10001, 2):
        assert goldbach_ways(n)
    ways = {n: len(goldbach_ways(n)) for n in range(4, 101, 2)}
    assert [ways[n] for n in (4, 6, 8, 10, 12, 14, 16, 18, 20)] == [1, 1, 1, 2, 1, 2, 2, 2, 2]
    assert ways[100] == 6 and goldbach_ways(100)[0] == (3, 97)
    assert ways[98] == 3 and max(ways.values()) == ways[90] == 9
    # With prime towers 2, 3, 5, 7 every even 4..14 is two towers; 16 is not.
    small = [2, 3, 5, 7]
    sums = {a + b for a in small for b in small}
    assert all(n in sums for n in range(4, 15, 2)) and 16 not in sums
    # Little Goldbach (NRICH): whole numbers 1..19 that are not a sum of two primes.
    not_sum = [n for n in range(1, 20)
               if not any(is_prime(p) and is_prime(n - p) for p in range(2, n - 1))]
    assert not_sum == [1, 2, 3, 11, 17]
    # Odd n is a sum of two primes exactly when n - 2 is prime (one prime must be 2).
    for n in range(5, 200, 2):
        assert bool(goldbach_ways(n)) == is_prime(n - 2)
    # Weak Goldbach checked small: every odd 7..2001 is a sum of three primes.
    primes = [p for p in range(2, 2002) if is_prime(p)]
    for n in range(7, 2002, 2):
        assert any(goldbach_ways(n - p) for p in primes if p <= n - 4 and (n - p) % 2 == 0)
    # Smallest first prime needed for even n up to 10000: never more than 173,
    # and 173 only for 7426.
    least = {n: min(p for p, q in goldbach_ways(n)) for n in range(4, 10001, 2)}
    assert max(least.values()) == 173
    assert [n for n in least if least[n] == 173] == [7426]


# ---------------------------------------------------------------- main
def main():
    for name in ["196", "197", "198", "199", "200", "201"]:
        globals()[f"check_week_{name}"]()
        print(f"week {name}: ok")


if __name__ == "__main__":
    main()
