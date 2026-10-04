"""
Generates the TikZ figures for the three student packets (Week 1, Tiling).

Every board is built from the design's single source of truth
(design-checks/instances.py), so the printed shapes are exactly the verified ones.
Units: 1 TikZ unit = 1 inch, so actual-size boards print with 1-inch small-triangle edges.

Each page's figure block is one tikzpicture whose top edge is y = 0 and whose
coordinates run downward (negative y).  The width is the text width, 7.5 in.

Run: python3 gen.py   (writes fig/*.tex)
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'design-checks'))

import tri                # noqa: E402
import lozenge as L       # noqa: E402
import instances as I     # noqa: E402

FIG = os.path.join(HERE, 'fig')
os.makedirs(FIG, exist_ok=True)

W = 7.5          # text width in inches
B = I.boards()
UP, DN = tri.UP, tri.DN

# flip points of the regular hexagon (lattice coordinates in the H222 frame), numbered 1-7
POINT_NUMBER = {(0, 2): 1, (1, 2): 2, (0, 3): 3, (-1, 3): 4, (-1, 2): 5, (0, 1): 6, (1, 1): 7}


def f(v):
    s = '%.4f' % v
    s = s.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def P(p):
    return '(%s,%s)' % (f(p[0]), f(p[1]))


class Fig:
    def __init__(self, height, width=W):
        self.h = height
        self.w = width
        self.c = []

    def add(self, s):
        self.c.append(s)

    def tex(self):
        out = [r'\begin{tikzpicture}[x=1in,y=1in]',
               r'\useasboundingbox (0,0) rectangle (%s,%s);' % (f(self.w), f(-self.h))]
        out += self.c
        out.append(r'\end{tikzpicture}')
        return '\n'.join(out) + '\n'

    def save(self, name):
        with open(os.path.join(FIG, name + '.tex'), 'w') as fh:
            fh.write(self.tex())


# ---------------------------------------------------------------- geometry helpers

def bbox(region):
    w, h = tri.bbox_inches(region)
    return w, h


def mapper(full, x, ytop, s):
    sx, sy = tri.min_corner(full)
    w, h = tri.bbox_inches(full)
    oy = ytop - h * s

    def T(p):  # p cartesian (unshifted)
        return ((p[0] - sx) * s + x, (p[1] - sy) * s + oy)
    return T


def poly(pts):
    return ' -- '.join(P(p) for p in pts) + ' -- cycle'


def edge_counts(cells):
    ec = Counter()
    for t in cells:
        cs = tri.corners(t)
        for k in range(3):
            ec[frozenset((cs[k], cs[(k + 1) % 3]))] += 1
    return ec


def draw_board(fig, region, x, ytop, s=1.0, holes=(), tint=None, tiling=None, tiling_fill='rhfill',
               grid=True, outline='1.8pt', rh_line='1.3pt', base=None, chain=None, chain_fill='chainfill',
               letters=None, points=None, grid_style='gridline'):
    """Draw a board whose bounding box has top-left corner (x, ytop), scaled by s."""
    full = set(base) if base is not None else set(region)
    T = mapper(full, x, ytop, s)
    loops = tri.boundary_vertices(full)
    # background
    for loop in loops:
        fig.add(r'\fill[%s] %s;' % (tint or 'white', poly([T(tri.cart(p)) for p in loop])))
    # tiling fill
    if tiling is not None:
        for rh in tiling:
            fill = chain_fill if (chain is not None and rh in chain) else tiling_fill
            fig.add(r'\fill[%s] %s;' % (fill, poly([T(p) for p in L.rhombus_cart(rh)])))
    # grid lines (interior edges only)
    if grid:
        ec = edge_counts(full)
        for e, c in sorted(ec.items(), key=lambda kv: sorted(kv[0])):
            if c == 2:
                a, b = sorted(e)
                fig.add(r'\draw[%s] %s -- %s;' % (grid_style, P(T(tri.cart(a))), P(T(tri.cart(b)))))
    # holes
    for t in holes:
        fig.add(r'\fill[black] %s;' % poly([T(tri.cart(c)) for c in tri.corners(t)]))
    # tiling edges
    if tiling is not None:
        for rh in tiling:
            fig.add(r'\draw[line width=%s, line join=round] %s;' % (rh_line, poly([T(p) for p in L.rhombus_cart(rh)])))
    if letters:
        for rh, ch in letters.items():
            pts = [T(p) for p in L.rhombus_cart(rh)]
            cx = sum(p[0] for p in pts) / 4
            cy = sum(p[1] for p in pts) / 4
            fig.add(r'\node[font=\bfseries\large] at %s {%s};' % (P((cx, cy)), ch))
    # outline
    for loop in loops:
        fig.add(r'\draw[line width=%s, line join=round] %s;' % (outline, poly([T(tri.cart(p)) for p in loop])))
    if points:
        for lp, label in points.items():
            q = T(tri.cart(lp))
            fig.add(r'\node[circle, draw, fill=white, inner sep=0.6pt, minimum size=0.17in, font=\footnotesize\bfseries] at %s {%s};'
                    % (P(q), label))
    w, h = tri.bbox_inches(full)
    return (x, ytop - h * s, x + w * s, ytop)  # x0, y0, x1, y1


def shape_of(region):
    w, h = tri.bbox_inches(region)
    return w, h


def icon(fig, piece, x, ybot, s=0.42, color='pbblue'):
    pts = tri.piece_vertices(tri.PIECES[piece])
    mx = min(p[0] for p in pts)
    my = min(p[1] for p in pts)
    q = [((p[0] - mx) * s + x, (p[1] - my) * s + ybot) for p in pts]
    fig.add(r'\filldraw[fill=%s, draw=black, line width=0.8pt, line join=round] %s;' % (color, poly(q)))
    return max(p[0] for p in q) - x, max(p[1] for p in q) - ybot


PIECE_COLOR = {'G': 'pbgreen', 'B': 'pbblue', 'R': 'pbred', 'Y': 'pbyellow', 'P': 'pbpurple'}


def icon_row(name, pieces, s=0.42, gap=0.25):
    """A small tikzpicture with block pictures side by side (bottom aligned)."""
    widths = []
    heights = []
    for p in pieces:
        pts = tri.piece_vertices(tri.PIECES[p])
        widths.append((max(q[0] for q in pts) - min(q[0] for q in pts)) * s)
        heights.append((max(q[1] for q in pts) - min(q[1] for q in pts)) * s)
    tw = sum(widths) + gap * (len(pieces) - 1)
    th = max(heights)
    fig = Fig(th, tw)
    x = 0
    for p, wd in zip(pieces, widths):
        icon(fig, p, x, -th, s, PIECE_COLOR[p])
        x += wd + gap
    fig.save(name)


# ---------------------------------------------------------------- record elements

def yesno(fig, cx, y):
    fig.add(r'\node[font=\Large] at %s {yes\hspace{0.55in}no};' % P((cx, y)))


def numbox(fig, cx, y, label, anchor='center'):
    fig.add(r'\node[anchor=%s] at %s {%s\ \ansbox};' % (anchor, P((cx, y)), label))


def lines(fig, x0, x1, ytop, n, gap=0.4):
    for k in range(n):
        y = ytop - gap * (k + 1)
        fig.add(r'\draw[ruleline] %s -- %s;' % (P((x0, y)), P((x1, y))))
    return ytop - gap * n


def label(fig, x, y, text, anchor='north west', font=r'\bfseries\large'):
    fig.add(r'\node[anchor=%s, font=%s, inner sep=0pt] at %s {%s};' % (anchor, font, P((x, y)), text))


# ---------------------------------------------------------------- K-1

def k1():
    icon_row('k1-icons-B', ['B'])
    icon_row('k1-icons-BG', ['B', 'G'])
    icon_row('k1-icons-YRBG', ['Y', 'R', 'B', 'G'], s=0.36, gap=0.18)

    # Problem 1: a, b in a row; c and d interlocked in a second row
    fig = Fig(6.0)
    y = -0.25
    draw_board(fig, B['K1-P1a'], 1.0, y)
    draw_board(fig, B['K1-P1b'], 4.5, y)
    yesno(fig, 2.0, y - 1.732 - 0.45)
    yesno(fig, 5.5, y - 1.732 - 0.45)
    y2 = y - 1.732 - 1.55
    c0 = 0.375
    draw_board(fig, B['K1-P1c'], c0, y2)
    draw_board(fig, B['K1-P1d'], c0 + 2.75, y2)
    yesno(fig, c0 + 1.25, y2 - 1.732 - 0.45)
    yesno(fig, c0 + 2.75 + 2.0, y2 - 1.732 - 0.45)
    fig.save('k1-p1')

    # Problem 2: triangles with 2, 3, 4 on each side
    fig = Fig(8.25)
    y = -0.1
    x2, x3 = 0.65, 0.65 + 2 + 1.2
    draw_board(fig, B['K1-P2a'], x2, y - (2.598 - 1.732))
    draw_board(fig, B['K1-P2b'], x3, y)
    ybox = y - 2.598 - 0.55
    numbox(fig, x2 + 1.0, ybox, r'\Large How many greens?')
    numbox(fig, x3 + 1.5, ybox, r'\Large How many greens?')
    y4 = ybox - 0.75
    draw_board(fig, B['K1-P2c'], 1.75, y4)
    numbox(fig, 3.75, y4 - 3.464 - 0.55, r'\Large How many greens?')
    fig.save('k1-p2')

    # Problem 3, first page: 3 copies of the yellow-hexagon shape, 4 copies of the 3-wide hexagon
    fig = Fig(6.35)
    y = -0.1
    for k in range(3):
        draw_board(fig, B['K1-P3a'], 0.15 + k * 2.6, y)
    y -= 1.732 + 0.65
    for r in range(2):
        for k in range(2):
            draw_board(fig, B['K1-P3b'], 0.3 + k * 3.9, y)
        y -= 1.732 + 0.4
    fig.save('k1-p3a')

    # Problem 3, second page: 5 copies of the 4-wide hexagon
    fig = Fig(9.4)
    y = -0.02
    for k in range(5):
        draw_board(fig, B['K1-P3c'], 1.75, y)
        y -= 1.732 + 0.17
    fig.save('k1-p3b')

    # Problem 4: side-3 triangle interlocked with the big hexagon, then the side-4 triangle
    fig = Fig(8.15)
    y = -0.1
    t0 = 0.35
    g = 0.8
    h0 = t0 + 2 + g
    draw_board(fig, B['K1-P4a'], t0, y - (3.464 - 2.598))
    draw_board(fig, B['K1-P4b'], h0, y)
    ybox = y - 3.464 - 0.55
    numbox(fig, t0 + 1.5, ybox, r'\Large How many blocks?')
    numbox(fig, h0 + 2.0, ybox, r'\Large How many blocks?')
    y4 = ybox - 0.8
    draw_board(fig, B['K1-P4c'], 0.6, y4)
    numbox(fig, 4.75, y4 - 1.9, r'\Large How many blocks?', anchor='west')
    fig.save('k1-p4')

    # Problem 5: big shapes from small blocks of their own colour
    def p5row(fig, key, piece, color, ytop):
        w, h = tri.bbox_inches(B[key])
        icon(fig, piece, 0.1, ytop - h / 2 - 0.2, 0.42, color)
        draw_board(fig, B[key], 1.15, ytop, tint=color + '!22')
        cy = ytop - h / 2
        fig.add(r'\node[anchor=west, font=\Large] at %s {yes\hspace{0.55in}no};' % P((5.45, cy + 0.42)))
        fig.add(r'\node[anchor=west] at %s {\Large How many? \ansbox};' % P((5.45, cy - 0.38)))
        return ytop - h

    fig = Fig(8.5)
    y = -0.1
    y = p5row(fig, 'K1-P5a', 'G', 'pbgreen', y) - 0.55
    y = p5row(fig, 'K1-P5b', 'R', 'pbred', y) - 0.55
    y = p5row(fig, 'K1-P5c', 'Y', 'pbyellow', y)
    fig.save('k1-p5a')
    fig = Fig(3.7)
    p5row(fig, 'K1-P5d', 'P', 'pbpurple', -0.1)
    fig.save('k1-p5b')

    # Problem 6: the game boards with tally boxes
    def tally(fig, ytop):
        fig.add(r'\node[anchor=south west, font=\large] at %s {first player won};' % P((0.3, ytop - 0.3)))
        fig.add(r'\draw[line width=0.8pt] %s rectangle %s;' % (P((0.3, ytop - 0.33)), P((2.8, ytop - 1.0))))
        fig.add(r'\node[anchor=south west, font=\large] at %s {second player won};' % P((3.1, ytop - 0.3)))
        fig.add(r'\draw[line width=0.8pt] %s rectangle %s;' % (P((3.1, ytop - 0.33)), P((5.6, ytop - 1.0))))
        fig.add(r'\node[anchor=west, font=\large] at %s {better:};' % P((5.85, ytop - 0.45)))
        fig.add(r'\node[anchor=west, font=\large] at %s {first\hspace{0.25in}second};' % P((5.85, ytop - 0.85)))
        return ytop - 1.0

    fig = Fig(7.85)
    y = -0.1
    draw_board(fig, B['K1-P6a'], 0.3, y)
    y = tally(fig, y - 1.732 - 0.12) - 0.45
    draw_board(fig, B['K1-P6b'], 0.3, y)
    y = tally(fig, y - 0.866 - 0.12) - 0.45
    draw_board(fig, B['K1-P6c'], 0.3, y)
    y = tally(fig, y - 0.866 - 0.12)
    fig.save('k1-p6')


# ---------------------------------------------------------------- grades 2-3

def g23():
    icon_row('g23-icon-P', ['P'], s=0.42)

    # Problem 1, page 1: A (big hexagon) interlocked with B (side-3 triangle)
    fig = Fig(4.3)
    y = -0.25
    a0, g = 0.35, 0.8
    b0 = a0 + 3 + g
    draw_board(fig, B['23-P1a'], a0, y)
    draw_board(fig, B['23-P1b'], b0, y - (3.464 - 2.598))
    label(fig, a0, y, 'A')
    label(fig, b0, y - (3.464 - 2.598), 'B')
    lines(fig, a0 + 1.0, a0 + 3.0, y - 3.464, 1, gap=0.6)
    lines(fig, b0 + 0.5, b0 + 2.5, y - 3.464, 1, gap=0.6)
    fig.save('g23-p1a')

    # Problem 1, page 2: C (side-4 triangle) and D (big chevron)
    fig = Fig(9.0)
    y = -0.3
    draw_board(fig, B['23-P1c'], 1.75, y)
    label(fig, 1.75, y, 'C')
    lines(fig, 2.75, 4.75, y - 3.464, 1, gap=0.6)
    y -= 3.464 + 1.3
    draw_board(fig, B['23-P1d'], 1.75, y)
    label(fig, 1.75, y, 'D')
    lines(fig, 2.75, 4.75, y - 3.464, 1, gap=0.6)
    fig.save('g23-p1b')

    # Problem 2: triangles 3, 4 (page 1) and 5 (page 2); greens box to the right
    fig = Fig(7.0)
    y = -0.15
    draw_board(fig, B['23-P2a'], 1.0, y)
    numbox(fig, 4.6, y - 1.6, r'\large Greens:', anchor='west')
    y -= 2.598 + 0.7
    draw_board(fig, B['23-P2b'], 0.5, y)
    numbox(fig, 4.6, y - 2.2, r'\large Greens:', anchor='west')
    fig.save('g23-p2a')
    fig = Fig(4.6)
    draw_board(fig, B['23-P2c'], 0.25, -0.15)
    numbox(fig, 5.0, -0.15 - 2.6, r'\large Greens:', anchor='west')
    fig.save('g23-p2b')

    # Problem 3: hexagons with two holes, two per page, writing lines on the right
    def holeboard(fig, key, letter, ytop):
        draw_board(fig, B[key], 0.3, ytop, holes=I.HOLES[key], base=I.HOLE_BASE[key])
        label(fig, 0.3, ytop, letter)
        lines(fig, 4.65, 7.45, ytop + 0.1, 9, gap=0.395)

    fig = Fig(8.0)
    holeboard(fig, '23-P3a', 'a', -0.3)
    holeboard(fig, '23-P3b', 'b', -0.3 - 3.464 - 0.75)
    fig.save('g23-p3a')
    fig = Fig(8.0)
    holeboard(fig, '23-P3c', 'c', -0.3)
    holeboard(fig, '23-P3d', 'd', -0.3 - 3.464 - 0.75)
    fig.save('g23-p3b')

    # Problem 4: side-7 triangle
    fig = Fig(8.45)
    y = -0.05
    draw_board(fig, B['23-P4'], 0.25, y)
    numbox(fig, 5.35, y - 1.0, r'\large Greens:', anchor='west')
    lines(fig, 0.0, 7.5, y - 6.062 - 0.05, 6, gap=0.39)
    fig.save('g23-p4')

    # Problem 5: chevrons on triangles 3, 4 (page 1) and 6 with the table (page 2)
    fig = Fig(6.75)
    y = -0.15
    draw_board(fig, B['23-P5a'], 1.0, y)
    numbox(fig, 4.6, y - 1.6, r'\large Greens:', anchor='west')
    y -= 2.598 + 0.55
    draw_board(fig, B['23-P5b'], 0.5, y)
    numbox(fig, 4.6, y - 2.2, r'\large Greens:', anchor='west')
    fig.save('g23-p5a')

    fig = Fig(9.35)
    y = -0.05
    draw_board(fig, B['23-P5c'], 0.25, y)
    numbox(fig, 5.1, y - 1.2, r'\large Greens:', anchor='west')
    y -= 5.196 + 0.35
    # comparison table
    cols = [2.85, 4.4, 5.95, 7.5]
    rows = [y, y - 0.55, y - 1.05, y - 1.55]
    for yy in rows:
        fig.add(r'\draw[line width=0.6pt] %s -- %s;' % (P((0, yy)), P((7.5, yy))))
    for xx in [0] + cols:
        fig.add(r'\draw[line width=0.6pt] %s -- %s;' % (P((xx, rows[0])), P((xx, rows[-1]))))
    heads = ['3 on each side', '4 on each side', '6 on each side']
    for k, t in enumerate(heads):
        fig.add(r'\node at %s {%s};' % (P(((cols[k] + cols[k + 1]) / 2, (rows[0] + rows[1]) / 2)), t))
    fig.add(r'\node[anchor=west] at %s {Triangle};' % P((0.1, (rows[0] + rows[1]) / 2)))
    fig.add(r'\node[anchor=west] at %s {Greens with blue rhombuses};' % P((0.1, (rows[1] + rows[2]) / 2)))
    fig.add(r'\node[anchor=west] at %s {Greens with purple chevrons};' % P((0.1, (rows[2] + rows[3]) / 2)))
    lines(fig, 0, 7.5, rows[-1] - 0.1, 5, gap=0.39)
    fig.save('g23-p5b')

    # Problem 6: hourglass boards with lines on the right
    fig = Fig(8.65)
    y = -0.3
    draw_board(fig, B['23-P6a'], 0.2, y)
    label(fig, 0.2, y + 0.1, 'a', anchor='south west')
    numbox(fig, 4.65, y - 0.35, r'\large Greens:', anchor='west')
    lines(fig, 4.65, 7.45, y - 0.75, 6, gap=0.39)
    y -= 3.464 + 0.65
    draw_board(fig, B['23-P6b'], 0.45, y)
    label(fig, 0.45, y + 0.1, 'b', anchor='south west')
    numbox(fig, 4.65, y - 0.35, r'\large Greens:', anchor='west')
    lines(fig, 4.65, 7.45, y - 0.75, 8, gap=0.39)
    fig.save('g23-p6')

    # Problem 7: a full grid page at actual size (9 rows of small triangles)
    rows_n = 9
    gw, gh = 7.0, rows_n * 0.8660254
    fig = Fig(gh + 0.85)
    x0, ytop = 0.25, -0.05
    yb = ytop - gh
    fig.add(r'\begin{scope}')
    fig.add(r'\clip %s rectangle %s;' % (P((x0, yb)), P((x0 + gw, ytop))))
    for k in range(rows_n + 1):
        yy = yb + k * 0.8660254
        fig.add(r'\draw[gridpage] %s -- %s;' % (P((x0, yy)), P((x0 + gw, yy))))
    # slanted lines through bottom grid points x0 + i
    for i in range(-12, 13):
        xa = x0 + i
        fig.add(r'\draw[gridpage] %s -- %s;' % (P((xa, yb)), P((xa + gh / 1.7320508, ytop))))
        fig.add(r'\draw[gridpage] %s -- %s;' % (P((xa, yb)), P((xa - gh / 1.7320508, ytop))))
    fig.add(r'\end{scope}')
    fig.add(r'\draw[line width=0.8pt] %s rectangle %s;' % (P((x0, yb)), P((x0 + gw, ytop))))
    numbox(fig, 7.5, yb - 0.45, r'\large Small triangles in my board:', anchor='east')
    fig.save('g23-p7')


# ---------------------------------------------------------------- grades 4-5

def tiling_of(words):
    return I.tiling_by_words(2, 2, 2, words)


def g45():
    # Problem 1 boards at actual size
    fig = Fig(6.85)
    y = -0.35
    draw_board(fig, B['45-P1a'], 0.6, y - (2.598 - 1.732))
    label(fig, 0.6, y - (2.598 - 1.732), 'A')
    draw_board(fig, B['45-P1b'], 3.9, y)
    label(fig, 3.9, y, 'B')
    y -= 2.598 + 0.6
    draw_board(fig, B['45-P1c'], 2.25, y)
    label(fig, 2.25, y, 'C')
    fig.save('g45-p1a')

    # Problem 1 drawing copies at half size
    fig = Fig(8.75)
    y = -0.25
    label(fig, 0, y + 0.02, 'A', anchor='north west')
    for k in range(3):
        draw_board(fig, B['45-P1a'], 0.55 + k * 1.45, y, s=0.5, outline='1.2pt', grid_style='gridsmall')
    y -= 0.866 + 0.38
    label(fig, 0, y + 0.02, 'B', anchor='north west')
    for k in range(4):
        draw_board(fig, B['45-P1b'], 0.55 + k * 1.75, y, s=0.5, outline='1.2pt', grid_style='gridsmall')
    y -= 1.299 + 0.38
    label(fig, 0, y + 0.02, 'C', anchor='north west')
    for r in range(2):
        for k in range(4):
            draw_board(fig, B['45-P1c'], 0.55 + k * 1.75, y, s=0.5, outline='1.2pt', grid_style='gridsmall')
        y -= 1.732 + 0.3
    lines(fig, 0, 7.5, y + 0.05, 4, gap=0.39)
    fig.save('g45-p1b')

    # Problem 2: the flip picture (yellow-hexagon shape filled both ways), actual size
    R1, ts1 = L.tilings(1, 1, 1)
    # order: first the one with the standing rhombus on the left (flip-1 in the design)
    def has_left_standing(T):
        sx, sy = tri.min_corner(R1)
        for rh in T:
            if L.kind(rh) == 'S':
                xs = [p[0] - sx for p in L.rhombus_cart(rh)]
                return min(xs) < 0.25
        return False
    ts1 = sorted(ts1, key=lambda T: 0 if has_left_standing(T) else 1)
    fig = Fig(1.9, 5.6)
    draw_board(fig, R1, 0.2, -0.08, tiling=ts1[0])
    fig.add(r'\draw[{Stealth[length=0.16in, width=0.14in]}-{Stealth[length=0.16in, width=0.14in]}, line width=1.6pt] (2.4,-0.946) -- (3.2,-0.946);')
    draw_board(fig, R1, 3.4, -0.08, tiling=ts1[1])
    fig.save('g45-flip')

    # Problem 2: map space and answer line
    fig = Fig(5.0)
    fig.add(r'\draw[line width=0.5pt, gray] (0,-0.05) rectangle (7.5,-4.3);')
    fig.add(r'\node[anchor=west, font=\large] at (0,-4.72) {Ways \rule{0.6in}{0.5pt} and \rule{0.6in}{0.5pt} need \rule{0.6in}{0.5pt} flips.};')
    fig.save('g45-p2')

    # Problem 3: example picture, hexagon (1,3,1) with chain R L R R shaded and lettered
    R131, ts131 = L.tilings(1, 3, 1)
    T = [t for t in ts131 if L.ribbons(t, 1, 3, 1) == ('RLRR',)][0]
    m = L.partner_map(T)
    chain = []
    cur = (0, 0, UP)
    for _ in range(4):
        p = m[cur]
        chain.append(frozenset((cur, p)))
        cur = (cur[0], cur[1] + 1, UP) if p == (cur[0], cur[1], DN) else (cur[0] - 1, cur[1] + 1, UP)
    letters = {rh: L.kind(rh) for rh in chain}
    w, h = tri.bbox_inches(R131)
    fig = Fig(h + 0.1, w + 0.1)
    draw_board(fig, R131, 0.05, -0.05, tiling=T, chain=set(chain), letters=letters, tiling_fill='white')
    fig.save('g45-chain-example')

    # Problem 3: table of chain letters and lines
    fig = Fig(4.1)
    y = -0.35
    for r in range(3):
        for c in range(2):
            n = r + 1 + 3 * c
            fig.add(r'\node[anchor=west, font=\large] at %s {Way %d:};' % (P((c * 3.9, y)), n))
            fig.add(r'\draw[ruleline] %s -- %s;' % (P((c * 3.9 + 0.95, y - 0.12)), P((c * 3.9 + 3.4, y - 0.12))))
        y -= 0.5
    lines(fig, 0, 7.5, y, 6, gap=0.39)
    fig.save('g45-p3')

    # Problem 4: hexagons D, E, F
    for key, letter, name, xb in [('45-P4a', 'D', 'g45-p4d', 0.4), ('45-P4b', 'E', 'g45-p4e', 0.4)]:
        w, h = tri.bbox_inches(B[key])
        fig = Fig(h + 0.5)
        draw_board(fig, B[key], xb, -0.3)
        label(fig, xb, -0.3, letter)
        numbox(fig, 4.9, -0.75, r'\large Number of ways:', anchor='west')
        fig.save(name)
    w, h = tri.bbox_inches(B['45-P4c'])
    fig = Fig(h + 0.35 + 0.39 * 5 + 0.15)
    draw_board(fig, B['45-P4c'], 0.4, -0.3)
    label(fig, 0.4, -0.3, 'F')
    numbox(fig, 4.9, -0.75, r'\large Number of ways:', anchor='west')
    lines(fig, 0, 7.5, -0.3 - h, 5, gap=0.39)
    fig.save('g45-p4f')

    # key picture: regular hexagon at half size with the 7 inner points numbered
    def keypic(name):
        fig = Fig(3.4641 * 0.45 + 0.1, 4 * 0.45 + 0.1)
        draw_board(fig, I.H222, 0.05, -0.05, s=0.45, outline='1.1pt', grid_style='gridsmall',
                   points={p: str(n) for p, n in POINT_NUMBER.items()})
        fig.save(name)
    keypic('g45-key')

    # Problem 5 parts: start at actual size (left), finish at half size (right), record lines
    def p5part(fig, part, ytop):
        s_, t_ = I.P5_PAIRS[part]
        draw_board(fig, I.H222, 0.3, ytop, tiling=tiling_of(s_))
        label(fig, 0.0, ytop, part)
        fig.add(r'\node[anchor=south west, font=\large] at %s {start};' % P((0.0, ytop - 3.464)))
        draw_board(fig, I.H222, 5.0, ytop, s=0.5, tiling=tiling_of(t_), outline='1.2pt', rh_line='0.8pt', grid=False)
        fig.add(r'\node[anchor=north, font=\large] at %s {finish};' % P((6.0, ytop - 1.732 - 0.02)))
        fig.add(r'\node[anchor=west, font=\large] at %s {Points flipped:};' % P((4.6, ytop - 2.32)))
        fig.add(r'\draw[ruleline] %s -- %s;' % (P((4.6, ytop - 2.85)), P((7.5, ytop - 2.85))))
        numbox(fig, 4.6, ytop - 3.2, r'\large Flips:', anchor='west')

    fig = Fig(7.3)
    p5part(fig, 'a', -0.05)
    p5part(fig, 'b', -0.05 - 3.464 - 0.3)
    fig.save('g45-p5a')
    fig = Fig(6.3)
    p5part(fig, 'c', -0.05)
    lines(fig, 0, 7.5, -0.05 - 3.464 - 0.1, 6, gap=0.39)
    fig.save('g45-p5b')

    # Problem 6: start covering at actual size and record lines
    fig = Fig(7.0)
    y = -0.1
    draw_board(fig, I.H222, 0.3, y, tiling=tiling_of(I.P6_START))
    fig.add(r'\node[anchor=west, font=\large] at %s {Round trip of 4 flips:};' % P((4.7, y - 0.9)))
    fig.add(r'\draw[ruleline] %s -- %s;' % (P((4.7, y - 1.5)), P((7.5, y - 1.5))))
    fig.add(r'\node[anchor=west, font=\large] at %s {Round trip of 6 flips:};' % P((4.7, y - 2.2)))
    fig.add(r'\draw[ruleline] %s -- %s;' % (P((4.7, y - 2.8)), P((7.5, y - 2.8))))
    lines(fig, 0, 7.5, y - 3.464 - 0.2, 8, gap=0.39)
    fig.save('g45-p6')

    # Problem 7: blank regular hexagon and work space
    fig = Fig(3.75)
    draw_board(fig, I.H222, 0.3, -0.15)
    numbox(fig, 4.9, -0.7, r'\large Number of ways:', anchor='west')
    fig.save('g45-p7')


if __name__ == '__main__':
    k1()
    g23()
    g45()
    print('figures written to', FIG)
