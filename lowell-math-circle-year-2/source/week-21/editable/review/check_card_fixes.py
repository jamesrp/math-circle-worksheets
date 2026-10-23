#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes for Week 21 (see card-fixes-2026-10-23.md).

Run after build.sh has built the packets and the guide (it is the last step of build.sh).
Reads the problem files (repository or ZIP layout), the generated LaTeX in src/, the guide
in build/ and the package README. Every line printed starts with PASS; any failure stops
with an error. Lengths are in centimetres unless a message says mm.
"""
import math
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent           # the editable package
LAYOUTS = [(ROOT / 'problem-files', ROOT / 'problem-files' / 'tools'),
           (ROOT.parent, ROOT.parent.parent / 'problem-files')]
for week, tools in LAYOUTS:
    if (week / 'week.toml').exists() and (tools / 'atoms.py').exists():
        break
else:
    sys.exit('Cannot find the Week 21 problem files and tools.')
sys.path.insert(0, str(tools))
import atoms  # noqa: E402

w = atoms.load_week(week)
BOARDS = w.figures['BOARDS']
tex = {b: (ROOT / 'src' / f'{b}.tex').read_text() for b in ('k-1', 'grades-2-3', 'grades-4-5')}
guide = ROOT / 'build' / 'facilitator-guide.pdf'
gpages = subprocess.run(['pdftotext', '-layout', str(guide), '-'], capture_output=True, text=True, check=True).stdout.split('\f')
gpages = [' '.join(p.split()) for p in gpages if p.strip()]
out = []


def ok(cond, msg):
    if not cond:
        sys.exit('FAIL: ' + msg)
    out.append('PASS: ' + msg)


def page(n):
    """Guide page n as printed in its footer (the unnumbered overview is PDF page 1)."""
    return gpages[n]


def length(b, a, c, t):
    pa, pc = b['points'][a], b['points'][c]
    m = (t, b['line']) if b['axis'] == 'h' else (b['line'], t)
    return math.dist(pa, m) + math.dist(m, pc)


def best(b, a, c):
    """The reflected crossing: where the straight segment from a to c's mirror image meets the line."""
    ix = 1 if b['axis'] == 'h' else 0
    pa, pc = b['points'][a], b['points'][c]
    da, dc = abs(pa[ix] - b['line']), abs(pc[ix] - b['line'])
    return (pa[1 - ix] * dc + pc[1 - ix] * da) / (da + dc)


def mm(cm):
    return 10 * cm


# Should 1: Grades 2-3 Problem 7 asks the Grades 4-5 question.
q = 'In which cases does the same route still give a shortest allowed route? Explain.'
restricted = [a for a in w.atoms if a.meta['id'] == 'w21.restricted'][0]
ok(q in tex['grades-2-3'] and q in tex['grades-4-5'] and 'is your shortest route still allowed' not in tex['grades-2-3'],
   'Grades 2-3 and 4-5 restricted-contact problems ask whether the same route is still a shortest allowed route')
r = BOARDS['restricted']
m = best(r, 'A', 'B')
marks = r['marks']
inside = {k: marks[k[0]] < m < marks[k[1]] for k in ('CD', 'EF', 'CF')}
ok(abs(m - 6.5) < 1e-9 and inside == {'CD': True, 'EF': False, 'CF': True},
   'restricted board: best contact x = 6.5 is strictly inside C-D and C-F, outside E-F')
ok('W21-23-v3' in tex['grades-2-3'] and 'W21-K-v2' in tex['k-1'] and 'W21-45-v2' in tex['grades-4-5']
   and 'W21-K-v2, W21-23-v3 and W21-45-v2' in page(1), 'Grades 2-3 prints W21-23-v3; the other bands keep v2; guide page 1 names all three')
ok('Both groups then ask when the same route remains a shortest allowed route' in page(13), 'guide page 13 describes one question for both bands')

# Should 2: string is coarse near the best contact. Every assigned pair on every board.
pairs = {'equal': ['AB'], 'guesses': ['AB'], 'mirror': ['AC'], 'unequal': ['AB'], 'compare': ['AB', 'AC'],
         'vertical': ['AB', 'AC', 'BC'], 'matching': ['AB', 'CD'], 'restricted': ['AB'], 'lengthtie': ['AB', 'AC'], 'unique': ['AB']}
