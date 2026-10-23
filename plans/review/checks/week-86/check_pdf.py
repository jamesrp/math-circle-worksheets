#!/usr/bin/env python3
"""Read the delivered Week 86 PDFs and check that every printed board is the
graph the text and the independent model (check_math.py) assume.

Written for the math-check stage of the review. It does not import or run the
package's build.py, verify.py or check_math.py.

For every student/material page it reads the vector drawing with PyMuPDF:
- dots = closed 4-Bezier circles (centre, diameter);
- roads = black stroked straight segments whose two ends sit on dot centres;
- dot labels = single lower-case letters, each assigned to the nearest dot;
- board names (P5, T1, R3, E4, D1, F1, Q6, ...) from the page text.
It then compares each board, label for label, with the expected graph that
check_math.py also uses, and checks geometry: dot diameters, nearest-centre
spacing, equal sides and radii of the regular rings, that no road passes
through a dot that is not one of its ends, that each label is nearer its own
dot than any other dot, and (D1/D2, E4/E5, F2) that every possible straight
road between two dots clears every other dot.
It also checks headers/footers, problem numbering, the fold example's boxes
and the materials page (tile squares, counter diameters).

Run: python3 check_pdf.py  (writes check_pdf.py.out beside itself)
"""
import itertools
import math
import re
import sys
from pathlib import Path

try:
    import pymupdf as fitz  # PyMuPDF >= 1.24
except ImportError:
    import fitz  # older PyMuPDF

HERE = Path(__file__).resolve().parent


def find_repo():
    if len(HERE.parents) > 3 and (HERE.parents[3] / 'AGENTS.md').is_file() \
            and (HERE.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return HERE.parents[3]
    for p in HERE.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    sys.exit('repository not found')


REPO = find_repo()
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-86'
MM = 72 / 25.4
OUT = []
FAILS = []


def log(s=''):
    OUT.append(s)
    print(s)


def check(cond, msg, detail=''):
    tag = 'PASS' if cond else 'FAIL'
    if not cond:
        FAILS.append(msg)
    log(f'{tag} {msg}' + (f'  [{detail}]' if detail != '' else ''))


def ring(n):
    v = [chr(97 + i) for i in range(n)]
    return v, {frozenset((v[i], v[(i + 1) % n])) for i in range(n)}


def pathg(n):
    v = [chr(97 + i) for i in range(n)]
    return v, {frozenset((v[i], v[i + 1])) for i in range(n - 1)}


def E(*pairs):
    return {frozenset(p) for p in pairs}


# Expected boards, read from the printed pictures and the task text.
EXPECTED = {
    'P5': pathg(5),
    'P7': pathg(7),
    'T1': (list('abcdefg'), E('ab', 'bc', 'cd', 'de', 'cf', 'fg')),
    'T2': (list('abcdefgh'), E('ab', 'bc', 'cd', 'de', 'cf', 'fg', 'fh')),
    'R3': ring(3), 'R4': ring(4), 'R5': ring(5), 'R6': ring(6),
    'E4': ring(4), 'E5': ring(5),
    'D1': (list('abcdef'), set()), 'D2': (list('abcdef'), set()),
    'Q6': ring(6), 'Q8': ring(8),
    'F1': (list('abcdef'), E('ab', 'bc', 'ca', 'cd', 'de', 'af')),
    'F2': (list('abcde'), ring(5)[1] | E('ac')),
    'EX': (list('wxyz'), E('wx', 'xy', 'xz')),        # rules-page example
    'FOLD4': (list('wxyz'), E('wx', 'xy', 'yz')),     # fold example input
    'FOLD3': (list('xyz'), E('xy', 'yz')),            # fold example output
}


def circles_and_lines(page):
    circles, roads, others = [], [], []
    for d in page.get_drawings():
        items = d['items']
        if items and all(it[0] == 'c' for it in items) and len(items) == 4:
            r = d['rect']
            circles.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2,
                            (r.width + r.height) / 2, d))
        elif len(items) == 1 and items[0][0] == 'l' and (d.get('color') or (0, 0, 0)) == (0, 0, 0) \
                and (d.get('width') or 0) > 1.0:
            p, q = items[0][1], items[0][2]
            roads.append(((p.x, p.y), (q.x, q.y)))
        else:
            others.append(d)
    return circles, roads, others


