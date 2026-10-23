#!/usr/bin/env python3
"""Check the claims added or changed by the October 23, 2026 card fixes for Week 100.

    python3 checks/card_fixes_2026_10_23.py [folder with week-100-*.pdf]

Mathematics (standard library): Problem 4's new question (one loop structure fits the
ten clues; repeated or one-card loops change no distance), Problem 5's three repairs
under the reworded "these ten clues, with A-C = 2", the K-1 route key, loop counts,
the third 4-label for Problem 10 and the cord-length estimates. With a PDF folder
(default ../../week-100) it also reads the printed wording and footers (PyMuPDF).
"""
import sys
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path

fails = []


def check(ok, what):
    print(('PASS ' if ok else 'FAIL ') + what)
    if not ok:
        fails.append(what)


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
    """Loop trees on frozenset `cards`, every loop with two or more children."""
    out = []
    for p in set_partitions(sorted(cards)):
        if len(p) < 2:
            continue
        opts = [[frozenset(b)] if len(b) == 1 else trees(frozenset(b)) for b in p]
        for ch in product(*opts):
            out.append((cards, ch))
    return tuple(out)


def labelings(t, labels, above=None):
    if isinstance(t, frozenset):
        yield {}
        return
    for lab in labels:
        if above is not None and lab >= above:
            continue
        for combo in product(*[list(labelings(c, labels, lab)) for c in t[1]]):
            d = {t[0]: lab}
            for x in combo:
                d.update(x)
            yield d


def dist_of(loops, cards):
    """loops: list of (card set, label); distance = label of the smallest common loop."""
    return {a + b: min((len(s), v) for s, v in loops if a in s and b in s)[1]
            for a, b in combinations(sorted(cards), 2)}


def worlds(cards, labels=(2, 4, 8)):
    return [(lab, dist_of(list(lab.items()), cards))
            for t in trees(frozenset(cards)) for lab in labelings(t, labels)]


def tables(cards, labels=(2, 4, 8)):
    return {tuple(sorted(d.items())) for _, d in worlds(cards, labels)}


def name(lab):
    return ', '.join(f'{"".join(sorted(s))}@{v}' for s, v in sorted(lab.items(), key=lambda kv: (kv[1], sorted(kv[0]))))


# Problem 4: the printed clues and the new question
clues = {'AB': 2, 'AC': 4, 'BC': 4, 'DE': 2, 'AD': 8, 'AE': 8, 'BD': 8, 'BE': 8, 'CD': 8, 'CE': 8}
W5 = worlds('ABCDE')
fits = [lab for lab, d in W5 if d == clues]
check(len(W5) == 358 and len(fits) == 1, f'P4: {len(fits)} of {len(W5)} five-card loop structures fits the ten clues: {name(fits[0])}')
check(len([lab for lab, d in worlds('ABCDE', tuple(range(1, 9))) if d == clues]) == 1,
      'P4: still one structure if any labels 1-8 were allowed')
base = list(fits[0].items())
extra = base + [(frozenset('DE'), 4)]
check(dist_of(extra, 'ABCDE') == clues, 'P4 key: a second loop labelled 4 around D and E changes no distance')
for c in 'ABCDE':
    check(dist_of(base + [(frozenset(c), 1)], 'ABCDE') == clues, f'P4 key: a loop around {c} alone changes no distance')
for r, parts in ((2, ['AB', 'C', 'DE']), (4, ['ABC', 'DE']), (8, ['ABCDE'])):
    classes = {frozenset(x for x in 'ABCDE' if x == y or clues.get(''.join(sorted(x + y)), 0) <= r) for y in 'ABCDE'}
    check(sorted(''.join(sorted(s)) for s in classes) == parts, f'P4 key: joining cards with clue at most {r} gives {", ".join(parts)}')

# Problem 5: "Change exactly one of these ten clues, with A-C = 2"
t5 = tables('ABCDE')
broken = {**clues, 'AC': 2}
check(tuple(sorted(broken.items())) not in t5, 'P5: with A-C = 2 no world fits')
reps = [f'{k}:{broken[k]}->{v}' for k in sorted(broken) for v in (2, 4, 8)
        if v != broken[k] and tuple(sorted({**broken, k: v}.items())) in t5]
check(reps == ['AB:2->4', 'AC:2->4', 'BC:4->2'], f'P5: exactly three repairs of the A-C = 2 set: {reps}')

# K-1 route: one small loop (close) inside one big loop (far) on circle, triangle, square
def k1_possible(ct, cs, ts):
    """Can the triple (circle-triangle, circle-square, triangle-square) be made?"""
    cards = 'cts'
    ok = False
    for small in [frozenset()] + [frozenset(x) for n in (2, 3) for x in combinations(cards, n)]:
        loops = [(frozenset(cards), 'far')] + ([(small, 'close')] if small else [])
        d = dist_of([(s, 1 if v == 'close' else 2) for s, v in loops], cards)
        ok |= (d['ct'], d['cs'], d['st']) == tuple(1 if x == 'close' else 2 for x in (ct, cs, ts))
    return ok

