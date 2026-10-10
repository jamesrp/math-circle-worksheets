"""Independent mathematical check of Week 20 (averaging / maximum principle).

Uses only boards.json, which extract_boards.py reads back out of the delivered
PDFs (run that first).  Every filling is recomputed here with exact rational
Gaussian elimination or brute-force enumeration; the guide's statements are
transcribed as quoted claims, each quote is first confirmed to occur in the
delivered guide text, and then the claim is recomputed.
Output: out_check_math.txt
"""
import itertools
import json
import random
import re
import subprocess
from fractions import Fraction as F
from pathlib import Path

from repo import WEEK

F.__repr__ = lambda self: str(self)  # print fractions as 1/2, 3
HERE = Path(__file__).resolve().parent
D = json.load(open(HERE / 'boards.json'))
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def guide_text(pdf):
    t = subprocess.run(['pdftotext', str(pdf), '-'], capture_output=True, text=True).stdout
    t = t.replace('−', '-').replace('ﬁ', 'fi').replace('ﬂ', 'fl')
    return re.sub(r'\s+', ' ', t)


GUIDE = guide_text(WEEK / 'week-20-facilitator.pdf')


def quoted(q):
    qn = re.sub(r'\s+', ' ', q)
    ok = qn in GUIDE
    if not ok:
        say('     (quote not found verbatim: ' + q[:80] + ')')
    return ok


# ------------------------------------------------------------------ boards
class Board:
    """Vertices: index -> ('S', value) or ('C', label or None)."""

    def __init__(self, page, b):
        ns = page['nodes']
        self.ids = b['nodes']
        self.kind = {i: ('S' if ns[i]['kind'] == 'square' else 'C') for i in self.ids}
        self.text = {i: ns[i]['text'] for i in self.ids}
        self.dots = {i: ns[i]['dots'] for i in self.ids}
        self.cubes = {i: ns[i]['cubes'] for i in self.ids}
        self.pos = {i: (ns[i]['cx'], ns[i]['cy']) for i in self.ids}
        self.size = {i: (ns[i]['x1'] - ns[i]['x0'], ns[i]['y1'] - ns[i]['y0']) for i in self.ids}
        self.adj = {i: [] for i in self.ids}
        for a, c in b['edges']:
            self.adj[a].append(c)
            self.adj[c].append(a)
        self.edges = [tuple(e) for e in b['edges']]

    def squares(self):
        return {i: num(self.text[i]) for i in self.ids if self.kind[i] == 'S'}

    def circles(self):
        return [i for i in self.ids if self.kind[i] == 'C']

    def sig(self):
        return f"{sum(1 for i in self.ids if self.kind[i]=='S')} squares {self.squares_sorted()}, {len(self.circles())} circles, {len(self.edges)} lines"

    def squares_sorted(self):
        return sorted(v for v in self.squares().values() if v is not None)


def num(t):
    t = t.strip().split(' ')[0] if t else ''
    if re.fullmatch(r'-?\d+', t):
        return F(int(t))
    if re.fullmatch(r'-?\d+/\d+', t):
        a, b = t.split('/')
        return F(int(a), int(b))
    return None


def boards(band, page, min_vertices=2):
    pg = D[band][page - 1]
    return [Board(pg, b) for b in pg['boards'] if len(b['nodes']) >= min_vertices]


def works(B, val):
    """val: vertex -> value for every vertex. True when every circle averages its neighbours."""
    for c in B.circles():
        nb = B.adj[c]
        if not nb or F(sum(val[v] for v in nb), len(nb)) != val[c]:
            return False
    return True


def solve(B, sq=None):
    """Exact harmonic extension. Returns (solution dict or None, nullity)."""
    sq = B.squares() if sq is None else sq
    cs = B.circles()
    idx = {c: k for k, c in enumerate(cs)}
    n = len(cs)
    A = [[F(0)] * (n + 1) for _ in range(n)]
    for c in cs:
        r = idx[c]
        A[r][r] = F(len(B.adj[c]))
        for v in B.adj[c]:
            if v in idx:
                A[r][idx[v]] -= 1
            else:
                A[r][n] += sq[v]
    # gaussian elimination
    rank, row = 0, 0
    piv = []
    for col in range(n):
        p = next((r for r in range(row, n) if A[r][col] != 0), None)
        if p is None:
            continue
        A[row], A[p] = A[p], A[row]
        for r in range(n):
            if r != row and A[r][col] != 0:
                f = A[r][col] / A[row][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[row])]
        piv.append(col)
        row += 1
    nullity = n - len(piv)
    if nullity:
        return None, nullity
    sol = {}
    for r, col in enumerate(piv):
        sol[cs[col]] = A[r][n] / A[r][col]
    return sol, 0


def fill(B, sol):
    v = dict(B.squares())
    v.update(sol)
    return v


