#!/usr/bin/env python3
"""Build the Week 23 table kit: a four-lane mat, cards, comparator bars.

Usage: python3 materials/build_materials.py [output-folder]   (default: build)

Every size is in millimetres and is set in the constants below. The script
writes materials/materials.tex and runs pdflatex twice into the output
folder. Check the result with materials/verify_materials.py.
"""
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# Sizes (mm). The review card asked for lanes about 45 mm apart, 3.5 cm cards
# and 3.5 cm start and finish boxes; boxes are 38 mm so a 35 mm card drops in.
LANE_GAP = 45.0
CARD = 35.0
BOX = 38.0
BAR_W = 14.0            # width of a comparator bar strip
BAR_END = 7.0           # end-dot centre to strip end
DOT_R = 3.0             # end-dot radius
BAR_SPANS = {1: 8, 2: 4, 3: 2}   # bars per table by lanes spanned
TIME_STRIP = 190.0      # length of the time strip
LETTER = (215.9, 279.4)
LANDSCAPE = (279.4, 215.9)
LANES_Y = [48.5 + LANE_GAP * i for i in range(4)]

# Mat seam: the right half is cut on its dashed line at x = CUT and laid on
# the left half's dashed line at x = JOIN, so right-half x maps to x + JOIN - CUT.
JOIN = 255.0
CUT = 15.0
START_X = 20.0          # left edge of the start boxes (left half)
FINISH_X = 225.0        # left edge of the finish boxes (right half)

HEADER = 'Week 23 / Sorting machines / Materials'
PACKET = 'W23-M-v1'

DOTS = {0: [], 1: [(0, 0)], 2: [(-8, 0), (8, 0)],
        3: [(-8, 6.5), (8, 6.5), (0, -8)],
        4: [(-8, -8), (8, -8), (-8, 8), (8, 8)]}
DOT_CARDS = [0, 0, 1, 1, 2, 3, 4]
NUMBER_ROWS = [['1', '2', '3', '4'], ['1', '2', '3', '4'],
               ['0', '0', '0', '0'], ['1', '1', '1', '1']]
GRAY_ROWS = {2, 3}      # the 0-1 set is printed on gray

PRE = r'''\documentclass{article}
\usepackage[paperwidth=215.9mm,paperheight=279.4mm,margin=0mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\ifdefined\pdfinfoomitdate\pdfinfoomitdate=1\fi
\ifdefined\pdftrailerid\pdftrailerid{}\fi
\ifdefined\pdfsuppressptexinfo\pdfsuppressptexinfo=15\fi
\begin{document}
'''


def f(v):
    return f'{v:.3f}'.rstrip('0').rstrip('.')


class Page:
    def __init__(self, size, heading, number, left=10):
        self.w, self.h = size
        self.cmd = []
        self.size = size
        landscape = self.w > self.h
        self.text(left, 6, HEADER, 10)
        self.cmd.append(rf'\draw[line width=.5pt] ({f(left)},11.5) -- ({f(self.w - 10)},11.5);')
        self.text(left, 14, heading, 10.5, width=(self.w - 120 - left) if landscape else (self.w - 10 - left))
        if landscape:
            self.scale_check(self.w - 110, 20, label_above=True)
        else:
            self.scale_check(left, 27)
        self.text(left, self.h - 9, f'Bellingham Math Circle / Week 23 / {PACKET}', 9)
        self.text(self.w - 14, self.h - 9, str(number), 9, width=4)

    def text(self, x, y, s, size, width=None, anchor='north west', extra=''):
        w = f',text width={f(width)}mm' if width else ''
        self.cmd.append(rf'\node[anchor={anchor},inner sep=0pt,align=left{w},'
                        rf'font=\fontsize{{{size}}}{{{size * 1.22:.1f}}}\selectfont{extra}] '
                        rf'at ({f(x)},{f(y)}) {{{s}}};')

    def scale_check(self, x, y, label_above=False):
        self.cmd.append(rf'\draw[line width=.8pt] ({f(x)},{f(y)}) -- ({f(x + 100)},{f(y)});')
        for xx in (x, x + 100):
            self.cmd.append(rf'\draw[line width=.8pt] ({f(xx)},{f(y - 2)}) -- ({f(xx)},{f(y + 2)});')
        label = '10 cm scale check: measure before cutting'
        if label_above:
            self.text(x + 50, y - 2.5, label, 8, anchor='south')
        else:
            self.text(x + 103, y, label, 8, anchor='west')

    def rect(self, x, y, w, h, style='line width=.5pt'):
        self.cmd.append(rf'\draw[{style}] ({f(x)},{f(y)}) rectangle ({f(x + w)},{f(y + h)});')

    def tex(self):
        w, h = self.size
        dims = (rf'\pdfpagewidth={w}mm \pdfpageheight={h}mm '
                rf'\paperwidth={w}mm \paperheight={h}mm' + '\n')
        return (dims + r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]' + '\n'
                + r'\begin{scope}[shift={(current page.north west)}]' + '\n'
                + '\n'.join(self.cmd) + '\n' + r'\end{scope}\end{tikzpicture}' + '\n')


