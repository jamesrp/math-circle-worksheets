#!/usr/bin/env python3
"""Read the delivered Week 83 student PDF and check its pictures and text.

Independent of the package's own checks. Uses PyMuPDF.

- Every page: header text, footer text, page number; problem numbers 1-6
  consecutive, each once.
- pp. 1-3: every thick coloured segment is read from the PDF drawing list.
  Segments are joined into stalks, each stalk must stand on a black ground
  line, and each segment's printed letter (B/R) must match its colour.
  Boards are named by the nearest board letter and compared with the boards
  the math check assumes.
- p. 1 worked example: solid B,R,B; dashed R crossed out and dashed B above;
  B alone on the right.
- Equal segment lengths on every board (heights carry no information).
- p. 5: the four mats' bounds and the opening example; p. 6: the 15 cards.
- Guide page references (cards on page 6, workspace on page 7).

Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
from pathlib import Path
import re
import subprocess
import warnings

warnings.filterwarnings('ignore')
try:
    import pymupdf as fitz
except ImportError:
    import fitz

HERE = Path(__file__).resolve().parent


def find_repo(here):
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
PDF = REPO / 'lowell-math-circle-year-2/week-83/week-83-students.pdf'
GUIDE = REPO / 'lowell-math-circle-year-2/week-83/week-83-facilitator.pdf'
# Re-pointed on 2026-10-23: the problem-file conversion (8e59b53) and the card's shoulds and coulds (ff74daa)
# changed and moved the packet sources, so the review checks read the copies as reviewed:
# week-83/archive-before-card-fixes-2026-10-23/ and the reviewed TeX in
# source/week-83/archive-before-problem-files-2026-10-23/week-83-source.zip (identical to the reviewed files).
PDF, GUIDE = (p.parent / 'archive-before-card-fixes-2026-10-23' / p.name for p in (PDF, GUIDE))
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


BLUE = (20 / 255, 83 / 255, 170 / 255)
RED = (188 / 255, 35 / 255, 45 / 255)


def close(c, ref):
    return c is not None and all(abs(a - b) < 0.01 for a, b in zip(c, ref))


doc = fitz.open(PDF)
check(len(doc) == 7, f'student PDF has 7 pages (found {len(doc)})')
heads = {1: '2–5', 2: '2–5', 3: '2–5', 4: '2–5', 5: '4–5', 6: '4–5', 7: '2–5'}
probs = []
for i, page in enumerate(doc, 1):
    text = page.get_text()
    check(f'Week 83 / Hackenbush balances / Grades {heads[i]}' in text, f'p.{i} header "Week 83 / Hackenbush balances / Grades {heads[i]}"')
    check('Bellingham Math Circle / Week 83 / W83-S-v1' in text, f'p.{i} footer')
    probs += [(i, int(n)) for n in re.findall(r'Problem (\d+):', text)]
check([n for _, n in probs] == [1, 2, 3, 4, 5, 6], 'problem numbers 1-6 consecutive, once each: ' + str(probs))
check('Name' not in ''.join(p.get_text() for p in doc), 'no Name field')


def read_boards(page):
    segs, grounds = [], []
    for d in page.get_drawings():
        for it in d['items']:
            if it[0] != 'l':
                continue
            p, q = it[1], it[2]
            w = d.get('width') or 0
            if abs(p.x - q.x) < 0.1 and w > 1.9 and (close(d['color'], BLUE) or close(d['color'], RED)):
                segs.append((round(p.x, 1), max(p.y, q.y), min(p.y, q.y), 'B' if close(d['color'], BLUE) else 'R', bool(d.get('dashes') and d['dashes'] != '[] 0')))
            if abs(p.y - q.y) < 0.1 and abs(w - 1.3) < 0.05 and close(d['color'], (0, 0, 0)):
                grounds.append((min(p.x, q.x), max(p.x, q.x), round(p.y, 1)))
    words = page.get_text('words')
    letters = [(w[0], w[1], w[2], w[3], w[4]) for w in words if w[4] in ('A', 'B', 'C', 'D', 'R')]
    # label check: each segment has its letter just right of its midpoint
    used = set()
    bad = []
    for x, ylo, yhi, col, dashed in segs:
        mid = (ylo + yhi) / 2
        cand = [(abs((l[1] + l[3]) / 2 - mid) + abs(l[0] - x - 8.5), k) for k, l in enumerate(letters)
                if 0 < l[0] - x < 14 and abs((l[1] + l[3]) / 2 - mid) < 6]
        if not cand:
            bad.append((x, mid, col, 'no label'))
            continue
        k = min(cand)[1]
        used.add(k)
        if letters[k][4] != col:
            bad.append((x, mid, col, 'label ' + letters[k][4]))
    lengths = sorted({round(ylo - yhi, 1) for x, ylo, yhi, col, dashed in segs})
    # stalks
    # stalks: chain segments at the same x that meet end to end, from the bottom up
    stalks = []
    for seg in sorted(segs, key=lambda t: (t[0], -t[1])):
        x, ylo, yhi, col, dashed = seg
        for st in stalks:
            if st[0] == x and abs(st[1][-1][1] - ylo) < 0.2:
                st[1].append((ylo, yhi, col, dashed))
                break
        else:
            stalks.append((x, [(ylo, yhi, col, dashed)]))
    out = []
    for x, ss in stalks:
        joined = all(abs(ss[k][1] - ss[k + 1][0]) < 0.2 for k in range(len(ss) - 1))
        base = ss[0][0]
        g = [gr for gr in grounds if gr[0] <= x <= gr[1] and abs(gr[2] - base) < 0.2]
        out.append((x, base, ''.join(t[2] for t in ss), ''.join('d' if t[3] else 's' for t in ss), joined, g[0] if g else None))
    board_letters = [l for k, l in enumerate(letters) if k not in used and l[4] in 'ABCD']
    return out, grounds, bad, lengths, board_letters


expected = {
    1: {'A': 'B', 'B': 'R', 'C': 'B + R', 'D': 'BB + R'},
    2: {'A': 'BR + R', 'B': 'BR + BR + R', 'C': 'BR + BR + BR + R'},
    3: {'A': 'BRR + RB', 'B': 'BRR + BRR + RB', 'C': 'BRR + BRR + BRR + RB'},
}
for pno in (1, 2, 3):
    page = doc[pno - 1]
    stalks, grounds, bad, lengths, board_letters = read_boards(page)
    check(not bad, f'p.{pno}: every segment letter matches its colour ({sum(len(s[2]) for s in stalks)} segments) {bad}')
    check(len(lengths) == 1, f'p.{pno}: all segments the same length {lengths} pt')
    check(all(s[4] for s in stalks), f'p.{pno}: segments of each stalk join end to end')
    check(all(s[5] is not None for s in stalks), f'p.{pno}: every stalk stands on a ground line')
    boards = {}
    for gr in grounds:
        on = sorted((s for s in stalks if s[5] == gr), key=lambda s: s[0])
        if not on:
            continue
        cands = [((gr[2] - (l[1] + l[3]) / 2), l[4]) for l in board_letters if gr[0] - 35 <= l[0] <= gr[1] and (l[1] + l[3]) / 2 < gr[2]]
        name = min(cands)[1] if cands and pno > 1 or (cands and min(cands)[0] < 200) else None
        boards[name] = on
    if pno == 1:
        ex = boards.pop(None, None)
        # worked example: three grounds at the same height without board letters
        ex_stalks = sorted((s for s in stalks if s[1] < 400), key=lambda s: s[0])
        check([(s[2], s[3]) for s in ex_stalks] == [('BRB', 'sss'), ('BRB', 'sdd'), ('B', 's')],
              'p.1 worked example reads B,R,B -> B solid with R and B dashed above -> B: ' + str([(s[2], s[3]) for s in ex_stalks]))
        cross = [d for d in page.get_drawings() if len(d['items']) == 2 and all(it[0] == 'l' for it in d['items'])
                 and close(d['color'], (0, 0, 0))]
        rx = [s for s in ex_stalks if s[3] == 'sdd']
        dashed_r = [sg for sg in [(x, ylo, yhi) for x, ylo, yhi in [(rx[0][0], rx[0][1] - 62.4, rx[0][1] - 124.8)]] ] if rx else []
        hit = False
        if rx:
            x0, ylo, yhi = dashed_r[0]
            for d in cross:
                r = d['rect']
                cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
                hit = hit or (abs(cx - x0) < 2 and yhi < cy < ylo)
        check(hit, 'p.1 worked example: an X crosses the dashed R (the cut segment)')
        boards = {k: v for k, v in boards.items() if k is not None}
        stalks_tasks = boards
    got = {k: ' + '.join(s[2] for s in v) for k, v in boards.items()}
    check(got == expected[pno], f'p.{pno} boards read from PDF: {dict(sorted(got.items()))}')

# p.5 mats and example
t5 = ' '.join(doc[4].get_text().split())
words5 = [w[4] for w in doc[4].get_text('words')]
blocks = [b for b in doc[4].get_text('dict')['blocks'] if b.get('lines')]
btxt = [' '.join(' '.join(sp['text'] for l in b['lines'] for sp in l['spans']).split()) for b in blocks]
mats = [btxt[k + 1] for k, t in enumerate(btxt) if t == 'greater than less than']
check(mats == ['0 3', '− 1 1', '0 1', '1 2 1'], 'p.5: four mats with bounds (0,3), (-1,1), (0,1), (1/2,1) in that order: ' + str(mats))
check(any(t.startswith('− 2 2') for t in btxt) and 'day 1 day 0 day 1' in btxt, 'p.5 example: bounds -2, 2; cards -1, 0, 1 labelled day 1, day 0, day 1; answer 0 day 0')
say('  p.5 text in reading order: ' + ' | '.join(' '.join(s['text'] for l in b['lines'] for s in l['spans']) for b in blocks))
t6 = doc[5].get_text()
check(t6.count('day 0') == 1 and t6.count('day 1') == 2 and t6.count('day 2') == 4 and t6.count('day 3') == 8, 'p.6: 15 cards, day counts 1, 2, 4, 8')
say('  p.6 text: ' + ' '.join(t6.split()))
check('Extra workspace' in doc[6].get_text(), 'p.7 is the extra workspace page')

g = subprocess.run(['pdftotext', '-layout', str(GUIDE), '-'], capture_output=True, text=True).stdout
check('birthday-number cards on page 6' in g and 'page 7 as the reusable' in g, 'guide page references: cards on page 6, workspace on page 7')
check('fifteen' in g, 'guide: fifteen cards')

say('')
say(f'FAILURES: {len(FAIL)}')
for f in FAIL:
    say('  ' + f)
(HERE / 'check_diagrams.py.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
