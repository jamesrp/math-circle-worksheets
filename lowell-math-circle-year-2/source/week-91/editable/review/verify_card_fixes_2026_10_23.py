#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes to Week 91 (plans/review/week-91.md).

    python3 verify_card_fixes_2026_10_23.py [--pdfs DIR] [--before DIR]

DIR holds the four week-91-*.pdf files (default: ../reference-pdfs). --before names a
folder of the previous print PDFs (default: the repository's
week-91/archive-before-card-fixes-2026-10-23, when present) for the unchanged-page
checks. Needs PyMuPDF.

Checks: the mathematics behind the changed keys and the new Problem 5; the K-1 key;
the return Problem 4 trace and the first-block claim; the page headers and footers;
the Problem 4 labels level with their roots; the new Problem 5 wording; the guide's
changed sentences; and that every page not meant to change differs only in its
header or footer.
"""
import argparse
import re
import sys
from itertools import product
from pathlib import Path

import pymupdf as fitz

HERE = Path(__file__).resolve().parent
MM = 72 / 25.4
FAILS = []


def check(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


# ------------------------------------------------------------------ machines
def tree_run(state, depth, n):
    """state: breadth-first cards, 'L'/'R' = next exit side. Returns the arrival word."""
    s = list(state)
    out = []
    for _ in range(n):
        node = 0
        for _ in range(depth):
            d = s[node]
            s[node] = 'R' if d == 'L' else 'L'
            node = 2 * node + (2 if d == 'R' else 1)
        out.append(chr(65 + node - (2 ** depth - 1)))
    return ''.join(out), ''.join(s)


def road_run(cards, entry, launches):
    """Road 0..m with interior cards at 1..m-1; returns exit words and the card state."""
    c = list(cards)
    ex = []
    for _ in range(launches):
        x = entry
        while 0 < x < len(c) + 1:
            d = c[x - 1]
            c[x - 1] = 'R' if d == 'L' else 'L'
            x += 1 if d == 'R' else -1
        ex.append(x)
    return ex, ''.join(c)


print('== Mathematics ==')
one = [tree_run(s, 1, 12)[0].translate(str.maketrans('AB', 'XY')) for s in 'LR']
check(one == ['XYXYXYXYXYXY', 'YXYXYXYXYXYX'], 'K-1 key: the one switch alternates, X never twice in a row')
four = {''.join(s): tree_run(s, 2, 8)[0] for s in product('LR', repeat=3)}
check(all(sorted(w[:4]) == list('ABCD') for w in four.values()), 'K-1 key: four counters reach four different exits from all 8 starts')
dfirst = {s: w for s, w in four.items() if w[0] == 'D'}
check(set(dfirst) == {'RLR', 'RRR'}, f'K-1 key and Problem 2: D first exactly from {sorted(dfirst)} (root and right child R)')
check(dfirst.get('RLR') == 'DACBDACB' and dfirst.get('RRR') == 'DBCADBCA', 'Problem 2 key table: DACB DACB and DBCA DBCA')
words4 = {w[:4] for w in four.values()}
check('ABCD' not in words4 and 'DABC' not in words4 and four['LLL'][:4] == 'ACBD' and four['LRR'][:4] == 'BDAC',
      'Problem 3: ACBD from LLL, BDAC from LRR, ABCD and DABC impossible')
check(all(not (w[1] < 'C' and w[2] < 'C') for w in words4),
      'Problem 3 key: counters 2 and 3 never both go left of the root (the reason DABC fails)')
eight = {''.join(s): tree_run(s, 3, 8)[0] for s in product('LR', repeat=7)}
check(len(eight) == 128 and len(set(eight.values())) == 128 and all(sorted(w) == list('ABCDEFGH') for w in eight.values()),
      'Problem 5: 128 starts give 128 different orders, each using every exit once')
check(eight['L' * 7] == 'AECGBFDH' and eight['R' * 7] == 'HDFBGCEA' and 'AEBFCGDH' not in eight.values()
      and 'ABCDEFGH' not in eight.values(), 'Problem 4 key: AECGBFDH all L, HDFBGCEA all R, AEBFCGDH impossible')
rev = ''.join(chr(65 + int(format(k, '03b')[::-1], 2)) for k in range(8))
check(rev == 'AECGBFDH', 'Problem 4 key: AECGBFDH is the bit-reversal order')

ex, after1 = road_run('LLR', 1, 4)
ex2, after2 = road_run(after1, 1, 4)
check(ex == [0, 0, 4, 0] and ex2 == [0, 0, 4, 0] and after1 == 'RLL' and after2 == 'RLL',
      f'return Problem 4: LLR entry 1 gives blocks {ex} {ex2} (0040 0040), states LLR, {after1}, {after2}')
bad = 0
lr = 0
for m in range(2, 11):
    for start in product('LR', repeat=m - 1):
        start = ''.join(start)
        for s in range(1, m):
            _, a = road_run(start, s, m)
            _, b = road_run(a, s, m)
            _, c = road_run(b, s, m)
            bad += not (a == b == c and 'LR' not in a)
            bad += (a != start) != ('LR' in start)
check(bad == 0, 'return Problem 4 key: for roads m <= 10, every start and entry, after one block = after two = after three, '
      'the block leaves R...RL...L, and cards change iff the start has L before R')
bad = 0
for m in (4, 5):
    for b in range(1, 2 * m + 1):
        for start in product('LR', repeat=m - 1):
            for s in range(1, m):
                cur, counts, states = ''.join(start), [], []
                for _ in range(6):
                    e, cur = road_run(cur, s, b)
                    counts.append(e.count(m))
                    states.append(cur)
                if len(set(counts)) == 1:
                    bad += len(set(states)) > 1
check(bad == 0, 'return Problem 4 key: on the printed roads, for every block size up to 2m whose counts stay equal over six blocks, '
      'the state after each block is the state after the first')

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--pdfs', type=Path, default=HERE.parent / 'reference-pdfs')
ap.add_argument('--before', type=Path, default=HERE.parents[3] / 'week-91' / 'archive-before-card-fixes-2026-10-23')
args = ap.parse_args()
flat = lambda s: ' '.join(s.split())
docs = {k: fitz.open(args.pdfs / f'week-91-{k}.pdf') for k in ('students', 'return-visit', 'materials', 'facilitator')}

print('== Headers and footers ==')
want = {'students': ['Grades 2–5'] * 3 + ['Grades 4–5'] * 2 + ['Grades 2–5']}
stu = [flat(p.get_text()) for p in docs['students']]
for i, (t, g) in enumerate(zip(stu, want['students'])):
    check(t.startswith(f'Week 91 / Rotor-router machines / {g}'), f'students p{i + 1} header {g}')
for k, f in [('students', 'F91-S-v1'), ('return-visit', 'F91-RV-v1'), ('materials', 'F91-M-v1'), ('facilitator', 'F91-FAC-v2')]:
    d = docs[k]
    check(all(f'Bellingham Math Circle / Week 91 / {f} {i + 1}' in flat(p.get_text()) for i, p in enumerate(d)),
          f'{k}: footer {f} on all {d.page_count} pages')

print('== Problem 4 labels ==')
p4 = docs['students'][3]
roots = sorted((r.y0 + r.y1) / 2 / MM for r in (dr['rect'] for dr in p4.get_drawings())
               if abs(r.width / MM - 6.6) < 0.4 and abs(r.height / MM - 6.6) < 0.4 and abs((r.x0 + r.x1) / 2 / MM - 104.9) < 0.6)
labels = []
for b in p4.get_text('dict')['blocks']:
    for ln in b.get('lines', []):
        t = ''.join(sp['text'] for sp in ln['spans']).strip()
        if t.replace(' ', '') in ('AECGBFDH', 'HDFBGCEA', 'AEBFCGDH'):
            labels.append((t, (ln['bbox'][1] + ln['bbox'][3]) / 2 / MM, ln['bbox'][1] / MM, ln['bbox'][2] / MM))
labels.sort(key=lambda r: r[1])
check(len(roots) == 3 and len(labels) == 3, f'Problem 4: three roots at y {[round(r, 1) for r in roots]} mm and three labels')
for (t, yc, top, right), ry in zip(labels, roots):
    check(abs(yc - ry) < 1.5 and right < 104.9 - 3.3, f'Problem 4: "{t}" centre {yc:.1f} mm, its root {ry:.1f} mm, label ends left of the tree')
leaf_rows = [r + 47.25 for r in roots]
for (t, yc, top, right), prev in zip(labels[1:], leaf_rows):
    check(top - (prev + 3) > 8, f'Problem 4: "{t}" starts {top - prev - 3:.1f} mm below the leaves of the tree above')

print('== Problem 5 ==')
check('Problem 5: How many different arrival orders can the eight-exit tree make? Explain why.' in stu[4],
      'Problem 5 asks how many orders the eight-exit tree makes')
check('Invent an eight-counter order' not in ' '.join(stu), 'the old Problem 5 is gone')

print('== Guide ==')
g = flat(' '.join(p.get_text() for p in docs['facilitator']))
for s in ['K–1 route, adult-read', 'Can X come twice in a row?', 'Does every exit get one?', 'Make the first counter land on D.',
          'Plain-words key', 'headed Grades 2–5', 'for an upper trio ready to continue in the same visit',
          'continues to P4 on the eight-exit tree in the same visit', 'DABC is impossible for the same root reason, one step later',
          'it is the bit-reversal order', 'Exactly 128 of the 40,320 orders', 'The first two output blocks are both 0040',
          'The cards can change only during the first block']:
    check(s in g, f'guide has "{s}"')
for s in ['deeper reason', 'both 0004', 'for ready groups', 'no multi-level coverage is implied', 'invent a balanced but impossible order',
          'Sleeve boards if available', 'A complete apparatus set']:
    check(s not in g, f'guide no longer has "{s}"')
heading_ok = False
for p in docs['facilitator']:
    for b in p.get_text('dict')['blocks']:
        for ln in b.get('lines', []):
            t = ''.join(sp['text'] for sp in ln['spans']).strip()
            if 'First packet: operating and programming' in t:
                heading_ok = t == 'First packet: operating and programming'
check(heading_ok, 'guide: "First packet: operating and programming" heading stands on its own line')

print('== Unchanged pages ==')
if not args.before.is_dir():
    print(f'SKIP no previous PDFs at {args.before}')
else:
    norm = lambda t: re.sub(r'(students|return-visit|materials)-v1|F91-(S|RV|M)-v1', 'FOOTER', re.sub(r'Grades [2-5]–[2-5]', 'GRADES', t))
    same = {'students': [1, 2, 3, 4, 6], 'return-visit': [1, 2, 3, 4], 'materials': [1, 2, 3, 4, 5, 6, 7]}
    for k, pages in same.items():
        old = fitz.open(args.before / f'week-91-{k}.pdf')
        new = docs[k]
        for n in pages:
            a, b = old[n - 1], new[n - 1]
            ta, tb = norm(flat(a.get_text())), norm(flat(b.get_text()))
            check(ta == tb, f'{k} p{n}: text unchanged apart from header grades and footer')
            clip = fitz.Rect(0, 22 * MM, a.rect.width, a.rect.height - 22 * MM)
            if k == 'students' and n == 4:
                continue  # labels moved on purpose
            pa = a.get_pixmap(dpi=100, clip=clip, colorspace=fitz.csGRAY).samples
            pb = b.get_pixmap(dpi=100, clip=clip, colorspace=fitz.csGRAY).samples
            diff = sum(abs(x - y) > 64 for x, y in zip(pa, pb)) if len(pa) == len(pb) else -1
            check(0 <= diff <= 200, f'{k} p{n}: body pixels between header and footer match ({diff} differ at 100 dpi; glyph antialiasing allowance 200)')

print()
print(f'{len(FAILS)} failure(s)')
sys.exit(1 if FAILS else 0)
