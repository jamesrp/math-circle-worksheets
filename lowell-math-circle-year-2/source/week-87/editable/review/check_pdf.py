#!/usr/bin/env python3
"""Read the Week 87 PDFs and check the October 23, 2026 card fixes on the printed pages.

    python3 check_pdf.py [FOLDER]   (FOLDER holds week-87-shared/line/upper/materials/
                                     facilitator.pdf; default: the repository's print folder)

With PyMuPDF it reads every 0-10 number line (the row of labels 0..10, the axis above it,
its ticks), every favorite stem (a vertical segment ending just above the axis) and every
V label above a stem, and checks that
- every stem on every line has the same length, so no stem marks a voter (fix 1);
- each line's favorites, read voter by voter from the stem under each label, are the ones
  the guide and check_card_fixes_2026_10_23.py use, with line P2's third set numbered out
  of left-to-right order;
- labels of voters who share a favorite stack over the one stem, and all other labels sit
  at one height;
- upper Problem 2's work line has eleven evenly spaced ticks (fix 10).
It also checks headers, footers and problem numbers, the revised and removed sentences on
the student pages and in the guide, and that every knockout-mat box on materials p. 4 is
at least 5 mm wider and 11 mm taller than the 28 mm tiles it must hold (fix 11).
"""
import re
import subprocess
import sys
from pathlib import Path

try:
    import pymupdf as fitz  # PyMuPDF >= 1.24
except ImportError:
    import fitz  # older PyMuPDF

HERE = Path(__file__).resolve().parent


def find_repo():
    for p in HERE.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    sys.exit('repository not found; pass the folder that holds the PDFs')


WEEK = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else find_repo() / 'lowell-math-circle-year-2' / 'week-87'
MM = 72 / 25.4
FAILS = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def words(page):
    return [(w[0], w[1], w[2], w[3], w[4]) for w in page.get_text('words')]


def text(page):
    """The page's words on one line, with words hyphenated across a line break rejoined."""
    return ' '.join(re.sub(r'(?<=[a-z])-\n(?=[a-z])', '', page.get_text()).split())


def segments(page):
    out = []
    for d in page.get_drawings():
        for it in d['items']:
            if it[0] == 'l':
                out.append((it[1].x, it[1].y, it[2].x, it[2].y))
    return out


def number_lines(page):
    """Each 0..10 line: axis y, tick x's, stems [(x, top, bottom)], labels {V: (x, y)}."""
    W, S = words(page), segments(page)
    found = []
    for z in [w for w in W if w[4] == '0']:
        row = sorted((w for w in W if abs(w[1] - z[1]) < 1 and re.fullmatch(r'\d+', w[4])), key=lambda w: w[0])
        if [w[4] for w in row] != [str(i) for i in range(11)]:
            continue
        axis = max((s for s in S if abs(s[1] - s[3]) < 0.1 and 0 < z[1] - s[1] < 12 and s[0] < z[2] + 6), key=lambda s: s[1])
        ay = axis[1]
        ticks = sorted({round(s[0], 2) for s in S if abs(s[0] - s[2]) < 0.1 and min(s[1], s[3]) < ay < max(s[1], s[3]) and abs(s[1] - s[3]) < 20})
        stems = sorted({(round(s[0], 2), round(min(s[1], s[3]), 2), round(max(s[1], s[3]), 2)) for s in S
                        if abs(s[0] - s[2]) < 0.1 and max(s[1], s[3]) < ay and ay - max(s[1], s[3]) < 7})
        # a label starts 4 mm left of its stem, so the stem passes under the label's right half
        labels = {w[4]: (next(st[0] for st in stems if w[0] <= st[0] <= w[2] + 3), w[3]) for w in W
                  if re.fullmatch(r'V\d', w[4]) and 0 < ay - w[3] < 80 and any(w[0] <= st[0] <= w[2] + 3 for st in stems)}
        found.append({'y': ay, 'ticks': ticks, 'stems': stems, 'labels': labels})
    return sorted(found, key=lambda n: n['y'])


def favorites(nl):
    """Voter-by-voter tick values, the set of stem lengths (mm) and the label heights by place."""
    favs, heights = {}, {}
    for v, (x, bottom) in nl['labels'].items():
        stem = min(nl['stems'], key=lambda st: abs(st[0] - x))
        tick = min(range(len(nl['ticks'])), key=lambda i: abs(nl['ticks'][i] - stem[0]))
        favs[v] = tick
        heights.setdefault(tick, []).append((round((nl['y'] - bottom) / MM, 1), v))
    lengths = {round((st[2] - st[1]) / MM, 2) for st in nl['stems']}
    return [favs[v] for v in sorted(favs)], lengths, heights


