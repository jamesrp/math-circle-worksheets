"""Independent check of the Week 30 bonus companion (week-30-bonus.pdf) and its
adult guide (week-30-bonus-facilitator.pdf).

Reads the P1 table, card strips, the search example, the P6 kits and their
team trays from the student PDF; reads the guide text; then solves every
problem: robust kits (all triples, with and without the 1-8 cap, with and
without equal-valued cards), the threshold-comparison search bound by
dynamic programming over every plan, and equal-team partitions.
Output: check_bonus.out
"""
import os
import re
import sys
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import PDF, reachable, ways, show_way, Log  # noqa: E402

L = Log('check_bonus.out')
doc = pymupdf.open(PDF['BON'])
TXT = [p.get_text() for p in doc]
G = pymupdf.open(PDF['BGUIDE'])
GT = re.sub(r'\s+', ' ', '\n'.join(p.get_text() for p in G))


def ghas(s):
    return re.sub(r'\s+', ' ', s) in GT


def boxes(page, wmin=30, wmax=200):
    out = []
    for d in page.get_drawings():
        r = d['rect']
        if d['type'] == 's' and [i[0] for i in d['items']] == ['l'] * 4 and wmin < r.width < wmax:
            out.append(r)
    return out


def labels_in(page, rects):
    words = page.get_text('words')
    out = []
    for r in sorted(rects, key=lambda r: (round(r.y0), r.x0)):
        ws = [w[4] for w in words if r.x0 < (w[0] + w[2]) / 2 < r.x1 and r.y0 < (w[1] + w[3]) / 2 < r.y1]
        out.append(' '.join(ws))
    return out


# ------------------------------------------------------------ P1
L.out('== P1: kit 1,2,3, one weight removed, targets 1,2,3')
p1 = doc[0]
cards = labels_in(p1, [r for r in boxes(p1, 30, 60) if r.height < 30])
L.ok(cards == ['1', '2', '3'], f'P1 cards {cards}')
ws1 = p1.get_text('words')
hdr = [w for w in ws1 if w[4] == 'Removed'][0]
rem_col = [w for w in ws1 if w[1] > hdr[3] and w[0] < 192 and w[4].isdigit()]
tgt_col = [w for w in ws1 if w[1] > hdr[3] and 192 < w[0] < 237 and w[4].isdigit()]
rows = [(a[4], b[4]) for a, b in zip(sorted(rem_col, key=lambda w: w[1]), sorted(tgt_col, key=lambda w: w[1]))]
L.ok(rows == [(str(a), str(b)) for a in (1, 2, 3) for b in (1, 2, 3)], f'P1 table rows (removed, target): {len(rows)} rows')
for rem in (1, 2, 3):
    kit = [w for w in (1, 2, 3) if w != rem]
    for t in (1, 2, 3):
        ws = ways(kit, t)
        L.ok(len(ws) > 0, f'removed {rem}, kit {kit}, target {t}: ' + '; '.join(show_way(t, *w) for w in ws))
for eq, kit in (('1+2=3', [2, 3]), ('2+1=3', [1, 3]), ('3=1+2', [1, 2])):
    l, r = eq.split('=')
    lv = [int(x) for x in l.split('+')]
    rv = [int(x) for x in r.split('+')]
    L.ok(sum(lv) == sum(rv) and all(x in kit for x in lv[1:] + rv), f'guide P1 balance "{eq}" uses only {kit}')

# ------------------------------------------------------------ P2, P3
L.out('\n== P2/P3: kits that survive any one removal')
p2 = doc[1]
strip = labels_in(p2, [r for r in boxes(p2, 30, 60) if r.height < 30])
L.ok(strip == [str(i) for i in range(1, 9)], f'P2 card strip {strip}')


def covers(kit, top):
    r = set(reachable(list(kit)))
    return all(t in r for t in range(1, top + 1))


def robust(kit, top):
    return all(covers([w for j, w in enumerate(kit) if j != i], top) for i in range(len(kit)))


