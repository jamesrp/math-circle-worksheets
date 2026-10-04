"""Generate all TikZ figures into src/fig/."""
import os
from tri import *
from shapes import *
from analyze45 import rtype, ribbons, flipgraph, dists

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, 'fig')
os.makedirs(FIG, exist_ok=True)


def save(name, body):
    with open(os.path.join(FIG, name + '.tex'), 'w') as f:
        f.write(body + '\n')


def pic(body, scale=1.0, opts=''):
    return "\\begin{tikzpicture}[x=%gin,y=%gin%s]\n%s\n\\end{tikzpicture}" % (scale, scale, (',' + opts) if opts else '', body)


def label_at(region, text, dx=-0.12, where='nw'):
    x0, y0, x1, y1 = bbox(region)
    if where == 'nw':
        return "\\node[boardlabel,anchor=north east] at (%.3f,%.3f) {%s};" % (x0 + dx, y1, text)
    if where == 'n':
        return "\\node[boardlabel,anchor=south] at (%.3f,%.3f) {%s};" % ((x0 + x1) / 2, y1 + 0.08, text)


def board(region, holes=(), lab=None, scale=1.0, grid='grid', outline='outline', where='nw', extra=''):
    body = tikz_region(region, grid=grid, outline=outline, holes=holes, fill='boardfill')
    if lab:
        body += "\n" + label_at(frozenset(region) | frozenset(holes), lab, where=where)
    if extra:
        body += "\n" + extra
    return pic(body, scale)


COLORS = {'G': 'pgreen', 'B': 'pblue', 'R': 'pred', 'P': 'ppurple', 'Y': 'pyellow'}


def icon(piece, scale=0.6, rot=0):
    tris = frozenset(PIECES[piece])
    for _ in range(rot):
        tris = transform(tris, rot60)
    tris = normalize(tris)
    body = "\\fill[%s] %s;\n\\draw[iconline] %s;" % (COLORS[piece], path_of(tris), path_of(tris))
    return pic(body, scale)


# ======================================================================  K-1
def k1():
    h1 = hex_around(1, 1)
    save('k1_hex', board(h1, grid='kgrid', outline='koutline'))
    for p in 'GBRPY':
        rot = 5 if p == 'P' else 0
        save('k1_icon_' + p, icon(p, 0.55, rot))
    # tracing hexagons
    save('k1_hex_trace', board(h1, grid='kgrid', outline='koutline'))
    for n in (2, 3, 4, 5):
        save('k1_tri%d' % n, board(big_triangle(n), grid='kgrid', outline='koutline'))
    save('k1_bighex', board(HEX2, grid='kgrid', outline='koutline'))
    # small shapes for blue-only
    shapes = {
        'rh2': scale2([U(0, 0), D(0, 0)]),                       # 2x blue
        't2': big_triangle(2),                                     # 2x green
        'chev': normalize(transform(transform(transform(transform(transform(frozenset(PIECES['P']), rot60), rot60), rot60), rot60), rot60)),
        'trap': frozenset(PIECES['R']),
        'strip3': frozenset([U(0, 0), D(0, 0), U(1, 0), D(1, 0), U(2, 0), D(2, 0)]),
        't2rh': big_triangle(2) | frozenset([D(1, 0), U(2, 0)]),
    }
    for k, s in shapes.items():
        save('k1_shape_' + k, board(s, grid='kgrid', outline='koutline'))
        print('k1 shape', k, len(s), counts(s), 'blue tilings', len(tilings(s)))
    # grid for drawing
    save('k1_grid', pic(rect_grid(7.0, 6.1, 'kgrid'), 1.0))


def rect_grid(w, h, style):
    """triangular grid lines clipped to triangles fully inside [0,w]x[0,h]"""
    tris = set()
    for j in range(0, int(h / S) + 1):
        for i in range(-j, int(w) + 2):
            for k in 'UD':
                t = (k, i, j)
                pts = [cart(v) for v in verts(t)]
                if all(-1e-9 <= p[0] <= w + 1e-9 and -1e-9 <= p[1] <= h + 1e-9 for p in pts):
                    tris.add(t)
    es = all_edges(tris)
    return "\\draw[%s] %s;" % (style, " ".join(seg(e) for e in sorted(es, key=sorted)))


# ======================================================================  2-3
def g23():
    bs = [('A', star), ('B', trap2), ('C', boat), ('D', chev2), ('E', pinwheel)]
    for lab, r in bs:
        save('g23_board_' + lab, board(r, lab=lab))
        print('g23', lab, len(r), counts(r), 'tilings', len(tilings(r)))
    holesF = [D(0, -2), U(3, -3)]
    holesG = [D(0, -2), D(2, -2)]
    for lab, hs in (('F', holesF), ('G', holesG)):
        rest = HEX2 - frozenset(hs)
        print('g23', lab, counts(rest), 'tilings', len(tilings(rest)))
        save('g23_board_' + lab, board(rest, holes=hs, lab=lab))
    save('g23_board_H', board(HEX2, lab='H'))
    print('g23 J', len(dumbbell), counts(dumbbell), 'tilings', len(tilings(dumbbell)))
    save('g23_board_J', board(dumbbell, lab='J'))
    for n in (3, 4, 5, 6):
        save('g23_tri%d' % n, board(big_triangle(n)))
    save('g23_grid', pic(rect_grid(7.0, 5.3, 'grid'), 1.0))


