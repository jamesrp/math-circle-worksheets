"""Build the Poisoned cookie (Chomp) materials file.

Writes src/materials.tex and compiles it with pdfLaTeX into ../materials.pdf.
US Letter, printed single-sided at 100%.  All drawing is in millimetres on
the page (TikZ x=1mm, y=-1mm from the top-left corner), so a 25 mm cell
prints at 25 mm.

Objects (names as the student pages use them):
  page 1  Bite card (150 mm square, cut out) and the 2 by 6 board  - every pair, all bands
  page 2  2 by 3 board, 2 by 4 board                               - grades 2-3 and 4-5 pairs
  page 3  3 by 3 board, 4 by 4 board                               - grades 2-3 and 4-5 pairs
  page 4  3 by 4 board, 3 by 5 board (landscape)                   - grades 2-3 and 4-5 pairs

Boards are drawn exactly like the 25 mm boards in the K-1 packet
(plans/topic-scouting/drafts/poisoned-cookie/src/build.py, position()):
grey cell squares, a light cookie circle in every cell and a dark poison disc
in the bottom-left cell.  Boards that share a page lie on a falling diagonal,
and the build stops if a 15 cm bite card set on one board (corner up to 3 mm
off) could reach another board, the same rule the student-page builder uses.
Run:  python3 build_materials.py
"""
import os
import shutil
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

WEEK = "Week NN"
TOPIC = "Poisoned cookie"
PACKET_ID = "NN-M-v1"

CELL = 25.0          # board squares, mm (outline: 25 mm squares)
COOKIE_R = 0.34 * CELL   # as in the student pages' position()
CARD = 150.0         # bite card side, mm (outline: about 15 by 15 cm)
SLACK = 3.0          # corner may sit up to 3 mm left of / below the cell corner
CARD_EDGE = 2.0      # width of the thick L on the card's corner edges, mm
MARGIN = 12.0        # nothing closer than this to a paper edge, mm

LETTER_P = (215.9, 279.4)
LETTER_L = (279.4, 215.9)

LABEL_GAP = 2.5      # label baseline box sits this far above its board
LABEL_H = 6.0        # room reserved above a board for its label


def f(x):
    return f"{x:.3f}".rstrip("0").rstrip(".")


# ---------------------------------------------------------------- page frame
def header_footer(w, h, page_no):
    left, right = 15.0, w - 15.0
    out = [
        f"\\node[anchor=north west,inner sep=0,font=\\fontsize{{11}}{{13}}\\selectfont] at ({f(left)},12.5) "
        f"{{{WEEK} / {TOPIC} / Materials}};",
        f"\\draw[gray,line width=0.4pt] ({f(left)},19.5) -- ({f(right)},19.5);",
        f"\\draw[gray,line width=0.4pt] ({f(left)},{f(h - 21)}) -- ({f(right)},{f(h - 21)});",
        f"\\node[anchor=north west,inner sep=0,font=\\fontsize{{9}}{{11}}\\selectfont] at ({f(left)},{f(h - 19.5)}) "
        f"{{Bellingham Math Circle / {WEEK} / {PACKET_ID}}};",
        f"\\node[anchor=north east,inner sep=0,font=\\fontsize{{9}}{{11}}\\selectfont] at ({f(right)},{f(h - 19.5)}) "
        f"{{{page_no}}};",
    ]
    return out


def content_box(w, h):
    """Top and bottom of the area between header rule and footer rule."""
    return 23.0, h - 24.0


# ---------------------------------------------------------------- objects
def board(nrows, ncols, x0, y0, label):
    """A board with its top-left corner at (x0, y0) mm, y measured down the page.
    Row 1 is the bottom row; the poison is row 1, column 1."""
    out = []
    for r in range(1, nrows + 1):
        for c in range(1, ncols + 1):
            x = x0 + (c - 1) * CELL
            y = y0 + (nrows - r) * CELL
            out.append(f"\\draw[line width=0.8pt,black!75] ({f(x)},{f(y)}) rectangle ++({f(CELL)},{f(CELL)});")
            cx, cy = x + CELL / 2, y + CELL / 2
            if (r, c) == (1, 1):
                out.append(f"\\fill[black!78] ({f(cx)},{f(cy)}) circle ({f(COOKIE_R)}mm);")
            else:
                out.append(f"\\draw[line width=0.8pt,black!35] ({f(cx)},{f(cy)}) circle ({f(COOKIE_R)}mm);")
    out.append(f"\\node[anchor=south west,inner sep=0,font=\\fontsize{{12}}{{14}}\\selectfont] "
               f"at ({f(x0)},{f(y0 - LABEL_GAP)}) {{{label}}};")
    return out


