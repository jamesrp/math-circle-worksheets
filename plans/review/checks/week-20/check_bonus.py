"""Independent check of the Week 20 bonus (encore) packet and its adult guide.

Boards come from boards.json (extract_boards.py, read from the delivered PDF).
Expectations are solved exactly and also simulated; the two tick rules are
iterated with exact fractions; roughness scores are enumerated.  Guide claims
are quoted (each quote confirmed in the delivered bonus guide) and recomputed.
Output: out_check_bonus.txt
"""
import itertools
import json
import random
import re
import subprocess
from fractions import Fraction as F
from pathlib import Path

from repo import WEEK

F.__repr__ = lambda self: str(self)
HERE = Path(__file__).resolve().parent
D = json.load(open(HERE / 'boards.json'))
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def norm(t):
    t = t.replace('−', '-')
    return re.sub(r'\s+', ' ', t)


GUIDE = norm(subprocess.run(['pdftotext', str(WEEK / 'week-20-bonus-facilitator.pdf'), '-'], capture_output=True, text=True).stdout)
PAGES = norm(subprocess.run(['pdftotext', str(WEEK / 'week-20-bonus.pdf'), '-'], capture_output=True, text=True).stdout)


def quoted(q):
    ok = norm(q) in GUIDE
    if not ok:
        say('     (quote not found: ' + q[:80] + ')')
    return ok


def graph(page, k):
    pg = D['bonus'][page - 1]
    b = [b for b in pg['boards'] if len(b['nodes']) >= 2][k]
    ns = pg['nodes']
    adj = {i: [] for i in b['nodes']}
    for a, c in b['edges']:
        adj[a].append(c); adj[c].append(a)
    kind = {i: ns[i]['kind'] for i in b['nodes']}
    text = {i: ns[i]['text'] for i in b['nodes']}
    pos = {i: (ns[i]['cx'], ns[i]['cy']) for i in b['nodes']}
    return adj, kind, text, pos


