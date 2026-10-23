#!/usr/bin/env python3
"""Build the Week 29 rod sheet: one pair-kit of paper rods on one page.

Usage: python3 materials/build_materials.py

Writes materials/materials.tex, runs pdflatex twice in qa/ and copies the PDF
to materials.pdf beside the other outputs. One unit is 10 mm, as on every
printed strip and ruler in the packets (Cuisenaire scale). A kit is ten rods
each of lengths 2, 3, 4, 5 and 7 and three 6-rods (for Grades 4-5 Problem 5),
228 units in all, cut from twelve abutting rows that are each 19 units
(190 mm) long, so every cut is straight and shared. Each rod is tinted by
length and carries its length in the middle; short ticks at its top and
bottom edges mark the units without crossing the numeral.
Check the result with materials/verify_materials.py.
"""
from pathlib import Path
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
UNIT = 10.0                      # mm per unit, as on the student strips and rulers
ROW_UNITS = 19
KIT = {2: 10, 3: 10, 4: 10, 5: 10, 6: 3, 7: 10}
ROWS = [(7, 7, 5)] * 5 + [(6, 5, 4, 4)] * 3 + [(5, 4, 4, 3, 3)] * 2 + [(3, 3, 3, 2, 2, 2, 2, 2)] * 2
TINT = {2: 'red!16', 3: 'green!16', 4: 'violet!16', 5: 'yellow!30', 6: 'teal!20', 7: 'black!14'}
HEADER = 'Week 29 / Two-length builders / Materials'
PACKET = 'F29-M-v1'

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


def rod(x, y, n):
    w = n * UNIT
    out = [rf'\draw[line width=.8pt,fill={TINT[n]}] ({f(x)},{f(y)}) rectangle ({f(x + w)},{f(y + UNIT)});']
    for k in range(1, n):
        u = x + k * UNIT
        out.append(rf'\draw[line width=.3pt,black!55] ({f(u)},{f(y)}) -- ({f(u)},{f(y + 1.8)}) '
                   rf'({f(u)},{f(y + UNIT - 1.8)}) -- ({f(u)},{f(y + UNIT)});')
    out.append(text(x + w / 2, y + UNIT / 2, rf'\textbf{{{n}}}', 11, anchor='center'))
    return out


def page():
    W, H = 215.9, 279.4
    x0, y0 = (W - ROW_UNITS * UNIT) / 2, 42.0
    cmd = [text(x0, 6, HEADER, 10), rf'\draw[line width=.5pt] ({f(x0)},11.5) -- ({f(W - x0)},11.5);',
           text(x0, 14, r'\textbf{Rod sheet: one pair-kit. Print 1 per pair or trio on card stock at 100\% '
                r'(5 for the current group).} Ten rods each of 2, 3, 4, 5 and 7 units and three 6-rods for '
                r'Grades 4--5 Problem 5. One unit is 1 cm, as on every printed strip and ruler. Cut along the '
                r'rows, then at the bold lines.', 10.5, width=ROW_UNITS * UNIT)]
    cmd += [rf'\draw[line width=.8pt] ({f(x0)},31) -- ({f(x0 + 100)},31);',
            rf'\draw[line width=.8pt] ({f(x0)},29) -- ({f(x0)},33);',
            rf'\draw[line width=.8pt] ({f(x0 + 100)},29) -- ({f(x0 + 100)},33);',
            text(x0 + 103, 31, '10 cm scale check: measure before cutting', 8, anchor='west')]
    for i, lengths in enumerate(ROWS):
        x = x0
        for n in lengths:
            cmd += rod(x, y0 + i * UNIT, n)
            x += n * UNIT
    cmd.append(text(x0, H - 15, 'Physically unrehearsed: sizes are checked digitally; nobody has built and used '
                    'this kit yet.', 8))
    cmd.append(text(x0, H - 9, f'Bellingham Math Circle / Week 29 / {PACKET}', 9))
    cmd.append(text(W - x0, H - 9, '1', 9, anchor='north east'))
    return (r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]' + '\n'
            + r'\begin{scope}[shift={(current page.north west)}]' + '\n'
            + '\n'.join(cmd) + '\n' + r'\end{scope}\end{tikzpicture}' + '\n')


def main():
    assert all(sum(r) == ROW_UNITS for r in ROWS)
    counts = {n: sum(r.count(n) for r in ROWS) for n in KIT}
    assert counts == KIT, counts
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
    print(f'Built {ROOT / "materials.pdf"}: 1 page, {sum(KIT.values())} rods in {len(ROWS)} rows.')


if __name__ == '__main__':
    main()
