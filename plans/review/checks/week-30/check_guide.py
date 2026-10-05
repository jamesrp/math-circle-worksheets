"""Independent check of the Week 30 base adult guide (week-30-facilitator.pdf).

Reads the guide text from the delivered PDF, parses the small-kit key, the
K-1 P1/P4 lists and the Grades 2-3 P2 balance table, and checks every answer,
proof step, general claim and extension against my own enumeration.
Output: check_guide.out
"""
import os
import re
import sys
from itertools import combinations_with_replacement, product

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import PDF, reachable, ways, run_length, first_miss, placements, Log  # noqa: E402

L = Log('check_guide.out')
doc = pymupdf.open(PDF['GUIDE'])
T = [p.get_text() for p in doc]
ALL = '\n'.join(T)
flat = re.sub(r'\s+', ' ', ALL)


def has(s):
    return re.sub(r'\s+', ' ', s) in flat


def parse_range(s):
    out = set()
    for part in re.split(r' and ', s):
        part = part.strip()
        m = re.fullmatch(r'(\d+) through (\d+)', part) or re.fullmatch(r'(\d+)\.\.\.(\d+)', part)
        if m:
            out |= set(range(int(m.group(1)), int(m.group(2)) + 1))
        else:
            out |= {int(x) for x in part.split(',')}
    return out


def check_eq(eq, kit, target=None):
    """'5+3+1 = 9' -> left list (first = target), right list; every weight from kit, each at most once."""
    l, r = eq.split('=')
    left = [int(x) for x in l.split('+')]
    right = [int(x) for x in r.split('+')]
    t = left[0]
    used = left[1:] + right
    okk = sum(left) == sum(right) and sorted(used) == sorted(set(used)) and all(u in kit for u in used)
    if target is not None:
        okk = okk and t == target
    return okk, t


# ------------------------------------------------------------ overview
L.out('== Overview (guide p. 1)')
for m in range(1, 8):
    kit = [3 ** i for i in range(m)]
    end = (3 ** m - 1) // 2
    vals = [v for _, v in placements(kit)]
    L.ok(run_length(kit) == end and sorted(vals) == list(range(-end, end + 1)),
         f'balanced ternary m={m}: {kit[:4]}{"..." if m > 4 else ""} covers 1..{end}, all 3^m placements distinct')
