"""Independent check of the Week 45 bonus companion (3 problems) and its
facilitator guide, by exact enumeration of every equally likely history.

The P1 cards (face colours and L/R order) are read from pdf_geometry.json
(the token rows extracted from the delivered bonus PDF).  The guide's claims
are read from the delivered guide PDF.  Output saved as check_bonus.out.
"""
import json
import os
import re
import sys
from fractions import Fraction as F
from itertools import product

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, PDFS, Log  # noqa: E402

log = Log()
geo = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))
guide = ''.join(p.get_text() for p in pymupdf.open(PDFS['bonus-guide']))
g = re.sub(r'\s+', ' ', guide)

# ------------------------------------------------------------------ P1: same card, two clues
tok = geo['bonus']['pages'][0]['tokens']
rows = {}
for t in tok:
    y = round((t['rect'][1] + t['rect'][3]) / 2)
    rows.setdefault(y, []).append(t)
card_rows = [sorted(v, key=lambda t: t['rect'][0]) for k, v in sorted(rows.items())][1:]
CARDS = {''.join(t['label'][0] for t in r): {'L': r[0]['label'][0], 'R': r[1]['label'][0]} for r in card_rows}
log.note(f'P1 cards read from the PDF table (L face, R face): {CARDS}')
log.check(list(CARDS) == ['RR', 'RB', 'BB'], 'P1: cards RR, RB, BB with RB showing R on its L face')

hist = [(c, a, b) for c in CARDS for a in 'LR' for b in 'LR']
log.check(len(hist) == 12, 'P1: 3 cards x 2 x 2 face tickets = 12 equally likely histories')


def post(clues):
    ws = {}
    for c, a, b in hist:
        if (CARDS[c][a], CARDS[c][b]) == clues:
            ws[c] = ws.get(c, 0) + 1
    tot = sum(ws.values())
    return {c: F(n, tot) for c, n in ws.items()}, ws


p_rr, w_rr = post(('R', 'R'))
p_rb, w_rb = post(('R', 'B'))
p_br, _ = post(('B', 'R'))
p_bb, w_bb = post(('B', 'B'))
log.check(w_rr == {'RR': 4, 'RB': 1} and p_rr['RR'] == F(4, 5), f'P1: red,red -> {w_rr}, RR best at 4/5')
log.check(p_rb == {'RB': 1}, 'P1: red,blue -> RB certain (only RB with L then R)')
log.check(p_br == {'RB': 1} and w_bb == {'BB': 4, 'RB': 1} and p_bb['BB'] == F(4, 5),
          'guide: blue,red forces RB; blue,blue gives BB 4/5')
one = {}
for c in CARDS:
    for a in 'LR':
        if CARDS[c][a] == 'R':
            one[c] = one.get(c, 0) + 1
log.check(F(one['RR'], sum(one.values())) == F(2, 3), 'guide: one red clue alone gives RR 2/3')
# knowing L then L
ll = {c: 1 for c, a, b in hist if a == b == 'L' and (CARDS[c]['L'], CARDS[c]['L']) == ('R', 'R')}
log.check(ll == {'RR': 1, 'RB': 1}, 'guide: knowing the clues came from L then L would change the retained space (RR 1/2)')
# fresh card per clue is different
fresh = {}
for c1, a, c2, b in product(CARDS, 'LR', CARDS, 'LR'):
    if CARDS[c1][a] == 'R' and CARDS[c2][b] == 'R':
        fresh[c1] = fresh.get(c1, 0) + 1
log.note(f'fresh card per clue (first card | red,red): {fresh} -> P(first card RR) = {F(fresh["RR"], sum(fresh.values()))}, not 4/5')
# guide grid
grid = re.search(r'Card L,L L,R R,L R,R (.*?) Each face ticket', g).group(1).split()
want = []
for c in CARDS:
    want.append(c)
    for a, b in [('L', 'L'), ('L', 'R'), ('R', 'L'), ('R', 'R')]:
        want.append(CARDS[c][a] + CARDS[c][b])
