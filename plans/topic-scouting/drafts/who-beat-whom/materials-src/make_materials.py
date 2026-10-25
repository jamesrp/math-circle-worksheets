"""Write materials.tex for "Who beat whom".

All positions are in mm from the top-left corner of a landscape US Letter page
(279.4 x 215.9 mm); the TikZ output converts them to a y-up system anchored at the
page's lower-left corner. Run:  python3 make_materials.py   (writes materials.tex)

Sizes (from the outline and the K-1 big board, which prints 40 mm animal squares and
23 mm lanes, 108 mm long on the sides and 153 mm on the diagonals):
  animal cards 40 x 40 mm, the size of the big board's animal squares;
  arrow cards 75 x 20 mm, short enough for every lane here and on the big board;
  line-up boxes 44 mm square, holding a 40 mm card with 2 mm to spare on each side;
  arrow-card lanes 23 mm wide, as on the big board.
"""
import math

W, H = 279.4, 215.9          # landscape Letter, mm
SIDE = 15.0                  # header/footer text margin
CARD = 40.0                  # animal card
ARROW_L, ARROW_W = 75.0, 20.0
BOX = 44.0                   # line-up box for a 40 mm card
LANE = 23.0                  # lane width for a 20 mm arrow card
NEW = 40.0                   # printed newcomer square (big-board style)
FACE = 16.2                  # face scale in mm, as on the big board (1.62 cm in a 4 cm square)
ANIMALS = ['cat', 'dog', 'bear', 'rabbit', 'frog', 'pig']


def f(x):
    s = f"{x:.3f}".rstrip('0').rstrip('.')
    return s if s not in ('-0', '') else '0'


def P(x, y):
    """Page point (x from left, y from top) -> TikZ coordinate."""
    return f"({f(x)},{f(H - y)})"


class Page:
    def __init__(self):
        self.out = []

    def add(self, s):
        self.out.append(s)

    def text(self, x, y, s, size=11, anchor='north west'):
        lead = size * 1.2
        self.add(f"\\node[anchor={anchor},inner sep=0,font=\\fontsize{{{size}}}{{{f(lead)}}}\\selectfont] "
                 f"at {P(x, y)} {{{s}}};")

    def rect(self, x0, y0, x1, y1, style='line width=0.6pt'):
        self.add(f"\\draw[{style}] {P(x0, y0)} rectangle {P(x1, y1)};")

    def poly(self, pts, style):
        self.add(f"\\draw[{style}] " + " -- ".join(P(x, y) for x, y in pts) + " -- cycle;")

    def fillpoly(self, pts, style='black'):
        self.add(f"\\fill[{style}] " + " -- ".join(P(x, y) for x, y in pts) + " -- cycle;")

    def face(self, name, x, y):
        self.add(f"\\pic[scale={f(FACE)}] at {P(x, y)} {{{name}}};")

    def tex(self, num):
        head = [r"\begin{tikzpicture}[remember picture,overlay,x=1mm,y=1mm,shift={(current page.south west)}]"]
        furn = Page()
        furn.text(SIDE, 12.5, "Week NN / Who beat whom / Materials", 11)
        furn.add(f"\\draw[gray] {P(SIDE, 20)} -- {P(W - SIDE, 20)};")
        furn.add(f"\\draw[gray] {P(SIDE, H - 19)} -- {P(W - SIDE, H - 19)};")
        furn.text(SIDE, H - 17, "Bellingham Math Circle / Week NN / FNN-M-v1", 9)
        furn.text(W - SIDE, H - 17, str(num), 9, anchor='north east')
        return "\n".join(head + furn.out + self.out + [r"\end{tikzpicture}\null\newpage"])


def arrowhead(tip, d, L, Wd):
    """Notched arrowhead as on the student pages: tip, two barbs, notch 0.72 L behind the tip."""
    tx, ty = tip
    dx, dy = d
    nx, ny = -dy, dx
    b1 = (tx - dx * L + nx * Wd / 2, ty - dy * L + ny * Wd / 2)
    b2 = (tx - dx * L - nx * Wd / 2, ty - dy * L - ny * Wd / 2)
    notch = (tx - dx * L * 0.72, ty - dy * L * 0.72)
    return [tip, b1, notch, b2]


def small_arrow(pg, x0, x1, y, L, Wd, lw='1.0pt'):
    """Right-pointing line-up arrow from x0 to x1 (tip) at height y."""
    pg.add(f"\\draw[line width={lw}] {P(x0, y)} -- {P(x1 - L * 0.6, y)};")
    pg.fillpoly(arrowhead((x1, y), (1, 0), L, Wd))


