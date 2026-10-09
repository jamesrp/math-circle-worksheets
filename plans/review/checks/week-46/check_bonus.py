"""Independent check of the Week 46 bonus companion (Boards that forget) and its guide.

Models (from the bonus student pages):
  P1  COPY i to j: each board copies its own slot i into its slot j.
      RESET i to R: slot i becomes red on both boards.
  P2  tickets 1, 2, 3 drawn in order; coverage = every number has appeared.
  P3  S: slot 1 becomes R.  T: (a, b, c) -> (b, c, a), the old left colour moves
      to the right end.
A story acts on every start the same way, so it is tracked symbolically: slot k
holds either an original slot index or the constant 'R'. A story makes every
pair of starts finish alike exactly when every slot ends holding 'R'.
"""
import itertools
import re
from collections import deque
from fractions import Fraction as F

from common import BOARDS, PDFS, Report, pdftext

R = Report()
GUIDE = re.sub(r'\s+', ' ', pdftext(PDFS['bonus-guide'], layout=False))
STUDENT = re.sub(r'\s+', ' ', pdftext(PDFS['bonus'], layout=False))


def quote(s, where=GUIDE, name='bonus guide'):
    ok = re.sub(r'\s+', ' ', s) in where
    R.check(ok, f'{name} prints: "{s[:90]}"')
    return s


def evaluate(sym, board):
    return ''.join('R' if v == 'R' else board[v] for v in sym)


# ---------------------------------------------------------------------------------
# P1: copies and one reset
# ---------------------------------------------------------------------------------
quote('COPY i to j reads slot i and gives its color to slot j, on each board separately', STUDENT, 'bonus page 1')
COPIES = [(i, j) for i in range(3) for j in range(3) if i != j]


def do_copy(sym, i, j):
    s = list(sym)
    s[j] = s[i]
    return tuple(s)


def do_reset(sym, i):
    s = list(sym)
    s[i] = 'R'
    return tuple(s)


# all symbolic states reachable with copies only
start = (0, 1, 2)
seen = {start}
dq = deque([start])
while dq:
    s = dq.popleft()
    for i, j in COPIES:
        t = do_copy(s, i, j)
        if t not in seen:
            seen.add(t)
            dq.append(t)
copy_states = seen
R.note(f'copy-only reachable maps: {len(copy_states)}')
R.check(all(evaluate(s, 'RRR') == 'RRR' and evaluate(s, 'BBB') == 'BBB' for s in copy_states),
        'P1 / overview: copies alone keep RRR as RRR and BBB as BBB')
never = [(a, b) for a, b in itertools.combinations(BOARDS, 2)
         if not any(evaluate(s, a) == evaluate(s, b) for s in copy_states)]
comp = [(a, b) for a, b in itertools.combinations(BOARDS, 2) if all(x != y for x, y in zip(a, b))]
R.check(never == comp and ('RRR', 'BBB') in never,
        f'P1: the pairs copies can never make alike are exactly the 4 complementary pairs {never}')
quote('RRR and BBB cannot match using any number of copies')

# BFS over stories using copies and resets; record resets used
INS = [('C', i, j) for i, j in COPIES] + [('X', i) for i in range(3)]


def step(sym, ins):
    return do_copy(sym, ins[1], ins[2]) if ins[0] == 'C' else do_reset(sym, ins[1])


def sync(sym):
    return all(v == 'R' for v in sym)


best = {}          # number of resets -> list of synchronising stories of the least length found
for L in range(0, 5):
    for story in itertools.product(INS, repeat=L):
        s = start
        for ins in story:
            s = step(s, ins)
        if not sync(s):
            continue
        resets = sum(1 for ins in story if ins[0] == 'X')
        if resets not in best or len(best[resets][0]) == L:
            best.setdefault(resets, []).append(story)
short_any = min(len(v[0]) for v in best.values())
R.check(short_any == 3, f'P1: no story of length <= 2 (any copies/resets) makes all starts finish alike; shortest is {short_any}')
one = [st for st in best.get(1, []) if len(st) == 3]
R.check(len(one) > 0 and all(st[0][0] == 'X' for st in one),
        f'P1: with exactly one RESET the shortest universal story has length 3; {len(one)} such stories, each starting with the RESET')
