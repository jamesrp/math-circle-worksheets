"""Check of the Week 56 critic follow-up, October 23, 2026 (N56-S-v4, N56-M-v3, N56-FAC-v3).

Critic B's should: the gap circles on materials p. 5 were 68 mm across while the fan pieces'
edges are 30 mm, so a corner's two free sides stopped 4 mm short of the rim and "cut out the
uncovered part" also took slivers beyond the triangles' far sides. v3 materials print 60 mm
circles (radius = one face edge) and say to cut along the two lines. Coulds: Problem 5 says
"the pyramid's total gap"; the guide says the octahedron/prism extension needs one more copy
of p. 5; the guide's "KK11 / 3333 / 445" is written out.

Reads the delivered PDFs (current and archived). Run: python3 check_critic_fixes.py
(writes out_check_critic_fixes.txt beside itself).
"""
import math
import os
import re

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
W = os.path.join(ROOT, 'lowell-math-circle-year-2/week-56')
ARC = os.path.join(W, 'archive-before-critic-fixes-2026-10-23')
MM = 72 / 25.4
OUT = []


def ok(cond, msg):
    if not cond:
        raise SystemExit('FAIL ' + msg)
    OUT.append('ok   ' + msg)


def flat(p):
    return re.sub(r'\s+', ' ', p.get_text()).replace('\u2019', "'")


S, SO = pymupdf.open(os.path.join(W, 'week-56-students.pdf')), pymupdf.open(os.path.join(ARC, 'week-56-students.pdf'))
M, MO = pymupdf.open(os.path.join(W, 'week-56-materials.pdf')), pymupdf.open(os.path.join(ARC, 'week-56-materials.pdf'))
G, GO = pymupdf.open(os.path.join(W, 'week-56-facilitator.pdf')), pymupdf.open(os.path.join(ARC, 'week-56-facilitator.pdf'))

# ---------------------------------------------------------------- materials p. 5: the gap circles


def circles(page):
    return [d['rect'] for d in page.get_drawings()
            if not d['fill'] and len(d['items']) == 4 and all(it[0] == 'c' for it in d['items']) and d['rect'].width > 100]


def face_edges(doc):
    """Edge lengths (mm) of the uncut fan pieces on materials pp. 3-4."""
    out = []
    for i in (2, 3):
        for d in doc[i].get_drawings():
            if d['fill']:
                continue
            items = d['items']
            big = d['rect'].width > 20 * MM and d['rect'].height > 20 * MM  # not a 6 mm glue tab or a net fold line
            if big and len(items) in (3, 4) and all(it[0] == 'l' for it in items):  # a cut-out triangle or square
                out += [math.dist(tuple(it[1]), tuple(it[2])) / MM for it in items]
    return [round(x, 3) for x in out]


edge = sorted(set(face_edges(M)))
ok(edge == [30.0] and len(face_edges(M)) == 8 * 3 + 8 * 4, f'materials pp. 3-4: all 8 triangles and 8 squares have {edge[0]} mm edges')
cn, co = circles(M[4]), circles(MO[4])
ok(len(cn) == len(co) == 6, 'materials p. 5: six gap circles, before and after')
ok(all(abs(r.width / MM - 68) < 0.01 for r in co), 'archived p. 5: circles were 68 mm across (radius 34 mm)')
ok(all(abs(r.width / MM - 60) < 0.01 and abs(r.height / MM - 60) < 0.01 for r in cn), 'materials p. 5: circles now 60 mm across')
R = cn[0].width / 2 / MM
ok(abs(R - edge[0]) < 0.01, f'materials p. 5: radius {R:.2f} mm = one face edge, so a free side laid from the center ends on the rim')
ok(all(not a.intersects(b) for i, a in enumerate(cn) for b in cn[i + 1:]), 'materials p. 5: no two circles overlap')
words = M[4].get_text('words')
foot = min(w[1] for w in words if w[4] == 'Bellingham')
text_bottom = max(w[3] for w in words if w[3] < min(r.y0 for r in cn))
ok(all(r.y1 < foot - 0.3 * 72 and r.x0 > 36 and r.x1 < 612 - 36 for r in cn) and text_bottom < min(r.y0 for r in cn),
   'materials p. 5: circles sit between the text and the footer, inside the margins')
# Centre dots: each circle has its dot at the centre.
dots = [d['rect'] for d in M[4].get_drawings() if d['fill'] and d['rect'].width < 6]
ok(len(dots) == 6 and all(min(math.dist(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2), ((q.x0 + q.x1) / 2, (q.y0 + q.y1) / 2)) for q in dots) < 0.05 for r in cn),
   'materials p. 5: each circle has its center dot')

# The fans, laid in the plane with every marked corner on the centre. Free sides are the
# first piece's first side and the last piece's last side, both of length one edge.
FANS = {'cube corner': [90] * 3, 'tetrahedron corner': [60] * 3, 'octahedron corner': [60] * 4,
        'prism corner': [90, 90, 60], 'pyramid top': [60] * 4, 'pyramid base corner': [90, 60, 60]}
