"""Read back the delivered Week 79 student PDF geometry and the guide text.

- Headers, footers, band labels and consecutive problem numbering per page.
- Opening worked visual: six bowl outlines (3 stages x A/B), equal sizes and
  equal x/y scaling, each card square mapped to the bowl that contains it and
  its printed label read; compared with a day-1 replay of the rule.
- Problem 2 cards 3, 6, 10, 20 with a Day blank under each.
- Problem 4 boards: titles, A/B labels, and no printed answer labels inside.
- Card sheet: 24 squares, side in mm, equal in x and y, labels 1..24 each
  centred in its own square, none missing or repeated.
- Mat: A and B regions, size in mm, how many 30 mm cards fit flat without
  overlap, against the 13-card peak occupancy found in check_math.py.
- Guide: reads the delivered facilitator PDF with pdftotext and confirms the
  sentences that math.md quotes or that check_math.py recomputes.
Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
Needs pdfplumber and poppler's pdftotext.
"""
import re
import subprocess
from pathlib import Path

import pdfplumber

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    four_up = here.parents[3]
    if (four_up / 'AGENTS.md').is_file():
        return four_up
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
# The reviewed v1 PDFs (organizer-approved October 15, guide corrected October 17) are
# archived since the October 23 revision (v2); this review checks them. The stored .out
# predates the October 17 correction; the hint check now quotes the corrected wording (see the guide section).
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-79' / 'archive-organizer-approved-2026-10-15'
STU = WEEK / 'week-79-students.pdf'
GUI = WEEK / 'week-79-facilitator.pdf'
PT_MM = 25.4 / 72
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def bbox(obj):
    if 'pts' in obj:
        xs = [p[0] for p in obj['pts']]
        ys = [p[1] for p in obj['pts']]
        return min(xs), min(ys), max(xs), max(ys)
    return obj['x0'], obj['top'], obj['x1'], obj['bottom']


def inside(word, box, pad=0.5):
    x0, y0, x1, y1 = box
    cx, cy = (word['x0'] + word['x1']) / 2, (word['top'] + word['bottom']) / 2
    return x0 - pad <= cx <= x1 + pad and y0 - pad <= cy <= y1 + pad


def page_text(pdf_path, page):
    return subprocess.run(['pdftotext', '-layout', '-f', str(page), '-l', str(page), str(pdf_path), '-'],
                          capture_output=True, text=True, check=True).stdout


pdf = pdfplumber.open(str(STU))
check(len(pdf.pages) == 5, f'student PDF has {len(pdf.pages)} pages (5 expected)')
for p in pdf.pages:
    check(abs(p.width - 612) < 0.5 and abs(p.height - 792) < 0.5, f'p{p.page_number}: US Letter')

# ------------------------------------------------------------ headers, footers, problems
say('== Headers, footers, problem numbering')
bands = {1: '2–5', 2: '2–5', 3: '4–5', 4: '2–5', 5: '2–5'}
probs = {}
for n in range(1, 6):
    t = page_text(STU, n)
    lines = [ln.strip() for ln in t.splitlines() if ln.strip()]
    check(lines[0] == f'Week 79 / Numbered-ball detectives / Grades {bands[n]}', f'p{n} header: {lines[0]!r}')
    check(re.match(r'Bellingham Math Circle / Week 79 / 79-ST-v1\s+%d$' % n, lines[-1]) is not None,
          f'p{n} footer: {lines[-1]!r}')
    for m in re.finditer(r'Problem (\d+):', t):
        probs[int(m.group(1))] = n
check(probs == {1: 1, 2: 2, 3: 2, 4: 3}, f'problems numbered consecutively 1-4 on pages {probs}')

# ------------------------------------------------------------ opening visual
say('== Opening worked visual (p. 1)')
p1 = pdf.pages[0]
w1 = p1.extract_words()
bowls = [bbox(c) for c in p1.curves if not c.get('fill') and (bbox(c)[2] - bbox(c)[0]) > 100]
cards = [bbox(c) for c in p1.curves if c.get('fill') and 15 < (bbox(c)[2] - bbox(c)[0]) < 30]
check(len(bowls) == 6, f'{len(bowls)} bowl outlines')
sizes = {(round(b[2] - b[0], 2), round(b[3] - b[1], 2)) for b in bowls}
check(len(sizes) == 1, f'all bowl outlines the same size {sizes} pt')
for b in cards:
    check(abs((b[2] - b[0]) - (b[3] - b[1])) < 0.05, f'card square {round(b[2]-b[0],2)} x {round(b[3]-b[1],2)} pt (equal scaling)')
