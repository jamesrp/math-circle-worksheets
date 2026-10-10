"""Independent check of the Week 49 bonus companion (3 student pages) and of
every mathematical claim in the bonus adult guide.

Run pdf_extract.py first: printed rings, labels, cycle edges, station sizes
and table sizes come from pdf_geometry.json (the delivered PDFs).

Writes check_bonus.out.
"""
import json
import os
import re
import sys
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import D, E, HERE, PDFS, Log, fmt, page_text, run  # noqa: E402

log = Log('Week 49 bonus companion: independent checks')
G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))['bonus']['pages']
GUIDE = re.sub(r'\s+', ' ', page_text(PDFS['bonus-guide']))
STUDENT = re.sub(r'\s+', ' ', page_text(PDFS['bonus']))


def groups(page, prob):
    return [g for g in G[page - 1]['groups'] if g['problem'] == prob]


def val(v):
    return int(v.replace('+', ''))


def by_label(g, order):
    d = {s['label']: s['value'] for s in g['stations']}
    return tuple(val(d[k]) for k in order)


def cyc_ok(g, order):
    want = sorted(sorted((order[i], order[(i + 1) % len(order)])) for i in range(len(order)))
    return g['edges'] == want


# ------------------------------------------------------------------ page 1
log.p('\n## Page 1 worked example and Problem 1 (find every old ring)')
ex_old, ex_new = groups(1, 'intro')
o, n = by_label(ex_old, 'ABCD'), by_label(ex_new, 'ABCD')
log.check(D(o) == n, f'worked example {fmt(o)} -> {fmt(n)}; D = {fmt(D(o))}; "A gap: 3 - 1 = 2" = |{o[1]}-{o[0]}|')
targets = []
for g in groups(1, 1):
    log.check(cyc_ok(g, 'ABCD'), f'P1 cycle joins A-B-C-D-A (edges {g["edges"]})')
    targets.append(by_label(g, 'ABCD'))
tables = G[0]['table_boxes'] // (2 * 4)
log.p(f'  P1 targets {[fmt(t) for t in targets]}; each recording table has {tables} rows')
guide_lists = {
    (1, 1, 1, 1): {(0, 1, 0, 1), (0, 1, 2, 1), (1, 0, 1, 0), (1, 0, 1, 2), (1, 2, 1, 0), (2, 1, 0, 1)},
    (1, 2, 1, 2): {(0, 1, 3, 2), (1, 0, 2, 3), (2, 3, 1, 0), (3, 2, 0, 1)},
}
for t in targets:
    pre = {s for s in product(range(4), repeat=4) if 0 in s and D(s) == t}
    log.p(f'  {fmt(t)}: {len(pre)} old rings with heights 0..3 and a 0: {sorted(fmt(s) for s in pre)}')
    log.check(pre == guide_lists[t], f'{fmt(t)}: guide list is exactly the complete set')
    log.check(len(pre) <= tables, f'{fmt(t)}: {len(pre)} answers fit the {tables}-row table')
    # every predecessor (any heights) normalised to min 0 lies in 0..3: the restriction loses nothing
    allpre = {tuple(x - min(s) for x in s) for s in product(range(8), repeat=4) if D(s) == t}
    log.check(allpre == pre, f'{fmt(t)}: the 0..3 / at-least-one-0 rule drops no normalised predecessor (0..7 search)')
# guide sign-count explanation
signs11 = [e for e in product((1, -1), repeat=4) if sum(e) == 0]
signs12 = [e for e in product((1, -1), repeat=4) if e[0] * 1 + e[1] * 2 + e[2] * 1 + e[3] * 2 == 0]
log.check(len(signs11) == 6 and len(signs12) == 4, 'sign choices: 6 for (1,1,1,1), 4 for (1,2,1,2) (guide agrees)')
log.check(D((5, 6, 7, 6)) == D((0, 1, 2, 1)) and D(tuple(2 - x for x in (0, 1, 2, 1))) == D((0, 1, 2, 1)),
          'adding a constant or replacing h by M-h leaves the next ring unchanged')
