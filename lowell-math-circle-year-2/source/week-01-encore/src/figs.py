"""Generate every TikZ figure used in the three packets into figs/*.tex.
Boards on which children place blocks are drawn at actual size (small edge = 1 inch)."""
import os
import glob
from draw import *
from pics import *
from cubes import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figs')
os.makedirs(OUT, exist_ok=True)

TINT = {'green': 'pbgreen!28', 'blue': 'pbblue!24', 'red': 'pbred!24', 'yellow': 'pbyellow!38'}
CHOICE = r'\LARGE 1st\hspace{0.55in}2nd'


def save(name, F):
    with open(os.path.join(OUT, name + '.tex'), 'w') as fh:
        fh.write(F.tex())


def choice(F, x, y, anchor='center'):
    F.text(x, y, CHOICE, anchor=anchor)


def board(F, R, x, y, anchor='sw', scale=1.0, rot=0, grid=GRID, fill=None, border=BORDER):
    X, b = place(R, x, y, scale, rot, anchor)
    F.region(R, X, fill=fill, grid=grid, border=border)
    return X, b


def labelled_box(F, x, y, label, w=0.75, h=0.62):
    """Label to the left of a record box whose lower-left corner is (x, y)."""
    F.text(x - 0.12, y + h / 2, r'\large ' + label, anchor='east')
    F.box(x, y, w, h)


# ------------------------------------------------------------------ K-1

def figK1():
    """Problem 1: the 2x shapes at actual size (tinted, no grid), each with a box to its right,
    and below them small pictures of the 3x Upscale pieces, each with a box to its right."""
    F = Fig()
    bw = 0.56     # record box
    gin = 0.12    # shape to its box
    # bottom row: small pictures of the 3x Upscale pieces
    s = 0.18
    shapes3 = [(tri_up(0, 0, 3), 'green'), (rhomb(3), 'blue'), (trap(0, 0, 6, 3), 'red'),
               (hexR(3, 3, 3), 'yellow')]
    sizes = [bbox_of(R, s) for R, _ in shapes3]
    rowh = max(h for _, h in sizes)
    total = sum(w + gin + bw for w, _ in sizes)
    gap = (7.4 - total) / 3
    x = 0.0
    for (R, c), (w, h) in zip(shapes3, sizes):
        board(F, R, x, rowh / 2, anchor='w', scale=s, grid=None, fill=TINT[c], border=BORDER_THIN)
        F.box(x + w + gin, rowh / 2 - bw / 2, bw, bw)
        x += w + gin + bw + gap
    # middle row: 2x hexagon, and the 2x trapezoid turned a quarter turn so it fits beside it
    trapR = trap(0, 0, 4, 2)
    tw, th = bbox_of(trapR, 1.0, 90)
    mid = rowh + 0.7 + th / 2
    X, b = board(F, HEX2, 0.0, mid, anchor='w', grid=None, fill=TINT['yellow'])
    F.box(b[0] + b[2] + gin, mid - bw / 2, bw, bw)
    xt = b[0] + b[2] + gin + bw + 0.34
    X, b = board(F, trapR, xt, mid, anchor='w', rot=90, grid=None, fill=TINT['red'])
    F.box(b[0] + b[2] + gin, mid - bw / 2, bw, bw)
    # top row: 2x triangle and 2x rhombus
    y = mid + th / 2 + 0.5
    X, b = board(F, tri_up(0, 0, 2), 0.0, y, grid=None, fill=TINT['green'])
    F.box(b[0] + b[2] + gin, b[1] + b[3] / 2 - bw / 2, bw, bw)
    X, b = board(F, rhomb(2), 3.4, y, grid=None, fill=TINT['blue'])
    F.box(b[0] + b[2] + gin, b[1] + b[3] / 2 - bw / 2, bw, bw)
    save('k1', F)