check(not k1_possible('close', 'close', 'far'), 'K-1 key: close, close, far cannot be made')
for trip in (('close', 'far', 'far'), ('far', 'far', 'far'), ('close', 'close', 'close')):
    check(k1_possible(*trip), f'K-1 key: {", ".join(trip)} can be made')
check(tables('ABC', (1, 2)) == {tuple(sorted(zip(('AB', 'AC', 'BC'), t))) for t in
      [(1, 1, 1), (2, 2, 2), (1, 2, 2), (2, 1, 2), (2, 2, 1)]},
      'K-1 key: with two labels and any number of loops, only the three listed kinds of triple occur')

# Loop counts and label supply
check(len(base) == 4, 'Per pair: the Problem 4 world uses 4 loops')
p1 = {frozenset('AB'): 2, frozenset('ABD'): 4, frozenset('CE'): 2, frozenset('ABCDEF'): 8}
check(len(p1) == 4 and dist_of(list(p1.items()), 'ABCDEF')['CE'] == 2, 'Per pair: the Problem 1 world uses 4 loops')
p8 = [frozenset(s) for s in ('04', '26', '15', '37', '0246', '1357', '01234567')]
check(len(p8) == 7, 'Per pair: the Problem 8 number world uses 7 loops')
W6 = worlds('ABCDEF')
check(len(W6) == 2471 and max(len(lab) for lab, _ in W6) == 5, 'Per pair: 2,471 six-card worlds, at most 5 loops each')
supply = {2: 4, 4: 2, 8: 2}
short = [lab for lab, _ in W6 if any(list(lab.values()).count(k) > n for k, n in supply.items())]
check(len(short) == 15 and all(list(lab.values()).count(4) == 3 for lab in short)
      and all(list(lab.values()).count(k) <= n for lab in short for k, n in {2: 4, 4: 3, 8: 2}.items()),
      'Per pair: 15 secret worlds exceed one page-1 label set, each needing just a third 4')

# Cord estimates: rounded-rectangle model, 27 mm cards, 6 mm gaps and margins
CARD, GAP = 27, 6
pair = (2 * CARD + GAP + 2 * GAP, CARD + 2 * GAP)
four = (2 * pair[0] + GAP + 2 * GAP, pair[1] + 2 * GAP)
eight = (four[0] + 2 * GAP, 2 * four[1] + GAP + 2 * GAP)
per = {k: 2 * (w + h) for k, (w, h) in (('pair', pair), ('four', four), ('eight', eight))}
print('     loop perimeters in mm (rectangle model):', per, '; eight-card loop', eight, 'mm')
check(per['pair'] <= 260 and per['four'] <= 460 and per['eight'] <= 660,
      'Per pair: about 30, 50 and 70 cm of cord leave at least 4 cm for a knot')
check(eight[0] <= 250 and eight[1] <= 180, 'Per pair: the eight-card world fits the 250 x 180 mm page-8 frame')

# Printed wording and footers
folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[3] / 'week-100'
try:
    import pymupdf as fitz
except ImportError:
    import fitz
sp = ' '.join(' '.join(p.get_text().split()) for p in fitz.open(folder / 'week-100-grades-3-5.pdf'))
gp = ' '.join(' '.join(p.get_text().split()) for p in fitz.open(folder / 'week-100-facilitator.pdf'))
for q in ['Draw your world. Could a world with different groups fit the same ten clues?',  # 'loops around different sets of cards' until the critic follow-up (v3)
          'Change exactly one of these ten clues, with A–C = 2, to a different value chosen from 2, 4, 8',
          'Then the builder shows the secret world: if any distance in the drawing is different, the round is lost.']:
    check(q in sp, f'student packet: "{q[:60]}..."')
check('two different-looking' not in sp, 'student packet: the old P4 question is gone')
check(sp.count('W100-G35-v3') == 8 and 'v1' not in sp, 'student packet: eight W100-G35-v3 footers (v2 until the critic follow-up)')
check(gp.count('W100-FAC-v2') == 5 and 'FAC-v1' not in gp, 'guide: five W100-FAC-v2 footers')
check('on page 1' not in gp and gp.count('in the mathematical overview') == 2, 'guide: both proofs point to the mathematical overview')
for q in ['K–1 route, adult-led', 'First route: Problems 1–4; return visits: Problems 5–10.',
          'The final question’s answer is no.', 'any distance in the asker’s drawing that differs loses the round',
          'write a third 4', 'two balls that partly overlap']:
    check(q in gp, f'guide: "{q}"')

print('\nFAILS: ' + (', '.join(fails) if fails else 'none'))
sys.exit(1 if fails else 0)
