"""Figures for the Week 9 problem files (Bouncing paths).

A problem file's `## figure` section is a Python expression evaluated here; it
returns the LaTeX for that problem's figures. The drawing code is the old student
builder's (src/gen.py, archived in archive-before-problem-files-2026-10-23/), carried
over unchanged: the ball simulation, tables, blank grids, sheets, the 4-5 chart, and
the row and stack layouts. All sizes are in inches, so that the printed squares are
exactly 3/4 inch (K-1) or 1/2 inch (grades 2-3 and 4-5) at 100% on US Letter.

`record_beside` wraps the 4-5 Problem 5 layout gen.py wrote inline, so that a figure
section stays one expression. src/check.py runs gen.py's sanity checks (the
simulation against the lcm rule, the unfolding sheets, and the targets of K-1
Problem 5, 2-3 Problem 4 and 4-5 Problem 6).
"""
from math import gcd

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



# ---------------------------------------------------------------- page pieces
def vspace(inches):
    return f"\\vspace*{{{inches}in}}\n"


def rules_block(text, picture_item, textwidth="0.52\\textwidth", picwidth="0.44\\textwidth"):
    s = ("\\noindent\\begin{minipage}[c]{%s}\\setlength{\\parskip}{5pt}\n%s\n\\end{minipage}\\hfill\n"
         % (textwidth, text))
    s += "\\begin{minipage}[c]{%s}\\centering\n" % picwidth
    s += "\\begin{tikzpicture}[x=1in, y=1in]\n" + picture_item.draw(0, 0) + "\\end{tikzpicture}\n"
    s += "\\end{minipage}\n\n"
    return s


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


def record_beside(sizes, t):
    """4-5 Problem 5: the record table for these tables, with table t beside it (gen.py's u45)."""
    rec = ("{\\renewcommand{\\arraystretch}{2.7}"
           "\\begin{tabular}{|>{\\centering\\arraybackslash}m{0.9in}|>{\\centering\\arraybackslash}m{1.25in}"
           "|>{\\centering\\arraybackslash}m{0.85in}|}\\hline\n"
           "table & corner & bounces \\\\\\hline\n")
    for w, h in sizes:
        rec += f"{w} by {h} & & \\\\\\hline\n"
    rec += "\\end{tabular}}"
    return ("\\par\\noindent\\begin{minipage}[t]{0.5\\textwidth}\\vspace{0pt}\n" + rec +
            "\n\\end{minipage}\\hfill\\begin{minipage}[t]{0.45\\textwidth}\\vspace{0pt}\\centering\n"
            "\\begin{tikzpicture}[x=1in,y=1in]\n" + t.draw(0, 0) +
            f"\\path (0,{-t.below}) rectangle ({t.width},{t.height});\n"
            "\\end{tikzpicture}\n\\end{minipage}\n\n")