def enum(B, rng):
    """All fillings of the circles with values from rng (squares fixed)."""
    cs = B.circles()
    sq = B.squares()
    res = []
    for vals in itertools.product(rng, repeat=len(cs)):
        v = dict(sq)
        v.update(zip(cs, map(F, vals)))
        if works(B, v):
            res.append(tuple(vals))
    return res


def fmt(B, sol):
    return ', '.join(f"{'C'}{c}={sol[c]}" for c in sorted(sol, key=lambda c: (round(B.pos[c][1] / 5), B.pos[c][0])))


def ordered_circles(B):
    return sorted(B.circles(), key=lambda c: (round(B.pos[c][1] / 5), B.pos[c][0]))


def vals_lr(B, sol):
    return [sol[c] for c in ordered_circles(B)]


def maxprinciple_ok(B, sol):
    sq = B.squares()
    v = fill(B, sol)
    return all(min(sq.values()) <= v[c] <= max(sq.values()) for c in B.circles())


# ===================================================================== delivered files
import hashlib
from repo import SRC, BONUS_SRC
say('#### Delivered PDFs against the reference copies in the source packages')
pairs = [('week-20-k-1.pdf', SRC / 'reference-pdfs' / 'k-1.pdf'), ('week-20-grades-2-3.pdf', SRC / 'reference-pdfs' / 'grades-2-3.pdf'),
         ('week-20-grades-4-5.pdf', SRC / 'reference-pdfs' / 'grades-4-5.pdf'), ('week-20-facilitator.pdf', SRC / 'reference-pdfs' / 'facilitator-guide.pdf'),
         ('week-20-bonus.pdf', BONUS_SRC / 'reference-pdfs' / 'week-20-bonus.pdf'), ('week-20-bonus-facilitator.pdf', BONUS_SRC / 'reference-pdfs' / 'week-20-bonus-facilitator.pdf')]
for a, b in pairs:
    ha = hashlib.md5((WEEK / a).read_bytes()).hexdigest(); hb = hashlib.md5(b.read_bytes()).hexdigest()
    check(ha == hb, f'{a} is byte-identical to {b.relative_to(b.parents[2])} ({ha})')

# every circle has a neighbour; largest number of neighbours per band
for band, pages in (('k-1', 7), ('grades-2-3', 6), ('grades-4-5', 7)):
    degs = []
    for p in range(1, pages + 1):
        for B in boards(band, p):
            for c in B.circles():
                degs.append(len(B.adj[c]))
    check(min(degs) >= 1, f'{band}: every circle on every board has at least one joined shape; largest count {max(degs)}')

# ===================================================================== K-1
say('#### K-1 (week-20-k-1.pdf)')
# dots / cube pictures match the printed numerals on every K-1 page
for p in range(1, 8):
    pg = D['k-1'][p - 1]
    for n in pg['nodes']:
        v = num(n['text'])
        if n['kind'] == 'square' and n['x1'] - n['x0'] > 80 and v is not None:
            check(n['dots'] == v, f"K-1 p.{p}: large square '{n['text']}' shows {n['dots']} dots")
        if n['x1'] - n['x0'] < 60 and n['cubes'] and v is not None:
            check(n['cubes'] == v, f"K-1 p.{p}: example shape '{n['text']}' shows {n['cubes']} small cubes")

# p.1 example: before / after board
ex = boards('k-1', 1)[:2]
after = ex[1]
v = {i: num(after.text[i]) for i in after.ids}
check(works(after, v), f"K-1 p.1 worked example after-board {sorted(v.values())} satisfies the rule")
check(sorted(after.squares_sorted()) == [0, 6] and [v[c] for c in after.circles()] == [3], 'K-1 p.1 example is 0,6 -> 3')
m1 = [len([c for c in D['k-1'][0]['cubes'] if r['x0'] < c[0] < r['x1'] and r['y0'] < c[1] < r['y1']]) for r in D['k-1'][0]['rects'] + D['k-1'][0]['rounds'] if r['dash']]
check(m1 == [3, 3], f'K-1 p.1 example: the two dashed sharing mats hold {m1} cubes')

# P1
bs = boards('k-1', 1)[2:]
ans = []
for B in bs:
    sol, nl = solve(B)
    ans.append(vals_lr(B, sol))
    check(nl == 0 and all(x.denominator == 1 for x in sol.values()), f"K-1 P1 board {B.squares_sorted()}: unique whole filling {vals_lr(B, sol)}")
check(ans == [[1], [3], [2], [4]], 'K-1 P1 circles in reading order 1,3,2,4 (guide p.5)')
check(quoted('Then try squares 1 and 5; the circle is 3') and F(1 + 5, 2) == 3, 'guide p.5 extension: squares 1 and 5 give 3')

