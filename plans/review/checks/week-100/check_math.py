#!/usr/bin/env python3
"""Independent mathematical check of Week 100 (Distance in nested worlds).

Written for the review; does not import or run the package's check_math.py.
Uses the data read back from the delivered PDF by check_diagrams.py
(pdf_extract.json; regenerated if missing).

Worlds are enumerated directly as the page-1 rules define them: a rooted
tree of loops (every loop has >= 2 children; one-child loops are redundant
frames and never change a distance) with labels from a label set, strictly
increasing outward; distance = label of the smallest common loop.

Covers:
  P1  table, P2 the six triples, P3 balls, P4 reconstruction (uniqueness of
  the loop structure), P5 all 20 single-clue changes (and the other reading
  of the second paragraph), P6/P7 over every 3..6-card world with labels
  {2,4,8} and over worlds with arbitrary labels {1..6}, P8/P9 number world
  (rules vs 8*2^-v, realisation, balls, triples), P10 query game (adversary
  witness for 15; exact minimax for 4 and 5 cards), label-card supply, and
  every numeric claim in the facilitator guide.
Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
import json
import subprocess
import sys
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT, FAILS = [], []


def say(s=''):
    OUT.append(str(s))
    print(s)


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


if not (HERE / 'pdf_extract.json').exists():
    subprocess.run([sys.executable, str(HERE / 'check_diagrams.py')], check=True)
DATA = json.loads((HERE / 'pdf_extract.json').read_text())


# ---------------------------------------------------------------- worlds
def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p


@lru_cache(maxsize=None)
def trees(cards):
    """All loop trees on frozenset `cards` (|cards|>=2): tuples (cards, children)."""
    out = []
    for p in set_partitions(sorted(cards)):
        if len(p) < 2:
            continue
        opts = []
        for block in p:
            fb = frozenset(block)
            opts.append([fb] if len(fb) == 1 else trees(fb))
        for ch in product(*opts):
            out.append((cards, ch))
    return tuple(out)


def internal(t):
    if isinstance(t, frozenset):
        return []
    res = [t[0]]
    for c in t[1]:
        res += internal(c)
    return res


def labelings(t, labels, above=None):
    """Yield dicts {loop cards: label}, labels strictly increasing outward."""
    if isinstance(t, frozenset):
        yield {}
        return
    for lab in labels:
        if above is not None and lab >= above:
            continue
        subs = [list(labelings(c, labels, lab)) for c in t[1]]
        for combo in product(*subs):
            d = {t[0]: lab}
            for x in combo:
                d.update(x)
            yield d


def dist_of(lab, cards):
    d = {}
    for a, b in combinations(sorted(cards), 2):
        d[a + b] = min((len(s), v) for s, v in lab.items() if a in s and b in s)[1]
    return d


def worlds(cards, labels=(2, 4, 8)):
    """List of (labelled loop family, distance dict) for every world."""
    fs = frozenset(cards)
    res = []
    for t in trees(fs):
        for lab in labelings(t, labels):
            res.append((lab, dist_of(lab, cards)))
    return res


def realizable_tables(cards, labels=(2, 4, 8)):
    return {tuple(sorted(d.items())) for _, d in worlds(cards, labels)}


def D(d, a, b):
    if a == b:
        return 0
    return d[a + b] if a + b in d else d[b + a]


def is_ultra(d, cards):
    for a, b, c in combinations(cards, 3):
        x = sorted([D(d, a, b), D(d, a, c), D(d, b, c)])
        if x[1] != x[2]:
            return False
    return True


def ball(d, cards, c, r):
    return frozenset(x for x in cards if D(d, c, x) <= r)


# ---------------------------------------------------------------- general
say('== worlds and the strong inequality ==')
counts = {}
for n in range(2, 7):
    cards = 'ABCDEF'[:n]
    tabs = realizable_tables(cards)
    counts[n] = len(tabs)
    allu = 0
    for vals in product((2, 4, 8), repeat=n * (n - 1) // 2):
        d = dict(zip([a + b for a, b in combinations(cards, 2)], vals))
        if is_ultra(d, cards):
            allu += 1
            if tuple(sorted(d.items())) not in tabs:
                FAILS.append(f'ultrametric not realised n={n}')
    check(allu == len(tabs), f'n={n}: realisable tables ({len(tabs)}) = ultrametrics with values in {{2,4,8}} ({allu})')
say(f'number of distinct distance tables by card count: {counts}')
W6 = worlds('ABCDEF')
say(f'6-card labelled loop structures (no redundant frames): {len(W6)}')

# P6 with arbitrary positive labels as well
for labels in [(2, 4, 8), (1, 2, 3, 4, 5, 6)]:
    bad = 0
    for n in range(3, 7 if labels == (2, 4, 8) else 6):
        for _, d in worlds('ABCDEF'[:n], labels):
            if not is_ultra(d, 'ABCDEF'[:n]):
                bad += 1
    check(bad == 0, f'P6: no world (labels {labels}) has a triple with a unique largest distance')

# P7 ball facts over all 6-card worlds, radii 0..9 and halves
radii = [x / 2 for x in range(0, 19)]
bad_overlap = bad_center = 0
for _, d in W6:
    cards = 'ABCDEF'
    balls = {}
    for c in cards:
        for r in radii:
            B = ball(d, cards, c, r)
            balls[(c, r)] = B
            for m in B:
                if ball(d, cards, m, r) != B:
                    bad_center += 1
    allb = set(balls.values())
    for B1, B2 in combinations(allb, 2):
        if B1 & B2 and not (B1 <= B2 or B2 <= B1):
            bad_overlap += 1
check(bad_overlap == 0, 'P7a: in every 6-card world, overlapping balls are nested')
check(bad_center == 0, 'P7b: moving the centre to any member never changes a ball')

# ---------------------------------------------------------------- P1
say('\n== Problem 1 / page 1 ==')
w1 = {k: v for k, v in DATA['world1']['dist'].items()}
check(is_ultra(w1, 'ABCDEF'), 'P1 world distances form a valid world table')
check(DATA['worked']['dist'] == {'XY': 3, 'XZ': 6, 'YZ': 6}, 'worked example X-Z=6, X-Y=3')
# labels the P1 world needs
need1 = sorted(lab for _, lab in DATA['world1']['groups'])
say(f'labels used by the P1 world: {need1}; label cards printed: {DATA["label_cards"]}')

# ---------------------------------------------------------------- P2
say('\n== Problem 2 ==')
tabs3 = realizable_tables('ABC')
possible3 = {(dict(t)['AB'], dict(t)['AC'], dict(t)['BC']) for t in tabs3}
res = []
for t in DATA['triples']:
    res.append((tuple(t), tuple(t) in possible3))
say(f'printed triples (AB,AC,BC) -> possible?: {res}')
check([r for _, r in res] == [True, True, False, True, False, True],
      'possible: 222, 244, 444, 288; impossible: 224, 248 (guide p.3 agrees)')
say(f'all realisable triples with labels 2,4,8: {sorted(possible3)}')

# ---------------------------------------------------------------- P3
say('\n== Problem 3 ==')
cards6 = 'ABCDEF'
for c in 'ACDF':
    say(f'  radius 3 around {c}: {sorted(ball(w1, cards6, c, 3))}')
check([sorted(ball(w1, cards6, c, 3)) for c in 'ACDF'] == [['A', 'B'], ['C', 'E'], ['D'], ['F']],
      'P3 radius-3 balls = {A,B},{C,E},{D},{F} (guide)')
coll = {}
for r in [0, 1, 2, 3, 4, 7, 8]:
    found = {ball(w1, cards6, c, r) for c in cards6 if 'B' in ball(w1, cards6, c, r)}
    check(len(found) == 1, f'radius {r}: every ball (any centre) containing B is the same set')
    for B in found:
        coll.setdefault(tuple(sorted(B)), []).append(r)
say(f'  balls containing B: {coll}')
check(coll == {('B',): [0, 1], ('A', 'B'): [2, 3], ('A', 'B', 'D'): [4, 7],
               ('A', 'B', 'C', 'D', 'E', 'F'): [8]}, 'P3 four collections with radii as in guide table')
check(sorted(ball(DATA['worked']['dist'], 'XYZ', 'X', 1)) == ['X'] and
      sorted(ball(DATA['worked']['dist'], 'XYZ', 'X', 4)) == ['X', 'Y'] and
      sorted(ball(DATA['worked']['dist'], 'XYZ', 'X', 3)) == ['X', 'Y'],
      'P3 text: radius 1 around X = {X}, radius 4 = {X,Y}; guide launch radius 3 = {X,Y}')

# ---------------------------------------------------------------- P4
say('\n== Problem 4 ==')
clues = DATA['clues']
W5 = worlds('ABCDE')
fits = [lab for lab, d in W5 if d == clues]
say(f'5-card loop structures (labels 2,4,8): {len(W5)}; fitting the ten clues: {len(fits)}')
for lab in fits:
    say('  ' + ', '.join(f'{"".join(sorted(s))}@{v}' for s, v in sorted(lab.items(), key=lambda kv: (kv[1], sorted(kv[0])))))
check(len(fits) == 1, 'P4: exactly one loop structure (up to redundant frames and layout)')
check(fits and {''.join(sorted(s)): v for s, v in fits[0].items()} == {'AB': 2, 'ABC': 4, 'DE': 2, 'ABCDE': 8},
      'P4 structure = AB@2, ABC@4, DE@2, all@8 (guide)')
fitsany = [lab for lab, d in worlds('ABCDE', (1, 2, 3, 4, 5, 6, 7, 8)) if d == clues]
check(len(fitsany) == 1, 'P4: still unique if any labels 1..8 were allowed')
check(clues != {k: v for k, v in w1.items() if 'F' not in k},
      'P4 hidden world differs from the P1 world restricted to A-E')

# ---------------------------------------------------------------- P5
say('\n== Problem 5 ==')
tabs5 = realizable_tables('ABCDE')


def ok5(d):
    return tuple(sorted(d.items())) in tabs5


broken = dict(clues)
broken['AC'] = 2
check(not ok5(broken), 'P5 first question: with A-C = 2 no world fits')
reps = []
for k in sorted(broken):
    for v in (2, 4, 8):
        if v == broken[k]:
            continue
        d = dict(broken)
        d[k] = v
        if ok5(d):
            reps.append(f'{k[0]}-{k[1]}:{broken[k]}->{v}')
say(f'  20 candidate changes from the broken set; repairs: {reps}')
check(reps == ['A-B:2->4', 'A-C:2->4', 'B-C:4->2'], 'P5: exactly three repairs, as the guide says')
# other reading: change one of Problem 4's original ten clues, keeping a world possible
alt = []
for k in sorted(clues):
    for v in (2, 4, 8):
        if v == clues[k]:
            continue
        d = dict(clues)
        d[k] = v
        if ok5(d):
            alt.append(f'{k[0]}-{k[1]}:{clues[k]}->{v}')
say(f'  other reading (start again from Problem 4 clues): single changes that keep a world: {alt}')
# guide completeness argument
check(not ok5({**broken, 'AB': 8}) and not ok5({**broken, 'AC': 8}) and not ok5({**broken, 'BC': 8}),
      'guide: AB->8, AC->8, BC->8 each fail')

# ---------------------------------------------------------------- P8/P9
say('\n== Problems 8-9: number world ==')
N = list(range(8))


def rule(a, b):
    if a == b:
        return 0
    if (a - b) % 2:
        return 8
    if a % 4 != b % 4:
        return 4
    return 2


def v2(x):
    x = abs(x)
    k = 0
    while x % 2 == 0:
        x //= 2
        k += 1
    return k


check(all(rule(a, b) == 8 * 2 ** -v2(a - b) for a in N for b in N if a != b),
      'rules = 8 * 2^-v(a-b) on cards 0..7 (guide overview)')
check(all(rule(a, b) == 2 for a in N for b in N if a != b and a % 4 == b % 4 and abs(a - b) == 4)
      and all(abs(a - b) == 4 for a in N for b in N if a != b and a % 4 == b % 4),
      'same remainder mod 4 on 0..7 <=> difference 4')
check(rule(1, 5) == 2, 'worked number example: 1 and 5 at distance 2')
Ns = [str(i) for i in N]
dn = {a + b: rule(int(a), int(b)) for a, b in combinations(Ns, 2)}
check(is_ultra(dn, Ns), 'P9: number distances satisfy the strong inequality (all 56 triples)')
eq = [t for t in combinations(N, 3) if len({rule(t[0], t[1]), rule(t[0], t[2]), rule(t[1], t[2])}) == 1]
check(not eq, 'guide: the number world has no equilateral triple')
# realise with loops: groups are radius-r balls at r = 2, 4, 8
grp = {}
for r in (2, 4, 8):
    for c in N:
        B = frozenset(x for x in N if rule(c, x) <= r)
        if len(B) > 1:
            grp.setdefault(B, r)  # smallest r giving it
lab = {}
for B, r in grp.items():
    lab[B] = r
dl = {}
for a, b in combinations(N, 2):
    dl[(a, b)] = min((len(s), v) for s, v in lab.items() if a in s and b in s)[1]
check(all(dl[(a, b)] == rule(a, b) for a, b in combinations(N, 2)), 'P8: loops {0,4},{2,6},{1,5},{3,7}@2, evens/odds@4, all@8 realise the rules')
need8 = sorted(lab.values())
say(f'  labels the P8 world needs: {need8}; printed label cards: {DATA["label_cards"]}')
pc = DATA['label_cards']
check(all(need8.count(int(k)) <= v for k, v in pc.items()), 'P8: printed label cards suffice for the number world')
b3 = sorted({tuple(x for x in N if rule(c, x) <= 3) for c in N})
b5 = sorted({tuple(x for x in N if rule(c, x) <= 5) for c in N})
say(f'  radius-3 balls: {b3}\n  radius-5 balls: {b5}')
check(b3 == [(0, 4), (1, 5), (2, 6), (3, 7)] and b5 == [(0, 2, 4, 6), (1, 3, 5, 7)], 'P8 balls as in the guide')
# 2-adic strong inequality on a wider range
check(all(2 ** -v2(a - c) <= max(2 ** -v2(a - b), 2 ** -v2(b - c))
          for a in range(-20, 21) for b in range(-20, 21) for c in range(-20, 21)
          if len({a, b, c}) == 3), '2-adic strong inequality on -20..20 (overview)')

# ---------------------------------------------------------------- P10
say('\n== Problem 10: question game ==')
pairs6 = [a + b for a, b in combinations('ABCDEF', 2)]
tabs6 = realizable_tables('ABCDEF')
all8 = {p: 8 for p in pairs6}
check(tuple(sorted(all8.items())) in tabs6, 'all-8 world is allowed')
check(all(tuple(sorted({**all8, p: 2}.items())) in tabs6 for p in pairs6),
      'for every pair, the world with just that pair at 2 is allowed (guide adversary)')
check(sum(1 for t in tabs6 if all(dict(t)['A' + x] == 2 for x in 'BCDEF')) == 1,
      'guide: A at 2 from all five others forces the all-2 world')
check(all(dict(t)['BC'] == 4 for t in tabs6 if dict(t)['AB'] == 2 and dict(t)['AC'] == 4),
      'guide: AB=2 and AC=4 force BC=4')


def minimax(n):
    cards = 'ABCDEF'[:n]
    pairs = [a + b for a, b in combinations(cards, 2)]
    tabs = [dict(t) for t in realizable_tables(cards)]

    @lru_cache(maxsize=None)
    def solve(cands):
        cs = [tabs[i] for i in cands]
        if len(cs) == 1:
            return 0
        best = None
        for p in pairs:
            vals = {c[p] for c in cs}
            if len(vals) == 1:
                continue
            worst = 0
            for v in vals:
                sub = tuple(i for i in cands if tabs[i][p] == v)
                worst = max(worst, 1 + solve(sub))
                if best is not None and worst >= best:
                    break
            if best is None or worst < best:
                best = worst
        return best

    return solve(tuple(range(len(tabs))))


for n in (3, 4, 5):
    m = minimax(n)
    check(m == n * (n - 1) // 2, f'exact worst-case questions for {n} cards = {m} = all pairs')

# label supply for Problem 10 worlds (non-redundant loops)
short = []
for lab, d in W6:
    labs = list(lab.values())
    if any(labs.count(int(k)) > v for k, v in DATA['label_cards'].items()):
        short.append(lab)
need_by_table = {}
for lab, d in W6:
    key = tuple(sorted(d.items()))
    labs = list(lab.values())
    over = any(labs.count(int(k)) > v for k, v in DATA['label_cards'].items())
    need_by_table[key] = need_by_table.get(key, True) and over
nshort = sum(1 for v in need_by_table.values() if v)
say(f'  6-card worlds whose loops need more label cards than one page-1 set supplies: {nshort} of {len(need_by_table)}')
for lab in short[:3]:
    say('    e.g. ' + ', '.join(f'{"".join(sorted(s))}@{v}' for s, v in sorted(lab.items(), key=lambda kv: kv[1])))

say()
say('FAILS: ' + (', '.join(FAILS) if FAILS else 'none'))
(HERE / 'check_math.py.out').write_text('\n'.join(OUT) + '\n')
