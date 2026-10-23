#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card fixes (plans/review/week-19.md): the card sheet,
the launch collection, the arrow rows in the Grades 2-3 P7 key, the cover-equals-maximum claim on
guide p. 1, the timing, and the changed student wording. Run from anywhere; prints PASS lines."""
import importlib.util, itertools, json, re, sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PKG = HERE.parent
for week in (PKG / 'problem-files', PKG.parent):
    if (week / 'figures.py').exists() and (week / 'week.toml').exists():
        break
else:
    sys.exit('Cannot find the Week 19 problem files')
spec = importlib.util.spec_from_file_location('w19fig', week / 'figures.py')
fig = importlib.util.module_from_spec(spec); spec.loader.exec_module(fig)

# --- the card sheet: sixteen distinct 4.5 cm cards, every one with its top mark inside it ---
tex = fig.card_sheet_tex()
rects = [tuple(map(float, m)) for m in re.findall(r'rounded corners=2pt\] \(([\d.]+),([\d.]+)\) rectangle \(([\d.]+),([\d.]+)\)', tex)]
assert len(rects) == 16
for x, y, X, Y in rects:
    assert abs((X - x) * 2.54 - 4.5) < 1e-9 and abs((Y - y) * 2.54 - 4.5) < 1e-9
assert sorted(fig.SHEET_ORDER) == list(range(16))
marks = [tuple(map(float, m)) for m in re.findall(r'line width=3pt\] \(([\d.]+),([\d.]+)\) -- \(([\d.]+),([\d.]+)\)', tex)]
assert len(marks) == 16
for (x, y, X, Y), (a, b, c, d) in zip(rects, marks):
    assert x < a < c < X and y < b == d < y + .1 * (Y - y)        # inside the top edge, so it survives cutting
left, right = min(r[0] for r in rects), max(r[2] for r in rects)
top, bottom = min(r[1] for r in rects), max(r[3] for r in rects)
assert left >= .4 and right <= 8.5 - .4 and abs(left - (8.5 - right)) < 1e-9   # centred, inside printer margins
assert top >= 1.9 and bottom <= 10.3                                          # below the note, above the footer
gaps = sorted({round(b[0] - a[2], 6) for a, b in zip(rects, rects[1:]) if abs(a[1] - b[1]) < 1e-9})
assert gaps == [fig.SHEET_GAP]
print(f'PASS: card sheet; 16 distinct 4.5 cm cards, {fig.SHEET_GAP} in cutting gaps, marks inside, grid {right-left:.2f} x {bottom-top:.2f} in.')

# --- symbols: A circle 1, B triangle 2, C square 4, D star 8 ---
name = lambda m: ''.join(s for b, s in enumerate('ABCD') if m >> b & 1) or 'empty'
card = lambda s: sum(1 << 'ABCD'.index(ch) for ch in s)
inside = lambda a, b: a & b == a
legal = lambda c: all(not inside(a, b) and not inside(b, a) for a, b in itertools.combinations(c, 2))

# --- the launch: BC and BD may go together, B is rejected (it is on BC), ACD joins; in no task ---
BC, BD, B, ACD = card('BC'), card('BD'), card('B'), card('ACD')
assert legal([BC, BD]) and inside(B, BC) and not legal([BC, BD, B]) and legal([BC, BD, ACD])
launch = {BC, BD, ACD}
pairs = {card(p) for p in ['AB', 'AC', 'AD', 'BC', 'BD', 'CD']}
assert not launch <= pairs                                          # not part of the unique six
starts = [{7}, {1}, {3}, {1, 6}, {15}, {1, 14}, {3, 5}]          # every printed starting collection
assert not any(s & launch for s in [{7}, {1}, {3}, {15}])          # no printed starting card at all
assert not any(s <= launch for s in starts)
groups = [{0, 1, 2}, {1, 3, 2}, {3, 5, 6}, {1, 6, 7}]               # K-1 P1's groups
assert not any(launch <= g for g in groups) and BD & 8 and ACD & 8  # D's star: not the eight-card deck
print('PASS: launch collection BC/BD/ACD is legal, B is rejected, and it answers no printed task.')

# --- Grades 2-3 P7 key: the arrow rows are a nested cover of all sixteen cards ---
rows = [['empty', 'A', 'AB', 'ABC', 'ABCD'], ['D', 'AD', 'ABD'], ['C', 'AC', 'ACD'], ['CD'], ['B', 'BC', 'BCD'], ['BD']]
val = lambda s: 0 if s == 'empty' else card(s)
cells = [val(s) for r in rows for s in r]
assert sorted(cells) == list(range(16))
assert all(inside(val(a), val(b)) and val(a) != val(b) for r in rows for a, b in zip(r, r[1:]))
print('PASS: the six arrow rows cover the sixteen cards once, each step a strict containment.')

# --- guide p. 1: each full deck has a cover with as many rows as its largest collection ---
def min_cover(n):
    """Fewest chains covering the 2^n subsets: vertices minus a maximum matching (Fulkerson)."""
    V = range(1 << n); match = {}
    def aug(u, seen):
        for v in V:
            if v != u and inside(u, v) and v not in seen:
                seen.add(v)
                if v not in match or aug(match[v], seen):
                    match[v] = u; return True
        return False
    return (1 << n) - sum(aug(u, set()) for u in V)
for n, top_size in [(2, 2), (3, 3), (4, 6)]:
    cards = range(1 << n)
    biggest = max(len(c) for r in range(1, top_size + 2) for c in itertools.combinations(cards, r) if legal(c))
    assert biggest == top_size == min_cover(n)
print('PASS: for two, three and four symbols the fewest rows equal the largest collection (2, 3, 6).')

# --- guide p. 2 timing: run 5, launch 6, work 15 + 15 + 5-10, sharing in what is left of 60 ---
for last in (5, 10):
    work = 15 + 15 + last
    assert 35 <= work <= 40 and 5 + 6 + work <= 60 - 4
print('PASS: timing; 35-40 working minutes leave at least four minutes to share.')

# --- student wording: the caption and the trimmed Grades 2-3 P6 ---
assert "self.text(3.40, 2.28, 4.1, 'One nested row.', size=12)" in (week / 'figures.py').read_text()
p6 = (week / 'problems' / '12-23-sixteen-search.md').read_text()
assert 'Explain why you think it is best' not in p6 and 'Find the largest collection you can.' in p6
print('PASS: student wording; "One nested row." caption, Grades 2-3 P6 trimmed.')
