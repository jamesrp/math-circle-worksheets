"""Write materials.tex: the printable objects for "Patterns you cannot avoid".

Run: ./build.sh  (writes materials.tex, compiles it twice, checks the log, measures the PDF)

Every coordinate is in millimetres on the paper, y measured down from the top edge, with equal
scaling on both axes (TikZ x=1mm, y=-1mm), so the drawn sizes are the printed sizes at 100%.

Pages
  1  Combs 1-4 (landscape)                 all bands: K-1 pages, and the playing strips of page 2
  2  Strips of 6, 7, 8 and 9 squares        Grades 2-3 and 4-5 Problems 1-3, counter work
  3  Cards 1 to 15, launch strip of 5       Grades 2-3 Problems 4, 5, 8; Grades 4-5 Problems 4, 9, 10
  4  Boards of six dots, 12 cm (landscape)  Sim: Grades 2-3 Problem 7, Grades 4-5 Problems 6-8
"""
import math
from pathlib import Path

WEEK = 'NN'
TOPIC = 'Patterns you cannot avoid'
PID = f'{WEEK}-M-v1'

PORTRAIT = (215.9, 279.4)
LANDSCAPE = (279.4, 215.9)
SIDE = 15.0          # left and right margin of header, footer and content

# Sizes taken from the outline and the student pages.
SQ = 25.0            # strip square: the K-1 pages draw 2.5 cm squares; outline: 25 mm
COMB_END = 5.0       # card beyond the outer squares (guide: 5 mm from the end)
WINDOW = 23.0        # window width, centred on a 25 mm square: a 22 mm counter shows whole within
                     # 0.5 mm of alignment, and its neighbours stay hidden within 2.5 mm
COMB_H = 34.0        # comb height: laid over a strip it reaches 9 mm above it, short of the counters
                     # on the strip above (K-1 strips are 11 mm apart at the closest)
COMB_DEPTH = 27.0    # notch depth: a whole 25 mm square shows in each window
CARD_W, CARD_H = 36.0, 48.0
CARD_CIRCLE_D = 26.0  # counter spot; counters no wider than 22 mm (guide)
SIX_DIAM = 120.0     # outline: dots on a circle about 12 cm across


def f(x):
    return f'{x:.3f}'


def text(x, y, s, size=11, anchor='north west', extra=''):
    return (rf'\node[anchor={anchor},inner sep=0,font=\fontsize{{{size}}}{{{size * 1.2:.1f}}}\selectfont{extra}] '
            rf'at ({f(x)},{f(y)}) {{{s}}};')


class Doc:
    def __init__(self):
        self.pages = []

    def add(self, body, title, size):
        w, h = size
        n = len(self.pages) + 1
        head = [
            text(SIDE, 12.6, f'Week {WEEK} / {TOPIC} / Materials', 11),
            rf'\draw[gray] ({f(SIDE)},19.5) -- ({f(w - SIDE)},19.5);',
            text(SIDE, 24, title, 16),
            rf'\draw[gray] ({f(SIDE)},{f(h - 20)}) -- ({f(w - SIDE)},{f(h - 20)});',
            text(SIDE, h - 14.5, f'Bellingham Math Circle / Week {WEEK} / {PID}', 9, 'base west'),
            text(w - SIDE, h - 14.5, str(n), 9, 'base east'),
        ]
        self.pages.append((size, '\n'.join(head + body)))

    def tex(self):
        out = [r'''\documentclass[12pt]{article}
\usepackage[letterpaper,margin=0mm]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand\familydefault{\sfdefault}
\pagestyle{empty}
\setlength\parindent{0pt}
\pdfinfoomitdate=1\pdftrailerid{}\pdfsuppressptexinfo=15
\begin{document}''']
        for (w, h), body in self.pages:
            out.append(rf'\paperwidth={w}mm\paperheight={h}mm\pdfpagewidth={w}mm\pdfpageheight={h}mm'
                       r'\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm,'
                       r'shift={(current page.north west)}]')
            out.append(body)
            out.append(r'\end{tikzpicture}\null\newpage')
        out.append(r'\end{document}')
        return '\n'.join(out) + '\n'


# ---------------------------------------------------------------- objects
def comb_length(d):
    return (2 * d + 1) * SQ + 2 * COMB_END


def comb_windows(d):
    """Window (notch) intervals measured from the comb's left edge, each centred on a square."""
    inset = (SQ - WINDOW) / 2
    if d == 1:
        return [(COMB_END + inset, COMB_END + 3 * SQ - inset)]   # the three windows join into one notch
    return [(COMB_END + k * d * SQ + inset, COMB_END + k * d * SQ + SQ - inset) for k in range(3)]


def comb(x0, y0, d):
    """A comb with its notches opening downward, so it lies over a strip with its label above."""
    L, h = comb_length(d), COMB_H
    pts = [(x0, y0), (x0 + L, y0), (x0 + L, y0 + h)]
    for a, b in reversed(comb_windows(d)):
        pts += [(x0 + b, y0 + h), (x0 + b, y0 + h - COMB_DEPTH), (x0 + a, y0 + h - COMB_DEPTH), (x0 + a, y0 + h)]
    pts.append((x0, y0 + h))
    path = ' -- '.join(f'({f(x)},{f(y)})' for x, y in pts) + ' -- cycle'
    spine = h - COMB_DEPTH
    return '\n'.join([rf'\filldraw[fill=gray!35, line width=0.6pt] {path};',
                      text(x0 + L / 2, y0 + spine / 2 + 0.2, rf'\bfseries Comb {d}', 10, 'center')])


