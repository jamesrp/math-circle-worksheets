"""Independent mathematical check of the Week 37 bonus companion (Mirror twins).

Reads the drawing data from source/week-37-bonus/student/build.py (outline
polygons, tetrahedron points and red edge sets, corner arm directions) and
checks each printed question, each guide answer and the guide's kit arithmetic
by enumeration.  Nothing from the bonus's own verify.py is imported.

Run: python3 check_bonus.py   (writes check_bonus.out beside itself)
"""
import ast
import itertools
import math
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent


def find_repo():
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand and (cand / 'lowell-math-circle-year-2' / 'week-37').is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):
        if (p / 'lowell-math-circle-year-2' / 'week-37').is_dir():
            return p
    sys.exit('repository not found above ' + str(HERE))


REPO = find_repo()
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-37'
BSRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-37-bonus'
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def note(msg):
    say('NOTE ' + msg)


src = (BSRC / 'student' / 'build.py').read_text()
shapes = ast.literal_eval(re.search(r'^shapes=(\[.*\])$', src, re.M).group(1))

# ------------------------------------------------------------------ P1 outlines
say('== P1 flat outlines (F-like, equal-arm L, T) and their mirrors')


def congruences(P, Q):
    """All vertex correspondences (cyclic shift, either direction) under which
    polygon P maps onto polygon Q by an isometry; returns list of det signs."""
    n = len(P)
    if len(Q) != n:
        return []
    out = []
    for d in (1, -1):
        for s in range(n):
            idx = [(s + d * i) % n for i in range(n)]
            Q2 = [Q[i] for i in idx]
            # distances preserved?
            ok = all(abs(math.dist(P[i], P[j]) - math.dist(Q2[i], Q2[j])) < 1e-9
                     for i in range(n) for j in range(i + 1, n))
            if ok:
                a = np.array(P[1]) - np.array(P[0]); b = np.array(P[2]) - np.array(P[0])
                c = np.array(Q2[1]) - np.array(Q2[0]); e = np.array(Q2[2]) - np.array(Q2[0])
                s1 = np.sign(a[0] * b[1] - a[1] * b[0]); s2 = np.sign(c[0] * e[1] - c[1] * e[0])
                out.append(int(s1 * s2))
    return out


def area2(P):
    return sum(P[i][0] * P[(i + 1) % len(P)][1] - P[(i + 1) % len(P)][0] * P[i][1] for i in range(len(P)))


