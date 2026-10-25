#!/usr/bin/env python3
"""Generate k-1.tex for Week 98 K-1 (Growing from a few seeds).

All lengths are in millimetres and printed at 100%.
Working boards: 30 mm squares.  Record boards: 15-16 mm squares.
Cells are (row, column), counted from the top left.

Revision of the draft (final/): rule says "two or more"; rule pictures are
grid fragments with the mark inside the target square; the printed-start
problem moved to Problem 2; 6 record boards on Problem 1; guesses before the
4x4 and 5x5; single-seed removal made explicit on Problem 8; Problem 9
shortened with 2 record boards; two-wide boards spread out; US spelling.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = 30          # working-board square
REC2 = 16       # record square for 2x2 and 3x3 records
REC = 15        # record square for larger records
TEXTW = 191.9   # text width in mm (letter, 12 mm side margins)

WORK_THIN = "line width=0.9pt"
WORK_THICK = "line width=1.7pt"
REC_THIN = "line width=0.6pt"
REC_THICK = "line width=1.1pt"


def grid(x, y, rows, cols, s, record=False):
    """Board with top-left corner at (x, y); y grows upward in TikZ."""
    thin, thick = (REC_THIN, REC_THICK) if record else (WORK_THIN, WORK_THICK)
    out = []
    for c in range(1, cols):
        out.append(f"\\draw[{thin}] ({x + c*s},{y}) -- ({x + c*s},{y - rows*s});")
    for r in range(1, rows):
        out.append(f"\\draw[{thin}] ({x},{y - r*s}) -- ({x + cols*s},{y - r*s});")
    out.append(f"\\draw[{thick}] ({x},{y}) rectangle ({x + cols*s},{y - rows*s});")
    return "\n".join(out)


def centre(x, y, r, c, s):
    return (x + (c - 0.5) * s, y - (r - 0.5) * s)


def seed_dots(x, y, cells, s=W, radius=3.6):
    out = []
    for r, c in cells:
        cx, cy = centre(x, y, r, c, s)
        out.append(f"\\fill ({cx:.2f},{cy:.2f}) circle ({radius});")
    return "\n".join(out)


def drawn_counters(x, y, cells, s=W, radius=11):
    out = []
    for r, c in cells:
        cx, cy = centre(x, y, r, c, s)
        out.append(f"\\filldraw[fill=black!28, draw=black, line width=0.8pt] "
                   f"({cx:.2f},{cy:.2f}) circle ({radius});")
    return "\n".join(out)


def pic(body):
    return ("\\begin{tikzpicture}[x=1mm,y=1mm,line cap=rect]\n"
            + body + "\n\\end{tikzpicture}")


def problem(n, text):
    return f"\\textbf{{Problem {n}:}} {text}\\par\\vspace{{5mm}}\n"


pages = []

# ---------------------------------------------------------------- page 1
# Rule pictures: 3x3 fragments of a larger grid (no outer border, lines run
# past the edge), so the mark reads as a verdict on one square, not a board.
RS = 12      # fragment square
EXT = 2.5    # how far the grid lines run past the fragment


def rule_fragment(x, y, counters, target, mark):
    body = []
    for i in range(4):
        body.append(f"\\draw[{REC_THIN}] ({x + i*RS},{y + EXT}) -- ({x + i*RS},{y - 3*RS - EXT});")
        body.append(f"\\draw[{REC_THIN}] ({x - EXT},{y - i*RS}) -- ({x + 3*RS + EXT},{y - i*RS});")
    for r, c in counters:
        cx, cy = centre(x, y, r, c, RS)
        body.append(f"\\filldraw[fill=black!28, draw=black, line width=0.6pt] "
                    f"({cx:.2f},{cy:.2f}) circle (4.4);")
    cx, cy = centre(x, y, *target, RS)
    body.append(f"\\draw[line width=0.9pt, dash pattern=on 2.2pt off 1.6pt] "
                f"({cx:.2f},{cy:.2f}) circle (4.4);")
    body.append(f"\\node at ({cx:.2f},{cy - 0.2:.2f}) {{\\fontsize{{13}}{{14}}\\selectfont {mark}}};")
    return "\n".join(body)


FRAG_W = 3 * RS + 2 * EXT
# Legal: the target has three filled side neighbours (shows "two or more").
# Not legal: one side neighbour and one corner neighbour.
RULE_OK = ([(1, 2), (2, 1), (2, 3)], (2, 2))
RULE_NO = ([(1, 2), (3, 3)], (2, 2))
rules_pic = pic(
    rule_fragment(EXT, 0, *RULE_OK, "\\ding{51}") + "\n" +
    rule_fragment(EXT + FRAG_W + 8, 0, *RULE_NO, "\\ding{55}")
)

rules_text = (
    "Seeds are the first counters on a board, all in one color. "
    "Grow the board with counters of the other color. "
    "A square gets a counter when two or more squares next to it, not corner to corner, have counters. "
    "Your partner points to two of them before each new counter. "
    "Counters stay put. "
    "When no square can get a counter, the board is filled or stuck."
)

p1 = []
p1.append("\\noindent\\begin{minipage}[t]{97mm}\\vspace{0pt}\\raggedright\\setlength{\\parskip}{0pt}\n"
          + rules_text + "\n\\end{minipage}\\hfill"
          "\\begin{minipage}[t]{" + f"{2*FRAG_W + 8 + 1:.1f}" + "mm}\\vspace{1mm}\\raggedleft\n"
          + rules_pic + "\n\\end{minipage}\\par\\vspace{10mm}\n")
p1.append(problem(1, "Find every way to put 2 seeds on this board. "
                     "Draw each way with dots, and ring the ways that fill."))
body = [grid(0, 0, 2, 2, W)]
# six 2x2 records (16 mm squares) in two rows of three
step = 2 * REC2 + 14
for i in range(6):
    row, col = divmod(i, 3)
    body.append(grid(col * step, -60 - 12 - row * (2 * REC2 + 10), 2, 2, REC2, record=True))
p1.append("\\noindent" + pic("\n".join(body)) + "\n")
pages.append("".join(p1))

# ---------------------------------------------------------------- page 2: printed starts
STARTS = [
    [(1, 1), (1, 2), (2, 1)],            # bent three: one more square
    [(2, 1), (2, 2), (2, 3)],            # middle row: already stuck
    [(1, 1), (1, 3), (2, 1)],            # gap in the top row: grows to two rows
    [(1, 1), (2, 1), (3, 1), (1, 3)],    # column and a gap: fills
]
p = [problem(2, "Which of these boards can still grow? Grow each one until it stops.")]
body = []
gx = TEXTW - 180 - 0.6
for i, cells in enumerate(STARTS):
    row, col = divmod(i, 2)
    x, y = col * (90 + gx), -row * (90 + 14)
    body.append(grid(x, y, 3, 3, W))
    body.append(drawn_counters(x, y, cells))
p.append("\\noindent" + pic("\n".join(body)) + "\n")
pages.append("".join(p))

# ---------------------------------------------------------------- page 3: 3x3 fewest
p = [problem(3, "Fill this board with as few seeds as you can, and draw the seeds.")]
body = [grid(0, 0, 3, 3, W)]
step = 3 * REC2 + 14
for i in range(6):
    row, col = divmod(i, 3)
    body.append(grid(col * step, -90 - 12 - row * (3 * REC2 + 10), 3, 3, REC2, record=True))
p.append("\\noindent" + pic("\n".join(body)) + "\n")
pages.append("".join(p))

GUESS = ("Guess how few seeds can fill this board. "
         "Then fill it with as few seeds as you can, and draw the seeds.")

# ---------------------------------------------------------------- page 4: 4x4 guess and fewest
p = [problem(4, GUESS)]
body = [grid(0, 0, 4, 4, W)]
rx = 120 + 10
body.append(grid(rx, 0, 4, 4, REC, record=True))
body.append(grid(rx, -60 - 6, 4, 4, REC, record=True))
body.append(grid(0, -126 - 8, 4, 4, REC, record=True))
body.append(grid(60 + 10, -126 - 8, 4, 4, REC, record=True))
p.append("\\noindent" + pic("\n".join(body)) + "\n")
pages.append("".join(p))

# ---------------------------------------------------------------- page 5: 5x5 guess and fewest
# The two-line problem text leaves less room: 3 mm after the text, 5 mm
# between the board and the records.
p = [problem(5, GUESS).replace("\\vspace{5mm}", "\\vspace{3mm}")]
body = [grid(0, 0, 5, 5, W)]
body.append(grid(0, -150 - 5, 5, 5, REC, record=True))
body.append(grid(75 + 12, -150 - 5, 5, 5, REC, record=True))
p.append("\\noindent" + pic("\n".join(body)) + "\n")
pages.append("".join(p))

# ---------------------------------------------------------------- page 6: strips
p = [problem(6, "Fill each strip with as few seeds as you can, and draw the seeds.")]
body = []
y = 0
for n in (3, 4, 5, 6):
    body.append(grid(0, y, 1, n, W))
    body.append(grid(0, y - W - 3.5, 1, n, REC, record=True))
    y -= W + 3.5 + REC + 11
p.append("\\noindent" + pic("\n".join(body)) + "\n")
pages.append("".join(p))

# ---------------------------------------------------------------- page 7: 2-wide boards (drawn upright)
# Left column: 3x2 and 4x2 with their records beside them.  Right: 5x2 with
# its record below.  Gaps between working boards are about 14-23 mm.
p = [problem(7, "Fill each board with as few seeds as you can, and draw the seeds.")]
body = []
REC_GAP = 12
left = [(3, 0), (4, -3 * W - 14)]
for n, y in left:
    body.append(grid(0, y, n, 2, W))
    ry = y - (n * W - n * REC) / 2          # record centred beside its board
    body.append(grid(2 * W + REC_GAP, ry, n, 2, REC, record=True))
xr = TEXTW - 2 * W - 0.6
body.append(grid(xr, 0, 5, 2, W))
body.append(grid(xr + (2 * W - 2 * REC) / 2, -5 * W - 6, 5, 2, REC, record=True))
p.append("\\noindent" + pic("\n".join(body)) + "\n")
pages.append("".join(p))

# ---------------------------------------------------------------- page 8: which seed can come off by itself
TAKE_ONE = [
    (2, 2, [(1, 1), (1, 2), (2, 1)]),                 # 2x2 bent three
    (3, 3, [(1, 1), (1, 3), (3, 1), (3, 3)]),         # four corners
    (3, 3, [(1, 1), (1, 3), (2, 2), (3, 1)]),         # three corners and the centre
    (3, 3, [(1, 2), (2, 1), (2, 3), (3, 2)]),         # middle of each side
]
p = [problem(8, "Put seeds on the dots of one board. "
                "Ring each seed that can come off by itself while the other seeds still fill the board. "
                "Put each seed back before you try the next one.")]
body = []
pos = [(0, 0), (90 + gx, 0), (0, -90 - 14), (90 + gx, -90 - 14)]
for (rows, cols, cells), (x, y) in zip(TAKE_ONE, pos):
    body.append(grid(x, y, rows, cols, W))
    body.append(seed_dots(x, y, cells))
p.append("\\noindent" + pic("\n".join(body)) + "\n")
pages.append("".join(p))

# ---------------------------------------------------------------- page 9: take seeds off until none can go
TAKE_ALL = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 1)]
p = [problem(9, "Put seeds on the dots. Take seeds off one at a time while the board still fills. "
                "Draw the seeds left when no more can go. "
                "Can you end with a different number of seeds?")]
body = [grid(0, 0, 3, 3, W), seed_dots(0, 0, TAKE_ALL)]
step = 3 * REC2 + 14
for i in range(2):
    body.append(grid(i * step, -90 - 12, 3, 3, REC2, record=True))
p.append("\\noindent" + pic("\n".join(body)) + "\n")
pages.append("".join(p))

PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage[letterpaper, left=12mm, right=12mm, top=17mm, bottom=17mm,
            headheight=6mm, headsep=5mm, footskip=9mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{tgheros}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usepackage{pifont}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{Week 98 / Growing from a few seeds / K--1}
\fancyfoot[L]{\small Bellingham Math Circle / Week 98 / W98-K-v1}
\fancyfoot[R]{\small \thepage}
\renewcommand{\headrulewidth}{0.4pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\raggedright
\begin{document}
"""

if __name__ == "__main__":
    tex = PREAMBLE + "\n\\newpage\n".join(pages) + "\n\\end{document}\n"
    (HERE / "k-1.tex").write_text(tex)
    print("wrote", HERE / "k-1.tex")
