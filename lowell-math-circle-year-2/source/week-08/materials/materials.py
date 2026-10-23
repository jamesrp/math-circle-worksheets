"""Build the Week 8 separate game boards: week-08-materials.pdf.

Run:  python3 materials.py   (needs xelatex and TeX Gyre Heros, as the student
pages do; writes materials.tex here and ../materials.pdf).  Then run
check_materials.py ../materials.pdf to measure the squares and the scale line.

The adult guide asks for seven 8-by-8 and three 5-by-5 boards with 1-inch
squares and a star outlined in one corner square, nothing else.  Sheet 1 is
the 8-by-8, sheet 2 the 5-by-5.  Sheets 3 and 4 are the 8-by-8 in two halves,
for a printer that cuts off an edge of sheet 1 (the board is 8 inches wide on
8.5-inch paper).  Every sheet has a 10 cm scale line.  The star sits in the
bottom-left square, as on the student pages, and is drawn exactly as there
(src/tikzlib.py)."""
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
PID = "F08-MAT-v1"

PREAMBLE = r"""\documentclass[12pt]{extarticle}
\usepackage[letterpaper, left=0.75in, right=0.75in, top=0.75in, bottom=0.6in,
  headheight=16pt, headsep=10pt, footskip=24pt]{geometry}
\usepackage{fontspec}
\setmainfont{texgyreheros}[Extension=.otf, UprightFont=*-regular,
  BoldFont=*-bold, ItalicFont=*-italic, BoldItalicFont=*-bolditalic]
\usepackage{tikz}
\usetikzlibrary{shapes.geometric}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{Week 8 / Rook race and Nim / Game boards}
\fancyfoot[L]{Bellingham Math Circle / Week 8 / %s}
\fancyfoot[R]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
\raggedright
""" % PID


def board(cols, rows, star=True, strip=0.0):
    """cols-by-rows board of 1-inch squares, lines as on the student pages.
    strip > 0 adds a grey taping strip of that width (inches) to the left."""
    out = [r"\begin{tikzpicture}[x=1in,y=1in]"]
    if strip:
        out.append(rf"\fill[black!12] ({-strip:.4f},0) rectangle (0,{rows:.4f});")
        out.append(rf"\node[rotate=90, font=\small] at ({-strip / 2:.4f},{rows / 2:.4f}) "
                   r"{lay the left half's thick edge on this board's thick left edge};")
    out.append(rf"\draw[line width=0.9pt] (0,0) grid[step=1] ({cols},{rows});")
    out.append(rf"\draw[line width=1.4pt] (0,0) rectangle ({cols},{rows});")
    if star:
        # as src/tikzlib.py draws it on a 1-inch board
        out.append(r"\node[star, star points=5, star point ratio=2.3, draw=black, "
                   r"line width=1.3pt, inner sep=0pt, outer sep=0pt, minimum size=0.620in] "
                   r"at (0.5,0.5) {};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def scale_line():
    """A 10 cm line with end ticks, to check the printer did not scale the page."""
    return (r"\begin{tikzpicture}[x=1cm,y=1cm]" "\n"
            r"\draw[line width=1pt] (0,0) -- (10,0);" "\n"
            r"\draw[line width=1pt] (0,-0.2) -- (0,0.2);" "\n"
            r"\draw[line width=1pt] (10,-0.2) -- (10,0.2);" "\n"
            r"\node[anchor=west] at (10.3,0) {10 cm};" "\n"
            r"\end{tikzpicture}")


def sheet(title, note, body):
    """A bold title line and a short note, the board centred on the page, then
    the scale line.  One sheet per page."""
    return ("\\textbf{" + title + "}\n\n\\vspace{0.05in}\n{\\small " + note + "\\par}\n\n"
            "\\vspace{0.14in}\n"
            "\\noindent\\makebox[\\textwidth][c]{" + body + "}\n\n"
            "\\vspace{0.2in}\n"
            "\\noindent\\makebox[\\textwidth][c]{" + scale_line() + "}\n\n\\newpage\n")


CHECK = ("Print single-sided at 100\\% (\\emph{Actual size}, not \\emph{Fit to page}). "
         "Check one sheet with a ruler before printing the rest: the line under the board "
         "must measure 10 cm and each square 1 inch.")
HALVES = ("Only if your printer cuts off an edge of the 8-by-8 board on sheet 1: print one "
          "left half (sheet 3) and one right half (sheet 4) for each 8-by-8 board. ")
SHEETS = 4


def build_tex():
    t = [PREAMBLE]
    t.append(sheet("8-by-8 game board: print 7 copies (2 for each table, 1 spare).",
                   CHECK, board(8, 8)))
    t.append(sheet("5-by-5 game board: print 3 copies (2 for the grades 2--3 table, 1 spare).",
                   CHECK, board(5, 5)))
    t.append(sheet("8-by-8 game board, left half, with the star.",
                   HALVES + "Cut this half along the board's thick right edge. Lay it on the "
                   "grey strip of sheet 4 so that this edge covers sheet 4's thick left edge, "
                   "tape the halves together on the back, and check that the squares at the "
                   "join are 1 inch.",
                   board(4, 8)))
    t.append(sheet("8-by-8 game board, right half.",
                   HALVES + "The left half (sheet 3) goes on the grey strip, with its thick "
                   "right edge on this board's thick left edge.",
                   board(4, 8, star=False, strip=0.6)))
    t.append("\\end{document}\n")
    return "".join(t)


def main():
    tex = build_tex()
    path = os.path.join(HERE, "materials.tex")
    with open(path, "w") as f:
        f.write(tex)
    for _ in range(2):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "materials.tex"],
                           cwd=HERE, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            raise SystemExit("compile failed: materials")
    log = open(os.path.join(HERE, "materials.log")).read()
    for key in ("Overfull \\vbox", "Float too large"):
        if key in log:
            raise SystemExit("materials: " + key)
    m = re.search(r"Output written on materials\.pdf \((\d+) pages?", log)
    if not m or int(m.group(1)) != SHEETS:
        raise SystemExit(f"materials: expected {SHEETS} pages, one per sheet")
    os.replace(os.path.join(HERE, "materials.pdf"), os.path.join(OUT, "materials.pdf"))
    for ext in ("aux", "log"):
        p = os.path.join(HERE, "materials." + ext)
        if os.path.exists(p):
            os.remove(p)
    print("materials: ok")


if __name__ == "__main__":
    main()
