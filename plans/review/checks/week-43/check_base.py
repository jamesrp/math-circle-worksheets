"""Independent enumeration of every base Week 43 task and every claim in the
adult guide. Reads the guide text from the delivered PDF and the printed
diagram data from extracted.json (run extract.py first).

Writes check_base.out.
"""
import json
import os
import re
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations
from math import factorial

from common import (HERE, PDFS, ROWS3, Report, chooser_stories, fisher_yates_stories, flat,
                    naive_stories, pdf_text, run_story, swap)

R = Report('check_base')
X = json.load(open(os.path.join(HERE, 'extracted.json')))
G = [flat(t) for t in pdf_text(PDFS['guide'])]
GUIDE = ' '.join(G)


def page(band, n):
    return X[band][n - 1]


def two_swap(start):
    return {s: run_story(start, s) for s in fisher_yates_stories(3)}


def ticket_groups(pg, problem, size=28):
    """Printed ticket boxes (with numbers) in a problem, grouped left to right."""
    boxes = [f for f in pg['empty_frames'] if f['problem'] == problem
             and abs(f['x1'] - f['x0'] - size) < 2 and abs(f['y1'] - f['y0'] - size) < 2]
    boxes.sort(key=lambda f: (round(f['y0']), f['x0']))
    groups = []
    for b in boxes:
        if groups and abs(groups[-1][-1]['y0'] - b['y0']) < 2 and b['x0'] - groups[-1][-1]['x1'] < 15:
            groups[-1].append(b)
        else:
            groups.append([b])
    return groups


def row_frames(pg, problem, w=None):
    """Three-card answer rows: empty frames grouped in touching triples."""
    fr = [f for f in pg['empty_frames'] if f['problem'] == problem and not f['text']
          and not (abs(f['x1'] - f['x0'] - 28.3) < 1 and abs(f['y1'] - f['y0'] - 28.3) < 1)
          and (w is None or abs(f['x1'] - f['x0'] - w) < 2)]
    fr.sort(key=lambda f: (round(f['y0']), f['x0']))
    rows = []
    for f in fr:
        if rows and abs(rows[-1][-1]['y0'] - f['y0']) < 2 and abs(rows[-1][-1]['x1'] - f['x0']) < 2.5:
            rows[-1].append(f)
        else:
            rows.append([f])
    return [r for r in rows if len(r) == 3]


# ====================================================================== core
R.head('Direct chooser (K-1 shared rule p2, 2-3 P1, 4-5 P1)')
ch = chooser_stories()
outs = [o for _, o in ch]
R.check(len(ch) == 6 and sorted(outs) == sorted(ROWS3), f'6 first-two stories give the 6 rows once each: {ch}')
R.check(all(Fraction(1, 3) * Fraction(1, 2) == Fraction(1, 6) for _ in ch), 'each story has probability 1/3*1/2 = 1/6')
for band in ['k-1', 'grades-2-3', 'grades-4-5']:
    pg = page(band, 2 if band == 'k-1' else 1)
    seq = [r['word'] for r in pg['rows'] if r['problem'] == 'rules']
    R.check(seq == ['C', 'A', 'CAB'], f'{band}: chooser picture draws C (triangle) then A (square), row {seq[-1]}')
    R.check('choose triangle, then square; circle is left' in pg['text'], f'{band}: caption matches the picture')
R.check(dict(ch)['CA'] == 'CAB', 'example story CA gives CAB')

R.head('Two-swap rule (Fisher-Yates, tickets {1,2,3} then {2,3})')
tab = two_swap('ABC')
R.note(f'from ABC: {tab}')
R.check(sorted(tab.values()) == sorted(ROWS3), 'from ABC: six stories give six different rows')
for st in permutations('ABC'):
    st = ''.join(st)
    R.check(sorted(two_swap(st).values()) == sorted(ROWS3), f'from {st}: bijection onto all six rows')
