"""Figures for the Week 4 problem files (Stars and secret wheels).

A problem file's `## figure` section is a Python expression evaluated here; it
returns the LaTeX for that problem's figures. The drawing code is the old student
builder's (src/gen.py, archived in archive-before-problem-files-2026-10-23/), carried
over unchanged: rings, stars and pictures come from src/tikzlib.py, and the row,
grid, ring-cell and code-block helpers below are gen.py's. The helpers after
`parts` wrap drawings gen.py wrote inline in its page functions, so that a figure
section stays one expression. src/check.py checks the codes, rings and pictures.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
from tikzlib import (A, f, P, pieces, pic, big_ring, small_ring, dot_ring, star_lines, box, hline,  # noqa: E402,F401
                     icon, PICS, picture_ring, wheel_page, cw_arrow)

TW = 7.3  # text width in inches


def enc(s, k):
    return ''.join(A[(A.index(c) + k) % 26] if c in A else c for c in s)


def row(cells, before='0.12in'):
    """Cells spread across the full text width; the row can never wrap."""
    return (f"\\par\\vspace{{{before}}}\\noindent\\makebox[\\textwidth][s]{{\\hfill "
            + "\\hfill ".join(cells) + "\\hfill}\\par")


def center(cell, before='0.15in'):
    return f"\\par\\vspace{{{before}}}\\noindent\\makebox[\\textwidth][c]{{{cell}}}\\par"


def text(t, before='0in'):
    return f"\\par\\vspace{{{before}}}\\noindent {t}\\par"


def lines(n, gap=0.4, before='0.05in'):
    b = [hline(0, TW, -gap * (i + 1), lw='0.5pt', color='black!55') for i in range(n)]
    return f"\\par\\vspace{{{before}}}\\noindent" + pic(b, TW, gap * n + 0.05, ox=0, oy=-gap * n - 0.05) + "\\par"


def grid(cells, ncol, w, before='0.15in', between='0.2in'):
    assert ncol * w <= TW + 1e-9, (ncol, w)
    out = []
    for i in range(0, len(cells), ncol):
        out.append(row(cells[i:i + ncol], before=before if i == 0 else between))
    return "\n".join(out)


def k1_small_cell(n, hop):
    b = small_ring(n, 0.9)
    b.append(f"\\node[font=\\Large] at (0,-1.25) {{hop {hop}}};")
    return pic(b, 2.3, 2.6, oy=-1.48)


def k1_restart_cell(n, hop):
    b = small_ring(n, 1.38, dr=0.085)
    b.append(f"\\node[font=\\Large, anchor=east] at (0.05,-1.95) {{hop {hop}}};")
    b.append(box(0.62, -1.95, 0.55))
    return pic(b, 3.4, 3.75, oy=-2.3)


def k1_picture_cell(n, k, R=0.78):
    b = star_lines(n, k, R, lw='2pt')
    for i in range(n):
        x, y = P(n, i, R)
        b.append(f"\\fill ({f(x)},{f(y)}) circle (0.07);")
    b.append(hline(-1.0, 1.0, -1.32, lw='0.8pt'))
    return pic(b, 2.3, 2.42, oy=-1.42)


def k1_trial_cell(n):
    return pic(small_ring(n, 0.66), 1.8, 1.72, oy=-0.82)


def k1_icon_box(name, cx, cy, s=0.8):
    o = [box(cx, cy, s, lw='1.2pt')]
    if name:
        o += icon(name, cx, cy, s * 0.82)
    return o


def k1_arrow(x0, x1, y):
    return f"\\draw[line width=1.4pt, -{{Stealth[length=8pt]}}] ({f(x0)},{f(y)}) -- ({f(x1)},{f(y)});"


def k1_pic_ring():
    return center(pic(picture_ring(R=1.38, pr=0.40), 3.7, 3.7), before='0.25in')


def dot_r_for(n):
    return 0.045 if n <= 12 else (0.04 if n <= 18 else 0.034)


def ring_cell(n, R, rows_tex, w):
    """A ring of n dots with one or more centred lines of text under it."""
    b = dot_ring(n, R, dr=dot_r_for(n))
    y = -R - 0.3
    for t in rows_tex:
        b.append(f"\\node[font=\\normalsize] at (0,{f(y)}) {{{t}}};")
        y -= 0.5
    bottom = y + 0.5 - 0.3
    return pic(b, w, R + 0.1 - bottom, oy=bottom)


def code_block(s, before='0.2in', answer_rows=1, pitch=0.32, row_gap=0.42):
    """A code in large typewriter letters, one cell per letter, with a short write-on line under each
    letter (one line per answer row). Long codes wrap between words."""
    maxc = int(TW / pitch)
    out_lines, cur = [], ''
    for w in s.split(' '):
        cand = w if not cur else cur + ' ' + w
        if len(cand) <= maxc:
            cur = cand
        else:
            out_lines.append(cur)
            cur = w
    out_lines.append(cur)
    out = []
    for j, ln in enumerate(out_lines):
        b = []
        for i, c in enumerate(ln):
            if c == ' ':
                continue
            x = (i + 0.5) * pitch
            b.append(f"\\node[font=\\Large\\ttfamily, anchor=base] at ({f(x)},0) {{{c}}};")
            for r in range(answer_rows):
                b.append(hline(x - 0.11, x + 0.11, -0.44 - r * row_gap, lw='0.7pt', color='black!70'))
        depth = 0.44 + (answer_rows - 1) * row_gap + 0.06
        out.append(f"\\par\\vspace{{{before if j == 0 else '0.12in'}}}\\noindent"
                   + pic(b, TW, 0.28 + depth, ox=0, oy=-depth) + "\\par")
    return "\n".join(out)


def wheels():
    """The two wheels to cut out, one per page (gen.py's wheel_pages)."""
    return (center(wheel_page('outer'), before='0in') + "\n\\vfill\n\n\\newpage\n"
            + center(wheel_page('inner'), before='0in'))


def erased_cell(n, k, R, w):
    b = star_lines(n, k, R, lw='1.2pt')
    b.append(f"\\node[font=\\normalsize] at (0,{f(-R - 0.32)}) {{dots \\blank\\qquad hop \\blank}};")
    return pic(b, w, 2 * R + 0.72, oy=-R - 0.6)


# ---------------------------------------------------------------- page pieces
def parts(*xs):
    """Pieces of one page, joined as gen.py's page() joined them."""
    return "\n".join(xs)


def k1_ring(n, hops):
    """K-1: the big ring to hop on and a small ring for each hop (gen.py's k1_ring_page)."""
    return parts(center(pic(big_ring(n), 5.0, 5.0), before='0.15in'),
                 row([k1_small_cell(n, h) for h in hops], before='0.15in'))


def k1_hop_rows(top=('sun', 'tree', 'fish'), rows=6):
    """K-1 Problem 8: the picture ring beside rows of boxes, the top row drawn."""
    b = picture_ring(R=1.48, pr=0.42, cx=1.95, cy=-2.4)
    gx0, s, gap = 4.75, 0.78, 0.95
    for r in range(rows):
        y = -0.45 - r * gap - (0.12 if r else 0)
        for c in range(3):
            b += k1_icon_box(top[c] if r == 0 else None, gx0 + c * gap, y, s)
    return center(pic(b, TW, 6.2, ox=0, oy=-6.1), before='0.3in')


def k1_hop_back(rows, s=0.72):
    """K-1 Problem 9: picture, hop k, new picture, then an empty hop box back to the first picture."""
    out = []
    for j, (a_, k, b_) in enumerate(rows):
        assert PICS[(PICS.index(a_) + k) % 6] == b_
        b = k1_icon_box(a_, 0.6, 0, s) + k1_icon_box(b_, 3.3, 0, s) + k1_icon_box(a_, 6.0, 0, s)
        b += [k1_arrow(1.08, 2.82, -0.05), f"\\node[font=\\large] at (1.95,0.2) {{hop {k}}};"]
        b += [k1_arrow(3.78, 5.52, -0.05), "\\node[font=\\large, anchor=east] at (4.75,0.21) {hop};",
              box(5.0, 0.22, 0.36, lw='1pt')]
        out.append(center(pic(b, 6.6, 0.85, ox=0, oy=-0.42), before='0.35in' if j == 0 else '0.18in'))
    return parts(*out)


def k1_secret(first, then, pictures, s=0.72):
    """K-1 Problem 10: the example (first -> then by a secret hop), then each picture -> an empty box."""
    assert (PICS.index(then) - PICS.index(first)) % 6 == 3
    ex = k1_icon_box(first, 0.6, 0, s) + k1_icon_box(then, 2.6, 0, s)
    ex += [k1_arrow(1.08, 2.12, -0.05), "\\node[font=\\large] at (1.6,0.2) {secret};"]
    b = []
    for j, name in enumerate(pictures):
        x0, y = 0.5 + (j % 2) * 3.5, -(j // 2) * 1.15
        b += k1_icon_box(name, x0, y, s) + k1_icon_box(None, x0 + 2.0, y, s)
        b += [k1_arrow(x0 + 0.48, x0 + 1.52, y - 0.05), f"\\node[font=\\large] at ({f(x0 + 1.0)},{f(y + 0.2)}) {{secret}};"]
    return parts(center(pic(ex, 3.2, 0.85, ox=0, oy=-0.42), before='0.35in'),
                 center(pic(b, 6.0, 2.0, ox=0, oy=-1.57), before='0.3in'))


def second_settings(firsts):
    """Grades 2-3 Problem 9: "first setting X, second setting [box]" for each first setting."""
    b = []
    for j, s in enumerate(firsts):
        y = -j * 0.62
        b.append(f"\\node[font=\\large, anchor=west] at (0,{f(y)}) {{first setting {s}}};")
        b.append(f"\\node[font=\\large, anchor=west] at (2.45,{f(y)}) {{second setting}};")
        b.append(box(4.35, y, 0.45, 0.42))
    return center(pic(b, 4.7, 2.4, ox=-0.05, oy=-2.1), before='0.3in')


def predict_pieces(cases, drawn=2):
    """Grades 4-5 Problem 3: a "pieces" line for each case, and rings for the first `drawn` cases."""
    b = []
    for j, (n, k) in enumerate(cases):
        y = -0.3 - j * 0.6
        b.append(f"\\node[font=\\normalsize, anchor=west] at (0,{f(y)}) {{{n} dots, hop {k}}};")
        b.append(f"\\node[font=\\normalsize, anchor=west] at (1.75,{f(y)}) {{pieces}};")
        b.append(hline(2.4, 3.2, y - 0.1, lw='0.7pt', color='black'))
    Rc, cxr = 1.38, 5.45
    for j, (n, k) in enumerate(cases[:drawn]):
        cy = -1.5 - j * 3.45
        b += dot_ring(n, Rc, cx=cxr, cy=cy, dr=0.038)
        b.append(f"\\node[font=\\normalsize] at ({f(cxr)},{f(cy - Rc - 0.3)}) {{{n} dots, hop {k}}};")
    return center(pic(b, TW, 6.65, ox=0, oy=-6.6), before='0.3in')


def settings_table(rows):
    """Grades 4-5 Problem 6: first, second and single setting; None is an empty box to fill."""
    b = []
    xs = [0.0, 1.6, 3.2]
    for x, h in zip(xs, ['first setting', 'second setting', 'single setting']):
        b.append(f"\\node[font=\\normalsize, anchor=west] at ({f(x)},0) {{{h}}};")
    for j, r in enumerate(rows):
        y = -0.5 - j * 0.48
        for x, v in zip(xs, r):
            if v:
                b.append(f"\\node[font=\\large] at ({f(x + 0.55)},{f(y)}) {{{v}}};")
            else:
                b.append(box(x + 0.55, y, 0.42, 0.36))
    return center(pic(b, 4.5, 2.8, ox=-0.1, oy=-2.65), before='0.25in')


def number_row(first, last):
    """Grades 4-5 Problem 8: the ring sizes to circle."""
    nums = [f"\\node[font=\\Large] at ({f(0.2 + 0.42 * i)},0) {{{n}}};" for i, n in enumerate(range(first, last + 1))]
    return center(pic(nums, TW, 0.5, ox=0, oy=-0.25), before='0.25in')


def times_rings():
    """Grades 4-5 Problem 12: two numbered rings of 24 dots, marked x2 and x3."""
    R = 1.85
    H = 2 * R + 0.64 + 3.75
    b = dot_ring(24, R, cx=R + 0.32, cy=-R - 0.32, dr=0.035, numbers=True, numsize='\\footnotesize', numgap=0.2)
    b.append(f"\\node[font=\\LARGE] at ({f(2 * R + 0.95)},{f(-0.35)}) {{\\texttimes2}};")
    cx2, cy2 = TW - R - 0.32, -R - 0.32 - 3.75
    b += dot_ring(24, R, cx=cx2, cy=cy2, dr=0.035, numbers=True, numsize='\\footnotesize', numgap=0.2)
    b.append(f"\\node[font=\\LARGE] at ({f(cx2 - R - 0.65)},{f(cy2 - R)}) {{\\texttimes3}};")
    return center(pic(b, TW, H, ox=0, oy=-H), before='0.3in')
