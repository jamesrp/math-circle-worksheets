"""Grades 4-5 packet (F01E-U-v1): every problem, from the boards as drawn in the delivered PDF,
with an independent 3-D model of cube piles for the shaded pictures.
Writes check_upper.out."""
import os
import sys
from collections import Counter, deque
from itertools import permutations
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import *
from fastgame import Board

log = Log(os.path.join(HERE, 'check_upper.out'))
BAND = 'grades-4-5'
ALL = lambda R: greens(R) + blues(R) + reds(R) + yellows(R)


def game(o, label=''):
    Bd = Board(o.R)
    w, good, moves = Bd.solve()
    ht = half_turn_centre(o.R)
    s = f'  {label}{BD.classify(o)}: {describe(o.R)}; {len(moves)} first moves; winner {w}'
    if w == '1st':
        s += f'; {len(good)} winning first moves'
    if ht:
        (si, sj), kind = ht
        s += f'; half-turn centre is a lattice {"point" if kind == "vertex" else "edge midpoint"}'
        if kind == 'edge':
            selfimg = [mv for mv in moves if frozenset(frozenset((si - v[0], sj - v[1]) for v in c) for c in Bd.move_cells(mv)) == Bd.move_cells(mv)]
            s += f'; {len(selfimg)} self-symmetric blue(s), winning: {[mv in good for mv in selfimg]}'
    else:
        s += '; no half-turn symmetry'
    log(s)


def same_as_middle(page4, page2):
    a = [normalize(o.R) for o in stroked_boards(BAND, page4)]
    b = [normalize(o.R) for o in stroked_boards('grades-2-3', page2)]
    return a == b


def flip_graph(R, Ts):
    """Two tilings are joined if they differ in exactly three rhombi that fill one small hexagon."""
    idx = {T: k for k, T in enumerate(Ts)}
    G = {T: [] for T in Ts}
    for T in Ts:
        for T2 in Ts:
            d = T - T2
            if len(d) == 3:
                cells = frozenset().union(*d)
                if len(cells) == 6 and len(frozenset.intersection(*cells)) == 1:
                    G[T].append(T2)
    return G


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


