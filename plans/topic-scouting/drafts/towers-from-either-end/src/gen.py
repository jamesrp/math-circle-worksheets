"""Build the three student packets for 'Towers from either end'.

Revision notes (final, after review.md and review-math.md):
- Tinted strips always start on a fresh page, so the colored pages can be
  stapled and handed out as a second set (K-1 page 6, 2-3 page 4, 4-5 page 3).
- Slot tints differ in lightness as well as hue, so the two slot colours stay
  distinguishable on a black-and-white copy.
- Colour wording refers to slots ("the red slots hold ..."), never to towers,
  so mixed-colour snap cubes cannot be confused with slot colours.
"""
import os
import subprocess
import sys

from diagrams import (towers, blank_towers, numstrip, k1_game_marks,
                      k1_choice, two_game_table, totals_blank, ruled,
                      cell_grid, triangle, ring_choices, order_example,
                      towers_to_numbers)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

WEEK = "NN"
TOPIC = "Towers from either end"


def preamble(band, pid, size):
    return r"""\documentclass[%s]{extarticle}
\usepackage[T1]{fontenc}
\usepackage{tgheros}
\renewcommand{\familydefault}{\sfdefault}
\usepackage[letterpaper,left=0.75in,right=0.75in,top=0.8in,bottom=0.8in,
  headheight=16pt,headsep=16pt,footskip=28pt]{geometry}
\usepackage{tikz}
\definecolor{slotred}{RGB}{248,182,182}
\definecolor{slotblue}{RGB}{112,152,228}
\usepackage{array}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\normalsize Week %s / %s / Grades %s}
\fancyfoot[L]{\small Bellingham Math Circle / Week %s / %s}
\fancyfoot[R]{\small \thepage}
\renewcommand{\headrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\newcounter{prob}
\newcommand{\problem}{\par\bigskip\stepcounter{prob}\noindent\textbf{Problem \theprob:} }
\newcommand{\ruledlines}[2]{\par\noindent\begin{tikzpicture}
  \foreach \k in {1,...,#1}{\draw[black!35] (0,-\k*#2) -- (\linewidth-1pt,-\k*#2);}
  \end{tikzpicture}\par}
\begin{document}
""" % (size, WEEK, TOPIC, band, WEEK, pid)


END = r"""
\end{document}
"""


def grid(cells, cols, colwidth, vspace="4mm", align="c"):
    """Lay out LaTeX snippets in a grid of minipages."""
    out = []
    for r in range(0, len(cells), cols):
        row = cells[r:r + cols]
        line = []
        for c in row:
            line.append(r"\begin{minipage}[b]{%s}\centering %s\end{minipage}" % (colwidth, c))
        out.append(r"\noindent " + r"\hfill".join(line) + (r"\hfill\null" if len(row) < cols else "")
                   + r"\par\vspace{%s}" % vspace)
    return "\n".join(out)


