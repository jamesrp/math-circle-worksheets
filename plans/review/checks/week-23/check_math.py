"""Independent mathematical check of Week 23 (sorting networks).

Every machine is taken from networks.json, i.e. read back out of the delivered PDFs by
extract_networks.py (run that first).  All answers are recomputed by brute force here;
the guide's stated answers are transcribed as CLAIMS and compared with the computation.
Output: out_check_math.txt
"""
import os, json, sys
from itertools import permutations, product, combinations
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
NET = json.load(open(os.path.join(HERE, 'networks.json')))
OUT = []
FAIL = []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def machines(band, page):
    return [tuple(tuple(p) for p in n['pairs_in_order']) for n in NET[band][page - 1]['networks']]


# ---------------------------------------------------------------- simulator
def run(v, net):
    v = list(v)
    for a, b in net:
        if v[a - 1] > v[b - 1]:
            v[a - 1], v[b - 1] = v[b - 1], v[a - 1]
    return tuple(v)


def run_rec(v, net):
    v = list(v); rec = ''
    for a, b in net:
        s = v[a - 1] > v[b - 1]
        rec += 'S' if s else 'N'
        if s:
            v[a - 1], v[b - 1] = v[b - 1], v[a - 1]
    return tuple(v), rec


def ok(v, net):
    return run(v, net) == tuple(sorted(v))


def perms(n):
    return list(permutations(range(1, n + 1)))


def binary(n):
    return list(product([0, 1], repeat=n))


def sorter(net, n):
    return all(ok(p, net) for p in perms(n))


def s(t):
    return ''.join(str(x) for x in t)


def tup(st):
    return tuple(int(c) for c in st)


def pairs(n):
    return list(combinations(range(1, n + 1), 2))


def adj(n):
    return [(i, i + 1) for i in range(1, n)]


def min_sorter(n, allowed, maxlen):
    for k in range(maxlen + 1):
        found = [net for net in product(allowed, repeat=k) if sorter(net, n)]
        if found:
            return k, found
    return None, []


T = ((1, 2), (2, 3)); R = ((2, 3), (1, 2)); Q = ((1, 3), (1, 2), (2, 3)); S3 = ((1, 2), (2, 3), (1, 2))
S4 = ((1, 2), (3, 4), (1, 3), (2, 4), (2, 3)); N4 = ((1, 2), (2, 3), (3, 4), (1, 2), (2, 3), (1, 2))

# ---------------------------------------------------------------- general facts
say('=== General facts used throughout')
k3, sorters3 = min_sorter(3, pairs(3), 4)
check(k3 == 3, f'3-lane minimum is {k3}; all {len(sorters3)} three-bar sorters: {sorters3}')
k4, sorters4 = min_sorter(4, pairs(4), 5)
check(k4 == 5, f'4-lane minimum is {k4} (all 6^4 = 1296 four-bar lists fail); {len(sorters4)} five-bar sorters')
ka, adjs = min_sorter(4, adj(4), 6)
check(ka == 6, f'4-lane neighbour-only minimum is {ka} (all 3^5 = 243 five-bar lists fail); {len(adjs)} six-bar sorters')
check(N4 in adjs and S4 in sorters4 and S3 in sorters3 and Q in sorters3, 'guide machines S3, Q, S4, N4 are sorters')
# zero-one principle, exhaustively, for every 3- and 4-lane list up to the lengths below,
# against every input over {1..n} with repeats (n^n inputs, includes all permutations)
for n, L in [(3, 4), (4, 5)]:
    bad = 0; cnt = 0
    allin = list(product(range(1, n + 1), repeat=n))
    for k in range(L + 1):
        for net in product(pairs(n), repeat=k):
            cnt += 1
            b = all(ok(v, net) for v in binary(n))
            a = all(ok(v, net) for v in allin)
            bad += (a != b)
    check(bad == 0, f'zero-one principle: for all {cnt} lists of <= {L} bars on {n} lanes, '
          f'"sorts all {2**n} binary" <=> "sorts all {n**n} inputs with repeats"')
