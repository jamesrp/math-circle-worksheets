#!/usr/bin/env python3
"""Independent mathematical checks for Week 94 (Calibration lab).

Written for the math-check stage of the review. It does not import or run the
package's own check_math.py files. Exact arithmetic with fractions.Fraction.

What it checks
- Data are read from the student LaTeX sources where they are data (strip
  lengths from common.tex, ruler labels, the machine families, the report
  boxes), so a source change shows up here.
- K-1: strip lengths; every placement with one end at 7 and both ends on the
  printed ruler labels; every pair of supplied pieces covered by a third.
- Grades 2-3: every hidden pair for reports 7 and 10; the difference
  invariant; the three standard rows; the partner game for every extra and
  every supplied standard; every single-report repair of each box (searching
  report values, not reasoning about them); an exhaustive check that every
  invented one-wrong-report puzzle has exactly one repair.
- Grades 4-5: the 21-machine game (which single requests always identify,
  which supplied strips or end-to-end combinations do, lucky single reports);
  Problem 2 candidates and separating second strips; Problem 3 rules and
  uniqueness; Problem 4 every one-report repair; Problem 5 tables; Problem 6
  stretch ranges by an exact feasibility test plus a brute-force grid over true
  reports; Problem 7 worst-case width for every reference pair, with a grid
  over all displays consistent with a positive-stretch machine; one reference
  repeated.
- Guide: every numerical claim in the solutions, and the Problem 7 remark that
  "a true stretch of 2 with exact displays avoids truncation for every allowed
  separation at least 1".
- Geometry (needs PyMuPDF): the printed unit is 12 mm on every ruler, strip and
  unit row in all three student PDFs; strip lengths in units; example diagrams.

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import re

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
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-94'
PDF = REPO / 'lowell-math-circle-year-2' / 'week-94'
OUT, FAIL, NOTE = [], [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def note(msg):
    say('NOTE ' + msg)
    NOTE.append(msg)


common = (SRC / 'student' / 'common.tex').read_text()
k1 = (SRC / 'student' / 'k-1.tex').read_text()
mid = (SRC / 'student' / 'grades-2-3.tex').read_text()
up = (SRC / 'student' / 'grades-4-5.tex').read_text()
guide = (SRC / 'guide' / 'facilitator.tex').read_text()

# ------------------------------------------------------------ source data
m = re.search(r'\\foreach \\x/\\y/\\n/\\s in \{([^}]*)\}', common)
STRIPS = {}
for item in m.group(1).split(','):
    x, y, n, s = item.split('/')
    STRIPS[s] = int(n)
say('strip lengths from common.tex:', STRIPS)
check(STRIPS == {'A': 2, 'B': 3, 'C': 4, 'D': 6}, 'strips A,B,C,D are 2,3,4,6 units')
m = re.search(r'\\foreach\\i in\{0,\.\.\.,(\d+)\}\{\\draw\(\\i,0\) rectangle', common)
UNITROW = int(m.group(1)) + 1
check(UNITROW == 12, 'unit row has 12 squares')
m = re.search(r'\\draw\[line width=\.8pt\] \(0,0\)--\((\d+),0\);\\foreach \\i in \{0,\.\.\.,(\d+)\}', common)
RULER_SPAN = int(m.group(2))
offsets = set(int(v) for v in re.findall(r'\\ruler\{(\d+)\}', k1))
check(offsets == {2}, 'every K-1 ruler is \\ruler{2}')
LABELS = list(range(2, 2 + RULER_SPAN + 1))
say('K-1 ruler labels:', LABELS[0], '...', LABELS[-1])
check(LABELS == list(range(2, 15)), 'K-1 rulers are labelled 2..14')

# ------------------------------------------------------------ K-1
say('\n== K-1 ==')
# P1: length = number of unit intervals between the two end marks, any placement
for s, n in STRIPS.items():
    places = [(a, a + n) for a in LABELS if a + n in LABELS]
    check(all(b - a == n for a, b in places) and len(places) > 0,
          f'P1 strip {s}: every placement on the ruler spans {n} units ({len(places)} placements)')
# P2: one end at 7, both ends on printed labels
P2 = {s: sorted({tuple(sorted((7, 7 + d * n))) for d in (1, -1)
                 if 7 + d * n in LABELS}) for s, n in STRIPS.items()}
say('P2 placements with one end at 7:', P2)
check(P2 == {'A': [(5, 7), (7, 9)], 'B': [(4, 7), (7, 10)], 'C': [(3, 7), (7, 11)], 'D': [(7, 13)]},
      'P2: A 5-7/7-9, B 4-7/7-10, C 3-7/7-11, D 7-13 only (1-7 is off the ruler)')
# P3: one of each piece per pair (guide); also test with the 12-unit row as a cover
pieces = dict(STRIPS)
p3 = [(a, b, c) for a, b in combinations(pieces, 2) for c in pieces
      if c not in (a, b) and pieces[a] + pieces[b] == pieces[c]]
say('P3 two pieces covered exactly by a third:', p3)
check(p3 == [('A', 'C', 'D')], 'P3: only A+C covered by D')
sums = sorted(pieces[a] + pieces[b] for a, b in combinations(pieces, 2))
check(sums == [5, 6, 7, 8, 9, 10], 'P3: distinct-piece sums are 5,6,7,8,9,10 (guide lists 5,8,7,9,10 besides 6)')
check(UNITROW not in sums, 'P3: the 12-unit row is not the length of any pair, so it cannot be a third cover')
# with duplicates allowed (if a child used two printed copies)
dup = [(a, b, c) for a, b in combinations(list(pieces) + list(pieces), 2) for c in pieces
       if pieces[a] + pieces[b] == pieces[c]]
say('P3 if duplicate pieces were available:', sorted(set(tuple(sorted((a, b))) + (c,) for a, b, c in dup)))

# ------------------------------------------------------------ Grades 2-3
say('\n== Grades 2-3 ==')
m = re.search(r'secret extra number: ([0-9, or]+)\.', mid)
EXTRAS = [int(v) for v in re.findall(r'\d+', m.group(1))]
check(EXTRAS == [1, 2, 3, 4, 5, 6], 'extras are 1..6')
# P1: one known strip identifies the extra
for s, n in STRIPS.items():
    reps = [n + e for e in EXTRAS]
    check(len(set(reps)) == 6, f'P1: strip {s} alone identifies every extra (reports {reps})')
check(max(n + e for n in STRIPS.values() for e in EXTRAS) <= UNITROW, 'P1: every report fits on the 12-square row')
# P2: P reports 7, Q reports 10, same extra, positive whole lengths
P2m = [(p, q, e) for e in EXTRAS for p in range(1, 30) for q in range(1, 30) if p + e == 7 and q + e == 10]
say('P2 worlds (P, Q, extra):', P2m)
check(len(P2m) == 6, 'P2: exactly six pairs; page gives seven rows')
check(set(P2m) == {(6, 9, 1), (5, 8, 2), (4, 7, 3), (3, 6, 4), (2, 5, 5), (1, 4, 6)}, 'P2 matches guide table')
check(max(q for p, q, e in P2m) <= 12, 'P2: every length buildable with 12 cubes')
# P3
check(all(q - p == 3 for p, q, e in P2m), 'P3: Q is always exactly 3 longer; P never longer')
# P4
rows = re.findall(r'(\d+) units \$\\longrightarrow\$ (\d+)', mid)
P4 = []
for known, rep in rows:
    e = int(rep) - int(known)
    check(e in EXTRAS, f'P4: known {known} -> {rep} gives allowed extra {e}')
    sol = [(h, ) for h in range(1, 30) if h + e == 9] + [(h,) for h in range(1, 30) if h + e == 12]
    P4.append(tuple(x[0] for x in sol))
say('P4 hidden lengths per row:', P4)
check(P4 == [(5, 8), (7, 10), (3, 6)], 'P4 matches guide (5,8),(7,10),(3,6)')
# P5: every extra, every supplied standard
ok = True
for e in EXTRAS:
    hidden = (7 - e, 10 - e)
    if min(hidden) < 1:
        ok = False
    for s, n in STRIPS.items():
        cands = [f for f in EXTRAS if n + f == n + e]
        if cands != [e]:
            ok = False
check(ok, 'P5: for every extra the hidden lengths are positive and one supplied standard reveals the extra')
# P6 boxes from source
boxtxt = mid[mid.index('Problem{6}') if 'Problem{6}' in mid else mid.index('\\problem{6}'):]
cells = re.findall(r'(\d+) units \$\\to\$ (\d+)', boxtxt)
cells = [(int(a), int(b)) for a, b in cells]
BOX = {'I': [cells[0], cells[3], cells[6]], 'II': [cells[1], cells[4], cells[7]], 'III': [cells[2], cells[5], cells[8]]}
say('P6 boxes (read column-wise from source):', BOX)


def consistent(pairs):
    ex = {y - x for x, y in pairs}
    return len(ex) == 1 and ex.pop() in EXTRAS


for name, box in BOX.items():
    reps = []
    if not consistent(box):
        for i in range(3):
            for newy in range(0, 40):
                if newy == box[i][1]:
                    continue
                trial = list(box)
                trial[i] = (box[i][0], newy)
                if consistent(trial):
                    reps.append((box[i], newy))
    say(f'P6 box {name}: consistent={consistent(box)} repairs={reps}')
check(consistent(BOX['II']) and not consistent(BOX['I']) and not consistent(BOX['III']), 'P6: only box II possible')
# P7 exhaustive: lengths 1..12, any extra, any single wrong integer report 0..30
bad = 0
total = 0
for e in EXTRAS:
    for xs in product(range(1, 13), repeat=3):
        true = [(x, x + e) for x in xs]
        for i in range(3):
            for wrong in range(0, 31):
                if wrong == true[i][1]:
                    continue
                puzzle = list(true)
                puzzle[i] = (xs[i], wrong)
                total += 1
                repairs = set()
                for j in range(3):
                    others = [puzzle[k] for k in range(3) if k != j]
                    ex = {y - x for x, y in others}
                    if len(ex) == 1 and ex.copy().pop() in EXTRAS:
                        f = ex.pop()
                        if puzzle[j][1] != puzzle[j][0] + f:
                            repairs.add((j, puzzle[j][0] + f))
                if repairs != {(i, true[i][1])}:
                    bad += 1
check(bad == 0, f'P7: all {total} one-wrong-report puzzles (lengths 1-12) have exactly one repair, the intended one')

# ------------------------------------------------------------ Grades 4-5
say('\n== Grades 4-5 ==')
check('makes 1, 2, or 3 copies' in up and 'adds 0, 1, 2, 3, 4, 5, or' in up.replace('\n', ' '), 'finite machine family read from source')
MACH = [(c, a) for c in (1, 2, 3) for a in range(0, 7)]
check(len(MACH) == 21, '21 machines')


def rep(mc, x):
    return mc[0] * x + mc[1]


def separates(x):
    return len({rep(mc, x) for mc in MACH}) == 21


single = [x for x in range(1, 20) if separates(x)]
say('P1 single lengths that separate all 21 machines (1..19):', single)
check(single[0] == 7 and all(x in single for x in range(7, 20)), 'P1: every length >= 7, and none <= 6, separates all 21 in one request')
for s, n in STRIPS.items():
    amb = sorted({rep(mc, n) for mc in MACH if sum(rep(m2, n) == rep(mc, n) for m2 in MACH) > 1})
    say(f'P1 strip {s} ({n}): ambiguous reports {amb}')
    check(len(amb) > 0, f'P1: strip {s} alone does not always identify')
two_ok = all(len({(rep(mc, x1), rep(mc, x2)) for mc in MACH}) == 21 for x1, x2 in combinations(STRIPS.values(), 2))
check(two_ok, 'P1: any two different supplied strips always identify the machine')
lucky = [(n, y) for n in STRIPS.values() for y in {rep(mc, n) for mc in MACH} if sum(rep(mc, n) == y for mc in MACH) == 1]
say('P1 lucky single reports with supplied strips (length, report):', sorted(lucky))
check((6, 24) in lucky, 'guide: input 6 report 24 forces 3 copies, extra 6')
combos = sorted({sum(STRIPS[s] for s in sub) for r in range(2, 5) for sub in combinations(STRIPS, r)})
say('P1 end-to-end combinations of distinct supplied strips:', combos, '-> separating:', [L for L in combos if separates(L)])
# guide: copies 1 and 2 overlap for every integer input at most 6 (and 2 vs 3)
check(all((2 * L <= L + 6) for L in range(1, 7)) and not (2 * 7 <= 7 + 6), 'guide: copies-1 and copies-2 ranges overlap exactly for L<=6')
check([(c * 7, c * 7 + 6) for c in (1, 2, 3)] == [(7, 13), (14, 20), (21, 27)], 'guide: input 7 gives 7-13, 14-20, 21-27')
# P2
P2u = [mc for mc in MACH if rep(mc, 2) == 6]
say('P2 machines with 2 -> 6:', P2u)
check(P2u == [(1, 4), (2, 2), (3, 0)], 'P2: three machines (1,4),(2,2),(3,0)')
sep2 = [r for r in range(0, 13) if len({rep(mc, r) for mc in P2u}) == 3]
say('P2 second lengths 0..12 that separate them:', sep2)
check(sep2 == [r for r in range(0, 13) if r != 2], 'P2: every second length except 2 separates')
check([rep(mc, 3) for mc in P2u] == [7, 8, 9], 'guide: input 3 gives 7,8,9')
check(any(len([mc for mc in MACH if rep(mc, 2) == y]) == 1 for y in range(0, 20)), 'P2: a single first request can identify (yes)')
# P3
say('P3 / P4 use the positive-stretch, any-shift family')


def line(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    b = F(y2 - y1, x2 - x1)
    return b, F(y1) - b * x1


for name, pts, want in [('A', [(2, 8), (6, 16)], (2, 4, [4, 12, 24])), ('B', [(2, 8), (6, 12)], (1, 6, [6, 10, 16]))]:
    b, a = line(*pts)
    vals = [b * x + a for x in (0, 4, 10)]
    say(f'P3 machine {name}: stretch {b}, shift {a}, reports at 0,4,10: {vals}')
    check((b, a, vals) == (want[0], want[1], want[2]) and b > 0, f'P3 machine {name} matches guide')
# uniqueness: two equations in two unknowns with x1 != x2 -> determinant nonzero
check((2 - 6) != 0, 'P3: distinct inputs give a unique line (no other rule)')
# P4
m = re.search(r'2 units \$\\to\$ (\d+) & 4 units \$\\to\$ (\d+) & 6 units \$\\to\$ (\d+)', up)
P4pts = [(2, int(m.group(1))), (4, int(m.group(2))), (6, int(m.group(3)))]
say('P4 reports:', P4pts)
b01, a01 = line(P4pts[0], P4pts[1])
check(b01 * 6 + a01 != P4pts[2][1], 'P4: the three reports are not on one line')
P4rep = []
for i in range(3):
    keep = [P4pts[j] for j in range(3) if j != i]
    b, a = line(*keep)
    P4rep.append((P4pts[i][0], b * P4pts[i][0] + a, b, a))
say('P4 repairs (changed length, new report, stretch, shift):', [(x, str(y), str(b), str(a)) for x, y, b, a in P4rep])
check([(x, y) for x, y, b, a in P4rep] == [(2, 6), (4, F(23, 2)), (6, 15)] and all(b > 0 for _, _, b, _ in P4rep),
      'P4: exactly three repairs 2->6, 4->11 1/2, 6->15, all positive stretch (guide rules 5/2x+1, 9/4x+5/2, 2x+3)')
check([(b, a) for _, _, b, a in P4rep] == [(F(5, 2), F(1)), (F(9, 4), F(5, 2)), (F(2), F(3))], 'P4 guide rules')
# P5
A = {x: 2 * x + 3 for x in range(1, 9)}
B = dict(A)
B[8] = 20
check(A[2] == B[2] == 7 and A[4] == B[4] == 11 and A[6] == B[6] == 15 and A[8] != B[8], 'P5: guide tables fit and differ at 8')
check([A[x] for x in range(1, 9)] == [5, 7, 9, 11, 13, 15, 17, 19], 'P5: table A as in guide')
# P6
say('P6: exact feasible stretch set for displays d1 at x1, d2 at x2, errors |e|<=1')


def slope_range(x1, d1, x2, d2, e=1):
    D = x2 - x1
    lo, hi = F(d2 - d1 - 2 * e, D), F(d2 - d1 + 2 * e, D)
    return lo, hi


def feasible(b, x1, d1, x2, d2, e=1):
    """exists shift a with |a+b*x1-d1|<=e and |a+b*x2-d2|<=e"""
    lo = max(d1 - e - b * x1, d2 - e - b * x2)
    hi = min(d1 + e - b * x1, d2 + e - b * x2)
    return lo <= hi


for name, (x1, d1, x2, d2), want, wits in [
        ('A', (2, 8, 4, 12), (F(1), F(3)), [((F(1), F(7)), (9, 11)), ((F(3), F(1)), (7, 13))]),
        ('B', (2, 8, 10, 24), (F(7, 4), F(9, 4)), [((F(7, 4), F(11, 2)), (9, 23)), ((F(9, 4), F(5, 2)), (7, 25))])]:
    lo, hi = slope_range(x1, d1, x2, d2)
    # brute force: true reports on a 1/8 grid inside the bands
    grid = [F(k, 8) for k in range(-8, 9)]
    bs = {F((d2 + g2) - (d1 + g1), x2 - x1) for g1 in grid for g2 in grid}
    bs = {b for b in bs if b > 0}
    say(f'P6 pair {name}: exact [{lo}, {hi}], grid min {min(bs)} max {max(bs)}')
    check((lo, hi) == want and min(bs) == lo and max(bs) == hi and lo > 0, f'P6 pair {name}: stretch range [{want[0]}, {want[1]}], both attained, positive')
    for (b, a), true in wits:
        t = (b * x1 + a, b * x2 + a)
        check(t == true and abs(t[0] - d1) <= 1 and abs(t[1] - d2) <= 1, f'P6 pair {name}: witness y={b}x+{a} gives true reports {true} within 1 of the displays')
    check(all(feasible(lo + (hi - lo) * F(k, 10), x1, d1, x2, d2) for k in range(11)), f'P6 pair {name}: every intermediate stretch feasible (sampled)')
    check(not feasible(lo - F(1, 1000), x1, d1, x2, d2) and not feasible(hi + F(1, 1000), x1, d1, x2, d2), f'P6 pair {name}: nothing outside the range')
# P7: worst-case width for each integer pair 1..10, over all displays consistent with some positive-stretch machine


def width_after_truncation(D, Delta, e=1):
    lo, hi = F(Delta - 2 * e, D), F(Delta + 2 * e, D)
    if hi <= 0:
        return None  # no positive-stretch machine fits
    return hi - max(lo, F(0))


worst = {}
for x1, x2 in combinations(range(1, 11), 2):
    D = x2 - x1
    ws = [width_after_truncation(D, F(k, 4)) for k in range(-200, 400)]
    worst[(x1, x2)] = max(w for w in ws if w is not None)
best = min(worst.values())
bestpairs = [p for p, w in worst.items() if w == best]
say('P7 smallest worst-case width', best, 'at', bestpairs)
check(best == F(4, 9) and bestpairs == [(1, 10)], 'P7: unique best pair 1 and 10, worst-case width 4/9')
check(all(w == F(4, x2 - x1) for (x1, x2), w in worst.items()), 'P7: worst-case width is exactly 4/D for every pair')
# one reference repeated: any positive stretch fits ten identical readings
x, y = 5, 12
check(all(abs((y - b * x) + b * x - y) <= 1 for b in (F(1, 100), F(1), F(100))), 'P7: one reference (even repeated) fits stretches 1/100, 1, 100')
# guide remark: true stretch 2, exact displays, separation D >= 1 "avoids truncation"
for D in (1, 2, 9):
    lo, hi = slope_range(0, 0, D, 2 * D)
    say(f'guide P7 remark: stretch 2, exact displays, D={D}: untruncated [{lo}, {hi}]')
lo1, hi1 = slope_range(0, 0, 1, 2)
if lo1 <= 0:
    note('guide P7: with true stretch 2, exact displays and D=1 the untruncated interval is [0, 4]; '
         'positivity removes the endpoint 0, so the positive-stretch set is (0, 4] (width still 4, '
         'but truncation does occur and the smallest stretch is not attained). Stretch 3 would avoid it: '
         f'lower endpoint {slope_range(0, 0, 1, 3)[0]} > 0 at D=1.')
check(all(slope_range(0, 0, D, 3 * D)[0] > 0 for D in range(1, 10)), 'stretch 3 with exact displays avoids truncation for every D in 1..9')

# ------------------------------------------------------------ geometry
say('\n== PDF geometry ==')
try:
    import pymupdf
except ImportError:
    try:
        import fitz as pymupdf
    except ImportError:
        pymupdf = None
if pymupdf is None:
    note('PyMuPDF not installed; geometry checks skipped')
else:
    MM12 = 72 / 25.4 * 12
    for name in ('k-1', 'grades-2-3', 'grades-4-5'):
        doc = pymupdf.open(str(PDF / f'week-94-{name}.pdf'))
        for pno, page in enumerate(doc, 1):
            dr = page.get_drawings()
            # rectangles built from three line segments + close (TikZ rectangles)
            rects = []
            for d in dr:
                r = d['rect']
                if len(d['items']) == 4 and all(it[0] == 'l' for it in d['items']):
                    f = d.get('fill')
                    rects.append((round(r.width / MM12, 3), round(r.height / MM12, 3),
                                  None if f is None else round(f[0], 3), round(r.x0 / MM12, 3), round(r.y0, 1)))
            strips = sorted(w for w, h, f, x0, y0 in rects if f == 0.95 and abs(h - 1) < 0.01)
            squares = [w for w, h, f, x0, y0 in rects if f is None and abs(w - 1) < 0.01 and abs(h - 1) < 0.01]
            small = [(w, f, x0, y0) for w, h, f, x0, y0 in rects if f is not None and h < 0.9]
            # ruler ticks: short vertical lines, grouped by their vertical position
            rows = {}
            for d in dr:
                r = d['rect']
                if len(d['items']) == 1 and d['items'][0][0] == 'l' and r.width < 0.01 and 7 < r.height < 9:
                    rows.setdefault(round(r.y0), []).append(r.x0)
            gaps = set()
            for y, xs in rows.items():
                xs = sorted(xs)
                # a gap over 1.2 units separates two different rulers drawn on one row
                gaps |= {round((b - a) / MM12, 3) for a, b in zip(xs, xs[1:]) if (b - a) / MM12 < 1.2}
            ticks = sum(len(v) for v in rows.values())
            alltick = sorted(round(x / MM12, 3) for xs in rows.values() for x in xs)
            msg = f'{name} p{pno}:'
            if strips:
                msg += f' strips {strips} units;'
            if squares:
                msg += f' {len(squares)} unit squares;'
            if ticks:
                msg += f' {len(rows)} tick rows, {ticks} ticks, gaps {sorted(gaps)} units;'
            if small:
                msg += f' example blocks (width units, grey, x0 units, y0 pt) {small}'
            say(msg)
            if strips:
                check(strips == [2.0, 3.0, 4.0, 6.0], f'{name} p{pno}: cut strips are 2,3,4,6 units of 12 mm, 1 unit tall')
            if squares:
                check(len(squares) == 12, f'{name} p{pno}: unit row is 12 squares of 12 mm')
            if ticks:
                check(gaps == {1.0}, f'{name} p{pno}: every ruler tick gap is 12 mm')
            if name == 'k-1' and pno == 1:
                placed = [(w, x0) for w, f, x0, y0 in small if y0 > 125]
                check(len(placed) == 1 and placed[0][1] in alltick and round(placed[0][1] + 1, 3) in alltick,
                      'k-1 p1 example: the placed 1-unit strip spans exactly one tick gap (ticks 8-9)')
            if name == 'grades-2-3' and pno == 1:
                check([w for w, f, x0, y0 in small] == [1.0, 1.0, 1.0], '2-3 example: input 1 unit, then input 1 + extra 1')
            if name == 'grades-4-5' and pno == 1:
                check([w for w, f, x0, y0 in small] == [1.0] * 5, '4-5 p1 example: input 1, three 1-unit copies, extra 1 (report 4)')
            if name == 'grades-4-5' and pno == 3:
                ws = [w for w, f, x0, y0 in small]
                check(ws == [1.0] * 3 + [1.5] * 3 + [3.5], '4-5 p3 example: 3 units, stretched pieces 1 1/2 each (4 1/2), report bar 3 1/2')

say('\nSUMMARY:', 'all checks passed' if not FAIL else f'{len(FAIL)} FAILED', f'; {len(NOTE)} note(s)')
for n in NOTE:
    say('  note:', n)
text = '\n'.join(OUT) + '\n'
(HERE / 'check_math.py.out').write_text(text)
print(text)
