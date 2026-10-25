"""Build the three Week 62 return-visit student packets (LaTeX + TikZ).

python3 gen.py  writes k-1.tex, grades-2-3.tex, grades-4-5.tex next to this file.
Every list puzzle, move task and arrow network is taken from instances.py,
which check_all() verifies by brute force before anything is written.
"""
import os
from draw import *
from nets import NETS
import instances as I

HERE = os.path.dirname(os.path.abspath(__file__))
TEXTWIDTH = 189.0   # mm (US Letter, 13 mm side margins)

LIST_BY_KEY = {(b, p, k): (net, I.L(lists)) for b, p, k, net, lists, _ in I.LISTS}
MOVE_SET = {(b, p, net, k, s, g) for b, p, net, k, s, g, _ in I.MOVES}


def net_name(lines):
    for name, (l, _) in NETS.items():
        if l == lines:
            return name
    raise KeyError(lines)


class Board:
    def __init__(self, body, bb):
        self.bb = bb
        x0, y0, x1, y1 = bb
        self.w, self.h = x1 - x0, y1 - y0
        self.tex = ("\\begin{tikzpicture}[x=1mm, y=1mm]\n"
                    f"\\useasboundingbox ({x0:.1f},{y0:.1f}) rectangle ({x1:.1f},{y1:.1f});\n"
                    + body + "\n\\end{tikzpicture}")


# ---------------------------------------------------------------- preamble
def preamble(level, pid, base=12):
    return rf"""\documentclass[{base}pt]{{article}}
\usepackage[letterpaper, top=17mm, bottom=16mm, left=13mm, right=13mm, headheight=15pt, headsep=4mm, footskip=8mm]{{geometry}}
\usepackage[T1]{{fontenc}}
\usepackage{{helvet}}
\renewcommand{{\familydefault}}{{\sfdefault}}
\usepackage{{tikz}}
\usetikzlibrary{{arrows.meta, decorations.markings}}
\tikzset{{midarrow/.style={{postaction={{decorate}}, decoration={{markings, mark=at position 0.5 with {{\arrow{{Stealth[length=3.6mm, width=3.2mm]}}}}}}}}}}
\tikzset{{smallarrow/.style={{postaction={{decorate}}, decoration={{markings, mark=at position 0.5 with {{\arrow{{Stealth[length=2.6mm, width=2.3mm]}}}}}}}}}}
\tikzset{{bigarrow/.style={{-{{Stealth[length=3mm, width=2.6mm]}}, line width=1.1pt}}}}
\usepackage{{fancyhdr}}
\pagestyle{{fancy}}
\fancyhf{{}}
\lhead{{\normalsize Week 62 / Conflict networks / {level}}}
\lfoot{{\small Bellingham Math Circle / Week 62 / {pid}}}
\rfoot{{\small \thepage}}
\renewcommand{{\headrulewidth}}{{0pt}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0pt}}
\raggedright
\begin{{document}}
"""


def problem(n, text):
    return f"\\textbf{{Problem {n}:}} {text}\\par\n"


def para(text):
    return text + "\\par\n"


def vspace(mm):
    return f"\\vspace{{{mm}mm}}\n"


def centred(*boards, gap=12):
    tot = sum(b.w for b in boards) + gap * (len(boards) - 1)
    if tot > TEXTWIDTH + 0.5:
        print(f"  WARNING: centred row {tot:.0f} mm wide", [round(b.w) for b in boards])
    return ("\\noindent\\makebox[\\linewidth][c]{" + f"\\hspace{{{gap}mm}}".join(b.tex for b in boards) + "}\\par\n")


def row(*boards):
    """boards spread across the line with equal gaps"""
    tot = sum(b.w for b in boards)
    if tot > TEXTWIDTH - 4:
        print(f"  WARNING: row {tot:.0f} mm wide", [round(b.w) for b in boards])
    return ("\\noindent\\makebox[\\linewidth][s]{\\hfill " + " \\hfill ".join(b.tex for b in boards) + " \\hfill}\\par\n")


def newpage():
    return "\\newpage\n"