log.check(grid == want, f'guide P1 grid {grid} matches enumeration')
# extension n red clues
ok = True
for n in range(1, 9):
    ws = {}
    for c in CARDS:
        for seq in product('LR', repeat=n):
            if all(CARDS[c][s] == 'R' for s in seq):
                ws[c] = ws.get(c, 0) + 1
    ok &= F(ws['RR'], sum(ws.values())) == F(2 ** n, 2 ** n + 1)
    for seq_col in product('RB', repeat=n):
        if 'R' in seq_col and 'B' in seq_col:
            cs = {c for c in CARDS for seq in product('LR', repeat=n) if tuple(CARDS[c][s] for s in seq) == seq_col}
            ok &= cs == {'RB'}
log.check(ok, 'guide P1 extension: n red clues -> RR 2^n/(2^n+1); mixed colours force RB (n = 1..8)')
m = re.search(r'There are (\S+)=12 equally likely histories', g)
log.check(m is not None and m.group(1) in ('3×2×2', '3·2·2', '3·2²', '3×2²'),
          f'guide overview: history-count expression printed as "{m.group(1) if m else None}=12" '
          '(should be a product equal to 12; source guide.md has 3*2*2=12 and the renderer turns *2* into italics)')

# ------------------------------------------------------------------ P2: two hosts
H = [(p, t) for p in (1, 2, 3) for t in (2, 3)]


def host_a(p, t, tie_rule='ticket'):
    empt = [d for d in (2, 3) if d != p]
    if len(empt) == 1:
        return empt[0]
    return t if tie_rule == 'ticket' else 2


def host_b(p, t):
    return None if t == p else t


def other(opened):
    return ({2, 3} - {opened}).pop()


A = [(p, t, host_a(p, t), other(host_a(p, t)) == p) for p, t in H]
B = [(p, t, host_b(p, t), None if host_b(p, t) is None else other(host_b(p, t)) == p) for p, t in H]
log.note(f'P2 Host A (prize, ticket, opens, switch wins): {A}')
log.note(f'P2 Host B (prize, ticket, opens, switch wins/None=discard): {B}')
log.check(all(o != 1 and o != p for p, t, o, _ in A), 'P2: Host A always opens an unchosen empty door')
log.check(F(sum(w for *_, w in A), 6) == F(2, 3), 'P2: Host A switch wins 4/6 = 2/3')
kept = [r for r in B if r[2] is not None]
log.check(len(kept) == 4 and F(sum(r[3] for r in kept), 4) == F(1, 2), 'P2: Host B keeps 4 histories, switch wins 2/4 = 1/2')
log.check(F(sum(1 for r in B if r[3]), 6) == F(2, 6) and F(sum(1 for r in B if r[2] is None), 6) == F(2, 6),
          'guide: before conditioning, blind switching wins 2/6 with 2/6 discarded')
gt = re.findall(r'(\d) (\d) (\d) (stay|switch) (\d) (stay|switch|discard)', g)
exp = [(str(p), str(t), str(a[2]), 'switch' if a[3] else 'stay', str(t), 'discard' if b[2] is None else ('switch' if b[3] else 'stay'))
       for (p, t), a, b in zip(H, A, B)]
log.check(gt == exp, f'guide P2 table matches enumeration ({len(gt)} rows)')
for door in (2, 3):
    a = [r for r in A if r[2] == door]
    b = [r for r in kept if r[2] == door]
    log.note(f'P2 door {door} opened: Host A switch {F(sum(r[3] for r in a), len(a))}, Host B switch {F(sum(r[3] for r in b), len(b))}')
a3 = [r for r in A if r[2] == 3]
b3 = [r for r in kept if r[2] == 3]
log.check(F(sum(r[3] for r in a3), len(a3)) == F(2, 3) and [r[0] for r in a3].count(1) == 1 and [r[0] for r in a3].count(2) == 2
          and F(sum(r[3] for r in b3), len(b3)) == F(1, 2),
          'guide P2 extension: door 3 opened -> A: prize 1 one history, prize 2 two (2/3); B: one each (1/2)')
A2 = [(p, t, host_a(p, t, 'always2'), other(host_a(p, t, 'always2')) == p) for p, t in H]
over = F(sum(r[3] for r in A2), 6)
d2 = [r for r in A2 if r[2] == 2]
d3 = [r for r in A2 if r[2] == 3]
log.check(over == F(2, 3), f'guide P2 extension: tie rule "always open 2" keeps overall switch rate 2/3 '
                           f'(door 2 opened: {F(sum(r[3] for r in d2), len(d2))}; door 3 opened: {F(sum(r[3] for r in d3), len(d3))})')

