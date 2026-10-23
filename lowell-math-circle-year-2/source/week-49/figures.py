"""Week 49 figures, carried over from the old builder
(archive-before-problem-files-2026-10-23/make.py and draw.py).

Coordinates are millimetres on the house 185 x 235 mm page canvas, y downward, so the
default page template in problem-files/canvas.py is the old builder's page. Problem
files call these functions by name in their `figure` sections; the wording lives in
the problem files.
"""
import math
from canvas import text, label, line, rect, circle


def ring(x, y, vals=None, span=42, r=7, gaps=False, letters=True, squares=False):
    """Four stations at the corners of a square (or three at a triangle's), with arrows
    from each station to the next; squares=True draws the cube mats."""
    vals = vals if vals is not None else [None]*4; n = len(vals)
    pts = [(x, y), (x+span, y), (x+span, y+span), (x, y+span)] if n == 4 else [(x+span/2, y), (x+span, y+span), (x, y+span)]
    s = ''; names = 'ABCD'
    for i, (a, b) in enumerate(pts):
        c, d = pts[(i+1) % n]; dist = math.hypot(c-a, d-b); vx = (c-a)/dist; vy = (d-b)/dist
        edge = (r/max(abs(vx), abs(vy))+1) if squares else (r+1)
        s += line(a+vx*edge, b+vy*edge, c-vx*edge, d-vy*edge, '-{Stealth[length=2mm]}')
        if gaps:
            if n == 4: offs = [(0, -5), (8, 0), (0, 5), (-8, 0)][i]
            else: offs = [(7, -2), (0, 6), (-7, -2)][i]
            s += label((a+c)/2+offs[0], (b+d)/2+offs[1], str(abs(vals[i]-vals[(i+1) % n])), 11)
    for i, (a, b) in enumerate(pts):
        if squares: s += rect(a-r, b-r, r*2, r*2, 'fill=white,rounded corners=1mm')
        else: s += circle(a, b, r, 'fill=white')
        if letters: s += label(a, b+r+4 if (i >= 2 if n == 4 else i >= 1) else b-r-4, names[i], 9)
        if vals[i] is not None: s += label(a, b, str(vals[i]), 13)
    return s


def record(x, y, vals=None):
    """One A-B-C-D row of record boxes."""
    vals = vals or ['']*4; s = ''
    for i, v in enumerate(vals):
        s += rect(x+i*14, y, 14, 11)+label(x+i*14+7, y+5.5, str(v), 12)
        s += label(x+i*14+7, y-4, 'ABCD'[i], 9)
    return s


def mats(y=60):
    """The paired old and new four-station cube mats: 36 mm stations, centres 52 mm
    apart, a 9 mm gap between the mats and the page-1 arrow from old to new."""
    return (ring(18, y, None, 52, 18, squares=True)+ring(115, y, None, 52, 18, squares=True)
            + line(78, y+26, 107, y+26, '-{Stealth[length=3mm]}'))


def moves_row(x, y, tx, w):
    """A record row with a moves-to-zero answer line beside it."""
    return record(x, y)+text(tx, y, r'Moves to zero: \rule{17mm}{.3pt}', w=w, size=12)


def worked_example():
    """Page 1: the old ring (1,4,2,0) with its gaps on the arrows, and the new ring."""
    return (label(41, 37, 'old', 12)+label(144, 37, 'new', 12)
            + ring(20, 52, [1, 4, 2, 0], 42, 7, True)+line(78, 73, 105, 73, '-{Stealth[length=3mm]}')+ring(122, 52, [3, 2, 2, 1], 42, 7))


def four_starts():
    """Problem 1's four starts, small."""
    s = ''
    for x, vs in zip([13, 60, 107, 154], [[1, 1, 0, 0], [1, 0, 1, 0], [2, 1, 0, 1], [0, 0, 0, 2]]):
        s += ring(x, 177, vs, 25, 5, letters=False)
    return s


def big_mats():
    """Page 2: the labelled old and new four-station mats."""
    return label(44, 43, 'old', 12)+label(141, 43, 'new', 12)+mats(71)


def three_station_mats(y=104):
    """The three-station starts' labelled old and new mats, spaced as the four-station ones."""
    return (label(44, y-28, 'old', 12)+label(141, y-28, 'new', 12)
            + ring(18, y, [None]*3, 52, 18, squares=True)+ring(115, y, [None]*3, 52, 18, squares=True)
            + line(70, y, 111, y, '-{Stealth[length=3mm]}'))


def abc_rows(x, y, first=1, n=3):
    """A block of A-B-C record rows, numbered by move."""
    s = ''
    for i in range(3):
        s += label(x+i*14+7, y-4, 'ABC'[i], 9)
    for r in range(n):
        s += label(x-6, y+r*11+5.5, str(first+r), 10)
        for i in range(3):
            s += rect(x+i*14, y+r*11, 14, 11)
    return s


def three_station_records(y=190):
    """Six numbered A-B-C rows for the three-station run, in two blocks."""
    return abc_rows(30, y, 1)+abc_rows(120, y, 4)


def old_row(x, y):
    """A four-box row for an old ring, labelled old."""
    return label(x-8, y+5.5, 'old', 10)+record(x, y)


def letter_runs(y):
    """Four columns of A-B-C-D letter boxes, each a start (move 0) and four moves."""
    s = label(5, y-4, 'move', 8)
    for r in range(5):
        s += label(5, y+r*9+4.5, str(r), 10)
    for c in range(4):
        x = 14+c*44
        for i in range(4):
            s += label(x+i*9+4.5, y-4, 'ABCD'[i], 9)
            for r in range(5):
                s += rect(x+i*9, y+r*9, 9, 9)
    return s
