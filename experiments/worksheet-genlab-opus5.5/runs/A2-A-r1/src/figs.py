"""Generate every TikZ figure block for the three Week 1 packets.

Run:  python3 figs.py      (writes src/figs/*.tex and prints checks)

All boards on which blocks are placed are drawn with 1 unit = 1 inch, so the
small triangle edge is exactly 1 inch when printed at 100%.
"""
import os
import sys
from geom import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'figs')
os.makedirs(OUT, exist_ok=True)
TW = 7.4  # text width in inches

CHECKS = []


def check(cond, msg):
    CHECKS.append((bool(cond), msg))
    if not cond:
        print('CHECK FAILED:', msg)


# ------------------------------------------------------------------ helpers

class Pic:
    """A block of figures with origin at its top-left; y grows upward (use negative y)."""

    def __init__(self, height, width=TW):
        self.h = height
        self.w = width
        self.items = []

    def board(self, region, x, ytop, scale=1.0, **kw):
        """Place region with its bounding box's top-left corner at (x, ytop)."""
        off, (w, h) = offset_of(region)
        if x < -1e-6 or x + w * scale > self.w + 1e-6 or ytop > 1e-6 or ytop - h * scale < -self.h - 1e-6:
            print('OUT OF BOUNDS: board at x=%.2f..%.2f y=%.2f..%.2f in pic %.2f x %.2f'
                  % (x, x + w * scale, ytop, ytop - h * scale, self.w, self.h))
        code = tikz_board(region, wrap=False, off=off, **kw)
        self.items.append('\\begin{scope}[shift={(%s,%s)},scale=%s]\n%s\n\\end{scope}'
                          % (fmt(x), fmt(ytop - h * scale), fmt(scale), code))
        return (x, ytop, w * scale, h * scale)

    def text(self, x, y, s, anchor='north west', size='\\normalsize'):
        self.items.append('\\node[anchor=%s,inner sep=0pt,font=%s] at (%s,%s) {%s};'
                          % (anchor, size, fmt(x), fmt(y), s))

    def raw(self, s):
        self.items.append(s)

    def lines(self, x, ytop, width, n, gap=0.4):
        for k in range(n):
            y = ytop - gap * (k + 1)
            self.items.append('\\draw[writeline] (%s,%s) -- (%s,%s);'
                              % (fmt(x), fmt(y), fmt(x + width), fmt(y)))
        return ytop - gap * n

    def tex(self):
        return ('\\begin{tikzpicture}[x=1in,y=1in,line join=round,line cap=round]\n'
                '\\path[use as bounding box] (0,0) rectangle (%s,%s);\n%s\n\\end{tikzpicture}'
                % (fmt(self.w), fmt(-self.h), '\n'.join(self.items)))

    def save(self, name):
        with open(os.path.join(OUT, name + '.tex'), 'w') as f:
            f.write(self.tex() + '\n')


def save_raw(name, code):
    with open(os.path.join(OUT, name + '.tex'), 'w') as f:
        f.write(code + '\n')


BLOCKS = {
    'G': frozenset([('U', 0, 0)]),
    'B': frozenset([('U', 0, 0), ('D', 0, 0)]),
    'R': frozenset([('U', 0, 0), ('D', 0, 0), ('U', 1, 0)]),
    'Y': hex_around((1, 1)),
    'P': frozenset([('U', 0, 0), ('D', 0, 0), ('U', 0, 1), ('D', -1, 1)]),
}
BLOCKNAME = {'G': 'green triangle', 'B': 'blue rhombus', 'R': 'red trapezoid',
             'Y': 'yellow hexagon', 'P': 'purple chevron'}


def icon_code(kind, scale):
    tris = BLOCKS[kind]
    off, (w, h) = offset_of(tris)
    paths = piece_outline(tris)
    p = paths[0]
    s = ' -- '.join(pstr(q, off) for q in p[:-1]) + ' -- cycle'
    code = '\\filldraw[fill=block%s,line width=0.9pt] %s;' % (kind, s)
    return code, w, h


