"""Independent model of squares and right-angled halves on a unit dot lattice.

Written for the guide review, without reading the writer's checker.
A cell (i,j) is split by both diagonals into four quarter triangles
S, E, N, W (0..3).  A square is all four quarters; a half is two
neighbouring quarters, named by the corner holding its right angle.
Inside and outline dots come from the corner angles that pieces put on
each dot (360 = inside, between 0 and 360 = outline), so Pick's rule is
never assumed.  Gaps are complement quarters that cannot reach the
outside through shared edges.
"""
from collections import defaultdict

S, E, N, W = 0, 1, 2, 3
HALF_Q = {'BL': (S, W), 'BR': (S, E), 'TR': (N, E), 'TL': (N, W)}


def corners(i, j):
    return {'BL': (i, j), 'BR': (i + 1, j), 'TR': (i + 1, j + 1), 'TL': (i, j + 1)}


def piece_square(i, j):
    return frozenset((i, j, q) for q in (S, E, N, W))


def piece_half(i, j, c):
    return frozenset((i, j, q) for q in HALF_Q[c])


def piece_kind(p):
    qs = {q for (_, _, q) in p}
    cells = {(i, j) for (i, j, _) in p}
    assert len(cells) == 1
    (i, j), = cells
    if len(qs) == 4:
        return ('sq', i, j, None)
    for c, t in HALF_Q.items():
        if set(t) == qs:
            return ('half', i, j, c)
    raise ValueError(p)


def piece_sides(p):
    kind, i, j, c = piece_kind(p)
    cn = corners(i, j)
    bot = frozenset([cn['BL'], cn['BR']]); rgt = frozenset([cn['BR'], cn['TR']])
    top = frozenset([cn['TL'], cn['TR']]); lft = frozenset([cn['BL'], cn['TL']])
    main = frozenset([cn['BL'], cn['TR']]); anti = frozenset([cn['BR'], cn['TL']])
    if kind == 'sq':
        return {bot, rgt, top, lft}
    return {'BL': {bot, lft, anti}, 'BR': {bot, rgt, main},
            'TR': {top, rgt, anti}, 'TL': {top, lft, main}}[c]


def piece_angles(p):
    kind, i, j, c = piece_kind(p)
    cn = corners(i, j)
    if kind == 'sq':
        return {v: 90 for v in cn.values()}
    opp = {'BL': 'TR', 'TR': 'BL', 'BR': 'TL', 'TL': 'BR'}
    out = {cn[c]: 90}
    for k in cn:
        if k != c and k != opp[c]:
            out[cn[k]] = 45
    return out


def all_pieces_in_cell(i, j, squares=True):
    ps = [piece_half(i, j, c) for c in HALF_Q]
    if squares:
        ps.append(piece_square(i, j))
    return ps


def neighbours(p, squares=True):
    """Pieces sharing a whole side with p (may overlap p's region; filtered later)."""
    kind, i, j, c = piece_kind(p)
    out = []
    sides = piece_sides(p)
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            for q in all_pieces_in_cell(i + di, j + dj, squares):
                if q != p and piece_sides(q) & sides:
                    out.append(q)
    return out


def quarters(shape):
    s = set()
    for p in shape:
        s |= p
    return s


def angle_map(shape):
    a = defaultdict(int)
    for p in shape:
        for v, ang in piece_angles(p).items():
            a[v] += ang
    return a


def counts(shape):
    a = angle_map(shape)
    assert all(v <= 360 for v in a.values()), 'overlap'
    inside = sum(1 for v in a.values() if v == 360)
    outline = sum(1 for v in a.values() if 0 < v < 360)
    halves = sum(4 if False else (2 if piece_kind(p)[0] == 'sq' else 1) for p in shape)
    return halves, outline, inside


def inside_dots(shape):
    return {v for v, ang in angle_map(shape).items() if ang == 360}


def outline_dots(shape):
    return {v for v, ang in angle_map(shape).items() if 0 < ang < 360}