for band, pno in [('k-1', 3), ('grades-2-3', 2), ('grades-4-5', 2)]:
    tr = page(band, pno)['transitions']
    R.check([(t['label'], t['before'], t['after']) for t in tr] ==
            [('1 with 3', 'ABC', 'CBA'), ('2 with 2', 'CBA', 'CBA')],
            f'{band} p{pno}: printed demo ABC -1 with 3-> CBA -2 with 2-> CBA')
R.check(tab[(3, 2)] == 'CBA', 'demo story (3,2) = CBA, which is one of the six answers (see notes)')

# ------------------------------------------------------------------ K-1
R.head('K-1')
pg = page('k-1', 1)
R.check([r['word'] for r in pg['rows']] == ['ABC'], 'P1 shows the three cards A B C')
rf = row_frames(pg, 1, w=74)
R.check(len(rf) == 6 and all(len(r) == 3 for r in rf), f'P1 prints {len(rf)} three-card record rows for 6 answers')

pg = page('k-1', 2)
crossed = [c['covers'][0] for c in pg['crossouts']]
R.check(crossed == ['A', 'B', 'C'], f'P2 crossed-out first cards: {crossed}')
rows = row_frames(pg, 2)
per = Counter()
for r in rows:
    cy = r[0]['y0']
    # assign a row to the crossed-out card whose icon is nearest above or level
    marks = sorted(pg['crossouts'], key=lambda c: c['y0'])
    owner = [c['covers'][0] for c in marks if c['y0'] - 5 <= cy][-1]
    per[owner] += 1
R.note(f'P2 printed three-card rows per crossed-out card: {dict(per)}')
first_is = {x: [w for w in ROWS3 if w[0] == x] for x in 'ABC'}
first_not = {x: [w for w in ROWS3 if w[0] != x] for x in 'ABC'}
R.note(f'reading "crossed-out = already drawn first" (guide): {first_is}')
R.note(f'reading "crossed-out = cannot come first": {first_not}')
R.check(all(len(first_is[x]) == 2 for x in 'ABC'), 'guide reading: 2 rows per case')
R.check(all(per[x] == len(first_not[x]) == 4 for x in 'ABC'),
        'printed space (4 rows per case) equals the count for the "cannot come first" reading, not the guide\'s 2')
# Could two different first-two draws make the same row?
R.check(len(set(outs)) == 6, 'P2: two different first-two draws never give the same row')

pg = page('k-1', 3)
R.check(len(ticket_groups(pg, 3)) == 6 and len(row_frames(pg, 3)) == 6, 'P3 prints 6 (two tickets + row) records')
R.check(len(set(tab.values())) == 6, 'P3: no row from two stories')
for (u, v), w in [((1, 2), 'ABC'), ((1, 3), 'ACB'), ((2, 2), 'BAC'), ((2, 3), 'BCA'), ((3, 2), 'CBA'), ((3, 3), 'CAB')]:
    R.check(tab[(u, v)] == w, f'P3 guide table ({u},{v}) {w}')
m = re.search(r'K to 1 answer key.*?Problem 3.*?Ticket story Final row Ticket story Final row (.*?) No final row', GUIDE)
pairs = re.findall(r'\((\d),(\d)\) ([ABC]{3})', m.group(1))
R.check(len(pairs) == 6 and all(tab[(int(a), int(b))] == w for a, b, w in pairs), f'K-1 P3 guide table parsed {pairs}')

pg = page('k-1', 4)
tg = ticket_groups(pg, 4)
sets = [tuple(int(b['text']) for b in g) for g in tg]
R.check(sets == [(2, 3), (1, 3), (1, 2)], f'P4 printed first-ticket sets {sets}')
R.check(len(row_frames(pg, 4)) == 6, 'P4 prints 2 rows per missing ticket')
for missing in (1, 2, 3):
    possible = {run_story('ABC', (u, v)) for u in (1, 2, 3) if u != missing for v in (2, 3)}
    imp = sorted(set(ROWS3) - possible)
    R.note(f'P4 missing ticket {missing}: impossible {imp}')
    exp = {1: ['ABC', 'ACB'], 2: ['BAC', 'BCA'], 3: ['CAB', 'CBA']}[missing]
    R.check(imp == exp, f'P4 guide: remove {missing} -> {exp}')