def icon(pic, kind, x, ycenter, scale=0.5):
    code, w, h = icon_code(kind, scale)
    pic.raw('\\begin{scope}[shift={(%s,%s)},scale=%s]%s\\end{scope}'
            % (fmt(x), fmt(ycenter - h * scale / 2), fmt(scale), code))
    return w * scale


def icon_row(kinds, scale=0.45, labels=True, size='\\normalsize', gap=0.35):
    """A one-line strip of block icons with names."""
    widths = []
    for k in kinds:
        _, w, h = icon_code(k, scale)
        widths.append(w * scale)
    hmax = max(icon_code(k, scale)[2] for k in kinds) * scale
    pic = Pic(hmax + 0.04)
    x = 0.0
    for k, w in zip(kinds, widths):
        icon(pic, k, x, -hmax / 2 - 0.02, scale)
        x += w + 0.08
        if labels:
            pic.text(x, -hmax / 2 - 0.02, BLOCKNAME[k], anchor='west', size=size)
            x += 0.105 * len(BLOCKNAME[k]) * (1.0 if size == '\\normalsize' else 1.15)
        x += gap
    pic.w = x
    return pic


def inline_icon(kind, scale=0.4):
    code, w, h = icon_code(kind, scale)
    return ('\\tikz[x=1in,y=1in,line join=round,baseline={([yshift=-.5ex]current bounding box.center)}]'
            '{\\begin{scope}[scale=%s]%s\\end{scope}}%%' % (fmt(scale), code))


def pieces_of(tiling):
    return [('B', r) for r in tiling]


# ------------------------------------------------------------------ regions

def trap_bottom(bottom, top, height):
    return poly_region((0, 0), [('E', bottom), ('NW', height), ('W', top), ('SW', height)])


TRI = {n: up_triangle(n) for n in range(1, 7)}
HEX111 = hexagon(1, 1, 1)
HEX211 = hexagon(2, 1, 1)
HEX311 = hexagon(3, 1, 1)
HEX221 = hexagon(2, 2, 1)
HEX222 = hexagon(2, 2, 2)
RH2 = poly_region((0, 0), [('E', 2), ('NE', 2), ('W', 2), ('SW', 2)])
TRAP13 = trap_bottom(3, 1, 2)
TRAP24 = trap_bottom(4, 2, 2)          # red trapezoid at 2x
PAR31 = poly_region((0, 0), [('E', 3), ('NE', 1), ('W', 3), ('SW', 1)])
STAR = up_triangle(3, (0, 0)) | down_triangle(3, (2, -1))


def corner_tris(region):
    """Triangles touching each extreme vertex: returns dict name -> list of triangles."""
    pts = {}
    for t in region:
        for v in verts(t):
            pts.setdefault(v, []).append(t)
    cs = {v: cart(v) for v in pts}
    xs = [c[0] for c in cs.values()]
    ys = [c[1] for c in cs.values()]
    res = {}
    for v, c in cs.items():
        name = None
        if abs(c[0] - min(xs)) < 1e-9:
            name = 'left'
        elif abs(c[0] - max(xs)) < 1e-9:
            name = 'right'
        if name:
            res[name] = pts[v]
    return res


# ============================================================ K-1 packet

