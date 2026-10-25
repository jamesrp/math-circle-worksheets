#!/usr/bin/env python3
"""Write fig-launch.tex: the launch run 4 3 1 2 5 -flip 4-> 2 1 3 4 5 -flip 2-> 1 2 3 4 5,
drawn in the style of the student pages (widths grow with size, spatula in the gap)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SC = 0.56          # scale
H = 0.5 * SC       # pancake thickness
GAP = 0.2 * SC     # gap holding the spatula
PH = 0.15 * SC     # plate thickness


def pw(size):
    return (0.7 + 0.32 * size) * SC


def f(v):
    return f"{v:.3f}"


def stack(x0, st, spatula=None):
    c = []
    wmax = max(pw(s) for s in st)
    plate = wmax + 0.5 * SC
    c.append(rf"\draw[platedraw, platefill, rounded corners={f(PH/2)}cm] ({f(x0-plate/2)},{f(-PH)}) rectangle ({f(x0+plate/2)},0);")
    y = 0.0
    ys = {}
    jy = None
    for idx in range(len(st) - 1, -1, -1):
        k = idx + 1
        if spatula == k:
            jy = y + GAP / 2
            y += GAP
        ys[idx] = y
        y += H
    for idx, s in enumerate(st):
        w = pw(s)
        yb = ys[idx]
        c.append(rf"\draw[cakefill, cakedraw, rounded corners={f(H*0.42)}cm] ({f(x0-w/2)},{f(yb)}) rectangle ({f(x0+w/2)},{f(yb+H)});")
        c.append(rf"\node[font=\scriptsize\bfseries, inner sep=0pt] at ({f(x0)},{f(yb+H/2)}) {{{s}}};")
    if spatula:
        wk = pw(st[spatula - 1])
        bx0 = x0 - wk / 2 + 0.25 * SC
        bx1 = x0 + wmax / 2 + 0.45 * SC
        bt = 0.035 * SC
        c.append(rf"\fill[black!65] ({f(bx0)},{f(jy-bt)}) rectangle ({f(bx1)},{f(jy+bt)});")
        ht = 0.11 * SC
        c.append(rf"\fill[black!40, rounded corners=1pt] ({f(bx1)},{f(jy-ht)}) rectangle ({f(bx1+0.8*SC)},{f(jy+ht)});")
    c.append(rf"\node[anchor=north, font=\small, inner sep=0pt] at ({f(x0)},{f(-PH-0.12)}) {{{' '.join(map(str, st))}}};")
    return c


def main():
    seq = [((4, 3, 1, 2, 5), 4, "flip 4"), ((2, 1, 3, 4, 5), 2, "flip 2"), ((1, 2, 3, 4, 5), None, None)]
    labels = ["Input", "After one flip", "Output"]
    cmds = []
    step = 4.6
    for i, (st, sp, lab) in enumerate(seq):
        x = i * step
        cmds += stack(x, st, sp)
        cmds.append(rf"\node[font=\small\bfseries] at ({f(x)},{f(5*H+0.35)}) {{{labels[i]}}};")
        if lab:
            ax0, ax1, ay = x + 1.75, x + step - 1.35, 0.9
            cmds.append(rf"\draw[-{{Stealth[length=6pt]}}, thick] ({f(ax0)},{ay}) -- ({f(ax1)},{ay});")
            cmds.append(rf"\node[above, font=\small] at ({f((ax0+ax1)/2)},{ay+0.04}) {{{lab}}};")
            cmds.append(rf"\draw[black!70, fill=black!12] ({f((ax0+ax1)/2)},{f(ay-0.35)}) circle (0.13);")
    with open(os.path.join(HERE, "fig-launch.tex"), "w") as fh:
        fh.write("\\begin{tikzpicture}\n" + "\n".join(cmds) + "\n\\end{tikzpicture}\n")


if __name__ == "__main__":
    main()