R.check([r['word'] for r in pg['rows'] if r['problem'] == 5] == ['ABC', 'CBA'], 'P5 shows starts ABC and CBA')
m = re.search(r'Story Finish from ABC Finish from CBA (.*?) Bellingham', GUIDE)
trip = re.findall(r'\((\d),(\d)\) ([ABC]{3}) ([ABC]{3})', m.group(1))
R.check(len(trip) == 6, 'P5 guide table has six stories')
for a, b, f1, f2 in trip:
    s = (int(a), int(b))
    R.check(run_story('ABC', s) == f1 and run_story('CBA', s) == f2 and f1 != f2,
            f'P5 guide row {s}: ABC->{f1}, CBA->{f2}')
ok = all(run_story(p, s) != run_story(q, s) for s in fisher_yates_stories(3)
         for p in ROWS3 for q in ROWS3 if p != q)
R.check(ok, 'P5 in general: a fixed story never merges two different starts (all pairs, all stories)')
# undo argument: applying the swaps in reverse order recovers the start
R.check(all(run_story(run_story(p, (u, v)), (v, u), slots=[2, 1]) == p for p in ROWS3 for (u, v) in tab),
        'P5 guide: undoing the swaps in reverse order recovers the start')

# ------------------------------------------------------------------ 2-3
R.head('Grades 2-3')
pg = page('grades-2-3', 1)
R.check(len(row_frames(pg, 1)) == 6, 'P1 prints 6 record rows')
m = re.search(r'Grades 2 to 3 answer key Problem 1 (.*?) Problem 2', GUIDE).group(1)
R.check(all(w in m for w in ROWS3) and 'AB, AC, BA, BC, CA, CB' in m and '1/6' in m, 'P1 guide: six stories, 1/6 each')
R.check([a + b for a, b in zip(['AB', 'AC', 'BA', 'BC', 'CA', 'CB'], 'CBCABA')] == ROWS3, 'P1 guide story->row order')

pg = page('grades-2-3', 2)
tg = [tuple(int(b['text']) for b in g) for g in ticket_groups(pg, 2)]
R.note(f'P2 printed ticket pairs (reading order): {tg}')
R.check(tg == [(1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)], 'P2 printed pairs = guide "printed order"')
R.check(sorted(tg) == sorted(fisher_yates_stories(3)), 'P2 prints all six stories exactly once')
m = re.search(r'Grades 2 to 3 answer key.*?Problem 2 (.*?) Problem 3', GUIDE).group(1)
mp = re.findall(r'\((\d),(\d)\) -> ([ABC]{3})', m)
R.check([(int(a), int(b)) for a, b, _ in mp] == tg and all(tab[(int(a), int(b))] == w for a, b, w in mp),
        f'P2 guide mappings {mp}')
R.check(len(row_frames(pg, 2)) == 6, 'P2 prints six answer rows')

pg = page('grades-2-3', 3)
targets = [r['word'] for r in pg['rows'] if r['problem'] == 3]
R.check(targets == ROWS3, f'P3 printed targets {targets}')
tbac = two_swap('BAC')
inv = {w: s for s, w in tbac.items()}
R.note(f'P3 from BAC: {inv}')
R.check(len(inv) == 6, 'P3: from BAC every row is reachable exactly once')
m = re.search(r'Target Ticket story Target Ticket story (.*?) Problem 4', GUIDE).group(1)
gp = re.findall(r'([ABC]{3}) \((\d),(\d)\)', m)
R.check(len(gp) == 6 and all(inv[w] == (int(a), int(b)) for w, a, b in gp), f'P3 guide table {gp}')
p3boxes = [f for f in pg['empty_frames'] if f['problem'] == 3 and abs(f['x1'] - f['x0'] - 57) < 2]
R.check(len(p3boxes) == 12, f'P3 prints two ticket boxes under each of the 6 targets ({len(p3boxes)} boxes)')
# P4: six shuffles need not show all six rows
p_all = Fraction(factorial(6), 6 ** 6)
R.note(f'P4: chance six fair shuffles show all six rows once = 6!/6^6 = {p_all} ~ {float(p_all):.4f}')
R.check(all(run_story('ABC', (1, 2)) == 'ABC' for _ in range(6)), 'P4 guide: (1,2) six times gives ABC six times')
R.check(Fraction(1, 6) ** 6 > 0, 'P4: that outcome has positive chance (1/6)^6')

