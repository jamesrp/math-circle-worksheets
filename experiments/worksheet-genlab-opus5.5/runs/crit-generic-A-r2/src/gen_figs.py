"""Generate every TikZ figure used by the three packets into src/figs/."""
import os
from tri import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'figs')
os.makedirs(OUT, exist_ok=True)


def save(name, s):
    with open(os.path.join(OUT, name + '.tex'), 'w') as f:
        f.write(s.rstrip() + '%')


def R(poly):
    return region_from_poly(poly)


# ------------------------------------------------------------------ shapes
hex1 = R(hexagon_poly(1, 1, 1))
h211 = R(hexagon_poly(2, 1, 1))
h221 = R(hexagon_poly(2, 2, 1))
h222 = R(hexagon_poly(2, 2, 2))
h133 = R(hexagon_poly(1, 3, 3))
tri = {n: R(triangle_poly(n)) for n in range(2, 6)}
rhomb2 = R([(0, 0), (2, 0), (2, 2), (0, 2)])
para32 = R([(0, 0), (3, 0), (3, 2), (0, 2)])
trap2 = R([(0, 0), (4, 0), (2, 2), (0, 2)])
trap31 = R([(0, 0), (3, 0), (1, 2), (0, 2)])
boat = R([(0, 0), (3, 0), (2, 1), (1, 1), (0, 2)])
strip6 = R([(0, 0), (3, 0), (3, 1), (0, 1)])
v = (0, 0)
ring = around(v)
chev = frozenset(ring[1:5])  # opens to the right
bumptri = tri[3] | {('D', -1, 1)}

checks = {
    'hex1': (hex1, 6), 'h211': (h211, 10), 'h221': (h221, 16), 'h222': (h222, 24), 'h133': (h133, 30),
    'rhomb2': (rhomb2, 8), 'para32': (para32, 12), 'trap2': (trap2, 12), 'trap31': (trap31, 8),
    'boat': (boat, 6), 'strip6': (strip6, 6), 'chev': (chev, 4), 'bumptri': (bumptri, 10),
}
for k, (cs, n) in checks.items():
    assert len(cs) == n, (k, len(cs))
    m = max_matching(cs)
    print('%-8s cells %2d  up/down %s  blue-coverable %s' % (k, len(cs), counts(cs), 2 * len(m) == len(cs)))

GRID = dict(grid_color='black!28', grid_w=0.5)

# ------------------------------------------------------------------ plain boards (actual size)
for name, cs in [('hex1', hex1), ('h211', h211), ('h221', h221), ('h222', h222), ('h133', h133),
                 ('rhomb2', rhomb2), ('para32', para32), ('trap2', trap2), ('trap31', trap31),
                 ('boat', boat), ('strip6', strip6), ('chev', chev), ('bumptri', bumptri),
                 ('tri2', tri[2]), ('tri3', tri[3]), ('tri4', tri[4]), ('tri5', tri[5])]:
    save(name, tikz(cs, scale=1.0, **GRID))

# ------------------------------------------------------------------ move picture
A = [frozenset((ring[0], ring[1])), frozenset((ring[2], ring[3])), frozenset((ring[4], ring[5]))]
B = [frozenset((ring[1], ring[2])), frozenset((ring[3], ring[4])), frozenset((ring[5], ring[0]))]
hexring = set(ring)
for sc, tag in [(1.0, 'k1'), (0.7, 'g45')]:
    save('moveA_' + tag, tikz(hexring, scale=sc, tiling=A, grid=True, grid_color='black!18', grid_w=0.4, tile_w=1.3))
    save('moveB_' + tag, tikz(hexring, scale=sc, tiling=B, grid=True, grid_color='black!18', grid_w=0.4, tile_w=1.3))


# ------------------------------------------------------------------ tilings by chain words
def tilings_by_words(cs):
    T = [frozenset(t) for t in all_tilings(cs)]
    return {tuple(w for w, _ in chains(t, cs)): t for t in T}


W221 = tilings_by_words(h221)
W222 = tilings_by_words(h222)


def draw_tiling(cs, t, scale, name, shade_chain=None, grid=True):
    fills = []
    if shade_chain is not None:
        ch = chains(t, cs)[shade_chain][1]
        fills.append((set(c for r in ch for c in r), 'black!22'))
    save(name, tikz(cs, scale=scale, tiling=t, grid=grid, fills=fills, grid_color='black!15', grid_w=0.35,
                    tile_w=1.1 if scale > 0.8 else 0.9, outline_w=1.6 if scale > 0.8 else 1.2))


# K-1 Problem 5 puzzles on h221 (actual size)
k1_pairs = [(('RLR', 'RLR'), ('LRR', 'RRL')), (('LRR', 'LRR'), ('RRL', 'RRL'))]
for i, (s, t) in enumerate(k1_pairs):
    draw_tiling(h221, W221[s], 1.0, 'k1_p5_%d_start' % i)
    draw_tiling(h221, W221[t], 1.0, 'k1_p5_%d_end' % i)

# grades 4-5 Problem 3 pairs (small pictures)
g45_pairs = [(('LLRR', 'LLRR'), ('RRLL', 'RRLL')), (('LRRL', 'LRRL'), ('RLLR', 'RLLR'))]
for i, (s, t) in enumerate(g45_pairs):
    draw_tiling(h222, W222[s], 0.5, 'g45_p3_%d_start' % i)
    draw_tiling(h222, W222[t], 0.5, 'g45_p3_%d_end' % i)