def side_connected(shape):
    shape = list(shape)
    if not shape:
        return False
    seen = {0}
    stack = [0]
    sides = [piece_sides(p) for p in shape]
    while stack:
        k = stack.pop()
        for m in range(len(shape)):
            if m not in seen and sides[k] & sides[m]:
                seen.add(m); stack.append(m)
    return len(seen) == len(shape)


def has_gap(shape):
    qs = quarters(shape)
    xs = [i for (i, _, _) in qs]; ys = [j for (_, j, _) in qs]
    x0, x1, y0, y1 = min(xs) - 1, max(xs) + 1, min(ys) - 1, max(ys) + 1
    free = {(i, j, q) for i in range(x0, x1 + 1) for j in range(y0, y1 + 1)
            for q in range(4)} - qs
    start = (x0, y0, S)
    seen = {start}; stack = [start]
    while stack:
        i, j, q = stack.pop()
        nb = [(i, j, (q + 1) % 4), (i, j, (q - 1) % 4)]
        if q == S: nb.append((i, j - 1, N))
        if q == N: nb.append((i, j + 1, S))
        if q == E: nb.append((i + 1, j, W))
        if q == W: nb.append((i - 1, j, E))
        for t in nb:
            if t in free and t not in seen:
                seen.add(t); stack.append(t)
    return len(seen) != len(free)


# ---- symmetry -------------------------------------------------------------
CENT = {S: (3, 1), E: (5, 3), N: (3, 5), W: (1, 3)}
INV = {v: k for k, v in CENT.items()}
SYMS = [lambda x, y: (x, y), lambda x, y: (-y, x), lambda x, y: (-x, -y), lambda x, y: (y, -x),
        lambda x, y: (-x, y), lambda x, y: (y, x), lambda x, y: (x, -y), lambda x, y: (-y, -x)]
ROTS = SYMS[:4]


def transform(shape, f):
    out = []
    for p in shape:
        np_ = []
        for (i, j, q) in p:
            cx, cy = CENT[q]
            X, Y = f(6 * i + cx, 6 * j + cy)
            np_.append((X // 6, Y // 6, INV[(X % 6, Y % 6)]))
        out.append(frozenset(np_))
    return out


def normalise(shape):
    qs = quarters(shape)
    mi = min(i for (i, _, _) in qs); mj = min(j for (_, j, _) in qs)
    return frozenset(frozenset((i - mi, j - mj, q) for (i, j, q) in p) for p in shape)


def key(shape):
    return tuple(sorted(tuple(sorted(p)) for p in normalise(shape)))


def canon(shape, syms=SYMS):
    return min(key(transform(shape, f)) for f in syms)


def region_key(shape, syms=SYMS):
    """Canonical form of the covered region only (ignores how it is cut into pieces)."""
    best = None
    for f in syms:
        t = transform(shape, f)
        qs = quarters(t)
        mi = min(i for (i, _, _) in qs); mj = min(j for (_, j, _) in qs)
        k = tuple(sorted((i - mi, j - mj, q) for (i, j, q) in qs))
        if best is None or k < best:
            best = k
    return best


def bbox(shape):
    qs = quarters(shape)
    xs = [i for (i, _, _) in qs]; ys = [j for (_, j, _) in qs]
    return max(xs) - min(xs) + 1, max(ys) - min(ys) + 1   # in cells = spacings


def fits(shape, w, h):
    a, b = bbox(shape)
    return (a <= w and b <= h) or (a <= h and b <= w)


# ---- enumeration of fixed (translation-normalised) side-connected shapes ---
def enumerate_shapes(nmax, squares=True):
    start = [normalise([p]) for p in all_pieces_in_cell(0, 0, squares)]
    levels = {1: set(start)}
    for n in range(2, nmax + 1):
        nxt = set()
        for sh in levels[n - 1]:
            qs = quarters(sh)
            for p in sh:
                for q in neighbours(p, squares):
                    if q in sh or (q & qs):
                        continue
                    nxt.add(normalise(list(sh) + [q]))
        levels[n] = nxt
    return levels
