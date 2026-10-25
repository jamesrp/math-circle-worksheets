"""Generate the Week 58 return-visit student pages (K-1, 2-3, 4-5) as LaTeX/TikZ.

Run:  python3 gen.py   (writes k-1.tex, grades-2-3.tex, grades-4-5.tex here)
Then compile each with pdflatex.  All TikZ coordinates are in millimetres.

Notes for whoever writes the facilitator guide (from the review of the draft):
- 2-3 P5/P6: in round 2 of X Z Y, Y X Z and Z Y X, the person who does not
  take the piece marks 12.5 mm into the last panel (a quarter panel, worth 2).
  The outcome only needs that this mark lies past the taker's 75 mm mark; its
  exact place is not needed.  No quarter-panel example is printed at 2-3.
- 2-3 P1 has eight blank rows for the six colour orders on purpose.
- Recording trains needs red and blue crayons, or circles and squares in pencil.
- Card supply: the longer trains (K-1 P2, P3, P5; 2-3 P2, P4; 4-5 P1) need up
  to six reds and four blues per pair, so print one extra unmounted copy of
  materials p. 1 per pair for this visit.  4-5 P8 needs two cuttable reds.
- Every cut on a strip, panel or card goes straight across (parallel to the
  colour join); a lengthwise cut would make the strip and panel tasks trivial.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent


# ------------------------------------------------------------------ preamble
def preamble(level, pid, size):
    return r"""\documentclass[%(size)s]{extarticle}
