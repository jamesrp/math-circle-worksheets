#!/usr/bin/env python3
"""Week 72 independent math check (review stage).

Recomputes every answer on the student packet and every number, construction
and general claim in the adult guide from the stated robot rules alone:
E/W move one column, N/S one row; N adds the current column to memory, S
subtracts it.  Then reads the delivered guide PDF and compares its printed
answers with the computation.  Does not import or run any checker from the
source package.
"""
import itertools, random, re, sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
GUIDE = REPO / 'lowell-math-circle-year-2/week-72/week-72-facilitator.pdf'
STUD = REPO / 'lowell-math-circle-year-2/week-72/week-72-students.pdf'

fails = []
n_checks = 0
def check(cond, msg):
    global n_checks
    n_checks += 1
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        fails.append(msg)

STEP = {'E': (1, 0), 'W': (-1, 0), 'N': (0, 1), 'S': (0, -1)}

def walk(word, start=(0, 0), z=0):
    """Return list of states (x,y,z) after each prefix, including the start."""
    x, y = start
    out = [(x, y, z)]
    for c in word:
        dx, dy = STEP[c]
        if c == 'N':
            z += x          # add the column number (column before = after)
        elif c == 'S':
            z -= x
        x += dx; y += dy
        out.append((x, y, z))
    return out

def final(word, start=(0, 0)):
    return walk(word, start)[-1]

def vertical_memories(word, start=(0, 0)):
    st = walk(word, start)
    return [st[i + 1][2] for i, c in enumerate(word) if c in 'NS']

def shoelace(pts):
    a = Fraction(0)
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        a += Fraction(x1 * y2 - x2 * y1, 2)
    return a

def winding_area(word, start=(0, 0)):
    """Sum over unit squares of winding number (algebraic area) of a closed word."""
    st = walk(word, start)
    pts = [(s[0], s[1]) for s in st]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    tot = 0
    for cx in range(min(xs), max(xs)):
        for cy in range(min(ys), max(ys)):
            px, py = cx + 0.5, cy + 0.5
            w = 0
            for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
                if x1 == x2 and x1 > px:              # vertical edge to the right
                    if y1 < py < y2: w += 1
                    elif y2 < py < y1: w -= 1
            tot += w
    return tot

# ---------------- group law ----------------
def mul(g, h):
    x, y, z = g; a, b, c = h
    return (x + a, y + b, z + c + x * b)
def mat(g):
    x, y, z = g
    return ((1, x, z), (0, 1, y), (0, 0, 1))
def mmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
GEN = {'E': (1, 0, 0), 'W': (-1, 0, 0), 'N': (0, 1, 0), 'S': (0, -1, 0)}

R = range(-2, 3)
elems = [(x, y, z) for x in R for y in R for z in R]
check(all(mat(mul(g, h)) == mmul(mat(g), mat(h)) for g in elems for h in elems),
      'law (x,y,z)(a,b,c)=(x+a,y+b,z+c+xb) is matrix multiplication (125^2 pairs)')
small = [(x, y, z) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)]
check(all(mul(mul(g, h), k) == mul(g, mul(h, k)) for g in small for h in small for k in small),
      'associativity on 27^3 triples')
ok = all(mul(g, h) == walk(c, (g[0], g[1]), g[2])[-1] for g in elems for c, h in GEN.items())
check(ok, 'right multiplication by E/W/N/S generators reproduces the printed card rules')
check(all(mul(g, (0, 0, k)) == mul((0, 0, k), g) for g in elems for k in range(-3, 4)),
      'states (0,0,k) are central')
check(all(mul(g, (-g[0], -g[1], -g[2] + g[0] * g[1])) == (0, 0, 0) for g in elems),
      'inverse (-x,-y,-z+xy) (MATHEMATICS.md)')

# symmetric (exponential) coordinates t = z - xy/2
def symmul(g, h):
    x, y, t = g; a, b, s = h
    return (x + a, y + b, t + s + Fraction(x * b - y * a, 2))
def to_sym(g):
    return (g[0], g[1], g[2] - Fraction(g[0] * g[1], 2))