# ======================================================================  4-5
def tiling_pic(region, tiling, scale, fills=None, grid=None, extra='', outline='outline'):
    body = ''
    body += "\\fill[boardfill] %s;\n" % path_of(region)
    body += tikz_tiling(tiling, fills=fills, outline='piece')
    body += "\n\\draw[%s] %s;" % (outline, path_of(region))
    if extra:
        body += "\n" + extra
    return pic(body, scale)


def g45():
    A, _ = hexagon(1, 2, 2)
    B, _ = hexagon(1, 2, 3)
    C, _ = hexagon(2, 2, 2)
    save('g45_board_A', board(A, lab='A'))
    save('g45_board_B', board(B, lab='B'))
    save('g45_board_C', board(C, lab='C'))
    save('g45_copy_A', board(A, scale=0.5, grid='cgrid', outline='coutline'))
    save('g45_copy_C', board(C, scale=0.34, grid='cgrid', outline='coutline'))
    big, _ = hexagon(1, 4, 4)
    save('g45_sketch_144', board(big, scale=0.32, grid='cgrid', outline='coutline'))

    # flip picture: two fillings of a unit hexagon
    h = hex_around(1, 1)
    T = tilings(h)
    assert len(T) == 2
    p0 = tiling_pic(h, T[0], 0.75, default_fill_style())
    p1 = tiling_pic(h, T[1], 0.75, default_fill_style())
    save('g45_flip_0', p0)
    save('g45_flip_1', p1)

    # ribbon example on hexagon (1,3,1): ribbon RLRR
    E, _ = hexagon(1, 3, 1)
    for t in tilings(E):
        w = ribbons(t, E)
        if w == ['RLRR']:
            ex = t
    rib = ribbon_pieces(ex, E)
    letters = ''
    for s in rib:
        cx = sum(centroid(x)[0] for x in s) / 2
        cy = sum(centroid(x)[1] for x in s) / 2
        letters += "\\node[ribbonletter] at (%.3f,%.3f) {%s};\n" % (cx, cy, rtype(s))
    fills = lambda name, s: 'ribbonfill' if s in rib else 'pfill'
    save('g45_ribbon_example', tiling_pic(E, ex, 0.8, fills, extra=letters))

    # board C: choose X, Y
    T, keys, adj = flipgraph(C)
    words = {k: ribbons(t, C) for k, t in zip(keys, T)}
    tmap = {k: t for k, t in zip(keys, T)}
    leaves = [k for k in keys if len(adj[k]) == 1]
    d = dists(adj, leaves[0])
    far = [k for k in keys if d[k] == 8]
    print('leaves', [words[k] for k in leaves], 'far', [words[k] for k in far])
    # pick X, Y at distance 4, neither a leaf, not mirror images trivially
    cands = []
    for x in keys:
        dx = dists(adj, x)
        for y in keys:
            if dx[y] == 4 and len(adj[x]) >= 2 and len(adj[y]) >= 2:
                cands.append((words[x], words[y], len(adj[x]), len(adj[y])))
    print('candidates d=4:', len(cands))
    for c in cands[:40]:
        print('  ', c)
    return C, keys, adj, words, tmap


def default_fill_style():
    return lambda name, s: 'pfill'


def ribbon_pieces(tiling, region):
    """pieces of all ribbons from top edges"""
    pieces = [s for _, s in tiling]
    top = {}
    for s in pieces:
        if rtype(s) == 'S':
            continue
        d = [x for x in s if x[0] == 'D'][0]
        k, i, j = d
        top[((i, j + 1), (i + 1, j + 1))] = s
    jmax = max(v[1] for t in region for v in verts(t))
    out = []
    for e in [e for e in top if e[0][1] == jmax]:
        while e in top:
            s = top[e]
            out.append(s)
            u = [x for x in s if x[0] == 'U'][0]
            e = ((u[1], u[2]), (u[1] + 1, u[2]))
    return out


if __name__ == '__main__':
    k1()
    g23()
    g45()


def g45_extra():
    C, _ = hexagon(2, 2, 2)
    T, keys, adj = flipgraph(C)
    words = {k: ribbons(t, C) for k, t in zip(keys, T)}
    tmap = {k: t for k, t in zip(keys, T)}
    byw = {tuple(words[k]): k for k in keys}
    X = byw[('LRRL', 'LRRL')]
    Y = byw[('RLLR', 'RLLR')]
    print('X->Y distance', dists(adj, X)[Y])
    save('g45_X', tiling_pic(C, tmap[X], 0.55, default_fill_style()))
    save('g45_Y', tiling_pic(C, tmap[Y], 0.55, default_fill_style()))
    Z = byw[('LRRL', 'RLRL')]
    shade = {'L': 'cubeL', 'R': 'cubeR', 'S': 'cubeS'}
    body = tiling_pic(C, tmap[Z], 0.6, lambda n, s: shade[rtype(s)])
    body = body.replace('[x=0.6in,y=0.6in]', '[x=0.6in,y=0.6in,rotate=90]')
    save('g45_cubes', body)
    # board A facts
    A, _ = hexagon(1, 2, 2)
    TA, kA, adjA = flipgraph(A)
    wA = {k: ribbons(t, A) for k, t in zip(kA, TA)}
    a0 = [k for k in kA if wA[k] == ['LLRR']][0]
    a1 = [k for k in kA if wA[k] == ['RRLL']][0]
    print('A: LLRR->RRLL', dists(adjA, a0)[a1])


g45_extra()
