#!/usr/bin/env python3
"""Independent check of every answer and claim printed in draft/k1-guide.pdf
(Week 87 K-1 adult guide), against the final student pages k-1.pdf.

Written by the reviewer without reading the writer's check_guide.py.
Card sets are read from the student PDF itself (large letters inside the
printed cards), and compared with the sets the guide prints.
Run: python3 verify.py [path/to/k-1.pdf] [path/to/week-87-materials.pdf]
"""
import itertools, sys, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
K1 = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'plans/k1-drafts/week-87/k-1.pdf')
MAT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, 'lowell-math-circle-year-2/week-87/week-87-materials.pdf')

fails = []
def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        fails.append(msg)

# ---------- voting model ----------
def pair(cards, x, y):
    """Each card votes for whichever of x, y is higher (earlier) on it."""
    vx = [i + 1 for i, c in enumerate(cards) if c.index(x) < c.index(y)]
    vy = [i + 1 for i, c in enumerate(cards) if c.index(y) < c.index(x)]
    assert len(vx) != len(vy)
    return (x, vx, vy) if len(vx) > len(vy) else (y, vy, vx)

def knockout(cards, first, wait):
    w1 = pair(cards, *first)[0]
    return w1, pair(cards, w1, wait)[0]

def winners(cards, letters='ABC'):
    out = {}
    for wait in letters:
        a, b = [l for l in letters if l != wait]
        out[wait] = knockout(cards, (a, b), wait)
    return out

def beats_both(cards, x, letters='ABC'):
    return all(pair(cards, x, y)[0] == x for y in letters if y != x)

PERMS = [''.join(p) for p in itertools.permutations('ABC')]

# ---------- read card sets from the student PDF ----------
try:
    import fitz
    doc = fitz.open(K1)
    check(doc.page_count == 6, f'student packet has 6 pages (found {doc.page_count})')
    def big_letters(pno, min_size, ymin=0, ymax=1e9):
        pts = []
        for b in doc[pno].get_text('dict')['blocks']:
            for l in b.get('lines', []):
                for s in l['spans']:
                    t = s['text'].strip()
                    if len(t) == 1 and t in 'ABCDEF' and s['size'] >= min_size and ymin <= s['bbox'][1] <= ymax:
                        pts.append((s['bbox'][0], s['bbox'][1], t))
        return pts
    def cards_from(pts, ncards=3):
        xs = sorted(set(round(p[0] / 25) for p in pts))
        cols = {}
        for x, y, t in pts:
            cols.setdefault(round(x / 25), []).append((y, t))
        keys = sorted(cols)[:ncards]
        return [''.join(t for y, t in sorted(cols[k])) for k in keys]
    pdf_sets = {}
    pdf_sets['launch'] = cards_from(big_letters(0, 14, 0, 250))       # small card pictures on p.1 top
    pdf_sets['P1'] = cards_from([p for p in big_letters(0, 30, 350, 800) if p[0] < 370])
    pdf_sets['P3'] = cards_from(big_letters(2, 40, 100, 400))
    pdf_sets['P4'] = cards_from(big_letters(3, 40, 100, 400))
    pdf_sets['P5'] = cards_from(big_letters(4, 20, 100, 300))
    for k, v in pdf_sets.items():
        print(f'     cards read from PDF for {k}: {v}')
except Exception as e:  # pragma: no cover
    print('could not read PDF:', e)
    pdf_sets = {}

FIXED = ['ABC', 'BCA', 'CAB']
P3 = ['CBA', 'BAC', 'CBA']
P4 = ['ABC', 'BAC', 'CAB']
LAUNCH = ['DFE', 'EFD', 'FED']
if pdf_sets:
    check(pdf_sets['launch'][:3] == LAUNCH, 'launch picture cards are DFE, EFD, FED')
    check(pdf_sets['P1'] == FIXED, 'P1 printed cards are ABC, BCA, CAB')
    check(pdf_sets['P3'] == P3, 'P3 printed cards are CBA, BAC, CBA (guide heading)')
    check(pdf_sets['P4'] == P4, 'P4 printed cards are ABC, BAC, CAB (guide heading)')
    check(pdf_sets['P5'] == FIXED, 'P5 printed cards are ABC, BCA, CAB (guide: "pictured original cards")')

