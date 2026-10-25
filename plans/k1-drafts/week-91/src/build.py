"""Build the Week 91 K-1 student pages (F91-K-v1) as LaTeX/TikZ.

Usage: python3 build.py   (writes k-1.tex next to this file; compile with pdflatex)
All diagram coordinates are in millimetres.  Every picture is set with
baseline=0, so pictures in one row line up on their top circle's centre.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- pieces

def card_arrow(x, y, d, half=3.2, lw='1.3pt'):
    """Card arrow centred at (x, y); d = 'L' (down-left) or 'R' (down-right)."""
    s = -1 if d == 'L' else 1
    return (f"\\draw[-{{Stealth[length=2.4mm,width=2.2mm]}}, line width={lw}] "
            f"({x - s*half:.2f},{y + half*1.15:.2f}) -- ({x + s*half:.2f},{y - half*1.15:.2f});")


DICE = {
    0: [],
    1: [(0, 0)],
    2: [(-1, 1), (1, -1)],
    3: [(-1, 1), (0, 0), (1, -1)],
    4: [(-1, 1), (1, 1), (-1, -1), (1, -1)],
    5: [(-1, 1), (1, 1), (0, 0), (-1, -1), (1, -1)],
}


def dots(x, y, n, step, r):
    return ''.join(f"\\fill ({x + a*step:.2f},{y + b*step:.2f}) circle ({r});" for a, b in DICE[n])


def exit_box(x, y, side, letter=None, fill=None, letter_gap=4.2):
    out = [f"\\draw[line width=0.8pt, rounded corners=1.2mm] ({x - side/2:.2f},{y - side/2:.2f}) "
           f"rectangle ({x + side/2:.2f},{y + side/2:.2f});"]
    if letter:
        out.append(f"\\node[font=\\bfseries\\large] at ({x:.2f},{y - side/2 - letter_gap:.2f}) {{{letter}}};")
    if fill:
        out.append(fill)
    return '\n'.join(out)


def switch_circle(x, y, r):
    return f"\\draw[line width=0.9pt] ({x},{y}) circle ({r});"


def counter(x, y, s=4.2):
    return (f"\\filldraw[fill=black!45, draw=black, line width=0.6pt] "
            f"({x - s/2:.2f},{y - s/2:.2f}) rectangle ({x + s/2:.2f},{y + s/2:.2f});")


def tikz(body):
    return "\\begin{tikzpicture}[x=1mm,y=1mm,baseline=0]\n" + body + "\n\\end{tikzpicture}"

# ---------------------------------------------------------------- one move

def small_card(x, y, arrow):
    """A tree card (18 x 22 mm in reality) drawn at 0.55 scale."""
    cw, ch = 9.9, 12.1
    return (f"\\draw[line width=0.6pt, fill=white] ({x - cw/2:.2f},{y - ch/2:.2f}) "
            f"rectangle ({x + cw/2:.2f},{y + ch/2:.2f});\n" + card_arrow(x, y, arrow, half=2.6, lw='1.1pt'))


def one_move_panel(arrow, counter_at, label):
    """A one-switch board with blank exits (no task's letters), drawn inside a
    light board outline, with the spare card that keeps the starting arrow
    lying beside the board."""
    r, ex, ey, side = 8.5, 12.5, -21, 13
    b = [r"\draw[line width=0.5pt, black!45, rounded corners=1.5mm] (-21,12.5) rectangle (21,-30);"]
    b.append(switch_circle(0, 0, r))
    b.append(small_card(0, 0, arrow))
    b.append(small_card(-28.5, 0, 'L'))          # spare card: the starting arrow
    for sx in (-1, 1):
        b.append(f"\\draw[line width=0.8pt] ({sx*r*0.62:.2f},{-r*0.78:.2f}) -- ({sx*ex:.2f},{ey + side/2:.2f});")
        b.append(exit_box(sx*ex, ey, side))
    if counter_at == 'beside':
        b.append(counter(r + 4.5, 0))
    else:
        b.append(counter(-ex, ey))
    b.append(f"\\node[font=\\large, anchor=base] at (0,-38) {{{label}}};")
    return tikz('\n'.join(b))

# ---------------------------------------------------------------- arrival rows

def arrival_rows(rows, boxes, side=14, gap_y=6):
    b = []
    for j in range(rows):
        y0 = -j*(side + gap_y)
        for i in range(boxes):
            x0 = i*side
            b.append(f"\\draw[line width=0.7pt] ({x0},{y0}) rectangle ({x0 + side},{y0 - side});")
            b.append(f"\\node[font=\\scriptsize, text=black!60] at ({x0 + side/2},{y0 + 2.4}) {{{i + 1}}};")
    return tikz('\n'.join(b))

# ---------------------------------------------------------------- one-switch pile picture

def switch_piles(x_n, y_n):
    r = 10.5
    ex, ey, side = 15, -29, 19
    b = [switch_circle(0, 0, r)]
    for sx, n, letter in ((-1, x_n, 'X'), (1, y_n, 'Y')):
        b.append(f"\\draw[line width=0.8pt] ({sx*r*0.62:.2f},{-r*0.78:.2f}) -- ({sx*ex:.2f},{ey + side/2:.2f});")
        b.append(exit_box(sx*ex, ey, side, letter, dots(sx*ex, ey, n, 5.0, 1.6), letter_gap=4.6))
    b.append(f"\\node[font=\\normalsize, anchor=base] at (0,{ey - side/2 - 13:.2f}) {{{x_n + y_n} counters}};")
    return tikz('\n'.join(b))

# ---------------------------------------------------------------- four-exit tree

TREE = {
    # 18 mm circles, for pages with many trees
    'compact': dict(r=9.0, lx=14, ly=-21, ex=7, ey=-40, side=10.5, step=2.9),
    # 21 mm circles (as in Problem 2), for pages with room
    'large': dict(r=10.5, lx=20, ly=-21, ex=9.5, ey=-40, side=12.5, step=3.2),
}


def tree(content=None, label=None, count=None, size='large'):
    """Three blank switch circles above exits A-D.
    content: dict letter -> ('dots', n) or ('num', k).
    label: text under the tree.  count: text beside the top circle."""
    g = TREE[size]
    r, lx, ly, ex, ey, side = g['r'], g['lx'], g['ly'], g['ex'], g['ey'], g['side']
    content = content or {}
    b = [switch_circle(0, 0, r)]
    for sx in (-1, 1):
        cx = sx*lx
        b.append(switch_circle(cx, ly, r))
        # line from top circle to lower circle
        dx, dy = cx, ly
        L = (dx*dx + dy*dy) ** 0.5
        b.append(f"\\draw[line width=0.8pt] ({dx/L*r:.2f},{dy/L*r:.2f}) -- ({dx - dx/L*r:.2f},{dy - dy/L*r:.2f});")
        for k, ox in enumerate((-ex, ex)):
            exx = cx + ox
            letter = 'ABCD'[(0 if sx < 0 else 2) + k]
            # line from lower circle to exit top
            tx, ty = exx, ey + side/2
            vx, vy = tx - cx, ty - ly
            V = (vx*vx + vy*vy) ** 0.5
            b.append(f"\\draw[line width=0.8pt] ({cx + vx/V*r:.2f},{ly + vy/V*r:.2f}) -- ({tx:.2f},{ty:.2f});")
            fill = None
            if letter in content:
                kind, val = content[letter]
                if kind == 'dots':
                    fill = dots(exx, ey, val, g['step'], 1.35)
                else:
                    fill = f"\\node[font=\\bfseries\\Large] at ({exx:.2f},{ey:.2f}) {{{val}}};"
            b.append(exit_box(exx, ey, side, letter, fill))
    if label:
        b.append(f"\\node[font=\\large, anchor=base] at (0,{ey - side/2 - 13:.2f}) {{{label}}};")
    if count:
        b.append(f"\\node[font=\\normalsize, anchor=east] at ({-r - 2.5:.2f},1) {{{count}}};")
        b.append("\\path (-39,0) (39,0);")   # same width with or without a two-digit count
    return tikz('\n'.join(b))

# ---------------------------------------------------------------- guess table

def guess_table(name, counters):
    w = [24, 27, 27]
    h, hh = 13, 9
    xs = [0, w[0], w[0] + w[1], sum(w)]
    n = len(counters)
    b = [f"\\node[font=\\large, anchor=base] at ({sum(w)/2},2.5) {{{name}}};"]
    heads = ['counter', 'guess', 'landed']
    for i, t in enumerate(heads):
        b.append(f"\\node[font=\\normalsize, text height=1.6ex, text depth=0.45ex] at ({(xs[i] + xs[i+1])/2},{-hh/2}) {{{t}}};")
    top, bottom = 0, -hh - n*h
    for x in xs:
        b.append(f"\\draw[line width=0.7pt] ({x},{top}) -- ({x},{bottom});")
    b.append(f"\\draw[line width=0.7pt] (0,{top}) -- ({xs[-1]},{top});")
    for j in range(n + 1):
        y = -hh - j*h
        b.append(f"\\draw[line width=0.7pt] (0,{y}) -- ({xs[-1]},{y});")
    for j, c in enumerate(counters):
        y = -hh - j*h - h/2
        b.append(f"\\node[font=\\Large] at ({xs[0] + w[0]/2},{y}) {{{c}}};")
    return tikz('\n'.join(b))

# ---------------------------------------------------------------- document

def problem(n, text):
    return f"\\problem{{{n}}}{{{text}}}\n"


def pair(a, b, gap=24):
    return '\\noindent\\hfill ' + a + f'\\hspace{{{gap}mm}}' + b + '\\hfill\\null\n\n'


def row(*items, sep='\\hfill'):
    return '\\noindent ' + f'\n{sep}\n'.join(items) + '\n\n'


PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage[letterpaper, top=22mm, bottom=20mm, left=15mm, right=15mm, headheight=15pt, headsep=6mm, footskip=10mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{tgheros}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyhead[L]{Week 91 / Rotor-router machines / K--1}
\fancyfoot[L]{\small Bellingham Math Circle / Week 91 / F91-K-v1}
\fancyfoot[R]{\small \thepage}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\linespread{1.15}
\newcommand{\problem}[2]{\par\noindent\textbf{Problem #1:} #2\par}
\begin{document}
"""

# Problem 6 pictures: (counters, piles A-D), read left to right, top to bottom.
P6 = [(8, (2, 2, 2, 2)), (6, (2, 1, 2, 1)),
      (6, (2, 2, 1, 1)), (12, (3, 3, 3, 3)),
      (6, (1, 2, 1, 2)), (8, (3, 1, 2, 2))]
P2 = [(2, 1), (3, 3), (2, 3), (5, 2), (5, 4), (3, 5)]
P9 = ['AD', 'DC', 'CB', 'BA']


def build():
    p = []
    # ---------- page 1: shared rules, one move, Problem 1
    p.append(r"""Before the first counter, clear the exits and point each card the way you choose.
Copy the starting arrows with spare cards beside the board.
A counter starts beside the top card and always waits beside a card, never on top of it.
At each card it moves where the arrow points, and then that card is flipped.
One counter reaches an exit before the next one starts.
The board's cards change only by flipping.

\vspace{6mm}
""")
    p.append('\\begin{center}\n' + '\\hspace{9mm}\n'.join([
        one_move_panel('L', 'beside', 'start'),
        one_move_panel('L', 'exit', 'move'),
        one_move_panel('R', 'exit', 'flip')]) + '\n\\end{center}\n\\vspace{6mm}\n')
    p.append(problem(1, "Set the card on the board with exits X and Y and send 10 counters, "
                        "writing where each one lands. Can two counters in a row land on the same exit?"))
    p.append('\\vspace{8mm}\n\\begin{center}\n' + arrival_rows(4, 10, side=15, gap_y=8) + '\n\\end{center}\n')
    p.append('\\newpage\n')

    # ---------- page 2: Problem 2
    p.append(problem(2, "Make the piles in each picture on the X and Y board, and draw the starting arrow "
                        "that makes them. Cross out any picture that no starting arrow can make."))
    pics = [switch_piles(x, y) for x, y in P2]
    p.append('\\vspace{18mm}\n')
    p.append(row(*pics[:3]))
    p.append('\\vspace{26mm}\n')
    p.append(row(*pics[3:]))
    p.append('\\newpage\n')

    # ---------- page 3: Problems 3 and 4
    p.append(problem(3, "Put the card away and toss the coin to choose X or Y for each counter. "
                        "Can the coin put two counters in a row on the same exit? "
                        "Can 7 tosses put 5 counters on one exit and 2 on the other?"))
    p.append('\\vspace{7mm}\n\\begin{center}\n' + arrival_rows(6, 7, side=13, gap_y=6) + '\n\\end{center}\n')
    p.append('\\vspace{5mm}\n')
    p.append(problem(4, "Your partner sets the card and sends one counter. Guess where each counter in the "
                        "table will land, and then send counters to see. Play again with the coin."))
    p.append('\\vspace{6mm}\n\\begin{center}\n' + guess_table('card', [5, 8, 7, 4]) +
             '\\hspace{18mm}' + guess_table('coin', [5, 8, 7, 4]) + '\n\\end{center}\n')
    p.append('\\newpage\n')

    # ---------- page 4: Problem 5
    p.append(problem(5, "Set the three cards on the board with exits A, B, C and D, draw your starting arrows, "
                        "and send four counters. Can two of the four counters land on the same exit?"))
    p.append('\\vspace{9mm}\n')
    tc = tree(size='compact')
    for k in range(3):
        p.append('\\noindent ' + tc + '\\hfill' + tc + '\\hfill' + tc + '\n\n')
        if k < 2:
            p.append('\\vspace{7mm}\n')
    p.append('\\newpage\n')

    # ---------- page 5: Problem 6
    p.append(problem(6, "Send counters on the A, B, C, D board to make the piles in each picture, "
                        "and draw the starting arrows that make them. Cross out any picture that no "
                        "starting arrows can make."))
    tp = [tree({L: ('dots', n) for L, n in zip('ABCD', piles)}, count=f"{c} counters") for c, piles in P6]
    p.append('\\vspace{12mm}\n')
    for k in range(3):
        p.append(pair(tp[2*k], tp[2*k + 1], gap=22))
        if k < 2:
            p.append('\\vspace{9mm}\n')
    p.append('\\newpage\n')

    # ---------- page 6: Problems 7 and 8
    p.append(problem(7, "Draw starting arrows that make B the first exit to get two counters. "
                        "Then draw starting arrows that make B the last exit to get two counters."))
    p.append('\\vspace{10mm}\n')
    p.append(pair(tree(label='B first'), tree(label='B last')))
    p.append('\\vspace{12mm}\n')
    p.append(problem(8, "Draw every way to set the three cards so that the first counter lands on C."))
    p.append('\\vspace{10mm}\n')
    p.append('\\noindent ' + tc + '\\hfill' + tc + '\\hfill' + tc + '\n\n')
    p.append('\\newpage\n')

    # ---------- page 7: Problem 9
    p.append(problem(9, "Draw starting arrows that send counter 1 to the exit marked 1 and counter 2 to the "
                        "exit marked 2. Cross out any picture where no starting arrows can do it."))
    tq = [tree({pr[0]: ('num', 1), pr[1]: ('num', 2)}) for pr in P9]
    p.append('\\vspace{14mm}\n')
    p.append(pair(tq[0], tq[1]))
    p.append('\\vspace{20mm}\n')
    p.append(pair(tq[2], tq[3]))

    tex = PREAMBLE + ''.join(p) + '\\end{document}\n'
    (HERE / 'k-1.tex').write_text(tex)


if __name__ == '__main__':
    build()
