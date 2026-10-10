"""Independent check of every Week 27 student problem (K-1, Grades 2-3,
Grades 4-5), using the profiles and drawn pairings read from the delivered
PDFs by extract.py.  Output: check_students.out
"""
import json
import os
import random
import subprocess
import sys
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, Log, blockers, stable_perfect, perfect_matchings, mname,  # noqa: E402
                    da_all_schedules, da_outcomes, all_profiles, prefers, rank)

L = Log()
if not os.path.exists(os.path.join(HERE, 'extracted.json')):
    subprocess.run([sys.executable, os.path.join(HERE, 'extract.py')], check=True)
X = json.load(open(os.path.join(HERE, 'extracted.json')))


def prof(case):
    return (case['L'], case['R'])


def board_m(bd):
    return {e[0]: e[1] for e in bd['solid']}


def stable_names(P):
    return [mname(M) for M in stable_perfect(P)]


def audit(P, tag):
    L.out(f'  {tag}: circles {P[0]} squares {P[1]}')
    for M in perfect_matchings(sorted(P[0]), sorted(P[1])):
        b = blockers(P, M)
        L.out(f'    {mname(M):18s} {"stable" if not b else "blockers " + ", ".join(b)}')


def page(band, n):
    return [p for p in X[band] if p['problem'] == n][0]


def example_page(band):
    p = X[band][0]
    L.out(f'=== {band} page 1 example')
    c = p['cases'][0]
    for bd in p['boards_above_strips']:
        L.check(sorted(bd['solid']) == ['PV', 'QU'] and bd['dashed'] == ['PU'],
                f'current pairs drawn P-V, Q-U with dashed P-U: {bd["solid"]} {bd["dashed"]}')
    # The two panels share the P strip; the U strips differ.  Read both panels from the PDF rows.
    import pdfplumber
    from common import WEEK
    fn = {'k-1': 'week-27-k-1.pdf', 'grades-2-3': 'week-27-grades-2-3.pdf'}[band]
    pg = pdfplumber.open(os.path.join(WEEK, fn)).pages[0]
    sys.path.insert(0, HERE)
    from extract import read_page
    info = read_page(pg)
    # read_page merges both panels into one case; re-read rows by x half
    from extract import shapes_on
    S = shapes_on(pg)
    for half, (x0, x1) in (('left', (0, 300)), ('right', (300, 620))):
        rows = {}
        for s in S:
            if x0 <= s['x'] < x1 and 380 < s['y'] < 500:
                rows.setdefault(round(s['y']), []).append(s)
        strips = {}
        shaded = {}
        for y, ss in rows.items():
            ss.sort(key=lambda s: s['x'])
            strips[ss[0]['label']] = [s['label'] for s in ss[1:]]
            shaded[ss[0]['label']] = [s['label'] for s in ss[1:] if s['shaded']]
        pU = prefers(strips['P'], 'U', 'V')
        uP = prefers(strips['U'], 'P', 'Q')
        L.out(f'  {half}: P strip {strips["P"]} (shaded {shaded["P"]}), U strip {strips["U"]} (shaded {shaded["U"]})')
        L.check(shaded['P'] == ['V'] and shaded['U'] == ['Q'], 'shaded choices are the current partners V and Q')
        printed = {'left': (True, True), 'right': (True, False)}[half]
        L.check((pU, uP) == printed, f'P prefers U to V: {pU}; U prefers P to Q: {uP} (page says {printed})')
    _ = info, c


# ---------------------------------------------------- strip conventions, every page
L.out('=== strip conventions on every student page')
for band, fn in (('k-1', 'week-27-k-1.pdf'), ('grades-2-3', 'week-27-grades-2-3.pdf'), ('grades-4-5', 'week-27-grades-4-5.pdf')):
    bad = []
    nrows = 0
    for p in X[band]:
        for c in p['cases']:
            pairs = ((c['L'], c['R']), (c['R'], c['L']))
            if p['problem'] is None:      # page-1 example shows only the P and U strips
                pairs = ((c['L'], {'U': 0, 'V': 0}), (c['R'], {'P': 0, 'Q': 0}))
            for side, other in pairs:
                for who, ch in side.items():
                    nrows += 1
                    filled = [x for x in ch if x]
                    if len(ch) != len(other) or len(set(filled)) != len(filled) or not set(filled) <= set(other):
                        bad.append((p['page'], who, ch))
    L.check(not bad, f'{band}: {nrows} strip rows; each lists only opposite-side letters, once each, one slot per opposite letter {bad}')

# ======================================================================= K-1
L.out('############ K-1')
example_page('k-1')

