"""Write materials.tex for Graceful labels (Week NN materials, FNN-M-v1).

Three landscape US Letter pages, drawn at 100% with absolute TikZ
coordinates in millimetres (origin at the page's top-left corner, y down),
in the style of the Week 91 materials file:

  1. Number cards: five sets of cards 0 to 10, 20 mm square, on shared cut
     lines; and the strip from 0 to 10 (Grades 4-5 Problem 7) with 23 mm
     squares, for counters or snap cubes up to 2 cm.
  2. Launch sheet: the triangle with a tail used in the guide's shared
     launch, dots 30 mm across and a 14 mm box on each link.
  3. Trees: the two starter trees of Grades 4-5 Problem 9 at card size
     (dots 25 mm, boxes 10 mm, as on the packets' other card boards).

Sizes come from the outline and the packet drawings: every card board in
the packets clears a square card of 2.41 cm (check_geom.py), so 20 mm cards
leave about 2 mm of slack on the tightest board.
"""
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

PW, PH = 279.4, 215.9          # landscape US Letter, mm
LEFT = 15.0                    # header/footer left edge (Week 91 uses 15 mm)
RIGHT = PW - 15.0
HEAD_Y = 13.0                  # top of the header text
HEAD_RULE = 20.5
FOOT_RULE = PH - 19.5
FOOT_Y = PH - 16.5             # top of the footer text (bottom about 13 mm from the edge)

CARD = 20.0                    # number card side
STRIP_SQ = 23.0                # strip square side
TREE_R = 12.5                  # tree dot radius (25 mm dots, as on the packets' card boards)
TREE_BOX = 10.0
TREE_D = 39.0                  # tree link length, centre to centre
LAUNCH_R = 15.0                # launch sheet dot radius (30 mm dots)
LAUNCH_BOX = 14.0
LAUNCH_SIDE = 80.0

GREY = "black!60"


