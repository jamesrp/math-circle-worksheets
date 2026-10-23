"""Generate the three Week 4 packets (K-1, 2-3, 4-5) as LaTeX and compile them.

Revision of the draft: the PDFs are written to the folder above this one (final/)."""
import os
import subprocess
from tikzlib import (A, f, P, pieces, pic, big_ring, small_ring, dot_ring, star_lines, box, hline,
                     icon, PICS, picture_ring, wheel_page, cw_arrow)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
TW = 7.3  # text width in inches


def enc(s, k):
    return ''.join(A[(A.index(c) + k) % 26] if c in A else c for c in s)


def preamble(level, pid, base='12pt'):
    return rf"""\documentclass[{base}]{{article}}
\usepackage[letterpaper, left=0.6in, right=0.6in, top=0.95in, bottom=0.95in,
  headheight=15pt, headsep=0.25in, footskip=0.45in]{{geometry}}
\usepackage[T1]{{fontenc}}
\usepackage[default]{{sourcesanspro}}
\usepackage{{inconsolata}}
\usepackage{{textcomp}}
\usepackage{{microtype}}
\usepackage{{tikz}}
\usetikzlibrary{{arrows.meta}}
\usepackage{{fancyhdr}}
\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[L]{{Week 4 / Stars and wheels / {level}}}
\fancyfoot[L]{{Bellingham Math Circle / Week 4 / {pid}}}
\fancyfoot[R]{{\thepage}}
\renewcommand{{\headrulewidth}}{{0pt}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0pt}}
\newcommand{{\prob}}[1]{{\textbf{{Problem #1:}}}}
\newcommand{{\bx}}{{\hspace{{0.07in}}\begingroup\setlength{{\fboxsep}}{{0pt}}\setlength{{\fboxrule}}{{0.8pt}}\raisebox{{-0.11in}}{{\framebox[0.42in]{{\rule{{0pt}}{{0.34in}}}}}}\endgroup}}
\newcommand{{\blank}}{{\rule[-3pt]{{0.85in}}{{0.6pt}}}}
\pagenumbering{{arabic}}
\begin{{document}}
"""


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


def page(*parts):
    return "\n".join(parts) + "\n\\vfill\n"


def build(name, pre, pages):
    tex = pre + "\n\\newpage\n".join(pages) + "\n\\end{document}\n"
    path = os.path.join(HERE, name + '.tex')
    with open(path, 'w') as fh:
        fh.write(tex)
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', name + '.tex'],
                           cwd=HERE, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            raise SystemExit(f"pdflatex failed for {name}")
    out = os.path.join(OUT, name + '.pdf')
    os.replace(os.path.join(HERE, name + '.pdf'), out)
    log = open(os.path.join(HERE, name + '.log')).read()
    for w in ('Overfull', 'Float too large'):
        if w in log:
            print(name, 'WARNING:', w, log.count(w))
    info = subprocess.run(['pdfinfo', out], capture_output=True, text=True).stdout
    npages = int([l for l in info.splitlines() if l.startswith('Pages')][0].split()[1])
    status = 'OK' if npages == len(pages) else f'OVERFLOW (expected {len(pages)})'
    print(f'built {name}: {npages} pages {status}')


def grid(cells, ncol, w, before='0.15in', between='0.2in'):
    assert ncol * w <= TW + 1e-9, (ncol, w)
    out = []
    for i in range(0, len(cells), ncol):
        out.append(row(cells[i:i + ncol], before=before if i == 0 else between))
    return "\n".join(out)


# =====================================================================  K-1
def k1_small_cell(n, hop):
    b = small_ring(n, 0.9)
    b.append(f"\\node[font=\\Large] at (0,-1.25) {{hop {hop}}};")
    return pic(b, 2.3, 2.6, oy=-1.48)


def k1_ring_page(n, hops, problem_text, first=False):
    parts = []
    if first:
        parts.append(text("To hop 2, move the counter 2 dots along the way the arrow points."))
        parts.append("\\vspace{0.14in}")
    parts.append(text(problem_text))
    parts.append(center(pic(big_ring(n), 5.0, 5.0), before='0.15in'))
    parts.append(row([k1_small_cell(n, h) for h in hops], before='0.15in'))
    return page(*parts)


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


P1_TEXT = ("Put a counter on the black dot and hop it until it is back. "
           "Draw each hop on a small ring, and circle each hop that lands on every dot.")


