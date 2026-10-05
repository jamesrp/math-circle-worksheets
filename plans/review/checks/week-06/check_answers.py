"""Every Week 6 problem, every band, the adult guide and the return visit.

Puzzle records, board sizes and block drawings are read back from the
delivered PDFs (pdf_data.json, written by extract_pdf.py).  Rules and numbers
that appear only in text are typed in from the PDFs, and each guide sentence
that is checked is first confirmed to be in the delivered guide PDF.
Answers come from codegame.py (exhaustive search).  Lines starting with
"MISMATCH" or "NOTE" are the ones to read.
"""
import os, sys, json, re, subprocess, math
from itertools import combinations, product, permutations
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from codegame import (HERE, PKT, codes, score, flip, fits, split, can_identify, min_identify,
                      can_end, min_end, separates, min_fixed, min_questions_any,
                      min_questions_pointing, weighing_min, weighing_min_bruteforce,
                      full_binary_depth_profiles, concat, collisions, sardinas_patterson)

GEO = os.path.join(HERE, 'pdf_data.json')
if not os.path.exists(GEO):
    subprocess.run([sys.executable, os.path.join(HERE, 'extract_pdf.py')], check=True, stdout=subprocess.DEVNULL)
D = json.load(open(GEO))

issues, notes = [], []


def check(label, ok, detail=''):
    print(f"  {'ok      ' if ok else 'MISMATCH'} {label}" + (f': {detail}' if detail else ''))
    if not ok:
        issues.append(label)


def note(label, detail=''):
    print(f'  NOTE     {label}' + (f': {detail}' if detail else ''))
    notes.append(label)