# ---------------------------------------------------------------- K-1
def k1():
    T = lambda h, tint=False, mh=5: towers(h, tint=tint, s=13, b=7, q=6.5,
                                            numsize=r"\small", maxh=mh)
    B = lambda n: blank_towers(n, 5, s=15, b=8, q=10, numsize=r"\normalsize")
    parts = [preamble("K--1", "NN-K-v1", "14pt")]
    parts.append(r"""
Build the towers on a strip and play with a partner. Take turns. On your
turn, take one whole tower from either end of the row. At the end, each
player snaps their cubes into one stack. The taller stack wins. If the
stacks are the same height, it is a tie.
""")
    # Problem 1
    parts.append(r"\problem Play each row two times, taking turns to go first. "
                 r"Ring who won each game, or ring tie.\par\vspace{6mm}")
    for h in [(5, 2, 1, 4), (1, 5, 2, 3), (2, 4, 3, 1)]:
        parts.append(r"\noindent\hspace*{4mm}" + T(h) + r"\hspace{12mm}"
                     + r"\raisebox{9mm}{" + k1_game_marks(2) + r"}\par\vspace{9mm}")
    parts.append(r"\newpage")
    # Problem 2
    parts.append(r"\problem You go first. Which tower should you take first "
                 r"so that you win, however your partner plays? Ring it."
                 r"\par\vspace{8mm}")
    parts.append(grid([T(h) for h in [(2, 1, 5, 3), (3, 5, 1, 2),
                                      (1, 1, 5, 2), (2, 5, 1, 1),
                                      (5, 1, 3, 2), (2, 3, 1, 4)]],
                      2, "0.48\\linewidth", vspace="12mm"))
    parts.append(r"\newpage")
    # Problem 3
    parts.append(r"\problem Is it better to go first or second on each row? "
                 r"Ring 1st or 2nd.\par\vspace{6mm}")
    rows3 = [(1, 5, 1), (5, 1, 5), (1, 4, 2), (3, 4, 2), (2, 5, 2)]
    cells = [T(h) + r"\\[3mm]" + k1_choice() for h in rows3]
    parts.append(grid(cells, 2, "0.48\\linewidth", vspace="9mm"))
    parts.append(r"\newpage")
    # Problem 4
    parts.append(r"\problem Make up rows of three towers where whoever goes "
                 r"first loses. Draw them.\par\vspace{7mm}")
    parts.append(grid([B(3) for _ in range(6)], 2,
                      "0.48\\linewidth", vspace="11mm"))
    parts.append(r"\newpage")
    # Problem 5
    parts.append(r"\problem Can you make a row of four towers where whoever "
                 r"goes first loses?\par\vspace{7mm}")
    parts.append(grid([B(4) for _ in range(6)], 2,
                      "0.48\\linewidth", vspace="11mm"))
    parts.append(r"\newpage")
    # Problem 6 (colored strips start here, on a fresh page)
    parts.append(r"\problem You and your partner play the grown-up together. "
                 r"The grown-up goes first on the colored strip. Can you beat "
                 r"the grown-up?\par\vspace{8mm}")
    parts.append(grid([T(h, True) for h in [(1, 2, 5, 2), (3, 4, 1, 2),
                                            (4, 1, 5, 2), (1, 4, 2, 3)]],
                      2, "0.48\\linewidth", vspace="14mm"))
    parts.append(r"\newpage")
    # Problem 7
    parts.append(r"\problem Now you go first on the colored strip. Can you "
                 r"play so that your partner can never beat you?"
                 r"\par\vspace{6mm}")
    parts.append(grid([T(h, True) for h in [(3, 1, 2, 5), (2, 4, 1, 1)]],
                      2, "0.48\\linewidth", vspace="10mm"))
    parts.append(grid([T(h, True, 3) for h in [(1, 3, 2, 1, 3, 1),
                                               (2, 1, 1, 3, 2, 2)]],
                      2, "0.49\\linewidth", vspace="4mm"))
    # Problem 8
    parts.append(r"\problem You go first on these colored rows. Which rows "
                 r"can you win, however your partner plays? Ring them."
                 r"\par\vspace{6mm}")
    parts.append(grid([T(h, True) for h in [(2, 1, 2, 3), (1, 3, 4, 2),
                                            (4, 1, 2, 5)]],
                      3, "0.32\\linewidth", vspace="2mm"))
    parts.append(END)
    return "".join(parts)


