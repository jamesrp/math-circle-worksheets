"""Build the three Week 5 packets (TeX + PDF) and check every printed puzzle.

Run:  python3 build.py
"""
import os
import subprocess
from collections import Counter
from itertools import combinations, permutations

import draw as D
from towers import lr, solutions, clues_of, show, view, all_with_clues

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)          # .../final

INCH = 2.54                          # printed grids for building: 1-inch squares

# ---------------------------------------------------------------- puzzles
# Clue keys: ('T',c) above column c, ('B',c) below column c,
# ('L',r) left of row r, ('R',r) right of row r; rows from the top,
# columns from the left.

def C(top=None, bottom=None, left=None, right=None):
    d = {}
    for side, vals in (('T', top), ('B', bottom), ('L', left), ('R', right)):
        if vals:
            for i, v in enumerate(vals):
                if v:
                    d[(side, i)] = v
    return d

# Grades 2-3, Problem 3 (three unique puzzles and one with no city)
P23 = [
    C(top=[0, 1, 3], left=[2, 0, 0], right=[0, 2, 1]),
    C(left=[2, 1, 0], right=[0, 0, 2]),
    C(top=[2, 2, 2]),                       # no city fits
    C(right=[0, 0, 2], bottom=[0, 2, 0]),
]
P23_EXPECT = [1, 1, 0, 1]
# Grades 2-3, Problem 4 (several cities)
P23_MANY = C(top=[1, 0, 0], left=[0, 0, 2])

# Grades 4-5, Problem 3: the ladder, easy to hard
E1 = C(top=[4, 0, 1, 3], left=[3, 2, 2, 1], right=[0, 0, 1, 3], bottom=[0, 2, 2, 2])
E2 = C(top=[2, 0, 0, 0], left=[3, 1, 0, 0], right=[2, 3, 0, 1], bottom=[3, 0, 4, 0])
M1 = C(top=[3, 2, 0, 0], left=[2, 0, 0, 0], right=[0, 2, 0, 1], bottom=[0, 3, 0, 0])
M2 = C(top=[0, 0, 4, 0], left=[2, 1, 0, 0], right=[0, 2, 3, 0], bottom=[2, 0, 0, 0])
H1 = C(top=[0, 3, 0, 2], left=[0, 0, 2, 0], bottom=[2, 0, 2, 0])
H2 = C(top=[2, 0, 2, 0], left=[0, 2, 0, 0], right=[0, 0, 0, 2])
LADDER = [E1, E2, M1, M2, H1, H2]
# Grades 4-5, Problem 4 (several cities)
TWO_FOURS = C(top=[4, 0, 0, 0], left=[4, 0, 0, 0])

K_ROWS_P1 = [(1, 3, 2), (3, 2, 1)]
K_EYE_ROW = (1, 3, 2)
K_CARDS3 = [(1, 3), (2, 1), (3, 3), (2, 2), (1, 1), (1, 2)]
K_CARDS4 = [(2, 3), (1, 4), (3, 3), (3, 1), (4, 2), (1, 2)]
U_CARDS4 = [(1, 2), (2, 3), (3, 3), (2, 2), (1, 4), (1, 1), (3, 2), (4, 2)]


def rows_for(n, pair):
    return [p for p in permutations(range(1, n + 1)) if lr(p) == pair]


def unique_puzzles(n, k):
    """Number of k-number clue sets (taken from some city) that fit exactly one city."""
    data = all_with_clues(n)
    keys = sorted(data[0][1].keys())
    count = 0
    for sub in combinations(keys, k):
        groups = Counter(tuple(cl[x] for x in sub) for sq, cl in data)
        count += sum(1 for v in groups.values() if v == 1)
    return count