def header_footer(doc, band, ident):
    nums = []
    for i, page in enumerate(doc):
        t = text(page)
        check(t.startswith(f'Week 87 / Voting and agendas / {band}') and f'Bellingham Math Circle / Week 87 / {ident} {i+1}' in t,
              f'{Path(doc.name).name} p{i+1}: header {band}, footer {ident}, page {i+1}')
        nums += [int(n) for n in re.findall(r'Problem (\d+):', t)]
    return nums


shared = fitz.open(WEEK / 'week-87-shared.pdf')
line = fitz.open(WEEK / 'week-87-line.pdf')
upper = fitz.open(WEEK / 'week-87-upper.pdf')
materials = fitz.open(WEEK / 'week-87-materials.pdf')
check(header_footer(shared, 'Grades 2–5', 'W87-S-v1') == [1, 2, 3] and len(shared) == 3, 'shared: 3 pages, Problems 1-3')
check(header_footer(line, 'Grades 3–5', 'W87-L-v1') == [1, 2, 3, 4] and len(line) == 4, 'line: 4 pages, Problems 1-4')
check(header_footer(upper, 'Grades 4–5', 'W87-U-v1') == [1, 2] and len(upper) == 2, 'upper: 2 pages, Problems 1-2')

# Fix 1: equal stems, the printed favorites, stacked labels only where favorites coincide
expected = {0: [[0, 2, 4, 7, 10]], 1: [[0, 0, 0, 8, 10], [1, 4, 4, 4, 9], [9, 1, 10, 6, 0]], 2: [[]], 3: [[1, 3, 7, 9], []]}
all_lengths = set()
for pn, exp in expected.items():
    nls = [n for n in number_lines(line[pn]) if len(n['ticks']) == 11 and n['ticks'][-1] - n['ticks'][0] > 150 * MM]
    got, lengths = [], set()
    for n in nls:
        favs, ls, heights = favorites(n)
        got.append(favs)
        lengths |= ls
        level = sorted({h[0][0] for h in heights.values()})
        stacks_ok = all([round(h - heights[t][0][0], 1) for h, _ in sorted(heights[t])] == [7.0 * k for k in range(len(heights[t]))]
                        and [v for _, v in sorted(heights[t])] == sorted(v for _, v in heights[t]) for t in heights)
        check(len(level) <= 1 and stacks_ok, f'line p{pn+1} y={n["y"] / MM:.0f} mm: lowest labels at one height {level} mm above the axis; shared favorites stack 7 mm apart in voter order')
    all_lengths |= lengths
    check(got == exp, f'line p{pn+1}: favorites by voter {got}')
check(all_lengths == {4.0}, f'line pp. 1-4: every favorite stem is 4 mm long {sorted(all_lengths)}')
p2 = [n for n in number_lines(line[1]) if len(n['ticks']) == 11]
third = favorites(p2[2])[0]
check(third != sorted(third) and third.index(6) == 3, 'line P2 third set is numbered out of left-to-right order; the winner 6 is V4')

nls = number_lines(upper[1])
small = [n for n in nls if n['ticks'][-1] - n['ticks'][0] < 60 * MM]
work = [n for n in nls if n['ticks'][-1] - n['ticks'][0] > 150 * MM]
check(len(small) == 1 and favorites(small[0])[0] == [1] and favorites(small[0])[1] == {4.0}, 'upper p2 worked example: V1 at 1 on a 4 mm stem (unchanged)')
gaps = [b - a for a, b in zip(work[0]['ticks'], work[0]['ticks'][1:])] if work else []
check(len(work) == 1 and len(work[0]['ticks']) == 11 and max(gaps) - min(gaps) < 0.05 and abs(gaps[0] - 17 * MM) < 0.05,
      'upper P2 work line: ticks 0-10, 17 mm apart (fix 10)')

