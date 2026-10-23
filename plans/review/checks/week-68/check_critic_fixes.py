#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 68 in the print PDFs.

The guide (GGT68-FAC-v3) prepares a fourth set, with one copy each of pages 1 and 4, for
the K-1 table, says "one shared copy of pages 1 and 4", and adds a Problem 3 follow-up
about two dots not on the same rung. The student packet stays GGT68-S-v2 and unchanged.
Also recomputes the follow-up's answer on the printed nine-column ladder: two-dot splits
not on one rung exist (the 16 diagonal pairs). Run from the repository root:
    python3 plans/review/checks/week-68/check_critic_fixes.py
Needs PyMuPDF."""
from itertools import combinations
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


# The ladder: columns -7..7 (the printed nine are -4..4), rails 0 and 1, rungs at every column.
cols = range(-7, 8)
V = {(x, y) for x in cols for y in (0, 1)}
E = [((x, y), (x + 1, y)) for x in range(-7, 7) for y in (0, 1)] + [((x, 0), (x, 1)) for x in cols]


def forever(blocked):
    open_ = V - blocked
    adj = {v: [] for v in open_}
    for a, b in E:
        if a in open_ and b in open_:
            adj[a].append(b); adj[b].append(a)
    seen, n = set(), 0
    for v in open_:
        if v in seen:
            continue
        stack, comp = [v], set()
        while stack:
            u = stack.pop()
            if u in comp:
                continue
            comp.add(u); stack.extend(adj[u])
        seen |= comp
        n += bool(comp & {(-7, 0), (-7, 1), (7, 0), (7, 1)})
    return n


printed = [(x, y) for x in range(-4, 5) for y in (0, 1)]
splits = [c for c in combinations(printed, 2) if forever(set(c)) == 2]
off_rung = [c for c in splits if c[0][0] != c[1][0]]
check(len(splits) == 25 and len(off_rung) == 16, f'printed ladder: 25 two-dot splits, {len(off_rung)} not on one rung')
check(all(abs(a[0] - b[0]) == 1 and a[1] != b[1] for a, b in off_rung), 'every off-rung split is a diagonal pair')

G = pymupdf.open(Y2 / 'week-68' / 'week-68-facilitator.pdf')
g = ' '.join(flat(p) for p in G)
check(len(G) == 3 and all('GGT68-FAC-v3' in flat(p) for p in G), 'guide: 3 pages, footer GGT68-FAC-v3')
check('Prepare four sets: three for two third-grade pairs' in g and 'a fourth, with one copy each of pages 1 and 4, for the K–1 table' in g, 'guide: a fourth set with pages 1 and 4 for the K-1 table')
check('one shared copy of pages 1 and 4' in g and 'one shared page' not in g and 'Prepare three sets' not in g, 'guide: "one shared copy of pages 1 and 4"')
check('Can you split it with two dots that are not on the same rung?' in g.replace('\n', ' '), 'guide: Problem 3 follow-up')
old = pymupdf.open(Y2 / 'week-68' / 'archive-before-critic-fixes-2026-10-23' / 'week-68-facilitator.pdf')
check(all('GGT68-FAC-v2' in flat(p) for p in old), 'archived guide is GGT68-FAC-v2')
S = pymupdf.open(Y2 / 'week-68' / 'week-68-students.pdf')
check(len(S) == 4 and all('GGT68-S-v2' in flat(p) for p in S), 'students unchanged: 4 pages, GGT68-S-v2')
check('Problem 1:' in flat(S[0]) and 'Problem 7:' in flat(S[3]), 'pages 1 and 4 hold Problems 1 and 7')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