cols = sorted({round(b[0], 1) for b in bowls})
stage_titles = ['Before', 'Add 1 and 2', 'Move 1 to B']
title_line = [w for w in w1 if 85 < w['top'] < 105]
state = {}
for ci, x0 in enumerate(cols):
    col = sorted([b for b in bowls if round(b[0], 1) == x0], key=lambda b: b[1])
    title = ' '.join(w['text'] for w in sorted(title_line, key=lambda w: w['x0'])
                     if col[0][0] <= (w['x0'] + w['x1']) / 2 <= col[0][2])
    check(title == stage_titles[ci], f'column {ci+1} title {title!r}')
    for bowl_name, box in zip('AB', col):
        letters = [w['text'] for w in w1 if inside(w, box) and w['text'] in 'AB' and w['x0'] < box[0] + 20]
        check(letters == [bowl_name], f'column {ci+1} {"top" if bowl_name=="A" else "bottom"} bowl labelled {letters}')
        labels = sorted(int(w['text']) for c in cards if inside({'x0': (c[0]+c[2])/2, 'x1': (c[0]+c[2])/2,
                        'top': (c[1]+c[3])/2, 'bottom': (c[1]+c[3])/2}, box)
                        for w in w1 if w['text'].isdigit() and inside(w, c))
        state[(ci, bowl_name)] = labels
say('   read:', state)
# day-1 replay of the printed rule
A, B = [], []
expected = {(0, 'A'): [], (0, 'B'): []}
A += [1, 2]
expected[(1, 'A')], expected[(1, 'B')] = sorted(A), sorted(B)
m = min(A); A.remove(m); B.append(m)
expected[(2, 'A')], expected[(2, 'B')] = sorted(A), sorted(B)
check(state == expected, f'opening stages match a replay of day 1: {expected}')

# ------------------------------------------------------------ P2
say('== Problem 2 cards (p. 2)')
p2 = pdf.pages[1]
w2 = p2.extract_words()
pcards = sorted([bbox(c) for c in p2.curves if not c.get('fill')], key=lambda b: b[0])
check(len(pcards) == 4, f'{len(pcards)} card outlines')
vals = []
for b in pcards:
    check(abs((b[2] - b[0]) - (b[3] - b[1])) < 0.05,
          f'card outline {round((b[2]-b[0])*PT_MM,1)} x {round((b[3]-b[1])*PT_MM,1)} mm')
    vals.append(' '.join(w['text'] for w in w2 if inside(w, b)))
check(vals == ['3', '6', '10', '20'], f'card labels {vals}')
days = [w for w in w2 if w['text'] == 'Day']
blanks = [l for l in p2.lines if l['top'] > 150 and l['top'] < 180]
check(len(days) == 4 and len(blanks) == 4, f'{len(days)} "Day" labels and {len(blanks)} answer blanks')
for b, d in zip(pcards, sorted(days, key=lambda w: w['x0'])):
    check(d['x0'] < (b[0] + b[2]) / 2 < d['x1'] + 45, f'"Day" blank sits under card {vals[pcards.index(b)]}')

# ------------------------------------------------------------ P4
say('== Problem 4 boards (p. 3)')
p3 = pdf.pages[2]
w3 = p3.extract_words()
boxes = sorted([bbox(r) for r in p3.rects], key=lambda b: (round(b[1]), b[0]))
check(len(boxes) == 4, f'{len(boxes)} boards')
t3 = page_text(STU, 3)
check('Move A’s smallest card' in t3 and 'Move the larger new card' in t3, 'board titles name both rules')
for i, b in enumerate(boxes):
    inner = [w['text'] for w in w3 if inside(w, b)]
    check(inner == ['AB'[i % 2]], f'board {i+1}: only its letter {inner} printed inside (no printed answer)')
    say(f'   board {i+1}: {round((b[2]-b[0])*PT_MM,1)} x {round((b[3]-b[1])*PT_MM,1)} mm')

