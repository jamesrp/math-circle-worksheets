"""Build the Week 81 K-1 student pages (Buckets of Fish) as LaTeX/TikZ.

Run:  python3 build.py && pdflatex k-1.tex
All lengths in the TikZ pictures are millimetres.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- geometry
TEXTW = 182.5          # usable text width in mm (see \geometry below)
DOT_R = 1.7            # printed dot radius
DOT_S = 4.2            # dot spacing
GAP = 3.0              # gap between neighbouring buckets in one picture

SW, SH = 14.0, 19.0    # start-picture bucket
AW, AH = 16.0, 22.0    # answer bucket (children draw in it)


def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def dots(n, cx, by):
    """Dots for n counters resting on the bottom of a bucket: rows of three."""
    out = []
    row = 0
    left = n
    while left > 0:
        k = min(3, left)
        xs = {1: [0.0], 2: [-DOT_S / 2, DOT_S / 2], 3: [-DOT_S, 0.0, DOT_S]}[k]
        y = by + 2.2 + DOT_R + row * DOT_S
        for dx in xs:
            out.append(f"\\fill ({f(cx + dx)},{f(y)}) circle ({DOT_R});")
        left -= k
        row += 1
    return "\n".join(out)


def buckets(x, y, counts, w=SW, h=SH, labels=None, empty=False):
    """Row of buckets with bottom-left corner at (x, y); bucket numbers beneath."""
    out = []
    labels = labels or [str(i + 1) for i in range(len(counts))]
    for i, n in enumerate(counts):
        bx = x + i * (w + GAP)
        out.append(
            f"\\draw[bucket] ({f(bx)},{f(y)}) rectangle ({f(bx + w)},{f(y + h)});"
        )
        out.append(
            f"\\node[num] at ({f(bx + w / 2)},{f(y - 3.2)}) {{{labels[i]}}};"
        )
        if not empty and n:
            out.append(dots(n, bx + w / 2, y))
    return "\n".join(out)


def width(k, w):
    return k * w + (k - 1) * GAP


def circle_choices(cx, ytop):
    return (
        f"\\node[choice] at ({f(cx)},{f(ytop)}) {{1st}};\n"
        f"\\node[choice] at ({f(cx)},{f(ytop - 7)}) {{2nd}};"
    )


def arrow(x1, x2, y):
    return f"\\draw[move] ({f(x1)},{f(y)}) -- ({f(x2)},{f(y)});"


def answer_box(cx, cy, w=13.0, h=10.0):
    return (
        f"\\draw[ans] ({f(cx - w / 2)},{f(cy - h / 2)}) rectangle "
        f"({f(cx + w / 2)},{f(cy + h / 2)});"
    )


def tikz(body, height=None):
    clip = ""
    if height is not None:
        # fixed bounding box so spacing is predictable
        clip = f"\\useasboundingbox (0,0) rectangle ({f(TEXTW)},{f(height)});\n"
    return (
        "\\begin{tikzpicture}[x=1mm,y=1mm]\n" + clip + body + "\n\\end{tikzpicture}"
    )


# ---------------------------------------------------------------- pictures
def rule_panels():
    """Worked bucket-2 move for the shared rules, showing that the refill is
    optional: start (3,2); take one from bucket 2 into Removed, giving (3,1),
    OR also put one from Supply into bucket 1, giving (4,1).  (3,2) is not a
    start anywhere in the packet, and neither move is its winning move (2,2).
    Supply and Removed are drawn as square-cornered boxes, labelled inside,
    spanning the width below the buckets, as on the kit board."""
    bw, bh = 14.0, 20.0
    pw = width(2, bw)
    boxw = (pw - 1.0) / 2      # two boxes with a 1 mm gap span the panel
    boxh = 12.0
    stages = [
        dict(b=(3, 2), sup=3, rem=0, out=False, inn=False),
        dict(b=(3, 1), sup=3, rem=1, out=True, inn=False),
        dict(b=(4, 1), sup=2, rem=1, out=True, inn=True),
    ]
    # panel left edges: a wider gap before the second result leaves room for
    # the two curved arrows and the word "or" between them
    pxs = [2.0, 62.0, 136.0]
    by = boxh + 10.0   # bucket bottom; numbers sit well clear of the boxes
    out = []
    for k, st in enumerate(stages):
        px = pxs[k]
        out.append(buckets(px, by, st["b"], w=bw, h=bh))
        for j, (name, n) in enumerate((("Supply", st["sup"]), ("Removed", st["rem"]))):
            bx = px + j * (boxw + 1.0)
            out.append(f"\\draw[store] ({f(bx)},0) rectangle ({f(bx + boxw)},{f(boxh)});")
            out.append(f"\\node[tiny] at ({f(bx + boxw / 2)},{f(boxh - 2.6)}) {{{name}}};")
            xs = {0: [], 1: [0.0], 2: [-2.0, 2.0], 3: [-4.0, 0.0, 4.0]}[n]
            for dx in xs:
                out.append(f"\\fill ({f(bx + boxw / 2 + dx)},3.6) circle (1.4);")
        if st["out"]:   # bucket 2 -> Removed, curving round the right
            out.append(
                f"\\draw[flow] ({f(px + pw + 0.8)},{f(by + 7)}) to[out=0,in=0,looseness=1.4] "
                f"({f(px + pw + 0.8)},4.5);"
            )
        if st["inn"]:   # Supply -> bucket 1, curving round the left
            out.append(
                f"\\draw[flow] ({f(px - 0.8)},4.5) to[out=180,in=180,looseness=1.4] "
                f"({f(px - 0.8)},{f(by + 7)});"
            )
    # an arrow from the start to the first result, "or" before the second
    mid = by + bh / 2
    a1 = pxs[0] + pw + 7
    a2 = pxs[1] - 7
    out.append(f"\\draw[stage] ({f(a1)},{f(mid)}) -- ({f(a2)},{f(mid)});")
    orx = (pxs[1] + pw + pxs[2]) / 2
    out.append(f"\\node[orword] at ({f(orx)},{f(mid)}) {{or}};")
    return tikz("\n".join(out), height=by + bh + 1)


def rule_tree():
    """Worked bucket-3 move: from (1,0,2), taking one from bucket 3 can end
    in any of the four positions (1,0,1), (2,0,1), (1,1,1), (2,1,1).
    (1,0,2) is not a start anywhere in the packet."""
    bw, bh = 11.0, 15.0
    pw = width(3, bw)
    results = [(1, 0, 1), (2, 0, 1), (1, 1, 1), (2, 1, 1)]
    g = 10.0
    total = 4 * pw + 3 * g
    x0 = (TEXTW - total) / 2
    ry = 5.0                 # bottom of the result buckets
    sy = ry + bh + 16.0      # bottom of the start buckets
    bar = ry + bh + 6.0
    out = []
    out.append(buckets(TEXTW / 2 - pw / 2, sy, (1, 0, 2), w=bw, h=bh))
    centres = []
    for k, r in enumerate(results):
        rx = x0 + k * (pw + g)
        out.append(buckets(rx, ry, r, w=bw, h=bh))
        centres.append(rx + pw / 2)
        if k < 3:
            out.append(f"\\node[orword] at ({f(rx + pw + g / 2)},{f(ry + bh / 2)}) {{or}};")
    out.append(f"\\draw[tree] ({f(TEXTW / 2)},{f(sy - 5.6)}) -- ({f(TEXTW / 2)},{f(bar)});")
    out.append(f"\\draw[tree] ({f(centres[0])},{f(bar)}) -- ({f(centres[-1])},{f(bar)});")
    for c in centres:
        out.append(f"\\draw[treearrow] ({f(c)},{f(bar)}) -- ({f(c)},{f(ry + bh + 1.0)});")
    return tikz("\n".join(out), height=sy + bh + 1)


def p1():
    # order breaks the strict odd/even alternation of 2, 3, 4, 5, ...
    starts = [2, 5, 3, 6, 4, 7, 11, 10]
    w, h = 16.0, 24.0
    col = TEXTW / 8
    out = []
    ytop = 44.0
    for i, n in enumerate(starts):
        cx = i * col + col / 2
        out.append(buckets(cx - w / 2, ytop - h, [n], w=w, h=h))
        out.append(circle_choices(cx, ytop - h - 10))
    return tikz("\n".join(out), height=46)


def p2():
    starts = [(1, 1), (2, 0), (0, 2), (2, 1), (1, 2), (2, 2)]
    col = TEXTW / 3
    out = []
    for i, p in enumerate(starts):
        r, c = divmod(i, 3)
        cx = c * col + col / 2
        ytop = 90 - r * 46
        out.append(buckets(cx - width(2, SW) / 2, ytop - SH, p))
        out.append(circle_choices(cx, ytop - SH - 10))
    return tikz("\n".join(out), height=92)


def start_to_answer(x, y, start, aw=AW, ah=AH, sw=SW, sh=SH, arrow_len=8.0, pad=3.0):
    """Start picture, arrow, empty answer picture; (x, y) = bottom-left of answer."""
    k = len(start)
    out = []
    swid = width(k, sw)
    awid = width(k, aw)
    sy = y + (ah - sh) / 2
    out.append(buckets(x, sy, start, w=sw, h=sh))
    ax = x + swid + pad
    out.append(arrow(ax, ax + arrow_len, y + ah / 2))
    out.append(buckets(ax + arrow_len + pad, y, [0] * k, w=aw, h=ah, empty=True))
    return "\n".join(out), swid + 2 * pad + arrow_len + awid


def p3():
    starts = [(1, 1), (2, 1), (1, 2), (3, 1), (2, 3), (3, 3)]
    out = []
    _, iw = start_to_answer(0, 0, starts[0])
    colx = [0, TEXTW - iw]
    for i, p in enumerate(starts):
        r, c = divmod(i, 2)
        body, _ = start_to_answer(colx[c], 82 - r * 36, p)
        out.append(body)
    return tikz("\n".join(out), height=108)


def p4():
    starts = [(4, 2), (3, 4)]
    col = TEXTW / 2
    out = []
    for i, p in enumerate(starts):
        cx = i * col + col / 2
        ytop = 44
        out.append(buckets(cx - width(2, SW) / 2, ytop - SH, p))
        out.append(circle_choices(cx, ytop - SH - 10))
    return tikz("\n".join(out), height=46)


def p5():
    """Start (2,2) on the left; a fan of arrows to three rows (the partner has
    exactly three moves: (1,2), (2,1), (3,1)); each row: partner's result ->
    the reply that keeps every bucket in pairs."""
    out = []
    rows = 3
    rh = 32.0
    total_h = rows * rh
    sx = 6.0
    sw = width(2, SW)
    sy = total_h / 2 - SH / 2 + 1.5
    out.append(buckets(sx, sy, (2, 2)))
    gx = 66.0
    awid = width(2, AW)
    fan_from = (sx + sw + 4, sy + SH / 2)
    for r in range(rows):
        y = total_h - (r + 1) * rh + 6
        mid = y + AH / 2
        out.append(
            f"\\draw[move] ({f(fan_from[0])},{f(fan_from[1])}) -- ({f(gx - 4)},{f(mid)});"
        )
        out.append(buckets(gx, y, (0, 0), empty=True, w=AW, h=AH))
        ax = gx + awid + 6
        out.append(arrow(ax, ax + 14, mid))
        out.append(buckets(ax + 20, y, (0, 0), empty=True, w=AW, h=AH))
    return tikz("\n".join(out), height=total_h)


def p6():
    """Five slots in each row: 4 counters has 3 answers, 6 counters has 4,
    so neither row's slot count gives the answer away."""
    out = []
    w, h = 13.0, 20.0
    fw = width(2, w)
    n = 5
    step = (TEXTW - fw) / (n - 1)
    rowh = 42.0
    for r, label in enumerate(("4 counters", "6 counters")):
        top = 2 * rowh - r * rowh
        out.append(f"\\node[rowlab,anchor=north west,inner xsep=0] at (0,{f(top)}) {{{label}}};")
        y = top - 8 - h
        for k in range(n):
            out.append(buckets(k * step, y, (0, 0), w=w, h=h, empty=True))
    return tikz("\n".join(out), height=2 * rowh)


