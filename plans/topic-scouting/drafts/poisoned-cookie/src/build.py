"""Build the three Poisoned cookie (Chomp) student packets.

Positions are tuples of row lengths, bottom row first; the poison is the
bottom-left cookie.  All drawing is in millimetres, so a 25 mm cell prints
at 25 mm when the PDF is printed at 100%.
Run:  python3 build.py   (writes k-1.tex, grades-2-3.tex, grades-4-5.tex and
compiles them into ../k-1.pdf, ../grades-2-3.pdf, ../grades-4-5.pdf).
Play-size boards that share a page are laid on a falling diagonal, and the
build stops if a 15 cm bite card set on one of them could reach another.
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from chomp import win, positions_in_box  # noqa: E402

WEEK = "Week NN"
TOPIC = "Poisoned cookie"


# ---------------------------------------------------------------- drawing
def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def cells_of(rows):
    for r, length in enumerate(rows, start=1):
        for c in range(1, length + 1):
            yield r, c


def position(rows, ox, oy, cell, x_at=None, cookies=True):
    """TikZ commands drawing a position with its bottom-left corner at (ox, oy) mm."""
    out = []
    lw = "0.5pt" if cell < 12 else "0.8pt"
    rad = 0.34 * cell
    for r, c in cells_of(rows):
        x0, y0 = ox + (c - 1) * cell, oy + (r - 1) * cell
        out.append(f"\\draw[line width={lw}, black!75] ({f(x0)},{f(y0)}) rectangle ++({f(cell)},{f(cell)});")
        cx, cy = x0 + cell / 2, y0 + cell / 2
        if (r, c) == (1, 1):
            out.append(f"\\fill[black!78] ({f(cx)},{f(cy)}) circle ({f(rad)});")
        elif cookies:
            out.append(f"\\draw[line width={lw}, black!35] ({f(cx)},{f(cy)}) circle ({f(rad)});")
    if x_at is not None:
        r, c = x_at
        cx, cy = ox + (c - 0.5) * cell, oy + (r - 0.5) * cell
        d = 0.26 * cell
        out.append(f"\\draw[line width=1.6pt] ({f(cx-d)},{f(cy-d)}) -- ({f(cx+d)},{f(cy+d)}) "
                   f"({f(cx-d)},{f(cy+d)}) -- ({f(cx+d)},{f(cy-d)});")
    return "\n".join(out)


def blank_grid(nrows, ncols, ox, oy, cell):
    """An empty grid for children to colour, with the poison drawn in its corner."""
    out = []
    for r in range(1, nrows + 1):
        for c in range(1, ncols + 1):
            x0, y0 = ox + (c - 1) * cell, oy + (r - 1) * cell
            out.append(f"\\draw[line width=0.5pt, black!40] ({f(x0)},{f(y0)}) rectangle ++({f(cell)},{f(cell)});")
    out.append(f"\\fill[black!78] ({f(ox + cell/2)},{f(oy + cell/2)}) circle ({f(0.34*cell)});")
    out.append(f"\\draw[line width=0.8pt, black!75] ({f(ox)},{f(oy)}) rectangle ++({f(cell)},{f(cell)});")
    return "\n".join(out)


def pic(body, extra=""):
    return ("\\begin{tikzpicture}[x=1mm, y=1mm" + extra + "]\n" + body + "\n\\end{tikzpicture}")


def row_of_positions(items, cell, gap, width=None, below=0.0):
    """Place positions left to right, bottoms aligned.  items: list of (rows, x_at).
    Returns TikZ body.  `below` leaves empty space under the boards (for writing)."""
    body = []
    x = 0.0
    for rows, x_at in items:
        body.append(position(rows, x, below, cell, x_at))
        x += max(rows) * cell + gap
    if width:
        # invisible frame so that the picture has a fixed width
        body.append(f"\\path (0,0) rectangle ({f(width)},1);")
    return "\n".join(body)


def bite_picture(cell):
    """Launch example: one bite on a 2 by 5 board (row 1, column 3)."""
    rows = (5, 5)
    body = []
    w = 5 * cell
    gap = 16.0
    # panel 1: board with the chosen cookie marked
    body.append(position(rows, 0, 0, cell, x_at=(1, 3)))
    # arrow
    a0 = w + 3
    body.append(f"\\draw[-{{Stealth[length=3mm]}}, line width=1pt] ({f(a0)},{f(cell)}) -- ++({f(gap-6)},0);")
    # panel 2: the card on the board
    x2 = w + gap
    body.append(position(rows, x2, 0, cell, x_at=(1, 3)))
    cx0 = x2 + 2 * cell
    over = 0.8 * cell
    body.append(f"\\fill[black!30, opacity=0.55] ({f(cx0)},0) rectangle ({f(x2 + w + over)},{f(2*cell + over)});")
    body.append(f"\\draw[line width=1.4pt] ({f(x2 + w + over)},0) -- ({f(cx0)},0) -- ({f(cx0)},{f(2*cell + over)});")
    # arrow
    a1 = x2 + w + over + 3
    body.append(f"\\draw[-{{Stealth[length=3mm]}}, line width=1pt] ({f(a1)},{f(cell)}) -- ++({f(gap-6)},0);")
    # panel 3: what is left
    x3 = x2 + w + over + gap
    body.append(position((2, 2), x3, 0, cell))
    return pic("\n".join(body))


# ---------------------------------------------------------------- document
def preamble(level, packet_id):
    return r"""\documentclass[12pt]{article}
