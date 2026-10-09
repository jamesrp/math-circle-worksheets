"""Independent enumeration of every Week 46 base task (K-1, 2-3, 4-5) and of every
answer, example and claim in the base adult guide.

Boards, stories and starting pairs are read from diagrams.json, which
extract_diagrams.py builds from the student TeX and cross-checks against the
delivered PDFs. Guide claims are quoted from the delivered guide's text layer
(each quote is first checked to occur there) and then recomputed.
"""
import itertools
import json
import re
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

from common import (BOARDS, SETS, TOGGLES, PDFS, Report, apply, run, hamming, pdftext)

R = Report()
D = json.load(open(Path(__file__).with_name('diagrams.json')))
GUIDE = re.sub(r'\s+', ' ', pdftext(PDFS['guide'], layout=False)).replace('ﬁ', 'fi')


def quote(s):
    """Assert a guide quotation is really printed, return it."""
    ok = re.sub(r'\s+', ' ', s) in GUIDE
    R.check(ok, f'guide prints: "{s[:90]}"')
    return s


def sec(band, page, name):
    return D[band]['pages'][page - 1]['sections'].get(name, {})


def pairs_of(band, page, name):
    return [(p['top'], p['bottom']) for p in sorted(sec(band, page, name).get('pairs', []),
                                                  key=lambda p: (round(p['y'], 2), p['x']))]


def singles_of(band, page, name):
    return [s['word'] for s in sorted(sec(band, page, name).get('singles', []), key=lambda s: s['y'])]


def stories_of(band, page, name):
    rows = {}
    for c in sec(band, page, name)['cards']:
        rows.setdefault(round(c['y'], 2), []).append(c)
    return [[(c['slot'], c['color']) for c in sorted(v, key=lambda c: c['x'])] for _, v in sorted(rows.items())]


def parse_story(s):
    """'1→R, toggle 1, 2→B' -> instruction list."""
    out = []
    for part in re.split(r',\s*|;\s*', s.strip()):
        part = part.strip()
        m = re.fullmatch(r'([123])→([RB])', part)
        if m:
            out.append((int(m.group(1)), m.group(2)))
            continue
        m = re.fullmatch(r'toggle ([123])', part)
        if m:
            out.append(('T', int(m.group(1))))
            continue
        raise ValueError(part)
    return out


# ---------------------------------------------------------------------------------
# 1. Minimum number of chosen colour-setting instructions for a pair (BFS)
# ---------------------------------------------------------------------------------
def min_repairs(a, b):
    """Breadth-first search over the pair state; returns fewest shared setting
    instructions that make the two boards equal."""
    seen = {(a, b): 0}
    frontier = [(a, b)]
    d = 0
    while frontier:
        for x, y in frontier:
            if x == y:
                return d
        d += 1
        nxt = []
        for x, y in frontier:
            for ins in SETS:
                s = (apply(x, ins), apply(y, ins))
                if s not in seen:
                    seen[s] = d
                    nxt.append(s)
        frontier = nxt
    return None


MIN = {(a, b): min_repairs(a, b) for a in BOARDS for b in BOARDS}
R.check(all(MIN[(a, b)] == hamming(a, b) for a in BOARDS for b in BOARDS),
        'for all 64 ordered pairs the BFS minimum equals the number of disagreeing slots')
R.check(max(MIN.values()) == 3, f'largest minimum over all pairs is {max(MIN.values())}')
dist = Counter(MIN[(a, b)] for a, b in itertools.combinations_with_replacement(BOARDS, 2))
R.note(f'unordered pairs (incl. equal) by minimum: {dict(sorted(dist.items()))}')

# K-1 P1 / 2-3 P1 (two single rows on page 1)
for band in ['k-1', 'grades-2-3']:
    w = singles_of(band, 1, 'P1')
    R.check(w == ['RBR', 'BRB'] and MIN[tuple(w)] == 3, f'{band} P1: boards {w} need {MIN[tuple(w)]} (no pair needs more)')