def check():
    report = []
    # K-1
    shown = set(K_ROWS_P1) | {K_EYE_ROW}
    for row in K_ROWS_P1:
        report.append(f"K P1 row {row}: views {lr(row)}")
    report.append(f"K P1 + eye picture show {len(shown)} of the 6 orders: {sorted(shown)}")
    for pair in K_CARDS3:
        report.append(f"K P3 card {pair}: {rows_for(3, pair)}")
    left1 = [p for p in permutations(range(1, 5)) if lr(p)[0] == 1]
    assert len(left1) == 6 and all(p[0] == 4 for p in left1)
    report.append(f"K P5 left view 1, four towers: {left1}")
    r22 = rows_for(4, (2, 2))
    assert len(r22) == 6
    report.append(f"K P6 (2,2) rows of four: {r22}")
    report.append(f"K P5/P6 cubes for towers 1-4: {sum(range(1, 5))} (a pair has 12)")
    for pair in K_CARDS4:
        report.append(f"K P7 card {pair}: {len(rows_for(4, pair))} rows {rows_for(4, pair)[:3]}")
    # 2-3
    pairs3 = sorted({lr(p) for p in permutations((1, 2, 3))})
    report.append(f"23 P1 pairs that occur: {pairs3}")
    assert all(sum(sum(r) for r in sq) == 18 for sq, cl in all_with_clues(3))
    report.append("23 P2: every 3-by-3 city uses 18 cubes")
    for i, (pz, ex) in enumerate(zip(P23, P23_EXPECT)):
        s = solutions(3, pz)
        assert len(s) == ex, (i, len(s))
        report.append(f"23 P3 puzzle {i+1}: {len(s)} solution(s) {[show(x).replace(chr(10), '/') for x in s]}")
    s = solutions(3, P23_MANY)
    assert len(s) == 3
    report.append(f"23 P4: {len(s)} cities {[show(x).replace(chr(10), '/') for x in s]}")
    adds = []
    for key in [(sd, k) for sd in 'TBLR' for k in range(3)]:
        if key in P23_MANY:
            continue
        for v in (1, 2, 3):
            t = dict(P23_MANY); t[key] = v
            if len(solutions(3, t)) == 1:
                adds.append((key, v))
    assert adds
    report.append(f"23 P4 single added clues that work: {adds}")
    # 2-3 P5: fewest numbers is 2
    for key in [(sd, k) for sd in 'TBLR' for k in range(3)]:
        for v in (1, 2, 3):
            assert len(solutions(3, {key: v})) > 1
    u2 = unique_puzzles(3, 2)
    assert u2 > 0
    report.append(f"23 P5: every one-number puzzle has at least 2 cities; "
                  f"{u2} two-number puzzles have one city, so the fewest is 2")
    tot = sorted({sum(cl.values()) for sq, cl in all_with_clues(3)})
    report.append(f"23 P6 number of cities (turned/flipped count as different): {len(all_with_clues(3))}")
    report.append(f"23 P7 totals: {tot}")
    # 4-5
    for pair in U_CARDS4:
        report.append(f"45 P1 card {pair}: {len(rows_for(4, pair))} rows")
    assert all(sum(sum(r) for r in sq) == 40 for sq, cl in all_with_clues(4))
    report.append("45 P2: every 4-by-4 city uses exactly 40 cubes")
    for name, pz in zip(['E1', 'E2', 'M1', 'M2', 'H1', 'H2'], LADDER):
        s = solutions(4, pz)
        assert len(s) == 1, name
        report.append(f"45 P3 ladder {name} ({len(pz)} clues): {show(s[0]).replace(chr(10), '/')}")
    s = solutions(4, TWO_FOURS)
    assert len(s) == 4
    report.append(f"45 P4 two fours: {[show(x).replace(chr(10), '/') for x in s]}")
    adds = []
    for key in [(sd, k) for sd in 'TBLR' for k in range(4)]:
        if key in TWO_FOURS:
            continue
        for v in (1, 2, 3, 4):
            t = dict(TWO_FOURS); t[key] = v
            if len(solutions(4, t)) == 1:
                adds.append((key, v))
    assert adds
    report.append(f"45 P4 single added clues that work: {adds}")
    assert unique_puzzles(4, 2) == 0 and unique_puzzles(4, 3) > 0
    report.append("45 P5: fewest numbers for one city is 3 (no two-number puzzle has one city)")
    # 4-5 P6: a three-number puzzle with no 4
    keys4 = [(sd, k) for sd in 'TBLR' for k in range(4)]
    ex = None
    for sq, cl in all_with_clues(4):
        for sub in combinations(keys4, 3):
            cs = {k: cl[k] for k in sub}
            if 4 not in cs.values() and len(solutions(4, cs)) == 1:
                ex = cs; break
        if ex: break
    assert ex
    report.append(f"45 P6 example: {ex}")
    c4 = Counter(lr(p) for p in permutations(range(1, 5)))
    report.append(f"45 P7 table: {sorted(c4.items())}")
    c5 = Counter(view(p) for p in permutations(range(1, 6)))
    report.append(f"45 P8 rows of five by left view: {sorted(c5.items())}")
    groups = {}
    for sq, cl in all_with_clues(4):
        groups.setdefault(tuple(sorted(cl.items())), []).append(sq)
    same = [v for v in groups.values() if len(v) > 1]
    report.append(f"45 P9: {len(same)} clue sets shared by 2+ cities, e.g. {[show(x).replace(chr(10), '/') for x in same[0][:2]]}")
    with open(os.path.join(HERE, 'answers-check.txt'), 'w') as f:
        f.write("\n".join(report) + "\n")
    print("\n".join(report))


