#!/usr/bin/env python3
"""Independent mathematical checks for Week 85 (Drawing machines, a pantograph).

Written for the math-check stage of the review. It does not import or run the
package's own check_math.py or generate.py: task coordinates are read from
generate.py as literal data with ast (nothing is executed), and the mat
geometry (anchors, zones, F and L outlines) is transcribed below and confirmed
against the delivered PDFs by check_diagrams.py.

What it checks
- The linkage from first principles: for an anchor O and a tracer position T,
  every configuration of the six-bar machine is found by circle intersections
  (not the author's pose()). On the open parallelogram branch P = 2T - O; the
  only other configurations with 0 < |OT| < 160 put P on O (long bars folded
  together). The fold branch T = Q, where O, T, P are not collinear, needs
  |OT| = 160 exactly. Also checked on random poses parameterised by the two
  long-bar angles.
- Reachability: every tracer position the tasks need (inputs, inverses of the
  outputs, both anchors, the moved M) is inside 0 < |OT| < 160 with margin; the
  rhombus angle stays well away from flat; every joint of both mirror poses
  stays on a 450 x 400 mm board centred on the joined mat.
- Every copy (A, B, C, E, G, H, I, J, K, M, D dots) lands where the guide says
  and inside the zone the page uses; segment lengths of A and C; the inverse
  positions of D and E; F's inverse rectangle; L's forward rectangle;
  J and K halved.
- Areas by the shoelace formula and by exact unit-cell covering (whole squares
  plus half-squares), and kit sufficiency (48 squares, 16 triangles).
- Upper Problem 4: copy shift under the anchor change and the unique
  compensating translation, and that the moved M stays in the T zone.

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
import ast
import math
import random
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-85'
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    if cond:
        say('  ok  ', msg)
    else:
        say('  FAIL', msg)
        FAIL.append(msg)


# ---------------------------------------------------------------- data
def literal(name):
    tree = ast.parse((SRC / 'student' / 'generate.py').read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, 'id', None) == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise SystemExit('no literal ' + name)


INPUTS = literal('INPUTS')
OUTPUTS = literal('OUTPUTS')
DOTS = literal('DOTS')

L = 80                      # half-bar length (mm)
O = (40, 140)               # anchor, mat mm (materials p3)
O2 = (60, 140)              # second anchor O'
TZONE = (110, 115, 160, 165)        # inner dashed square, x0 y0 x1 y1
INCORNERS = (100, 105, 170, 175)    # input insert corners (70 x 70)
OUTCORNERS = (180, 90, 290, 190)    # output target corners (110 x 100)
F_RECT = (220, 125, 260, 155)       # F's small solid box, mat mm
L_RECT = (125, 130, 155, 150)       # L's small solid box, mat mm
MAT = (0, 0, 431.8, 279.4)
BOARD = (MAT[2] / 2 - 225, MAT[3] / 2 - 200, MAT[2] / 2 + 225, MAT[3] / 2 + 200)


def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def mul(k, a): return (k * a[0], k * a[1])
def norm(a): return math.hypot(*a)
def dist(a, b): return norm(sub(a, b))
def fwd(T, A=O): return (2 * T[0] - A[0], 2 * T[1] - A[1])           # P = 2T - A
def inv(P, A=O): return (Fr(P[0] + A[0], 2), Fr(P[1] + A[1], 2))     # T = (P + A)/2
def inside(p, box, eps=1e-9): return box[0] - eps <= p[0] <= box[2] + eps and box[1] - eps <= p[1] <= box[3] + eps


def circ(c1, r1, c2, r2):
    """Intersection points of two circles (list of 0, 1 or 2 points)."""
    d = dist(c1, c2)
    if d > r1 + r2 + 1e-12 or d < abs(r1 - r2) - 1e-12 or d == 0:
        return []
    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h = math.sqrt(max(r1 * r1 - a * a, 0.0))
    ex = mul(1 / d, sub(c2, c1))
    m = add(c1, mul(a, ex))
    if h < 1e-12:
        return [m]
    n = (-ex[1], ex[0])
    return [add(m, mul(h, n)), add(m, mul(-h, n))]


def configurations(A, T):
    """All poses of the machine with anchor A and tracer T.

    Bars: A-X-Q rigid with AX = XQ = L; Q-Y-P rigid with QY = YP = L;
    X-T and T-Y of length L. X lies on circle(A, L) and circle(T, L); then
    Q = 2X - A; Y lies on circle(Q, L) and circle(T, L); then P = 2Y - Q.
    """
    res = []
    for X in circ(A, L, T, L):
        Q = sub(mul(2, X), A)
        for Y in circ(Q, L, T, L):
            P = sub(mul(2, Y), Q)
            res.append(dict(O=A, X=X, Q=Q, Y=Y, T=T, P=P))
    return res


def collinear(a, b, c, tol=1e-6):
    u, v = sub(b, a), sub(c, a)
    return abs(u[0] * v[1] - u[1] * v[0]) <= tol * max(1.0, norm(u) * norm(v))


def area(poly):
    pts = poly[:-1] if poly[0] == poly[-1] else poly
    s = 0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        s += Fr(x1) * Fr(y2) - Fr(x2) * Fr(y1)
    return abs(s) / 2


def point_in_poly(p, poly):
    pts = poly[:-1] if poly[0] == poly[-1] else poly
    x, y = p
    c = False
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xi > x:
                c = not c
    return c


def unit_cover(poly, unit=10):
    """Cover a polygon by the 10 mm grid through its first vertex.

    Returns (whole squares, half-square triangles) if every grid cell is
    fully inside, fully outside, or cut exactly along one diagonal into two
    halves; otherwise None. Cell membership is tested on 5 x 5 interior
    sample points.
    """
    pts = poly[:-1] if poly[0] == poly[-1] else poly
    ox, oy = pts[0]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    whole = halves = 0
    for i in range(int((min(xs) - ox) // unit) - 1, int((max(xs) - ox) // unit) + 1):
        for j in range(int((min(ys) - oy) // unit) - 1, int((max(ys) - oy) // unit) + 1):
            x0, y0 = ox + i * unit, oy + j * unit
            samp = [(x0 + unit * (a + .5) / 5, y0 + unit * (b + .5) / 5) for a in range(5) for b in range(5)]
            ins = [point_in_poly(s, pts) for s in samp]
            if all(ins):
                whole += 1
            elif not any(ins):
                continue
            else:
                # exactly a half along a diagonal?
                d1 = all(ins[k] == ((samp[k][0] - x0) + (samp[k][1] - y0) < unit) for k in range(25))
                d1b = all(ins[k] == ((samp[k][0] - x0) + (samp[k][1] - y0) > unit) for k in range(25))
                d2 = all(ins[k] == ((samp[k][0] - x0) < (samp[k][1] - y0)) for k in range(25))
                d2b = all(ins[k] == ((samp[k][0] - x0) > (samp[k][1] - y0)) for k in range(25))
                if d1 or d1b or d2 or d2b:
                    halves += 1
                else:
                    return None
    return whole, halves


def seglens(path):
    return [dist(a, b) for a, b in zip(path, path[1:])]


# ---------------------------------------------------------------- 1. linkage
say('1. Linkage from first principles (circle intersections, L = 80 mm)')
random.seed(85)
bad_open = bad_other = 0
n_open = n_other = 0
for _ in range(20000):
    r = random.uniform(1, 159)
    th = random.uniform(-math.pi, math.pi)
    T = (O[0] + r * math.cos(th), O[1] + r * math.sin(th))
    for c in configurations(O, T):
        lens_ok = all(abs(dist(c[a], c[b]) - L) < 1e-7 for a, b in
                      [('O', 'X'), ('X', 'Q'), ('Q', 'Y'), ('Y', 'P'), ('X', 'T'), ('T', 'Y')])
        assert lens_ok
        is_par = dist(c['X'], c['Y']) > 1e-6       # X != Y: open frame
        if is_par:
            n_open += 1
            # parallelogram XQYT: X + Y = Q + T
            if dist(add(c['X'], c['Y']), add(c['Q'], c['T'])) > 1e-6 or dist(c['P'], fwd(T)) > 1e-6:
                bad_open += 1
        else:
            n_other += 1
            if dist(c['P'], O) > 1e-6:
                bad_other += 1
check(bad_open == 0 and n_open == 40000,
      f'open frame: every one of {n_open} poses (2 mirror poses for each of 20000 random T with 1<|OT|<159) is a parallelogram with P = 2T - O')
check(bad_other == 0 and n_other == 40000,
      f'the only other poses for such T ({n_other}) have Y = X and P on O (long bars folded together): O, T, P still on one line')

# Parameterise instead by the two long-bar directions: T must be on circle(X,L) and circle(Y,L),
# so T = Q (fold branch) or T = X + Y - Q (open branch).
fold_noncol = 0
fold_r = []
open_bad = 0
for _ in range(20000):
    a, b = random.uniform(-math.pi, math.pi), random.uniform(-math.pi, math.pi)
    Q = (O[0] + 2 * L * math.cos(a), O[1] + 2 * L * math.sin(a))
    P = (Q[0] + 2 * L * math.cos(b), Q[1] + 2 * L * math.sin(b))
    X, Y = mul(.5, add(O, Q)), mul(.5, add(Q, P))
    Topen = sub(add(X, Y), Q)
    if dist(P, fwd(Topen)) > 1e-6:
        open_bad += 1
    fold_r.append(dist(O, Q))
    if not collinear(O, Q, P):
        fold_noncol += 1
check(open_bad == 0, 'long-bar parameterisation: open branch T = X + Y - Q always gives P = 2T - O')
check(fold_noncol > 19000 and max(abs(r - 160) for r in fold_r) < 1e-9,
      f'fold branch T = Q breaks collinearity in {fold_noncol}/20000 random poses, but always has |OT| = 160 exactly')
say('     Branches meet only where T = Q = X + Y - Q (Q the midpoint of OP: full extension, |OT| = 160)')
say('     or X = Y (P on O). So with |OT| < 160 and P off O, no pose breaks O, T, P collinearity.')

# ---------------------------------------------------------------- 2. data and zones
say('')
say('2. Task coordinates (read from generate.py as data)')
for k, v in INPUTS.items():
    say(f'     input {k}: {v}')
for k, v in OUTPUTS.items():
    say(f'     output {k}: {v}')
say(f'     D dots: {DOTS}')
check(all(inside(p, TZONE) for v in INPUTS.values() for p in v), 'every input vertex A, B, C, G, H, I, M is inside the T zone 110..160 x 115..165')
check(all(inside(p, OUTCORNERS) for v in OUTPUTS.values() for p in v) and all(inside(p, OUTCORNERS) for p in DOTS),
      'every output vertex E, J, K and every D dot is inside the 110 x 100 output target')
img = (2 * TZONE[0] - O[0], 2 * TZONE[1] - O[1], 2 * TZONE[2] - O[0], 2 * TZONE[3] - O[1])
check(img == (180, 90, 280, 190), f'the T zone doubled about O is {img}, inside the output target {OUTCORNERS}')

# ---------------------------------------------------------------- 3. shared packet
say('')
say('3. Shared packet')
say('   Problem 1 (A, B, C traced by T; P draws)')
for k in 'ABC':
    cp = [fwd(p) for p in INPUTS[k]]
    check(all(inside(p, OUTCORNERS) for p in cp), f'{k} copy {cp} lies inside the output zone')
    l1, l2 = seglens(INPUTS[k]), seglens(cp)
    check(all(abs(b - 2 * a) < 1e-9 for a, b in zip(l1, l2)), f'{k} segment lengths {[round(x, 2) for x in l1]} -> {[round(x, 2) for x in l2]} (x2)')
check([round(x, 6) for x in seglens(INPUTS['A'])] == [35, 20], "guide: 'In A, 35 mm then 20 mm becomes 70 mm then 40 mm'")
check([round(x, 6) for x in seglens(INPUTS['C'])] == [10, 15, 20, 25, 10], "guide: C segments 10,15,20,25,10 mm become 20,30,40,50,20")
# orientation of B preserved (signed area same sign)
def signed(poly):
    pts = poly[:-1] if poly[0] == poly[-1] else poly
    return sum(Fr(x1) * y2 - Fr(x2) * y1 for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1])) / 2
check(signed(INPUTS['B']) * signed([fwd(p) for p in INPUTS['B']]) > 0, 'B: copy keeps orientation (signed area same sign, x4)')

say('   Problem 2 (D dots and E house, inverse control)')
tD = [inv(p) for p in DOTS]
guideD = [(115, 125), (130, 160), (155, 150), (150, 120), (125, 140)]
check(tD == guideD, f'D tracer positions {[(float(a), float(b)) for a, b in tD]} match the guide list in order')
check(all(inside(p, TZONE) for p in tD), 'all five D tracer positions are inside the T zone')
tE = [inv(p) for p in OUTPUTS['E']]
guideE = [(120, 125), (150, 125), (150, 145), (135, Fr(315, 2)), (120, 145), (120, 125)]
check(tE == guideE, f'E tracer vertices {[(float(a), float(b)) for a, b in tE]} match the guide')
check(all(inside(p, TZONE) for p in tE), 'E tracer outline inside the T zone')

say('   Problem 3 (rule for poses): see section 1; OT = TP and OP = 2 OT on the open branch')
for T in [(110, 115), (160, 165), (135, 140), (110, 165), (160, 115)]:
    for c in configurations(O, T):
        if dist(c['X'], c['Y']) > 1e-6:
            assert abs(dist(O, c['T']) - dist(c['T'], c['P'])) < 1e-9 and collinear(O, c['T'], c['P'])
check(True, 'OT = TP and collinear at the T-zone corners and centre (both mirror poses)')

say('   Problem 4 (stay inside F)')
Fin = (inv((F_RECT[0], F_RECT[1])), inv((F_RECT[2], F_RECT[3])))
check(Fin == ((130, Fr(265, 2)), (150, Fr(295, 2))), f'F (40 x 30) pulls back to the 20 x 15 tracer rectangle {[(float(a), float(b)) for a, b in Fin]}')
check(inside(Fin[0], TZONE) and inside(Fin[1], TZONE), 'that tracer rectangle is inside the T zone')
# the forward map is a bijection, so T-paths with copies inside F are exactly T-paths inside the pulled-back rectangle
random.seed(4)
ok = True
for _ in range(5000):
    T = (random.uniform(110, 160), random.uniform(115, 165))
    a = inside(fwd(T), F_RECT)
    b = inside(T, (130, 132.5, 150, 147.5))
    ok &= (a == b)
check(ok, 'random tracer points: copy inside F exactly when T is inside the 20 x 15 rectangle')

# ---------------------------------------------------------------- 4. upper packet
say('')
say('4. Upper packet')
say('   Problem 1: the six equal lengths and joined bars force P = 2T - O on the open branch (section 1);')
say('   with equal lengths alone, the fold pose T = Q (|OT| = 160) is the exception the page excludes by "open and uncrossed".')

say('   Problem 2 (areas of G, H, I and copies)')
pieces_needed = {}
for k, a0 in [('G', 4), ('H', 4), ('I', Fr(9, 2))]:
    poly = INPUTS[k]
    cp = [fwd(p) for p in poly]
    a1, a2 = area(poly) / 100, area(cp) / 100
    check(a1 == a0 and a2 == 4 * a0, f'{k}: area {a1} units, copy {a2} units (guide: {a0} and {4 * a0})')
    c1, c2 = unit_cover(poly), unit_cover(cp)
    check(c1 is not None and c2 is not None and c1[0] + Fr(c1[1], 2) == a1 and c2[0] + Fr(c2[1], 2) == a2,
          f'{k}: exact covering by 10 mm squares and half-squares: original {c1}, copy {c2} (whole, halves)')
    check(all(inside(p, OUTCORNERS) for p in cp), f'{k} copy lies inside the output zone')
    pieces_needed[k] = (c1[0] + c2[0], c1[1] + c2[1])
check(all(s <= 48 and t <= 16 for s, t in pieces_needed.values()),
      f'kit of 48 squares and 16 triangles covers one original and its copy at a time: needs {pieces_needed}')

say('   Problem 3 (reverse: P moves, T draws)')
for k in 'JK':
    t = [inv(p) for p in OUTPUTS[k]]
    l1, l2 = seglens(OUTPUTS[k]), seglens([(float(a), float(b)) for a, b in t])
    check(all(inside(p, TZONE) for p in t), f'{k} halved copy {[(float(a), float(b)) for a, b in t]} inside the T zone')
    check(all(abs(b - a / 2) < 1e-9 for a, b in zip(l1, l2)), f'{k} lengths halve: {[round(x, 2) for x in l1]} -> {[round(x, 2) for x in l2]}')
jt = [inv(p) for p in OUTPUTS['J']]
check((float(jt[0][0]), float(jt[0][1]), float(jt[2][0]), float(jt[2][1])) == (120, 125, 150, 145),
      "guide: J's 60 x 40 rectangle becomes 30 x 20 (at 120..150 x 125..145)")
Lp = (fwd((L_RECT[0], L_RECT[1])), fwd((L_RECT[2], L_RECT[3])))
check(Lp == ((210, 120), (270, 160)), f'L (30 x 20 at {L_RECT}) needs P on the 60 x 40 rectangle {Lp}')
check(inside(Lp[0], OUTCORNERS) and inside(Lp[1], OUTCORNERS), 'that P rectangle is inside the output zone')
check(Lp[0] != (200, 110), 'J itself (200..260 x 110..150) is not the answer: same size, 10 mm off in x and y')

say('   Problem 4 (anchor O -> O\')')
M = INPUTS['M']
c1 = [fwd(p, O) for p in M]
c2 = [fwd(p, O2) for p in M]
check(all(sub(b, a) == (-20, 0) for a, b in zip(c1, c2)), f'keeping M fixed, copy moves from {c1} to {c2}: 20 mm left')
Mn = [(x + 10, y) for x, y in M]
check([fwd(p, O2) for p in Mn] == c1, 'moving M 10 mm right puts the second copy exactly on the first')
# uniqueness: 2(T + s) - O' = 2T - O  <=>  s = (O' - O)/2
check(mul(.5, sub(O2, O)) == (10, 0), 'the compensating shift is unique: half the anchor shift, same direction')
check(all(inside(p, TZONE) for p in Mn), f'moved M {Mn} stays inside the T zone (touches x = 160)')
check(all(inside(p, OUTCORNERS) for p in c1 + c2), 'both copies inside the output zone')

# ---------------------------------------------------------------- 5. reach, frame shape, board
say('')
say('5. Reach and support (ideal geometry; not a hardware test)')
need = []
need += [(O, p, 'input ' + k) for k, v in INPUTS.items() for p in v]
need += [(O, (float(a), float(b)), 'D/E inverse') for a, b in tD + tE]
need += [(O, (float(a), float(b)), 'J/K halved') for k in 'JK' for a, b in (inv(p) for p in OUTPUTS[k])]
need += [(O, (float(a), float(b)), 'F inverse') for a, b in Fin]
need += [(O, p, 'L box') for p in [(125, 130), (155, 150), (125, 150), (155, 130)]]
need += [(O2, p, 'M with O\'') for p in M + Mn]
need += [(O, (x, y), 'T zone corner') for x in (110, 160) for y in (115, 165)]
rs = [dist(A, T) for A, T, _ in need]
check(min(rs) > 40 and max(rs) < 130, f'every needed tracer position has {min(rs):.1f} <= |OT| <= {max(rs):.1f} mm (singular at 0 and 160)')
angs = [math.degrees(2 * math.asin(r / 160)) for r in rs]
check(min(angs) > 45 and max(angs) < 110, f'rhombus angle at Q stays between {min(angs):.0f} and {max(angs):.0f} degrees (flat would be 0 or 180)')
ext = []
for A, T, _ in need:
    for c in configurations(A, T):
        if dist(c['X'], c['Y']) > 1e-6:
            ext += [c[n] for n in 'OXQYTP']
xs = [p[0] for p in ext]; ys = [p[1] for p in ext]
margin = 9 + 11   # half bar width plus bar end beyond the hole
check(min(xs) - margin >= BOARD[0] and max(xs) + margin <= BOARD[2] and min(ys) - margin >= BOARD[1] and max(ys) + margin <= BOARD[3],
      f'joint centres of both mirror poses span x {min(xs):.0f}..{max(xs):.0f}, y {min(ys):.0f}..{max(ys):.0f}; with 20 mm bar ends they stay on the board {tuple(round(v, 1) for v in BOARD)}')
say(f'     (the mat is y 0..279.4: Q leaves the paper in some poses, as the guide warns, but stays on the board)')

say('')
say(f'{len(FAIL)} failures')
text = '\n'.join(OUT)
print(text)
(HERE / 'check_math.py.out').write_text(text + '\n')