def inside(P, q):
    x, y = q
    c = False
    n = len(P)
    for i in range(n):
        (x1, y1), (x2, y2) = P[i], P[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            c = not c
    return c


names = ['F-like', 'L', 'T']
expect_face_up = [False, True, True]
for name, P, exp in zip(names, shapes, expect_face_up):
    M = [(-x, y) for x, y in P]            # the printed mirror (x -> -x)
    sym = congruences(P, P)
    rev = [s for s in sym if s < 0]
    cong = congruences(P, M)
    face_up = any(s > 0 for s in cong)
    flipped = any(s < 0 for s in cong)
    say(f'     {name}: {len(P)} corners, area {abs(area2(P)) / 2}, symmetries {len(sym)} '
        f'(orientation-reversing {len(rev)})')
    check(face_up == exp, f'P1 {name}: face-up slides/turns {"can" if face_up else "cannot"} match the mirror '
                          f'(guide: {"yes" if exp else "no"})')
    check(flipped, f'P1 {name}: turning a tile over matches it (yes for all three)')
    check((len(rev) > 0) == face_up, f'P1 {name}: face-up match iff the outline has a reflection symmetry')
    check(inside(P, (9, 9)) and inside(M, (-9, 9)), f'P1 {name}: face dot lies inside the tile and its mirror')
L = shapes[1]
arm = (max(x for x, _ in L) - min(x for x, _ in L), max(y for _, y in L) - min(y for _, y in L))
check(arm[0] == arm[1], f'P1 L arms are equal ({arm[0]} and {arm[1]}): its diagonal is a mirror line')
rot = sorted((-y, x) for x, y in L)
check(rot == sorted((-x, y) for x, y in L), 'P1 L: a face-up quarter turn carries L onto its mirror (guide)')
Tt = shapes[2]
xs = [x for x, _ in Tt]
check((min(xs) + max(xs)) / 2 == 9 and sorted((18 - x, y) for x, y in Tt) == sorted(Tt),
      'P1 T: stem and bar share the vertical axis x = 9, so the mirror is the same outline')

# ------------------------------------------------------------------ P2 edges
say('')
say('== P2 three red edges on a regular tetrahedron')
V = 'ABCD'
EDGES = [''.join(e) for e in itertools.combinations(V, 2)]


def parity(p):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s = -s
    return s


def image(red, p):
    m = dict(zip(V, p))
    return frozenset(''.join(sorted(m[a] + m[b])) for a, b in red)


def chiral(red):
    red = frozenset(red)
    return not any(image(red, p) == red and parity([V.index(c) for c in p]) < 0
                   for p in itertools.permutations(V))


def kind(red):
    deg = sorted((sum(v in e for e in red) for v in V), reverse=True)
    return {(3, 1, 1, 1): 'star', (2, 2, 2, 0): 'triangle', (2, 2, 1, 1): 'path'}.get(tuple(deg), str(deg))


allpat = [frozenset(c) for c in itertools.combinations(EDGES, 3)]
tally = {}
for r in allpat:
    k = (kind(r), chiral(r))
    tally[k] = tally.get(k, 0) + 1
say('     all 20 patterns (type, chiral): count =', tally)
check(tally == {('path', True): 12, ('star', False): 4, ('triangle', False): 4},
      '20 patterns: 12 paths (chiral), 4 stars and 4 triangles (achiral)')
check(all(sum(1 for p in itertools.permutations(V) if image(r, p) == r) == 2 for r in allpat if kind(r) == 'path'),
      'a three-edge path has exactly 2 vertex automorphisms (identity, reversal), both even')

reds = [set(ast.literal_eval(x)) for x in re.findall(r"\(\d+,(\{'[A-D]{2}','[A-D]{2}','[A-D]{2}'\})\)", src)]
check(len(reds) == 3, f'three printed patterns read from build.py: {[sorted(r) for r in reds]}')
exp = [('path', 'no'), ('star', 'yes'), ('triangle', 'yes')]
for r, (k_, a) in zip(reds, exp):
    check(kind(r) == k_ and (not chiral(r)) == (a == 'yes'),
          f'P2 {"/".join(sorted(r))}: {kind(r)}, mirror {"matches" if not chiral(r) else "cannot match"} (guide: {a})')
# guide edits
edits = [({'AB', 'BC', 'CD'}, 'CD', 'AC', 'triangle'), ({'AB', 'AC', 'AD'}, 'AD', 'CD', 'path'),
         ({'AB', 'AC', 'BC'}, 'AC', 'CD', 'path')]
for r, out_, in_, k_ in edits:
    new = (r - {out_}) | {in_}
    check(kind(new) == k_ and chiral(new) != chiral(r),
          f'guide edit {"/".join(sorted(r))}: move {out_} to {in_} gives {kind(new)} {"/".join(sorted(new))}, answer changes')
for r in reds:
    ch = sum(1 for o in r for i in set(EDGES) - r if chiral((r - {o}) | {i}) != chiral(r))
    say(f'     {kind(r)}: {ch} of 9 single-sleeve moves change the answer')

# geometry of the bonus tetrahedron drawing
pts_src = re.search(r"pts=\{'A':\(cx,cy\+(\d+)\),'B':\(cx-(\d+),cy-(\d+)\),'C':\(cx\+(\d+),cy-(\d+)\),'D':\(cx,cy\+(\d+)\)\}", src)
a_up, bx, by, cx_, cy_, d_up = map(int, pts_src.groups())
P = {'A': (0, a_up), 'B': (-bx, -by), 'C': (cx_, -cy_), 'D': (0, d_up)}
Lsq = (2 * bx) ** 2
za2 = Lsq - (bx ** 2 + (a_up + by) ** 2)          # depth of A relative to B, C
sols = []
for za in (math.sqrt(za2), -math.sqrt(za2)):
    A3 = np.array([0, a_up, za]); B3 = np.array([-bx, -by, 0.0]); C3 = np.array([bx, -by, 0.0])
    cen = (A3 + B3 + C3) / 3
    nrm = np.cross(B3 - A3, C3 - A3); nrm /= np.linalg.norm(nrm)
    h = math.sqrt(2 / 3) * 2 * bx
    for sgn in (1, -1):
        D3 = cen + sgn * h * nrm
        if D3[2] < min(A3[2], B3[2], C3[2]):       # behind the front face
            sols.append((za, D3))
say(f'     bonus tetra drawing: A(0,{a_up}) B(-{bx},-{by}) C({cx_},-{cy_}) D(0,{d_up}) pt')
for za, D3 in sols:
    say(f'     exact regular-tetrahedron D for that A, B, C (A depth {za:+.1f}): D at ({D3[0]:.1f},{D3[1]:.1f}),'
        f' printed D at (0,{d_up})')
best = min(abs(D3[1] - d_up) for _, D3 in sols)
note(f'bonus p2 tetrahedra are schematic, not exact orthographic views: D is {best:.0f} pt from the exact '
     f'position (edge 130 pt); far vertex still inside the front face, so the hidden-edge reading is unchanged')

# ------------------------------------------------------------------ P3 corners
say('')
say('== P3 right-angle corners')
E = np.eye(3)
PROPER = []
for p in itertools.permutations(range(3)):
    M = np.zeros((3, 3))
    for i in range(3):
        M[p[i], i] = 1
    if round(np.linalg.det(M)) == 1:
        PROPER.append(p)
check(len(PROPER) == 3, 'rotations taking the arm directions {+x,+y,+z} to themselves: the 3 cyclic ones')
# all 24 rotations of the signed axes, for completeness
signed = []
for p in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3))
        for i in range(3):
            M[p[i], i] = s[i]
        if round(np.linalg.det(M)) == 1:
            signed.append(M)