# ------------------------------------------------------------------ page 1: animal cards
def page_animals():
    pg = Page()
    pg.text(SIDE, 24, "Animal cards", 16)
    sets = 3
    gx0 = (W - 6 * CARD) / 2
    gy0 = 36.0
    for r in range(sets):
        for c, a in enumerate(ANIMALS):
            x0, y0 = gx0 + c * CARD, gy0 + r * CARD
            pg.rect(x0, y0, x0 + CARD, y0 + CARD)
            pg.face(a, x0 + CARD / 2, y0 + CARD / 2)
    # scale check
    y = gy0 + sets * CARD + 18
    x0 = gx0
    pg.add(f"\\draw[line width=0.6pt] {P(x0, y)} -- {P(x0 + 100, y)};")
    for x in (x0, x0 + 100):
        pg.add(f"\\draw[line width=0.6pt] {P(x, y - 2.5)} -- {P(x, y + 2.5)};")
    pg.text(x0 + 104, y - 1.6, "100 mm scale check", 9)
    return pg


# ------------------------------------------------------------------ page 2: arrow cards
def arrow_card(pg, x0, y0):
    pg.rect(x0, y0, x0 + ARROW_L, y0 + ARROW_W)
    yc = y0 + ARROW_W / 2
    tip = (x0 + ARROW_L - 3.0, yc)
    L, Wd = 15.0, 13.0
    shaft_end = tip[0] - L * 0.72 + 0.4
    pg.fillpoly([(x0 + 5.0, yc - 1.5), (shaft_end, yc - 1.5), (shaft_end, yc + 1.5), (x0 + 5.0, yc + 1.5)])
    pg.fillpoly(arrowhead(tip, (1, 0), L, Wd))


def page_arrows():
    pg = Page()
    pg.text(SIDE, 24, "Arrow cards", 16)
    cols, rows = 3, 6
    gx0 = (W - cols * ARROW_L) / 2
    gy0 = 38.0
    for r in range(rows):
        for c in range(cols):
            arrow_card(pg, gx0 + c * ARROW_L, gy0 + r * ARROW_W)
    return pg


# ------------------------------------------------------------------ page 3: line-up strip
STRIP_GAP = 12.0
STRIP_PAD = 3.0
STRIP_JOIN = 10.6          # left part's length after box 3


def strip_part(pg, x0, y0, boxes, lead, trail, arrow_after_last):
    """One part of the line-up strip: outer cut rectangle, boxes, arrows between boxes."""
    h = BOX + 2 * STRIP_PAD
    n = len(boxes)
    width = lead + n * BOX + (n - 1) * STRIP_GAP + trail
    pg.rect(x0, y0, x0 + width, y0 + h, 'line width=0.6pt')
    yc = y0 + h / 2
    x = x0 + lead
    for i in range(n):
        pg.add(f"\\draw[line width=1.0pt, rounded corners=2pt] {P(x, y0 + STRIP_PAD)} rectangle {P(x + BOX, y0 + STRIP_PAD + BOX)};")
        if i < n - 1 or arrow_after_last:
            small_arrow(pg, x + BOX + 2.0, x + BOX + STRIP_GAP - 2.0, yc, 4.6, 4.0, lw='1.2pt')
        x += BOX + STRIP_GAP
    return width, h


def page_strip():
    pg = Page()
    pg.text(SIDE, 24, "Line-up strip (K--1)", 16)
    # The left part ends 10.6 mm after box 3, just past the arrow from box 3 to box 4;
    # the right part starts 1.4 mm before box 4, so the joined gap is 12 mm like the others.
    x0 = SIDE
    pg.text(x0, 37, "left part", 9)
    strip_part(pg, x0, 42, [1, 2, 3], STRIP_PAD, STRIP_JOIN, True)
    pg.text(x0, 105, "right part", 9)
    strip_part(pg, x0, 110, [4, 5, 6], STRIP_GAP - STRIP_JOIN, STRIP_PAD, False)
    return pg


# ------------------------------------------------------------------ pages 4-5: joining mats
def sq(cx, cy, s):
    h = s / 2
    return (cx - h, cy - h, cx + h, cy + h)


def rect_pts(s, e, w):
    dx, dy = e[0] - s[0], e[1] - s[1]
    D = math.hypot(dx, dy)
    ux, uy = dx / D, dy / D
    nx, ny = -uy, ux
    hw = w / 2
    return [(s[0] + nx * hw, s[1] + ny * hw), (e[0] + nx * hw, e[1] + ny * hw),
            (e[0] - nx * hw, e[1] - ny * hw), (s[0] - nx * hw, s[1] - ny * hw)]


