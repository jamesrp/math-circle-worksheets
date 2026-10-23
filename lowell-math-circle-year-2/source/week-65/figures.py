"""Week 65 figures and canvas page template, carried over from the old student builder
(archive-before-problem-files-2026-10-23/build.py, packet()).

Coordinates are inches from the bottom-left corner of the paper, y up. Each page is one
overlay picture on the whole sheet that draws its own header, footer and page number
(page_open and page_close). The geometry of the {8,4} tiling is in student/geometry.py,
which student/build.py checks. Problem files call the functions below by name in their
`figure` sections; the rule, prompt and caption wording lives in the problem files.
"""
import importlib.util
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location('week65_geometry', Path(__file__).resolve().parent / 'student' / 'geometry.py')
_geometry = importlib.util.module_from_spec(_spec)
_keep, sys.dont_write_bytecode = sys.dont_write_bytecode, True   # no __pycache__ in source folders
try:
    _spec.loader.exec_module(_geometry)
finally:
    sys.dont_write_bytecode = _keep
V, n, edge, polygon, full_ends, point, tangent = (_geometry.V, _geometry.n, _geometry.edge, _geometry.polygon,
                                                   _geometry.full_ends, _geometry.point, _geometry.tangent)
LEFT, RIGHT, BOUNDARY, SQUARE_BOUNDARY = _geometry.LEFT, _geometry.RIGHT, _geometry.BOUNDARY, _geometry.SQUARE_BOUNDARY
PAIR_SCALE, SINGLE_SCALE, stubs, key = _geometry.PAIR_SCALE, _geometry.SINGLE_SCALE, _geometry.stubs, _geometry.key
TILES, FOUR, NAMES, P, corner_view = _geometry.TILES, _geometry.FOUR, _geometry.NAMES, _geometry.P, _geometry.corner_view


# ---------------------------------------------------------------- page template (packet's page_start and end)

