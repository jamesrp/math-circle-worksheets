#!/usr/bin/env python3
"""Generate the Week 9 (Bouncing paths) student pages as LaTeX/TikZ and compile them.

All diagram sizes are in inches so that the printed squares are exactly
3/4 inch (K-1) or 1/2 inch (grades 2-3 and 4-5) at 100% scale on US Letter.
"""
import os
import subprocess
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFT = os.path.dirname(HERE)

GRID = r"black!45"        # thin grid lines
GRIDW = "0.6pt"
WALLW = "2.2pt"           # table walls


# ---------------------------------------------------------------- simulation
def ball_path(w, h, max_steps=None):
    """Grid points visited by the ball on a w x h table, from (0,0) to the stopping corner."""
    x = y = 0
    dx = dy = 1
    pts = [(0, 0)]
    bounces = 0
    while True:
        x += dx
        y += dy
        pts.append((x, y))
        if max_steps is not None and len(pts) > max_steps:
            return pts, None, None
        hx, hy = x in (0, w), y in (0, h)
        if hx and hy:
            break
        if hx:
            dx = -dx
            bounces += 1
        if hy:
            dy = -dy
            bounces += 1
    corner = ("top" if y == h else "bottom") + " " + ("right" if x == w else "left")
    return pts, corner, bounces


def rule(w, h):
    L = w * h // gcd(w, h)
    a, b = L // w, L // h
    return ("top" if b % 2 else "bottom") + " " + ("right" if a % 2 else "left"), a + b - 2


# ---------------------------------------------------------------- tikz items
class Item:
    """A drawable placed in a row. width/height in inches; drawn with lower-left at (x0, y0)."""

    def __init__(self, width, height, draw, below=0.0, above=0.0):
        self.width = width
        self.height = height
        self.draw = draw
        self.below = below   # extra space used under y0 (labels, boxes)
        self.above = above


def f(v):
    return f"{v:.4f}".rstrip("0").rstrip(".") if isinstance(v, float) else str(v)


def grid_code(x0, y0, w, h, u):
    """Thin grid lines drawn one by one, so they are exactly aligned with (x0, y0)."""
    s = ""
    for i in range(w + 1):
        x = x0 + i * u
        s += f"\\draw[{GRID}, line width={GRIDW}] ({f(x)},{f(y0)}) -- ({f(x)},{f(y0 + h * u)});\n"
    for j in range(h + 1):
        y = y0 + j * u
        s += f"\\draw[{GRID}, line width={GRIDW}] ({f(x0)},{f(y)}) -- ({f(x0 + w * u)},{f(y)});\n"
    return s


def dot_code(x, y, r):
    return f"\\fill ({f(x)},{f(y)}) circle ({f(r)});\n"


def table(w, h, u, label=None, dot="bl", box=None, path_steps=None, arrow=False,
          labelsize=r"\normalsize", dotr=None, walls=True):
    """A w x h table of u-inch squares with the start dot.

    box: side (in) of an empty answer box drawn under the table.
    path_steps: draw the first path_steps steps of the ball's path (used only for the rule picture).
    """
    dotr = dotr if dotr is not None else (0.10 if u >= 0.7 else 0.075)
    below = 0.0
    if label:
        below = 0.42
    if box:
        below = max(below, box + 0.25)

    def draw(x0, y0):
        s = grid_code(x0, y0, w, h, u)
        if walls:
            s += (f"\\draw[line width={WALLW}] ({f(x0)},{f(y0)}) rectangle "
                  f"({f(x0 + w * u)},{f(y0 + h * u)});\n")
        if path_steps:
            pts, _, _ = ball_path(w, h, max_steps=path_steps)
            pts = pts[:path_steps + 1]
            coords = " -- ".join(f"({f(x0 + px * u)},{f(y0 + py * u)})" for px, py in pts)
            style = "line width=1.6pt, -{Stealth[length=9pt,width=8pt]}" if arrow else "line width=1.6pt"
            s += f"\\draw[{style}] {coords};\n"
        if dot:
            cx = x0 if dot[1] == "l" else x0 + w * u
            cy = y0 if dot[0] == "b" else y0 + h * u
            s += dot_code(cx, cy, dotr)
        if label:
            s += (f"\\node[anchor=north, inner sep=0pt] at ({f(x0 + w * u / 2)},{f(y0 - 0.14)}) "
                  f"{{{labelsize} {label}}};\n")
        if box:
            bx = x0 + w * u / 2 - box / 2
            s += (f"\\draw[line width=1pt] ({f(bx)},{f(y0 - 0.25 - box)}) rectangle "
                  f"({f(bx + box)},{f(y0 - 0.25)});\n")
        return s

    return Item(w * u, h * u, draw, below=below)