# Three-swap (wrong-range) rule
naive = {s: run_story('ABC', s) for s in naive_stories(3)}
cnt = Counter(naive.values())
R.note(f'naive 27-story counts from ABC: {[cnt[w] for w in ROWS3]} for {ROWS3}')
R.check([cnt[w] for w in ROWS3] == [4, 5, 5, 5, 4, 4], 'guide: counts 4,5,5,5,4,4')
abc = sorted(s for s, w in naive.items() if w == 'ABC')
R.check(abc == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (3, 2, 1)], f'P5 guide: exactly four stories give ABC: {abc}')
pg = page('grades-2-3', 4)
tr = [(t['label'], t['before'], t['after']) for t in pg['transitions']]
R.note(f'p4 printed demo transitions: {tr}')
R.check(tr == [('1 with 3', 'ABC', 'CBA'), ('2 with 2', 'CBA', 'CBA'), ('3 with 1', 'CBA', 'ABC')],
        'p4 demo is the complete story (3,2,1): ABC -> CBA -> CBA -> ABC')
R.check(naive[(3, 2, 1)] == 'ABC' and naive[(1, 2, 3)] == 'ABC',
        'printed demo (3,2,1) ends at ABC, as does the all-self-swap story (1,2,3): '
        'the page itself shows a P5 collision (see report)')
alt = {s: naive[s] for s in [(3, 2, 3), (3, 2, 2)]}
R.note(f'alternative demo endings: {alt}; all stories for CBA: '
       f'{sorted(s for s, w in naive.items() if w == "CBA")}; all stories for CAB: '
       f'{sorted(s for s, w in naive.items() if w == "CAB")}')
R.check(len(ticket_groups(pg, 5)) == 3 and len(row_frames(pg, 5)) == 3, 'P5 prints three story records')
R.check(27 % 6 != 0, 'P6: 27 is not a multiple of 6')
m = re.search(r'Final order (ABC ACB BAC BCA CAB CBA) History count ([\d ]+?) The fact', GUIDE)
R.check(m and [int(v) for v in m.group(2).split()] == [cnt[w] for w in m.group(1).split()], 'P6 guide table matches')
m = re.search(r'Grades 2 to 3 answer key.*?Problem 5 (.*?) Problem 6', GUIDE).group(1)
R.check(all(f'({a},{b},{c})' in m for a, b, c in abc), 'P5 guide lists the four ABC stories')
# descriptions in the P5 guide: which slot pairs are swapped twice
desc = {(1, 3, 2): {2, 3}, (2, 1, 3): {1, 2}, (3, 2, 1): {1, 3}}
for s, pair in desc.items():
    real = [frozenset((i + 1, t)) for i, t in enumerate(s) if t != i + 1]
    R.check(len(real) == 2 and real[0] == real[1] == frozenset(pair), f'P5 guide description of {s}: swaps {sorted(pair)} twice')

