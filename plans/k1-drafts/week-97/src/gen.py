#!/usr/bin/env python3
"""Generate k-1.tex for Week 97 K-1 (Square remainders), packet W97-K-v1.

Revised after review: the shared rules and worked strip sit above Problem 1,
the actual-size board is a separate sheet at the back, and the packet has
three secret-square rounds (groups of 4, 6 and 8) plus a groups-of-2 page.

All lengths in the TikZ pictures are millimetres (x=1mm, y=1mm).
Boards and group cards that hold real tiles use 26 mm cells (1-inch tiles).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CELL = 26.0  # actual-size cell for 1-inch tiles
TW = 180.0   # usable text width in mm (8.5in - 2 x 0.7in = 180.3 mm)

PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage[letterpaper,left=0.7in,right=0.7in,top=0.85in,bottom=0.85in,
  headheight=16pt,headsep=12pt,footskip=26pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage{tgheros}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\lhead{\small Week 97 / Square remainders / K--1}
\lfoot{\small Bellingham Math Circle / Week 97 / W97-K-v1}
\rfoot{\small \thepage}
\renewcommand{\headrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\definecolor{tilefill}{RGB}{126,166,214}
\definecolor{tileline}{RGB}{40,70,115}
\definecolor{ringA}{RGB}{70,118,190}
\definecolor{ringB}{RGB}{245,205,85}
\definecolor{cardfill}{RGB}{255,246,214}
\tikzset{
  tile/.style={fill=tilefill,draw=tileline,line width=0.45pt},
  wbox/.style={draw=black,line width=0.9pt,rounded corners=1.5mm},
  lab/.style={font=\normalsize},
}
\newcommand{\prob}[1]{\textbf{Problem #1:}~}
\begin{document}
\large
"""

END = r"""
\end{document}
"""


def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


# ---------- drawing helpers (return TikZ code strings) ----------

def tile(x, y, c, style="tile", inset=None):
    """One tile with lower-left cell corner (x, y), cell size c."""
    g = inset if inset is not None else max(0.3, 0.06 * c)
    return (f"\\filldraw[{style}] ({f(x+g)},{f(y+g)}) rectangle "
            f"({f(x+c-g)},{f(y+c-g)});\n")


def ghost(x, y, c):
    g = max(0.3, 0.06 * c)
    return (f"\\filldraw[fill=black!6,draw=black!18,line width=0.3pt] ({f(x+g)},{f(y+g)}) "
            f"rectangle ({f(x+c-g)},{f(y+c-g)});\n")


def rect_tiles(x0, y0, cols, rows, c, style="tile"):
    s = ""
    for i in range(cols):
        for j in range(rows):
            s += tile(x0 + i * c, y0 + j * c, c, style)
    return s


def ring_square(x0, y0, n, c):
    """n x n square (n odd) coloured by rings from the middle out."""
    s = ""
    mid = (n - 1) // 2
    for i in range(n):
        for j in range(n):
            k = max(abs(i - mid), abs(j - mid))
            col = "ringA" if k % 2 == 0 else "ringB"
            s += tile(x0 + i * c, y0 + j * c, c,
                      f"fill={col},draw=tileline,line width=0.45pt")
    return s


def wbox(cx, ytop, size=13, text=None):
    s = (f"\\draw[wbox] ({f(cx-size/2)},{f(ytop-size)}) rectangle "
         f"({f(cx+size/2)},{f(ytop)});\n")
    if text is not None:
        s += (f"\\node[font=\\LARGE,text=black!45] at ({f(cx)},{f(ytop-size/2)}) "
              f"{{{text}}};\n")
    return s


def group_card(x0, y0, cols, rows, c=CELL, pad=4.0):
    """Actual-size group card: cols x rows cells of size c, lower-left (x0, y0)."""
    w = cols * c + 2 * pad
    h = rows * c + 2 * pad
    s = (f"\\filldraw[fill=cardfill,draw=black,line width=1.1pt,rounded corners=3mm] "
         f"({f(x0)},{f(y0)}) rectangle ({f(x0+w)},{f(y0+h)});\n")
    for i in range(cols):
        for j in range(rows):
            x = x0 + pad + i * c
            y = y0 + pad + j * c
            s += (f"\\filldraw[fill=white,draw=black!70,line width=0.6pt] "
                  f"({f(x)},{f(y)}) rectangle ({f(x+c)},{f(y+c)});\n")
    return s, w, h


def card_size(cols, rows, c=CELL, pad=4.0):
    return cols * c + 2 * pad, rows * c + 2 * pad


def tikz(body, extra=""):
    return f"\\begin{{tikzpicture}}[x=1mm,y=1mm{extra}]\n{body}\\end{{tikzpicture}}"


