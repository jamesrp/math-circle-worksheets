#!/usr/bin/env python3
"""Write launch-figure.tex: the launch train 2 1 as input, one step, output.

The mat schematic copies the geometry of mat_panel() in the student pages'
build.py (plans/topic-scouting/drafts/train-yard-sorting/src/build.py), so the
guide's picture matches page 1 of every packet: departure track on the left,
arrival track on the right, a five-place siding below the junction.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def fmt(v):
    return f'{v:.2f}'.rstrip('0').rstrip('.')


def car(x, y, s, label, font):
    return (rf'\draw[line width=0.9pt, fill=white, rounded corners=0.6mm] ({fmt(x)},{fmt(y)}) '
            rf'rectangle ({fmt(x + s)},{fmt(y + s)});' + '\n' +
            rf'\node at ({fmt(x + s / 2)},{fmt(y + s / 2)}) {{{font} {label}}};')


def mat_panel(dep, siding, arr, u, ndep=3, narr=3, labels=False, arrows=False,
              font=r'\bfseries\small'):
    L = 5
    out = []
    x0, x1 = -ndep * u, (narr + 1) * u
    out.append(rf'\fill[black!8] ({fmt(x0)},0) rectangle ({fmt(x1)},{fmt(u)});')
    out.append(rf'\fill[black!8] (0,{fmt(-L * u)}) rectangle ({fmt(u)},0);')
    out.append(rf'\draw[black!45, line width=0.5pt] ({fmt(x0)},{fmt(u)}) -- ({fmt(x1)},{fmt(u)});')
    out.append(rf'\draw[black!45, line width=0.5pt] ({fmt(x0)},0) -- (0,0);')
    out.append(rf'\draw[black!45, line width=0.5pt] ({fmt(u)},0) -- ({fmt(x1)},0);')
    out.append(rf'\draw[line width=1.6pt] (0,0) -- (0,{fmt(-L * u)}) -- ({fmt(u)},{fmt(-L * u)}) -- ({fmt(u)},0);')
    pad = 0.08 * u
    s = u - 2 * pad
    for k, c in enumerate(dep):
        out.append(car((-ndep + k) * u + pad, pad, s, c, font))
    for k, c in enumerate(siding):
        out.append(car(pad, -L * u + k * u + pad, s, c, font))
    for k, c in enumerate(arr):
        out.append(car((k + 1) * u + pad, pad, s, c, font))
    if labels:
        out.append(r'\node[font=\scriptsize, below left, inner xsep=1pt] at (-0.8,-0.4) {departure};')
        out.append(rf'\node[font=\scriptsize, below right, inner xsep=1pt] at ({fmt(u + 0.8)},-0.4) {{arrival}};')
        out.append(rf'\node[font=\scriptsize, right] at ({fmt(u + 0.6)},{fmt(-L * u / 2 - u)}) {{siding}};')
    if arrows:
        h = u + 0.55 * u
        a = r'-{Stealth[length=1.4mm]}, line width=0.6pt, black!70, rounded corners=1.2mm'
        out.append(rf'\draw[{a}] ({fmt(x1 - 0.4 * u)},{fmt(h)}) -- ({fmt(0.68 * u)},{fmt(h)}) -- ({fmt(0.68 * u)},{fmt(-1.3 * u)});')
        out.append(rf'\draw[{a}] ({fmt(0.32 * u)},{fmt(-1.3 * u)}) -- ({fmt(0.32 * u)},{fmt(h)}) -- ({fmt(x0 + 0.4 * u)},{fmt(h)});')
    return '\n'.join(out)


def launch_figure(u=4.3):
    """Input: 2 1 waiting, car 2 at the front. Partway: after 2 in, 1 in,
    1 out, car 2 waits in the siding and car 1 has left. Output: 1 2."""
    w = 7 * u
    gap = 12
    stages = [('Input', '', [], [], ['2', '1'], True),
              ('Partway', '2 in, 1 in, 1 out', ['1'], ['2'], [], False),
              ('Output', '', ['1', '2'], [], [], False)]
    out = [r'\begin{tikzpicture}[x=1mm,y=1mm]']
    for i, (title, note, d, sd, a, first) in enumerate(stages):
        dx = i * (w + gap) + 3 * u
        out.append(rf'\begin{{scope}}[shift={{({fmt(dx)},0)}}]')
        out.append(mat_panel(d, sd, a, u, labels=first, arrows=first))
        out.append(rf'\node[font=\small\bfseries] at ({fmt(0.5 * u)},{fmt(2.6 * u)}) {{{title}}};')
        if note:
            out.append(rf'\node[font=\scriptsize] at ({fmt(0.5 * u)},{fmt(1.75 * u)}) {{{note}}};')
        out.append(r'\end{scope}')
        if i < 2:
            xa = dx + 4 * u + gap / 2
            out.append(rf'\draw[-{{Stealth[length=2mm]}}, line width=0.8pt] '
                       rf'({fmt(xa - 4)},{fmt(-1.5 * u)}) -- ({fmt(xa + 4)},{fmt(-1.5 * u)});')
    out.append(r'\end{tikzpicture}')
    return '\n'.join(out)


if __name__ == '__main__':
    with open(os.path.join(HERE, 'launch-figure.tex'), 'w') as fh:
        fh.write(launch_figure() + '\n')
    print('wrote launch-figure.tex')
