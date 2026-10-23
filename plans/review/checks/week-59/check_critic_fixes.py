#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 59 in the print PDFs and band views.

Problem 6 (page 6) draws the curved triangle's three arcs at one line width, with no bold
BC arc (W59-S-v4); only page 6 changed above the footer. The guide (W59-F-v3) has the
adult write the K-1 grid-square counts beside each piece's name on page 2, and describes
Problem 6's arcs as drawn alike. Also recomputes Problem 6: three 60-degree arcs of radius
60 mm and a radius-30 circle both measure 60 pi mm. Run from the repository root:
    python3 plans/review/checks/week-59/check_critic_fixes.py
Needs PyMuPDF."""
from fractions import Fraction
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


# Lengths in units of pi mm: an arc of radius r and angle a degrees is r * a / 180.
check(3 * Fraction(60 * 60, 180) == Fraction(2 * 30) == 60, 'Problem 6: both boundaries 60 pi mm')

S = pymupdf.open(Y2 / 'week-59' / 'week-59-students.pdf')
check(len(S) == 6 and all('W59-S-v4' in flat(p) for p in S), 'students: 6 pages, footer W59-S-v4')
old = pymupdf.open(Y2 / 'week-59' / 'archive-before-critic-fixes-2026-10-23' / 'week-59-students.pdf')
same = [flat(a).rsplit('Bellingham', 1)[0] == flat(b).rsplit('Bellingham', 1)[0] for a, b in zip(S, old)]
check(all(same), f'student text unchanged above the footer {same}')


def stroke_widths(page):
    """Line widths of the stroked curves (arcs) drawn on the page."""
    out = []
    for d in page.get_drawings():
        if d.get('type') in ('s', 'fs') and any(it[0] == 'c' for it in d['items']):
            out.append(round(d.get('width') or 0, 2))
    return out


new_w, old_w = stroke_widths(S[5]), stroke_widths(old[5])
check(max(old_w) > min(old_w), f'v3 page 6 had a heavier arc (widths {sorted(set(old_w))})')
check(len(set(new_w)) == 1, f'v4 page 6 draws every curve at one width (widths {sorted(set(new_w))})')
pages_changed = []
for i, (a, b) in enumerate(zip(S, old)):
    pa = a.get_pixmap(dpi=60, clip=pymupdf.Rect(0, 0, a.rect.width, a.rect.height - 60))
    pb = b.get_pixmap(dpi=60, clip=pymupdf.Rect(0, 0, b.rect.width, b.rect.height - 60))
    if pa.samples != pb.samples:
        pages_changed.append(i + 1)
check(pages_changed == [6], f'only page 6 changed above the footer {pages_changed}')

G = ' '.join(flat(p) for p in pymupdf.open(Y2 / 'week-59' / 'week-59-facilitator.pdf'))
check('W59-F-v3' in G and '(six pages, W59-S-v4)' in G, 'guide: W59-F-v3, prints W59-S-v4')
check("writing the two counts beside each piece’s name on page 2" in G.replace("'", '’'), 'guide: K-1 counts written on page 2')
check('its three arcs drawn alike' in G and 'arc highlighted' not in G, 'guide: Problem 6 arcs drawn alike')
M = pymupdf.open(Y2 / 'week-59' / 'week-59-materials.pdf')
check(all('W59-M-v1' in flat(p) for p in M), 'materials unchanged at W59-M-v1')
for name, n in (('k-1', 1), ('grades-2-3', 5)):
    B = pymupdf.open(Y2 / 'band-views' / 'week-59' / f'week-59-{name}.pdf')
    check(len(B) == n and all('W59-S-v4' in flat(p) for p in B), f'{name} band slice: {n} pages, v4')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
