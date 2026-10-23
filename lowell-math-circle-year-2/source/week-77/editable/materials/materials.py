#!/usr/bin/env python3
"""Write materials.tex: Week 77's print-and-cut tiles, edge strips, edge tokens and stage cards.

Every tile corner and strip length is taken from the student boards (centimetres,
y down), so a page printed at 100% gives tiles that cover their printed triangles.
Each tile carries its name, its board and the name of each edge along that side.
Run `python3 materials.py` after changing a board; build.py runs it too."""
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Board coordinates, copied from the student pages (problem files 01-06).
SQUARE = {'A': (0, 0), 'B': (6.2, 0), 'C': (6.2, 6.2), 'D': (0, 6.2)}
JOINED = {'A': (0, 0), 'B': (0, 5.8), 'C': (5.8, 1.4), 'D': (11.6, 0), 'E': (11.6, 5.8)}
FAN = {'A': (0, 0), 'B': (8, 0), 'C': (8, 8), 'D': (0, 8), 'O': (4, 4)}
LAUNCH = {'X': (0, 1.4), 'Y': (0.9, 0), 'Z': (1.8, 1.4)}

# Edge names as the student pages and the guide write them.
NAMES = ['AB', 'BC', 'CD', 'DA', 'AC', 'CE', 'DE', 'AO', 'BO', 'CO', 'DO', 'XY', 'YZ', 'XZ']
NAME = {frozenset(n): n for n in NAMES}

# (board word, coordinates, tiles, page offset)
TILE_GROUPS = [
    ('joined', JOINED, ['ABC', 'CDE'], (0.0, 2.3)),
    ('square', SQUARE, ['ABC', 'ACD'], (0.0, 9.4)),
    ('fan', FAN, ['ABO', 'BCO', 'CDO', 'DAO'], (9.4, 9.4)),
    ('launch', LAUNCH, ['XYZ'], (12.4, 5.2)),
]

# (edge, board word, length in cm, page position of the left end)
def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])

STRIPS = [
    ('AB', 'joined', dist(JOINED['A'], JOINED['B']), (12.4, 2.4)),
    ('DE', 'joined', dist(JOINED['D'], JOINED['E']), (12.4, 3.6)),
    ('AB', 'square', dist(SQUARE['A'], SQUARE['B']), (0.0, 16.5)),
    ('BC', 'square', dist(SQUARE['B'], SQUARE['C']), (0.0, 17.7)),
    ('CD', 'square', dist(SQUARE['C'], SQUARE['D']), (0.0, 18.9)),
    ('DA', 'square', dist(SQUARE['D'], SQUARE['A']), (0.0, 20.1)),
    ('AC', 'square', dist(SQUARE['A'], SQUARE['C']), (9.4, 18.3)),
]
STRIP_HEIGHT = 0.8

TOKEN_W, TOKEN_H, TOKEN_COLS = 18.2 / 8, 1.6, 8
EDGE_TOKENS = [n for n in NAMES[:11] for _ in range(3)]
LAUNCH_TOKENS = [n for n in ('XY', 'YZ', 'XZ') for _ in range(2)]
BLANK_TOKENS = 48 - len(EDGE_TOKENS) - len(LAUNCH_TOKENS)
STAGES = ['0', '2', '3', '4', '5', '8', '', '']


def f(x):
    return f'{x:.3f}'.rstrip('0').rstrip('.')


def tile_layout(coords, tile, offset, small):
    """Corners, edge-label positions/angles, corner-letter positions and the incentre."""
    pts = [coords[v] for v in tile]
    pts = [(x + offset[0], y + offset[1]) for x, y in pts]
    sides = [dist(pts[(i + 1) % 3], pts[(i + 2) % 3]) for i in range(3)]  # side opposite corner i
    per = sum(sides)
    inc = tuple(sum(sides[i] * pts[i][k] for i in range(3)) / per for k in (0, 1))
    area = abs((pts[1][0] - pts[0][0]) * (pts[2][1] - pts[0][1]) - (pts[2][0] - pts[0][0]) * (pts[1][1] - pts[0][1])) / 2
    inradius = 2 * area / per
    edges = []
    inset = 0.38
    for i in range(3):
        p, q, other = pts[i], pts[(i + 1) % 3], pts[(i + 2) % 3]
        name = NAME[frozenset((tile[i], tile[(i + 1) % 3]))]
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        dx, dy = q[0] - p[0], q[1] - p[1]
        length = math.hypot(dx, dy)
        nx, ny = -dy / length, dx / length
        if (other[0] - mx) * nx + (other[1] - my) * ny < 0:
            nx, ny = -nx, -ny
        angle = math.degrees(math.atan2(-dy, dx))  # on paper, y up
        if angle > 90:
            angle -= 180
        if angle <= -90:
            angle += 180
        edges.append((name, (mx + inset * nx, my + inset * ny), angle))
    corners = []
    for i in range(3):
        v, a, b = pts[i], pts[(i + 1) % 3], pts[(i + 2) % 3]
        ua = ((a[0] - v[0]) / dist(a, v), (a[1] - v[1]) / dist(a, v))
        ub = ((b[0] - v[0]) / dist(b, v), (b[1] - v[1]) / dist(b, v))
        theta = math.acos(max(-1, min(1, ua[0] * ub[0] + ua[1] * ub[1])))
        bis = (ua[0] + ub[0], ua[1] + ub[1])
        norm = math.hypot(*bis)
        r = 0.36 / math.sin(theta / 2)
        corners.append((tile[i], (v[0] + r * bis[0] / norm, v[1] + r * bis[1] / norm)))
    return pts, edges, corners, inc, inradius