def lane_labels(p, x):
    for i, y in enumerate(LANES_Y):
        p.text(x, y, rf'\textbf{{{i + 1}}}', 16, anchor='center')


def mat_left(n):
    p = Page(LANDSCAPE, r'\textbf{Four-lane mat, left half. Print 1 per table} (paper or card stock). '
             r'Tape the right half over the gray strip; the lanes must meet.', n)
    p.text(START_X, LANES_Y[0] - BOX / 2 - 1.5, 'Start', 10, anchor='south west')
    p.cmd.append(rf'\fill[black!12] ({f(JOIN)},{f(LANES_Y[0] - BOX / 2)}) rectangle '
                 rf'({f(p.w - 10)},{f(LANES_Y[-1] + BOX / 2)});')
    p.cmd.append(rf'\draw[dashed,line width=.6pt] ({f(JOIN)},{f(LANES_Y[0] - BOX / 2 - 4)}) -- '
                 rf'({f(JOIN)},{f(LANES_Y[-1] + BOX / 2 + 4)});')
    p.text(p.w / 2, p.h - 9, 'Physically unrehearsed: sizes are checked digitally; nobody has built and used this kit yet.',
           8, anchor='north')
    lane_labels(p, 13)
    for y in LANES_Y:
        p.rect(START_X, y - BOX / 2, BOX, BOX, 'line width=.8pt')
        p.cmd.append(rf'\draw[line width=1.2pt] ({f(START_X + BOX)},{f(y)}) -- ({f(p.w - 10)},{f(y)});')
    return p


def mat_right(n):
    p = Page(LANDSCAPE, r'\textbf{Four-lane mat, right half. Print 1 per table.} Cut on the dashed line '
             r'at the left. Lay that edge on the left half\textquoteright s dashed line, lanes meeting, and tape.', n,
             left=CUT + 5)
    p.cmd.append(rf'\draw[dashed,line width=.8pt] ({f(CUT)},4) -- ({f(CUT)},{f(p.h - 4)});')
    p.text(FINISH_X, LANES_Y[0] - BOX / 2 - 1.5, 'Finish', 10, anchor='south west')
    for y in LANES_Y:
        p.cmd.append(rf'\draw[line width=1.2pt,-{{Stealth[length=4mm,width=3mm]}}] ({f(CUT)},{f(y)}) -- '
                     rf'({f(FINISH_X)},{f(y)});')
        p.rect(FINISH_X, y - BOX / 2, BOX, BOX, 'line width=.8pt')
    lane_labels(p, FINISH_X + BOX + 5)
    return p


def dot_card(p, x, y, n):
    p.rect(x, y, CARD, CARD)
    cx, cy = x + CARD / 2, y + CARD / 2
    for dx, dy in DOTS[n]:
        p.cmd.append(rf'\fill ({f(cx + dx)},{f(cy + dy)}) circle[radius={f(DOT_R)}];')