check(all(to_sym(mul(g, h)) == symmul(to_sym(g), to_sym(h)) for g in elems for h in elems),
      'guide p3: t=z-xy/2 turns the law into t+s+(xb-ya)/2')

# ---------------- launch example ----------------
st = walk('EENE')
check(st[2] == (2, 0, 0) and st[3] == (2, 1, 2) and st[4] == (3, 1, 2),
      f'p1 / guide p1 EENE example: EE->(2,0) m0, EEN->(2,1) m2, EENE->(3,1) m2 [{st[2:]}]')
check(final('EN') == (1, 1, 1) and final('NE') == (1, 1, 0), 'guide p1: EN memory 1, NE memory 0 at (1,1)')
check(walk('N', (-2, 0))[-1][2] == -2 and walk('NS', (-2, 0))[-1][2] == 0,
      'guide p2: at column -2, N takes 0 to -2, S returns to 0')

# ---------------- Problem 1 ----------------
routes = sorted(set(''.join(p) for p in itertools.permutations('EENN')))
mem1 = {r: final(r) for r in routes}
print('P1 routes:', {r: mem1[r][2] for r in routes})
check(len(routes) == 6, 'P1: exactly 6 distinct routes')
check(all(m[:2] == (2, 2) for m in mem1.values()), 'P1: all routes end at the ring (2,2)')
check(sorted(m[2] for m in mem1.values()) == [0, 1, 2, 2, 3, 4], 'P1: memories 0,1,2,2,3,4')
check(len({m[2] for m in mem1.values()}) == 5, 'P1: five different memories')
guide_p1 = {'EENN': 4, 'ENEN': 3, 'ENNE': 2, 'NEEN': 2, 'NENE': 1, 'NNEE': 0}
check(all(mem1[r][2] == v for r, v in guide_p1.items()), 'guide P1 table matches')
pos = [''.join('E' if i in c else 'N' for i in range(1, 5)) for c in [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]]
check(pos == list(guide_p1), 'guide P1: E-positions 12..34 give the six words in table order')
check(max(abs(s[0]) for r in routes for s in walk(r)) <= 3, 'P1 routes stay on the printed 0..3 board')

# ---------------- Problem 2 ----------------
orders = [''.join(p) for p in itertools.permutations('ENWS')]
fin2 = [final(o) for o in orders]
check(len(set(orders)) == 24, 'P2: 24 orders of four distinct cards')
check(all(f[:2] == (0, 0) for f in fin2), 'P2: every order returns to O')
cnt = Counter(f[2] for f in fin2)
print('P2 distribution:', dict(sorted(cnt.items())))
check(set(cnt) == {-1, 0, 1}, 'P2: possible memories exactly -1,0,1')
check((cnt[-1], cnt[0], cnt[1]) == (4, 16, 4), 'guide P2: counts 4,16,4')
check(final('NESW')[2] == -1 and final('EWNS')[2] == 0 and final('ENWS')[2] == 1, 'guide P2 witnesses')
colsets_ok = all(
    ({s[0] for s in walk(o)} <= {0, 1}) if o.index('E') < o.index('W') else ({s[0] for s in walk(o)} <= {-1, 0})
    for o in orders)
check(colsets_ok, 'guide P2: visited columns in {0,1} or {-1,0} by first horizontal move')
check(all(abs(s[0]) <= 1 and abs(s[1]) <= 1 for o in orders for s in walk(o)), 'P2 routes fit the -2..2 board')

# ---------------- Problem 3 ----------------
# Outlines taken from students.tex (check_diagrams.py re-reads them from the PDF).
def loop_words(corners):
    """Unit-step words around a lattice polygon given by corners from the dot, both directions."""
    def unit(pts):
        w = ''
        for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
            dx, dy = x2 - x1, y2 - y1
            n = abs(dx) + abs(dy)
            c = 'E' if dx > 0 else 'W' if dx < 0 else 'N' if dy > 0 else 'S'
            w += c * n
        return w
    rev = [corners[0]] + corners[:0:-1]
    return unit(corners), unit(rev)
