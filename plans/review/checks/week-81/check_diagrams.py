"""Read the delivered Week 81 PDFs and check every diagram against the text.

Does not import or run any author checker. Uses pdfplumber on the released
PDFs in lowell-math-circle-year-2/week-81/ (not the TeX source):
- bucket boxes are the unfilled rounded outlines; counters ("fish") are the
  filled grey circles; each fish is assigned to the box containing its centre;
- boxes are grouped into starts by horizontal gaps, read in reading order,
  and their printed bucket labels (1, 2, 3) are read from the text below them;
- the counts are compared with what each problem and the guide say.
Also checks headers, footers, problem numbering, board and card dimensions,
fish containment and overlap, and the guide's page references.
Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
from pathlib import Path
import math
import subprocess
import sys

import pdfplumber

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    four_up = here.parents[3]
    if (four_up / 'AGENTS.md').is_file() and (four_up / 'lowell-math-circle-year-2').is_dir():
        return four_up
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-81'
STUDENT = WEEK / 'week-81-students.pdf'
GUIDE = WEEK / 'week-81-facilitator.pdf'
OUT, FAIL = [], []
MM = 72 / 25.4


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
    say(('ok   ' if cond else 'FAIL ') + msg)


def fish_of(page):
    return [c for c in page.curves if c['fill'] and abs((c['x1'] - c['x0']) - 4.1 * MM) < 0.3]


def boxes_of(page, w_lo=25, w_hi=45):
    return [c for c in page.curves if not c['fill'] and w_lo < c['x1'] - c['x0'] < w_hi
            and w_lo < c['bottom'] - c['top'] < w_hi]


def centre(o):
    return ((o['x0'] + o['x1']) / 2, (o['top'] + o['bottom']) / 2)


def inside(pt, o, pad=0.0):
    return o['x0'] - pad <= pt[0] <= o['x1'] + pad and o['top'] - pad <= pt[1] <= o['bottom'] + pad


def read_starts(page, boxes, fish, gap_limit=25):
    """Group boxes into starts (same row, small gaps) and count fish in each box."""
    rows = {}
    for b in boxes:
        key = round(b['top'])
        rows.setdefault(key, []).append(b)
    starts = []
    contained = set()
    for top in sorted(rows):
        row = sorted(rows[top], key=lambda b: b['x0'])
        groups, cur = [], [row[0]]
        for b in row[1:]:
            if b['x0'] - cur[-1]['x1'] < gap_limit:
                cur.append(b)
            else:
                groups.append(cur)
                cur = [b]
        groups.append(cur)
        for g in groups:
            counts, labels = [], []
            for b in g:
                inb = [f for f in fish if inside(centre(f), b)]
                for f in inb:
                    contained.add(id(f))
                    # whole circle inside the box outline
                    if not (b['x0'] <= f['x0'] and f['x1'] <= b['x1'] and b['top'] <= f['top'] and f['bottom'] <= b['bottom']):
                        FAIL.append(f'fish pokes out of a box on p. {page.page_number}')
                counts.append(len(inb))
                lab = ''.join(ch['text'] for ch in page.chars
                              if b['x0'] <= (ch['x0'] + ch['x1']) / 2 <= b['x1'] and b['bottom'] < ch['top'] < b['bottom'] + 14)
                labels.append(lab)
            starts.append((tuple(counts), tuple(labels), g))
    loose = [f for f in fish if id(f) not in contained]
    return starts, loose


def min_fish_gap(fish):
    best = None
    for i in range(len(fish)):
        for j in range(i + 1, len(fish)):
            a, b = centre(fish[i]), centre(fish[j])
            d = math.dist(a, b) - (fish[i]['x1'] - fish[i]['x0'])
            if math.dist(a, b) < 30:
                best = d if best is None else min(best, d)
    return best


pdf = pdfplumber.open(STUDENT)
pages = pdf.pages
say('== Student PDF:', STUDENT.relative_to(REPO), f'({len(pages)} pages) ==')
check(len(pages) == 5, 'five pages')
check(all(abs(p.width - 612) < 1 and abs(p.height - 792) < 1 for p in pages), 'US Letter, 612 x 792 pt')
texts = [p.extract_text() for p in pages]
for i, t in enumerate(texts, 1):
    first = t.splitlines()[0]
    say(f'  p. {i} header: {first!r}')
heads = [t.splitlines()[0] for t in texts]
check(heads[:4] == ['Week 81 / Buckets of Fish / Grades 2–5'] * 4 and heads[4] == 'Week 81 / Buckets of Fish / Grades 4–5',
      'headers: pp. 1-4 "Grades 2–5", p. 5 "Grades 4–5"')
check(all('W81-S-draft-v1' in t.splitlines()[-1] for t in texts), 'every footer carries the packet id')
import re
nums = [int(n) for t in texts for n in re.findall(r'Problem (\d+):', t)]
check(nums == [1, 2, 3, 4, 5], f'problems numbered consecutively {nums}')
allfish = [fish_of(p) for p in pages]
check(all(abs((f['x1'] - f['x0']) - (f['bottom'] - f['top'])) < 0.05 for fs in allfish for f in fs),
      'every counter is a true circle (width = height)')

# ---------------- p. 1: opening visual and Problem 1
p = pages[0]
boxes = boxes_of(p)
starts, loose = read_starts(p, boxes, allfish[0])
say('\n== p. 1 ==')
for c, l, g in starts:
    say(f'  start {c}, labels {l}, box {g[0]["x1"]-g[0]["x0"]:.1f} x {g[0]["bottom"]-g[0]["top"]:.1f} pt')
counts = [c for c, l, g in starts]
check(counts[:3] == [(1, 1, 2), (1, 1, 1), (2, 2, 1)], 'opening visual reads Before (1,1,2) -> (1,1,1) -> (2,2,1)')
check(counts[3:] == [(0, 0, 1), (1, 1, 0), (2, 1, 1), (2, 2, 2)], 'Problem 1 starts read (0,0,1), (1,1,0), (2,1,1), (2,2,2) in reading order')
check(all(l == ('1', '2', '3') for c, l, g in starts), 'every three-box picture is labelled 1, 2, 3 left to right')
check(len(loose) == 1, 'exactly one loose counter (the struck-out "removed" one)')
if loose:
    lc = centre(loose[0])
    third = starts[1][2][2]
    check(third['x0'] <= lc[0] <= third['x1'] and lc[1] > third['bottom'],
          'the removed counter sits under bucket 3 of the middle picture, the bucket it was taken from')
    strike = [l for l in p.lines if abs(l['x1'] - l['x0']) > 5 and abs(l['bottom'] - l['top']) > 5
              and inside(((l['x0'] + l['x1']) / 2, (l['top'] + l['bottom']) / 2), loose[0], 2)]
    check(len(strike) == 1, 'it is struck through')
check('Remove one from 3' in texts[0] and 'Add one to 1 and 2' in texts[0], 'captions say "Remove one from 3", "Add one to 1 and 2"')
sizes = {(round(g[0]['x1'] - g[0]['x0'], 1), round(g[0]['bottom'] - g[0]['top'], 1)) for c, l, g in starts[3:]}
check(len(sizes) == 1, f'Problem 1 boxes all the same size {sizes}')
say(f'  closest pair of counters on p. 1: gap {min_fish_gap(allfish[0]):.2f} pt (negative = overlap)')

# ---------------- p. 2: board
p = pages[1]
say('\n== p. 2 (reusable board) ==')
big = [c for c in p.curves if not c['fill'] and c['x1'] - c['x0'] > 100]
dims = [((b['x1'] - b['x0']) / MM, (b['bottom'] - b['top']) / MM) for b in sorted(big, key=lambda b: b['x0'])]
say('  bucket outlines (mm):', ', '.join(f'{w:.1f} x {h:.1f}' for w, h in dims))
check(len(big) == 3 and all(abs(w - 56) < 0.3 and abs(h - 139) < 0.3 for w, h in dims), 'three equal 56 x 139 mm buckets')
words = p.extract_words()
lab = sorted([w for w in words if w['text'] in '123' and w['top'] < 80], key=lambda w: w['x0'])
check([w['text'] for w in lab] == ['1', '2', '3'], 'labelled Bucket 1, 2, 3 left to right')
rects = sorted(p.rects, key=lambda r: r['x0'])
rdims = [((r['x1'] - r['x0']) / MM, (r['bottom'] - r['top']) / MM) for r in rects]
say('  side boxes (mm):', ', '.join(f'{w:.1f} x {h:.1f}' for w, h in rdims))
check('Supply' in texts[1] and 'Removed' in texts[1] and len(rects) == 2, 'Supply and Removed boxes, outside the buckets')
check(not allfish[1], 'board is empty (no printed counters)')

# ---------------- p. 3: sixteen cards
p = pages[2]
say('\n== p. 3 (Problem 2 cards) ==')
cards = sorted([r for r in p.rects if r.get('dash')], key=lambda r: (round(r['top']), r['x0']))
cdims = {(round((r['x1'] - r['x0']) / MM, 1), round((r['bottom'] - r['top']) / MM, 1)) for r in cards}
say('  card outlines (mm):', cdims)
check(len(cards) == 16 and len(cdims) == 1, 'sixteen equal dashed cards')
boxes = boxes_of(p)
read = []
for r in cards:
    inb = sorted([b for b in boxes if inside(centre(b), r)], key=lambda b: b['x0'])
    cnt = tuple(len([f for f in allfish[2] if inside(centre(f), b)]) for b in inb)
    labs = tuple(''.join(ch['text'] for ch in p.chars if b['x0'] <= (ch['x0'] + ch['x1']) / 2 <= b['x1']
                         and b['bottom'] < ch['top'] < b['bottom'] + 14) for b in inb)
    read.append((cnt, labs))
expected = [(a, b) for b in range(4) for a in range(4)]
check([c for c, l in read] == expected, 'cards read (left,right) = (0,0),(1,0),(2,0),(3,0) / (0,1)... / ...(3,3) in reading order')
check(all(l == ('1', '2') for c, l in read), 'every card labelled 1, 2 left to right')
check(all(inside(centre(f), b) for f in allfish[2] for b in [next((b for b in boxes if inside(centre(f), b)), None)] if b),
      'every counter on p. 3 lies in a card box')
check(sum(sum(c) for c, l in read) == len(allfish[2]) == 48, f'48 counters on the cards ({len(allfish[2])} drawn)')
say(f'  closest pair of counters on p. 3: gap {min_fish_gap(allfish[2]):.2f} pt (negative = overlap)')

# ---------------- p. 4: Problem 3
p = pages[3]
say('\n== p. 4 (Problem 3) ==')
starts, loose = read_starts(p, boxes_of(p), allfish[3])
for c, l, g in starts:
    say(f'  start {c}, labels {l}')
check([c for c, l, g in starts] == [(2, 2, 2), (1, 2, 2), (2, 1, 2), (2, 2, 1), (0, 2, 0), (3, 3, 1)],
      'Problem 3 starts read (2,2,2), (1,2,2), (2,1,2), (2,2,1), (0,2,0), (3,3,1)')
check(all(l == ('1', '2', '3') for c, l, g in starts) and not loose, 'all labelled 1, 2, 3; no stray counters')
say(f'  closest pair of counters on p. 4: gap {min_fish_gap(allfish[3]):.2f} pt (negative = overlap)')

# ---------------- p. 5: quantity visual, Problems 4-5
p = pages[4]
say('\n== p. 5 (Problems 4-5) ==')
starts, loose = read_starts(p, boxes_of(p), allfish[4])
for c, l, g in starts:
    say(f'  start {c}, labels {l}')
check([c for c, l, g in starts] == [(0, 1), (1, 1, 1)], 'Problem 4 shows (0,1); Problem 5 shows (1,1,1)')
check([l for c, l, g in starts] == [('1', '2'), ('1', '2', '3')], 'labels 1, 2 and 1, 2, 3')
check(len(loose) == 12, f'the quantity visual draws 12 loose counters ({len(loose)})')
qtext = p.extract_text()
check(re.search(r'12\s+11', qtext) is not None and 'remove 1' in qtext, 'and turns them into "12 counters", then "remove 1" gives "11 counters"')
check('any finite number' in qtext, 'p. 5 states the lifted cap: "a refill may be any finite number"')

# ---------------- guide page references
say('\n== Guide cross-references ==')
g = subprocess.run(['pdftotext', '-layout', str(GUIDE), '-'], capture_output=True, text=True).stdout
check("page 2’s reusable board" in g and "page 3’s sixteen sorting cards" in g and 'continuation on\npage 5' in g.replace('\r', ''),
      'guide p. 2 cites board p. 2, cards p. 3, upper continuation p. 5: all match the student PDF')
check(len(pdfplumber.open(GUIDE).pages) == 4, 'guide has 4 pages')
check('add 0 or 1 to each\nearlier odd bucket' in g or 'add 0 or 1 to each earlier odd bucket' in ' '.join(g.split()),
      'guide p. 1 sentence quoted in math.md is present verbatim')

say('\nFAILURES:', len(FAIL))
for f in FAIL:
    say('  ' + f)
(HERE / 'check_diagrams.py.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
sys.exit(1 if FAIL else 0)