def seg_point_dist(p, q, c):
    (x1, y1), (x2, y2), (x0, y0) = p, q, c
    dx, dy = x2 - x1, y2 - y1
    t = max(0, min(1, ((x0 - x1) * dx + (y0 - y1) * dy) / (dx * dx + dy * dy)))
    return math.hypot(x1 + t * dx - x0, y1 + t * dy - y0)


def words(page):
    return [(w[0], w[1], w[2], w[3], w[4]) for w in page.get_text('words')]


def extract_boards(page, names):
    """Group dots into boards by connected roads + proximity, label dots."""
    circles, roads, others = circles_and_lines(page)
    ws = words(page)
    # Dot labels: single lower-case letters not in running text (below dots).
    letters = [w for w in ws if re.fullmatch(r'[a-z]', w[4])]
    lab = {}
    used = set()
    for i, (cx, cy, dia, _) in enumerate(circles):
        best = None
        for j, w in enumerate(letters):
            wx, wy = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
            dd = math.hypot(wx - cx, wy - cy)
            if wy > cy and (best is None or dd < best[0]):
                best = (dd, j)
        if best and best[0] < dia / 2 + 6 * MM:
            lab[i] = letters[best[1]][4]
            used.add(best[1])
    # Map road ends to dots.
    edges = []
    bad_ends = []
    for p, q in roads:
        ends = []
        for pt in (p, q):
            k = [i for i, c in enumerate(circles) if math.hypot(pt[0] - c[0], pt[1] - c[1]) < 0.5]
            ends.append(k[0] if k else None)
        if None in ends:
            bad_ends.append((p, q))
        else:
            edges.append(tuple(ends))
    # Components by board name: assign each dot to nearest board-name word
    # that lies above-left of it (names are printed above each board).
    name_words = [w for w in ws if w[4].rstrip(':') in names]
    groups = {}
    for i, c in enumerate(circles):
        cand = [w for w in name_words if w[3] < c[1]]
        if not cand:
            continue
        w = max(cand, key=lambda w: w[3])  # nearest name above
        groups.setdefault(w[4].rstrip(':'), []).append(i)
    return circles, edges, bad_ends, lab, groups, letters, used, others


def board_graph(circles, edges, lab, idx):
    s = set(idx)
    v = sorted(lab.get(i, '?') for i in idx)
    e = {frozenset((lab.get(a, '?'), lab.get(b, '?'))) for a, b in edges if a in s and b in s}
    cross = [(a, b) for a, b in edges if (a in s) != (b in s)]
    return v, e, cross