# ---------------------------------------------------------------- TeX

def preamble(size, level, pid):
    return rf"""\documentclass[{size}]{{extarticle}}
\usepackage[T1]{{fontenc}}
\usepackage[default]{{sourcesanspro}}
\usepackage[letterpaper,top=0.75in,bottom=0.75in,left=0.65in,right=0.65in,
  headheight=18pt,headsep=0.28in,footskip=0.45in]{{geometry}}
\usepackage{{tikz}}
\usepackage{{fancyhdr}}
\usepackage[none]{{hyphenat}}
\usepackage{{ragged2e}}
\definecolor{{cube}}{{RGB}}{{176,204,236}}
\definecolor{{folder}}{{RGB}}{{240,218,166}}
\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[L]{{Week 5 / Tower cities / {level}}}
\fancyfoot[L]{{Bellingham Math Circle / Week 5 / {pid}}}
\fancyfoot[R]{{\thepage}}
\renewcommand{{\headrulewidth}}{{0.4pt}}
\renewcommand{{\footrulewidth}}{{0pt}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0pt}}
\raggedbottom
\RaggedRight
\newcommand{{\prob}}[1]{{\textbf{{Problem #1:}}\ }}
\begin{{document}}
"""


def pic(body, center=True):
    s = "\\begin{tikzpicture}\n" + body + "\\end{tikzpicture}"
    if center:
        return "\\begin{center}\n" + s + "\n\\end{center}\n"
    return s


def place(items, cols, dx, dy):
    """items: list of tikz bodies; arranged in rows of `cols`, top to bottom."""
    s = ""
    for i, body in enumerate(items):
        r, c = divmod(i, cols)
        s += f"\\begin{{scope}}[shift={{({c*dx:.3f},{-r*dy:.3f})}}]\n{body}\\end{{scope}}\n"
    return s


def block(text, figure="", after=""):
    """One problem (or the first part of one) kept on one page."""
    return ("\\begin{minipage}{\\linewidth}\\RaggedRight\n" + text + "\n" + figure + after
            + "\\end{minipage}\n\\par\\vspace{0.75cm}\n")


def gap(cm):
    return f"\\vspace*{{{cm}cm}}\n"


def inch_grids(n, count, dy=None):
    """`count` empty n-by-n grids with 1-inch squares and clue boxes, one above the
    other and staggered left and right, so that the boxes under one grid do not
    sit beside the boxes over the next."""
    g = D.city(n, INCH, boxes=True)
    dy = dy if dy is not None else n * INCH + 2.6
    dx = 8.3 if n == 3 else 0
    s = ""
    for i in range(count):
        s += f"\\begin{{scope}}[shift={{({(i % 2) * dx:.3f},{-i * dy:.3f})}}]\n{g}\\end{{scope}}\n"
    return pic(s)


