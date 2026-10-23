#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes for Week 17.

    python3 review/verify_card_fixes_2026_10_23.py [build folder] [return-visit PDF]

Reads the built PDFs (default build/, as written by build.sh), the guide source in
facilitator-src/ and, when given, the return-visit packet. Checks, independently of
the drawing code:
  - the shared-ending pages (K-1 P6, Grades 2-3 P4, Grades 4-5 P2): every pair of
    printed rows is joined by one brace to one '+' and one answer line long enough
    for "can't", and each row keeps its own answer to circle; the rows are read back
    from the page;
  - the mathematics behind those pages and the guide's keys: which pairs a shared
    ending can separate, and the shortest such ending (at most two cards, as the kit
    allows);
  - the launch row R R B on the K-1 P1 machine, the K-1 P2 card count, the answer
    lines in Grades 2-3 and 4-5 P1, and the hour's table time;
  - the guide wording: four markers, partner roles, check marks in the K-1 keys, the
    Grades 4-5 route offer, and no leftover process notes;
  - the return visit's "next to each other" and what the old wording allowed;
  - the v3 and W17-RV-v2 footers.
The kit itself is measured by materials/verify_materials.py.
"""
import itertools
import json
import re
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
BUILD = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build'
RV = Path(sys.argv[2]) if len(sys.argv) > 2 else None
fails = []


def check(ok, what):
    print(('PASS ' if ok else 'FAIL ') + what)
    if not ok:
        fails.append(what)


def inch(r):
    return [v / 72 for v in r]


# ------------------------------------------------------------- the machines
def run(word, delta, start=0):
    s = start
    for c in word:
        s = delta[s][c]
    return s


EVEN = {0: {'R': 1, 'B': 0}, 1: {'R': 0, 'B': 1}}                       # K-1 P1: state 0 says yes
THREE = {i: {'R': (i + 1) % 3, 'B': i} for i in range(3)}                # groups of three: state 0 says yes


def yes3(word):
    return run(word, THREE) == 0


def shortest_split(a, b, longest=4):
    for n in range(longest + 1):
        for e in map(''.join, itertools.product('RB', repeat=n)):
            if yes3(a + e) != yes3(b + e):
                return e
    return None


# ------------------------------------------------- the shared-ending pages
PAGES = {'k-1': (5, 4, 'K'), 'grades-2-3': (3, 6, '23'), 'grades-4-5': (2, 4, '45')}
KEYS = {   # the guide's keys (pp. 5, 6 and 8): '' or a witness ending, None for impossible
    'k-1': [('', 'R', ''), ('R', 'RR', 'R'), ('RR', 'RBR', None), ('B', 'RRR', None)],
    'grades-2-3': [('', 'R', ''), ('R', 'RR', 'R'), ('RR', 'RRR', ''), ('RBR', 'RR', None), ('B', 'RRR', None),
                   ('RB', 'BR', None)],
    'grades-4-5': [('', 'R', ''), ('R', 'RR', 'R'), ('RR', 'BRR', None), ('BBB', 'RRR', None)]}
BRACE = ('c', 'l', 'c', 'c', 'l', 'c')

for band, (pno, npairs, _tag) in PAGES.items():
    page = pymupdf.open(BUILD / f'{band}.pdf')[pno - 1]
    dr = page.get_drawings()
    words = [(w[4], inch(w[:4])) for w in page.get_text('words')]
    braces = sorted((inch(d['rect']) for d in dr if d['type'] == 's' and tuple(i[0] for i in d['items']) == BRACE),
                    key=lambda r: r[1])
    check(len(braces) == npairs, f'{band} p. {pno}: {len(braces)} braces for {npairs} pairs')
    lines = [inch(d['rect']) for d in dr if d['type'] == 's' and tuple(i[0] for i in d['items']) == ('l',)
             and abs(d['rect'].y0 - d['rect'].y1) < .01]
    read = []
    ok_layout = True
    for x0, y0, x1, y1 in braces:
        inside = [(t, r) for t, r in words if r[2] < x0 and y0 <= (r[1] + r[3]) / 2 <= y1]
        rows = {}
        for t, r in inside:
            rows.setdefault(round((r[1] + r[3]) / 2, 1), []).append((r[0], t))
        rows = [' '.join(t for _x, t in sorted(v)) for _k, v in sorted(rows.items())]
        rows = ['' if r == 'no cards' else r.replace(' ', '') for r in rows]
        plus = [r for t, r in words if t == '+' and r[0] > x1 and y0 <= (r[1] + r[3]) / 2 <= y1]
        answer = [r for r in lines if r[0] > x1 and y0 <= r[1] <= y1]
        ys = sorted({round((r[1] + r[3]) / 2, 1) for t, r in inside})
        if band == 'k-1':
            per_row = [sum(1 for t, r in words if t in '✓×' and abs((r[1] + r[3]) / 2 - y) < .12) for y in ys]
            per_row_ok = per_row == [2, 2]
        else:
            per_row = [sum(1 for t, r in words if t in ('YES', 'NO') and abs((r[1] + r[3]) / 2 - y) < .12) for y in ys]
            per_row_ok = per_row == [2, 2]
        ok = (len(rows) == 2 and len(plus) == 1 and len(answer) == 1 and answer[0][2] - answer[0][0] >= 2.5
              and per_row_ok and y1 - y0 > ys[-1] - ys[0])
        ok_layout &= ok
        read.append(tuple(rows))
    check(ok_layout, f'{band} p. {pno}: each pair has two rows inside one brace, one "+" and one answer line '
          f'at least 2.5 in long to its right, and each row its own answer to circle')
    key = KEYS[band]
    check(read == [k[:2] for k in key], f'{band} p. {pno}: rows read from the page {read}')
    math_ok = True
    for a, b, witness in key:
        split = shortest_split(a, b)
        sep = (a.count('R') - b.count('R')) % 3 != 0
        math_ok &= (split is None) == (witness is None) == (not sep)
        if witness is not None:
            math_ok &= yes3(a + witness) != yes3(b + witness) and len(split) <= len(witness) <= 2
    check(math_ok, f'{band}: the guide key is right (a shared ending separates a pair exactly when the red counts '
          f'differ mod 3; each witness is a shortest one, at most 2 cards)')

# -------------------------------------------------------- other claims
k1p1 = (ROOT.parent / 'problems' / '01-k1-try-rows.md')
if not k1p1.exists():
    k1p1 = ROOT / 'problem-files' / 'problems' / '01-k1-try-rows.md'
printed = re.search(r"answer_rows\(\[(.*?)\]", k1p1.read_text()).group(1)
printed = [w.strip("' ") for w in printed.split(',')]
check(run('RRB', EVEN) == 0 and 'RRB' not in printed,
      f'launch: R R B ends on the K-1 P1 machine\'s check-mark circle and is not one of P1\'s rows {printed}')

rows_k1p2 = [''.join(t) + 'R' for t in itertools.product('RB', repeat=3)]
reds = sum(w.count('R') for w in rows_k1p2)
check(len(rows_k1p2) == 8 and reds == 20 and reds > 12,
      f'K-1 P2: the eight answers hold {reds} R cards, more than a kit\'s 12, so sort the recorded rows')

two3 = [w for w in map(''.join, itertools.product('RB', repeat=4))
        if (w.count('R') % 2 == 0) != w.endswith('R')]
four5 = [w for w in map(''.join, itertools.product('RB', repeat=5)) if w.count('R') % 3 == 0]
p23 = [inch(d['rect']) for d in pymupdf.open(BUILD / 'grades-2-3.pdf')[0].get_drawings()
       if abs(d['rect'].y0 - d['rect'].y1) < .01 and abs((d['rect'].x1 - d['rect'].x0) / 72 - 2.6) < .01]
p45 = [inch(d['rect']) for d in pymupdf.open(BUILD / 'grades-4-5.pdf')[0].get_drawings()
       if abs(d['rect'].y0 - d['rect'].y1) < .01 and abs((d['rect'].x1 - d['rect'].x0) / 72 - 1.85) < .01]
check((len(two3), len(p23), len(four5), len(p45)) == (8, 12, 11, 15),
      f'P1 lines are not answer counts: Grades 2-3 has {len(p23)} lines for {len(two3)} rows, '
      f'Grades 4-5 {len(p45)} short lines for {len(four5)} rows')

g = json.loads((ROOT / 'facilitator-src' / 'guide.json').read_text())
table = next(e['table'] for e in g['pages'][1]['elements'] if isinstance(e, dict) and 'table' in e)
spans = [tuple(map(int, r[0].split('-'))) for r in table[1:]]
work = sum(b - a for (a, b), r in zip(spans, table[1:]) if r[1][:3] in ('K-1', 'Cho'))
check(spans[0] == (0, 5) and all(spans[i][1] == spans[i + 1][0] for i in range(len(spans) - 1))
      and 35 <= work <= 40 and spans[-1][1] <= 60,
      f'hour: a 5-minute run, {work} minutes at the tables (context.md: 35-40), ending at {spans[-1][1]}')

guide = ''.join(p.get_text() for p in pymupdf.open(BUILD / 'facilitator-guide.pdf'))
flat = ' '.join(guide.split())
k1keys = ' '.join(' '.join(p.get_text().split()) for p in list(pymupdf.open(BUILD / 'facilitator-guide.pdf'))[3:5])
wording = {
    'four markers, two solid and two rings': '4 markers, two solid and two rings' in flat,
    'the kit named': 'week-17-materials.pdf' in flat,
    'partner roles': 'one turns the next card and names its arrow, the other moves the marker' in flat
                     and 'switch after each row' in flat,
    'launch on R R B': 'run it on R R B' in flat and 'on RBR' not in flat,
    'crayons at K-1': 'red and blue crayons at the K-1 table' in flat,
    'rows one above the other, both markers moved': flat.count('one above the other') >= 3
                                                   and 'move both markers' in flat,
    'K-1 keys in check marks': not re.search(r'\b(YES|NO)\b', k1keys) and '✓' in k1keys,
    'Grades 4-5 offered the Grades 2-3 machines': 'can first build the two Grades 2-3 machines' in flat,
    'no process notes': not re.search(r'FINAL|have not been edited|Artifact scope', flat),
}
for k, v in wording.items():
    check(v, f'guide: {k}')
check(len(pymupdf.open(BUILD / 'facilitator-guide.pdf')) == 11, 'guide: 11 pages, as before')

# ------------------------------------------------------------- return visit
def rr(word):
    return 'RR' in word


def two_reds(word):
    return word.count('R') >= 2


check([rr(w) for w in ('RRBB', 'RBR', 'BRRB')] == [True, False, True] and two_reds('RBR'),
      'return visit P1: with "next to each other" the guide\'s YES, NO, YES for RRBB, RBR, BRRB holds; '
      'the old "in a row" let RBR count as two reds')
if RV:
    t = ' '.join(''.join(p.get_text() for p in pymupdf.open(RV)).split())
    check('two red cards next to each other have appeared anywhere' in t and 'in a row' not in t
          and t.count('W17-RV-v2') == 3 and 'draft' not in t, 'return visit: wording and W17-RV-v2 footers')

# ------------------------------------------------------------------ footers
for band, (_p, _n, tag) in PAGES.items():
    doc = pymupdf.open(BUILD / f'{band}.pdf')
    check(all(f'Week 17 / W17-{tag}-v3' in p.get_text() for p in doc) and len(doc) == 5,
          f'{band}: five pages, every footer W17-{tag}-v3')

print(f'\n{len(fails)} failures' if fails else '\nAll card-fix checks pass.')
sys.exit(1 if fails else 0)
