#!/usr/bin/env python3
"""Build the Week 63 return-visit student packets (K-1, 2-3, 4-5).

Run: python3 build.py   (writes .tex here and PDFs one level up)
Check the mathematics with: python3 verify.py
"""
import os
import subprocess
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tikzlib import (row, board, pentagon, grid, swapline, box, tikz, label_pair,
                     font, f)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)


def preamble(level, pid, base_pt=11):
    return rf"""\documentclass[{base_pt}pt]{{article}}
\usepackage[letterpaper, top=0.7in, bottom=0.75in, left=0.7in, right=0.7in,
  headheight=15pt, headsep=12pt, footskip=26pt]{{geometry}}
\usepackage[T1]{{fontenc}}
\usepackage{{helvet}}
\renewcommand{{\familydefault}}{{\sfdefault}}
\usepackage{{tikz}}
\usetikzlibrary{{arrows.meta}}
\usepackage{{fancyhdr}}
\pagestyle{{fancy}}
\fancyhf{{}}
\lhead{{Week 63 / Cards away from home / {level}}}
\lfoot{{Bellingham Math Circle / Week 63 / {pid}}}
\rfoot{{\thepage}}
\renewcommand{{\headrulewidth}}{{0.4pt}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0pt}}
\newcommand{{\prob}}[1]{{\textbf{{Problem #1:}}}}
\begin{{document}}
"""


END = "\n\\end{document}\n"


def fig(body, indent=0):
    return f"\n\\par\\vspace{{3mm}}\\noindent\\hspace*{{{indent}mm}}" + tikz(body) + "\\par\n"


def demo(w=10, h=10, card_pt=11, lab_pt=7, arrow_pt=10):
    """Shared-rule example: one swap of two non-neighbouring cards (U-X)."""
    b = row(0, 0, "VUWX", homes="UVWX", w=w, h=h, card_pt=card_pt, lab_pt=lab_pt,
            bold=(0, 3))
    x1 = 4 * w + 6
    b += (f"\\draw[-{{Stealth[length=2.4mm]}}, line width=0.9pt] ({f(x1)},{f(h/2)}) -- "
          f"({f(x1+22)},{f(h/2)});\n")
    b += f"\\node[font={font(arrow_pt)}] at ({f(x1+11)},{f(h/2+4)}) {{VX}};\n"
    b += row(x1 + 28, 0, "XUWV", homes="UVWX", w=w, h=h, card_pt=card_pt,
             lab_pt=lab_pt, bold=(0, 3))
    return b