def make_k1():
    pages = []
    pages.append(k1_ring_page(4, [1, 2, 3], "\\prob{1} " + P1_TEXT, first=True))
    pages.append(k1_ring_page(5, [1, 2, 3], "\\prob{2} Do the same with this ring of 5 dots."))
    pages.append(k1_ring_page(6, [1, 2, 3], "\\prob{3} Do the same with this ring of 6 dots."))

    # Problem 4: start again until every dot has a line
    p = [text("\\prob{4} Draw the hops from the black dot until you are back. "
              "If a dot has no line, start again there with the same hop. "
              "Write in the box how many times you started.")]
    p.append(row([k1_restart_cell(6, 2), k1_restart_cell(6, 3)], before='0.25in'))
    p.append(row([k1_restart_cell(8, 2), k1_restart_cell(8, 3)], before='0.3in'))
    pages.append(page(*p))

    # Problem 5: which hops draw each picture, with rings to try hops on
    p = [text("\\prob{5} Find every hop from 1 to 5 that draws each picture. Write the hops under the picture.")]
    p.append(row([k1_picture_cell(5, 1), k1_picture_cell(5, 2), k1_picture_cell(6, 1)], before='0.3in'))
    p.append(row(["\\hspace{0.6in}", k1_picture_cell(6, 2), k1_picture_cell(6, 3), "\\hspace{0.6in}"],
                 before='0.3in'))
    p.append(row([k1_trial_cell(5), k1_trial_cell(5), k1_trial_cell(6), k1_trial_cell(6)], before='0.45in'))
    pages.append(page(*p))

    # Problems 6 and 7: ring of 7, every hop from 1 to 6
    pages.append(k1_ring_page(7, [1, 2, 3], "\\prob{6} " + P1_TEXT))
    pages.append(k1_ring_page(7, [4, 5, 6], "\\prob{7} Do the same with hop 4, hop 5 and hop 6 on this ring of 7 dots."))

    # Problem 8: hopping rows of pictures
    p = [text("\\prob{8} Hop 2 changes each picture into the picture 2 places along the arrow. "
              "Use hop 2 on each row to make the next row, until you get the top row again.")]
    b = picture_ring(R=1.48, pr=0.42, cx=1.95, cy=-2.4)
    top = ['sun', 'tree', 'fish']
    gx0, s, gap = 4.75, 0.78, 0.95
    for r in range(6):
        y = -0.45 - r * gap - (0.12 if r else 0)
        for c in range(3):
            b += k1_icon_box(top[c] if r == 0 else None, gx0 + c * gap, y, s)
    p.append(center(pic(b, TW, 6.2, ox=0, oy=-6.1), before='0.3in'))
    pages.append(page(*p))

    # Problem 9: hopping back, with the picture ring on the same page
    p = [text("\\prob{9} Which hop changes the picture back to what it was? Write that hop in the box.")]
    p.append(k1_pic_ring())
    rows9 = [('sun', 1, 'moon'), ('moon', 2, 'tree'), ('fish', 3, 'moon'), ('heart', 4, 'sun')]
    s = 0.72
    for j, (a_, k, b_) in enumerate(rows9):
        assert PICS[(PICS.index(a_) + k) % 6] == b_
        b = k1_icon_box(a_, 0.6, 0, s) + k1_icon_box(b_, 3.3, 0, s) + k1_icon_box(a_, 6.0, 0, s)
        b += [k1_arrow(1.08, 2.82, -0.05), f"\\node[font=\\large] at (1.95,0.2) {{hop {k}}};"]
        b += [k1_arrow(3.78, 5.52, -0.05), "\\node[font=\\large, anchor=east] at (4.75,0.21) {hop};",
              box(5.0, 0.22, 0.36, lw='1pt')]
        p.append(center(pic(b, 6.6, 0.85, ox=0, oy=-0.42), before='0.35in' if j == 0 else '0.18in'))
    pages.append(page(*p))

    # Problem 10: secret hop, with the picture ring on the same page
    p = [text("\\prob{10} A secret hop changed the sun into the tree. "
              "Draw what the same hop changes each of these pictures into.")]
    p.append(k1_pic_ring())
    assert PICS[(PICS.index('sun') + 3) % 6] == 'tree'
    ex = k1_icon_box('sun', 0.6, 0, s) + k1_icon_box('tree', 2.6, 0, s)
    ex += [k1_arrow(1.08, 2.12, -0.05), "\\node[font=\\large] at (1.6,0.2) {secret};"]
    p.append(center(pic(ex, 3.2, 0.85, ox=0, oy=-0.42), before='0.35in'))
    b = []
    for j, name in enumerate(['moon', 'heart', 'fish', 'house']):
        x0, y = 0.5 + (j % 2) * 3.5, -(j // 2) * 1.15
        b += k1_icon_box(name, x0, y, s) + k1_icon_box(None, x0 + 2.0, y, s)
        b += [k1_arrow(x0 + 0.48, x0 + 1.52, y - 0.05), f"\\node[font=\\large] at ({f(x0 + 1.0)},{f(y + 0.2)}) {{secret}};"]
    p.append(center(pic(b, 6.0, 2.0, ox=0, oy=-1.57), before='0.3in'))
    pages.append(page(*p))

    pre = preamble('K--1', 'F04-K-v4') + "\\fontsize{14}{19}\\selectfont\n"
    build('k-1', pre, pages)


# =====================================================================  2-3 and 4-5 shared
RULE = ("To draw hop 3 on a ring of dots, start at any dot and draw a straight line to the dot 3 places clockwise. "
        "Keep hopping 3 until you are back where you started. If some dots still have no line, start again at one "
        "of them, and stop when every dot has a line.")
RULE_45 = RULE + " The lines you draw from one start make one piece."


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


def wheel_setup():
    return ("Cut out the two wheels on the last two pages and join them through the middle dots with a brass "
            "fastener. Setting the wheel to D means turning it until the inner A is next to the outer D. "
            "Each letter of a message on the inner wheel goes into code as the outer letter next to it, "
            "so with the wheel set to D, CAT goes into code as FDW.")


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


def wheel_pages():
    return [page(center(wheel_page('outer'), before='0in')),
            page(center(wheel_page('inner'), before='0in'))]


# =====================================================================  2-3
def make_23():
    pages = []
    W3, W2 = 2.42, 3.6
    # p1: rings of 8
    p = [text(RULE), text("\\prob{1} Draw hop 1, hop 2, hop 3 and hop 4 on these rings of 8 dots. "
                          "Write how many times you started in the box under each drawing.", before='0.16in')]
    cells = [ring_cell(8, 1.3, [f"hop {k}\\qquad\\bx"], W2) for k in (1, 2, 3, 4)]
    p.append(grid(cells, 2, W2, before='0.3in', between='0.4in'))
    pages.append(page(*p))
    # p2: rings of 10
    p = [text("\\prob{2} Draw hop 2, hop 3, hop 4 and hop 5 on these rings of 10 dots. "
              "Write how many times you started in the box under each drawing.")]
    cells = [ring_cell(10, 1.3, [f"hop {k}\\qquad\\bx"], W2) for k in (2, 3, 4, 5)]
    p.append(grid(cells, 2, W2, before='0.35in', between='0.45in'))
    pages.append(page(*p))
    # p3: rings of 12, guess first
    p = [text("\\prob{3} Before you draw each hop on these rings of 12 dots, guess how many times you will "
              "start and write your guess. Then draw it and write how many times you did start.")]
    cells = [ring_cell(12, 1.0, [f"hop {k}", "guess~\\bx\\quad started~\\bx"], W3) for k in range(2, 7)]
    p.append(grid(cells, 3, W3, before='0.3in', between='0.45in'))
    pages.append(page(*p))
    # p4: the wheel, decoding, then partner messages
    p = [text("\\prob{4} " + wheel_setup() + " Set your wheel to D and find what each of these codes came from.")]
    for w in ["STAR", "FOX", "WHEEL", "PENCIL", "I CAN DRAW A STAR"]:
        p.append(code_block(enc(w, 3), before='0.25in' if w == "STAR" else '0.2in'))
    p.append(text("\\prob{5} Write a message of at least five words for your partner, and put it into code with a "
                  "setting you choose. Swap codes and settings with your partner, and find your partner's message.",
                  before='0.4in'))
    p.append(lines(5))
    pages.append(page(*p))
    # p5: more rings, guess first
    p = [text("\\prob{6} Before you draw each of these, guess how many times you will start and write your "
              "guess. Then draw it and write how many times you did start.")]
    cases = [(9, 2), (15, 5), (16, 6), (12, 8)]
    cells = [ring_cell(n, 1.25, [f"{n} dots, hop {k}", "guess~\\bx\\quad started~\\bx"], W2) for n, k in cases]
    p.append(grid(cells, 2, W2, before='0.3in', between='0.45in'))
    pages.append(page(*p))
    # p6: exactly 3 starts
    p = [text("\\prob{7} On each of these rings, find a hop bigger than 3 that makes you start exactly 3 times, "
              "and draw it. If a ring has no such hop, explain why.")]
    cells = [ring_cell(n, 1.2, [f"{n} dots, hop \\blank"], W2) for n in (9, 16, 18, 15)]
    p.append(grid(cells, 2, W2, before='0.25in', between='0.35in'))
    p.append(lines(3, before='0.1in'))
    pages.append(page(*p))
    # p7: cracking and undoing
    p = [text("\\prob{8} These messages were put into code with settings nobody wrote down. Find the messages.")]
    p.append(code_block(enc("A STAR CAN HAVE TEN POINTS", 7), before='0.3in'))
    p.append(code_block(enc("MEET ME BY THE BIG TREE", 16), before='0.35in'))
    p.append(text("\\prob{9} Sam put a word into code. Then he put that code into code again with a second setting, "
                  "and he got his word back. Find the second setting for each of these first settings.", before='0.6in'))
    b = []
    for j, s in enumerate("DHNW"):
        y = -j * 0.62
        b.append(f"\\node[font=\\large, anchor=west] at (0,{f(y)}) {{first setting {s}}};")
        b.append(f"\\node[font=\\large, anchor=west] at (2.45,{f(y)}) {{second setting}};")
        b.append(box(4.35, y, 0.45, 0.42))
    p.append(center(pic(b, 4.7, 2.4, ox=-0.05, oy=-2.1), before='0.3in'))
    pages.append(page(*p))
    # p8, p9: one wheel per page
    pages += wheel_pages()
    build('grades-2-3', preamble('Grades 2--3', 'F04-M-v4'), pages)


# =====================================================================  4-5
def erased_cell(n, k, R, w):
    b = star_lines(n, k, R, lw='1.2pt')
    b.append(f"\\node[font=\\normalsize] at (0,{f(-R - 0.32)}) {{dots \\blank\\qquad hop \\blank}};")
    return pic(b, w, 2 * R + 0.72, oy=-R - 0.6)


def make_45():
    pages = []
    W3, W2 = 2.42, 3.6
    # p1: rings of 12
    p = [text(RULE_45), text("\\prob{1} Draw hops 1 to 6 on these rings of 12 dots. "
                             "Write how many pieces each drawing has.", before='0.16in')]
    cells = [ring_cell(12, 1.0, [f"hop {k}", "pieces~\\bx"], W3) for k in range(1, 7)]
    p.append(grid(cells, 3, W3, before='0.3in', between='0.4in'))
    pages.append(page(*p))
    # p2: mixed rings
    p = [text("\\prob{2} Draw each of these, and write how many pieces it has.")]
    cases = [(10, 4), (9, 6), (15, 10), (16, 12), (18, 8), (24, 9)]
    cells = [ring_cell(n, 1.0, [f"{n} dots, hop {k}", "pieces~\\bx"], W3) for n, k in cases]
    p.append(grid(cells, 3, W3, before='0.3in', between='0.45in'))
    pages.append(page(*p))
    # p3: predict, then check two by drawing
    p = [text("\\prob{3} Find how many pieces each of these drawings has, without drawing it. "
              "Then draw the first two on the rings to check.")]
    cases = [(20, 8), (24, 10), (30, 12), (36, 27), (17, 5), (100, 35), (60, 45)]
    b = []
    for j, (n, k) in enumerate(cases):
        y = -0.3 - j * 0.6
        b.append(f"\\node[font=\\normalsize, anchor=west] at (0,{f(y)}) {{{n} dots, hop {k}}};")
        b.append(f"\\node[font=\\normalsize, anchor=west] at (1.75,{f(y)}) {{pieces}};")
        b.append(hline(2.4, 3.2, y - 0.1, lw='0.7pt', color='black'))
    Rc, cxr = 1.38, 5.45
    for j, (n, k) in enumerate(cases[:2]):
        cy = -1.5 - j * 3.45
        b += dot_ring(n, Rc, cx=cxr, cy=cy, dr=0.038)
        b.append(f"\\node[font=\\normalsize] at ({f(cxr)},{f(cy - Rc - 0.3)}) {{{n} dots, hop {k}}};")
    p.append(center(pic(b, TW, 6.65, ox=0, oy=-6.6), before='0.3in'))
    pages.append(page(*p))
    # p4: the wheel and cracking
    p = [text("\\prob{4} " + wheel_setup() + " These codes were made with settings nobody wrote down. "
              "Find the messages, and find two different words that the last code could have come from.")]
    p.append(code_block(enc("I DREW A STAR WITH TWELVE POINTS", 9), before='0.3in'))
    p.append(code_block(enc("WE MEET AT NOON BY THE BIG TREE", 18), before='0.35in'))
    p.append(code_block(enc("BALLOON", 23), before='0.35in'))
    p.append(code_block(enc("CHEER", 10), before='0.35in', answer_rows=2))
    assert enc("CHEER", 10) == enc("JOLLY", 3)
    pages.append(page(*p))
    # p5: partner codes, combining settings
    p = [text("\\prob{5} Write a message of at least six words, and put it into code with a setting you keep "
              "secret. Give only the code to a partner, who finds the message.")]
    p.append(lines(5))
    p.append(text("\\prob{6} Put a word into code with the wheel set to H, and then put the result into code again "
                  "with the wheel set to K. Which single setting gives the same result in one go? Find the single "
                  "setting for each pair in the table, and the missing second setting in the last row.",
                  before='0.45in'))
    b = []
    xs = [0.0, 1.6, 3.2]
    for x, h in zip(xs, ['first setting', 'second setting', 'single setting']):
        b.append(f"\\node[font=\\normalsize, anchor=west] at ({f(x)},0) {{{h}}};")
    for j, r in enumerate([('H', 'K', None), ('D', 'F', None), ('T', 'M', None), ('P', 'L', None), ('H', None, 'A')]):
        y = -0.5 - j * 0.48
        for x, v in zip(xs, r):
            if v:
                b.append(f"\\node[font=\\large] at ({f(x + 0.55)},{f(y)}) {{{v}}};")
            else:
                b.append(box(x + 0.55, y, 0.42, 0.36))
    p.append(center(pic(b, 4.5, 2.8, ox=-0.1, oy=-2.65), before='0.25in'))
    pages.append(page(*p))
    # p6: the rule for pieces, rings that always give one piece
    p = [text("\\prob{7} Write a rule that gives the number of pieces from the number of dots and the hop. "
              "Explain why your rule always works.")]
    p.append(lines(7))
    p.append(text("\\prob{8} For which rings, from 4 dots up to 20 dots, does every hop smaller than the number of "
                  "dots draw a line to every dot without starting again? Circle them, and explain why your list "
                  "is complete.", before='0.45in'))
    nums = [f"\\node[font=\\Large] at ({f(0.2 + 0.42 * i)},0) {{{n}}};" for i, n in enumerate(range(4, 21))]
    p.append(center(pic(nums, TW, 0.5, ox=0, oy=-0.25), before='0.25in'))
    p.append(lines(5))
    pages.append(page(*p))
    # p7: erased drawings
    p = [text("\\prob{9} Each of these drawings was made on a ring of dots with one hop, and then the dots were "
              "erased. Find the number of dots and a hop for each drawing.")]
    cells = [erased_cell(n, k, 1.2, W2) for n, k in [(15, 6), (20, 5), (14, 6), (21, 6)]]
    p.append(grid(cells, 2, W2, before='0.35in', between='0.5in'))
    pages.append(page(*p))
    # p8: double settings, full cycles
    p = [text("\\prob{10} Lee puts each message into code twice, with two different settings, so that it will be "
              "harder to crack. Explain whether this makes his messages any harder to crack.")]
    p.append(lines(5))
    p.append(text("\\prob{11} Set the wheel to C. Put A into code, then put the new letter into code, and keep going "
                  "until you get back to A. Which settings take A through all 26 letters before it comes back? "
                  "Explain why your list is complete.", before='0.45in'))
    p.append(lines(9))
    pages.append(page(*p))
    # p9: times tables
    p = [text("\\prob{12} On the ring marked \\texttimes2, draw a line from each dot to the dot with twice its "
              "number, counting on around the ring past 23 when you need to, so that dot 13 joins dot 2. On the "
              "ring marked \\texttimes3, draw a line from each dot to the dot with three times its number. "
              "A dot that lands on itself gets no line.")]
    R = 1.85
    H = 2 * R + 0.64 + 3.75
    b = dot_ring(24, R, cx=R + 0.32, cy=-R - 0.32, dr=0.035, numbers=True, numsize='\\footnotesize', numgap=0.2)
    b.append(f"\\node[font=\\LARGE] at ({f(2 * R + 0.95)},{f(-0.35)}) {{\\texttimes2}};")
    cx2, cy2 = TW - R - 0.32, -R - 0.32 - 3.75
    b += dot_ring(24, R, cx=cx2, cy=cy2, dr=0.035, numbers=True, numsize='\\footnotesize', numgap=0.2)
    b.append(f"\\node[font=\\LARGE] at ({f(cx2 - R - 0.65)},{f(cy2 - R)}) {{\\texttimes3}};")
    p.append(center(pic(b, TW, H, ox=0, oy=-H), before='0.3in'))
    pages.append(page(*p))
    # p10, p11: one wheel per page
    pages += wheel_pages()
    build('grades-4-5', preamble('Grades 4--5', 'F04-U-v4'), pages)


if __name__ == '__main__':
    make_k1()
    make_23()
    make_45()
