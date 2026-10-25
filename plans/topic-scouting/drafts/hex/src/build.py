"""Build the three Hex student packets (K-1, 2-3, 4-5).

Run:  python3 build.py        (writes .tex files here, PDFs one level up)
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hexgeom as h  # noqa: E402

OUT = os.path.dirname(HERE)
WEEK = "Week NN"
TOPIC = "Hex"

TEXTWIDTH_MM = 190.5

# ------------------------------------------------------------------ boards

BIG = 24.0          # hexagon width (across flats) for play boards, mm
BIG_BAND = 8.0
BIG7 = 24.0         # 7 x 7 board on the landscape page (same hexagons as the others)
BAND7 = 5.0


def big_board(n, **kw):
    kw.setdefault('band', BIG_BAND)
    kw.setdefault('label_size', r"\small")
    return h.hex_board(n, BIG, **kw)


def centred(tikz):
    return "\n\\begin{center}\n" + tikz + "\n\\end{center}\n"


# Example finished game for the shared rules (6 x 6, a size no task uses).
EXAMPLE_RED = [(0, 2), (1, 2), (2, 1), (3, 1), (3, 2), (4, 2), (5, 1)]
EXAMPLE_BLUE = [(1, 1), (2, 2), (2, 3), (4, 1), (4, 3), (1, 4)]


def example_board():
    counters = {p: 'R' for p in EXAMPLE_RED}
    counters.update({p: 'B' for p in EXAMPLE_BLUE})
    return h.hex_board(6, 7.5, band=3.0, label_size=r"\tiny", counters=counters,
                       line_width=0.4, counter_scale=0.34)


# Puzzle positions for grades 2-3 (Blue to move; checked in check_puzzles.py)
PUZZLES = [
    # (red cells, blue cells)
    ([(0, 1), (1, 1), (2, 1)], [(3, 0), (0, 3)]),          # Blue wins only at (3,1)
    ([(0, 2), (1, 1), (3, 0)], [(1, 2), (2, 2)]),          # Red wins
    ([(1, 1), (2, 2)], [(0, 0)]),                          # Red wins
    ([(0, 0), (1, 1), (2, 2)], [(2, 3), (3, 2)]),          # Blue wins only at (2,1)
]


PUZZLE_BAND = 6.5


def puzzle_row(red, blue):
    """A 4 x 4 position at playing size, with a writing line beside it."""
    counters = {p: 'R' for p in red}
    counters.update({p: 'B' for p in blue})
    board = big_board(4, counters=counters, band=PUZZLE_BAND)
    return (r"\noindent\begin{minipage}[c]{150mm}" + board + r"\end{minipage}\hfill"
            r"\begin{minipage}[c]{36mm}\textcolor{writeline}{\rule{36mm}{0.6pt}}\end{minipage}\par" + "\n")


# Grades 2-3: fewest blue counters when Red already holds five hexagons
# (5 x 5; the answer is 6, checked in check_puzzles.py).
OBSTACLE_RED = [(0, 2), (1, 2), (2, 2), (3, 2), (4, 0)]

# Grades 4-5: Red to move; Red's only winning move is (1, 2).  With one extra
# red counter on any empty hexagon Red still wins (check_puzzles.py).
EXTRA_RED = [(1, 1), (3, 1)]
EXTRA_BLUE = [(0, 1), (2, 3)]


# Full boards for the boundary path (grades 4-5; checked in check_hex.py)
WALK_BOARDS = [
    ["BRBBR",
     "BRRRB",
     "RBBRB",
     "BRRBR",
     "BRBRB"],
    ["RRBRB",
     "BRRBR",
     "RBRBB",
     "BBRBR",
     "RBBRB"],
]


def walk_board(rows, w=16.0, n=None):
    """A board for the boundary path, with a star at the top-left corner.
    rows=None gives a blank n x n board for the child to color."""
    if rows is None:
        fills = {}
    else:
        n = len(rows)
        fills = {(r, c): rows[r][c] for r in range(n) for c in range(n)}
    tikz = h.hex_board(n, w, band=5.5, label_size=r"\scriptsize", fills=fills,
                       line_width=0.5)
    tl = h.corners(n, w)['TL']
    star = (rf"\node[star,star points=5,star point ratio=2.3,fill=black,draw=white,"
            rf"line width=0.3pt,inner sep=0pt,minimum size=5.2mm] at {h.fmt(tl)} {{}};")
    return tikz.replace(r"\end{tikzpicture}", star + "\n" + r"\end{tikzpicture}")


def lines(n, gap=10.0):
    return "\\par\\vspace{11mm}\\noindent" + h.writing_lines(TEXTWIDTH_MM - 1.0, n, gap) + "\\par\n"


# ------------------------------------------------------------------ document

PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage[letterpaper,top=0.8in,bottom=0.8in,left=0.5in,right=0.5in,
            headheight=15pt,headsep=0.25in,footskip=0.4in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric}
\usepackage{fancyhdr}
\usepackage{xcolor}
%(colours)s
\pagestyle{fancy}
\fancyhf{}
\lhead{%(header)s}
\lfoot{%(footer)s}
\rfoot{\thepage}
\renewcommand{\headrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\newcommand{\prob}[1]{\textbf{Problem #1:}}
\newsavebox{\landbox}
\begin{document}
%(textsize)s\raggedright
"""