# ---------------------------------------------------------------- K-1

def k1():
    t = preamble("14pt", "K--1", "F05-K-v4")
    # packet rule with a picture; the eye sits several cube-widths from the row
    body, (a, b, w) = D.side_row(K_EYE_ROW, cube=0.8, gap=0.4, circles=False,
                                 base_extra=5.6, base_extra_right=1.0)
    body += D.eye(a + 0.75, 0.32, scale=0.85)
    t += ("Put your eye down at the table about a foot from one end of a row of towers "
          "and look along the row. You see a tower when it is taller than every tower in front of it.\n")
    t += pic(body)
    t += "\\vspace{0.2cm}\n"
    # Problem 1
    rows = [D.side_row(r, cube=1.2, gap=0.6)[0] for r in K_ROWS_P1]
    t += block(r"\prob{1}Make towers of 1, 2, and 3 cubes. Build each row in the picture, "
               r"and write in each circle how many towers you see from that end.",
               pic(place(rows, 2, 9.4, 5.4)))
    t += "\\newpage\n"
    # Problem 2
    charts = [D.chart(3, box=1.0, pitch=1.25)[0] for _ in range(8)]
    t += block(r"\prob{2}Find every different way to stand your three towers in a row. "
               r"Draw each way, and write how many towers you see from each end.",
               gap(0.3) + pic(place(charts, 2, 9.0, 4.5)))
    t += "\\newpage\n"
    # Problem 3
    cards = [D.card(3, a_, b_, box=1.0, pitch=1.25) for a_, b_ in K_CARDS3]
    t += block(r"\prob{3}Build a row of your three towers that shows the two numbers on each card, "
               r"and draw it. If no row can, put an X on the card and tell why.",
               gap(0.3) + pic(place(cards, 2, 9.0, 4.9)))
    t += "\\newpage\n"
    # Problem 4
    scene = D.folder_scene((2, 3, 1), cube=0.9, gap=0.45)
    rec = [D.chart(3, box=0.85, pitch=1.05)[0] for _ in range(6)]
    t += block(r"\prob{4}One partner hides a row of three towers behind a folder and says how many "
               r"towers you can see from each end. The other builds a row that shows those numbers and draws it, "
               r"and then you swap.",
               pic(scene) + gap(0.3) + pic(place(rec, 3, 6.15, 4.3)))
    t += "\\newpage\n"
    # Problem 5
    ch = [D.chart(4, box=0.85, pitch=1.05, left=1, show_right=False)[0] for _ in range(8)]
    t += block(r"\prob{5}Put your cubes together with your partner's and make towers of 1, 2, 3, and 4 cubes. "
               r"Find and draw every row of these four towers where you see just 1 tower "
               r"from the left end. How do you know you have them all?",
               gap(0.3) + pic(place(ch, 2, 9.0, 4.6)))
    t += "\\newpage\n"
    # Problem 6
    ch = [D.chart(4, box=0.85, pitch=1.05, left=2, right=2)[0] for _ in range(8)]
    t += block(r"\prob{6}Find and draw every row of your four towers where you see 2 towers from each end.",
               gap(0.3) + pic(place(ch, 2, 9.0, 4.6)))
    t += "\\newpage\n"
    # Problem 7
    cards = [D.card(4, a_, b_, box=0.85, pitch=1.05) for a_, b_ in K_CARDS4]
    t += block(r"\prob{7}Build a row of your four towers that shows the two numbers on each card, "
               r"and draw it. If no row can, put an X on the card and tell why.",
               gap(0.3) + pic(place(cards, 2, 9.0, 5.2)))
    t += "\\end{document}\n"
    return t


# ---------------------------------------------------------------- 2-3

