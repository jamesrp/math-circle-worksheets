"""Build k-1.tex for Week 66 K-1 (Lamplighter streets).

Run:  python3 pages.py && pdflatex k-1.tex
All lengths in TikZ pictures are millimetres.
"""
from problems import P1, P2, P3, P4, P5, P6_TOP, P6, P7_TOP, P7, P8

# ---------------------------------------------------------------- picture parts
PITCH = 10.9        # target pictures: lamp centres
R_LAMP = 4.0        # target pictures: lamp radius
FRAME_W = 80.0
SQ = 9.0            # record squares (two rows of six)
SQ_COLS, SQ_ROWS = 6, 2
SQ_H = SQ_ROWS * SQ  # height of the record grid
ROW_SQ = 9.5        # Problem 5: squares in each row of marks
ROW_N = 8           # Problem 5: squares per row
ROW_LINES = 5       # Problem 5: rows per picture
ROW_GAP = 2.6       # Problem 5: gap between rows

ST_PITCH = 24.0     # working street: lamp centres (17 mm counters)
ST_R = 10.0         # working street: lamp radius (20 mm circles)
SPOT_R = 8.5        # working street: walker spot radius
PAWN_S = 1.08       # walker glyph scale in target pictures
HOUSE_H = 4.8       # home mark height in target pictures


def pawn(x, yb, s=1.0):
    """Walker glyph standing with its base at (x, yb), scale s (height ~6.8*s)."""
    def p(dx, dy):
        return f"({x + dx * s:.2f},{yb + dy * s:.2f})"
    return (
        f"\\draw[line width=0.4pt, fill=black!45] {p(-2.5, 0)} -- {p(2.5, 0)} -- {p(2.5, 0.9)} "
        f"-- {p(1.8, 0.9)} .. controls {p(1.2, 2.2)} and {p(0.9, 3.2)} .. {p(0.9, 4.0)} "
        f"-- {p(-0.9, 4.0)} .. controls {p(-0.9, 3.2)} and {p(-1.2, 2.2)} .. {p(-1.8, 0.9)} "
        f"-- {p(-2.5, 0.9)} -- cycle;\n"
        f"\\draw[line width=0.4pt, fill=black!45] {p(0, 5.35)} circle ({1.45 * s:.2f});\n"
    )


def house(x, ytop, w, h, r, lw="0.5pt"):
    """Home mark: apex at (x, ytop), roof height r, wall height h, width w."""
    return (
        f"\\draw[line width={lw}, line join=round] ({x:.2f},{ytop:.2f}) -- ({x + w / 2:.2f},{ytop - r:.2f}) "
        f"-- ({x + w / 2:.2f},{ytop - r - h:.2f}) -- ({x - w / 2:.2f},{ytop - r - h:.2f}) "
        f"-- ({x - w / 2:.2f},{ytop - r:.2f}) -- cycle;\n"
    )


def target(cx, cy, tgt, squares=True):
    """A target picture centred horizontally at cx with lamp centres at height cy.
    Returns (tikz, (x0, y0, x1, y1)) where the box is the frame."""
    lit, w = tgt
    out = []
    top = cy + R_LAMP + 1.0 + 6.8 * PAWN_S + 2.2
    bottom = cy - (R_LAMP + 1.0 + HOUSE_H) - (2.2 + SQ_H + 2.4 if squares else 2.4)
    x0, x1 = cx - FRAME_W / 2, cx + FRAME_W / 2
    out.append(f"\\draw[line width=0.5pt, black!55, rounded corners=2.5] ({x0:.2f},{bottom:.2f}) rectangle ({x1:.2f},{top:.2f});\n")
    out.append(f"\\draw[line width=0.9pt, black!40] ({cx - 3 * PITCH:.2f},{cy:.2f}) -- ({cx + 3 * PITCH:.2f},{cy:.2f});\n")
    for i in range(-3, 4):
        x = cx + i * PITCH
        fill = "black!80" if i in lit else "white"
        out.append(f"\\draw[line width=0.6pt, fill={fill}] ({x:.2f},{cy:.2f}) circle ({R_LAMP});\n")
    out.append(pawn(cx + w * PITCH, cy + R_LAMP + 1.0, s=PAWN_S))
    out.append(house(cx, cy - R_LAMP - 1.0, 4.6, 2.6, 2.2))
    if squares:
        ytop = cy - (R_LAMP + 1.0 + HOUSE_H) - 2.2
        xl = cx - SQ_COLS * SQ / 2
        for r in range(SQ_ROWS):
            for k in range(SQ_COLS):
                xa, ya = xl + k * SQ, ytop - (r + 1) * SQ
                out.append(f"\\draw[line width=0.5pt, black!70] ({xa:.2f},{ya:.2f}) rectangle ({xa + SQ:.2f},{ya + SQ:.2f});\n")
    return "".join(out), (x0, bottom, x1, top)


