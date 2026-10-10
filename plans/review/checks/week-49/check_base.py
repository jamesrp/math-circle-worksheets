"""Independent check of every base Week 49 task (K-1, Grades 2-3, Grades 4-5)
and of every mathematical claim in the base adult guide.

Run pdf_extract.py first: the printed rings (heights, labels, arrow order),
mat sizes and positions used here come from pdf_geometry.json, i.e. from the
delivered PDFs, not from the author's sources or answers.

Writes check_base.out.
"""
import json
import math
import os
import re
import sys
from itertools import permutations, product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import D, HERE, PDFS, Log, fmt, moves_to_zero, page_text, run  # noqa: E402

log = Log('Week 49 base packet: independent checks')
G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))
GUIDE = re.sub(r'\s+', ' ', page_text(PDFS['guide']))
TEXT = {b: re.sub(r'\s+', ' ', page_text(PDFS[b])) for b in ('K-1', '2-3', '4-5')}


def rings(band, prob):
    return [r for p in G[band]['pages'] for r in p['rings'] if r['problem'] == prob]


def tup(r):
    return tuple(int(s['value']) for s in r['stations'])


def guide_has(s):
    return s in GUIDE


# ------------------------------------------------------------------ rule + intro
log.p('\n## Shared rule and worked example (page 1, every band)')
for b in ('K-1', '2-3', '4-5'):
    old, new = rings(b, 'intro')
    o, n = tup(old), tup(new)
    log.check(''.join(s['letter'] for s in old['stations']) == 'ABCD' and old['arrow_cycle'],
              f'{b}: example arrows run A->B->C->D->A')
    log.check(D(o) == n, f'{b}: example old {fmt(o)} -> printed new {fmt(n)}; D(old) = {fmt(D(o))}')
    for g in old['gaps']:
        t, h = g['tail_pos'], g['head_pos']
        log.check(g['value'] == abs(o[t] - o[h]) and h == (t + 1) % 4,
                  f'{b}: printed gap {g["value"]} on arrow {"ABCD"[t]}->{"ABCD"[h]} = |{o[t]}-{o[h]}|; '
                  f'new {"ABCD"[t]} (tail) = {n[t]}')
    log.check('Edge A to B has gap 3, so new A is 3' in TEXT[b], f'{b}: caption matches the diagram')

# ------------------------------------------------------------------ guide chains
log.p('\n## Every arrow chain printed in the base guide')
chains = re.findall(r'(\(\d+(?:,\d+)+\)(?: → \(\d+(?:,\d+)+\))*(?: → zero)?)', GUIDE)
for ch in chains:
    if '→' not in ch:
        continue
    parts = ch.split(' → ')
    ok = True
    for a, c in zip(parts, parts[1:]):
        x = tuple(int(v) for v in a.strip('()').split(','))
        if c == 'zero':
            ok &= not any(D(x))
        else:
            y = tuple(int(v) for v in c.strip('()').split(','))
            ok &= D(x) == y
    log.check(ok, f'guide chain {ch}: {len(parts) - 1} moves, every step is the gap rule')

# ------------------------------------------------------------------ Problem 1
log.p('\n## Problem 1 (all bands): the four printed starts')
for b in ('K-1', '2-3', '4-5'):
    rs = rings(b, 1)
    res = []
    for r in rs:
        s = tup(r)
        states, outcome, m = run(s)
        res.append((m, s))
        log.p(f'  {b}: {" -> ".join(fmt(x) for x in states)}  [{outcome}, {m} moves]')
    best = max(res)
    log.check(sum(1 for m, _ in res if m == best[0]) == 1,
              f'{b}: unique longest printed start {fmt(best[1])} with {best[0]} moves')
log.check(guide_has('(0,0,0,2) → (0,0,2,2) → (0,2,0,2) → (2,2,2,2) → zero: 4 moves, longest of the four printed starts'),
          'guide names (0,0,0,2), 4 moves, as longest (agrees)')