END = r"""
\end{document}
"""


def landscape_page(header, footer, body_tex, pagenum_tex=r"\thepage"):
    """A page whose content is turned a quarter turn, displayed in landscape.

    The page stays US Letter portrait; the drawing is rotated and the PDF
    page gets /Rotate 90 so viewers show it the right way up.
    """
    return r"""
\clearpage
\sbox{\landbox}{\begin{minipage}{254mm}%s\end{minipage}}
\pdfpageattr{/Rotate 90}
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
\begin{scope}[shift={(current page.center)},rotate=90,transform shape]
\node[anchor=base west,inner sep=0pt] at (-127mm,94mm) {%s};
\node[anchor=base west,inner sep=0pt] at (-127mm,-97.8mm) {%s};
\node[anchor=base east,inner sep=0pt] at (127mm,-97.8mm) {%s};
\node[anchor=north,inner sep=0pt] at (0,87mm) {\usebox{\landbox}};
\end{scope}
\end{tikzpicture}
\mbox{}
\clearpage
\pdfpageattr{}
""" % (body_tex, header, footer, pagenum_tex)


RULES = (r"Red and Blue take turns putting a counter of their own color on an empty "
         r"hexagon. Red wins by joining the two red edges with a chain of red hexagons. "
         r"Blue wins by joining the two blue edges with a chain of blue hexagons. "
         r"Each hexagon in a chain shares a side with the next one.")


def rules_block(width="0.56"):
    return (r"\begin{minipage}[c]{%s\textwidth}\raggedright " % width + RULES + r"\end{minipage}\hfill"
            r"\begin{minipage}[c]{0.38\textwidth}\centering " + example_board() +
            r"\end{minipage}" + "\n\\par\\vspace{7mm}\n")


def document(header, footer, pages, textsize=""):
    tex = PREAMBLE % {
        'colours': h.COLOURS, 'header': header, 'footer': footer,
        'textsize': textsize,
    }
    tex += "\n\\clearpage\n".join(p for p in pages if not p.startswith("%LANDSCAPE"))
    for p in pages:
        if p.startswith("%LANDSCAPE"):
            tex += p[len("%LANDSCAPE"):]
    tex += END
    return tex


def header_for(level):
    return f"{WEEK} / {TOPIC} / Grades {level}"


def footer_for(pid):
    return f"Bellingham Math Circle / {WEEK} / {pid}"


# ------------------------------------------------------------------ K-1

def yes_no():
    return "\\par\\vspace{1mm}\\centerline{\\Large YES\\hspace{36mm}NO}\n"