fmt = lambda st: '; '.join(f'RESET {i[1] + 1}' if i[0] == 'X' else f'COPY {i[1] + 1} to {i[2] + 1}' for i in st)
R.note('all shortest one-RESET stories: ' + ' | '.join(fmt(st) for st in one))
s = start
for ins in [('X', 0), ('C', 0, 1), ('C', 0, 2)]:
    s = step(s, ins)
R.check(sync(s) and all(evaluate(s, b) == 'RRR' for b in BOARDS), 'P1 guide: RESET 1; COPY 1 to 2; COPY 1 to 3 sends every start to RRR')
quote('RESET 1 to R; COPY 1 to 2; COPY 1 to 3 sends every start to RRR')
# an instruction story with at most two instructions leaves a slot never a destination
R.check(all(len({ins[2] if ins[0] == 'C' else ins[1] for ins in st}) < 3
            for L in range(3) for st in itertools.product(INS, repeat=L)),
        'P1 guide: a story of at most two instructions has at most two destination slots')

# P1 extension: directed copy graphs, one reset at site r


def can_sync(n, edges, r):
    st0 = (tuple(range(n)), False)
    seen = {st0}
    dq = deque([st0])
    while dq:
        sym, used = dq.popleft()
        if used and all(v == 'R' for v in sym):
            return True
        moves = [(do_copy(sym, i, j), used) for i, j in edges]
        if not used:
            moves.append((do_reset(sym, r), True))
        for m in moves:
            if m not in seen:
                seen.add(m)
                dq.append(m)
    return False


def reaches_all(n, edges, r):
    seen = {r}
    dq = [r]
    while dq:
        x = dq.pop()
        for i, j in edges:
            if i == x and j not in seen:
                seen.add(j)
                dq.append(j)
    return len(seen) == n


for n in (3, 4):
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    bad = []
    tested = 0
    for mask in range(1 << len(arcs)):
        edges = [a for k, a in enumerate(arcs) if mask >> k & 1]
        for r in range(n):
            tested += 1
            if can_sync(n, edges, r) != reaches_all(n, edges, r):
                bad.append((edges, r))
    R.check(not bad, f'P1 extension: for all {1 << len(arcs)} directed copy graphs on {n} sites and each reset site '
            f'({tested} cases), one reset synchronises iff the reset site reaches every site {bad[:2]}')
quote('synchronization from one reset is possible exactly when the reset site can reach every site in that directed graph')

# ---------------------------------------------------------------------------------
# P2: coverage counts
# ---------------------------------------------------------------------------------
def covering(m):
    return sum(1 for s in itertools.product((1, 2, 3), repeat=m) if set(s) == {1, 2, 3})


c3, c4 = covering(3), covering(4)
R.check((c3, c4) == (6, 36), f'P2: {c3} of 27 three-draw and {c4} of 81 four-draw stories cover')
R.check((F(c3, 27), F(c4, 81)) == (F(2, 9), F(4, 9)), 'P2 guide: probabilities 2/9 and 4/9')
R.check(3 * 6 * 2 == 36 and 3 * 2 * 1 == 6, 'P2 guide counting: 3 x 6 x 2 = 36 and 3 x 2 x 1 = 6')
four = [s for s in itertools.product((1, 2, 3), repeat=4) if set(s) == {1, 2, 3}]
R.check(all(sorted(__import__('collections').Counter(s).values()) == [1, 1, 2] for s in four),
        'P2 guide: in every covering four-draw story one label appears twice and the others once')
noreplace = list(itertools.permutations((1, 2, 3), 3))
R.check(len(noreplace) == 6 and all(set(s) == {1, 2, 3} for s in noreplace), 'P2: without replacement all 6 three-draw stories cover')
R.check(all(set((1,) * m) != {1, 2, 3} for m in range(1, 50)), 'P2: 1,1,...,1 never covers, for every length')
for m in range(1, 13):
    miss = F(3 ** m - covering(m), 3 ** m) if m <= 9 else 3 * F(2, 3) ** m - 3 * F(1, 3) ** m
    if m <= 9:
        R.check(miss == 3 * F(2, 3) ** m - 3 * F(1, 3) ** m and miss <= 3 * F(2, 3) ** m,
                f'P2 overview: m={m}: P(not covered) = {miss} <= 3(2/3)^m = {3 * F(2, 3) ** m}')