# ------------------------------------------------------------ card sheet
say('== Card sheet (p. 4)')
p4 = pdf.pages[3]
w4 = p4.extract_words()
sq = sorted([bbox(r) for r in p4.rects], key=lambda b: (round(b[1]), b[0]))
check(len(sq) == 24, f'{len(sq)} card squares')
sides = {(round((b[2]-b[0])*PT_MM, 2), round((b[3]-b[1])*PT_MM, 2)) for b in sq}
check(sides == {(30.0, 30.0)}, f'every card is {sides} mm (square, 30 mm)')
labs = []
for b in sq:
    ws = [w for w in w4 if inside(w, b)]
    check(len(ws) == 1, f'one label in square at ({round(b[0])},{round(b[1])})')
    w = ws[0]
    cx, cy = (w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2
    centred = abs(cx - (b[0] + b[2]) / 2) < 3 and abs(cy - (b[1] + b[3]) / 2) < 4
    if not centred:
        check(False, f'label {w["text"]} centred')
    labs.append(int(w['text']))
check(labs == list(range(1, 25)), 'labels read 1..24 in reading order, none missing or repeated')

# ------------------------------------------------------------ mat
say('== A/B mat (p. 5)')
p5 = pdf.pages[4]
w5 = p5.extract_words()
mats = sorted([bbox(c) for c in p5.curves], key=lambda b: b[1])
check(len(mats) == 2, f'{len(mats)} mat regions')
for name, b in zip('AB', mats):
    wmm, hmm = (b[2]-b[0])*PT_MM, (b[3]-b[1])*PT_MM
    fit = int(wmm // 30) * int(hmm // 30)
    above = [w['text'] for w in w5 if w['bottom'] <= b[1] + 1 and w['top'] > b[1] - 40]
    check(above == [name], f'region labelled {above} above it')
    check(fit >= 13, f'region {name}: {wmm:.1f} x {hmm:.1f} mm holds {fit} flat 30 mm cards (peak need 13)')

# ------------------------------------------------------------ guide text
say('== Guide (delivered PDF) sentences checked in math.md / check_math.py')
g = re.sub(r'\s+', ' ', subprocess.run(['pdftotext', str(GUI), '-'], capture_output=True, text=True, check=True).stdout)
for phrase in [
    # The review's must 1 quoted "Problems 3–4: inspect a named finite list of labels"; the October 17 correction
    # (b29e64f) gave this archived copy "Problem 4, smallest-card rule:" (the pre-correction guide is only in git
    # history).  The current v2 guide, with one more problem, says "Problem 5, smallest-card rule:" (checked below).
    'Problem 4, smallest-card rule: inspect a named finite list of labels',
    'Any fixed finite list eventually has all its labels in B.',
    'At every positive finite day N , label N + 1 is still in A.',
    'For the changed rule, the larger new card is 2n, so it moves immediately to B.',
    'The smaller 2n − 1 never moves.',
    'Day 6 gives A = {7, . . . , 12} and B = {1, . . . , 6}.',
    'Day 10 gives A = {11, . . . , 20} and B = {1, . . . , 10}.',
    'label 3 enters on day 2 and moves on day 3',
    '20 enters on day 10 and moves on day 20',
    'label 8 enters on day 4, remains in A through day 7 and moves on day 8',
    'Day 0 is empty because no labels have entered',
    'Grades 4–5 can formulate the uniform-day obstruction and changed-rule comparison',
]:
    check(phrase in g, f'guide prints: "{phrase}"')
g_now = re.sub(r'\s+', ' ', subprocess.run(['pdftotext', str(WEEK.parent / 'week-79-facilitator.pdf'), '-'],
                                           capture_output=True, text=True, check=True).stdout)
check('Problem 5, smallest-card rule: inspect a named finite list of labels' in g_now,
      'current guide (v2) prints: "Problem 5, smallest-card rule: inspect a named finite list of labels"')
check('Day 12' not in g and '13, . . . , 24' not in g, 'guide gives no day-12 state (the page\'s printed continuation)')
check(not re.search(r'odd labels? (settle|end|are) in A|odds? in A', g),
      'guide never states the changed rule\'s settled arrangement or its finite-day answer for Problem 4')

say()
say(f'{len(FAIL)} failure(s)')
(HERE / 'check_diagrams.py.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