# record injectivity: per network, at most one distinct-value start finishes sorted per record
for n, L in [(3, 4), (4, 5)]:
    viol = 0; maxrec = 0
    for k in range(L + 1):
        for net in product(pairs(n), repeat=k):
            g = defaultdict(int); recs = set()
            for p in perms(n):
                o, r = run_rec(p, net); recs.add(r)
                if o == tuple(sorted(p)):
                    g[r] += 1
            viol += any(c > 1 for c in g.values())
            maxrec = max(maxrec, len(recs) - 2 ** k)
    check(viol == 0 and maxrec <= 0, f'{n} lanes, <= {L} bars: no record is shared by two sorted distinct starts; '
          f'records never exceed 2^k')

# ================================================================ K-1
say('\n=== K-1')
m = machines('k-1', 1)
check(m == [T], f'P1 machine read from PDF {m}')
fc = NET['k-1'][0]['free_cards']
cols = []
for grp in (fc[0:3], fc[3:6]):
    for j in range(3):
        cols.append(''.join(r['values'][j][0] for r in grp))
say('P1 pictured starts (top->bottom lane), row by row:', cols)
check(cols == ['123', '132', '213', '231', '312', '321'], 'P1 pictures are the six orders in the guide\'s order')
res = {c: s(run(tup(c), T)) for c in cols}
say('P1 outcomes under T:', res)
check([c for c in cols if res[c] == '123'] == ['123', '132', '213', '312'], 'P1 circled: 123 132 213 312; 231,321 -> 213')
claim_tbl = {'123': ('123', '123'), '132': ('123', '123'), '213': ('123', '123'), '231': ('213', '123'),
             '312': ('123', '123'), '321': ('213', '123')}
check(all((s(run(tup(c), T)), s(run(tup(c), S3))) == v for c, v in claim_tbl.items()), 'guide p4 table (After T / After S3)')
say('P2: minimum 3 (see general facts)')
up, lo = machines('k-1', 3)
check(up == S3 and lo == ((1, 2), (1, 2), (2, 3)), f'P3 machines read {up} / {lo}')
fu = [s(p) for p in perms(3) if not ok(p, up)]; fl = [(s(p), s(run(p, lo))) for p in perms(3) if not ok(p, lo)]
check(fu == [] and fl == [('231', '213'), ('321', '213')], f'P3 failures: upper {fu}; lower {fl}')
# P4
left = sorted(set(permutations((0, 0, 1)))); right = sorted(set(permutations((0, 1, 1))))
fc = NET['k-1'][3]['free_cards'][0]['values']
check(fc == ['0dots', '0dots', '1dots', '0dots', '1dots', '1dots'], f'P4 card sets read {fc}')
for name, A, B in [('left-not-right', left, right), ('right-not-left', right, left)]:
    for k in range(4):
        sols = [net for net in product(pairs(3), repeat=k)
                if all(ok(v, net) for v in A) and not all(ok(v, net) for v in B)]
        if sols:
            say(f'P4 {name}: shortest {k} bars; all such: {sols}')
            break
check(all(ok(v, T) for v in left) and [s(v) for v in right if not ok(v, T)] == ['110'] and s(run((1, 1, 0), T)) == '101',
      'guide P4: T sorts 001 set, fails only 110 -> 101')
check(all(ok(v, R) for v in right) and [s(v) for v in left if not ok(v, R)] == ['100'] and s(run((1, 0, 0), R)) == '010',
      'guide P4: R sorts 011 set, fails only 100 -> 010')
# P5
ms = machines('k-1', 5)
check(ms == [T, R, ((1, 3), (1, 2))], f'P5 machines read {ms}')
for mm, want in zip(ms, [(1, 2), (2, 3), (2, 3)]):
    good = [b for b in pairs(3) if sorter(mm + (b,), 3)]
    check(not sorter(mm, 3) and good == [want], f'P5 {mm}: fails as printed; working last bars {good} (guide: {want}, unique)')