def blank_grid(w, h, u, dot=True, label=None, icon=None, labelsize=r"\normalsize"):
    """Thin grid with the start dot at its lower-left point (children draw the table)."""
    dotr = 0.10 if u >= 0.7 else 0.075
    below = 0.5 if label else 0.0
    above = 0.8 if icon else 0.0

    def draw(x0, y0):
        s = grid_code(x0, y0, w, h, u)
        if dot:
            s += dot_code(x0, y0, dotr)
        if label:
            s += (f"\\node[anchor=north, inner sep=0pt, align=center] at "
                  f"({f(x0 + w * u / 2)},{f(y0 - 0.14)}) {{{labelsize} {label}}};\n")
        if icon:
            s += icon_code(x0 + w * u / 2 - 0.25, y0 + h * u + 0.17, icon, side=0.5)
        return s

    return Item(w * u, h * u, draw, below=below, above=above)


def icon_code(x0, y0, target, side=0.6):
    """Small square picture: dot at lower left, ring at the target corner."""
    s = f"\\draw[line width=1.4pt] ({f(x0)},{f(y0)}) rectangle ({f(x0 + side)},{f(y0 + side)});\n"
    s += dot_code(x0, y0, 0.06)
    tx = x0 if target[1] == "l" else x0 + side
    ty = y0 if target[0] == "b" else y0 + side
    s += f"\\draw[line width=1.5pt] ({f(tx)},{f(ty)}) circle (0.13);\n"
    return s


def icon_item(target, side=0.6):
    def draw(x0, y0):
        return icon_code(x0, y0 + 0.13, target, side)
    return Item(side, side + 0.26, draw)


def icon_mid(target, H, side=0.6):
    """The small target picture, centred vertically in a slot of height H (placed beside a grid)."""
    def draw(x0, y0):
        return icon_code(x0, y0 + H / 2 - side / 2, target, side)
    return Item(side, H, draw)


def sheet(cols, rows, w, h, u, label=None, dashed=False, labelsize=r"\normalsize"):
    """cols x rows copies of a w x h table: a (cols*w) x (rows*h) grid with the copy walls.

    dashed=True draws the inner copy walls as dashed fold lines (K-1); otherwise thick lines.
    """
    W, H = cols * w, rows * h
    below = 0.45 if label else 0.0

    def draw(x0, y0):
        s = grid_code(x0, y0, W, H, u)
        inner = (f"line width=1.6pt, dash pattern=on 7pt off 5pt" if dashed
                 else f"line width={WALLW}")
        for i in range(1, cols):
            x = x0 + i * w * u
            s += f"\\draw[{inner}] ({f(x)},{f(y0)}) -- ({f(x)},{f(y0 + H * u)});\n"
        for j in range(1, rows):
            y = y0 + j * h * u
            s += f"\\draw[{inner}] ({f(x0)},{f(y)}) -- ({f(x0 + W * u)},{f(y)});\n"
        s += (f"\\draw[line width={WALLW}] ({f(x0)},{f(y0)}) rectangle "
              f"({f(x0 + W * u)},{f(y0 + H * u)});\n")
        s += dot_code(x0, y0, 0.10 if u >= 0.7 else 0.075)
        if label:
            s += (f"\\node[anchor=north, inner sep=0pt] at ({f(x0 + W * u / 2)},{f(y0 - 0.14)}) "
                  f"{{{labelsize} {label}}};\n")
        return s

    return Item(W * u, H * u, draw, below=below)


