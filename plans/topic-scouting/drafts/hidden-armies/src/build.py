#!/usr/bin/env python3
"""Build the three Hidden armies student packets (K-1, grades 2-3, grades 4-5).

Writes k-1.tex, grades-2-3.tex and grades-4-5.tex next to this file, compiles
them in ./build/, and copies the PDFs to the folder one level up.
Answers used by the pages are checked separately in check_answers.py.
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
BUILD = os.path.join(HERE, "build")

WEEK = "Week NN"
TOPIC = "Hidden armies"


# ---------------------------------------------------------------- preamble

def preamble(band_label, packet_id):
    return rf"""\documentclass[12pt]{{article}}
\usepackage[letterpaper,top=0.9in,bottom=0.85in,left=0.75in,right=0.75in,
  headheight=16pt,headsep=0.25in,footskip=0.45in]{{geometry}}
\usepackage[T1]{{fontenc}}
\usepackage{{tgheros}}
\renewcommand{{\familydefault}}{{\sfdefault}}
\usepackage{{tikz}}
\usetikzlibrary{{arrows.meta,calc}}
\usepackage{{fancyhdr}}
\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[L]{{{WEEK} / {TOPIC} / {band_label}}}
\fancyfoot[L]{{\small Bellingham Math Circle / {WEEK} / {packet_id}}}
\fancyfoot[R]{{\small \thepage}}
\renewcommand{{\headrulewidth}}{{0.4pt}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0pt}}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\newcommand{{\prob}}[1]{{\par\vspace{{16pt}}\noindent\textbf{{Problem #1:}}\ }}
\tikzset{{sbox/.style={{draw,line width=0.6pt,minimum width=#1,minimum height=0.5cm,
  inner sep=0pt,outer sep=0pt,font=\sffamily}},sbox/.default=0.56cm}}
% a plan strip written inline: cubes on hills 1, 2, 3
\newcommand{{\strip}}[4][0.56cm]{{\hspace{{1.5pt}}\tikz[baseline={{([yshift=-0.75ex]a.center)}}]{{%
  \node[sbox=#1] (a) {{#2}};\node[sbox=#1,anchor=west] (b) at (a.east) {{#3}};%
  \node[sbox=#1,anchor=west] (c) at (b.east) {{#4}};}}\hspace{{1.5pt}}}}
\begin{{document}}
\raggedright
"""


END = "\n\\end{document}\n"


# ---------------------------------------------------------------- drawing helpers

def f(v):
    return f"{v:.3f}"


def plan_cmds(x0, y0, vals, cube=0.45, gap=1.5, rx=0.6, ry=0.19, tokens=(),
              fill="black!25", numfont=r"\small\bfseries"):
    """Side view of a hill mat: hill i is centred at (x0 + i*gap, y0); towers of cubes stand on it."""
    c = []
    for i in range(3):
        x = x0 + i * gap
        c.append(rf"\draw[line width=0.8pt,fill=black!4] ({f(x)},{f(y0)}) ellipse ({rx} and {ry});")
        c.append(rf"\node[font={numfont}] at ({f(x)},{f(y0 - ry - 0.27)}) {{{i + 1}}};")
        n = vals[i] if vals else 0
        for k in range(n):
            c.append(rf"\draw[line width=0.6pt,fill={fill}] ({f(x - cube / 2)},{f(y0 + k * cube)}) "
                     rf"rectangle ({f(x + cube / 2)},{f(y0 + (k + 1) * cube)});")
        if i in tokens:
            c.append(rf"\fill ({f(x + cube / 2 + 0.2)},{f(y0 - 0.02)}) circle (0.14);")
    return c


def plan_pic(vals, height, **kw):
    """A stand-alone plan picture with a fixed bounding box (height above the hills in cm)."""
    gap = kw.get("gap", 1.5)
    rx = kw.get("rx", 0.6)
    ry = kw.get("ry", 0.19)
    c = [r"\begin{tikzpicture}",
         rf"\useasboundingbox ({f(-rx - 0.1)},{f(-ry - 0.55)}) rectangle ({f(2 * gap + rx + 0.1)},{f(height)});"]
    c += plan_cmds(0, 0, vals, **kw)
    c.append(r"\end{tikzpicture}")
    return "\n".join(c)


def strip_cmds(x, y, vals=None, w=0.85, h=0.72, font=r"\large", fill=None, labels=False):
    """A plan strip with lower-left corner (x, y). vals=None draws a blank strip."""
    c = []
    style = "line width=0.7pt" + (f",fill={fill}" if fill else "")
    for i in range(3):
        c.append(rf"\draw[{style}] ({f(x + i * w)},{f(y)}) rectangle ({f(x + (i + 1) * w)},{f(y + h)});")
        if vals is not None:
            c.append(rf"\node[font={font}] at ({f(x + (i + 0.5) * w)},{f(y + h / 2)}) {{{vals[i]}}};")
        if labels:
            c.append(rf"\node[font=\footnotesize\bfseries] at ({f(x + (i + 0.5) * w)},{f(y + h + 0.25)}) {{{i + 1}}};")
    return c


def lines(n, sep=0.85):
    """n light writing lines across the text width."""
    return (r"\par\noindent\begin{tikzpicture}" +
            "".join(rf"\draw[black!30,line width=0.5pt] (0,{f(-k * sep)}) -- (\linewidth-1pt,{f(-k * sep)});"
                    for k in range(1, n + 1)) +
            r"\end{tikzpicture}\par")


def tikz(cmds, opts=""):
    return "\\begin{tikzpicture}[" + opts + "]\n" + "\n".join(cmds) + "\n\\end{tikzpicture}"


def cube_icon_cmds(x, y, n, s=0.32):
    """n loose cubes in a row: a count shown as objects for children who do not read."""
    return [rf"\draw[line width=0.6pt,fill=black!25] ({f(x + k * (s + 0.1))},{f(y)}) rectangle "
            rf"({f(x + k * (s + 0.1) + s)},{f(y + s)});" for k in range(n)]


def circle_cmds(cx, cy, top_vals=None, dx=2.55, dy=1.35, w=0.85, h=0.72):
    """Three strips round a triangle with arrows top -> right -> left -> top, each labelled 'beats'."""
    c = []
    pos = {"t": (cx, cy + dy), "r": (cx + dx, cy - dy), "l": (cx - dx, cy - dy)}
    sw = 3 * w
    for key, (px, py) in pos.items():
        vals = top_vals if key == "t" else None
        c += strip_cmds(px - sw / 2, py - h / 2, vals, w=w, h=h)
    arrow = r"\draw[-{Stealth[length=3mm]},line width=0.9pt]"
    tx, ty = pos["t"]
    rxp, ryp = pos["r"]
    lxp, lyp = pos["l"]
    # top -> right
    c.append(rf"{arrow} ({f(tx + sw / 2 + 0.1)},{f(ty - 0.15)}) -- ({f(rxp + 0.25)},{f(ryp + h / 2 + 0.12)})"
             r" node[midway,above right=-1pt,font=\small\itshape] {beats};")
    # right -> left
    c.append(rf"{arrow} ({f(rxp - sw / 2 - 0.12)},{f(ryp)}) -- ({f(lxp + sw / 2 + 0.12)},{f(lyp)})"
             r" node[midway,below,font=\small\itshape] {beats};")
    # left -> top
    c.append(rf"{arrow} ({f(lxp - 0.25)},{f(lyp + h / 2 + 0.12)}) -- ({f(tx - sw / 2 - 0.1)},{f(ty - 0.15)})"
             r" node[midway,above left=-1pt,font=\small\itshape] {beats};")
    return c


def die_cmds(x, y, n, s=0.62):
    pips = {1: [(0.5, 0.5)], 2: [(0.25, 0.75), (0.75, 0.25)], 3: [(0.25, 0.75), (0.5, 0.5), (0.75, 0.25)],
            4: [(0.25, 0.25), (0.25, 0.75), (0.75, 0.25), (0.75, 0.75)],
            5: [(0.25, 0.25), (0.25, 0.75), (0.5, 0.5), (0.75, 0.25), (0.75, 0.75)],
            6: [(0.25, 0.2), (0.25, 0.5), (0.25, 0.8), (0.75, 0.2), (0.75, 0.5), (0.75, 0.8)]}
    c = [rf"\draw[line width=0.7pt,rounded corners=1.5pt] ({f(x)},{f(y)}) rectangle ({f(x + s)},{f(y + s)});"]
    for px, py in pips[n]:
        c.append(rf"\fill ({f(x + px * s)},{f(y + py * s)}) circle (0.055);")
    return c


def rules_picture_older():
    """Worked example of writing a plan: towers on the mat -> counts -> strip."""
    c = plan_cmds(0, 0, (3, 0, 2), cube=0.38, gap=1.25, rx=0.5, ry=0.16)
    c.append(r"\draw[-{Stealth[length=3mm]},line width=0.9pt] (3.25,0.55) -- (4.25,0.55);")
    c += strip_cmds(4.55, 0.19, (3, 0, 2), w=0.7, h=0.66, labels=True)
    return tikz(c)


RULES_OLDER = (
    "Both players have the same number of cubes. Behind your folder, put all your cubes on the "
    "three hills of your mat. This is your plan. A hill can stay empty. Lift the folders at the "
    "same time. On each hill, the player with more cubes wins the hill and puts a token on it. "
    "If the cubes are equal, nobody wins that hill. The player who wins more hills wins the game. "
    "If both players win the same number of hills, the game is a tie. "
    "A plan is written as three numbers in a strip: the cubes on hills 1, 2 and 3."
)


def rules_block_older():
    return (r"\begin{minipage}[c]{0.55\linewidth}\raggedright " + RULES_OLDER + r"\end{minipage}\hfill"
            r"\begin{minipage}[c]{0.42\linewidth}\centering" + rules_picture_older() + r"\end{minipage}" + "\n")


# ---------------------------------------------------------------- shared layouts for older bands

def game_record_grid(n_games=8, cols=2):
    """Pairs of blank strips, one pair per game, numbered in small grey."""
    c = []
    rows = (n_games + cols - 1) // cols
    sw = 3 * 0.85
    colw = 8.6
    for g in range(n_games):
        col, row = divmod(g, rows)
        x = col * colw
        y = -row * 1.25
        c.append(rf"\node[font=\small,text=black!55,anchor=east] at ({f(x + 0.35)},{f(y + 0.36)}) {{{g + 1}}};")
        c += strip_cmds(x + 0.5, y, None)
        c += strip_cmds(x + 0.5 + sw + 0.9, y, None)
    return tikz(c)


def test_record_table(n_rows=8, cols=2, head=("plan shown", "plan that beats it")):
    c = []
    rows = (n_rows + cols - 1) // cols
    sw = 3 * 0.85
    colw = 8.6
    for col in range(cols):
        x = col * colw
        c.append(rf"\node[font=\small,anchor=south] at ({f(x + 0.5 + sw / 2)},0.05) {{{head[0]}}};")
        c.append(rf"\node[font=\small,anchor=south] at ({f(x + 0.5 + sw + 0.9 + sw / 2)},0.05) {{{head[1]}}};")
        for r in range(rows):
            y = -0.85 - r * 1.15
            c += strip_cmds(x + 0.5, y, None)
            c += strip_cmds(x + 0.5 + sw + 0.9, y, None)
    return tikz(c)


def given_grid(groups, gw=0.6, gh=0.56, bw=0.85, bh=0.72, label_w=2.1, pair_w=5.4, row_h=1.15):
    """groups: list of (label, [plans]); two plan/answer pairs per row."""
    c = []
    y = 0.0
    for label, plist in groups:
        for i in range(0, len(plist), 2):
            if i == 0:
                c.append(rf"\node[anchor=west,font=\normalsize] at (0,{f(y + bh / 2)}) {{{label}}};")
            for j, p in enumerate(plist[i:i + 2]):
                big = max(p) >= 10
                w = 0.78 if big else gw
                x = label_w + j * (pair_w + 1.2)
                c += strip_cmds(x, y + (bh - gh) / 2, p, w=w, h=gh, font=r"\normalsize", fill="black!10")
                c += strip_cmds(x + 3 * 0.78 + 0.45, y, None, w=1.05 if big else bw, h=bh)
            y -= row_h
    return tikz(c)


def blank_strip_grid(n, per_row=5, gap_x=0.75, gap_y=0.45, w=0.85, h=0.72):
    c = []
    sw = 3 * w
    for k in range(n):
        r, col = divmod(k, per_row)
        c += strip_cmds(col * (sw + gap_x), -r * (h + gap_y), None, w=w, h=h)
    return tikz(c)


# ---------------------------------------------------------------- K-1 packet

def blank_cmds(x0, y0, height, **kw):
    """Empty hills for a child to draw a plan on, inside a light frame."""
    gap = kw.get("gap", 1.5)
    rx = kw.get("rx", 0.6)
    ry = kw.get("ry", 0.19)
    c = [rf"\draw[black!35,line width=0.6pt,rounded corners=5pt] ({f(x0 - rx - 0.25)},{f(y0 - ry - 0.62)}) "
         rf"rectangle ({f(x0 + 2 * gap + rx + 0.25)},{f(y0 + height)});"]
    return c + plan_cmds(x0, y0, None, **kw)


def k1():
    s = [preamble("Grades K--1", "HA-K-v1"), r"\large"]

    # Rules with the launch example: 1-0-4 against 2-3-0; tokens on the hills won.
    kw = dict(cube=0.5, gap=1.7, rx=0.66, ry=0.21)
    ex = []
    ex += plan_cmds(0, 3.35, (1, 0, 4), tokens=(2,), **kw)
    ex += plan_cmds(0, 0, (2, 3, 0), tokens=(0, 1), **kw)
    s.append(r"\begin{minipage}[c]{0.58\linewidth}\raggedright "
             "Both players have the same number of cubes. Behind your folder, put all your cubes on "
             "the three hills of your mat. This is your plan. A hill can stay empty. Lift the folders "
             "at the same time. On each hill, the player with more cubes wins the hill and puts a token "
             "on it. If the cubes are equal, nobody wins that hill. The player who wins more hills wins "
             "the game. If both players win the same number of hills, the game is a tie."
             r"\end{minipage}\hfill\begin{minipage}[c]{0.38\linewidth}\centering" + tikz(ex) +
             r"\end{minipage}")

    s.append(r"\prob{1}Play with 5 cubes each. In each new game, try to beat the plan your partner just used.")

    # Problem 2: is there a plan with 5 cubes that nobody can beat?  Pairs: plan shown / plan that beats it.
    kw = dict(cube=0.5, gap=1.5, rx=0.6, ry=0.19)
    xl, xr = 4.3, 11.3
    c = [rf"\node[font=\normalsize,anchor=south] at ({f(xl + 1.5)},3.05) {{plan shown}};",
         rf"\node[font=\normalsize,anchor=south] at ({f(xr + 1.5)},3.05) {{plan that beats it}};"]
    for r in range(3):
        y = -r * 4.15
        c += cube_icon_cmds(0, y + 0.95, 5, s=0.38)
        c += blank_cmds(xl, y, 2.9, **kw)
        c += blank_cmds(xr, y, 2.9, **kw)
    s.append(r"\prob{2}Your partner can see your plan and tries to beat it. "
             r"Is there a plan with 5 cubes that nobody can beat?")
    s.append(r"\par\vspace{10pt}\noindent" + tikz(c))

    # Problem 3: one beating plan for each given plan.
    s.append(r"\newpage")
    s.append(r"\prob{3}For each plan below, draw a plan with 5 cubes that beats it.")
    kw3 = dict(cube=0.55, gap=1.8, rx=0.7, ry=0.22)
    c = []
    for r, p in enumerate([(5, 0, 0), (0, 4, 1), (0, 3, 2), (2, 1, 2)]):
        y = -r * 4.75
        c += plan_cmds(1.2, y, p, **kw3)
        c += blank_cmds(10.6, y, 3.4, **kw3)
    s.append(r"\par\vspace{12pt}\noindent" + tikz(c))

    # Problem 4: small numbers of cubes, one board for each number.
    s.append(r"\newpage")
    s.append(r"\prob{4}Is there a plan that nobody can beat when each player has 2 cubes? 3 cubes? 4 cubes?")
    kw4 = dict(cube=0.55, gap=1.8, rx=0.7, ry=0.22)
    c = []
    for r, n in enumerate([2, 3, 4]):
        y = -r * 4.75
        c += cube_icon_cmds(1.0, y + 1.1, n, s=0.42)
        c += blank_cmds(6.2, y, 3.4, **kw4)
    s.append(r"\par\vspace{12pt}\noindent" + tikz(c))

    # Problem 5: two groups of three plans; one has a best plan, one is a circle.
    # Each plan keeps its own column, so each box visibly holds three plans, each met twice.
    s.append(r"\newpage")
    s.append(r"\prob{5}Build the two plans in each row and circle the winner. "
             r"In each box, is one plan the best?")
    groups = [
        ((4, 1, 0), (2, 2, 1), (0, 0, 5)),
        ((0, 1, 4), (2, 0, 3), (1, 2, 2)),
    ]
    games = [(0, 1), (1, 2), (0, 2)]
    kw = dict(cube=0.42, gap=1.55, rx=0.6, ry=0.19)
    colx = [1.55, 7.25, 12.95]
    c = []
    y = 0.0
    for plans3 in groups:
        top = y + 2.45
        for a, b in games:
            c += plan_cmds(colx[a], y, plans3[a], **kw)
            c += plan_cmds(colx[b], y, plans3[b], **kw)
            y -= 3.05
        bottom = y + 3.05 - 0.85
        c.append(rf"\draw[black!45,line width=0.8pt,rounded corners=6pt] (0.3,{f(bottom)}) rectangle (17.3,{f(top)});")
        y -= 0.75
    s.append(r"\par\vspace{12pt}\noindent" + tikz(c))

    # Problem 6: fewest cubes.
    s.append(r"\newpage")
    s.append(r"\prob{6}You may use any number of cubes. "
             r"For each plan below, draw a plan that beats it with as few cubes as you can.")
    kw = dict(cube=0.5, gap=1.8, rx=0.7, ry=0.22)
    c = []
    for r, p in enumerate([(5, 0, 0), (1, 4, 0), (1, 3, 1), (2, 2, 1), (1, 1, 1)]):
        y = -r * 4.15
        c += plan_cmds(1.2, y, p, **kw)
        c += blank_cmds(10.6, y, 3.0, **kw)
    s.append(r"\par\vspace{12pt}\noindent" + tikz(c))

    # Problem 7: every plan that beats a given plan.  3-1-1 has 3 beaters (4 boards),
    # 4-0-1 has 6 beaters (8 boards).  Three columns of full-size boards.
    s.append(r"\newpage")
    s.append(r"\prob{7}For each plan below, find every plan with 5 cubes that beats it.")
    kwb = dict(cube=0.5, gap=1.8, rx=0.7, ry=0.22)
    colx = [0.95, 6.85, 12.75]
    pitch = 4.15
    c = []
    y = 0.0
    # 3-1-1: given plan, then 2 + 2 boards
    c += plan_cmds(colx[0], y, (3, 1, 1), **kwb)
    for (r, col) in [(0, 1), (0, 2), (1, 1), (1, 2)]:
        c += blank_cmds(colx[col], y - r * pitch, 3.0, **kwb)
    y -= 2 * pitch + 0.5
    c.append(rf"\draw[black!45,line width=0.8pt] (0,{f(y + 3.4)}) -- (17.3,{f(y + 3.4)});")
    # 4-0-1: given plan, then 2 + 3 + 3 boards
    c += plan_cmds(colx[0], y, (4, 0, 1), **kwb)
    for (r, col) in [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]:
        c += blank_cmds(colx[col], y - r * pitch, 3.0, **kwb)
    s.append(r"\par\vspace{12pt}\noindent" + tikz(c))

    s.append(END)
    return "\n".join(s)


# ---------------------------------------------------------------- grades 2-3 packet

def target_and_grid(target, n, per_row, gap_x=0.7, gap_y=0.45, w=0.85, h=0.72, x_grid=3.2):
    """A given plan (grey) at the left, then a grid of blank strips."""
    c = strip_cmds(0, 0, target, w=0.62, h=0.58, font=r"\normalsize", fill="black!10")
    sw = 3 * w
    for k in range(n):
        r, col = divmod(k, per_row)
        c += strip_cmds(x_grid + col * (sw + gap_x), (0.58 - h) / 2 - r * (h + gap_y), None, w=w, h=h)
    return tikz(c)


def g23():
    s = [preamble("Grades 2--3", "HA-23-v1")]
    s.append(rules_block_older())

    s.append(r"\prob{1}Play the game with 6 cubes each. For each game, write both plans and circle the plan "
             r"that won, if one did.")
    s.append(r"\par\vspace{10pt}\noindent\hspace*{0.3cm}" + game_record_grid(8))

    s.append(r"\prob{2}Is there a plan with 6 cubes that nobody can beat? Take turns: one player shows a "
             r"plan, and the other tries to beat it.")
    s.append(r"\par\vspace{12pt}\noindent\hspace*{0.3cm}" + test_record_table(10))

    s.append(r"\newpage")
    s.append(r"\prob{3}Beat each plan below. "
             r"Then explain how you can beat any plan with 6 or more cubes that your partner names.")
    s.append(r"\par\vspace{12pt}\noindent" + given_grid([
        ("6 cubes", [(2, 2, 2), (1, 4, 1), (3, 0, 3), (0, 1, 5)]),
        ("7 cubes", [(3, 2, 2), (1, 1, 5)]),
        ("10 cubes", [(4, 4, 2), (2, 5, 3)]),
        ("20 cubes", [(7, 7, 6)]),
    ], label_w=2.4))
    s.append(r"\par\vspace{10pt}" + lines(5))

    s.append(r"\prob{4}Each player has 3 cubes. Find a plan that nobody can beat, and explain why "
             r"nobody can beat it. Is there a plan like that when each player has 4 cubes?")
    s.append(r"\par\vspace{2pt}" + lines(7))

    s.append(r"\newpage")
    s.append(r"\prob{5}Find three plans with 6 cubes so that each plan beats the next one around the circle. "
             r"Then make a circle like this with \strip{2}{2}{2} in it, and one with \strip{6}{0}{0} in it. "
             r"If you cannot, explain why.")
    c = []
    c += circle_cmds(4.1, 0, None)
    c += circle_cmds(13.3, 0, None)
    c += circle_cmds(4.1, -4.6, (2, 2, 2))
    c += circle_cmds(13.3, -4.6, (6, 0, 0))
    s.append(r"\par\vspace{16pt}\noindent" + tikz(c))
    s.append(r"\par\vspace{6pt}" + lines(6))

    s.append(r"\newpage")
    s.append(r"\prob{6}Find every plan with 6 cubes that beats \strip{2}{2}{2}, and explain how you know "
             r"there are no others. Then find every plan with 6 cubes that beats \strip{6}{0}{0}.")
    s.append(r"\par\vspace{14pt}\noindent" + target_and_grid((2, 2, 2), 6, per_row=3))
    s.append(r"\par\vspace{2pt}" + lines(4))
    s.append(r"\par\vspace{20pt}\noindent" + target_and_grid((6, 0, 0), 20, per_row=4))

    s.append(r"\newpage")
    s.append(r"\prob{7}Now the two players may have different numbers of cubes. Beat each plan below with "
             r"as few cubes as you can. Then find a quick way to tell how many cubes you need to beat any plan.")
    s.append(r"\par\vspace{12pt}\noindent" + given_grid([
        ("6 cubes", [(6, 0, 0), (4, 1, 1), (3, 2, 1), (2, 2, 2), (3, 3, 0)]),
        ("3 cubes", [(1, 1, 1)]),
        ("10 cubes", [(8, 1, 1), (5, 3, 2)]),
    ], label_w=2.4))
    s.append(r"\par\vspace{10pt}" + lines(8))

    s.append(END)
    return "\n".join(s)


# ---------------------------------------------------------------- grades 4-5 packet

def ranking_table():
    """All 28 plans with 6 cubes, one row for each number on hill 1, each with a circle below for a count."""
    c = []
    w, h = 0.56, 0.52
    cellw = 2.5
    for i in range(7):
        first = 6 - i
        y = -i * 1.85
        for j in range(i + 1):
            second = i - j
            third = j
            x = 0.1 + j * cellw
            c += strip_cmds(x, y, (first, second, third), w=w, h=h, font=r"\normalsize")
            c.append(rf"\draw[line width=0.6pt] ({f(x + 1.5 * w)},{f(y - 0.6)}) circle (0.44);")
    return tikz(c)


def g45():
    s = [preamble("Grades 4--5", "HA-45-v1")]
    s.append(rules_block_older())

    s.append(r"\prob{1}Play the game with 6 cubes each. Is there a plan that nobody can beat? "
             r"To test a plan, one player shows it and the others try to beat it.")
    s.append(r"\par\vspace{12pt}\noindent\hspace*{0.3cm}" + test_record_table(14))

    s.append(r"\newpage")
    s.append(r"\prob{2}Beat each plan below. "
             r"Then explain a way to beat any plan with 6 or more cubes that your partner names.")
    s.append(r"\par\vspace{12pt}\noindent" + given_grid([
        ("6 cubes", [(2, 2, 2), (1, 4, 1)]),
        ("7 cubes", [(3, 2, 2), (1, 1, 5)]),
        ("9 cubes", [(3, 3, 3)]),
        ("10 cubes", [(1, 8, 1)]),
        ("20 cubes", [(7, 7, 6)]),
        ("100 cubes", [(34, 33, 33), (50, 0, 50)]),
    ], label_w=2.4, row_h=1.1))
    s.append(r"\par\vspace{10pt}" + lines(6))
    s.append(r"\prob{3}For which numbers of cubes is there a plan that nobody can beat? Explain.")
    s.append(r"\par\vspace{2pt}" + lines(8))

    s.append(r"\newpage")
    s.append(r"\prob{4}There are 28 plans with 6 cubes. For each one, find how many of the 28 plans it beats. "
             r"Share the work. Which plans beat the most? Which beat the fewest?")
    s.append(r"\par\vspace{16pt}\noindent" + ranking_table())
    s.append(r"\par\vspace{12pt}" + lines(5))

    s.append(r"\newpage")
    s.append(r"\prob{5}Find three plans with 6 cubes so that each plan beats the next one around the circle. "
             r"Which plans with 6 cubes can be part of a circle like this, and which cannot? Explain why.")
    c = []
    c += circle_cmds(4.1, 0, None)
    c += circle_cmds(13.3, 0, None)
    c += circle_cmds(4.1, -4.6, None)
    c += circle_cmds(13.3, -4.6, None)
    s.append(r"\par\vspace{16pt}\noindent" + tikz(c))
    s.append(r"\par\vspace{6pt}" + lines(7))

    s.append(r"\newpage")
    s.append(r"\prob{6}Now the two players may have different numbers of cubes. What is the fewest cubes "
             r"that can beat each plan below? Find a rule that works for any plan, and explain why it works.")
    s.append(r"\par\vspace{12pt}\noindent" + given_grid([
        ("6 cubes", [(6, 0, 0), (4, 1, 1), (3, 2, 1), (2, 2, 2)]),
        ("3 cubes", [(1, 1, 1)]),
        ("100 cubes", [(40, 30, 30)]),
    ], label_w=2.4))
    s.append(r"\par\vspace{10pt}" + lines(5))
    s.append(r"\prob{7}Your partner has 6 cubes. What is the fewest cubes you need for a plan that your "
             r"partner cannot beat? For a plan that beats every plan your partner could make?")
    s.append(r"\par\vspace{2pt}" + lines(7))

    s.append(r"\newpage")
    s.append(r"\prob{8}Ben and Mia each choose a plan with 6 cubes by rolling a die and using the list below. "
             r"You know their lists but not their rolls. For each of them, look for a plan with 6 cubes that "
             r"beats more of their six plans than it loses to. If there is none, explain why.")
    ben = [(3, 2, 1), (3, 1, 2), (2, 3, 1), (2, 1, 3), (1, 3, 2), (1, 2, 3)]
    mia = [(4, 2, 0), (4, 0, 2), (2, 4, 0), (2, 0, 4), (0, 4, 2), (0, 2, 4)]
    c = [r"\node[font=\normalsize\bfseries] at (2.77,0.85) {Ben};",
         r"\node[font=\normalsize\bfseries] at (6.27,0.85) {Mia};"]
    for k in range(6):
        y = -0.25 - k * 0.95
        c += die_cmds(0, y, k + 1)
        c += strip_cmds(1.9, y, ben[k], w=0.58, h=0.62, font=r"\normalsize")
        c += strip_cmds(5.4, y, mia[k], w=0.58, h=0.62, font=r"\normalsize")
    s.append(r"\par\vspace{14pt}\noindent\hspace*{0.5cm}" + tikz(c))
    s.append(r"\par\vspace{6pt}" + lines(10))

    s.append(END)
    return "\n".join(s)


# ---------------------------------------------------------------- build

def compile_tex(name, text):
    os.makedirs(BUILD, exist_ok=True)
    tex = os.path.join(HERE, name + ".tex")
    with open(tex, "w") as fh:
        fh.write(text)
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                            "-output-directory", BUILD, tex], capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            sys.exit(f"pdflatex failed for {name}")
    log = open(os.path.join(BUILD, name + ".log")).read()
    for warn in ("Overfull", "Underfull \\vbox", "LaTeX Warning"):
        if warn in log:
            print(f"  note: {name}.log contains '{warn}'")
    shutil.copy(os.path.join(BUILD, name + ".pdf"), os.path.join(OUT, name + ".pdf"))
    print("built", os.path.join(OUT, name + ".pdf"))


if __name__ == "__main__":
    compile_tex("k-1", k1())
    compile_tex("grades-2-3", g23())
    compile_tex("grades-4-5", g45())