\usepackage[letterpaper,top=20mm,bottom=20mm,left=16mm,right=16mm,headheight=16pt,headsep=7mm,footskip=10mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{tgheros}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,decorations.pathreplacing}
\usepackage{fancyhdr}
\usepackage{xcolor}
\definecolor{cardred}{RGB}{206,38,38}
\definecolor{cardblue}{RGB}{28,92,196}
\colorlet{stripred}{cardred!32}
\colorlet{stripblue}{cardblue!28}
\colorlet{panelgrey}{black!20}
\colorlet{boxgrey}{black!45}
\tikzset{cardedge/.style={draw=black!70,line width=0.5pt}}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Week 58 / Fair division / %(level)s}
\fancyfoot[L]{\small Bellingham Math Circle / Week 58 / %(pid)s}
\fancyfoot[R]{\small \thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}
\newcommand{\prob}[1]{\par\noindent\textbf{Problem #1:} }
\begin{document}
""" % dict(level=level, pid=pid, size=size)


END = "\n\\end{document}\n"


def pic(body, opts=""):
    return "\\begin{tikzpicture}[x=1mm,y=1mm%s]\n%s\n\\end{tikzpicture}" % (opts, "\n".join(body))


def centered(body, opts=""):
    return "\\begin{center}\n" + pic(body, opts) + "\n\\end{center}\n"


def f(v):
    return f"{v:.2f}".rstrip('0').rstrip('.')


# ------------------------------------------------------------------ shapes
def card(x, y, kind, s, label=None, paper=False):
    """Goods card with lower-left corner (x, y) and side s mm."""
    out = []
    style = "cardedge, fill=white" if not paper else "draw=black!70, line width=0.5pt, dashed, fill=white"
    out.append(f"\\draw[{style}, rounded corners={f(0.12 * s)}mm] ({f(x)},{f(y)}) rectangle ({f(x + s)},{f(y + s)});")
    cx = x + s / 2
    cy = y + s / 2 + (0.12 * s if label else 0)
    if kind == 'R':
        out.append(f"\\fill[cardred] ({f(cx)},{f(cy)}) circle ({f(0.27 * s)}mm);")
    else:
        h = 0.24 * s
        out.append(f"\\fill[cardblue] ({f(cx - h)},{f(cy - h)}) rectangle ({f(cx + h)},{f(cy + h)});")
    if label:
        out.append(f"\\node[font=\\footnotesize] at ({f(cx)},{f(y + 0.16 * s)}) {{{label}}};")
    return out


def train(x, y, seq, s, gap):
    out = []
    for i, k in enumerate(seq):
        out += card(x + i * (s + gap), y, k, s)
    return out


def train_width(n, s, gap):
    return n * s + (n - 1) * gap


def blank_row(x, y, n, s, gap):
    out = []
    for i in range(n):
        xx = x + i * (s + gap)
        out.append(f"\\draw[boxgrey, line width=0.5pt, rounded corners={f(0.12 * s)}mm] ({f(xx)},{f(y)}) rectangle ({f(xx + s)},{f(y + s)});")
    return out


def cutline(x, y0, y1):
    return [f"\\draw[black!70, line width=1.4pt] ({f(x)},{f(y0)}) -- ({f(x)},{f(y1)});"]


def tray(x, y, w, h):
    return [f"\\draw[black!45, fill=black!6, line width=0.6pt, rounded corners=2.5mm] ({f(x)},{f(y)}) rectangle ({f(x + w)},{f(y + h)});"]


def strip(x, y, L, H, ticks=False):
    """Schematic 240 mm strip drawn L mm long; red 0-120, blue 120-240."""
    out = [f"\\fill[stripred] ({f(x)},{f(y)}) rectangle ({f(x + L / 2)},{f(y + H)});",
           f"\\fill[stripblue] ({f(x + L / 2)},{f(y)}) rectangle ({f(x + L)},{f(y + H)});",
           f"\\draw[black!70, line width=0.6pt] ({f(x)},{f(y)}) rectangle ({f(x + L)},{f(y + H)});",
           f"\\draw[black!70, line width=0.6pt] ({f(x + L / 2)},{f(y)}) -- ({f(x + L / 2)},{f(y + H)});"]
    if ticks:
        k = L / 240
        for mm in range(0, 241, 10):
            t = 2.6 if mm % 40 == 0 else 1.5
            out.append(f"\\draw[black!70, line width=0.4pt] ({f(x + mm * k)},{f(y)}) -- ({f(x + mm * k)},{f(y - t)});")
            if mm % 40 == 0:
                out.append(f"\\node[font=\\scriptsize, below] at ({f(x + mm * k)},{f(y - 2.4)}) {{{mm}}};")
        out.append(f"\\node[font=\\scriptsize, right] at ({f(x + L + 1)},{f(y - 4.6)}) {{mm}};")
    return out


def panel_row(x, y, order, H=10, labels=True, unit=1.0):
    """Row of X, Y, Z panels, each 50 mm (times unit) long."""
    out = []
    w = 50 * unit
    for i, p in enumerate(order):
        xx = x + i * w
        out.append(f"\\draw[black!70, fill=panelgrey, line width=0.6pt] ({f(xx)},{f(y)}) rectangle ({f(xx + w)},{f(y + H)});")
        out.append(f"\\node[font=\\bfseries] at ({f(xx + 7)},{f(y + H / 2)}) {{{p}}};")
    if labels:
        for i in range(4):
            out.append(f"\\draw[black!70, line width=0.4pt] ({f(x + i * w)},{f(y)}) -- ({f(x + i * w)},{f(y - 1.8)});")
            out.append(f"\\node[font=\\scriptsize, below] at ({f(x + i * w)},{f(y - 1.6)}) {{{50 * i}}};")
        out.append(f"\\node[font=\\scriptsize, right] at ({f(x + 3 * w + 1)},{f(y - 3.6)}) {{mm}};")
    return out


def two_person_cards(x, y):
    """Small pictures of the two-person cards A (red 3, blue 1) and B (red 1, blue 3)."""
    out = []
    for j, (name, r, b) in enumerate([("A", 3, 1), ("B", 1, 3)]):
        xx = x + j * 52
        out.append(f"\\draw[black!70, line width=0.6pt, rounded corners=1.5mm] ({f(xx)},{f(y)}) rectangle ({f(xx + 44)},{f(y + 22)});")
        out.append(f"\\node[font=\\Large\\bfseries] at ({f(xx + 7)},{f(y + 11)}) {{{name}}};")
        # red line
        out.append(f"\\fill[cardred] ({f(xx + 17)},{f(y + 15.5)}) circle (2.4mm);")
        out.append(f"\\node[font=\\large] at ({f(xx + 24)},{f(y + 15.5)}) {{{r}}};")
        for d in range(r):
            out.append(f"\\fill[black] ({f(xx + 29.5 + d * 4)},{f(y + 15.5)}) circle (1mm);")
        # blue line
        out.append(f"\\fill[cardblue] ({f(xx + 14.8)},{f(y + 4.3)}) rectangle ({f(xx + 19.2)},{f(y + 8.7)});")
        out.append(f"\\node[font=\\large] at ({f(xx + 24)},{f(y + 6.5)}) {{{b}}};")
        for d in range(b):
            out.append(f"\\fill[black] ({f(xx + 29.5 + d * 4)},{f(y + 6.5)}) circle (1mm);")
    return out


def three_person_table(x, y):
    """Table of the three-person cards A, B, C against panels X, Y, Z. (x, y) = top-left."""
    vals = {'A': (4, 8, 0), 'B': (0, 4, 8), 'C': (8, 0, 4)}
    out = []
    colx = [x + 40 + 22 * i for i in range(3)]
    # header panels
    for i, p in enumerate("XYZ"):
        out.append(f"\\draw[black!70, fill=panelgrey, line width=0.5pt] ({f(colx[i] - 7)},{f(y - 8)}) rectangle ({f(colx[i] + 7)},{f(y)});")
        out.append(f"\\node[font=\\bfseries] at ({f(colx[i])},{f(y - 4)}) {{{p}}};")
    for r, name in enumerate("ABC"):
        yy = y - 15 - 8 * r
        out.append(f"\\node[anchor=west] at ({f(x)},{f(yy)}) {{card {name}}};")
        for i in range(3):
            out.append(f"\\node at ({f(colx[i])},{f(yy)}) {{{vals[name][i]}}};")
    out.append(f"\\draw[black!50, line width=0.4pt] ({f(x)},{f(y - 10.5)}) -- ({f(colx[2] + 10)},{f(y - 10.5)});")
    return out


def panel_cut_example(x, y):
    """Y, 50 mm, worth 8 to card A  ->  two 25 mm halves worth 4 each."""
    out = []
    H = 10
    out.append(f"\\draw[black!70, fill=panelgrey, line width=0.6pt] ({f(x)},{f(y)}) rectangle ({f(x + 50)},{f(y + H)});")
    out.append(f"\\node[font=\\bfseries] at ({f(x + 25)},{f(y + H / 2)}) {{Y}};")
    out.append(f"\\draw[|-|, black!70, line width=0.4pt] ({f(x)},{f(y - 3)}) -- node[below, font=\\footnotesize] {{50 mm, worth 8 to card A}} ({f(x + 50)},{f(y - 3)});")
    out.append(f"\\draw[-{{Stealth[length=2.6mm]}}, line width=0.9pt] ({f(x + 56)},{f(y + H / 2)}) -- ({f(x + 70)},{f(y + H / 2)});")
    x2 = x + 76
    for j in range(2):
        xx = x2 + j * 29
        out.append(f"\\draw[black!70, fill=panelgrey, line width=0.6pt] ({f(xx)},{f(y)}) rectangle ({f(xx + 25)},{f(y + H)});")
        out.append(f"\\node[font=\\bfseries] at ({f(xx + 12.5)},{f(y + H / 2)}) {{Y}};")
        out.append(f"\\draw[|-|, black!70, line width=0.4pt] ({f(xx)},{f(y - 3)}) -- node[below, font=\\footnotesize, align=center] {{25 mm,\\\\ worth 4}} ({f(xx + 25)},{f(y - 3)});")
    return out


def share_example(x, y, s=10.0, gap=2.6):
    """RBR|BRR  ->  two trays holding RBR and BRR (a non-task worked example:
    equal counts in different orders, so the trays need not hold the same train)."""
    seq = "RBRBRR"
    out = train(x, y, seq, s, gap)
    gx = x + 3 * s + 2.5 * gap
    out += cutline(gx, y - 2.5, y + s + 2.5)
    w = train_width(6, s, gap)
    out.append(f"\\draw[-{{Stealth[length=2.8mm]}}, line width=0.9pt] ({f(x + w + 4)},{f(y + s / 2)}) -- ({f(x + w + 16)},{f(y + s / 2)});")
    tx = x + w + 21
    tw = train_width(3, s, gap) + 6
    for j, piece in enumerate(["RBR", "BRR"]):
        xx = tx + j * (tw + 5)
        out += tray(xx, y - 3, tw, s + 6)
        out += train(xx + 3, y, piece, s, gap)
    return out


# ------------------------------------------------------------------ K-1
def k1():
    pid = "W58-RV-K-v1"
    t = [preamble("K--1", pid, "14pt")]
    t.append(r"""A train is a row of goods cards. To share a train, pull it apart between cards and put each piece into one of two trays. A tray may get more than one piece. Both trays must get the same number of red cards and the same number of blue cards.
""")
    t.append(centered(share_example(0, 0, s=9.5, gap=2.5)))
    t.append("\\vspace{1mm}\n")
    t.append(r"""\prob{1}Make each train. Share it by pulling it apart at as few places as you can, and draw a line at each place.
""")
    trains = ["RBRB", "RRBB", "BRRB", "BBRR", "RBBR", "BRBR"]
    s, gap = 16, 6
    body = []
    for i, tr in enumerate(trains):
        body += train(0, -i * 27.5, tr, s, gap)
    t.append("\\vspace{1mm}\n" + centered(body))
    t.append("\\newpage\n")

    t.append(r"""\prob{2}Make each train and share it, pulling it apart at as few places as you can. Draw a line at each place, or cross out the train if it cannot be shared.
""")
    trains2 = ["RRRRBB", "BRRBRR", "RBRBR", "RRBBBBRR", "RRRRBBBB", "RRRBBBBRRR", "RRRRRRBBBB"]
    s, gap = 13, 4.2
    body = []
    for i, tr in enumerate(trains2):
        body += train(0, -i * 27, tr, s, gap)
    # invisible frame keeps all rows left-aligned on a common width
    body.append(f"\\path (0,0) -- ({f(train_width(10, s, gap))},0);")
    t.append("\\vspace{4mm}\n" + centered(body))
    t.append("\\newpage\n")

    t.append(r"""\prob{3}One player makes a train with four red cards and four blue cards that cannot be shared by pulling it apart at only one place. The other player tries to share it that way. Draw each train that could not be shared.
""")
    s, gap = 13, 4.2
    body = []
    for i in range(7):
        body += blank_row(0, -i * 27, 8, s, gap)
    t.append("\\vspace{4mm}\n" + centered(body))
    t.append("\\newpage\n")

    t.append(r"""\prob{4}Share one red and blue strip between the two trays so that both trays get the same amount of red and the same amount of blue. Mark where an adult should cut straight across the strip, using as few cuts as you can.
""")
    body = []
    for i in range(3):
        body += strip(0, -i * 50, 168, 28)
    t.append("\\vspace{8mm}\n" + centered(body))
    t.append("\\newpage\n")

    t.append(r"""\prob{5}Can you make a train that has to be pulled apart at three places to share it? You may use up to six red cards and four blue cards.
""")
    s, gap = 13, 4.2
    body = []
    for i in range(7):
        body += blank_row(0, -i * 27, 10, s, gap)
    t.append("\\vspace{4mm}\n" + centered(body))
    t.append(END)
    return "".join(t)


# ------------------------------------------------------------------ shared older-band pieces
TRAIN_RULES = r"""A train is a row of goods cards. To share a train, cut it at some of the gaps between neighbouring cards, so that every card stays whole, and put each piece into one of two trays. A tray may get more than one piece. Both trays must get the same number of red cards and the same number of blue cards.
"""

STRIP_RULE = r"""On a strip, each number is the value of the whole 120\,mm panel of that colour, and value follows length: 40\,mm of red is worth 1 to A. Every cut goes straight across the strip."""

PANEL_RULE = r"""Each number is the value of a whole 50\,mm panel. A panel may be cut straight across, and value follows length within a panel:
"""

GAME_RULES = r"""Each person marks where the piece from the left end first becomes worth 4 by their own card. Whoever marked leftmost takes that piece. The other two mark again from the new left end, aiming at 4 again, and whoever marked leftmost takes that piece. The last person takes the rest."""

TIE_RULE = r"""If two marks are at the same place, either of those people may take the piece."""


def strips_block(n, gapy=30):
    body = []
    for i in range(n):
        body += strip(0, -i * gapy, 168, 16, ticks=True)
    return body


def xyz_example_round1(x, y):
    """Worked first round on the row X Y Z.  At 2-3 X Y Z is not a task; at 4-5
    the X Y Z row of Problem 5 asks children to finish this game."""
    out = panel_row(x, y, "XYZ", H=10, labels=True)
    marks = [(25, "C"), (50, "A"), (100, "B")]
    for mm, who in marks:
        out.append(f"\\draw[black, line width=1.3pt] ({f(x + mm)},{f(y - 0.5)}) -- ({f(x + mm)},{f(y + 13)});")
        out.append(f"\\node[font=\\footnotesize, above] at ({f(x + mm)},{f(y + 13)}) {{{who}'s mark}};")
    out.append(f"\\draw[decorate, decoration={{brace, amplitude=2mm, mirror}}, line width=0.6pt] ({f(x)},{f(y - 7.5)}) -- ({f(x + 25)},{f(y - 7.5)});")
    out.append(f"\\node[font=\\footnotesize, align=center, below] at ({f(x + 12.5)},{f(y - 10)}) {{C takes\\\\this piece}};")
    out.append(f"\\draw[-{{Stealth[length=2.2mm]}}, line width=0.7pt] ({f(x + 62)},{f(y - 15)}) -- ({f(x + 26)},{f(y - 5.5)});")
    out.append(f"\\node[font=\\footnotesize, anchor=west] at ({f(x + 63)},{f(y - 15)}) {{A and B mark again from here}};")
    return out


def record_row(x, y, order):
    out = panel_row(x, y, order, H=10, labels=True)
    return out


# ------------------------------------------------------------------ grades 2-3
def g23():
    pid = "W58-RV-M-v1"
    t = [preamble("Grades 2--3", pid, "12pt")]
    t.append(TRAIN_RULES)
    t.append(centered(share_example(0, 0)))
    t.append("\\vspace{1mm}\n")
    t.append(r"""\prob{1}Find every train you can make with two red cards and two blue cards, counting only the order of the colours. Share each one with as few cuts as you can.
""")
    s, gap = 13, 5
    w = train_width(4, s, gap)
    body = []
    for i in range(8):
        col, row = i % 2, i // 2
        body += blank_row(col * (w + 28), -row * 27, 4, s, gap)
    t.append("\\vspace{4mm}\n" + centered(body))
    t.append("\\newpage\n")

    t.append(r"""\prob{2}Share each of these trains with as few cuts as you can. If a train cannot be shared, cross it out.
""")
    trains2 = ["RRRRBB", "RBBRRR", "BRRBRRBB", "RRRBBBBR", "RBRRBRB", "RRBRRRBBBR", "RBBRRRRBBR"]
    s, gap = 12.5, 4.5
    body = []
    for i, tr in enumerate(trains2):
        body += train(0, -i * 26, tr, s, gap)
    body.append(f"\\path (0,0) -- ({f(train_width(10, s, gap))},0);")
    t.append("\\vspace{4mm}\n" + centered(body))
    t.append("\\newpage\n")

    t.append(r"""\prob{3}One person uses the two-person card A, and another person uses the two-person card B.
""")
    t.append(centered(two_person_cards(0, 0)))
    t.append(STRIP_RULE + r""" Share one strip between two trays so that A finds the two trays worth the same, and B also finds them worth the same. Use as few cuts as you can. Can one cut do it? Measure on your strip from the red end, and mark in pencil before anyone cuts.
""")
    t.append("\\vspace{6mm}\n" + centered(strips_block(4, gapy=34)))
    t.append("\\newpage\n")

    t.append(r"""\prob{4}Can you make a train that needs three cuts to share it? Use an even number of red cards and an even number of blue cards.
""")
    s, gap = 10.5, 4.5
    body = []
    for i in range(8):
        body += blank_row(0, -i * 21, 12, s, gap)
    t.append("\\vspace{4mm}\n" + centered(body))
    t.append("\\newpage\n")

    t.append(r"""\prob{5}Three people use the three-person cards A, B and C, which give these values to the grey panels X, Y and Z.
""")
    t.append(centered(three_person_table(0, 0)))
    t.append(PANEL_RULE)
    t.append(centered(panel_cut_example(0, 0)))
    t.append(r"""The three people share a row of the panels with a marking game, run by a referee. """ + GAME_RULES + r"""
""")
    t.append(centered(xyz_example_round1(0, 0)))
    t.append(r"""Play the game with the panels in the order X~Z~Y.
""")
    t.append("\\vspace{3mm}\n" + centered(record_row(0, 0, "XZY")))
    t.append("\\newpage\n")

    t.append(r"""\prob{6}Play the game again with the panels in the orders Y~X~Z and Z~Y~X. In your three games, does anyone get less than 4 by their own card? Would anyone rather have someone else's piece?
""")
    body = record_row(0, 0, "YXZ") + record_row(0, -75, "ZYX")
    t.append("\\vspace{6mm}\n" + centered(body))
    t.append(END)
    return "".join(t)


# ------------------------------------------------------------------ grades 4-5
ROW45 = 26


def g45():
    pid = "W58-RV-U-v1"
    t = [preamble("Grades 4--5", pid, "12pt")]
    t.append(TRAIN_RULES)
    t.append(centered(share_example(0, 0)))
    t.append("\\vspace{1mm}\n")
    t.append(r"""\prob{1}Share each of these trains with as few cuts as you can. How can you tell, without trying, whether a train of four red cards and four blue cards can be shared with one cut?
""")
    trains = ["RRRBBBBR", "BRRBRBBR", "RRRRBBBB", "RBRRRRBRBB", "BBRRRRRRBB", "RRRRRRBB"]
    s, gap = 12, 4.4
    body = []
    for i, tr in enumerate(trains):
        body += train(0, -i * 22, tr, s, gap)
    body.append(f"\\path (0,0) -- ({f(train_width(10, s, gap))},0);")
    t.append("\\vspace{3mm}\n" + centered(body))
    t.append("\\newpage\n")

    t.append(r"""\prob{2}Can a train with an even number of red cards and an even number of blue cards ever need more than two cuts? Explain.
""")
    t.append("\\vspace{88mm}\n")
    t.append(r"""\prob{3}One person uses the two-person card A, and another person uses the two-person card B.
""")
    t.append(centered(two_person_cards(0, 0)))
    t.append(STRIP_RULE + r""" Share one strip between two trays so that A finds the two trays worth the same, and B does too. Use as few cuts as you can, and explain why fewer cuts cannot work. Is there more than one way to do it with that many cuts? If the two people held cards with any other numbers, could two cuts always do it? Explain.
""")
    t.append("\\vspace{5mm}\n" + centered(strips_block(2, gapy=30)))
    t.append("\\newpage\n")

    t.append(r"""\prob{4}Three people use the three-person cards A, B and C, which give these values to the grey panels X, Y and Z.
""")
    t.append(centered(three_person_table(0, 0)))
    t.append(PANEL_RULE)
    t.append(centered(panel_cut_example(0, 0)))
    t.append(r"""Lay the panels in the row X~Y~Z. Share the row between two trays so that each of the three people finds the two trays worth the same. Use as few cuts as you can, and explain why fewer cuts cannot work.
""")
    t.append("\\vspace{4mm}\n" + centered(record_row(0, 0, "XYZ") + record_row(0, -30, "XYZ")))
    t.append("\\newpage\n")

    t.append(r"""\prob{5}The same three people share the row with a marking game. """ + GAME_RULES.replace(
        "worth 4 by their own card.", "worth 4 by their own card, a third of their total.") + " " + TIE_RULE + r"""
""")
    t.append(centered(xyz_example_round1(0, 0)))
    t.append(r"""Finish this game, and play the game with the panels in each of the other five orders. Does anyone get less than 4 by their own card? Would anyone rather have someone else's piece?
""")
    body = []
    for i, order in enumerate(["XYZ", "XZY", "YXZ", "YZX", "ZXY", "ZYX"]):
        body += record_row(0, -i * ROW45, order)
    t.append("\\vspace{2mm}\n" + centered(body))
    t.append("\\newpage\n")

    t.append(r"""\prob{6}Explain why the marking game gives each person at least a third of their own total, whatever the order of the panels and whatever values the cards give. Giving A the whole Y, B the whole Z and C the whole X gives each of them 8 by their own card. Can the game ever do that well for all three?
""")
    t.append("\\vspace{80mm}\n")
    t.append(r"""\prob{7}Lay the goods cards touching in this row, using the paper R3. Here a card may be cut straight across, and its value is spread evenly from its left edge to its right edge.
""")
    body = []
    for i, (k, lab) in enumerate([("R", "R1"), ("B", "B1"), ("R", "R3"), ("B", "B2"), ("R", "R2")]):
        body += card(i * 25, 0, k, 25, label=lab, paper=(lab == "R3"))
    t.append(centered(body))
    t.append(r"""Two people both use the two-person card A. Where should one cut go so that each of them gets exactly half of the total by card A? Can you arrange the five cards so that the cut falls between two cards, or inside a blue card?
""")
    t.append("\\newpage\n")

    t.append(r"""\prob{8}Explain why the marking game for three people, on any row of whole goods cards, never cuts more than two cards. Three people all value every red card at 1 and every blue card at 0, as card U does. They share two paper red cards lying side by side. Can each of them get at least a third of the total while only one card is cut?
""")
    t.append(END)
    return "".join(t)


if __name__ == "__main__":
    for name, fn in [("k-1", k1), ("grades-2-3", g23), ("grades-4-5", g45)]:
        (HERE / f"{name}.tex").write_text(fn())
        print("wrote", name + ".tex")
