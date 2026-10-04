"""Check every answer the packets rely on, using the same regions the figures draw.
Run: python3 verify.py   (prints a line per check; stops on the first failure)."""
from collections import Counter
from tri import *
from pics import *
from cubes import *
from fewest import solve

def ok(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        raise SystemExit(1)


def winner(R):
    return game_winner(R)[0]


def fewest(R):
    return solve(R)[0]


# ---------------------------------------------------------------- K-1
for n in (2, 3):
    ok(count_tilings(tri_up(0, 0, n), greens(tri_up(0, 0, n))) == 1 and len(tri_up(0, 0, n)) == n * n,
       f'{n}x green triangle takes {n*n} small greens')
    R = rhomb(n)
    ok(count_tilings(R, rhombi(R)) >= 1 and len(R) // 2 == n * n, f'{n}x rhombus takes {n*n} small blues')
    R = trap(0, 0, 2 * n, n)
    ok(count_tilings(R, trapezoids(R)) >= 1 and len(R) // 3 == n * n, f'{n}x trapezoid takes {n*n} small reds')
    R = hexR(n, n, n)
    ok(count_tilings(R, hexes(R)) == 0, f'{n}x hexagon cannot be covered by small hexagons')
ok(count_tilings(trap(0, 0, 4, 2), trapezoids(trap(0, 0, 4, 2))) == 1, '2x trapezoid: exactly one way with 4 reds')

for name, R, w in [('hexagon 1,1,1', hexR(1, 1, 1), 'second'), ('3-by-1 strip', parR(3, 1), 'first'),
                   ('2-by-2 parallelogram', parR(2, 2), 'second'), ('3-by-2 parallelogram', parR(3, 2), 'first'),
                   ('triangle 3', triR(3), 'first'), ('4-by-2 parallelogram', parR(4, 2), 'second')]:
    ok(winner(R) == w, f'K-1 game on {name}: {w} player wins')

for name, R, few in [('triangle 3', triR(3), 3), ('star', STAR, 6), ('boat', BOAT, 5), ('2x hexagon', HEX2, 6)]:
    ok(fewest(R) == few, f'K-1 picture {name}: fewest {few}, most {len(R)}')

# K-1 Problem 5: only small red pieces, then only small blue pieces (figs.ONE_COLOUR, top to bottom)
from figs import ONE_COLOUR, RED_ICON, BLUE_ICON
for R, red, blue in zip(ONE_COLOUR, [(3, 4), (5, 5), (0, None)], [(1, 6), (0, None), (6, 8)]):
    nr, nb = count_tilings(R, trapezoids(R)), count_tilings(R, rhombi(R))
    ok(nr == red[0] and (nr == 0 or len(R) == 3 * red[1]), f'K-1 P5 shape with {len(R)} triangles: red {red}')
    ok(nb == blue[0] and (nb == 0 or len(R) == 2 * blue[1]), f'K-1 P5 shape with {len(R)} triangles: blue {blue}')
ok(len(RED_ICON) == 3 and len(BLUE_ICON) == 2, 'K-1 P5 icons are one small trapezoid and one small rhombus')

H1 = hexR(1, 1, 1)
ok(count_tilings(H1, trapezoids(H1)) == 3, 'hexagon with two reds: 3 ways (3 recording copies)')
ok(count_tilings(H1, rhombi(H1)) == 2, 'hexagon with three blues: 2 ways (2 recording copies)')

# ---------------------------------------------------------------- game boards for 2-3 and 4-5
for name, R, w in [('hexagon 1,1,1', hexR(1, 1, 1), 'second'), ('2-by-2', parR(2, 2), 'second'),
                   ('3-by-2', parR(3, 2), 'first'), ('hexagon 1,1,2', hexR(1, 1, 2), 'first'),
                   ('hexagon 2,2,2', hexR(2, 2, 2), 'second'), ('3-by-3', parR(3, 3), 'first'),
                   ('4-by-2', parR(4, 2), 'second'), ('triangle 3', triR(3), 'first'),
                   ('triangle 4', triR(4), 'second')]:
    ok(winner(R) == w, f'game on {name}: {w} player wins')
r = game_winner(triR(3))
ok(r[1] == r[2], 'triangle 3: every first move wins')


def half_turn_check(R):
    """Return 'second' if the region has half-turn symmetry about a grid point (copying works for the
    second player), 'first' if about an edge midpoint with exactly one self-symmetric placement."""
    pts = [cart(v) for t in R for v in verts(t)]
    cx = (min(p[0] for p in pts) + max(p[0] for p in pts)) / 2
    cy = (min(p[1] for p in pts) + max(p[1] for p in pts)) / 2
    cents = {t: centroid(t) for t in R}
    img = {}
    for t, c in cents.items():
        q = (2 * cx - c[0], 2 * cy - c[1])
        m = [u for u, d in cents.items() if abs(d[0] - q[0]) < 1e-6 and abs(d[1] - q[1]) < 1e-6]
        assert len(m) == 1, 'region not symmetric'
        img[t] = m[0]
    selfsym = [p for p in rhombi(R) if frozenset(img[t] for t in p) == p]
    return 'second' if len(selfsym) == 0 else ('first' if len(selfsym) == 1 else '?')


for name, R, w in [('hexagon 3,3,3', hexR(3, 3, 3), 'second'), ('hexagon 1,2,3', hexR(1, 2, 3), 'first'),
                   ('4-by-4', parR(4, 4), 'second'), ('5-by-2', parR(5, 2), 'first')]:
    ok(half_turn_check(R) == w, f'Problem 9 (4-5) {name}: copying strategy gives {w} player')
ok(winner(hexR(1, 2, 3)) == 'first' and winner(parR(5, 2)) == 'first', 'brute force agrees on 1,2,3 and 5-by-2')

# ---------------------------------------------------------------- fewest pieces
ok(fewest(triR(4)) == 5, 'triangle 4: fewest 5')
ok(fewest(hexR(3, 3, 3)) == 12, '3x hexagon: fewest 12')
n7 = solve(hexR(3, 3, 3), extra=[('hex', 7, 7)])[0]
ok(n7 == 13, '3x hexagon using 7 small hexagons needs 13 pieces')

# ---------------------------------------------------------------- trapezoid kinds
for name, R, n, xy in [('triangle 3', triR(3), 2, (3, 0)), ('hexagon 2,2,2', HEX2, 9, (4, 4)),
                       ('triangle 6', triR(6), 220, (9, 3))]:
    T = tilings(R, trapezoids(R))
    c = Counter((sum(trap_kind(p) == 'two-up' for p in t), sum(trap_kind(p) == 'two-down' for p in t)) for t in T)
    ok(len(T) == n and set(c) == {xy}, f'{name}: {n} trapezoid fillings, each with {xy[0]} two-up and {xy[1]} two-down')
ok(updown(triR(6)) == (21, 15), 'triangle 6 has 21 up and 15 down')

# ---------------------------------------------------------------- cubes and flips
for (a, b, c), ntil, dist, counts in [((2, 2, 2), 20, 8, {'L': 4, 'M': 4, 'D': 4}),
                                      ((1, 3, 3), 20, 9, {'L': 9, 'M': 3, 'D': 3})]:
    R = frozenset(hexR(a, b, c))
    empty, full, Ts, G = empty_and_full(R)
    d = bfs(G, empty)
    bip = all((d[u] - d[v]) % 2 for u in Ts for v in G[u])
    cnt = {tuple(sorted(Counter(shade_class(p) for p in T).items())) for T in Ts}
    ok(len(Ts) == ntil, f'hexagon {a},{b},{c}: {ntil} blue fillings')
    ok(d[full] == dist and max(d.values()) == dist, f'hexagon {a},{b},{c}: fewest flips empty->full = {dist}')
    ok(bip, f'hexagon {a},{b},{c}: every closed route of flips has even length')
    ok(cnt == {tuple(sorted(counts.items()))}, f'hexagon {a},{b},{c}: every filling has shades {counts}')
    ok(Counter(shade_class(p) for p in empty)['L'] == counts['L'], 'empty picture shows the floor')

R, Ts = frozenset(HEX2), [frozenset(t) for t in tilings(HEX2, trapezoids(HEX2))]
Ts.sort(key=lambda T: sorted(sorted(p) for p in T))  # same order as figs.py, so C and D match
diffs = Counter(len(S - T) for S in Ts for T in Ts if S != T)
ok(set(diffs) == {2, 6, 8}, 'trapezoid fillings of 2,2,2 differ in 2, 6 or 8 trapezoids')
fam = {}
for S in Ts:
    fam[S] = frozenset(T for T in Ts if len(S - T) <= 2)
ok(len(set(fam.values())) == 3 and all(len(f) == 3 for f in fam.values()), 'three families of three')
C = Ts[0]
D = [T for T in Ts if len(C - T) == 6][0]
ok(D not in fam[C], 'C and D are in different families: moves of five or fewer cannot connect them')
ok(len(C - D) == 6, 'C to D in one move needs six trapezoids picked up')
print('all checks passed')