# grades 4-5 Problem 5: example with shaded left chain, and four coverings
draw_tiling(h222, W222[('RLLR', 'RLRL')], 0.75, 'g45_p5_example', shade_chain=0)
for i, w in enumerate([('LLRR', 'RRLL'), ('LRLR', 'RLRL'), ('LRRL', 'LRRL'), ('RRLL', 'RRLL')]):
    draw_tiling(h222, W222[w], 0.55, 'g45_p5_%d' % i)

# L and R single blocks for the chain picture
uL = ('U', 0, 0)
Lblock = {uL, ('D', -1, 0)}
Rblock = {uL, ('D', 0, 0)}
save('blockL', tikz(Lblock, scale=0.5, grid=False, outline_w=1.0, extra=''))
save('blockR', tikz(Rblock, scale=0.5, grid=False, outline_w=1.0, extra=''))

# small blank copies for recording
for name, cs, sc in [('h221_small', h221, 0.5), ('h222_small', h222, 0.42), ('h222_small55', h222, 0.5)]:
    save(name, tikz(cs, scale=sc, grid=True, grid_color='black!22', grid_w=0.35, outline_w=1.1))

# ------------------------------------------------------------------ holes (grades 2-3 Problem 3)
holes = [
    [('U', 0, 0), ('D', -1, 3)],   # up + down, far apart: coverable
    [('U', 0, 0), ('U', 1, 2)],    # two up: not coverable
    [('D', -1, 1), ('D', 0, 2)],   # two down: not coverable
    [('U', -2, 3), ('D', 0, 1)],   # up + down: coverable
]
for i, hs in enumerate(holes):
    rest = h222 - set(hs)
    ok = 2 * len(max_matching(rest)) == len(rest)
    print('hole board', i, hs, 'up/down left', counts(rest), 'coverable', ok)
    save('holes_%d' % i, tikz(h222, scale=1.0, fills=[(set(hs), 'black!55')], **GRID))

# ------------------------------------------------------------------ triangular grid paper (actual size)
def grid_paper(width_in, height_in):
    rows = int(height_in / S)
    cells = set()
    for b in range(rows):
        for a in range(-rows, int(width_in) + rows):
            for t in 'UD':
                c = (t, a, b)
                xs = [cart(p)[0] for p in corners(c)]
                if min(xs) >= -1e-9 and max(xs) <= width_in + 1e-9:
                    cells.add(c)
    es = set()
    for c in cells:
        for e in edges(c):
            es.add(e)
    lines = ['\\begin{tikzpicture}[x=1in,y=1in,line cap=round]']
    lines.append('\\draw[black!35,line width=0.5pt] %s;' % ' '.join(seg(e) for e in sorted(es, key=sorted)))
    lines.append('\\end{tikzpicture}')
    return '\n'.join(lines)


save('gridpaper', grid_paper(7.0, 6.2))

# ------------------------------------------------------------------ icon
save('greenicon', '\\begin{tikzpicture}[x=0.32in,y=0.32in]\\filldraw[fill=green!55!black!45,draw=black,line width=0.8pt] (0,0)--(1,0)--(0.5,0.866)--cycle;\\end{tikzpicture}')

for k, (cs, n) in {'h221': (h221, 0), 'h222': (h222, 0), 'h133': (h133, 0)}.items():
    print(k, 'bbox', [round(x, 3) for x in bbox(cs)])

# K-1 Problem 5 targets drawn smaller, beside the actual-size starting board
for i, (s, t) in enumerate(k1_pairs):
    draw_tiling(h221, W221[t], 0.62, 'k1_p5_%d_end_small' % i)

strip5 = R([(0, 0), (3, 0), (2, 1), (0, 1)])
assert len(strip5) == 5
save('strip5', tikz(strip5, scale=1.0, **GRID))

# grades 4-5 extra sizes
for i, (s, t) in enumerate(g45_pairs):
    draw_tiling(h222, W222[s], 0.36, 'g45_p3_%d_start' % i)
    draw_tiling(h222, W222[t], 0.36, 'g45_p3_%d_end' % i)
for i, w in enumerate([('LLRR', 'RRLL'), ('LRLR', 'RLRL'), ('LRRL', 'LRRL'), ('RRLL', 'RRLL')]):
    draw_tiling(h222, W222[w], 0.5, 'g45_p5_%d' % i)
for name, cs, sc in [('h221_s50', h221, 0.5), ('h222_s40', h222, 0.4), ('h222_s45', h222, 0.45)]:
    save(name, tikz(cs, scale=sc, grid=True, grid_color='black!22', grid_w=0.35, outline_w=1.1))

for i, (s, t) in enumerate(g45_pairs):
    draw_tiling(h222, W222[s], 0.45, 'g45_p3_%d_start' % i)
    draw_tiling(h222, W222[t], 0.45, 'g45_p3_%d_end' % i)
for i, w in enumerate([('LLRR', 'RRLL'), ('LRLR', 'RLRL'), ('LRRL', 'LRRL'), ('RRLL', 'RRLL')]):
    draw_tiling(h222, W222[w], 0.44, 'g45_p5_%d' % i)