check(len(signed) == 24, '24 proper signed-axis rotations (cube rotation group)')


def corner_chiral(attr):
    """attr: arm identities on +x,+y,+z.  Mirror x<->y.  Chiral iff no rotation
    in the full rotation group maps the corner onto its mirror with identities kept."""
    arms = {tuple(E[i]): attr[i] for i in range(3)}
    mirror = {(0, 1, 0): attr[0], (1, 0, 0): attr[1], (0, 0, 1): attr[2]}
    for M in signed:
        img = {tuple(int(v) for v in M @ np.array(k)): a for k, a in arms.items()}
        if img == mirror:
            return False
    # any proper rotation at all (not only signed axes) must send the orthonormal arm frame
    # onto the mirror's; those are signed-axis maps, so the search is complete
    return True


cases = [(('R', 'B', 'G'), True, 'equal-length R/B/G: no mirror match'),
         (('R', 'R', 'G'), False, 'R/R/G: mirror matches'),
         (('R', 'G', 'R'), False, 'R/G/R (other placement of the pair): mirror matches'),
         (('R', 'R', 'R'), False, 'R/R/R: mirror matches'),
         ((30, 60, 90), True, 'one colour, lengths 30/60/90: no mirror match'),
         ((60, 60, 90), False, 'one colour, lengths 60/60/90: mirror matches (two equal lengths are not enough)')]
for attr, exp_c, msg in cases:
    check(corner_chiral(attr) == exp_c, 'P3 ' + msg)
# child certificate: G toward viewer, R to the right -> B up (original) / down (mirror)
for name, arms in [('original', {'R': (1, 0, 0), 'B': (0, 1, 0), 'G': (0, 0, 1)}),
                   ('mirror', {'R': (0, 1, 0), 'B': (1, 0, 0), 'G': (0, 0, 1)})]:
    g = np.array(arms['G'], float); r = np.array(arms['R'], float); b = np.array(arms['B'], float)
    up = np.cross(g, r)      # screen up = toward x right (right-handed: right x up = toward)
    say(f'     certificate, {name}: G toward viewer, R right -> B points {"up" if np.dot(b, up) > 0 else "down"}')
up_o = np.dot(np.array((0, 1, 0)), np.cross((0, 0, 1), (1, 0, 0)))
up_m = np.dot(np.array((1, 0, 0)), np.cross((0, 0, 1), (0, 1, 0)))
check(up_o > 0 and up_m < 0, 'guide certificate: B up in one model and down in the mirror')
# printed corner diagrams: three arms 120 degrees apart and equal = view along the cube diagonal
dirs = [(80, -80 / math.sqrt(3)), (-80, -80 / math.sqrt(3)), (0, 160 / math.sqrt(3))]
src_dirs = re.search(r'dirs=\[\(80,-80/math\.sqrt\(3\)\),\(-80,-80/math\.sqrt\(3\)\),\(0,160/math\.sqrt\(3\)\)\]', src)
lens = [math.hypot(*d) for d in dirs]
angs = sorted(math.degrees(math.atan2(d[1], d[0])) % 360 for d in dirs)
check(src_dirs is not None and max(lens) - min(lens) < 1e-9 and
      all(abs((angs[(i + 1) % 3] - angs[i]) % 360 - 120) < 1e-9 for i in range(3)),
      'P3 corner pictures: equal arms 120 degrees apart (exact view along the body diagonal)')