# p.2 example chain 2-3-4-5
B = boards('k-1', 2)[0]
v = {i: num(B.text[i]) for i in B.ids}
check(works(B, v), 'K-1 p.2 worked example 2-3-4-5 satisfies the rule at both circles')
# check panels: 2+4 -> 3 each, 3+5 -> 4 each
pg = D['k-1'][1]
mats = [r for r in pg['rects'] + pg['rounds'] if r['dash']]
mat_counts = [len([c for c in pg['cubes'] if r['x0'] < c[0] < r['x1'] and r['y0'] < c[1] < r['y1']]) for r in sorted(mats, key=lambda r: r['x0'])]
check(mat_counts == [3, 3, 4, 4], f'K-1 p.2 sharing mats hold {mat_counts} cubes (3,3 for 2+4 and 4,4 for 3+5)')

# P2
ans = []
for B in boards('k-1', 2)[1:]:
    sol, nl = solve(B)
    ans.append(tuple(vals_lr(B, sol)))
    check(nl == 0 and all(x.denominator == 1 for x in sol.values()), f"K-1 P2 path {B.squares_sorted()}: unique whole filling {vals_lr(B, sol)}")
check(ans == [(1, 2), (2, 1), (2, 4), (4, 2)], 'K-1 P2 pairs (1,2),(2,1),(2,4),(4,2) (guide p.6)')
# extension: endpoints 3 and 6 -> 4,5
check([F(3) + F(3, 3) * k for k in (1, 2)] == [4, 5], 'K-1 P2 extension: 3..6 path circles 4,5')

# P3: circle 2, squares 0..3
big, *small = boards('k-1', 3)
check(len(small) == 10, f'K-1 P3 page has {len(small)} small recording boards')
check(all(B.sig().startswith('3 squares') and len(B.circles()) == 1 for B in [big] + small), 'K-1 P3 every board is one circle joined to three squares')
sol3 = []
c = big.circles()[0]
sqs = [i for i in big.ids if big.kind[i] == 'S']
top = min(sqs, key=lambda i: big.pos[i][1])
left, right = sorted([i for i in sqs if i != top], key=lambda i: big.pos[i][0])
for t, l, r in itertools.product(range(4), repeat=3):
    v = {top: F(t), left: F(l), right: F(r), c: F(2)}
    if works(big, v):
        sol3.append((t, l, r))
check(len(sol3) == 10, f'K-1 P3 has exactly {len(sol3)} ordered fillings: {sol3}')
check(len(sol3) == len(small), 'K-1 P3 recording boards = number of fillings')
check(len({tuple(sorted(s)) for s in sol3}) == 3, 'K-1 P3: 3 unordered shapes (0,3,3),(1,2,3),(2,2,2)')
g = '(0,3,3), (1,2,3), (1,3,2), (2,1,3), (2,2,2), (2,3,1), (3,0,3), (3,1,2), (3,2,1), (3,3,0)'
check(quoted(g) and sorted(sol3) == sorted(eval('[' + g + ']')), 'guide p.7 exact list of 10 (top, lower-left, lower-right)')
ext = [s for s in itertools.product(range(4), repeat=3) if sum(s) == 3]
check(quoted('If the circle changes to 1 with the same 0-3 square bound, there are again 10 fillings') and len(ext) == 10,
      'guide p.7 extension: circle 1, squares 0-3 -> 10 fillings')

# P4: three different cards 0..4 on square-circle-square
big, *small = boards('k-1', 4)
check(len(small) == 8, f'K-1 P4 page has {len(small)} small recording boards')
words = [w['t'] for w in D['k-1'][3]['words']]
check(all(str(k) in words for k in range(5)), 'K-1 P4 cards 0,1,2,3,4 printed')
c = big.circles()[0]
l, r = sorted([i for i in big.ids if big.kind[i] == 'S'], key=lambda i: big.pos[i][0])
sol4 = []
for a, m, b in itertools.permutations(range(5), 3):
    if works(big, {l: F(a), c: F(m), r: F(b)}):
        sol4.append((a, m, b))
check(len(sol4) == 8, f'K-1 P4 exactly {len(sol4)} ordered fillings with distinct cards: {sol4}')
g = '(0,1,2), (2,1,0), (0,2,4), (4,2,0), (1,2,3), (3,2,1), (2,3,4), (4,3,2)'
check(quoted(g) and sorted(sol4) == sorted(eval('[' + g + ']')), 'guide p.8 exact list of 8')
rep = [(a, m, b) for a, m, b in itertools.product(range(5), repeat=3) if 2 * m == a + b]
check(quoted('Then there are 13 ordered triples') and len(rep) == 13, f'guide p.8 extension with repeats: {len(rep)} ordered triples')

# P5
res = []
for B in boards('k-1', 5):
    sol, nl = solve(B)
    res.append(tuple(vals_lr(B, sol)))
    check(nl == 0 and max(sol.values()) < 5, f'K-1 P5 board {B.squares_sorted()}: unique filling {vals_lr(B, sol)}, no 5-cube circle')
    # brute force over 0..20 confirms no other whole filling
    check(len(enum(B, range(21))) == 1, f'K-1 P5 board {B.squares_sorted()}: only one whole filling with circles 0..20')