def chart(n=6, cell=0.7):
    """Recording chart for every table from 1 by 1 to n by n: columns = width, rows = height."""
    def draw(x0, y0):
        s = ""
        for i in range(n + 1):
            s += f"\\draw[line width=0.9pt] ({f(x0 + i * cell)},{f(y0)}) -- ({f(x0 + i * cell)},{f(y0 + n * cell)});\n"
            s += f"\\draw[line width=0.9pt] ({f(x0)},{f(y0 + i * cell)}) -- ({f(x0 + n * cell)},{f(y0 + i * cell)});\n"
        for i in range(n):
            s += f"\\node[anchor=base] at ({f(x0 + (i + 0.5) * cell)},{f(y0 - 0.28)}) {{{i + 1}}};\n"
            s += f"\\node at ({f(x0 - 0.22)},{f(y0 + (i + 0.5) * cell)}) {{{i + 1}}};\n"
        s += f"\\node[anchor=base] at ({f(x0 + n * cell / 2)},{f(y0 - 0.62)}) {{width}};\n"
        s += f"\\node[rotate=90] at ({f(x0 - 0.58)},{f(y0 + n * cell / 2)}) {{height}};\n"
        return s
    return Item(n * cell, n * cell, draw, below=0.75)


def gap_list(gap, n):
    """gap may be one number (used between every pair of items) or a list of n - 1 gaps."""
    return list(gap) if isinstance(gap, (list, tuple)) else [gap] * max(n - 1, 0)


def row(items, gap=0.45, align="bottom", xshift=0.0):
    """One tikzpicture with the items side by side, centred on the line."""
    gaps = gap_list(gap, len(items))
    total = sum(it.width for it in items) + sum(gaps)
    maxh = max(it.height for it in items)
    s = "\\begin{center}\n\\begin{tikzpicture}[x=1in, y=1in]\n"
    x = xshift
    for i, it in enumerate(items):
        y0 = 0.0 if align == "bottom" else maxh - it.height
        s += it.draw(x, y0)
        x += it.width + (gaps[i] if i < len(gaps) else 0.0)
    # make the bounding box include the space used by labels/boxes and icons
    below = max(it.below for it in items)
    above = max(it.above for it in items)
    s += f"\\path (0,{f(-below)}) rectangle ({f(total)},{f(maxh + above)});\n"
    s += "\\end{tikzpicture}\n\\end{center}\n"
    return s


def stack(rows, row_gap=0.3, gaps=None):
    """Several rows of items in one tikzpicture, each row centred; rows listed top to bottom."""
    gaps = gaps or [0.8] * len(rows)
    gaps = [gap_list(g, len(r)) for r, g in zip(rows, gaps)]
    widths = [sum(it.width for it in r) + sum(g) for r, g in zip(rows, gaps)]
    total = max(widths)
    s = "\\begin{center}\n\\begin{tikzpicture}[x=1in, y=1in]\n"
    y = 0.0
    for r, g, wd in zip(rows, gaps, widths):
        above = max(it.above for it in r)
        maxh = max(it.height for it in r)
        below = max(it.below for it in r)
        y -= above + maxh            # baseline (bottom of the tallest drawing) of this row
        x = (total - wd) / 2
        for i, it in enumerate(r):
            s += it.draw(x, y)
            x += it.width + (g[i] if i < len(g) else 0.0)
        y -= below + row_gap
    y += row_gap
    s += f"\\path (0,{f(y)}) rectangle ({f(total)},0);\n"
    s += "\\end{tikzpicture}\n\\end{center}\n"
    return s


# ---------------------------------------------------------------- documents
PREAMBLE = r"""\documentclass[%(size)s,letterpaper]{%(cls)s}
\usepackage[margin=0.6in, includehead, includefoot, headheight=18pt, headsep=0.22in, footskip=0.4in]{geometry}
\usepackage[T1]{fontenc}
\usepackage[scaled=0.95]{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{array}
\usepackage{enumitem}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{Week 9 / Bouncing paths / %(level)s}
\fancyfoot[L]{Bellingham Math Circle / Week 9 / %(pid)s}
\fancyfoot[R]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\raggedright
\newcommand{\prob}[1]{\textbf{Problem #1:}}
\begin{document}
"""