# ---------- record row of squares ----------

def square_record(sides, c=5.5, gap=10.5, prefill=None, box=13):
    """Squares sitting on a baseline, side number under each, then a writing
    box. prefill: {side: text} printed in grey in the box."""
    prefill = prefill or {}
    s = ""
    x = 0.0
    for n in sides:
        s += rect_tiles(x, 0, n, n, c)
        cx = x + n * c / 2
        s += f"\\node[lab] at ({f(cx)},-4) {{{n}}};\n"
        s += wbox(cx, -8, box, prefill.get(n))
        x += n * c + gap
    return s


def band(card_dims, numerals=None):
    """Full-width strip: numerals to circle at the left (optional) and the
    actual-size group card at the right."""
    w, h = card_size(*card_dims)
    s = f"\\useasboundingbox (0,0) rectangle ({f(TW)},{f(-h)});\n"
    if numerals:
        sp = min(22.0, (TW - w - 30) / max(1, len(numerals) - 1))
        for k, n in enumerate(numerals):
            s += f"\\node[font=\\Huge] at ({f(10 + k * sp)},-9) {{{n}}};\n"
    gc, _, _ = group_card(TW - w, -h, *card_dims)
    s += gc
    return "\\noindent" + tikz(s) + "\\par\n"


# ---------- pages ----------

def worked_strip():
    """The shared launch: a 3 x 3 square in groups of 4 leaves 1.
    Three states joined by 'next' arrows; each later state has the full card
    beside it. The record (side 3, box 1) sits under the starting square,
    exactly as in the problems' record rows."""
    c = 6.0
    s = ""

    def square_state(x0, keep):
        out = ""
        for i in range(3):
            for j in range(3):
                if (i, j) in keep:
                    out += tile(x0 + i * c, j * c, c)
                else:
                    out += ghost(x0 + i * c, j * c, c)
        return out

    def small_card(x0):
        out = (f"\\filldraw[fill=cardfill,draw=black,line width=0.8pt,rounded corners=1mm] "
               f"({f(x0)},2) rectangle ({f(x0+16)},16);\n")
        for i in range(2):
            for j in range(2):
                out += (f"\\draw[black!60,line width=0.4pt] ({f(x0+2+i*c)},{f(3+j*c)}) "
                        f"rectangle ({f(x0+2+(i+1)*c)},{f(3+(j+1)*c)});\n")
                out += tile(x0 + 2 + i * c, 3 + j * c, c)
        return out

    def arrow(x0):
        return (f"\\draw[-{{Stealth[length=3mm]}},line width=1pt] ({f(x0)},9) -- "
                f"({f(x0+11)},9);\n")

    all_cells = {(i, j) for i in range(3) for j in range(3)}
    # first group: top row and one more (not the card's shape)
    g1 = {(0, 2), (1, 2), (2, 2), (0, 1)}
    # second group: four of the remaining five
    g2 = {(1, 1), (2, 1), (0, 0), (1, 0)}
    s += square_state(0, all_cells)
    s += "\\node[lab] at (9,-4) {3};\n"
    s += wbox(9, -8, 13, "1")
    s += arrow(23)
    s += square_state(39, all_cells - g1)
    s += small_card(60)
    s += arrow(81)
    s += square_state(97, all_cells - g1 - g2)
    s += small_card(118)
    return tikz(s)


def page_one():
    rules = (
        "Build each square on the board, filled in. To take away a group, fill "
        "the group card with tiles from the square and put them in the cup. "
        "When too few tiles are left to fill the card, those tiles are the "
        "leftover. The leftover can be 0.\\par\n"
    )
    rec = tikz(square_record(range(1, 7), prefill={3: "1"}))
    return (
        rules +
        "\\vspace{6mm}\n{\\centering " + worked_strip() + "\\par}\n"
        "\\vspace{10mm}\n"
        "\\prob{1}Build each square and take away groups of~4. "
        "Circle every number a square can leave.\\par\n"
        "\\vspace{9mm}\n{\\centering " + rec + "\\par}\n"
        "\\vspace{9mm}\n" + band((2, 2), [0, 1, 2, 3]) +
        "\\vfill\n\\newpage\n"
    )


def page_squares(num, text, card_dims, sides=range(1, 7), numerals=None):
    rec = tikz(square_record(sides))
    return (
        f"\\prob{{{num}}}{text}\\par\n"
        "\\vspace{10mm}\n{\\centering " + rec + "\\par}\n"
        "\\vspace{10mm}\n" + band(card_dims, numerals) +
        "\\vfill\n\\newpage\n"
    )


