"""Week 50 figures, carried over unchanged from source/week-50/editable/src/make.py.

Coordinates are millimetres on the 185 x 235 mm page canvas, y downward.
Problem files call these by name in their `figure` sections.
"""
from canvas import BS, text, label, line, rect, circle


def path(x, y, pts, opts='line width=1.1pt'):
    return BS+'draw['+opts+'] '+' -- '.join(f'({x+a},{y+120-b})' for a, b in pts)+';\n'


def stairs(n):
    pts = [(0, 0)]
    for i in range(n):
        pts.extend([((i+1)*160/n, i*120/n), ((i+1)*160/n, (i+1)*120/n)])
    return pts


def diagram(y=45, paths=(), corridor=None, diag=True):
    x = 10; s = ''
    if corridor:
        d = corridor; pts = [(0, 120), (0, 120-d), (160-d/.75, 0), (160, 0), (160, d), (d/.75, 120)]
        s += BS+'fill[gray!20] '+' -- '.join(f'({x+a},{y+b})' for a, b in pts)+' -- cycle;\n'
    s += rect(x, y, 160, 120, 'gray!25,line width=.4pt')
    if diag:
        s += line(x, y+120, x+160, y, 'densely dotted,line width=.8pt')
    for pts, opts in paths:
        s += path(x, y, pts, opts)
    s += circle(x, y+120, 1.4, 'fill=black')+circle(x+160, y, 1.4, 'fill=black')
    s += label(x-4, y+124, 'S', 11)+label(x+164, y-2, 'F', 11)
    s += label(x+80, y+128, '160 mm', 11)+(BS+'node[rotate=90,font='+BS+'small] at ('+str(x-7)+','+str(y+60)+') {120 mm};'+chr(10))
    return s


def calibration(y=221):
    return line(10, y, 110, y, 'line width=.7pt')+line(10, y-2, 10, y+2)+line(110, y-2, 110, y+2)+label(60, y+6, '100 mm', 10)


def example():
    s = text(0, 0, 'A staircase goes only right and up. Measure along all its pieces.', size=12)
    s += rect(15, 26, 40, 30, 'gray!60')
    pts = [(15, 56), (25, 56), (25, 36), (55, 36), (55, 26)]
    for a, b in zip(pts, pts[1:]):
        s += line(*a, *b, 'line width=1pt')
    for x, y, t in [(20, 61, 'A: 10'), (17, 45, 'C: 20'), (40, 31, 'B: 30'), (63, 30, 'D: 10')]:
        s += label(x, y, t, 9)
    s += line(73, 43, 86, 43, '-{Stealth[length=2mm]}')
    s += rect(96, 28, 10, 7, 'fill=gray!15')+rect(106, 28, 30, 7, 'fill=gray!15')
    s += label(101, 31.5, 'A', 9)+label(121, 31.5, 'B', 9)+label(145, 31.5, '40 mm', 10)
    s += rect(96, 48, 20, 7, 'fill=gray!15')+rect(116, 48, 10, 7, 'fill=gray!15')
    s += label(106, 51.5, 'C', 9)+label(121, 51.5, 'D', 9)+label(145, 51.5, '30 mm', 10)
    s += label(117, 23, 'right pieces', 10)+label(116, 43, 'up pieces', 10)
    return s


LEFT_ONCE = [(0, 0), (80, 0), (80, 40), (40, 40), (40, 80), (160, 80), (160, 120)]


def left_once(y=42):
    s = diagram(y, [(LEFT_ONCE, 'line width=1.2pt')])
    # Mark the route's essential segment lengths without requiring ruler accuracy.
    for x, yy, t in [(50, 157, '80'), (96, 142, '40'), (70, 128, '40'), (44, 102, '40'), (110, 76, '120'), (177, 61, '40')]:
        s += label(x, yy, t, 10)
    return s


# The eight-turn witness in the ±15 mm strip, used by the adult key.
EIGHT_TURNS = [(0, 0), (20, 0), (20, 30), (60, 30), (60, 60), (100, 60), (100, 90), (140, 90), (140, 120), (160, 120)]