# ---------------------------------------------------------------- boards
def list_board(key, fixed=None, avoid=None, pad=1):
    lines, lists = LIST_BY_KEY[key]
    name = net_name(lines)
    _, pos = NETS[name]
    edges = parse_edges(lines)
    print(f"list board {key} ({name})")
    ang = choose_label_angles(pos, edges, lists, fixed=fixed, avoid=avoid)
    body = tikz_network(pos, edges, lists=lists, label_angles=ang)
    x0, y0, x1, y1 = bbox(pos)
    for v, a in ang.items():
        w, h = label_size(lists[v])
        ux, uy = unit(a)
        d = R_FULL + GAP + border_dist(w, h, a)
        lx, ly = pos[v][0] + d * ux, pos[v][1] + d * uy
        x0, y0 = min(x0, lx - w / 2), min(y0, ly - h / 2)
        x1, y1 = max(x1, lx + w / 2), max(y1, ly + h / 2)
    return Board(body, (x0 - pad, y0 - pad, x1 + pad, y1 + pad))


INVENT_SET = {(b, p, k): (net, printed) for b, p, k, net, printed, _ in I.INVENT}


def invent_board(key, pad=8, padx=None):
    """A network where children write two numbers next to every circle; some circles may be pre-printed."""
    net, printed = INVENT_SET[key]
    name = net_name(net)
    lines, pos = NETS[name]
    edges = parse_edges(lines)
    if printed:
        lists = I.L(printed)
        ang = choose_label_angles(pos, edges, lists)
        body = tikz_network(pos, edges, lists=lists, label_angles=ang)
    else:
        body = tikz_network(pos, edges)
    x0, y0, x1, y1 = bbox(pos)
    px = pad if padx is None else padx
    return Board(body, (x0 - px, y0 - pad, x1 + px, y1 + pad))


def blank_board(name, pad=8, padx=None):
    lines, pos = NETS[name]
    body = tikz_network(pos, parse_edges(lines))
    x0, y0, x1, y1 = bbox(pos)
    px = pad if padx is None else padx
    return Board(body, (x0 - px, y0 - pad, x1 + px, y1 + pad))


ARROW_SET = {a for _, _, _, a, _ in I.ARROWS}


def arrow_board(name, pad=2):
    lines, pos = NETS[name]
    assert lines in ARROW_SET, name
    body = tikz_network(pos, [], arrows=parse_edges(lines))
    x0, y0, x1, y1 = bbox(pos)
    return Board(body, (x0 - pad, y0 - pad, x1 + pad, y1 + pad))


def compact(name, state, s, dx, dy, letters=False, r=3.8, arrows=False, bold=(), arrow_style="smallarrow"):
    lines, pos = NETS[name]
    edges = parse_edges(lines)
    p = scaled(pos, s, dx, dy)
    nums = {w[0]: w[1:] for w in state.split()} if state else None
    lo = outward_angles(p, edges) if letters else None
    kw = dict(r=r, numbers=nums, letters=not nums, letter_font=r"\footnotesize\bfseries",
              number_font=r"\small\bfseries", line_w=0.7, letter_out=lo, bold_nodes=bold)
    if arrows:
        t = tikz_network(p, [], arrows=edges, **kw).replace("midarrow", arrow_style)
        return t, p
    return tikz_network(p, edges, **kw), p


def key_counters(x, y, nums):
    """the word Counters and a row of shaded discs: the counters that may be used"""
    out = [f"\\node[anchor=west, font=\\small] at ({x:.1f},{y:.1f}) {{Counters}};"]
    xx = x + 19
    for n in nums:
        out.append(f"\\draw[line width=0.5pt, fill=black!22] ({xx+3.2:.1f},{y:.1f}) circle (3.2mm);")
        out.append(f"\\node[font=\\small\\bfseries] at ({xx+3.2:.1f},{y:.1f}) {{{n}}};")
        xx += 8.4
    return "\n".join(out), xx


def bbox_of(p, r):
    xs = [q[0] for q in p.values()]; ys = [q[1] for q in p.values()]
    return min(xs) - r, min(ys) - r, max(xs) + r, max(ys) + r


