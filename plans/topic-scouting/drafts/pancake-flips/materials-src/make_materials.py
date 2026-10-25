#!/usr/bin/env python3
"""Write and compile the Pancake flips materials page (materials.tex -> ../materials.pdf).

One US Letter page, printed single-sided at 100% on card stock, one copy per
pair plus one for the launch: pancakes 1 to 6 (4, 5, 6, 7, 8 and 9 cm across,
outline "Pancake flips", Materials) and one card spatula (about 4 x 15 cm,
facilitator guide draft, "Per pair").

The printed face of each pancake is its dark side: a solid dark brown disc
(the student pages' dark-side colour) with the size number knocked out in
white. The unprinted back of the card is the light side, so no colouring is
needed; the volunteer writes each number on the back.

Coordinates are millimetres from the top-left corner of the page, y downward,
drawn in a remember-picture overlay as in the Week 91 materials source.
"""
import os
import shutil
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)
BUILD = os.path.join(HERE, "build")

WEEK = "NN"
PAGE_W, PAGE_H = 215.9, 279.4
LEFT, RIGHT = 15.0, 200.9          # header and footer rules, as in the models

# Pancakes: (number, diameter mm, centre x, centre y). Sizes from the outline:
# 4, 5, 6, 7, 8 and 9 cm across, one size per number, 1 smallest.
PANCAKES = [
    (6, 90.0, 58.0, 84.0),
    (5, 80.0, 158.0, 80.0),
    (4, 70.0, 48.0, 170.5),
    (3, 60.0, 115.0, 148.0),
    (2, 50.0, 178.4, 152.0),
    (1, 40.0, 183.4, 208.0),
]

# Spatula, lying horizontally: blade on the left, handle on the right.
SP_X0 = 13.0            # front edge of the blade
SP_YC = 233.0           # centre line
BLADE_L, BLADE_W = 80.0, 42.0
TAPER_L = 12.0
HANDLE_W = 18.0
SP_LEN = 145.0          # overall length, front edge to handle end
BLADE_R = 8.0           # rounding of the blade's front corners

BROWN = (85, 50, 20)    # burntc in the student packets' preamble


def f(v):
    return f"{v:.3f}".rstrip("0").rstrip(".")


def digit_pt(d):
    """Font size (pt) giving digits about 0.3 d tall (Helvetica digits are about 0.71 em)."""
    return round(0.30 * d / 0.709 / 0.3528, 1)


def pancake(num, d, cx, cy):
    r = d / 2
    fs = digit_pt(d)
    gap, bar = 0.06 * fs, 0.05 * fs      # bar under the 6 (pt)
    lift = (gap + bar) / 2 if num == 6 else 0.0
    out = [rf"\fill[burnt] ({f(cx)},{f(cy)}) circle[radius={f(r)}];",
           rf"\draw[cutline] ({f(cx)},{f(cy)}) circle[radius={f(r)}];",
           rf"\node[text=white,inner sep=0pt,font=\fontsize{{{fs}}}{{{fs}}}\bfseries\selectfont] "
           rf"(n{num}) at ([yshift={f(lift)}pt]{f(cx)},{f(cy)}) {{{num}}};"]
    if num == 6:
        # Bar under the 6, so that it is not read as a 9 when a pancake lies turned round.
        out.append(rf"\fill[white] ([yshift=-{f(gap)}pt]n6.south west) rectangle "
                   rf"([yshift=-{f(gap+bar)}pt]n6.south east);")
    return out


def spatula():
    x0, yc = SP_X0, SP_YC
    hb, hh = BLADE_W / 2, HANDLE_W / 2
    xb = x0 + BLADE_L            # back of the blade
    xh = xb + TAPER_L            # start of the handle
    xe = x0 + SP_LEN             # end of the handle (rounded)
    path = (rf"({f(xh)},{f(yc-hh)}) -- ({f(xb)},{f(yc-hb)}) "
            rf"[rounded corners={f(BLADE_R)}mm] -- ({f(x0)},{f(yc-hb)}) -- ({f(x0)},{f(yc+hb)}) "
            rf"[sharp corners] -- ({f(xb)},{f(yc+hb)}) -- ({f(xh)},{f(yc+hh)}) "
            rf"-- ({f(xe-hh)},{f(yc+hh)}) arc[start angle=90,end angle=-90,radius={f(hh)}] -- cycle")
    # y is flipped (y=-1mm), so the arc above runs through the far right end of the handle.
    return [rf"\fill[spatulafill] {path};",
            rf"\draw[cutline,line join=round] {path};",
            rf"\node[font=\fontsize{{11}}{{13}}\selectfont,inner sep=0pt] at ({f((xh+xe-hh)/2)},{f(yc)}) {{spatula}};"]


