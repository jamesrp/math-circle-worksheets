"""Check of the Week 62 review card's fixes, October 23, 2026 (W62-S-v2, W62-FAC-v2, W62-M-v1).

Reads the delivered PDFs, not the source. Networks are rebuilt from extracted.json (the
math check's own extraction of the v1 packet) and compared with the v2 packet's circles and
lines, so the 18 networks are shown unchanged. Every changed claim is checked by brute
force: the K-1 plain-words key, the p. 9 example, the overview's swapping sentence, the
sheet, kit, marker and counter arithmetic, and the materials grid.

Run: python3 check_card_fixes.py   (writes out_check_card_fixes.txt beside itself)
"""
import itertools
import json
import os
import re
import sys

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
W = os.path.join(ROOT, 'lowell-math-circle-year-2/week-62')
NEW_S = pymupdf.open(os.path.join(W, 'week-62-students.pdf'))
NEW_G = pymupdf.open(os.path.join(W, 'week-62-facilitator.pdf'))
MAT = pymupdf.open(os.path.join(W, 'week-62-materials.pdf'))
OLD_S = pymupdf.open(os.path.join(W, 'archive-before-card-fixes-2026-10-23/week-62-students.pdf'))
OLD_G = pymupdf.open(os.path.join(W, 'archive-before-card-fixes-2026-10-23/week-62-facilitator.pdf'))
OUT = []
MM = 72 / 25.4


def ok(cond, msg):
    if not cond:
        raise SystemExit('FAIL ' + msg)
    OUT.append('ok   ' + msg)


def flat(page):
    return re.sub(r'\s+', ' ', page.get_text()).replace('’', "'")


def body(page, footer):
    return flat(page).replace(footer, '')


# ------------------------------------------------------------------ graph tools
def colourings(V, E, k):
    for vals in itertools.product(range(1, k + 1), repeat=len(V)):
        c = dict(zip(V, vals))
        if all(c[a] != c[b] for a, b in E):
            yield c


def chi(V, E):
    return next(k for k in range(1, len(V) + 1) if any(True for _ in colourings(V, E, k)))


def alpha(V, E):
    Es = {frozenset(e) for e in E}
    return max(r for r in range(len(V) + 1) for S in itertools.combinations(V, r)
               if all(frozenset(p) not in Es for p in itertools.combinations(S, 2)))


def edges(s):
    return [tuple(p) for p in s.split()]


# ------------------------------------------------------------- student packet
S_OLD, S_NEW = 'W62-S-v1', 'W62-S-v2'
ok(len(NEW_S) == 9, 'student packet still has 9 pages')
for i, p in enumerate(NEW_S, 1):
    ok(f'Bellingham Math Circle / Week 62 / {S_NEW}' in flat(p), f'student p. {i} footer {S_NEW}')
want = {1: '2–5', 2: '2–5', 3: '2–5', 4: '4–5', 5: '4–5', 6: '3–5', 7: '3–5', 8: '4–5', 9: '4–5'}
for i, p in enumerate(NEW_S, 1):
    ok(f'Week 62 / Conflict networks / Grades {want[i]}' in flat(p), f'student p. {i} headed Grades {want[i]}')

# Unchanged pages: same text apart from the footer id, same vector drawings.
for i in (2, 4, 5, 8):
    a, b = OLD_S[i - 1], NEW_S[i - 1]
    ok(body(a, S_OLD) == body(b, S_NEW), f'student p. {i} text unchanged apart from the footer')
    da = [(d['rect'].round(), len(d['items'])) for d in a.get_drawings()]
    db = [(d['rect'].round(), len(d['items'])) for d in b.get_drawings()]
    ok(da == db, f'student p. {i} drawings unchanged')

# The 18 networks: circles and conflict lines identical to the v1 extraction.
ext = json.load(open(os.path.join(HERE, 'extracted.json')))


sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
from extract import circles_and_segments, label_circles, group_graphs  # noqa: E402  (the math check's extractor)