\usepackage[letterpaper, left=13mm, right=13mm, top=20mm, bottom=20mm,
  headheight=15pt, headsep=5mm, footskip=10mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{tgheros}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{fancyhdr}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\pagestyle{fancy}
\fancyhf{}
\lhead{\small """ + WEEK + " / " + TOPIC + " / " + level + r"""}
\lfoot{\small Bellingham Math Circle / """ + WEEK + " / " + packet_id + r"""}
\rfoot{\small \thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\newcommand{\prob}[1]{\par\textbf{Problem #1:}~}
\raggedright
\begin{document}
"""


END = "\n\\end{document}\n"


def para(text, after=3):
    return text + f"\\par\\vspace{{{after}mm}}\n"


def center(tikz, after=6):
    return "{\\centering " + tikz + "\\par}\\vspace{" + str(after) + "mm}\n"


def left(tikz, after=6):
    return tikz + "\\par\\vspace{" + str(after) + "mm}\n"


NEWPAGE = "\\newpage\n"


# ---------------------------------------------------------------- bite-card safety
CARD = 150.0   # the bite card reaches about 15 cm up and to the right of its corner
SLACK = 3.0    # allow the corner to be placed up to 3 mm left of or below the cell corner


def diagonal(items, cell, gap):
    """Place play-size boards on a falling diagonal, the first at the top left.
    Returns (TikZ body, placements), placements = [(rows, ox, oy)] in mm.
    Each later board lies wholly below and to the right of every earlier one,
    so a bite card set on one board never reaches another."""
    total_h = sum(len(rows) * cell for rows in items) + gap * (len(items) - 1)
    body, placed = [], []
    x, top = 0.0, total_h
    for rows in items:
        oy = top - len(rows) * cell
        body.append(position(rows, x, oy, cell))
        placed.append((rows, x, oy))
        x += max(rows) * cell + gap
        top = oy - gap
    return "\n".join(body), placed


def card_check(name, placed, cell):
    """Fail the build if a bite on one play-size board could put the card over another."""
    def cells(rows, ox, oy):
        return [(ox + (c - 1) * cell, oy + (r - 1) * cell) for r, c in cells_of(rows)]
    for i, (ra, xa, ya) in enumerate(placed):
        bites = [(x, y) for (x, y) in cells(ra, xa, ya)
                 if (x, y) != (xa, ya)]                       # never the poison
        for j, (rb, xb, yb) in enumerate(placed):
            if i == j:
                continue
            for (bx, by) in bites:
                x0, y0 = bx - SLACK, by - SLACK
                for (cx, cy) in cells(rb, xb, yb):
                    if cx + cell > x0 and cx < x0 + CARD and cy + cell > y0 and cy < y0 + CARD:
                        raise SystemExit(f"{name}: a bite on board {ra} reaches board {rb}")


# ---------------------------------------------------------------- K-1
def build_k1():
    s = [preamble("Grades K--1", "NN-K-v1")]
    s.append(para("Two players take turns. On your turn, put the corner of the bite card on a cookie "
                  "and eat every cookie under the card. Whoever has to eat the poison cookie loses.", 4))
    s.append(center(bite_picture(10), 8))
    C = 25

    # Problem 1: small boards around the losing L (2,1)
    s.append(para("\\prob{1}It is your turn on each board. Mark your first bite with an X if you can "
                  "make sure you win, or circle the board if you can't.", 5))
    body, placed = diagonal([(2, 1), (2, 2), (3, 1)], C, 7)
    card_check("K-1 P1", placed, C)
    s.append(left(pic(body), 0))
    s.append(NEWPAGE)

    # Problem 2: two-row rectangles
    s.append(para("\\prob{2}Play on each board with your partner, taking turns going first. Find how to "
                  "make sure you win when you go first, and mark your first bite with an X.", 6))
    body, placed = diagonal([(3, 3), (4, 4)], C, 12)
    card_check("K-1 P2", placed, C)
    s.append(left(pic(body), 0))
    s.append(NEWPAGE)

    # Problem 3: L shapes, equal and unequal arms
    s.append(para("\\prob{3}Play on each board with your partner. Circle each board where the player "
                  "who goes second can make sure to win.", 6))
    body, placed = diagonal([(3, 1, 1), (4, 1, 1)], C, 12)
    card_check("K-1 P3", placed, C)
    s.append(left(pic(body), 0))
    s.append(NEWPAGE)

    # Problem 4: squares
    s.append(para("\\prob{4}Play on each board with your partner, taking turns going first. Find how to "
                  "make sure you win when you go first, and mark your first bite with an X.", 6))
    body, placed = diagonal([(3, 3, 3), (4, 4, 4, 4)], C, 12)
    card_check("K-1 P4", placed, C)
    s.append(left(pic(body), 0))
    s.append(NEWPAGE)

    # Problem 5: a longer two-row board
    s.append(para("\\prob{5}Play on this board with your partner, taking turns going first. Find how to "
                  "make sure you win when you go first, and mark your first bite with an X.", 6))
    s.append(left(pic(position((6, 6), 0, 0, C)), 0))
    s.append(NEWPAGE)

    # Problem 6: invent second-player wins by biting a 4 by 4 board
    s.append(para("\\prob{6}Take bites from a full 4 by 4 board to make a board where the player who "
                  "goes second can make sure to win. Color each board you find on a grid.", 8))
    g = 14
    body = []
    for i in range(3):
        for j in range(3):
            body.append(blank_grid(4, 4, j * (4 * g + 10), -i * (4 * g + 12), g))
    s.append(left(pic("\n".join(body)), 0))
    s.append(END)
    return "".join(s)


# ---------------------------------------------------------------- 2-3
RULES_OLDER = ("Two players take turns. On your turn, put the corner of the bite card on any cookie "
               "and eat every cookie under the card. That is the chosen cookie and every cookie "
               "above it or to its right, including those up and to the right. Whoever has to eat "
               "the poison cookie in the bottom-left corner loses. To record a bite, draw an X on "
               "the chosen cookie.")


def build_23():
    s = [preamble("Grades 2--3", "NN-23-v1")]
    s.append(para(RULES_OLDER, 4))
    s.append(center(bite_picture(9), 8))

    # Problem 1: small positions, decide and explain
    s.append(para("\\prob{1}It is your turn on each board. If you can make sure to win, however your "
                  "partner plays, mark your first bite. If you can't, explain why.", 5))
    items = [(3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (3, 1, 1)]
    cell = 11
    body = []
    slot_w, slot_h = 65, 66
    maxh = 3 * cell
    for k, rows in enumerate(items):
        i, j = divmod(k, 3)
        body.append(position(rows, j * slot_w, -i * slot_h - maxh, cell))
    s.append(left(pic("\n".join(body)), 0))
    s.append(NEWPAGE)

    # Problem 2: two-row rectangles
    s.append(para("\\prob{2}On each board, mark a first bite after which the first player can make "
                  "sure to win.", 5))
    cell = 11
    s.append(left(pic(row_of_positions([((3, 3), None), ((4, 4), None), ((6, 6), None)], cell, 16)), 18))

    # Problem 3: two-row positions and the rule
    s.append(para("\\prob{3}It is your turn on each board. If you can make sure to win, mark your "
                  "first bite. Then find a rule that tells, for every board with two rows, whether "
                  "the player whose turn it is can make sure to win. Explain why your rule always "
                  "works.", 5))
    cell = 10
    items = [(5, 4), (5, 2), (5, 3), (4, 1), (6, 5), (6, 3)]
    body = []
    slot_w, slot_h = 63, 30
    for k, rows in enumerate(items):
        i, j = divmod(k, 3)
        body.append(position(rows, j * slot_w, -i * slot_h - 2 * cell, cell))
    s.append(left(pic("\n".join(body)), 0))
    s.append(NEWPAGE)

    # Problem 4: squares
    s.append(para("\\prob{4}On each board, mark a first bite after which the first player can make "
                  "sure to win.", 5))
    s.append(left(pic(row_of_positions([((3, 3, 3), None), ((4, 4, 4, 4), None)], 11, 20)), 18))

    # Problem 5: squares explained
    s.append(para("\\prob{5}Explain how the first player can make sure to win on every square board "
                  "bigger than one cookie, even this 10 by 10 one.", 5))
    s.append(left(pic(position(tuple([10] * 10), 0, 0, 6)), 0))
    s.append(NEWPAGE)

    # Problem 6: 3 by 4
    s.append(para("\\prob{6}On the 3 by 4 board, mark a first bite after which the first player can "
                  "make sure to win.", 5))
    s.append(left(pic(position((4, 4, 4), 0, 0, 11)), 0))
    s.append(NEWPAGE)

    # Problem 7: invent three-row second-player wins inside 3 by 5
    s.append(para("\\prob{7}Take bites from a full 3 by 5 board to make boards with three rows where "
                  "the player who goes second can make sure to win. Color each one you find on a "
                  "grid.", 8))
    g = 12
    body = []
    for i in range(3):
        for j in range(2):
            body.append(blank_grid(3, 5, j * (5 * g + 34), -i * (3 * g + 20), g))
    s.append(left(pic("\n".join(body)), 0))
    s.append(END)
    return "".join(s)


# ---------------------------------------------------------------- 4-5
ANA = ("Ana says: \\textit{``On a rectangle with more than one cookie, the first player can make "
       "sure to win. Suppose instead that the second player could make sure to win. Then if the "
       "first player ate only the top-right cookie, the second player would have a reply after "
       "which the first player cannot make sure to win. But every bite on the full board eats the "
       "top-right cookie too, so the first player could have made that same bite at the start. "
       "Then the second player would face that same board, and the first player would be the one "
       "who can make sure to win. That can't be, so the first player can make sure to win.''}")


def build_45():
    s = [preamble("Grades 4--5", "NN-45-v1")]
    s.append(para(RULES_OLDER, 4))
    s.append(center(bite_picture(9), 8))

    # Problem 1: find winning first bites on rectangles
    s.append(para("\\prob{1}On each board, mark a first bite after which the first player can make "
                  "sure to win.", 5))
    cell = 10
    s.append(left(pic(row_of_positions([((4, 4), None), ((6, 6), None)], cell, 20)), 10))
    s.append(left(pic(row_of_positions([((3, 3, 3), None), ((4, 4, 4, 4), None)], cell, 20)), 0))
    s.append(NEWPAGE)

    # Problem 2: classify all boards inside 3 by 3
    s.append(para("\\prob{2}For each board below, decide whether the player whose turn it is can "
                  "make sure to win. Write W in its box if so, and L if not.", 6))
    ps = positions_in_box(3, 3)
    ps = sorted(ps, key=lambda p: (-sum(p), [-x for x in p]))
    cell = 8
    per_row = 5
    slot_w, slot_h = 38, 49
    body = []
    for k, rows in enumerate(ps):
        i, j = divmod(k, per_row)
        x = j * slot_w
        base = -i * slot_h - 3 * cell
        body.append(position(rows, x, base, cell))
        body.append(f"\\draw[line width=0.6pt, black!60] ({f(x)},{f(base - 14)}) rectangle ++(10,10);")
    s.append(left(pic("\n".join(body)), 0))
    s.append(NEWPAGE)

    # Problem 3: longer two-row boards
    s.append(para("\\prob{3}It is your turn on each board. If you can make sure to win, mark your "
                  "first bite.", 5))
    cell = 10
    items = [(5, 4), (6, 3), (4, 1), (6, 5), (5, 2), (6, 4)]
    body = []
    slot_w, slot_h = 63, 30
    for k, rows in enumerate(items):
        i, j = divmod(k, 3)
        body.append(position(rows, j * slot_w, -i * slot_h - 2 * cell, cell))
    s.append(left(pic("\n".join(body)), 12))

    # Problem 4: explain two rows and squares
    s.append(para("\\prob{4}Explain how the first player can make sure to win on every rectangle with "
                  "two rows and on every square bigger than one cookie, however long the sides are.", 0))
    s.append(NEWPAGE)

    # Problem 5: every winning first bite on 3 by 4
    s.append(para("\\prob{5}Mark every first bite on the 3 by 4 board after which the first player "
                  "can make sure to win.", 5))
    s.append(left(pic(position((4, 4, 4), 0, 0, 11)), 12))
    g = 8
    body = []
    for i in range(3):
        for j in range(4):
            body.append(blank_grid(3, 4, j * (4 * g + 18), -i * (3 * g + 12), g))
    s.append(left(pic("\n".join(body)), 0))
    s.append(NEWPAGE)

    # Problem 6: strategy stealing
    s.append(para("\\prob{6}" + ANA, 4))
    s.append(para("On the 3 by 4 board, the first player eats only the top-right cookie. Find a reply "
                  "that lets the second player make sure to win, and mark it on this board.", 5))
    s.append(left(pic(position((4, 4, 3), 0, 0, 11)), 10))
    s.append(para("Is Ana right? Then explain which step of her reason breaks on this board, where "
                  "the first player cannot make sure to win.", 5))
    s.append(left(pic(position((3, 1, 1), 0, 0, 11)), 0))
    s.append(NEWPAGE)

    # Problem 7: three rows
    s.append(para("\\prob{7}Nobody knows a simple rule for finding a winning first bite on rectangles "
                  "with three rows. On the 3 by 5 board and on this 3 by 6 board, mark a first bite "
                  "after which the first player can make sure to win.", 6))
    s.append(left(pic(position((5, 5, 5), 0, 0, 11)), 14))
    C = 25
    s.append(left(pic(position((6, 6, 6), 0, 0, C)), 0))
    s.append(END)
    return "".join(s)


# ---------------------------------------------------------------- main
def compile_tex(name, tex):
    path = os.path.join(HERE, name + ".tex")
    with open(path, "w") as fh:
        fh.write(tex)
    build = os.path.join(HERE, "build")
    os.makedirs(build, exist_ok=True)
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                            "-output-directory", build, path], capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            raise SystemExit(f"pdflatex failed on {name}")
    log = open(os.path.join(build, name + ".log")).read()
    for bad in ("Overfull", "Underfull \\vbox", "Float too large"):
        if bad in log:
            print(f"warning: {name}: {bad} in log")
    shutil.copy(os.path.join(build, name + ".pdf"), os.path.join(OUT, name + ".pdf"))


if __name__ == "__main__":
    compile_tex("k-1", build_k1())
    compile_tex("grades-2-3", build_23())
    compile_tex("grades-4-5", build_45())
    print("built")
