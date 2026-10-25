"""Generate the three student packets as LaTeX/TikZ.

Run: ./build.sh  (checks the mathematics, writes the .tex files, compiles, and puts the PDFs in final/)
"""
import math

TOPIC = 'Patterns you cannot avoid'
WEEK = 'NN'


# ---------------------------------------------------------------- drawing helpers
def f(x):
    return f'{x:.3f}'


def strip(n, s, x0=0.0, y0=0.0, givens=None, numbers=True, numsize=r'\small'):
    """A numbered strip of n squares of side s cm with its lower-left corner at (x0, y0)."""
    givens = givens or {}
    out = []
    for i in range(1, n + 1):
        x = x0 + (i - 1) * s
        out.append(rf'\draw[line width=0.9pt] ({f(x)},{f(y0)}) rectangle ({f(x + s)},{f(y0 + s)});')
        if numbers:
            out.append(rf'\node[font={numsize}, anchor=base] at ({f(x + s / 2)},{f(y0 - 0.45)}) {{{i}}};')
    for i, c in givens.items():
        out.append(counter(x0 + (i - 0.5) * s, y0 + s / 2, s, c))
    return '\n'.join(out)


def counter(cx, cy, s, c):
    col = 'cred' if c == 'R' else 'cblue'
    return (rf'\fill[{col}] ({f(cx)},{f(cy)}) circle ({f(0.36 * s)});'
            rf'\node[text=white,font=\bfseries\small] at ({f(cx)},{f(cy)}) {{{c}}};')


def comb_on_strip(n, s, first, gap, colours=None, x0=0.0, y0=0.0, full=None, overhang=0.32):
    """Strip of n squares with a comb laid on it, windows at first, first+gap, first+2gap.

    full: a colouring of every square (such as 'RRBRBR'); the comb card hides the squares it covers.
    """
    wins = [first, first + gap, first + 2 * gap]
    out = [strip(n, s, x0, y0)]
    if full:
        assert len(full) == n
        for i, c in enumerate(full, start=1):
            out.append(counter(x0 + (i - 0.5) * s, y0 + s / 2, s, c))
    if colours:
        for w, c in zip(wins, colours):
            out.append(counter(x0 + (w - 0.5) * s, y0 + s / 2, s, c))
    left = x0 + (wins[0] - 1) * s - overhang * s
    right = x0 + wins[2] * s + overhang * s
    bot, top = y0 - 0.1 * s, y0 + s + 0.1 * s
    path = rf'({f(left)},{f(bot)}) rectangle ({f(right)},{f(top)})'
    holes = ' '.join(rf'({f(x0 + (w - 1) * s + 0.04)},{f(y0 + 0.04)}) rectangle '
                     rf'({f(x0 + w * s - 0.04)},{f(y0 + s - 0.04)})' for w in wins)
    out.append(rf'\fill[gray!55, even odd rule] {path} {holes};')
    out.append(rf'\draw[line width=0.8pt] {path};')
    for w in wins:
        out.append(rf'\draw[line width=0.6pt] ({f(x0 + (w - 1) * s + 0.04)},{f(y0 + 0.04)}) rectangle '
                   rf'({f(x0 + w * s - 0.04)},{f(y0 + s - 0.04)});')
    return '\n'.join(out)


def dots(n, diameter, cx=0.0, cy=0.0):
    """n dots on a circle with every joining line drawn faintly."""
    r = diameter / 2
    pts = [(cx + r * math.cos(math.pi / 2 + 2 * math.pi * k / n),
            cy + r * math.sin(math.pi / 2 + 2 * math.pi * k / n)) for k in range(n)]
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            out.append(rf'\draw[gray!55, line width=0.6pt] ({f(pts[i][0])},{f(pts[i][1])}) -- '
                       rf'({f(pts[j][0])},{f(pts[j][1])});')
    for x, y in pts:
        out.append(rf'\fill ({f(x)},{f(y)}) circle (0.11);')
    return '\n'.join(out)


def number_row(nums, d, x0=0.0, y0=0.0, step=None):
    """Circles to colour, each with its number underneath."""
    step = step or d * 1.3
    out = []
    for k, m in enumerate(nums):
        x = x0 + k * step + d / 2
        out.append(rf'\draw[line width=0.9pt] ({f(x)},{f(y0 + d / 2)}) circle ({f(d / 2)});')
        out.append(rf'\node[font=\small\bfseries, anchor=base] at ({f(x)},{f(y0 - 0.45)}) {{{m}}};')
    return '\n'.join(out)


def tikz(body, center=True):
    pic = '\\begin{tikzpicture}\n' + body + '\n\\end{tikzpicture}'
    return ('\\begin{center}\n' + pic + '\n\\end{center}') if center else pic


