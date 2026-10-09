"""Independent enumeration of every base Week 47 task, and of every claim in
the base adult guide.

Run pdf_extract.py first: the clue positions, board sizes, rows, star and
shaded marks used here are read from pdf_geometry.json (taken from the
delivered PDFs), not from the author's sources or answers.

Writes check_base.out.
"""
import json
import os
import re
import sys
from itertools import combinations, product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, PDFS, Log, completions, legal, page_text, path_edges, shortest_moves)  # noqa: E402

log = Log('Week 47 base packet: independent enumeration')
G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))
GUIDE = page_text(PDFS['guide'])
GUIDE_FLAT = re.sub(r'\s+', ' ', GUIDE)


def boards(band, prob):
    return [b for p in G[band]['pages'] for b in p['boards'] if b['problem'] == prob]


def rows(band, prob):
    return [r for p in G[band]['pages'] for r in p['rows'] if r['problem'] == prob]


def clues_of(board):
    return {int(k): v for k, v in board['clues'].items()}


def row_clues(row):
    return {i: int(v) for i, v in enumerate(row['values']) if v is not None and row['locked'][i]}


def tuples_in(text):
    return [tuple(int(x) for x in m.split(',')) for m in re.findall(r'\((\d+(?:,\d+)+)\)', text)]


def para(start, end):
    """Guide text between two markers (flattened)."""
    i = GUIDE_FLAT.index(start)
    j = GUIDE_FLAT.index(end, i + len(start)) if end else len(GUIDE_FLAT)
    return GUIDE_FLAT[i:j]


def envelope(n, clues):
    L = tuple(max([0] + [a - abs(i - c) for c, a in clues.items()]) for i in range(n))
    U = tuple(min(a + abs(i - c) for c, a in clues.items()) for i in range(n))
    return L, U


def text_of(band, page):
    return re.sub(r'\s+', ' ', G[band]['text'][page - 1])


BANDS = ('k-1', 'grades-2-3', 'grades-4-5')

# ------------------------------------------------------------------ Problem 1
log.section('Problem 1 (all bands): clues read from the board')
for band in BANDS:
    b = boards(band, 1)[0]
    n, cl = b['sites'], clues_of(b)
    sols = completions(n, path_edges(n), cl)
    mid = sorted({s[2] for s in sols})
    log.note('%s: %d sites, clues %s -> %d completions; middle (site 2) can be %s; tallest marker %d (board top %d)' % (
        band, n, cl, len(sols), mid, max(max(s) for s in sols), b['top_level']))
    log.check(len(sols) >= 4, '%s P1: at least four different landscapes exist (%d)' % (band, len(sols)))
    log.check(0 in mid and 3 in mid, '%s P1: middle height 0 possible and 3 possible' % band)
    log.check(max(max(s) for s in sols) <= b['top_level'], '%s P1: every completion fits on the printed board' % band)
P1 = completions(5, path_edges(5), {0: 1, 4: 1})
g = para('Problem 1, all bands.', 'Problem 2, all bands.')
ex = tuples_in(g)
log.check(len(ex) == 4 and all(t in P1 for t in ex) and len(set(ex)) == 4, 'guide P1: its four examples %s are different legal completions' % ex)
log.check('range is 0-3' in g and sorted({s[2] for s in P1}) == [0, 1, 2, 3], 'guide P1: "full possible range is 0-3" for the middle')

# ------------------------------------------------------------------ Problem 2
log.section('Problem 2 (all bands): starred marker')
for band in BANDS:
    b = boards(band, 2)[0]
    n, cl, star = b['sites'], clues_of(b), b['star_site']
    sols = completions(n, path_edges(n), cl)
    vals = sorted({s[star] for s in sols})
    log.note('%s: clues %s, star over site %s -> star heights %s (%d completions)' % (band, cl, star, vals, len(sols)))
    log.check(vals == [0, 1, 2], '%s P2: star can be exactly 0, 1, 2 (highest 2, lowest 0)' % band)
