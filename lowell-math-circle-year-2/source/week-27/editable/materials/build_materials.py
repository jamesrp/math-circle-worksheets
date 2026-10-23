#!/usr/bin/env python3
"""Build the Week 27 table kit: tokens, links, tiles, markers and case cards.

Usage: python3 materials/build_materials.py [output-folder]   (default: build)

A case card holds every preference strip of one printed case, rank 1 at the
left, so nobody copies a profile by hand. The profiles come from
src/math_checks.json, the same data the student builder uses. Sizes are in
millimetres in the constants below. Check the result with
materials/verify_materials.py.
"""
from pathlib import Path
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = json.loads((ROOT / 'src' / 'math_checks.json').read_text())

ICON = 20.0         # strip icons: circle diameter and square side (guide: at least 20 mm)
PITCH = 23.0        # choice spacing inside a strip
ROW = 24.0          # strip spacing on a case card
TOKEN = 24.0        # token card side; the drawn shape is TOKEN - 2
TILE = 18.0         # K-1 letter tiles, to lay over a 20 mm strip icon
MARKER = 18.0       # already-asked markers
LINK = (90.0, 9.0)  # pairing links
LETTER = (215.9, 279.4)
LANDSCAPE = (279.4, 215.9)
HEADER = 'Week 27 / Stable pairings / Materials'
PACKET = 'W27-M-v1'

# The launch profile is printed in no packet (review card fix 2): with AY and BX
# nothing blocks; with AX and BY, A and Y block.
LAUNCH = ({'A': ['Y', 'X'], 'B': ['X', 'Y']}, {'X': ['A', 'B'], 'Y': ['A', 'B']})


def prof(key, **blank):
    left, right = DATA[key]['left'], dict(DATA[key]['right'])
    for k in blank:
        right[k] = ['', '']
    return left, right


CASES = {
    'K-1': [
        ('K--1 Problem 1, top case', prof('k_unique_mutual')),
        ('K--1 Problem 1, bottom case', prof('k_unique_shared')),
        ('K--1 Problem 2, top case', prof('k_two_stable')),
        ('K--1 Problem 2, bottom case', prof('k_unique_cross')),
        ('K--1 Problem 3, top case', prof('k_one_blocker')),
        ('K--1 Problem 3, bottom case', prof('k_unique_cross')),
        ('K--1 Problem 4, top case (Y\\textquoteright s strip is empty)', prof('k_two_stable', Y=1)),
        ('K--1 Problem 4, bottom case (Y\\textquoteright s strip is empty)',
         ({'A': ['X', 'Y'], 'B': ['X', 'Y']}, {'X': ['B', 'A'], 'Y': ['', '']})),
    ],
    '2-3': [
        ('Grades 2--3 Problem 1, top case', prof('k_unique_shared')),
        ('Grades 2--3 Problem 1, bottom case', prof('k_two_stable')),
        ('Grades 2--3 Problem 2', prof('middle_unique')),
        ('Grades 2--3 Problem 3', prof('middle_three')),
        ('Grades 2--3 Problem 4', prof('middle_four')),
    ],
    '4-5': [
        ('Grades 4--5 Problem 1, top case', prof('k_two_stable')),
        ('Grades 4--5 Problem 1, bottom case', prof('middle_unique')),
        ('Grades 4--5 Problem 2', prof('older_four')),
    ],
}