END = "\\end{document}\n"


def vspace(inches):
    return f"\\vspace*{{{inches}in}}\n"


def rules_block(text, picture_item, textwidth="0.52\\textwidth", picwidth="0.44\\textwidth"):
    s = ("\\noindent\\begin{minipage}[c]{%s}\\setlength{\\parskip}{5pt}\n%s\n\\end{minipage}\\hfill\n"
         % (textwidth, text))
    s += "\\begin{minipage}[c]{%s}\\centering\n" % picwidth
    s += "\\begin{tikzpicture}[x=1in, y=1in]\n" + picture_item.draw(0, 0) + "\\end{tikzpicture}\n"
    s += "\\end{minipage}\n\n"
    return s


# ------------------------------------------------------------------- K-1
def k1():
    u = 0.75
    s = PREAMBLE % dict(size="14pt", cls="extarticle", level="K--1", pid="F09-K-v4")

    rules = ("The ball rolls on a table. It starts at the dot and rolls across the squares from "
             "corner to corner. It bounces off the walls and stops when it gets to a corner of "
             "the table. Each time it hits a wall is one bounce. Stopping at the corner is not "
             "a bounce.\n\n"
             "Partners take turns. One puts a counter on the corner where they think the ball "
             "will stop, and the other moves a counter along the path and draws it with a crayon.")
    # the arrow ends inside the table, just after the bounce off the top wall
    s += rules_block(rules, table(5, 3, 0.5, path_steps=4, arrow=True))
    s += vspace(0.15)

    # Problem 1: floor grid (3 squares by 5 squares)
    s += ("\\prob{1} Take turns walking as the ball on the floor grid. Walk once from each "
          "dot, and draw each walk.\n")
    s += row([table(3, 5, u, dot="bl"), table(3, 5, u, dot="br")], gap=1.2)
    s += "\\newpage\n"

    # Problem 2: where does it stop
    s += "\\prob{2} Where does the ball stop on each table? Draw its path.\n"
    s += vspace(0.2)
    s += row([table(2, 2, u), table(1, 3, u), table(2, 1, u)], gap=0.9)
    s += vspace(0.35)
    s += row([table(2, 3, u), table(3, 3, u), table(3, 2, u)], gap=0.5)
    s += "\\newpage\n"

    # Problem 3: count the bounces
    s += ("\\prob{3} How many times does the ball bounce on each table? "
          "Write the number in the box.\n")
    s += vspace(0.2)
    s += row([table(1, 4, u, box=0.65), table(1, 5, u, box=0.65),
              table(2, 5, u, box=0.65), table(3, 4, u, box=0.65)], gap=0.55)
    s += "\\newpage\n"

    # Problem 4: same shape, bigger (two families: 1x2 2x4 3x6 and 2x3 4x6)
    s += ("\\prob{4} Draw the path on each table. Write the number of bounces in the box.\n")
    s += vspace(0.2)
    s += row([table(1, 2, u, box=0.65), table(2, 4, u, box=0.65), table(3, 6, u, box=0.65)], gap=0.8)
    s += "\\newpage\n"
    s += vspace(0.3)
    s += row([table(2, 3, u, box=0.65), table(4, 6, u, box=0.65)], gap=1.2)
    s += "\\newpage\n"

    # Problem 5: make the ball stop at a chosen corner (two 3x3 grids per target)
    s += ("\\prob{5} For each little picture, draw a table starting at the dot so that the "
          "ball stops at the corner with the circle.\n")
    gh = 3 * u
    s += stack([[icon_mid(t, gh), blank_grid(3, 3, u), blank_grid(3, 3, u)]
                for t in ("tl", "br", "tr")],
               row_gap=0.42, gaps=[[0.6, 0.7]] * 3)
    s += "\\newpage\n"

    # Problem 6: back to the dot
    s += ("\\prob{6} Can you draw a table where the ball comes back to the dot and stops there?\n")
    s += row([icon_item("bl")])
    s += row([blank_grid(4, 4, u), blank_grid(4, 4, u)], gap=0.8)
    s += vspace(0.15)
    s += row([blank_grid(4, 4, u), blank_grid(4, 4, u)], gap=0.8)
    s += "\\newpage\n"

    # Problem 7: fold a straight line; each big square sits beside the table it folds onto
    s += ("\\prob{7} With a ruler, draw a straight line from the dot to the far corner of each "
          "big square. Cut out the square and fold it on the dashed lines, with the dot on top. "
          "Hold it up to the light, and draw the line you see on the small table next to it.\n")
    s += vspace(0.2)
    s += row([sheet(2, 1, 1, 2, u, dashed=True), table(1, 2, u),
              sheet(3, 1, 1, 3, u, dashed=True), table(1, 3, u)], gap=[0.35, 1.2, 0.35])
    s += vspace(0.45)
    s += row([sheet(2, 1, 2, 4, u, dashed=True), table(2, 4, u)], gap=0.5)
    s += END
    return s