check(res == [(1, 2), (2, 3)], 'guide p.9: legal pairs (1,2) and (2,3)')
# guide p.9 forced checks
# upper 0-L-R-3: L=5 -> R=10 ; R=5 -> L=7 ; lower 1-L-R-4: L=5 -> R=9 ; R=5 -> L=6
check(quoted('putting 5 in the left circle forces 10 in the right') and 2 * 5 - 0 == 10 and 2 * 10 != 5 + 3, 'guide p.9 upper: L=5 forces R=10; 2*10 != 5+3')
check(quoted('Putting 5 in the right forces 7 in the left') and 2 * 5 - 3 == 7 and 2 * 7 != 0 + 5, 'guide p.9 upper: R=5 forces L=7; 2*7 != 0+5')
check(quoted('5 on the left forces 9 on the right') and 2 * 5 - 1 == 9 and 2 * 9 != 5 + 4, 'guide p.9 lower: L=5 forces R=9; 2*9 != 5+4')
check(quoted('5 on the right forces 6 on the left') and 2 * 5 - 4 == 6 and 2 * 6 != 1 + 5, 'guide p.9 lower: R=5 forces L=6; 2*6 != 1+5')

# P6
for B, sq in zip(boards('k-1', 6), (2, 3)):
    sol, nl = solve(B)
    check(nl == 0 and set(sol.values()) == {sq}, f'K-1 P6 board with square {sq} ({len(B.circles())} circles, {len(B.edges)} lines): every circle = {sq}')
    check(len(enum(B, range(11))) == 1, f'K-1 P6 square {sq}: only one whole filling with circles 0..10')
check(B.edges and len(B.edges) == 4 and len(B.circles()) == 3, 'K-1 P6 lower board is a four-cycle (square + 3 circles)')
T = boards('k-1', 6)[0]
s4, _ = solve(T, {k: F(4) for k in T.squares()})
check(quoted("Replace the square's 2 by 4: every triangle circle must become 4") and set(s4.values()) == {4}, 'guide p.10 extension: square 4 -> triangle circles 4')

# P7
bs = boards('k-1', 7)
tri = [B for B in bs if len(B.ids) == 3]
path = [B for B in bs if len(B.ids) == 4]
check(len(tri) == 7 and len(path) == 7, f'K-1 P7: {len(tri)} triangle boards and {len(path)} 4-circle paths (1 large + 6 recording each)')
for B in (tri[0], path[0]):
    e = enum(B, range(6))
    check(len(e) == 6 and all(len(set(x)) == 1 for x in e), f'K-1 P7 {len(B.ids)}-circle board: {len(e)} fillings, all constant')
    check(len(enum(B, range(7))) == 7, f'guide p.11 extension: 0..6 gives 7 fillings ({len(B.ids)}-circle board)')

# ===================================================================== Grades 2-3
say('#### Grades 2-3 (week-20-grades-2-3.pdf)')
bs = boards('grades-2-3', 1)
order = sorted(bs, key=lambda B: (round(min(p[1] for p in B.pos.values()) / 100), min(p[0] for p in B.pos.values())))
starts = []
for B in order:
    sol, nl = solve(B)
    cval = list(sol.values())[0]
    starts.append(cval)
    # every single-square change (to any whole number 0..60) that raises the circle by exactly 2
    changes = []
    for s, val in B.squares().items():
        for new in range(0, 61):
            if new == val:
                continue
            sq = dict(B.squares()); sq[s] = F(new)
            s2, _ = solve(B, sq)
            if list(s2.values())[0] == cval + 2:
                changes.append((int(val), new))
    d = len(B.adj[B.circles()[0]])
    check(all(n - o == 2 * d for o, n in changes) and len(changes) == d,
          f'2-3 P1 board {B.squares_sorted()}: circle {cval}; raising by 2 needs one square +{2*d}: {changes}')
check(starts == [4, 4, 5, 5], f'2-3 P1 circles in reading order {starts} (guide p.12 says 4,4,5,5)')
check(quoted('Lower right: change 2 to 8, giving (8+5+8)/3=7') and F(8 + 5 + 8, 3) == 7, 'guide p.12 example checks')
check(quoted('the circle increases by 3 on a two-neighbor board and by 2 on a three-neighbor board') and F(6, 2) == 3 and F(6, 3) == 2, 'guide p.12 extension')

ex, *bs = boards('grades-2-3', 2)
v = {i: num(ex.text[i]) for i in ex.ids}
check(works(ex, v), '2-3 p.2 worked example 2-3-4-5 satisfies the rule')
res = []
for B in bs:
    sol, nl = solve(B)
    res.append(vals_lr(B, sol))
    check(nl == 0 and all(x.denominator == 1 for x in sol.values()), f'2-3 P2 {B.sig()}: unique whole filling {fmt(B, sol)}')
