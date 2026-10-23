"""Check of the Week 44 critic follow-up, October 23, 2026 (W44-grades-2-3-v4 and the guide).

Critic B's coulds: Grades 2-3 Problem 6 asked "which bag is more likely: ... or ...?" while the
two bags are equally likely, so v4 asks "which bag is more likely, if either". The route note's
random games (about ten copying and ten return-only two-draw games per pair) had no time on
page 2's timeline, and a small pooled chart often fails to show the pattern; the guide now gives
them about 15 minutes and says a chart of 20 pooled games of each kind shows fewer two-red,
two-blue bags for copying than for returning only about four times in five.

Enumerates marked histories for the exact answers, computes the chart probability exactly,
then reads the delivered PDFs (current and archived).
Run: python3 check_critic_fixes.py (writes out_check_critic_fixes.txt beside itself).
"""
import os
import re
from fractions import Fraction as F
from math import comb

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
W = os.path.join(ROOT, 'lowell-math-circle-year-2/week-44')
ARC = os.path.join(W, 'archive-before-critic-fixes-2026-10-23')
REF = os.path.join(ROOT, 'lowell-math-circle-year-2/source/week-44/editable/reference-pdfs')
OUT = []


def ok(cond, msg):
    if not cond:
        raise SystemExit('FAIL ' + msg)
    OUT.append('ok   ' + msg)


# ---------------------------------------------------------------- the mathematics
def finals(draws):
    """Final (red, blue) of every marked history: each draw picks one of the counters present."""
    out = {}

    def go(r, b, k):
        if k == 0:
            out[(r, b)] = out.get((r, b), 0) + 1
            return
        for _ in range(r):
            go(r + 1, b, k - 1)
        for _ in range(b):
            go(r, b + 1, k - 1)
    go(1, 1, draws)
    return out


f4 = finals(4)
total = sum(f4.values())
ok(total == 120 and f4[(5, 1)] == f4[(3, 3)] == 24, f'four draws: 120 marked histories, 24 end 5R/1B and 24 end 3R/3B, so neither bag is more likely (1/5 each)')
ok(set(f4.values()) == {24}, 'four draws: every final bag from 5R/1B to 1R/5B has 24 histories (the uniform law)')
f2 = finals(2)
ok(f2 == {(3, 1): 2, (2, 2): 2, (1, 3): 2}, 'two copying draws: 3R/1B, 2R/2B, 1R/3B each from 2 of 6 histories (1/3)')
ret = {k: comb(2, k) for k in range(3)}  # return only: red draws 0, 1, 2 of 4 equally likely words
ok(ret == {0: 1, 1: 2, 2: 1}, 'two return-only draws: one red draw in 2 of 4 words (1/2)')


def p_fewer(n, p=F(1, 3), q=F(1, 2)):
    b = lambda n, p, k: comb(n, k) * p ** k * (1 - p) ** (n - k)
    return sum(b(n, p, x) * b(n, q, y) for x in range(n + 1) for y in range(x + 1, n + 1))


chances = {n: float(p_fewer(n)) for n in (10, 20, 30)}
ok(0.78 < chances[20] < 0.85, f'20 pooled games of each kind: copying shows fewer middle bags than returning with chance {chances[20]:.3f}, "about four times in five"')
ok(chances[10] < chances[20] < chances[30], f'the chance grows with the chart: {chances[10]:.3f} at 10, {chances[30]:.3f} at 30')

# ---------------------------------------------------------------- the delivered pages


def flat(p):
    return re.sub(r'\s+', ' ', p.get_text()).replace('’', "'")


S, SO = pymupdf.open(os.path.join(W, 'week-44-grades-2-3.pdf')), pymupdf.open(os.path.join(ARC, 'week-44-grades-2-3.pdf'))
ok(len(S) == len(SO) == 5, 'Grades 2-3: still 5 pages')
old_q = 'which bag is more likely: five red and one blue, or three red and three blue?'
new_q = 'which bag is more likely, if either: five red and one blue, or three red and three blue?'
ok(new_q in flat(S[4]) and old_q in flat(SO[4]), 'Grades 2-3 p. 5, Problem 6: "which bag is more likely, if either"')
for i in range(5):
    ok('W44-grades-2-3-v4' in S[i].get_text(), f'Grades 2-3 p. {i + 1}: footer W44-grades-2-3-v4')
    old = flat(SO[i]).replace('W44-grades-2-3-v3', 'W44-grades-2-3-v4').replace(old_q, new_q)
    ok(old == flat(S[i]), f'Grades 2-3 p. {i + 1}: text unchanged apart from the footer' + (' and that question' if i == 4 else ''))
    if i < 4:
        a = SO[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 740)).samples
        b = S[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 740)).samples
        ok(a == b, f'Grades 2-3 p. {i + 1}: pixels above the footer unchanged')
