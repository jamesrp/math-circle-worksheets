#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes in the built Week 77 PDFs.

    python3 verify_card_fixes_2026_10_23.py [DIR]

DIR holds week-77-students.pdf, week-77-facilitator.pdf and week-77-materials.pdf
(default: ../reference-pdfs). Needs PyMuPDF (pip install pymupdf). It reads the
rendered pages: footers; the Problem 2, 3 and 5 wording; the bend at C on the
joined board; that every printed tile has the shape and size of its triangle on the
student pages, with its name and each edge's name along the matching side; the
strips, tokens and stage cards; and the guide's new or changed passages.
"""
import itertools
import math
import sys
from collections import Counter
from pathlib import Path
import pymupdf as fitz

HERE = Path(__file__).resolve().parent
DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / 'reference-pdfs'
CM = 72 / 2.54
FAIL = []


def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg)
    if not ok:
        FAIL.append(msg)


def flat(page):
    return ' '.join(page.get_text().split())


def dots(page):
    """Centres (cm) of the 2.2 pt vertex dots."""
    out = []
    for d in page.get_drawings():
        r = d['rect']
        if d['type'] == 'f' and abs(r.width - 4.4) < .3 and abs(r.height - 4.4) < .3:
            out.append(((r.x0 + r.x1) / 2 / CM, (r.y0 + r.y1) / 2 / CM))
    return out


def normalized(points):
    x0, y0 = min(p[0] for p in points), min(p[1] for p in points)
    return sorted((round(x - x0, 2), round(y - y0, 2)) for x, y in points)


def same_shape(a, b, tol=.03):
    return len(a) == len(b) and all(math.dist(p, q) < tol for p, q in zip(normalized(a), normalized(b)))


S = fitz.open(DIR / 'week-77-students.pdf')
G = fitz.open(DIR / 'week-77-facilitator.pdf')
M = fitz.open(DIR / 'week-77-materials.pdf')
check((len(S), len(G), len(M)) == (6, 4, 2), f'page counts 6/4/2: {len(S)}/{len(G)}/{len(M)}')
for i, p in enumerate(S):
    check('Week 77 / F77-45-v3' in flat(p), f'student p.{i+1} footer F77-45-v3')
for i, p in enumerate(G):
    check('Week 77 / F77-FAC-v3' in flat(p), f'guide p.{i+1} footer F77-FAC-v3')
for i, p in enumerate(M):
    check('Week 77 / F77-M-v1' in flat(p), f'materials p.{i+1} footer F77-M-v1')

# Shoulds 1 and 3, could 8: the student wording.
p2, p3, p5 = flat(S[2]), flat(S[3]), flat(S[4])
check('hole' not in p2.replace('Persistent holes', ''), 'should 3: Problem 2 no longer states hole counts')
for phrase in ['Whichever dashed edge comes first, can the first loop be gone at stage 5?',
               'Answer the same question for the square in Problem 2.',
               'record a schedule your partner can replay or explain why there is none.',
               'AB first:', 'DE first:', 'Square:',
               'Count each enclosed, unfilled region as one hole. Every build on these two boards has 0, 1, 2, 1, 0 holes after stages 0, 2, 4, 5, 8.',
               'Can those counts alone tell you when the first loop disappears?']:
    check(phrase in p3, f'should 1/3: Problem 3 has "{phrase[:60]}"')
check('Make one build' not in p3 and 'Both builds' not in p3, 'should 1: the old Problem 3 request is gone')
check('gone at one stage and come back at a later stage' in p5 and 'survive again' not in p5, 'could 8: Problem 5 says "come back"')

# Could 6: the joined board bends at C (dots read from the page, in cm).
J = dots(S[3])
check(len(J) == 5, f'joined board has 5 dots: {len(J)}')
J = sorted(J, key=lambda p: (p[0], p[1]))
A, B, C, D, E = J[0], J[1], J[2], J[3], J[4]  # by x, then y: A above B, C, D above E


def turn(a, b, c):
    return math.degrees(abs(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(b[1] - a[1], b[0] - a[0])))


check(turn(A, C, E) > 15 and turn(B, C, D) > 15, f'A-C-E and B-C-D bend at C by {turn(A, C, E):.1f} and {turn(B, C, D):.1f} degrees')
check(abs(math.dist(A, B) - 5.8) < .02 and abs(math.dist(D, E) - 5.8) < .02, 'AB and DE still 5.8 cm')

# Should 4: materials page 1, tiles. Group triangles that share corners into boards.
tris = []
for d in M[0].get_drawings():
    items = d['items']
    if len(items) == 3 and all(it[0] == 'l' for it in items):
        tris.append([(it[1].x / CM, it[1].y / CM) for it in items])
check(len(tris) == 9, f'nine tiles: {len(tris)}')
groups = []
for t in tris:
    hits = [g for g in groups if any(math.dist(p, q) < .01 for p in t for q in itertools.chain(*g))]
    merged = [t] + [x for g in hits for x in g]
    groups = [g for g in groups if g not in hits] + [merged]
by_size = sorted(groups, key=len)


def corners(group):
    pts = []
    for t in group:
        for p in t:
            if not any(math.dist(p, q) < .01 for q in pts):
                pts.append(p)
    return pts


xyz, square, joined, fan = (by_size[0], by_size[1], by_size[2], by_size[3]) if [len(g) for g in by_size] == [1, 2, 2, 4] else (None,) * 4
if xyz is None:
    check(False, f'tile groups 1, 2, 2, 4: {[len(g) for g in by_size]}')
else:
    if len(corners(square)) == 5:
        square, joined = joined, square
    check(same_shape(corners(square), dots(S[1])), 'square tiles match the Problem 1 square (6.2 cm)')
    check(same_shape(corners(square), dots(S[2])), 'square tiles match the Problem 2 square')
    check(same_shape(corners(joined), dots(S[3])), 'joined tiles match the Problem 3 board, bent at C')
    check(same_shape(corners(fan), dots(S[5])), 'fan tiles match the Problem 6 board (8 cm, centre O)')
    xyz_page1 = [d for d in S[0].get_drawings() if d['type'] == 'fs' and len(d['items']) == 3]
    check(xyz_page1 and same_shape(corners(xyz), [(it[1].x / CM, it[1].y / CM) for it in xyz_page1[0]['items']]),
          'launch tile matches the shaded XYZ triangle on student page 1')

    words = [(w[4], ((w[0] + w[2]) / 2 / CM, (w[1] + w[3]) / 2 / CM)) for w in M[0].get_text('words')]

    def inside(t, p):
        s = [(t[(i + 1) % 3][0] - t[i][0]) * (p[1] - t[i][1]) - (t[(i + 1) % 3][1] - t[i][1]) * (p[0] - t[i][0]) for i in range(3)]
        return all(x > 0 for x in s) or all(x < 0 for x in s)

    def seg_dist(p, a, b):
        ax, ay, bx, by = *a, *b
        t = max(0, min(1, ((p[0] - ax) * (bx - ax) + (p[1] - ay) * (by - ay)) / ((bx - ax) ** 2 + (by - ay) ** 2)))
        return math.dist(p, (ax + t * (bx - ax), ay + t * (by - ay)))

    expected = {'square': {'ABC', 'ACD'}, 'joined': {'ABC', 'CDE'}, 'fan': {'ABO', 'BCO', 'CDO', 'DAO'}}
    for board, group in (('square', square), ('joined', joined), ('fan', fan)):
        names = set()
        for t in group:
            ws = [(w, p) for w, p in words if inside(t, p)]
            name = [w for w, _ in ws if len(w) == 3 and w.isupper()]
            letters = {}
            for v in t:  # the corner letter nearest each corner
                cand = [(math.dist(p, v), w) for w, p in ws if len(w) == 1]
                letters[v] = min(cand)[1]
            ok_edges = True
            for w, p in ws:
                if len(w) == 2 and w.isupper():
                    side = min(range(3), key=lambda i: seg_dist(p, t[i], t[(i + 1) % 3]))
                    ok_edges &= set(w) == {letters[t[side]], letters[t[(side + 1) % 3]]}
            edge_words = sorted(w for w, _ in ws if len(w) == 2 and w.isupper())
            tile = name[0] if len(name) == 1 else '?'
            names.add(tile)
            check(len(name) == 1 and board in [w for w, _ in ws] and set(letters.values()) == set(tile)
                  and len(edge_words) == 3 and ok_edges,
                  f'{board} tile {tile}: board word, corner letters, edges {edge_words} each along its own side')
        check(names == expected[board], f'{board} tiles named {sorted(names)}')
    check('XYZ' in [w for w, p in words if inside(xyz[0], p)], 'launch tile named XYZ')

    # Strips: seven rectangles 0.8 cm high, lengths from the boards.
    strips = sorted(round(d['rect'].width / CM, 2) for d in M[0].get_drawings()
                    if len(d['items']) == 4 and abs(d['rect'].height / CM - .8) < .01)
    check(strips == sorted([5.8, 5.8, 6.2, 6.2, 6.2, 6.2, round(6.2 * math.sqrt(2), 2)]),
          f'strips 2 x 5.8, 4 x 6.2 and one 8.77 cm: {strips}')
    m1 = flat(M[0])
    for label in ['AB joined', 'DE joined', 'AB square', 'BC square', 'CD square', 'DA square', 'AC square']:
        check(label in m1, f'strip "{label}"')

# Materials page 2: tokens and stage cards.
rects = [d['rect'] for d in M[1].get_drawings() if len(d['items']) == 4 and all(it[0] == 'l' for it in d['items'])]
tokens = [r for r in rects if abs(r.height / CM - 1.6) < .01 and abs(r.width / CM - 18.2 / 8) < .01]
cards = [r for r in rects if abs(r.height / CM - 2.4) < .01]
check(len(tokens) == 48 and len(cards) == 8, f'48 tokens and 8 stage cards: {len(tokens)}, {len(cards)}')
labels = Counter(w[4] for w in M[1].get_text('words') if w[3] - w[1] > 12)
want = Counter({e: 3 for e in ['AB', 'BC', 'CD', 'DA', 'AC', 'CE', 'DE', 'AO', 'BO', 'CO', 'DO']})
want.update({e: 2 for e in ['XY', 'YZ', 'XZ']})
want.update({s: 1 for s in ['0', '2', '3', '4', '5', '8']})
check(labels == want, f'33 edge tokens, 6 launch tokens and stage numbers 0 2 3 4 5 8: {dict(labels) if labels != want else "as listed"}')
check(sum(want[e] for e in want if len(e) == 2) + 9 == 48, '9 blank tokens')

# The guide.
g = ' '.join(flat(p) for p in G)
for phrase in ['When R closes first (DA before AC), either one-tile filling leaves R nonzero; both kill it.',
               'When a triangle rim closes first, on the square or on two triangles meeting at a vertex, filling that triangle first kills the older loop.',
               'a loop is gone exactly when every triangle inside it (inside either lobe of a figure eight) is filled',
               'week-77-materials.pdf',
               '33 edge tokens, three each of',
               'nine blank tokens',
               '5–8: shared launch',
               '4–5 table. 8–10: the token test on student page 1.',
               'K–1 and 2–3 tables: adult-led, on the same pages, 8–55.',
               'Is every triangle inside your loop covered?',
               'Key in plain words:',
               'Yes, either way:',
               'On the square, only with AC first.',
               'No, the counts alone do not tell when the first loop disappears.',
               "bonus challenges, Problem 1C (F02-BONUS-v1), find the same divided square's three do-nothing line sets".replace("'", "’")]:
    check(phrase in g, f'guide has "{phrase[:70]}"')
for gone in ['This packet supplies no route', 'Two triangles meeting at a single vertex can instead',
             '45 token cards', 'Trace/cut', 'Other tables: zero copies']:
    check(gone not in g, f'guide no longer has "{gone}"')

print('FAIL' if FAIL else 'PASS', f'({len(FAIL)} failures)')
sys.exit(1 if FAIL else 0)