def move_board(band, prob, name, start, goal, k, *, s=0.3, letters=True, key=None, moves=None,
               moves_len=120, goal2=None, moves_rows=1, side_by_side=False):
    """Full-size network with compact Start/Goal copies on its right (stacked, or side by side).

    moves: None, 'box' (K-1 tally box) or 'line' (move word lines).
    """
    lines, pos = NETS[name]
    assert (band, prob, lines, k, start, goal) in MOVE_SET, (band, prob, name, start, goal)
    if goal2:
        assert (band, prob, lines, k, start, goal2) in MOVE_SET
    edges = parse_edges(lines)
    body = [tikz_network(pos, edges)]
    x0, y0, x1, y1 = bbox(pos)
    cr = 3.8
    cp = scaled(pos, s)
    cx0, cy0, cx1, cy1 = bbox_of(cp, cr)
    lpad = 2.5 if letters else 0
    cw, ch = cx1 - cx0 + 2 * lpad, cy1 - cy0 + 2 * lpad
    copies = [("Start", start), ("Goal", goal)]
    if goal2:
        copies = [("Start", start), ("Goal 1", goal), ("Goal 2", goal2)]
    bx = x1 + 12
    n = len(copies)
    if side_by_side:
        hstep = max(cw, 14) + 8
        top = (y0 + y1) / 2 + (ch + 5) / 2
        for i, (lab, st) in enumerate(copies):
            xx = bx + i * hstep
            body.append(f"\\node[anchor=north west, font=\\small\\bfseries, inner sep=0] at ({xx:.1f},{top:.1f}) {{{lab}}};")
            tz, p = compact(name, st, s, xx + lpad - cx0, top - 5 - lpad - cy1, letters=letters)
            body.append(tz)
        right = bx + (n - 1) * hstep + max(cw, 14)
        bottom = min(y0, top - 5 - ch)
    else:
        step = ch + 5 + 5
        total = n * step - 5
        top = (y0 + y1) / 2 + total / 2
        yy = top
        for lab, st in copies:
            body.append(f"\\node[anchor=north west, font=\\small\\bfseries, inner sep=0] at ({bx:.1f},{yy:.1f}) {{{lab}}};")
            tz, p = compact(name, st, s, bx + lpad - cx0, yy - 5 - lpad - cy1, letters=letters)
            body.append(tz)
            yy -= step
        right = bx + max(cw, 14)
        bottom = min(y0, yy)
    top_ = max(y1, top)
    if key:
        ky = bottom - 5
        kt, kx = key_counters(x0, ky, key)
        body.append(kt)
        right = max(right, kx)
        bottom = ky - 4
    if moves == "box":
        my = bottom - 9
        body.append(f"\\node[anchor=west, font=\\small] at ({x0:.1f},{my:.1f}) {{Moves}};")
        body.append(f"\\draw[line width=0.6pt] ({x0+19:.1f},{my-6.5:.1f}) rectangle ({x0+64:.1f},{my+6.5:.1f});")
        bottom = my - 7.5
    elif moves == "line":
        for i in range(moves_rows):
            my = bottom - 9
            lab = "Moves:" if i == 0 else ""
            if goal2:
                lab = f"Goal {i+1}:"
            body.append(f"\\node[anchor=west, font=\\small] at ({x0:.1f},{my:.1f}) {{{lab}}};")
            body.append(f"\\draw[line width=0.5pt] ({x0+17:.1f},{my-2:.1f}) -- ({x0+moves_len:.1f},{my-2:.1f});")
            bottom = my - 3
        right = max(right, x0 + moves_len)
    return Board("\n".join(body), (x0 - 1, bottom - 1, right + 1, top_ + 1))


# ---------------------------------------------------------------- demos
def demo_lists():
    """input -> one counter placed -> finished, on a two-card network"""
    r = 6.5
    pos = {"A": (0, 0), "B": (20, 0)}
    edges = [("A", "B")]
    lists = {"A": [1, 3], "B": [2, 3]}
    ang = {"A": 90, "B": 90}
    out = []
    panels = [None, {"A": 3}, {"A": 3, "B": 2}]
    step = 56
    for i, cnt in enumerate(panels):
        x = i * step
        p = shift(pos, x, 0)
        out.append(tikz_network(p, edges, r=r, lists=lists, label_angles=ang, counters=cnt,
                                letter_font=r"\large\bfseries", number_font=r"\large\bfseries",
                                list_font=r"\large\bfseries", line_w=0.8))
        if i < 2:
            out.append(f"\\draw[bigarrow] ({x+31:.1f},0) -- ({x+45:.1f},0);")
    return Board("\n".join(out), (-8, -8, 2 * step + 28, 14))