L.ok(has('the endpoints are 4,13,40,121') and [(3 ** m - 1) // 2 for m in (2, 3, 4, 5)] == [4, 13, 40, 121],
     'endpoints 4, 13, 40, 121 for m = 2..5')
# optimality: exhaustive for small m and bounded weights (the counting argument itself is general)
for m, cap in ((1, 60), (2, 60), (3, 40), (4, 25)):
    best = max(len(reachable(list(k))) for k in combinations_with_replacement(range(1, cap + 1), m))
    L.ok(best == (3 ** m - 1) // 2,
         f'optimality m={m}, weights 1..{cap} (repeats allowed): max distinct positive targets {best}')
# why powers of three: S from the m-kit; W = 2S+1 vs heavier / lighter
for m in range(1, 5):
    kit = [3 ** i for i in range(m)]
    S = sum(kit)
    W = 2 * S + 1
    good = run_length(kit + [W]) == 3 * S + 1 and all(len(ways(kit + [W], t)) == 1 for t in range(1, 3 * S + 2))
    heavy = all(first_miss(kit + [W + d]) == S + 1 for d in range(1, 6))
    light = all(run_length(kit + [W - d]) < 3 * S + 1 for d in range(1, W))
    L.ok(good and heavy and light,
         f'S={S}: adding {W} covers -(3S+1)..3S+1 uniquely; heavier misses S+1={S + 1}; lighter falls short')

# ------------------------------------------------------------ small-kit key (p. 2)
L.out('\n== Small-kit key (guide p. 2)')
rows = re.findall(r'\n(1,\d(?:,\d+)?)\n([^\n]+)\n([^\n]+)', T[1])
L.ok(len(rows) == 6, f'parsed {len(rows)} table rows')
for kit_s, targ, reason in rows:
    kit = [int(x) for x in kit_s.split(',')]
    claim = parse_range(targ)
    L.ok(claim == set(reachable(kit)), f'kit {kit_s}: guide "{targ}" vs computed {reachable(kit)}')
L.ok(sorted({8 + v for _, v in placements([1, 3])}) == list(range(4, 13)), '1,3,8 reason: 8 + (-4..4) = 4..12')
L.ok(sorted({9 + v for _, v in placements([1, 3])}) == list(range(5, 14)), '1,3,9 reason: 9 + (-4..4) = 5..13')
L.ok(min(10 + v for _, v in placements([1, 3])) == 6, '1,3,10 reason: new interval starts at 6')

# ------------------------------------------------------------ K-1 key
L.out('\n== K-1 answer key (guide p. 2)')
for eq, t in (('1=1', 1), ('2+1=3', 2), ('3=3', 3), ('4=1+3', 4)):
    L.ok(has(eq) and check_eq(eq, [1, 3], t)[0], f'P1 "{eq}" valid with kit 1,3')
L.ok(has('Exactly 1,2,3 work with 1 and 2; 4 and 5 exceed their total weight 3.')
     and [t for t in range(1, 6) if t in reachable([1, 2])] == [1, 2, 3], 'P2')
L.ok(has('each kit reaches four of 1-6. The 1/4 kit reaches 1,3,4,5; the 1/3 kit reaches 1,2,3,4.')
     and [t for t in range(1, 7) if t in reachable([1, 4])] == [1, 3, 4, 5]
     and [t for t in range(1, 7) if t in reachable([1, 3])] == [1, 2, 3, 4], 'P3 tie')
p4 = re.findall(r'\{(\d),(\d)\} → \{([\d,]+)\}', flat)
L.ok(len(p4) == 6, f'P4 parsed {len(p4)} kits')
for a, b, s in p4:
    L.ok({int(x) for x in s.split(',')} == set(reachable([int(a), int(b)])), f'P4 {{{a},{b}}} -> {{{s}}}')
L.ok(has('The 8-kit cannot reach 13 because its total is 12') and sum([1, 3, 8]) == 12, 'P5 8-kit total 12')
L.ok(has('5+4<10') and 5 not in reachable([1, 3, 10]), 'P5 10-kit misses 5')
L.ok(has('The 9-kit constructions are on the next page') and 'Balanced pans' in T[2],
     'P5 cross-reference: table on guide p. 3')

# ------------------------------------------------------------ Grades 2-3 key
L.out('\n== Grades 2-3 answer key (guide p. 3)')
L.ok(has('Use the small-kit table on page 2') and 'Small-kit key' in T[1], 'P1 cross-reference to p. 2')
eqs = re.findall(r'\n(\d+)\n(\d+(?:\+\d+)* = \d+(?:\+\d+)*)', T[2])
L.ok(len(eqs) == 13 and sorted(int(t) for t, _ in eqs) == list(range(1, 14)),
     f'P2 table rows: {len(eqs)} (targets 1..13)')
for t, eq in eqs:
    okk, tt = check_eq(eq.replace(' ', ''), [1, 3, 9], int(t))
    L.ok(okk, f'P2 target {t}: "{eq}"')
L.ok([w for w in range(1, 200) if all(x in reachable([1, 3, w]) for x in range(1, 14))] == [9],
     'P2 9 is the only choice')
L.ok(has('1/3/8 → 13; 1/3/9 → 14; 1/3/10 → 5')
     and (first_miss([1, 3, 8]), first_miss([1, 3, 9]), first_miss([1, 3, 10])) == (13, 14, 5), 'P3 first misses')
L.ok(len(ways([1, 3, 8], 4)) == 2 and len(ways([1, 3, 9], 4)) == 1
     and check_eq('4=3+1', [1, 3, 8], 4)[0] and check_eq('4+3+1=8', [1, 3, 8], 4)[0], 'P4 two / one balances of 4')
L.ok(has('Fourteen different positive targets require at least 29 placements') and 2 * 14 + 1 == 29 > 27,
     'P5 29 > 27')
L.ok(sorted({v for _, v in placements([1, 3, 9])}) == list(range(-13, 14))
     and sorted({27 + v for _, v in placements([1, 3, 9])}) == list(range(14, 41)), 'P6 27 + (-13..13) = 14..40')
L.ok(all(sum([1, 3, 9, w]) < 40 for w in range(1, 27))
     and all(14 not in reachable([1, 3, 9, w]) for w in range(28, 200)),
     'P6 below 27: total < 40; above 27: misses 14')

# ------------------------------------------------------------ Grades 4-5 key
L.out('\n== Grades 4-5 answer key (guide p. 4)')
okp1 = True
for a in range(1, 80):
    for b in range(a + 1, 80):
        if set(reachable([a, b])) - {a, b, b - a, a + b}:
            okp1 = False
L.ok(okp1, 'P1 for 0<a<b the positive targets are among a, b, b-a, a+b (checked a<b<80)')
L.ok(all(sum([1, 3, w]) < 13 for w in range(1, 9)) and all(5 not in reachable([1, 3, w]) for w in range(10, 200)),
     'P2 w<9 total < 13; w>9 misses 5')
L.ok(2 * (1 + 3) == 8 < 9 and 2 * 1 == 2 < 3 and 0 < 1, 'P3 inequalities 8<9, 2<3, 0<1')
diffs_ok = all(abs(sum((c1 - c2) * w for c1, c2, w in zip(p, q, [1, 3, 9]))) > 0
               for p in product((-1, 0, 1), repeat=3) for q in product((-1, 0, 1), repeat=3) if p != q)
L.ok(diffs_ok, 'P3 no two distinct placements of 1,3,9 give the same difference')
L.ok(has('(page 3)') and 'Three weights have 27 placements' in T[2],
     'P4 cross-reference: the 27-placement bound is on guide p. 3')
L.ok(reachable([1, 2, 3]) == list(range(1, 7)), 'P5 1,2,3 reaches only 1-6')
L.ok(reachable([1, 4, 16]) == [1, 3, 4, 5, 11, 12, 13, 15, 16, 17, 19, 20, 21]
     and has('{1,3,4,5,11,12,13,15,16,17,19,20,21}'), f'P5 1,4,16 -> {reachable([1, 4, 16])}')
L.ok(sorted({v for _, v in placements([1, 3, 9, 27])}) == list(range(-40, 41)) and 27 > 2 * (1 + 3 + 9) == 26,
     'P6 intervals [-40,-14], [-13,13], [14,40]; 27 > 26')
L.ok(sorted({v for _, v in placements([1, 3, 9, 27, 81])}) == list(range(-121, 122)) and 3 ** 5 == 243,
     'P7 [-121,-41], [-40,40], [41,121]; 243 placements')
one = {}
for cs in product((0, 1), repeat=3):
    v = sum(c * w for c, w in zip(cs, [1, 2, 4]))
    one.setdefault(v, []).append(cs)
L.ok(sorted(v for v in one if v > 0) == list(range(1, 8)) and all(len(one[v]) == 1 for v in one),
     'Extension: weights opposite only, 1,2,4 cover 1-7 uniquely')

# ------------------------------------------------------------ launch / route note
L.out('\n== Launch, timing and route note')
L.ok(has('Put 1 beside the target and 4 opposite, so 3+1=4'), 'Launch example matches the student pages (3 + 1 = 4)')
L.ok(has('K-1 can choose among two-weight kits (P4) or add a third weight (P5)'),
     'Route note K-1 references P4/P5 correctly')
L.ok(has('Grades 4-5 can choose uniqueness (P3), a universal placement bound (P4-5), or the four-/five-weight '
         'construction (P6-7)'), 'Route note 4-5 references P3, P4-5, P6-7 correctly')
L.ok(has('Grades 2-3 can compare repeated balances (P4) before the counting bound and fourth-weight kit (P5-6)'),
     'Route note 2-3 references P4, P5-6 correctly')
L.save()
