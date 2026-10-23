#!/usr/bin/env python3
"""Build the Week 17 table kit: one card-stock sheet per table.

Usage: python3 materials/build_materials.py [output-folder]   (default: build)

Every size is in millimetres and is set in the constants below. A sheet holds
12 R cards and 12 B cards (30 mm squares; R is a red square and B a blue
circle, as on the student pages), 12 blank state circles (30 mm circles on
34 mm squares) and 4 markers (14 mm squares, two solid and two rings). Every
piece is cut on straight grey lines. The script writes materials/materials.tex
and runs pdflatex twice into the output folder. Check the result with
materials/verify_materials.py.
"""
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

W, H = 215.9, 279.4
CARD = 30.0             # card side; 'about 3 cm across' in the guide
GLYPH = 24.0            # the R square's side and the B circle's diameter on a card
TILE = 34.0             # state-circle tile side
STATE = 30.0            # state-circle diameter
MARKER = 14.0           # marker tile side: smaller than the pages' 16.8 mm printed circles
DOT = 11.0              # marker disc or ring diameter
CARDS_PER_ROW = 6
TILES_PER_ROW = 5
CARDS_Y = 37.0
TILES_Y = CARDS_Y + 4 * CARD + 4.0
HEADER = 'Week 17 / Machine memory / Materials'
PACKET = 'W17-M-v1'

PRE = r'''\documentclass{article}
\usepackage[paperwidth=215.9mm,paperheight=279.4mm,margin=0mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\definecolor{cardred}{RGB}{203,45,45}
\definecolor{cardblue}{RGB}{34,95,176}
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


def cut(x, y, side):
    return rf'\draw[black!45,line width=.5pt] ({f(x)},{f(y)}) rectangle ({f(x + side)},{f(y + side)});'


def card(kind, x, y):
    cx, cy, g = x + CARD / 2, y + CARD / 2, GLYPH / 2
    out = [cut(x, y, CARD)]
    if kind == 'R':
        out.append(rf'\draw[draw=cardred,fill=cardred!10,line width=1.6pt] ({f(cx - g)},{f(cy - g)}) rectangle ({f(cx + g)},{f(cy + g)});')
    else:
        out.append(rf'\draw[draw=cardblue,fill=cardblue!10,line width=1.6pt] ({f(cx)},{f(cy)}) circle ({f(g)});')
    out.append(text(cx, cy, rf'\bfseries {kind}', 34, anchor='center'))
    return out


def state(x, y):
    return [cut(x, y, TILE), rf'\draw[line width=1.1pt] ({f(x + TILE / 2)},{f(y + TILE / 2)}) circle ({f(STATE / 2)});']


def marker(solid, x, y):
    c = (x + MARKER / 2, y + MARKER / 2)
    disc = (rf'\fill ({f(c[0])},{f(c[1])}) circle ({f(DOT / 2)});' if solid else
            rf'\draw[line width=2.4pt] ({f(c[0])},{f(c[1])}) circle ({f(DOT / 2 - .42)});')
    return [cut(x, y, MARKER), disc]


def page():
    cmd = [text(10, 6, HEADER, 10), r'\draw[line width=.5pt] (10,11.5) -- (205.9,11.5);',
           text(10, 14, r'\textbf{Table kit. Print 1 per table on card stock at 100\%.} Cut on the grey lines: '
                r'12 R cards, 12 B cards, 12 blank state circles and 4 markers. Each pair takes one solid and one '
                r'ring marker, so two runs on one machine can be told apart. A marker fits on a printed circle '
                r'of the student pages, and two fit side by side on a state circle.', 10.5, width=W - 20)]
    cmd += [r'\draw[line width=.8pt] (10,31) -- (110,31);',
            r'\draw[line width=.8pt] (10,29) -- (10,33);', r'\draw[line width=.8pt] (110,29) -- (110,33);',
            text(113, 31, '10 cm scale check: measure before cutting', 8, anchor='west')]
    x0 = (W - CARDS_PER_ROW * CARD) / 2
    for r, kind in enumerate('RRBB'):
        for i in range(CARDS_PER_ROW):
            cmd += card(kind, x0 + i * CARD, CARDS_Y + r * CARD)
    t0 = (W - TILES_PER_ROW * TILE) / 2
    for n in range(12):
        cmd += state(t0 + (n % TILES_PER_ROW) * TILE, TILES_Y + (n // TILES_PER_ROW) * TILE)
    mx = t0 + 2 * TILE + 8
    my = TILES_Y + 2 * TILE + (TILE - MARKER) / 2
    for i, solid in enumerate([True, False, True, False]):
        cmd += marker(solid, mx + i * (MARKER + 6), my)
    cmd.append(text(mx, my + MARKER + 4, 'Physically unrehearsed: sizes are checked digitally only.', 8))
    cmd.append(text(10, H - 9, f'Bellingham Math Circle / Week 17 / {PACKET}', 9))
    cmd.append(text(W - 14, H - 9, '1', 9, width=4))
    return (r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]' + '\n'
            + r'\begin{scope}[shift={(current page.north west)}]' + '\n'
            + '\n'.join(cmd) + '\n' + r'\end{scope}\end{tikzpicture}' + '\n')


def main():
    out = (ROOT / (sys.argv[1] if len(sys.argv) > 1 else 'build')).resolve()
    out.mkdir(parents=True, exist_ok=True)
    src = HERE / 'materials.tex'
    src.write_text(PRE + page() + r'\end{document}' + '\n')
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                            f'-output-directory={out}', str(src)], capture_output=True, text=True)
        if r.returncode:
            sys.stdout.write(r.stdout[-3000:])
            raise SystemExit('pdflatex failed')
    print(f'Built {out / "materials.pdf"}: 1 page, 12 R and 12 B cards, 12 state circles, 4 markers.')


if __name__ == '__main__':
    main()
