"""Week 47 figures, carried over from the old builder
(archive-before-problem-files-2026-10-23/make.py, draw.py and examples.py).

Coordinates are millimetres on the house 185 x 235 mm page canvas, y downward, so the
default page template in problem-files/canvas.py is the old builder's page. Problem
files call these functions by name in their `figure` sections; the wording lives in
the problem files.
"""
from canvas import text, label, line, rect, circle, prob

STATE = {'width': None}


def prompt_width(w):
    """Set the text width of the next numbered prompt (the old Problem 1 was 113 mm wide,
    beside the 'jump too big' picture). Draws nothing."""
    STATE['width'] = w
    return ''


def page_prompt(n, body, x, y, size):
    """A numbered prompt at the left margin, as the old builder's prob()."""
    w, STATE['width'] = STATE['width'], None
    if w is not None:
        return text(0, y or 0, rf'\textbf{{Problem {n}:}} '+body, w=w, size=size or 13)
    return prob(n, body, y or 0, size=size or 13)


def board(x, y, n=7, H=5, clues=None, star=None, dx=22, dy=20):
    """A board of n sites and levels 0..H; clues {site: height} are black discs."""
    clues = clues or {}; s = ''
    for h in range(H+1):
        s += line(x-6, y+(H-h)*dy, x+(n-1)*dx+6, y+(H-h)*dy, 'gray!45')
        s += label(x-12, y+(H-h)*dy, str(h), 11)
    for i in range(n):
        s += line(x+i*dx, y, x+i*dx, y+H*dy, 'gray!45')
        for h in range(H+1): s += circle(x+i*dx, y+(H-h)*dy, .8, 'fill=white')
        s += label(x+i*dx, y+H*dy+9, str(i), 11)
        if i in clues:
            h = clues[i]; s += circle(x+i*dx, y+(H-h)*dy, 5, 'fill=black')
            s += label(x+i*dx, y+(H-h)*dy, rf'\color{{white}}{h}', 11)
        if i == star: s += label(x+i*dx, y-8, r'$\star$', 16)
    return s


def row(x, y, vals, locked=(), dx=22):
    """A row of boxes with site numbers below; locked boxes are shaded clues."""
    s = ''
    for i, v in enumerate(vals):
        s += rect(x+i*dx, y, dx-2, 12, 'rounded corners=1mm'+(',fill=gray!20' if i in locked else ''))
        s += label(x+i*dx+(dx-2)/2, y+6, '' if v is None else str(v), 13)
        s += label(x+i*dx+(dx-2)/2, y+17, str(i), 9)
    return s


def hill(x, y, hs, scale=6):
    """Block towers of the given heights, with each height below."""
    s = ''
    for i, h in enumerate(hs):
        for j in range(h): s += rect(x+i*(scale+1), y-(j+1)*scale, scale, scale, 'fill=gray!15')
        if h == 0: s += circle(x+i*(scale+1)+scale/2, y-2, 1.4)
        s += label(x+i*(scale+1)+scale/2, y+5, str(h), 10)
    return s


def height_example():
    """Page 1: towers 1, 2, 2, 1 -> one marker per column -> the boxed row."""
    s = text(0, 17, 'One marker in each column shows its tower height.', size=11)
    s += hill(15, 58, [1, 2, 2, 1])+label(28, 68, 'allowed', 11)
    for h in range(3):
        y = 58-10*h
        s += line(72, y, 114, y, 'gray!45')+label(66, y, str(h), 9)
    for i, h in enumerate((1, 2, 2, 1)):
        x = 76+11*i
        s += line(x, 38, x, 58, 'gray!45')+circle(x, 58-10*h, 2.1, 'fill=white,line width=.9pt')
        s += label(x, 64, str(i), 9)
    s += line(48, 50, 60, 50, '-{Stealth[length=2mm]},line width=.8pt')
    s += line(117, 50, 128, 50, '-{Stealth[length=2mm]},line width=.8pt')
    s += rect(133, 44, 44, 12, 'line width=.8pt')
    for i, h in enumerate((1, 2, 2, 1)):
        if i: s += line(133+11*i, 44, 133+11*i, 56, 'line width=.8pt')
        s += label(138.5+11*i, 50, str(h), 13)+label(138.5+11*i, 64, str(i), 9)
    return s


def jump_too_big():
    """Page 1, beside Problem 1: the illegal 1, 3, 2 towers."""
    return hill(142, 99, [1, 3, 2])+label(152, 110, 'jump too big', 11)


def clue_sets():
    """Problem 4: three clue sets on rows, then a five-site board."""
    s = ''
    for y, vs in [(36, [0, None, 3, None, None]), (69, [3, None, None, None, 0]), (102, [None, 0, None, 3, None])]:
        s += row(35, y, vs, tuple(i for i, v in enumerate(vs) if v is not None))
    return s+board(35, 151, 5, 3, dx=25, dy=20)


def shaded_single_clue():
    """Grades 4-5 Problem 6 (October 4 version): one clue at height 2, with the allowed
    heights at sites 1, 2, 4 and 5 shaded."""
    # example explicitly shows permitted single-clue bands, not combined envelopes
    s = board(25, 48, 7, 5, {3: 2})
    for i in [1, 2, 4, 5]:
        for h in range(max(0, 2-abs(i-3)), min(5, 2+abs(i-3))+1): s += circle(25+22*i, 48+(5-h)*20, 3, 'fill=gray!45')
    return s
