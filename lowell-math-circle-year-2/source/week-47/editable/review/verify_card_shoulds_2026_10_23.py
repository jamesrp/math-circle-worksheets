#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes to Week 47 (shoulds 1-7, coulds 8-13) by enumeration
and by reading the reference PDFs.

A landscape is a row of whole heights, at least 0, neighbours differing by at most 1, with
some sites fixed as clues. Every changed claim is recomputed here by brute force, with no
height ceiling unless a check says otherwise, and the boards, rows and clue discs are read
from the PDFs. Nothing is imported from the builders. Run from anywhere:
    python3 review/verify_card_shoulds_2026_10_23.py [folder with the four PDFs]
"""
import re
import sys
from collections import deque
from itertools import combinations, product
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
REF = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'reference-pdfs'
MM = 72 / 25.4
checks = []


def legal(h):
    return min(h) >= 0 and all(abs(a - b) <= 1 for a, b in zip(h, h[1:]))


def completions(n, clues, top=None):
    """Every landscape on sites 0..n-1 through clues {site: height}; heights never exceed
    max(clue) + n, which no completion can reach, unless a drawn top is given."""
    cap = top if top is not None else max(clues.values(), default=0) + n
    rows = [(h,) for h in range(cap + 1)]
    for _ in range(n - 1):                                   # grow left to right, one step at a time
        rows = [r + (v,) for r in rows for v in (r[-1] - 1, r[-1], r[-1] + 1) if 0 <= v <= cap]
    return [h for h in rows if all(h[c] == a for c, a in clues.items())]


def envelopes(n, clues):
    L = tuple(max([0] + [a - abs(i - c) for c, a in clues.items()]) for i in range(n))
    U = tuple(min(a + abs(i - c) for c, a in clues.items()) for i in range(n))
    return L, U


def N(s):
    """Drop hyphens and a following space, so a word hyphenated at a line end still matches."""
    return re.sub(r'-\s?', '', ' '.join(s.split()))


class T(str):
    """Page text whose `in` and startswith ignore hyphenation."""
    def __contains__(self, s):
        return N(s) in N(str(self))

    def startswith(self, s):
        return N(str(self)).startswith(N(s))


def text(page):
    return T(' '.join(page.get_text().split()))


def boxes(page, shaded):
    """Row boxes (rounded rectangles of a given fill) as (x mm, y mm, w mm, label)."""
    words = page.get_text('words')
    out = []
    for d in page.get_drawings():
        r, f = d['rect'], d.get('fill')
        if r.height / MM < 11.5 or r.height / MM > 12.5 or r.width / MM < 10 or r.width / MM > 24:
            continue
        if shaded != (f is not None and f[0] < .95):
            continue
        inside = [w[4] for w in words if r.x0 < (w[0] + w[2]) / 2 < r.x1 and r.y0 < (w[1] + w[3]) / 2 < r.y1]
        out.append((round(r.x0 / MM, 1), round(r.y0 / MM, 1), round(r.width / MM, 1), ''.join(inside)))
    return sorted(out, key=lambda b: (b[1], b[0]))


def discs(page):
    """Black clue discs (10 mm) as (centre x mm, centre y mm, printed height)."""
    words = page.get_text('words')
    out = []
    for d in page.get_drawings():
        r, f = d['rect'], d.get('fill')
        if f == (0, 0, 0) or (f and max(f) < .05):
            if abs(r.width / MM - 10) < .3:
                inside = [w[4] for w in words if r.contains(pymupdf.Point((w[0] + w[2]) / 2, (w[1] + w[3]) / 2))]
                out.append((round((r.x0 + r.x1) / 2 / MM, 1), round((r.y0 + r.y1) / 2 / MM, 1), ''.join(inside)))
    return sorted(out)


def grid_dots(page):
    return [d['rect'] for d in page.get_drawings() if d.get('fill') and min(d['fill']) > .95
            and abs(d['rect'].width / MM - 1.6) < .1]


k1, b23, b45 = (pymupdf.open(REF / f) for f in ('k-1.pdf', 'grades-2-3.pdf', 'grades-4-5.pdf'))
guide = pymupdf.open(REF / 'facilitator-guide.pdf')
g = [text(p) for p in guide]
G = T(' '.join(g))
assert (len(k1), len(b23), len(b45), len(guide)) == (6, 5, 6, 5)
for name, doc, tag in (('K-1', k1, 'K'), ('2-3', b23, '23'), ('4-5', b45, '45')):
    numbers = []
    for i, p in enumerate(doc):
        t = text(p)
        assert f'Bellingham Math Circle / Week 47 / F47-{tag}-v4' in t, (name, i)
        numbers += [int(n) for n in re.findall(r'Problem (\d+):', t)]
    assert numbers == list(range(1, 8)), (name, numbers)
checks.append('packets: K-1 6 pages, Grades 2-3 5, Grades 4-5 6, guide 5; footers F47-*-v4; Problems 1-7 in order')

# --- Should 1: record rows for Grades 2-3 and 4-5 Problems 1 and 2 ------------------------
p1 = completions(5, {0: 1, 4: 1})
p2 = completions(5, {0: 0, 4: 2})
assert len(p1) == 18 and {h[2] for h in p1} == {0, 1, 2, 3}
assert sorted({h[2] for h in p2}) == [0, 1, 2]
for doc in (b23, b45):
    s1, s2 = boxes(doc[0], True), boxes(doc[1], True)
    assert [b[3] for b in s1] == ['1'] * 8 and len(boxes(doc[0], False)) == 12, s1   # four rows 1 _ _ _ 1
    assert [b[3] for b in s2][:6] == ['0', '2'] * 3 and all(b[2] == 11 for b in s2[:6]), s2   # three rows 0 _ _ _ 2
    assert 'Problem 3' in text(doc[1])                      # P3 keeps its place on page 2
checks.append('should 1: Grades 2-3 and 4-5 p. 1 print four rows 1 _ _ _ 1 beside the Problem 1 board (18 landscapes '
              'exist, middle 0-3), p. 2 three rows 0 _ _ _ 2 beside the Problem 2 board (star heights exactly 0, 1, '
              '2); Problem 3 stays on p. 2')

# --- Should 2: K-1 Problem 7 has its own empty board, levels 0-4 ----------------------------
t6 = text(k1[5])
assert t6.startswith('Week 47 / Gentle-step landscapes / K–1 Problem 7: Put two clues on this board for a friend to solve.')
assert len(grid_dots(k1[5])) == 25 and not discs(k1[5])            # 5 sites x 5 levels, no clues
assert 'Replace the old clues' not in ' '.join(text(p) for p in k1)
forcing = []
for (c, d) in combinations(range(5), 2):
    for a, b in product(range(5), repeat=2):                          # clue heights on the drawn levels 0-4
        if len(completions(5, {c: a, d: b})) == 1:
            forcing.append(((c, a), (d, b)))
assert forcing == [((0, 0), (4, 4)), ((0, 4), (4, 0))], forcing
old = [((c, a), (d, b)) for (c, d) in combinations(range(5), 2) for a, b in product(range(4), repeat=2)
       if len(completions(5, {c: a, d: b})) == 1]
assert old == []                                                    # the old P6 board (levels 0-3) had none
assert 'no other pair of clues on this board forces one landscape' in G and '(4,3,2,1,0)' in G
checks.append('should 2: K-1 p. 6 is Problem 7, "Put two clues on this board for a friend to solve.", on an empty '
              'five-site board, levels 0-4; on it only h(0)=0, h(4)=4 and the mirror force a landscape (on the old '
              'levels 0-3 board none did), as the guide now says')

# --- Should 3: counters and partner checks in the guide ------------------------------------
assert '7 white and 3 black flat counters' in G and 'move off those discs' in G
assert 'the other checks both jumps beside it before the next move' in G
assert (1, 2, 0, 2, 1) and not legal((1, 2, 0, 2, 1)) and 'gives (1,2,0,2,1), with two jumps of 2' in G
assert max(len(discs(p)) for d in (k1, b23, b45) for p in d) == 3     # never more than 3 printed clues
checks.append('should 3: the guide gives each child 7 white and 3 black counters (boards have at most 7 sites and 3 '
              'printed clues), says when black counters leave their printed discs, and has the K-1 Problem 6 partner '
              'check both jumps; lowering the middle first, (1,2,0,2,1), is illegal')

# --- Should 4: Grades 4-5 Problem 6 --------------------------------------------------------
t5 = text(b45[4])
assert 'On each board, shade every height each white marker can have. If you pick one shaded height in every ' \
       'column, do your picks always make a landscape?' in t5 and 'The shaded marks' not in t5
assert not [d for d in b45[4].get_drawings() if d.get('fill') and .5 < d['fill'][0] < .9]   # no gray shading printed
assert [x[2] for x in discs(b45[4])] == ['0', '2', '3'] and len(grid_dots(b45[4])) == 2 * 42   # two 7 x 6 grids
for clues, expect in (({3: 2}, {0: (0, 5), 1: (0, 4), 2: (1, 3), 4: (1, 3), 5: (0, 4), 6: (0, 5)}),
                      ({0: 0, 5: 3}, {1: (0, 1), 2: (0, 2), 3: (1, 3), 4: (2, 4), 6: (2, 4)})):
    sols = completions(7, clues)
    got = {i: (min(h[i] for h in sols), max(h[i] for h in sols)) for i in range(7) if i not in clues}
    assert got == expect and all(set(h[i] for h in sols) == set(range(lo, hi + 1)) for i, (lo, hi) in got.items())
    assert max(max(h) for h in sols) <= 5                                  # fits the drawn levels 0-5
    L, U = envelopes(7, clues)
    assert L in sols and U in sols                                         # lowest picks and highest picks fit
board2 = completions(7, {0: 0, 5: 3})
assert any(h[2] == 0 for h in board2) and any(h[3] == 3 for h in board2) and not any(h[2] == 0 and h[3] == 3 for h in board2)
board1 = completions(7, {3: 2})
assert any(h[1] == 4 for h in board1) and any(h[2] == 1 for h in board1) and not any(h[1] == 4 and h[2] == 1 for h in board1)
assert 'sites 1-4 allow 0-1, 0-2, 1-3, 2-4 and site 6 allows 2-4' in G and 'never together' in G
checks.append('should 4: Grades 4-5 p. 5 asks children to shade, on h(3)=2 (ranges 0-5, 0-4, 1-3 | 1-3, 0-4, 0-5) '
              'and on h(0)=0, h(5)=3 (0-1, 0-2, 1-3, 2-4, then 2-4), with no printed shading; 0 at site 2 and 3 at '
              'site 3, and 4 at site 1 and 1 at site 2, are each allowed but never together, while the lowest and '
              'highest picks are landscapes; the guide keys both')

# --- Should 5: Grades 2-3 Problem 6, the only forcing pairs --------------------------------
pairs = [((c, a), (d, b)) for (c, d) in combinations(range(7), 2) for a, b in product(range(7), repeat=2)
         if abs(a - b) <= d - c]
force7 = [p for p in pairs if len(completions(7, dict(p))) == 1]
assert len(pairs) == 679 and force7 == [((0, 0), (6, 6)), ((0, 6), (6, 0))]
assert len(completions(7, {1: 0, 5: 4})) == 6
assert 'On this board these are the only forcing pairs' in G and 'still allows 6 landscapes' in G
assert 'not a required classification' not in G
checks.append('should 5: of the 679 consistent two-clue sets on the Grades 2-3 Problem 6 board only h(0)=0, h(6)=6 '
              'and its mirror force a landscape, and h(1)=0, h(5)=4 allows 6, as the guide now says')

# --- Should 6: the overview's hypothesis and the move fact ---------------------------------
assert 'When the pairwise condition holds, the simultaneous least and greatest completions are' in G
L, U = envelopes(5, {0: 0, 2: 3})
assert (L, U) == ((1, 2, 3, 2, 1), (0, 1, 2, 3, 4)) and not completions(5, {0: 0, 2: 3})
assert 'they give L = (1,2,3,2,1) and U = (0,1,2,3,4)' in G
for n, top in ((4, 3), (5, 3), (6, 2)):
    rows = [h for h in product(range(top + 1), repeat=n) if legal(h)]
    cap = top + n
    for s in rows:
        dist, q = {s: 0}, deque([s])                                       # legal one-level moves, no ceiling
        while q:
            h = q.popleft()
            for i in range(1, n - 1):                                      # the end sites are clues
                for e in (-1, 1):
                    t = h[:i] + (h[i] + e,) + h[i + 1:]
                    if 0 <= t[i] <= cap and legal(t) and t not in dist:
                        dist[t] = dist[h] + 1; q.append(t)
        for t in rows:
            if (t[0], t[-1]) == (s[0], s[-1]):
                assert dist[t] == sum(abs(a - b) for a, b in zip(s, t)), (s, t)
assert 'the fewest moves between two landscapes with the same clues always equals the total change' in G
checks.append('should 6: the overview says "When the pairwise condition holds"; P4\'s first set gives L = '
              '(1,2,3,2,1), U = (0,1,2,3,4), neither a landscape; fewest legal moves = total change for every pair '
              'of landscapes with equal end clues on 4 and 5 sites (heights 0-3) and 6 sites (0-2)')

# --- Should 7 and could 13: the hour --------------------------------------------------------
assert 'stand and act out' not in G and '0-5 running; 5-9 launch; 9-47 at the tables' in G
assert 'eleven-child group' in G and 'ten-child' not in G and 'after the five-minute run' in G
checks.append('should 7, could 13: the hour starts with the five-minute run, the unexplained walk is gone, and the '
              'group is eleven')

# --- Coulds 8-12 ---------------------------------------------------------------------------
for doc in (k1, b23, b45):
    words = doc[0].get_text('words')
    y = {w[4]: w[1] / MM for w in words if w[4] in ('allowed', 'jump', 'Problem')}
    assert y['allowed'] < y['jump'] < y['Problem']
    t = text(doc[0])
    assert 'Black circles and shaded boxes are fixed clues.' in t
    assert all('Shaded boxes are fixed clues' not in text(p) for p in doc)
checks.append('coulds 8-9: page 1 shows "jump too big" under the "allowed" towers, above Problem 1, and the rules say '
              '"Black circles and shaded boxes are fixed clues"; the P3 sentence is gone')
p5 = completions(7, {0: 1, 4: 3, 6: 1})
tot = sorted(sum(h) for h in p5)
assert len(p5) == 10 and tot[0] == 10 and tot[-1] == 16 and tot.count(10) == tot.count(16) == 1
assert envelopes(7, {0: 1, 4: 3, 6: 1}) == ((1, 0, 1, 2, 3, 2, 1), (1, 2, 3, 4, 3, 2, 1))
assert 'Is there a landscape that is as low as possible at every site at once?' in text(b45[3])
assert 'smallest total height' in text(b23[3]) and 'fewest blocks' not in text(b23[3])
assert 'upward tent f' in G and 'Make one landscape that is as low' not in text(b45[3])
checks.append('coulds 10-12: Grades 4-5 Problem 5 asks whether one landscape is lowest everywhere (yes: '
              '1,0,1,2,3,2,1; highest 1,2,3,4,3,2,1), Grades 2-3 says "smallest total height" (10 and 16, each from '
              'one landscape), and the guide defines the upward tents')

for c in checks:
    print('PASS', c)
