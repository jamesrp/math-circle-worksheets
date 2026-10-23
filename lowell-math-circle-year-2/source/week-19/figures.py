"""Week 19 (No card inside another): drawing code and page template for the problem files.

Carried over unchanged from the old student builder (archive-before-problem-files-2026-10-23/
build_packets.py, class Packet): inches with y measured down from the top-left page corner,
Latin Modern, and each page an overlay on the whole sheet that draws its own header, rule,
footer and page number. Every item ends with a newline, so a page's LaTeX is the old
builder's byte for byte. The figure functions return the LaTeX of the old builder's
deck(), card(), row_example() and line() calls.
"""
from math import cos, sin, pi

# Four and eight-card decks are not shown in rank order.
D4 = [0, 3, 1, 2]
D8 = [5, 0, 2, 7, 1, 6, 3, 4]
D16 = [5, 10, 0, 7, 12, 1, 14, 3, 8, 6, 15, 9, 2, 13, 4, 11]

PRE = r'''\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.65in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage{tikz}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000\exhyphenpenalty=10000
\begin{document}
'''


class Items:
    """A list of TikZ items, drawn by the old builder's Packet methods."""

    def __init__(self):
        self.items = []

    def out(self):
        return ''.join(s + '\n' for s in self.items)

    def raw(self, s):
        self.items.append(s)

    def text(self, x, y, w, t, size=12, align='left'):
        self.raw(rf'\node[anchor=north west,inner sep=0pt,text width={w}in,align={align},font=\fontsize{{{size}}}{{{size*1.25}}}\selectfont] at ({x},{y}) {{{t}}};')

    def card(self, mask, x, y, s=.72):
        self.raw(rf'\draw[line width=.7pt,rounded corners=2pt] ({x},{y}) rectangle ({x+s},{y+s});')
        # A small mark on the border is present on every card, including the empty card.
        self.raw(rf'\draw[line width=1.5pt] ({x+.08*s},{y}) -- ({x+.16*s},{y});')
        spots = [(.28, .28), (.72, .28), (.28, .72), (.72, .72)]
        for b, (dx, dy) in enumerate(spots):
            if not (mask >> b & 1):
                continue
            a, c = x + dx * s, y + dy * s
            r = .122 * s
            if b == 0:
                self.raw(rf'\draw[line width=.95pt] ({a},{c}) circle[radius={r}in];')
            if b == 1:
                self.raw(rf'\draw[line width=.95pt,line join=round] ({a},{c-r*1.15})--({a+r*1.1},{c+r*.85})--({a-r*1.1},{c+r*.85})--cycle;')
            if b == 2:
                self.raw(rf'\draw[line width=.95pt] ({a-r},{c-r}) rectangle ({a+r},{c+r});')
            if b == 3:
                pts = []
                for k in range(10):
                    rr = r * (1.3 if k % 2 == 0 else .54)
                    ang = -pi / 2 + k * pi / 5
                    pts.append(f'({a+rr*cos(ang):.5f},{c+rr*sin(ang):.5f})')
                self.raw(r'\draw[line width=.85pt,line join=round] ' + '--'.join(pts) + '--cycle;')

    def deck(self, masks, y, cols=None, s=.72, gap=.24, x=None):
        cols = cols or len(masks)
        w = cols * s + (cols - 1) * gap
        x = (8.5 - w) / 2 if x is None else x
        for i, m in enumerate(masks):
            self.card(m, x + (i % cols) * (s + gap), y + (i // cols) * (s + gap), s)

    def row_example(self):
        self.card(1, 1.0, 2.06, .62)
        self.card(3, 2.43, 2.06, .62)
        self.raw(r'\draw[-stealth,line width=.8pt] (1.74,2.37)--(2.30,2.37);')
        self.text(3.40, 2.02, 4.1, 'Example of one nested row: the first card fits inside the next. This is not a whole-deck arrangement.', size=12)

    def line(self, y):
        self.raw(rf'\draw[black!22,line width=.35pt] (.65,{y})--(7.85,{y});')


def _draw(method, *args, **kw):
    i = Items()
    getattr(i, method)(*args, **kw)
    return i.out()


def deck(masks, y, **kw):
    """A row (or grid) of cards, centred unless x is given."""
    return _draw('deck', masks, y, **kw)


def row_example():
    """The two-card nested-row example before each band's first row task."""
    return _draw('row_example')


def line(y):
    """A light rule between two problems on one page."""
    return _draw('line', y)


# ---- page template -----------------------------------------------------------------------

def page_preamble(week, topic, header, footer):
    return PRE


def page_open(page):
    i = Items()
    i.raw(r'\begin{tikzpicture}[remember picture,overlay]\begin{scope}[shift={(current page.north west)},x=1in,y=-1in]')
    i.text(.65, .41, 7.2, f'Week {page.week} / {page.topic} / {page.header}', size=11)
    i.raw(r'\draw[line width=.35pt] (.65,.70)--(7.85,.70);')
    i.text(.65, 10.43, 6.7, f'Bellingham Math Circle / Week {page.week} / {page.footer}', size=9)
    i.text(7.3, 10.43, .55, str(page.number), size=9, align='right')
    return i.out()


def page_close(page):
    return r'\end{scope}\end{tikzpicture}\mbox{}' + '\n'


def page_prompt(n, body, x, y, size):
    return _draw('text', .65 if x is None else x, y, 7.2, rf'\textbf{{Problem {n}:}} {body}', size=size)


def page_text(x, y, body, w, size):
    return _draw('text', .65 if x is None else x, y, 7.2 if w is None else w, body, size=size)
