"""Generate all TikZ figures for the three Week 1 packets and check the mathematics."""
import os
from tri import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figs')
os.makedirs(OUT, exist_ok=True)


def save(name, code):
    with open(os.path.join(OUT, name + '.tex'), 'w') as f:
        f.write(code + '\n')


def sectors(v, start, n):
    return frozenset(sector(v, start + k) for k in range(n))


BOARD = dict(outline_w='1.8pt', grid_color='black!40', grid_w='0.6pt')
SMALL = dict(outline_w='1.0pt', grid_color='black!25', grid_w='0.35pt')

# ------------------------------------------------------------ shapes
hex1 = hexagon(1, 1, 1)
tri2, tri3, tri4, tri5 = (big_triangle(n) for n in (2, 3, 4, 5))
trap3 = sectors((1, 0), 0, 3)
chev = sectors((1, 1), 1, 4)
rhomb2 = region_from_poly(turtle([(0, 2), (1, 2), (3, 2), (4, 2)]))
trap8 = tri3 - {(0, 2, 'U')}
long211 = hexagon(2, 1, 1)
trap2x = region_from_poly(turtle([(0, 4), (2, 2), (3, 2), (4, 2)]))
b122 = hexagon(1, 2, 2)
b132 = hexagon(1, 3, 2)
b133 = hexagon(1, 3, 3)
hex2 = hexagon(2, 2, 2)


def star():
    h = frozenset(sector((0, 0), k) for k in range(6))
    out = set(h)
    for t in h:
        for n in neighbors(t):
            if n not in h:
                out.add(n)
    return frozenset(out)


star12 = star()
up2 = big_triangle(2)
down2 = region_from_poly(turtle([(2, 2), (0, 2), (4, 2)], start=(0, 2)))
hourglass = up2 | down2