def p7():
    """One board only: the task has no solution."""
    out = [buckets(6, 6, (0, 0), w=16, h=22, empty=True)]
    return tikz("\n".join(out), height=30)


def p8():
    starts = [(0, 1), (0, 2), (0, 3), (1, 1), (2, 2), (3, 3)]
    out = []
    colx = [4, TEXTW / 2 + 4]
    for i, p in enumerate(starts):
        c = i // 3
        r = i % 3
        y = 70 - r * 33
        x = colx[c]
        out.append(buckets(x, y, p))
        lx = x + width(2, SW) + 8
        out.append(f"\\node[choice,anchor=west] at ({f(lx)},{f(y + SH - 3)}) {{shortest}};")
        out.append(f"\\node[choice,anchor=west] at ({f(lx)},{f(y + 3)}) {{longest}};")
        out.append(answer_box(lx + 30, y + SH - 3, w=14, h=9))
        out.append(answer_box(lx + 30, y + 3, w=14, h=9))
    return tikz("\n".join(out), height=92)


def three_starts_with_box(starts, height=44):
    out = []
    col = TEXTW / 3
    for i, p in enumerate(starts):
        cx = i * col + col / 2
        y = height - SH - 1
        out.append(buckets(cx - width(3, SW) / 2, y, p))
        out.append(answer_box(cx, y - 15, w=16, h=10))
    return tikz("\n".join(out), height=height)