def networks(page):
    """Each full-size network on a page: vertices, edges, and centres relative to its first vertex."""
    circles, segs = circles_and_segments(page)
    label_circles(page, circles)
    nets = []
    for grp in group_graphs(circles, segs):
        cs = [o for k, o in grp if k == 'c']
        ss = [o for k, o in grp if k == 's']
        lab = {id(c): ''.join(c['labels']) for c in cs}
        x0, y0 = cs[0]['cx'], cs[0]['cy']
        geo = sorted((lab[id(c)], round(c['cx'] - x0, 1), round(c['cy'] - y0, 1), round(c['w'] / MM, 1)) for c in cs)
        ends = []
        for sg in ss:
            e = sorted(lab[id(c)] for c in cs for pt in (sg['p'], sg['q'])
                       if abs(pt[0] - c['cx']) < 0.6 and abs(pt[1] - c['cy']) < 0.6)
            ends.append(e)
        nets.append((geo, sorted(ends)))
    return nets


old_nets = [n for p in OLD_S for n in networks(p)]
new_nets = [n for p in NEW_S for n in networks(p)]
ok(len(new_nets) == 18 and old_nets == new_nets,
   'the 18 networks have the same letters, conflict lines, 20 mm circles and relative positions as v1')
moved = [i + 1 for i in range(9) if [(round(c['cx'], 1), round(c['cy'], 1)) for c in circles_and_segments(OLD_S[i])[0]]
         != [(round(c['cx'], 1), round(c['cy'], 1)) for c in circles_and_segments(NEW_S[i])[0]]]
ok(moved == [3, 9], f'only the networks on pp. 3 and 9 moved, down by a few points (pages {moved})')
ext_nets = sorted((n['vertices'], n['edges']) for p in ext['pages'] for n in p['networks'])
ok(sorted(([g[0] for g in geo], ends) for geo, ends in new_nets) == ext_nets,
   "v2's networks match the math check's extraction of v1 (extracted.json)")

t1 = flat(NEW_S[0])
ok('Put each card in exactly one slot.' in t1 and 'Put every card in one slot' not in t1,
   'p. 1 rule reads "Put each card in exactly one slot" (could 6, math check item 1)')

t3 = flat(NEW_S[2])
ok(t3.count('Fewest slots:') == 2 and t3.count('Largest group:') == 2,
   'p. 3 has "Largest group:" beside each "Fewest slots:" (could 9)')
w = NEW_S[2].rect.width
rules = [d for d in NEW_S[2].get_drawings() if d['rect'].width > 0.8 * (w - 2 * 0.65 * 72) and d['rect'].height < 2 and d['rect'].y0 > 100]
ok(len(rules) == 2 and min(r['rect'].y0 for r in rules) > 450,
   'p. 3 has two full-width answer lines for the yes-or-no question (could 9)')
ok(max(r['rect'].y1 for r in rules) < 792 - 0.65 * 72, 'p. 3 answer lines sit above the bottom margin')

t7, t8 = flat(NEW_S[6]), flat(NEW_S[7])
ok('make the first-slot rule use' in t7 and 'make the rule use' not in t7 and 'first-slot rule' in t8,
   'Problems 7 and 8 both say "the first-slot rule" (could 8)')

t9 = flat(NEW_S[8])
for s in ('slots 1, 2, 3', 'slot 1', 'slot 2', 'slot 3', 'empty', 'different schedules',
          'X 1, Y 2', 'X 2, Y 1', 'X 1, Y 3'):
    ok(s in t9, f'p. 9 example shows "{s}"')
ok('place X in slot 1' not in t9 and 'two different schedules' not in t9,
   'p. 9 example no longer fixes X in slot 1 or says "two" (should 2)')
XY = ['X', 'Y'], [('X', 'Y')]
allxy = list(colourings(*XY, 3))
printed = [{'X': 1, 'Y': 2}, {'X': 2, 'Y': 1}, {'X': 1, 'Y': 3}]
ok(len(allxy) == 6 and all(c in allxy for c in printed) and len({tuple(c.values()) for c in printed}) == 3,
   'p. 9: the three printed schedules are legal and different, three of the 6 with slots 1, 2, 3')
