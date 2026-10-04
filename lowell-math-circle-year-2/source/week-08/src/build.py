"""Build the three Week 8 student packets (K-1, 2-3, 4-5) as LaTeX + TikZ.

Run:  python3 build.py   (needs xelatex; writes ../k-1.pdf, ../grades-2-3.pdf,
../grades-4-5.pdf).  Answers are checked separately in check.py."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from tikzlib import board, piles, choice, answer_line  # noqa: E402

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(SRC)


def preamble(size, level, pid):
    return rf"""\documentclass[{size}pt]{{extarticle}}
\usepackage[letterpaper, left=0.75in, right=0.75in, top=0.8in, bottom=0.8in,
  headheight=20pt, headsep=16pt, footskip=30pt]{{geometry}}
\usepackage{{fontspec}}
\setmainfont{{texgyreheros}}[Extension=.otf, UprightFont=*-regular,
  BoldFont=*-bold, ItalicFont=*-italic, BoldItalicFont=*-bolditalic]
\usepackage{{tikz}}
\usetikzlibrary{{shapes.geometric, arrows.meta}}
\usepackage{{array}}
\usepackage{{fancyhdr}}
\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[L]{{Week 8 / Rook race and Nim / {level}}}
\fancyfoot[L]{{Bellingham Math Circle / Week 8 / {pid}}}
\fancyfoot[R]{{\thepage}}
\renewcommand{{\headrulewidth}}{{0pt}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0pt}}
\linespread{{1.12}}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\newcommand{{\prob}}[1]{{\textbf{{Problem #1:}}}}
\begin{{document}}
\raggedright
"""


END = "\n\\end{document}\n"


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


def side_by_side(text, pic, textw="4.55in", picw="2.1in", align="c"):
    if align == "t":
        return (
            "\\noindent\\begin{minipage}[t]{" + textw + "}\\vspace{0pt}\\raggedright\n" + text +
            "\n\\end{minipage}\\hfill"
            "\\begin{minipage}[t]{" + picw + "}\\vspace{0pt}\\raggedleft\n" + pic +
            "\n\\end{minipage}\n\n"
        )
    return (
        "\\noindent\\begin{minipage}[c]{" + textw + "}\\raggedright\n" + text + "\n\\end{minipage}\\hfill"
        "\\begin{minipage}[c]{" + picw + "}\\raggedleft\n" + pic + "\n\\end{minipage}\n\n"
    )


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


RULES_OLDER = (
    "Players take turns. On a board, a move slides the token straight left or "
    "straight down, toward the star's side, one or more squares. Whoever moves the "
    "token onto the star wins.\n\n"
    "\\vspace{0.12in}\n"
    "In a game with piles of counters, a move takes one or more counters from one pile. "
    "Whoever takes the last counter wins."
)


# ---------------------------------------------------------------- K-1 -------
def k1():
    t = [preamble(14, "K--1", "F08-K-v4")]
    rules = (
        "On your turn, slide the token straight left or straight down, toward the "
        "star's side, one or more squares. Whoever moves the token onto the star wins."
    )
    t.append(side_by_side(rules, rook_moves_picture(0.4), textw="4.85in", picw="1.8in"))
    t.append("\\vspace{0.45in}\n")
    # Problem 1: two 3x3 starts at playing size (far corner: second; top middle: first)
    t.append("\\prob{1} Play many games from the dot on each board. "
             "Circle if you would rather go first or second.\n\n\\vspace{0.35in}\n")
    cells = [stack(board(3, 1.0, dots=[d]), choice(0.85, 0.42, 0.25), sep="0.2in")
             for d in [(2, 2), (1, 2)]]
    t.append(grid2(cells, colw="3.3in"))
    t.append("\\newpage\n")

    # Problem 2: four 4x4 boards at playing size, two per page
    t.append("\\prob{2} Play many games from the dot on each board on this page and the "
             "next page. Circle if you would rather go first or second.\n\n\\vspace{0.1in}\n")
    t.append(board_with_choice(4, 1.0, (3, 3)))
    t.append("\\vspace{0.05in}\n")
    t.append(board_with_choice(4, 1.0, (3, 0)))
    t.append("\\newpage\n")
    t.append("\\vspace*{0.2in}\n")
    t.append(board_with_choice(4, 1.0, (2, 2)))
    t.append("\\vspace{0.3in}\n")
    t.append(board_with_choice(4, 1.0, (1, 3)))
    t.append("\\newpage\n")

    # Problem 3: four 5x5 boards, find the winning move
    t.append("\\prob{3} It is your turn, and the token is on the dot. "
             "Color the square you should move it to so that you can win.\n\n\\vspace{0.3in}\n")
    cells = [board(5, 0.66, dots=[d]) for d in [(0, 3), (3, 1), (2, 4), (4, 3)]]
    t.append(grid2(cells, vsep="0.45in"))
    t.append("\\newpage\n")

    # Problem 4: 6x6 board, colour every square you want to move to
    t.append("\\prob{4} Play many games on this board, starting on any square except the "
             "star. Color every square you want to move the token to.\n\n\\vspace{0.3in}\n")
    t.append(centered(board(6, 1.05)))
    t.append("\\newpage\n")

    # Problem 5: two piles, first or second (pile rule given here, where it is used)
    t.append("\\prob{5} On your turn, take one or more counters from one pile, and whoever "
             "takes the last counter wins. Play with each pair of piles and circle if you "
             "would rather go first or second.\n\n\\vspace{0.3in}\n")
    starts = [(3, 3), (4, 1), (2, 2), (5, 3)]
    cells = []
    for i, p in enumerate(starts):
        rowmax = max(max(starts[i - i % 2]), max(starts[i - i % 2 + 1]))
        cells.append(stack(piles(p, r=0.14, gap=0.6, maxk=rowmax),
                           choice(0.85, 0.42, 0.25), sep="0.15in"))
    t.append(grid2(cells, vsep="0.4in"))
    t.append("\\vspace{0.5in}\n\n")
    # Problem 6: 7 and 7, show you can always win
    t.append("\\prob{6} Your partner goes first with these two piles of 7. "
             "Show the adult how you can always win.\n\n\\vspace{0.2in}\n")
    t.append(centered(piles((7, 7), r=0.14, gap=0.65)))
    t.append("\\newpage\n")

    # Problem 7: printed 8x8 from the far corner, show you can always win
    t.append("\\prob{7} Your partner goes first, with the token in the corner farthest from "
             "the star on the separate 8-by-8 board. Show the adult how you can always win."
             "\n\n\\vspace{0.15in}\n")
    t.append(centered(board(8, 0.42, dots=[(7, 7)])))
    t.append("\\vspace{0.3in}\n\n")
    # Problem 8: three piles
    t.append("\\prob{8} Make each set of three piles with counters and play many games. "
             "Circle if you would rather go first or second.\n\n\\vspace{0.25in}\n")
    starts = [(1, 1, 1), (1, 1, 2), (1, 2, 3), (2, 2, 3)]
    cells = []
    for i, p in enumerate(starts):
        rowmax = max(max(starts[i - i % 2]), max(starts[i - i % 2 + 1]))
        cells.append(stack(piles(p, r=0.13, gap=0.6, maxk=rowmax),
                           choice(0.85, 0.42, 0.25), sep="0.12in"))
    t.append(grid2(cells, vsep="0.3in"))
    t.append(END)
    return "".join(t)


# ---------------------------------------------------------------- 2-3 -------
def labelled_piles(p, label, r=0.1, gap=0.4, maxk=None, w="1.55in", line=1.3):
    return ("\\begin{minipage}[b]{" + w + "}\\centering\n" + piles(p, r=r, gap=gap, maxk=maxk)
            + "\n\n\\vspace{0.12in}" + label + "\n\n\\vspace{0.35in}"
            + answer_line(line) + "\n\\end{minipage}")


def g23():
    t = [preamble(12, "Grades 2--3", "F08-M-v4")]
    t.append(side_by_side(RULES_OLDER, rook_moves_picture(0.38), textw="4.9in", picw="1.8in"))
    t.append("\\vspace{0.35in}\n")
    # Problem 1: four 5x5 starts
    t.append("\\prob{1} Play many games on a 5-by-5 board from each of these starting squares. "
             "Would you rather go first or second?\n\n"
             "\\vspace{0.3in}\n")
    cells = [stack(board(5, 0.46, dots=[d]), answer_line(1.8), sep="0.45in")
             for d in [(4, 4), (4, 2), (3, 3), (1, 4)]]
    t.append(grid2(cells, vsep="0.4in"))
    t.append("\\newpage\n")

    # Problem 2: colour the 8x8 board
    t.append("\\prob{2} Color every square of this 8-by-8 board except the star. "
             "Color a square green if you would rather go first when the token starts there, "
             "and red if you would rather go second.\n\n\\vspace{0.25in}\n")
    t.append(centered(board(8, 0.55)))
    t.append("\\vspace{0.35in}\n\n")
    # Problem 3: explain the second player's win from the corner
    t.append(side_by_side(
        "\\prob{3} Your partner goes first, with the token in the top-right corner of an "
        "8-by-8 board. Explain how you can always win, however your partner moves.",
        board(8, 0.26, dots=[(7, 7)], line="0.6pt"), textw="4.5in", picw="2.2in", align="t"))
    t.append("\\newpage\n")

    # Problem 4: two-pile games, played with counters
    t.append("\\prob{4} Play many games with two piles of counters from each start. "
             "Would you rather go first or second?\n\n\\vspace{0.3in}\n")
    starts = [(4, 4), (6, 2), (5, 3), (7, 7)]
    t.append("\\noindent " + "\\hfill".join(
        labelled_piles(p, f"{p[0]} and {p[1]}", maxk=7) for p in starts) + "\n")
    t.append("\\vspace{0.6in}\n\n")
    # Problem 5: board = two piles
    t.append(side_by_side(
        "\\prob{5} Which two piles of counters make the same game as this 8-by-8 board "
        "with the token on the dot? Explain how each move on the board "
        "matches a move with the piles.",
        board(8, 0.4, dots=[(5, 2)]), textw="3.3in", picw="3.3in", align="t"))
    t.append("\\newpage\n")

    # Problem 6: one large two-pile start, with an explanation
    t.append("\\prob{6} A game starts with piles of 52 and 37 counters. Would you rather go "
             "first or second? Explain how you can always win, however the other player moves.\n\n")
    t.append("\\vspace{3.9in}\n\n")
    # Problem 7: small three-pile games
    t.append("\\prob{7} Play many games with three piles from each start. Would you rather go "
             "first or second?\n\n\\vspace{0.3in}\n")
    starts = [(1, 1, 1), (1, 1, 2), (2, 2, 3), (1, 2, 3)]
    t.append("\\noindent " + "\\hfill".join(
        labelled_piles(p, ", ".join(map(str, p)), gap=0.36) for p in starts) + "\n")
    t.append("\\newpage\n")

    # Problem 8: all starts with piles 1..3
    t.append("\\prob{8} Find every start with three piles, each with 1, 2 or 3 counters, where "
             "you would rather go second. The order of the piles does not matter. Explain how "
             "you know you have found them all.\n\n")
    t.append("\\vspace{4.1in}\n\n")
    # Problem 9: piles 1..6
    t.append("\\prob{9} Find all the starts with three piles, each with 1 to 6 counters, "
             "where you would rather go second. The order of the piles does not matter.\n")
    t.append(END)
    return "".join(t)


# ---------------------------------------------------------------- 4-5 -------
def start_row(starts, sep="\\hspace{0.45in}"):
    return ("\\begin{center}" + sep.join(starts) + "\\end{center}\n")


def g45():
    t = [preamble(12, "Grades 4--5", "F08-U-v4")]
    t.append(side_by_side(RULES_OLDER, rook_moves_picture(0.38), textw="4.9in", picw="1.8in"))
    t.append("\\vspace{0.35in}\n")
    t.append("\\prob{1} Color every square of this 8-by-8 board except the star: green if the "
             "first player can always win when the token starts there, red if the second player "
             "can always win. Explain why the second player can always win from a red square.\n\n"
             "\\vspace{0.2in}\n")
    t.append(centered(board(8, 0.46)))
    t.append("\\newpage\n")

    t.append("\\prob{2} Find two piles of counters that make the same game as this board with "
             "the token on the dot. Explain how each move on the board matches a move with the "
             "piles. Which player can always win from piles of 23 and 17? From piles of 30 and 30?"
             "\n\n\\vspace{0.2in}\n")
    t.append(centered(board(8, 0.4, dots=[(6, 3)])))
    t.append("\\newpage\n")

    t.append("\\prob{3} Play many games with three piles from each start. Which player can "
             "always win?\n\n\\vspace{0.25in}\n")
    starts = ["1, 1, 1", "1, 1, 2", "1, 2, 3", "2, 2, 5", "1, 3, 4", "1, 4, 5"]
    rows = []
    for i in range(0, 6, 2):
        rows.append("\\noindent\\hspace{0.3in}" + "\\hspace{0.6in}".join(
            "\\makebox[0.9in][l]{" + s + "}" + answer_line(1.6) for s in starts[i:i + 2]))
    t.append("\n\n\\vspace{0.3in}\n".join(rows) + "\n")
    t.append("\\vspace{0.6in}\n\n")
    t.append("\\prob{4} Find all the starts with three piles, each with 1 to 7 counters, where "
             "the second player can always win. The order of the piles does not matter.\n")
    t.append("\\newpage\n")

    t.append("\\prob{5} The second player can always win from each of these starts.\n")
    t.append(start_row(["1, 2, 3", "1, 4, 5", "2, 4, 6", "3, 5, 6", "2, 5, 7"]))
    t.append("The first player can always win from each of these starts.\n")
    t.append(start_row(["1, 2, 4", "2, 3, 5", "2, 4, 7", "3, 4, 6"]))
    t.append("Make these starts with counters, and split every pile into stacks of 1, 2, 4, 8, "
             "16 and so on, with no two stacks in one pile the same size. Find a rule about the "
             "stacks that tells which player can always win.\n\n")
    t.append("\\vspace{4.0in}\n\n")
    t.append("\\prob{6} Which player can always win from each of these starts? When it is the "
             "first player, find a first move that lets the first player always win.\n\n"
             "\\vspace{0.3in}\n")
    starts = ["3, 5, 7", "6, 10, 12", "13, 9, 7", "11, 14, 21"]
    t.append("\n\n\\vspace{0.32in}\n".join(
        "\\noindent\\hspace{0.3in}\\makebox[1.2in][l]{" + s + "}" + answer_line(4.6) for s in starts) + "\n")
    t.append("\\newpage\n")

    t.append("\\prob{7} Explain why your rule from Problem 5 is right for every start, even with "
             "piles of hundreds of counters.\n")
    t.append("\\newpage\n")

    t.append(side_by_side(
        "\\prob{8} In a new game, the token may also slide diagonally down and to the left, one "
        "or more squares. Color every square of this 8-by-8 board except the star: green if the "
        "first player can always win when the token starts there, red if the second player can "
        "always win.", queen_moves_picture(0.34), textw="4.7in", picw="1.9in", align="t"))
    t.append("\\vspace{0.3in}\n")
    t.append(centered(board(8, 0.6)))
    t.append("\\newpage\n")

    t.append("\\prob{9} In the game from Problem 8, mark all the red squares on this 20-by-20 "
             "board. Explain how you know you have found them all.\n\n\\vspace{0.2in}\n")
    t.append(centered(board(20, 0.3, line="0.5pt")))
    t.append(END)
    return "".join(t)


def compile_tex(name, tex):
    path = os.path.join(SRC, name + ".tex")
    with open(path, "w") as f:
        f.write(tex)
    for _ in range(2):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error",
                            "-output-directory", SRC, path], capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            raise SystemExit("compile failed: " + name)
    os.replace(os.path.join(SRC, name + ".pdf"), os.path.join(OUT, name + ".pdf"))
    log = open(os.path.join(SRC, name + ".log")).read()
    for key in ("Overfull", "Underfull \\vbox", "Float too large"):
        n = log.count(key)
        if n:
            print(f"{name}: {n} x {key}")


if __name__ == "__main__":
    compile_tex("k-1", k1())
    compile_tex("grades-2-3", g23())
    compile_tex("grades-4-5", g45())
    print("ok")
