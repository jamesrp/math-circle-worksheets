#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes in the built Week 74 PDFs.

    python3 verify_card_fixes_2026_10_23.py [DIR]

DIR holds week-74-students.pdf, week-74-facilitator.pdf and week-74-materials.pdf
(default: ../reference-pdfs). Needs PyMuPDF (pip install pymupdf). It reads the
rendered pages, not the sources: the footers, the student wording changes, every
board's column labels, Problem 4's answer lines, the stride-strip tick positions
against the board's dot pitch, and the guide's new sentences.
"""
import sys
from pathlib import Path
import pymupdf as fitz

HERE = Path(__file__).resolve().parent
DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / 'reference-pdfs'
FAIL = []


def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg)
    if not ok:
        FAIL.append(msg)


def flat(page):
    return ' '.join(page.get_text().split())


S = fitz.open(DIR / 'week-74-students.pdf')
G = fitz.open(DIR / 'week-74-facilitator.pdf')
M = fitz.open(DIR / 'week-74-materials.pdf')
check(len(S) == 4 and len(G) == 3 and len(M) == 1, f'page counts 4/3/1: {len(S)}/{len(G)}/{len(M)}')
for i, p in enumerate(S):
    check('Week 74 / GGT74-S-v2' in flat(p), f'student p.{i+1} footer GGT74-S-v2')
for i, p in enumerate(G):
    check('Week 74 / GGT74-FAC-v2' in flat(p), f'guide p.{i+1} footer GGT74-FAC-v2')
check('Week 74 / GGT74-M-v1' in flat(M[0]), 'materials footer GGT74-M-v1')

# Coulds 6 and 7: "marker", and no restated start in Problem 3.
text = ' '.join(flat(p) for p in S)
check(flat(S[0]).startswith('Week 74 / Doubling elevators / Grades 4–5 Move a marker.'), 'p.1 opens "Move a marker."')
check('pawn' not in text, 'no "pawn" on the student pages')
check('Problem 3: With each move budget, finish as far right as possible on level 0.' in text, 'Problem 3 starts with the budget task')
check('Start at 0 on level 0' not in text, 'Problem 3 no longer restates the start')

# Could 4: every column labelled, centred on its column, on the three boards.
pitch = .23 * 72
for n in (1, 2, 4):
    page = S[n - 1]
    words = page.get_text('words')
    y_axis = sorted((w for w in words if w[4] == 'ground'), key=lambda w: -w[1])  # the board's axis title
    labels = {}
    for w in words:
        if y_axis and 5 < y_axis[0][1] - w[1] < 30 and w[4].lstrip('-').isdigit():
            labels[int(w[4])] = (w[0] + w[2]) / 2
    xs = [labels.get(x) for x in range(-4, 25)]
    ok = None not in xs and all(abs((xs[i] - xs[0]) - i * pitch) < .6 for i in range(len(xs)))
    check(ok, f'p.{n} board labels -4..24 all present, {pitch:.2f} pt apart')

# Could 5: Problem 4 has eight answer lines.
p3 = S[2]
y4 = p3.search_for('Problem 4:')[0].y1
rules = sorted({round(d['rect'].y0, 1) for d in p3.get_drawings()
                if d['rect'].y0 > y4 and d['rect'].width > 400 and d['rect'].height < 2})
check(len(rules) == 8, f'Problem 4 answer lines: {len(rules)}')

# Should 2: stride-strip ticks at 1, 2, 4, 8 and 16 board dot spaces from 0.
page = M[0]
ticks = [d['rect'] for d in page.get_drawings() if d['rect'].width < 1.5 and 20 < d['rect'].height < 30]
rows = {}
for r in ticks:
    rows.setdefault(round(r.y0), []).append((r.x0 + r.x1) / 2)
want = [0, .23, .46, .92, 1.84, 3.68]
good = [sorted(xs) for xs in rows.values() if len(xs) == 6]
check(len(good) == 10, f'ten strips with six ticks each: {len(good)}')
err = max(abs((xs[i] - xs[0]) / 72 - want[i]) for xs in good for i in range(6))
check(err < .002, f'tick offsets 0.23, 0.46, 0.92, 1.84, 3.68 in, worst error {err:.4f} in')

# Should 1, 2, 3 and could 8 in the guide.
g = ' '.join(flat(p) for p in G)
for phrase in ['these are the only two eight-move trips',
               'A different claimed route of eight or fewer moves has a replay error',
               'a stride strip cut from week-74-materials.pdf',
               'the 4 tick lands on (5, 2)',
               'The other tables that hour.',
               'Eight takes 6 moves, by exactly two trips, URRRRD and UURRDD',
               'to 4 both take 4 moves',
               'reach 4, 8, 16, 32',
               'is 2k moves for k ≥1']:
    check(phrase in g, f'guide says "{phrase}"')
check('Do not reject different routes' not in g, 'the old Problem 2 sentence is gone')
check('even when its label is not printed' not in g, 'the stale unlabelled-column sentence is gone')
print('RESULT: ' + ('all checks pass' if not FAIL else f'{len(FAIL)} failed'))
sys.exit(1 if FAIL else 0)
