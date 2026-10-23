"""Read back the delivered Week 80 student PDF geometry and the guide text.

- Page count and size; header band label, footer and problem numbers per page.
- Every timeline / strip line: length in mm (should be 180), end ticks, end labels.
- p. 1 worked visual: three equal 52 x 18 mm strips, the fold crease and the
  unfold mark at the midpoint, the fold arrow pointing from the MIDNIGHT end to
  the 11:30 end, and the 11:30 / MIDNIGHT / 11:45 labels under the right places.
- p. 2: START-END line, the counter circle (centre on the START tick, round).
- p. 3: the MIDNIGHT box against the ON/OFF card size from p. 5.
- p. 4: the two "At midnight:" boxes.
- p. 5: cut rectangles for both strips (tick distance from the cut edge), the
  ON and OFF panels (equal sizes, so they can be glued back-to-back).
- Guide: pdftotext of the delivered facilitator PDF; confirms the sentences
  math.md quotes, and records the band and mark-count wording.
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
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-80'
STU = WEEK / 'week-80-students.pdf'
GUI = WEEK / 'week-80-facilitator.pdf'
# Re-pointed on 2026-10-23: the problem-file conversions of Weeks 80 and 79 (a7cb913) removed student/students.tex,
# and the card's shoulds and coulds (bad980d) and the critic follow-up (65fb9bc) changed the packet and guide.  The
# review checks read the copies as reviewed: week-80/archive-before-card-fixes-2026-10-23/ and the reviewed
# students.tex files kept in source/week-NN/archive-before-problem-files-2026-10-23/.
STU, GUI = (WEEK / 'archive-before-card-fixes-2026-10-23' / f.name for f in (STU, GUI))
PT_MM = 25.4 / 72
OUT, FAIL = [], []
TOL = 0.05  # mm


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def finding(msg):
    """A located observation reported in math.md; not a script failure."""
    say('FINDING ' + msg)


def mm(v):
    return v * PT_MM


def box(o):
    return mm(o['x0']), mm(o['top']), mm(o['x1']), mm(o['bottom'])


def near(a, b, tol=TOL):
    return abs(a - b) <= tol


def words(page):
    return [(w['text'], mm(w['x0']), mm(w['top']), mm(w['x1']), mm(w['bottom'])) for w in page.extract_words()]


def find_word(ws, text):
    return [w for w in ws if w[0] == text]


def timeline(page, ymin=20, ymax=260):
    """Horizontal lines >= 170 mm long with vertical end ticks."""
    found = []
    for o in page.lines:
        x0, y0, x1, y1 = box(o)
        if near(y0, y1) and x1 - x0 > 170 and ymin < y0 < ymax:
            ticks = [box(t) for t in page.lines if near(box(t)[0], box(t)[2]) and box(t)[1] < y0 < box(t)[3]
                     and (near(box(t)[0], x0) or near(box(t)[0], x1))]
            if len(ticks) == 2:          # skips the header rule, which has no end ticks
                found.append(((x0, y0, x1), ticks))
    return found


say(f'repository: {REPO}')
pdf = pdfplumber.open(STU)
pages = pdf.pages
check(len(pages) == 5, f'student PDF has {len(pages)} pages (index says 5)')
check(all(near(mm(p.width), 215.9, 0.1) and near(mm(p.height), 279.4, 0.1) for p in pages), 'every page is US Letter')

say('== Headers, footers, problem numbers')
bands, probs = [], []
for i, p in enumerate(pages, 1):
    text = p.extract_text()
    first = text.splitlines()[0]
    m = re.match(r'Week 80 / Midnight laboratory / (Grades .*)', first)
    bands.append(m.group(1) if m else None)
    check(m is not None, f'p. {i} header: "{first}"')
    check('Bellingham Math Circle / Week 80 / M80-D-v1' in text.replace('BellinghamMathCircle/Week80/M80-D-v1', 'Bellingham Math Circle / Week 80 / M80-D-v1'),
          f'p. {i} footer present')
    probs += [int(n) for n in re.findall(r'Problem (\d+):', text)]
say('   bands by page:', bands)
check(probs == [1, 2, 3, 4, 5], f'problems numbered consecutively: {probs}')
check(bands == ['Grades 2–5', 'Grades 2–5', 'Grades 4–5', 'Grades 4–5', 'Grades 2–5'], 'band labels read as listed')
finding('pp. 3-4 (Problems 3-5) are headed Grades 4–5; guide p. 2 calls them a "Grades 3–5 continuation"')

say('== Timelines and strips (length between end ticks)')
for i in (1, 2, 3, 5):
    p = pages[i - 1]
    for (x0, y, x1), ticks in timeline(p):
        ws = words(p)
        below = sorted([w for w in ws if y + 2 < w[2] < y + 20], key=lambda w: w[1])
        left = below[0] if below else None
        right = below[-1] if below else None
        check(near(x1 - x0, 180.0) and len(ticks) == 2,
              f'p. {i} line at y={y:.1f} mm: {x1 - x0:.2f} mm between {len(ticks)} end ticks; labels "{left[0] if left else "-"}" ... "{right[0] if right else "-"}"')
        if left:
            check(left[1] >= x0 - 0.5 and right[3] <= x1 + 0.5, f'p. {i} end labels sit inside the ticks (left at {left[1]:.1f}, right ends {right[3]:.1f})')

say('== p. 1 worked visual')
p1 = pages[0]
ws1 = [w for w in words(p1) if 85 < w[2] < 100]   # labels under the worked visual only
rects = [box(r) for r in p1.rects]
strips = [r for r in rects if near(r[2] - r[0], 52) and near(r[3] - r[1], 18)]
check(len(strips) >= 3, f'{len(strips)} strip outlines of 52 x 18 mm (Input, Fold ghost, Unfold) + fold half')
inp = min(strips, key=lambda r: r[0])
unf = max(strips, key=lambda r: r[0])
half = [r for r in rects if near(r[2] - r[0], 26) and near(r[3] - r[1], 18)]
check(len(half) == 1, 'one folded half 26 x 18 mm (exactly half the strip)')
fold_ghost = [r for r in strips if r is not inp and r is not unf][0]
crease = [box(l) for l in p1.lines if near(box(l)[0], box(l)[2]) and l.get('dash') and l['dash'][0]]
check(len(crease) == 1 and near(crease[0][0], (fold_ghost[0] + fold_ghost[2]) / 2), f'dashed crease at x={crease[0][0]:.2f} = midpoint of the fold strip')
check(near(half[0][0], fold_ghost[0]) and near(half[0][2], crease[0][0]), 'shaded folded half is the left half, ending at the crease')
mark = [box(l) for l in p1.lines if near(box(l)[0], box(l)[2]) and l['linewidth'] > 1.0]
check(len(mark) == 1 and near(mark[0][0], (unf[0] + unf[2]) / 2), f'bold unfold mark at x={mark[0][0]:.2f} = midpoint of the unfolded strip')
lab = {t: find_word(ws1, t) for t in ('11:30', '11:45', 'MIDNIGHT', 'Input', 'Fold', 'Unfold')}
w1130 = lab['11:30'][0]
w1145 = lab['11:45'][0]
midn = lab['MIDNIGHT']
check(near(w1130[1], inp[0], 2.0), f'"11:30" starts at the Input strip left end ({w1130[1]:.1f} vs {inp[0]:.1f} mm)')
check(any(near(w[3], inp[2], 2.0) for w in midn), f'"MIDNIGHT" ends at the Input strip right end ({midn[0][3]:.1f} vs {inp[2]:.1f} mm)')
check(near((w1145[1] + w1145[3]) / 2, mark[0][0], 1.0), f'"11:45" is centred under the unfold mark ({(w1145[1] + w1145[3]) / 2:.1f} vs {mark[0][0]:.1f} mm)')
check(near(inp[0], min(box(l)[0] for l in p1.lines if near(box(l)[0], box(l)[2]) and box(l)[0] < 20)), 'Input strip: the 11:30 end tick is drawn at the paper edge')
arrow = [c for c in p1.curves if c.get('fill') and mm(c['x0']) > fold_ghost[0] and mm(c['x1']) < fold_ghost[2] and mm(c['top']) < fold_ghost[1]]
check(len(arrow) == 1 and mm(arrow[0]['x1']) < crease[0][0], 'fold arrowhead sits over the LEFT (11:30) end: the MIDNIGHT end is folded onto 11:30')
txt1 = p1.extract_text()
check('MIDNIGHTmeets11:30' in txt1.replace(' ', ''), 'fold caption "MIDNIGHT meets 11:30"')

say('== p. 2 counter board')
p2 = pages[1]
c2 = [box(c) for c in p2.curves]
check(len(c2) == 1, 'one circle drawn (the counter at START)')
cx, cy = (c2[0][0] + c2[0][2]) / 2, (c2[0][1] + c2[0][3]) / 2
(lx0, ly, lx1), _ = timeline(p2)[0]
check(near(cx, lx0) and near(cy, ly), f'counter centre ({cx:.2f}, {cy:.2f}) is on the START tick ({lx0:.2f}, {ly:.2f})')
check(near(c2[0][2] - c2[0][0], c2[0][3] - c2[0][1]), f'counter drawn round: {c2[0][2] - c2[0][0]:.2f} x {c2[0][3] - c2[0][1]:.2f} mm (equal x/y scaling)')
check('Card' in p2.extract_text() and 'Counter' in p2.extract_text(), 'Card and Counter recording columns present')

say('== p. 5 cut-out strips and ON/OFF card')
p5 = pages[4]
cut = sorted([box(r) for r in p5.rects if near(box(r)[2] - box(r)[0], 184)], key=lambda r: r[1])
check(len(cut) == 2 and all(near(r[3] - r[1], 36) for r in cut), 'two dashed strip cut rectangles, each 184 x 36 mm')
for r, ((x0, y, x1), ticks) in zip(cut, sorted(timeline(p5), key=lambda t: t[0][1])):
    check(r[1] < y < r[3] and near(x0 - r[0], 2) and near(r[2] - x1, 2),
          f'strip at y={y:.1f}: line {x1 - x0:.1f} mm, ticks {x0 - r[0]:.1f} mm in from each cut edge (the p. 1 demo draws the ticks at the paper ends; error evidence in check_math.py)')
panels = sorted([box(r) for r in p5.rects if not near(box(r)[2] - box(r)[0], 184)], key=lambda r: r[0])
psz = [(round(r[2] - r[0], 2), round(r[3] - r[1], 2)) for r in panels]
check(len(panels) == 2 and psz[0] == psz[1], f'ON and OFF panels the same size {psz}: can be glued back-to-back')
ws5 = words(p5)
for t, r in zip(('ON', 'OFF'), panels):
    w = find_word(ws5, t)[0]
    check(r[0] < w[1] and w[3] < r[2] and r[1] < w[2] and w[4] < r[3], f'"{t}" inside its panel')
card_w, card_h = psz[0]

say('== p. 3 MIDNIGHT box against the card')
p3 = pages[2]
c3 = [box(c) for c in p3.curves]
check(len(c3) == 1, 'one rounded box on p. 3')
bw, bh = c3[0][2] - c3[0][0], c3[0][3] - c3[0][1]
say(f'   MIDNIGHT box {bw:.1f} x {bh:.1f} mm; ON/OFF card {card_w} x {card_h} mm')
if bw >= card_w and bh >= card_h:
    say('ok   the cut ON/OFF card fits inside the p. 3 MIDNIGHT box')
else:
    finding(f'the {card_w} x {card_h} mm card does not fit the {bw:.0f} x {bh:.0f} mm MIDNIGHT box '
            f'(overhang {card_w - bw:.0f} mm wide, {card_h - bh:.0f} mm tall)')
mlab = [w for w in find_word(words(p3), 'MIDNIGHT') if w[2] < c3[0][1]]
check(any(c3[0][1] - w[4] > 0 for w in mlab), 'the box label MIDNIGHT sits above the box')

say('== p. 4 boxes')
p4 = pages[3]
b4 = [box(r) for r in p4.rects]
say('   boxes:', [(round(r[2] - r[0], 1), round(r[3] - r[1], 1)) for r in b4])
check(len(b4) == 2 and len(find_word(words(p4), 'midnight:')) == 2, 'two "At midnight:" boxes for the two extra rules')
pdf.close()

say('== Guide text (delivered PDF)')
g = subprocess.run(['pdftotext', str(GUI), '-'], text=True, capture_output=True, check=True).stdout
g1 = ' '.join(g.split())
quotes = [
    'switches ON at 11:30, OFF at 11:45, ON at 11:52:30, and so on',
    'They have no limit: arbitrarily close to midnight both states occur. There is no last switch before midnight.',
    'Appending ON or OFF as a separate endpoint assignment is mathematically consistent with those earlier instructions. Requiring continuity at 1 is impossible.',
    'Work on the first four halves only, leaving a physically usable gap',
    'Problems 3–5 are a Grades 3–5 continuation when endpoint discussion is ready.',
    'Grades 2–3 manipulate and compare; Grades 4–5 can separate an endpoint convention from a consequence.',
    'This is not a proof from six drawings: the rule continues for every finite number of actions.',
    'Take the odd and even post-switch subsequences; one is always ON and the other always OFF.',
    'each label there does settle, even though the total count does not pass to the membership limit',
    'Use the counter’s center as its position; stop physical moves before counter size hides the gap.',
    'Allow 15 minutes marks and flips; 10 minutes halfway-counter motion on a fresh line; 10 minutes comparing what settles; five minutes considering extra endpoint rules.',
]
for q in quotes:
    check(q in g1, 'guide contains: "' + q[:90] + ('…"' if len(q) > 90 else '"'))
finding('guide p. 3 says "six drawings" while student Problem 1 and guide p. 2 use four marks')
check(not re.search(r'\bcounter\b[^.]*\b(\d+\s*mm|diameter|size \d)', g1), 'guide gives no counter size (only "one counter")')
check('MIDNIGHT box' not in g1 and 'box' not in g1.lower(), 'guide never says what the p. 3 MIDNIGHT box is for')
check(not re.search(r'Problem 2[^0-9][^.]*card', g1), 'guide has no explicit Problem 2 answer sentence for the card (the overview covers it)')

say()
say(f'{len(FAIL)} failure(s); FINDING lines are observations reported in math.md')
(HERE / 'check_diagrams.py.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