# ---------------------------------------------------------------- K-1
def build_k():
    s = preamble("K--1", "W63-RV-K-v1", 12)
    W, H = 14, 14
    big = dict(w=W, h=H, card_pt=17, card_s=6.2, lab_pt=9, lab_s=3.4, lab_gap=4)
    rec = dict(w=10, h=10, lab_pt=7, lab_s=2.6, blank=True)

    # page 1
    s += ("The homes stay in place. A card is at home when it sits under its own letter "
          "and picture. A swap trades the places of any two cards, near or far. "
          "Write each swap as the letters of the two cards it trades.\n")
    s += "\n\\vspace{2mm}\n"
    s += fig(demo(w=13, h=13, card_pt=15, lab_pt=9, arrow_pt=12), 20)
    s += "\n\\vspace{9mm}\n"
    s += ("\\prob{1} Start with A, B and C at home. Swap cards until no card is at home, "
          "using as few swaps as you can.\n")
    b = row(0, 0, "ABC", **big)
    for k in range(4):
        y = 6 - k * 17
        b += swapline(58, y + 2, 62, pt=10)
        b += row(140, y - 2, "ABC", **rec)
    b += box(150, -66, "fewest swaps", w=14, h=10, pt=10)
    s += fig(b, 2)
    s += "\n\\newpage\n"

    # page 2
    s += ("\\prob{2} Do Problem 1 again with A, B, C and D. "
          "Which rows can you end with in the fewest swaps?\n")
    b = row(0, 0, "ABCD", **big)
    for k in range(5):
        y = 6 - k * 16
        b += swapline(66, y + 2, 52, pt=10)
        b += row(136, y - 2, "ABCD", **rec)
    b += box(150, -76, "fewest swaps", w=14, h=10, pt=10)
    s += fig(b, 2)
    s += "\n\\vfill\n"
    s += ("\\prob{3} Start with all five cards at home. "
          "Can two swaps leave no card at home? Can three?\n")
    b = row(0, 0, "ABCDE", w=13, h=13, card_pt=16, card_s=5.8, lab_pt=9, lab_s=3.4,
            lab_gap=4)
    rec5 = dict(rec, w=8.5, h=9)
    for k in range(4):
        y = 6 - k * 16
        b += swapline(72, y + 2, 50, pt=10)
        b += row(135, y - 2, "ABCDE", **rec5)
    s += fig(b, 2)
    s += "\n\\vfill\n\\newpage\n"

    # page 3
    s += ("\\prob{4} Set out each row. Bring every card home "
          "using as few swaps as you can.\n")
    b = ""
    for k, r in enumerate(["CBA", "BCA", "BADC", "BCDA"]):
        y = -k * 46
        b += row(0, y, r, **big)
        b += swapline(66, y + 6, 58, pt=10)
        b += box(158, y + 1, "fewest swaps", w=14, h=10, pt=10)
    s += fig(b, 2)
    s += "\n\\vfill\n\\newpage\n"

    # page 4
    s += ("\\prob{5} Put a counter on every letter at home on the six A--C outcome cards. "
          "Are there more counters, more outcome cards, or the same number, "
          "and how many counters does each letter get?\n")
    b = box(22, 0, "counters", w=16, h=11, pt=11)
    b += box(84, 0, "outcome cards", w=16, h=11, pt=11)
    for k, L in enumerate("ABC"):
        x = 10 + k * 44
        b += label_pair(L, x, -16.5, 13, 4.4)
        b += f"\\draw[line width=0.6pt] ({f(x+8)},{f(-22)}) rectangle ({f(x+24)},{f(-11)});\n"
    s += fig(b, 6)
    s += "\n\\vspace{26mm}\n"
    s += ("\\prob{6} A card may not go in a home that shows its picture crossed out. "
          "Find every way to put A, B and C in these homes.\n")
    b = board(0, 0, "ABC", {"A": "A", "B": "AB", "C": "BC"})
    for k in range(3):
        b += row(130, 40 - k * 19, "ABC", **rec)
    s += fig(b, 2)
    s += "\n\\vfill\n\\newpage\n"

    # page 5
    s += "\\prob{7} Find every way to put A, B, C and D in these homes.\n"
    b = board(0, 0, "ABCD", {"A": "A", "B": "AB", "C": "BC", "D": "CD"})
    for k in range(5):
        b += row((k % 3) * 56, -22 - (k // 3) * 20, "ABCD", **rec)
    s += fig(b, 2)
    s += "\n\\vfill\n"
    s += "\\prob{8} Find every way to put A, B, C and D in these homes.\n"
    b = board(0, 0, "ABCD", {"A": "AB", "B": "ABC", "C": "BCD", "D": "CD"},
              mc_w=8, mc_h=11, mc_pt=9, gap=1.0)
    for k in range(3):
        b += row(k * 56, -22, "ABCD", **rec)
    s += fig(b, 2)
    s += "\n\\vfill\n"
    s += END
    return s


# ---------------------------------------------------------------- shared 2-5
RULES_UPPER = ("The homes stay in place. A card is at home when it sits in the home "
               "with its own letter. A swap trades the places of any two cards, near or far. "
               "Write each swap as the letters of the two cards it trades.\n")

REC = dict(w=8, h=8, lab_pt=6, lab_s=2.2, lab_gap=2.8, blank=True)
SMALL = dict(w=10, h=10, card_pt=11, card_s=4.2, lab_pt=7, lab_s=2.6)


def rows_to_bring_home(rows_, pitch=50):
    b = ""
    for k, r in enumerate(rows_):
        col = k % 2
        line = k // 2
        x = col * 92
        y = -line * pitch
        b += row(x, y, r, **SMALL)
        b += swapline(x, y - 10, 52, pt=9)
        b += box(x + 72, y - 14, "fewest", w=11, h=8, pt=9)
    return b


def piles_table(x, y, n, label, cell=12, pt=9):
    b = f"\\node[anchor=east, font={font(pt, False)}] at ({f(x)},{f(y+cell/2+8)}) {{at home}};\n"
    b += f"\\node[anchor=east, font={font(pt, False)}] at ({f(x)},{f(y+cell*0.4)}) {{{label}}};\n"
    for k in range(n + 1):
        xx = x + 2 + k * (cell + 3)
        b += f"\\node[font={font(pt)}] at ({f(xx+cell/2)},{f(y+cell/2+8)}) {{{k}}};\n"
        b += f"\\draw[line width=0.6pt] ({f(xx)},{f(y)}) rectangle ({f(xx+cell)},{f(y+cell*0.8)});\n"
    return b


# ---------------------------------------------------------------- 2-3
def build_m():
    s = preamble("Grades 2--3", "W63-RV-M-v1", 11)
    s += RULES_UPPER
    s += fig(demo(), 30)
    s += "\n\\vspace{8mm}\n"
    s += ("\\prob{1} Start with A, B, C and D at home. Swap cards until no card is at home, "
          "using as few swaps as you can. Which rows can you end with in that many swaps? "
          "Then find the fewest swaps for all five cards.\n")
    b = ""
    for k in range(5):
        y = -k * 15
        b += swapline(0, y + 2, 70, pt=9)
        b += row(90, y - 2, "ABCD", **REC)
    for k in range(2):
        y = -(5 + k) * 15 - 4
        b += swapline(0, y + 2, 70, pt=9)
        b += row(90, y - 2, "ABCDE", **REC)
    b += box(160, -30, "four cards", w=12, h=9, pt=9)
    b += box(160, -92, "five cards", w=12, h=9, pt=9)
    b += f"\\node[font={font(9, False)}] at (166,-14) {{fewest swaps}};\n"
    s += fig(b, 2)
    s += "\n\\newpage\n"

    s += ("\\prob{2} Set out each row below. Bring every card home "
          "using as few swaps as you can.\n")
    s += fig(rows_to_bring_home(["CBAD", "BCAD", "DCBA", "ACDB", "BCDA", "CDBA"],
                                pitch=42), 2)
    s += "\n\\vspace{10mm}\n"
    s += ("\\prob{3} Find every row of A, B, C and D that needs the most swaps to come "
          "home. Could any row need 4 swaps? Explain.\n")
    b = ""
    for k in range(8):
        b += row((k % 4) * 46, -(k // 4) * 19, "ABCD",
                 **dict(REC, w=10, h=10, lab_pt=7, lab_s=2.6, lab_gap=3.2))
    s += fig(b, 2)
    s += "\n\\vfill\n\\newpage\n"

    s += ("\\prob{4} In which of these rows can one swap bring two cards home at once? "
          "Explain how you can tell for any row.\n")
    b = ""
    for k, r in enumerate(["BCDA", "CDAB", "BCAD", "DBCA", "DACB"]):
        b += row((k % 3) * 62, -(k // 3) * 20, r, **SMALL)
    s += fig(b, 2)
    s += "\n\\vspace{56mm}\n"
    s += ("\\prob{5} On the uncut sheet of 24 A--D outcome cards, circle every letter that "
          "sits in its own home. How many circles are there in all? "
          "How many does each letter get?\n")
    b = box(26, 0, "circles in all", w=14, h=9, pt=9)
    for k, L in enumerate("ABCD"):
        x = 62 + k * 30
        b += label_pair(L, x, 4.5, 10, 3.4)
        b += f"\\draw[line width=0.6pt] ({f(x+6)},0) rectangle ({f(x+20)},9);\n"
    s += fig(b, 2)
    s += "\n\\vfill\n\\newpage\n"

    s += ("\\prob{6} How many circles would the six A--C outcome cards get? "
          "There are 120 rows of the five cards A, B, C, D and E. How many circles would "
          "all 120 rows get? Explain without listing the rows.\n")
    b = box(40, 0, "A--C circles", w=14, h=9, pt=9)
    b += box(120, 0, "A--E circles", w=14, h=9, pt=9)
    s += fig(b, 0)
    s += "\n\\vspace{68mm}\n"
    s += ("\\prob{7} Sort the 24 cut A--D outcome cards into piles by how many letters are "
          "at home. Explain why the pile with exactly one letter at home and the pile with "
          "exactly two have the sizes they do.\n")
    s += fig(piles_table(30, 0, 4, "how many"), 4)
    s += "\n\\vfill\n\\newpage\n"

    s += ("\\prob{8} A crossed-out card above a home may not sit in that home. "
          "How many of the 24 A--D outcome cards obey each board?\n")
    boards = [
        {"A": "A", "B": "B", "C": "C", "D": "D"},
        {"A": "A", "B": "AB", "C": "C"},
        {"A": "AB", "B": "AB"},
        {"A": "A", "B": "A", "C": "A", "D": "A"},
    ]
    b = ""
    for k, rf in enumerate(boards):
        y = -k * 40
        b += board(0, y, "ABCD", rf, W=32, H=13, actual=False, mc_w=9, mc_h=11,
                   lab_pt=10, lab_s=3.4, mc_pt=9, gap=2.4)
        b += box(158, y + 1.5, "obey", w=13, h=9, pt=9)
    s += fig(b, 2)
    s += "\n\\vfill\n\\newpage\n"

    s += ("\\prob{9} Cross out four cards on the first board so that as many of the 24 "
          "outcome cards as possible obey it. On the other boards, cross out four cards so "
          "that exactly 8 obey, and then four so that exactly 6 obey. Can four crossed-out "
          "cards make exactly 5 obey?\n")
    b = ""
    for k in range(4):
        y = -k * 42
        b += board(0, y, "ABCD", {}, W=36, H=13, actual=False, mc_w=6.4, mc_h=8.4,
                   lab_pt=10, lab_s=3.4, menu=True, mc_pt=7, gap=1.0)
        b += box(158, y + 1.5, "obey", w=13, h=9, pt=9)
    s += fig(b, 2)
    s += "\n\\vfill\n"
    s += END
    return s


# ---------------------------------------------------------------- 4-5
def build_u():
    s = preamble("Grades 4--5", "W63-RV-U-v1", 11)
    s += RULES_UPPER
    s += fig(demo(), 30)
    s += "\n\\vspace{8mm}\n"
    s += ("\\prob{1} Start with every card at home. Reach a row with no card at home in as "
          "few swaps as you can, with three cards, with four and with all five. "
          "For five cards, explain why no fewer swaps will do.\n")
    b = f"\\node[font={font(9, False)}] at (166,9) {{fewest swaps}};\n"
    y = 0
    for g, (homes, n_lines, lab) in enumerate([("ABC", 2, "three"), ("ABCD", 2, "four"),
                                               ("ABCDE", 3, "five")]):
        y0 = y
        for k in range(n_lines):
            b += swapline(0, y + 2, 70, pt=9)
            b += row(90, y - 2, homes, **REC)
            y -= 15
        b += box(160, y0 - 3, lab, w=12, h=9, pt=9)
        y -= 6
    s += fig(b, 2)
    s += "\n\\newpage\n"

    s += ("\\prob{2} Set out each row below. Bring every card home "
          "using as few swaps as you can.\n")
    s += fig(rows_to_bring_home(["EBCDA", "BCADE", "BADEC", "BCAED", "BCDEA", "DEABC"]), 2)
    s += "\n\\vfill\n\\newpage\n"

    s += ("\\prob{3} An arrow goes from each card's letter to the letter of the home where "
          "the card sits.\n")
    b = row(0, 8, "WUVXY", homes="UVWXY", w=8, h=8, card_pt=10, card_s=3, lab_pt=7,
            lab_s=2.4)
    b += pentagon(76, 12, "UVWXY", r=12, arrows=[("W", "U")], name="e")
    b += f"\\node[font={font(8, False)}] at (76,-6) {{W sits in home U}};\n"
    b += pentagon(138, 12, "UVWXY", r=12, arrows=[("W", "U"), ("U", "V"), ("V", "W")],
                  loops="XY", name="g")
    b += f"\\node[font={font(8, False)}] at (138,-6) {{X and Y are at home}};\n"
    s += fig(b, 4)
    s += ("\n\\vspace{6mm}\nDraw the arrows for each row of Problem 2. How can you tell the "
          "fewest swaps from the arrows? Explain why no row can come home in fewer swaps "
          "than that.\n")
    b = ""
    for k, r in enumerate(["EBCDA", "BCADE", "BADEC", "BCAED", "BCDEA", "DEABC"]):
        cx = 28 + (k % 3) * 62
        cy = -(k // 3) * 52
        b += f"\\node[font={font(9)}] at ({f(cx)},{f(cy+22)}) {{{r}}};\n"
        b += pentagon(cx, cy, "ABCDE", r=15, node_mm=6.5, name=f"t{k}")
    s += fig(b, 0)
    s += "\n\\vfill\n\\newpage\n"

    s += ("\\prob{4} Which rows of A, B, C, D and E need the most swaps to come home? "
          "How many such rows are there? How many of the 44 rows with no card at home "
          "need fewer swaps than that?\n")
    s += "\n\\vspace{80mm}\n"
    s += ("\\prob{5} Can BACDE be brought home in exactly 2 swaps? In exactly 3, 4 or 5? "
          "Try the same numbers with BCADE. Explain which numbers of swaps can bring a "
          "row home.\n")
    b = ""
    for c, r in enumerate(["BACDE", "BCADE"]):
        b += row(c * 92, 0, r, **SMALL)
        for k in range(4):
            b += swapline(c * 92, -10 - k * 12, 70, pt=9)
    s += fig(b, 2)
    s += "\n\\vfill\n\\newpage\n"

    s += ("\\prob{6} On the uncut sheet of 24 A--D outcome cards, circle every letter that "
          "sits in its own home. How many circles are there in all, and how many for each "
          "letter? Without listing, find how many circles the 120 rows of A, B, C, D and E "
          "would get, and explain.\n")
    b = box(24, 0, "A--D circles", w=13, h=9, pt=9)
    for k, L in enumerate("ABCD"):
        x = 52 + k * 25
        b += label_pair(L, x, 4.5, 10, 3.4)
        b += f"\\draw[line width=0.6pt] ({f(x+6)},0) rectangle ({f(x+18)},9);\n"
    b += box(162, 0, "A--E", w=13, h=9, pt=9)
    s += fig(b, 0)
    s += "\n\\vspace{80mm}\n"
    s += ("\\prob{7} Any two circles on the same outcome card make a pair. How many pairs "
          "are on the 24 A--D outcome cards? Without listing, how many pairs would the "
          "120 rows of A--E have?\n")
    b = box(40, 0, "A--D pairs", w=13, h=9, pt=9)
    b += box(110, 0, "A--E pairs", w=13, h=9, pt=9)
    s += fig(b, 0)
    s += "\n\\vfill\n\\newpage\n"

    s += ("\\prob{8} Sort the 24 cut A--D outcome cards into piles by how many letters are "
          "at home. Without listing, predict the piles for the 120 rows of A--E, and "
          "explain.\n")
    b = piles_table(24, 22, 4, "A--D")
    b += piles_table(24, 0, 5, "A--E")
    s += fig(b, 2)
    s += "\n\\vspace{62mm}\n"
    s += ("\\prob{9} For three cards, the pile with no card at home has 2 rows and the pile "
          "with exactly one card at home has 3. Compare those two piles for four cards and "
          "for five cards. What happens, and why?\n")
    s += "\n\\vfill\n\\newpage\n"

    strip5 = {"A": "A", "B": "AB", "C": "BC", "D": "CD", "E": "DE"}
    s += ("\\prob{10} A card may not sit in a home that shows its picture crossed out. "
          "Find every row that obeys this board using homes A to C, using homes A to D, "
          "and using all five homes.\n")
    b = board(0, 0, "ABCDE", strip5)
    rec5 = dict(REC, w=6.4, h=7, lab_pt=5.5, lab_s=2)
    b += f"\\node[anchor=west, font={font(9, False)}] at (0,-9) {{A to C}};\n"
    for k in range(2):
        b += row(18 + k * 30, -12, "ABC", **rec5)
    b += f"\\node[anchor=west, font={font(9, False)}] at (82,-9) {{A to D}};\n"
    for k in range(4):
        b += row(100 + (k % 2) * 36, -12 - (k // 2) * 14, "ABCD", **rec5)
    b += f"\\node[anchor=west, font={font(9, False)}] at (0,-40) {{A to E}};\n"
    for k in range(18):
        b += row((k % 5) * 36, -54 - (k // 5) * 14, "ABCDE", **rec5)
    s += fig(b, 1)
    s += "\n\\vfill\n\\newpage\n"

    s += "\\prob{11} Find every row that obeys each of these boards.\n"
    b = board(0, 0, "ABCD", {"A": "AD", "B": "AB", "C": "BC", "D": "CD"})
    for k in range(4):
        b += row(146, 36 - k * 14, "ABCD", **dict(rec5, w=7))
    s += fig(b, 1)
    s += "\n\\vspace{6mm}\n"
    b = board(0, 0, "ABCDE", {"A": "AE", "B": "AB", "C": "BC", "D": "CD", "E": "DE"})
    for k in range(15):
        b += row((k % 5) * 36, -14 - (k // 5) * 14, "ABCDE", **rec5)
    s += fig(b, 1)
    s += "\n\\vfill\n\\newpage\n"

    s += ("\\prob{12} In a grid, a shaded square means that card may not sit in that home. "
          "A row puts one dot in every line across and every column.\n")
    ex_shade = [("U", "V"), ("W", "W"), ("X", "U")]
    b = row(0, 4, "VXUW", homes="UVWX", w=8, h=8, card_pt=10, card_s=3, lab_pt=7, lab_s=2.4)
    b += grid(68, 20, "UVWX", ex_shade, [("V", "U")])
    b += f"\\node[font={font(8, False)}] at (80,-9) {{V sits in home U}};\n"
    b += grid(130, 20, "UVWX", ex_shade, [("V", "U"), ("X", "V"), ("U", "W"), ("W", "X")])
    s += fig(b, 8)
    s += ("\n\\vspace{5mm}\nCount the rows that obey each of these four-card grids "
          "without listing them.\n")

    def strip(n):
        L = "ABCDE"[:n]
        sh = [(L[i], L[i]) for i in range(n)] + [(L[i], L[i + 1]) for i in range(n - 1)]
        return L, sh

    def ring(n):
        L, sh = strip(n)
        return L, sh + [(L[-1], "A")]

    def grids_page(n, word):
        Ls, shs = strip(n)
        Lr, shr = ring(n)
        cell = 7
        b = grid(14, 0, Ls, shs, [], cell=cell)
        b += (f"\\node[font={font(8, False)}] at ({f(14 + n*cell/2)},{f(-n*cell - 5)}) "
              f"{{Problem 10, {word} cards}};\n")
        b += grid(84, 0, Lr, shr, [], cell=cell)
        b += (f"\\node[font={font(8, False)}] at ({f(84 + n*cell/2)},{f(-n*cell - 5)}) "
              f"{{Problem 11, {word} cards}};\n")
        top = -n * cell - 16
        b += f"\\node[anchor=west, font={font(8, False)}] at (0,{f(top)}) {{extra grids}};\n"
        small = 5
        pitch = 42
        for line, (L, sh) in enumerate([(Ls, shs), (Lr, shr)]):
            y = top - 7 - line * (n * small + 9)
            for k in range(4):
                b += grid(6 + k * pitch, y, L, sh, [], cell=small, pt=6.5, captions=False)
        return b

    s += fig(grids_page(4, "four"), 0)
    s += "\n\\vfill\n\\newpage\n"
    s += ("\\prob{13} Count the rows that obey each of these five-card grids "
          "without listing them.\n")
    s += fig(grids_page(5, "five"), 0)
    s += "\n\\vfill\n"
    s += END
    return s


def compile_tex(name, tex):
    path = os.path.join(HERE, name + ".tex")
    with open(path, "w") as fh:
        fh.write(tex)
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                            name + ".tex"], cwd=HERE, capture_output=True, text=True)
        if r.returncode:
            print(r.stdout[-3000:])
            raise SystemExit(f"pdflatex failed for {name}")
    os.replace(os.path.join(HERE, name + ".pdf"), os.path.join(OUT, name + ".pdf"))
    log = open(os.path.join(HERE, name + ".log")).read()
    for line in log.splitlines():
        if "Overfull" in line or "Underfull \\vbox" in line:
            print(name, line)
    for ext in (".aux", ".log"):
        os.remove(os.path.join(HERE, name + ext))


if __name__ == "__main__":
    compile_tex("k-1", build_k())
    compile_tex("grades-2-3", build_m())
    compile_tex("grades-4-5", build_u())
    print("ok")
