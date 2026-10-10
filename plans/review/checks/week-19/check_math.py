"""Independent finite checks for Week 19 (no card inside another: antichains).

Own code only: no packet builder, checker or answer file is imported.
Printed decks come from pdf_decks.json (written by extract_pdf.py from the
delivered PDFs). Guide claims are quoted from the delivered guide PDFs, and
each quote is first confirmed to appear in the guide text.

Cards are frozensets of letters: A circle, B triangle, C square, D star.
"X fits inside Y" means X is a subset of Y. A legal collection is a set of
distinct cards with no card a subset of another (an antichain).
"""
import itertools
import json
import re
import subprocess

from repo import HERE, PDF

FAILS = []


def ok(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def card(s):
    s = s.strip()
    return frozenset() if s in ('', 'empty') else frozenset(s)


def name(c):
    return ''.join(sorted(c)) or 'empty'


def names(cs):
    return '/'.join(name(c) for c in sorted(cs, key=lambda c: (len(c), sorted(c))))


def comparable(x, y):
    return x <= y or y <= x


def legal(coll):
    coll = list(coll)
    if len(set(coll)) != len(coll):
        return False
    return all(not comparable(a, b) for a, b in itertools.combinations(coll, 2))


def antichains(deck):
    """All antichains (including the empty family) by backtracking."""
    deck = list(dict.fromkeys(deck))
    out = []

    def rec(i, cur):
        if i == len(deck):
            out.append(tuple(cur))
            return
        rec(i + 1, cur)
        if all(not comparable(deck[i], c) for c in cur):
            cur.append(deck[i])
            rec(i + 1, cur)
            cur.pop()
    rec(0, [])
    return out


def max_antichains(deck):
    ants = antichains(deck)
    m = max(map(len, ants))
    return m, [frozenset(a) for a in ants if len(a) == m]


def min_chain_partition(deck):
    """Minimum number of chains covering each card exactly once.
    Minimum path cover of the strict-containment DAG = n - maximum matching
    (the DAG is transitive, so a path cover is a chain partition)."""
    deck = list(dict.fromkeys(deck))
    n = len(deck)
    adj = {i: [j for j in range(n) if deck[i] < deck[j]] for i in range(n)}
    match_r = {}

    def aug(u, seen):
        for v in adj[u]:
            if v in seen:
                continue
            seen.add(v)
            if v not in match_r or aug(match_r[v], seen):
                match_r[v] = u
                return True
        return False
    m = sum(aug(u, set()) for u in range(n))
    return n - m


def chain_partition_brute(deck, k):
    """True if the deck can be split into at most k chains (exhaustive search)."""
    deck = sorted(dict.fromkeys(deck), key=len)
    rows = []

    def rec(i):
        if i == len(deck):
            return True
        c = deck[i]
        for r in rows:
            if r[-1] < c:  # cards placed in order of size: append to the top
                r.append(c)
                if rec(i + 1):
                    return True
                r.pop()
        if len(rows) < k:
            rows.append([c])
            if rec(i + 1):
                return True
            rows.pop()
        return False
    return rec(0)


def valid_partition(deck, rows):
    flat = [c for r in rows for c in r]
    cover = sorted(map(name, flat)) == sorted(map(name, deck)) and len(flat) == len(set(flat))
    nested = all(a < b for r in rows for a, b in zip(r, r[1:]))
    return cover and nested


def parse_rows(text, sep='/'):
    return [[card(x) for x in r.strip().split(sep)] for r in text.split(';')]


def full_deck(letters):
    return [frozenset(s) for k in range(len(letters) + 1) for s in itertools.combinations(letters, k)]


# ------------------------------------------------------------------ guide text
def pdf_text(path):
    t = subprocess.run(['pdftotext', str(path), '-'], capture_output=True, text=True, check=True).stdout
    return re.sub(r'\s+', ' ', t)


GUIDE = pdf_text(PDF['guide'])
BGUIDE = pdf_text(PDF['bonus-guide'])
BONUS = pdf_text(PDF['bonus'])
STUDENT = {b: pdf_text(PDF[b]) for b in ('K-1', '2-3', '4-5')}


def quote(q, text=None, where='guide'):
    text = GUIDE if text is None else text
    found = re.sub(r'\s+', ' ', q) in text
    ok(found, f'{where} quote present: "{q[:90]}"')
    return found


# ------------------------------------------------------------------ printed decks
D = json.loads((HERE / 'pdf_decks.json').read_text())


def groups(band, prob):
    out = []
    for pg in D[band]:
        out += pg['decks'].get(str(prob), [])
    return [[card(c['card']) for c in g] for g in out]


D2 = full_deck('AB')
D3 = full_deck('ABC')
D4 = full_deck('ABCD')


def is_deck(g, full):
    return sorted(map(name, g)) == sorted(map(name, full)) and len(g) == len(full)


print('=' * 70)
print('Printed decks')
for band in ('K-1', '2-3', '4-5'):
    for pg in D[band]:
        for pn, gs in pg['decks'].items():
            for g in gs:
                cs = [card(c['card']) for c in g]
                kind = ('full 2-symbol deck' if is_deck(cs, D2) else 'full 3-symbol deck' if is_deck(cs, D3)
                        else 'full 4-symbol deck' if is_deck(cs, D4) else 'group ' + names(cs))
                print(f'  {band} p{pg["page"]} P{pn}: {len(cs)} cards = {kind}')

# ------------------------------------------------------------------ general facts
print('=' * 70)
print('General facts')
for letters, mx in (('AB', 2), ('ABC', 3), ('ABCD', 6)):
    deck = full_deck(letters)
    m, best = max_antichains(deck)
    ok(m == mx, f'{len(letters)} symbols: largest antichain {m} (guide: {mx})')
    ok(min_chain_partition(deck) == mx, f'{len(letters)} symbols: fewest nested rows {min_chain_partition(deck)}')
    ok(chain_partition_brute(deck, mx) and not chain_partition_brute(deck, mx - 1),
       f'{len(letters)} symbols: exhaustive row search agrees ({mx} possible, {mx - 1} impossible)')
    print(f'    largest collections: {[names(b) for b in best]}')
ants = {n: len(antichains(full_deck('ABCD'[:n]))) for n in (2, 3, 4)}
ok(ants == {2: 6, 3: 20, 4: 168}, f'legal collections incl. zero-card family: {ants} (guide: 6, 20, 168)')
quote('It finds 6, 20, and 168 legal collections including the zero-card family for two, three, and four symbols, and maxima 2,3,6.')
quote('For the full two-, three- and four-symbol decks the maxima are 2, 3 and 6')
m, best = max_antichains(D4)
ok(len(best) == 1 and best[0] == frozenset(c for c in D4 if len(c) == 2), 'four symbols: unique six-card collection = all two-symbol cards')
quote('On four symbols the unique six-card antichain is the family of all two-symbol cards.')
from math import comb
for n in range(1, 6):
    m, best = max_antichains(full_deck('ABCDE'[:n]))
    ok(m == comb(n, n // 2), f'Sperner n={n}: max {m} = C({n},{n // 2})')
# complement preserves antichains (guide p. 11 extension)
for letters in ('ABC', 'ABCD'):
    U = frozenset(letters)
    allok = all(legal([U - c for c in a]) for a in antichains(full_deck(letters)))
    ok(allok, f'complementing every card of a legal collection keeps it legal ({len(letters)} symbols)')

# ------------------------------------------------------------------ K-1
print('=' * 70)
print('K-1')
gs = groups('K-1', 1)
ok(len(gs) == 4, 'P1 has four groups')
want = ['A/B', 'A/B', 'AB/AC/BC', 'A/BC']
for i, g in enumerate(gs):
    m, best = max_antichains(g)
    ok(len(best) == 1 and names(best[0]) == want[i], f'P1 group {i + 1} [{names(g)}]: largest {m}, unique = {[names(b) for b in best]}')
quote('In printed order, choose A/B (size 2); A/B (size 2); AB/AC/BC (size 3); A/BC (size 2). These are the unique largest choices in their respective pictured groups.')

g = groups('K-1', 2)[0]
ok(is_deck(g, D2), 'P2 deck is the full two-symbol deck')
ne = [a for a in antichains(g) if a]
ok(len(ne) == 5, f'P2: {len(ne)} collections of one or more cards: {[names(a) for a in ne]}')
quote('There are five: empty alone; A alone; B alone; AB alone; and A/B.')

g = groups('K-1', 3)[0]
ok(is_deck(g, D3), 'P3 deck is the full three-symbol deck')
two = sorted(names(a) for a in antichains(g) if len(a) == 2)
ok(len(two) == 9, f'P3: {len(two)} two-card collections: {two}')
guide9 = 'A/B, A/C, B/C; AB/AC, AB/BC, AC/BC; A/BC, B/AC, C/AB'
quote('The full list of nine is ' + guide9)
ok(sorted(names([card(x) for x in p.strip().split('/')]) for p in re.split('[,;]', guide9)) == two, 'P3: guide list equals enumeration')

g = groups('K-1', 4)[0]
ok(is_deck(g, D3), 'P4 deck is the full three-symbol deck')
m, best = max_antichains(g)
ok(m == 3 and sorted(names(b) for b in best) == ['A/B/C', 'AB/AC/BC'], f'P4: largest {m}; all largest {[names(b) for b in best]}')


def starts(band, prob, deck):
    res = []
    for s in groups(band, prob):
        if not legal(s):
            res.append((names(s), None, None, None))
            continue
        exts = [a for a in antichains(deck) if set(s) <= set(a)]
        m = max(map(len, exts))
        addable = [c for c in deck if c not in s and legal(list(s) + [c])]
        res.append((names(s), m, [names(set(a) - set(s)) for a in exts if len(a) == m], len(addable) == 0))
    return res


for st, m, adds, maximal in starts('K-1', 5, D3):
    print(f'    K-1 P5 start {st}: largest final size {m}; best additions {adds}; already unextendable {maximal}')
r = starts('K-1', 5, D3)
ok([x[1] for x in r] == [1, 3, 3, 2], f'P5 final sizes {[x[1] for x in r]} (guide 1, 3, 3, 2)')
ok([x[0] for x in r] == ['ABC', 'A', 'AB', 'A/BC'], 'P5 starts in printed order are ABC; A; AB; A/BC')
quote('The four starts are ABC; A; AB; A/BC. Their largest final sizes are respectively 1, 3, 3, 2. Add nothing to ABC; add B and C to A; add AC and BC to AB; add nothing to A/BC.')

gs = groups('K-1', 6)
ok(len(gs) == 4 and gs[0] == [card('A')] and gs[1] == [card('AB')], 'P6 example row shows A then AB (A fits inside AB)')
ok(card('A') < card('AB'), 'P6 example: A is strictly inside AB')
ok(is_deck(gs[2], D2) and is_deck(gs[3], D3), 'P6 decks are the full two- and three-symbol decks')
ok(min_chain_partition(gs[2]) == 2 and min_chain_partition(gs[3]) == 3, 'P6 fewest rows: 2 and 3')
r4 = parse_rows('empty/A/AB; B')
r8 = parse_rows('empty/A/AB/ABC; C/AC; B/BC')
ok(valid_partition(D2, r4) and valid_partition(D3, r8), 'guide p. 3 / P6 partitions cover each card once and are nested')
quote('For the four-card deck the minimum is two rows: empty -> A -> AB, and B. For the eight-card deck the minimum is three: empty -> A -> AB -> ABC; C -> AC; B -> BC.')

g = groups('K-1', 7)[0]
ok(is_deck(g, D3), 'P7 deck is the full three-symbol deck')
four = [a for a in antichains(g) if len(a) == 4]
ok(len(four) == 0, 'P7: no legal four-card collection')
ok(groups('K-1', 8) == [], 'P8 prints no deck of its own ("this deck" = the P7 deck above it on the page)')
allr = True
for d in D3:
    rest = [c for c in D3 if c != d]
    m, best = max_antichains(rest)
    allr &= m == 3
    print(f'    K-1 P8 set aside {name(d)}: largest remaining {m}: {[names(b) for b in best]}')
ok(allr, 'P8: a three-card collection survives every single removal')

# ------------------------------------------------------------------ 2-3
print('=' * 70)
print('Grades 2-3')
g = groups('2-3', 1)[0]
ok(is_deck(g, D2) and len([a for a in antichains(g) if a]) == 5, 'P1: two-symbol deck, 5 collections')
g = groups('2-3', 2)[0]
m, best = max_antichains(g)
ok(is_deck(g, D3) and m == 3 and len(best) == 2, f'P2: largest 3, exactly two: {[names(b) for b in best]}')
quote('The maximum is three, attained by exactly A/B/C and AB/AC/BC.')
r = starts('2-3', 3, D3)
for x in r:
    print(f'    2-3 P3 start {x[0]}: largest final {x[1]}; best additions {x[2]}; unextendable {x[3]}')
ok([(x[0], x[1]) for x in r] == [('ABC', 1), ('A/BC', 2), ('AB', 3)], 'P3 starts ABC, A/BC, AB give 1, 2, 3')
ok(r[0][3] and r[1][3] and not r[2][3], 'P3: ABC and A/BC are unextendable but smaller than 3')
quote('For ABC, keep it alone: final size 1. For A/BC, add nothing: size 2. For AB, add AC and BC: size 3.')
gs = groups('2-3', 4)
ok(is_deck(gs[2], D2) and is_deck(gs[3], D3) and min_chain_partition(gs[2]) == 2 and min_chain_partition(gs[3]) == 3,
   'P4: fewest rows 2 and 3')
g = groups('2-3', 5)[0]
ok(is_deck(g, D3) and not [a for a in antichains(g) if len(a) == 4], 'P5: no four-card collection')
g = groups('2-3', 6)[0]
ok(is_deck(g, D4), 'P6 deck is the full four-symbol deck (16 distinct cards)')
m, best = max_antichains(g)
ok(m == 6, f'P6/P8: largest {m}')
ok(min_chain_partition(g) == 6, 'P7: fewest rows 6')
rows16 = parse_rows('empty/A/AB/ABC/ABCD; D/AD/ABD; C/AC/ACD; CD; B/BC/BCD; BD')
quote('Read its rows as empty/A/AB/ABC/ABCD; D/AD/ABD; C/AC/ACD; CD; B/BC/BCD; BD.')
ok(valid_partition(D4, rows16) and len(rows16) == 6, 'guide p. 4 / P7 six-row partition covers all 16 once and is nested')
# the drawn p. 4 diagram: read the box labels row by row, and count arrowheads per row
import pdfplumber
with pdfplumber.open(str(PDF['guide'])) as gpdf:
    gp = gpdf.pages[3]
    labels = {'empty'} | {name(c) for c in D4}
    ws = [w for w in gp.extract_words() if w['text'] in labels and 100 < w["top"] < 330]
    byrow = {}
    for w in ws:
        byrow.setdefault(round(w['top']), []).append(w)
    drawn = [[w['text'] for w in sorted(r, key=lambda w: w['x0'])] for _, r in sorted(byrow.items())]
    heads = [c for c in gp.curves + gp.rects if c.get('fill') and (c['x1'] - c['x0']) < 12 and 100 < c["top"] < 330]
    per_row = {}
    for hd in heads:
        cy = (hd['top'] + hd['bottom']) / 2
        row = min(range(len(byrow)), key=lambda i: abs(sorted(byrow)[i] + 4 - cy))
        per_row[row] = per_row.get(row, 0) + 1
print(f'    guide p. 4 drawn rows: {drawn}; filled arrowheads per row: {per_row}')
ok([[name(c) for c in r] for r in rows16] == drawn, 'guide p. 4 drawn diagram rows equal the rows stated in 2-3 P7')
ok(all(per_row.get(i, 0) == len(r) - 1 for i, r in enumerate(drawn)), 'guide p. 4: each row has one arrow between consecutive boxes')
quote('Many valid six-row partitions exist.')

# ------------------------------------------------------------------ 4-5
print('=' * 70)
print('Grades 4-5')
gs = groups('4-5', 1)
ok(is_deck(gs[0], D2) and is_deck(gs[1], D3) and max_antichains(gs[0])[0] == 2 and max_antichains(gs[1])[0] == 3,
   'P1: largest 2 and 3')
g = groups('4-5', 2)[0]
ok(is_deck(g, D4) and max_antichains(g)[0] == 6, 'P2: largest 6')
r = starts('4-5', 3, D4)
for x in r:
    print(f'    4-5 P3 start {x[0]}: largest final {x[1]}; best additions {x[2]}; unextendable {x[3]}')
ok([(x[0], x[1]) for x in r] == [('ABCD', 1), ('A/BCD', 2), ('AB/AC', 6)], 'P3 starts ABCD, A/BCD, AB/AC give 1, 2, 6')
ok(r[0][3] and r[1][3] and not r[2][3], 'P3: ABCD and A/BCD are unextendable')
ok(r[2][2] == ['AD/BC/BD/CD'], 'P3: AB/AC extends to six in exactly one way (add AD, BC, BD, CD)')
quote('Start ABCD: size 1, add nothing. Start A/BCD: size 2, add nothing. Start AB/AC: size 6, add AD, BC, BD, CD.')
gs = groups('4-5', 4)
ok(min_chain_partition(gs[2]) == 2 and min_chain_partition(gs[3]) == 3, 'P4: fewest rows 2 and 3')
ok(min_chain_partition(D4) == 6, 'P5: fewest rows 6')
g = groups('4-5', 7)[0]
ok(g == [card('A')], 'P7 shows the circle card A')
withA = [a for a in antichains(D4) if card('A') in a]
mA = max(map(len, withA))
bestA = sorted(names(a) for a in withA if len(a) == mA)
ok(mA == 4, f'P7: largest collection containing A has {mA} cards; all of them: {bestA}')
ok('A/B/C/D' in bestA and 'A/BC/BD/CD' in bestA, 'P7: guide examples A/B/C/D and A/BC/BD/CD are largest')
quote('The maximum is four. Examples are A/B/C/D and A/BC/BD/CD.')
m, best = max_antichains(D4)
ok(len(best) == 1, 'P8: exactly one six-card collection')
quote('There is exactly one size-six collection: AB/AC/AD/BC/BD/CD.')
# P8 argument steps
for s in D4:
    with_s = [a for a in antichains(D4) if s in a]
    mx = max(map(len, with_s))
    exp = {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}[len(s)]
    ok(mx == exp, f'P8 step: largest collection containing {name(s)} has {mx} cards')

# ------------------------------------------------------------------ guide extras
print('=' * 70)
print('Guide other claims')
quote('The one-card collection ABCD cannot accept any other card, but it has size one. A/BCD is also unextendable, with size two.')
ok(all(not legal([card('ABCD'), c]) for c in D4 if c != card('ABCD')), 'ABCD is unextendable')
ok(all(not legal([card('A'), card('BCD'), c]) for c in D4 if c not in (card('A'), card('BCD'))), 'A/BCD is unextendable')
quote('No: remove A and BC.')
rest = [c for c in D3 if c not in (card('A'), card('BC'))]
ok(max_antichains(rest)[0] == 2, 'three-symbol deck without A and BC: largest 2')
bad = [names(pair) for pair in itertools.combinations(D3, 2) if max_antichains([c for c in D3 if c not in pair])[0] < 3]
print(f'    removals of two cards that leave no triple: {bad}')
quote('removing any two-symbol card reduces the maximum to five')
quote('Removing any non-pair card leaves all six pair cards intact.')
for c in D4:
    m = max_antichains([x for x in D4 if x != c])[0]
    ok(m == (5 if len(c) == 2 else 6), f'four-symbol deck without {name(c)}: largest {m}')
quote('Total: six decks, 96 cards, and 60 counters.')
ok(3 * 2 == 6 and 6 * 16 == 96 and 3 * 20 == 60, 'supply arithmetic: 3 tables x 2 decks x 16 cards, 3 x 20 counters')
ok(sorted(names([c]) for c in D4) == sorted(
    'empty A B C D AB AC AD BC BD CD ABC ABD ACD BCD ABCD'.split()), 'guide p. 2 inventory lists the 16 cards once each')

# ------------------------------------------------------------------ bonus packet
print('=' * 70)
print('Bonus packet (Subset cards encore)')
B = {}
for pg in D['bonus']:
    for pn, gs in pg['decks'].items():
        B[int(pn)] = [[card(c['card']) for c in g] for g in gs]
for pn, gs in sorted(B.items()):
    for g in gs:
        print(f'  bonus P{pn}: {len(g)} cards, full {"3" if is_deck(g, D3) else "4" if is_deck(g, D4) else "?"}-symbol deck')
ok(is_deck(B[1][0], D3) and is_deck(B[2][0], D3) and is_deck(B[7][0], D3), 'bonus P1, P2, P7 decks are the full 3-symbol deck')
ok(is_deck(B[3][0], D4) and is_deck(B[4][0], D4) and is_deck(B[4][1], D4) and is_deck(B[8][0], D4),
   'bonus P3, P4 (both), P8 decks are the full 4-symbol deck')


def intersecting_families(deck):
    deck = [c for c in deck if c]
    out = []
    n = len(deck)
    for mask in range(1 << n):
        fam = [deck[i] for i in range(n) if mask >> i & 1]
        if all(a & b for a, b in itertools.combinations(fam, 2)):
            out.append(fam)
    return out


for letters, mx in (('ABC', 4), ('ABCD', 8)):
    fams = intersecting_families(full_deck(letters))
    m = max(map(len, fams))
    best = [f for f in fams if len(f) == m]
    nocommon = [f for f in best if not frozenset.intersection(*f)]
    ok(m == mx, f'bonus: largest pairwise-sharing collection on {len(letters)} symbols = {m}; {len(best)} such, {len(nocommon)} with no common symbol')
    if letters == 'ABC':
        ok(len(nocommon) == 1 and names(nocommon[0]) == 'AB/AC/BC/ABC', f'bonus P2: the only size-4 family with no common symbol is {names(nocommon[0])}')
quote('P1 maximum is 4. One witness is A,AB,AC,ABC.', BGUIDE, 'bonus guide')
quote('This is the only size-four family with no common symbol on this deck', BGUIDE, 'bonus guide')
fam = [card(x) for x in 'AB,AC,BC,ABC,ABD,ACD,BCD,ABCD'.split(',')]
ok(len(set(fam)) == 8 and all(a & b for a, b in itertools.combinations(fam, 2)) and not frozenset.intersection(*fam),
   'bonus P3: AB,AC,BC,ABC,ABD,ACD,BCD,ABCD is pairwise sharing, size 8, no common symbol')
quote('Another maximum is AB,AC,BC,ABC,ABD,ACD,BCD,ABCD, with no symbol common to all eight.', BGUIDE, 'bonus guide')


def works(trigs, deck):
    return [c for c in deck if any(t <= c for t in trigs)]


w1 = works([card('AB'), card('D')], D4)
w2 = works([card('A'), card('BC')], D4)
g1 = [card(x) for x in 'D,AB,AD,BD,CD,ABC,ABD,ACD,BCD,ABCD'.split(',')]
g2 = [card(x) for x in 'A,AB,AC,AD,BC,ABC,ABD,ACD,BCD,ABCD'.split(',')]
ok(set(w1) == set(g1) and len(w1) == 10, f'bonus P4 triggers AB and D: {names(w1)}')
ok(set(w2) == set(g2) and len(w2) == 10, f'bonus P4 triggers A and BC: {names(w2)}')
quote('P4, AB or D: working cards are D,AB,AD,BD,CD,ABC,ABD,ACD,BCD,ABCD. A or BC: A,AB,AC,AD,BC,ABC,ABD,ACD,BCD,ABCD.', BGUIDE, 'bonus guide')
p5 = [card(x) for x in 'B, AB, BC, BD, ABC, ABD, BCD, ABCD, AC, ACD'.split(',')]
quote('These cards work: B, AB, BC, BD, ABC, ABD, BCD, ABCD, AC, ACD.', BONUS, 'bonus page')
ok(all(c2 in p5 for c in p5 for c2 in D4 if c <= c2), 'bonus P5: the working set is closed under adding symbols')
minimal = [c for c in p5 if not any(d < c for d in p5)]
ok(sorted(map(name, minimal)) == ['AC', 'B'], f'bonus P5: minimal working cards {names(minimal)}')
# fewest triggers: brute force over all trigger sets of size <= 2
fewest = None
for k in range(0, 4):
    for T in itertools.combinations(D4, k):
        if set(works(T, D4)) == set(p5):
            fewest = k
            break
    if fewest is not None:
        break
ok(fewest == 2, f'bonus P5: fewest triggers = {fewest}')


def upsets(deck):
    deck = list(deck)
    n = len(deck)
    out = []
    for mask in range(1 << n):
        S = {deck[i] for i in range(n) if mask >> i & 1}
        if all(y in S for x in S for y in deck if x <= y):
            out.append(S)
    return out


U4 = upsets(D4)
ok(len(U4) == 168, f'bonus guide: {len(U4)} four-symbol monotone rules')
allrec, altfail = True, []
for S in U4:
    found = [c for c in S if all((c - {x}) not in S for x in c)]  # every single-symbol removal fails (vacuous for empty)
    allrec &= set(works(found, D4)) == S
    found_alt = [c for c in S if any((c - {x}) not in S for x in c)]  # "some removal fails" reading
    if set(works(found_alt, D4)) != S:
        altfail.append(len(S))
ok(allrec, 'bonus P6: for all 168 rules, cards failing on every single removal recreate the rule')
print(f'    other reading ("some removal makes it fail") fails only for rules of size {altfail} (16 = every card works)')
quote('an all-working deck has the empty card as its only minimal trigger. The empty card satisfies the no-removal condition vacuously.', BGUIDE, 'bonus guide')


def no_triple(fam):
    return not any(a < b < c for a, b, c in itertools.permutations(fam, 3))


def no_chain(fam, k):
    fam = sorted(fam, key=len)
    for combo in itertools.combinations(fam, k):
        if all(x < y for x, y in zip(combo, combo[1:])):
            return False
    return True


for letters, mx in (('ABC', 6), ('ABCD', 10)):
    deck = full_deck(letters)
    n = len(deck)
    chains3 = []
    for a, b, c in itertools.permutations(range(n), 3):
        if deck[a] < deck[b] < deck[c]:
            chains3.append((1 << a) | (1 << b) | (1 << c))
    best, cnt = 0, 0
    bestfams = []
    for mask in range(1 << n):
        if any(mask & ch == ch for ch in chains3):
            continue
        k = bin(mask).count('1')
        if k > best:
            best, bestfams = k, [mask]
        elif k == best:
            bestfams.append(mask)
    fams = [[deck[i] for i in range(n) if m >> i & 1] for m in bestfams]
    ok(best == mx, f'bonus: no nested triple on {len(letters)} symbols: largest {best}; {len(fams)} largest families: {[names(f) for f in fams][:6]}')
    if letters == 'ABC':
        ok(len(fams) == 1 and names(fams[0]) == 'A/B/C/AB/AC/BC', 'bonus P7: unique maximum A,B,C,AB,AC,BC')
quote('P7 maximum is 6: A,B,C,AB,AC,BC.', BGUIDE, 'bonus guide')
quote('It is the only maximum family', BGUIDE, 'bonus guide')
r7 = parse_rows('empty/A/AB/ABC; B/BC; C/AC')
ok(valid_partition(D3, r7) and sorted(map(len, r7)) == [2, 2, 4], 'bonus P7 chain partition (lengths 4,2,2) valid')
r8b = parse_rows('empty/A/AB/ABC/ABCD; D/AD/ABD; C/AC/ACD; CD; B/BC/BCD; BD')
ok(valid_partition(D4, r8b) and [len(r) for r in r8b] == [5, 3, 3, 1, 3, 1] and sum(min(2, len(r)) for r in r8b) == 10,
   'bonus P8 chain partition (lengths 5,3,3,1,3,1) valid, capacity 10')
w_a = [c for c in D4 if len(c) in (1, 2)]
w_b = [c for c in D4 if len(c) in (2, 3)]
ok(no_triple(w_a) and no_triple(w_b) and len(w_a) == len(w_b) == 10, 'bonus P8 witnesses (sizes 1+2, sizes 2+3) are legal')
# depth: forbid four-chains on three symbols
n = len(D3)
best7 = []
for r in range(n, 0, -1):
    fams = [f for f in itertools.combinations(D3, r) if no_chain(f, 4)]
    if fams:
        best7 = fams
        break
ok(len(best7[0]) == 7 and sorted(name(next(iter(set(D3) - set(f)))) for f in best7) == ['ABC', 'empty'],
   f'bonus guide depth: no four-chain on 3 symbols: largest {len(best7[0])}, omitting {[name(next(iter(set(D3) - set(f)))) for f in best7]}')
quote('The maximum is 7: omit empty or omit ABC.', BGUIDE, 'bonus guide')
ok(card('ABC') & card('ABD') and not (card('D') & card('C')), 'bonus guide: ABC, ABD share; complements D, C do not')
ok(set(works([card('B'), card('AB'), card('AC')], D4)) == set(works([card('B'), card('AC')], D4)),
   'bonus guide: triggers B,AB,AC give the same rule as B,AC')
ok(2 ** 8 == 256 and 2 ** 16 == 65536, 'bonus guide: 256 and 65,536 families')

# ------------------------------------------------------------------ guide page references
print('=' * 70)
print('Guide "Student page" references vs the delivered PDFs')
heads = re.findall(r'(K-1|Grades 2-3|Grades 4-5) solutions for Problems (\d) to (\d)(.*?)(?=(?:K-1|Grades 2-3|Grades 4-5) solutions for Problems|Sources extensions)', GUIDE)
bandkey = {'K-1': 'K-1', 'Grades 2-3': '2-3', 'Grades 4-5': '4-5'}
nrefs = 0
for band, a, b, body in heads:
    actual = {n: pg['page'] for pg in D[bandkey[band]] for n in pg['problems_on_page']}
    for pn, pg in re.findall(r'Problem (\d) .*? Student page (\d)', body):
        nrefs += 1
        ok(actual[int(pn)] == int(pg), f'{band} P{pn}: guide says student page {pg}, PDF has it on page {actual[int(pn)]}')
ok(nrefs == 24, f'{nrefs} guide page references checked')

print('=' * 70)
print(f'{len(FAILS)} failures')
for f in FAILS:
    print('  FAIL', f)