P3 = {
    'rect a=0':  [(0, 0), (2, 0), (2, 1), (0, 1)],
    'rect a=2':  [(2, 0), (4, 0), (4, 1), (2, 1)],
    'rect a=-3': [(-3, 0), (-1, 0), (-1, 1), (-3, 1)],
    'L':         [(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)],
}
for name, cs in P3.items():
    w1, w2 = loop_words(cs)
    f1, f2 = final(w1, cs[0]), final(w2, cs[0])
    A = shoelace(cs)
    print(f'P3 {name}: {w1} -> {f1[2]}, {w2} -> {f2[2]}, shoelace {A}')
    check(f1[:2] == cs[0] and f2[:2] == cs[0], f'P3 {name}: both walks return to the dot')
    check(f1[2] == A and f2[2] == -A, f'P3 {name}: memories = +/- signed area {A}')
    # starting at any vertex of the loop gives the same memory (rotation invariance)
    rots = {final(w1[i:] + w1[:i], walk(w1, cs[0])[i][:2])[2] for i in range(len(w1))}
    check(rots == {A}, f'P3 {name}: same memory from every starting point on the loop')
check(final('EENWWS')[2] == 2 and final('NEESWW')[2] == -2, 'guide P3: EENWWS +2, reverse -2')
check(final('EENWNWSS')[2] == 3 and final('EENWNWSS')[:2] == (0, 0), 'guide P3: L route EENWNWSS gives 3')
vm = [(c, walk('EENWNWSS')[i][0]) for i, c in enumerate('EENWNWSS') if c in 'NS']
check(vm == [('N', 2), ('N', 1), ('S', 0), ('S', 0)], f'guide P3: L up-steps on columns 2,1, down-steps on column 0 {vm}')
check([final('EENWWS', (a, 0))[2] for a in (0, 2, -3)] == [2, 2, 2], 'guide P3: 2-0, 4-2, (-1)-(-3) all 2')

# ---------------- Problem 4 ----------------
for word, want, seq in [('EEEENWNW', 7, [4, 7]), ('NNNENESS', -3, [0, 0, 0, 1, -1, -3])]:
    st = walk(word)
    check(st[-1] == (2, 2, want), f'guide P4: {word} ends at (2,2) with memory {want}')
    check(vertical_memories(word) == seq, f'guide P4: {word} vertical-move memories {seq}')
    check(all(-1 <= s[0] <= 4 and -1 <= s[1] <= 4 for s in st), f'guide P4: {word} stays on printed -1..4 board')
    check(all(-10 <= s[2] <= 10 for s in st), f'guide P4: {word} stays on the -10..10 strip')
    check(all(word.count(c) <= 8 for c in 'ENWS') and len(word) == 8, f'guide P4: {word} uses 8 moves, <=8 cards of each kind')
check(walk('NNNEN')[-1] == (1, 4, 1), 'guide P4: after NNNEN at (1,4) memory 1')
okk = True
for k in range(-60, 61):
    w = ('ENWS' * k if k > 0 else 'NESW' * (-k)) + 'NNEE'
    st = walk(w)
    if st[-1] != (2, 2, k): okk = False
    if not all(0 <= s[0] <= 2 and 0 <= s[1] <= 2 for s in st): okk = False
    if any(s[:2] == (2, 2) for s in st[:-1]): okk = False
check(okk, 'guide P4 uniform plan: every k in -60..60 reaches (2,2) with memory k, stays in 0..2 square, first reaches ring at end')
check(final('NNEE') == (2, 2, 0), 'NNEE adds 0')

# shortest routes, for information (guide does not claim shortness)
from collections import deque
def shortest(target, box=None):
    seen = {(0, 0, 0): ''}
    dq = deque([(0, 0, 0)])
    while dq:
        s = dq.popleft()
        if s == target: return seen[s]
        if len(seen[s]) >= 12: continue
        for c in 'ENWS':
            x, y, z = s
            nz = z + (x if c == 'N' else -x if c == 'S' else 0)
            t = (x + STEP[c][0], y + STEP[c][1], nz)
            if box and not (box[0] <= t[0] <= box[1] and box[0] <= t[1] <= box[1]): continue
            if abs(nz) > 30: continue
            if t not in seen:
                seen[t] = seen[s] + c; dq.append(t)
    return None
