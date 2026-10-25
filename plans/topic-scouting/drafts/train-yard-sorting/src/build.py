#!/usr/bin/env python3
"""Build the three train-yard sorting packets and the track mat.

Writes k-1.tex, grades-2-3.tex, grades-4-5.tex and track-mat.tex next to
this script, compiles them with pdflatex, and copies the PDFs to the parent
folder (draft/ when run from draft/src, final/ when run from final/src).

The track mat is a full-size landscape print (one per pair, plus one extra
for the 4-5 table's two-siding problem). Its siding is 29 mm wide and five
29 mm places long, for 25 mm card squares or 2 cm cubes. The fit has not
been rehearsed with the real cars.

Usage: python3 build.py
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
BUILD = os.path.join(HERE, 'build')

WEEK = 'Week NN'
TOPIC = 'Train-yard sorting'

CHECK = r'\ding{51}'
CROSS = r'\ding{55}'


# ---------------------------------------------------------------------------
# TikZ helpers (all lengths in mm)
# ---------------------------------------------------------------------------

def fmt(v):
    return f'{v:.2f}'.rstrip('0').rstrip('.')


def car(x, y, s, label='', font=r'\bfseries', dashed=False):
    style = 'dashed, line width=0.5pt' if dashed else 'line width=0.9pt, fill=white'
    out = [rf'\draw[{style}, rounded corners=0.6mm] ({fmt(x)},{fmt(y)}) '
           rf'rectangle ({fmt(x + s)},{fmt(y + s)});']
    if label != '':
        out.append(rf'\node at ({fmt(x + s / 2)},{fmt(y + s / 2)}) {{{font} {label}}};')
    return '\n'.join(out)


def box(x, y, s):
    return (rf'\draw[line width=0.6pt] ({fmt(x)},{fmt(y)}) '
            rf'rectangle ({fmt(x + s)},{fmt(y + s)});')


def train_at(x, y, cars, s, font, gap=1.0):
    """cars: list of labels; '' gives an empty car to fill in."""
    out = []
    for i, c in enumerate(cars):
        out.append(car(x + i * (s + gap), y, s, c, font))
    return '\n'.join(out), len(cars) * (s + gap) - gap


def train_grid(trains, cols, s, font, colw, rowh, with_box=True, boxs=None,
               align_boxes=False):
    """A grid of trains, each optionally followed by a check box.

    align_boxes puts every check box of a column at the same x, after the
    longest train in the grid."""
    boxs = boxs or 0.8 * s
    longest = max(len(t) for t in trains)
    wmax = longest * (s + 1.0) - 1.0
    out = [r'\begin{tikzpicture}[x=1mm,y=1mm]']
    for k, t in enumerate(trains):
        r, c = divmod(k, cols)
        x, y = c * colw, -r * rowh
        code, w = train_at(x, y, t, s, font)
        out.append(code)
        if with_box:
            bw = wmax if align_boxes else w
            out.append(box(x + bw + 0.55 * s, y + (s - boxs) / 2, boxs))
    out.append(r'\end{tikzpicture}')
    return '\n'.join(out)


def mat_panel(dep, siding, arr, u, ndep=3, narr=3, labels=False,
              arrows=False, font=r'\bfseries\small'):
    """Schematic of the track mat.

    dep: departed cars, first departed first (drawn leftmost).
    siding: cars in the siding, bottom first.
    arr: cars still to arrive, front car first (next to the junction).
    """
    L = 5  # siding length in cars
    out = []
    x0, x1 = -ndep * u, (narr + 1) * u
    # main line bed
    out.append(rf'\fill[black!8] ({fmt(x0)},0) rectangle ({fmt(x1)},{fmt(u)});')
    out.append(rf'\fill[black!8] (0,{fmt(-L * u)}) rectangle ({fmt(u)},0);')
    # rails of the main line
    out.append(rf'\draw[black!45, line width=0.5pt] ({fmt(x0)},{fmt(u)}) -- ({fmt(x1)},{fmt(u)});')
    out.append(rf'\draw[black!45, line width=0.5pt] ({fmt(x0)},0) -- (0,0);')
    out.append(rf'\draw[black!45, line width=0.5pt] ({fmt(u)},0) -- ({fmt(x1)},0);')
    # siding walls
    out.append(rf'\draw[line width=1.6pt] (0,0) -- (0,{fmt(-L * u)}) -- ({fmt(u)},{fmt(-L * u)}) -- ({fmt(u)},0);')
    pad = 0.08 * u
    s = u - 2 * pad
    n_total = len(dep)
    for k, c in enumerate(dep):
        cell = -ndep + k
        out.append(car(cell * u + pad, pad, s, c, font))
    for k, c in enumerate(siding):
        out.append(car(pad, -L * u + k * u + pad, s, c, font))
    for k, c in enumerate(arr):
        out.append(car((k + 1) * u + pad, pad, s, c, font))
    if labels:
        out.append(rf'\node[font=\footnotesize, below left, inner xsep=1pt] at (-0.8,-0.4) {{departure track}};')
        out.append(rf'\node[font=\footnotesize, below right, inner xsep=1pt] at ({fmt(u + 0.8)},-0.4) {{arrival track}};')
        out.append(rf'\node[font=\footnotesize, right] at ({fmt(u + 0.6)},{fmt(-L * u / 2 - u)}) {{siding}};')
    if arrows:
        h = u + 0.55 * u
        a = r'-{Stealth[length=1.6mm]}, line width=0.7pt, black!70, rounded corners=1.2mm'
        out.append(rf'\draw[{a}] ({fmt(x1 - 0.4 * u)},{fmt(h)}) -- ({fmt(0.68 * u)},{fmt(h)}) -- ({fmt(0.68 * u)},{fmt(-1.3 * u)});')
        out.append(rf'\draw[{a}] ({fmt(0.32 * u)},{fmt(-1.3 * u)}) -- ({fmt(0.32 * u)},{fmt(h)}) -- ({fmt(x0 + 0.4 * u)},{fmt(h)});')
    return '\n'.join(out)


def rules_picture(u=7.0, font=r'\bfseries\small'):
    """Three stages of the launch train 1 3 2."""
    w = 7 * u
    gap = 11
    out = [r'\begin{tikzpicture}[x=1mm,y=1mm]']
    stages = [([], [], ['1', '3', '2'], True),
              (['1'], ['3'], ['2'], False),
              (['1', '2', '3'], [], [], False)]
    for i, (d, sd, a, first) in enumerate(stages):
        dx = i * (w + gap) + 3 * u
        out.append(rf'\begin{{scope}}[shift={{({fmt(dx)},0)}}]')
        out.append(mat_panel(d, sd, a, u, labels=first, arrows=first, font=font))
        out.append(r'\end{scope}')
        if i < 2:
            xa = dx + 4 * u + gap / 2
            out.append(rf'\draw[-{{Stealth[length=2mm]}}, line width=0.9pt] '
                       rf'({fmt(xa - 4)},{fmt(-1.5 * u)}) -- ({fmt(xa + 4)},{fmt(-1.5 * u)});')
    out.append(r'\end{tikzpicture}')
    return '\n'.join(out)


def path_grid(x, y, n, step, word=None, dots=True, line='line width=1.4pt'):
    """Lattice for paths of n ups and n downs; optional drawn path."""
    out = []
    W, H = 2 * n, n
    if dots:
        for i in range(W + 1):
            for j in range(H + 1):
                if (i + j) % 2 == 0:
                    out.append(rf'\fill[black!65] ({fmt(x + i * step)},{fmt(y + j * step)}) circle (0.55);')
    out.append(rf'\draw[black!55, line width=0.6pt] ({fmt(x)},{fmt(y)}) -- ({fmt(x + W * step)},{fmt(y)});')
    if word:
        pts = [(0, 0)]
        for ch in word:
            i, j = pts[-1]
            pts.append((i + 1, j + (1 if ch == 'U' else -1)))
        coords = ' -- '.join(f'({fmt(x + i * step)},{fmt(y + j * step)})' for i, j in pts)
        out.append(rf'\draw[{line}, line join=round, line cap=round] {coords};')
    return '\n'.join(out)


def answer_lines(n, gap=9):
    return (r'\par\vspace{3pt}\noindent\begin{tikzpicture}[x=1mm,y=1mm]' + '\n' +
            '\n'.join(rf'\draw[black!30, line width=0.4pt] (0,{fmt(-k * gap)}) -- ({fmt(177)},{fmt(-k * gap)});'
                      for k in range(1, n + 1)) +
            '\n' + r'\end{tikzpicture}\par')


# ---------------------------------------------------------------------------
# Document frame
# ---------------------------------------------------------------------------

def preamble(level, packet, size):
    cls = 'extarticle' if size == '14pt' else 'article'
    return rf"""\documentclass[{size},letterpaper]{{{cls}}}