def demo_move(word=True):
    """paw network: one legal move, D from 2 to 1 (the changed circle is shaded)"""
    s = 0.36
    out = []
    tz, p = compact("PAW", "A1 B2 C3 D2", s, 0, 0, letters=True, r=4.3)
    out.append(tz)
    xa = 34
    out.append(f"\\draw[bigarrow] ({xa:.1f},4) -- ({xa+16:.1f},4);")
    if word:
        out.append(f"\\node[font=\\bfseries] at ({xa+8:.1f},8.5) {{D1}};")
    tz, p2 = compact("PAW", "A1 B2 C3 D1", s, xa + 30, 0, letters=True, r=4.3, bold=("D",))
    dx, dy = p2["D"]
    tz = tz.replace(f"fill=white] ({dx:.2f},{dy:.2f})", f"fill=black!14] ({dx:.2f},{dy:.2f})", 1)
    assert "black!14" in tz
    out.append(tz)
    return Board("\n".join(out), (-11, -7, xa + 30 + 31, 18))


def header_card(x, y, n, w=13, h=15, key=True):
    """a slot header: numeral, and the key counter in its dashed circle"""
    t = (f"\\draw[line width=0.7pt, fill=white] ({x:.1f},{y:.1f}) rectangle ({x+w:.1f},{y+h:.1f});\n"
         f"\\draw[dashed, line width=0.4pt] ({x+w/2:.1f},{y+h-5:.1f}) circle (3.3mm);\n")
    if key:
        t += f"\\draw[line width=0.5pt, fill=black!22] ({x+w/2:.1f},{y+h-5:.1f}) circle (2.6mm);\n"
    t += f"\\node[font=\\bfseries] at ({x+w/2:.1f},{y+3.6:.1f}) {{{n}}};"
    return t


def header_key():
    """the four headers 1-4, each with its key counter"""
    w, h, gap = 11.5, 15, 3
    out = [header_card(i * (w + gap), 0, i + 1, w=w, h=h) for i in range(4)]
    return Board("\n".join(out), (-0.5, -0.5, 4 * w + 3 * gap + 0.5, h + 0.5))


def act_card(x, y, letter, w=10, h=11):
    return (f"\\draw[line width=0.6pt, fill=white] ({x:.1f},{y:.1f}) rectangle ({x+w:.1f},{y+h:.1f});\n"
            f"\\node[font=\\bfseries] at ({x+w/2:.1f},{y+h/2:.1f}) {{{letter}}};")


def demo_arrows():
    """arrows A->B, A->C: input network, cards under headers, counters on the network"""
    out = []
    s = 0.62
    tz, p = compact("DEMOARR", None, s, 0, 0, arrows=True, r=5.5)
    out.append(tz)
    out.append("\\draw[bigarrow] (32,0) -- (42,0);")
    hx = 48
    for i in range(4):
        out.append(header_card(hx + i * 16, 3, i + 1))
    out.append(act_card(hx + 1.5, -10, "A"))
    out.append(act_card(hx + 16 + 1.5, -10, "B"))
    out.append(act_card(hx + 16 + 1.5, -23, "C"))
    out.append(f"\\draw[bigarrow] ({hx+67:.1f},0) -- ({hx+77:.1f},0);")
    tz, p = compact("DEMOARR", "A1 B2 C2", s, hx + 88, 0, arrows=True, r=5.5, letters=True)
    out.append(tz)
    return Board("\n".join(out), (-7, -24, hx + 88 + 31, 20))


# ---------------------------------------------------------------- packets
KEY_RULE = "The headers show which colour goes with each number. "
LIST_RULES_K = (KEY_RULE + "Put one counter on each circle. Two circles joined by a line must not have the same number. "
                "The numbers next to a circle show which counters it may have.")
LIST_RULES = (KEY_RULE + "Put one counter on each circle. Two circles joined by a line must not get the same number. "
              "When numbers are printed next to a circle, its counter must be one of them.")
MOVE_RULES_K = ("A move takes one counter off a circle and puts a counter with a different number there. "
                "After every move, circles joined by a line must still have different numbers.")
MOVE_RULES = ("A move takes one counter off a circle and puts a counter with a different number there. "
              "After every move, no line may have the same number at both ends. "
              "Write a move as the circle's letter and its new number, like D1.")
ARROW_RULES = ("Lay the headers in a row, 1, 2, 3, 4, where 1 comes first. Put each card under a header, and a counter "
               "with that header's number on the card's circle. An arrow from one card to another means the first card "
               "must come earlier, under a smaller number. Cards with no arrow between them may share a header.")