def strip(n):
    return frozenset((k // 2, 0, 'U') if k % 2 == 0 else (k // 2, 0, 'D') for k in range(n))


# ------------------------------------------------------------ checks
def blue_ok(R):
    return count_tilings(R, ('B',), limit=1) > 0


def check(cond, msg):
    assert cond, msg
    print('ok:', msg)


# K-1 Problem 1
check([blue_ok(x) for x in (hex1, tri2, rhomb2, trap3, chev, trap8)] ==
      [True, False, True, False, True, False], 'K-1 P1 yes/no pattern')
check(counts(trap8) == (5, 3) and len(tri2) == 4, 'K-1 P1 even-area impossible boards')
# K-1 Problem 2 / 2-3 Problem 3: fewest greens
for n, R in ((2, tri2), (3, tri3), (4, tri4), (5, tri5)):
    check(len(R) - 2 * max_matching(R) == n, f'triangle side {n} needs exactly {n} greens with blues')
# K-1 Problem 3
check(count_tilings(hex1) == 2 and count_tilings(long211) == 3, 'K-1 P3 counts 2 and 3')
# K-1 Problem 4 fewest blocks
KINDS = ['Y', 'P', 'R', 'B', 'G']
for R, m in ((tri3, 3), (rhomb2, 3), (trap2x, 4)):
    c, sol = min_pieces(R, KINDS)
    check(c == m, f'K-1 P4 fewest blocks {m}: {sorted(k for k, p in sol)}')
# K-1 Problem 5 games
res = {n: game_outcome(strip(n))[0] for n in (4, 5, 6, 7)}
check(res == {4: True, 5: False, 6: True, 7: True}, f'K-1 P5 strips first-player wins {res}')
check(game_outcome(hex1)[0] is False, 'K-1 P5 hexagon: second player wins')
# K-1 P6, 4-5 P1
check(count_tilings(b122) == 6, '1,2,2 board has 6 coverings')
# 2-3 Problem 1
check([blue_ok(x) for x in (star12, tri3, trap2x, long211)] == [True, False, False, True], '2-3 P1 pattern')
check(len(star12) == 12 and count_tilings(star12) == 1, 'star: 12 triangles, one covering')
check(counts(trap2x) == (7, 5), '2x trapezoid 7 up 5 down')
# 2-3 Problem 2
holesE = [(0, 0, 'U'), (0, 3, 'U')]
holesF = [(0, 0, 'U'), (-1, 3, 'D')]
for h in holesE + holesF:
    assert h in hex2
E23 = hex2 - set(holesE)
F23 = hex2 - set(holesF)
check(not blue_ok(E23) and blue_ok(F23) and not blue_ok(hourglass), '2-3 P2 pattern E no, F yes, hourglass no')
check(counts(hourglass) == (4, 4), 'hourglass balanced')
# 2-3 Problem 5 chevrons
for n, R, m in ((2, tri2, 4), (3, tri3, 5), (4, tri4, 4), (5, tri5, 5)):
    c, _ = min_pieces(R, ['P', 'G'], weight={'P': 0, 'G': 1})
    check(c == m, f'chevron+green on triangle {n}: {m}')
# 2-3 Problem 5: example of a 19-triangle one-piece board needing 5 greens (side-4 triangle plus 3 triangles)
grown = tri4 | {(-1, 0, 'D'), (-1, 0, 'U'), (-1, 1, 'U')}
check(len(grown) == 19 and len(grown) - 2 * max_matching(grown) == 5, '2-3 P5 example exists')
# 2-3 Problem 7: hexagon minus one up and one down always coverable
ups = [t for t in hex2 if t[2] == 'U']
downs = [t for t in hex2 if t[2] == 'D']
check(all(blue_ok(hex2 - {u, d}) for u in ups for d in downs), '2-3 P7 every up/down pair works')
check(not any(blue_ok(hex2 - {u, v}) for u in ups for v in ups if u < v), '2-3 P7 no same-direction pair works')
# 4-5
tl, adj = flip_graph(hex2)
check(len(tl) == 20 and count_tilings(b133) == 20, '4-5 counts 20 and 20')
rib = {t: tuple(ribbons(hex2, t)) for t in tl}
by_rib = {r: t for t, r in rib.items()}
dist = {i: bfs(adj, i) for i in adj}
idx = {t: i for i, t in enumerate(tl)}
PAIRS = [(('RLRL', 'RLRL'), ('LRRL', 'LRLR')), (('LRRL', 'LRRL'), ('RLLR', 'RLLR')), (('RRLL', 'RRLL'), ('LLRR', 'LLRR'))]
pair_d = [dist[idx[by_rib[a]]][idx[by_rib[b]]] for a, b in PAIRS]
check(pair_d == [3, 4, 8], f'4-5 P3 distances {pair_d}')
# bipartite: no odd cycles
col = {0: 0}
for x in bfs(adj, 0):
    pass
bip = all((dist[0][a] + dist[0][b]) % 2 == 1 for a in adj for b in adj[a])
check(bip, 'flip graph of 2,2,2 is bipartite')
a0 = idx[by_rib[PAIRS[0][0]]]
c4 = sum(1 for b in adj[a0] for c in adj[b] if c != a0 for d in adj[c] if d != b and d != a0 and a0 in adj[d])
check(c4 > 0, '4-5 P4: a 4-flip round trip from covering A exists')

# ------------------------------------------------------------ K-1 figures
for name, R in (('k1_hex', hex1), ('k1_tri2', tri2), ('k1_rhomb2', rhomb2), ('k1_trap3', trap3),
                 ('k1_chev', chev), ('k1_trap8', trap8), ('k1_tri3', tri3), ('k1_tri4', tri4),
                 ('k1_long', long211), ('k1_trap2x', trap2x), ('k1_b122', b122)):
    save(name, tikz_region(R, **BOARD))
for n in (4, 5, 6, 7):
    save(f'k1_strip{n}', tikz_region(strip(n), **BOARD))
save('k1_b122_small', tikz_region(b122, scale=0.5, **SMALL))

# piece icons
ICON = {'G': sectors((0, 0), 0, 1), 'B': sectors((0, 0), 0, 2), 'R': sectors((0, 0), 0, 3),
        'Y': sectors((0, 0), 0, 6), 'P': sectors((0, 0), 1, 4)}
for k, p in ICON.items():
    sc = 0.2 if k in 'GBR' else 0.135
    save(f'icon_{k}', tikz_region(p, scale=sc, grid=False, tiles=[(k, p)], outline_w='0.6pt'))
    save(f'iconbig_{k}', tikz_region(p, scale=0.3, grid=False, tiles=[(k, p)], outline_w='0.8pt'))

# ------------------------------------------------------------ 2-3 figures
for name, R in (('g23_star', star12), ('g23_tri3', tri3), ('g23_trap2x', trap2x), ('g23_long', long211),
                ('g23_tri2', tri2), ('g23_tri4', tri4), ('g23_tri5', tri5), ('g23_hourglass', hourglass),
                ('g23_hex2', hex2)):
    save(name, tikz_region(R, **BOARD))
save('g23_E', tikz_region(E23, holes=holesE, **BOARD))
save('g23_F', tikz_region(F23, holes=holesF, **BOARD))


def tri_grid(width_in, height_in):
    """Actual-size triangular grid lines clipped to a rectangle."""
    L = [f"\\begin{{tikzpicture}}[x=1in,y=1in]",
         f"\\clip (0,0) rectangle ({width_in},{height_in});"]
    rows = int(height_in / S3) + 2
    for r in range(rows + 1):
        y = r * S3
        L.append(f"\\draw[black!40,line width=0.6pt] (-1,{fmt(y)})--({width_in + 1},{fmt(y)});")
    # slanted lines through lattice points on y=0 and above
    span = int(width_in + height_in) + 4
    for i in range(-span, span + 1):
        x0 = i
        # 60 degree line: points (x0 + t/2, t*S3)
        L.append(f"\\draw[black!40,line width=0.6pt] ({fmt(x0 - 6)},{fmt(-12 * S3)})--({fmt(x0 + 6)},{fmt(12 * S3)});")
        L.append(f"\\draw[black!40,line width=0.6pt] ({fmt(x0 + 6)},{fmt(-12 * S3)})--({fmt(x0 - 6)},{fmt(12 * S3)});")
    L.append(f"\\end{{tikzpicture}}")
    return "\n".join(L)


save('g23_grid', tri_grid(7.0, round(7 * S3, 4)))
save('g23_hex2_small', tikz_region(hex2, scale=0.3, **SMALL))

# ------------------------------------------------------------ 4-5 figures
save('g45_b122', tikz_region(b122, **BOARD))
save('g45_b122_small', tikz_region(b122, scale=0.4, **SMALL))
save('g45_hex2', tikz_region(hex2, **BOARD))
save('g45_b133', tikz_region(b133, **BOARD))
save('g45_hex2_small', tikz_region(hex2, scale=0.3, **SMALL))

TILEFILL = 'pbblue!45'


def draw_tiling(R, tiling, scale, label_ribbon=False, highlight=None, letters=True, grid=False):
    tiles = []
    for p in tiling:
        col = TILEFILL
        if highlight and p in highlight:
            col = 'pbblue!95!black'
        tiles.append((col, p))
    extra = ''
    if label_ribbon and highlight:
        x0, y0, _, _ = bbox(R)
        for p in highlight:
            cs = [centroid(t) for t in p]
            cx = sum(c[0] for c in cs) / len(cs) - x0
            cy = sum(c[1] for c in cs) / len(cs) - y0
            extra += f"\\node[white,font=\\bfseries\\small] at ({fmt(cx)},{fmt(cy)}) {{{lozenge_type(p)}}};\n"
    return tikz_region(R, scale=scale, grid=grid, tiles=tiles, outline_w='1.3pt', tile_w='0.7pt', extra=extra,
                       grid_color=SMALL['grid_color'], grid_w=SMALL['grid_w'])


names = 'ABCDEF'
for k, (a, b) in enumerate(PAIRS):
    save(f'g45_pair_{names[2 * k]}', draw_tiling(hex2, by_rib[a], 0.36, grid=True))
    save(f'g45_pair_{names[2 * k + 1]}', draw_tiling(hex2, by_rib[b], 0.36, grid=True))

# flip picture: unit hexagon two ways
hA = [sectors((0, 0), 0, 2), sectors((0, 0), 2, 2), sectors((0, 0), 4, 2)]
hB = [sectors((0, 0), 1, 2), sectors((0, 0), 3, 2), sectors((0, 0), 5, 2)]
save('g45_flipA', draw_tiling(hex1 if False else frozenset(sector((0, 0), k) for k in range(6)), hA, 0.55))
save('g45_flipB', draw_tiling(frozenset(sector((0, 0), k) for k in range(6)), hB, 0.55))

# ribbon example on the 1,3,2 board
tl132 = all_lozenge_tilings(b132)
target = None
for t in tl132:
    if ribbons(b132, t) == ['LRRLR']:
        target = t
assert target is not None, [ribbons(b132, t) for t in tl132]
# collect the ribbon tiles
tri_to_tile = {}
for p in target:
    for t in p:
        tri_to_tile[t] = p
chain = []
topj = max(t[1] for t in b132 if t[2] == 'D')
cur = [t for t in b132 if t[2] == 'D' and t[1] == topj][0]
while cur in tri_to_tile:
    p = tri_to_tile[cur]
    chain.append(p)
    u = [t for t in p if t[2] == 'U'][0]
    cur = (u[0], u[1] - 1, 'D')
check(''.join(lozenge_type(p) for p in chain) == 'LRRLR', 'ribbon example reads LRRLR')
save('g45_ribbon_example', draw_tiling(b132, target, 0.55, label_ribbon=True, highlight=set(chain)))
# single L and R rhombi
Lr = frozenset([(1, 0, 'U'), (0, 0, 'D')])
Rr = frozenset([(0, 0, 'U'), (0, 0, 'D')])
check(lozenge_type(Lr) == 'L' and lozenge_type(Rr) == 'R', 'L/R icons')
save('g45_Lrh', tikz_region(Lr, scale=0.45, grid=False, tiles=[(TILEFILL, Lr)], outline_w='1.0pt'))
save('g45_Rrh', tikz_region(Rr, scale=0.45, grid=False, tiles=[(TILEFILL, Rr)], outline_w='1.0pt'))

print('figures written to', OUT)