\usepackage[T1]{{fontenc}}
\usepackage{{tgheros}}
\renewcommand{{\familydefault}}{{\sfdefault}}
\usepackage[letterpaper, left=0.75in, right=0.75in, top=0.85in, bottom=0.85in,
  headheight=16pt, headsep=14pt, footskip=26pt]{{geometry}}
\usepackage{{fancyhdr}}
\usepackage{{pifont}}
\usepackage{{tikz}}
\usetikzlibrary{{arrows.meta}}
\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[L]{{{WEEK} / {TOPIC} / {level}}}
\fancyfoot[L]{{\small Bellingham Math Circle / {WEEK} / {packet}}}
\fancyfoot[R]{{\small \thepage}}
\renewcommand{{\headrulewidth}}{{0.4pt}}
\renewcommand{{\footrulewidth}}{{0pt}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{4pt}}
\newcommand{{\problem}}[1]{{\par\vspace{{14pt}}\noindent\textbf{{Problem #1:}} }}
\newcommand{{\yes}}{{{CHECK}}}
\newcommand{{\no}}{{{CROSS}}}
\begin{{document}}
"""


END = r'\end{document}' + '\n'


def centered(tikz, before=6, after=0):
    return rf'\par\vspace{{{before}pt}}\begin{{center}}' + '\n' + tikz + '\n' + r'\end{center}' + \
        (rf'\vspace{{{after}pt}}' if after else '') + '\n'


def split(s):
    return s.split()


# ---------------------------------------------------------------------------
# K-1
# ---------------------------------------------------------------------------

def build_k1():
    big = r'\bfseries\Large'
    doc = [preamble('Grades K–1', 'TY-K-v1', '14pt')]
    doc.append(r"""Line up a train on the arrival track the way it is drawn. The car on the left goes first, and cars never jump over each other. Each car drives down into the siding and then out to the departure track. Only the top car in the siding can drive out. Car 1 must leave first, then car 2, then car 3, and so on.
""")
    doc.append(centered(rules_picture(u=7.0), before=2))

    p1 = [split(t) for t in ['1 2 3', '1 3 2', '2 1 3', '2 3 1', '3 1 2', '3 2 1']]
    doc.append(r'\problem{1}Which of these trains can leave 1, 2, 3? Mark each one \yes{} or \no, and show with the cars why each \no{} train gets stuck.')
    doc.append(centered(train_grid(p1, 2, 15, big, colw=88, rowh=24), before=8))

    doc.append(r'\newpage')
    p2 = [split(t) for t in ['2 1 4 3', '3 4 1 2', '4 3 2 1', '1 4 3 2',
                              '4 2 3 1', '3 1 2 4', '4 1 3 2', '1 3 4 2']]
    doc.append(r'\problem{2}Which of these trains can leave 1, 2, 3, 4? Mark each one \yes{} or \no.')
    doc.append(centered(train_grid(p2, 2, 14, big, colw=88, rowh=26), before=8))

    doc.append(r'\newpage')
    p3 = [['', '', '', '1'] for _ in range(6)]
    doc.append(r'\problem{3}Car 1 is last in each of these trains. Fill in cars 2, 3, 4 in different ways, and find every train that can leave 1, 2, 3, 4.')
    doc.append(centered(train_grid(p3, 2, 14, big, colw=88, rowh=27), before=8))

    doc.append(r'\newpage')
    p4 = [split(t) for t in ['4 5 1 2 3', '2 1 5 4 3', '5 4 3 2 1',
                              '5 1 3 2 4', '1 3 5 2 4', '3 2 5 1 4']]
    doc.append(r'\problem{4}Which of these trains can leave 1, 2, 3, 4, 5? Mark each one \yes{} or \no.')
    doc.append(centered(train_grid(p4, 2, 12, big, colw=95, rowh=24), before=8))
    doc.append(r'\vspace{6pt}')
    doc.append(r'\problem{5}One partner lines up all five cars, and the other partner guesses whether they can leave 1, 2, 3, 4, 5. Drive them to check, then switch jobs.')

    doc.append(r'\newpage')
    p6 = [['', '', '', ''] for _ in range(10)]
    doc.append(r'\problem{6}Find all 10 trains of cars 1, 2, 3, 4 that cannot leave 1, 2, 3, 4.')
    doc.append(centered(train_grid(p6, 2, 14, big, colw=88, rowh=26, with_box=False), before=8))
    doc.append(END)
    return '\n'.join(doc)


# ---------------------------------------------------------------------------
# Grades 2-3
# ---------------------------------------------------------------------------

RULES_UPPER = r"""Put a train on the arrival track exactly as it is drawn, so the car on the left arrives first. Each move sends the front car of the arrival track down into the siding, or sends the top car of the siding out to the departure track. Cars slide along the table and never jump over each other. A car in the siding cannot go back to the arrival track. A train can \emph{leave in order} if its cars can reach the departure track in the order 1, 2, 3, and so on."""


def insertion_row(x, y, cars, s, slot, font, gap=1.2):
    out = []
    cx = x
    for k in range(len(cars) + 1):
        out.append(car(cx, y + (s - slot) / 2, slot, '', dashed=True))
        cx += slot + gap
        if k < len(cars):
            out.append(car(cx, y, s, cars[k], font))
            cx += s + gap
    return '\n'.join(out)


def build_g23():
    f = r'\bfseries\large'
    doc = [preamble('Grades 2–3', 'TY-23-v1', '12pt')]
    doc.append(RULES_UPPER + '\n')
    doc.append(centered(rules_picture(u=7.0), before=2))

    p1 = [['', '', ''] for _ in range(6)]
    doc.append(r'\problem{1}Write every different train you can make with cars 1, 2, 3. Mark each one \yes{} if it can leave in order and \no{} if it cannot.')
    doc.append(centered(train_grid(p1, 3, 10, f, colw=62, rowh=18), before=8))

    doc.append(r'\newpage')
    doc.append(r'\problem{2}Cars 1, 2, 3, 4 can be lined up as 24 different trains. With the other pair at your table, write each of these trains on a card, drive it, and sort the cards into a pile of trains that can leave in order and a pile of trains that cannot. How many cards are in each pile?')
    doc.append(r'\par\vspace{14pt}\hspace*{1.5em}Can leave in order: \rule{2.2cm}{0.5pt}\hspace{3em}Cannot: \rule{2.2cm}{0.5pt}')
    p3 = [split(t) for t in ['3 2 1 5 4', '4 1 3 2 5', '2 4 3 5 1', '1 2 5 3 4',
                              '4 5 3 2 1', '3 1 5 4 2', '5 2 1 4 3', '1 5 3 4 2']]
    doc.append(r'\vspace{18pt}')
    doc.append(r'\problem{3}Which of these trains can leave in order? Mark each one \yes{} or \no.')
    doc.append(centered(train_grid(p3, 2, 11, f, colw=86, rowh=21), before=8))

    doc.append(r'\newpage')
    doc.append(r'\problem{4}What makes a train impossible? Write a way to tell, without driving the cars, whether a train can leave in order.')
    doc.append(answer_lines(8))
    p5 = [split(t) for t in ['4 2 5 1 3', '1 4 2 3 5', '3 4 5 2 1',
                              '5 3 4 1 2', '5 4 1 3 2', '2 1 5 3 4']]
    doc.append(r'\vspace{10pt}')
    doc.append(r'\problem{5}Decide without driving which of these trains can leave in order, and mark each one \yes{} or \no. Then drive them to check.')
    doc.append(centered(train_grid(p5, 2, 11, f, colw=86, rowh=21), before=8))

    doc.append(r'\newpage')
    doc.append(r'\problem{6}Each of these trains can leave in order. Write 5 in every dashed box where car 5 could join the train so that it still leaves in order. How can you tell where car 5 can go?')
    rows = [split(t) for t in ['2 1 4 3', '4 3 2 1', '1 3 2 4', '3 1 2 4']]
    code = [r'\begin{tikzpicture}[x=1mm,y=1mm]']
    for k, t in enumerate(rows):
        code.append(insertion_row(0, -k * 21, t, 10, 8, f))
    code.append(r'\end{tikzpicture}')
    doc.append(centered('\n'.join(code), before=10))
    doc.append(answer_lines(4))
    doc.append(r'\vspace{2pt}')
    doc.append(r'\problem{7}How many of the 120 trains with cars 1, 2, 3, 4, 5 can leave in order? Explain how you know your count is right.')
    doc.append(answer_lines(9))
    doc.append(END)
    return '\n'.join(doc)


# ---------------------------------------------------------------------------
# Grades 4-5
# ---------------------------------------------------------------------------

def worked_path():
    """Train 1 3 2, its moves, and its path."""
    st = 9.0
    out = [r'\begin{tikzpicture}[x=1mm,y=1mm]']
    code, w = train_at(0, 4, ['1', '3', '2'], 8, r'\bfseries')
    out.append(code)
    out.append(rf'\draw[-{{Stealth[length=2mm]}}, line width=0.9pt] ({fmt(w + 5)},8) -- ({fmt(w + 15)},8);')
    x0 = w + 22
    out.append(path_grid(x0, 0, 3, st, 'UDUUDD'))
    moves = [('1', 'in'), ('1', 'out'), ('3', 'in'), ('2', 'in'), ('2', 'out'), ('3', 'out')]
    for i, (c, m) in enumerate(moves):
        xm = fmt(x0 + (i + 0.5) * st)
        out.append(rf'\node[font=\footnotesize\bfseries] at ({xm},-3.5) {{{c}}};')
        out.append(rf'\node[font=\footnotesize] at ({xm},-7.5) {{{m}}};')
    out.append(r'\end{tikzpicture}')
    return '\n'.join(out)


def build_g45():
    f = r'\bfseries\large'
    fs = r'\bfseries'
    doc = [preamble('Grades 4–5', 'TY-45-v1', '12pt')]
    doc.append(RULES_UPPER + ' For trains with more than five cars, make extra cars from paper squares, and pretend the siding is long enough to hold every car.\n')
    doc.append(centered(rules_picture(u=7.0), before=2))

    p1 = [split(t) for t in ['1 2 3', '1 3 2', '2 1 3', '2 3 1', '3 1 2', '3 2 1']]
    doc.append(r'\problem{1}Which of these six trains can leave in order? Mark each one \yes{} or \no. How many of the 24 trains with cars 1, 2, 3, 4 can leave in order?')
    doc.append(centered(train_grid(p1, 3, 9, f, colw=62, rowh=16), before=8))
    doc.append(r'\par\vspace{6pt}\hspace*{1.5em}Four cars: \rule{1.8cm}{0.5pt} of 24 can leave in order.')

    doc.append(r'\newpage')
    p2 = [split(t) for t in ['3 1 2 5 4', '2 4 1 5 3', '1 3 5 4 2', '5 1 4 2 3',
                              '3 6 1 2 4 5', '2 1 4 6 3 5', '1 7 2 6 3 5 4', '3 2 1 7 6 4 5',
                              '4 1 3 2 8 6 7 5', '4 3 1 2 8 5 7 6']]
    doc.append(r'\problem{2}Which of these trains can leave in order? Mark each one \yes{} or \no.')
    doc.append(centered(train_grid(p2, 2, 8, fs, colw=93, rowh=14.5, align_boxes=True), before=8))
    doc.append(r'\vspace{4pt}')
    doc.append(r'\problem{3}Find a way to tell from its numbers alone whether a train can leave in order. Explain why your way always gives the right answer.')
    doc.append(answer_lines(10))

    doc.append(r'\newpage')
    doc.append(r'\problem{4}A drive can be recorded as a path that steps up when a car goes into the siding and steps down when a car comes out, as shown for the train 1 3 2. Draw a path for each four-car train that can leave in order, and write the train under its path.')
    doc.append(centered(worked_path(), before=4))
    st = 4.6
    code = [r'\begin{tikzpicture}[x=1mm,y=1mm]']
    for k in range(14):
        r, c = divmod(k, 4)
        x, y = c * 45, -r * 40
        code.append(path_grid(x, y, 4, st))
        tc, _ = train_at(x + 6, y - 12, ['', '', '', ''], 7, fs)
        code.append(tc)
    code.append(r'\end{tikzpicture}')
    doc.append(centered('\n'.join(code), before=6))

    doc.append(r'\newpage')
    doc.append(r'\problem{5}Each of these paths comes from a five-car train that leaves in order. Find the train for each path.')
    words = ['UDUUUDDUDD', 'UUUDDUUDDD', 'UUDUUDDDUD', 'UUUUDDDUDD']
    st = 5.0
    code = [r'\begin{tikzpicture}[x=1mm,y=1mm]']
    for k, wd in enumerate(words):
        r, c = divmod(k, 2)
        x, y = c * 88, -r * 50
        code.append(path_grid(x, y, 5, st, wd))
        tc, _ = train_at(x + 6, y - 15, ['', '', '', '', ''], 8, fs)
        code.append(tc)
    code.append(r'\end{tikzpicture}')
    doc.append(centered('\n'.join(code), before=8))
    doc.append(r'\vspace{4pt}')
    doc.append(r'\problem{6}Can one train be driven out in order in two different ways? Can two different trains have the same path? Which paths with four steps up and four steps down come from a train that can leave in order? Explain.')
    doc.append(answer_lines(9))

    doc.append(r'\newpage')
    doc.append(r'\problem{7}How many of the 120 five-car trains can leave in order? How many of the 720 six-car trains? Explain how you know your counts are right.')
    doc.append(answer_lines(12))
    doc.append(r'\vspace{6pt}')
    doc.append(r'\problem{8}Place a second track mat to the left of yours, so that cars leaving your siding go along its arrival track and into its siding. With these two sidings, which of these trains can leave in order? Is there a train of seven cars that cannot leave in order through two sidings?')
    p8 = [split(t) for t in ['2 3 1', '3 4 1 2', '2 5 3 4 1']]
    doc.append(centered(train_grid(p8, 3, 8.5, fs, colw=58, rowh=14), before=8))
    doc.append(answer_lines(5))
    doc.append(END)
    return '\n'.join(doc)


# ---------------------------------------------------------------------------
# Track mat (full size, landscape)
# ---------------------------------------------------------------------------

def build_mat():
    """One full-size track mat on landscape US Letter.

    The main line runs off both page edges so that waiting and departed cars
    can continue on the table, and two mats laid side by side join into one
    line (4-5 Problem 8). The siding is a walled dead end one car wide and
    five car places long."""
    W, H = 279.4, 215.9          # landscape US Letter, mm
    u = 29.0                     # one car place: 25 mm card or 2 cm cube
    L = 5                        # siding length in places
    xj = W / 2 - u / 2           # left wall of the siding
    yb = 22.0                    # bottom (dead end) of the siding
    ym = yb + L * u              # bottom rail of the main line
    yt = ym + u                  # top rail of the main line
    g = []
    g.append(rf'\fill[black!7] (-2,{fmt(ym)}) rectangle ({fmt(W + 2)},{fmt(yt)});')
    g.append(rf'\fill[black!7] ({fmt(xj)},{fmt(yb)}) rectangle ({fmt(xj + u)},{fmt(ym)});')
    rail = 'black!55, line width=1pt'
    g.append(rf'\draw[{rail}] (-2,{fmt(yt)}) -- ({fmt(W + 2)},{fmt(yt)});')
    g.append(rf'\draw[{rail}] (-2,{fmt(ym)}) -- ({fmt(xj)},{fmt(ym)});')
    g.append(rf'\draw[{rail}] ({fmt(xj + u)},{fmt(ym)}) -- ({fmt(W + 2)},{fmt(ym)});')
    for k in range(1, L):
        y = yb + k * u
        g.append(rf'\draw[black!25, line width=0.5pt] ({fmt(xj)},{fmt(y)}) -- ({fmt(xj + u)},{fmt(y)});')
    g.append(rf'\draw[line width=3pt, line join=miter] ({fmt(xj)},{fmt(ym)}) -- ({fmt(xj)},{fmt(yb)}) '
             rf'-- ({fmt(xj + u)},{fmt(yb)}) -- ({fmt(xj + u)},{fmt(ym)});')
    a = r'-{Stealth[length=4mm]}, line width=1.4pt, black!40, rounded corners=3mm'
    h = yt + 7
    g.append(rf'\draw[{a}] ({fmt(W - 30)},{fmt(h)}) -- ({fmt(xj + 0.68 * u)},{fmt(h)}) '
             rf'-- ({fmt(xj + 0.68 * u)},{fmt(ym - 1.2 * u)});')
    g.append(rf'\draw[{a}] ({fmt(xj + 0.32 * u)},{fmt(ym - 1.2 * u)}) -- ({fmt(xj + 0.32 * u)},{fmt(h)}) '
             rf'-- (30,{fmt(h)});')
    lab = r'font=\sffamily\Large'
    g.append(rf'\node[{lab}, below] at ({fmt(xj / 2)},{fmt(ym - 3)}) {{departure track}};')
    g.append(rf'\node[{lab}, below] at ({fmt(xj + u + xj / 2)},{fmt(ym - 3)}) {{arrival track}};')
    g.append(rf'\node[{lab}, right] at ({fmt(xj + u + 4)},{fmt(yb + 1.5 * u)}) {{siding}};')
    g.append(rf'\node[font=\sffamily\small, anchor=base west] at (14,9) '
             rf'{{Bellingham Math Circle / {WEEK} / TY-mat-v1}};')
    g.append(rf'\node[font=\sffamily\small, anchor=base east] at ({fmt(W - 14)},9) '
             rf'{{Print at 100\%. One car place is 29 mm. Not yet tried with the real cars.}};')
    body = '\n'.join(g)
    return rf"""\documentclass{{article}}
\usepackage[T1]{{fontenc}}
\usepackage{{tgheros}}
\renewcommand{{\familydefault}}{{\sfdefault}}
\usepackage[letterpaper, landscape, margin=0.3in]{{geometry}}
\usepackage{{tikz}}
\usetikzlibrary{{arrows.meta}}
\pagestyle{{empty}}
\begin{{document}}
\begin{{tikzpicture}}[remember picture, overlay, x=1mm, y=1mm]
\begin{{scope}}[shift={{(current page.south west)}}]
{body}
\end{{scope}}
\end{{tikzpicture}}
\end{{document}}
"""


# ---------------------------------------------------------------------------

def compile_tex(name, text):
    os.makedirs(BUILD, exist_ok=True)
    src = os.path.join(HERE, name + '.tex')
    with open(src, 'w') as fh:
        fh.write(text)
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                            '-output-directory', BUILD, src],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            sys.exit(f'pdflatex failed on {name}')
    log = open(os.path.join(BUILD, name + '.log')).read()
    for bad in ('Overfull \\hbox', 'Overfull \\vbox'):
        if bad in log:
            print(f'warning: {bad} in {name}')
    shutil.copy(os.path.join(BUILD, name + '.pdf'), os.path.join(OUT, name + '.pdf'))
    print('built', os.path.join(OUT, name + '.pdf'))


def main():
    compile_tex('k-1', build_k1())
    compile_tex('grades-2-3', build_g23())
    compile_tex('grades-4-5', build_g45())
    compile_tex('track-mat', build_mat())


if __name__ == '__main__':
    main()