ok(printed[1] == {'X': printed[0]['Y'], 'Y': printed[0]['X']}, 'p. 9: X 2, Y 1 is X 1, Y 2 with slots 1 and 2 switched')
ok(3 not in printed[0].values() and 2 not in printed[2].values(),
   'p. 9: the card panel (X in slot 1, Y in slot 2) leaves slot 3 empty, and X 1, Y 3 leaves slot 2 empty')

# ------------------------------------------------------------------ materials
ok(len(MAT) == 1, 'materials sheet is one page')
mt = flat(MAT[0])
ok('Week 62 / Conflict networks / Materials' in mt and 'Bellingham Math Circle / Week 62 / W62-M-v1' in mt,
   'materials header and footer W62-M-v1')
words = MAT[0].get_text('words')
toks = [x[4] for x in words if x[1] > 60 and x[3] < 740]
for L in 'ABCDEFGH':
    ok(toks.count(L) == 3, f'materials: card {L} printed 3 times (one per kit)')
for n in '1234':
    ok(toks.count(n) == 3, f'materials: header {n} printed 3 times')
ok(toks.count('slot') == 12, 'materials: 12 slot headers, so 3 kits of 8 cards and 4 headers per sheet')
xs, ys = set(), set()
for d in MAT[0].get_drawings():
    if not d.get('color') or d['color'][0] < 0.2:  # the grid is grey; skip the black header rule
        continue
    for it in d['items']:
        if it[0] == 'l':
            a, b = it[1], it[2]
            if abs(a.x - b.x) < 0.01:
                xs.add(round(a.x, 1))
            if abs(a.y - b.y) < 0.01:
                ys.add(round(a.y, 1))
xs, ys = sorted(xs), sorted(ys)
dx = {round((b - a) / MM) for a, b in zip(xs, xs[1:])}
dy = {round((b - a) / MM) for a, b in zip(ys, ys[1:])}
ok(len(xs) == 7 and len(ys) == 7 and dx == {31} and dy == {38},
   f'materials: a 6 x 6 cut grid of 31 x 38 mm cells (guide: "each 31 by 38 mm")')
dashed = [d for d in MAT[0].get_drawings() if d.get('dashes') and d['dashes'] != '[] 0']
diam = {round(d['rect'].width / MM, 1) for d in dashed}
ok(len(dashed) == 12 and diam == {16.0}, 'materials: each header has a 16 mm key circle, room for a counter up to 15 mm')
ok(3 * 3 >= 6 + 1, 'three sheets give 9 kits for the 6 working kits and 1 spare ("nine kits for the seven needed")')

# ---------------------------------------------------------------------- guide
G_OLD = 'W62-FAC-v1'
G_NEW = next(f for f in ('W62-FAC-v3', 'W62-FAC-v2') if f in flat(NEW_G[0]))  # v3 since the roster-label fix (p. 2 only)
ok(len(NEW_G) == 10, 'guide still has 10 pages, each section on its own page')
for i, p in enumerate(NEW_G, 1):
    ok(f'Bellingham Math Circle / Week 62 / {G_NEW}' in flat(p), f'guide p. {i} footer {G_NEW}')
for i in (5, 6, 10):
    ok(body(OLD_G[i - 1], G_OLD) == body(NEW_G[i - 1], G_NEW), f'guide p. {i} unchanged apart from the footer')
g = ' '.join(flat(p) for p in NEW_G)

# could 7: swapping two slot numbers changes an assignment exactly when one of them is used.
P = ['A', 'B', 'C', 'D'], edges('AB BC CD')
bad = 0
for c in colourings(*P, 4):
    used = set(c.values())
    for i, j in itertools.combinations(range(1, 5), 2):
        sw = {v: (j if s == i else i if s == j else s) for v, s in c.items()}
        if (sw != c) != bool({i, j} & used):
            bad += 1
ok(bad == 0, 'swapping two slot numbers changes a path assignment (slots 1-4) exactly when at least one is used')
ok('Swapping two slot numbers, at least one of them used, gives a different assignment.' in g,
   'guide p. 1 adds the hypothesis "at least one of them used" (could 7, math check item 3)')