# ---------------------------------------------------------------- 2-3
def g23():
    T = lambda h, tint=False, mh=6: towers(h, tint=tint, s=10, b=5.5, q=5,
                                            maxh=mh)
    parts = [preamble("2--3", "NN-23-v1", "12pt")]
    parts.append(r"""
Build the towers on a strip of slots and play with a partner. Take turns. On
your turn, take one whole tower from either end of the row. When the row is
empty, the player with more cubes wins. The same number of cubes is a tie.
Playing as well as you can means collecting as many cubes as you can be sure
of. A row can be written with its heights:
\par\smallskip
\centerline{%s}
""" % towers_to_numbers((3, 1, 4, 2)))
    # Problem 1
    parts.append(r"\problem Play each row twice, so that each of you goes "
                 r"first once. Write both players' totals.\par\vspace{3mm}")
    for h in [(5, 2, 1, 4), (2, 6, 3, 4), (2, 4, 3, 1)]:
        parts.append(r"\noindent\hspace*{18mm}" + T(h) + r"\hspace{24mm}"
                     + r"\raisebox{3mm}{" + two_game_table() + r"}\par\vspace{5mm}")
    parts.append(r"\newpage")
    # Problem 2
    parts.append(r"\problem You go first on each of these rows. Find a first "
                 r"move that wins, however your partner plays after it. Ring "
                 r"that tower.\par\vspace{5mm}")
    parts.append(grid([T(h) for h in [(2, 1, 5, 3), (3, 6, 1, 2),
                                      (2, 3, 1, 5), (1, 4, 6, 2)]],
                      4, "0.24\\linewidth", vspace="2mm"))
    # Problem 3
    parts.append(r"\problem Is it better to go first or second on each of "
                 r"these rows? Ring your answer. Then find a way to tell from "
                 r"the three heights, without playing.\par\vspace{4mm}")
    rows3 = [(1, 5, 1), (5, 1, 5), (2, 6, 3), (3, 4, 2), (2, 5, 3), (4, 6, 1)]
    ch = ring_choices(["first", "second", "no difference"], gap=4, font=r"\small")
    parts.append(grid([T(h) + r"\\[2mm]" + ch for h in rows3], 3,
                      "0.32\\linewidth", vspace="6mm"))
    parts.append(ruled(4, "8mm"))
    parts.append(r"\newpage")
    # Problem 4
    parts.append(r"\problem Can you find a row of four towers on which the "
                 r"first player loses, however the first player plays?"
                 r"\par\vspace{2mm}")
    parts.append(r"\vspace{4mm}")
    parts.append(grid([numstrip([None] * 4, s=12, slotsize=r"\footnotesize")
                       for _ in range(8)], 2, "0.48\\linewidth", vspace="9mm"))
    parts.append(ruled(5, "9mm"))
    parts.append(r"\newpage")
    # Problem 5 (colored strips start here, on a fresh page)
    parts.append(r"\problem You and your partner play the grown-up together. "
                 r"The grown-up goes first on these colored rows. Can you beat "
                 r"the grown-up? How does the grown-up choose which towers to "
                 r"take?\par\vspace{4mm}")
    parts.append(grid([T(h, True) for h in [(1, 2, 5, 1, 3, 2),
                                            (3, 1, 1, 4, 2, 2)]],
                      2, "0.48\\linewidth", vspace="5mm"))
    parts.append(r"\centerline{" + T((1, 2, 3, 1, 2, 1, 3, 2), True) + r"}\par")
    parts.append(ruled(6, "8mm"))
    parts.append(r"\newpage")
    # Problem 6
    parts.append(r"\problem Go first on this colored row using the "
                 r"grown-up's plan. Can your partner ever make you take a tower "
                 r"on the other color? Try every way your partner can play, "
                 r"and write each game as the slot numbers in the order the "
                 r"towers were taken.\par\vspace{4mm}")
    parts.append(r"\centerline{" + order_example() + r"}\par\vspace{7mm}")
    parts.append(r"\centerline{" + T((2, 4, 1, 1, 3, 2), True) + r"}\par\vspace{6mm}")
    parts.append(r"\noindent\hfill" + cell_grid(3, 6) + r"\hfill"
                 + cell_grid(3, 6) + r"\hfill\null\par")
    parts.append(r"\newpage")
    # Problem 7
    parts.append(r"\problem In each of these colored rows, the red slots and "
                 r"the blue slots hold the same number of cubes. Which rows can "
                 r"the first player win? Write the totals when both players play "
                 r"as well as they can.\par\vspace{4mm}")
    tb = totals_blank("first", "second", 11)
    cells = [T(h, True) + r"\\[2mm]" + tb for h in [(2, 1, 2, 3), (1, 3, 4, 2),
                                                    (4, 1, 2, 5), (2, 4, 5, 3)]]
    parts.append(grid(cells, 2, "0.48\\linewidth", vspace="7mm"))
    parts.append(r"\centerline{\begin{minipage}{0.48\linewidth}\centering "
                 + T((3, 2, 4, 5), True) + r"\\[2mm]" + tb
                 + r"\end{minipage}}\par")
    parts.append(r"\newpage")
    # Problem 8
    parts.append(r"\problem Does the grown-up's plan work on rows of five? Find "
                 r"out who wins each of these colored rows when both players "
                 r"play as well as they can.\par\vspace{4mm}")
    cells = [T(h, True) + r"\\[2mm]" + tb for h in [(2, 1, 5, 1, 2), (4, 1, 1, 1, 4),
                                                    (1, 4, 2, 4, 1), (1, 2, 4, 2, 1)]]
    parts.append(grid(cells, 2, "0.48\\linewidth", vspace="6mm"))
    # Problem 9
    parts.append(r"\problem Make up a colored row of six where the red slots "
                 r"and the blue slots hold the same number of cubes, and the "
                 r"first player wins when both players play as well as they "
                 r"can.\par\vspace{6mm}")
    for _ in range(3):
        parts.append(r"\centerline{" + numstrip([None] * 6, True, s=14,
                                                 slotsize=r"\footnotesize")
                     + r"}\par\vspace{8mm}")
    parts.append(END)
    return "".join(parts)


