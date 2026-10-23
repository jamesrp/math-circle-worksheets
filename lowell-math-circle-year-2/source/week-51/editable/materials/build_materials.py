#!/usr/bin/env python3
"""Build the Week 51 kit: one strip set per pair or trio.

Usage: python3 materials/build_materials.py

Writes materials/materials.tex, runs pdflatex twice in build/ and copies the
PDF to materials.pdf beside the other outputs. One unit is 10 mm, as on the
student pages. A set is two gray strips of every whole length from 1 to 15
units and two white add-ons each of 4 and 1 units, cut from abutting rows
that are each 16 units (160 mm) long. Every extreme in the guide's keys is a
whole length, so whole strips reach every bound; no sleeves are needed.
Check the result with materials/verify_materials.py.
"""
from pathlib import Path
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
UNIT = 10.0                      # mm per unit, as on the student rulers
ROW_UNITS = 16                   # each row is one 0-16 ruler long
GRAY = [(16 - k, k) for k in range(1, 8) for _ in range(2)] + [(8, 8)]
WHITE = (4, 1, 4, 1)             # add-ons for the shared-A comparisons
HEADER = 'Week 51 / Honest measurement ranges / Materials'
PACKET = 'W51-M-v1'

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


def strip(x, y, units, white):
    w = units * UNIT
    fill = 'white' if white else 'black!12'
    out = [rf'\draw[line width=.5pt,fill={fill}] ({f(x)},{f(y)}) rectangle ({f(x + w)},{f(y + UNIT)});']
    # Gray strips carry their length in the first unit; add-ons are labelled in the middle, as on the pages.
    cx = x + (w / 2 if white else UNIT / 2)
    out.append(text(cx, y + UNIT / 2, str(units), 8, anchor='center'))
    return out


def page():
    W, H = 215.9, 279.4
    cmd = [text(10, 6, HEADER, 10), r'\draw[line width=.5pt] (10,11.5) -- (205.9,11.5);',
           text(10, 14, r'\textbf{Strip set. Print 1 per pair or trio on card stock} (2 for a table of two pairs). '
                r'Two gray strips of each length from 1 to 15 units; two white add-ons each of 4 and 1. '
                r'One unit is 10 mm. Cut on the lines.', 10.5, width=W - 20)]
    cmd += [r'\draw[line width=.8pt] (10,27) -- (110,27);',
            r'\draw[line width=.8pt] (10,25) -- (10,29);', r'\draw[line width=.8pt] (110,25) -- (110,29);',
            text(113, 27, '10 cm scale check: measure before cutting', 8, anchor='west')]
    x0, y0 = (W - ROW_UNITS * UNIT) / 2, 40.0
    rows = [(r, False) for r in GRAY] + [(WHITE, True)]
    for i, (lengths, white) in enumerate(rows):
        x = x0
        for n in lengths:
            cmd += strip(x, y0 + i * UNIT, n, white)
            x += n * UNIT
    cmd.append(text(10, H - 15, 'Physically unrehearsed: sizes are checked digitally; nobody has built and used '
                    'this kit yet.', 8))
    cmd.append(text(10, H - 9, f'Bellingham Math Circle / Week 51 / {PACKET}', 9))
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
    print(f'Built {ROOT / "materials.pdf"}: 1 page, {2 * len(GRAY)} gray strips and {len(WHITE)} add-ons.')


if __name__ == '__main__':
    main()