# ------------------------------------------------------------------- 2-3
RULES_OLDER = ("The ball starts at the dot in the bottom left corner of a table and rolls up and "
               "to the right, crossing each square from corner to corner. It bounces off every wall "
               "it hits and stops when it reaches a corner of the table. Each time the ball hits "
               "a wall counts as one bounce; reaching the corner at the end does not count. "
               "A 7 by 3 table is 7 squares wide and 3 squares high.")


def rule_picture():
    """The 7 by 3 table of the rules text, labelled, with the first 5 steps (arrow ends inside)."""
    return table(7, 3, 0.4, path_steps=5, arrow=True, dotr=0.065, label="7 by 3")


def lab(w, h):
    return f"{w} by {h}"


def tables_with(corner, bounces, W, H):
    """Every w x h table with w <= W and h <= H whose ball stops at corner after bounces."""
    return [(w, h) for w in range(1, W + 1) for h in range(1, H + 1)
            if rule(w, h) == (corner, bounces)]


# Grades 2-3, Problem 4 targets on 6 x 6 grids, with the tables that meet them.
M23_TARGETS = [("bottom right", 1), ("top right", 4), ("top left", 7), ("top right", 3)]
M23_EXPECT = {("bottom right", 1): [(2, 1), (4, 2), (6, 3)],
              ("top right", 4): [(1, 5), (5, 1)],
              ("top left", 7): [(5, 4)],
              ("top right", 3): []}
M23_LABEL = {t: f"stops at the {t[0]}\\\\after {t[1]} bounce{'s' if t[1] != 1 else ''}"
             for t in M23_TARGETS}

# Grades 4-5, Problem 6 targets on the 14 x 12 grid (the last one is impossible).
U45_TARGETS = [("top left", 13), ("top right", 8), ("bottom right", 11), ("bottom right", 10)]


