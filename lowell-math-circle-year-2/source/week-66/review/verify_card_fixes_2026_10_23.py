#!/usr/bin/env python3
"""Check every claim, key and count changed by the October 23, 2026 card fixes (GGT66 v2).

Run from anywhere: python3 review/verify_card_fixes_2026_10_23.py [students.pdf facilitator.pdf]
Checks the dead-end rule (Problem 6's key and the guide's paragraph), the K-1 key and its
plain-word routes, the launch's goal example, Problem 5's answer, the lamp and counter
sizes in the materials line, and the printed wording, numbering and footers.
"""
import itertools, re, sys
from collections import deque
from pathlib import Path

WEEK = Path(__file__).resolve().parent.parent

def moves(s):
    p, lamps = s
    return {'L': (p-1, lamps), 'R': (p+1, lamps), 'F': (p, lamps ^ {p})}
START = (0, frozenset())
def run(word):
    s = START
    for c in word: s = moves(s)[c]
    return s
def formula(p, lamps):
    lo, hi = min(lamps | {0}), max(lamps | {0})
    return len(lamps) + min(-lo + (hi-lo) + abs(p-hi), hi + (hi-lo) + abs(p-lo))
def shape(s):
    p, lamps = s
    return p == 0 and 0 in lamps and min(lamps) < 0 < max(lamps)

# Breadth-first search with no street ends, to distance 14.
dist = {START: 0}; dq = deque([START])
while dq:
    s = dq.popleft()
    if dist[s] == 14: continue
    for t in moves(s).values():
        if t not in dist: dist[t] = dist[s] + 1; dq.append(t)
assert all(formula(*s) == d for s, d in dist.items())
dead = [s for s, d in dist.items() if d < 14 and all(dist[t] == d-1 for t in moves(s).values())]
assert all(shape(s) for s in dead) and len(dead) == sum(1 for s, d in dist.items() if d < 14 and shape(s))
assert all(abs(dist[t]-d) == 1 for s, d in dist.items() if d < 14 for t in moves(s).values())
# The same rule from the formula on a wider window: every walker -6..6, lamps within -5..5.
count = 0
for p in range(-6, 7):
    for bits in range(1 << 11):
        lamps = frozenset(i-5 for i in range(11) if bits >> i & 1)
        d = formula(p, lamps); near = [formula(*t) for t in moves((p, lamps)).values()]
        assert all(abs(x-d) == 1 for x in near)
        assert all(x < d for x in near) == shape((p, lamps)); count += 1

# Guide and Problem 6 key.
for lamps, d in [({-1,0,1},7), ({-2,0,1},9), ({-1,0,2},9), ({-2,-1,0,1},10), ({-1,0,1,2},10), ({-2,0,2},11)]:
    s = (0, frozenset(lamps)); assert dist[s] == d and sorted(dist[t] for t in moves(s).values()) == [d-1]*3
assert sorted(dist[s] for s in dead)[:6] == [7, 9, 9, 10, 10, 11]
assert dist[(0, frozenset({-1,1}))] == 6 and dist[moves((0, frozenset({-1,1})))['F']] == 7
assert dist[(0, frozenset({0,2}))] == 6 and dist[moves((0, frozenset({0,2})))['L']] == 7
# Problem 5: the Problem 3 target has no next move that makes it harder.
assert all(dist[t] < 7 for t in moves((0, frozenset({-1,0,1}))).values())
# Launch goal example and the K-1 key in plain words.
assert run('LFLRR') == run('LFR') == (0, frozenset({-1})) and dist[run('LFR')] == 3
k1 = {'1A': ('RF', (1, {1}), 2), '1B': ('LFRRF', (1, {-1,1}), 5), '1C': ('FRRFLL', (0, {0,2}), 6),
      '2A': ('FRRFLLLLF', (-2, {-2,0,2}), 9), '2C': ('FLLFRRRRF', (2, {-2,0,2}), 9)}
for name, (word, (p, lamps), d) in k1.items():
    assert run(word) == (p, frozenset(lamps)) and len(word) == dist[(p, frozenset(lamps))] == d, name

# Materials line: 13 mm lamps on 19 mm centres; a 17 mm counter leaves 2 mm between neighbours.
tmpl = (WEEK/'template.tex').read_text()
m = re.search(r'\\newcommand\{\\homestreet\}\{\\begin\{tikzpicture\}\[x=([\d.]+)cm.*?circle \(([\d.]+)cm\)', tmpl, re.S)
centre_mm, diameter_mm = float(m.group(1))*10, 2*float(m.group(2))*10
assert abs(centre_mm-19) < 1e-9 and abs(diameter_mm-13) < 1e-9 and centre_mm - 17 == 2

# Printed wording and numbering.
tex = (WEEK/'student'/'students.tex').read_text()
assert re.findall(r'\\problem\{(\d)\}', tex) == ['1','2','3','4','5','6']
assert tex.count('Every target starts with every lamp off and the walker at home, 0.') == 1
for gone in ['Start with every lamp off and the walker at 0.', 'These targets have the same lamps on',
             'Use the large street for your counters.', 'Can you always make a target harder',
             r'\street{1.9}{.65}{0}{}']:
    assert gone not in tex, gone
assert tex.count(r'\homestreet') == 4 + 1          # P1, P2, P3 workspace, P6, plus its definition
assert 'Does every target have at least one next move, L, R or F, that makes it harder to reach from all-off at 0?' in tex
assert 'Find other targets where L, R and F each make the target easier to reach from all-off at 0. Which targets are like this?' in tex
assert tex.count(r'\deadrow') == 6 + 1 and 'GGT66-S-v2' in tex and 'GGT66-S-v1' not in tex
guide = (WEEK/'guide'/'facilitator.tex').read_text()
for s in ['GGT66-FAC-v2', 'Which targets are dead ends.', '13 mm across on 19 mm centres', '17 mm across or smaller',
          'K--1 tables.', r'\word{LFLRR}', r'\word{LFR}', 'Problems 4--6', r'\textbf{Problem 6.}', 'the five student pages']:
    assert s in guide, s

if len(sys.argv) == 3:
    import pymupdf
    st, gd = pymupdf.open(sys.argv[1]), pymupdf.open(sys.argv[2])
    assert len(st) == 5 and len(gd) == 3
    assert all('GGT66-S-v2' in p.get_text() and 'Week 66 / Lamplighter streets / Grades 3' in p.get_text() for p in st)
    assert all('GGT66-FAC-v2' in p.get_text() for p in gd)
    assert 'Problem 6:' in st[4].get_text() and 'Problem 5:' in st[3].get_text()
    print('PDFs: 5 student pages and 3 guide pages, v2 footers, Problem 6 on p. 5.')
print(f'Dead ends to distance 13: {len(dead)}, all of the stated shape; formula window: {count} targets agree.')
print('Neighbouring targets always differ by exactly one move. Keys, launch example and K-1 routes replay.')
print(f'Lamps {diameter_mm:.0f} mm on {centre_mm:.0f} mm centres. Wording, numbering and footers checked. All card-fix checks passed.')