def geom_checks(name, circles, edges, lab, idx, regular=None, all_pairs=False):
    s = set(idx)
    cs = [circles[i] for i in idx]
    dias = sorted(round(c[2] / MM, 2) for c in cs)
    log(f'  {name}: dot diameters (mm) {sorted(set(dias))}')
    spac = min(math.hypot(a[0] - b[0], a[1] - b[1]) for a, b in itertools.combinations(cs, 2)) / MM
    log(f'  {name}: nearest centre spacing {spac:.2f} mm')
    # roads clear non-endpoint dots
    clear = True
    worst = 1e9
    for a, b in edges:
        if a in s and b in s:
            for k in idx:
                if k in (a, b):
                    continue
                d = seg_point_dist(circles[a][:2], circles[b][:2], circles[k][:2]) - circles[k][2] / 2
                worst = min(worst, d)
                if d <= 0:
                    clear = False
    if worst < 1e8:
        check(clear, f'{name}: every road clears every non-endpoint dot', f'min clearance {worst / MM:.2f} mm')
    if all_pairs:
        worst = 1e9
        for a, b in itertools.combinations(idx, 2):
            for k in idx:
                if k in (a, b):
                    continue
                d = seg_point_dist(circles[a][:2], circles[b][:2], circles[k][:2]) - circles[k][2] / 2
                worst = min(worst, d)
        check(worst > 0, f'{name}: any straight road between two dots would clear the other dots',
              f'min clearance {worst / MM:.2f} mm')
        coll = 0
        for a, b, c in itertools.combinations(idx, 3):
            (x1, y1), (x2, y2), (x3, y3) = circles[a][:2], circles[b][:2], circles[c][:2]
            if abs((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) < 1e-3 * MM * MM * 10:
                coll += 1
        check(coll == 0, f'{name}: no three dot centres collinear', coll)
    if regular:
        cx = sum(c[0] for c in cs) / len(cs)
        cy = sum(c[1] for c in cs) / len(cs)
        radii = [math.hypot(c[0] - cx, c[1] - cy) / MM for c in cs]
        sides = []
        for a, b in edges:
            if a in s and b in s:
                sides.append(math.hypot(circles[a][0] - circles[b][0], circles[a][1] - circles[b][1]) / MM)
        if regular == 'hex-no-edges':
            order = sorted(idx, key=lambda i: math.atan2(circles[i][1] - cy, circles[i][0] - cx))
            sides = [math.hypot(circles[order[i]][0] - circles[order[i - 1]][0],
                                circles[order[i]][1] - circles[order[i - 1]][1]) / MM for i in range(len(order))]
        check(max(radii) - min(radii) < 0.05 and max(sides) - min(sides) < 0.05,
              f'{name}: regular polygon (equal radii and sides, equal x/y scale)',
              f'radius {min(radii):.2f}-{max(radii):.2f} mm, side {min(sides):.2f}-{max(sides):.2f} mm')
    # labels nearest own dot
    okl = True
    for i in idx:
        pass
    return okl


def label_nearest_check(name, circles, idx, lab, letters):
    bad = []
    for i in idx:
        L = lab.get(i)
        w = [w for w in letters if w[4] == L]
        # the label word assigned: nearest below
        cx, cy = circles[i][:2]
        w = min(w, key=lambda w: math.hypot((w[0] + w[2]) / 2 - cx, (w[1] + w[3]) / 2 - cy))
        wx, wy = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
        d_own = math.hypot(wx - cx, wy - cy) - circles[i][2] / 2
        for k in idx:
            if k == i:
                continue
            d_other = math.hypot(wx - circles[k][0], wy - circles[k][1]) - circles[k][2] / 2
            if d_other < d_own:
                bad.append((L, lab.get(k)))
    check(not bad, f'{name}: each label is nearer (edge to edge) its own dot than any other dot', bad or '')


def label_on_road(name, circles, edges, idx, lab, letters):
    """Report labels whose white box sits on a road (cosmetic)."""
    s = set(idx)
    hits = []
    for i in idx:
        L = lab.get(i)
        cx, cy = circles[i][:2]
        w = min([w for w in letters if w[4] == L],
                key=lambda w: math.hypot((w[0] + w[2]) / 2 - cx, (w[1] + w[3]) / 2 - cy))
        wx, wy = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
        for a, b in edges:
            if a in s and b in s and seg_point_dist(circles[a][:2], circles[b][:2], (wx, wy)) < 1.5 * MM:
                hits.append(f'{L} on road {lab.get(a)}-{lab.get(b)}')
    log(f'  {name}: labels printed on a road (cosmetic): {hits if hits else "none"}')


def compare(name, got, expected):
    v, e, cross = got
    ev, ee = expected
    ok = sorted(v) == sorted(ev) and e == ee and not cross
    det = '' if ok else f'got V={v} E={sorted(tuple(sorted(x)) for x in e)} cross={cross}'
    check(ok, f'{name}: printed graph equals expected graph, label for label '
              f'({len(ev)} dots, {len(ee)} roads)', det)


def header_footer(doc, level, tag, label):
    for n, page in enumerate(doc, 1):
        t = page.get_text()
        check(f'Week 86 / Pursuit and escape / {level}' in t, f'{label} p{n}: header')
        check(f'Bellingham Math Circle / Week 86 / {tag} / {n}' in t, f'{label} p{n}: footer')
        r = page.rect
        check(abs(r.width - 612) < 0.5 and abs(r.height - 792) < 0.5, f'{label} p{n}: US Letter')


def main():
    shared = fitz.open(WEEK / 'week-86-shared.pdf')
    upper = fitz.open(WEEK / 'week-86-upper.pdf')
    mats = fitz.open(WEEK / 'week-86-materials.pdf')
    log('== Page counts, headers, footers, numbering ==')
    check(len(shared) == 4, 'shared has 4 pages', len(shared))
    check(len(upper) == 6, 'upper has 6 pages', len(upper))
    check(len(mats) == 3, 'materials has 3 pages', len(mats))
    header_footer(shared, 'Grades 2–5', 'W86-S-v1', 'shared')
    header_footer(upper, 'Grades 4–5', 'W86-U-v1', 'upper')
    header_footer(mats, 'Grades 2–5', 'W86-M-v1', 'materials')
    for doc, lab, want in ((shared, 'shared', [1, 2, 3, 4]), (upper, 'upper', [1, 2, 3, 4, 5, 6])):
        nums = []
        for page in doc:
            nums += [int(m) for m in re.findall(r'Problem (\d+):', page.get_text())]
        check(nums == want, f'{lab}: problems numbered consecutively', nums)
    t1 = shared[0].get_text()
    t2 = upper[0].get_text()
    strip = lambda t: re.sub(r'Grades \d–5|W86-[SU]-v1', '', t)
    check(strip(t1) == strip(t2), 'upper p1 text is the shared p1 text (apart from header/footer)')

    pages = [
        ('shared', shared, 0, ['P5', 'P7']),
        ('shared', shared, 1, ['T1', 'T2']),
        ('shared', shared, 2, ['R3', 'R4']),
        ('shared', shared, 3, ['R5', 'R6']),
        ('upper', upper, 0, ['P5', 'P7']),
        ('upper', upper, 1, ['E4', 'E5']),
        ('upper', upper, 2, ['D1', 'D2']),
        ('upper', upper, 4, ['Q6']),
        ('upper', upper, 5, ['Q8']),
    ]
    regular = {'R3', 'R4', 'R5', 'R6', 'E4', 'E5', 'Q6', 'Q8'}
    for lab, doc, pno, names in pages:
        log(f'\n== {lab} p{pno + 1}: boards {names} ==')
        page = doc[pno]
        circles, edges, bad_ends, labs, groups, letters, used, others = extract_boards(page, names)
        # The rules-page example dots (8 mm) are not under a board name; split them off.
        big = {k: [i for i in v if circles[i][2] / MM > 15] for k, v in groups.items()}
        check(not bad_ends, f'{lab} p{pno + 1}: every road ends at dot centres', len(bad_ends))
        for nm in names:
            idx = big.get(nm, [])
            compare(f'{lab} p{pno + 1} {nm}', board_graph(circles, edges, labs, idx), EXPECTED[nm])
            geom_checks(f'{lab} p{pno + 1} {nm}', circles, edges, labs, idx,
                        regular=('hex-no-edges' if nm in ('D1', 'D2') else (True if nm in regular else None)),
                        all_pairs=nm in ('D1', 'D2', 'E4', 'E5'))
            label_nearest_check(f'{lab} p{pno + 1} {nm}', circles, idx, labs, letters)
            label_on_road(f'{lab} p{pno + 1} {nm}', circles, edges, idx, labs, letters)
        if pno == 0:
            small = [i for i, c in enumerate(circles) if c[2] / MM < 15]
            # three panels of the example, split by x
            panels = {}
            for i in small:
                panels.setdefault(int(circles[i][0] // (64 * MM)), []).append(i)
            texts = page.get_text('words')
            occ_words = [w for w in texts if w[4] in ('C', 'R')]
            states = []
            for key in sorted(panels):
                idx = panels[key]
                compare(f'{lab} p1 example panel {key}', board_graph(circles, edges, labs, idx), EXPECTED['EX'])
                st = {}
                for w in occ_words:
                    wx, wy = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
                    for i in idx:
                        if math.hypot(wx - circles[i][0], wy - circles[i][1]) < circles[i][2] / 2:
                            st[w[4]] = labs[i]
                states.append(st)
            log(f'  example states (C,R positions): {states}')
            check(states == [{'C': 'w', 'R': 'y'}, {'C': 'x', 'R': 'y'}, {'C': 'x', 'R': 'y'}],
                  f'{lab} p1 example: Start C@w R@y; C takes one road -> C@x; R stays -> R@y')
            body = page.get_text()
            order = [m for m in re.findall(r'(C turn|R turn)', body)]
            check(order == ['C turn', 'R turn', 'C turn'], f'{lab} p1 example tiles C, R, C turn', order)

    # Fold page (upper p4)
    log('\n== upper p4: fold example ==')
    page = upper[3]
    circles, roads, others = circles_and_lines(page)
    ws = words(page)
    letters = [w for w in ws if re.fullmatch(r'[wxyz]', w[4])]
    labs = {}
    for i, (cx, cy, dia, _) in enumerate(circles):
        cand = [w for w in letters if (w[1] + w[3]) / 2 > cy]
        w = min(cand, key=lambda w: math.hypot((w[0] + w[2]) / 2 - cx, (w[1] + w[3]) / 2 - cy))
        labs[i] = w[4]
    edges = []
    for p, q in roads:
        a = [i for i, c in enumerate(circles) if math.hypot(p[0] - c[0], p[1] - c[1]) < 0.5]
        b = [i for i, c in enumerate(circles) if math.hypot(q[0] - c[0], q[1] - c[1]) < 0.5]
        if a and b:
            edges.append((a[0], b[0]))
    # three diagrams split by position
    rows = {}
    for i, c in enumerate(circles):
        key = ('top-left' if c[0] < 306 and c[1] < 250 else 'top-right' if c[1] < 250 else 'bottom')
        rows.setdefault(key, []).append(i)
    compare('fold example original', board_graph(circles, edges, labs, rows['top-left']), EXPECTED['FOLD4'])
    compare('fold example compare', board_graph(circles, edges, labs, rows['top-right']), EXPECTED['FOLD4'])
    compare('fold example result', board_graph(circles, edges, labs, rows['bottom']), EXPECTED['FOLD3'])
    # blue boxes: which dots does each enclose?
    boxes = [d['rect'] for d in others if d.get('color') and d['color'][2] > d['color'][0]]
    for key, want in (('top-left', ['w', 'x']), ('top-right', ['w', 'x', 'y'])):
        idx = rows[key]
        box = [b for b in boxes if any(b.contains(fitz.Point(circles[i][0], circles[i][1])) for i in idx)]
        inside = sorted(labs[i] for i in idx if box and box[0].contains(fitz.Rect(
            circles[i][0] - circles[i][2] / 2, circles[i][1] - circles[i][2] / 2,
            circles[i][0] + circles[i][2] / 2, circles[i][1] + circles[i][2] / 2)))
        check(inside == want, f'fold example {key}: blue box encloses exactly {want}', inside)

    # Materials
    log('\n== materials ==')
    for pno, nm in ((0, 'F1'), (1, 'F2')):
        page = mats[pno]
        circles, edges, bad_ends, labs, groups, letters, used, others = extract_boards(page, ['Original', 'Working'])
        check(not bad_ends, f'materials p{pno + 1}: every road ends at dot centres')
        for g in ('Original', 'Working'):
            idx = groups.get(g, [])
            compare(f'materials p{pno + 1} {nm} {g}', board_graph(circles, edges, labs, idx), EXPECTED[nm])
            geom_checks(f'materials p{pno + 1} {nm} {g}', circles, edges, labs, idx,
                        regular=None, all_pairs=False)
            label_nearest_check(f'materials p{pno + 1} {nm} {g}', circles, idx, labs, letters)
            label_on_road(f'materials p{pno + 1} {nm} {g}', circles, edges, idx, labs, letters)
        if nm == 'F2':
            idx = groups['Original']
            # pentagon: regular? (radii and the five ring sides)
            cx = sum(circles[i][0] for i in idx) / 5
            cy = sum(circles[i][1] for i in idx) / 5
            radii = [math.hypot(circles[i][0] - cx, circles[i][1] - cy) / MM for i in idx]
            check(max(radii) - min(radii) < 0.05, 'F2: dots on a regular pentagon (equal radii)',
                  f'{min(radii):.2f}-{max(radii):.2f} mm')
    page = mats[2]
    circles, roads, others = circles_and_lines(page)
    dias = sorted(round(c[2] / MM, 2) for c in circles)
    check(len(circles) == 4 and all(abs(d - 18) < 0.1 for d in dias), 'materials p3: four 18 mm counters', dias)
    rects = [d['rect'] for d in others if d['rect'].width > 50]
    sq = sorted((round(r.width / MM, 2), round(r.height / MM, 2)) for r in rects)
    check(len(rects) == 4 and all(abs(a - 35) < 0.2 and abs(b - 35) < 0.2 for a, b in sq),
          'materials p3: four 35 mm square tile faces', sq)
    t = page.get_text()
    for s in ('C turn', 'R turn', 'Both cops'):
        check(s in t, f'materials p3: tile text "{s}" present')
    # Working dots vs counters: counter (18 mm) fits inside every working dot?
    log('\nSummary: %d failures' % len(FAILS))
    for f in FAILS:
        log('  FAIL ' + f)
    (HERE / 'check_pdf.py.out').write_text('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
