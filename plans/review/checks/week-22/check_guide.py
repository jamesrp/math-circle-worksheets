"""Check every answer, table and construction stated in the Week 22 adult guide
(week-22-facilitator.pdf) against my own exact computation.

The guide's claims are transcribed below by hand from the rendered guide text
(render/week-22-facilitator.txt); each is recomputed with geom.py.
Also checks the guide's page cross-references against the printed page numbers.

Output: out_check_guide.txt
"""
import os
import re
import subprocess
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from geom import find_root, P, hull, successes, fmt_shared, orient, two_splits  # noqa: E402

ROOT = find_root()
GUIDE = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-22', 'week-22-facilitator.pdf')
LINES = []
BAD = []


def say(s=''):
    LINES.append(s)
    print(s)


def check(name, pts, claimed, shared=None):
    s = successes({k: P(*v) for k, v in pts.items()})
    ok = set(s) == set(claimed)
    msg = f'  {name}: computed {sorted(s)}; guide {sorted(claimed)} -> {"OK" if ok else "MISMATCH"}'
    if shared:
        for k, want in shared.items():
            got = fmt_shared(s[k]) if k in s else 'none'
            good = got == want
            ok &= good
            msg += f'\n      {k}: {got} (guide: {want}) {"OK" if good else "MISMATCH"}'
    say(msg)
    if not ok:
        BAD.append(name)
    return s


def corners(pts):
    return len(hull([P(*v) for v in pts.values()]))


say('Splits: ' + ', '.join(a + '|' + b for a, b in two_splits('ABCD')) + f'  ({len(two_splits("ABCD"))}; '
    f'{sum(1 for a, b in two_splits("ABCD") if min(len(a), len(b)) == 1)} of type 1+3)')

say('K-1 P1 (guide p. 5)')
k1 = {'A': (2, 2), 'B': (10, 3), 'C': (4, 10)}
check('upper-right D=(9,9)', dict(k1, D=(9, 9)), ['AD|BC'])
check('inside D=(4.3,4.7)', dict(k1, D=(4.3, 4.7)), ['ABC|D'])
check('left D=(0.8,7.2)', dict(k1, D=(0.8, 7.2)), ['AC|BD'])
say(f"  hull corners: upper-right {corners(dict(k1, D=(9, 9)))}, left {corners(dict(k1, D=(0.8, 7.2)))} (guide: convex quadrilaterals)")

say('K-1 P2 (guide p. 6)')
k2 = {'A': (2, 3), 'B': (8, 3), 'C': (5, 10)}
check('D on AB', dict(k2, D=(5, 3)), ['AB|CD', 'ABC|D'], {'AB|CD': 'point (5, 3)', 'ABC|D': 'point (5, 3)'})
check('D beyond B', dict(k2, D=(11, 3)), ['AD|BC', 'ACD|B'], {'AD|BC': 'point (8, 3)', 'ACD|B': 'point (8, 3)'})
check('D on AC', dict(k2, D=(3.5, 6.5)), ['AC|BD', 'ABC|D'], {'AC|BD': 'point (7/2, 13/2)', 'ABC|D': 'point (7/2, 13/2)'})

say('K-1 P3 (guide p. 7)')
check('A D C B', {'A': (1.8, 6.3), 'B': (10.8, 6.3), 'C': (7.5, 6.3), 'D': (4.5, 6.3)},
      ['AB|CD', 'AC|BD', 'ABC|D', 'ABD|C'],
      {'AB|CD': 'segment (9/2, 63/10)-(15/2, 63/10)', 'AC|BD': 'segment (9/2, 63/10)-(15/2, 63/10)',
       'ABC|D': 'point (9/2, 63/10)', 'ABD|C': 'point (15/2, 63/10)'})

say('K-1 P5 (guide p. 9)')
k5 = {'A': (2.5, 5.6), 'B': (8.8, 5.6)}
check('middle cross', dict(k5, C=(6, 5.6)), ['AB|C'])
check('right cross', dict(k5, C=(11, 5.6)), ['AC|B'])
check('upper cross', dict(k5, C=(5.5, 9.5)), [])
check('C left of A', dict(k5, C=(1, 5.6)), ['A|BC'])
check('C = A', dict(k5, C=(2.5, 5.6)), ['A|BC', 'AB|C'])
check('C = B', dict(k5, C=(8.8, 5.6)), ['AC|B', 'AB|C'])

