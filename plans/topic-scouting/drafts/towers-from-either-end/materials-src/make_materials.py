"""Write and compile the materials file for 'Towers from either end'.

Usage:  python3 src/make_materials.py        (from the kit-run folder or anywhere)

Writes src/materials.tex and compiles it to ../materials.pdf with pdfLaTeX.
The look follows week-91-materials.pdf: Helvetica, a TikZ overlay in
absolute millimetres, a grey rule under the header and over the footer.

Objects (named as the student pages name them):
  page 1  Strips of slots          plain strips of 4 and 3, five rows (one row per pair)
  page 2  Strips of slots, 4-5     plain strips of 6 and 5 (Grades 4-5 Problems 10-11)
  page 3  Colored strips           colored strips of 8, 6, 5 and 4 (one page per pair)

Sizes from the outline: square slots 25 mm across, so a tower of 2 cm cubes
stands inside one; slots numbered from the left in a band below the square;
colored strips shaded slot 1 red, slot 2 blue, ... in the student pages'
exact colours.  Nothing else is printed: no heights, totals or instructions.
"""
from pathlib import Path
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
WEEK = "NN"
TOPIC = "Towers from either end"
FOOT_ID = "NN-M-v1"

SLOT = 25.0          # square slot, mm (outline: about 25 mm; a 2 cm cube stands inside)
BAND = 9.0           # number band under each slot, mm
STRIP_H = SLOT + BAND
GAP_X = 10.0         # gap between two strips on one row, mm
PORTRAIT = (215.9, 279.4)
LANDSCAPE = (279.4, 215.9)

PRE = r"""\documentclass[12pt]{article}
\usepackage[letterpaper,margin=0mm]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand\familydefault{\sfdefault}
\definecolor{slotred}{RGB}{248,182,182}
\definecolor{slotblue}{RGB}{112,152,228}
\pagestyle{empty}
\setlength\parindent{0pt}
\pdfinfoomitdate=1\pdftrailerid{}\pdfsuppressptexinfo=15
\begin{document}
"""


def text(x, y, w, s, size=13):
    return (rf"\node[anchor=north west,inner sep=0,text width={w}mm,align=left,"
            rf"font=\fontsize{{{size}}}{{{size * 1.28:.1f}}}\selectfont] at ({x:.2f},{y:.2f}) {{{s}}};"
            + "\n")


def text_right(x, y, s, size=9):
    """A short label whose top-right corner is at (x, y)."""
    return (rf"\node[anchor=north east,inner sep=0,"
            rf"font=\fontsize{{{size}}}{{{size * 1.28:.1f}}}\selectfont] at ({x:.2f},{y:.2f}) {{{s}}};"
            + "\n")


def line(x, y, xx, yy, style=""):
    return rf"\draw[{style}] ({x:.2f},{y:.2f}) -- ({xx:.2f},{yy:.2f});" + "\n"


def strip(x, y, n, tint):
    """A strip of n square slots, top-left corner (x, y), y downwards.

    Each slot is a SLOT x SLOT square with its number centred in a BAND-high
    band underneath.  On a colored strip the whole column (square and band)
    is shaded, odd slots red and even slots blue, so the colour still shows in
    front of a standing tower, as in the pages' pictures.  The outer rectangle
    is the cut line."""
    s = []
    for i in range(n):
        x0 = x + i * SLOT
        fill = ("slotred" if i % 2 == 0 else "slotblue") if tint else "white"
        s.append(rf"\fill[{fill}] ({x0:.2f},{y:.2f}) rectangle ++({SLOT},{STRIP_H});")
    for i in range(n):
        x0 = x + i * SLOT
        # the square the tower stands in
        s.append(rf"\draw[line width=0.6pt] ({x0:.2f},{y:.2f}) rectangle ++({SLOT},{SLOT});")
        # the column divider through the number band
        if i:
            s.append(line(x0, y + SLOT, x0, y + STRIP_H, "line width=0.6pt").rstrip())
        s.append(rf"\node[font=\fontsize{{15}}{{18}}\selectfont,inner sep=0] at "
                 rf"({x0 + SLOT / 2:.2f},{y + SLOT + BAND / 2 + 0.2:.2f}) {{{i + 1}}};")
    # cut line
    s.append(rf"\draw[line width=1.1pt] ({x:.2f},{y:.2f}) rectangle ++({n * SLOT},{STRIP_H});")
    return "\n".join(s) + "\n"