def figK2():
    """Problem 2: three small game boards."""
    F = Fig()
    # bottom row: 3-by-1 strip, choice to the right
    X, b = board(F, parR(3, 1), 0.6, 0)
    choice(F, 5.6, b[1] + b[3] / 2)
    # top row: hexagon 1,1,1 and 2-by-2 parallelogram, choices below
    y = b[3] + 1.25
    X, b1 = board(F, hexR(1, 1, 1), 0.6, y)
    choice(F, b1[0] + b1[2] / 2, y - 0.45)
    X, b2 = board(F, parR(2, 2), 4.1, y)
    choice(F, b2[0] + b2[2] / 2, y - 0.45)
    save('k2', F)


def fewest_most(F, x, y):
    """Two labelled boxes stacked; (x, y) is the lower-left of the lower box."""
    labelled_box(F, x, y, 'most')
    labelled_box(F, x, y + 0.95, 'fewest')


def figK3():
    """Problem 3: big triangle and star outlines at actual size."""
    F = Fig()
    X, b = board(F, STAR, 1.0, 0, grid=None, fill='black!6')
    fewest_most(F, 6.0, b[3] / 2 - 0.8)
    y = b[3] + 0.6
    X, b = board(F, triR(3), 1.0, y, grid=None, fill='black!6')
    fewest_most(F, 6.0, y + b[3] / 2 - 0.8)
    save('k3', F)


def figK4():
    """Problem 4: three more game boards, choices to the right."""
    F = Fig()
    rows = [parR(4, 2), triR(3), parR(3, 2)]  # bottom to top
    y = 0
    for R in rows:
        X, b = board(F, R, 0.3, y)
        choice(F, 6.25, y + b[3] / 2)
        y += b[3] + 0.55
    save('k4', F)


def icon_box(F, x, y, icon, colour, bw=0.62):
    """A small piece icon to the left of a record box whose lower-left corner is (x, y)."""
    X, b = place(icon, x - 0.14, y + bw / 2, 0.42, 0, 'e')
    F.region(icon, X, fill=colour, grid=None, border=BORDER_THIN)
    F.box(x, y, bw, bw)


RED_ICON = trap(0, 0, 2, 1)
BLUE_ICON = rhomb(1)
ONE_COLOUR = [FISH, trap(0, 0, 4, 1), hexR(2, 2, 1)]   # top to bottom


def figK5():
    """Problem 5: three outlines at actual size, each with a red box and a blue box."""
    F = Fig()
    bw = 0.62
    y = 0
    for R in reversed(ONE_COLOUR):
        X, b = board(F, R, 0.6, y, grid=None, fill='black!6')
        mid = b[1] + b[3] / 2
        icon_box(F, 6.0, mid + 0.12, RED_ICON, 'pbred', bw)
        icon_box(F, 6.0, mid - 0.12 - bw, BLUE_ICON, 'pbblue', bw)
        y += b[3] + 0.55
    save('k5', F)


def figK6():
    """Problem 6: boat and 2x hexagon outlines at actual size."""
    F = Fig()
    X, b = board(F, HEX2, 0.8, 0, grid=None, fill='black!6')
    fewest_most(F, 6.0, b[3] / 2 - 0.8)
    y = b[3] + 0.5
    X, b = board(F, BOAT, 0.8, y, grid=None, fill='black!6')
    fewest_most(F, 6.0, y + b[3] / 2 - 0.8)
    save('k6', F)


def small_hex_spokes(F, cx, cy, side):
    R = hexR(1, 1, 1)
    X, b = place(R, cx, cy, side, 0, 'c')
    F.region(R, X, grid=GRID_LIGHT, border=BORDER_THIN)


def figK7():
    """Problem 7: actual-size yellow hexagon outline; three small hexagons for the red ways
    and two for the blue ways (3 and 2 are the numbers of fillings)."""
    F = Fig()
    for row, (icon, col, n) in enumerate([(rhomb(1), 'pbblue', 2), (trap(0, 0, 2, 1), 'pbred', 3)]):
        cy = 0.8 + row * 1.85
        X, b = place(icon, 0.6, cy, 0.55, 0, 'c')
        F.region(icon, X, fill=col, grid=None, border=BORDER_THIN)
        for i in range(n):
            small_hex_spokes(F, 1.95 + i * 1.58, cy, 0.72)
    y = 0.8 + 1.85 + 1.15
    X, b = board(F, hexR(1, 1, 1), 4.0, y, anchor='s', grid=None, fill=TINT['yellow'])
    F.invisible(0, 0, 7.3, y + b[3])
    save('k7', F)