def street():
    """The working street: seven 20 mm lamps on 24 mm centres, walker spots above."""
    out = ["\\begin{tikzpicture}[x=1mm, y=1mm]\n"]
    out.append(f"\\draw[line width=1.4pt, black!35] ({-3 * ST_PITCH - 6:.1f},0) -- ({3 * ST_PITCH + 6:.1f},0);\n")
    for i in range(-3, 4):
        x = i * ST_PITCH
        out.append(f"\\draw[line width=0.9pt, fill=white] ({x:.1f},0) circle ({ST_R});\n")
        out.append(f"\\draw[line width=0.6pt, black!60, dash pattern=on 2pt off 1.6pt] ({x:.1f},{ST_R + 3 + SPOT_R:.1f}) circle ({SPOT_R});\n")
    out.append(house(0, -ST_R - 1.8, 8.0, 4.6, 3.4, lw="0.8pt"))
    out.append("\\end{tikzpicture}")
    return "".join(out)


def grid4(targets):
    """Four target pictures in two rows of two, each with record squares."""
    out = ["\\begin{tikzpicture}[x=1mm, y=1mm]\n"]
    xs = (-(FRAME_W / 2 + 5), FRAME_W / 2 + 5)
    rowgap = 55.0
    for k, t in enumerate(targets):
        cx = xs[k % 2]
        cy = -(k // 2) * rowgap
        out.append(target(cx, cy, t)[0])
    out.append("\\end{tikzpicture}")
    return "".join(out)


MINI_PITCH, MINI_R, MINI_PAWN = 5.8, 2.2, 0.68


def mini_lamps(cx, cy, lit, w):
    """A three-lamp piece of street with the walker over lamp w (-1, 0 or 1)."""
    pitch, r = MINI_PITCH, MINI_R
    out = [f"\\draw[line width=0.7pt, black!40] ({cx - pitch:.2f},{cy:.2f}) -- ({cx + pitch:.2f},{cy:.2f});\n"]
    for i in (-1, 0, 1):
        fill = "black!80" if i in lit else "white"
        out.append(f"\\draw[line width=0.5pt, fill={fill}] ({cx + i * pitch:.2f},{cy:.2f}) circle ({r});\n")
    out.append(pawn(cx + w * pitch, cy + r + 0.8, s=MINI_PAWN))
    return "".join(out)


def label_arrow(a, b, lab, side=1, off=3.6, head="2.2mm", lw="0.7pt", font="\\sffamily\\bfseries\\small"):
    """Arrow from a to b with its label set off to one side of the shaft.
    side=+1 puts the label on the left of the direction of travel, -1 on the right."""
    (xa, ya), (xb, yb) = a, b
    dx, dy = xb - xa, yb - ya
    n = (dx * dx + dy * dy) ** 0.5
    nx, ny = -dy / n * side, dx / n * side
    mx, my = (xa + xb) / 2 + nx * off, (ya + yb) / 2 + ny * off
    return (f"\\draw[-{{Stealth[length={head}]}}, line width={lw}] ({xa:.2f},{ya:.2f}) -- ({xb:.2f},{yb:.2f});\n"
            f"\\node[font={font}, inner sep=0pt] at ({mx:.2f},{my:.2f}) {{{lab}}};\n")


def moves_picture():
    """Each kind of move from one position: the L picture to the left, R to the right, F below."""
    out = ["\\begin{tikzpicture}[x=1mm, y=1mm]\n"]
    out.append(mini_lamps(0, 0, (), 0))
    yb, xo = -25.0, 21.0
    out.append(mini_lamps(-xo, yb, (), -1))
    out.append(mini_lamps(0, yb, (0,), 0))
    out.append(mini_lamps(xo, yb, (), 1))
    out.append(label_arrow((-6.0, -4.2), (-15.5, -14.8), "L", side=-1))
    out.append(label_arrow((6.0, -4.2), (15.5, -14.8), "R", side=1))
    out.append(label_arrow((0, -4.6), (0, -14.2), "F", side=1, off=3.0))
    out.append("\\end{tikzpicture}")
    return "".join(out)


def one_more(top, nbrs):
    """Top picture on the left, the three pictures one move later on the right."""
    out = ["\\begin{tikzpicture}[x=1mm, y=1mm]\n"]
    cxl, cxr = -(FRAME_W / 2 + 10), FRAME_W / 2 + 10
    out.append(target(cxl, 0, top)[0])
    ys = (54.0, 0.0, -54.0)
    for (m, t), y in zip(nbrs, ys):
        out.append(target(cxr, y, t)[0])
        a = (cxl + FRAME_W / 2 + 1.5, y * 0.12)
        b = (cxr - FRAME_W / 2 - 1.5, y)
        side = 1 if y >= 0 else -1      # above-left of the upper arrows, below-left of the lower one
        out.append(label_arrow(a, b, m, side=side, off=4.2, head="2.6mm", lw="0.8pt", font="\\sffamily\\bfseries"))
    out.append("\\end{tikzpicture}")
    return "".join(out)


def mark_square(x, y, s, mark=None):
    """A square with lower-left corner (x, y), side s; mark is None, 'flip', 'R' or 'L'."""
    out = [f"\\draw[line width=0.5pt, black!70] ({x:.2f},{y:.2f}) rectangle ({x + s:.2f},{y + s:.2f});\n"]
    cx, cy = x + s / 2, y + s / 2
    if mark == "flip":
        out.append(f"\\fill ({cx:.2f},{cy:.2f}) circle (1.5);\n")
    elif mark in ("R", "L"):
        d = 1 if mark == "R" else -1
        out.append(f"\\draw[-{{Stealth[length=1.9mm]}}, line width=0.9pt] ({cx - d * 3.0:.2f},{cy:.2f}) -- ({cx + d * 3.2:.2f},{cy:.2f});\n")
    return "".join(out)


def marks_example():
    """Non-task example of the Problem 5 record: flip, then step right."""
    out = ["\\begin{tikzpicture}[x=1mm, y=1mm]\n"]
    s = ROW_SQ
    out.append(mini_lamps(0, 0, (), 0))
    out.append(mark_square(13.0, -s / 2 + 1.5, s, "flip"))
    out.append(mini_lamps(13.0 + s + 13.0, 0, (0,), 0))
    out.append(mark_square(13.0 + s + 26.0, -s / 2 + 1.5, s, "R"))
    out.append(mini_lamps(13.0 + 2 * s + 39.0, 0, (0,), 1))
    out.append("\\end{tikzpicture}")
    return "".join(out)


def ways_rows(targets):
    """Each picture on the left with rows of empty squares on the right for its ways."""
    out = ["\\begin{tikzpicture}[x=1mm, y=1mm]\n"]
    cx = -(ROW_N * ROW_SQ + 6) / 2 - 2
    xr = cx + FRAME_W / 2 + 6
    block = ROW_LINES * ROW_SQ + (ROW_LINES - 1) * ROW_GAP
    ytop = 0.0
    for t in targets:
        tz, (x0, y0, x1, y1) = target(cx, 0, t, squares=False)
        h = y1 - y0
        cy = ytop - (block - h) / 2 - (y1 - 0)      # centre the frame on its block of rows
        tz, _ = target(cx, cy, t, squares=False)
        out.append(tz)
        for j in range(ROW_LINES):
            yrow = ytop - j * (ROW_SQ + ROW_GAP) - ROW_SQ
            for k in range(ROW_N):
                out.append(mark_square(xr + k * ROW_SQ, yrow, ROW_SQ))
        ytop -= block + 13.0
    out.append("\\end{tikzpicture}")
    return "".join(out)


def tower(x, ybase, n, num=True):
    c = 5.0
    out = []
    for k in range(n):
        out.append(f"\\draw[line width=0.5pt, fill=black!22] ({x - c / 2:.2f},{ybase + k * c:.2f}) rectangle ({x + c / 2:.2f},{ybase + (k + 1) * c:.2f});\n")
    if num:
        out.append(f"\\node[font=\\sffamily\\small, anchor=north] at ({x:.2f},{ybase - 1.2:.2f}) {{{n}}};\n")
    return "".join(out)


def tower_rows(rows):
    out = ["\\begin{tikzpicture}[x=1mm, y=1mm]\n"]
    cx = -50.0
    gap = 12.0
    prev_bottom = None
    for t, towers in rows:
        _, (x0, y0, x1, y1) = target(cx, 0, t, squares=False)
        above, below = y1, -y0          # frame extent above / below the lamp line
        rise = max(above, 5.5 + 5.0 * max(towers) - below)
        y = 0.0 if prev_bottom is None else prev_bottom - gap - rise
        tz, (x0, y0, x1, y1) = target(cx, y, t, squares=False)
        out.append(tz)
        for j, n in enumerate(towers):
            out.append(tower(6 + j * 22.0, y0 + 5.5, n))
        prev_bottom = y0
    out.append("\\end{tikzpicture}")
    return "".join(out)


# ---------------------------------------------------------------- text
RULES = (
    "Start every try with all lamps off and the walker at home. "
    "A move is one step left, one step right, or a flip of the lamp under the walker. "
    "One partner moves the walker. The other points to the lamp under the walker, then flips it. "
    "Swap jobs for each new picture. "
    "Put one cube on your tower for each move. "
    "Color one square under the picture for each cube in your shortest tower."
)

FEWEST = "Build each picture with as few moves as you can."
FROM_OFF = "Build each picture, starting with all lamps off, with as few moves as you can."

PAGES = []

PAGES.append(
    "\\noindent\\begin{minipage}[t]{0.62\\textwidth}\\vspace{0pt}\n" + RULES + "\n\\end{minipage}\\hfill"
    "\\begin{minipage}[t]{0.345\\textwidth}\\vspace{1mm}\\centering\n" + moves_picture() + "\n\\end{minipage}\n\n"
    "\\vspace{6mm}\\noindent\\textbf{Problem 1:} " + FEWEST + "\n\n\\vspace{5mm}\\centerline{" + grid4(P1) + "}\n"
)
PAGES.append("\\noindent\\textbf{Problem 2:} " + FEWEST + "\n\n\\vspace{5mm}\\centerline{" + grid4(P2) + "}\n")
PAGES.append("\\noindent\\textbf{Problem 3:} " + FEWEST + "\n\n\\vspace{5mm}\\centerline{" + grid4(P3) + "}\n")
PAGES.append("\\noindent\\textbf{Problem 4:} " + FEWEST + "\n\n\\vspace{5mm}\\centerline{" + grid4(P4) + "}\n")
PAGES.append(
    "\\noindent\\textbf{Problem 5:} Find every way to build each picture with the fewest moves. "
    "Draw each way in a row of squares, with a dot for each flip and an arrow for each step. "
    "Explain why there is no quicker way.\n\n"
    "\\vspace{4mm}\\centerline{" + marks_example() + "}\n\n"
    "\\vspace{7mm}\\centerline{" + ways_rows(P5) + "}\n"
)
PAGES.append(
    "\\noindent\\textbf{Problem 6:} " + FROM_OFF + " Which one needs the most moves?\n\n"
    "\\vspace{5mm}\\centerline{" + one_more(P6_TOP, P6) + "}\n"
)
PAGES.append(
    "\\noindent\\textbf{Problem 7:} " + FROM_OFF + " Which one needs the most moves?\n\n"
    "\\vspace{5mm}\\centerline{" + one_more(P7_TOP, P7) + "}\n"
)
PAGES.append(
    "\\noindent\\textbf{Problem 8:} For each tower, try to build the picture in its row with exactly that many moves. "
    "Circle every tower that works.\n\n\\vspace{6mm}\\centerline{" + tower_rows(P8) + "}\n"
)

PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage[letterpaper, margin=0.7in, headheight=15pt, headsep=14pt, footskip=26pt, includeheadfoot=false]{geometry}
\usepackage[T1]{fontenc}
\usepackage{tgheros}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{Week 66 / Lamplighter streets / K--1}
\fancyfoot[L]{Bellingham Math Circle / Week 66 / GGT66-K-v1}
\fancyfoot[R]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\setlength{\parindent}{0pt}
\linespread{1.12}
\begin{document}
"""


def main():
    body = []
    for k, page in enumerate(PAGES):
        body.append(page + "\n\\vfill\n\\centerline{" + street() + "}\n\\vspace*{2mm}\n")
        body.append("\\newpage\n" if k < len(PAGES) - 1 else "")
    with open("k-1.tex", "w") as f:
        f.write(PREAMBLE + "".join(body) + "\\end{document}\n")


if __name__ == "__main__":
    main()