def k1():
    header = header_for("K--1")
    footer = footer_for("HEX-K-v1")
    p = []
    # page 1
    p.append(rules_block() +
             r"\prob{1} Play Hex on this board. Take turns going first." +
             centred(big_board(3)))
    # page 2
    p.append(r"\prob{2} Can you put a red or a blue counter on every hexagon so that nobody wins?" +
             centred(big_board(3)) + r"\vspace{8mm}" + "\n\n" +
             r"\prob{3} Can you put a red or a blue counter on every hexagon so that Red and Blue both win?" +
             centred(big_board(3)))
    # page 3
    p.append(r"\prob{4} Play Hex on this bigger board." + centred(big_board(4)))
    # page 4
    p.append(r"\prob{5} Can you put a red or a blue counter on every hexagon so that nobody wins?" +
             centred(big_board(4)))
    # page 5
    p.append(r"\prob{6} Red puts the first counter on the star. Can Red always win, whatever Blue does? "
             r"Circle yes or no." +
             centred(big_board(3, stars=[(1, 1)])) + yes_no() + r"\vspace{6mm}" + "\n" +
             centred(big_board(3, stars=[(0, 0)])) + yes_no())
    # page 6
    p.append(r"\prob{7} Put some blue counters on each board, then fill every other hexagon with red counters. "
             r"Use as few blue counters as you can so that Red does not win." +
             centred(big_board(3)) + r"\vspace{4mm}" + "\n" + centred(big_board(4)))
    return document(header, footer, p, textsize=r"\large")


# ------------------------------------------------------------------ 2-3

def g23():
    header = header_for("2--3")
    footer = footer_for("HEX-23-v1")
    p = []
    # page 1
    p.append(rules_block() +
             r"\prob{1} Play Hex on this board. Take turns going first." +
             centred(big_board(5)))
    # page 2
    p.append(r"\prob{2} Can you put a red or a blue counter on every hexagon so that nobody wins? "
             r"Can you do it so that Red and Blue both win?" + centred(big_board(4)))
    # page 3
    p.append(r"\prob{3} On this board of squares, a chain is made of squares that each share a side with the next. "
             r"Put a red or a blue counter on every square so that nobody wins. "
             r"Why can't you do this on the hexagon board?" +
             centred(h.square_board(4, 24.0, band=BIG_BAND, label_size=r"\small")) + lines(5))
    # page 4
    p.append(r"\prob{4} Put blue counters on this board so that Red cannot win, "
             r"even when every other hexagon is red. Use as few blue counters as you can. "
             r"Explain why fewer blue counters will not work." +
             centred(big_board(5)) + lines(5))
    # page 5
    obstacle = {q: 'R' for q in OBSTACLE_RED}
    p.append(r"\prob{5} Red already has five counters on this board. Put blue counters on it so that "
             r"Red cannot win, even when every other hexagon is red. Use as few blue counters as you can." +
             centred(big_board(5, counters=obstacle)))
    # pages 6 and 7: four positions at playing size, two per page
    p.append(r"\prob{6} In each game, Red went first and now it is Blue's turn. "
             r"Can Blue stop Red from winning, however Red plays? "
             r"Write yes or no beside each game. If yes, mark the hexagon where Blue should play." +
             "\\par\\vspace{2mm}\n" + puzzle_row(*PUZZLES[0]) + "\\vspace{9mm}\n" + puzzle_row(*PUZZLES[1]))
    p.append(r"\prob{7} Answer the questions in Problem 6 for these two games." +
             "\\par\\vspace{2mm}\n" + puzzle_row(*PUZZLES[2]) + "\\vspace{9mm}\n" + puzzle_row(*PUZZLES[3]))
    # page 8
    p.append(r"\prob{8} Red goes first on this board. Find every hexagon where Red can put the first counter "
             r"and then be sure to win, however Blue plays. Put an X on those hexagons on the small board." +
             centred(big_board(3)) + r"\vspace{6mm}" +
             centred(h.hex_board(3, 13.0, band=4.0, label_size=r"\tiny", line_width=0.5)))
    return document(header, footer, p, textsize=r"\large")


# ------------------------------------------------------------------ 4-5