P2 = completions(5, path_edges(5), {0: 0, 4: 2})
g = para('Problem 2, all bands.', 'Problem 3.')
ex = tuples_in(g)
log.check(ex and all(t in P2 for t in ex) and sorted(t[2] for t in ex) == [0, 1, 2], 'guide P2: witnesses %s are legal with star heights 0,1,2' % ex)
log.check('possible heights are exactly 0, 1, 2' in g, 'guide P2: states exactly 0, 1, 2')
ub = min(a + abs(2 - c) for c, a in {0: 0}.items())
log.check(ub == 2, 'guide P2: the left clue alone bounds the star above by 2 (right clue alone allows %d)' % (2 + 2))

# ------------------------------------------------------------------ Problem 3
log.section('Problem 3: forced ramp')
rk = rows('k-1', 3)[0]
cl = row_clues(rk)
sols = completions(5, path_edges(5), cl)
log.note('k-1 P3 row clues %s -> completions %s' % (cl, sols))
log.check(sols == [(0, 1, 2, 3, 4)], 'k-1 P3: exactly one landscape, (0,1,2,3,4)')
for band in ('grades-2-3', 'grades-4-5'):
    r = rows(band, 3)[0]
    cl = row_clues(r)
    log.check(cl == {0: 0} and r['locked'][4] and r['values'][4] is None, '%s P3: left clue 0 printed, right clue box shaded and blank' % band)
    res = {}
    for rr in range(0, 12):
        res[rr] = len(completions(5, path_edges(5), {0: 0, 4: rr}, cap=20))
    forcing = [rr for rr, c in res.items() if c == 1]
    log.note('%s P3: completions by right-clue height %s' % (band, res))
    log.check(forcing == [4], '%s P3: the only right-clue height that forces every marker is 4' % band)
g = para('Problem 3.', 'Problem 4, all bands')
for rr in range(4):
    L, U = envelope(5, {0: 0, 4: rr})
    log.check(L != U, 'guide P3: r=%d least %s and greatest %s differ' % (rr, L, U))
log.check(all(res[rr] == 0 for rr in range(5, 12)), 'guide P3: larger heights (5..11) are impossible')

# ------------------------------------------------------------------ Problem 4
log.section('Problem 4: which clue sets can be completed')
for band in BANDS:
    b = boards(band, 4)[0]
    outs = []
    for r in rows(band, 4):
        cl = row_clues(r)
        sols = completions(5, path_edges(5), cl)
        outs.append((cl, len(sols), max((max(s) for s in sols), default=None)))
    log.note('%s P4 rows (top to bottom): %s; board levels 0..%d' % (band, outs, b['top_level']))
    log.check([o[1] > 0 for o in outs] == [False, True, False], '%s P4: first impossible, second possible, third impossible' % band)
    log.check(outs[1][2] <= b['top_level'], '%s P4: every completion of the possible set fits the board (max %d)' % (band, outs[1][2]))
P4b = completions(5, path_edges(5), {0: 3, 4: 0})
log.note('P4 second set: all %d completions %s' % (len(P4b), P4b))
log.check((3, 2, 1, 0, 0) in P4b, 'guide P4: (3,2,1,0,0) is a completion')

# ------------------------------------------------------------------ Problem 5
log.section('Problem 5: seven-site landscape')
for band in BANDS:
    b = boards(band, 5)[0]
    n, cl = b['sites'], clues_of(b)
    sols = completions(n, path_edges(n), cl)
    lo = tuple(min(s[i] for s in sols) for i in range(n))
    hi = tuple(max(s[i] for s in sols) for i in range(n))
    tot = sorted(sum(s) for s in sols)
    log.note('%s P5: clues %s -> %d completions; pointwise min %s, max %s; totals %s; board top %d; answer rows %d' % (
        band, cl, len(sols), lo, hi, tot, b['top_level'], len(rows(band, 5))))
    log.check(lo in sols and hi in sols, '%s P5: pointwise min and max are themselves landscapes' % band)
    log.check([s for s in sols if sum(s) == tot[0]] == [lo] and [s for s in sols if sum(s) == tot[-1]] == [hi],
              '%s P5: the fewest-block landscape is unique and is the pointwise min; same for most/max' % band)
    log.check(max(hi) <= b['top_level'], '%s P5: every completion fits the board' % band)
    if band == 'k-1':
        log.check(len(sols) >= 3 and 1 + len(rows(band, 5)) == 3, 'k-1 P5: three different landscapes exist; one board + two rows = three slots')
    whites = [i for i in range(n) if i not in cl]
    log.note('%s P5: white-column totals only: %d to %d' % (band, sum(lo[i] for i in whites), sum(hi[i] for i in whites)))