# should 3: K-1 route and plain-words key.
ok('K–1 route, adult-led.' in g and 'skip the six-line network' in g, 'guide p. 4 has an adult-led K–1 route on pp. 1–2')
key = {
    'path': (['A', 'B', 'C', 'D'], edges('AB BC CD'), 2, {'A': 1, 'C': 1, 'B': 2, 'D': 2}),
    'star': (list('ABCDEF'), edges('AB AC AD AE AF'), 2, {'A': 1, 'B': 2, 'C': 2, 'D': 2, 'E': 2, 'F': 2}),
    'diamond': (list('ABCD'), edges('AB AC BC AD BD'), 3, {'A': 1, 'B': 2, 'C': 3, 'D': 3}),
    'all joined': (list('ABCD'), edges('AB AC AD BC BD CD'), 4, {'A': 1, 'B': 2, 'C': 3, 'D': 4}),
}
for name, (V, E, k, sched) in key.items():
    ok(chi(V, E) == k and all(sched[a] != sched[b] for a, b in E) and len(set(sched.values())) == k,
       f'K–1 key, {name}: {k} colours, and the schedule in words is legal')
ok('Path: two colours; A and C share one, B and D the other' in g and 'Star: two colours' in g
   and 'Diamond: three colours' in g and 'D can match C' in g and 'All joined: four colours' in g,
   'K–1 key printed in plain words')
ok(('C', 'D') not in key['diamond'][1] and ('D', 'C') not in key['diamond'][1], 'diamond: C and D are not joined, so D can match C')
ok('shallow trial entry' not in g and 'optional younger trial' not in g, 'the "shallow trial" K–1 wording is gone')

# should 1: counters carry the slot colour; enough counters of each colour.
ok("set one counter of that colour in its header's dashed circle" in g
   and "put a counter of that header's colour on the card's circle" in g
   and 'sees two different colours' in g and 'rejects a line with one colour at both ends' in g,
   'counters now mark a slot by colour, shown in the launch and used by the checker (should 1)')
nets = [(n['vertices'], n['edges']) for p in ext['pages'] for n in p['networks']]
amax = max(alpha(V, [tuple(e) for e in E]) for V, E in nets)
ok(amax <= 8 - 1, f'one counter per colour sits on its header and 7 remain; no printed network has more than {amax} cards able to share a slot')

# should 4: grades 2-3 continuations and print plan.
ok('A quick pair continues with the p. 6 tree' in g and 'the first-slot rule on p. 7' in g,
   'Grades 2–3 route names the p. 6 tree and P7 as continuations (should 4)')
sheets = 3 * 3 + 2 * 2 + 6 + 2 * 2 + 9
ok(sheets == 32 and '32 student sheets' in g and '26 student sheets' not in g,
   'print plan: pp. 1–3 x3 + pp. 6–7 x2 + pp. 4–9 + pp. 1–2 x2 + spare set = 32 sheets')

# should 5: printable cards, dry-erase markers, realistic preparation.
ok('distinct simple picture' not in g and 'week-62-materials.pdf' in g, 'cards come from the printed sheet, without pictures (should 5)')
ok(2 + 2 + 1 + 1 + 2 == 8 and 'Eight fine-tip dry-erase markers' in g,
   'markers: 2 K–1 pairs + 2 third-grade pairs + 1 upper team + demonstration + 2 spares = 8')
ok('15--20' not in g and '15–20 minutes' not in g and '20–25 minutes' in g, 'preparation estimate revised to 20–25 minutes, marked untimed')

# should 2: the guide's p. 9 note matches the new example.
ok('lists three of the six schedules of one conflicting pair with slots 1–3' in g and 'fixes X in 1' not in g,
   "guide p. 9 note matches the new example (should 2)")

out = os.path.join(HERE, 'out_check_card_fixes.txt')
open(out, 'w').write('\n'.join(OUT) + f'\n{len(OUT)} checks passed\n')
print('\n'.join(OUT))
print(f'{len(OUT)} checks passed')
