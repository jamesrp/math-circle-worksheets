#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 69 in the print PDFs.

The guide (GGT69-FAC-v4) gives the K-1 table paper strips, one per route on each road (or
the adult colours), allows new homes and the second tree on the extra copies of page 1, and
gives about 15-20 minutes. The student packet stays GGT69-S-v3 and unchanged. Also
recomputes the strip count: on both printed trees every used road lies on exactly two of the
three routes, and no route has more than 6 roads, so ten strips per colour suffice.
Run from the repository root:
    python3 plans/review/checks/week-69/check_critic_fixes.py
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


# The two printed trees (template.tex \treeone, \treetwo).
TREES = {'tree 1': ['ab', 'bc', 'cd', 'de', 'df', 'cg', 'gh', 'hk', 'bi', 'ij', 'al'],
         'tree 2': ['ab', 'bc', 'cd', 'de', 'bf', 'fg', 'fh', 'di', 'ij', 'ik']}


def route(adj, s, t):
    prev, q = {s: None}, [s]
    for u in q:
        for v in adj[u]:
            if v not in prev:
                prev[v] = u; q.append(v)
    out, v = [], t
    while prev[v] is not None:
        out.append(frozenset((v, prev[v]))); v = prev[v]
    return out


for name, edges in TREES.items():
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b); adj.setdefault(b, []).append(a)
    longest, ok = 0, True
    for h in combinations(sorted(adj), 3):
        routes = [route(adj, h[0], h[1]), route(adj, h[1], h[2]), route(adj, h[0], h[2])]
        longest = max(longest, *map(len, routes))
        used = set().union(*routes)
        ok &= all(sum(e in r for r in routes) == 2 for e in used)
    check(ok, f'{name}: every used road gets exactly two strips, for every three homes')
    check(longest <= 6, f'{name}: longest route {longest} roads, within ten strips per colour')

G = pymupdf.open(Y2 / 'week-69' / 'week-69-facilitator.pdf')
g = ' '.join(flat(p) for p in G)
check(len(G) == 3 and all('GGT69-FAC-v4' in flat(p) for p in G), 'guide: 3 pages, footer GGT69-FAC-v4')
check('A K–1 table works Problem 1 for about 15–20 minutes' in g, 'guide: K-1 route about 15-20 minutes')
check("lay one paper strip of that pair’s colour on every road of its route" in g.replace("'", '’') and 'or the adult colours each route while the children trace it' in g, 'guide: one strip per route, or the adult colours')
check('the second tree on the extra copies of page 1' in g and 'works only the first tree' not in g, 'guide: second tree allowed')
check('every road used gets two strips, never one' in g and 'coloured twice' not in g, 'guide: plain-words key in strips')
check('ten paper strips about 12 by 4 mm in each of the three colours' in g, 'guide: materials list the strips')
old = pymupdf.open(Y2 / 'week-69' / 'archive-before-critic-fixes-2026-10-23' / 'week-69-facilitator.pdf')
check(all('GGT69-FAC-v3' in flat(p) for p in old), 'archived guide is GGT69-FAC-v3')
S = pymupdf.open(Y2 / 'week-69' / 'week-69-students.pdf')
check(len(S) == 4 and all('GGT69-S-v3' in flat(p) for p in S), 'students unchanged: 4 pages, GGT69-S-v3')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