def f(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return s if s not in ("-0", "") else "0"


class Page:
    def __init__(self, number):
        self.n = number
        self.out = []

    def add(self, s):
        self.out.append(s)

    def text(self, x, y, s, size=11, anchor="north west", colour=None, bold=False):
        col = f",text={colour}" if colour else ""
        b = r"\bfseries" if bold else ""
        lead = size * 1.2
        self.add(rf"\node[anchor={anchor},inner sep=0{col}] at ({f(x)},{f(y)}) "
                 rf"{{\fontsize{{{size}}}{{{f(lead)}}}\selectfont{b} {s}}};")

    def title(self, x, y, name, note=None):
        """Object name (16 pt, as in the Week 91 materials) and a short grey note."""
        s = rf"\fontsize{{16}}{{19}}\selectfont {name}"
        if note:
            s += rf"\hspace{{5mm}}{{\fontsize{{11}}{{13}}\selectfont\color{{{GREY}}} {note}}}"
        self.add(rf"\node[anchor=north west,inner sep=0] at ({f(x)},{f(y)}) {{{s}}};")

    def scale_check(self, x, y):
        """A 50 mm bar with end ticks, its left end at (x, y)."""
        self.add(rf"\draw[line width=0.6pt] ({f(x)},{f(y)}) -- ({f(x + 50)},{f(y)});")
        for xx in (x, x + 50):
            self.add(rf"\draw[line width=0.6pt] ({f(xx)},{f(y - 2)}) -- ({f(xx)},{f(y + 2)});")
        self.text(x + 25, y + 3, "50 mm scale check", size=9, anchor="north", colour=GREY)

    def render(self):
        head = [r"\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm,shift={(current page.north west)}]"]
        head.append(rf"\node[anchor=north west,inner sep=0] at ({f(LEFT)},{f(HEAD_Y)}) "
                    r"{\fontsize{11}{14}\selectfont Week NN / Graceful labels / Materials};")
        head.append(rf"\draw[gray] ({f(LEFT)},{f(HEAD_RULE)}) -- ({f(RIGHT)},{f(HEAD_RULE)});")
        foot = [rf"\draw[gray] ({f(LEFT)},{f(FOOT_RULE)}) -- ({f(RIGHT)},{f(FOOT_RULE)});",
                rf"\node[anchor=north west,inner sep=0] at ({f(LEFT)},{f(FOOT_Y)}) "
                r"{\fontsize{9}{11.5}\selectfont Bellingham Math Circle / Week NN / FNN-M-v1};",
                rf"\node[anchor=north east,inner sep=0] at ({f(RIGHT)},{f(FOOT_Y)}) "
                rf"{{\fontsize{{9}}{{11.5}}\selectfont {self.n}}};",
                r"\end{tikzpicture}\null\newpage"]
        return "\n".join(head + self.out + foot) + "\n"


# --------------------------------------------------------------- page 1
def set_mark(p, cx, cy, kind):
    """A small grey mark that tells the five card sets apart."""
    s = 1.15
    if kind == 0:
        p.add(rf"\fill[{GREY}] ({f(cx)},{f(cy)}) circle ({f(s)});")
    elif kind == 1:
        p.add(rf"\fill[{GREY}] ({f(cx - s)},{f(cy - s)}) rectangle ({f(cx + s)},{f(cy + s)});")
    elif kind == 2:
        h = s * 1.25
        p.add(rf"\fill[{GREY}] ({f(cx)},{f(cy - h)}) -- ({f(cx + h)},{f(cy + h * 0.8)}) -- ({f(cx - h)},{f(cy + h * 0.8)}) -- cycle;")
    elif kind == 3:
        h = s * 1.35
        p.add(rf"\fill[{GREY}] ({f(cx)},{f(cy - h)}) -- ({f(cx + h)},{f(cy)}) -- ({f(cx)},{f(cy + h)}) -- ({f(cx - h)},{f(cy)}) -- cycle;")
    else:
        pts = []
        for k in range(10):
            rad = 1.6 if k % 2 == 0 else 0.68
            a = math.radians(-90 + 36 * k)
            pts.append(f"({f(cx + rad * math.cos(a))},{f(cy + rad * math.sin(a))})")
        p.add(rf"\fill[{GREY}] " + " -- ".join(pts) + " -- cycle;")


def page_cards():
    p = Page(1)
    top = 26.0
    p.title(LEFT, top, "Number cards", "Grades 2--3 and 4--5")
    p.scale_check(RIGHT - 50, top + 3.5)
    cols, rows = 11, 5
    x0 = (PW - cols * CARD) / 2
    y0 = 37.0
    for r in range(rows):
        for c in range(cols):
            x, y = x0 + c * CARD, y0 + r * CARD
            p.add(rf"\draw[line width=0.5pt] ({f(x)},{f(y)}) rectangle ({f(x + CARD)},{f(y + CARD)});")
            cx, cy = x + CARD / 2, y + CARD / 2
            # digits are placed by their baseline so that round and flat tops line up
            p.add(rf"\node[anchor=base,inner sep=0] at ({f(cx)},{f(cy + 4.25)}) {{\fontsize{{34}}{{34}}\selectfont\bfseries {c}}};")
            if c in (6, 9):
                p.add(rf"\draw[line width=1.3pt] ({f(cx - 3.6)},{f(cy + 6.0)}) -- ({f(cx + 3.6)},{f(cy + 6.0)});")
            set_mark(p, x + CARD - 2.9, y + CARD - 2.9, r)

    # the strip from 0 to 10, Grades 4-5 Problem 7
    ty = y0 + rows * CARD + 11.0
    p.title(LEFT, ty, "Strip from 0 to 10", "Grades 4--5 Problem 7")
    sx0 = (PW - 11 * STRIP_SQ) / 2
    sy = ty + 11.0
    for i in range(11):
        x = sx0 + i * STRIP_SQ
        p.add(rf"\draw[line width=0.9pt] ({f(x)},{f(sy)}) rectangle ({f(x + STRIP_SQ)},{f(sy + STRIP_SQ)});")
        p.text(x + STRIP_SQ / 2, sy + STRIP_SQ + 6.2, str(i), size=14, anchor="base")
    return p


# --------------------------------------------------------------- networks
def network(p, pts, edges, r, box, caption=None, capsize=12, lw="0.9pt", boxlw="0.7pt"):
    for a, b in edges:
        (x1, y1), (x2, y2) = pts[a], pts[b]
        p.add(rf"\draw[line width={lw}] ({f(x1)},{f(y1)}) -- ({f(x2)},{f(y2)});")
    h = box / 2
    for a, b in edges:
        (x1, y1), (x2, y2) = pts[a], pts[b]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        p.add(rf"\draw[line width={boxlw}, fill=white] ({f(mx - h)},{f(my - h)}) rectangle ({f(mx + h)},{f(my + h)});")
    for x, y in pts:
        p.add(rf"\draw[line width={lw}, fill=white] ({f(x)},{f(y)}) circle ({f(r)});")
    if caption:
        xs = [q[0] for q in pts]
        ys = [q[1] for q in pts]
        p.text((min(xs) + max(xs)) / 2, max(ys) + r + 1.8, caption, size=capsize, anchor="north")


def page_launch():
    p = Page(2)
    top = 26.0
    p.title(LEFT, top, "Launch sheet")
    p.scale_check(RIGHT - 50, top + 3.5)
    s = LAUNCH_SIDE
    hgt = s * math.sqrt(3) / 2
    width = 2 * s + 2 * LAUNCH_R
    lx = (PW - width) / 2 + LAUNCH_R
    area_top, area_bot = 40.0, FOOT_RULE - 8.0
    ty = (area_top + area_bot) / 2 - (hgt + 2 * LAUNCH_R) / 2 + LAUNCH_R
    T = (lx + s / 2, ty)
    L = (lx, ty + hgt)
    R = (lx + s, ty + hgt)
    E = (lx + 2 * s, ty + hgt)
    network(p, [T, L, R, E], [(0, 1), (1, 2), (2, 0), (2, 3)], LAUNCH_R, LAUNCH_BOX,
            lw="1.1pt", boxlw="0.9pt")
    return p


def page_trees():
    p = Page(3)
    d = TREE_D
    r = TREE_R
    # the spider (cards 0 to 6), top left: legs of two links to the left, right and down
    edge = 13.0                            # closest approach of a dot to the paper edge
    sx = edge + r + 2 * d                  # its middle dot
    sy = HEAD_RULE + 4.0 + r
    spider = [(sx, sy), (sx - d, sy), (sx - 2 * d, sy), (sx + d, sy), (sx + 2 * d, sy),
              (sx, sy + d), (sx, sy + 2 * d)]
    network(p, spider, [(0, 1), (1, 2), (0, 3), (3, 4), (0, 5), (5, 6)], r, TREE_BOX,
            caption="cards 0 to 6")
    # the caterpillar (cards 0 to 7), bottom right: a spine of four dots
    cap_h = 8.0
    cy = FOOT_RULE - 3.0 - cap_h - r - d        # spine height
    cx0 = PW - edge - r - 3 * d                # left end of the spine
    cat = [(cx0, cy), (cx0 + d, cy), (cx0 + 2 * d, cy), (cx0 + 3 * d, cy),
           (cx0 + d, cy - d), (cx0 + d, cy + d), (cx0 + 2 * d, cy + d), (cx0 + 3 * d, cy + d)]
    network(p, cat, [(0, 1), (1, 2), (2, 3), (1, 4), (1, 5), (2, 6), (3, 7)], r, TREE_BOX,
            caption="cards 0 to 7")
    # name and note in the empty top-right corner, scale check bottom left
    p.add(rf"\node[anchor=north east,inner sep=0,align=right] at ({f(RIGHT)},{f(HEAD_RULE + 5.5)}) "
          rf"{{\fontsize{{16}}{{19}}\selectfont Trees\\[1mm]"
          rf"\fontsize{{11}}{{13}}\selectfont\color{{{GREY}}} Grades 4--5 Problem 9}};")
    p.scale_check(LEFT, FOOT_RULE - 22.0)
    return p


def main():
    pages = [page_cards(), page_launch(), page_trees()]
    doc = [r"\documentclass[12pt]{article}",
           r"\usepackage[letterpaper,landscape,margin=0mm]{geometry}",
           r"\usepackage[T1]{fontenc}",
           r"\usepackage{helvet}",
           r"\renewcommand\familydefault{\sfdefault}",
           r"\usepackage{xcolor}",
           r"\usepackage{tikz}",
           r"\pagestyle{empty}",
           r"\setlength\parindent{0pt}",
           r"\pdfinfoomitdate=1\pdftrailerid{}\pdfsuppressptexinfo=15",
           r"\begin{document}"]
    for pg in pages:
        doc.append(pg.render())
    doc.append(r"\end{document}")
    with open(os.path.join(HERE, "materials.tex"), "w") as fh:
        fh.write("\n".join(doc) + "\n")
    print("wrote materials.tex")


if __name__ == "__main__":
    main()