# K-1 P2 and 4-5 P1 (four pairs)
for band, page, name in [('k-1', 2, 'P2'), ('grades-4-5', 1, 'P1')]:
    ps = pairs_of(band, page, name)
    vals = [MIN[p] for p in ps]
    R.check(vals == [1, 2, 0, 3], f'{band} {name}: pairs {ps} need {vals} (guide: 1, 2, 0, 3)')
    R.check(sorted(vals) == [0, 1, 2, 3], f'{band} {name}: the four pairs show every possible minimum 0-3 once')

# K-1 P3: exactly two possible; four impossible
R.check(dist[2] > 0 and 4 not in dist, f'K-1 P3: {dist[2]} unordered pairs need exactly 2; none needs 4')

# ---------------------------------------------------------------------------------
# 2. Fixed stories: universality, shortest length, finishes
# ---------------------------------------------------------------------------------
def finishes(story):
    return {run(s, story) for s in BOARDS}


def universal(story):
    return len(finishes(story)) == 1


def visited(story):
    return {i for (i, c) in story if i != 'T'}


univ_by_len = {}
for L in range(0, 6):
    stories = list(itertools.product(SETS, repeat=L))
    u = [s for s in stories if universal(s)]
    univ_by_len[L] = len(u)
    R.check(all(universal(s) == (visited(s) == {1, 2, 3}) for s in stories),
            f'length {L}: a setting story synchronises all 8 starts iff it names all three slots ({len(u)}/{len(stories)})')
    R.check(all(len(finishes(s)) == 2 ** (3 - len(visited(s))) for s in stories),
            f'length {L}: every setting story has exactly 2^u finishes (u = unnamed slots)')
R.check(univ_by_len[0] == univ_by_len[1] == univ_by_len[2] == 0 and univ_by_len[3] == 48,
        f'shortest universal story has length 3; there are {univ_by_len[3]} = 3!*2^3 of them (K-1 P4, 2-3 P5)')

# K-1 P4 guide example
s = parse_story(quote('1 becomes R, 2 becomes B, 3 becomes R').replace(' becomes ', '→'))
R.check(finishes(s) == {'RBR'}, 'K-1 P4 guide: 1R,2B,3R sends every start to RBR')

# K-1 P5: story 1→R, 3→B
st = stories_of('k-1', 3, 'P5')[0]
same = [(a, b) for a, b in itertools.combinations(BOARDS, 2) if run(a, st) == run(b, st)]
diff = [(a, b) for a, b in itertools.combinations(BOARDS, 2) if run(a, st) != run(b, st)]
R.check(all((a[1] == b[1]) == (run(a, st) == run(b, st)) for a in BOARDS for b in BOARDS),
        f'K-1 P5: under {st} two starts finish alike iff their middle colours agree '
        f'({len(same)} distinct pairs match, {len(diff)} stay different)')
quote('A pair that matches afterward: RRR / BRB, both finishing RRB')
R.check(run('RRR', st) == run('BRB', st) == 'RRB', 'K-1 P5 guide: RRR/BRB both finish RRB')
quote('A pair that stays different: RRR / BBB, finishing RRB and RBB')
R.check((run('RRR', st), run('BBB', st)) == ('RRB', 'RBB'), 'K-1 P5 guide: RRR/BBB finish RRB and RBB')