def scale_bar(x, y, length=100):
    s = line(x, y, x + length, y, "line width=0.6pt")
    s += line(x, y - 3, x, y + 3, "line width=0.6pt")
    s += line(x + length, y - 3, x + length, y + 3, "line width=0.6pt")
    s += text(x + length + 5, y - 1.6, 60, f"{length} mm scale check", 9)
    return s


class Doc:
    def __init__(self):
        self.pages = []

    def add(self, title, body, land=False):
        w, h = LANDSCAPE if land else PORTRAIT
        p = (rf"\paperwidth={w}mm\paperheight={h}mm\pdfpagewidth={w}mm\pdfpageheight={h}mm"
             rf"\begin{{tikzpicture}}[remember picture,overlay,x=1mm,y=-1mm,"
             rf"shift={{(current page.north west)}}]" + "\n")
        p += text(15, 13, w - 30, rf"Week {WEEK} / {TOPIC} / Materials", 11)
        p += line(15, 21, w - 15, 21, "gray")
        p += text(15, 28, w - 30, title, 16)
        p += body
        p += line(15, h - 21, w - 15, h - 21, "gray")
        p += text(15, h - 17.5, w - 60, rf"Bellingham Math Circle / Week {WEEK} / {FOOT_ID}", 9)
        p += text_right(w - 15, h - 17.5, str(len(self.pages) + 1), 9)
        p += "\\end{tikzpicture}\\null\\newpage\n"
        self.pages.append(p)


def build():
    D = Doc()

    # Page 1: plain strips of 4 and 3, one row per pair, five rows.
    w, h = PORTRAIT
    row_w = 4 * SLOT + GAP_X + 3 * SLOT
    x0 = (w - row_w) / 2
    b = ""
    for r in range(5):
        y = 40 + r * (STRIP_H + 8)
        b += strip(x0, y, 4, False)
        b += strip(x0 + 4 * SLOT + GAP_X, y, 3, False)
    b += scale_bar(x0, 250)
    D.add("Strips of slots", b)

    # Page 2: plain strips of 6 and 5 for Grades 4-5 (Problems 10 and 11).
    x0 = (w - 6 * SLOT) / 2
    b = strip(x0, 42, 6, False) + strip(x0, 42 + STRIP_H + 14, 5, False)
    b += scale_bar(x0, 250)
    D.add(r"Strips of slots / Grades 4--5", b)

    # Page 3 (landscape): colored strips of 8, 6, 5 and 4, one set per pair.
    w, h = LANDSCAPE
    block_w = 5 * SLOT + GAP_X + 4 * SLOT
    x0 = (w - block_w) / 2
    b = strip(x0, 40, 8, True)
    b += strip(x0, 40 + STRIP_H + 12, 6, True)
    y3 = 40 + 2 * (STRIP_H + 12)
    b += strip(x0, y3, 5, True) + strip(x0 + 5 * SLOT + GAP_X, y3, 4, True)
    b += scale_bar(x0, 180)
    D.add("Colored strips", b, land=True)

    tex = PRE + "".join(D.pages) + "\\end{document}\n"
    src = HERE / "materials.tex"
    src.write_text(tex)
    latex = shutil.which("pdflatex")
    for _ in range(2):
        r = subprocess.run([latex, "-halt-on-error", "-interaction=nonstopmode",
                            f"-output-directory={HERE}", str(src)],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if r.returncode:
            print(r.stdout[-3000:])
            sys.exit(1)
    log = (HERE / "materials.log").read_text(errors="replace")
    bad = [k for k in ("Overfull", "Underfull", "Warning") if k in log]
    shutil.move(HERE / "materials.pdf", RUN / "materials.pdf")
    print("built", RUN / "materials.pdf", "pages:", len(D.pages),
          "log issues:", bad or "none")


if __name__ == "__main__":
    build()