for band in ('k-1', 'grades-4-5'):
    a = open(os.path.join(W, f'week-44-{band}.pdf'), 'rb').read()
    ok(a == open(os.path.join(REF, f'{band}.pdf'), 'rb').read() and f'W44-{band}-v3' in pymupdf.open(os.path.join(W, f'week-44-{band}.pdf'))[0].get_text(),
       f'{band} packet unchanged (v3), equal to its reference copy')
for name, ref in (('grades-2-3', 'grades-2-3'), ('facilitator', 'facilitator-guide')):
    ok(open(os.path.join(W, f'week-44-{name}.pdf'), 'rb').read() == open(os.path.join(REF, f'{ref}.pdf'), 'rb').read(),
       f'{name}: print copy equals the reference copy')

# The critic follow-up's guide was replaced later on October 23 when could 14's timeline was made
# (guide p. 2 only); it is archived in archive-before-small-coulds-2026-10-23/, checked here, and
# the current guide is compared with it at the end.
SC = os.path.join(W, 'archive-before-small-coulds-2026-10-23')
G, GO = pymupdf.open(os.path.join(SC, 'week-44-facilitator.pdf')), pymupdf.open(os.path.join(ARC, 'week-44-facilitator.pdf'))
ok(len(G) == len(GO) == 6, 'guide: still 6 pages')
g2, g6 = flat(G[1]), flat(G[5])
ok('7-22: choose short stories and compare final bags; the random games on page 6 add about 15 minutes.' in g2,
   'guide p. 2: the timeline gives the random games about 15 minutes')
ok('The games take about 15 minutes. A chart of 20 pooled games of each kind shows fewer two-red, two-blue bags for copying than for returning only about four times in five, so a chart that does not is ordinary chance; the exact count decides.' in g6,
   'guide p. 6: the games\' time and what a small pooled chart can show')
ok(flat(GO[1]).replace('compare final bags.', 'compare final bags; the random games on page 6 add about 15 minutes.') == g2,
   'guide p. 2: text otherwise unchanged')
for i in (0, 2, 3, 4):
    ok(flat(GO[i]) == flat(G[i]), f'guide p. {i + 1}: text unchanged')
    a = GO[i].get_pixmap(dpi=100).samples
    b = G[i].get_pixmap(dpi=100).samples
    ok(a == b, f'guide p. {i + 1}: pixels unchanged')
key = ' '.join(flat(p) for p in G)
ok('P6' in key and ('Neither' in key or 'neither' in key), "guide: the Problem 6 key still answers neither")

# ---------------------------------------------------------------- later the same day: could 14's timeline
GC = pymupdf.open(os.path.join(W, 'week-44-facilitator.pdf'))
ok(len(GC) == 6, 'current guide: 6 pages')
old_t = ('0-7 minutes: handle counters and demonstrate returning plus copying. 7-22: choose short stories and compare final bags; '
         'the random games on page 6 add about 15 minutes. 22-34: K-1 extends or reverses stories; older groups construct the six '
         'marked two-draw histories. 34-37: movement break: one child is the original counter, another joins as its copy. 37-50: '
         'compare return-only sampling or investigate three/four draws. 50-58: share an exact count or an invariant. 58-60: restore the starting kits.')
new_t = ('0-5 minutes: running around. 5-10: handle counters and demonstrate returning plus copying. 10-22: choose short stories and compare final bags; '
         'the random games on page 6 add about 15 minutes. 22-33: K-1 extends or reverses stories; older groups construct the six '
         'marked two-draw histories. 33-35: movement break: one child is the original counter, another joins as its copy. 35-47: '
         'compare return-only sampling or investigate three/four draws. 47-53: share an exact count or an invariant with the group. 53-56: restore the starting kits.')
ok(old_t in g2 and flat(GC[1]) == g2.replace(old_t, new_t), 'current guide p. 2: only the flexible hour changed, retimed to running around, about 37 minutes at the tables and sharing')
for i in (0, 2, 3, 4, 5):
    ok(G[i].get_pixmap(dpi=100).samples == GC[i].get_pixmap(dpi=100).samples, f'current guide p. {i + 1}: pixels unchanged')

print('\n'.join(OUT))
print(f'{len(OUT)} checks passed')
with open(os.path.join(HERE, 'out_check_critic_fixes.txt'), 'w') as f:
    f.write('\n'.join(OUT) + f'\n{len(OUT)} checks passed\n')
