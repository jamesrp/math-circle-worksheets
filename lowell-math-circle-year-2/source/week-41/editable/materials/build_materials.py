#!/usr/bin/env python3
"""Build the Week 41 table copies: one sheet of four lettered 90 mm copies of the portal map.

Usage: python3 materials/build_materials.py

Writes materials/materials.tex, runs pdflatex twice in build/ and copies the PDF to
materials.pdf beside the other outputs. Each copy is the portal map without its seam
marks (copies in the array simply touch): a 90 mm square, three 30 mm cells a side,
lettered A B C / D H E / F G I as on the student pages. Four sheets per table give
nine copies for the 3-by-3 array and seven spares to extend it. Check the result with
materials/verify_materials.py.
"""
from pathlib import Path
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
COPY = 90.0
LETTERS = [['A', 'B', 'C'], ['D', 'H', 'E'], ['F', 'G', 'I']]
HEADER = 'Week 41 / Portals / Materials'
PACKET = 'F41-M-v1'

PRE = r'''\documentclass{article}
\usepackage[paperwidth=215.9mm,paperheight=279.4mm,margin=0mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,tikz}
\pdfmapfile{+lm.map}
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
            rf'font=\fontsize{{{size}}}{{{size * 1.25:.2f}}}\selectfont] at ({f(x)},{f(y)}) {{{s}}};')


def copy(x, y):
    """One copy at top-left (x, y); y points down."""
    c = COPY / 3
    out = []
    for k in (1, 2):
        out.append(rf'\draw[gray!50,line width=.4pt] ({f(x + k * c)},{f(y)}) -- ({f(x + k * c)},{f(y + COPY)});')
        out.append(rf'\draw[gray!50,line width=.4pt] ({f(x)},{f(y + k * c)}) -- ({f(x + COPY)},{f(y + k * c)});')
    for r in range(3):
        for col in range(3):
            cx, cy = x + (col + .5) * c, y + (r + .5) * c
            out.append(text(cx, cy - 4, LETTERS[r][col], 16, anchor='center'))
            out.append(rf'\fill[gray] ({f(cx)},{f(cy)}) circle (.8);')
    out.append(rf'\draw[line width=.9pt] ({f(x)},{f(y)}) rectangle ({f(x + COPY)},{f(y + COPY)});')
    return out


def page():
    W, H = 215.9, 279.4
    x0 = (W - 2 * COPY) / 2
    cmd = [text(16, 11, HEADER, 10.5), r'\draw[gray!55] (16,19) -- (200,19);',
           text(16, 23, r'\textbf{Table copies. Print 4 per table at 100\%}: 16 copies of the portal map. Cut on the '
                r"black lines. Lay nine edge to edge, letters upright, as a 3-by-3 array, and write ``original''"
                r' on the centre copy. Keep the other seven to add beside the array before a trip reaches its edge.',
                10.5, width=184),
           r'\draw[line width=.8pt] (16,42) -- (116,42);',
           r'\draw[line width=.8pt] (16,40) -- (16,44);', r'\draw[line width=.8pt] (116,40) -- (116,44);',
           text(119, 42, '10 cm scale check: measure before cutting', 8, anchor='west')]
    for i in range(2):
        for j in range(2):
            cmd += copy(x0 + j * COPY, 52 + i * COPY)
    cmd.append(text(16, 248, 'Physically unrehearsed: sizes are checked digitally; nobody has cut and used these copies yet.', 8))
    cmd.append(text(16, 266, f'Bellingham Math Circle / Week 41 / {PACKET}', 9))
    cmd.append(text(198, 268, '1', 9, anchor='center'))
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
    print(f'Built {ROOT / "materials.pdf"}: 1 page, four lettered 90 mm copies of the portal map.')


if __name__ == '__main__':
    main()