def k1():
    # ---- Problem 1: cover the hexagon in different ways (9 outlines, actual size)
    w, h = bbox_in(HEX111)
    gx = (TW - 3 * w) / 2
    rows = 3
    gy = 0.35
    pic = Pic(rows * h + (rows - 1) * gy + 0.05)
    for r in range(rows):
        for c in range(3):
            pic.board(HEX111, c * (w + gx), -r * (h + gy), grid=True)
    pic.save('k1_p1_hexes')
    mixes = all_mixes(HEX111, 'GBR')
    check(len(mixes) == 7, 'K-1 P1: hexagon has 7 mixes of G/B/R: %s' % sorted(mixes))

    # ---- Problem 2: fewest blocks (actual size)
    n3, s3 = min_pieces(TRI[3])
    nr, sr = min_pieces(RH2)
    nh, sh = min_pieces(HEX222)
    check((n3, nr, nh) == (3, 3, 6), 'K-1 P2 fewest blocks tri3=%d rh2=%d hex2=%d' % (n3, nr, nh))
    bl = 'blocks: \\underline{\\hspace{0.9in}}'
    pic = Pic(7.2)
    pic.board(TRI[3], 0.4, 0)
    pic.board(RH2, 4.0, -(2.598 - 1.732) / 2)
    pic.text(0.4, -2.598 - 0.25, bl)
    pic.text(4.0, -2.598 - 0.25, bl)
    y2 = -3.65
    pic.board(HEX222, 0.4, y2)
    pic.text(4.9, y2 - 1.732, bl, anchor='west')
    pic.save('k1_p2_fewest')

    # ---- Problem 3: blue only, yes / no
    yesno = '\\textbf{yes}\\hspace{0.5in}\\textbf{no}'
    shapes = [PAR31, TRI[2], HEX211, TRAP24, STAR]
    expect = [True, False, True, False, True]
    for s, e in zip(shapes, expect):
        check(tileable(s) == e, 'K-1 P3 shape tileable == %s' % e)
    pic = Pic(7.3)
    def yn(xc, ybot):
        pic.text(xc, ybot - 0.25, yesno, anchor='north')
    # left column
    pic.board(PAR31, 0.1, -0.1)
    yn(0.1 + 1.75, -0.966)
    pic.board(HEX211, 0.1, -2.0)
    yn(0.1 + 1.5, -2.0 - 1.732)
    pic.board(TRAP24, 0.1, -4.75)
    yn(0.1 + 2.0, -4.75 - 1.732)
    # right column
    pic.board(TRI[2], 4.8, 0)
    yn(4.8 + 1.0, -1.732)
    pic.board(STAR, 4.3, -2.75)
    yn(4.3 + 1.5, -2.75 - 3.464)
    pic.save('k1_p3_blue')

    # ---- Problem 4: blue + green, fewest greens on triangles 2, 3, 4
    for n in (2, 3, 4):
        check(min_greens(TRI[n]) == n, 'K-1 P4 triangle %d needs %d greens' % (n, n))
    pic = Pic(2.6 + 0.75 + 0.3 + 3.464 + 0.75)
    pic.board(TRI[2], 0.6, -(2.598 - 1.732))
    pic.board(TRI[3], 3.8, 0)
    yb = -2.598 - 0.3
    gl = 'green triangles: \\underline{\\hspace{0.7in}}'
    pic.text(0.3, yb, gl)
    pic.text(3.8, yb, gl)
    y2 = yb - 0.75
    pic.board(TRI[4], (TW - 4) / 2, y2)
    pic.text((TW - 4) / 2, y2 - 3.464 - 0.3, gl)
    pic.save('k1_p4_greens')

    # ---- Problem 5: blue only, find all the ways (hex111 x3, hex211 x4)
    check(len(rhombus_tilings(HEX111)) == 2 and len(rhombus_tilings(HEX211)) == 3,
          'K-1 P5: 2 and 3 tilings')
    w1, h1 = bbox_in(HEX111)
    w2, h2 = bbox_in(HEX211)
    gy = 0.45
    pic = Pic(3 * h1 + 2 * gy + 0.05)
    g1 = (TW - 3 * w1) / 2
    for c in range(3):
        pic.board(HEX111, c * (w1 + g1), 0)
    g2 = 0.9
    x0 = (TW - 2 * w2 - g2) / 2
    for r in range(2):
        for c in range(2):
            pic.board(HEX211, x0 + c * (w2 + g2), -(r + 1) * (h1 + gy))
    pic.save('k1_p5_ways')



# ============================================================ grades 2-3 packet