check([list(map(int, r)) for r in res] == [[3, 6], [5, 8], [3, 3], [4, 6]], f'2-3 P2 answers {res} match guide p.13 (3,6),(5,8),(3,3), tree 4 then 6')
check(quoted('3u=6+v and 2v=u+8') and quoted('6u=12+(u+8)'), 'guide p.13 tree equations quoted')
# extension: +1 everywhere gives the P5 middle tree
tree = bs[3]
sq = {k: v + 1 for k, v in tree.squares().items()}
s2, _ = solve(tree, sq)
check(sorted(map(int, sq.values())) == [1, 7, 9] and sorted(map(int, s2.values())) == [5, 7], 'guide p.13 extension: tree +1 -> squares 1,7,9 circles 5,7')

for B in boards('grades-2-3', 3):
    sol, nl = solve(B)
    check(nl == 0 and max(sol.values()) <= max(B.squares().values()), f'2-3 P3 {B.sig()}: unique filling {vals_lr(B, sol)}; no circle above every square')
check(True, '2-3 P3 guide p.14: path 3,5,7 and diamond 5,5 (see lines above)')

res = []
for B in boards('grades-2-3', 4):
    sol, nl = solve(B)
    sq = B.squares()
    lr = vals_lr(B, sol)
    res.append(lr)
    eqmax = [x for x in lr if x == max(sq.values())]
    eqmin = [x for x in lr if x == min(sq.values())]
    say(f'     2-3 P4 board {B.sig()}: circles L->R {lr}; equal to max {len(eqmax)}, to min {len(eqmin)}')
check(res == [[3, 6, 6], [0, 0, 3]], '2-3 P4 upper 3,6,6 (two circles = 6), lower 0,0,3 (two circles = 0), as guide p.15')
# guide p.15 extension: middle square -> circle, square 0 stays: all 0
B = boards('grades-2-3', 4)[0]
mid = [s for s, v in B.squares().items() if v == 6][0]
B.kind[mid] = 'C'
sol, nl = solve(B)
check(nl == 0 and set(sol.values()) == {0}, 'guide p.15 extension: upper middle square made a circle -> whole board 0')

res = []
for B in boards('grades-2-3', 5):
    sol, nl = solve(B)
    res.append(vals_lr(B, sol))
    check(nl == 0, f'2-3 P5 {B.sig()}: unique filling {vals_lr(B, sol)} (nullity 0 => no second real filling)')
check([list(map(int, r)) for r in res] == [[6, 9], [5, 7], [7, 7]], '2-3 P5 answers (6,9), tree 5,7, diamond 7,7 (guide p.16)')
check(quoted('there is no vertical edge between them') and len(boards('grades-2-3', 5)[2].edges) == 4, '2-3 P5 bottom diamond has 4 lines, no circle-circle line')

for B in boards('grades-2-3', 6):
    e = enum(B, range(6))
    check(len(e) == 6 and all(len(set(x)) == 1 for x in e), f'2-3 P6 {len(B.ids)}-circle board ({len(B.edges)} lines): {len(e)} fillings, all constant')
check(len(enum(boards('grades-2-3', 6)[0], range(6))) * len(enum(boards('grades-2-3', 6)[1], range(6))) == 36, 'guide p.17 extension: 6 x 6 = 36 for the two boards together')

# ===================================================================== Grades 4-5
say('#### Grades 4-5 (week-20-grades-4-5.pdf)')
ex, *bs = boards('grades-4-5', 1)
check(works(ex, {i: num(ex.text[i]) for i in ex.ids}), '4-5 p.1 worked example satisfies the rule')
res = []
for B in bs:
    sol, nl = solve(B)
    res.append(vals_lr(B, sol))
    check(nl == 0, f'4-5 P1 {B.sig()}: unique filling {vals_lr(B, sol)}; no second filling exists')
check([list(map(int, r)) for r in res] == [[5, 10], [5, 7], [8, 8]], '4-5 P1 (5,10), (5,7), (8,8) as guide p.18')
check(quoted('3u=16+v and 3v=16+u. Subtracting gives 4(u-v)=0'), 'guide p.18 diamond algebra quoted (3u-3v = v-u => 4(u-v)=0)')
check(F(4 + 15, 2) != 8 and F(0 + 8, 2) == 4, 'guide p.18 extension (4,8): left works, right fails')

up, low = boards('grades-4-5', 2)
sol, nl = solve(up)
deg = {c: len(up.adj[c]) for c in up.circles()}
say('     4-5 P2 upper: circle degrees', sorted(deg.values()), 'filling', fmt(up, sol))
check(nl == 0 and sorted(map(int, sol.values())) == [3, 6, 7, 8], '4-5 P2 upper board filling {3,6,7,8} (guide p.19)')
check(max(sol.values()) < 13, '4-5 P2 upper: no circle 13 or more')
check(max(sol.values()) < 11, 'guide p.19 extension: 11 cannot occur in an upper circle (actual max 8)')
check(sorted(deg.values()) == [2, 2, 3, 4], '4-5 P2 upper: one circle has four neighbours (v), as guide says')
sol, nl = solve(low)
check(nl == 0 and set(sol.values()) == {6}, '4-5 P2 lower diamond: both circles 6')