# 2-3 P2 and 4-5 P2: the three printed stories
expected_fin = {0: {'BRR', 'BBR'}, 1: {'RRB'}, 2: {'RBR', 'RBB', 'BBR', 'BBB'}}
for band in ['grades-2-3', 'grades-4-5']:
    sts = stories_of(band, 2, 'P2')
    for k, s in enumerate(sts):
        f = finishes(s)
        un = {1, 2, 3} - visited(s)
        R.check(f == expected_fin[k], f'{band} P2 story {k + 1} {s}: finishes {sorted(f)} ({len(f)}), unnamed slots {sorted(un)}')
    R.check([universal(s) for s in sts] == [False, True, False], f'{band} P2: only the second story is universal')
    if band == 'grades-2-3':
        R.check([sorted(visited(s)) for s in sts] == [[1, 3], [1, 2, 3], [2]], '2-3 P2: marker sets {1,3}, {1,2,3}, {2}')
        quote('Under the first story the finishes are BRR/BBR, which differ at slot 2')
        R.check((run('RRR', sts[0]), run('BBB', sts[0])) == ('BRR', 'BBR'), '2-3 P2 guide: story 1 on RRR/BBB gives BRR/BBR')
        quote('Under the third they are RBR/BBB, differing at slots 1 and 3')
        R.check((run('RRR', sts[2]), run('BBB', sts[2])) == ('RBR', 'BBB'), '2-3 P2 guide: story 3 on RRR/BBB gives RBR/BBB')
        quote('every start finishes RRB')

# 2-3 P3 / 4-5 P3: a pair can match before all slots are named
early = [(a, b, s) for a, b in itertools.combinations(BOARDS, 2) for L in (1, 2)
         for s in itertools.product(SETS, repeat=L) if run(a, s) == run(b, s) and len(visited(s)) < 3]
R.check(len(early) > 0, f'2-3 P3 / 4-5 P3: {len(early)} (pair, story) cases match with fewer than 3 slots named')
R.check(all(set(i + 1 for i in range(3) if a[i] != b[i]) <= visited(s) for a, b, s in early) and
        all((run(a, s) == run(b, s)) == (set(i + 1 for i in range(3) if a[i] != b[i]) <= visited(s))
            for a, b in itertools.combinations(BOARDS, 2) for L in (0, 1, 2, 3) for s in itertools.product(SETS, repeat=L)),
        'a particular pair matches under a setting story iff every initially differing slot is named')
R.check(all(run(a, ()) == run(a, ()) for a in BOARDS) and len(BOARDS) == 8,
        '2-3 P3 / 4-5 P3 other reading: each of the 8 identical pairs (RRR/RRR, ...) already matches with no instruction and no marker')
quote('RRR/BRR becomes a matching RRR pair after 1→R')
R.check(run('RRR', [(1, 'R')]) == run('BRR', [(1, 'R')]) == 'RRR', '2-3 P3 guide: RRR/BRR match after 1→R')
quote('RRR/BBB under the same one-instruction story finishes RRR/RBB')
R.check((run('RRR', [(1, 'R')]), run('BBB', [(1, 'R')])) == ('RRR', 'RBB'), '2-3 P3 guide: RRR/BBB -> RRR/RBB')
quote('RRR and BRR match after 1→R, with two untouched slots')

# 2-3 P1 guide examples
for txt, pair, need in [('RRR/RRR needs zero', ('RRR', 'RRR'), 0), ('RBR/RRR needs one', ('RBR', 'RRR'), 1),
                        ('RRR/BBR needs two', ('RRR', 'BBR'), 2)]:
    quote(txt)
    R.check(MIN[pair] == need, f'2-3 P1 guide: {pair} needs {need}')
quote('Example needing exactly two: RRR versus BBR')
R.check(MIN[('RRR', 'BBR')] == 2, 'K-1 P3 guide: RRR/BBR needs exactly two')

# K-1 P2 guide table repairs
for pair, rep in [(('RBR', 'RRR'), [(2, 'R')]), (('RRB', 'BRR'), [(1, 'R'), (3, 'R')]), (('RRR', 'BBB'), [(1, 'R'), (2, 'R'), (3, 'R')])]:
    R.check(run(pair[0], rep) == run(pair[1], rep), f'K-1 P2 guide repair {rep} works on {pair}')

# 2-3 P5 guide example
s = parse_story(quote('Example: 1→R, 2→B, 3→R').split(': ')[1])
R.check(universal(s), '2-3 P5 guide: 1→R, 2→B, 3→R is universal')