# ------------------------------------------------------------------ grades 2-3 and 4-5

def figGame1():
    """Problem 1 (2-3 and 4-5): four small boards, choices below each."""
    F = Fig()
    # bottom row: 3-by-2 parallelogram and hexagon 1,1,2
    X, b1 = board(F, parR(3, 2), 0.2, 0.55)
    choice(F, b1[0] + b1[2] / 2, 0.15)
    X, b2 = board(F, hexR(1, 1, 2), 5.0, 0.55)
    choice(F, b2[0] + b2[2] / 2, 0.15)
    y = 0.55 + max(b1[3], b2[3]) + 0.55 + 0.4
    X, b3 = board(F, hexR(1, 1, 1), 0.7, y)
    choice(F, b3[0] + b3[2] / 2, y - 0.4)
    X, b4 = board(F, parR(2, 2), 4.3, y)
    choice(F, b4[0] + b4[2] / 2, y - 0.4)
    save('game1', F)


def figGame2():
    """Strategy problem (2-3 Problem 5, 4-5 Problem 2): hexagon 2,2,2 and 3-by-3 parallelogram."""
    F = Fig()
    X, b = board(F, parR(3, 3), 0.1, 0)
    y = b[3] + 0.6
    X, b = board(F, hexR(2, 2, 2), 0.1, y)
    F.invisible(0, 0, 7.4, y + b[3])
    save('game2', F)


def count_box(F, x, y, label='pieces'):
    labelled_box(F, x, y, label)


def copy_and_count(F, R, b, s=0.4, xc=4.85, xbox=5.75):
    """A small copy of R top-aligned with the board whose box is b, and a count box under it."""
    top = b[1] + b[3]
    X, bc = board(F, R, xc, top, anchor='nw', scale=s, grid=GRID_LIGHT, border=BORDER_THIN)
    count_box(F, xbox, bc[1] - 0.3 - 0.62)


def figM3():
    """Problem 3 (2-3): fewest pieces on the 2x hexagon and the 4-triangle, gridded, each with
    a small copy to draw on and a count box."""
    F = Fig()
    X, b = board(F, triR(4), 0.1, 0, grid=GRID_LIGHT)
    copy_and_count(F, triR(4), b)
    y = b[3] + 0.6
    X, b = board(F, HEX2, 0.1, y, grid=GRID_LIGHT)
    copy_and_count(F, HEX2, b)
    save('m3', F)


def updown_labels(F, cx, ytop):
    F.text(cx, ytop, r'two up: \rule{0.45in}{0.5pt}', anchor='north')
    F.text(cx, ytop - 0.3, r'two down: \rule{0.45in}{0.5pt}', anchor='north')


def figM4():
    """Problem 4 (2-3): 3-triangle board, two small triangles (it has exactly two trapezoid
    fillings) and eight small hexagons for recording."""
    F = Fig()
    sh = 0.42
    hw, hh = bbox_of(HEX2, sh)
    lab = 0.7
    # two rows of four small hexagons (bottom)
    y = lab
    for row in range(2):
        for i in range(4):
            x = 0.05 + i * 1.85
            X, b = board(F, HEX2, x, y, scale=sh, grid=GRID_LIGHT, border=BORDER_THIN)
            updown_labels(F, b[0] + b[2] / 2, y - 0.08)
        y += hh + lab + 0.25
    # top row: board and two small triangles
    X, b = board(F, triR(3), 0.1, y)
    st = 0.4
    for i in range(2):
        x = 3.9 + i * 1.75
        X2, b2 = board(F, triR(3), x, y + 0.75, scale=st, grid=GRID_LIGHT, border=BORDER_THIN)
        updown_labels(F, b2[0] + b2[2] / 2, y + 0.67)
    save('m4', F)


