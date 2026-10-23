"""Check of the Week 63 K-1 route and card fixes, October 23, 2026 (written for the card fixes).

The K-1 route (guide p. 3): the launch; P1, both questions; P2's two-ring sort up to
"How many rows are outside both groups?"; P3 split by the card in home A, one branch
per pair, pooled to nine; then aloud, "Can exactly three of A, B, C, D be home?".
This script enumerates every row itself (itertools, not rows63 or the package
verifiers) and checks:

  * the counts the route and the revised pages rely on: D3 = 2 with no row of exactly
    two matches; P2's three rows outside both groups; P3's 9 = 3 + 3 + 3 by the card in
    home A; no four-card row with exactly three matches; P4 = 14; P5 = 9; P8 = 11;
    each of E's four homes gives 11, pooled 44; the rule from D1 = 0, D2 = 1 for n >= 3;
  * with PDFs given: the guide's K-1 key lists exactly those rows; the student headers
    (K-5 on pp. 1-3) and footers W63-S-v4 (v3 before the critic follow-up); p. 8 without the worked removals and with
    twelve A-E boards; p. 9's "three or more" and "homes B, C, D"; and on materials
    pp. 1-2 that every home letter, outcome letter and group label has, just to its
    right or left, the picture of that letter's card (circle, triangle, square,
    diamond, star), classified from the PDF's own vector paths.

Run: python3 check_k1_route.py [students.pdf materials.pdf facilitator.pdf]
     (writes out_check_k1_route.txt beside itself; the recorded run used the print copies)
"""
import itertools
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def rows(labels):
    return [''.join(p) for p in itertools.permutations(labels)]


def home_matches(labels, row):
    return {h for h, c in zip(labels, row) if h == c}


def home_free(labels):
    return [r for r in rows(labels) if not home_matches(labels, r)]


say('== Counts the K-1 route and the revised pages use ==')
three = home_free('ABC')
check(three == ['BCA', 'CAB'], f'P1: home-free A-C rows {three}')
check(not [r for r in rows('ABC') if len(home_matches('ABC', r)) == 2], 'P1: no A-C row has exactly two home matches')
a_home = [r for r in rows('ABC') if r[0] == 'A']
b_home = [r for r in rows('ABC') if r[1] == 'B']
outside = [r for r in rows('ABC') if r not in a_home and r not in b_home]
check(a_home == ['ABC', 'ACB'] and b_home == ['ABC', 'CBA'] and set(a_home) & set(b_home) == {'ABC'},
      f'P2: A-home {a_home}, B-home {b_home}, shared ABC')
check(outside == ['BAC', 'BCA', 'CAB'] and len(outside) == 6 - 2 - 2 + 1, f'P2: outside both {outside} = 6-2-2+1')
four = home_free('ABCD')
branches = {x: [r for r in four if r[0] == x] for x in 'BCD'}
check(len(four) == 9 and all(len(v) == 3 for v in branches.values()), f'P3: 9 home-free A-D rows, by home A {branches}')
check(not [r for r in rows('ABCD') if len(home_matches('ABCD', r)) == 3],
      'aloud: no A-D row has exactly three home matches (the fourth card is forced home)')
p4 = [r for r in rows('ABCD') if r[0] != 'A' and r[1] != 'B']
check(len(p4) == 14 == 24 - 6 - 6 + 2, 'P4: 14 rows with A and B away = 24-6-6+2')
check(len(four) == 24 - 4 * 6 + 6 * 2 - 4 * 1 + 1, 'P5: 24-24+12-4+1 = 9')
five = home_free('ABCDE')
e_branch = {h: [r for r in five if r['ABCDE'.index(h)] == 'E'] for h in 'ABCD'}
check(len(e_branch['A']) == 11, f'P8: E in home A gives {len(e_branch["A"])} rows')
recip = [r for r in e_branch['A'] if r[4] == 'A']
check(len(recip) == 2 and len(e_branch['A']) - len(recip) == 9, 'P8: 2 reciprocal (A in home E) and 9 longer rows')
check(all(len(v) == 11 for v in e_branch.values()) and len(five) == 44, 'P9: each of E\'s four homes gives 11; pooled 44')
D = {1: 0, 2: 1}
for n in range(3, 7):
    D[n] = (n - 1) * (D[n - 1] + D[n - 2])
check([D[n] for n in range(3, 7)] == [len(home_free('ABCDEF'[:n])) for n in range(3, 7)],
      f'rule from D1 = 0, D2 = 1: D3..D6 = {[D[n] for n in range(3, 7)]} match enumeration')