def m23():
    u = 0.5
    s = PREAMBLE % dict(size="12pt", cls="article", level="Grades 2--3", pid="F09-M-v4")
    rules = RULES_OLDER + ("\n\nPartners take turns: one predicts where the ball will stop, "
                           "and the other traces the path.")
    s += rules_block(rules, rule_picture(),
                     textwidth="0.56\\textwidth", picwidth="0.4\\textwidth")
    s += vspace(0.05)

    s += ("\\prob{1} Trace the path on each table. Under each table, write the corner where the "
          "ball stops and the number of bounces.\n")
    sizes1 = [(2, 3), (3, 2), (1, 4)]
    sizes2 = [(3, 4), (4, 3), (3, 5)]
    s += row([table(w, h, u, label=lab(w, h)) for w, h in sizes1], gap=1.1)
    s += vspace(0.45)
    s += row([table(w, h, u, label=lab(w, h)) for w, h in sizes2], gap=1.1)
    s += "\\newpage\n"

    s += ("\\prob{2} Trace the path on each table, and write the corner where the ball stops and "
          "the number of bounces.\n")
    s += vspace(0.1)
    s += row([table(w, h, u, label=lab(w, h)) for w, h in [(1, 2), (2, 4), (3, 6)]], gap=1.2)
    s += vspace(0.5)
    s += row([table(w, h, u, label=lab(w, h)) for w, h in [(1, 3), (2, 6), (4, 6)]], gap=1.2)
    s += "\\newpage\n"

    s += ("\\prob{3} Before you trace these two tables, write the corner where you think the ball "
          "will stop and the number of bounces you expect. Then trace the paths to check.\n")
    s += vspace(0.1)
    s += row([table(5, 10, u, label=lab(5, 10)), table(8, 12, u, label=lab(8, 12))], gap=0.6)
    s += "\\newpage\n"

    # Problem 4: none of these outcomes appears on pages 1-3; the last one is impossible
    # (a top right stop always takes an even number of bounces). See M23_TARGETS.
    s += ("\\prob{4} On each grid, draw a table with its bottom left corner at the dot, so that the "
          "ball does what is written under the grid. If there is no such table, explain why.\n")
    s += vspace(0.1)
    labels = [M23_LABEL[t] for t in M23_TARGETS]
    s += row([blank_grid(6, 6, u, label=labels[0]), blank_grid(6, 6, u, label=labels[1])], gap=0.9)
    s += vspace(0.35)
    s += row([blank_grid(6, 6, u, label=labels[2]), blank_grid(6, 6, u, label=labels[3])], gap=0.9)
    s += "\\newpage\n"

    s += ("\\prob{5} Play this game with your partner. One player draws a table on the grid, no "
          "more than 6 squares wide and 6 squares high, and marks its dot. The other player says "
          "where the ball will stop and how many times it will bounce, and then traces the path. "
          "The player who predicted scores 1 point for the right corner and 1 point for the right "
          "number of bounces. Then swap jobs. After each player has predicted three tables, the "
          "player with more points wins.\n")
    s += vspace(0.05)
    s += row([blank_grid(14, 15, u, dot=False)])
    s += "\\newpage\n"

    s += ("\\prob{6} Find every table no more than 6 squares wide and no more than 6 squares "
          "high where the ball bounces exactly once. Explain how you know you have found them "
          "all.\n")
    s += vspace(0.05)
    s += row([blank_grid(14, 10, u, dot=False)])
    s += "\\newpage\n"

    # Problem 7: 2x3 sheet (3 crossings, bottom right; cut down to 4 panels) and
    # 1x3 sheet (2 crossings, top right; 3 panels). At most 4 layers when folded.
    s += ("\\prob{7} With a ruler and a dark marker, draw a straight line from the dot to the "
          "opposite corner of each sheet. How many thick lines inside the sheet does each line "
          "cross? Then cut out the tables each line passes through, keeping them in one piece. "
          "Fold them on the thick lines until they are the size of one table with the dot in "
          "front. Hold them up to the light, and copy the path you see onto the small table "
          "beside the sheet.\n")
    s += vspace(0.1)
    s += row([sheet(3, 2, 2, 3, u), table(2, 3, u, label=lab(2, 3))], gap=0.8)
    s += vspace(0.3)
    s += row([sheet(3, 1, 1, 3, u), table(1, 3, u, label=lab(1, 3))], gap=0.8)
    s += "\\newpage\n"

    s += ("\\prob{8} Is there a table where the ball stops at the corner it started from? "
          "Find one, or explain why there is none.\n")
    s += vspace(0.05)
    s += row([blank_grid(14, 10, u, dot=False)])
    s += END
    return s