say('Grades 2-3 P1 (guide p. 10)')
m1 = {'A': (2, 3), 'B': (10, 2), 'C': (3, 10)}
check('upper-right', dict(m1, D=(9, 9)), ['AD|BC'])
check('interior', dict(m1, D=(4, 5)), ['ABC|D'], {'ABC|D': 'point (4, 5)'})
check('on AB', dict(m1, D=(6, 2.5)), ['AB|CD', 'ABC|D'], {'AB|CD': 'point (6, 5/2)', 'ABC|D': 'point (6, 5/2)'})
s = check('below AB', dict(m1, D=(6, 1)), ['AB|CD'])
say(f"      below-AB crossing is not D: {fmt_shared(s['AB|CD']) != 'point (6, 1)'}")

say('Grades 2-3 P2 (guide p. 11)')
check('A D B C', {'A': (2, 6.3), 'B': (7.8, 6.3), 'C': (10.8, 6.3), 'D': (4.6, 6.3)},
      ['AB|CD', 'AC|BD', 'ABC|D', 'ACD|B'],
      {'AB|CD': 'segment (23/5, 63/10)-(39/5, 63/10)', 'AC|BD': 'segment (23/5, 63/10)-(39/5, 63/10)',
       'ABC|D': 'point (23/5, 63/10)', 'ACD|B': 'point (39/5, 63/10)'})
check('extension: same order, other gaps', {'A': (0, 6), 'B': (9, 6), 'C': (12, 6), 'D': (1, 6)},
      ['AB|CD', 'AC|BD', 'ABC|D', 'ACD|B'])

say('Grades 2-3 P3 and P4 (guide p. 12)')
check('P3 construction x=2,4,8,10', {'A': (2, 6), 'B': (4, 6), 'C': (8, 6), 'D': (10, 6)},
      ['AC|BD', 'AD|BC', 'ABD|C', 'ACD|B'], {'AD|BC': 'segment (4, 6)-(8, 6)'})
first = {'A': (2, 2), 'B': (10, 2), 'C': (2, 10), 'D': (4, 4)}
second = {'A': (2, 2), 'B': (10, 2), 'C': (10, 10), 'D': (2, 10)}
third = {'A': (2, 6), 'B': (4, 6), 'C': (8, 6), 'D': (10, 6)}
s1 = check('P4 first', first, ['ABC|D'])
s2 = check('P4 second', second, ['AC|BD'], {'AC|BD': 'point (6, 6)'})
say(f'      success sets disjoint: {not set(s1) & set(s2)}')

say('Grades 2-3 P5 (guide p. 13)')
check('printed triangle', {'A': (2, 3), 'B': (10, 4), 'C': (6, 10)}, [])
A, B = P(2, 3), P(10, 4)
for x in (Fr(0), Fr(63, 5)):
    y = Fr(11, 4) + x / 8
    say(f'  locus point ({x}, {y}) on AB: {orient(A, B, (x, y)) == 0}')

say('Grades 4-5 P1 (guide p. 14)')
u1 = {'A': (2, 2), 'B': (10.5, 3), 'C': (4.5, 10)}
check('upper-right', dict(u1, D=(9.8, 9)), ['AD|BC'])
check('interior', dict(u1, D=(5, 5)), ['ABC|D'])
check('on AB', dict(u1, D=(6.25, 2.5)), ['AB|CD', 'ABC|D'])
check('left', dict(u1, D=(1, 6)), ['AC|BD'])

say('Grades 4-5 P2 (guide p. 15)')
check('A C B D', {'A': (2, 3), 'B': (8, 9), 'C': (5, 6), 'D': (10, 11)}, ['AB|CD', 'AD|BC', 'ABD|C', 'ACD|B'],
      {'AB|CD': 'segment (5, 6)-(8, 9)', 'AD|BC': 'segment (5, 6)-(8, 9)'})
say(f'  length of CB squared = {(8 - 5) ** 2 + (9 - 6) ** 2} (guide: 3 sqrt 2, i.e. 18)')

say('Grades 4-5 P4 (guide p. 16)')
check('A = D', {'A': (3, 3), 'B': (10, 4.5), 'C': (5.5, 10), 'D': (3, 3)}, ['A|BCD', 'AB|CD', 'AC|BD', 'ABC|D'])
check('all four coincide', {'A': (3, 3), 'B': (3, 3), 'C': (3, 3), 'D': (3, 3)},
      [a + '|' + b for a, b in two_splits('ABCD')])

say('Grades 4-5 P5 table (guide p. 17)')
table = {  # split: (first, second, third)
    'A|BCD': ('no', 'no', 'no'), 'AB|CD': ('no', 'no', 'no'), 'AC|BD': ('no', 'yes', 'yes'),
    'AD|BC': ('no', 'no', 'yes'), 'ABC|D': ('yes', 'no', 'no'), 'ABD|C': ('no', 'no', 'yes'),
    'ACD|B': ('no', 'no', 'yes')}