rel = {tuple(x - min(y) for x in y) for y in [(0, 1, 0, 1)] + [tuple(m - x for x in (0, 1, 0, 1)) for m in range(1, 4)]}
log.check((0, 1, 2, 1) not in rel, '(0,1,0,1) and (0,1,2,1) are not related by translation or complement (guide claim)')

# ------------------------------------------------------------------ page 2
log.p('\n## Page 2, Problem 2: binary rings on six and eight stations')


def X(s):
    n = len(s)
    return tuple(s[i] ^ s[(i + 1) % n] for i in range(n))


six = [g for g in groups(2, 2) if len(g['stations']) == 6][0]
eight = [g for g in groups(2, 2) if len(g['stations']) == 8][0]
log.check(cyc_ok(six, [str(i) for i in range(1, 7)]) and cyc_ok(eight, [str(i) for i in range(1, 9)]),
          'cycles join stations in number order, wrapping to 1')
s6 = by_label(six, [str(i) for i in range(1, 7)])
s8 = by_label(eight, [str(i) for i in range(1, 9)])
st, oc, m = run(s6, X)
log.p(f'  six-station start {"".join(map(str, s6))}: {" -> ".join("".join(map(str, x)) for x in st)}  [{oc}]')
log.check(oc == ('repeat', 1) and len(st) - 2 == 3, 'six-station start enters a nonzero period-3 cycle from round 1')
st8 = [s8]
for _ in range(8):
    st8.append(X(st8[-1]))
log.p(f'  eight-station start: {" -> ".join("".join(map(str, x)) for x in st8)}')
log.check(st8[7] == (1,) * 8 and st8[8] == (0,) * 8, 'printed eight-start: round 7 = 11111111, round 8 = 00000000')
allz = all((lambda z: not any(z))(__import__('functools').reduce(lambda a, _: X(a), range(8), s)) for s in product((0, 1), repeat=8))
log.check(allz, 'all 256 eight-station starts are all 0 at round 8')
late = [s for s in product((0, 1), repeat=8) if any(__import__('functools').reduce(lambda a, _: X(a), range(7), s))]
log.p(f'  eight-starts with a 1 at round 7: {len(late)} (those with an odd number of 1s)')
ok = True
for n in (6, 8, 16):
    for s in product((0, 1), repeat=n) if n <= 8 else [tuple((i * 7 + 3) % 5 % 2 for i in range(16))]:
        for j in range(4):
            if 2 ** j > n:
                break
            y = s
            for _ in range(2 ** j):
                y = X(y)
            ok &= y == tuple(s[i] ^ s[(i + 2 ** j) % n] for i in range(n))
log.check(ok, 'doubling distance: after 2^j rounds each entry is x_i xor x_(i+2^j)')
cyc6 = [s for s in product((0, 1), repeat=6) if run(s, X)[1] != 'zero']
log.p(f'  six-station starts that never reach all 0: {len(cyc6)} of 64; '
      f'those that do: {sorted("".join(map(str, s)) for s in product((0, 1), repeat=6) if run(s, X)[1] == "zero")}')
for n in (5, 7, 16):
    dies = all(run(s, X)[1] == 'zero' for s in (product((0, 1), repeat=n) if n < 16 else
                                              [tuple(int(c) for c in format(k, '016b')) for k in range(0, 65536, 97)]))
    log.p(f'  {n} stations: every start reaches all 0? {dies}')
log.check(G[1]['table_boxes'] == 9 * 6 + 9 * 8, 'page-2 tables have rounds 0..8 for 6 and 8 stations')

# ------------------------------------------------------------------ page 3
log.p('\n## Page 3, Problem 3: directed differences')
eo, en = groups(3, 'intro')
o, n = by_label(eo, 'ABCD'), by_label(en, 'ABCD')
log.check(E(o) == n, f'worked example {fmt(o)} -> {fmt(n)}; E = {fmt(E(o))}')
starts = [by_label(g, 'ABCD') for g in groups(3, 3)]
far = {}
for s in starts:
    st = [s]
    for _ in range(9):
        st.append(E(st[-1]))
    log.p(f'  {fmt(s)}: ' + ' -> '.join(fmt(x) for x in st))
    far[s] = next((k for k, x in enumerate(st) if max(abs(v) for v in x) > 10), None)
    log.p(f'    first round with an entry more than 10 from 0: {far[s]}')
