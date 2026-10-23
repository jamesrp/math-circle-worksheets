#!/usr/bin/env python3
"""Read back the delivered Week 98 PDFs and check the diagrams against the text.

Reads lowell-math-circle-year-2/week-98/*.pdf with PyMuPDF (words and vector
drawings), never the TeX sources or the builder.  Checks:
  every student page : header, footer id, page number, consecutive problems.
  every board        : rows and columns from the drawn grid lines, square
                       cells (equal x and y pitch), board size in mm.
  marks              : seed dots, grey shading, + marks and open circles,
                       each located in its board cell; compared with the
                       data that check_math.py uses.
  guide              : pdftotext; every sentence math.md quotes is present.
Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
import re
import subprocess
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')
import pymupdf as fitz  # noqa: E402

HERE = Path(__file__).resolve().parent


def find_repo():
    # Committed copy: plans/review/checks/week-98/ -> repo is four folders up.
    cands = []
    if len(HERE.parents) > 3:
        cands.append(HERE.parents[3])
    cands += list(HERE.parents)
    for c in cands:
        if (c / 'lowell-math-circle-year-2' / 'week-98').is_dir():
            return c
    raise SystemExit('repository not found above ' + str(HERE))


REPO = find_repo()
WK = REPO / 'lowell-math-circle-year-2' / 'week-98'
MM = 72 / 25.4
OUT, FAILS = [], []


def say(s=''):
    OUT.append(s)
    print(s)


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def mm(v):
    return round(v / MM, 2)


def page_objects(page):
    """Boards (outer 0.65 rectangles + 0.45 grid lines), dots, grey cells,
    plus marks and open circles, all in mm."""
    boards, glines, dots, greys, pluses, rings = [], [], [], [], [], []
    for d in page.get_drawings():
        items = d['items']
        w = round(d.get('width') or 0, 2)
        kinds = [it[0] for it in items]
        if d['type'] == 'f' and d.get('fill') and all(k == 'c' for k in kinds):
            if max(d['fill']) < 0.1:
                r = d['rect']
                dots.append(((mm(r.x0) + mm(r.x1)) / 2, (mm(r.y0) + mm(r.y1)) / 2,
                             (mm(r.x1) - mm(r.x0)) / 2))
            continue
        if d['type'] == 'f' and d.get('fill') and 0.8 < d['fill'][0] < 0.95:
            r = d['rect']
            greys.append((mm(r.x0), mm(r.y0), mm(r.x1), mm(r.y1)))
            continue
        if d['type'] == 's' and all(k == 'c' for k in kinds) and w == 0.9:
            r = d['rect']
            rings.append(((mm(r.x0) + mm(r.x1)) / 2, (mm(r.y0) + mm(r.y1)) / 2,
                          (mm(r.x1) - mm(r.x0)) / 2))
            continue
        if d['type'] == 's' and w == 0.9 and kinds == ['l', 'l']:
            r = d['rect']
            pluses.append(((mm(r.x0) + mm(r.x1)) / 2, (mm(r.y0) + mm(r.y1)) / 2))
            continue
        if d['type'] == 's' and w == 0.65 and kinds == ['l'] * 4 and \
                (d.get('color') or (1,))[0] < 0.1:
            r = d['rect']
            boards.append([mm(r.x0), mm(r.y0), mm(r.x1), mm(r.y1)])
            continue
        if d['type'] == 's' and w == 0.45 and kinds == ['l']:
            p, q = items[0][1], items[0][2]
            glines.append((mm(p.x), mm(p.y), mm(q.x), mm(q.y)))
    out = []
    for (x0, y0, x1, y1) in boards:
        xs = sorted({x0, x1} | {a for (a, b, c, e) in glines
                                if a == c and x0 < a < x1 and
                                min(b, e) >= y0 - .01 and max(b, e) <= y1 + .01})
        ys = sorted({y0, y1} | {b for (a, b, c, e) in glines
                                if b == e and y0 < b < y1 and
                                min(a, c) >= x0 - .01 and max(a, c) <= x1 + .01})
        out.append({'box': (x0, y0, x1, y1), 'xs': xs, 'ys': ys})
    out.sort(key=lambda b: (round(b['box'][1] / 20), b['box'][0]))

    def locate(x, y):
        for i, b in enumerate(out):
            x0, y0, x1, y1 = b['box']
            if x0 < x < x1 and y0 < y < y1:
                c = max(j for j, v in enumerate(b['xs']) if v < x)
                r = max(j for j, v in enumerate(b['ys']) if v < y)
                return i, (r, c)
        return None, None

    for b in out:
        b.update(dots=set(), greys=set(), plus=set(), rings=set(),
                 rows=len(b['ys']) - 1, cols=len(b['xs']) - 1)
        px = {round(b['xs'][j + 1] - b['xs'][j], 2) for j in range(b['cols'])}
        py = {round(b['ys'][j + 1] - b['ys'][j], 2) for j in range(b['rows'])}
        b['pitch'] = (px, py)
    loose = []
    for (x, y, rad) in dots:
        i, cell = locate(x, y)
        if i is None:
            loose.append(('dot', x, y))
            continue
        b = out[i]
        # centred in its cell?
        cx = (b['xs'][cell[1]] + b['xs'][cell[1] + 1]) / 2
        cy = (b['ys'][cell[0]] + b['ys'][cell[0] + 1]) / 2
        if abs(cx - x) > .2 or abs(cy - y) > .2:
            loose.append(('off-centre dot', x, y))
        b['dots'].add(cell)
    for (x0, y0, x1, y1) in greys:
        i, cell = locate((x0 + x1) / 2, (y0 + y1) / 2)
        if i is None:
            loose.append(('grey', x0, y0))
            continue
        b = out[i]
        if abs(b['xs'][cell[1]] - x0) > .05 or abs(b['xs'][cell[1] + 1] - x1) > .05 \
                or abs(b['ys'][cell[0]] - y0) > .05 or abs(b['ys'][cell[0] + 1] - y1) > .05:
            loose.append(('grey not one cell', x0, y0))
        b['greys'].add(cell)
    for (x, y) in pluses:
        i, cell = locate(x, y)
        (loose.append(('plus', x, y)) if i is None else out[i]['plus'].add(cell))
    for (x, y, rad) in rings:
        i, cell = locate(x, y)
        (loose.append(('ring', x, y)) if i is None else out[i]['rings'].add(cell))
    return out, loose


def words(page):
    return page.get_text('text')


def S(*rc):
    return set(rc)


EMPTY = dict(dots=set(), greys=set(), plus=set(), rings=set())
four = S((0, 0), (0, 1), (1, 2), (2, 2))
dels = [four - {x} for x in [(0, 0), (0, 1), (1, 2), (2, 2)]]
ex_start = S((0, 0), (1, 0), (1, 1))
example = [
    dict(rows=2, cols=3, dots=ex_start, greys=ex_start, plus=set(), rings=set()),
    dict(rows=2, cols=3, dots=ex_start, greys=ex_start | {(0, 1)},
         plus={(0, 1)}, rings=set()),
    dict(rows=2, cols=3, dots=ex_start, greys=ex_start | {(0, 1)},
         plus={(0, 1)}, rings=set()),
]


def blank(n, k=1):
    return [dict(rows=n, cols=n, **EMPTY) for _ in range(k)]


def seeded(n, seeds, ring=None):
    return dict(rows=n, cols=n, dots=set(seeds), greys=set(seeds), plus=set(),
                rings={ring} if ring else set())


EXPECT = {
    'grades-2-3': {
        1: example + blank(3, 2),
        2: blank(4, 4),
        3: blank(3, 4),
        4: blank(3, 4),
        5: [seeded(3, four)] + [seeded(3, s) for s in dels],
    },
    'grades-4-5': {
        1: example + blank(3, 2),
        2: blank(4, 4),
        3: [dict(rows=5, cols=5, **EMPTY), dict(rows=10, cols=10, **EMPTY)],
        4: [seeded(3, S((0, 1), (1, 0)), (1, 1)),
            seeded(3, S((0, 1), (1, 0), (1, 2)), (1, 1)),
            seeded(3, S((0, 1), (1, 0), (1, 2), (2, 1)), (1, 1))],
        5: [dict(rows=4, cols=4, **EMPTY), dict(rows=5, cols=5, **EMPTY)],
        6: [seeded(3, four)] + blank(3) + [seeded(3, s) for s in dels],
    },
}
HEAD = {'grades-2-3': 'Week 98 / Growing from a few seeds / Grades 2–3',
        'grades-4-5': 'Week 98 / Growing from a few seeds / Grades 4–5'}
FOOT = {'grades-2-3': 'Bellingham Math Circle / Week 98 / W98-23-v1',
        'grades-4-5': 'Bellingham Math Circle / Week 98 / W98-45-v1'}

for band, pages in EXPECT.items():
    doc = fitz.open(WK / f'week-98-{band}.pdf')
    say(f'== {band}: {doc.page_count} pages ==')
    check(doc.page_count == len(pages), f'{band}: {len(pages)} pages')
    probs = []
    for pno in range(doc.page_count):
        page = doc[pno]
        t = words(page)
        check(abs(page.rect.width / MM - 215.9) < .1 and
              abs(page.rect.height / MM - 279.4) < .1, f'p{pno + 1} US Letter')
        check(HEAD[band] in t and FOOT[band] in t and
              re.search(rf'(^|\n){pno + 1}\n', t) is not None,
              f'p{pno + 1}: header, footer, page number')
        probs += [int(m) for m in re.findall(r'Problem (\d+):', t)]
        boards, loose = page_objects(page)
        want = pages[pno + 1]
        check(not loose, f'p{pno + 1}: every mark lies centred in a board cell '
              f'{loose[:3]}')
        check(len(boards) == len(want), f'p{pno + 1}: {len(want)} boards '
              f'(found {len(boards)})')
        for i, (b, w) in enumerate(zip(boards, want), 1):
            px, py = b['pitch']
            sq = len(px) == 1 and px == py
            desc = (f'p{pno + 1} board {i}: {b["rows"]}x{b["cols"]}, cell '
                    f'{sorted(px)} mm, at ({b["box"][0]:.0f},{b["box"][1]:.0f})')
            ok = (b['rows'] == w['rows'] and b['cols'] == w['cols'] and sq and
                  b['dots'] == w['dots'] and b['greys'] == w['greys'] and
                  b['plus'] == w['plus'] and b['rings'] == w['rings'])
            marks = ''
            if b['dots'] or b['plus'] or b['rings']:
                marks = (f'; seeds {sorted(b["dots"])}' +
                         (f', + {sorted(b["plus"])}' if b['plus'] else '') +
                         (f', circled {sorted(b["rings"])}' if b['rings'] else '') +
                         (', grey = seeds' if b['greys'] == b['dots'] else
                          f', grey {sorted(b["greys"])}'))
            check(ok, desc + marks)
    check(probs == list(range(1, len(probs) + 1)),
          f'{band}: problems numbered {probs}')
    say()

# Labels on the board pages
d23 = fitz.open(WK / 'week-98-grades-2-3.pdf')
t3 = words(d23[2])
check(all(f'{k} filled squares' in t3 for k in (3, 4, 6, 9)),
      '2-3 p3 labels: 3, 4, 6 and 9 filled squares')
t4 = words(d23[3])
check(t4.count('First finish') == 2 and t4.count('Second finish') == 2,
      '2-3 p4 labels: two First/Second finish pairs')
for band in ('grades-2-3', 'grades-4-5'):
    t = words(fitz.open(WK / f'week-98-{band}.pdf')[0])
    check(all(x in t for x in ('Start', 'One square added', 'Stopped')),
          f'{band} p1 example labels')
say()

# Guide quotes used in math.md
say('== guide quotes ==')
gt = subprocess.run(['pdftotext', '-layout', str(WK / 'week-98-facilitator.pdf'),
                     '-'], capture_output=True, text=True).stdout
gflat = re.sub(r'\s+', ' ', gt)
QUOTES = [
    'Only side-neighbors count; there are no outside cells or wraparound edges.',
    'Let C be any closed set containing the seeds, where closed means no '
    'outside cell has two neighbors in C.',
    'A terminal run is itself closed and therefore is contained in every '
    'closed superset of the seeds.',
    'If there is no legal addition, the total is 3.',
    'If those two seeds are diagonally opposite corners of a unit square, '
    'their closure is that 2 × 2 square.',
    'A third seed on that line gives 3;',
    'Otherwise two seeds support a first addition.',
    'Removing the four seeds in that order leaves terminal counts 6, 3, 3, 6.',
    'the checker finds 9 inclusion-minimal four-seed starts on 3 × 3',
    'There are 14 three-seed filling starts.',
    'In the three printed pictures the before/after counts are 8 → 8, '
    '12 → 10 and 16 → 12, respectively.',
    'For the three diagonal seeds, there are four legal first additions;',
]
for q in QUOTES:
    check(re.sub(r'\s+', ' ', q) in gflat, f'guide contains: "{q}"')
say()
say(f'FAILURES: {len(FAILS)}')
for f in FAILS:
    say('  ' + f)
(HERE / 'check_diagrams.py.out').write_text('\n'.join(OUT) + '\n')