for col, cfg in enumerate((first, second, third)):
    s = successes({k: P(*v) for k, v in cfg.items()})
    claimed = [k for k, v in table.items() if v[col] == 'yes']
    ok = set(s) == set(claimed)
    say(f'  column {col + 1}: computed {sorted(s)} vs table {sorted(claimed)} -> {"OK" if ok else "MISMATCH"}')
    if not ok:
        BAD.append(f'P5 table column {col + 1}')
s3 = successes({k: P(*v) for k, v in third.items()})
say(f"  third: AC|BD {fmt_shared(s3['AC|BD'])}, AD|BC {fmt_shared(s3['AD|BC'])} (guide: both share BC)")
for name, cfg in (('first', first), ('second', second)):
    gp = all(orient(*(P(*cfg[x]) for x in t)) != 0 for t in ('ABC', 'ABD', 'ACD', 'BCD'))
    say(f'  {name} in general position: {gp}; inside the 12.6 board: {all(0 <= c <= 12.6 for v in cfg.values() for c in v)}')

say('Grades 4-5 P7 (guide p. 19)')
check('printed triangle', {'A': (2, 3), 'B': (10.3, 4), 'C': (4.8, 10.1)}, [])
say(f"  (B-A) x (C-A) = {orient(P(2, 3), P(10.3, 4), P(4.8, 10.1))} (guide: 5613/100)")

say('Extensions (guide p. 20)')
tri_seg = {'A': (0, 0), 'B': (6, 0), 'C': (0, 6), 'D': (1, 1), 'E': (2, 2)}
s = successes({k: P(*v) for k, v in tri_seg.items()})
say(f"  five labels, triangle ABC vs segment DE: {fmt_shared(s['ABC|DE'])}")
two_tri = {'A': (0, 0), 'B': (6, 0), 'C': (0, 6), 'D': (6, 6), 'E': (0, 2), 'F': (2, 0)}
s = successes({k: P(*v) for k, v in two_tri.items()})
say(f"  six labels, triangles ABC vs DEF: {fmt_shared(s['ABC|DEF'])}")
say('  (one-dimensional threshold, maximum of seven, four for distinct collinear: see check_theorem.py)')

# printed page numbers and cross-references
txt = subprocess.run(['pdftotext', '-layout', GUIDE, '-'], capture_output=True, text=True).stdout
pages = txt.split('\f')
printed = {}
for i, pg in enumerate(pages, 1):
    m = re.findall(r'\s(\d+)\s*$', pg.rstrip())
    head = next((ln.strip() for ln in pg.splitlines()[1:12] if ln.strip() and 'BELLINGHAM' not in ln and 'Week 22 /' not in ln), '')
    if m:
        printed[int(m[-1])] = (i, head)
say('Printed page -> PDF page and heading:')
for n in sorted(printed):
    say(f'  printed {n:2d} = PDF {printed[n][0]:2d}: {printed[n][1][:60]}')
finder = {5: 'K-1 Problem 1', 6: 'K-1 Problem 2', 7: 'K-1 Problem 3', 8: 'K-1 Problems 4 and 6', 9: 'K-1 Problem 5',
          10: 'Grades 2-3 Problem 1', 11: 'Grades 2-3 Problem 2', 12: 'Grades 2-3 Problems 3 and 4',
          13: 'Grades 2-3 Problems 5 and 6', 14: 'Grades 4-5 Problem 1', 15: 'Grades 4-5 Problems 2 and 3',
          16: 'Grades 4-5 Problem 4', 17: 'Grades 4-5 Problem 5', 18: 'Grades 4-5 Problem 6',
          19: 'Grades 4-5 Problem 7', 20: 'Extensions and fidelity limits', 21: 'Sources and verification',
          4: 'Adult mathematical tools', 3: 'Flexible hour menu'}
for n, h in finder.items():
    ok = n in printed and printed[n][1].startswith(h)
    if not ok:
        BAD.append(f'finder p{n}')
    say(f'  finder/cross-reference p. {n} -> {h}: {"OK" if ok else "MISMATCH"}')
say(f"  'middle ... P5 and P6 can continue another day' is on printed p. "
    f"{[n for n, (i, h) in printed.items() if 'P5 and P6 can continue' in pages[i - 1]]}; "
    f"route note says 'already marked on guide p4'")
say(f'  printed page numbers present: {sorted(printed)} (missing: {sorted(set(range(1, max(printed) + 1)) - set(printed))})')

say()
say('MISMATCHES: ' + (', '.join(BAD) if BAD else 'none'))
open(os.path.join(HERE, 'out_check_guide.txt'), 'w').write('\n'.join(LINES) + '\n')