def bipartite(G):
    col = {}
    for s in G:
        if s in col:
            continue
        col[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in G[u]:
                if v not in col:
                    col[v] = 1 - col[u]
                    q.append(v)
                elif col[v] == col[u]:
                    return False
    return True


def match_model(o):
    """Find box dimensions (a,b,c) whose projected corner picture has the drawn outline;
    return (abc, model dict, centred outline match)."""
    sides = sorted(set(round(s) for s in o.sides))
    found = []
    lens = [round(s) for s in o.sides]
    for abc in set(permutations(lens[:3])):
        if model_boundary_key(*abc) == region_outline_key(o.R, o.frame):
            found.append(abc)
    return found


log('Grades 4-5 packet, delivered PDF', os.path.relpath(PP.PDFS[BAND], PP.ROOT))

log('\nProblem 1 (page 1): same four boards as grades 2-3 Problem 1:', same_as_middle(1, 1))
for o in stroked_boards(BAND, 1, min_lw=1.5):
    game(o)
log('\nProblem 2 (page 2): same two boards as grades 2-3 Problem 5:', same_as_middle(2, 5))
for o in stroked_boards(BAND, 2, min_lw=1.5):
    game(o)
log('\nProblem 3 (page 3): triangles 3 and 4')
for o in stroked_boards(BAND, 3, min_lw=1.5):
    game(o)
    log(f'    possible game lengths: {sorted(game_lengths(o.R))}')

# ------------------------------------------------------------------ Problem 4
log('\nProblem 4 (page 4): blue fillings of the hexagon as cube piles')
big4 = stroked_boards(BAND, 4, min_lw=1.5)[0]
log(f'  board: {BD.classify(big4)}, unit {big4.unit:.4f} in, grid angle {big4.theta:.1f} deg (30 = vertical sides)')
Ts4 = [frozenset(T) for T in all_tilings(big4.R, blues(big4.R))]
log(f'  blue fillings: {len(Ts4)}')
dims = match_model(big4)
log(f'  box dimensions whose corner picture has this outline (floor x, floor y, height): {dims}')
a, b, c = dims[0]
M, _ = model_pictures(a, b, c)
log(f'  plane partitions in the {a}x{b}x{c} box: {len(M)}')
cubes_of = {}
for T in Ts4:
    K = frozenset(tiling_face_keys(T, big4.frame))
    cubes_of[T] = M[K][1] if K in M else None
log(f'  every filling is the picture of exactly one pile: {all(v is not None for v in cubes_of.values())}; '
    f'fillings per cube count: {dict(sorted(Counter(cubes_of.values()).items()))}')

# piles in the guide's notation: back (corner), left, right, front
piles = {}
for K, (h, n, faces) in M.items():
    # x runs to the lower left, y to the lower right: h[1][0] is the left stack, h[0][1] the right
    s = f'{h[0][0]}{h[1][0]}{h[0][1]}{h[1][1]}'
    piles.setdefault(n, []).append(s)
GUIDE_PILES = {0: ['0000'], 1: ['1000'], 2: ['2000', '1100', '1010'], 3: ['2100', '2010', '1110'],
               4: ['2200', '2110', '2020', '1111'], 5: ['2210', '2120', '2111'], 6: ['2220', '2211', '2121'],
               7: ['2221'], 8: ['2222']}
log(f'  guide list of 20 piles (back, left, right, front) equals the model list: '
    f'{ {k: sorted(v) for k, v in piles.items()} == {k: sorted(v) for k, v in GUIDE_PILES.items()} }')


def shaded_pictures(band, pg):
    groups = cluster(drawn_pieces(band, pg))
    W = PP.words(band)
    out = []
    for g in groups:
        t = tiling_from_pieces(g)
        # nearest single-letter label to the left
        labs = [w for w in W if w[0] == pg - 1 and len(w[5]) == 1 and w[5].isalpha()]
        cx, cy = t['centre']
        lab = min(labs, key=lambda w: (w[1] - cx) ** 2 + ((w[2] + w[4]) / 2 - cy) ** 2)[5] if labs else '?'
        out.append((lab, t))
    return out


def shade_report(lab, t, M, a, b, c):
    K = tiling_face_keys(t['tiling'], t['frame'])
    keyset = frozenset(K)
    ok = keyset in M
    s = f'  picture {lab}: {len(t["tiling"])} rhombi, valid filling of a {len(t["region"])}-cell region: {t["disjoint"]}, snap error {t["snap_err"]:.4f}'
    if ok:
        h, n, faces = M[keyset]
        shade_by_type = {}
        for k, p in K.items():
            shade_by_type.setdefault(faces[k], set()).add(colour_name(t['colours'][p]))
        s += f'; it is the pile with {n} cubes, heights {h}; shades by face type: ' + \
            ', '.join(f'{ty}: {sorted(v)}' for ty, v in sorted(shade_by_type.items()))
    else:
        s += '; NOT a picture of a pile in this box'
    log(s)
    return (M[keyset][1] if ok else None), (shade_by_type if ok else None)


log('  shaded examples on page 4:')
W4 = PP.words(BAND)
pics4 = shaded_pictures(BAND, 4)
for lab, t in pics4:
    n, sh = shade_report(lab, t, M, a, b, c)
cube_words = [w for w in W4 if w[0] == 3 and w[5] in ('0', '8')]
log(f'  printed counts under the examples: {[w[5] for w in sorted(cube_words, key=lambda w: w[1])]}')

# ------------------------------------------------------------------ Problem 5
log('\nProblem 5 (page 5): flips from A to B; odd round trips')
pics5 = shaded_pictures(BAND, 5)
for lab, t in pics5:
    shade_report(lab, t, M, a, b, c)
G = flip_graph(big4.R, Ts4)
# locate A and B among the board's fillings by cube count (0 and 8 are unique piles)
A = [T for T in Ts4 if cubes_of[T] == 0][0]
B = [T for T in Ts4 if cubes_of[T] == 8][0]
d = bfs(G, A)
log(f'  flip graph: {len(G)} fillings, {sum(len(v) for v in G.values()) // 2} flips; connected: {len(d) == len(G)}; '
    f'bipartite (no odd round trip): {bipartite(G)}; fewest flips A->B: {d[B]}')
log(f'  every flip changes the cube count by exactly one: {all(abs(cubes_of[u] - cubes_of[v]) == 1 for u in G for v in G[u])}; '
    f'flips available in A: {len(G[A])}, in B: {len(G[B])}')
log(f'  recording copies on page 5: {len([o for o in stroked_boards(BAND, 5) if o.grid])}')

# ------------------------------------------------------------------ Problem 6
log('\nProblem 6 (page 6): the 1,3,3 hexagon')
big6 = stroked_boards(BAND, 6, min_lw=1.5)[0]
log(f'  board: {BD.classify(big6)}, unit {big6.unit:.4f} in, grid angle {big6.theta:.1f}')
Ts6 = [frozenset(T) for T in all_tilings(big6.R, blues(big6.R))]
dims6 = match_model(big6)
log(f'  blue fillings: {len(Ts6)}; box dimensions (floor x, floor y, height) with this outline: {dims6}')
a6, b6, c6 = dims6[0]
M6, _ = model_pictures(a6, b6, c6)
cnt = Counter()
cubes6 = {}
for T in Ts6:
    K = tiling_face_keys(T, big6.frame)
    h, n, faces = M6[frozenset(K)]
    cubes6[T] = n
    cnt[tuple(sorted(Counter(faces[k] for k in K).items()))] += 1
log(f'  face types per filling (top = light, as in A and B): {dict(cnt)}')
G6 = flip_graph(big6.R, Ts6)
E = [T for T in Ts6 if cubes6[T] == 0][0]
F = [T for T in Ts6 if cubes6[T] == max(cubes6.values())][0]
log(f'  most cubes {cubes6[F]}; fewest flips from no cubes to most: {bfs(G6, E)[F]}; bipartite: {bipartite(G6)}')
log(f'  recording copies on page 6: {len([o for o in stroked_boards(BAND, 6) if o.lw < 1.5])}')

# ------------------------------------------------------------------ Problem 7
log('\nProblem 7 (page 7): red fillings of the 2x hexagon (as drawn on page 4)')
TR = [frozenset(T) for T in all_tilings(big4.R, reds(big4.R))]
pts = Counter(v for cc in big4.R for v in cc)
cx = sum(centroid(cc)[0] for cc in big4.R) / len(big4.R)
cy = sum(centroid(cc)[1] for cc in big4.R) / len(big4.R)
mid = min(pts, key=lambda p: (lcart(p)[0] - cx) ** 2 + (lcart(p)[1] - cy) ** 2)
H = unit_hex(mid)
rings = {}
middles = {}
for T in TR:
    inside = frozenset(p for p in T if p <= H)
    ring = frozenset(p for p in T if not p <= H)
    rings.setdefault(ring, []).append(T)
    middles.setdefault(inside, []).append(T)
log(f'  red fillings: {len(TR)}; every filling has exactly two trapezoids inside the middle hexagon: '
    f'{all(sum(1 for p in T if p <= H) == 2 for T in TR)}; distinct rings: {len(rings)}; distinct middles: {len(middles)}; '
    f'every ring with every middle: {all(len(v) == len(middles) for v in rings.values())}')
ringlist = list(rings)
log(f'  the {len(ringlist)} rings pairwise share no trapezoid: {all(not (r1 & r2) for r1 in ringlist for r2 in ringlist if r1 != r2)}')


def turn60(P):
    # a sixth of a turn about the middle lattice point
    def f(v):
        d = (v[0] - mid[0], v[1] - mid[1])
        r = rot60(d)
        return (mid[0] + r[0], mid[1] + r[1])
    return frozenset(frozenset(frozenset(f(v) for v in c) for c in p) for p in P)


log(f'  each ring is unchanged by a sixth of a turn: {[turn60(r) == r for r in ringlist]}; '
    f'the three middle cuts are moved round by it: {sorted(len({m, turn60(m), turn60(turn60(m))}) for m in middles)}')
# symmetry classes of the 9 fillings
classes = set()
for T in TR:
    imgs = []
    for f in SYMS:
        img = frozenset(map_cells(f, p) for p in T)
        imgs.append(normalize(frozenset(c for p in img for c in p)) and tuple(sorted(normalize(p) for p in img)))
    # canonical: translate whole tiling so that region is fixed
    best = None
    for f in SYMS:
        img = frozenset(map_cells(f, p) for p in T)
        reg = frozenset(c for p in img for c in p)
        dd = translate_to(reg, big4.R)
        if dd is None:
            continue
        key = tuple(sorted(tuple(sorted(tuple(sorted(c)) for c in p)) for p in shift(img, dd)))
        best = key if best is None or key < best else best
    classes.add(best)
classes_rot = set()
for T in TR:
    best = None
    for k, f in enumerate(SYMS):
        if k % 2:
            continue  # rotations only
        img = frozenset(map_cells(f, p) for p in T)
        reg = frozenset(c for p in img for c in p)
        dd = translate_to(reg, big4.R)
        if dd is None:
            continue
        key = tuple(sorted(tuple(sorted(tuple(sorted(c)) for c in p)) for p in shift(img, dd)))
        best = key if best is None or key < best else best
    classes_rot.add(best)
log(f'  fillings up to rotation: {len(classes_rot)}; up to rotation and reflection: {len(classes)}')
log(f'  recording copies on page 7: {len([o for o in stroked_boards(BAND, 7) if o.grid])}')

# ------------------------------------------------------------------ Problem 8
log('\nProblem 8 (page 8): moves on red fillings; C and D')
pics8 = shaded_pictures(BAND, 8)
CD = {}
for lab, t in pics8:
    dd = translate_to(t['region'], big4.R) if same_shape(t['region'], big4.R) else None
    # the pictures are drawn at another scale/origin; compare after translation in lattice coordinates
    reg = t['region']
    log(f'  picture {lab}: {len(t["tiling"])} pieces, kinds {Counter(kind_of(p) for p in t["tiling"])}, colours '
        f'{Counter(colour_name(v) for v in t["colours"].values())}, disjoint {t["disjoint"]}, same outline as the page-4 hexagon: {same_shape(reg, big4.R)}')
    # map into the page-4 board frame through the shared lattice orientation
    found = None
    for f in SYMS:
        img = frozenset(map_cells(f, p) for p in t['tiling'])
        r2 = frozenset(c for p in img for c in p)
        d2 = translate_to(r2, big4.R)
        if d2 is None:
            continue
        cand = shift(img, d2)
        if cand in TR:
            # keep the identity-like map: check orientation by comparing page geometry
            found = found or (f, cand)
    CD[lab] = t
# Work directly in each picture's own lattice: rings and middles there.


def ring_mid(t):
    R = t['region']
    pts = Counter(v for cc in R for v in cc)
    cx = sum(centroid(cc)[0] for cc in R) / len(R)
    cy = sum(centroid(cc)[1] for cc in R) / len(R)
    mid = min(pts, key=lambda p: (lcart(p)[0] - cx) ** 2 + (lcart(p)[1] - cy) ** 2)
    H = unit_hex(mid)
    T = t['tiling']
    return frozenset(p for p in T if not p <= H), frozenset(p for p in T if p <= H), H


if 'C' in CD and 'D' in CD:
    tC, tD = CD['C'], CD['D']
    # put D into C's lattice frame through page coordinates
    def to_frame(t, fr):
        out = set()
        for p in t['tiling']:
            out.add(frozenset(frozenset(fr.to_lat(t['frame'].to_page(v))[0] for v in c) for c in p))
        return frozenset(out)
    # scale check: both drawn at the same unit
    log(f'  C and D drawn at units {tC["unit"]:.4f} and {tD["unit"]:.4f} in')
    # translate D's picture onto C's position (same unit and angle) and compare in C's frame
    dx = tC['centre'][0] - tD['centre'][0]
    dy = tC['centre'][1] - tD['centre'][1]

    class Shifted:
        pass
    frD = tD['frame']
    frD2 = Frame(frD.unit, frD.theta, (frD.origin[0] + dx, frD.origin[1] + dy))
    Dt = frozenset(frozenset(frozenset(tC['frame'].to_lat(frD2.to_page(v))[0] for v in c) for c in p) for p in tD['tiling'])
    Ct = tC['tiling']
    regC = frozenset().union(*Ct)
    log(f'  D moved onto C covers the same region: {frozenset().union(*Dt) == regC}')
    TRc = [frozenset(T) for T in all_tilings(regC, reds(regC))]
    log(f'  C is a red filling: {Ct in TRc}; D is a red filling: {Dt in TRc}; trapezoids C and D share: {len(Ct & Dt)}; differ in {len(Ct - Dt)}')
    rC, mC, Hc = ring_mid({'region': regC, 'tiling': Ct})
    rD, mD, _ = ring_mid({'region': regC, 'tiling': Dt})
    log(f'  C and D: same middle {mC == mD}; same ring {rC == rD}')
    # move graphs
    for k in (2, 5, 6):
        G = {T: [T2 for T2 in TRc if T2 != T and len(T - T2) <= k] for T in TRc}
        comp = bfs(G, Ct)
        log(f'  moves picking up at most {k} trapezoids: C reaches D: {Dt in comp}; graph bipartite: {bipartite(G)}; '
            f'component sizes: {sorted(Counter(len(bfs(G, T)) for T in TRc).items())}')
    G2 = {T: [T2 for T2 in TRc if T2 != T and len(T - T2) <= 2] for T in TRc}
    # shortest odd closed walk
    best = None
    for s in TRc:
        for T2 in G2[s]:
            for T3 in G2[T2]:
                if T3 != s and s in G2[T3]:
                    best = 3
    log(f'  shortest odd round trip with two-trapezoid moves: {best}')
    def mirror_symmetric(ring, fr):
        # left-right mirror on the page, about the vertical line through the picture's centre
        pts = [fr.to_page(v) for p in ring for c in p for v in c]
        cx = (min(x for x, _ in pts) + max(x for x, _ in pts)) / 2
        def key(p, flip):
            out = []
            for c in p:
                q = [fr.to_page(v) for v in c]
                x = sum(a for a, _ in q) / 3 - cx
                y = sum(b for _, b in q) / 3
                out.append((round(-x if flip else x, 3) + 0.0, round(y, 3)))
            return frozenset(out)
        return frozenset(key(p, False) for p in ring) == frozenset(key(p, True) for p in ring)
    log(f'  C ring mirror-symmetric on the page: {mirror_symmetric(rC, tC["frame"])} (a pinwheel if False); '
        f'D ring mirror-symmetric: {mirror_symmetric(rD, tC["frame"])} (the frame if True); '
        f'guide row/column labels are checked in check_guide.py')

# ------------------------------------------------------------------ Problem 9
log('\nProblem 9 (page 9): four small boards')
for o in stroked_boards(BAND, 9):
    ht = half_turn_centre(o.R)
    s = f'  {BD.classify(o)}: {describe(o.R)}; half-turn centre: ' + (('lattice point' if ht[1] == 'vertex' else 'edge midpoint') if ht else 'none')
    if len(o.R) <= 22:
        Bd = Board(o.R)
        w, good, moves = Bd.solve()
        s += f'; exhaustive search: winner {w}, {len(good)} winning first moves of {len(moves)}'
        if ht and ht[1] == 'edge':
            (si, sj), _ = ht
            selfimg = [mv for mv in moves if frozenset(frozenset((si - v[0], sj - v[1]) for v in c) for c in Bd.move_cells(mv)) == Bd.move_cells(mv)]
            s += f'; {len(selfimg)} self-symmetric (centre) blue, winning: {[mv in good for mv in selfimg]}'
    else:
        s += '; exhaustive search in big_games.py (big_games_*.out)'
    log(s)

log('\nProblem 10 (page 10): same board as grades 2-3 Problem 6:', same_as_middle(10, 6))
log.save()