say('P6: minimum 5 (see general facts)')

# ================================================================ Grades 2-3
say('\n=== Grades 2-3')
ms = machines('grades-2-3', 1)
check(ms == [T, R, Q], f'P1 machines read {ms}')
for mm in ms:
    say(f'  {mm}: sorts {[s(p) for p in perms(3) if ok(p, mm)]}; fails {[(s(p), s(run(p, mm))) for p in perms(3) if not ok(p, mm)]}')
check([s(p) for p in perms(3) if ok(p, R)] == ['123', '132', '213', '231'] and
      {s(run(p, R)) for p in perms(3) if not ok(p, R)} == {'132'}, 'guide P1: R sorts 123,132,213,231; 312,321 -> 132')
# P2 nine-row table
tbl = [((1, 2), (1, 2), '132', '132'), ((1, 2), (1, 3), '132', '132'), ((1, 2), (2, 3), '231', '213'),
       ((1, 3), (1, 2), '132', '132'), ((1, 3), (1, 3), '132', '132'), ((1, 3), (2, 3), '213', '213'),
       ((2, 3), (1, 2), '312', '132'), ((2, 3), (1, 3), '213', '213'), ((2, 3), (2, 3), '213', '213')]
check(len({(a, b) for a, b, _, _ in tbl}) == 9 and all(s(run(tup(st), (a, b))) == fin and fin != '123' for a, b, st, fin in tbl),
      'guide P2 table: nine distinct lists, each stated start fails with the stated final order')
# P3
ms = machines('grades-2-3', 3)
check(ms == [((1, 2), (3, 4), (1, 3), (2, 4)), ((1, 3), (2, 4), (1, 2), (3, 4)), ((1, 2), (3, 4), (1, 4), (2, 3))],
      f'P3 machines read {ms}')
for mm in ms:
    good = [b for b in pairs(4) if sorter(mm + (b,), 4)]
    say(f'  P3 {mm}: sorts as printed? {sorter(mm, 4)}; working last bars {good}')
check([[b for b in pairs(4) if sorter(mm + (b,), 4)] for mm in ms] == [[(2, 3)], [(2, 3)], []], 'P3: (2,3), (2,3), impossible')
check(s(run((2, 4, 1, 3), ms[2])) == '2143', 'guide P3 witness 2413 -> 2143 on the bottom machine')
# can the bottom machine be repaired by any two bars? (context for "explain why")
two = [bb for bb in product(pairs(4), repeat=2) if sorter(ms[2] + bb, 4)]
say(f'  P3 bottom: two-bar repairs exist: {two[:4]}... ({len(two)})')
# P4
W = machines('grades-2-3', 4)[0]
check(W == ((1, 2), (1, 3), (2, 3), (2, 4)), f'P4 machine read {W}')
check(NET['grades-2-3'][3]['free_cards'][0]['values'] == ['0', '0', '1', '1'], 'P4 cards 0 0 1 1')
w2 = sorted(set(permutations((0, 0, 1, 1))))
check(len(w2) == 6 and all(ok(v, W) for v in w2), 'P4: all 6 arrangements of 0011 sort')
fails = [(s(v), s(run(v, W))) for v in binary(4) if not ok(v, W)]
say('P4: binary failures of W (start, finish):', fails)
check(fails == [('0010', '0010'), ('0100', '0010'), ('1000', '0010'), ('1110', '1011')], 'P4 failures computed')
check(s(run((1, 1, 1, 0), W)) == '1101', 'guide p7: "1110 finishes 1101"')
say('    trace 1110:', [s(run((1, 1, 1, 0), W[:i])) for i in range(5)])
# P5 audit table
audit = {'0000': '0000', '0001': '0001', '0010': '0001', '0011': '0011', '0100': '0001', '0101': '0011', '0110': '0011',
         '0111': '0111', '1000': '0001', '1001': '0011', '1010': '0011', '1011': '0111', '1100': '0011', '1101': '0111',
         '1110': '0111', '1111': '1111'}