def text(pdf):
    return subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True, check=True).stdout


if len(sys.argv) == 4:
    import pymupdf
    students, materials, guide = sys.argv[1:]
    say('')
    say(f'== Guide K-1 page: {guide} ==')
    gdoc = pymupdf.open(guide)
    k1 = ' '.join(gdoc[2].get_text().split())
    check('The K–1 route at the parent' in k1, 'guide p. 3 is the K-1 route page')
    m = re.search(r'Key: two rows, (B C A) and (C A B)', k1)
    check(m and [g.replace(' ', '') for g in m.groups()] == three, 'key P1 lists BCA and CAB')
    m = re.search(r'A-home holds (\w+) and (\w+); B-home holds (\w+) and (\w+);.*?Outside both: (\w+), (\w+) and (\w+)', k1)
    check(m and list(m.groups()) == a_home + b_home + outside, f'key P2 groups and outside rows {m and m.groups()}')
    m = re.search(r'B in home A gives (\w+), (\w+), (\w+); C gives (\w+), (\w+), (\w+); D gives (\w+), (\w+), (\w+)\.', k1)
    check(m and list(m.groups()) == branches['B'] + branches['C'] + branches['D'], 'key P3 lists the three branches exactly')
    check('Can exactly three of A, B, C, D be home?' in k1 and 'Key: no' in k1, 'key: exactly three of four home is impossible')
    p9g = ' '.join(gdoc[9].get_text().split())
    check('For three or more distinct cards, starting from' in p9g, 'guide P9 rule stated for three or more from D1, D2')

    say('')
    say(f'== Student packet: {students} ==')
    sdoc = pymupdf.open(students)
    check(len(sdoc) == 9, f'{len(sdoc)} pages')
    want = {1: 'K–5', 2: 'K–5', 3: 'K–5', 4: '3–5', 5: '3–5', 6: '4–5', 7: '4–5', 8: '4–5', 9: '4–5'}
    for i, page in enumerate(sdoc, 1):
        t = page.get_text()
        check(f'Week 63 / Cards away from home / Grades {want[i]}' in t and 'Bellingham Math Circle / Week 63 / W63-S-v4' in t
              and re.findall(r'Problem (\d+):', t) == [str(i)], f'p. {i}: Grades {want[i]}, W63-S-v4, Problem {i}')
    p1 = ' '.join(sdoc[0].get_text().split())
    check('different rows count separately' not in p1, 'p. 1: "different rows count separately" removed (could 7)')
    p2 = ' '.join(sdoc[1].get_text().split())
    check('It can belong to several groups' not in p2 and 'Group the outcome cards on the table' not in p2
          and 'A card may belong to both groups' in p2, 'p. 2: one statement of shared membership (could 6)')
    p8 = sdoc[7]
    t8 = ' '.join(p8.get_text().split())
    check('Remove both' not in t8 and 'becomes' not in t8 and 'These examples remove U' not in t8
          and 'smaller home-free rows? A smaller row keeps its letters.' in t8, 'p. 8: worked removals gone; the letters convention kept, inside P8 since the critic follow-up (should 2)')
    cells = [d for d in p8.get_drawings() if abs(d['rect'].width * 25.4 / 72 - 12) < 0.05 and abs(d['rect'].height * 25.4 / 72 - 10) < 0.05]
    check(len(cells) == 60, f'p. 8: {len(cells)} cells of 12 x 10 mm = twelve A-E boards (should 3)')
    t9 = ' '.join(sdoc[8].get_text().split())
    check('three or more distinct cards' in t9 and 'Choose one of homes B, C, D for E' in t9,
          'p. 9: "three or more" (should 4) and "homes B, C, D" (could 8)')

    say('')
    say(f'== Materials pictures: {materials} ==')
    mdoc = pymupdf.open(materials)
    check(len(mdoc) == 3 and all('W63-M-v3' in p.get_text() for p in mdoc), 'three pages, footer W63-M-v3')
    SHAPE = {'A': 'circle', 'B': 'triangle', 'C': 'square', 'D': 'diamond', 'E': 'star'}

    def kind(d):
        items = d['items']
        if d['fill'] is None or not items:
            return None
        if all(it[0] == 'c' for it in items) and len(items) == 4:
            return 'circle'
        if len(items) == 1 and items[0][0] == 're':
            r = items[0][1]
            return 'square' if abs(r.width - r.height) < 0.05 else None
        if all(it[0] == 'l' for it in items):
            pts = [items[0][1]] + [it[2] for it in items]
            if math.dist(pts[0], pts[-1]) < 0.01:
                pts.pop()
            sides = [math.dist(pts[j], pts[(j + 1) % len(pts)]) for j in range(len(pts))]
            if len(pts) == 3 and max(sides) - min(sides) < 0.05:
                return 'triangle'
            if len(pts) == 4 and max(sides) - min(sides) < 0.05:
                axis = all(abs(pts[j].x - pts[(j + 1) % 4].x) < 0.01 or abs(pts[j].y - pts[(j + 1) % 4].y) < 0.01 for j in range(4))
                return 'square' if axis else 'diamond'
            if len(pts) == 10:
                return 'star'
        return None

    def pictures(page):
        out = []
        for d in page.get_drawings():
            k = kind(d)
            if k:
                out.append((k, d['rect']))
        return out

    def beside(page, word, pics, side='right'):
        x0, y0, x1, y1 = word[:4]
        cy = (y0 + y1) / 2
        best = None
        for k, r in pics:
            if abs((r.y0 + r.y1) / 2 - cy) > 3.5:
                continue
            gap = r.x0 - x1 if side == 'right' else x0 - r.x1
            if 0 <= gap < 16 and (best is None or gap < best[0]):  # points; within 5.6 mm
                best = (gap, k, r)
        return best

    page = mdoc[0]
    pics = pictures(page)
    homes = [d['rect'] for d in page.get_drawings()
             if abs(d['rect'].width * 25.4 / 72 - 35) < 0.05 and abs(d['rect'].height * 25.4 / 72 - 45) < 0.05]
    ok = len(homes) == 10
    for r in homes:
        letters = [w for w in page.get_text('words', clip=r) if re.fullmatch('[A-E]', w[4])]
        b = beside(page, letters[0], pics) if len(letters) == 1 else None
        band = b and b[2].y0 >= r.y0 - 0.01 and b[2].y1 <= r.y0 + 5 * 72 / 25.4
        ok = ok and bool(b) and b[1] == SHAPE[letters[0][4]] and bool(band)
        say(f'     home {letters[0][4] if letters else "?"}: picture {b and b[1]}, {b and round(b[2].height * 25.4 / 72, 2)} mm tall, in top 5 mm band {bool(band)}')
    check(ok, 'p. 1: all ten home cells show their own card\'s picture beside the letter, inside the top 5 mm band')

    page = mdoc[1]
    pics = pictures(page)
    frames = [d['rect'] for d in page.get_drawings()
              if abs(d['rect'].width * 25.4 / 72 - 56) < 0.05 and abs(d['rect'].height * 25.4 / 72 - 27) < 0.05]
    seen, ok = [], True
    for r in frames:
        words = page.get_text('words', clip=r)
        ids = [w[4] for w in words if re.fullmatch('[A-C]{3}', w[4])]
        if not ids:
            continue
        letters = [w for w in words if re.fullmatch('[A-C]', w[4])]
        top = sorted([w for w in letters if (w[1] + w[3]) / 2 - r.y0 < 9 * 72 / 25.4], key=lambda w: w[0])
        cards = sorted([w for w in letters if w not in top], key=lambda w: w[0])
        good = (''.join(w[4] for w in top) == 'ABC' and ''.join(w[4] for w in cards) == ids[0]
                and all((b := beside(page, w, pics)) and b[1] == SHAPE[w[4]] for w in top + cards))
        ok = ok and good
        seen.append(ids[0])
    check(ok and sorted(seen) == rows('ABC'), f'p. 2: all six A-C outcomes {sorted(seen)}: every home and card letter has its own picture beside it')
    lab_ok = 0
    for w in page.get_text('words'):
        if re.fullmatch('[A-E]', w[4]):
            nxt = [v for v in page.get_text('words') if abs(v[1] - w[1]) < 1 and 0 < v[0] - w[2] < 4 and v[4] == 'in']
            if nxt:
                b = beside(page, w, pics, side='left')
                lab_ok += bool(b and b[1] == SHAPE[w[4]])
    check(lab_ok == 5, f'p. 2: {lab_ok} of 5 group labels show their card\'s picture to the left')

with open(os.path.join(HERE, 'out_check_k1_route.txt'), 'w') as f:
    f.write('\n'.join(OUT) + f'\n\nFAILURES: {len(FAIL)}\n')
print('\n'.join(OUT) + f'\n\nFAILURES: {len(FAIL)}')
sys.exit(1 if FAIL else 0)