costs = []
for name, ps in pairs.items():
    b = BOARDS[name]
    for a, c in ps:
        t = best(b, a, c)
        low = length(b, a, c, t)
        ok(all(length(b, a, c, t + k / 100) >= low - 1e-12 for k in range(-300, 301)), f'{name} {a}{c}: the contact at {t:.3f} is the shortest of 601 sampled contacts within 3 cm')
        costs += [mm(length(b, a, c, t + s) - low) for s in (-1.5, 1.5)]
ok(0.95 < min(costs) and max(costs) < 3.5, f'a contact 1.5 cm from the best costs {min(costs):.2f} to {max(costs):.2f} mm on every board ("only 1 to 3.5 mm")')
g = BOARDS['guesses']
gx = [mm(length(g, 'A', 'B', x) - length(g, 'A', 'B', best(g, 'A', 'B'))) for x, _ in [(p[1][0], p) for p in g['paths']]]
cb = BOARDS['compare']
gap = mm(length(cb, 'A', 'C', best(cb, 'A', 'C')) - length(cb, 'A', 'B', best(cb, 'A', 'B')))
ok(min(gx) > 5 and gap > 5, f'the printed guesses are {gx[0]:.1f} and {gx[1]:.1f} mm longer than the best; the two minima on page 8 differ by {gap:.1f} mm (all 5 mm or more)')
ok('String should settle differences of 5 mm or more, such as the printed guesses (page 5) or the two minima on page 8' in page(1)
   and 'a contact 1.5 cm from the best is only 1 to 3.5 mm longer' in page(1), 'guide page 1 (Physical model) states what string can and cannot settle')
u = BOARDS['unequal']
mid = mm(length(u, 'A', 'B', 8.3) - length(u, 'A', 'B', best(u, 'A', 'B')))
ok(1.5 < mid < 2.5 and 'The midpoint route is only about 2 mm longer, too little for string to show' in page(7),
   f'unequal board: the midpoint guess x = 8.3 is {mid:.2f} mm longer, and guide page 7 says to show it with the fold')

# Should 3: eleven children at 4 / 4 / 3, two strings per pair.
p1 = page(1)
ok('Preparation for eleven children and three adults' in p1 and '4 / 4 / 3' in p1 and 'four 60 cm non-stretch strings' in p1
   and 'twelve strings' in p1 and 4 * 3 == 12, 'guide page 1: eleven children at 4 / 4 / 3, four strings per table, twelve in all')
pages = {b: t.count(r'\newpage') + 1 for b, t in tex.items()}
ok(set(pages.values()) == {7} and 11 * 7 == 77 and '77 pages' in p1, f'packets are {sorted(pages.values())} pages, so eleven full packets are 77 pages, as page 1 says')
ok('eleven-child / three-adult' in page(17) and 'ten-child' not in ' '.join(gpages), 'the sources page names the eleven-child group; no ten-child planning remains')

# Should 4: each contact is also given from the left (or bottom) end mark, x - 0.6.
def from_end(x):
    return f'{x - 0.6:.1f}'
claims = [
    (4, [from_end(6.4) + ' and ' + from_end(10.4), from_end(8.4)]),
    (5, [from_end(best(g, 'A', 'B')), f'x = 3.5 ({from_end(3.5)} cm from the end mark)', f'x = 11.5 ({from_end(11.5)} cm)']),
    (6, [from_end(best(BOARDS['mirror'], 'A', 'C'))]),
    (7, [from_end(best(u, 'A', 'B'))]),
    (8, [from_end(best(cb, 'A', 'B')) + ' and ' + from_end(best(cb, 'A', 'C'))]),
    (9, [', '.join(from_end(best(BOARDS['vertical'], *p)) for p in ('AB', 'AC'))
         + ' and ' + from_end(best(BOARDS['vertical'], 'B', 'C')) + ' cm']),
    (10, [from_end(BOARDS['inverse']['marks']['P'])]),
    (11, [from_end(best(BOARDS['lengthtie'], 'A', 'B')) + ' and ' + from_end(best(BOARDS['lengthtie'], 'A', 'C'))]),
    (12, [from_end(best(BOARDS['matching'], 'A', 'B'))]),
    (13, [from_end(m), f'C-D allows {from_end(marks["C"])} to {from_end(marks["D"])} cm: yes', f'E-F allows {from_end(marks["E"])} to {from_end(marks["F"])} cm: no',
          f'C-F allows {from_end(marks["C"])} to {from_end(marks["F"])} cm: yes']),
    (14, [from_end(best(BOARDS['unique'], 'A', 'B'))]),
]
ok(abs(best(BOARDS['matching'], 'A', 'B') - best(BOARDS['matching'], 'C', 'D')) < 1e-9, 'matching board: A-B and C-D share the contact')
for n, texts in claims:
    ok(all(t in page(n) for t in texts) and 'end mark' in page(n), f'guide page {n} gives ' + '; '.join(texts) + ' from the end mark')