# ---------- launch / table demonstration ----------
w, sup, opp = pair(LAUNCH, 'D', 'E')
check((w, sup, opp) == ('E', [2, 3], [1]), 'demo: D or E -> E, V2 and V3 for E, V1 for D (guide p.2 tally)')
w, sup, opp = pair(LAUNCH, 'E', 'F')
check((w, len(sup), len(opp)) == ('F', 2, 1), 'demo knockout final: F beats E 2-1')
check(knockout(LAUNCH, ('D', 'E'), 'F') == ('E', 'F'), 'demo knockout D/E first, F waits: E then F')
check(beats_both(LAUNCH, 'F', 'DEF'), 'demo cards: F beats both, no circle (guide: "one fixed winner, not a cycle")')
demo_pairs = {frozenset(p): pair(LAUNCH, *p)[0] for p in itertools.combinations('DEF', 2)}
check(len(set(demo_pairs.values())) < 3, 'demo pair results are not a circle')

# ---------- Problem 1 ----------
res = {p: pair(FIXED, *p) for p in [('A', 'B'), ('B', 'C'), ('C', 'A')]}
check([res[p][0] for p in res] == ['A', 'B', 'C'], 'P1 circle A, B, C')
check(res[('A', 'B')][1] == [1, 3] and res[('B', 'C')][1] == [1, 2] and res[('C', 'A')][1] == [2, 3],
      'P1 supporters: A/B by V1,V3; B/C by V1,V2; C/A by V2,V3')
check(not any(beats_both(FIXED, x) for x in 'ABC'), 'P1: no letter beats both')

# ---------- Problem 2 ----------
p2 = [(('B', 'C'), 'A', 'B', 'A'), (('C', 'A'), 'B', 'C', 'B'), (('A', 'B'), 'C', 'A', 'C')]
for first, wait, fw, fin in p2:
    check(knockout(FIXED, first, wait) == (fw, fin), f'P2 first {first} wait {wait}: first winner {fw}, winner {fin}')
    check(knockout(FIXED, first[::-1], wait) == (fw, fin), f'P2 reversing {first} changes nothing')
allvotes = [pair(FIXED, *first) for first, *_ in p2] + [pair(FIXED, fw, wait) for first, wait, fw, fin in p2]
check(all(len(v[1]) == 2 for v in allvotes), 'P2 every vote is 2-1')

# ---------- Problem 3 ----------
check(pair(P3, 'C', 'A')[:2] == ('C', [1, 3]) and pair(P3, 'C', 'B')[:2] == ('C', [1, 3]),
      'P3: C beats A and B, each 2-1, using V1 and V3')
check(pair(P3, 'B', 'A')[:2] == ('B', [1, 2, 3]), 'P3: B beats A 3-0')
check(winners(P3) == {'A': ('C', 'C'), 'B': ('C', 'C'), 'C': ('B', 'C')},
      'P3 knockouts: A waits C then C; B waits C then C; C waits B then C')
check({fin for _, fin in winners(P3).values()} == {'C'}, 'P3 answer: C only')

# ---------- Problem 4 ----------
check(pair(P4, 'A', 'B')[:2] == ('A', [1, 3]) and pair(P4, 'A', 'C')[:2] == ('A', [1, 2])
      and pair(P4, 'B', 'C')[:2] == ('B', [1, 2]), 'P4: A beats B (V1/V3), A beats C (V1/V2), B beats C (V1/V2), each 2-1')
check(winners(P4) == {'A': ('B', 'A'), 'B': ('A', 'A'), 'C': ('A', 'A')},
      'P4 knockouts: waiting A gives B then A; waiting B gives A then A; waiting C gives A then A')
check(sorted(c[0] for c in P4) == ['A', 'B', 'C'], 'P4: each letter first on one card')
diff = [i for i in range(3) if P4[i] != FIXED[i]]
check(diff == [1] and sorted(P4[1]) == sorted(FIXED[1]) and
      sum(a != b for a, b in zip(P4[1], FIXED[1])) == 2 and set(c for a, c in zip(P4[1], FIXED[1]) if a != c) == {'A', 'C'},
      'P4 differs from P1 only by V2 exchanging A and C')

# ---------- Problem 5 ----------
def swaps(card):
    for i, j in itertools.combinations(range(3), 2):
        s = list(card); s[i], s[j] = s[j], s[i]
        yield ''.join(s), {card[i], card[j]}, card[j]  # moved-up letter is card[j]
working = []
moved_up_rule = True
for v in range(3):
    for new, pairset, up in swaps(FIXED[v]):
        cards = FIXED[:]; cards[v] = new
        fins = {fin for _, fin in winners(cards).values()}
        if not (len(fins) == 1 and fins == {up} and beats_both(cards, up)):
            moved_up_rule = False
        if fins == {'C'}:
            working.append((v + 1, new, ''.join(sorted(pairset)), pair(cards, 'C', 'A'), pair(cards, 'C', 'B')))