# ------------------------------------------------------------------ P3: noisy reporter
counters = ['R1', 'R2', 'R3', 'B']
tickets = ['H1', 'H2', 'F']


def report(c, t):
    col = c[0]
    return col if t.startswith('H') else ('B' if col == 'R' else 'R')


rep = {(c, t): report(c, t) for c in counters for t in tickets}
blue = [(c, t) for (c, t), r in rep.items() if r == 'B']
red = [(c, t) for (c, t), r in rep.items() if r == 'R']
nb_r = sum(1 for c, t in blue if c[0] == 'R')
log.check(len(blue) == 5 and nb_r == 3, f'P3: blue report has 5 histories, 3 hide red -> red better at {F(nb_r, len(blue))}')
log.check(F(sum(1 for c, t in red if c[0] == 'R'), len(red)) == F(6, 7), 'guide: red report gives red 6/7')
log.check(F(sum(1 for (c, t) in rep if t != 'F'), 12) == F(2, 3), 'guide: reporter honest in 2/3 of rounds')
gt3 = re.search(r'Counter H1 H2 F (.*?) For guessing', g).group(1).split()
exp3 = []
for c in counters:
    exp3 += [c] + [rep[(c, t)] for t in tickets]
log.check(gt3 == exp3, f'guide P3 report table matches {gt3}')
sols = []
for kinds in product('HF', repeat=4):
    br = sum(1 for c in counters for k in kinds if c[0] == 'R' and k == 'F')
    bb = sum(1 for c in counters for k in kinds if c[0] == 'B' and k == 'H')
    if br == bb and br > 0:
        sols.append(''.join(kinds))
log.check(sorted(sols) == sorted(['FHHH', 'HFHH', 'HHFH', 'HHHF']),
          f'P3 redesign: four-ticket sets giving a blue-report tie: {sols} (exactly three honest, one flip; any placement)')
log.check(all((h == 3) == (3 * (4 - h) == h) for h in range(5)), 'guide: h for blue vs 3(4-h) for red tie exactly at h=3')
ok = True
for r_, b_, h, f in product(range(0, 5), range(0, 5), range(0, 5), range(0, 5)):
    if h + f == 0 or r_ + b_ == 0:
        continue
    cs = ['R%d' % i for i in range(r_)] + ['B%d' % i for i in range(b_)]
    ts = ['H%d' % i for i in range(h)] + ['F%d' % i for i in range(f)]
    hid = [c[0] for c in cs for t in ts if report(c, t) == 'B']
    balanced = hid.count('R') == hid.count('B') and len(hid) > 0
    ok &= balanced == (b_ * h == r_ * f and b_ * h > 0)
log.check(ok, 'guide extension: blue report balanced <=> b*h = r*f (>0), by enumerating histories for r,b,h,f <= 4')
perfect = {c[0] for c in counters if report(c, 'H1') == 'B'}
zero = {c[0] for c in counters if report(c, 'F') == 'B'}
log.check(perfect == {'B'} and zero == {'R'}, 'guide: perfect reporter -> blue report means blue for certain; zero-honesty -> opposite colour for certain')

# ------------------------------------------------------------------ materials arithmetic in the guide
per_kit = {'card-choice': 3, 'face': 2, 'prize': 3, 'host': 2, 'reporter': 3, 'blank': 1}
log.check(sum(per_kit.values()) == 14 and 'fourteen equal-size paper tickets' in g, 'guide: 3+2+3+2+3+1 = 14 tickets per kit')
log.check(5 * 14 == 70 and 'seventy tickets' in g and 5 * 4 == 20 and 'twenty two-sided cards (five are non-task' in g
          and 5 * 3 == 15 and 'fifteen doors' in g and 5 * 4 == 20 and 'twenty source counters' in g
          and 5 * 2 == 10 and 'ten cups' in g, 'guide: five-kit totals (70 tickets, 20 cards incl. 5 GB demos, 15 doors, 20 counters, 10 cups)')

log.summary()
