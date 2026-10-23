#!/usr/bin/env python3
"""Build the Week 35 kit: footprint cards in two printed forms.

Usage: python3 materials/build_materials.py

Writes materials/materials.tex, runs pdflatex twice in build/ and copies the
PDF to materials.pdf beside the other outputs. The footprint is the notched F
of the student pages (src/mathematical-checks.json), drawn 26 mm wide. One
page holds two sets of 12 A cards and 12 mirror-A cards (A flipped over a
horizontal line); turning a card half way round gives the other two forms.
Check the result with materials/verify_materials.py.
"""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
V = json.loads((ROOT / 'src' / 'mathematical-checks.json').read_text())['motif_vertices']
SCALE = 10.0              # motif units to mm: the polygon is 2.6 units wide, so 26 mm
ARROW = ((-0.25, -0.86), (0.55, -0.86))
CARD = (29.0, 26.0)       # at most 30 mm wide and 30 mm tall: Border E puts centres 3 cm apart
COLS, ROWS = 6, 2         # per form and set: 6 x 2 = 12 cards
HEADER = 'Week 35 / Footprint borders / Materials'
PACKET = 'W35-M-v1'

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


def text(x, y, s, size, anchor='north west', width=None):
    w = f',text width={f(width)}mm' if width else ''
    return (rf'\node[anchor={anchor},inner sep=0pt,align=left{w},'
            rf'font=\fontsize{{{size}}}{{{size * 1.22:.1f}}}\selectfont] at ({f(x)},{f(y)}) {{{s}}};')


def footprint(cx, cy, mirror):
    sy = -1 if mirror else 1
    pts = ' -- '.join(f'({f(cx + SCALE * x)},{f(cy + SCALE * sy * y)})' for x, y in V)
    (ax, ay), (bx, by) = ARROW
    return [rf'\draw[line width=.7pt,fill=black!15] {pts} -- cycle;',
            rf'\draw[-{{Stealth}},line width=.65pt] ({f(cx + SCALE * ax)},{f(cy + SCALE * sy * ay)}) -- '
            rf'({f(cx + SCALE * bx)},{f(cy + SCALE * sy * by)});']


def card_set(x0, y0):
    w, h = CARD
    out = []
    for r in range(2 * ROWS):
        for c in range(COLS):
            x, y = x0 + c * w, y0 + r * h
            out.append(rf'\draw[line width=.5pt] ({f(x)},{f(y)}) rectangle ({f(x + w)},{f(y + h)});')
            out += footprint(x + w / 2, y + h / 2, mirror=r >= ROWS)
    return out


def page():
    W, H = 215.9, 279.4
    cmd = [text(10, 6, HEADER, 10), r'\draw[line width=.5pt] (10,11.5) -- (205.9,11.5);',
           text(10, 14, r'\textbf{Footprint cards. Print 1 per table on card stock.} Each set is 24 cards for one '
                r'pair or trio: 12 A cards and 12 mirror-A cards. A table with one group can start with Set 1 only. '
                r'Cut on the lines.', 10.5, width=W - 20)]
    cmd += [r'\draw[line width=.8pt] (10,27) -- (110,27);',
            r'\draw[line width=.8pt] (10,25) -- (10,29);', r'\draw[line width=.8pt] (110,25) -- (110,29);',
            text(113, 27, '10 cm scale check: measure before cutting', 8, anchor='west')]
    gw, gh = COLS * CARD[0], 2 * ROWS * CARD[1]
    x0 = (W - gw) / 2
    for i, y0 in enumerate((38.0, 38.0 + gh + 10)):
        cmd.append(text(x0, y0 - 1.5, f'Set {i + 1}: two rows of A, then two rows of mirror A', 9, anchor='south west'))
        cmd += card_set(x0, y0)
    cmd.append(text(10, H - 15, 'Physically unrehearsed: sizes are checked digitally; nobody has built and used '
                    'this kit yet.', 8))
    cmd.append(text(10, H - 9, f'Bellingham Math Circle / Week 35 / {PACKET}', 9))
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
    print(f'Built {ROOT / "materials.pdf"}: 1 page, two sets of {2 * COLS * ROWS} cards.')


if __name__ == '__main__':
    main()