# ---------------------------------------------------------------- 4-5
def result_table(rows, first="first player", second="second player"):
    out = [r"{\renewcommand{\arraystretch}{1.8}\begin{tabular}{l@{\hspace{8mm}}l@{\hspace{2mm}}p{13mm}@{\hspace{5mm}}l@{\hspace{2mm}}p{13mm}}"]
    for h in rows:
        out.append(", ".join(map(str, h)) + r" & %s & \hrulefill & %s & \hrulefill\\" % (first, second))
    out.append(r"\end{tabular}}")
    return "\n".join(out)


def g45():
    N = lambda h, tint=False: numstrip(h, tint=tint, s=9)
    parts = [preamble("4--5", "NN-45-v1", "12pt")]
    parts.append(r"""
Build the towers on a strip of slots. Two players take turns. On your turn,
take one whole tower from either end of the row. When the row is empty, the
player with more cubes wins. The same number of cubes is a tie. A row is
written as its tower heights from slot 1, so this row is 3, 1, 4, 2:
\par\smallskip
\centerline{%s}
\par\smallskip
Playing as well as you can means collecting as many cubes as you can be sure
of. Who wins a row, and by how many cubes, means the result when both players
play as well as they can.
""" % towers_to_numbers((3, 1, 4, 2)))
    # Problem 1
    parts.append(r"\problem For each row, find who wins and by how many "
                 r"cubes. Write each player's total.\par\vspace{2mm}")
    parts.append(r"\centerline{" + result_table([(2, 1, 5, 3), (1, 4, 6, 2),
                                                 (2, 4, 3, 1), (6, 2, 1, 5)])
                 + r"}\par")
    # Problem 2
    parts.append(r"\problem Who wins each row of three? Write each player's "
                 r"total. Find a rule that tells you who wins from the three "
                 r"heights, and explain why it works.\par\vspace{2mm}")
    parts.append(r"\centerline{" + result_table([(1, 5, 1), (5, 1, 5), (2, 6, 3),
                                                 (3, 4, 2), (2, 5, 3), (6, 1, 2)])
                 + r"}\par")
    parts.append(ruled(4, "8mm"))
    parts.append(r"\newpage")
    # Problem 3
    parts.append(r"\problem Is there a row of four towers, each 1 to 6 cubes "
                 r"high, on which the first player loses?\par\vspace{2mm}")
    parts.append(r"\vspace{4mm}")
    parts.append(grid([numstrip([None] * 4, s=12, slotsize=r"\footnotesize")
                       for _ in range(8)], 2, "0.48\\linewidth", vspace="9mm"))
    parts.append(ruled(6, "9mm"))
    parts.append(r"\newpage")
    # Problem 4 (colored strips start here, on a fresh page)
    parts.append(r"\problem The grown-up goes first on the colored strips and "
                 r"never loses. Play these rows against the grown-up as a team, "
                 r"and work out the grown-up's plan.\par\vspace{4mm}")
    parts.append(r"\noindent\hfill" + N((1, 2, 5, 1, 3, 2), True) + r"\hfill"
                 + N((3, 1, 1, 4, 2, 2), True) + r"\hfill\null\par\vspace{5mm}")
    parts.append(r"\centerline{" + N((1, 2, 3, 1, 2, 1, 3, 2), True) + r"}\par")
    parts.append(ruled(4, "8mm"))
    # Problem 5
    parts.append(r"\problem Explain why the grown-up's plan never loses on a "
                 r"row with an even number of towers, whatever the other player "
                 r"does.\par\vspace{2mm}")
    parts.append(ruled(8, "8.5mm"))
    parts.append(r"\newpage")
    # Problem 6
    parts.append(r"\problem In each of these colored rows, the red slots and "
                 r"the blue slots hold the same number of cubes. Which rows can "
                 r"the first player win, and by how many cubes?\par\vspace{4mm}")
    tb = totals_blank("first", "second", 11)
    cells = [N(h, True) + r"\\[3mm]" + tb for h in [(2, 1, 2, 3), (1, 3, 4, 2),
                                                    (4, 1, 2, 5), (2, 4, 5, 3),
                                                    (3, 1, 1, 3), (4, 2, 1, 3)]]
    parts.append(grid(cells, 3, "0.32\\linewidth", vspace="7mm"))
    # Problem 7
    parts.append(r"\problem In each of these colored rows of five, the blue "
                 r"slots hold more cubes than the red slots. Who wins each "
                 r"row? Explain why.\par\vspace{4mm}")
    cells = [N(h, True) + r"\\[3mm]" + tb for h in [(1, 4, 2, 4, 1), (2, 3, 1, 5, 2),
                                                    (3, 5, 2, 4, 1), (1, 3, 3, 3, 1)]]
    parts.append(grid(cells, 2, "0.48\\linewidth", vspace="6mm"))
    parts.append(ruled(5, "8mm"))
    parts.append(r"\newpage")
    # Problem 8
    parts.append(r"\problem In each of these colored rows of five, the red "
                 r"slots hold more cubes than the blue slots. Who wins each "
                 r"row?\par\vspace{4mm}")
    cells = [N(h, True) + r"\\[3mm]" + tb for h in [(4, 1, 1, 1, 4), (1, 2, 4, 2, 1),
                                                    (2, 1, 5, 1, 2), (4, 2, 1, 2, 4),
                                                    (4, 1, 6, 2, 3)]]
    parts.append(grid(cells, 2, "0.48\\linewidth", vspace="6mm"))
    # Problem 9
    parts.append(r"\problem Can the first player win a row of five on which the "
                 r"red slots and the blue slots hold the same number of cubes? "
                 r"Explain.\par\vspace{2mm}")
    parts.append(ruled(6, "8mm"))
    parts.append(r"\newpage")
    # Problem 10
    parts.append(r"\problem For each row, ring the first player's best first "
                 r"move, and find who wins and by how many cubes."
                 r"\par\vspace{4mm}")
    cells = [N(h) + r"\\[3mm]" + tb for h in [(3, 1, 4, 1, 5), (2, 1, 2, 5, 3),
                                              (5, 2, 6, 1, 3)]]
    parts.append(grid(cells, 3, "0.32\\linewidth", vspace="4mm"))
    # Problem 11
    parts.append(r"\problem In each box, write the most cubes the player whose "
                 r"turn it is can be sure of collecting from that row, in a game "
                 r"on 2, 3, 6, 2, 1, 4.\par\vspace{5mm}")
    parts.append(r"\centerline{" + triangle((2, 3, 6, 2, 1, 4)) + r"}\par")
    parts.append(END)
    return "".join(parts)


def build(name, tex):
    src = os.path.join(HERE, name + ".tex")
    with open(src, "w") as f:
        f.write(tex)
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                            "-output-directory", HERE, src],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            sys.exit(1)
    os.replace(os.path.join(HERE, name + ".pdf"), os.path.join(OUT, name + ".pdf"))
    log = open(os.path.join(HERE, name + ".log")).read()
    for w in ("Overfull", "Underfull \\hbox"):
        if w in log:
            print(name, "has", log.count(w), w)
    print("built", name)


if __name__ == "__main__":
    build("k-1", k1())
    build("grades-2-3", g23())
    build("grades-4-5", g45())
