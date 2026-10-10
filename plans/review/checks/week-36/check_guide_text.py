#!/usr/bin/env python3
"""Tie the numbers I verified to the delivered guide text, page by page.

Reads week-36-facilitator.pdf and week-36-bonus-facilitator.pdf with pdftotext and checks that
each claim tested in check_math.py / check_bonus.py is printed on the page the guide cites.
Run: python3 check_guide_text.py > out_check_guide_text.txt
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import PRINT, ok, finish  # noqa: E402


def pages(pdf):
    out = subprocess.run(["pdftotext", "-layout", str(PRINT / pdf), "-"], capture_output=True, text=True).stdout
    return [" ".join(p.split()) for p in out.split("\f")]


G = pages("week-36-facilitator.pdf")
B = pages("week-36-bonus-facilitator.pdf")

claims = [
    (G, 1, "It has 12 allowed threes, four through each tile. Distinct threes meet in 0 or 1 tile."),
    (G, 1, "There are exactly four ways to partition the nine tiles into three allowed threes"),
    (G, 1, "The largest line-free collection has 4 tiles."),
    (G, 1, "Legal collection sizes 0, 1, 2, 3, 4 have respectively 9, 8, 6, 3, 0 legal extensions."),
    (G, 1, "the second player wins regardless of choices"),
    (G, 3, "Top left: open circle + striped circle → solid circle. Top right: open circle + open triangle → open square. Bottom left: striped circle + solid triangle → open square. Bottom right: striped triangle + open square → solid circle."),
    (G, 3, "four partitions exist in total; page 4 lists all."),
    (G, 3, "page 5 explains why no five-tile answer can exist."),
    (G, 3, "striped circle + solid circle; open triangle + open square; striped triangle + solid square; solid triangle + striped square."),
    (G, 3, "all legal games last exactly four moves."),
    (G, 4, "Split 3: {CO, TH, SF}; {CH, TF, SO}; {CF, TO, SH}."),
    (G, 4, "Split 4: {CO, TF, SH}; {CH, TO, SF}; {CF, TH, SO}."),
    (G, 4, "the ten-pair argument on page 5".capitalize()),
    (G, 5, "Counts of legal subsets of sizes 0 through 5 are 1, 9, 36, 72, 54 and 0."),
    (G, 5, "The maximum proof with physical pairs"),
    (B, 1, "the first player can force a win."),
    (B, 1, "there are four wrap-around triples not in ordinary tic-tac-toe."),
    (B, 1, "The student sites are 108 pt (38.1 mm); the layer sites are 58 pt (20.5 mm)."),
    (B, 2, "(3,024 losing terminal branches, latest loss on second's fourth claim)"),
    (B, 2, "There are 3,762 valid assignments with three named colors"),
    (B, 2, "RRB RRB BBG"),
    (B, 2, "122 233 233"),
    (B, 2, "Changing all numbers to 1 makes all 12 shape/fill threes reappear."),
    (B, 2, "different coordinates may create cross-layer triples."),
]
for doc, page, text in claims:
    which = "base guide" if doc is G else "bonus guide"
    ok(text in doc[page - 1], "%s p.%d prints: %s" % (which, page, text[:90]))
finish()