LEGAL = "with different numbers at the two ends of every line"


def rules_with_key(text):
    """opening rules on the left, the four headers with their key counters on the right"""
    return ("\\noindent\\begin{minipage}[c]{0.64\\linewidth}\\raggedright " + text + "\\end{minipage}"
            "\\hfill\\begin{minipage}[c]{0.33\\linewidth}\\raggedleft " + header_key().tex + "\\end{minipage}\\par\n")


def build_k1():
    t = preamble("K--1", "W62-RV-K-v1", 12)
    # page 1
    t += rules_with_key(LIST_RULES_K) + vspace(5) + centred(demo_lists()) + vspace(5)
    t += problem(1, "Put a counter on every circle.")
    t += vspace(4)
    t += row(list_board(("K", 1, "a"), avoid="x"), list_board(("K", 1, "b"), avoid="x"))
    t += vspace(10)
    t += row(list_board(("K", 1, "c")), list_board(("K", 1, "d")))
    t += newpage()
    # page 2
    t += problem(2, "Some of these can't be done. Find them and show why.")
    t += vspace(10)
    t += row(list_board(("K", 2, "c")), list_board(("K", 2, "d")))
    t += vspace(18)
    t += centred(list_board(("K", 2, "a"), avoid="y"))
    t += vspace(18)
    t += centred(list_board(("K", 2, "b"), avoid="y"))
    t += newpage()
    # page 3
    t += problem(3, "Put a counter on every circle, or show why it can't be done.")
    t += vspace(10)
    t += centred(list_board(("K", 3, "a")))
    t += vspace(16)
    t += centred(list_board(("K", 3, "b")))
    t += newpage()
    # page 4: moves
    t += para(MOVE_RULES_K) + vspace(3) + centred(demo_move(word=False)) + vspace(4)
    t += problem(4, "Set up Start. Can you change it into Goal one move at a time, using only the counters shown?")
    t += vspace(5)
    t += centred(move_board("K", 4, "PATH2", "A1 B2", "A2 B1", 2, key=[1, 2], s=0.32, letters=False))
    t += vspace(9)
    t += centred(move_board("K", 4, "PATH2", "A1 B2", "A2 B1", 3, key=[1, 2, 3], s=0.32, letters=False))
    t += vspace(12)
    t += problem(5, "Set up Start, then change it into Goal in as few moves as you can.")
    t += vspace(5)
    t += centred(move_board("K", 5, "PATH3", "A1 B2 C1", "A2 B1 C2", 3, key=[1, 2, 3], s=0.32, letters=False))
    t += newpage()
    # page 5
    t += problem(6, "Set up Start, then change it into Goal in as few moves as you can.")
    t += vspace(5)
    t += centred(move_board("K", 6, "STAR5", "A1 B2 C2 D2 E2 F2", "A2 B1 C1 D1 E1 F1", 3, key=[1, 2, 3],
                            s=0.3, letters=False))
    t += vspace(14)
    t += problem(7, "Set up Start, then change it into Goal in as few moves as you can.")
    t += vspace(5)
    t += centred(move_board("K", 7, "SQUARE", "A1 B2 C1 D2", "A2 B1 C2 D1", 3, key=[1, 2, 3],
                            s=0.3, letters=False))
    t += newpage()
    # page 6
    t += problem(8, "Set up Start. Can you change it into Goal one move at a time, using only the counters shown?")
    t += vspace(12)
    t += centred(move_board("K", 8, "TRI", "A1 B2 C3", "A2 B3 C1", 3, key=[1, 2, 3], s=0.34, letters=False))
    t += vspace(20)
    t += centred(move_board("K", 8, "TRI", "A1 B2 C3", "A2 B3 C1", 4, key=[1, 2, 3, 4], s=0.34, letters=False))
    t += "\\end{document}\n"
    return t