CORNERS = {'cube corner': 8, 'tetrahedron corner': 4, 'octahedron corner': 6, 'prism corner': 6}
for name, angles in FANS.items():
    free = [(edge[0], 0.0), (edge[0] * math.cos(math.radians(sum(angles))), edge[0] * math.sin(math.radians(sum(angles))))]
    for r, label in ((R, 'now'), (34.0, 'before')):
        short = [r - math.hypot(*p) for p in free]
        if label == 'now':
            ok(all(abs(s) < 0.01 for s in short), f'{name}: both free sides reach the 30 mm rim (within 0.01 mm)')
        else:
            ok(all(abs(s - 4) < 0.01 for s in short), f'{name}: on a 68 mm circle both free sides stopped 4 mm short of the rim')
    gap = 360 - sum(angles)
    ok(gap > 0, f'{name}: the two cuts leave a gap copy of {gap} degrees with no face on it')
    # Triangles' far sides sit 25.98 mm from the centre, inside the rim: "the uncovered part" was more than the gap.
    if 60 in angles:
        h = edge[0] * math.sqrt(3) / 2
        ok(h < R, f'{name}: a triangle\'s far side is {h:.2f} mm out, inside the rim, so the uncovered part is more than the gap; cutting along the two lines is not')
for name, n in CORNERS.items():
    gap = 360 - sum(FANS[name])
    ok(n * gap == 720, f'{name}: {n} gap copies of {gap} degrees make {n * gap // 360} whole circles')
ok((360 - 240) + 4 * (360 - 210) == 720 and 150 - 120 == 30, 'pyramid: top gap 120, base gap 150 (a twelfth of a circle more), total 720')

# Circle counts for the younger pair and the extension.
ok(8 + 4 + 2 == 14 and 3 * 6 == 18 and 18 - 14 == 4, 'younger pair: 14 circles used of 18 printed (3 copies of p. 5), 4 spare')
ok(CORNERS['octahedron corner'] == 6 > 4 and 4 + 6 >= 6, 'extension: the octahedron or prism needs 6 circles, more than the 4 spares; one more copy of p. 5 gives 6')

# ---------------------------------------------------------------- wording and unchanged pages
m5 = flat(M[4])
ok('Cut six circles, each 60 mm across' in m5 and 'cut along those two lines' in m5 and 'The piece with no face on it is the gap copy.' in m5
   and 'uncovered' not in m5 and '68 mm' not in m5, 'materials p. 5: 60 mm, cut along the two lines, the faceless piece is the copy')
for i in range(4):
    ok(flat(MO[i]).replace('N56-M-v2', 'N56-M-v3') == flat(M[i]), f'materials p. {i + 1}: text unchanged apart from the footer')
    a = MO[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 740)).samples
    b = M[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 740)).samples
    ok(a == b, f'materials p. {i + 1}: pixels above the footer unchanged')
ok(len(S) == len(SO) == 9, 'student packet: 9 pages')
s5 = flat(S[4])
ok("Find the pyramid's total gap." in s5 and 'Find its total gap.' not in s5, "student p. 5: \"Find the pyramid's total gap.\"")
for i in range(9):
    ok('N56-S-v4' in S[i].get_text(), f'student p. {i + 1}: footer N56-S-v4')
    old = flat(SO[i]).replace('N56-S-v3', 'N56-S-v4')
    if i == 4:
        old = old.replace('Find its total gap.', "Find the pyramid's total gap.")
    ok(old == flat(S[i]), f'student p. {i + 1}: text unchanged apart from the footer' + (' and that sentence' if i == 4 else ''))
    if i != 4:
        a = SO[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 740)).samples
        b = S[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 740)).samples
        ok(a == b, f'student p. {i + 1}: pixels above the footer unchanged')
ok(len(G) == len(GO) == 11, 'guide: 11 pages')
g = ' '.join(flat(p) for p in G)
ok('draw along the two free sides out to the rim, and cut along those two lines; the piece with no face on it is the gap copy.' in g
   and 'cut out the uncovered part' not in g, 'guide p. 3: the K-1 Problem 4 route cuts along the two lines')
ok('That needs six gap circles and a pair has four spares, so print one more copy of materials p.5 for such a pair.' in g,
   'guide p. 3: the extension asks for one more copy of p. 5')
ok('The group is four K–1 children, four third graders, and three in Grades 4–5.' in g and 'KK11' not in g and 4 + 4 + 3 == 11,
   'guide p. 2: the group written out, eleven children')
words = G[1].get_text('words')
tot = next(w for w in words if w[4] == 'Totals:')
table_bottom = max(d['rect'].y1 for d in G[1].get_drawings() if d['rect'].y1 < tot[3])
ok(tot[1] - table_bottom > 1, f'guide p. 2: "Totals" now clears the print table by {tot[1] - table_bottom:.1f} pt')
for i in range(11):
    ok('N56-FAC-v3' in G[i].get_text(), f'guide p. {i + 1}: footer N56-FAC-v3')
    if i not in (1, 2):
        ok(flat(GO[i]).replace('N56-FAC-v2', 'N56-FAC-v3') == flat(G[i]), f'guide p. {i + 1}: text unchanged apart from the footer')

print('\n'.join(OUT))
print(f'{len(OUT)} checks passed')
with open(os.path.join(HERE, 'out_check_critic_fixes.txt'), 'w') as f:
    f.write('\n'.join(OUT) + f'\n{len(OUT)} checks passed\n')
