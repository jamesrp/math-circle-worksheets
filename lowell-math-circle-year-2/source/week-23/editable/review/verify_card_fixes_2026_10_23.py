#!/usr/bin/env python3
"""Check every claim changed by the October 23, 2026 card shoulds and coulds.

    python3 review/verify_card_fixes_2026_10_23.py [build-folder] [bonus-folder]

The build folder (default build/) holds k-1.pdf, grades-2-3.pdf, grades-4-5.pdf and
facilitator-guide.pdf from build.sh; the optional bonus folder holds week-23-bonus.pdf
and week-23-bonus-facilitator.pdf from the bonus package's build.py. Needs PyMuPDF.
"""
import re
import sys
from itertools import permutations, product
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
build = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build'
bonus = Path(sys.argv[2]) if len(sys.argv) > 2 else None

LAYOUTS = [(ROOT / 'problem-files', ROOT / 'problem-files' / 'tools'),
           (ROOT.parent, ROOT.parent.parent / 'problem-files')]
for week_dir, tools in LAYOUTS:
    if (week_dir / 'week.toml').exists() and (tools / 'atoms.py').exists():
        break
else:
    sys.exit('Cannot find the Week 23 problem files and tools')
sys.path.insert(0, str(tools))
import atoms  # noqa: E402


def run(values, bars):
    v = list(values)
    for a, b in bars:
        if v[a - 1] > v[b - 1]:
            v[a - 1], v[b - 1] = v[b - 1], v[a - 1]
    return tuple(v)


def text(pdf, page=None):
    d = fitz.open(pdf)
    pages = [p.get_text() for p in d]
    flat = lambda t: ' '.join(t.replace('–', '-').split())
    return flat(pages[page - 1]) if page else [flat(t) for t in pages]


checks = 0
def ok(cond, what):
    global checks
    assert cond, what
    checks += 1


# ---------------------------------------------------------------- student pages
week = atoms.load_week(week_dir)
by_id = {a.meta['id']: a for a in week.atoms}

# Shoulds 2 and 3: the rules, as printed on p. 1 of each band.
k1 = text(build / 'k-1.pdf', 1)
# The last sentence was the card's "The machine sorts when the fewest dots finish at the top." until the
# Critic L must later the same day restored the whole order (verify_sorts_rule_2026_10_23.py); either passes here.
ok(any('Cards move left to right. At each bar, look at the two cards at its ends: the one with fewer dots goes up. Equal cards stay. '
       'The bars stay the same for every start. ' + last in k1
       for last in ('The machine sorts when the fewest dots finish at the top.',
                    'The machine sorts when the cards finish in order: fewest dots at the top, most dots at the bottom.')), 'K-1 rule')
ok('fewer dots go above' not in k1 and 'black dots' not in k1, 'K-1 rule no longer calls bar ends dots')
for band in ('grades-2-3', 'grades-4-5'):
    t = text(build / f'{band}.pdf', 1)
    ok('compare only the two lanes with black dots: the smaller value goes to the upper lane and the larger to the lower lane.' in t, band + ' rule')
    ok('A machine sorts when the final values never get smaller from lane 1 down.' in t, band + ' sorted rule')
    ok('lower-numbered' not in ' '.join(text(build / f'{band}.pdf')), band + ' has no "lower-numbered"')
# "never get smaller from lane 1 down" is the sorted condition, ties allowed.
for v in product(range(3), repeat=4):
    ok((tuple(sorted(v)) == v) == all(v[i] <= v[i + 1] for i in range(3)), 'sorted means never smaller going down')

# Should 4: K-1 Problem 3 prints Problem 1's six starts under each machine, to circle.
p3 = text(build / 'k-1.pdf', 3)
ok('Problem 3: For each machine, circle every start that finishes in the wrong order.' in p3, 'K-1 P3 prompt')
fig = [s.raw for s in by_id['w23.k1-wrong-order'].sections if s.kind == 'figure'][0]
machines = [eval(m) for m in re.findall(r'network\(3,(\[[^\]]*\])', fig)]
grids = re.findall(r'start_grid\(ORDERS3,(\[[^\]]*\]),\[([\d.]+)\]\)', fig)
ok(machines == [[(1, 2), (2, 3), (1, 2)], [(1, 2), (1, 2), (2, 3)]], 'K-1 P3 machines unchanged')
ok(len(grids) == 2 and all(len(eval(xs)) == 6 for xs, y in grids), 'six starts under each machine')
orders = week.figures['ORDERS3']
p1fig = [s.raw for s in by_id['w23.k1-every-start'].sections if s.kind == 'figure'][0]
ok('start_grid(ORDERS3' in p1fig and orders == list(permutations([1, 2, 3])), 'same starts, same order as Problem 1')
wrong = [[i + 1 for i, s in enumerate(orders) if run(s, m) != (1, 2, 3)] for m in machines]
ok(wrong == [[], [4, 6]], 'circle nothing under the upper machine; the 4th and 6th starts under the lower one')
ok([''.join(map(str, orders[i - 1])) for i in wrong[1]] == ['231', '321'], 'they are 231 and 321')
# the 36 start cards are drawn: 6 starts x 3 cards x 2 machines, plus 2 x 6 lane boxes
d = fitz.open(build / 'k-1.pdf')
ok(len([1 for path in d[2].get_drawings() if [i[0] for i in path['items']] == ['l'] * 4]) == 36 + 12, 'card boxes on K-1 p. 3')