def g23():
    # ---- Problem 1: boards A-D, blue only
    yesno = 'Can it be done?\\quad yes\\quad no'
    pic = Pic(6.5)
    lab = lambda L: '\\textbf{\\Large %s}' % L
    check(not tileable(TRAP13) and counts(TRAP13) == (5, 3), '2-3 P1 A impossible')
    check(tileable(RH2), '2-3 P1 B possible')
    check(not tileable(TRAP24) and counts(TRAP24) == (7, 5), '2-3 P1 C impossible')
    check(tileable(STAR) and len(rhombus_tilings(STAR)) == 1, '2-3 P1 D possible (unique)')
    pic.text(0, 0, lab('A'))
    pic.board(TRAP13, 0.35, 0)
    pic.text(0.35, -1.732 - 0.15, yesno)
    pic.text(3.9, 0, lab('B'))
    pic.board(RH2, 4.25, 0)
    pic.text(4.25, -1.732 - 0.15, yesno)
    y = -2.55
    pic.text(0, y, lab('C'))
    pic.board(TRAP24, 0.25, y)
    pic.text(0.25, y - 1.732 - 0.15, yesno)
    pic.text(4.4, y, lab('D'))
    pic.board(STAR, 4.4, y)
    pic.text(4.4, y - 3.464 - 0.15, yesno)
    pic.save('g23_p1')

    # ---- Problem 2: triangles E (2), F (3), G (4) on one page, H (5) next page
    for n in (2, 3, 4, 5):
        check(min_greens(TRI[n]) == n, '2-3 P2 triangle %d needs %d' % (n, n))
    gl = 'green triangles: \\underline{\\hspace{0.7in}}'
    pic = Pic(2.598 + 0.7 + 0.3 + 3.464 + 0.6)
    pic.text(0, -0.866, lab('E'))
    pic.board(TRI[2], 0.4, -0.866)
    pic.text(0.4, -2.598 - 0.25, gl)
    pic.text(3.6, 0, lab('F'))
    pic.board(TRI[3], 4.0, 0)
    pic.text(4.0, -2.598 - 0.25, gl)
    y = -2.598 - 0.95
    pic.text(0.8, y, lab('G'))
    pic.board(TRI[4], 1.2, y)
    pic.text(1.2, y - 3.464 - 0.25, gl)
    pic.save('g23_p2a')
    pic = Pic(4.33 + 0.65)
    pic.text(0.8, 0, lab('H'))
    pic.board(TRI[5], 1.2, 0)
    pic.text(1.2, -4.33 - 0.25, gl)
    pic.save('g23_p2b')

    # ---- Problem 3: chevron icon (inline) -- checks
    # A chevron is two blue rhombi, so it can never beat blue rhombi.
    chev = BLOCKS['P']
    check(len(rhombus_tilings(chev)) == 1, 'chevron is exactly two blues')

    # ---- Problem 4: hexagon with two black triangles
    E = HEX221
    holes = {
        'J': [('U', -2, 2), ('U', 1, 1)],   # two ups at the two ends: impossible
        'K': [('U', -2, 2), ('D', 1, 0)],   # an up and a down at the two ends: possible
        'L': [('U', 0, 1), ('D', -2, 1)],   # an up and a down: possible
        'M': [('D', -1, 0), ('D', -1, 2)],  # two downs: impossible
    }
    expect = {'J': False, 'K': True, 'L': True, 'M': False}
    for k, hs in holes.items():
        assert all(h in E for h in hs)
        ok = tileable(E - set(hs))
        check(ok == expect[k], '2-3 P4 board %s tileable=%s holes=%s' % (k, ok, hs))
    yesno = 'Can it be done?\\quad yes\\quad no'
    w, h = bbox_in(E)
    pic = Pic(2 * (h + 0.5) + 0.3)
    for r, keys in enumerate((('J', 'K'), ('L', 'M'))):
        y = -r * (h + 0.8)
        for c, k in enumerate(keys):
            x = c * (TW - w)
            pic.board(E, x, y, black=holes[k])
            pic.text(x, y, lab(k))
            pic.text(x + 0.5, y - h - 0.15, yesno)
    pic.save('g23_p4')

    # ---- Problem 6: blank actual-size grid for designing a board
    # grid of up/down triangles in a parallelogram-free rectangle-ish strip
    rows = 4
    width = 7
    keep = set()
    for j in range(rows):
        for i in range(-rows - 3, width + 4):
            for kk in 'UD':
                t = (kk, i, j)
                c = centroid(t)
                if -1 <= c[0] <= width + 1:
                    keep.add(t)
    pic = Pic(rows * H + 0.05)
    # draw grid lines clipped to a rectangle
    code = ['\\begin{scope}', '\\clip (0,0) rectangle (%s,%s);' % (fmt(width), fmt(-rows * H))]
    for t in keep:
        vs = [cart(v) for v in verts(t)]
        code.append('\\draw[gridgray,line width=0.6pt] ' + ' -- '.join(
            '(%s,%s)' % (fmt(x), fmt(y - rows * H)) for x, y in vs) + ' -- cycle;')
    code.append('\\end{scope}')
    pic.raw('\\begin{scope}[shift={(%s,0)}]' % fmt((TW - width) / 2) + '\n'.join(code) + '\\end{scope}')
    pic.save('g23_p6_grid')
    # verify the claimed maximum of 6 greens for a connected 16-triangle board
    tree = tree_board()
    check(len(tree) == 16 and min_greens(tree) == 6 and connected(tree),
          '2-3 P6: a connected 16-triangle board needing 6 greens exists')