# Revised and removed sentences on the student pages
st = {name: [text(p) for p in doc] for name, doc in [('shared', shared), ('line', line), ('upper', upper)]}
check('The same cards stay visible' not in st['shared'][1], 'shared p2: "The same cards stay visible in both rounds" removed (fix 7)')
check(st['shared'][2].startswith('Week 87 / Voting and agendas / Grades 2–5 Problem 3: Each ranking card must contain A, B and C once. Make three different cards')
      and 'Keep each set of cards unchanged' not in st['shared'][2], 'shared P3: the card rule opens the problem; the repeated "keep unchanged" is gone (fix 6)')
check('Keep X/Y proposals on the board' not in st['line'][0] and 'Use only the numbered ticks.' in st['line'][0], 'line p1: the proposal/tally-label sentence moved to the guide (fix 12)')
check('third favorite' not in st['line'][2] and 'How can you tell which location beats every other location without trying every vote? Explain why your way always works.' in st['line'][2],
      'line P3: asks how to tell the winner; the third-favorite question is now a held prompt (fix 2)')
check('for each set of cards? Explain how you can tell without playing every knockout.' in st['upper'][0] and 'pair votes' not in st['upper'][0], 'upper P1: "for each set", "Explain how you can tell" (fix 9)')
check('Favorite markers above' not in st['upper'][1], 'upper p2: "Favorite markers above; letter tiles below" removed (fix 8)')

# Fix 11: knockout mat boxes on materials p. 4
page = materials[3]
W = words(page)
rects = [d['rect'] for d in page.get_drawings() if d['rect'].width > 5 and d['rect'].height > 5]
boxes = {}
for r in rects:
    # a box's label is the words in its top-left corner, on one baseline
    lab = ' '.join(w[4] for w in sorted(W, key=lambda w: w[0]) if r.x0 < w[0] < r.x1 and r.y0 < w[1] < r.y0 + 5 * MM)
    tiles = {'First pair': 2, 'Waiting': 1, 'Out': 2, 'First winner': 1, 'Final pair': 2, 'Winner': 1}.get(lab)
    if tiles:
        boxes[lab] = (r.width / MM, r.height / MM, tiles)
check(set(boxes) == {'First pair', 'Waiting', 'Out', 'First winner', 'Final pair', 'Winner'}, f'materials p4: six knockout boxes found {sorted(boxes)}')
for name, (w, h, tiles) in sorted(boxes.items()):
    check(w - 28 * tiles >= 5 - 0.05 and h - 28 >= 11 - 0.05, f'materials p4 {name}: {w:.1f} x {h:.1f} mm holds {tiles} tile(s) of 28 mm with {w - 28 * tiles:.1f} mm to spare across, {h - 28:.1f} mm down')
frame = [r for r in rects if abs(r.width / MM - 175) < 0.2 and abs(r.height / MM - 100) < 0.2]
inner = [r for r in rects if frame and r != frame[0] and frame[0].y0 < r.y0 < frame[0].y1]
check(len(frame) == 1 and len(inner) == 6 and all(frame[0].x0 + 2 * MM <= r.x0 and r.x1 <= frame[0].x1 - 2 * MM and r.y1 <= frame[0].y1 - 2 * MM for r in inner)
      and not any(a != b and a.intersects(b) for a in inner for b in inner),
      'materials p4: the knockout mat is still 175 x 100 mm; its six boxes sit at least 2 mm inside it and do not overlap')

# The guide
g = ' '.join(subprocess.run(['pdftotext', str(WEEK / 'week-87-facilitator.pdf'), '-'], capture_output=True, text=True, check=True).stdout.split())
g = g.replace('- ', '-')
for s in ['K–1 route (adult-led)', 'Plain-words key: A beats B, B beats C and C beats A, each two tokens to one',
          'Upper Problem 1 continues the same visit after shared Problem 2',
          'Three different cards cannot share a first choice, since only two rankings start with each letter.',
          'Every working set uses exactly the cards ABC, BCA, CAB or ACB, CBA, BAC, in some order.',
          'so no voter number points to the winner', 'Does the third favorite from the left always beat every different location?',
          'The X and Y proposal markers stay on the board', 'Use it in the first agenda visit, after shared Problem 2']:
    check(s in g, f'guide has "{s[:70]}"')
for s in ['invent another', 'need not have identical first choices', 'There is no independent K–1 edition']:
    check(s not in g, f'guide no longer says "{s}"')

print('PASS: Week 87 PDFs carry the card fixes' if not FAILS else f'FAIL: {len(FAILS)} checks failed')
raise SystemExit(1 if FAILS else 0)