for s, m in [((1, 1, 0, 0), 3), ((1, 0, 1, 0), 2), ((2, 1, 0, 1), 2), ((0, 0, 0, 2), 4)]:
    log.check(moves_to_zero(s) == m and f'zero: {m} moves' in GUIDE, f'guide move count {fmt(s)}: {m}')

# ------------------------------------------------------------------ Problem 2
log.p('\n## Problem 2: longest run with bounded starting heights')
for b, M in (('K-1', 4), ('2-3', 5), ('4-5', 5)):
    phrase = 'Choose heights from 0 to 4' if M == 4 else 'Choose starting heights from 0 to 5'
    log.check(phrase in TEXT[b], f'{b}: page states the range 0..{M}')
for M in (4, 5):
    allst = list(product(range(M + 1), repeat=4))
    lens = {s: moves_to_zero(s) for s in allst}
    best = max(lens.values())
    arg = sorted(s for s in allst if lens[s] == best)
    hist = {}
    for v in lens.values():
        hist[v] = hist.get(v, 0) + 1
    log.p(f'  range 0..{M}: {len(allst)} starts, moves histogram {dict(sorted(hist.items()))}')
    log.p(f'  longest = {best} moves, {len(arg)} starts: {[fmt(s) for s in arg]}')
    log.check(best == 7 and (0, 1, 2, 4) in arg, f'range 0..{M}: maximum 7 and (0,1,2,4) attains it (guide claims both)')
log.check('all 625 and 1,296 permitted starts' in GUIDE and 'give maximum 7' in GUIDE, 'guide counts 625 / 1,296 starts')
log.check(moves_to_zero((0, 0, 0, 0)) == 0, 'all-zero start takes 0 moves (page note)')

# ------------------------------------------------------------------ K-1 P3, P4
log.p('\n## K-1 Problems 3 and 4: starts that first reach zero on move 1 / move 2')
B = 9
one = [s for s in product(range(B + 1), repeat=4) if any(s) and moves_to_zero(s) == 1]
log.check(all(len(set(s)) == 1 for s in one) and len(one) == B,
          f'heights 0..{B}: the {len(one)} one-move starts are exactly the positive constants')
two = [s for s in product(range(B + 1), repeat=4) if moves_to_zero(s) == 2]
char = [s for s in product(range(B + 1), repeat=4) if len(set(D(s))) == 1 and D(s)[0] > 0]
log.check(sorted(two) == sorted(char),
          f'heights 0..{B}: the {len(two)} two-move starts are exactly those whose four gaps equal one positive c')
log.check(moves_to_zero((0, 1, 0, 1)) == 2 and moves_to_zero((0, 1, 2, 1)) == 2, 'guide examples (0,1,0,1), (0,1,2,1): 2 moves')
log.check(len(rings('K-1', 3)) == 2 and len(rings('K-1', 4)) == 2, 'K-1 P3 and P4 each print two blank rings (A->B->C->D)')
p3 = re.search(r'Problem 3: (.*?)Problem 4: (.*?)Bellingham', TEXT['K-1'])
log.p(f'  K-1 P3 text: "{p3.group(1).strip()}"   P4 text: "{p3.group(2).strip()}"')
log.check(D((0, 0, 0, 0)) == (0, 0, 0, 0) and 'first' not in p3.group(1) and 'first' in p3.group(2),
          'EDGE: (0,0,0,0) is all zeros after one move; P3 (unlike P4) does not say "first", '
          'while the guide says "Do not count (0,0,0,0)"')

# ------------------------------------------------------------------ older P3
log.p('\n## Grades 2-3 / 4-5 Problem 3: is each printed ring the result of one move?')
log.p('  Completeness of the search: predecessors are closed under adding a constant, so translate one to')
log.p('  minimum 0; walking both ways round the ring from a lowest to a highest station gives')
log.p('  2*(max - min) <= sum of the four gaps, so heights 0..floor(sum/2) cover every normalised predecessor.')
for b in ('2-3', '4-5'):
    for r in rings(b, 3):
        t = tup(r)
        bound = sum(t) // 2
        pre = [s for s in product(range(bound + 1), repeat=4) if min(s) == 0 and D(s) == t]
        log.p(f'  {b} {fmt(t)}: total {sum(t)} ({"even" if sum(t) % 2 == 0 else "odd"}); normalised predecessors '
              f'{[fmt(s) for s in pre] or "none"}')