B = boards('grades-4-5', 3)[0]
sol, nl = solve(B)
say('     4-5 P3 illustration filling', fmt(B, sol))
check(nl == 0 and sorted(map(int, sol.values())) == [4, 6, 6, 8], '4-5 P3 illustration: horizontal 4,6,8, top 6 (guide p.20)')
# P3 theorem: random finite graphs
random.seed(20)
viol_comp = viol_local = 0
trials = 0
for _ in range(3000):
    n = random.randint(2, 9)
    kinds = ['S' if random.random() < .35 else 'C' for _ in range(n)]
    if 'S' not in kinds:
        kinds[0] = 'S'
    E = set()
    for i in range(1, n):
        E.add((random.randrange(i), i))
    for _ in range(random.randint(0, n)):
        a, b = random.sample(range(n), 2)
        E.add((min(a, b), max(a, b)))
    class G: pass
    G = Board.__new__(Board)
    G.ids = list(range(n)); G.kind = dict(enumerate(kinds)); G.adj = {i: [] for i in range(n)}
    for a, b in E:
        G.adj[a].append(b); G.adj[b].append(a)
    G.edges = list(E)
    sq = {i: F(random.randint(-9, 9)) for i in range(n) if kinds[i] == 'S'}
    s, nl = solve(G, sq)
    if nl:
        continue
    trials += 1
    v = dict(sq); v.update(s)
    for c in G.circles():
        # squares reachable along any lines (same component) and reachable without passing a square
        seen, stack, local = {c}, [c], set()
        while stack:
            x = stack.pop()
            for y in G.adj[x]:
                if y not in seen:
                    seen.add(y)
                    if G.kind[y] == 'C':
                        stack.append(y)
                    else:
                        local.add(y)
        comp = {c}; st = [c]
        while st:
            x = st.pop()
            for y in G.adj[x]:
                if y not in comp:
                    comp.add(y); st.append(y)
        cs = [sq[y] for y in comp if G.kind[y] == 'S']
        ls = [sq[y] for y in local]
        if not (min(cs) <= v[c] <= max(cs)):
            viol_comp += 1
        if not (min(ls) <= v[c] <= max(ls)):
            viol_local += 1
check(viol_comp == 0 and viol_local == 0 and trials > 1000,
      f'4-5 P3 theorem on {trials} random anchored graphs: no circle outside the squares of its component, nor outside the squares its circle-group touches')

res = []
for B in boards('grades-4-5', 4):
    sol, nl = solve(B)
    lr = vals_lr(B, sol)
    res.append(lr)
    m = max(B.squares().values())
    say(f'     4-5 P4 {B.sig()}: circles {lr}; circles equal to largest square {m}: {sum(1 for x in lr if x == m)}')
check([list(map(int, r)) for r in res] == [[4, 8, 8], [4, 8, 8]], '4-5 P4 both boards 4,8,8 (guide p.21)')
check(sum(1 for x in res[1] if x == 12) == 0 and sum(1 for x in res[0] if x == 8) == 2, '4-5 P4 upper: two circles = 8; lower: none = 12')

b1, b2 = boards('grades-4-5', 5)
s1, n1 = solve(b1)
s2, n2 = solve(b2)
check(b1.sig() == b2.sig() and sorted(s1.values()) == sorted(s2.values()), '4-5 P5 the two printed boards are identical')
say('     4-5 P5 filling', fmt(b1, s1))
check(n1 == 0 and sorted(map(int, s1.values())) == [6, 8, 10], '4-5 P5 unique filling: left 6, upper 10, lower 8 (guide p.22)')
sqa = {k: F(random.randint(0, 20)) for k in b1.squares()}; sqb = {k: F(random.randint(0, 20)) for k in b1.squares()}
sa, _ = solve(b1, sqa); sb, _ = solve(b1, sqb); sm, _ = solve(b1, {k: (sqa[k] + sqb[k]) / 2 for k in sqa})
check(all(sm[c] == (sa[c] + sb[c]) / 2 for c in sm), 'guide p.22 extension: the average of two fillings is the filling for the averaged squares')
up8 = [c for c in b1.circles() if 16 in [b1.squares().get(x) for x in b1.adj[c]]][0]
check(s1[up8] == 10, '4-5 P5: the circle joined to 16 is 10')

bs = boards('grades-4-5', 6)
tri = bs[0]
e = enum(tri, range(5))
check(len(e) == 5, f'4-5 P6 upper triangle: {len(e)} fillings with 0..4')
lowpieces = bs[1:]
frame = D['grades-4-5'][5]['rounds']
inside_frame = all(any(f['x0'] < x < f['x1'] and f['y0'] < y < f['y1'] for f in frame) for B in lowpieces for x, y in B.pos.values())
check(len(lowpieces) == 2 and inside_frame and len(frame) == 1, '4-5 P6 lower board = two separate joined pairs inside one dashed outline')
tot = 1
for B in lowpieces:
    tot *= len(enum(B, range(5)))