def slice_hits(c, u, w, b, clear):
    nx, ny = -u[1], u[0]
    x0, y0, x1, y1 = b[0] - clear, b[1] - clear, b[2] + clear, b[3] + clear
    for k in range(-40, 41):
        s = k / 40 * w / 2
        px, py = c[0] + nx * s, c[1] + ny * s
        if x0 < px < x1 and y0 < py < y1:
            return True
    return False


def lane(A, T, w, row_boxes, nbox, clear=1.5, step=0.02):
    """Lane of width w along the line from A (a line-up box centre) toward T, trimmed so
    it clears every line-up box and the newcomer square by `clear` mm."""
    dx, dy = T[0] - A[0], T[1] - A[1]
    D = math.hypot(dx, dy)
    u = (dx / D, dy / D)
    t = 0.0
    while any(slice_hits((A[0] + u[0] * t, A[1] + u[1] * t), u, w, b, clear) for b in row_boxes):
        t += step
    t0 = t
    while not slice_hits((A[0] + u[0] * t, A[1] + u[1] * t), u, w, nbox, clear):
        t += step
    t1 = t - step
    return (A[0] + u[0] * t0, A[1] + u[1] * t0), (A[0] + u[0] * t1, A[1] + u[1] * t1)


MAT_PITCH = 52.0
MAT_ROW_TOP = 23.0
MAT_NEW_BOTTOM = 194.5
# Aim points for the lanes, relative to the newcomer square's centre: spread along its top
# edge and down its sides so that neighbouring lanes overlap only close to the newcomer.
TARGETS = {
    4: [(-20, 4), (-10, -20), (10, -20), (20, 4)],
    5: [(-20, 10), (-16, -20), (0, -20), (16, -20), (20, 10)],
}


def mat_geometry(n):
    xc = W / 2
    yr = MAT_ROW_TOP + BOX / 2
    xs = [xc + (i - (n - 1) / 2) * MAT_PITCH for i in range(n)]
    yn = MAT_NEW_BOTTOM - NEW / 2
    rows = [sq(x, yr, BOX) for x in xs]
    nb = sq(xc, yn, NEW)
    lanes = [lane((x, yr), (xc + tx, yn + ty), LANE, rows, nb) for x, (tx, ty) in zip(xs, TARGETS[n])]
    return xs, yr, xc, yn, rows, nb, lanes


def page_mat(n, animal, label):
    pg = Page()
    xs, yr, xc, yn, rows, nb, lanes = mat_geometry(n)
    for s, e in lanes:
        pg.poly(rect_pts(s, e, LANE), 'gray!70, dashed, line width=0.9pt')
    gap = MAT_PITCH - BOX
    for i, b in enumerate(rows):
        pg.add(f"\\draw[line width=1.0pt, rounded corners=2pt] {P(b[0], b[1])} rectangle {P(b[2], b[3])};")
        if i < n - 1:
            small_arrow(pg, b[2] + 1.2, b[2] + gap - 1.2, yr, 3.6, 3.2, lw='1.0pt')
    pg.add(f"\\filldraw[fill=white, line width=1.2pt, rounded corners=3pt] {P(nb[0], nb[1])} rectangle {P(nb[2], nb[3])};")
    pg.face(animal, xc, yn)
    pg.text(SIDE, MAT_NEW_BOTTOM - 6.5, label, 16)
    return pg


def main():
    pages = [page_animals(), page_arrows(), page_strip(),
             page_mat(4, 'frog', 'K--1 Problem 2: frog'),
             page_mat(5, 'pig', 'K--1 Problem 2: pig')]
    pre = r"""\documentclass[12pt]{article}
\usepackage[letterpaper,landscape,margin=0mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand\familydefault{\sfdefault}
\usepackage{tikz}
\input{animals.tex}
\pagestyle{empty}
\setlength\parindent{0pt}
\pdfinfoomitdate=1\pdftrailerid{}\pdfsuppressptexinfo=15
\pdfinfo{/Title (Who beat whom: materials) /Author (Bellingham Math Circle)}
\begin{document}
\large
"""
    body = "\n".join(p.tex(i + 1) for i, p in enumerate(pages))
    with open('materials.tex', 'w') as fh:
        fh.write(pre + body + "\n\\end{document}\n")
    for n in (4, 5):
        xs, yr, xc, yn, rows, nb, lanes = mat_geometry(n)
        print(n, 'lane lengths', [round(math.hypot(e[0] - s[0], e[1] - s[1]), 1) for s, e in lanes])


if __name__ == '__main__':
    main()