# Could 12: grades 4-5 Problem 7.
p7 = text(build / 'grades-4-5.pdf', 7)
ok('Problem 7:' in p7 and 'explain why fewer bars cannot work.' in p7 and 'Count each bar' not in p7, '4-5 P7 sentence cut')

# Footers.
for band, tag, pages in (('k-1', 'K', 6), ('grades-2-3', '23', 6), ('grades-4-5', '45', 7)):
    t = text(build / f'{band}.pdf')
    vs = ('v3', 'v4') if tag == 'K' else ('v3',)  # K-1 went to v4 with the Critic L must
    ok(len(t) == pages and all(any(f'Bellingham Math Circle / Week 23 / F23-{tag}-{v}' in x for v in vs) for x in t), band + ' footers v3')

# ---------------------------------------------------------------- the guide
g = text(build / 'facilitator-guide.pdf')
G = ' '.join(g)
ok(len(g) == 13, 'guide is the overview plus 12 pages')
ok(any(f'F23-K-{v}, F23-23-v3 and F23-45-v3' in G for v in ('v3', 'v4')), 'guide names the v3 packets (K-1 v4 after the Critic L must)')
T = [(1, 2), (2, 3)]
# Should 6: rehearse and run 312, which sorts (231, the old rehearsal, is a failure P1 asks for).
ok('rehearse input 312 on bars (1,2), (2,3)' in g[1] and 'start 312 on bars (1,2), (2,3), which sorts' in g[1], 'launch runs 312')
ok(run((3, 1, 2), T) == (1, 2, 3) and run((2, 3, 1), T) != (1, 2, 3), '312 sorts on T; 231 does not')
ok('(3, 1, 2 and 1, 2, 3)' in g[1], 'launch writes start and finish by lane')
# Should 5: partners keep the rule.
ok('one child chooses the start; the partner slides the time strip one bar at a time' in g[1] and 'At the 4-5 table a third child referees.' in g[1], 'partner rule')
# Could 10: the hour starts with about five minutes of running around.
rows = re.findall(r'(\d+)-(\d+) min', g[2])
ok([(int(a), int(b)) for a, b in rows] == [(0, 5), (5, 12), (12, 27), (27, 30), (30, 50), (50, 57), (57, 60)], 'time table rows')
ok(all(int(rows[i][1]) == int(rows[i + 1][0]) for i in range(len(rows) - 1)), 'time rows are contiguous')
ok(35 <= 50 - 12 <= 40, 'table work 12-50 min is 38 minutes, within the thirty-five to forty in context.md')
ok('Arrival and about five minutes of running around.' in g[2], 'running-around row')
ok('"lower-numbered" means higher on the page' not in G and 'the upper lane is the one nearer lane 1, higher on the page' in g[2], 'confusions line matches the new rule')
# K-1 P3 key names the circled pictures.
ok('children circle nothing under the upper machine and the fourth and sixth pictures under the lower one' in g[4], 'K-1 P3 key')
# Should 7: 1110 finishes 1011 on W.
W = [(1, 2), (1, 3), (2, 3), (2, 4)]
ok(run((1, 1, 1, 0), W) == (1, 0, 1, 1) and '1110 finishes 1011' in g[7] and '1110 finishes 1101' not in G, '1110 trace')
# Should 8: certifying a repair takes 24 starts, six for each top card.
four = list(permutations([1, 2, 3, 4]))
ok(len(four) == 24 and all(sum(1 for s in four if s[0] == c) == 6 for c in range(1, 5)), '24 starts, six per top card')
for m in ([(1, 2), (3, 4), (1, 3), (2, 4)], [(1, 3), (2, 4), (1, 2), (3, 4)]):
    for s in four:
        out = run(s, m)
        ok(out[0] == 1 and out[3] == 4, 'smallest reaches lane 1 and largest lane 4 before the last bar')
    ok(all(run(s, m + [(2, 3)]) == (1, 2, 3, 4) for s in four), 'the repair (2,3) sorts all 24')
ok('split them by top card (six each)' in g[7], 'P3 guide sentence')
# Should 9: a machine that sorts every 0-1 start sorts every order (zero-one principle), checked
# here for every four-lane machine of up to six bars.
pairs = [(a, b) for a in range(1, 5) for b in range(a + 1, 5)]
binary = list(product([0, 1], repeat=4))
for k in range(7):
    for m in product(pairs, repeat=k):
        if all(run(s, m) == tuple(sorted(s)) for s in binary):
            ok(all(run(s, m) == (1, 2, 3, 4) for s in four), 'zero-one principle')
ok('Can a machine sort every 0-1 start and still fail one?' in g[8] and 'Grades 4-5 Problem 4, page 10' in g[8] and 'Problem 4' in g[10], 'held question')
# Could 11: the build residue is gone.
ok('Final student authority' not in G and 'PROMPT.md' not in G, 'sources page residue cut')

# ---------------------------------------------------------------- the bonus companion
if bonus:
    b = text(bonus / 'week-23-bonus.pdf')
    ok('sends the smaller value to the upper lane.' in b[0] and 'lower-numbered' not in ' '.join(b), 'bonus rule')
    ok(all('W23-BON-v2' in x for x in b), 'bonus footers v2')
    bg = text(bonus / 'week-23-bonus-facilitator.pdf')
    ok('send the smaller value to the upper lane.' in ' '.join(bg) and all(('W23-BON-FAC-v2' in x) or ('W23-BON-FAC-v3' in x) for x in bg), 'bonus guide (v3 after the band-label fix)')

print(f'PASS: {checks} checks of the October 23 card fixes' + (' (with the bonus)' if bonus else ''))