def figTriGame(name, with_par=False):
    """Triangle boards with 3 and 4 small edges per side (and optionally a 4-by-2 parallelogram)."""
    F = Fig()
    y = 0
    if with_par:
        X, b = board(F, parR(4, 2), 0.2, 0)
        choice(F, 6.3, b[3] / 2)
        y = b[3] + 1.0
    X, b1 = board(F, triR(3), 0.15, y + 0.45)
    choice(F, b1[0] + b1[2] / 2, y)
    X, b2 = board(F, triR(4), 3.45, y + 0.45)
    choice(F, b2[0] + b2[2] / 2, y)
    save(name, F)


def figBigHex(name):
    """3x hexagon at actual size with a light grid, plus a small copy and a count box."""
    F = Fig()
    R = hexR(3, 3, 3)
    X, b = board(F, R, 0.2, 0, scale=0.36, grid=GRID_LIGHT, border=BORDER_THIN)
    count_box(F, 4.6, b[3] / 2 - 0.3)
    y = b[3] + 0.4
    X, b = board(F, R, 0.75, y, grid=GRID_LIGHT)
    save(name, F)


def figM7():
    """Problem 7 (2-3): triangle with 6 small edges per side, gridded, two small copies."""
    F = Fig()
    R = triR(6)
    s = 0.3
    for i in range(2):
        board(F, R, 0.2 + i * 2.2, 0, scale=s, grid=GRID_LIGHT, border=BORDER_THIN)
    y = bbox_of(R, s)[1] + 0.4
    X, b = board(F, R, 0.75, y)
    save('m7', F)


# ------------------------------------------------------------------ grades 4-5: cubes

FILLS = {'L': 'shadeL', 'M': 'shadeM', 'D': 'shadeD'}


def draw_rhombus_tiling(F, R, T, X, rot=90):
    for p in T:
        F.piece(p, X, FILLS[shade_class(p, rot)])
    loops = boundary_loops(R)
    F.add(f"\\draw[{BORDER_THIN}] " + ' '.join(F.path([X(q) for q in L]) for L in loops) + ';')


def figU4():
    """Problem 4 (4-5): the 2,2,2 hexagon at actual size; shaded fillings A (empty corner) and
    B (full box) as the shading example; small copies to shade."""
    F = Fig()
    R = HEX2
    empty, full, Ts, G = empty_and_full(R)
    s = 0.33
    sw, sh = bbox_of(R, s, 90)
    lab = 0.42

    def copy(x, y):
        X, b = board(F, R, x, y, scale=s, rot=90, grid=GRID_LIGHT, border=BORDER_THIN)
        F.text(b[0] + b[2] / 2, y - 0.12, r'cubes: \rule{0.4in}{0.5pt}', anchor='north')
    # bottom: two rows of five small copies
    for r in range(2):
        for i in range(5):
            copy(0.25 + i * 1.5, lab + (1 - r) * (sh + lab + 0.12))
    y0 = 2 * (sh + lab) + 0.12 + 0.45
    # big board on the left
    X, bb = board(F, R, 0.1, y0, rot=90)
    top = y0 + bb[3]
    # right, top: the examples A and B, with their cube counts
    ye = top - sh - 0.05
    for c, (T, name, n) in enumerate([(empty, 'A', 0), (full, 'B', 8)]):
        x = 4.45 + c * 1.6
        X, b = place(R, x, ye, s, 90, 'sw')
        draw_rhombus_tiling(F, R, T, X)
        F.text(b[0] - 0.17, b[1] + b[3] / 2, r'\large ' + name, anchor='center')
        F.text(b[0] + b[2] / 2, ye - 0.12, r'cubes: %d' % n, anchor='north')
    # right, below the examples: two small copies
    for c in range(2):
        copy(4.45 + c * 1.6, y0 + lab - 0.1)
    save('u4', F)


def figU5():
    """Problem 5 (4-5): A and B again, and twelve small copies for routes of flips."""
    F = Fig()
    R = HEX2
    empty, full, Ts, G = empty_and_full(R)
    s = 0.27
    sw, sh = bbox_of(R, s, 90)
    # two rows of six small copies
    for r in range(2):
        for i in range(6):
            board(F, R, 0.1 + i * 1.25, r * (sh + 0.25), scale=s, rot=90, grid=GRID_LIGHT,
                  border=BORDER_THIN)
    y = 2 * (sh + 0.25) + 0.25
    big = 0.5
    X, b = place(R, 1.2, y, big, 90, 'sw')
    draw_rhombus_tiling(F, R, empty, X)
    F.text(b[0] - 0.3, b[1] + b[3] / 2, r'\Large A', anchor='center')
    X, b = place(R, 4.6, y, big, 90, 'sw')
    draw_rhombus_tiling(F, R, full, X)
    F.text(b[0] - 0.3, b[1] + b[3] / 2, r'\Large B', anchor='center')
    save('u5', F)