quote('coverage occurs in 6 of the 27 length-three stories and 36 of the 81 length-four stories')
quote('the probability a particular position is missing after m draws is (2/3)^m')
# extension: fresh fair colours at each visit -> conditional uniformity, also without replacement
for stories, label in [([s for s in itertools.product((1, 2, 3), repeat=4) if set(s) == {1, 2, 3}], 'with replacement, 4 draws'),
                       (noreplace, 'without replacement')]:
    ok = True
    for ps in stories:
        for startb in ('RRR', 'BRB'):
            cnt = {}
            for cols in itertools.product('RB', repeat=len(ps)):
                b = list(startb)
                for p, c in zip(ps, cols):
                    b[p - 1] = c
                cnt[''.join(b)] = cnt.get(''.join(b), 0) + 1
            ok &= len(cnt) == 8 and len(set(cnt.values())) == 1
    R.check(ok, f'P2 extension: covering position story + fresh fair colours gives uniform final board ({label})')

# ---------------------------------------------------------------------------------
# P3: S and T
# ---------------------------------------------------------------------------------
R.check('RBB'[1:] + 'RBB'[:1] == 'BBR', 'P3 picture: T sends RBB to BBR')


def S(sym):
    return ('R',) + sym[1:]


def T(sym):
    return sym[1:] + sym[:1]


def shortest_words(n, maxlen):
    out = []
    for L in range(0, maxlen + 1):
        for w in itertools.product('ST', repeat=L):
            s = tuple(range(n))
            for ch in w:
                s = S(s) if ch == 'S' else T(s)
            if all(v == 'R' for v in s):
                out.append(''.join(w))
        if out:
            return L, out
    return None, []


L3, w3 = shortest_words(3, 8)
R.check(L3 == 5 and w3 == ['STSTS'], f'P3: shortest synchronising word length {L3}, words {w3}')
traj = []
s = ('x', 'y', 'z')
for ch in 'STSTS':
    s = S(s) if ch == 'S' else T(s)
    traj.append(''.join(s))
R.check(traj == ['Ryz', 'yzR', 'RzR', 'zRR', 'RRR'], f'P3 guide trajectory {traj}')
quote('From (x,y,z), STSTS gives (R,y,z), (y,z,R), (R,z,R), (z,R,R), (R,R,R)')
okST = True
for L in range(0, 9):
    for w in itertools.product('ST', repeat=L):
        s = (0, 1, 2)
        for ch in w:
            s = S(s) if ch == 'S' else T(s)
        if all(v == 'R' for v in s):
            okST &= w.count('S') >= 3 and w.count('T') >= 2
R.check(okST, 'P3 guide: every synchronising word up to length 8 has at least three S and at least two T')
for n in range(2, 7):
    Ln, wn = shortest_words(n, 2 * n)
    target = 'S' + 'TS' * (n - 1)
    R.check(Ln == 2 * n - 1 and wn == [target], f'P3 extension: n={n} slots: shortest length {Ln} = 2n-1, unique word {wn}')
# the same word on the 8 actual boards


def word_on_board(b, w):
    for ch in w:
        b = 'R' + b[1:] if ch == 'S' else b[1:] + b[0]
    return b


R.check({word_on_board(b, 'STSTS') for b in BOARDS} == {'RRR'}, 'P3: STSTS sends all 8 actual boards to RRR')
R.check(all(len({word_on_board(b, ''.join(w)) for b in BOARDS}) > 1 for L in range(5) for w in itertools.product('ST', repeat=L)),
        'P3: no word of length <= 4 sends all 8 actual boards to one finish')

# ---------------------------------------------------------------------------------
# guide arithmetic
# ---------------------------------------------------------------------------------
diam = 2 * 31 / 72 * 25.4
R.check(abs(diam - 21.9) < 0.05, f'guide: working circles {diam:.2f} mm across (builder radius 31 pt)')
quote('Large circles are 21.9 mm across')
kids = 'KK11 3333 445'.replace(' ', '')
R.check(len(kids) == 11, 'guide: KK11 / 3333 / 445 is eleven children')
pairs = 2 + 2 + 1
R.check((pairs * 2, pairs * 6, pairs * 3, pairs, pairs * 3, pairs) == (10, 30, 15, 5, 15, 5),
        'guide totals: 10 rows, 30 counters, 15 tickets, 5 cups, 15 markers, 5 pencils for 5 pair kits')
quote('Totals: ten working rows, thirty reversible counters (or thirty of each single color), fifteen tickets, five cups, fifteen coverage markers, five pencils')
R.check(pairs * 6 == 30, 'guide: six red and six blue paper circles per pair -> thirty of each colour')

R.summary('check_bonus')