def solve_expect(adj, kind, val):
    """Exact expected terminal score: harmonic extension by fixed-point elimination (small boards)."""
    circ = [i for i in adj if kind[i] == 'circle']
    n = len(circ); idx = {c: k for k, c in enumerate(circ)}
    A = [[F(0)] * (n + 1) for _ in range(n)]
    for c in circ:
        r = idx[c]; A[r][r] = F(len(adj[c]))
        for v in adj[c]:
            if v in idx:
                A[r][idx[v]] -= 1
            else:
                A[r][n] += val[v]
    for col in range(n):
        p = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[p] = A[p], A[col]
        for r in range(n):
            if r != col and A[r][col]:
                f = A[r][col] / A[col][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return {c: A[idx[c]][n] / A[idx[c]][idx[c]] for c in circ}


# ------------------------------------------------------------------ P1
say('#### Bonus P1: stopping walks')
adj, kind, text, pos = graph(1, 0)
val = {i: F(int(text[i])) for i in adj if kind[i] == 'square'}
check(sorted(text.values()) == ['0', '6', 'A', 'B'] and all(len(adj[i]) == 2 for i in adj if kind[i] == 'circle'), 'P1 upper board is the path 0 - A - B - 6')
E = solve_expect(adj, kind, val)
name = {i: text[i] for i in adj}
EA = [E[i] for i in E if name[i] == 'A'][0]; EB = [E[i] for i in E if name[i] == 'B'][0]
check((EA, EB) == (2, 4), f'P1 exact expectations A={EA}, B={EB}')
check(quoted('a=b/2 and b=(a+6)/2. Hence a=2,b=4'), 'guide p.2 first-step equations quoted')
check(quoted('the chances of stopping at 6 are 1/3 and 2/3') and (EA / 6, EB / 6) == (F(1, 3), F(2, 3)), 'guide p.2: P(stop at 6) = 1/3 from A, 2/3 from B')
adj2, kind2, text2, pos2 = graph(1, 1)
val2 = {i: F(int(text2[i])) for i in adj2 if kind2[i] == 'square'}
E2 = solve_expect(adj2, kind2, val2)
check(sorted(val2.values()) == [0, 3, 6] and list(E2.values()) == [3], f'P1 C (joined to 0,3,6) expectation {list(E2.values())}')
# simulation with the printed graphs
random.seed(2020)


def walk(start, adj, kind, val):
    x, steps = start, 0
    while kind[x] != 'square':
        x = random.choice(adj[x]); steps += 1
    return val[x], steps


for lab, (a, k, v) in {'A': (adj, kind, val), 'B': (adj, kind, val), 'C': (adj2, kind2, val2)}.items():
    s = [i for i in a if (text if a is adj else text2)[i] == lab][0]
    runs = [walk(s, a, k, v) for _ in range(200000)]
    mean = sum(r[0] for r in runs) / len(runs)
    say(f'     simulation from {lab}: mean score {float(mean):.3f} over {len(runs)} walks, longest walk {max(r[1] for r in runs)} moves')
# twelve-walk sample means vary
samples = [sum(walk([i for i in adj if text[i] == 'A'][0], adj, kind, val)[0] for _ in range(12)) / 12 for _ in range(10000)]
say(f'     twelve-walk sample means from A range {min(samples)} .. {max(samples)}; P(sample mean == 2) ~ {sum(1 for s in samples if s == 2)/len(samples):.3f}')
check(quoted('replace square scores 0,6 by 0,3: A and B expectations become 1,2'), 'guide p.2 scaling extension quoted')
v3 = {i: (F(3) if x == 6 else x) for i, x in val.items()}
E3 = solve_expect(adj, kind, v3)
check(sorted(E3.values()) == [1, 2], 'scaling extension: 0,3 squares give A=1, B=2')
check(quoted('Probability of surviving n moves is (1/2)^n'), 'guide p.2: from A or B half the choices end the walk -> survival (1/2)^n')

# ------------------------------------------------------------------ dynamics
say('#### Bonus P2-P4: whole-board ticks')


def tick(state, adj, own=False):
    new = {}
    for i in adj:
        vals = [state[j] for j in adj[i]] + ([state[i]] if own else [])
        new[i] = F(sum(vals), len(vals))
    return new


# printed example p.2: 0-3-6 -> 3,3,3
pg = D['bonus'][1]
bs = [b for b in pg['boards'] if len(b['nodes']) >= 2]
ns = pg['nodes']


def bgraph(b):
    adj = {i: [] for i in b['nodes']}
    for a, c in b['edges']:
        adj[a].append(c); adj[c].append(a)
    return adj


before, after = bs[0], bs[1]
ab = bgraph(before)
st = {i: F(int(ns[i]['text'])) for i in ab}
nx = tick(st, ab)
ex_after = [int(ns[i]['text']) for i in sorted(after['nodes'], key=lambda i: ns[i]['cx'])]
check([nx[i] for i in sorted(ab, key=lambda i: ns[i]['cx'])] == ex_after == [3, 3, 3], 'p.2 worked example: 0,3,6 -> 3,3,3 under the neighbour-only tick')

cyc = bs[2]
ac = bgraph(cyc)
check(all(len(v) == 2 for v in ac.values()) and len(ac) == 4, 'P2 board is a four-cycle')
# positions: TL, TR, BR, BL
xs = sorted({round(ns[i]['cx']) for i in ac}); ys = sorted({round(ns[i]['cy']) for i in ac})
where = {}
for i in ac:
    where[('T' if round(ns[i]['cy']) == ys[0] else 'B') + ('L' if round(ns[i]['cx']) == xs[0] else 'R')] = i
order = [where[k] for k in ('TL', 'TR', 'BR', 'BL')]
start = [F(int(ns[i]['text'])) for i in order]
check(start == [0, 6, 0, 6], f'P2 printed board (TL,TR,BR,BL) = {start}, matching the table row "0 0 6 0 6"')
check(norm('0 0 6 0 6') in PAGES, 'P2 table tick-0 row printed as 0 | 0 6 0 6')
s = dict(zip(order, start))
seq = [tuple(s[i] for i in order)]
for t in range(4):
    s = tick(s, ac)
    seq.append(tuple(s[i] for i in order))
check(seq[1] == (6, 0, 6, 0) and seq[2] == seq[0], f'P2 sequence {seq}: first return after exactly two ticks')


def first_return(st, adj, order, own=False, limit=12):
    s = dict(zip(order, st))
    for t in range(1, limit + 1):
        s = tick(s, adj, own)
        if tuple(s[i] for i in order) == tuple(st):
            return t
    return None


two = [st for st in itertools.product(range(7), repeat=4) if first_return(tuple(map(F, st)), ac, order) == 2]
alt = all(st[0] == st[2] and st[1] == st[3] and st[0] != st[1] for st in two)
check(alt and len(two) == 42, f'P2: among whole-number states 0..6, exactly {len(two)} first return after two ticks, all alternating a,b,a,b with a != b')
one = [st for st in itertools.product(range(7), repeat=4) if first_return(tuple(map(F, st)), ac, order) == 1]
check(all(len(set(x)) == 1 for x in one), f'P2: the {len(one)} states returning after one tick are the constants')
nev = sum(1 for st in itertools.product(range(7), repeat=4) if first_return(tuple(map(F, st)), ac, order) is None)
say(f'     P2: {nev} of 2401 states never return to themselves (the board still becomes periodic after one tick)')

# P3: two joined circles
b3 = [b for b in D['bonus'][2]['boards'] if len(b['nodes']) >= 2][0]
a3 = bgraph(b3)
n3 = D['bonus'][2]['nodes']
o3 = sorted(a3, key=lambda i: n3[i]['cx'])
s = {i: F(int(n3[i]['text'])) for i in a3}
old = [tuple(s[i] for i in o3)]
for _ in range(4):
    s = tick(s, a3)
    old.append(tuple(s[i] for i in o3))
s = {i: F(int(n3[i]['text'])) for i in a3}
new = [tuple(s[i] for i in o3)]
for _ in range(4):
    s = tick(s, a3, own=True)
    new.append(tuple(s[i] for i in o3))
check(old[:3] == [(0, 6), (6, 0), (0, 6)] and len(set(old)) == 2, f'P3 neighbour-only: {old} (swaps forever, never settles)')
check(new[1:] == [(3, 3)] * 4, f'P3 own-and-neighbour: {new} (settles at 3,3 after one tick)')

# P4: own+neighbour on the four-cycle
s = dict(zip(order, start))
seq4 = [tuple(s[i] for i in order)]
for t in range(60):
    s = tick(s, ac, own=True)
    seq4.append(tuple(s[i] for i in order))
g = [(4, 2, 4, 2), (F(8, 3), F(10, 3), F(8, 3), F(10, 3)), (F(28, 9), F(26, 9), F(28, 9), F(26, 9))]
check(seq4[1:4] == g, f'P4 next three boards {seq4[1:4]}')
check(quoted('4,2,4,2; 8/3,10/3,8/3,10/3; 28/9,26/9,28/9,26/9'), 'guide p.3 P4 boards quoted')
check(all(x != 3 for st in seq4 for x in st), 'P4: no circle equals 3 at any tick 0..60')
check(all(seq4[t] == (3 - 3 * F(-1, 3) ** t, 3 + 3 * F(-1, 3) ** t) * 2 for t in range(61)), 'guide p.3 formula 3 -/+ 3(-1/3)^t holds for t = 0..60')
check(all(sum(st) == 12 for st in seq4), 'P4: total 12 (pair sum 6) is invariant')
check(quoted('Their sum remains 6, while their signed difference reverses and is divided by 3'), 'guide p.3 invariant quoted')

# ------------------------------------------------------------------ roughness
say('#### Bonus P5-P6: least roughness')
# example 0-1-3
b4 = [b for b in D['bonus'][3]['boards'] if len(b['nodes']) >= 2]
n4 = D['bonus'][3]['nodes']
exb = b4[0]
vals = {i: int(n4[i]['text']) for i in exb['nodes']}
score = sum((vals[a] - vals[c]) ** 2 for a, c in exb['edges'])
check(sorted(vals.values()) == [0, 1, 3] and score == 5, f'p.4 example 0-1-3 roughness {score}')
lines = D['bonus'][3]['loose_lines']
# gap squares drawn near the example: side 1 unit and 2 units, the second split into 4 cells
small = [l for l in lines if l['a'][1] < 140 and 260 < min(l['a'][0], l['b'][0]) < 300]
big = [l for l in lines if l['a'][1] < 140 and 305 < min(l['a'][0], l['b'][0]) < 360]
side = lambda ls: (max(max(l['a'][0], l['b'][0]) for l in ls) - min(min(l['a'][0], l['b'][0]) for l in ls),
                   max(max(l['a'][1], l['b'][1]) for l in ls) - min(min(l['a'][1], l['b'][1]) for l in ls))
s1, s2 = side(small), side(big)
check(abs(s1[0] - s1[1]) < .3 and abs(s2[0] - s2[1]) < .3 and abs(s2[0] / s1[0] - 2) < .02 and len(big) == 6,
      f'p.4 gap squares: {s1[0]:.1f}x{s1[1]:.1f} pt and {s2[0]:.1f}x{s2[1]:.1f} pt (ratio {s2[0]/s1[0]:.3f}), larger one cut into 2x2')
# squared paper on p.4 and p.5 is square
for p in (4, 5):
    L = D['bonus'][p - 1]['loose_lines']
    hs = sorted({round(l['a'][1], 2) for l in L if abs(l['a'][1] - l['b'][1]) < .01 and 100 < l['a'][0] < 110})
    lo, hi = min(hs) - .5, max(hs) + .5
    vs = sorted({round(l['a'][0], 2) for l in L if abs(l['a'][0] - l['b'][0]) < .01 and lo <= min(l['a'][1], l['b'][1]) and max(l['a'][1], l['b'][1]) <= hi})
    dh = {round(b - a, 2) for a, b in zip(hs, hs[1:])}; dv = {round(b - a, 2) for a, b in zip(vs, vs[1:])}
    check(len(hs) > 5 and len(vs) > 5 and abs(max(dh) - min(dv)) < .1, f'p.{p} squared paper: row spacing {sorted(dh)} pt, column spacing {sorted(dv)} pt')
# P5
p5 = b4[1]
sc5 = {x: x ** 2 + (6 - x) ** 2 for x in range(7)}
check(len(p5['nodes']) == 3 and sorted(int(n4[i]['text']) for i in p5['nodes'] if n4[i]['kind'] == 'square') == [0, 6], 'P5 board: square 0 - circle - square 6')
check(list(sc5.values()) == [36, 26, 20, 18, 20, 26, 36] and min(sc5, key=sc5.get) == 3, f'P5 scores x=0..6: {list(sc5.values())}; unique min 18 at 3')
check(quoted('score=18+2(x-3)^2') and all(F(x) ** 2 + (6 - F(x)) ** 2 == 18 + 2 * (F(x) - 3) ** 2 for x in [F(k, 7) for k in range(-50, 90)]), 'guide p.4 identity score = 18 + 2(x-3)^2')
# P6
b5 = [b for b in D['bonus'][4]['boards'] if len(b['nodes']) >= 2][0]
check(len(b5['nodes']) == 4 and len(b5['edges']) == 3, 'P6 board: path 0 - circle - circle - 6')
sc6 = {(x, y): x ** 2 + (y - x) ** 2 + (6 - y) ** 2 for x in range(7) for y in range(7)}
best = min(sc6.values())
arg = [k for k, v in sc6.items() if v == best]
check(best == 12 and arg == [(2, 4)] and len(sc6) == 49, f'P6: 49 pairs, unique minimum {best} at {arg}')
check(all(F(x) ** 2 + (F(y) - F(x)) ** 2 + (6 - F(y)) ** 2 - 12 == (F(x) - 2) ** 2 + (F(y) - F(x) - 2) ** 2 + (6 - F(y) - 2) ** 2
          for x in range(-5, 12) for y in range(-5, 12)), 'guide p.4 identity score-12 = sum (d_i - 2)^2')
# path minimum (B-A)^2/L
ok = True
for A in range(0, 5):
    for B in range(0, 9):
        for L in range(1, 5):
            # real minimiser: equal gaps
            m = F((B - A) ** 2, L)
            # random real competitors never beat it
            for _ in range(30):
                pts = [F(A)] + [F(random.randint(-40, 80), 7) for _ in range(L - 1)] + [F(B)]
                if sum((b - a) ** 2 for a, b in zip(pts, pts[1:])) < m:
                    ok = False
check(ok and quoted('its real minimum score is (B-A)^2/L'), 'guide p.4 path minimum (B-A)^2/L never beaten by random rational competitors')

# energy theorem on random graphs: harmonic filling has least roughness, uniquely
random.seed(5)
bad = 0; cnt = 0
for _ in range(400):
    n = random.randint(3, 8)
    kinds = ['square' if random.random() < .4 else 'circle' for _ in range(n)]
    kinds[0] = 'square'
    if 'circle' not in kinds:
        kinds[-1] = 'circle'
    E = set((random.randrange(i), i) for i in range(1, n))
    for _ in range(random.randint(0, 3)):
        a, b = random.sample(range(n), 2); E.add((min(a, b), max(a, b)))
    adj = {i: [] for i in range(n)}
    for a, b in E:
        adj[a].append(b); adj[b].append(a)
    kd = dict(enumerate(kinds))
    val = {i: F(random.randint(0, 9)) for i in range(n) if kinds[i] == 'square'}
    h = dict(val); h.update(solve_expect(adj, kd, val))
    eh = sum((h[a] - h[b]) ** 2 for a, b in E)
    for _ in range(20):
        g = {i: (F(random.randint(-20, 20), 5) if kinds[i] == 'circle' else F(0)) for i in range(n)}
        if all(x == 0 for x in g.values()):
            continue
        cnt += 1
        e2 = sum((h[a] + g[a] - h[b] - g[b]) ** 2 for a, b in E)
        if not e2 > eh:
            bad += 1
check(bad == 0 and cnt > 5000, f'guide p.4 energy proof: harmonic filling strictly beats {cnt} random competitors on random anchored graphs')

say('')
say(f'{len(FAIL)} failure(s)')
for f in FAIL:
    say('  FAIL ' + f)
(HERE / 'out_check_bonus.txt').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