def page_rectangles(num):
    c = 6.0
    rects = [(4, 3), (3, 2), (5, 2), (5, 3)]  # (width, height); 4 x 3 first
    s = ""
    x = 0.0
    gap = 22
    for (wd, ht) in rects:
        s += rect_tiles(x, 0, wd, ht, c)
        cx = x + wd * c / 2
        s += f"\\node[lab] at ({f(cx)},-4) {{{wd}}};\n"
        s += f"\\node[lab] at ({f(x-3.5)},{f(ht*c/2)}) {{{ht}}};\n"
        s += wbox(cx, -8)
        x += wd * c + gap
    rec = tikz(s)
    return (
        f"\\prob{{{num}}}Build each rectangle and take away groups of~4. "
        "Can a rectangle leave 2~or~3?\\par\n"
        "\\vspace{10mm}\n{\\centering " + rec + "\\par}\n"
        "\\vspace{10mm}\n" + band((2, 2)) +
        "\\vfill\n\\newpage\n"
    )


def mini_card(x0, y0, n, w=22, h=28, dot_sp=2.9, r=0.85, numsize="\\Large"):
    s = (f"\\draw[line width=0.7pt,rounded corners=1mm] ({f(x0)},{f(y0)}) rectangle "
         f"({f(x0+w)},{f(y0+h)});\n")
    s += f"\\node[font={numsize}\\bfseries] at ({f(x0+w/2)},{f(y0+h-5.5)}) {{{n}}};\n"
    span = (n - 1) * dot_sp
    cx = x0 + w / 2
    cy = y0 + (h - 10) / 2 + 0.5
    for i in range(n):
        for j in range(n):
            s += (f"\\fill[tileline] ({f(cx - span/2 + i*dot_sp)},"
                  f"{f(cy - span/2 + j*dot_sp)}) circle ({f(r)});\n")
    return s


def page_secret(num, text, sides, card_dims, rounds=4):
    # the allowed cards, exactly as laid out on the table
    s = ""
    for k, n in enumerate(sides):
        s += mini_card(k * 27, 0, n)
    cards = tikz(s)
    # record: leftover box, then the allowed cards to circle; one row a round
    r = ""
    row_h = 21.0
    for t in range(rounds):
        y = -t * row_h
        r += f"\\draw[wbox] (0,{f(y-15)}) rectangle (15,{f(y)});\n"
        for k, n in enumerate(sides):
            x = 25 + k * 18
            r += (f"\\draw[line width=0.7pt,rounded corners=1mm] ({f(x)},{f(y-15)}) "
                  f"rectangle ({f(x+14)},{f(y)});\n")
            r += f"\\node[font=\\LARGE] at ({f(x+7)},{f(y-7.5)}) {{{n}}};\n"
    rows = tikz(r)
    return (
        f"\\prob{{{num}}}{text}\\par\n"
        "\\vspace{7mm}\n{\\centering " + cards + "\\par}\n"
        "\\vspace{10mm}\n"
        "\\noindent\\hspace*{3mm}" + rows + "\\par\n"
        "\\vspace{8mm}\n" + band(card_dims) +
        "\\vfill\n\\newpage\n"
    )


def page_big(num):
    c = 8.0
    s = ""
    s += rect_tiles(0, 0, 9, 9, c, "fill=tilefill!45,draw=tileline,line width=0.4pt")
    s += f"\\node[lab] at ({f(4.5*c)},-4) {{9}};\n"
    s += wbox(4.5 * c, -8)
    x2 = 9 * c + 16
    s += rect_tiles(x2, 0, 10, 10, c, "fill=tilefill!45,draw=tileline,line width=0.4pt")
    s += f"\\node[lab] at ({f(x2+5*c)},-4) {{10}};\n"
    s += wbox(x2 + 5 * c, -8)
    return (
        f"\\prob{{{num}}}Without building these squares, find what each one would leave "
        "in groups of~4. Explain how you know.\\par\n"
        "\\vspace{8mm}\n{\\centering " + tikz(s) + "\\par}\n"
        "\\vfill\n\\newpage\n"
    )


def page_rings(num):
    c = 7.0
    s = ""
    x = 0.0
    gap = 14
    for n in (1, 3, 5):
        s += ring_square(x, 0, n, c)
        cx = x + n * c / 2
        s += f"\\node[lab] at ({f(cx)},-4) {{{n}}};\n"
        s += wbox(cx, -8)
        x += n * c + gap
    w, h = card_size(2, 4)
    gc, _, _ = group_card(TW - 6 - w, 35 - h, 2, 4)
    return (
        f"\\prob{{{num}}}Build each square on the table from the middle out, one ring "
        "at a time, and take away groups of~8. What does each square leave?\\par\n"
        "\\vspace{8mm}\n"
        "\\noindent\\hspace*{3mm}" + tikz(s + gc) + "\\par\n"
        "\\vfill\n\\newpage\n"
    )


