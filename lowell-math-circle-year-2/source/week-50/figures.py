"""Week 50 figures, carried over from the old student builder (make.py, archived in
archive-before-problem-files-2026-10-23/).

Coordinates are millimetres on the 185 x 235 mm page canvas, y downward. Problem
files call these by name in their `figure` sections.
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
    # The pieces are lettered in path order (October 23, 2026; before, A and B were the
    # right pieces and C and D the up pieces, in two bars). B's label sits beside B.
    for x, y, t in [(20, 61, 'A: 10'), (31, 46, 'B: 20'), (40, 31, 'C: 30'), (63, 30, 'D: 10')]:
        s += label(x, y, t, 9)
    s += line(73, 43, 86, 43, '-{Stealth[length=2mm]}')
    # One 70 mm bar: the pieces end to end, in path order.
    x = 93
    for t, w in (('A', 10), ('B', 20), ('C', 30), ('D', 10)):
        s += rect(x, 39.5, w, 7, 'fill=gray!15')+label(x+w/2, 43, t, 9)
        x += w
    s += label(128, 34.5, 'the pieces in a row', 10)+label(x+10, 43, '70 mm', 10)
    return s


LEFT_ONCE = [(0, 0), (80, 0), (80, 40), (40, 40), (40, 80), (160, 80), (160, 120)]


def left_once(y=42):
    s = diagram(y, [(LEFT_ONCE, 'line width=1.2pt')])
    # Mark the route's essential segment lengths without requiring ruler accuracy.
    for x, yy, t in [(50, 157, '80'), (96, 142, '40'), (70, 128, '40'), (44, 102, '40'), (110, 76, '120'), (177, 61, '40')]:
        s += label(x, yy, t, 10)
    return s
