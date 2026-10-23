"""Week 48 figures, carried over from the old builder
(archive-before-problem-files-2026-10-23/make.py and draw.py).

Coordinates are millimetres on the house 185 x 235 mm page canvas, y downward, so the
default page template in problem-files/canvas.py is the old builder's page. Problem
files call these functions by name in their `figure` sections; the wording lives in
the problem files.
"""
from canvas import text, label, line, rect


def shape(x, y, n, kind, side=120):
    """An n-by-n grid of side mm, with the triangle, diamond or trapezoid drawn on the 4-by-4 frame."""
    s = ''; u = side/4
    pts = {'triangle': [(0, 4), (4, 4), (4, 0)], 'diamond': [(0, 2), (2, 0), (4, 2), (2, 4)], 'trap': [(.5, .5), (3.5, .5), (3, 3.5), (1, 3.5)]}.get(kind)
    if pts:
        s += r'\fill[gray!22] '+' -- '.join(f'({x+a*u},{y+b*u})' for a, b in pts)+' -- cycle;\n'
    for i in range(n+1):
        s += line(x+i*side/n, y, x+i*side/n, y+side, 'gray!70')+line(x, y+i*side/n, x+side, y+i*side/n, 'gray!70')
    if n == 8:
        for i in range(5):
            s += line(x+i*side/4, y, x+i*side/4, y+side, 'line width=.8pt')+line(x, y+i*side/4, x+side, y+i*side/4, 'line width=.8pt')
    if pts: s += r'\draw[line width=1pt] '+' -- '.join(f'({x+a*u},{y+b*u})' for a, b in pts)+' -- cycle;\n'
    return s


def legend(y=0):
    s = rect(7, y, 30, 30, 'fill=gray!15')+label(44, y+15, '=', 16)
    for a in range(2):
        for b in range(2): s += rect(51+a*15, y+b*15, 15, 15, 'fill=gray!15')
    s += text(92, y+2, r'1 big square\\ = 4 small squares', w=83, size=12)
    return s


def blanks(y, fine=False):
    return text(10, y, (r'Inside: \rule{15mm}{.3pt} big-square units\\[5mm]Cover: \rule{15mm}{.3pt} big-square units'), w=170, size=13)


def samples():
    """Page 1: a whole, a partial and an outside cell; the outside cell's gray neighbour
    shows that a touch at an edge adds no square."""
    s = rect(12, 25, 24, 24, 'fill=gray!22')+label(24, 55, 'whole', 11)
    s += r'\fill[gray!22] (63,49)--(87,49)--(87,25)--cycle;'+'\n'+rect(63, 25, 24, 24)+line(63, 49, 87, 25, 'line width=1pt')+label(75, 55, 'partial', 11)
    s += r'\fill[gray!22] (104,25) rectangle (114,49);'+'\n'
    s += rect(114, 25, 24, 24)+line(114, 25, 114, 49, 'line width=1.2pt')+label(126, 55, 'outside', 11)
    return s


def split_picture():
    """4-5 Problem 6: one big square of the triangle split into four."""
    return legend(37)+shape(25, 88, 1, 'triangle', 30)+label(91, 103, r'$\longrightarrow$', 20)+shape(125, 88, 2, 'triangle', 30)


def two_boards(y):
    """K-1 and 2-3: two blank 85 mm boards side by side, one for each shape."""
    return shape(4, y, 4, 'blank', 85)+shape(96, y, 4, 'blank', 85)


def two_grid_blanks(y):
    """2-3 trapezoid: inside and cover on the big grid and on the small grid."""
    row = r'Inside \rule{15mm}{.3pt} \quad Cover \rule{15mm}{.3pt} big-square units'
    return text(10, y, r'\begin{tabular}{@{}ll@{}}Big squares: & '+row+r'\\[5mm]Small squares: & '+row+r'\end{tabular}',
                w=170, size=13)