def page_seven(num):
    c = 10.0
    s7 = ring_square(0, 0, 7, c)
    s7 += f"\\node[lab] at ({f(3.5*c)},-4) {{7}};\n"
    s7 += wbox(3.5 * c, -8)
    return (
        f"\\prob{{{num}}}What would this square leave in groups of~8? "
        "Explain how you know.\\par\n"
        "\\vspace{8mm}\n"
        "\\noindent\\hspace*{3mm}" + tikz(s7) + "\\par\n"
        "\\vfill\n\\newpage\n"
    )


def page_board():
    """Actual-size board, nested squares from the top-left corner.
    No shading: only the grid and the thick outlines of sides 1 to 6."""
    b = ""
    C = CELL
    for t in range(1, 6):
        b += f"\\draw[black!35,line width=0.4pt] ({f(t*C)},0) -- ({f(t*C)},{f(-6*C)});\n"
        b += f"\\draw[black!35,line width=0.4pt] (0,{f(-t*C)}) -- ({f(6*C)},{f(-t*C)});\n"
    for n in range(1, 6):
        b += (f"\\draw[black,line width=1.5pt] (0,{f(-n*C)}) -- ({f(n*C)},{f(-n*C)}) "
              f"-- ({f(n*C)},0);\n")
    b += f"\\draw[black,line width=1.8pt] (0,0) rectangle ({f(6*C)},{f(-6*C)});\n"
    for n in range(1, 7):
        b += f"\\node[font=\\large,text=black!70] at ({f(n*C-C/2)},5) {{{n}}};\n"
        b += f"\\node[font=\\large,text=black!70] at (-5,{f(-(n*C-C/2))}) {{{n}}};\n"
    return "\\vspace*{6mm}\n{\\centering " + tikz(b) + "\\par}\n\\vfill\n\\newpage\n"


def page_cards():
    W, H = 58.0, 74.0
    s = ""
    for k, n in enumerate(range(1, 7)):
        col = k % 3
        row = k // 3
        x0 = col * W
        y0 = -(row + 1) * H
        s += f"\\node[font=\\fontsize{{40}}{{44}}\\selectfont\\bfseries] at ({f(x0+W/2)},{f(y0+H-14)}) {{{n}}};\n"
        sp = 5.0
        span = (n - 1) * sp
        cx = x0 + W / 2
        cy = y0 + (H - 26) / 2 + 2
        for i in range(n):
            for j in range(n):
                s += (f"\\fill[tileline] ({f(cx-span/2+i*sp)},{f(cy-span/2+j*sp)}) "
                      f"circle (1.5);\n")
    # dashed cut lines
    for col in range(4):
        s += f"\\draw[dashed,line width=0.7pt,black!60] ({f(col*W)},0) -- ({f(col*W)},{f(-2*H)});\n"
    for row in range(3):
        s += f"\\draw[dashed,line width=0.7pt,black!60] (0,{f(-row*H)}) -- ({f(3*W)},{f(-row*H)});\n"
    return "\\vspace*{8mm}\n{\\centering " + tikz(s) + "\\par}\n\\vfill\n"


def main():
    out = PREAMBLE
    out += page_one()                                                   # P1, g4
    out += page_secret(2, "Behind the folder, one partner builds the square from "
                       "one of these cards and takes away groups of~4. The other "
                       "partner sees only the leftover and circles every card that "
                       "could have made it. Then show the card.",
                       range(1, 6), (2, 2))                             # P2 game g4
    out += page_rectangles(3)                                           # P3 g4
    out += page_squares(4, "Build each square and take away groups of~3. "
                        "Circle every number a square can leave.", (3, 1),
                        numerals=[0, 1, 2])                             # P4 g3
    out += page_squares(5, "Build each square and take away groups of~6. "
                        "Circle every number a square can leave.", (2, 3),
                        numerals=[0, 1, 2, 3, 4, 5])                    # P5 g6
    out += page_secret(6, "Play Problem~2 again with these cards and groups of~6.",
                       range(1, 7), (3, 2))                             # P6 game g6
    out += page_squares(7, "Build each square and take away groups of~2. "
                        "Which squares leave~1?", (2, 1), sides=range(1, 6))  # P7 g2
    out += page_big(8)                                                  # P8 g4
    out += page_rings(9)                                                # P9 g8
    out += page_seven(10)                                               # P10 g8
    out += page_secret(11, "Play Problem~2 again with these cards and groups of~8.",
                       range(1, 7), (4, 2))                             # P11 game g8
    out += page_board()
    out += page_cards()
    out += END
    with open(os.path.join(HERE, "k-1.tex"), "w") as fh:
        fh.write(out)


if __name__ == "__main__":
    main()