def build_m():
    t = preamble("Grades 2--3", "W62-RV-M-v1", 12)
    t += rules_with_key(LIST_RULES) + vspace(4) + centred(demo_lists()) + vspace(4)
    t += problem(1, "Put a counter on every circle, or explain why it can't be done.")
    t += vspace(3)
    t += centred(list_board(("M", 1, "a"), avoid="y"))
    t += vspace(7)
    t += centred(list_board(("M", 1, "b"), avoid="y", fixed={"A": 90}))
    t += newpage()
    t += problem(2, "Which of these can be done?")
    t += vspace(8)
    t += row(list_board(("M", 2, "a"), avoid="x"), list_board(("M", 2, "b"), avoid="x"))
    t += vspace(12)
    t += row(list_board(("M", 2, "c"), avoid="x"), list_board(("M", 2, "d"), avoid="x"))
    t += newpage()
    t += problem(3, "Which of these can be done?")
    t += vspace(12)
    t += centred(list_board(("M", 3, "a")))
    t += vspace(22)
    t += centred(list_board(("M", 3, "b")))
    t += newpage()
    t += problem(4, "For each network, can you write two of the numbers 1, 2, 3, 4 next to every circle without "
                 "numbers, so that it can't be done?")
    t += vspace(6)
    t += centred(invent_board(("M", 4, "a"), pad=10, padx=4))
    t += vspace(12)
    t += centred(invent_board(("M", 4, "b"), pad=10, padx=14))
    t += newpage()
    # moves
    t += para(MOVE_RULES) + vspace(3) + centred(demo_move(word=True)) + vspace(3)
    t += problem(5, "Use counters 1, 2 and 3. Set up Start, then change it into Goal in as few moves as you can. Write your moves.")
    t += vspace(8)
    t += centred(move_board("M", 5, "PATH2", "A1 B2", "A2 B1", 3, moves="line", s=0.32, moves_len=110))
    t += vspace(14)
    t += centred(move_board("M", 5, "PATH3", "A1 B2 C1", "A2 B1 C2", 3, moves="line", s=0.32, moves_len=140))
    t += newpage()
    t += problem(6, "Use counters 1, 2 and 3. Change each Start into its Goal in as few moves as you can. Write your moves.")
    t += vspace(8)
    t += centred(move_board("M", 6, "PATH4", "A1 B2 C1 D2", "A2 B1 C2 D1", 3, moves="line", s=0.3, moves_len=170))
    t += vspace(14)
    t += centred(move_board("M", 6, "STAR5", "A1 B2 C2 D2 E2 F2", "A2 B1 C1 D1 E1 F1", 3, moves="line", s=0.3,
                            moves_len=150, moves_rows=2))
    t += newpage()
    t += problem(7, "Using only the counters shown, can you change Start into Goal? Write the fewest moves you can "
                 "find, or explain why it can't be done.")
    t += vspace(10)
    t += centred(move_board("M", 7, "TRI", "A1 B2 C3", "A2 B3 C1", 3, key=[1, 2, 3], moves="line", s=0.34, moves_len=110))
    t += vspace(18)
    t += centred(move_board("M", 7, "TRI", "A1 B2 C3", "A2 B3 C1", 4, key=[1, 2, 3, 4], moves="line", s=0.34, moves_len=110))
    t += newpage()
    t += problem(8, f"Use counters 1, 2 and 3. On which of these rings can you place counters, {LEGAL}, "
                 "so that no counter can move?")
    t += vspace(10)
    t += row(blank_board("RING4", pad=3), blank_board("RING5", pad=3))
    t += vspace(12)
    t += row(blank_board("RING6", pad=3), blank_board("RING7", pad=3))
    t += newpage()
    # arrows
    t += para(ARROW_RULES) + vspace(3) + centred(demo_arrows()) + vspace(4)
    t += problem(9, "Put every card under a header, using as few headers as you can.")
    t += vspace(10)
    t += centred(arrow_board("I1"))
    t += newpage()
    t += problem(10, "Can the cards of each network be put under the four headers?")
    t += vspace(10)
    t += row(arrow_board("CIRC3"), arrow_board("CHAIN5"))
    t += vspace(14)
    t += row(arrow_board("LAYC"), arrow_board("LAYD"))
    t += "\\end{document}\n"
    return t


