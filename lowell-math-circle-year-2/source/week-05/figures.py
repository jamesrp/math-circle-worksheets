"""Figures for the Week 5 problem files (Tower cities).

A problem file's `## figure` section is a Python expression evaluated here; it
returns the LaTeX for that problem's figures. The drawing code is the old student
builder's (src/build.py, archived in archive-before-problem-files-2026-10-23/),
carried over unchanged: rows, charts, cards, cities and the folder scene come from
src/draw.py (as D), and pic, place, gap and inch_grids below are build.py's. The
puzzles are named here, as in build.py, and src/check.py checks each one (how many
cities fit) together with every other count the pages rely on.

The old builder kept each problem on one page in a minipage holding its statement
and figures. week.toml's prompt opens it, and `close(figure, after)`, the last thing
in a problem's first figure section, closes it as build.py's block() did.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
import draw as D  # noqa: E402
from towers import lr, solutions, clues_of, show, view, all_with_clues  # noqa: E402,F401

INCH = 2.54                          # printed grids for building: 1-inch squares

# ---------------------------------------------------------------- puzzles
# Clue keys: ('T',c) above column c, ('B',c) below column c,
# ('L',r) left of row r, ('R',r) right of row r; rows from the top,
# columns from the left.

def C(top=None, bottom=None, left=None, right=None):
    d = {}
    for side, vals in (('T', top), ('B', bottom), ('L', left), ('R', right)):
        if vals:
            for i, v in enumerate(vals):
                if v:
                    d[(side, i)] = v
    return d

# Grades 2-3, Problem 3 (three unique puzzles and one with no city)
P23 = [
    C(top=[0, 1, 3], left=[2, 0, 0], right=[0, 2, 1]),
    C(left=[2, 1, 0], right=[0, 0, 2]),
    C(top=[2, 2, 2]),                       # no city fits
    C(right=[0, 0, 2], bottom=[0, 2, 0]),
]
P23_EXPECT = [1, 1, 0, 1]
# Grades 2-3, Problem 4 (several cities)
P23_MANY = C(top=[1, 0, 0], left=[0, 0, 2])

# Grades 4-5, Problem 3: the ladder, easy to hard
E1 = C(top=[4, 0, 1, 3], left=[3, 2, 2, 1], right=[0, 0, 1, 3], bottom=[0, 2, 2, 2])
E2 = C(top=[2, 0, 0, 0], left=[3, 1, 0, 0], right=[2, 3, 0, 1], bottom=[3, 0, 4, 0])
M1 = C(top=[3, 2, 0, 0], left=[2, 0, 0, 0], right=[0, 2, 0, 1], bottom=[0, 3, 0, 0])
M2 = C(top=[0, 0, 4, 0], left=[2, 1, 0, 0], right=[0, 2, 3, 0], bottom=[2, 0, 0, 0])
H1 = C(top=[0, 3, 0, 2], left=[0, 0, 2, 0], bottom=[2, 0, 2, 0])
H2 = C(top=[2, 0, 2, 0], left=[0, 2, 0, 0], right=[0, 0, 0, 2])
LADDER = [E1, E2, M1, M2, H1, H2]
# Grades 4-5, Problem 4 (several cities)
TWO_FOURS = C(top=[4, 0, 0, 0], left=[4, 0, 0, 0])

K_ROWS_P1 = [(1, 3, 2), (3, 2, 1)]
K_EYE_ROW = (1, 3, 2)
K_CARDS3 = [(1, 3), (2, 1), (3, 3), (2, 2), (1, 1), (1, 2)]
K_CARDS4 = [(2, 3), (1, 4), (3, 3), (3, 1), (4, 2), (1, 2)]
U_CARDS4 = [(1, 2), (2, 3), (3, 3), (2, 2), (1, 4), (1, 1), (3, 2), (4, 2)]


def rows_for(n, pair):
    return [p for p in permutations(range(1, n + 1)) if lr(p) == pair]


def pic(body, center=True):
    s = "\\begin{tikzpicture}\n" + body + "\\end{tikzpicture}"
    if center:
        return "\\begin{center}\n" + s + "\n\\end{center}\n"
    return s


def place(items, cols, dx, dy):
    """items: list of tikz bodies; arranged in rows of `cols`, top to bottom."""
    s = ""
    for i, body in enumerate(items):
        r, c = divmod(i, cols)
        s += f"\\begin{{scope}}[shift={{({c*dx:.3f},{-r*dy:.3f})}}]\n{body}\\end{{scope}}\n"
    return s


def gap(cm):
    return f"\\vspace*{{{cm}cm}}\n"


def inch_grids(n, count, dy=None):
    """`count` empty n-by-n grids with 1-inch squares and clue boxes, one above the
    other and staggered left and right, so that the boxes under one grid do not
    sit beside the boxes over the next."""
    g = D.city(n, INCH, boxes=True)
    dy = dy if dy is not None else n * INCH + 2.6
    dx = 8.3 if n == 3 else 0
    s = ""
    for i in range(count):
        s += f"\\begin{{scope}}[shift={{({(i % 2) * dx:.3f},{-i * dy:.3f})}}]\n{g}\\end{{scope}}\n"
    return pic(s)


def close(figure="", after=""):
    """End a problem's minipage after its figure, as build.py's block() did."""
    return figure + after + "\\end{minipage}\n\\par\\vspace{0.75cm}\n"


def eye_row(row):
    """K-1 rule picture: a row of towers seen by an eye several cube-widths from its end."""
    body, (a, b, w) = D.side_row(row, cube=0.8, gap=0.4, circles=False,
                                 base_extra=5.6, base_extra_right=1.0)
    body += D.eye(a + 0.75, 0.32, scale=0.85)
    return pic(body)