def pdftext(fn):
    t = subprocess.run(['pdftotext', os.path.join(PKT, fn), '-'], capture_output=True, text=True).stdout
    t = t.replace('’', "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('−', '-')
    t = t.replace('ﬁ', 'fi').replace('ﬂ', 'fl')
    # drop running heads and feet so that sentences broken by a page turn still match
    t = re.sub(r'Week 6 / Code breaking / Adult (return-visit )?guide\s*', ' ', t)
    t = re.sub(r'Bellingham Math Circle / Week 6 / (F06-FAC-v4|RV6-FAC-v1)\s+\d+\s*', ' ', t)
    t = t.replace('\f', ' ')
    return re.sub(r'\s+', ' ', t)


GUIDE = pdftext('week-06-facilitator.pdf')
RVG = pdftext('week-06-return-visit-facilitator.pdf')


def quoted(text, q, where='guide'):
    qn = re.sub(r'\s+', ' ', q.replace('–', '-'))
    ok = qn in text
    check(f'{where} says: "{q[:90]}{"..." if len(q) > 90 else ""}"', ok, '' if ok else 'quote NOT found in delivered PDF')
    return ok


def page(band, p):
    return D[band][p - 1]


def blocks_on(band, p):
    return {b['name']: b for b in page(band, p)['blocks']}


# ------------------------------------------------------------- the solver
print('== Solver results (exhaustive adaptive search)')
MI = {n: min_identify(n) for n in (2, 3, 4)}
ME = {n: min_end(n) for n in (2, 3, 4)}
for n in (2, 3, 4):
    print(f'  n={n}: {2**n} secrets; fewest tests that always identify = {MI[n]}; fewest that always end on a full score = {ME[n]}')
print(f'  n=5: identify in 3 always? {can_identify(5, 3)}; in 4? {can_identify(5, 4)}')

# independent second method for the two lower bounds the pages rely on
def explicit_lower_bound(n, k):
    """Explicit loops (no memo): is there a first test and adaptive later tests
    separating all secrets within k tests?  Returns True if possible."""
    T = codes(n)
    def rec(cands, k):
        if len(cands) <= 1:
            return True
        if k == 0:
            return False
        return any(all(rec(g, k - 1) for g in split(T, cands, t).values()) and len(split(T, cands, t)) > 1 for t in T)
    return rec(T, k)
check('second method: 1 test cannot do 2 counters', not explicit_lower_bound(2, 1))
check('second method: 2 tests cannot do 3 counters', not explicit_lower_bound(3, 2))
check('second method: 3 tests cannot do 4 counters', not explicit_lower_bound(4, 3))
check('second method: 2/3/4 tests do 2/3/4 counters', all(explicit_lower_bound(n, n) for n in (2, 3, 4)))

# ------------------------------------------------------------- blocks
SIDES = {name: b['n'] for name, b in blocks_on('k-1', 2).items()}
print('== Block drawings: number of sides as drawn (K-1 p2):', SIDES)
for band, p in (('k-1', 1), ('k-1', 2), ('grades-2-3', 1), ('grades-2-3', 2)):
    B = blocks_on(band, p)
    reg = (B['green triangle']['sides_rel'] == [1.0] * 3 and set(B['yellow hexagon']['sides_rel']) == {1.0}
           and all(abs(a - 120) < 0.05 for a in B['yellow hexagon']['angles'])
           and all(abs(a - 60) < 0.05 for a in B['green triangle']['angles']))
    check(f'{band} p{p}: triangle and hexagon drawn regular, equal x/y scale', reg and page(band, p)['scales'] == [[1.0, 1.0]])
    check(f'{band} p{p}: chevron = 2 rhombi in area, concave, 6 sides',
          abs(B['purple chevron']['area_in_triangles'] - 2 * B['blue rhombus']['area_in_triangles']) < 0.01
          and not B['purple chevron']['convex'] and B['purple chevron']['n'] == 6)
    check(f'{band} p{p}: same side counts as K-1 p2', {k: v['n'] for k, v in B.items()} == SIDES)

COLOUR = {n: n.split()[0] for n in SIDES}
ORDER = ['green triangle', 'blue rhombus', 'red trapezoid', 'yellow hexagon',
         'purple chevron', 'pink right triangle', 'teal kite', 'gray dart']
TOP = ORDER[:4]
# top row on the K-1 P3 picture, from the drawing positions
k1p2 = page('k-1', 2)


def question_tree_unique(items, tree):
    """Play an adaptive plan for every item; return dict item -> (pattern, items left)."""
    out = {}
    for x in items:
        left, pat, d = list(items), '', 0
        while len(left) > 1 and d < 5:
            q = tree(tuple(left), d)
            a = q(x)
            pat += 'Y' if a else 'N'
            left = [y for y in left if q(y) == a]
            d += 1
        out[x] = (pat, left)
    return out


print('== K-1')
print(' P1: four blocks, two questions')
check('K-1 P1 two questions always suffice for 4 (exhaustive split search)', min_questions_any(4) == 2)
four = TOP
q4 = [b for b in four if SIDES[b] == 4]
check('guide K-1 P1 "Does it have four sides?" splits the four 2/2', len(q4) == 2 and set(q4) == {'blue rhombus', 'red trapezoid'})
quoted(GUIDE, 'Yes leaves rhombus and trapezoid; no leaves triangle and hexagon.')
print(' P2: pointing only')
check('K-1 P2 / 2-3 P1 pointing only: worst case 7 questions before sure', min_questions_pointing(8) == 7)
quoted(GUIDE, 'After seven "no" answers one block is left, so you are sure without asking.')
print(' P3: eight blocks, three questions')
check('K-1 P3 three questions suffice for 8; two never', min_questions_any(8) == 3)
plan = lambda left, d: ((lambda x: x in TOP) if d == 0 else (lambda x: SIDES[x] == 4) if d == 1 else (lambda x, l=left: x == l[0]))
res = question_tree_unique(ORDER, plan)
check('guide K-1 P3 plan (top row?, four sides?, point) ends at one block for all 8', all(len(v[1]) == 1 for v in res.values()) and max(len(v[0]) for v in res.values()) == 3,
      str({k: v[0] for k, v in res.items()}))
quoted(GUIDE, 'Is it in the top row of the picture?" (triangle, rhombus, trapezoid, hexagon). "Does it have four sides?" Two blocks are left: "Is it this one?"')
print(' P4: two questions')
# exhaustive over all subsets: any adaptive two-question plan leaves two blocks together
from functools import lru_cache
@lru_cache(None)
def best_left(mask, k):
    items = [i for i in range(8) if mask >> i & 1]
    if k == 0:
        return len(items)
    best = len(items)
    for q in range(256):
        y, n_ = mask & q, mask & ~q & 255
        best = min(best, max(best_left(y, k - 1) if y else 0, best_left(n_, k - 1) if n_ else 0))
    return best
check('K-1 P4 / 2-3 P3: every adaptive 2-question plan (all 256 subsets each time) leaves >= 2 blocks for some secret', best_left(255, 2) == 2)
check('... and 3 questions can leave 1', best_left(255, 3) == 1)
quoted(GUIDE, 'Whatever the first question is, the yes pile or the no pile has at least four blocks. The second question leaves at least two of those.')
print(' P5, P8: counting secrets')
check('K-1 P5: 4 two-counter secrets; trays on p3 hold 6', len(codes(2)) == 4 and page('k-1', 3)['tray_slot_count'] == 12)
check('K-1 P8: 8 three-counter secrets; trays on p6 hold 10', len(codes(3)) == 8 and page('k-1', 6)['tray_slot_count'] == 30)
check('guide K-1 P8 hint: 1, 3, 3, 1 secrets with 3, 2, 1, 0 reds', [sum(1 for s in codes(3) if s.count('R') == r) for r in (3, 2, 1, 0)] == [1, 3, 3, 1])
print(' P6: two-counter game')
T2 = codes(2)
check('K-1 P6 one test never always enough (every test leaves a group of 2)', all(max(len(g) for g in split(T2, T2, t).values()) >= 2 for t in T2))
check('K-1 P6 two tests always enough', can_identify(2, 2))
check('guide: every test has two secrets that score 1', all(len(split(T2, T2, t).get(1, [])) == 2 for t in T2))
sep = [t for t in T2 if len(split(T2, ['RY', 'YR'], t)) == 2]
check('guide: after RR scores 1, the second test must have one red and one yellow', sorted(sep) == ['RY', 'YR'], str(sep))
check('guide: RR scoring 0 or 2 settles it at once', split(T2, T2, 'RR')[0] == ['YY'] and split(T2, T2, 'RR')[2] == ['RR'])
quoted(GUIDE, 'Test red-red: 2 means red-red; 0 means yellow-yellow; 1 means red-yellow or yellow-red, so test red-yellow next: 2 means red-yellow, 0 means yellow-red.')
b = page('k-1', 4)['board']
check('K-1 p4 board: 2 slots secret/copy, 2 triangle outlines, 3 test rows with score boxes', b['rows_above_fold'] == [2, 2] and b['triangles'] == 2 and b['rows_below_fold'] == [2, 2, 2] and b['score_boxes'] == 3)
print(' P7: drawn tests')
k1 = page('k-1', 5)['k1_puzzles']
check('K-1 P7 drawn counters: fill colour matches letter on every counter', page('k-1', 5)['k1_colours_ok'])
guide_k1 = [['RR'], ['YR'], ['RY', 'YR'], ['RY'], ['YY']]
for i, pz in enumerate(k1):
    sol = fits([tuple(r) for r in pz])
    check(f'K-1 P7 row {i+1} {pz}: answer {sol} (two trays per row)', sorted(sol) == sorted(guide_k1[i]) and len(sol) <= 2)
quoted(GUIDE, 'Row 1 (RR scores 2): RR. Row 2 (RY scores 0): YR. Row 3 (RR scores 1): RY and YR, both trays. Row 4 (RR 1, YR 0): RY. Row 5 (RY 1, RR 0): YY.')
print(' P9: three-counter game')
T3 = codes(3)
check('K-1 P9 three tests always enough', can_identify(3, 3))
ok = all(score('YRR', s) - score('RRR', s) == (1 if s[0] == 'Y' else -1) and score('RYR', s) - score('RRR', s) == (1 if s[1] == 'Y' else -1) for s in T3)
check('guide K-1 P9 rule: YRR/RYR score up by one = yellow there, down by one = red', ok)
check('guide method RRR, YRR, RYR separates all 8 (fixed in advance)', separates(['RRR', 'YRR', 'RYR'], 3))
b = page('k-1', 7)['board']
check('K-1 p7 board: 3 slots, 3 outlines, 4 test rows', b['rows_above_fold'] == [3, 3] and b['triangles'] == 3 and b['rows_below_fold'] == [3] * 4)

print('== Grades 2-3')
check('2-3 P1 naming one block: at most 7', min_questions_pointing(8) == 7)
quoted(GUIDE, 'Naming one block at a time: at most 7 (the round ends when you are sure; 8 if they also ask about the last block).')
print(' P2: the guide\'s three fixed questions')
Q = [lambda x: x in TOP, lambda x: SIDES[x] == 4, lambda x: COLOUR[x] in ('red', 'yellow', 'purple', 'gray')]
pats = {x: ''.join('Y' if q(x) else 'N' for q in Q) for x in ORDER}
guide_pats = {'green triangle': 'YNN', 'blue rhombus': 'YYN', 'red trapezoid': 'YYY', 'yellow hexagon': 'YNY',
              'purple chevron': 'NNY', 'pink right triangle': 'NNN', 'teal kite': 'NYN', 'gray dart': 'NYY'}
check('2-3 P2 guide patterns match the drawn shapes and colours', pats == guide_pats, str(pats))
check('2-3 P2 guide patterns all different', len(set(pats.values())) == 8)
quoted(GUIDE, 'Q1 "Is it the triangle, rhombus, trapezoid or hexagon?" (top row of the picture)')
# Is there a "top row" in the 2-3 P2 picture?  Count rows of block drawings on p2 by their label line
p2 = page('grades-2-3', 2)
labels_lines = [t for t in p2['text'] if 'green triangle' in t or 'purple chevron' in t]
if len(labels_lines) == 1 and 'gray dart' in labels_lines[0]:
    note('2-3 P2 picture is ONE row of eight blocks, so the guide\'s "(top row of the picture)" has no top row on that page '
         '(the two-row picture is on 2-3 p1)', labels_lines[0])
print(' P3')
check('2-3 P3 two questions never always enough', best_left(255, 2) >= 2)
print(' P4, P5: two counters')
check('2-3 P4 two tests suffice; RR then RY', can_identify(2, 2))
vec = {s: (score('RR', s), score('RY', s)) for s in T2}
check('guide 2-3 P5 fixed pair RR, RY vectors', vec == {'RR': (2, 1), 'RY': (1, 2), 'YR': (1, 0), 'YY': (0, 1)}, str(vec))
check('guide 2-3 P5: the two one-turn rows of any test both score 1', all(score(t, flip(t, {i})) == 1 for t in T2 for i in (0, 1)))
b = page('grades-2-3', 3)['board']
check('2-3 p3 board: 2 counters, 3 test rows', b['rows_above_fold'] == [2, 2] and b['rows_below_fold'] == [2] * 3 and b['triangles'] == 2)
check('2-3 p4 record tables: 4 tables x 5 rows x (2+1) cells', page('grades-2-3', 4)['record_table_cells'] == 60)
print(' P6')
check('2-3 P6 three tests suffice, two never', MI[3] == 3)
b = page('grades-2-3', 5)['board']
check('2-3 p5 board: 3 counters, 4 test rows', b['rows_above_fold'] == [3, 3] and b['rows_below_fold'] == [3] * 4)
print(' P7: finished games (read from PDF)')
g23 = page('grades-2-3', 6)['records']
guide23 = [['RRY', 'RYR', 'YRR'], ['YRR', 'YYY'], ['RRY'], ['RRR'], []]
for i, gm in enumerate(g23):
    sol = fits([tuple(r) for r in gm])
    check(f'2-3 P7 game {i+1} {gm}: {sol}', sorted(sol) == sorted(guide23[i]))
gm = [tuple(r) for r in g23[2]]
sub = {len(c): [len(fits(list(c))) for c in combinations(gm, len(c))] for c in [gm[:1], gm[:2]]}
check('guide 2-3 P7 game 3: each row alone leaves 3, each pair leaves 2, so all three needed', sub == {1: [3, 3, 3], 2: [2, 2, 2]}, str(sub))
quoted(GUIDE, 'Game 5 (RRR 3, RYR 1): none. RRR scoring 3 means the secret is RRR, and then RYR would score 2: the keeper made a scoring mistake.')
check('2-3 p6 cell fills: R cells pink, Y cells yellow', set(map(tuple, page('grades-2-3', 6)['record_fills']['R'])) == {(246, 207, 212)} and set(map(tuple, page('grades-2-3', 6)['record_fills']['Y'])) == {(252, 233, 161)})
print(' P8: lookup table in the guide PDF')
tab = re.search(r'Secret RRR YRR RYR((?: [RY]{3} \d \d \d){8})', GUIDE)
if tab:
    rows = re.findall(r'([RY]{3}) (\d) (\d) (\d)', tab.group(1))
    ok = all((int(a), int(b_), int(c)) == (score('RRR', s), score('YRR', s), score('RYR', s)) for s, a, b_, c in rows) and len(rows) == 8
    check('guide p7 score table RRR/YRR/RYR: all 8 rows correct', ok)
else:
    # layout text order may interleave; fall back to the -layout extraction
    lay = subprocess.run(['pdftotext', '-layout', '-f', '7', '-l', '7', os.path.join(PKT, 'week-06-facilitator.pdf'), '-'], capture_output=True, text=True).stdout
    rows = re.findall(r'\b([RY]{3})\s+(\d)\s+(\d)\s+(\d)\s*$', lay, re.M)
    ok = len(rows) == 8 and all((int(a), int(b_), int(c)) == (score('RRR', s), score('YRR', s), score('RYR', s)) for s, a, b_, c in rows)
    check('guide p7 score table RRR/YRR/RYR: all 8 rows correct (layout text)', ok, str(rows))
print(' P9: ending on a full score')
check('2-3 P9: the breaker can always end by the 4th test', can_end(3, 4))
check('guide 2-3 P9: ending by the 3rd test cannot be promised', not can_end(3, 3))
print(' P10, P11: four counters')
check('2-3 P10 four tests suffice, three never', MI[4] == 4)
check('guide 2-3 P11 RRRR, YRRR, RYRR, RRYR separates all 16', separates(['RRRR', 'YRRR', 'RYRR', 'RRYR'], 4))
check('guide 2-3 P11: all red plus one test per place (5 tests) also works', separates(['RRRR', 'YRRR', 'RYRR', 'RRYR', 'RRRY'], 4))
alt = separates(['YRRR', 'RYRR', 'RRYR', 'RRRY'], 4)
quoted(GUIDE, 'Testing every place separately without the count takes 5.')
if alt:
    dec = {s: tuple(score(t, s) for t in ['YRRR', 'RYRR', 'RRYR', 'RRRY']) for s in codes(4)}
    note('guide 2-3 P11 "Testing every place separately without the count takes 5": the four one-place tests '
         'YRRR, RYRR, RRYR, RRRY alone (no all-red test) separate all 16 secrets in 4 tests',
         f"RRRR -> {dec['RRRR']}, YYYY -> {dec['YYYY']}, RYRY -> {dec['RYRY']}; higher scores mark the yellow places")
b = page('grades-2-3', 9)['board']
check('2-3 p9 board: 4 counters, 4 test rows', b['rows_above_fold'] == [4, 4] and b['rows_below_fold'] == [4] * 4)

print('== Grades 4-5')
check('4-5 P1: 1-16 needs 4; 1-20 needs 5 (exhaustive split search)', min_questions_any(16) == 4 and min_questions_any(20) == 5)
chain = [20]
while chain[-1] > 1:
    chain.append(math.ceil(chain[-1] / 2))
check('guide 4-5 P1 chain 20, 10, 5, 3, 2, 1 (worst side each time)', chain == [20, 10, 5, 3, 2, 1])
check('guide: 2^3 = 8 < 16 and 2^4 = 16 < 20; 7 for 1-100 (64 < 100)', 2**3 < 16 and 2**4 < 20 and min_questions_any(100) == 7)
print(' P3: finished games (read from PDF)')
g45 = page('grades-4-5', 3)['records']
guide45 = [['RRR'], ['RRY', 'RYR'], ['RYYY'], ['RRRR', 'YYYY'], []]
for i, gm in enumerate(g45):
    sol = fits([tuple(r) for r in gm])
    check(f'4-5 P3 game {i+1} {gm}: {sol}', sorted(sol) == sorted(guide45[i]))
g5 = [t for t, _ in g45[4]]
check('guide 4-5 P3 game 5: all three tests have an even number of Y', all(t.count('Y') % 2 == 0 for t in g5))
check('guide parity rule: score parity = parity of Y in secret when the test has an even number of Y (n=4, all pairs)',
      all(score(t, s) % 2 == s.count('Y') % 2 for t in codes(4) if t.count('Y') % 2 == 0 for s in codes(4)))
check('guide child reason: changing two counters of a test changes any score by 0 or 2',
      all(abs(score(t, s) - score(flip(t, set(q)), s)) in (0, 2) for t in codes(4) for s in codes(4) for q in combinations(range(4), 2)))
quoted(GUIDE, 'Game 4 (RRYY 2, RYRY 2, RYYR 2): RRRR and YYYY.')
print(' P4-P6')
check('4-5 P4 three-counter method in 3 tests exists', can_identify(3, 3))
check('4-5 P6 four-counter method in 4 tests exists', can_identify(4, 4))
ok = all(score(t, s) - score('RRRR', s) == (1 if s[i] == 'Y' else -1) for i, t in enumerate(['YRRR', 'RYRR', 'RRYR']) for s in codes(4))
check('guide 4-5 P6: each later score is one more (yellow) or one less (red) than the first', ok)
print(' P7')
check('4-5 P7: turning over both counters in one place never changes the score (n = 1..5, every place)',
      all(score(t, s) == score(flip(t, {i}), flip(s, {i})) for n in range(1, 6) for t in codes(n) for s in codes(n) for i in range(n)))
print(' P8')
check('4-5 P8 one test cannot do two counters', not can_identify(2, 1))
check('4-5 P8 two tests cannot do three counters (adaptive)', not can_identify(3, 2))
check('guide: 4*4 = 16 >= 8, so counting alone does not settle it', 4 * 4 >= 8)
check('guide: turning over one counter changes a row\'s score on any test by exactly 1 (n = 2..4)',
      all(abs(score(t, s) - score(t, flip(s, {i}))) == 1 for n in (2, 3, 4) for t in codes(n) for s in codes(n) for i in range(n)))
quoted(GUIDE, 'Turning over one counter changes a row\'s score on any other test by exactly 1.')
print(' P9: the guide\'s argument, checked case by case')
ok_formula = True
for t1 in codes(4):
    six = [(flip(t1, set(Q)), set(Q)) for Q in combinations(range(4), 2)]
    for T in codes(4):
        Dp = {i for i in range(4) if T[i] != t1[i]}
        s = score(T, t1)
        for r, Qs in six:
            if score(T, r) != s - 2 + 2 * len(Qs & Dp):
                ok_formula = False
check('guide formula s - 2 + 2|Q n D| for the six two-turn rows (all 16 first tests, all 16 later tests)', ok_formula)
splits = {}
for T in codes(4):
    Dp = sum(1 for i in range(4) if T[i] != 'R')
    six = [flip('RRRR', set(Q)) for Q in combinations(range(4), 2)]
    sizes = tuple(sorted(len(g) for g in split(None, six, T).values()))
    splits.setdefault(Dp, set()).add(sizes)
check('guide splits by |D| = 0..4: 6; 3+3; 1+4+1; 3+3; 6', splits == {0: {(6,)}, 1: {(3, 3)}, 2: {(1, 1, 4)}, 3: {(3, 3)}, 4: {(6,)}}, str(splits))
# after test 1 scores 2, any test 2 and any adaptive test 3 leave two of the six together
worst_ok = True
for t1 in codes(4):
    six = [flip(t1, set(Q)) for Q in combinations(range(4), 2)]
    for t2 in codes(4):
        for g in split(None, six, t2).values():
            if len(g) >= 3 and any(len(split(None, g, t3)) == len(g) for t3 in codes(4)):
                worst_ok = False
check('guide: every group of >= 3 left after test 2 keeps two secrets together under any test 3', worst_ok)
check('guide: "never two, two and two"', all(sizes != (2, 2, 2) for v in splits.values() for sizes in v))
quoted(GUIDE, 'As |D| = 0, 1, 2, 3, 4, test 2 splits the six as 6; 3+3; 1+4+1; 3+3; 6, so a group of 3 or 4 is left.')
if any(max(sz) == 6 for v in splits.values() for sz in v):
    note('guide 4-5 P9 "so a group of 3 or 4 is left": for |D| = 0 or 4 the group left is all six, a case the next sentences do not treat '
         '(three values for six rows still leaves two together)')
print(' P10')
check('4-5 P10 three counters: 4 tests to be sure of ending; four counters: 5', ME[3] == 4 and ME[4] == 5)
check('guide reduction: ending by test k implies knowing after k-1 (n = 2..4, k = 1..n+1)',
      all((not can_end(n, k)) or can_identify(n, k - 1) for n in (2, 3, 4) for k in range(1, n + 2)))
check('4-5 p9 record tables: 2 three-counter and 2 four-counter tables of 6 rows', page('grades-4-5', 9)['record_table_cells'] == 2 * 6 * 4 + 2 * 6 * 5)

print('== Guide: overview, materials, launch, section 5')
quoted(GUIDE, 'One wrong score makes a game impossible to solve')
# What does one wrong score do?  Standard methods, every secret, every test whose score is misreported by +-1
def play_with_one_error(n, strategy, s, j, d):
    """Play the guide's way against secret s, misreporting the j-th score by d.
    The breaker stops as soon as at most one secret fits.  Returns 'none',
    'wrong', 'right' or None (error impossible: score out of range / test not reached)."""
    rec = []
    while True:
        cand = fits(rec, n) if rec else codes(n)
        if len(cand) <= 1:
            break
        t = strategy(rec)
        sc = score(t, s)
        if len(rec) == j:
            sc += d
            if not 0 <= sc <= n:
                return None
        rec.append((t, sc))
    if len(rec) <= j:
        return None
    cand = fits(rec, n)
    return 'none' if not cand else 'right' if cand == [s] else 'wrong'


def fixed_order(tests):
    return lambda rec: tests[len(rec)]


def guide_two(rec):        # K-1 P6 / 2-3 P4: RR, and after a score of 1, RY
    return 'RR' if not rec else 'RY'


GUIDE_WAYS = {2: guide_two, 3: fixed_order(['RRR', 'YRR', 'RYR']), 4: fixed_order(['RRRR', 'YRRR', 'RYRR', 'RRYR'])}
wrong_examples = []
for n, way in GUIDE_WAYS.items():
    tally = {'none': 0, 'wrong': 0, 'right': 0}
    for s in codes(n):
        for j in range(n):
            for d in (-1, 1):
                r = play_with_one_error(n, way, s, j, d)
                if r:
                    tally[r] += 1
                    if r == 'wrong' and len(wrong_examples) < 4:
                        wrong_examples.append((n, s, j + 1, d))
    print(f"  info     n={n}, the guide's way, stopping when one secret fits: one score off by 1 -> "
          f"fits no secret {tally['none']} times, fits one WRONG secret {tally['wrong']} times, still right {tally['right']} times")
if wrong_examples:
    n, s, j, d = wrong_examples[0]
    note('guide overview "One wrong score makes a game impossible to solve": with the guide\'s own ways, a wrong score '
         'often leaves exactly one WRONG secret fitting', f'examples (n, secret, test misreported, by): {wrong_examples}')
check('full boards take 10, 18, 24 counters', [n + n + (3 if n == 2 else 4) * n for n in (2, 3, 4)] == [10, 18, 24])
check('K-1 pair 45 >= eight 3-counter secrets (24) + full 3-counter board (18) = 42', 45 >= 24 + 18)
check('counter totals: 2*45+10 = 100, 2*30+10 = 70, 30+10+10 = 50, sum 220', (2 * 45 + 10, 2 * 30 + 10, 30 + 10 + 10) == (100, 70, 50) and 100 + 70 + 50 == 220)
check('green triangles: 2*3+2 = 8, 2*4+2 = 10, 4+2 = 6, total 24', (2 * 3 + 2, 2 * 4 + 2, 4 + 2) == (8, 10, 6) and 8 + 10 + 6 == 24)
check('folders 3+3+2 = 8, pencils 5+5+4 = 14, whiteboards 2+2+3 = 7', 3 + 3 + 2 == 8 and 5 + 5 + 4 == 14 and 2 + 2 + 3 == 7)
quoted(GUIDE, 'a cut two-counter board (an extra copy of 2-3 p. 3), one folder, 6 counters, 2 green triangles.')
quoted(GUIDE, 'Take the copy and the triangles away. A second child makes the next test; score it the same way.')
launch_need = 2 + 2 + 2 + 2   # secret, test 1 (stays as the record), test 2, copy of test 2
if launch_need > 6:
    note('guide launch: 6 counters are too few for the scripted second test',
         f'secret 2 + first test row 2 (kept) + second test row 2 + copy of the second test 2 = {launch_need}')
check('launch: secret RY, test RR scores 1 under column 1; RY and YR fit', score('RR', 'RY') == 1 and fits([('RR', 1)]) == ['RY', 'YR'])
check('section 5: smallest k with (n+1)^k >= 2^n is 2 for n = 2, 3, 4', [min(k for k in range(10) if (n + 1) ** k >= 2 ** n) for n in (2, 3, 4)] == [2, 2, 2])
check('section 5: true minimum 2, 3, 4; full-score ending 3, 4, 5', [MI[n] for n in (2, 3, 4)] == [2, 3, 4] and [ME[n] for n in (2, 3, 4)] == [3, 4, 5])
check('section 5: n one-turn neighbours all score n-1 and any later test gives them at most two values',
      all(len({score(T, flip(t1, {i})) for i in range(n)}) <= 2 and all(score(t1, flip(t1, {i})) == n - 1 for i in range(n))
          for n in (2, 3, 4) for t1 in codes(n) for T in codes(n)))
check('section 5: parity rule d(t,s) = w(t)+w(s) mod 2 (n = 1..5)',
      all((len(t) - score(t, s)) % 2 == (t.count('Y') + s.count('Y')) % 2 for n in range(1, 6) for t in codes(n) for s in codes(n)))
check('section 5: fixed tests RRRRR, RRRYY, RRYRY, RYRRY give all 32 secrets different scores', separates(['RRRRR', 'RRRYY', 'RRYRY', 'RYRRY'], 5))
check('section 5: five counters need 4 (3 adaptive tests are not enough)', not can_identify(5, 3) and can_identify(5, 4))
k5, _ = min_fixed(5, 4)
check('section 5: smallest fixed set for five counters is 4', k5 == 4)
ok = all(score(t, s) == (s.count('R') - t.count('Y') + 2 * sum(1 for i in range(5) if t[i] == 'Y' and s[i] == 'Y')) for t in codes(5) for s in codes(5))
check('section 5: with the red count known, the score gives how many of the test\'s yellow places are yellow', ok)
check('section 5 / attention: 2^6 = 64 < 100 <= 128 = 2^7', 2**6 < 100 <= 2**7)

print('== Guide page references and board pages')
raw = re.sub(r'\s+', ' ', subprocess.run(['pdftotext', os.path.join(PKT, 'week-06-facilitator.pdf'), '-'], capture_output=True, text=True).stdout)
sec, refs = None, {}
for m in re.finditer(r'(K–1|2–3|4–5) table|Problem (\d+) page (\d+)', raw):
    if m.group(1):
        sec = {'K–1': 'k-1', '2–3': 'grades-2-3', '4–5': 'grades-4-5'}[m.group(1)]
    elif sec:
        refs.setdefault(sec, []).append((int(m.group(2)), int(m.group(3))))
for band in ('k-1', 'grades-2-3', 'grades-4-5'):
    actual = [(pr, pg['page']) for pg in D[band] for pr in pg['problems']]
    check(f'guide "Problem N page P" lines for {band} match the PDF', refs.get(band) == actual, str(refs.get(band)))
    nums = [pr for pr, _ in actual]
    check(f'{band}: problems numbered 1..{len(nums)} consecutively', nums == list(range(1, len(nums) + 1)))
    heads = {pg['header'] for pg in D[band]}
    foots = {re.sub(r' \d+$', '', pg['footer']) for pg in D[band]}
    print(f'  info     {band}: headers {heads}; footers {foots}')
boards = {band: [pg['page'] for pg in D[band] if 'board' in pg] for band in ('k-1', 'grades-2-3', 'grades-4-5')}
check('guide set-up list of code-board pages (K-1 pp. 4, 7; 2-3 pp. 3, 5, 9; 4-5 pp. 2, 5)', boards == {'k-1': [4, 7], 'grades-2-3': [3, 5, 9], 'grades-4-5': [2, 5]}, str(boards))
quoted(GUIDE, 'Set up every code board page (K-1 pp. 4, 7; 2-3 pp. 3, 5, 9; 4-5 pp. 2, 5).')
tri_side = {round(s_, 3) for band in boards for p_ in boards[band] for s_ in page(band, p_)['board']['triangle_sides']}
quoted(GUIDE, 'the slots must be 1 inch for a counter, and the triangle outlines must fit a green triangle.')
quoted(GUIDE, 'A counter fits inside a printed slot and a green triangle inside a printed outline. If not, the printer shrank the page.')
note('triangle outlines on every board are equilateral with side exactly the green block\'s 1 in (path centre, 0.7 pt line), '
     'so a 1 in triangle covers the outline rather than fitting inside it', f'sides {sorted(tri_side)} in')

print('== Return visit (F06-RV-v1)')
check('RV P1: one weighing cannot find 1 of 9; two can (search over actual card sets)', weighing_min_bruteforce(range(1, 10), 3) == 2)
plan_ok = True
for s in range(1, 10):
    o1 = 'L' if s in (1, 2, 3) else 'R' if s in (4, 5, 6) else 'B'
    grp = {'L': (1, 2, 3), 'R': (4, 5, 6), 'B': (7, 8, 9)}[o1]
    o2 = 'L' if s == grp[0] else 'R' if s == grp[1] else 'B'
    if {'L': grp[0], 'R': grp[1], 'B': grp[2]}[o2] != s:
        plan_ok = False
check('RV guide plan 123|456 then one-each identifies all 9', plan_ok)
counts = {N: weighing_min(N, 5) for N in range(1, 31)}
check('RV guide: 27 labels need exactly 3', counts[27] == 3 and weighing_min_bruteforce(range(1, 10), 3) == 2)
cap = all(counts[N] == math.ceil(math.log(N, 3) - 1e-9) if N > 1 else counts[N] == 0 for N in counts)
print(f'  info     equal-pan weighings never cost more than ceil(log3 N) for N = 1..30: {cap}')
quoted(RVG, 'an equal-pan constraint may forbid a desired split, though uniform powers of three avoid that issue.', 'RV guide')
freqs = {'A': 4, 'B': 2, 'C': 1, 'D': 1}
best = None
for prof in full_binary_depth_profiles(4):
    for perm in permutations(prof):
        c = sum(f * d for f, d in zip(freqs.values(), perm))
        if best is None or c < best[0]:
            best = (c, [perm])
        elif c == best[0]:
            best[1].append(perm)
check('RV P2: least total 14; every optimal plan has depths A1 B2 C3 D3, worst case 3',
      best[0] == 14 and set(best[1]) == {(1, 2, 3, 3)}, str(best))
check('RV P2: tree shapes with 4 leaves have depth profiles {2,2,2,2} and {1,2,3,3} only', full_binary_depth_profiles(4) == {(2, 2, 2, 2), (1, 2, 3, 3)})
check('RV P2: balanced plan costs 16', sum(f * 2 for f in freqs.values()) == 16)
books = {1: {'A': 'R', 'B': 'RY', 'C': 'Y'}, 2: {'A': 'R', 'B': 'YR', 'C': 'YY'}, 3: {'A': 'R', 'B': 'RY'}}
for k, bk in books.items():
    col = collisions(bk, 8)
    ud = sardinas_patterson(bk.values())
    print(f'  info     Book {k}: uniquely decodable (Sardinas-Patterson) = {ud}; collisions among messages of length <= 8: {len(col)}; first {col[:1]}')
check('RV P3: only Book 1 has collisions; B and AC both give RY', [k for k, bk in books.items() if not sardinas_patterson(bk.values())] == [1]
      and concat(books[1], 'B') == concat(books[1], 'AC') == 'RY')
pg3 = page('return-visit', 3)
check('RV p3 example: M=YR, N=R gives Y R | R then Y R R, counter colours match letters',
      [l for _, l, _ in pg3['rv_counters']] == list('YRRYRR') and all((l == 'R') == (tuple(f) == (218, 94, 83)) for _, l, f in pg3['rv_counters']))
check('RV p1 pan boxes 3.05 x 1.35 in, as the guide says', [3.05, 1.35] in page('return-visit', 1)['rect_sizes'])

print()
print(f'{len(issues)} MISMATCH lines; {len(notes)} NOTE lines')
for n_ in notes:
    print('  NOTE:', n_)