# ---------------------------------------------------------------------------------
# 3. Agreement is absorbing (K-1 P7) and random draws (K-1 P6, 2-3 P4)
# ---------------------------------------------------------------------------------
R.check(all((x[i] == y[i]) <= (apply(x, ins)[i] == apply(y, ins)[i]) for x in BOARDS for y in BOARDS
            for ins in SETS for i in range(3)),
        'K-1 P7 / overview: a shared setting instruction never turns an agreeing slot into a disagreeing one')

# exact distribution of matching time from RRR/BBB under random draws
def p_unmatched(start_pair, m):
    """Exact probability (Fraction) that the pair is still unmatched after m draws."""
    a, b = start_pair
    states = Counter({(a, b): 1})
    for _ in range(m):
        nxt = Counter()
        for (x, y), w in states.items():
            for ins in SETS:
                nxt[(apply(x, ins), apply(y, ins))] += w
        states = nxt
    tot = sum(states.values())
    return F(sum(w for (x, y), w in states.items() if x != y), tot)


p6 = singles_of('k-1', 4, 'P6')
R.check(p6 == ['RRR', 'BBB'], f'K-1 P6 starts {p6}')
pm = {m: p_unmatched(tuple(p6), m) for m in range(0, 11)}
R.check(pm[3] == F(7, 9), f'K-1 P6: P(still unmatched after 3 draws) = {pm[3]} (match by 3 = {1 - pm[3]} = 6/27)')
R.check(pm[6] == F(189, 729) and pm[10] > 0, f'K-1 P6: unmatched after 6 draws {pm[6]} = {float(pm[6]):.3f}; after 10 {float(pm[10]):.4f} > 0')
R.check(all(pm[m] == 3 * F(2, 3) ** m - 3 * F(1, 3) ** m for m in range(1, 11)),
        'from RRR/BBB, P(unmatched after m) = P(some slot unnamed) = 3(2/3)^m - 3(1/3)^m exactly')
R.check(all(pm[m] <= 3 * F(2, 3) ** m for m in range(0, 11)), 'overview union bound 3(2/3)^m holds')
quote('From RRR/BBB, drawing “1 becomes R” six times leaves RRR/RBB')
R.check((run('RRR', [(1, 'R')] * 6), run('BBB', [(1, 'R')] * 6)) == ('RRR', 'RBB'), 'K-1 P6 guide example')
quote('A counterexample is 1→R, 1→R, 1→R from RRR/BBB, leaving RRR/RBB')
R.check((run('RRR', [(1, 'R')] * 3), run('BBB', [(1, 'R')] * 3)) == ('RRR', 'RBB'), '2-3 P4 guide 3-draw counterexample')
R.check(run('RRR', [(1, 'R')] * 10) != run('BBB', [(1, 'R')] * 10), '2-3 P4: ten repeats of 1→R also fail')
fail3 = [s for s in itertools.product(SETS, repeat=3) if not universal(s)]
R.check(len(fail3) == 216 - 48, f'2-3 P4: {len(fail3)} of 216 three-draw stories fail some pair')

# ---------------------------------------------------------------------------------
# 4. Toggles (2-3 P6, 4-5 P4) and mixed stories (2-3 P7, 4-5 P5)
# ---------------------------------------------------------------------------------
R.check(run('RBR', [('T', 2)]) == 'RRR' and run('BRB', [('T', 2)]) == 'BBB',
        'toggle picture: toggling slot 2 sends RBR/BRB to RRR/BBB')
tp = [(p['top'], p['bottom']) for p in sorted([v for k, v in D['grades-2-3']['pages'][3]['sections'].items()
                                               if k.startswith('rule')][0]['pairs'], key=lambda p: p['x'])]
R.check(tp == [('RBR', 'BRB'), ('RRR', 'BBB')], f'toggle picture read from page: {tp}')


def dis(a, b):
    return frozenset(i for i in range(3) if a[i] != b[i])


ok = True
for L in range(0, 7):
    for s in itertools.product(TOGGLES, repeat=L):
        for a in BOARDS:
            for b in BOARDS:
                ok &= dis(run(a, s), run(b, s)) == dis(a, b)
