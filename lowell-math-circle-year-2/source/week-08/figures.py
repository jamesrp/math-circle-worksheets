"""Figures for the Week 8 problem files (Rook race and Nim).

A problem file's `## figure` section is a Python expression evaluated here; it
returns the LaTeX for that figure. The drawing code is the old student builder's
(src/build.py, archived in archive-before-problem-files-2026-10-23/), carried over
unchanged: the boards, piles and answer boxes come from src/tikzlib.py, and the
layout helpers below are build.py's. `pile_grid` and `start_rows` wrap loops
build.py wrote inline, so that a figure section stays one expression.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
from tikzlib import board, piles, choice, answer_line  # noqa: E402,F401


def centered(x):
    return "\\begin{center}\n" + x + "\n\\end{center}\n"


def grid2(cells, colw="3.35in", vsep="0.35in"):
    """Arrange cells in a 2-column grid, each centred in its column."""
    rows = []
    for i in range(0, len(cells), 2):
        pair = cells[i:i + 2]
        row = " \\hfill ".join(
            "\\begin{minipage}[t]{" + colw + "}\\centering\n" + c + "\n\\end{minipage}" for c in pair
        )
        rows.append("\\noindent " + row)
    return ("\n\n\\vspace{" + vsep + "}\n\n").join(rows) + "\n"


def stack(*items, sep="0.18in"):
    return ("\n\n\\vspace{" + sep + "}\n").join(items)


def rook_moves_picture(s=0.42):
    """The move rule: a token with arrows to the left and down."""
    return board(4, s, dots=[(2, 3)], arrows=[((2, 3), (0, 3)), ((2, 3), (2, 0))])


def queen_moves_picture(s=0.42):
    """The extended rule: left, down, or diagonally down-left."""
    return board(5, s, dots=[(3, 4)],
                 arrows=[((3, 4), (0, 4)), ((3, 4), (3, 0)), ((3, 4), (0, 1))])


def board_with_choice(n, s, dot):
    """A playing board with the 1st / 2nd boxes stacked to its right."""
    return (
        "\\begin{center}\n"
        "\\begin{minipage}[c]{" + f"{n * s + 0.05:.2f}" + "in}\n" + board(n, s, dots=[dot]) +
        "\n\\end{minipage}\\hspace{0.45in}"
        "\\begin{minipage}[c]{1.0in}\n" + choice(0.95, 0.5, 0.35, vertical=True) +
        "\n\\end{minipage}\n"
        "\\end{center}\n"
    )


def labelled_piles(p, label, r=0.1, gap=0.4, maxk=None, w="1.55in", line=1.3):
    return ("\\begin{minipage}[b]{" + w + "}\\centering\n" + piles(p, r=r, gap=gap, maxk=maxk)
            + "\n\n\\vspace{0.12in}" + label + "\n\n\\vspace{0.35in}"
            + answer_line(line) + "\n\\end{minipage}")


def pile_grid(starts, r, sep, vsep, gap=0.6):
    """Piles with 1st / 2nd boxes, two starts to a row; both starts in a row are
    drawn to the height of the row's largest pile (K-1 Problems 5 and 8)."""
    cells = []
    for i, p in enumerate(starts):
        rowmax = max(max(starts[i - i % 2]), max(starts[i - i % 2 + 1]))
        cells.append(stack(piles(p, r=r, gap=gap, maxk=rowmax),
                           choice(0.85, 0.42, 0.25), sep=sep))
    return grid2(cells, vsep=vsep)


def start_rows(starts, per_row, label_w, line_w, vsep):
    """Starts written as text, each followed by an answer line, per_row to a row
    (grades 4-5 Problems 3 and 6)."""
    rows = []
    for i in range(0, len(starts), per_row):
        rows.append("\\noindent\\hspace{0.3in}" + "\\hspace{0.6in}".join(
            "\\makebox[" + label_w + "][l]{" + s + "}" + answer_line(line_w) for s in starts[i:i + per_row]))
    return ("\n\n\\vspace{" + vsep + "}\n").join(rows) + "\n"