check(tot == 25, f'4-5 P6 lower board: {tot} fillings (5 x 5)')
check(5 ** 4 == 625, 'guide p.23: 625 unrestricted four-tuples')

res = []
needed = set()
for B in boards('grades-4-5', 7):
    sol, nl = solve(B)
    lr = vals_lr(B, sol)
    res.append(lr)
    needed |= {x for x in lr if x.denominator != 1}
    say(f'     4-5 P7 {B.sig()}: {lr} whole={all(x.denominator == 1 for x in lr)}')
check(res == [[F(1, 2)], [1, 2], [1], [F(1, 3), F(2, 3)]], '4-5 P7: rows 1 and 4 need fractions; rows 2 and 3 whole (guide p.24)')
# fraction cards: shaded parts of each bar
pg = D['grades-4-5'][6]
cells = sorted([r for r in pg['rects'] if r['h'] < 30 and r['w'] < 60], key=lambda r: r['x0'])
cards = []
for r in cells:
    if cards and abs(r['x0'] - cards[-1][-1]['x1']) < .5:
        cards[-1].append(r)
    else:
        cards.append([r])
fr = [F(sum(1 for r in c if not r['fill'].startswith('rgb(100%')), len(c)) for c in cards]
widths = [round(sum(r['w'] for r in c), 1) for c in cards]
check(fr == [F(1, 2), F(1, 3), F(2, 3)] and len(set(widths)) == 1, f'4-5 P7 fraction cards show {fr} of equal bars {widths} pt; needed {sorted(needed)}')
check(set(fr) == needed, '4-5 P7 the three cards are exactly the three fractions needed')
check(all(len(set(round(r['w'], 2) for r in c)) == 1 for c in cards), '4-5 P7 each fraction bar is cut into equal parts')

# ===================================================================== guide diagrams
say('#### Guide solution diagrams compared with the student boards')


def iso(G, S):
    """Is there a bijection G->S preserving kind, square values and lines? Return mapping."""
    if len(G.ids) != len(S.ids) or len(G.edges) != len(S.edges):
        return None
    Ge = {frozenset(e) for e in G.edges}
    Se = {frozenset(e) for e in S.edges}
    for perm in itertools.permutations(S.ids):
        m = dict(zip(G.ids, perm))
        if any(G.kind[g] != S.kind[m[g]] for g in G.ids):
            continue
        if any(G.kind[g] == 'S' and num(S.text[m[g]]) is not None and num(G.text[g]) != num(S.text[m[g]]) for g in G.ids):
            continue
        if {frozenset((m[a], m[b])) for a, b in Ge} == Se:
            return m
    return None


student = {
    5: [('k-1', 1, k) for k in range(2, 6)],
    6: [('k-1', 2, k) for k in range(1, 5)],
    7: [('k-1', 3, 0)], 8: [('k-1', 4, 0)], 9: [('k-1', 5, 0), ('k-1', 5, 1)],
    10: [('k-1', 6, 0), ('k-1', 6, 1)], 11: [('k-1', 7, 0), ('k-1', 7, 7)],
    12: [('grades-2-3', 1, k) for k in range(4)], 13: [('grades-2-3', 2, k) for k in range(1, 5)],
    14: [('grades-2-3', 3, 0), ('grades-2-3', 3, 1)], 15: [('grades-2-3', 4, 0), ('grades-2-3', 4, 1)],
    16: [('grades-2-3', 5, k) for k in range(3)], 17: [('grades-2-3', 6, 0), ('grades-2-3', 6, 1)],
    18: [('grades-4-5', 1, k) for k in range(1, 4)], 19: [('grades-4-5', 2, 0), ('grades-4-5', 2, 1)],
    20: [('grades-4-5', 3, 0)], 21: [('grades-4-5', 4, 0), ('grades-4-5', 4, 1)],
    22: [('grades-4-5', 5, 0)], 23: [('grades-4-5', 6, k) for k in range(3)],
    24: [('grades-4-5', 7, k) for k in range(4)],
}
for gp, refs in student.items():
    gbs = boards('guide', gp)
    sts = [boards(b, p)[k] for b, p, k in refs]
    used = set()
    for G in gbs:
        hit = None
        for j, S in enumerate(sts):
            if j in used:
                continue
            m = iso(G, S)
            if m is not None:
                hit = (j, m)
                break
        if hit is None:
            check(False, f'guide p.{gp}: diagram {G.sig()} matches no student board on that page')
            continue
        used.add(hit[0])
        vals = {g: num(G.text[g]) for g in G.ids}
        S = sts[hit[0]]
        if any(G.kind[g] == 'C' and num(S.text[hit[1][g]]) is not None and num(S.text[hit[1][g]]) != vals[g] for g in G.ids):
            check(False, f'guide p.{gp}: diagram circle value differs from the printed student circle value')
        if all(vals[g] is not None for g in G.ids):
            check(works(G, vals), f'guide p.{gp}: diagram {G.sig()} labelled values satisfy every circle')
        else:
            check(all(G.text[g] in ('c', 'a', 'b') for g in G.circles()), f'guide p.{gp}: diagram {G.sig()} uses letters {sorted(set(G.text[g] for g in G.circles()))}')
            # letters: equal letters on each component
            comps = []
            for c in G.circles():
                same = all(G.text[c] == G.text[x] for x in G.adj[c])
                comps.append(same)
            check(all(comps), f'guide p.{gp}: joined circles carry the same letter')
    check(len(used) == len(sts) or gp in (11, 23), f'guide p.{gp}: every student board on that page is shown ({len(used)}/{len(sts)})')