def p9():
    # most counters on the board at once: 2, 4, 6
    return three_starts_with_box([(0, 0, 1), (0, 0, 2), (0, 0, 3)])


def p10():
    # one winning move each: (2,0,0) no refill; (2,0,0) refill bucket 1;
    # (0,2,0) refill bucket 2; (2,2,0) refill both
    starts = [(2, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
    out = []
    rh = 38.0
    aw, ah = 18.0, 25.0
    _, iw = start_to_answer(0, 0, starts[0], aw=aw, ah=ah)
    x = (TEXTW - iw) / 2
    for r, p in enumerate(starts):
        body, _ = start_to_answer(x, 3 * rh + 5 - r * rh, p, aw=aw, ah=ah)
        out.append(body)
    return tikz("\n".join(out), height=3 * rh + 5 + ah + 1)


def p11():
    # longest games: 6, 7, 12
    return three_starts_with_box([(0, 1, 1), (1, 1, 1), (0, 0, 3)])


def p12():
    # (2,2,2): every game ends; lengths 6 to 14, at most 8 counters on the board
    out = [buckets(6, 4, (2, 2, 2))]
    return tikz("\n".join(out), height=26)


# ---------------------------------------------------------------- text
RULES = (
    "Two players take turns. On your turn, take one counter out of a bucket "
    "and put it in Removed. If you took it from bucket 2, you may also put "
    "one counter from Supply into bucket 1. If you took it from bucket 3, you "
    "may also put one counter from Supply into bucket 1, into bucket 2, or "
    "into both. Whoever takes the last counter wins. Start each game with "
    "Removed empty."
)

PROBLEMS = {
    1: "Cover buckets 2 and 3. Put counters in bucket 1 like each picture and "
       "play. Circle who wins.",
    2: "Uncover bucket 2. Play from each start, taking turns going first. "
       "Circle who can always win.",
    3: "You go first from each start. Find a first move that lets you always "
       "win, and draw the buckets after it.",
    4: "Play against the adult from each start, taking turns going first. "
       "Circle who can always win, and show the adult how.",
    5: "Your partner goes first from this start. Draw the buckets after each "
       "move your partner can make. Next to each, draw the buckets after a "
       "move that lets you always win.",
    6: "Find every way to put 4 counters into buckets 1 and 2 so that the "
       "player who goes second can always win. A bucket can be empty. Then do "
       "the same with 6 counters.",
    7: "If you can, put 5 counters into buckets 1 and 2 so that the player who "
       "goes second can always win. If you can't, explain why.",
    8: "Work together. From each start, make the game as short as you can and "
       "then as long as you can. Write how many counters end up in Removed.",
    9: "Uncover bucket 3. Work together to make the buckets hold as many "
       "counters as you can. Write the most they hold.",
    10: "You go first from each start. Find a first move that lets you always "
        "win, and draw the buckets after it.",
    11: "Work together to make the game from each start last as long as you "
        "can. Write how many counters end up in Removed.",
    12: "Could a game from this start go on forever? Explain.",
}

PICTURES = {1: p1, 2: p2, 3: p3, 4: p4, 5: p5, 6: p6, 7: p7, 8: p8,
            9: p9, 10: p10, 11: p11, 12: p12}

# extra blank space (mm) after a problem's picture, for drawings/explanations
AFTER = {}

PAGES = [[1], [2, 3], [4, 5], [6, 7], [8, 9], [10], [11, 12]]

PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage[letterpaper,left=16.5mm,right=16.5mm,top=20mm,bottom=20mm,
  headheight=15pt,headsep=7mm,footskip=11mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[default]{sourcesanspro}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\fancyhead[L]{Week 81 / Buckets of Fish / K\textendash 1}
\fancyfoot[L]{\small Bellingham Math Circle / Week 81 / W81-K-v1}
\fancyfoot[R]{\small \thepage}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\linespread{1.12}
\frenchspacing
\raggedright
\tikzset{
  bucket/.style={line width=0.7pt, rounded corners=1.6mm},
  store/.style={line width=0.7pt},
  ans/.style={line width=0.6pt},
  num/.style={font=\small\bfseries},
  tiny/.style={font=\scriptsize},
  choice/.style={font=\normalsize},
  orword/.style={font=\normalsize},
  rowlab/.style={font=\normalsize},
  move/.style={-{Stealth[length=2.6mm]}, line width=0.9pt},
  stage/.style={-{Stealth[length=3mm]}, line width=1.2pt},
  flow/.style={-{Stealth[length=2.2mm]}, line width=0.7pt},
  tree/.style={line width=0.9pt},
  treearrow/.style={-{Stealth[length=2.4mm]}, line width=0.9pt},
}
\newcommand{\problem}[2]{\par\noindent\textbf{Problem #1:} #2\par}
\begin{document}
"""


def main():
    parts = [PREAMBLE]
    for pi, page in enumerate(PAGES):
        if pi:
            parts.append("\\newpage\n")
        if pi == 0:
            parts.append(RULES + "\\par\\vspace{4mm}\n")
            parts.append("\\noindent " + rule_panels() + "\\par\\vspace{7mm}\n")
            parts.append("\\noindent " + rule_tree() + "\\par\\vspace{9mm}\n")
        for j, n in enumerate(page):
            if j:
                parts.append("\\vspace{10mm}\n")
            parts.append(f"\\problem{{{n}}}{{{PROBLEMS[n]}}}\\vspace{{5mm}}\n")
            parts.append("\\noindent " + PICTURES[n]() + "\\par\n")
            if n in AFTER:
                parts.append(f"\\vspace{{{AFTER[n]}mm}}\n")
    parts.append("\\end{document}\n")
    (HERE / "k-1.tex").write_text("".join(parts))


if __name__ == "__main__":
    main()
