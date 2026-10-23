#!/usr/bin/env python3
"""Build the Week 32 K-1 square sheet: two square sets on one page, one set per pair.

Usage: python3 materials/build_materials.py

Writes materials/materials.tex, runs pdflatex twice in qa/ and copies the PDF
to materials.pdf beside the other outputs. One unit is 10 mm, as on the K-1
boards. A set is one square each of sides 6 and 5, two each of 4 and 2, six
of 3 and three of 1: enough to carry out the biggest-square rule on every K-1
Problem 1-3 board at once, with the next size up for every Problem 4 test and
four 3-by-3 squares for Problem 5. Each square is tinted by size, carries a
light 1 cm grid so it lines up with the board's grid, and shows its side in
its top-left cell. Squares are 3 mm apart so each is cut on its own outline.
Check the result with materials/verify_materials.py.
"""
from pathlib import Path
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
UNIT = 10.0                      # mm per unit, as on the K-1 boards
GAP = 3.0                        # mm between neighbouring squares
SET = {6: 1, 5: 1, 4: 2, 3: 6, 2: 2, 1: 3}
# (side, x, y) in mm from a set's top-left corner. Row 1 is 63 mm tall: the 6, the 5 with a 1 under it,
# and each 4 with a 2 and a 1 under it. Row 2 is the six 3s.
LAYOUT = [(6, 0, 0), (5, 63, 0), (1, 63, 53), (4, 116, 0), (2, 116, 43), (1, 139, 43),
          (4, 159, 0), (2, 159, 43), (1, 182, 43)] + [(3, 33 * i, 66) for i in range(6)]
SET_W, SET_H = 199.0, 96.0
TINT = {1: 'black!10', 2: 'red!14', 3: 'green!16', 4: 'violet!14', 5: 'yellow!28', 6: 'teal!16'}
HEADER = 'Week 32 / Squares inside rectangles / Materials'
PACKET = 'F32-M-v1'

PRE = r'''\documentclass{article}
\usepackage[paperwidth=215.9mm,paperheight=279.4mm,margin=0mm]{geometry}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\pagestyle{empty}
\pdfmapfile{+cm.map}
\pdfmapfile{+ps2pk35.map}
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


def square(x, y, n):
    s = n * UNIT
    out = [rf'\draw[line width=.8pt,fill={TINT[n]}] ({f(x)},{f(y)}) rectangle ({f(x + s)},{f(y + s)});']
    for k in range(1, n):
        u = k * UNIT
        out.append(rf'\draw[line width=.3pt,black!35] ({f(x + u)},{f(y)}) -- ({f(x + u)},{f(y + s)}) '
                   rf'({f(x)},{f(y + u)}) -- ({f(x + s)},{f(y + u)});')
    out.append(text(x + UNIT / 2, y + UNIT / 2, rf'\textbf{{{n}}}', 9, anchor='center'))
    return out


def page():
    W, H = 215.9, 279.4
    x0 = (W - SET_W) / 2
    cmd = [text(x0, 6, HEADER, 10), rf'\draw[line width=.5pt] ({f(x0)},11.5) -- ({f(W - x0)},11.5);',
           text(x0, 14, r'\textbf{K--1 square sets: one per pair. Print at 100\% on card stock '
                r'(1 page for a table of two pairs).} Each set has one square each of sides 6 and 5, two each '
                r'of 4 and 2, six of 3 (four for Problem 5) and three of 1. One unit is 1 cm, as on the K--1 '
                r'boards. Cut on the outlines.', 10.5, width=SET_W)]
    cmd += [rf'\draw[line width=.8pt] ({f(x0)},31) -- ({f(x0 + 100)},31);',
            rf'\draw[line width=.8pt] ({f(x0)},29) -- ({f(x0)},33);',
            rf'\draw[line width=.8pt] ({f(x0 + 100)},29) -- ({f(x0 + 100)},33);',
            text(x0 + 103, 31, '10 cm scale check: measure before cutting', 8, anchor='west')]
    tops = (38.0, 38.0 + SET_H + 12)
    for top in tops:
        for n, dx, dy in LAYOUT:
            cmd += square(x0 + dx, top + dy, n)
    mid = tops[0] + SET_H + 6
    cmd.append(rf'\draw[line width=.4pt,black!45,dash pattern=on 2mm off 1.5mm] ({f(x0)},{f(mid)}) -- ({f(W - x0)},{f(mid)});')
    cmd.append(text(x0, H - 15, 'Physically unrehearsed: sizes are checked digitally; nobody has built and used '
                    'this kit yet.', 8))
    cmd.append(text(x0, H - 9, f'Bellingham Math Circle / Week 32 / {PACKET}', 9))
    cmd.append(text(W - x0, H - 9, '1', 9, anchor='north east'))
    return (r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]' + '\n'
            + r'\begin{scope}[shift={(current page.north west)}]' + '\n'
            + '\n'.join(cmd) + '\n' + r'\end{scope}\end{tikzpicture}' + '\n')


def main():
    counts = {n: sum(1 for m, _, _ in LAYOUT if m == n) for n in SET}
    assert counts == SET, counts
    boxes = [(x, y, x + n * UNIT, y + n * UNIT) for n, x, y in LAYOUT]
    assert all(0 <= a and 0 <= b and c <= SET_W and d <= SET_H for a, b, c, d in boxes)
    for i, p in enumerate(boxes):  # no two squares closer than GAP
        for q in boxes[i + 1:]:
            assert p[2] + GAP <= q[0] or q[2] + GAP <= p[0] or p[3] + GAP <= q[1] or q[3] + GAP <= p[1], (p, q)
    qa = ROOT / 'qa'
    qa.mkdir(exist_ok=True)
    src = HERE / 'materials.tex'
    src.write_text(PRE + page() + r'\end{document}' + '\n')
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                            f'-output-directory={qa}', str(src)], capture_output=True, text=True,
                           env=os.environ.copy())
        if r.returncode:
            sys.stdout.write(r.stdout[-3000:])
            raise SystemExit('pdflatex failed')
    shutil.copyfile(qa / 'materials.pdf', ROOT / 'materials.pdf')
    print(f'Built {ROOT / "materials.pdf"}: 1 page, 2 sets of {len(LAYOUT)} squares.')


if __name__ == '__main__':
    main()