log.check(far[starts[0]] == 5 and (far[starts[1]] is None or far[starts[1]] > 5),
          'only the first start passes 10 within five rounds (guide agrees)')
st = [starts[0]]
for _ in range(5):
    st.append(E(st[-1]))
log.check(max(map(abs, st[4])) == 8 and max(map(abs, st[5])) == 16,
          'EDGE: first start is 8 from 0 at round 4 and 16 at round 5, so "within five rounds" '
          'must include round 5 (rows 0..5); counting five rows (rounds 0..4) gives "neither"')
log.check(all(sum(E(s)) == 0 for s in product(range(-3, 4), repeat=4)), 'every directed output sums to zero')
log.check(all(E((a, -a, a, -a)) == (-2 * a, 2 * a, -2 * a, 2 * a) for a in range(-5, 6)),
          'alternating (a,-a,a,-a) -> (-2a,2a,-2a,2a): magnitude doubles, so unbounded')
log.check(G[2]['table_boxes'] == 2 * 8 * 4, 'page-3 tables have rounds 0..7')

# guide chains
log.p('\n## Every chain printed in the bonus guide')
for ch in re.findall(r'((?:[01]{6,8} -> )+[01]{6,8})', GUIDE):
    parts = [tuple(int(c) for c in p) for p in ch.split(' -> ')]
    log.check(all(X(a) == b for a, b in zip(parts, parts[1:])), f'binary chain {ch}')
for ch in re.findall(r'(\(-?\d+(?:,-?\d+){3}\)(?: -> \(-?\d+(?:,-?\d+){3}\))+)', GUIDE):
    parts = [tuple(int(v) for v in p.strip('()').split(',')) for p in ch.split(' -> ')]
    f = E if any(v < 0 for p in parts for v in p) else D
    log.check(all(f(a) == b for a, b in zip(parts, parts[1:])), f'chain ({f.__name__}) {ch}')
sec = re.search(r'Second run through five rounds: ((?:\(-?\d+(?:,-?\d+){3}\),? ?)+)', GUIDE).group(1)
parts = [tuple(int(v) for v in p.split(',')) for p in re.findall(r'\(([^)]*)\)', sec)]
log.check(all(E(a) == b for a, b in zip(parts, parts[1:])) and parts[0] == starts[1],
          f'guide second run {", ".join(fmt(p) for p in parts)}')
log.check(D((1, 3, 2, 0)) == (2, 1, 2, 1) and '(2,1,2,1)' in GUIDE, 'guide launch output (2,1,2,1)')
log.check(E((1, 3, 3, 1)) == (2, 0, -2, 0), 'guide launch visual (1,3,3,1) -> (+2,0,-2,0)')

# ------------------------------------------------------------------ materials
log.p('\n## Bonus guide: sizes and counts')
p1 = {s['w_mm'] for g in groups(1, 1) for s in g['stations']}
p2 = {s['w_mm'] for g in groups(2, 2) for s in g['stations']}
log.check(p1 == {20.46} and '20.5 mm' in GUIDE, f'page-1 stations {p1} mm (guide 20.5)')
log.check(p2 == {21.87} and '21.9 mm' in GUIDE, f'page-2 stations {p2} mm (guide 21.9)')
log.check(2 * 8 == 16 and 2 * 4 == 8, 'sixteen 0/1 counters = old + new eight-ring; eight cards = old + new four-ring')
mx = max(sum(s) + sum(t) for t in targets for s in guide_lists[t])
log.p(f'  largest cube need for one listed old ring plus its new ring: {mx} (guide: twelve optional cubes)')
log.check('256 bounded four-starts' in GUIDE and 4 ** 4 == 256, '256 = four heights 0..3')
log.finish()
