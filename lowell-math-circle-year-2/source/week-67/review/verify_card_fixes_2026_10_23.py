#!/usr/bin/env python3
"""Check every claim, key and count changed by the October 23, 2026 card fixes (GGT67 v2).

Run from anywhere: python3 review/verify_card_fixes_2026_10_23.py [students.pdf facilitator.pdf]
Checks Problem 4's new right-hand homes and key, the claim that the old triples were the
three neighbours of one label, the guide's launch, K-1 key, two extra maps and majority
rule, the counter size, and the printed wording, numbering, pages and footers.
"""
import re, sys
from collections import deque
from itertools import combinations, product
from pathlib import Path

WEEK = Path(__file__).resolve().parent.parent

def dist(adj):
    out = {}
    for s in adj:
        d = {s: 0}; q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if w not in d: d[w] = d[v] + 1; q.append(w)
        out[s] = d
    return out
def meet(adj, homes):
    d = dist(adj)
    return {m for m in adj if all(d[a][m] + d[m][b] == d[a][b] for a, b in combinations(homes, 2))}
def grid(w, h):
    vs = [(x, y) for x in range(w) for y in range(h)]
    return {v: [u for u in vs if abs(u[0]-v[0]) + abs(u[1]-v[1]) == 1] for v in vs}

cube = {''.join(t): [] for t in product('01', repeat=3)}
for a in cube:
    cube[a] = [b for b in cube if sum(x != y for x, y in zip(a, b)) == 1]
cd = dist(cube)
# Problem 4: the left key is unchanged; the right homes are now 000, 001, 111 with key 001.
assert meet(cube, ['000', '110', '101']) == {'100'}
assert meet(cube, ['000', '001', '111']) == {'001'}
assert [cd[a][b] for a, b in combinations(['000', '001', '111'], 2)] == [1, 3, 2]
for route in [['000', '001'], ['000', '001', '011', '111'], ['001', '011', '111'], ['000', '001', '101', '111'], ['001', '101', '111']]:
    assert all(b in cube[a] for a, b in zip(route, route[1:])) and len(route) - 1 == cd[route[0]][route[-1]]
# The card's point: both old triples were the three neighbours of their meeting label; the new one is not.
assert set(cube['100']) == {'000', '110', '101'} and set(cube['011']) == {'001', '010', '111'}
assert '111' not in cube['001']
# Majority = middle value, for every triple of distinct labels.
for homes in combinations(cube, 3):
    assert meet(cube, homes) == {''.join(sorted(h[k] for h in homes)[1] for k in range(3))}
# Launch: all six dots work for P = (0,0) and Q = (2,1).
g = grid(3, 2); gd = dist(g)
assert {m for m in g if gd[(0, 0)][m] + gd[m][(2, 1)] == gd[(0, 0)][(2, 1)]} == set(g)
# K-1 key on Problem 1's left board.
G = grid(5, 5); Gd = dist(G)
two = {m for m in G if Gd[(0, 0)][m] + Gd[m][(4, 1)] == Gd[(0, 0)][(4, 1)]}
assert two == {(x, y) for x in range(5) for y in range(2)} and len(two) == 10
assert meet(G, [(0, 0), (4, 1), (1, 4)]) == {(1, 1)}
tree = {}
for a, b in [('a','u'),('u','v'),('v','w'),('w','b'),('v','t'),('t','c'),('w','s'),('s','r'),('u','q')]:
    tree.setdefault(a, []).append(b); tree.setdefault(b, []).append(a)
assert meet(tree, 'abc') == {'v'} and 't' in tree['c'] and 'v' in tree['t']   # the junction below C
# The guide's two extra maps.
k23 = {h: ['x', 'y'] for h in 'abc'}; k23.update({c: list('abc') for c in 'xy'})
assert meet(k23, 'abc') == {'x', 'y'}
ring = {i: [(i-1) % 6, (i+1) % 6] for i in range(6)}
assert meet(ring, [0, 2, 4]) == set()

# Counter size: dot spacing 1.6 cm (1.55 cm on p. 2) against a 1.2 cm counter.
problems = {p.name: p.read_text() for p in (WEEK/'problems').glob('*.md')}
assert '[x=1.6cm,y=1.6cm]\\grid{4}' in problems['01-grid-meeting-dots.md']
assert '[x=1.55cm,y=1.55cm]\\grid{4}' in problems['02-none-or-two.md']
assert '[x=1.6cm,y=1.6cm,font=\\small]' in problems['00-rules.md']      # the P-M-Q example at board spacing
assert 15.5 - 12 > 3

# Printed wording and numbering.
tex = (WEEK/'student'/'students.tex').read_text()
assert re.findall(r'\\problem\{(\d)\}', tex) == ['1', '2', '3', '4', '5']
assert 'and 000, 001, and 111 on the right.' in tex
for gone in ['Each dot on these maps has a three-digit label.', 'Keep a drawing of your attempts.', '001, 010, and 111']:
    assert gone not in tex, gone
assert tex.count('\\cube\\end{tikzpicture}') == 4 and 'GGT67-S-v2' in tex and 'GGT67-S-v1' not in tex
guide = (WEEK/'guide'/'facilitator.tex').read_text()
for s in ['GGT67-FAC-v2', 'K--1 tables.', 'median graphs', 'middle value', 'all six dots work for P and Q',
          'about 1.2 cm across', 'keep a drawing of each attempt', 'Two more maps for a ready pair',
          'unique meeting label is \\textbf{001}', 'the five student pages', 'pages 4--5']:
    assert s in guide, s
assert 'No K--1 adaptation' not in guide and '\\textbf{011}' not in guide

if len(sys.argv) == 3:
    import pymupdf
    st, gdoc = pymupdf.open(sys.argv[1]), pymupdf.open(sys.argv[2])
    assert len(st) == 5 and len(gdoc) == 3
    assert all('GGT67-S-v2' in p.get_text() and 'Week 67 / Meeting on shortest roads / Grades 3' in p.get_text() for p in st)
    assert all('GGT67-FAC-v2' in p.get_text() for p in gdoc)
    assert 'Problem 4:' in st[3].get_text() and 'Problem 5:' not in st[3].get_text() and 'Problem 5:' in st[4].get_text()
    print('PDFs: 5 student pages and 3 guide pages, v2 footers, Problem 5 alone on p. 5.')
print('Problem 4 keys 100 and 001; majority rule on all 56 cube triples; launch, K-1 key and extra maps checked.')
print('Wording, numbering and footers checked. All card-fix checks passed.')
