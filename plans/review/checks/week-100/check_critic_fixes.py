"""Check of the Week 100 critic follow-up, October 23, 2026 (W100-G35-v3).

Critic B's could: Problem 4 asked "Could loops around different sets of cards fit the same ten
clues?", but the packet's word (p. 1 rules) is "group". v3 asks "Could a world with different
groups fit the same ten clues?". The guide's answer is unchanged: the clues determine the
groups (AB at 2, ABC at 4, DE at 2, all five at 8), and an extra loop around the same cards as
another, or around one card, changes no distance.

Run: python3 check_critic_fixes.py (writes out_check_critic_fixes.txt beside itself).
"""
import os
import re
from itertools import combinations

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
W = os.path.join(ROOT, 'lowell-math-circle-year-2/week-100')
ARC = os.path.join(W, 'archive-before-critic-fixes-2026-10-23')
OUT = []


def ok(cond, msg):
    if not cond:
        raise SystemExit('FAIL ' + msg)
    OUT.append('ok   ' + msg)


def flat(p):
    return re.sub(r'\s+', ' ', p.get_text()).replace('’', "'")


S, SO = pymupdf.open(os.path.join(W, 'week-100-grades-3-5.pdf')), pymupdf.open(os.path.join(ARC, 'week-100-grades-3-5.pdf'))
ok(len(S) == len(SO) == 8, 'packet still 8 pages')
p1, p4 = flat(S[0]), flat(S[3])
rules = p1.split('Problem 1:')[0]
ok(rules.count('group') + rules.count('Group') >= 5 and 'loop' not in rules.lower(),
   'p. 1 rules define "groups"; "loops" are the physical objects in the problems')
ok('Draw your world. Could a world with different groups fit the same ten clues?' in p4 and 'sets of cards' not in p4,
   'p. 4, Problem 4: "Could a world with different groups fit the same ten clues?"')
for i in range(8):
    ok('W100-G35-v3' in S[i].get_text(), f'p. {i + 1}: footer W100-G35-v3')
    old = flat(SO[i]).replace('W100-G35-v2', 'W100-G35-v3')
    if i == 3:
        old = old.replace('Could loops around different sets of cards fit the same ten clues?', 'Could a world with different groups fit the same ten clues?')
    ok(old == flat(S[i]), f'p. {i + 1}: text unchanged apart from the footer' + (' and that question' if i == 3 else ''))
    if i != 3:
        a = SO[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, S[i].rect.width, S[i].rect.height - 40)).samples
        b = S[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, S[i].rect.width, S[i].rect.height - 40)).samples
        ok(a == b, f'p. {i + 1}: pixels above the footer unchanged')

# The clues printed on p. 4 determine the groups.
clues = dict(re.findall(r'([A-E]–[A-E]) = (\d)', p4))
ok(len(clues) == 10, 'p. 4 prints ten clue cards')
d = {tuple(k.split('–')): int(v) for k, v in clues.items()}
dist = lambda x, y: 0 if x == y else d.get((x, y), d.get((y, x)))
cards = 'ABCDE'
ok(all(dist(x, z) <= max(dist(x, y), dist(y, z)) for x in cards for y in cards for z in cards),
   'the ten clues are ultrametric (every triangle has its two largest distances equal)')
groups = set()
for t in sorted(set(d.values())):
    parts = []
    for c in cards:
        for part in parts:
            if dist(c, part[0]) <= t:
                part.append(c)
                break
        else:
            parts.append([c])
    groups |= {(''.join(p), t) for p in parts if len(p) > 1}
smallest = {}
for g, t in sorted(groups, key=lambda x: x[1]):
    smallest.setdefault(g, t)
ok(smallest == {'AB': 2, 'DE': 2, 'ABC': 4, 'ABCDE': 8}, f'the clues force the groups {smallest}, the guide\'s answer')
G = open(os.path.join(W, 'week-100-facilitator.pdf'), 'rb').read()
ok(G == open(os.path.join(ROOT, 'lowell-math-circle-year-2/source/week-100/reference-pdfs/week-100-facilitator.pdf'), 'rb').read()
   and "The final question's answer is no." in ' '.join(flat(p) for p in pymupdf.open(os.path.join(W, 'week-100-facilitator.pdf'))),
   'guide unchanged (W100-FAC-v2); its answer to the final question still applies')

print('\n'.join(OUT))
print(f'{len(OUT)} checks passed')
with open(os.path.join(HERE, 'out_check_critic_fixes.txt'), 'w') as f:
    f.write('\n'.join(OUT) + f'\n{len(OUT)} checks passed\n')