def bite_card(x0, y0):
    """The bite card: a CARD-mm square cut on its outline, with a thick L on the
    left and bottom edges marking the corner that goes on the chosen cookie,
    as in the picture on page 1 of every packet.  Left white so that thin paper
    shows as much as possible of the counters underneath."""
    s = CARD
    e = CARD_EDGE
    return [
        # thick L, drawn inside the outline so that cutting on the outline keeps it
        f"\\fill[black] ({f(x0)},{f(y0)}) rectangle ({f(x0 + e)},{f(y0 + s)});",
        f"\\fill[black] ({f(x0)},{f(y0 + s - e)}) rectangle ({f(x0 + s)},{f(y0 + s)});",
        # cut outline
        f"\\draw[line width=0.4pt,black] ({f(x0)},{f(y0)}) rectangle ({f(x0 + s)},{f(y0 + s)});",
        f"\\node[font=\\fontsize{{16}}{{19}}\\selectfont] at ({f(x0 + s / 2)},{f(y0 + s / 2)}) {{Bite card}};",
    ]


def scale_bar(x0, y0, length=100.0):
    return [
        f"\\draw[line width=0.6pt] ({f(x0)},{f(y0)}) -- ({f(x0 + length)},{f(y0)});",
        f"\\draw[line width=0.6pt] ({f(x0)},{f(y0 - 2)}) -- ({f(x0)},{f(y0 + 2)});",
        f"\\draw[line width=0.6pt] ({f(x0 + length)},{f(y0 - 2)}) -- ({f(x0 + length)},{f(y0 + 2)});",
        f"\\node[anchor=west,inner sep=0,font=\\fontsize{{9}}{{11}}\\selectfont] at ({f(x0 + length + 3)},{f(y0)}) {{100 mm}};",
    ]


# ---------------------------------------------------------------- layout
def falling_diagonal(boards, w, top, hgap, vgap):
    """Place boards (nrows, ncols, label) from top-left to bottom-right, each
    wholly right of and below the one before, centred across the page.
    Returns [(nrows, ncols, label, x0, y0)] with (x0, y0) the board's top-left."""
    total_w = sum(c * CELL for _, c, _ in boards) + hgap * (len(boards) - 1)
    x = (w - total_w) / 2
    y = top + LABEL_H
    placed = []
    for nrows, ncols, label in boards:
        placed.append((nrows, ncols, label, x, y))
        x += ncols * CELL + hgap
        y += nrows * CELL + vgap + LABEL_H
    return placed


def card_check(page, placed):
    """Stop if a bite card on one board could lie over another board on the page.
    A bite at a cell covers the CARD-mm square whose lower-left corner is the
    cell's lower-left corner (moved up to SLACK mm left and down)."""
    def cells(nrows, ncols, x0, y0):
        for r in range(1, nrows + 1):
            for c in range(1, ncols + 1):
                yield r, c, x0 + (c - 1) * CELL, y0 + (nrows - r) * CELL   # top-left of cell
    for i, (ra, ca, la, xa, ya) in enumerate(placed):
        for r, c, cx, cy in cells(ra, ca, xa, ya):
            if (r, c) == (1, 1):
                continue                     # the poison is never bitten
            left, bottom = cx - SLACK, cy + CELL + SLACK        # card corner (y down)
            card = (left, bottom - CARD, left + CARD, bottom)  # x0, y0, x1, y1
            for j, (rb, cb, lb, xb, yb) in enumerate(placed):
                if i == j:
                    continue
                for _, _, bx, by in cells(rb, cb, xb, yb):
                    if bx + CELL > card[0] and bx < card[2] and by + CELL > card[1] and by < card[3]:
                        raise SystemExit(f"page {page}: a bite on the {la} reaches the {lb}")


def margin_check(page, w, h, placed, extra=()):
    for nrows, ncols, label, x0, y0 in placed:
        x1, y1 = x0 + ncols * CELL, y0 + nrows * CELL
        if x0 < MARGIN or y0 - LABEL_H < MARGIN or x1 > w - MARGIN or y1 > h - MARGIN:
            raise SystemExit(f"page {page}: {label} is within {MARGIN} mm of an edge")
    for name, (x0, y0, x1, y1) in extra:
        if x0 < MARGIN or y0 < MARGIN or x1 > w - MARGIN or y1 > h - MARGIN:
            raise SystemExit(f"page {page}: {name} is within {MARGIN} mm of an edge")