pairs3 = [(a, b) for a in range(1, 201) for b in range(a, 201) if covers((a, b), 3)]
L.ok(pairs3 == [(1, 2), (1, 3), (2, 3)], f'pairs (<=200, equal values allowed) covering 1..3: {pairs3}')
pairs4 = [(a, b) for a in range(1, 201) for b in range(a, 201) if covers((a, b), 4)]
L.ok(pairs4 == [(1, 3)], f'pairs (<=200, equal values allowed) covering 1..4: {pairs4}')
r8 = [k for k in combinations(range(1, 9), 3) if robust(k, 3)]
L.ok(r8 == [(1, 2, 3)], f'P2 robust triples of different weights from 1..8: {r8}')
r60 = [k for k in combinations(range(1, 61), 3) if robust(k, 3)]
L.ok(r60 == [(1, 2, 3)], f'P2 without the cap (weights <= 60): {r60}')
r60m = [k for k in combinations_with_replacement(range(1, 61), 3) if robust(k, 3)]
L.ok(r60m == [(1, 2, 3)], f'P2 with equal-valued cards allowed (<= 60): {r60m}')
q60 = [k for k in combinations(range(1, 61), 3) if robust(k, 4)]
L.ok(q60 == [], f'P3 robust triples for 1..4 (different weights <= 60): {q60}')
q60m = [k for k in combinations_with_replacement(range(1, 61), 3) if robust(k, 4)]
L.ok(q60m == [], f'P3 with equal-valued cards allowed (<= 60): {q60m}')
L.out('   => allowing equal-valued cards changes neither conclusion (P2 still only {1,2,3}; P3 still impossible)')
L.ok(ghas('Ask how the conclusion changes if equal-valued cards are allowed'),
     'guide p. 2 asks "how the conclusion changes" with equal-valued cards (it does not change; see above)')
L.ok(not covers((3, 9), 1) and not covers((3, 9), 2) and 1 not in reachable([3, 9]) and 2 not in reachable([3, 9]),
     'guide: {1,3,9} minus 1 leaves 3, 9, which cannot balance 1 or 2')

# ------------------------------------------------------------ P4, P5: threshold search
L.out('\n== P4/P5: find a hidden card by comparisons with a known whole-number mass')
p3 = doc[2]
strip = labels_in(p3, [r for r in boxes(p3, 30, 60) if r.height < 30])
L.ok(strip == [str(i) for i in range(1, 8)], f'P4 card strip {strip}')
L.ok('candidates: 8, 9, 10' in TXT[2].replace('\n', ' ') or re.search(r'8,\s*9,\s*10', TXT[2]) is not None,
     'example candidates 8, 9, 10')
cand = [8, 9, 10]
heavier = [c for c in cand if c > 9]
L.ok(heavier == [10], 'example: compare with 9, heavier -> keep 10')


def split(cands, t):
    return (tuple(c for c in cands if c < t), tuple(c for c in cands if c == t), tuple(c for c in cands if c > t))


@lru_cache(maxsize=None)
def need(cands):
    """Fewest comparisons that always identify the hidden card among cands (any whole thresholds)."""
    if len(cands) <= 1:
        return 0
    best = 99
    for t in range(min(cands) - 1, max(cands) + 2):
        parts = split(cands, t)
        if max(len(p) for p in parts) == len(cands):
            continue
        best = min(best, 1 + max(need(p) for p in parts))
    return best


for n in range(1, 17):
    L.out(f'   candidates 1..{n}: {need(tuple(range(1, n + 1)))} comparisons needed')
L.ok(need(tuple(range(1, 8))) == 2 and need(tuple(range(1, 9))) == 3, 'P4 seven need 2; P5 eight need 3 (so "no")')
largest = {k: max(n for n in range(1, 40) if need(tuple(range(1, n + 1))) <= k) for k in range(0, 4)}
L.ok(largest == {k: 2 ** (k + 1) - 1 for k in range(4)}, f'largest set for k comparisons: {largest} = 2^(k+1)-1')
# non-consecutive candidate sets behave the same (only order matters)
L.ok(need((2, 5, 6, 11, 12, 30, 31)) == 2 and need((2, 5, 6, 11, 12, 30, 31, 40)) == 3, 'non-consecutive sets: same bound')


def plan4(h):
    seq = []
    seq.append(4)
    if h == 4:
        return seq, 4
    t2 = 2 if h < 4 else 6
    seq.append(t2)
    if h < t2:
        return seq, t2 - 1
    if h == t2:
        return seq, t2
    return seq, t2 + 1