def g45():
    header = header_for("4--5")
    footer = footer_for("HEX-45-v1")
    p = []
    # page 1
    p.append(rules_block() +
             r"\prob{1} Play Hex on this board. Take turns going first." +
             centred(big_board(5)))
    # page 2
    p.append(r"\prob{2} Can you put a red or a blue counter on every hexagon so that nobody wins? "
             r"Can you do it so that Red and Blue both win?" + centred(big_board(5)))
    # page 3
    p.append(r"\prob{3} Red goes first on this board. Find every hexagon where Red can put the first counter "
             r"and then be sure to win, however Blue plays. Put an X on those hexagons on the small board." +
             r"\par\vspace{2mm}\begin{center}" + big_board(3) + r"\hspace{12mm}" +
             h.hex_board(3, 13.0, band=4.0, label_size=r"\tiny", line_width=0.5) +
             r"\end{center}")
    # page 4
    p.append(r"\prob{4} On this board of squares, a chain is made of squares that each share a side with the next. "
             r"Put a red or a blue counter on every square so that nobody wins. "
             r"Next, count squares that touch only at a corner as touching too. "
             r"Fill the board so that Red and Blue both win." +
             centred(h.square_board(4, 24.0, band=BIG_BAND, label_size=r"\small")) +
             r"\vspace{6mm}" + "\n\n" +
             r"\prob{5} Explain why Red and Blue can never both have a winning chain on the same hexagon board." +
             lines(5))
    # page 5
    p.append(r"\prob{6} On each board, start at the star and draw a path along the sides of the hexagons, "
             r"always with red on one side of the path and blue on the other. "
             r"The colored edges count as red and blue. Follow the path as far as it goes. Where does it end?" +
             centred(walk_board(WALK_BOARDS[0])) + r"\vspace{4mm}" + "\n" +
             centred(walk_board(WALK_BOARDS[1])))
    # page 6
    p.append(r"\prob{7} Color every hexagon on these boards red or blue, any way you like. "
             r"Then draw the path from the star on each board, as in Problem 6. "
             r"Can a path end anywhere other than the places where the paths in Problem 6 ended?" +
             r"\par\vspace{2mm}\begin{center}" + walk_board(None, n=3) + r"\hspace{10mm}" +
             walk_board(None, n=4) + r"\end{center}" + r"\vspace{8mm}" + "\n\n" +
             r"\prob{8} Explain why somebody always has a winning chain when every hexagon has a counter." +
             lines(6))
    # page 7
    extra = {q: 'R' for q in EXTRA_RED}
    extra.update({q: 'B' for q in EXTRA_BLUE})
    p.append(r"\prob{9} It is Red's turn in this game. Can Red make sure to win, however Blue plays? "
             r"Next, put one more red counter on any empty hexagon. It is still Red's turn. "
             r"Can Red still make sure to win? Can an extra red counter ever stop Red from winning?" +
             centred(big_board(4, counters=extra)) + lines(5))
    # page 8
    p.append(r"\prob{10} Hex players often use a board with 11 rows of 11 hexagons. "
             r"Nobody knows a sure way to win on it. Maya says she has a way to always win "
             r"on that board when she goes second, playing by the rules on page 1. "
             r"Explain why Maya must be wrong." + lines(14))
    # page 9 (landscape)
    land_body = (r"\large\prob{11} Play Hex on this board. Take turns going first.\par\vspace{3mm}"
                 r"\centering " + h.hex_board(7, BIG7, band=BAND7, label_size=r"\small"))
    p.append("%LANDSCAPE" + landscape_page(header, footer, land_body))
    return document(header, footer, p, textsize=r"\large")


# ------------------------------------------------------------------ build

def compile_tex(name, tex):
    path = os.path.join(HERE, name + ".tex")
    with open(path, "w") as f:
        f.write(tex)
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                            name + ".tex"], cwd=HERE, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            raise SystemExit(f"pdflatex failed for {name}")
    os.replace(os.path.join(HERE, name + ".pdf"), os.path.join(OUT, name + ".pdf"))
    for ext in (".aux", ".log"):
        try:
            os.remove(os.path.join(HERE, name + ext))
        except FileNotFoundError:
            pass
    print("built", os.path.join(OUT, name + ".pdf"))


if __name__ == "__main__":
    compile_tex("k-1", k1())
    compile_tex("grades-2-3", g23())
    compile_tex("grades-4-5", g45())