def stack_strips(lengths, s, gap, givens_list=None):
    """Several strips stacked vertically in one picture, left-aligned."""
    givens_list = givens_list or [None] * len(lengths)
    parts = []
    y = 0.0
    for n, g in zip(lengths, givens_list):
        parts.append(strip(n, s, 0, y, givens=g))
        y -= s + gap
    return tikz('\n'.join(parts))


def problem(n, text):
    return rf'\par\noindent\textbf{{Problem {n}:}} {text}\par' + '\n'


# ---------------------------------------------------------------- document wrapper
def document(level, pid, body, ptsize, landscape=False):
    cls = 'extarticle' if ptsize == 14 else 'article'
    orient = 'landscape,' if landscape else ''
    return rf'''\documentclass[{ptsize}pt,letterpaper]{{{cls}}}
\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{helvet}}
\renewcommand{{\familydefault}}{{\sfdefault}}
\usepackage[letterpaper,{orient}left=0.75in,right=0.75in,top=0.85in,bottom=0.85in,headheight=18pt,headsep=14pt,footskip=26pt]{{geometry}}
\usepackage{{tikz}}
\usepackage{{pifont}}
\usepackage{{fancyhdr}}
\definecolor{{cred}}{{RGB}}{{214,39,40}}
\definecolor{{cblue}}{{RGB}}{{31,92,204}}
\pagestyle{{fancy}}
\fancyhf{{}}
\renewcommand{{\headrulewidth}}{{0pt}}
\lhead{{Week {WEEK} / {TOPIC} / {level}}}
\lfoot{{Bellingham Math Circle / Week {WEEK} / {pid}}}
\rfoot{{\thepage}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{4pt}}
\linespread{{1.12}}
\begin{{document}}
{body}
\end{{document}}
'''


# ---------------------------------------------------------------- K-1
# K-1 pages are landscape so that every strip is drawn at the size of the printed strips
# (25 mm squares): counters sit on the page squares and the spacing combs line up with them.
K1_S = 2.5


def k1():
    b = []
    # shared rule, with one full strip that a comb shows is not good
    b.append(r'Put a red or a blue counter on every square of a strip. '
             r'The strip is good if a comb never shows three counters of one color, wherever you slide it.')
    s = 1.25
    pic = [comb_on_strip(6, s, 2, 2, full='RRBRBR', overhang=0.1),
           rf'\node[font=\Huge] at ({f(6 * s + 1.0)},{f(s / 2)}) {{\ding{{55}}}};']
    b.append(r'\vspace{-4pt}' + tikz('\n'.join(pic)))
    b.append(r'\vspace{2pt}')
    b.append(problem(1, r'Make each strip good, then color it.'))
    b.append(r'\vspace{2pt}' + stack_strips([4, 6, 7], K1_S, 1.1))
    b.append(r'\newpage')

    b.append(problem(2, r'Finish each strip so that it is good.'))
    b.append(r'\vspace{2pt}' + stack_strips([7, 8, 8, 8], K1_S, 1.3,
                                           [{2: 'R', 3: 'R'}, {1: 'R', 2: 'R'},
                                            {2: 'B', 4: 'B'}, {5: 'R', 8: 'R'}]))
    b.append(r'\newpage')

    b.append(problem(3, r'Make the strip of 8 squares good. Can you make the strip of 9 squares good?'))
    b.append(r'\vspace{6pt}' + stack_strips([8, 9], K1_S, 2.2))
    b.append(r'\newpage')

    b.append(problem(4, r'Play against the adult or a partner on the strip of 9 squares. '
                        r'Take turns putting a red or a blue counter on an empty square. '
                        r'Check with the combs after every turn. '
                        r'If a comb shows three counters of one color, the player who just moved loses.'))
    b.append(r'\vspace{2pt}' + tikz(strip(9, K1_S)))
    b.append(r'\vspace{1.4cm}')
    b.append(problem(5, r'Play the same game on the strip of 8 squares. '
                        r'Can a game end with all the squares filled and nobody losing? '
                        r'On the strip of 9 squares, would you rather go first or second?'))
    b.append(r'\vspace{2pt}' + tikz(strip(8, K1_S)))
    b.append(r'\newpage')

    b.append(problem(6, r'Find every good strip of 8 squares.'))
    b.append(r'\vspace{2pt}' + stack_strips([8] * 3, K1_S, 1.6))
    b.append(r'\newpage')
    b.append(r'More strips for Problem 6.\par\vspace{2pt}' + stack_strips([8] * 3, K1_S, 1.6))
    return document('Grades K--1', f'{WEEK}-K-v1', '\n'.join(b), 14, landscape=True)