def figU6():
    """Problem 6 (4-5): hexagon 1,3,3 at actual size and six small copies."""
    F = Fig()
    R = hexR(1, 3, 3)
    s = 0.3
    sw, sh = bbox_of(R, s, 90)
    # bottom row of four small copies
    for i in range(4):
        board(F, R, 0.1 + i * 1.85, 0, scale=s, rot=90, grid=GRID_LIGHT, border=BORDER_THIN)
    y = sh + 0.45
    X, b = board(F, R, 0.1, y, rot=90)
    for r in range(2):
        board(F, R, 5.65, y + r * (sh + 0.5), scale=s, rot=90, grid=GRID_LIGHT, border=BORDER_THIN)
    save('u6', F)


def figU7():
    """Problem 7 (4-5): twelve small copies of the 2,2,2 hexagon for the trapezoid fillings."""
    F = Fig()
    R = HEX2
    s = 0.4
    sw, sh = bbox_of(R, s, 90)
    for r in range(3):
        for i in range(4):
            board(F, R, 0.3 + i * 1.85, r * (sh + 0.3), scale=s, rot=90, grid=GRID_LIGHT,
                  border=BORDER_THIN)
    save('u7', F)


def trap_tilings_hex2():
    R = frozenset(HEX2)
    Ts = [frozenset(t) for t in tilings(R, trapezoids(R))]
    Ts.sort(key=lambda T: sorted(sorted(p) for p in T))
    return R, Ts


def figU8():
    """Problem 8 (4-5): five small copies for a route of moves, then fillings C and D."""
    F = Fig()
    R, Ts = trap_tilings_hex2()
    # C and D: same middle, different rings (they differ in exactly six trapezoids)
    C = Ts[0]
    D = [T for T in Ts if len(C - T) == 6][0]
    s = 0.55
    for i, (T, lab) in enumerate([(C, 'C'), (D, 'D')]):
        X, b = place(R, 1.3 + i * 3.4, 0, s, 90, 'sw')
        for p in T:
            F.piece(p, X, 'pbred!30')
        F.text(b[0] - 0.35, b[1] + b[3] / 2, r'\Large ' + lab, anchor='center')
    y = b[3] + 0.6
    sc = 0.36
    for i in range(5):
        board(F, R, 0.15 + i * 1.5, y, scale=sc, rot=90, grid=GRID_LIGHT, border=BORDER_THIN)
    save('u8', F)
    return C, D


def figU9():
    """Problem 9 (4-5): four boards drawn small, to decide who wins without playing them out."""
    F = Fig()
    s = 0.3
    boards = [hexR(3, 3, 3), hexR(1, 2, 3), parR(4, 4), parR(5, 2)]
    widths = [bbox_of(R, s)[0] for R in boards]
    gap = (7.3 - sum(widths)) / 3
    x = 0.1
    for R, w in zip(boards, widths):
        X, b = board(F, R, x, 0.5, scale=s, grid=GRID_LIGHT, border=BORDER_THIN)
        F.text(x + w / 2, 0.15, r'\large 1st\hspace{0.3in}2nd', anchor='center')
        x += w + gap
    save('u9', F)


if __name__ == '__main__':
    for old in glob.glob(os.path.join(OUT, '*.tex')):
        os.remove(old)
    figK1(); figK2(); figK3(); figK4(); figK5(); figK6(); figK7()
    figGame1(); figGame2(); figM3(); figM4()
    figTriGame('tri3-4-par', with_par=True); figTriGame('tri3-4')
    figBigHex('bighex'); figM7()
    figU4(); figU5(); figU6(); figU7(); figU8(); figU9()
    print('figures written to', OUT)