def tiles_tex():
    out = []
    for board, coords, tiles, offset in TILE_GROUPS:
        small = board == 'launch'
        for tile in tiles:
            pts, edges, corners, inc, _ = tile_layout(coords, tile, offset, small)
            out.append(r'\draw[line width=.6pt] (%s,%s)--(%s,%s)--(%s,%s)--cycle;' % tuple(f(c) for p in pts for c in p))
            if small:
                # Too small for edge names: its name inside, the board beside it.
                out.append(r'\node[font=\fontsize{8}{9}\selectfont\bfseries] at (%s,%s) {%s};' % (f(inc[0]), f(inc[1]), tile))
                x, y = min(p[0] for p in pts), max(p[1] for p in pts) + 0.3
                out.append(r'\node[anchor=north west,inner sep=0pt,font=\fontsize{10}{12}\selectfont] at (%s,%s) {launch tile, student page 1};' % (f(x), f(y)))
                continue
            for name, (x, y), angle in edges:
                out.append(r'\node[rotate=%s,font=\fontsize{10}{12}\selectfont] at (%s,%s) {%s};' % (f(angle), f(x), f(y), name))
            for letter, (x, y) in corners:
                out.append(r'\node[font=\fontsize{9}{10}\selectfont,text=black!60] at (%s,%s) {%s};' % (f(x), f(y), letter))
            out.append(r'\node[align=center,font=\fontsize{14}{16}\selectfont\bfseries] at (%s,%s) {%s\\[-1pt]{\mdseries\fontsize{8}{9}\selectfont %s}};'
                       % (f(inc[0]), f(inc[1]), tile, board))
    for edge, board, length, (x, y) in STRIPS:
        out.append(r'\draw[line width=.6pt] (%s,%s) rectangle (%s,%s);' % (f(x), f(y), f(x + length), f(y + STRIP_HEIGHT)))
        out.append(r'\node[font=\fontsize{10}{12}\selectfont] at (%s,%s) {\textbf{%s}\quad %s};' % (f(x + length / 2), f(y + STRIP_HEIGHT / 2), edge, board))
    return '\n'.join(out)


def tokens_tex():
    out = []
    labels = EDGE_TOKENS + LAUNCH_TOKENS + [''] * BLANK_TOKENS
    top = 1.7
    for k, label in enumerate(labels):
        r, c = divmod(k, TOKEN_COLS)
        x, y = c * TOKEN_W, top + r * TOKEN_H
        fill = ',fill=black!10' if label in ('XY', 'YZ', 'XZ') else ''
        out.append(r'\draw[line width=.6pt%s] (%s,%s) rectangle (%s,%s);' % (fill, f(x), f(y), f(x + TOKEN_W), f(y + TOKEN_H)))
        if label:
            out.append(r'\node[font=\fontsize{18}{20}\selectfont\bfseries] at (%s,%s) {%s};' % (f(x + TOKEN_W / 2), f(y + TOKEN_H / 2), label))
    top = top + 6 * TOKEN_H + 1.0
    for c, stage in enumerate(STAGES):
        x = c * TOKEN_W
        out.append(r'\draw[line width=.6pt] (%s,%s) rectangle (%s,%s);' % (f(x), f(top), f(x + TOKEN_W), f(top + 2.4)))
        out.append(r'\node[font=\fontsize{9}{10}\selectfont] at (%s,%s) {stage};' % (f(x + TOKEN_W / 2), f(top + 0.45)))
        if stage:
            out.append(r'\node[font=\fontsize{30}{32}\selectfont\bfseries] at (%s,%s) {%s};' % (f(x + TOKEN_W / 2), f(top + 1.45), stage))
    return '\n'.join(out)


PREAMBLE = r"""% Written by materials.py; edit that file, not this one.
\pdfmapfile{+cm.map}
\pdfmapfile{+cmextra.map}
\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.65in,headheight=15pt,headsep=16pt,footskip=24pt]{geometry}
\usepackage{tikz}
\usepackage{fancyhdr}
\renewcommand{\familydefault}{\sfdefault}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\fontsize{11}{13}\selectfont Week 77 / Persistent holes / Tiles, strips and tokens}
\fancyfoot[L]{\fontsize{9}{11}\selectfont Bellingham Math Circle / Week 77 / F77-M-v1}
\fancyfoot[R]{\fontsize{9}{11}\selectfont\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}
\newcommand{\note}[1]{\node[anchor=north west,inner sep=0pt,text width=18.2cm,align=left,font=\fontsize{10}{13}\selectfont] at (0,0) {#1};}
\begin{document}
"""

PAGE1_NOTE = (r"Adults: print at 100\% (Actual size), on card stock if you have it. Cut out every tile and strip "
              r"along its outline, including the lines inside the square and the fan. Each tile fits its "
              r"triangle on the student pages; names repeat across boards but sizes differ, so keep each "
              r"board's tiles in its own envelope. These pieces have not yet been tried with children.")
PAGE2_NOTE = (r"Edge tokens: three of each board edge, two each of the launch edges XY, YZ and XZ (shaded), and "
              r"%d blanks. Stage cards: 0, 2, 3, 4, 5, 8 and two blanks. Cut along every line." % BLANK_TOKENS)


def document():
    page = r'\begin{tikzpicture}[x=1cm,y=-1cm]\path[use as bounding box] (0,0) rectangle (18.2,22.15);'
    return (PREAMBLE + page + '\n' + r'\note{%s}' % PAGE1_NOTE + '\n' + tiles_tex() + '\n\\end{tikzpicture}\n\\newpage\n'
            + page + '\n' + r'\note{%s}' % PAGE2_NOTE + '\n' + tokens_tex() + '\n\\end{tikzpicture}\n\\end{document}\n')


if __name__ == '__main__':
    (HERE / 'materials.tex').write_text(document())
    print(HERE / 'materials.tex')