check(len(audit) == 16 and all(s(run(tup(k), S4)) == v for k, v in audit.items()), 'guide P5 S4 16-row audit table')
check(all(ok(v, N4) for v in binary(4)), 'N4 sorts all 16 binary starts')
# P6
trace = [s(run((4, 3, 2, 1), N4[:i])) for i in range(7)]
check(trace == ['4321', '3421', '3241', '3214', '2314', '2134', '1234'], f'guide N4 trace of 4321: {trace}')

# ================================================================ Grades 4-5
say('\n=== Grades 4-5')
ms = machines('grades-4-5', 1)
check(ms == [T, Q], f'P1 machines read {ms}')
for mm in ms:
    for ms_ in [(1, 2, 3), (1, 1, 3), (1, 3, 3)]:
        arr = sorted(set(permutations(ms_)))
        say(f'  P1 {mm} on {ms_}: fails {[(s(v), s(run(v, mm))) for v in arr if not ok(v, mm)]}')
check([s(v) for v in sorted(set(permutations((1, 3, 3)))) if not ok(v, T)] == ['331'] and s(run((3, 3, 1), T)) == '313'
      and all(ok(v, T) for v in permutations((1, 1, 3))), 'guide P1: T sorts 113 set; only 331 fails (-> 313)')
# P3 thresholds over all real t: breakpoints are the values themselves
rows_claim = {(-2, 8, 5, 8): ['1111', '0111', '0101', '0000'], (6, 2, 9, 4): ['1111', '1011', '1010', '0010', '0000'],
              (4, 4, 4, 4): ['1111', '0000']}
starts = [tuple(int(x) for x in r['values']) for r in NET['grades-4-5'][2]['free_cards'][2:]]
check(starts == list(rows_claim), f'P3 starts read {starts}')
ex = NET['grades-4-5'][2]['free_cards'][:2]
check([int(x) for x in ex[1]['values']] == [0 if int(v) <= 4 else 1 for v in ex[0]['values']], 'P3 example t=4: 3 7 4 -> 0 1 0')
for st in starts:
    vals = sorted(set(st)); ts = [vals[0] - 1] + vals + [x + 0.5 for x in vals]
    rows = []
    for t in sorted(ts):
        r = s(tuple(0 if v <= t else 1 for v in st))
        if r not in rows:
            rows.append(r)
    nonneg = sorted({s(tuple(0 if v <= t else 1 for v in st)) for t in range(0, 20)})
    say(f'  P3 {st}: rows over all t {rows}; using only t = 0,1,2,... gives {len(nonneg)} rows {nonneg}')
    check(rows == rows_claim[st], f'guide P3 rows for {st}')
# commutation, exhaustively on a small range including ties and negatives
bad = [(a, b, t) for a in range(-3, 6) for b in range(-3, 6) for t in range(-4, 7)
       if (lambda f: (f(min(a, b)), f(max(a, b))) != (min(f(a), f(b)), max(f(a), f(b))))(lambda v: 0 if v <= t else 1)]
check(not bad, 'P3 second part: thresholding commutes with one comparator (all a,b in -3..5, t in -4..6)')
# P4: a binary sorter can never output 9 above 4 -- check for every 4-lane binary sorter up to 6 bars
bs = [net for k in range(7) for net in product(pairs(4), repeat=k) if all(ok(v, net) for v in binary(4))]
vals = [1, 4, 9]
viol = [net for net in bs for v in product(vals, repeat=4) if run(v, net)[1:3] == (9, 4)]
check(not viol, f'P4: none of the {len(bs)} binary sorters with <= 6 bars ever finishes 9 in lane 2 above 4 in lane 3 '
      f'(all 81 inputs over {{1,4,9}})')