g = para('Problem 5, all bands.', 'Key for the K-1 finish')
P5 = completions(7, path_edges(7), {0: 1, 4: 3, 6: 1})
ex = tuples_in(g)
log.check(ex[:2] == [(1, 0, 1, 2, 3, 2, 1), (1, 2, 3, 4, 3, 2, 1)], 'guide P5: least/greatest landscapes as printed')
log.check('total 10' in g and 'total 16' in g and sum(ex[0]) == 10 and sum(ex[1]) == 16, 'guide P5: totals 10 and 16')
log.check(ex[2] in P5 and ex[2] not in ex[:2], 'guide P5: third K-1 answer %s is legal and different' % (ex[2],))
log.check('exactly 10 completions' in g and len(P5) == 10, 'guide P5: exactly 10 completions')

# ------------------------------------------------------------------ K-1 Problem 6
log.section('K-1 Problem 6: fewest one-level moves')
b = boards('k-1', 6)[0]
r0, r1 = rows('k-1', 6)
start = tuple(int(v) for v in r0['values'])
target = tuple(int(v) for v in r1['values'])
fixed = {i for i, f in enumerate(r0['locked']) if f}
log.check(legal(start, path_edges(5)) and legal(target, path_edges(5)), 'K-1 P6: start %s and finish %s are legal' % (start, target))
log.check(clues_of(b) == {0: start[0], 4: start[4]} and fixed == {0, 4}, 'K-1 P6: board clues match the shaded ends of both rows')
for cap in (b['top_level'], 10):
    d, path = shortest_moves(start, target, 5, path_edges(5), fixed, cap)
    log.check(d == 5, 'K-1 P6: BFS shortest = %d moves with heights capped at %d (one route: %s)' % (d, cap, path))
# count all shortest routes
from functools import lru_cache  # noqa: E402


def count_routes(s, t, steps):
    @lru_cache(None)
    def f(v, k):
        if k == 0:
            return 1 if v == t else 0
        tot = 0
        for i in range(5):
            if i in fixed:
                continue
            for dl in (-1, 1):
                w = list(v)
                w[i] += dl
                w = tuple(w)
                if legal(w, path_edges(5)):
                    tot += f(w, k - 1)
        return tot
    return f(s, steps)


log.note('K-1 P6: number of different 5-move routes = %d' % count_routes(start, target, 5))
g = para('Problem 6. The minimum', 'Problem 7. Replace')
route = tuples_in(g)
ok = route[0] == start and route[-1] == target and len(route) == 6 and all(legal(v, path_edges(5)) for v in route) and \
    all(sum(abs(x - y) for x, y in zip(a, c)) == 1 and a[0] == c[0] and a[4] == c[4] for a, c in zip(route, route[1:]))
log.check(ok, 'guide K-1 P6: printed 5-move route is legal step by step')
# a tempting first move that breaks the rule
log.check(not legal((1, 2, 0, 2, 1), path_edges(5)), 'K-1 P6: lowering the middle first is illegal (2,0,2) - order matters')

# ------------------------------------------------------------------ K-1 Problem 7
log.section('K-1 Problem 7: two new clues (board of Problem 6, levels 0..%d)' % b['top_level'])
top = b['top_level']


def two_clue_survey(n, top_level, cap_unbounded):
    cons = force_unb = force_cap = 0
    forcing_unb, forcing_cap = [], []
    for (c, d) in combinations(range(n), 2):
        for a, bb in product(range(top_level + 1), repeat=2):
            cl = {c: a, d: bb}
            s_unb = completions(n, path_edges(n), cl, cap=cap_unbounded)
            if s_unb:
                cons += 1
            if len(s_unb) == 1:
                force_unb += 1
                forcing_unb.append(cl)
            s_cap = completions(n, path_edges(n), cl, cap=top_level)
            if len(s_cap) == 1:
                force_cap += 1
                forcing_cap.append(cl)
    return cons, forcing_unb, forcing_cap