def page():
    L = []
    L.append(rf"\node[anchor=north west,inner sep=0,font=\fontsize{{11}}{{14.08}}\selectfont] at ({f(LEFT)},12) "
             rf"{{Week {WEEK} / Pancake flips / Materials}};")
    L.append(rf"\draw[gray] ({f(LEFT)},20.5) -- ({f(RIGHT)},20.5);")
    L.append(rf"\node[anchor=north west,inner sep=0,font=\fontsize{{16}}{{20.48}}\selectfont] at ({f(LEFT)},25) "
             r"{Pancakes and spatula};")
    # 100 mm scale check, in the title row, clear of every piece.
    y = 29.5
    L.append(rf"\draw[line width=0.6pt] ({f(RIGHT-100)},{f(y)}) -- ({f(RIGHT)},{f(y)});")
    for x in (RIGHT - 100, RIGHT):
        L.append(rf"\draw[line width=0.6pt] ({f(x)},{f(y-2)}) -- ({f(x)},{f(y+2)});")
    L.append(rf"\node[anchor=east,inner sep=0,font=\fontsize{{9}}{{11.52}}\selectfont] at ({f(RIGHT-103)},{f(y)}) {{100 mm}};")
    for p in PANCAKES:
        L += pancake(*p)
    L += spatula()
    L.append(rf"\draw[gray] ({f(LEFT)},258.5) -- ({f(RIGHT)},258.5);")
    L.append(rf"\node[anchor=north west,inner sep=0,font=\fontsize{{9}}{{11.52}}\selectfont] at ({f(LEFT)},261) "
             rf"{{Bellingham Math Circle / Week {WEEK} / {WEEK}-M-v1}};")
    L.append(rf"\node[anchor=north east,inner sep=0,font=\fontsize{{9}}{{11.52}}\selectfont] at ({f(RIGHT)},261) {{1}};")
    return L


def tex():
    body = "\n".join(page())
    return (r"""\documentclass[12pt]{article}
\usepackage[letterpaper,margin=0mm]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand\familydefault{\sfdefault}
\pagestyle{empty}
\setlength\parindent{0pt}
\pdfinfoomitdate=1\pdftrailerid{}\pdfsuppressptexinfo=15
\definecolor{burntc}{RGB}{%d,%d,%d}
\tikzset{
  burnt/.style={fill=burntc},
  cutline/.style={draw=black,line width=0.6pt},
  spatulafill/.style={fill=black!12},
}
\begin{document}
\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm,shift={(current page.north west)}]
""" % BROWN) + body + "\n" + r"""\end{tikzpicture}\null
\end{document}
"""


def main():
    os.makedirs(BUILD, exist_ok=True)
    src = os.path.join(HERE, "materials.tex")
    with open(src, "w") as fh:
        fh.write(tex())
    for _ in range(2):  # remember picture needs a second pass
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                            f"-output-directory={BUILD}", src],
                           cwd=HERE, capture_output=True, text=True)
        if r.returncode:
            print(r.stdout[-3000:])
            raise SystemExit("pdflatex failed")
    log = open(os.path.join(BUILD, "materials.log"), errors="replace").read()
    bad = [ln for ln in log.splitlines()
           if ln.startswith(("Overfull", "Underfull", "! ")) or "Warning" in ln]
    for ln in bad:
        print("LOG:", ln)
    shutil.copy(os.path.join(BUILD, "materials.pdf"), os.path.join(RUN, "materials.pdf"))
    print("wrote", os.path.join(RUN, "materials.pdf"), "log issues:", len(bad))


if __name__ == "__main__":
    main()