# P5
up, lo = machines('grades-4-5', 5)
check(up == S4 and lo == ((1, 2), (3, 4), (1, 3), (2, 3), (2, 4)), f'P5 machines read {up} / {lo}')
check(sorter(up, 4) and all(ok(v, up) for v in product(range(1, 5), repeat=4)), 'P5 upper sorts all 256 inputs over 1..4')
bf = [(s(v), s(run(v, lo))) for v in binary(4) if not ok(v, lo)]
check(bf == [('0100', '0010'), ('1000', '0010')], f'P5 lower binary failures {bf} (guide: 0100, 1000 -> 0010, all others sort)')
say('  P5 lower distinct-value failures:', [(s(p), s(run(p, lo))) for p in perms(4) if not ok(p, lo)])
check([s(run((1, 0, 0, 0), lo[:i])) for i in range(6)] == ['1000', '0100', '0100', '0100', '0010', '0010'],
      'guide P5 trace 1000 -> 0100 -> 0100 -> 0100 -> 0010 -> 0010')
# P6
ex, m1, m2 = machines('grades-4-5', 6)
n6 = NET['grades-4-5'][5]['networks'][0]
check(ex == ((1, 2), (1, 2)) and n6['ins'] == ['3', '1'] and n6['outs'] == ['1', '3'] and
      run_rec((3, 1), ex) == ((1, 3), 'SN') and [c[2] for c in n6['mid_cards']] == ['1', '3'],
      'P6 example: 3,1 -> swap -> 1,3 -> stay; record SN')
check(m1 == T and m2 == S3, f'P6 machines read {m1} / {m2}')
claim6 = {T: {'NN': ['123'], 'NS': ['132', '231'], 'SN': ['213'], 'SS': ['312', '321']},
          S3: {'NNN': ['123'], 'NSN': ['132'], 'SNN': ['213'], 'NSS': ['231'], 'SSN': ['312'], 'SSS': ['321']}}
for mm in (m1, m2):
    g = defaultdict(list)
    for p in perms(3):
        g[run_rec(p, mm)[1]].append(s(p))
    say(f'  P6 {mm}: {dict(g)}')
    check(dict(g) == claim6[mm], f'guide P6 record table for {mm}')
# P7: see general facts (3 and 5); record bound
say('P7: minima 3 and 5; record bound 2^k (see general facts)')

# ================================================================ Guide extras
say('\n=== Guide extensions')
# depth: S4 in three stages of disjoint bars; no depth-2 sorter on 4 lanes
stages = [((1, 2), (3, 4)), ((1, 3), (2, 4)), ((2, 3),)]
check(sum(stages, ()) == S4, 'S4 = stages {(1,2),(3,4)}, {(1,3),(2,4)}, {(2,3)}')
layers = [l for k in (1, 2) for l in combinations(pairs(4), k) if len({x for b in l for x in b}) == 2 * k]
d2 = [a + b for a in layers for b in layers if sorter(a + b, 4)]
check(not d2, f'no 4-lane network of two stages sorts ({len(layers)} possible stages)')
# neighbour-only optimum for n = 5 is 10: bubble network sorts; BFS on binary output sets shows 9 bars never suffice
n = 5
bub = tuple(p for k in range(n - 1, 0, -1) for p in adj(n)[:k])
check(len(bub) == 10 and all(ok(v, bub) for v in binary(5)) and sorter(bub, 5), 'n=5 repeated-pass neighbour network: 10 bars, sorts')
start = frozenset(binary(5)); frontier = {start}; seen = {start}; depth = 0; target = None
while frontier and target is None and depth < 10:
    depth += 1; nxt = set()
    for st in frontier:
        for b in adj(5):
            ns = frozenset(run(v, (b,)) for v in st)
            if ns not in seen:
                seen.add(ns); nxt.add(ns)
                if all(v == tuple(sorted(v)) for v in ns):
                    target = depth
    frontier = nxt
check(target == 10, f'n=5 neighbour-only minimum by exhaustive search over binary output sets: {target}')

say('\nSUMMARY:', 'all checks passed' if not FAIL else f'{len(FAIL)} check(s) failed:')
for f in FAIL:
    say('  -', f)
open(os.path.join(HERE, 'out_check_math.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