# ---------------------------------------------------------------- shared text for grades 2-5
def upper_rule():
    txt = (r'Color each square of a strip red or blue. The strip is good if no three equally spaced '
           r'squares, such as 2, 5, 8 or 4, 5, 6, are all the same color.')
    return txt + '\n' + tikz(comb_on_strip(9, 0.9, 2, 3, overhang=0.1)) + r'\vspace{8pt}'


SUM_RULE = (r'If two of the numbers add up to another one, like 1 + 3 = 4, those three numbers must not all '
            r'be the same color. A number can be added to itself: 2 + 2 = 4, so 2 and 4 cannot be the same '
            r'color.')

SIM_RULES = (r'Play Sim with a partner on a board of six dots. One player colors lines red and the other blue. '
             r'Take turns, coloring one line each turn. If you join three dots with three lines of your own '
             r'color, you lose.')

NO_TRIANGLE = r'so that no three dots are joined by three lines of the same color'

FIVE_DIAM = 7.5   # five-dot boards to work on
SIX_DIAM = 8.0    # six-dot boards


def tri_example():
    """A small five-dot board with three dots joined by three red lines, marked with a cross."""
    d = 2.3
    r = d / 2
    pts = [(r * math.cos(math.pi / 2 + 2 * math.pi * k / 5), r * math.sin(math.pi / 2 + 2 * math.pi * k / 5))
           for k in range(5)]
    out = [dots(5, d)]
    for i, j in ((0, 2), (0, 3), (2, 3)):
        out.append(rf'\draw[cred, line width=2.2pt] ({f(pts[i][0])},{f(pts[i][1])}) -- '
                   rf'({f(pts[j][0])},{f(pts[j][1])});')
    for x, y in pts:
        out.append(rf'\fill ({f(x)},{f(y)}) circle (0.11);')
    out.append(rf'\node[font=\huge] at ({f(r + 0.85)},0) {{\ding{{55}}}};')
    return r'\begin{tikzpicture}[baseline=(current bounding box.north)]' + '\n'.join(out) + r'\end{tikzpicture}'


def problem_with_picture(n, text, pic, width=0.76):
    """A problem statement with a small convention picture to its right."""
    return (r'\par\noindent\begin{minipage}[t]{' + f'{width}' + r'\linewidth}\raggedright\textbf{Problem ' + str(n) +
            r':} ' + text + r'\end{minipage}\hfill\begin{minipage}[t]{' + f'{0.98 - width:.2f}' +
            r'\linewidth}\raggedleft' + pic + r'\end{minipage}\par' + '\n')


def boards(n, diam, cols, rows, gapx=1.8, gapy=1.4):
    parts = [dots(n, diam, c * (diam + gapx), -r * (diam + gapy)) for r in range(rows) for c in range(cols)]
    return tikz('\n'.join(parts))


def rows_grid(nums, d, rows, cols, colgap=1.2, rowgap=1.25, step=None):
    step = step or d * 1.3
    width = (len(nums) - 1) * step + d
    parts = []
    for r in range(rows):
        for c in range(cols):
            parts.append(number_row(nums, d, c * (width + colgap), -r * (d + rowgap), step))
    return tikz('\n'.join(parts))


# ---------------------------------------------------------------- grades 2-3
def g23():
    b = [upper_rule()]
    b.append(problem(1, r'What is the longest strip you can make good? Color your good strips.'))
    b.append(r'\vspace{6pt}' + stack_strips([6, 7, 8, 9], 1.5, 1.3))
    b.append(r'\newpage')

    b.append(problem(2, r'Find every good way to color a strip of 8 squares.'))
    b.append(r'\vspace{6pt}' + stack_strips([8] * 8, 1.3, 1.0))
    b.append(r'\newpage')

    b.append(problem(3, r'Can a strip of 9 squares be good? Explain how you know.'))
    b.append(r'\vspace{6pt}' + stack_strips([9, 9, 9], 1.3, 1.0))
    b.append(r'\newpage')

    b.append(problem(4, r'Put a red or a blue counter on each of the cards 1, 2, 3 and 4. ' + SUM_RULE +
                        r' Find every way to color the cards.'))
    b.append(r'\vspace{6pt}' + rows_grid([1, 2, 3, 4], 0.9, 2, 2, colgap=2.6, rowgap=1.0))
    b.append(r'\vspace{2.0cm}')
    b.append(problem(5, r'Can the cards 1, 2, 3, 4 and 5 be colored by the same rule? Explain how you know.'))
    b.append(r'\vspace{6pt}' + rows_grid([1, 2, 3, 4, 5], 0.9, 2, 2, colgap=2.6, rowgap=1.0))
    b.append(r'\newpage')

    b.append(problem_with_picture(6, r'Color each of the ten lines joining these five dots red or blue ' +
                                  NO_TRIANGLE + '.', tri_example()))
    b.append(r'\vspace{4pt}' + boards(5, FIVE_DIAM, 2, 2, gapx=1.6, gapy=1.0))
    b.append(r'\newpage')

    b.append(problem(7, SIM_RULES + r' Can a game end with all fifteen lines colored and nobody losing?'))
    b.append(r'\vspace{4pt}' + boards(6, SIX_DIAM, 2, 1, gapx=1.4))
    b.append(r'\vspace{0.8cm}')
    b.append(problem(8, r'Color the numbers 1, 2, 3, 4, \dots{} red, blue or green, using the rule from '
                        r'Problem 4. How far can you go?'))
    b.append(r'\vspace{6pt}' + rows_grid(list(range(1, 16)), 0.8, 4, 1, rowgap=1.0, step=1.12))
    return document('Grades 2--3', f'{WEEK}-23-v1', '\n'.join(b), 12)