def g23():
    t = preamble("14pt", "Grades 2--3", "F05-M-v4")
    t += ("Look along a row of towers from one end, with your eye down at the table about a foot away. "
          "You see a tower when it is taller than every tower in front of it.\n\\par\\vspace{0.6cm}\n")
    # Problem 1
    recs = [D.row_record(3, sq=1.2) for _ in range(8)]
    t += block(r"\prob{1}Stand towers of 1, 2, and 3 cubes in a row. Find every order of the three towers, "
               r"and write each one with the number of towers seen from each end. "
               r"Which pairs of numbers can a row of three towers never show? Explain why.",
               gap(0.2) + pic(place(recs, 2, 8.8, 1.95)), gap(3.2))
    t += "\\newpage\n"
    # Problem 2: build on 1-inch grids
    t += block(r"\prob{2}Build nine towers on the first grid with your 18 cubes, one tower on each square, "
               r"so that every row and every column has one tower of each height 1, 2, and 3. "
               r"Towers placed like this make a city. In the boxes around the grid, write how many towers "
               r"you see from each end of every row and every column, and write the heights in the grid. "
               r"Then build a different city on the second grid and do the same.",
               gap(0.1) + inch_grids(3, 2))
    t += "\\newpage\n"
    # Problem 3: four puzzles on 1-inch grids, two per page
    pz = [D.city(3, INCH, clues=c) for c in P23]
    t += block(r"\prob{3}Find the city that fits the numbers around each grid, and write its heights in the grid. "
               r"If no city fits, explain why.",
               gap(0.3) + pic(place(pz[:2], 1, 0, 10.4)))
    t += "\\newpage\n"
    t += gap(0.3) + pic(place(pz[2:], 1, 0, 10.4))
    t += "\\newpage\n"
    # Problem 4
    small = [D.city(3, 1.4) for _ in range(6)]
    t += block(r"\prob{4}More than one city fits the numbers around this grid. Find every city that fits. "
               r"Then write one more number around the grid so that only one of your cities fits.",
               gap(0.2) + pic(D.city(3, INCH, clues=P23_MANY)) + gap(0.4) + pic(place(small, 3, 5.8, 5.4)))
    t += "\\newpage\n"
    # Problem 5: puzzles for a partner, on 1-inch grids, two per page
    t += block(r"\prob{5}Build a city behind a folder, out of your partner's sight. "
               r"Write some of its numbers around an empty grid so that your city is the only one that fits. "
               r"Your partner solves the puzzle and tries to find a second city that fits the same numbers. "
               r"How few numbers can a puzzle have and still fit only one city? Explain why fewer cannot work.",
               gap(0.1) + inch_grids(3, 2))
    t += "\\newpage\n"
    t += gap(0.6) + inch_grids(3, 2, dy=11.0)
    t += "\\newpage\n"
    # Problem 6
    many = [D.city(3, 1.0) for _ in range(15)]
    t += block(r"\prob{6}How many different 3-by-3 cities are there? Cities that are turned or flipped "
               r"count as different. Write each city you find in a grid. "
               r"Explain how you know you have found them all.",
               gap(0.3) + pic(place(many, 5, 3.65, 3.75)))
    t += "\\newpage\n"
    # Problem 7
    g = [D.city(3, 1.5, boxes=True) for _ in range(2)]
    t += block(r"\prob{7}Add up the twelve numbers around a 3-by-3 city. Which totals can a city have? "
               r"Explain why.",
               gap(0.3) + pic(place(g, 2, 9.0, 0)))
    t += "\\end{document}\n"
    return t


# ---------------------------------------------------------------- 4-5