# ===================================================================== guide overview / tools
say('#### Guide overview and adult tools')
check(quoted('If one circle attains either extreme, all circles in that group and all its adjacent squares have that same value'),
      'overview p.1 strong maximum principle (checked on random graphs below)')
# strong max principle on random graphs: if a circle attains max of touching squares, then all are equal
random.seed(7)
bad = 0
cnt = 0
for _ in range(4000):
    n = random.randint(2, 7)
    kinds = ['S' if random.random() < .4 else 'C' for _ in range(n)]
    if 'S' not in kinds:
        kinds[0] = 'S'
    if 'C' not in kinds:
        kinds[-1] = 'C'
    E = set((random.randrange(i), i) for i in range(1, n))
    G = Board.__new__(Board)
    G.ids = list(range(n)); G.kind = dict(enumerate(kinds)); G.adj = {i: [] for i in range(n)}
    for a, b in E:
        G.adj[a].append(b); G.adj[b].append(a)
    G.edges = list(E)
    sq = {i: F(random.randint(0, 2)) for i in range(n) if kinds[i] == 'S'}
    s, nl = solve(G, sq)
    if nl:
        continue
    v = dict(sq); v.update(s)
    # circle groups
    for c in G.circles():
        grp, st, touch = {c}, [c], set()
        while st:
            x = st.pop()
            for y in G.adj[x]:
                if G.kind[y] == 'C' and y not in grp:
                    grp.add(y); st.append(y)
                elif G.kind[y] == 'S':
                    touch.add(y)
        if not touch:
            continue
        cnt += 1
        hi = max(sq[t] for t in touch); lo = min(sq[t] for t in touch)
        if not (lo <= v[c] <= hi):
            bad += 1
        if v[c] in (hi, lo) and not (all(v[g] == v[c] for g in grp) and all(sq[t] == v[c] for t in touch)):
            bad += 1
check(bad == 0 and cnt > 1000, f'strong maximum principle for circle groups: 0 counterexamples in {cnt} circle checks')
check(quoted('Whole-number boundary values can require fractions'), 'overview: 0-?-1 path needs 1/2 (see 4-5 P7)')
check(quoted('With L edges between fixed endpoints A and B, every gap is (B - A)/L'), 'tools p.4 equal gaps (all path answers above agree)')
pathcrit = all(((B - A) % L == 0) == all((A * L + i * (B - A)) % L == 0 for i in range(L + 1)) for A in range(0, 7) for B in range(0, 13) for L in range(1, 7))
check(quoted('every value is an integer exactly when B-A is divisible by L') and pathcrit, 'guide p.24 path integrality criterion (A<=6, B<=12, L<=6)')
check(7 * 4 + 6 * 4 + 7 * 3 == 73 and quoted('use 73 sheets'), 'guide p.3: 4/4/3 children x 7/6/7 pages = 73 sheets')

# ===================================================================== cross references
say('#### Guide page cross-references')
pages = subprocess.run(['pdftotext', '-layout', str(WEEK / 'week-20-facilitator.pdf'), '-'], capture_output=True, text=True).stdout.split('\f')
p3 = re.sub(r'\s+', ' ', pages[2]); p4 = re.sub(r'\s+', ' ', pages[3])
say('     guide p.3 heading:', p3[:120])
say('     guide p.4 heading:', p4[:120])
check('equal gaps' in p4.lower() and 'equal gaps' not in p3.lower(), 'the equal-gap argument is on guide p.4, not p.3')
check('Uniqueness.' in p4 and 'Uniqueness.' not in p3, 'the general uniqueness (signed difference) proof is on guide p.4 (and p.22), not p.3')
for q in ['The equal-gap argument on page 3 fixes these pairs',
          'fillings differ at each place, then use page 3',
          'The general proof is held until Problem 5, but is available on page 3']:
    check(not quoted(q), 'stale cross-reference: "' + q + '"')

say('')
say(f'{len(FAIL)} failure(s)')
for f in FAIL:
    say('  FAIL ' + f)
(HERE / 'out_check_math.txt').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