# the cube-corner sketch: orthographic?
phi, eps = math.radians(30), math.radians(25)
v = [(-35 * math.sin(phi), -35 * math.sin(eps) * math.cos(phi)), (35 * math.cos(phi), -35 * math.sin(eps) * math.sin(phi)),
     (0, 35 * math.cos(eps))]
G2 = sum(np.outer(x, x) for x in v) / 35 ** 2
check(np.allclose(G2, np.eye(2)), 'cube-corner sketch is an exact orthographic projection of three perpendicular arms')
check(re.search(r'if turn:dx,dy=-dy,dx', src) is not None,
      'the "whole-model turn" sketch is the three-arm sketch turned 90 degrees in the page (a legal rotation)')
note('a three-arm picture viewed along the diagonal cannot show whether the arms point toward or away from '
     'the eye, so a printed corner alone does not fix its handedness; the questions ask children to build '
     'a corner and its mirror, so no printed answer depends on reading it')

# ------------------------------------------------------------------ guide arithmetic
say('')
say('== Bonus guide kit arithmetic')
per_pair = dict(tiles=6, frames=2, red_edge=6, eq_corners=2, R=6, B=2, G=2, uneq=2, uneq_sleeves=6)
full = {k: 6 * v for k, v in per_pair.items()}
check(full == dict(tiles=36, frames=12, red_edge=36, eq_corners=12, R=36, B=12, G=12, uneq=12, uneq_sleeves=36),
      'six full pair kits: 36 tiles, 12 frames, 36 red edge sleeves, 12 corners with 36R/12B/12G, 12 unequal, 36 sleeves')
need = dict(R=6, B=2, G=2)   # max over RBG+mirror (2R2B2G), RRG+mirror (4R2G), RRR+mirror (6R)
check(max(2, 4, 6) == need['R'] and need['B'] == 2 and need['G'] == 2,
      'per pair 6 R, 2 B, 2 G arm sleeves cover RBG, RRG and RRR pairs')
outline_kits, corner_kits, complete_kits = 2 + 2 + 2, 2 + 2, 2
check((outline_kits * 6, complete_kits * 2, complete_kits * 6, corner_kits * 2, corner_kits * 6, corner_kits * 2,
       complete_kits * 2, complete_kits * 2 * 3) == (36, 4, 12, 8, 24, 8, 4, 12),
      'practical minimum: 36 tiles, 4 frames, 12 red edge sleeves, 8 corners, 24 R / 8 B / 8 G, '
      '4 unequal models (complete kits only), 12 sleeves')

# ------------------------------------------------------------------ PDF text
say('')
say('== Delivered bonus PDFs')
st = subprocess.run(['pdftotext', str(WEEK / 'week-37-bonus.pdf'), '-'], capture_output=True, text=True).stdout
nums = [int(n) for n in re.findall(r'Problem (\d+):', st)]
check(nums == [1, 2, 3], f'bonus problems numbered {nums}')
gt = ' '.join(subprocess.run(['pdftotext', str(WEEK / 'week-37-bonus-facilitator.pdf'), '-'],
                             capture_output=True, text=True).stdout.split())
for phrase in ['face-up answers are no, yes, yes', 'Answers are no, yes, yes',
               '12 are paths (chiral), four stars and four triangles (achiral)',
               'To change the path\'s answer move red CD to AC', 'Equal-length R/B/G: no mirror match',
               'B then points up in one model and down in the mirror']:
    check(phrase.replace("'", '’') in gt or phrase in gt, f'bonus guide says: "{phrase}"')
for t in ['Use each flat tile and its mirror twin', 'Build each edge pattern and its mirror',
          'Build a corner and its mirror with three different arm colors']:
    check(t in ' '.join(st.split()), f'student bonus text present: "{t}"')

say('')
say(f'{len(FAIL)} failure(s)')
(HERE / 'check_bonus.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