R.check(ok, '4-5 P4: every toggle story of length <= 6 preserves the disagreement set of every pair')
R.check(all(len({run(a, s) for a in BOARDS}) == 8 for L in range(4) for s in itertools.product(TOGGLES, repeat=L)),
        '4-5 P4 guide: each toggle story is a bijection of the eight boards')

p6pairs = pairs_of('grades-2-3', 4, 'P6')
reach = {}
for a, b in p6pairs:
    states = {(a, b)}
    frontier = [(a, b)]
    while frontier:
        nf = []
        for x, y in frontier:
            for t in TOGGLES:
                s = (apply(x, t), apply(y, t))
                if s not in states:
                    states.add(s)
                    nf.append(s)
        frontier = nf
    reach[(a, b)] = any(x == y for x, y in states)
R.check(p6pairs == [('RBR', 'RRR'), ('RRB', 'BRR'), ('BRB', 'BRB')] and
        [reach[p] for p in p6pairs] == [False, False, True],
        f'2-3 P6: pairs {p6pairs}; can be matched by toggles: {[reach[p] for p in p6pairs]} (only the already-equal pair)')

MIXED = SETS + TOGGLES
ok_crit = True
count = 0
for L in range(0, 6):
    for s in itertools.product(MIXED, repeat=L):
        assigned = {i for (i, c) in s if i != 'T'}
        ok_crit &= (len(finishes(s)) == 1) == (assigned == {1, 2, 3})
        count += 1
R.check(ok_crit, f'2-3 P7 / 4-5 P5 / overview: over all {count} mixed stories of length <= 5, every start gives the '
        'same finish iff each slot gets at least one colour-setting instruction')
# number of finishes for a mixed story is 2^(slots never assigned)
ok_u = all(len(finishes(s)) == 2 ** (3 - len({i for (i, c) in s if i != 'T'}))
           for L in range(0, 5) for s in itertools.product(MIXED, repeat=L))
R.check(ok_u, 'mixed stories of length <= 4: finishes = 2^(slots never assigned)')
s = parse_story(quote('1→R, toggle 1, 2→B, 3→R').replace('toggle 1', 'toggle 1'))
R.check(finishes(s) == {'BBR'}, '2-3 P7 guide: 1→R, toggle 1, 2→B, 3→R sends every start to BBR')
quote('Every start finishes BBR')
s = parse_story('1→R, toggle 2')
quote('A mixed story that can fail: 1→R, toggle 2. From RRR/BBB it produces RBR/RRB')
R.check((run('RRR', s), run('BBB', s)) == ('RBR', 'RRB'), '2-3 P7 guide: 1→R, toggle 2 on RRR/BBB gives RBR/RRB')
# toggles never undo an agreement
R.check(all((x[i] == y[i]) == (apply(x, t)[i] == apply(y, t)[i]) for x in BOARDS for y in BOARDS
            for t in TOGGLES for i in range(3)), '2-3 P7 guide: a shared toggle neither erases nor creates agreement')

# ---------------------------------------------------------------------------------
# 5. Random colours (4-5 P6, P7, overview)
# ---------------------------------------------------------------------------------
pos = [1, 3, 1, 2]
R.check('Suppose the chosen slots are 1, 3, 1, 2, in that order' in D['grades-4-5']['problems'][5],
        '4-5 P6 position story read from the TeX statement: 1,3,1,2')
for start in BOARDS:
    cnt = Counter(run(start, list(zip(pos, cols))) for cols in itertools.product('RB', repeat=4))
    if not (len(cnt) == 8 and set(cnt.values()) == {2}):
        R.check(False, f'4-5 P6: start {start} gives {cnt}')
        break
else:
    R.check(True, '4-5 P6: for each of the 8 starts, each of the 8 final boards comes from exactly 2 of the 16 colour stories')