PRE = r'''\documentclass[letterpaper]{article}
\usepackage[margin=0in]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc}
\usepackage{amssymb}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''


def page_preamble(week, topic, header, footer):
    return PRE


def page_open(page):
    return (r'\noindent\begin{tikzpicture}[remember picture,overlay,x=1in,y=1in]' + '\n'
            + r'\begin{scope}[shift={(current page.south west)}]' + '\n'
            + f'\\node[anchor=west,font=\\sffamily\\fontsize{{10.8}}{{13}}\\selectfont] at (0.62,10.52) {{Week {page.week} / {page.topic} / {page.header}}};\n'
            + f'\\node[anchor=west,font=\\sffamily\\fontsize{{9}}{{11}}\\selectfont] at (0.62,0.42) {{Bellingham Math Circle / Week {page.week} / {page.footer}}};\n'
            + f'\\node[anchor=east,font=\\sffamily\\small] at (7.88,0.42) {{{page.number}}};\n')


def page_close(page):
    """Every page ended \\newpage in the old builder; the tools put \\newpage between pages."""
    return '\\end{scope}\n\\end{tikzpicture}\\null' + ('\\newpage\n' if page.number == page.count else '')


LEADING = {12.5: 16, 12: 15, 11.5: 14, 10.5: 13}


def text(x, y, width, body, size=12.5, leading=16):
    return f'\\node[anchor=north west,inner sep=0pt,text width={width}in,align=left,font=\\sffamily\\fontsize{{{size}}}{{{leading}}}\\selectfont] at ({x},{y}) {{{body}}};\n'


def page_prompt(n_, body, x, y, size):
    return text(x, y, 7.1, r'\textbf{Problem ' + str(n_) + ':} ' + body)


def page_text(x, y, body, w, size):
    size = size or 12.5
    return text(x, y, w or 7.1, body, size, LEADING[size])


def scope(x, y, scale): return f'\\begin{{scope}}[shift={{({x},{y})}},x={scale}in,y={scale}in]\n'


def square_grid(size=4, step=.5):
    s = ''
    for k in range(-size, size + 1):
        s += f'\\draw[black!65,line width=0.6pt] ({k*step},{-size*step}) -- ({k*step},{size*step});\n'
        s += f'\\draw[black!65,line width=0.6pt] ({-size*step},{k*step}) -- ({size*step},{k*step});\n'
    for k in range(-size, size + 1):
        for l in range(-size, size + 1): s += f'\\fill[black] ({k*step},{l*step}) circle[radius=1.25pt];\n'
    return s


def arrow(p, q, style='black,line width=1.2pt'):
    return f'\\draw[{style},-{{Latex[length=3mm,width=2.2mm]}}] {n(p)} -- {n(q)};\n'


# ---------------------------------------------------------------- page 1

def move_panels(labels):  # 00: start, move one edge, turn left on a small square grid
    out = ''
    for j, (label, pos, heading) in enumerate(zip(labels, [0j, 1 + 0j, 1 + 0j], [1, 1, 1j])):
        out += scope(1.62 + j*2.55, 8.72, .4)
        for k in range(-1, 3):
            out += f'\\draw[black!35,line width=.55pt] ({k},-1) -- ({k},1);\n'
        for k in range(-1, 2): out += f'\\draw[black!35,line width=.55pt] (-1,{k}) -- (2,{k});\n'
        out += point(0j, rad='1.5pt') + point(1 + 0j, rad='1.5pt')
        if j: out += '\\draw[black,line width=1.6pt] (0,0)--(1,0);\n'
        out += arrow(pos - heading*.17, pos + heading*.43)
        out += '\\end{scope}\n'
        out += text(.99 + j*2.55, 8.19, 2.1, label, 10.5, 13)
    return out


def square_board():  # 01: the square-grid board with A and the start arrow
    out = scope(4.25, 3.96, 1)
    out += square_grid(3, .76)
    out += point(0j, rad='2.2pt')
    out += '\\node[font=\\sffamily\\bfseries\\normalsize,fill=white,inner sep=2pt] at (-.26,-.26) {A};\n'
    out += arrow(.07 + 0j, .49 + 0j)
    out += '\\end{scope}\n'
    return out


# ---------------------------------------------------------------- page 2

def curved_panels(rule, labels):  # 02: the second rule line, then start, arrive, turn on a bending road
    out = text(.65, 9.47, 7.1, rule)
    for j, label in enumerate(labels):
        out += scope(1.25 + j*2.5, 7.91, 1.20)
        out += edge(V[0], V[1], 'black!55,line width=.8pt')
        out += edge(V[1], V[2], 'black!55,line width=.8pt')
        out += point(V[0], rad='1.7pt') + point(V[1], rad='1.7pt')
        pos = V[0] if j == 0 else V[1]
        direction = tangent(V[0], V[1]) if j == 0 else (-tangent(V[1], V[0]) if j == 1 else tangent(V[1], V[2]))
        out += arrow(pos - direction*.14, pos + direction*.19, 'black,line width=1.35pt,preaction={draw=white,line width=3.8pt}')
        out += '\\end{scope}\n'
        out += text(.80 + j*2.5, 7.97, 2.35, label, 10.5, 13)
    return out


def octagon_board():  # 03: one octagon, vertices A-H, the start arrow at A toward B
    out = scope(4.25, 3.69, SINGLE_SCALE)
    out += stubs([V], .10)
    for k in range(8): out += edge(V[k], V[(k + 1) % 8], 'black,line width=1.05pt')
    for k, z in enumerate(V):
        out += point(z, rad='2.4pt')
        out += f'\\node[font=\\sffamily\\bfseries\\large,fill=white,inner sep=2pt] at {n(z*.78)} {{{chr(65+k)}}};\n'
    start = V[0]; t = tangent(V[0], V[1]); out += arrow(start + t*.025, start + t*.147)
    out += '\\end{scope}\n'
    return out


# ---------------------------------------------------------------- page 3

def octagon_pair():  # 04: two side-sharing octagons seen from the middle of the shared side
    out = scope(4.25, 6.88, PAIR_SCALE)
    out += stubs([LEFT, RIGHT], .06)
    out += edge(LEFT[7], LEFT[0], 'black!65,line width=.85pt')
    for k, z in enumerate(BOUNDARY):
        out += edge(z, BOUNDARY[(k + 1) % 14], 'black,line width=1.15pt')
        out += point(z, rad='2.3pt')
    # Only endpoints of the shared side are tiling junctions. Never dot its midpoint.
    start = LEFT[0]; t = tangent(start, LEFT[1])
    out += arrow(start + t*.025, start + t*.135)
    out += f'\\node[font=\\sffamily\\bfseries\\large,inner sep=2pt,fill=white] at {n(start+.12+.06j)} {{A}};\n'
    out += '\\end{scope}\n'
    return out


def square_pair():  # 04: two side-sharing squares with crossing stubs
    out = scope(3.15, 2.48, 1.1)
    for z in SQUARE_BOUNDARY:
        for direction in (1, -1, 1j, -1j):
            out += f'\\draw[black!55,line width=.65pt] {n(z)} -- {n(z+.18*direction)};\n'
    for k, z in enumerate(SQUARE_BOUNDARY):
        q = SQUARE_BOUNDARY[(k + 1) % 6]
        out += f'\\draw[black,line width=1.15pt] {n(z)} -- {n(q)};\n'
        out += point(z, rad='2.3pt')
    out += '\\draw[black!65,line width=.85pt] (1,0)--(1,1);\n'
    out += arrow(.94 + 1j, .582 + 1j)
    out += '\\node[font=\\sffamily\\bfseries\\large,inner sep=2pt,fill=white] at (1.22,1.24) {A};\n'
    out += '\\end{scope}\n'
    return out


# ---------------------------------------------------------------- page 4

def streets_board(r_at=(-0.77, 0.08)):  # 05: complete streets of one octagon, the dashed street R and P
    out = scope(4.25, 5.20, 2.92)
    out += '\\draw[black!45,densely dotted,line width=.75pt] (0,0) circle[radius=1];\n'
    for k in range(8):
        a, b = full_ends(V[k], V[(k + 1) % 8])
        out += edge(a, b, 'black,line width=.78pt')
    a, b = full_ends(V[3], V[4]); out += edge(a, b, 'black,line width=2.3pt,dash pattern=on 5pt off 2.8pt')
    out += f'\\node[font=\\sffamily\\bfseries\\large,fill=white,inner sep=3pt] at ({r_at[0]},{r_at[1]}) {{R}};\n'
    out += point(P, rad='2.8pt')
    out += f'\\node[font=\\sffamily\\bfseries\\large,inner sep=0pt] at {n(P-.10-.045j)} {{P}};\n'
    out += '\\end{scope}\n'
    return out


# ---------------------------------------------------------------- page 5

def door_example(caption):  # 06: C -> D -> E, two door crossings
    out = scope(1.32, 8.70, .52)
    for k, lab in enumerate('CDE'):
        out += f'\\draw[line width=.75pt] ({k},0) rectangle ({k+1},1);\n'
        out += f'\\node[font=\\sffamily\\normalsize] at ({k+.5},.65) {{{lab}}};\n'
    out += '\\draw[-{Latex[length=2mm]},line width=1pt] (.35,.25)--(2.65,.25);\n'
    out += '\\end{scope}\n'
    out += text(3.30, 9.05, 4.10, caption, 11.5, 14)
    return out


def four_rooms(star_font='\\Large'):  # 06: Home, A, B and the star around one corner, recentred
    out = scope(4.25, 3.72, 2.82)
    # Lightly differentiated printable fills support the four readable regions.
    for i in FOUR:
        poly = [corner_view(z) for z in TILES[i][1]]
        out += polygon(poly, 'fill=black!' + ('5' if i == 0 else '0') + ',draw=none')
    seen = set()
    for i in FOUR:
        poly = [corner_view(z) for z in TILES[i][1]]
        for k in range(8):
            p, q = poly[k], poly[(k + 1) % 8]; ek = tuple(sorted((key(p), key(q))))
            if ek in seen: continue
            seen.add(ek); out += edge(p, q, 'black,line width=.9pt')
        c = corner_view(TILES[i][0])*.88
        font = star_font if NAMES[i] == r'$\star$' else '\\Large'
        out += f'\\node[font=\\sffamily\\bfseries{font},inner sep=3pt] at {n(c)} {{{NAMES[i]}}};\n'
    out += point(0j, rad='2pt')
    out += '\\end{scope}\n'
    return out


# ---------------------------------------------------------------- page 6

def route_rows(short_heading, long_heading):  # 07: 3 rows for 2-crossing routes, 10 for 4-crossing routes
    out = text(.80, 9.47, 7.0, short_heading, 12.5, 16)
    for y in (8.85, 8.25, 7.65):
        out += f'\\draw[black!55,line width=.4pt] (.80,{y}) -- (7.70,{y});\n'
    out += text(.80, 7.06, 7.0, long_heading, 12.5, 16)
    for j in range(10):
        y = 6.45 - j*.55
        out += f'\\draw[black!55,line width=.4pt] (.80,{y:.2f}) -- (7.70,{y:.2f});\n'
    return out