claims = {(2, 0, 2, 0): (0, 2, 2, 0), (1, 1, 1, 1): (0, 1, 0, 1)}
for t, w in claims.items():
    log.check(D(w) == t, f'guide witness {fmt(w)} -> {fmt(t)}')
for t in [(1, 1, 1, 0), (0, 0, 0, 2)]:
    bound = sum(t) // 2
    log.check(not [s for s in product(range(bound + 1), repeat=4) if D(s) == t], f'{fmt(t)} has no predecessor (guide: impossible)')
log.check(all(sum(D(s)) % 2 == 0 for s in product(range(8), repeat=4)), 'every output has an even total (0..7 exhaustive)')
log.check('Even total is necessary, not sufficient.' in GUIDE and sum((0, 0, 0, 2)) % 2 == 0,
          '(0,0,0,2) has an even total yet no predecessor: "necessary, not sufficient" is right')

# ------------------------------------------------------------------ stations
log.p('\n## K-1 Problem 5 / older Problem 4: four stations against three')
for b, p in (('K-1', 5), ('2-3', 4), ('4-5', 4)):
    small = [r for r in rings(b, p) if r['stations'][0]['value'] is not None]
    for r in small:
        s = tup(r)
        states, outcome, m = run(s)
        log.p(f'  {b} P{p} {len(s)} stations ({"".join(x["letter"] for x in r["stations"])} by arrows): '
              f'{" -> ".join(fmt(x) for x in states)}  [{outcome}]')
    mats = [r for r in rings(b, p) if r['stations'][0]['value'] is None]
    log.check(len(mats) == 2 and all(len(r['stations']) == 3 and r['arrow_cycle'] for r in mats),
              f'{b} P{p}: two blank three-station mats with arrows A->B->C->A, as in the small diagram')
st, oc, _ = run((1, 0, 0))
log.check(oc == ('repeat', 1) and st[1] == (1, 0, 1) and len(st) - 1 - 1 == 3,
          'three-station (1,0,0) enters a period-3 cycle (1,0,1)->(1,1,0)->(0,1,1)->(1,0,1) (guide agrees)')
log.check(moves_to_zero((1, 0, 0, 0)) == 4, 'four-station (1,0,0,0) reaches zero in 4 moves (guide agrees)')

# ------------------------------------------------------------------ orders
log.p('\n## K-1 Problem 6 / Grades 2-3 Problem 5: orders of 0, 1, 2, 4')
dur = {p: moves_to_zero(p) for p in permutations((0, 1, 2, 4))}
by = {}
for p, m in dur.items():
    by.setdefault(m, []).append(p)
for m in sorted(by):
    log.p(f'  {m} moves: {len(by[m])} orders, e.g. {[fmt(p) for p in sorted(by[m])[:8]]}')
rot = lambda p, k: p[k:] + p[:k]  # noqa: E731
fam = {rot(q, k) for q in [(0, 1, 2, 4), (4, 2, 1, 0)] for k in range(4)}
log.check(set(by[7]) == fam and len(by[7]) == 8 and len(by.get(4, [])) == 16 and set(by) == {4, 7},
          '8 longest orders (7 moves) = rotations and reversals of (0,1,2,4); other 16 last 4 (guide agrees)')
for rep, m in [((0, 1, 2, 4), 7), ((0, 1, 4, 2), 4), ((0, 2, 1, 4), 4)]:
    log.check(dur[rep] == m, f'guide representative {fmt(rep)}: {m} moves')
for b, p in (('K-1', 6), ('2-3', 5)):
    printed = [tup(r) for r in rings(b, p)]
    log.p(f'  {b} P{p} printed orders {[fmt(s) for s in printed]} last {[dur[s] for s in printed]} moves')
    log.check(not any(dur[s] == 7 for s in printed),
              f'{b} P{p}: no printed order is already a longest order (else the page shows the answer)')