def connected(region):
    region = set(region)
    start = next(iter(region))
    seen = {start}
    stack = [start]
    while stack:
        t = stack.pop()
        for n in nbrs(t):
            if n in region and n not in seen:
                seen.add(n)
                stack.append(n)
    return len(seen) == len(region)


def tree_board():
    # a row of 6 ups and 5 downs, with an up on top of every down: 11 ups, 5 downs
    reg = set()
    for i in range(5):
        reg |= {('U', i, 0), ('D', i, 0)}
    reg |= {('U', 5, 0)}
    reg |= {('U', i, 1) for i in range(5)}
    return reg


# ============================================================ grades 4-5 packet

def g45():
    lab = lambda L: '\\textbf{\\Large %s}' % L
    # ---- Problem 1: boards A (1-1-1), B (2-1-1), C (3-1-1) with small pictures
    nA, nB, nC = (len(rhombus_tilings(x)) for x in (HEX111, HEX211, HEX311))
    check((nA, nB, nC) == (2, 3, 4), '4-5 P1 counts %s' % ((nA, nB, nC),))
    check(len(rhombus_tilings(hexagon(10, 1, 1))) == 11, '4-5 P1 top edge 10 gives 11')
    s = 0.4
    pic = Pic(1.732 + 0.45 + 1.732 + 0.45 + 2.3)
    # row A
    y = 0
    pic.text(0, y, lab('A'))
    pic.board(HEX111, 0.4, y)
    for c in range(4):
        pic.board(HEX111, 2.95 + c * 1.12, y - 0.5, scale=s, boundary_w=1.1, grid_w=0.4)
    # row B
    y = -1.732 - 0.45
    pic.text(0, y, lab('B'))
    pic.board(HEX211, 0.4, y)
    for r in range(2):
        for c in range(3):
            pic.board(HEX211, 3.85 + c * 1.2 + 0.0, y - 0.1 - r * 0.92, scale=0.36,
                      boundary_w=1.1, grid_w=0.4)
    # row C
    y = -2 * (1.732 + 0.45)
    pic.text(0, y, lab('C'))
    pic.board(HEX311, 0.4, y)
    for r in range(3):
        for c in range(2):
            pic.board(HEX311, 4.75 + c * 1.35, y - 0.0 - r * 0.77, scale=0.3,
                      boundary_w=1.1, grid_w=0.4)
    pic.save('g45_p1')

    # ---- Problem 2: board D (2-2-1) + 9 small pictures
    TD = rhombus_tilings(HEX221)
    check(len(TD) == 6, '4-5 P2 board D has 6 coverings')
    pic = Pic(2.598 + 0.35 + 1.04 + 0.1)
    pic.text(0, 0, lab('D'))
    pic.board(HEX221, 0.4, 0)
    s = 0.4
    xs = [4.3, 5.95]
    for r in range(2):
        for c in range(2):
            pic.board(HEX221, xs[c], -r * 1.3, scale=s, boundary_w=1.1, grid_w=0.4)
    y = -2.598 - 0.35
    for c in range(5):
        pic.board(HEX221, 0.05 + c * 1.47, y, scale=s, boundary_w=1.1, grid_w=0.4)
    pic.save('g45_p2')

    # ---- Problem 3: moves on board E, pictures S, T, U
    E = HEX222
    TE = rhombus_tilings(E)
    check(len(TE) == 20, '4-5 board E has 20 coverings')
    W = {t: tuple(w for _, w in ribbons(t, E)) for t in TE}
    byw = {v: k for k, v in W.items()}
    S = byw[('RRLL', 'RRLL')]
    T = byw[('LLRR', 'LLRR')]
    U = byw[('RLRL', 'RLLR')]
    adj = flip_graph(TE)
    idx = {t: n for n, t in enumerate(TE)}
    dS = bfs(adj, idx[S])
    dU = bfs(adj, idx[U])
    check(dS[idx[T]] == 8 and dS[idx[U]] == 3 and dU[idx[T]] == 5,
          '4-5 P3 distances S-T 8, S-U 3, U-T 5: %d %d %d' % (dS[idx[T]], dS[idx[U]], dU[idx[T]]))
    # every round trip is even: graph is bipartite
    color = {}
    bip = True
    for st in adj:
        if st in color:
            continue
        color[st] = 0
        q = [st]
        while q:
            x = q.pop()
            for y2 in adj[x]:
                if y2 not in color:
                    color[y2] = 1 - color[x]
                    q.append(y2)
                elif color[y2] == color[x]:
                    bip = False
    check(bip, '4-5 P7 flip graph is bipartite (no odd round trips)')

    pic = Pic(3.464 + 0.45 + 1.386 + 0.45)
    pic.text(0, 0, lab('E'))
    pic.board(E, 0.4, 0)
    # move picture to the right of E
    h1 = HEX111
    t1, t2 = rhombus_tilings(h1)
    sc = 0.7
    xm = 5.2
    pic.board(h1, xm, -0.15, scale=sc, pieces=pieces_of(t1), grid=False, boundary_w=1.4, piece_w=1.1)
    pic.raw('\\draw[line width=1.2pt,<->,>=stealth] (%s,%s) -- (%s,%s);'
            % (fmt(xm + 0.7), fmt(-0.15 - 1.212 - 0.15), fmt(xm + 0.7), fmt(-0.15 - 1.212 - 0.75)))
    pic.board(h1, xm, -0.15 - 1.212 - 0.9, scale=sc, pieces=pieces_of(t2), grid=False, boundary_w=1.4, piece_w=1.1)
    pic.text(xm + 0.9, -0.15 - 1.212 - 0.45, 'one move', anchor='west')
    # S, T, U
    s = 0.4
    y = -3.464 - 0.45
    for k, (L, til) in enumerate((('S', S), ('T', T), ('U', U))):
        x = 0.4 + k * 2.45
        pic.text(x, y, lab(L))
        pic.board(E, x + 0.4, y, scale=s, pieces=pieces_of(til), grid=False,
                  boundary_w=1.3, piece_w=0.9)
    pic.save('g45_p3')

    # ---- Problem 4: chains; R and L pictures, example, and four pairs for board E
    # R / L icons
    rR = frozenset([('U', 0, 0), ('D', 0, 0)])
    rL = frozenset([('U', 1, 0), ('D', 0, 0)])
    check(rhombus_kind(rR) == 'R' and rhombus_kind(rL) == 'L', 'R/L icons')
    pic = Pic(1.6)
    sc = 0.7
    pic.board(rR, 0.3, -0.5, scale=sc, pieces=[('B', rR)], grid=False, boundary_w=1.3)
    pic.text(0.3 + 0.75, -0.5 - 0.606 - 0.12, 'R (leans right)', anchor='north')
    pic.board(rL, 2.1, -0.5, scale=sc, pieces=[('B', rL)], grid=False, boundary_w=1.3)
    pic.text(2.1 + 0.75, -0.5 - 0.606 - 0.12, 'L (leans left)', anchor='north')
    # example: a covering of board D with its left chain shaded and lettered
    ex = [t for t in TD if [w for _, w in ribbons(t, HEX221)] == ['RLL', 'LRL']][0]
    rib = ribbons(ex, HEX221)
    chain, word = rib[0]
    sc = 0.55
    off, (bw, bh) = offset_of(HEX221)
    xe = 4.3
    letters = []
    for r in chain:
        cx = sum(centroid(t)[0] for t in r) / 2 - off[0]
        cy = sum(centroid(t)[1] for t in r) / 2 - off[1]
        letters.append('\\node[font=\\small\\bfseries] at (%s,%s) {%s};'
                       % (fmt(cx), fmt(cy), rhombus_kind(r)))
    pic.board(HEX221, xe, -0.05, scale=sc, pieces=pieces_of(ex), grid=False,
              chains=[set(t for r in chain for t in r)], boundary_w=1.3, piece_w=0.9,
              piece_fill=False, extra='\n'.join(letters))
    pic.text(xe + bw * sc + 0.2, -0.05 - bh * sc / 2, 'letters: %s' % word, anchor='west')
    pic.save('g45_p4_rl')
    check(word == 'RLL', 'example chain word')

    pairs = [('RLRL', 'RLLR'), ('LRLR', 'RLRL'), ('RRLL', 'LLRR'), ('LRRL', 'RRLL')]
    allw = set(W.values())
    exp = [True, False, True, False]
    for p, e in zip(pairs, exp):
        check((p in allw) == e, '4-5 P4 pair %s possible=%s' % (p, e))
    s = 0.4
    pic = Pic(1.386 + 0.75)
    for k, (a, b) in enumerate(pairs):
        x = 0.1 + k * 1.85
        pic.board(E, x, 0, scale=s, boundary_w=1.1, grid_w=0.4)
        pic.text(x + 0.8, -1.386 - 0.12, 'left: %s' % a, anchor='north')
        pic.text(x + 0.8, -1.386 - 0.42, 'right: %s' % b, anchor='north')
    pic.save('g45_p4_pairs')

    # ---- Problem 5: all coverings of E (25 small pictures)
    s = 0.32
    w, h = 4 * s, 3.464 * s
    cols, rws = 5, 5
    gx = (TW - cols * w) / (cols - 1)
    gy = 0.2
    pic = Pic(rws * h + (rws - 1) * gy + 0.02)
    for r in range(rws):
        for c in range(cols):
            pic.board(E, c * (w + gx), -r * (h + gy), scale=s, boundary_w=1.0, grid_w=0.35)
    pic.save('g45_p5')


LINE_BLOCKS = {
    'g23_lines_p3': 5, 'g23_lines_p4': 3, 'g23_lines_p5': 5,
    'g45_lines_p1': 3, 'g45_lines_p2': 3, 'g45_lines_p4': 5,
    'g45_lines_p5': 2, 'g45_lines_p6': 7, 'g45_lines_p7': 8,
}


def write_line_blocks(gap=0.42):
    for name, n in LINE_BLOCKS.items():
        pic = Pic(n * gap + 0.08)
        pic.lines(0, 0, TW, n, gap)
        pic.save(name)


def write_inline_icons():
    for k in BLOCKS:
        save_raw('icon_' + k, inline_icon(k))


if __name__ == '__main__':
    k1()
    g23()
    g45()
    write_inline_icons()
    write_line_blocks()
    bad = [m for ok, m in CHECKS if not ok]
    print('%d checks, %d failed' % (len(CHECKS), len(bad)))
    for ok, m in CHECKS:
        print(('ok   ' if ok else 'FAIL ') + m)
