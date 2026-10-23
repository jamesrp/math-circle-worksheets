#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 70 in the print PDFs.

The guide (GGT70-FAC-v3) extends its possible Grades 2-3 route from "Problem 1 alone" to
Problem 2's shots A-C, about 15-20 minutes. The student packet stays GGT70-S-v2.
Also recomputes the route's claims in the side-4 room (S = (0,0), T copies at 2 mod 4):
the shots at A (2,6) and B (6,2) reach their own letter first and fold to Problem 1's two
drawn shots, (0,0)-(4/3,4) then (4/3,0)-(2,2), and (0,0)-(4,4/3) then (0,4/3)-(2,2); the
shot at C (6,6) stops at the room's own T (2,2). Run from the repository root:
    python3 plans/review/checks/week-70/check_critic_fixes.py
Needs PyMuPDF."""
from fractions import Fraction as F
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y2 = ROOT / 'lowell-math-circle-year-2'
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


def flat(page):
    return ' '.join(page.get_text().split())


def first_t(x, y):
    """First T copy (both coordinates 2 mod 4) on the segment from (0,0) to (x,y)."""
    for k in range(1, 241):
        s = F(k, 240)
        px, py = s * x, s * y
        if px.denominator == py.denominator == 1 and px % 4 == 2 and py % 4 == 2:
            return (int(px), int(py)), s


def on_segment(p, a, b):
    (px, py), (ax, ay), (bx, by) = p, a, b
    return (bx - ax) * (py - ay) == (by - ay) * (px - ax) and min(ax, bx) <= px <= max(ax, bx) and min(ay, by) <= py <= max(ay, by)


def folds_onto(x, y, pieces):
    """Every sampled point of the shot up to its first T, folded into the room, lies on the pieces."""
    _, s_end = first_t(x, y)
    for k in range(1, 241):
        s = s_end * F(k, 240)
        q = (s * x % 4, s * y % 4)
        if not any(on_segment(q, a, b) for a, b in pieces):
            return False
    return True


STEEP = [((0, 0), (F(4, 3), 4)), ((F(4, 3), 0), (2, 2))]
SHALLOW = [((0, 0), (4, F(4, 3))), ((0, F(4, 3)), (2, 2))]
check(first_t(2, 6)[0] == (2, 6) and first_t(6, 2)[0] == (6, 2), 'A and B reach their own letter first')
check(first_t(6, 6)[0] == (2, 2), "C stops at the room's own T (2,2)")
check(folds_onto(2, 6, STEEP), "A's shot folds onto Problem 1's steep drawn shot")
check(folds_onto(6, 2, SHALLOW), "B's shot folds onto Problem 1's shallow drawn shot")

G = pymupdf.open(Y2 / 'week-70' / 'week-70-facilitator.pdf')
g = ' '.join(flat(p) for p in G)
check(len(G) == 3 and all('GGT70-FAC-v3' in flat(p) for p in G), 'guide: 3 pages, footer GGT70-FAC-v3')
check('A possible Grades 2–3 route, untested, about 15–20 minutes' in g and 'Problem 1 alone' not in g, 'guide: 2-3 route about 15-20 minutes, not Problem 1 alone')
check("then Problem 2’s shots A–C, laying a ruler from S to each letter" in g.replace("'", '’'), "guide: 2-3 route continues to Problem 2's shots A-C")
check("A and B are Problem 1’s drawn shots unfolded; C stops at the room’s own T." in g.replace("'", '’'), 'guide: what A, B and C show')
old = pymupdf.open(Y2 / 'week-70' / 'archive-before-critic-fixes-2026-10-23' / 'week-70-facilitator.pdf')
check(all('GGT70-FAC-v2' in flat(p) for p in old), 'archived guide is GGT70-FAC-v2')
S = pymupdf.open(Y2 / 'week-70' / 'week-70-students.pdf')
check(len(S) == 4 and all('GGT70-S-v2' in flat(p) for p in S), 'students unchanged: 4 pages, GGT70-S-v2')
p2 = flat(S[1])
check('A (2, 6), B (6, 2), C (6, 6)' in p2, 'page 2 letters the T copies A-C')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