cons, fu, fc = two_clue_survey(5, top, 12)
log.note('K-1 P7 on the P6 board: %d consistent two-clue puzzles with clue heights 0..%d; forcing (no ceiling) %s; forcing if the drawn top is a ceiling %s' % (cons, top, fu, fc))
log.check(len(fu) == 0, 'K-1 P7: no two-clue puzzle drawable on the P6 board (levels 0..3) has a unique answer')
g = para('Problem 7. Replace', 'Key for the older finishes')
log.check(completions(5, path_edges(5), {0: 0, 4: 4}) == [(0, 1, 2, 3, 4)], 'guide K-1 P7: h(0)=0, h(4)=4 forces (0,1,2,3,4)')
log.check(4 <= top, 'guide K-1 P7: its forcing example (height 4) can be placed on the P6 board the child is using (top level %d)' % top)
log.check(len(completions(5, path_edges(5), {0: 1, 4: 1})) > 1, 'guide K-1 P7: h(0)=h(4)=1 allows many answers')

# ------------------------------------------------------------------ Grades 2-3 Problem 6
log.section('Grades 2-3 Problem 6: two clues that force one landscape (seven-site board)')
b = boards('grades-2-3', 6)[0]
cons, fu, fc = two_clue_survey(b['sites'], b['top_level'], 14)
log.note('2-3 P6: %d sites, levels 0..%d; %d consistent two-clue sets; forcing (no ceiling): %s; forcing if the top is a ceiling: %s' % (
    b['sites'], b['top_level'], cons, fu, fc))
log.check(len(fu) >= 1, '2-3 P6: a forcing pair exists on the board')
log.check(sorted(sorted(x.items()) for x in fu) == [[(0, 0), (6, 6)], [(0, 6), (6, 0)]], '2-3 P6: the only forcing pairs on the board are the full ramps h(0)=0,h(6)=6 and h(0)=6,h(6)=0')
# a natural near-miss: steep pair not at the ends
near = completions(7, path_edges(7), {1: 0, 5: 4})
log.note('2-3 P6 near-miss h(1)=0, h(5)=4: %d completions (sites 0 and 6 stay free)' % len(near))
g = para('Grades 2-3 Problem 6.', 'Grades 2-3 Problem 7.')
log.check(completions(7, path_edges(7), {0: 0, 6: 6}) == [(0, 1, 2, 3, 4, 5, 6)], 'guide 2-3 P6: h(0)=0,h(6)=6 force the ramp')
z = completions(7, path_edges(7), {0: 0, 6: 0})
log.check((0,) * 7 in z and (0, 1, 0, 0, 0, 0, 0) in z, 'guide 2-3 P6: all-zero and (0,1,0,0,0,0,0) both complete h(0)=h(6)=0')

# ------------------------------------------------------------------ Grades 2-3 Problem 7
log.section('Grades 2-3 Problem 7: two clues d steps apart')
ok = True
for d in range(0, 7):
    for a in range(0, 7):
        poss = [h for h in range(0, a + d + 5) if completions(d + 1, path_edges(d + 1), {0: a, d: h} if d else {0: a}, cap=a + d + 5)
                and (d > 0 or h == a)]
        if poss != list(range(max(0, a - d), a + d + 1)):
            ok = False
log.check(ok, '2-3 P7: for all d<=6, a<=6 the possible heights are max(0,a-d)..a+d')
d4 = [h for h in range(12) if completions(5, path_edges(5), {0: 1, 4: h}, cap=15)]
log.check(d4 == [0, 1, 2, 3, 4, 5], '2-3 P7: 4 steps from height 1 -> heights %s' % d4)
g = para('Grades 2-3 Problem 7.', 'Grades 4-5 Problem 6.')
log.check('0,1,2,3,4,5' in g, 'guide 2-3 P7: lists 0,1,2,3,4,5')

# ------------------------------------------------------------------ Grades 4-5 Problem 6
log.section('Grades 4-5 Problem 6: one clue, allowed heights per site')
b = boards('grades-4-5', 6)[0]
n, cl = b['sites'], clues_of(b)
sols = completions(n, path_edges(n), cl)
allowed = {i: sorted({s[i] for s in sols}) for i in range(n)}
log.note('4-5 P6: clue %s; allowed per site %s; shaded on the page %s' % (cl, allowed, b['shaded']))
log.check(all(allowed[int(k)] == v for k, v in b['shaded'].items()) and sorted(int(k) for k in b['shaded']) == [1, 2, 4, 5],
          '4-5 P6: the shaded marks at sites 1,2,4,5 are exactly the allowed heights')