for k in (7, -3):
    s = shortest((2, 2, k))
    print(f'info: a shortest route to (2,2) with memory {k}: {s} (length {len(s)})')

# ---------------- general claims (finite confirmation) ----------------
words = [''.join(p) for L in range(0, 9) for p in itertools.product('ENWS', repeat=L)]
closed = [w for w in words if final(w)[:2] == (0, 0)]
print('words length<=8:', len(words), 'closed:', len(closed))
check(all(final(w)[2] == winding_area(w) for w in closed),
      'closed words <=8: memory = algebraic area (sum of winding numbers), incl. self-crossing/repeated')
def is_simple(w):
    pts = [s[:2] for s in walk(w)]
    return len(set(pts[:-1])) == len(pts) - 1 and len(w) > 0
simple = [w for w in closed if is_simple(w)]
check(all(final(w)[2] == shoelace([s[:2] for s in walk(w)][:-1]) for w in simple),
      f'{len(simple)} simple closed words <=8: memory = shoelace signed area (CCW +)')
rng = random.Random(72)
check(all(final(w, (h, v))[2] == final(w)[2] for w in closed for h, v in [(rng.randint(-9, 9), rng.randint(-9, 9))]),
      'closed words <=8: translation leaves memory unchanged')
# compare with shoelace of path+chord polygon for open words (area of path closed by chord)
check(all(shoelace([s[:2] for s in walk(w)]) == final(w)[2] - Fraction(final(w)[0] * final(w)[1], 2)
          for w in words if final(w)[:2] != (0, 0) and len(w) <= 7),
      'open words <=7: signed area of path + straight chord = z - xy/2 (guide p1 convention)')
z, = [final('EENN')[2]]
check(z == 4 and z - Fraction(2 * 2, 2) == 2, 'guide p3: EENN memory 4, symmetric height 2')
check(final('ENWSENWS')[2] == 2, 'guide p3: two identical unit loops remember 2')
check(final('NESW')[2] == -1 and final('ENWS')[2] == 1 and
      [s[:2] for s in walk('NESW')] == [s[:2] for s in walk('ENWS')][::-1], 'NESW is ENWS walked backward')
check(sum(4 ** L for L in range(8)) == 21845 and sum(1 for w in words if len(w) <= 7 and final(w)[:2] == (0, 0)) == 441,
      'MATHEMATICS.md: 21,845 words of length <=7, 441 closed')

# ---------------- guide text vs computation ----------------
try:
    import pymupdf as fitz
except ImportError:
    import fitz
gtext = ' '.join(fitz.open(GUIDE)[i].get_text() for i in range(3))
g = re.sub(r'\s+', ' ', gtext).replace('−', '-')
check('There are six distinct routes' in g and 'five different possible memories' in g, 'guide text: P1 six routes, five memories')
m = re.search(r'EENN ENEN ENNE NEEN NENE NNEE ([\d ]+)', g)
check(m is not None and m.group(1).split()[:6] == ['4', '3', '2', '2', '1', '0'], 'guide text: P1 table values 4 3 2 2 1 0')
check('Exactly -1, 0, +1 are possible' in g and 'NESW for -1, EWNS for 0, and ENWS for +1' in g
      and 'counts are 4, 16, 4' in g, 'guide text: P2 answer, witnesses, counts')
check('+2 counterclockwise, -2 clockwise' in g and '+3 counterclockwise, -3 clockwise' in g, 'guide text: P3 answers')
check('7 EEEENWNW 4, then 7' in g and '-3 NNNENESS 0, 0, 0, 1, -1, -3' in g, 'guide text: P4 table')
check('ticks are 7.2 mm apart' in g and 'cards are 1.8 cm square' in g and '32 move cards' in g, 'guide text: apparatus sizes quoted')
stext = re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in fitz.open(STUD))).replace('−', '-')
check('EENE: memory 2' in stext and 'EEN: memory 2' in stext and 'EE: memory 0' in stext, 'student p1: example captions')
check('memory 7' in stext and 'memory -3' in stext, 'student p4: targets 7 and -3')

print(f'\n{n_checks} checks, {len(fails)} failures')
sys.exit(1 if fails else 0)