L.out('=== K-1 Problem 1: circle every pairing that can stay')
for i, c in enumerate(page('k-1', 1)['cases']):
    P = prof(c)
    audit(P, f'case {i+1}')
    st = [mname(board_m(bd)) for bd in c['boards'] if not blockers(P, board_m(bd))]
    L.out(f'  case {i+1}: boards that can stay: {st}')

L.out('=== K-1 Problem 2: draw every pairing that can stay')
for i, c in enumerate(page('k-1', 2)['cases']):
    P = prof(c)
    audit(P, f'case {i+1}')
    s = stable_names(P)
    L.check(len(s) <= len(c['boards']), f'case {i+1}: {len(s)} stable {s}; {len(c["boards"])} blank boards')

L.out('=== K-1 Problem 3: reverse one strip so the drawn pairing stays')
for i, c in enumerate(page('k-1', 3)['cases']):
    P = prof(c)
    M = board_m(c['boards'][0])
    L.out(f'  case {i+1}: drawn {mname(M)}; blockers before: {blockers(P, M)}')
    works = []
    for side in (0, 1):
        for who in P[side]:
            Q = ({k: list(v) for k, v in P[0].items()}, {k: list(v) for k, v in P[1].items()})
            Q[side][who] = Q[side][who][::-1]
            b = blockers(Q, M)
            L.out(f'    reverse {who}: {"stable" if not b else "blockers " + ", ".join(b)}')
            if not b:
                works.append(who)
    L.out(f'  case {i+1}: strips that work alone: {works or "none (cross out)"}')

L.out('=== K-1 Problem 4: fill the empty strip so both drawn pairings stay')
for i, c in enumerate(page('k-1', 4)['cases']):
    P = prof(c)
    blank = [k for side in (0, 1) for k, v in P[side].items() if '' in v]
    L.check(blank == ['Y'], f'case {i+1}: blank strip {blank}')
    ok = []
    for order in (['A', 'B'], ['B', 'A']):
        Q = (P[0], {**P[1], 'Y': order})
        ms = [board_m(bd) for bd in c['boards']]
        res = [blockers(Q, m) for m in ms]
        L.out(f'    Y: {order}: ' + '; '.join(f'{mname(m)} -> {r or "stable"}' for m, r in zip(ms, res)))
        if not any(res):
            ok.append(''.join(order))
    L.out(f'  case {i+1}: fills that work: {ok or "none (cross out)"}')

L.out('=== K-1 Problems 5 and 6: all 16 two-pair profiles')
only_straight, both = [], []
for P in all_profiles('AB', 'XY'):
    s = stable_names(P)
    key = ' '.join(''.join(P[0][a]) for a in 'AB') + ' ' + ' '.join(''.join(P[1][x]) for x in 'XY')
    if s == ['AX / BY']:
        only_straight.append(key)
    if len(s) == 2:
        both.append(key)
    L.check(len(s) >= 1, f'{key}: stable {s}')
L.out(f'  only AX/BY stable: {len(only_straight)} profiles: {only_straight}')
L.out(f'  both pairings stable: {len(both)} profiles: {both}')
for n in (5, 6):
    pg = page('k-1', n)
    for c in pg['cases']:
        L.check(sorted(sorted(bd['solid']) for bd in c['boards']) == [['AX', 'BY'], ['AY', 'BX']],
                f'P{n}: drawn pairings straight (left) and crossed (right): {[bd["solid"] for bd in c["boards"]]}')
L.check(len(only_straight) >= 2, 'P5: at least two different sets of strips exist')
L.check(len(both) == len(page('k-1', 6)['cases']), f'P6: {len(both)} ways, {len(page("k-1", 6)["cases"])} printed cases')

# ================================================================ Grades 2-3
L.out('############ Grades 2-3')
example_page('grades-2-3')
L.out('=== 2-3 Problem 1')
for i, c in enumerate(page('grades-2-3', 1)['cases']):
    P = prof(c)
    for bd in c['boards']:
        m = board_m(bd)
        b = blockers(P, m)
        L.out(f'  case {i+1}: {mname(m)}: {"stable (circle it)" if not b else "join " + " or ".join(b)}')
for n, boards in ((2, 6), (3, 6), (4, 4)):
    c = page('grades-2-3', n)['cases'][0]
    P = prof(c)
    L.out(f'=== 2-3 Problem {n}')
    audit(P, 'all candidates')
    s = stable_names(P)
    L.check(len(c['boards']) == boards and len(s) <= len(c['boards']),
            f'{len(s)} stable {s}; {len(c["boards"])} blank boards')
    if n == 4:
        allfirst = [mname(M) for M in perfect_matchings('ABCD', 'WXYZ')
                    if all(P[0][a][0] == M[a] for a in M) and all(P[1][s_][0] == a for a, s_ in M.items())]
        L.out(f'  matchings giving all eight letters their first choice: {allfirst or "none"}')