cols = itertools.product('RB', repeat=4)
R.check(all(run('RRR', list(zip(pos, c))) == c[2] + c[3] + c[1] for c in itertools.product('RB', repeat=4)),
        '4-5 P6 guide: final board is (c3, c4, c2)')

ok7 = True
for m in range(3, 8):
    for ps in itertools.product((1, 2, 3), repeat=m):
        if set(ps) != {1, 2, 3}:
            continue
        for start in ('RRR', 'BRB'):
            cnt = Counter(run(start, list(zip(ps, c))) for c in itertools.product('RB', repeat=m))
            ok7 &= len(cnt) == 8 and set(cnt.values()) == {2 ** (m - 3)}
R.check(ok7, '4-5 P7: every covering position story of length 3-7 gives all 8 boards equal weight from any start')

# conditional uniformity under fully random draws, and start-dependence without coverage
for m in (3, 4, 5, 6):
    for start in BOARDS:
        cov = Counter()
        allc = Counter()
        for st in itertools.product(SETS, repeat=m):
            f = run(start, st)
            allc[f] += 1
            if visited(st) == {1, 2, 3}:
                cov[f] += 1
        if not (len(cov) == 8 and len(set(cov.values())) == 1):
            R.check(False, f'overview: covering draws of length {m} from {start} not uniform')
            break
    else:
        R.check(True, f'overview: {m} random draws, conditional on covering, give each final board probability 1/8 from every start')
d4 = {start: Counter(run(start, st) for st in itertools.product(SETS, repeat=4)) for start in ('RRR', 'BBB')}
R.check(d4['RRR'] != d4['BBB'], f'4-5 P7: after 4 random draws the final distribution still depends on the start '
        f'(P(RRR) = {F(d4["RRR"]["RRR"], 6 ** 4)} from RRR vs {F(d4["BBB"]["RRR"], 6 ** 4)} from BBB)')
cov4 = sum(1 for ps in itertools.product((1, 2, 3), repeat=4) if set(ps) == {1, 2, 3})
R.check(cov4 == 36, f'4 random draws cover all slots in {cov4}/81 = {F(cov4, 81)} of slot stories')
quote('Four draws of 1→R leave slots 2 and 3 unchanged')

# stopping rules that look at colours break uniformity (overview caution)
# rule: draw until coverage AND slot 1 shows R (within 6 draws); look at the stopped boards
law = Counter()
for st in itertools.product(SETS, repeat=6):
    b = 'BBB'
    seen = set()
    for k, ins in enumerate(st):
        b = apply(b, ins)
        seen.add(ins[0])
        if seen == {1, 2, 3} and b[0] == 'R':
            break
    if seen == {1, 2, 3} and b[0] == 'R':
        law[b] += 1
R.check(sorted(law) == sorted(x for x in BOARDS if x[0] == 'R'),
        f'overview caution: stopping at the first covered board whose slot 1 is R gives only {len(law)} of the 8 boards, so the stopped board is not uniform')

# ---------------------------------------------------------------------------------
# 6. Guide quotes for the 4-5 P2 table and materials arithmetic
# ---------------------------------------------------------------------------------
quote('BRR, BBR (2)')
quote('RRB (1)')
quote('RBR, RBB, BBR, BBB (4)')
quote('The displayed pairs need 1, 2, 0, 3 instructions in reading order')
quote('For ten children in pairs, prepare ten three-slot paper strips, thirty reversible R/B counters, and five cups')
pairs_n = 10 // 2
R.check(pairs_n * 2 == 10 and 10 * 3 == 30 and pairs_n == 5, 'materials: 5 pairs x 2 strips = 10; 10 strips x 3 = 30 counters; 5 cups')
quote('Print four pages per grade band')
R.check(all(len(D[b]['pages']) == 4 for b in ['k-1', 'grades-2-3', 'grades-4-5']), 'each band has four pages')
quote('Toggle slot 2 to get RRR and BBB')
quote('the first remains RBR and the second becomes BBB')
quote('after m draws, the chance some slot is missing is at most 3(2/3)')

R.summary('check_base')
