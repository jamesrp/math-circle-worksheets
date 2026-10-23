#!/usr/bin/env python3
"""Build the Week 43 card kit: one sheet per pair, plus one per adult table.

Usage: python3 materials/build_materials.py

Writes materials/materials.tex, runs pdflatex twice in build/ and copies the PDF
to materials.pdf beside the other outputs. A sheet holds five picture cards
A-E at 1.7 x 2.2 in (43.18 x 55.88 mm) with the student pages' pictures
(square, circle, triangle, diamond, pentagon), tickets 1-5 and a second 2 and 3
as 20 mm squares, and a three-slot strip whose slots are the K-1 Problem 1 mat's
47 x 61 mm. Cards A, B, C and tickets 1, 2, 3 serve every band; the second 2 and 3
let K-1 Problem 4 take a ticket from the first set and leave the second set whole
(Critic K, October 23); D, E and tickets 4, 5 are for Grades 4-5 Problems 6-7. Check the result with materials/verify_materials.py.
"""
from pathlib import Path
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CARD = (43.18, 55.88)          # 1.7 x 2.2 in
SLOT = (47.0, 61.0)            # the K-1 Problem 1 mat's slots, 4.7 x 6.1 cm
TICKET = 20.0
HEADER = 'Week 43 / Shuffling picture cards / Materials'
PACKET = 'W43-M-v2'   # v2: a second 2 and 3 for K-1 Problem 4 (Critic K, October 23)
FILL = {'A': 'orange!22', 'B': 'green!22', 'C': 'violet!22', 'D': 'cyan!22', 'E': 'yellow!25'}

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


def text(x, y, s, size, anchor='north west', width=None):
    w = f',text width={f(width)}mm' if width else ''
    return (rf'\node[anchor={anchor},inner sep=0pt,align=left{w},'
            rf'font=\fontsize{{{size}}}{{{size * 1.22:.1f}}}\selectfont] at ({f(x)},{f(y)}) {{{s}}};')


def picture(c, x, y, s):
    """The student pages' card pictures (figures.py icon), centred at (x, y), half-size s mm; y points down."""
    fill = rf'\draw[fill={FILL[c]},line width=1pt]'
    if c == 'A':
        return fill + rf' ({f(x - s)},{f(y - s)}) rectangle ({f(x + s)},{f(y + s)});'
    if c == 'B':
        return fill + rf' ({f(x)},{f(y)}) circle ({f(s)});'
    if c == 'C':
        return fill + rf' ({f(x)},{f(y - s)}) -- ({f(x + s)},{f(y + s)}) -- ({f(x - s)},{f(y + s)}) -- cycle;'
    if c == 'D':
        return fill + rf' ({f(x)},{f(y - s)}) -- ({f(x + s)},{f(y)}) -- ({f(x)},{f(y + s)}) -- ({f(x - s)},{f(y)}) -- cycle;'
    return fill + (rf' ({f(x - s)},{f(y + s)}) -- ({f(x + s)},{f(y + s)}) -- ({f(x + s)},{f(y)}) -- '
                   rf'({f(x)},{f(y - s)}) -- ({f(x - s)},{f(y)}) -- cycle;')


def card(c, x, y):
    w, h = CARD
    return [rf'\draw[line width=.5pt] ({f(x)},{f(y)}) rectangle ({f(x + w)},{f(y + h)});',
            picture(c, x + w / 2, y + 23, 11), text(x + w / 2, y + h - 8, c, 16, anchor='center')]


def ticket(n, x, y):
    return [rf'\draw[line width=.5pt] ({f(x)},{f(y)}) rectangle ({f(x + TICKET)},{f(y + TICKET)});',
            text(x + TICKET / 2, y + TICKET / 2, str(n), 20, anchor='center')]


def strip(x, y):
    w, h = SLOT
    out = [rf'\draw[line width=.5pt] ({f(x)},{f(y)}) rectangle ({f(x + 3 * w)},{f(y + h)});']
    for i in range(3):
        if i:
            out.append(rf'\draw[line width=.5pt,gray] ({f(x + i * w)},{f(y)}) -- ({f(x + i * w)},{f(y + h)});')
        out.append(text(x + i * w + 2, y + 2, str(i + 1), 11))
    return out


def page():
    W, H = 215.9, 279.4
    cmd = [text(10, 6, HEADER, 10), r'\draw[line width=.5pt] (10,11.5) -- (205.9,11.5);',
           text(10, 14, r'\textbf{Card kit. Print 1 per pair on card stock at 100\%}, plus 1 per adult table for a '
                r'second A B C set to compare starts. Cut on the outer lines; keep the strip in one piece. '
                r'Cards A, B, C and tickets 1, 2, 3 serve every band; D, E and tickets 4, 5 are for Grades 4--5 '
                r'Problems 6--7. Add a cup for the tickets.', 10.5, width=W - 20)]
    cmd += [r'\draw[line width=.8pt] (10,32) -- (110,32);',
            r'\draw[line width=.8pt] (10,30) -- (10,34);', r'\draw[line width=.8pt] (110,30) -- (110,34);',
            text(113, 32, '10 cm scale check: measure before cutting', 8, anchor='west')]
    gap = (W - 20 - 4 * CARD[0]) / 3
    for i, c in enumerate('ABCD'):
        cmd += card(c, 10 + i * (CARD[0] + gap), 42)
    cmd += card('E', 10, 42 + CARD[1] + 10)
    tx = 10 + CARD[0] + gap
    ty = 42 + CARD[1] + 10 + 4
    for i in range(5):
        cmd += ticket(i + 1, tx + i * (TICKET + 6), ty)
    for i in range(2):
        cmd += ticket(i + 2, tx + i * (TICKET + 6), ty + TICKET + 8)
    cmd.append(text(tx + 2 * (TICKET + 6) + 2, ty + 1.5 * TICKET + 8, 'second set for K--1 Problem 4', 9, anchor='west'))
    cmd.append(text(10, 172, 'Three-slot strip (slots as on the K--1 page 1 mat)', 9))
    cmd += strip(10, 178)
    cmd.append(text(10, H - 15, 'Physically unrehearsed: sizes are checked digitally; nobody has built and used '
                    'this kit yet.', 8))
    cmd.append(text(10, H - 9, f'Bellingham Math Circle / Week 43 / {PACKET}', 9))
    cmd.append(text(W - 14, H - 9, '1', 9, width=4))
    return (r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]' + '\n'
            + r'\begin{scope}[shift={(current page.north west)}]' + '\n'
            + '\n'.join(cmd) + '\n' + r'\end{scope}\end{tikzpicture}' + '\n')


def main():
    build = ROOT / 'build'
    build.mkdir(exist_ok=True)
    src = HERE / 'materials.tex'
    src.write_text(PRE + page() + r'\end{document}' + '\n')
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                            f'-output-directory={build}', str(src)], capture_output=True, text=True,
                           env=os.environ.copy())
        if r.returncode:
            sys.stdout.write(r.stdout[-3000:])
            raise SystemExit('pdflatex failed')
    shutil.copyfile(build / 'materials.pdf', ROOT / 'materials.pdf')
    print(f'Built {ROOT / "materials.pdf"}: 1 page, cards A-E, tickets 1-5, a second 2 and 3, and a three-slot strip.')


if __name__ == '__main__':
    main()