# ------------------------------------------------------------------- 4-5
def u45():
    u = 0.5
    s = PREAMBLE % dict(size="12pt", cls="article", level="Grades 4--5", pid="F09-U-v4")
    rules = RULES_OLDER + ("\n\nBefore one of you traces a path, the others predict where the "
                           "ball will stop. Then they check the tracing.")
    s += rules_block(rules, rule_picture(),
                     textwidth="0.56\\textwidth", picwidth="0.4\\textwidth")
    s += vspace(0.05)

    s += ("\\prob{1} Trace the path on each table. Under each table, write the corner where the "
          "ball stops and the number of bounces.\n")
    s += row([table(w, h, u, label=lab(w, h)) for w, h in [(2, 3), (3, 2), (1, 4), (3, 4)]], gap=0.75)
    s += vspace(0.2)
    s += row([table(w, h, u, label=lab(w, h)) for w, h in [(6, 4), (3, 5)]], gap=1.5)
    s += "\\newpage\n"

    # Problem 2: the chart on its own page, then a full page of grid for tracing
    s += ("\\prob{2} Find where the ball stops and how many times it bounces on every table from "
          "1 by 1 to 6 by 6. Record each table in the chart: put a dot in the corner of its box "
          "where the ball stops, and write the number of bounces inside the box.\n")
    s += vspace(0.2)
    s += row([chart(6, 0.85)])
    s += "\\newpage\n"
    s += row([blank_grid(14, 16, u, dot=False)])
    s += "\\newpage\n"

    # Problem 3: unfolding the 2 by 3 table. The 8 x 9 sheet (4 x 3 copies) is bigger than
    # needed; the line first meets a crossing of thick lines at (6,6) after crossing 3 of them.
    # Cutting out the tables it passes through leaves 4 panels, so the fold has 4 layers.
    s += ("\\prob{3} With a ruler and a dark marker, draw a straight line on the big sheet from the "
          "dot, crossing each square from corner to corner. Stop when the line first reaches "
          "another point where two thick lines cross. How many thick lines did it cross before it "
          "reached that point? Then cut out the tables the line passes through, keeping them in "
          "one piece. Fold them on the thick lines until they are the size of the 2 by 3 table "
          "with the dot in front. Hold them up to the light, and copy the path you see onto the "
          "small 2 by 3 table.\n")
    s += vspace(0.15)
    s += row([sheet(4, 3, 2, 3, u), table(2, 3, u, label=lab(2, 3))], gap=1.0)
    s += "\\newpage\n"

    # Problem 4: the child makes the sheet for the 4 by 3 table (3 copies across, 4 up, 5 crossings)
    s += ("\\prob{4} On this grid, draw thick lines to make a sheet for the 4 by 3 table, the way "
          "the sheet in Problem 3 is made for the 2 by 3 table. Draw the straight line from the dot "
          "until it first reaches another point where two thick lines cross. How many tables "
          "across and how many tables up does the line travel? Where does the ball stop on the "
          "4 by 3 table, and how many times does it bounce?\n")
    s += vspace(0.05)
    s += row([blank_grid(13, 13, u)])
    s += "\\newpage\n"

    s += ("\\prob{5} Without tracing, find where the ball stops and how many times it bounces on "
          "each of these tables. Then trace the 6 by 10 table to check.\n")
    s += vspace(0.15)
    rec = ("{\\renewcommand{\\arraystretch}{2.7}"
           "\\begin{tabular}{|>{\\centering\\arraybackslash}m{0.9in}|>{\\centering\\arraybackslash}m{1.25in}"
           "|>{\\centering\\arraybackslash}m{0.85in}|}\\hline\n"
           "table & corner & bounces \\\\\\hline\n")
    for w, h in [(6, 10), (8, 12), (12, 9), (7, 5), (5, 8), (20, 30)]:
        rec += f"{w} by {h} & & \\\\\\hline\n"
    rec += "\\end{tabular}}"
    t = table(6, 10, u, label=lab(6, 10))
    s += ("\\par\\noindent\\begin{minipage}[t]{0.5\\textwidth}\\vspace{0pt}\n" + rec +
          "\n\\end{minipage}\\hfill\\begin{minipage}[t]{0.45\\textwidth}\\vspace{0pt}\\centering\n"
          "\\begin{tikzpicture}[x=1in,y=1in]\n" + t.draw(0, 0) +
          f"\\path (0,{-t.below}) rectangle ({t.width},{t.height});\n"
          "\\end{tikzpicture}\n\\end{minipage}\n\n")
    s += "\\newpage\n"

    # Problem 6: none of these outcomes appears on pages 1-5; bottom right after 10 is impossible.
    items = "".join(f"\\item The ball stops at the {c} corner after {b} bounces.\n"
                    for c, b in U45_TARGETS)
    s += ("\\prob{6} Find a table for each of these, or explain why there is none.\n"
          "\\begin{itemize}[itemsep=1pt, topsep=2pt]\n" + items + "\\end{itemize}\n")
    s += row([blank_grid(14, 12, u, dot=False)])
    s += "\\newpage\n"

    s += "\\prob{7} Explain why the ball never stops at the corner where it started.\n"
    s += "\\vspace*{3.9in}\n\n"
    s += ("\\prob{8} Write a rule that tells where the ball stops and how many times it bounces on "
          "any table, without tracing. Explain why your rule works.\n")
    s += END
    return s