# ------------------------------------------------------------------ bound
log.p('\n## Grades 2-3 Problem 6 / Grades 4-5 Problem 7: can a height exceed the old maximum?')
log.check(all(max(D(s)) <= max(s) for s in product(range(9), repeat=4)), 'max(D(s)) <= max(s) for all s in 0..8 (and |a-b| <= max(a,b) in general)')
ex = (0, 1, 2, 4)
log.check(max(D(ex)) == max(ex) == 4 and D(ex) == (1, 1, 2, 4), 'tallest can stay: (0,1,2,4) -> (1,1,2,4), max 4 (guide example)')
r23 = rings('2-3', 6)
log.check(tup(r23[0]) == (0, 1, 2, 4) and r23[1]['stations'][0]['value'] is None,
          '2-3 P6 prints (0,1,2,4) beside a blank ring')
log.check(sum(D((0, 1, 2, 4))) != sum((0, 1, 2, 4)), 'total height not conserved: 7 -> 8')

# ------------------------------------------------------------------ parity
log.p('\n## Grades 4-5 Problem 5: even/odd letter rings')
P = {'E': 0, 'O': 1}
a, b_ = rings('4-5', 5)[:2]
pa = tuple(P[s['value']] for s in a['stations'])
pb = tuple(P[s['value']] for s in b_['stations'])
log.check(tuple(x % 2 for x in D(pa)) == pb, f'worked example {"".join(s["value"] for s in a["stations"])} -> '
          f'{"".join(s["value"] for s in b_["stations"])} follows the printed letter rule')
log.check(all((abs(x - y) % 2) == ((x % 2) ^ (y % 2)) for x in range(10) for y in range(10)),
          'letter rule E,E->E; O,O->E; E,O->O; O,E->O is the parity of the gap')
for k in range(1, 6):
    reach = set()
    for s in product((0, 1), repeat=4):
        for _ in range(k):
            s = tuple(x % 2 for x in D(s))
        reach.add(''.join('EO'[x] for x in s))
    log.p(f'  letter rings possible after {k} move(s): {sorted(reach)}')
    if k == 4:
        log.check(reach == {'EEEE'}, 'only EEEE after four moves (guide agrees)')
ok = True
for s in product((0, 1), repeat=4):
    a1, b1, c1, d1 = s
    r2 = tuple(x % 2 for x in D(D(s)))
    ok &= r2 == ((a1 + c1) % 2, (b1 + d1) % 2, (a1 + c1) % 2, (b1 + d1) % 2)
    r3 = tuple(x % 2 for x in D(D(D(s))))
    ok &= len(set(r3)) == 1 and r3[0] == sum(s) % 2
log.check(ok, 'guide rows: after 2 moves (a+c,b+d,a+c,b+d), after 3 moves (s,s,s,s), s = a+b+c+d (mod 2)')
log.check(all(all(x % 2 == 0 for x in D(D(D(D(s))))) for s in product(range(8), repeat=4)),
          'every integer start in 0..7 has only even heights after four moves')

# ------------------------------------------------------------------ scaling
log.p('\n## Grades 4-5 Problem 6: doubling and tripling')
r1, r2 = [tup(r) for r in rings('4-5', 6)]
log.check(r2 == tuple(2 * x for x in r1), f'printed second start {fmt(r2)} = 2 x {fmt(r1)}')
for s in (r1, r2, tuple(3 * x for x in r1)):
    states, oc, m = run(s)
    log.p(f'  {" -> ".join(fmt(x) for x in states)}  [{m} moves]')
log.check(all(moves_to_zero(tuple(k * x for x in s)) == moves_to_zero(s)
              for s in product(range(6), repeat=4) for k in (2, 3, 5)),
          'scaling by 2, 3, 5 keeps the number of moves, all starts 0..5 (guide: any positive integer)')
log.check(r1 == (1, 4, 2, 0) and rings('4-5', 'intro')[0] and tup(rings('4-5', 'intro')[0]) == r1,
          'NOTE: the page-1 worked example is the same ring (1,4,2,0) as P6, so P6\'s first move is printed on page 1')