# ---------------------------------------------------------------- pages
def page(w, h, page_no, body):
    size = (f"\\paperwidth={f(w)}mm\\paperheight={f(h)}mm"
            f"\\pdfpagewidth={f(w)}mm\\pdfpageheight={f(h)}mm\n")
    pic = ("\\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm,shift={(current page.north west)}]\n"
           + "\n".join(header_footer(w, h, page_no) + body)
           + "\n\\end{tikzpicture}\\null\\newpage\n")
    return size + pic


def build_pages():
    pages = []

    # Page 1: bite card and 2 by 6 board (every pair, every band)
    w, h = LETTER_P
    top, bottom = content_box(w, h)
    cx0, cy0 = (w - CARD) / 2, top + 4.0
    body = bite_card(cx0, cy0)
    b_top = cy0 + CARD + 10.0 + LABEL_H
    placed = [(2, 6, "2 by 6 board", (w - 6 * CELL) / 2, b_top)]
    if b_top + 2 * CELL > bottom:
        raise SystemExit("page 1 overflows")
    margin_check(1, w, h, placed, [("bite card", (cx0, cy0, cx0 + CARD, cy0 + CARD))])
    for nr, nc, lab, x0, y0 in placed:
        body += board(nr, nc, x0, y0, lab)
    pages.append((w, h, body, placed))

    # Page 2: two-row boards 2 by 3 and 2 by 4, plus the scale check
    w, h = LETTER_P
    top, bottom = content_box(w, h)
    placed = falling_diagonal([(2, 3, "2 by 3 board"), (2, 4, "2 by 4 board")], w, top + 4, 12.0, 10.0)
    card_check(2, placed)
    sx, sy = placed[0][3], bottom - 10.0
    margin_check(2, w, h, placed, [("scale bar", (sx, sy - 2, sx + 118, sy + 2))])
    body = []
    for nr, nc, lab, x0, y0 in placed:
        body += board(nr, nc, x0, y0, lab)
    body += scale_bar(sx, sy)
    pages.append((w, h, body, placed))

    # Page 3: squares 3 by 3 and 4 by 4
    w, h = LETTER_P
    top, bottom = content_box(w, h)
    placed = falling_diagonal([(3, 3, "3 by 3 board"), (4, 4, "4 by 4 board")], w, top + 4, 10.0, 10.0)
    card_check(3, placed)
    margin_check(3, w, h, placed)
    if placed[-1][4] + placed[-1][0] * CELL > bottom:
        raise SystemExit("page 3 overflows")
    body = []
    for nr, nc, lab, x0, y0 in placed:
        body += board(nr, nc, x0, y0, lab)
    pages.append((w, h, body, placed))

    # Page 4 (landscape): three-row boards 3 by 4 and 3 by 5
    w, h = LETTER_L
    top, bottom = content_box(w, h)
    placed = falling_diagonal([(3, 4, "3 by 4 board"), (3, 5, "3 by 5 board")], w, top, 14.0, 3.5)
    card_check(4, placed)
    margin_check(4, w, h, placed)
    if placed[-1][4] + placed[-1][0] * CELL > bottom:
        raise SystemExit("page 4 overflows")
    body = []
    for nr, nc, lab, x0, y0 in placed:
        body += board(nr, nc, x0, y0, lab)
    pages.append((w, h, body, placed))
    return pages


PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage[letterpaper,margin=0mm]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand\familydefault{\sfdefault}
\pagestyle{empty}
\setlength\parindent{0pt}
\pdfinfoomitdate=1\pdftrailerid{}\pdfsuppressptexinfo=15
\begin{document}
"""


def main():
    pages = build_pages()
    tex = PREAMBLE + "".join(page(w, h, i + 1, body) for i, (w, h, body, _) in enumerate(pages)) + "\\end{document}\n"
    path = os.path.join(HERE, "materials.tex")
    with open(path, "w") as fh:
        fh.write(tex)
    build = os.path.join(HERE, "build")
    os.makedirs(build, exist_ok=True)
    for _ in range(2):   # remember picture needs two runs
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                            "-output-directory", build, path], capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            raise SystemExit("pdflatex failed")
    log = open(os.path.join(build, "materials.log")).read()
    problems = [bad for bad in ("Overfull", "Underfull", "Warning") if bad in log]
    if problems:
        raise SystemExit(f"log contains: {problems}")
    shutil.copy(os.path.join(build, "materials.pdf"), os.path.join(OUT, "materials.pdf"))
    print("built", os.path.join(OUT, "materials.pdf"))


if __name__ == "__main__":
    main()