L.out('=== 2-3 Problem 5: complete 3x3 lists with exactly two stable pairings')
counts = {}
example = None
for P in all_profiles('ABC', 'XYZ'):
    k = len(stable_perfect(P))
    counts[k] = counts.get(k, 0) + 1
    if k == 2 and example is None:
        example = P
L.out(f'  number of stable pairings over all 46,656 profiles: {dict(sorted(counts.items()))}')
L.check(counts.get(2, 0) > 0, f'exactly two is possible, e.g. {example}')
L.check(len(page('grades-2-3', 5)['cases'][0]['boards']) == 2, 'two blank boards for the two pairings')

# ================================================================ Grades 4-5
L.out('############ Grades 4-5')
L.out('=== 4-5 Problem 1')
pg = page('grades-4-5', 1)
for i, c in enumerate(pg['cases']):
    P = prof(c)
    s = stable_names(P)
    L.check(len(s) <= len(c['boards']), f'case {i+1}: {len(s)} stable {s}; {len(c["boards"])} blank boards')

L.out('=== 4-5 Problem 2: asking rules from both sides, every schedule')
c = page('grades-4-5', 2)['cases'][0]
P = prof(c)
audit(P, 'all 24 candidates')
for side, nm in (('L', 'A, B, C, D ask'), ('R', 'W, X, Y, Z ask')):
    out, logs = da_all_schedules(P, side)
    L.out(f'  {nm}: outcomes {{matching: request counts}} = {dict((k, sorted(v)) for k, v in out.items())}')
    for k, lg in logs.items():
        L.out('    one run: ' + '; '.join(f'{a}->{r} keeps {kp}' + (f' frees {fr}' if fr else '') for a, r, kp, fr in lg))
    for k in out:
        M = {p[0]: p[1] for p in k.split(' / ')}
        L.check(not blockers(P, M), f'{nm}: result {k} is stable')

L.out('=== 4-5 Problem 3: changed rule (keep the first asker)')
bad_profiles = 0
total = 0
term_ok = True
for P in all_profiles('ABC', 'XYZ'):
    total += 1
    try:
        out = da_outcomes(P, 'L', keep_first=True)
    except RuntimeError:
        term_ok = False
        continue
    if any(blockers(P, {p[0]: p[1] for p in k.split(' / ')}) for k in out):
        bad_profiles += 1
L.check(term_ok, 'changed rule always ends with every asker held (all 46,656 profiles, every order)')
L.out(f'  profiles where some asking order ends unstable: {bad_profiles} of {total}')

L.out('=== 4-5 Problem 4: request bounds')
# requests made by the asking rules = sum over askers of the rank of the final partner (schedule independent)


def requests(P):
    out = da_outcomes(P, 'L')
    vals = set().union(*out.values())
    assert len(vals) == 1
    return vals.pop()


rng = random.Random(27)
best = 0
bestP = None
for trial in range(400):
    P = ({a: rng.sample('WXYZ', 4) for a in 'ABCD'}, {s: rng.sample('ABCD', 4) for s in 'WXYZ'})
    r = requests(P)
    for step in range(150):          # simple hill climb
        Q = ({k: list(v) for k, v in P[0].items()}, {k: list(v) for k, v in P[1].items()})
        side = rng.randrange(2)
        who = rng.choice(list(Q[side]))
        i, j = rng.sample(range(4), 2)
        Q[side][who][i], Q[side][who][j] = Q[side][who][j], Q[side][who][i]
        rq = requests(Q)
        if rq >= r:
            P, r = Q, rq
    if r > best:
        best, bestP = r, P
L.out(f'  largest request count found by search (n=4): {best}; example {bestP}')
L.check(best <= 13, 'never above n^2 - n + 1 = 13; the printed n^2 = 16 is a valid but loose bound')

L.out('=== 4-5 Problems 5 and 6, and the 3x3 census')
stable_total = 0
maxlast = 0
witness = None
da_ok = True
for P in all_profiles('ABC', 'XYZ'):
    st = stable_perfect(P)
    stable_total += len(st)
    for M in st:
        last = sum(P[0][a][-1] == M[a] for a in M) + sum(P[1][s][-1] == a for a, s in M.items())
        if last > maxlast:
            maxlast, witness = last, (P, mname(M))
    for side in ('L', 'R'):
        out = da_outcomes(P, side)
        if len(out) != 1 or any(blockers(P, {p[0]: p[1] for p in k.split(' / ')}) for k in out):
            da_ok = False
L.check(da_ok, 'P5: asking rules give one stable result, whatever the order, on all 46,656 profiles from both sides')
L.out(f'  stable matchings summed over all 46,656 profiles: {stable_total}')
L.out(f'  P6: largest number of last-choice letters in a stable pairing: {maxlast}; e.g. {witness}')

L.save(os.path.join(HERE, 'check_students.out'))