def g45():
    t = preamble("14pt", "Grades 4--5", "F05-U-v4")
    t += ("Look along a row of towers from one end, with your eye down at the table about a foot away. "
          "You see a tower when it is taller than every tower in front of it.\n\\par\\vspace{0.6cm}\n")
    # Problem 1
    cards = [D.row_record(4, sq=1.1, left=a, right=b, frame=True) for a, b in U_CARDS4]
    t += block(r"\prob{1}Use towers of 1, 2, 3, and 4 cubes. For each card, find a row that shows the left number "
               r"from the left end and the right number from the right end, and write the heights of the row on the card. "
               r"If no row can, explain why.",
               gap(0.2) + pic(place(cards, 2, 9.0, 2.05)), gap(3.0))
    t += "\\newpage\n"
    # Problem 2: build one city on a 1-inch grid
    t += block(r"\prob{2}Build sixteen towers on this grid with your 40 cubes, one tower on each square, "
               r"so that every row and every column has one tower of each height 1, 2, 3, and 4. "
               r"Towers placed like this make a city. In the boxes around the grid, write how many towers "
               r"you see from each end of every row and every column, and write the heights in the grid.",
               gap(0.3) + inch_grids(4, 1))
    t += "\\newpage\n"
    # Problem 3: the ladder, four puzzles then two
    pz = [D.city(4, 1.7, clues=c) for c in LADDER]
    t += block(r"\prob{3}Find the city that fits the numbers around each grid, and write its heights in the grid.",
               gap(0.3) + pic(place(pz[:4], 2, 9.4, 9.6)))
    t += "\\newpage\n"
    t += gap(0.3) + pic(place(pz[4:], 2, 9.4, 0))
    t += "\\newpage\n"
    # Problem 4
    small = [D.city(4, 1.0) for _ in range(6)]
    t += block(r"\prob{4}More than one city fits the numbers around this grid. Find every city that fits. "
               r"Then write one more number around the grid so that only one of your cities fits.",
               gap(0.2) + pic(D.city(4, 1.7, clues=TWO_FOURS)) + gap(0.3) + pic(place(small, 3, 5.8, 5.0)))
    t += "\\newpage\n"
    # Problem 5
    empt = [D.city(4, 1.2, boxes=True) for _ in range(4)]
    t += block(r"\prob{5}Build a city behind a folder, out of your partner's sight. "
               r"Write some of its numbers around an empty grid so that your city is the only one that fits, "
               r"using as few numbers as you can. Your partner solves the puzzle and then tries to find a second city "
               r"that fits the same numbers.",
               gap(0.2) + pic(place(empt, 2, 9.0, 8.4)))
    t += "\\newpage\n"
    # Problems 6 and 7
    empt = [D.city(4, 1.2, boxes=True) for _ in range(2)]
    t += block(r"\prob{6}Make a puzzle with only three numbers around the grid, none of them a 4, "
               r"that has exactly one city.",
               gap(0.2) + pic(place(empt, 2, 9.0, 0)))
    t += block(r"\prob{7}There are 24 different rows of four towers 1, 2, 3, and 4 cubes tall. "
               r"Sort them by the two numbers seen from the ends, and write in the table how many rows show each pair.",
               gap(0.2) + pic(D.table(4, 1.3)))
    t += "\\newpage\n"
    # Problems 8 and 9
    t += block(r"\prob{8}There are 120 different rows of five towers 1, 2, 3, 4, and 5 cubes tall. "
               r"How many of them show exactly 1 tower from the left end? How many show exactly 2? "
               r"Explain how you counted.", gap(6.0))
    g = [D.city(4, 1.2, boxes=True) for _ in range(2)]
    t += block(r"\prob{9}Can two different 4-by-4 cities have exactly the same sixteen numbers around them? "
               r"If they can, find two. If not, explain why.",
               gap(0.2) + pic(place(g, 2, 9.0, 0)), gap(3.0))
    t += "\\end{document}\n"
    return t


def compile_tex(name, tex):
    path = os.path.join(HERE, name + ".tex")
    with open(path, "w") as f:
        f.write(tex)
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                           cwd=HERE, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            raise SystemExit(f"pdflatex failed for {name}")
    os.replace(os.path.join(HERE, name + ".pdf"), os.path.join(OUT, name + ".pdf"))
    log = open(os.path.join(HERE, name + ".log")).read()
    over = [l for l in log.splitlines() if "Overfull" in l]
    print(name, "overfull boxes:", len(over))
    for l in over:
        print("  ", l)
    for ext in (".aux", ".log"):
        p = os.path.join(HERE, name + ext)
        if os.path.exists(p):
            os.remove(p)


if __name__ == "__main__":
    check()
    compile_tex("k-1", k1())
    compile_tex("grades-2-3", g23())
    compile_tex("grades-4-5", g45())