L.ok(all(plan4(h)[1] == h and len(plan4(h)[0]) <= 2 for h in range(1, 8)), 'guide P4 plan (4; then 2 or 6) finds every card 1..7')
firsts = [t for t in range(0, 9) if all(need(p) <= 1 for p in split(tuple(range(1, 8)), t))]
L.ok(firsts == [4], f'P4 first thresholds that allow a two-comparison plan: {firsts}')


def plan15(h):
    cands = list(range(1, 16))
    used = 0
    while len(cands) > 1:
        t = cands[len(cands) // 2]
        used += 1
        cands = [c for c in cands if (c < t if h < t else c == t if h == t else c > t)]
    return used, cands[0]


L.ok(all(plan15(h) == (plan15(h)[0], h) and plan15(h)[0] <= 3 for h in range(1, 16)),
     'guide depth: 15 candidates in three comparisons (threshold 8, then 4 or 12, then middle)')
L.ok(ghas('compare first with 4') and ghas('If lighter, compare with 2') and ghas('If heavier than 4, compare with 6'),
     'guide P4 text matches the plan checked')

# ------------------------------------------------------------ P6, P7: equal teams
L.out('\n== P6/P7: equal-weight teams')


def partitions(items, m):
    """Unordered partitions of items into exactly m nonempty blocks with equal sums."""
    total = sum(items)
    if total % m:
        return []
    target = total // m
    items = sorted(items, reverse=True)
    res = set()

    def go(i, blocks):
        if i == len(items):
            if len(blocks) == m and all(sum(b) == target for b in blocks):
                res.add(tuple(sorted(tuple(sorted(b)) for b in blocks)))
            return
        x = items[i]
        for b in blocks:
            if sum(b) + x <= target:
                b.append(x)
                go(i + 1, blocks)
                b.pop()
        if len(blocks) < m:
            blocks.append([x])
            go(i + 1, blocks)
            blocks.pop()
    go(0, [])
    return sorted(res)


p4 = doc[3]
words = p4.get_text('words')
trays = [r for r in boxes(p4, 40, 120) if r.height > 35]
kits = []
for w in words:
    if w[4] == 'Kit':
        line = [x for x in words if (x[5], x[6]) == (w[5], w[6])]
        nums = [int(n) for n in re.findall(r'\d+', ' '.join(x[4] for x in line))]
        nt = [x for x in words if x[4] == 'teams' and 0 < x[1] - w[1] < 20]
        teams_n = int([x for x in words if (x[5], x[6]) == (nt[0][5], nt[0][6])][0][4])
        ntray = len([r for r in trays if r.y0 - 5 < w[1] < r.y1 + 5])
        kits.append((nums, teams_n, ntray))
for nums, m, ntray in kits:
    ps = partitions(nums, m)
    L.out(f'P6 kit {nums} into {m} teams ({ntray} trays printed): {len(ps)} partition(s) {ps}')
    L.ok(ntray == m, f'   trays printed = teams requested ({ntray} = {m})')
expect = {(1, 2, 3, 4): 1, (1, 2, 3, 4, 5, 6): 1, (1, 2, 5): 0, (1, 2, 3, 4, 5, 6, 7, 8): 1}
L.ok({tuple(n): len(partitions(n, m)) for n, m, _ in kits} == expect, 'P6 counts: 1, 1, impossible, 1')
L.ok(sum([1, 2, 5]) % 2 == 0 and partitions([1, 2, 5], 2) == [], 'P6 {1,2,5}: total even yet impossible (5 > 4)')
p7 = partitions([1, 2, 3, 4, 5, 6], 3)
L.ok(p7 == [((1, 6), (2, 5), (3, 4))], f'P7 every split of 1..6 into three equal teams: {p7}')
for r in range(1, 7):
    items = list(range(1, 2 * r + 1))
    L.ok(((tuple((i, 2 * r + 1 - i) for i in range(1, r + 1))) in
          [tuple(sorted(p)) for p in partitions(items, r)]), f'endpoint pairing 1..{2 * r} into {r} teams of {2 * r + 1}')
# divisors of r: combine pairs
okc = True
for r in range(1, 7):
    for m in range(1, r + 1):
        if r % m == 0 and not partitions(list(range(1, 2 * r + 1)), m):
            okc = False
L.ok(okc, 'guide depth: if m divides r, 1..2r splits into m equal teams (r <= 6)')
L.save()