def number_card(p, x, y, s, gray):
    if gray:
        p.cmd.append(rf'\fill[black!15] ({f(x)},{f(y)}) rectangle ({f(x + CARD)},{f(y + CARD)});')
    p.rect(x, y, CARD, CARD)
    p.text(x + CARD / 2, y + CARD / 2, rf'\textbf{{{s}}}', 60, anchor='center')


def cards(n):
    p = Page(LETTER, r'\textbf{Cards. Print 1 per table on card stock.} The K--1 table cuts the dot cards; '
             r'the Grades 2--3 and 4--5 tables cut the number cards. Cut on the lines.', n)
    x0 = (LETTER[0] - 4 * CARD) / 2
    y0 = 38
    p.text(x0, y0 - 2, r'Dot cards for the K--1 table: two blank, two with 1 dot, one each with 2, 3 and 4 dots',
           9, anchor='south west')
    for i, d in enumerate(DOT_CARDS):
        dot_card(p, x0 + (i % 4) * CARD, y0 + (i // 4) * CARD, d)
    y1 = y0 + 2 * CARD + 14
    p.text(x0, y1 - 2, r'Number cards for the Grades 2--5 tables: 1 to 4 twice, and the gray 0--1 set (four 0s, four 1s)',
           9, anchor='south west')
    for r, row in enumerate(NUMBER_ROWS):
        for c, s in enumerate(row):
            number_card(p, x0 + c * CARD, y1 + r * CARD, s, r in GRAY_ROWS)
    return p


def bar(p, x, y, span):
    length = LANE_GAP * span + 2 * BAR_END
    p.rect(x, y, BAR_W, length)
    cx = x + BAR_W / 2
    a, b = y + BAR_END, y + length - BAR_END
    p.cmd.append(rf'\draw[line width=1.5mm] ({f(cx)},{f(a)}) -- ({f(cx)},{f(b)});')
    for yy in (a, b):
        p.cmd.append(rf'\fill ({f(cx)},{f(yy)}) circle[radius={f(DOT_R)}];')
    return length


def bar_columns():
    """Columns of vertical bars that share cut lines, longest first."""
    left = dict(BAR_SPANS)
    cols = []
    for pattern in ([3, 1], [3, 1], [2, 2], [2, 2], [1, 1, 1], [1, 1, 1]):
        for s in pattern:
            left[s] -= 1
        cols.append(pattern)
    assert all(v == 0 for v in left.values()), left
    return cols


def bars(n):
    p = Page(LETTER, r'\textbf{Comparator bars and time strip. Print 1 per table on card stock.} '
             r'8 bars join neighboring lanes, 4 skip a lane, 2 join lane 1 to lane 4. '
             r'Spares are on purpose. Cut on the lines.', n)
    cols = bar_columns()
    total_w = (len(cols) + 1) * BAR_W
    x0 = (LETTER[0] - total_w) / 2
    y0 = 36
    for i, pattern in enumerate(cols):
        y = y0
        for s in pattern:
            y += bar(p, x0 + i * BAR_W, y, s)
    xt = x0 + len(cols) * BAR_W
    p.cmd.append(rf'\fill[black!12] ({f(xt)},{f(y0)}) rectangle ({f(xt + BAR_W)},{f(y0 + TIME_STRIP)});')
    p.rect(xt, y0, BAR_W, TIME_STRIP)
    p.text(xt + BAR_W / 2, y0 + TIME_STRIP / 2, 'time strip', 10, anchor='center', extra=',rotate=90')
    return p


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build'
    if not out.is_absolute():
        out = ROOT / out
    out.mkdir(parents=True, exist_ok=True)
    pages = [mat_left(1), mat_right(2), cards(3), bars(4)]
    tex = PRE + r'\newpage'.join(p.tex() for p in pages) + r'\end{document}' + '\n'
    src = HERE / 'materials.tex'
    src.write_text(tex)
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                            f'-output-directory={out}', str(src)], capture_output=True, text=True)
        if r.returncode:
            sys.stdout.write(r.stdout[-3000:])
            raise SystemExit('pdflatex failed')
    print(f'Built {out / "materials.pdf"}: {len(pages)} pages.')


if __name__ == '__main__':
    main()