PRE = r'''\documentclass{article}
\usepackage[paperwidth=215.9mm,paperheight=279.4mm,margin=0mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
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
    def __init__(self, size, heading, number, note=None):
        self.w, self.h = size
        self.size = size
        self.cmd = []
        landscape = self.w > self.h
        self.text(10, 6, HEADER, 10)
        self.cmd.append(rf'\draw[line width=.5pt] (10,11.5) -- ({f(self.w - 10)},11.5);')
        self.text(10, 14, heading, 10.5, width=(self.w - 130) if landscape else (self.w - 20))
        if landscape:
            self.scale_check(self.w - 110, 20, label_above=True)
        else:
            self.scale_check(10, 27)
        self.text(10, self.h - 9, f'Bellingham Math Circle / Week 27 / {PACKET}', 9)
        self.text(self.w - 14, self.h - 9, str(number), 9, width=4)
        if note:
            self.text(10, self.h - 15, note, 8)

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

    def icon(self, cx, cy, letter, circle, d=ICON, size=24, fill=None):
        style = 'line width=.8pt' + (f',fill={fill}' if fill else '')
        if circle:
            self.cmd.append(rf'\draw[{style}] ({f(cx)},{f(cy)}) circle[radius={f(d / 2)}];')
        else:
            self.cmd.append(rf'\draw[{style}] ({f(cx - d / 2)},{f(cy - d / 2)}) rectangle '
                            rf'({f(cx + d / 2)},{f(cy + d / 2)});')
        if letter:
            self.text(cx, cy, letter, size, anchor='center')

    def tex(self):
        w, h = self.size
        return (rf'\pdfpagewidth={w}mm \pdfpageheight={h}mm \paperwidth={w}mm \paperheight={h}mm' + '\n'
                + r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]' + '\n'
                + r'\begin{scope}[shift={(current page.north west)}]' + '\n'
                + '\n'.join(self.cmd) + '\n' + r'\end{scope}\end{tikzpicture}' + '\n')


def strip_width(n):
    return 28 + n * PITCH + 2


def card_size(n):
    return 2 * strip_width(n) + 14, 8 + (n - 1) * ROW + ICON + 4


def case_card(p, x, y, label, profile):
    left, right = profile
    n = len(left)
    w, h = card_size(n)
    p.rect(x, y, w, h)
    p.text(x + 3, y + 1.8, label, 8)
    sw = strip_width(n)
    for col, (side, strips) in enumerate((('circle', left), ('square', right))):
        bx = x + 4 + col * (sw + 6)
        for row, (owner, choices) in enumerate(strips.items()):
            cy = y + 8 + ICON / 2 + row * ROW
            p.icon(bx + ICON / 2, cy, owner, side == 'circle')
            p.text(bx + 24, cy, ':', 20, anchor='center')
            p.rect(bx + 28, cy - ICON / 2 - 1.5, n * PITCH + 2, ICON + 3, 'line width=.65pt')
            for j, c in enumerate(choices):
                p.icon(bx + 29 + PITCH / 2 + j * PITCH, cy, c, side != 'circle')
            if row == 0 and n > 2:
                for j in range(n):
                    p.text(bx + 29 + PITCH / 2 + j * PITCH, cy - ICON / 2 - 2, str(j + 1), 7, anchor='south')
    return h


def tokens(p, x, y, circles, squares, per_row=4):
    for i, (letter, circle) in enumerate([(c, True) for c in circles] + [(s, False) for s in squares]):
        tx = x + (i % per_row) * TOKEN
        ty = y + (i // per_row) * TOKEN
        p.rect(tx, ty, TOKEN, TOKEN)
        p.icon(tx + TOKEN / 2, ty + TOKEN / 2, letter, circle, d=TOKEN - 2, size=26)
    return ((len(circles) + len(squares) + per_row - 1) // per_row) * TOKEN


def links(p, x, y, solid=4, dashed=1):
    lw, lh = LINK
    for i in range(solid + dashed):
        ly = y + i * lh
        p.rect(x, ly, lw, lh)
        style = 'line width=2.2pt' + (',dashed' if i >= solid else '')
        p.cmd.append(rf'\draw[{style}] ({f(x + 4)},{f(ly + lh / 2)}) -- ({f(x + lw - 4)},{f(ly + lh / 2)});')
    return (solid + dashed) * lh


def tiles(p, x, y):
    letters = [('A', True)] * 4 + [('B', True)] * 4 + [('X', False)] * 4 + [('Y', False)] * 4
    for i, (letter, circle) in enumerate(letters):
        tx, ty = x + (i % 8) * TILE, y + (i // 8) * TILE
        p.rect(tx, ty, TILE, TILE)
        p.icon(tx + TILE / 2, ty + TILE / 2, letter, circle, d=TILE - 2, size=20)
    return 2 * TILE


def markers(p, x, y):
    for i in range(16):
        tx, ty = x + (i % 8) * MARKER, y + (i // 8) * MARKER
        p.cmd.append(rf'\fill[black!15] ({f(tx)},{f(ty)}) rectangle ({f(tx + MARKER)},{f(ty + MARKER)});')
        p.rect(tx, ty, MARKER, MARKER)
        p.cmd.append(rf'\draw[line width=2.4pt,line cap=round,line join=round] ({f(tx + 4.5)},{f(ty + 9.5)}) -- '
                     rf'({f(tx + 8)},{f(ty + 13)}) -- ({f(tx + 13.5)},{f(ty + 5)});')
    return 2 * MARKER


def label(p, x, y, s):
    p.text(x, y - 1.5, s, 9, anchor='south west')


LAUNCH_CARD = ('Launch: for the shared demonstration; printed in no packet', LAUNCH)


def stack(p, x, y, cards, gap=0):
    """Case cards one above another, sharing cut lines when gap is 0."""
    for lab, profile in cards:
        w, h = card_size(len(profile[0]))
        case_card(p, (p.w - w) / 2 if x is None else x, y, lab, profile)
        y += h + gap
    assert y <= p.h - 12, (lab, y)
    return y


def pieces_page(n, heading, circles, squares, extra, cards):
    note = 'Physically unrehearsed: sizes are checked digitally; nobody has built and used this kit yet.' if n == 1 else None
    p = Page(LETTER, heading, n, note)
    x0, y = 10, 38
    label(p, x0, y, 'Tokens' if len(circles) == 2 else 'Tokens: circles A--D, squares W--Z')
    th = tokens(p, x0, y, circles, squares)
    lx = x0 + 4 * TOKEN + 10
    label(p, lx, y, 'Links: four for pairs; dashed for the pair being checked')
    lh = links(p, lx, y)
    y += max(th, lh) + 12
    if extra == 'tiles':
        label(p, x0, y, 'Letter tiles for Problems 3--6: lay them over a strip\\textquoteright s choices to swap or fill it')
        y += tiles(p, x0, y) + 12
    elif extra == 'markers':
        label(p, x0, y, 'Already-asked markers for Problem 2: cover each choice an asker has asked')
        y += markers(p, x0, y) + 12
    label(p, x0, y, 'Case cards')
    stack(p, x0, y, cards)
    return p


def cases_page(n, size, heading, cards):
    p = Page(size, heading, n)
    stack(p, None, 34 if size == LETTER else 27, cards)
    return p


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build'
    if not out.is_absolute():
        out = ROOT / out
    out.mkdir(parents=True, exist_ok=True)
    K, M, U = CASES['K-1'], CASES['2-3'], CASES['4-5']
    head = r'\textbf{%s table, sheet %d of 3. Print 1 on card stock.} '
    cut = 'Cut on the lines.'
    pages = [
        pieces_page(1, head % ('K--1', 1) + 'Tokens, links, letter tiles and the launch card. ' + cut,
                    'AB', 'XY', 'tiles', [LAUNCH_CARD]),
        cases_page(2, LETTER, head % ('K--1', 2) + 'Case cards for Problems 1 and 2. ' + cut, K[0:4]),
        cases_page(3, LETTER, head % ('K--1', 3) + 'Case cards for Problems 3 and 4. ' + cut, K[4:8]),
        pieces_page(4, head % ('Grades 2--3', 1) + 'Tokens, links and case cards for Problem 1. ' + cut,
                    'ABCD', 'WXYZ', None, M[0:2]),
        cases_page(5, LANDSCAPE, head % ('Grades 2--3', 2) + 'Case cards for Problems 2 and 3. ' + cut, M[2:4]),
        cases_page(6, LANDSCAPE, head % ('Grades 2--3', 3) + 'Case card for Problem 4 and the launch card. ' + cut,
                   [M[4], LAUNCH_CARD]),
        pieces_page(7, head % ('Grades 4--5', 1) + 'Tokens, links, already-asked markers and the case card for '
                    'Problem 1, top. ' + cut, 'ABCD', 'WXYZ', 'markers', U[0:1]),
        cases_page(8, LANDSCAPE, head % ('Grades 4--5', 2) + 'Case card for Problem 1, bottom, and the launch card. '
                   + cut, [U[1], LAUNCH_CARD]),
        cases_page(9, LANDSCAPE, head % ('Grades 4--5', 3) + 'Case card for Problem 2. ' + cut, U[2:3]),
    ]
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