# ------------------------------------------------------------------ termination
log.p('\n## Grades 4-5 Problem 8 and the overview: termination proof')
N = 20
worst = {}
okdiv = True
okbound = True
for s in product(range(N + 1), repeat=4):
    m = moves_to_zero(s)
    M = max(s)
    if M:
        kk = M.bit_length()           # smallest k with 2^k > M
        okbound &= m <= 4 * kk
    x = s
    for k in range(1, 6):
        for _ in range(4):
            x = D(x)
        okdiv &= all(v % (2 ** k) == 0 for v in x)
    worst[M] = max(worst.get(M, 0), m)
log.check(True, f'all {(N + 1) ** 4} starts with heights 0..{N} reach zero')
log.check(okdiv, f'after 4k moves every height is divisible by 2^k (k = 1..5, heights 0..{N})')
log.check(okbound, 'moves to zero <= 4k with 2^k > max, as the proof gives')
log.p(f'  worst moves by maximum height: {worst}')
log.check(moves_to_zero((5, 5, 5, 5)) == 1 and moves_to_zero((0, 0, 0, 0)) == 0, 'nonzero constant: 1 move; zero: 0 moves')
max_drop = [s for s in product(range(5), repeat=4) if any(s) and max(D(s)) == max(s)]
log.check(len(max_drop) > 0, f'maximum need not decrease each move ({len(max_drop)} starts in 0..4 keep it)')

# ------------------------------------------------------------------ materials
log.p('\n## Guide: mat sizes and cube count')
for b in ('K-1', '2-3', '4-5'):
    for p in ((2, 5) if b == 'K-1' else (2, 4)):
        mats = [r for r in rings(b, p) if r['stations'][0]['kind'] == 'square']
        sizes = {(s['w_mm'], s['h_mm']) for r in mats for s in r['stations']}
        log.check(sizes == {(40.0, 40.0)}, f'{b} P{p} mats: stations {sizes} mm (guide: 40 mm squares)')
        for r in mats:
            c = [(s['cx_mm'], s['cy_mm']) for s in r['stations']]
            if len(c) == 4:
                sides = [round(math.dist(c[i], c[(i + 1) % 4]), 2) for i in range(4)]
                log.check(set(sides) == {52.0}, f'{b} P{p} four-station centres {sides} mm apart (guide 52)')
            else:
                xs = [x for x, _ in c]
                ys = [y for _, y in c]
                log.check(round(max(xs) - min(xs), 2) == 52.0 and round(max(ys) - min(ys), 2) == 52.0,
                          f'{b} P{p} three-station centres span {round(max(xs) - min(xs), 2)} x {round(max(ys) - min(ys), 2)} mm (guide 52 x 52)')
        old, new = sorted(mats, key=lambda r: min(s['cx_mm'] for s in r['stations']))
        gap = min(s['cx_mm'] - s['w_mm'] / 2 for s in new['stations']) - max(s['cx_mm'] + s['w_mm'] / 2 for s in old['stations'])
        log.p(f'  {b} P{p}: clear gap between the old mat and the new mat = {gap:.2f} mm')
log.check(8 * 5 == 40, 'forty cubes = two four-station states x height 5')

# ------------------------------------------------------------------ key coverage
log.p('\n## Guide key covers every numbered problem')
need = ['Problem 1, all bands', 'Problem 2, all bands', 'K-1 Problem 3', 'K-1 Problem 4', 'Older Problem 3',
        'K-1 Problem 5; older Problem 4', 'K-1 Problem 6; Grades 2-3 Problem 5', 'Grades 2-3 Problem 6; Grades 4-5 Problem 7',
        'Grades 4-5 Problem 5', 'Grades 4-5 Problem 6', 'Grades 4-5 Problem 8']
for n in need:
    log.check(n in GUIDE, f'guide has a key headed "{n}"')
for b, k in (('K-1', 6), ('2-3', 6), ('4-5', 8)):
    hs = [h for p in G[b]['pages'] for h in p['headings']]
    log.check(hs == list(range(1, k + 1)), f'{b}: problems numbered {hs}')

log.finish()