def strip(x0, y0, n, s=SQ):
    """A numbered strip of n squares, drawn like the K-1 pages (numbers under the squares)."""
    out = []
    for i in range(1, n + 1):
        x = x0 + (i - 1) * s
        out.append(rf'\draw[line width=0.9pt] ({f(x)},{f(y0)}) rectangle ({f(x + s)},{f(y0 + s)});')
        out.append(text(x + s / 2, y0 + s + 5.2, str(i), 12, 'base'))
    return '\n'.join(out)


def cards(x0, y0, nums, cols):
    """Number cards on shared cut lines: a counter spot with the number underneath, as on the page rows."""
    rows = math.ceil(len(nums) / cols)
    out = []
    for k, m in enumerate(nums):
        r, c = divmod(k, cols)
        x, y = x0 + c * CARD_W, y0 + r * CARD_H
        out.append(rf'\draw[line width=0.9pt] ({f(x + CARD_W / 2)},{f(y + 4 + CARD_CIRCLE_D / 2)}) '
                   rf'circle ({f(CARD_CIRCLE_D / 2)});')
        out.append(text(x + CARD_W / 2, y + 42.0, rf'\bfseries {m}', 18, 'base'))
    for c in range(cols + 1):
        out.append(rf'\draw[line width=0.5pt] ({f(x0 + c * CARD_W)},{f(y0)}) -- ({f(x0 + c * CARD_W)},{f(y0 + rows * CARD_H)});')
    for r in range(rows + 1):
        out.append(rf'\draw[line width=0.5pt] ({f(x0)},{f(y0 + r * CARD_H)}) -- ({f(x0 + cols * CARD_W)},{f(y0 + r * CARD_H)});')
    return '\n'.join(out)


def dot_points(n, diam, cx, cy):
    """n dots on a circle, the first at the top, as on the student pages (counterclockwise)."""
    r = diam / 2
    return [(cx + r * math.cos(math.pi / 2 + 2 * math.pi * k / n),
             cy - r * math.sin(math.pi / 2 + 2 * math.pi * k / n)) for k in range(n)]


def dots_board(n, diam, cx, cy):
    pts = dot_points(n, diam, cx, cy)
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            out.append(rf'\draw[gray!55, line width=0.8pt] ({f(pts[i][0])},{f(pts[i][1])}) -- '
                       rf'({f(pts[j][0])},{f(pts[j][1])});')
    for x, y in pts:
        out.append(rf'\fill ({f(x)},{f(y)}) circle (1.5);')
    return '\n'.join(out)


def scale_bar(x, y, length=100):
    return '\n'.join([rf'\draw[line width=0.6pt] ({f(x)},{f(y)}) -- ({f(x + length)},{f(y)});',
                      rf'\draw[line width=0.6pt] ({f(x)},{f(y - 2.5)}) -- ({f(x)},{f(y + 2.5)});',
                      rf'\draw[line width=0.6pt] ({f(x + length)},{f(y - 2.5)}) -- ({f(x + length)},{f(y + 2.5)});',
                      text(x + length + 4, y, f'{length} mm', 9, 'west')])


# ---------------------------------------------------------------- pages
def build():
    D = Doc()
    W, H = LANDSCAPE

    # Page 1: one set of four combs.
    b = []
    rows = [[4], [3], [2, 1]]
    gap_x, y = 10.0, 34.0
    for row in rows:
        width = sum(comb_length(d) for d in row) + gap_x * (len(row) - 1)
        x = (W - width) / 2
        for d in row:
            b.append(comb(x, y, d))
            x += comb_length(d) + gap_x
        y += COMB_H + 9.0
    b.append(scale_bar((W - comb_length(4)) / 2, 178.0))
    D.add(b, 'Combs', LANDSCAPE)

    # Page 2: playing-size strips for the older tables (the lengths of their Problem 1).
    b = []
    x0 = (W - 9 * SQ) / 2
    for k, n in enumerate((6, 7, 8, 9)):
        b.append(strip(x0, 35.0 + 40.0 * k, n))
    D.add(b, 'Strips of 6, 7, 8 and 9 squares', LANDSCAPE)

    # Page 3: cards 1 to 15 and the launch strip.
    W, H = PORTRAIT
    b = []
    x0 = (W - 5 * CARD_W) / 2
    b.append(cards(x0, 34.0, list(range(1, 16)), 5))
    b.append(text(x0, 192.0, 'Launch strip of 5 squares', 11))
    b.append(strip(x0, 199.0, 5))
    D.add(b, 'Cards 1 to 15', PORTRAIT)

    # Page 4: two boards of six dots for Sim.
    W, H = LANDSCAPE
    b = []
    half_w = SIX_DIAM / 2 * math.cos(math.pi / 6)
    gap = 30.0
    cy = 46.0 + SIX_DIAM / 2
    for cx in (W / 2 - gap / 2 - half_w, W / 2 + gap / 2 + half_w):
        b.append(dots_board(6, SIX_DIAM, cx, cy))
    D.add(b, 'Boards of six dots', LANDSCAPE)
    return D


if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    (here / 'materials.tex').write_text(build().tex())
    print('wrote materials.tex')