# ------------------------------------------------------------------ 4-5
R.head('Grades 4-5')
R.check(len(row_frames(page('grades-4-5', 1), 1)) == 6, 'P1 prints 6 record rows')
R.check(page('grades-4-5', 2)['rows'][-1]['word'] == 'CBA', 'P3 shows start CBA')
tcba = two_swap('CBA')
R.check(sorted(tcba.values()) == ROWS3, 'P3: from CBA still uniform (bijection)')
# guide relabelling argument: swap labels A<->C
sw = str.maketrans('AC', 'CA')
R.check(all(tcba[s] == tab[s].translate(sw) for s in tab), 'P3 guide: relabel A<->C maps ABC-experiment to CBA-experiment')
R.check(sorted(cnt.values()) != [27 // 6] * 6, 'P4: wrong-range rule not uniform')
for n in range(3, 8):
    R.check((n ** n) % factorial(n) != 0, f'wrong-range rule n={n}: n^n={n ** n} not divisible by n!={factorial(n)}')
for n in (3, 4, 5, 6):
    cn = Counter(run_story(''.join('ABCDEF'[:n]), s) for s in naive_stories(n))
    R.check(len(set(cn.values())) > 1 or len(cn) < factorial(n), f'wrong-range rule n={n}: unequal counts (min {min(cn.values())}, max {max(cn.values())})')
nos = {s: run_story('ABC', s) for s in [(2, 3), (3, 3)]}
R.note(f'P5 no-self-swap rule: {nos}')
R.check(sorted(nos.values()) == ['BCA', 'CAB'], 'P5: only BCA and CAB')
R.check(swap('ABC', 1, 2) == 'BAC' and swap('BAC', 2, 3) == 'BCA' and swap('ABC', 1, 3) == 'CBA' and swap('CBA', 2, 3) == 'CAB',
        'P5 guide intermediate rows BAC, BCA, CBA, CAB')
for n in (4, 5):
    for st in permutations('ABCDE'[:n]):
        st = ''.join(st)
        o = [run_story(st, s) for s in fisher_yates_stories(n)]
        if len(o) != factorial(n) or len(set(o)) != factorial(n):
            R.check(False, f'P{n + 2}: FY from {st} not bijective')
            break
    else:
        R.check(True, f'P{n + 2}: left-to-right FY for {n} cards: {factorial(n)} stories, bijective from every start')
for n in (2, 3, 4, 5, 6):
    st = 'ABCDEF'[:n]
    o = Counter(run_story(st, s) for s in fisher_yates_stories(n))
    R.check(len(o) == factorial(n) and set(o.values()) == {1}, f'overview: FY n={n} gives n! orders once each')
# unique-target construction described in the guide
for n in (3, 4, 5):
    start = 'ABCDE'[:n]
    for tgt in permutations(start):
        row, story = start, []
        for i in range(1, n):
            j = row.index(tgt[i - 1]) + 1
            assert j >= i
            story.append(j)
            row = swap(row, i, j)
        if row != ''.join(tgt) or run_story(start, tuple(story)) != ''.join(tgt):
            R.check(False, f'unique-target construction fails n={n} {tgt}')
            break
    else:
        R.check(True, f'guide unique-target construction works for every target, n={n}')
R.check('4 × 3 × 2 = 24' in GUIDE and '5 × 4 × 3 × 2 = 120' in GUIDE, 'P6/P7 guide counts 24 and 120')
R.check(len(page('grades-4-5', 4)['rows']) == 2 and [r['word'] for r in page('grades-4-5', 4)['rows']] == ['ABCD', 'ABCDE'],
        'P6/P7 card strips ABCD and ABCDE')

# ------------------------------------------------------------------ guide p1-2
R.head('Guide overview and session pages')
p1 = G[0]
R.check('3³ = 27' in p1 or '33 = 27' in p1, 'overview: 3^3 = 27')
R.check('4, 5, 5, 5, 4, 4' in p1, 'overview counts present')
R.check('produces only BCA and CAB' in p1, 'overview: no-self-swap gives only BCA, CAB')
R.check('Draw C and then A from a cup without replacement, giving C A B' in G[1], 'launch chooser example CAB')
R.check(run_story('ABC', (3,)) == 'CBA' and run_story('ABC', (3, 2)) == 'CBA', 'launch swap demo: ticket 3 -> CBA, ticket 2 -> CBA')
R.check('The27-story' in G[5], 'route note typo "The27-story" (cosmetic)')

R.finish()