log.check(allowed[0] == allowed[6] == [0, 1, 2, 3, 4, 5], '4-5 P6: sites 0 and 6 allow 0..5')
log.check(max(allowed[0]) <= b['top_level'], '4-5 P6: every allowed height fits the board (top %d)' % b['top_level'])
g = para('Grades 4-5 Problem 6.', 'Grades 4-5 Problem 7.')
log.check('0 through 5' in g, 'guide 4-5 P6: "0 through 5"')

# ------------------------------------------------------------------ Grades 4-5 Problem 7 and the overview theorem
log.section('Grades 4-5 Problem 7 and the guide overview: exhaustive small rows')
viol = []
checked = 0
for n in range(1, 7):
    for k in range(1, n + 1):
        for sites in combinations(range(n), k):
            for hs in product(range(5), repeat=k):
                cl = dict(zip(sites, hs))
                checked += 1
                pair_ok = all(abs(cl[c] - cl[d]) <= abs(c - d) for c, d in combinations(sites, 2))
                sols = completions(n, path_edges(n), cl, cap=4 + n)
                if pair_ok != bool(sols):
                    viol.append(('feasibility', n, cl))
                if sols:
                    L, U = envelope(n, cl)
                    if L not in sols or U not in sols:
                        viol.append(('envelope not legal', n, cl))
                    if any(any(not (L[i] <= s[i] <= U[i]) for i in range(n)) for s in sols):
                        viol.append(('outside envelope', n, cl))
                    if min(map(sum, sols)) != sum(L) or max(map(sum, sols)) != sum(U):
                        viol.append(('totals', n, cl))
log.check(not viol, 'overview + 4-5 P7: on every row of 1..6 sites with every clue set (heights 0..4), %d cases: completion exists <=> pairwise |a_c-a_d|<=|c-d|; L and U are completions; every completion lies between; L,U minimise/maximise the total %s' % (checked, viol[:3]))
# the envelope formulas without the pairwise hypothesis (P4's first, impossible clue set)
L4, U4 = envelope(5, {0: 0, 2: 3})
log.note('overview hypothesis: for the impossible P4 set h(0)=0, h(2)=3 the formulas give L=%s (h(0)=%d, not 0) and U=%s (h(2)=%d, not 3)' % (L4, L4[0], U4, U4[2]))
log.check(L4[0] != 0 and U4[2] != 3, 'overview: "Both envelopes are themselves legal" needs the pairwise condition (fails for P4 set 1)')
# no clues: least completion all zeros, no greatest
log.check(legal((0,) * 5, path_edges(5)) and legal((7,) * 5, path_edges(5)), 'overview: with no clues every constant row is legal, so there is no greatest completion')

# ------------------------------------------------------------------ guide's printed dimensions
log.section('Guide preparation claims vs printed boards')
main = [(band, b['problem'], sorted(set(round(x, 1) for x in b['dx_mm'])), sorted(set(round(x, 1) for x in b['dy_mm'])))
        for band in BANDS for p in G[band]['pages'] for b in p['boards'] if b['problem'] is not None]
log.note('board pitches (site mm, level mm): %s' % main)
log.check(all(dy == [20.0] for _, _, _, dy in main), 'guide: every task board has 20 mm level spacing')
log.check(all(dx == [22.0] for _, pr, dx, _ in main if pr != 4) and all(dx == [25.0] for _, pr, dx, _ in main if pr == 4),
          'guide: 22 mm site spacing except the P4 five-site board at 25 mm')

# ------------------------------------------------------------------ page wording that the enumeration depends on
log.section('Page wording used above')
for band, page, phrase in [('k-1', 2, 'Move the right clue to 4'), ('grades-2-3', 2, 'forces every marker'),
                           ('grades-2-3', 4, 'fewest blocks'), ('grades-4-5', 4, 'as low as possible at every site'),
                           ('grades-2-3', 5, 'force exactly one whole landscape'), ('grades-2-3', 5, 'Two clues are 4 steps apart. One is height 1.'),
                           ('grades-4-5', 5, 'Find the allowed heights at sites 0 and 6.'), ('k-1', 5, 'Replace the old clues with two new clues')]:
    log.check(phrase in text_of(band, page), '%s p%d prints "%s"' % (band, page, phrase))

log.dump(os.path.join(HERE, 'check_base.out'))