# ---------------------------------------------------------------- grades 4-5
def g45():
    b = [upper_rule()]
    b.append(problem(1, r'What is the longest strip you can make good? Color your good strips.'))
    b.append(r'\vspace{6pt}' + stack_strips([6, 7, 8, 9], 1.5, 1.3))
    b.append(r'\newpage')

    b.append(problem(2, r'Find every good way to color a strip of 8 squares.'))
    b.append(r'\vspace{6pt}' + stack_strips([8] * 8, 1.3, 1.0))
    b.append(r'\newpage')

    b.append(problem(3, r'Can a strip of 9 squares be good? Explain how you know.'))
    b.append(r'\vspace{6pt}' + stack_strips([9, 9, 9], 1.1, 0.95))
    b.append(r'\vspace{4.0cm}')
    b.append(problem(4, r'Color the numbers 1, 2, 3, \dots{} red or blue. ' + SUM_RULE +
                        r' How far can you go? Explain why no coloring can go further.'))
    b.append(r'\vspace{6pt}' + rows_grid(list(range(1, 9)), 0.8, 2, 2, colgap=1.4, rowgap=1.0, step=1.0))
    b.append(r'\newpage')

    b.append(problem_with_picture(5, r'Color the ten lines joining five dots red or blue ' + NO_TRIANGLE +
                                  r'. Find every way to do this.', tri_example()))
    b.append(r'\vspace{2pt}' + boards(5, 3.9, 4, 4, gapx=0.6, gapy=0.75))
    b.append(r'\newpage')

    b.append(problem(6, SIM_RULES + r' Would you rather go first or second?'))
    b.append(r'\vspace{4pt}' + boards(6, SIX_DIAM, 2, 1, gapx=1.4))
    b.append(r'\vspace{0.4cm}')
    b.append(problem(7, r'Can the fifteen lines joining six dots be colored red or blue with no one-color '
                        r'triangle (three dots joined by three lines of one color)? Explain how you know.'))
    b.append(r'\vspace{4pt}' + boards(6, SIX_DIAM, 1, 1))
    b.append(r'\newpage')

    b.append(problem(8, r'Color the fifteen lines joining six dots red or blue with as few one-color triangles '
                        r'as possible. What is the fewest you can get?'))
    b.append(r'\vspace{4pt}' + boards(6, SIX_DIAM, 2, 2, gapx=1.2, gapy=1.0))
    b.append(r'\newpage')

    b.append(problem(9, r'Use red and blue again, with one change to the rule of Problem 4: a number cannot be '
                        r'added to itself. Now 2 + 2 = 4 does not count, but 1 + 3 = 4 still does. '
                        r'How far can you go?'))
    b.append(r'\vspace{6pt}' + rows_grid(list(range(1, 13)), 0.8, 3, 1, rowgap=1.0, step=1.12))
    b.append(r'\vspace{1.0cm}')
    b.append(problem(10, r'Use red, blue and green with the rule of Problem 4, where 2 + 2 = 4 counts again. '
                         r'How far can you go?'))
    b.append(r'\vspace{6pt}' + rows_grid(list(range(1, 16)), 0.8, 4, 1, rowgap=1.0, step=1.12))
    return document('Grades 4--5', f'{WEEK}-45-v1', '\n'.join(b), 12)


if __name__ == '__main__':
    for name, fn in (('k-1', k1), ('grades-2-3', g23), ('grades-4-5', g45)):
        with open(f'{name}.tex', 'w') as fh:
            fh.write(fn())
    print('wrote k-1.tex grades-2-3.tex grades-4-5.tex')