# ------------------------------------------------------------------- build
def build(name, tex):
    path = os.path.join(HERE, name + ".tex")
    with open(path, "w") as fh:
        fh.write(tex)
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                           cwd=HERE, capture_output=True, text=True)
        if r.returncode:
            print(r.stdout[-3000:])
            raise SystemExit(f"LaTeX failed for {name}")
    log = open(os.path.join(HERE, name + ".log")).read()
    for key in ("Overfull", "Underfull \\vbox", "Float too large", "headheight is too small"):
        if key in log:
            print(f"{name}: {key} found in log")
    os.replace(os.path.join(HERE, name + ".pdf"), os.path.join(DRAFT, name + ".pdf"))


def unfold(cols, rows, w, h):
    """Walk the straight line on a sheet of cols x rows copies of a w x h table.

    Returns (end point, thick lines crossed before it, panels the line passes through).
    The end point is the first point after the start where two copy walls meet."""
    x = y = 0
    panels = set()
    while True:
        panels.add((x // w, y // h))      # the square from (x,y) to (x+1,y+1) lies in this panel
        x += 1
        y += 1
        if x % w == 0 and y % h == 0:
            break
    assert x <= cols * w and y <= rows * h, "sheet too small"
    crossed = (x // w - 1) + (y // h - 1)
    return (x, y), crossed, len(panels)


if __name__ == "__main__":
    # sanity: simulation agrees with the lcm rule for every table used or asked about
    for w in range(1, 61):
        for h in range(1, 61):
            _, c, b = ball_path(w, h)
            assert (c, b) == rule(w, h), (w, h)
            assert c != "bottom left"
    # unfolding sheets: crossings equal bounces; folded layers stay small
    for cols, rows, w, h, layers in [(2, 1, 1, 2, 2), (3, 1, 1, 3, 3), (2, 1, 2, 4, 2),  # K-1
                                     (3, 2, 2, 3, 4), (3, 1, 1, 3, 3),                    # 2-3
                                     (4, 3, 2, 3, 4), (3, 4, 4, 3, 6)]:                   # 4-5
        end, crossed, n = unfold(cols, rows, w, h)
        assert crossed == rule(w, h)[1] and n == layers, (cols, rows, w, h, end, crossed, n)
    # K-1 Problem 5: each target can be made on a 3 x 3 grid
    for t in ("top left", "bottom right", "top right"):
        assert any(rule(w, h)[0] == t for w in range(1, 4) for h in range(1, 4))
    # Grades 2-3 Problem 4 targets on 6 x 6 grids
    for t in M23_TARGETS:
        assert tables_with(t[0], t[1], 6, 6) == M23_EXPECT[t], (t, tables_with(t[0], t[1], 6, 6))
    # Grades 4-5 Problem 6: first three fit the 14 x 12 grid; the last has no table at all
    for c, b in U45_TARGETS[:3]:
        assert tables_with(c, b, 14, 12), (c, b)
    assert not tables_with("bottom right", 10, 60, 60)
    build("k-1", k1())
    build("grades-2-3", m23())
    build("grades-4-5", u45())
    print("built")