def build_u():
    t = preamble("Grades 4--5", "W62-RV-U-v1", 12)
    t += rules_with_key(LIST_RULES) + vspace(4) + centred(demo_lists()) + vspace(4)
    t += problem(1, "Which of these can be done? For any that can't, explain why.")
    t += vspace(5)
    t += centred(list_board(("M", 3, "a"), avoid="y"))
    t += vspace(11)
    t += centred(list_board(("M", 3, "b"), avoid="y"))
    t += newpage()
    t += problem(2, "Can you write two of the numbers 1, 2, 3, 4 next to every circle of this network so that it can't be done? Explain.")
    t += vspace(2)
    t += centred(invent_board(("U", 2, ""), pad=7, padx=14))
    t += vspace(8)
    t += problem(3, "Can you write two of the numbers 1, 2, 3, 4 next to every circle of this tree so that it can't be done? Explain.")
    t += vspace(2)
    t += centred(invent_board(("U", 3, ""), pad=7, padx=14))
    t += newpage()
    t += problem(4, "Which of these can be done? Suppose every circle of a ring, of any size, has two numbers next to it. "
                 "When can it not be done? Explain.")
    t += vspace(8)
    t += row(list_board(("U", 4, "a"), avoid="x"), list_board(("U", 4, "b"), avoid="x"))
    t += vspace(12)
    t += row(list_board(("U", 4, "c"), avoid="x"), list_board(("U", 4, "d"), avoid="x"))
    t += newpage()
    t += para(MOVE_RULES) + vspace(3) + centred(demo_move(word=True)) + vspace(3)
    t += problem(5, "Using only the counters shown, can you change Start into Goal? Write the fewest moves you can "
                 "find, or explain why it can't be done.")
    t += vspace(6)
    t += centred(move_board("U", 5, "TRI", "A1 B2 C3", "A2 B3 C1", 3, key=[1, 2, 3], moves="line", s=0.34, moves_len=125,
                            side_by_side=True))
    t += vspace(12)
    t += centred(move_board("U", 5, "TRI", "A1 B2 C3", "A2 B3 C1", 4, key=[1, 2, 3, 4], moves="line", s=0.34, moves_len=125,
                            side_by_side=True))
    t += newpage()
    t += problem(6, f"Use counters 1, 2 and 3. On which of these rings can you place counters, {LEGAL}, "
                 "so that no counter can move? Explain.")
    t += vspace(10)
    t += row(blank_board("RING4", pad=3), blank_board("RING5", pad=3))
    t += vspace(12)
    t += row(blank_board("RING6", pad=3), blank_board("RING7", pad=3))
    t += newpage()
    t += problem(7, "Use counters 1, 2 and 3, and begin at Start each time. Which goals can you reach? Write your moves. "
                 "For a goal you can't reach, explain why.")
    t += vspace(8)
    t += centred(move_board("U", 7, "RING5", "A1 B2 C3 D1 E2", "A2 B3 C1 D2 E3", 3, goal2="A1 B3 C2 D1 E3",
                            moves="line", s=0.3, moves_len=170, moves_rows=2))
    t += newpage()
    t += problem(8, "Now counter 4 may be used too. Change Start into Goal in as few moves as you can. "
                 f"On a ring of any size, with counters 1, 2, 3, 4, can every placement {LEGAL} be changed "
                 "into every other one? Explain.")
    t += vspace(10)
    t += centred(move_board("U", 8, "RING5", "A1 B2 C3 D1 E2", "A1 B3 C2 D1 E3", 4, moves="line", s=0.3, moves_len=150))
    t += newpage()
    t += para(ARROW_RULES) + vspace(3) + centred(demo_arrows()) + vspace(4)
    t += problem(9, "Put every card under a header, using as few headers as you can. Explain why fewer headers can't work.")
    t += vspace(10)
    t += centred(arrow_board("I1"))
    t += newpage()
    t += problem(10, "Can the cards of each network be put under the four headers?")
    t += vspace(10)
    t += centred(arrow_board("I3"))
    t += vspace(16)
    t += centred(arrow_board("I2"))
    t += newpage()
    t += problem(11, "Draw an arrowhead on every line so that the longest path along the arrows passes through as few "
                 "cards as you can. Then put the cards under headers to follow your arrows. On the first network, "
                 "can you draw the arrows so that no path along the arrows passes through three cards? Explain.")
    t += vspace(6)
    t += centred(blank_board("RING5LEAF", pad=3))
    t += vspace(8)
    t += centred(blank_board("RING6LEAVES", pad=3))
    t += "\\end{document}\n"
    return t


if __name__ == "__main__":
    assert I.check_all()
    for fn, b in (("k-1.tex", build_k1), ("grades-2-3.tex", build_m), ("grades-4-5.tex", build_u)):
        print("==", fn)
        with open(os.path.join(HERE, fn), "w") as f:
            f.write(b())
