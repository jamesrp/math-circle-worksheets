#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 13 (F13-K-v4, F13-45-v4) in the print PDFs.

Grades 4-5 Problem 5 asks for change-walks on both Problem 1 boards. A new page, "Extra
workspace for Problem 5.", reprints those boards with their reserved routes right after
Problem 5, in the full packet and in the 4-5 return view; on each board exactly one
change-walk exists and adds a route. K-1 Problem 1 no longer says "largest collection";
the guide's supplies are for eleven children. Run from the repository root:
    python3 plans/review/checks/week-13/check_critic_fixes.py
Needs PyMuPDF."""
import importlib.util
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y2 = ROOT / 'lowell-math-circle-year-2'
PRINT, VIEWS = Y2 / 'week-13', Y2 / 'band-views' / 'week-13'
spec = importlib.util.spec_from_file_location('w13figures', Y2 / 'source' / 'week-13' / 'figures.py')
F = importlib.util.module_from_spec(spec)
spec.loader.exec_module(F)
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


def change_walks(name, marks):
    """Every change-walk from s to t: unused arrows forward, reserved arrows backward, no dot twice."""
    steps = {}
    for a, b in F.G[name]['edges']:
        if (a, b) in marks:
            steps.setdefault(b, []).append(a)
        else:
            steps.setdefault(a, []).append(b)
    out = []

    def go(path):
        if path[-1] == 't':
            out.append('-'.join(path))
            return
        for n in steps.get(path[-1], []):
            if n not in path:
                go(path + [n])
    go(['s'])
    return out


def routes_after(name, marks, walk):
    """Toggle the walk's arrows and split the reserved arrows into Start-to-Finish routes."""
    used = set(marks)
    for a, b in zip(walk.split('-'), walk.split('-')[1:]):
        used ^= {(a, b)} if (a, b) in F.G[name]['edges'] else {(b, a)}
    return sum(1 for a, b in used if a == 's'), used


for name, marks, want in (('greedy', F.R1, 's-B-A-t'), ('doubletrap', F.RDOUBLE, 's-B-A-C-E-D-t')):
    walks = change_walks(name, marks)
    n, used = routes_after(name, marks, want)
    starts = sum(1 for a, b in F.G[name]['edges'] if a == 's')
    check(walks == [want] and n == 2 == starts and sum(1 for a, b in used if b == 't') == 2,
          f'{name}: the only change-walk is {walks}, giving {n} routes (all {starts} Start arrows)')

for band, tag, n in (('k-1', 'K-v4', 6), ('grades-2-3', '23-v3', 7), ('grades-4-5', '45-v4', 8)):
    d = pymupdf.open(PRINT / f'week-13-{band}.pdf')
    check(len(d) == n and all(f'Week 13 / F13-{tag}' in p.get_text() for p in d), f'{band}: {n} pages, footer F13-{tag}')

d = pymupdf.open(PRINT / 'week-13-grades-4-5.pdf')
texts = [' '.join(p.get_text().split()) for p in d]
p5 = next(i for i, t in enumerate(texts) if 'Problem 5:' in t)
check('Extra workspace for Problem 5.' in texts[p5 + 1] and 'Problem' not in texts[p5 + 1].replace('Problem 5.', ''),
      f'grades-4-5: page {p5 + 2}, right after Problem 5, is "Extra workspace for Problem 5." with no numbered problem')


def board_shapes(page):
    """The page's drawn paths (board arrows, dots, thick reserved routes): stroke width, colour and
    points, shifted so the topmost drawing starts at 0, in drawing order."""
    ds = page.get_drawings()
    y0 = min(dr['rect'].y0 for dr in ds)
    return [(round(dr.get('width') or 0, 2), dr.get('color'),
             [(pt.x, pt.y - y0) for it in dr['items'] for pt in it[1:] if isinstance(pt, pymupdf.Point)]) for dr in ds]


def same_boards(p, q):
    """Same paths in the same order, each point within 0.2 pt (the boards sit at different heights)."""
    a, b = board_shapes(p), board_shapes(q)
    return len(a) == len(b) > 0 and all(w1 == w2 and c1 == c2 and len(s1) == len(s2) and
                                        all(abs(x1 - x2) < .2 and abs(y1 - y2) < .2 for (x1, y1), (x2, y2) in zip(s1, s2))
                                        for (w1, c1, s1), (w2, c2, s2) in zip(a, b))


check(same_boards(d[p5 + 1], d[0]),
      'grades-4-5: the workspace boards draw exactly what Problem 1 draws, reserved routes included')
r = pymupdf.open(VIEWS / 'week-13-grades-4-5-return.pdf')
rt = [' '.join(p.get_text().split()) for p in r]
i = next(i for i, t in enumerate(rt) if 'Problem 5:' in t)
check('Extra workspace for Problem 5.' in rt[i + 1] and same_boards(r[i + 1], d[0])
      and all('F13-45-v4-return' in t for t in rt),
      f'return view: {len(r)} pages, the Problem 1 boards follow Problem 5 (page {i + 2}), footer F13-45-v4-return')
k = ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(PRINT / 'week-13-k-1.pdf'))
check('Find another way to fit that many routes, if you can.' in k and 'collection' not in k,
      'k-1: Problem 1 asks for another way to fit that many routes; "collection" appears nowhere')
g = ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(PRINT / 'week-13-facilitator.pdf'))
check('For eleven children' in g and 'about 132 small paper closure markers' in g and 'ten children' not in g
      and 'F13-K-v4' in g and 'F13-45-v4 (8 pages' in g and 'upper page 7' in g,
      'guide: eleven children, about 132 markers, names F13-K-v4 and the 8-page F13-45-v4 with its page 7')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