order = {(1, 'ACB'): 0, (1, 'CBA'): 1, (2, 'CBA'): 2}   # the guide's printed order
working.sort(key=lambda w: order.get((w[0], w[1]), 9))
for wk in working:
    print('     P5 working swap:', wk[:3], 'C/A', wk[3], 'C/B', wk[4])
check([(v, n) for v, n, *_ in working] == [(1, 'ACB'), (1, 'CBA'), (2, 'CBA')],
      'P5: exactly V1->ACB, V1->CBA, V2->CBA (3 of 9 swaps)')
check([len(w[3][1]) for w in working] == [2, 3, 2] and all(len(w[4][1]) == 2 for w in working),
      'P5: C beats A 2-1, 3-0, 2-1 and C beats B 2-1 in each')
check(moved_up_rule, 'P5 (not in guide): every one of the 9 swaps makes the letter that moved up the only winner')
# reason offered in the review: every swap on the fixed cards carries the moved-up letter past
# the letter that beat it in the circle, and moving up never costs a letter a vote
beater = {x: pair(FIXED, x, y)[0] for x in 'ABC' for y in 'ABC' if x != y and pair(FIXED, x, y)[0] != x}
passes = True
for v in range(3):
    for new, pairset, up in swaps(FIXED[v]):
        old = FIXED[v]
        passed = {y for y in 'ABC' if y != up and old.index(y) < old.index(up) and new.index(up) < new.index(y)}
        if beater[up] not in passed:
            passes = False
check(passes, 'P5 reason: each of the 9 swaps carries the moved-up letter past the letter that beat it')
moved_up_C = []
for v in range(3):
    for new, pairset, up in swaps(FIXED[v]):
        if up == 'C': moved_up_C.append((v + 1, new))
check(sorted(moved_up_C) == [(1, 'ACB'), (1, 'CBA'), (2, 'CBA')], 'P5: the working swaps are exactly the swaps that move C up')
# hint: "Which card could change its vote between B and C?" -> V1, V2 have B above C
check([i + 1 for i, c in enumerate(FIXED) if c.index('B') < c.index('C')] == [1, 2], 'P5 hint: V1 and V2 vote B over C originally')

# ---------- Problems 6-8: all ordered and unordered card sets ----------
ordered = list(itertools.product(PERMS, repeat=3))
def B_wins_all(cards):
    return {fin for _, fin in winners(list(cards)).values()} == {'B'}
check(B_wins_all(['BAC', 'BCA', 'ABC']), 'P6 example BAC, BCA, ABC: B wins all three knockouts')
check(pair(['BAC', 'BCA', 'ABC'], 'B', 'A')[1] == [1, 2] and len(pair(['BAC', 'BCA', 'ABC'], 'B', 'C')[1]) == 3,
      'P6 example: B beats A 2-1 and C 3-0')
nfirst = lambda cs: sum(c[0] == 'B' for c in cs)
check(all(B_wins_all(cs) for cs in ordered if nfirst(cs) >= 2), 'P6/overview: B first on 2 or 3 cards always works')
print('     P6: ordered sets where B wins every knockout:', sum(B_wins_all(cs) for cs in ordered), 'of 216')
multisets = sorted(set(tuple(sorted(cs)) for cs in ordered))
one = [m for m in multisets if nfirst(m) == 1]
one_ok = [m for m in one if B_wins_all(m)]
print(f'     P7: {len(one_ok)} of {len(one)} card sets with B first exactly once work: {one_ok}')
check(one_ok == [('ABC', 'BAC', 'CBA'), ('ABC', 'BCA', 'CBA')], 'P7: only {ABC,BAC,CBA} and {ABC,BCA,CBA}')
check(all(B_wins_all(p) for m in one_ok for p in itertools.permutations(m)), 'P7: any assignment to V1-V3 works')
for m in one_ok:
    check(len(pair(list(m), 'B', 'A')[1]) == 2 and len(pair(list(m), 'B', 'C')[1]) == 2, f'P7 {m}: B beats A and C, both 2-1')
none = [m for m in multisets if nfirst(m) == 0]
check(not any(B_wins_all(m) for m in none), f'P8: none of the {len(none)} card sets with B never first works')
check(all(sum(c.index('B') < c.index(x) for x in 'AC') <= 1 for c in PERMS if c[0] != 'B'),
      'P8 loops: a card without B first puts B above at most one rival')

