#!/usr/bin/env python3
"""Build the Week 48 tile sheet: one set of paper tiles per pair.

Usage: python3 materials/build_materials.py

Writes materials/materials.tex, runs pdflatex twice in build/ and copies the
PDF to materials.pdf beside the other outputs. The student boards are 120 mm
square, so a big tile is 30 mm (one cell of the 4-by-4 boards) and a small
tile is 15 mm (one cell of the 8-by-8 boards). A set is 16 big tiles, enough
to cover every cell of the trapezoid, and 16 small tiles, enough for the
three splits of grades 4-5 with four to spare. The tiles are cut from
abutting blocks, so every cut is straight and shared. Check the result with
materials/verify_materials.py.
"""
from pathlib import Path
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BIG, SMALL = 30.0, 15.0          # mm: one cell of the 4-by-4 and 8-by-8 student boards
BIG_BLOCK = (4, 4)               # columns, rows
SMALL_BLOCK = (8, 2)
HEADER = 'Week 48 / Inside and outside covers / Materials'
PACKET = 'W48-M-v1'

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


def block(x, y, side, cols, rows):
    """Abutting squares, each drawn as its own closed outline."""
    return [rf'\draw[line width=.5pt] ({f(x + c * side)},{f(y + r * side)}) rectangle '
            rf'({f(x + (c + 1) * side)},{f(y + (r + 1) * side)});' for r in range(rows) for c in range(cols)]


def page():
    W, H = 215.9, 279.4
    nb, ns = BIG_BLOCK[0] * BIG_BLOCK[1], SMALL_BLOCK[0] * SMALL_BLOCK[1]
    cmd = [text(10, 6, HEADER, 10), r'\draw[line width=.5pt] (10,11.5) -- (205.9,11.5);',
           text(10, 14, rf'\textbf{{Tile set. Print 1 per pair on card stock at actual size.}} '
                rf'{nb} big squares (30 mm) and {ns} small squares (15 mm), the cells of the 120 mm boards. '
                r'Cut on the lines.', 10.5, width=W - 20)]
    cmd += [r'\draw[line width=.8pt] (10,27) -- (110,27);',
            r'\draw[line width=.8pt] (10,25) -- (10,29);', r'\draw[line width=.8pt] (110,25) -- (110,29);',
            text(113, 27, '10 cm scale check: measure before cutting', 8, anchor='west')]
    x0 = (W - BIG_BLOCK[0] * BIG) / 2
    cmd += block(x0, 40, BIG, *BIG_BLOCK)
    cmd += block(x0, 40 + BIG_BLOCK[1] * BIG + 12, SMALL, *SMALL_BLOCK)
    cmd.append(text(10, H - 15, 'Physically unrehearsed: sizes are checked digitally; nobody has cut and used '
                    'these tiles yet.', 8))
    cmd.append(text(10, H - 9, f'Bellingham Math Circle / Week 48 / {PACKET}', 9))
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
    print(f'Built {ROOT / "materials.pdf"}: 1 page, {BIG_BLOCK[0] * BIG_BLOCK[1]} big and '
          f'{SMALL_BLOCK[0] * SMALL_BLOCK[1]} small tiles.')


if __name__ == '__main__':
    main()