ok('measure along the line from the left end mark (the bottom one on the vertical board)' in p1, 'guide page 1 explains measuring from the end mark')
ok('5.9 cm from the left end mark' in restricted.meta['kernel'] and '5.6 cm from its left end mark'
   in [a for a in w.atoms if a.meta['id'] == 'w21.45-shared-contact'][0].meta['kernel'], 'the key kernels use end-mark distances')

# Should 5: on the matching diagram (page 12) C's label is beside C, and D' is labelled below-left of its dot.
bbox = subprocess.run(['pdftotext', '-bbox', '-f', '13', '-l', '13', str(guide), '-'], capture_output=True, text=True, check=True).stdout
words = [(float(x0), float(y0), float(x1), float(y1), wd) for x0, y0, x1, y1, wd in
         re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>', bbox)]
lab = {wd: (x0, y0, x1, y1) for x0, y0, x1, y1, wd in words if wd in ('A', 'C', 'B′', 'D′') and y0 < 360}
sc = min((524 - 40) / 16.8, (184 - 18) / 18.2)              # build_guide.py's diagram scale (points per cm)
mt = BOARDS['matching']['points']
c_dot = lab['A'][0] + 16 + (mt['C'][0] - mt['A'][0]) * sc    # A's label starts 16 pt left of A's dot
d_dot = lab['B′'][0] - 5 - (mt['B'][0] - mt['D'][0]) * sc    # B'’s label starts 5 pt right of B'’s dot
ok(lab['C'][0] > c_dot, f'C label starts {lab["C"][0] - c_dot:.1f} pt right of C\'s dot, not above A')
ok(lab['D′'][2] < d_dot and lab['D′'][1] > lab['B′'][1] + 10, 'D′ label is left of and below its dot, not between D′ and B′')

# Coulds 6-9.
p2 = page(2)
ok('draw a line and two dots on a blank sheet' in p2 and 'spare board' not in p2, 'page 2 launch uses a line and two dots on a blank sheet')
ok('5 to 12 minutes together' in p2 and 'After the opening five minutes of running around' in p2 and '12 to 54 minutes at tables' in p2
   and '54 to 60 minutes' in p2 and '48 to 60' not in p2, 'page 2 timing: five-minute run, launch 5-12, tables 12-54, share 54-60')
ok('Explanations can be told aloud or written on a blank sheet, since B′ needs the space below the line.' in page(3), 'page 3: explanations aloud or on a blank sheet')
allg = ' '.join(gpages)
readme = (ROOT / 'README.md').read_text()
ok('What was checked' not in allg and 'Rebuild and review' not in allg and 'separate new production' not in allg
   and '## Guide production and rebuild notes' in readme and 'K-1 P2 is the guesses board' in readme,
   'production and rebuild notes moved from the guide to the package README')
n = len(gpages) - 1
ok(n == 18 and all(page(i).endswith(f'{i} / {n}') for i in range(1, n + 1)) and 'Starting routes and return visits' in page(n),
   'guide pages read 1 / 18 to 18 / 18 after the unnumbered overview; the route update is 18 / 18')
ok(all(page(i).startswith('BELLINGHAM MATH CIRCLE / ADULT GUIDE / UNSCHEDULED LIBRARY SLOT 21') and 'Week 21 / Draft and unpiloted / Facilitator guide' in page(i)
       for i in range(1, n + 1)), 'every numbered page, the route update included, has the same header and footer')

print('\n'.join(out))