# ---------- overview general claims ----------
claim_iff = all(
    ({fin for _, fin in winners(list(cs)).values()} == {x}) == beats_both(list(cs), x)
    for cs in ordered for x in 'ABC')
check(claim_iff, 'overview: a letter wins every knockout iff it beats both (all 216 profiles)')
cyc = [cs for cs in ordered if not any(beats_both(list(cs), x) for x in 'ABC')]
check(len(cyc) == 12, f'outline/overview: 12 of 216 profiles are circles (found {len(cyc)})')
dich = all(
    ({fin for _, fin in winners(list(cs)).values()} == set('ABC')) if cs in cyc
    else len({fin for _, fin in winners(list(cs)).values()}) == 1 for cs in ordered)
check(dich, 'dichotomy (not stated in guide overview): circle -> each letter wins by waiting; otherwise exactly one letter can ever win')
check(all(all(winners(list(cs))[w][1] == w for w in 'ABC') for cs in cyc), 'in every circle the waiting letter wins')

# ---------- materials and pages ----------
mm = 25.4 / 72
try:
    md = fitz.open(MAT)
    def rects(page):
        return sorted({(round(r.width * mm, 1), round(r.height * mm, 1)) for r in (d['rect'] for d in md[page].get_drawings())
                       if r.width * mm > 8 and r.height * mm > 8})
    r1, r2, r4 = rects(0), rects(1), rects(3)
    check((45.0, 80.0) in r1 and (28.0, 28.0) in r1 and (18.0, 18.0) in r1, 'materials p.1: 45x80 cards, 28 mm tiles, 18 mm tokens')
    check((45.0, 80.0) in r2 and (21.0, 21.0) in r2, 'materials p.2: 45x80 blank cards, 21 mm slips')
    check((170.0, 90.0) in r4 and (54.0, 54.0) in r4 and (175.0, 100.0) in r4, 'materials p.4: 170x90 tally mat, 54 mm wells, 175x100 knockout mat')
    # card row heights on blank cards: horizontal lines inside first card
    ys = set()
    for d in md[1].get_drawings():
        for it in d['items']:
            if it[0] == 'l':
                a, b = it[1], it[2]
                if abs(a.y - b.y) < 0.1 and a.x * mm < 75 and a.y * mm < 135:
                    ys.add(round(a.y * mm, 1))
            elif it[0] == 're':
                r = it[1]
                if r.x0 * mm < 75 and r.y0 * mm < 135 and r.width * mm > 40:
                    ys.update({round(r.y0 * mm, 1), round(r.y1 * mm, 1)})
    ys = sorted(ys)
    print('     materials p.2 first card horizontal edges (mm):', ys, 'gaps', [round(b - a, 1) for a, b in zip(ys, ys[1:])])
    slips = sum(1 for d in md[1].get_drawings() if round(d['rect'].width * mm) == 21 and round(d['rect'].height * mm) == 21)
    check(slips == 18, f'materials p.2: 18 slips (found {slips})')
    txt = md[0].get_text()
    check(all(t in txt for t in ['V4', 'V5']), 'materials p.1 prints V4 and V5 tokens (guide: set aside)')
    allt = ''.join(md[i].get_text() for i in range(md.page_count))
    check(not any(f' {x}\n' in allt or f'\n{x}\n' in allt for x in 'DEF'), 'no week materials page prints movable D/E/F tiles (guide p.2)')
except Exception as e:
    print('materials check skipped:', e)

# student page geometry the guide refers to
pg = lambda i: sorted({(round(d['rect'].width * mm, 1), round(d['rect'].height * mm, 1)) for d in doc[i].get_drawings() if d['rect'].width * mm > 8})
check((45.0, 80.0) in pg(2) and (45.0, 80.0) in pg(3), 'P3, P4 pictures are full-size 45x80 cards (guide: "full-size pictures")')
check((22.5, 40.0) in pg(4) and (22.5, 40.0) in pg(5), 'P6-P8 frames are half-size 22.5x40 (slips cannot fit; guide: pencil records)')
check((27.0, 48.0) in pg(4), 'P5 pictured cards are 27x48 (60 percent), so children use the cut cards')

# pacing
route = [5, 5, 5, 10, 15, 15, 5]
check(sum(route) == 60, f'one-hour route sums to {sum(route)}')

print()
print('FAILURES:', len(fails))
for f in fails: print('  ', f)
