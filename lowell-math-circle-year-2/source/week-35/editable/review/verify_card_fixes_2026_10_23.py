#!/usr/bin/env python3
"""Check every claim changed by the October 23, 2026 card shoulds and coulds.

    python3 review/verify_card_fixes_2026_10_23.py [build-folder]

The build folder (default: this package's root, where build.py leaves k-1.pdf,
grades-2-3.pdf, grades-4-5.pdf and facilitator-guide.pdf) holds the built PDFs.
Needs PyMuPDF. The witness recipes are checked with the package's own motif and an
exact frieze test written here; nothing imports the student or guide builders.
"""
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
build = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
CM = 72 / 2.54
checks = 0


def ok(cond, what):
    global checks
    assert cond, what
    checks += 1


def text(page):
    """Page text on one line; words TeX hyphenated across a line break are joined."""
    t = ' '.join(page.get_text().replace('–', '-').replace('’', "'").split())
    return re.sub(r'([a-z])- ([a-z])', r'\1\2', t)


def boxes(page):
    """The 17.65 x 6 cm working boards, as (top, bottom) in cm from the top of the paper."""
    out = []
    for d in page.get_drawings():
        r = d['rect']
        if abs(r.width - 17.65 * CM) < 1 and abs(r.height - 6 * CM) < 1:
            out.append((r.y0 / CM, r.y1 / CM))
    return sorted(set((round(a, 2), round(b, 2)) for a, b in out))


def words_box(page, phrase):
    """Bounding box (cm) of the first line of text that starts with phrase."""
    for b in page.get_text('blocks'):
        if ' '.join(b[4].split()).startswith(phrase):
            return b[0] / CM, b[1] / CM, b[2] / CM, b[3] / CM
    raise AssertionError(phrase)


docs = {n: pymupdf.open(build / f'{n}.pdf') for n in ('k-1', 'grades-2-3', 'grades-4-5')}
T = {n: [text(p) for p in d] for n, d in docs.items()}

# ---------------------------------------------------------------- footers and page counts (fix 4)
for n, count in (('k-1', 5), ('grades-2-3', 4), ('grades-4-5', 5)):
    ok(len(T[n]) == count, (n, 'pages', len(T[n])))
    for i, t in enumerate(T[n], 1):
        ok(f'Bellingham Math Circle / Week 35 / W35-{n}-v4' in t, (n, i, 'footer v4'))
        ok(f'Week 35 / Footprint borders / ' in t, (n, i, 'header'))

# ---------------------------------------------------------------- rules (second run 2; fix 9)
box_rule = 'Use the loose footprints. Build each border in its box, or on a long strip if it needs more room.'
k1 = T['k-1'][0]
ok(box_rule + ' A match must fit every footprint. Test with a tracing copy; leave the original in place.' in k1, 'K-1 rules')
for gone in ('repeats forever', 'strip ends', 'A slide must move the copy', 'long strips.'):
    ok(gone not in ' '.join(T['k-1']), ('K-1 leaves to the launch', gone))
for n in ('grades-2-3', 'grades-4-5'):
    ok(box_rule + ' Each border repeats forever both ways. A match must fit every footprint. Only footprints count, '
       'not strip ends or guide lines. A slide must move the copy. Test with a tracing copy; leave the original in place.'
       in T[n][0], (n, 'rules'))
    rules = words_box(docs[n][0], 'Use the loose footprints.')
    p1 = words_box(docs[n][0], 'Problem 1:')
    ok(p1[1] - rules[3] > 0.4, (n, 'rules clear of Problem 1', p1[1] - rules[3]))

# ---------------------------------------------------------------- the changed prompts
ok("Problem 4: Make another border like Problem 3's, with a longer slide." in T['k-1'][2], 'K-1 P4 (second run 5, fix 11)')
ok('Problem 1: Make two repeating borders whose shortest matching slides are different lengths.' in T['grades-2-3'][0], '2-3 P1 shortest')
ok('Problem 1: Build two repeating borders with different shortest matching slides. Measure those slides; explain why a '
   'shorter slide cannot match each border.' in T['grades-4-5'][0], '4-5 P1 shortest')
for n in docs:
    ok('smallest' not in ' '.join(T[n]) and 'smaller' not in ' '.join(T[n]), (n, 'shortest throughout (fix 12)'))
ok('Make two borders that match after a glide but fail after the flip alone. Give them different shortest matching slides.'
   in T['grades-2-3'][1], '2-3 P2 two glide borders (second run 3)')
ok('Problem 3: On each border, how does the shortest matching glide compare with the shortest matching slide?'
   in T['grades-2-3'][1], '2-3 P3 on each border')
ok('Problem 3: A border matches after a 3 cm glide. Must a 6 cm slide also match? Must a 3 cm slide match? Explain why.'
   in T['grades-4-5'][1], '4-5 P3 a 3 cm glide (fix 6)')
ok('A glide is a flip over the middle line followed by a nonzero slide along it.' in T['grades-4-5'][1], '4-5 glide defined on the P3 page')
p6 = T['grades-4-5'][4]
ok('Problem 6: For one border you made, describe every matching slide, glide, flip and turn. Explain why no other move matches.'
   in p6, '4-5 P6 (fix 7)')
ok('Problem 6' not in T['grades-4-5'][3], '4-5 P6 left page 4')
bottom = words_box(docs['grades-4-5'][4], 'Problem 6:')[3]
foot = words_box(docs['grades-4-5'][4], 'Bellingham Math Circle')[1]
ok(foot - bottom > 27.94 / 2, ('4-5 P6 has at least half a page to write', foot - bottom))
ok(not boxes(docs['grades-4-5'][4]) and len(docs['grades-4-5'][4].get_drawings()) == 0, '4-5 P6 page is blank below')

# ---------------------------------------------------------------- boards and the extra-workspace labels (fix 10)
want = {('k-1', 1): 1, ('k-1', 2): 2, ('k-1', 3): 2, ('k-1', 4): 2, ('k-1', 5): 2,
        ('grades-2-3', 1): 2, ('grades-2-3', 2): 2, ('grades-2-3', 3): 2, ('grades-2-3', 4): 2,
        ('grades-4-5', 1): 2, ('grades-4-5', 2): 2, ('grades-4-5', 3): 2, ('grades-4-5', 4): 2, ('grades-4-5', 5): 0}
labelled = {('grades-2-3', 3), ('grades-2-3', 4), ('grades-4-5', 2), ('grades-4-5', 3), ('grades-4-5', 4)}
for (n, i), count in want.items():
    page = docs[n][i - 1]
    b = boxes(page)
    ok(len(b) == count, (n, i, 'boards', b))
    has = 'Extra workspace' in T[n][i - 1]
    ok(has == ((n, i) in labelled), (n, i, 'extra workspace label'))
    if has:
        lab = words_box(page, 'Extra workspace')
        gap = b[1][0] - lab[3]
        ok(0.05 < gap < 0.6 and lab[1] > b[0][1], (n, i, 'label sits just above the second board', gap))
# 2-3 p. 2: the longer P2 prompt clears its first board; P3 clears the second.
pg = docs['grades-2-3'][1]
b = boxes(pg)
ok(b[0][0] - words_box(pg, 'start flip over the line')[3] > 0.25, ('2-3 P2 prompt clear of board', b))
ok(words_box(pg, 'Problem 3:')[1] - b[1][1] > 0.25, '2-3 P3 clear of board')
ok(words_box(pg, 'Bellingham Math Circle')[1] - words_box(pg, 'Problem 3:')[3] > 1, '2-3 P3 clear of the footer')

# ---------------------------------------------------------------- the witnesses, exactly
V = json.loads((ROOT / 'src' / 'mathematical-checks.json').read_text())['motif_vertices']
MOTIF = [(F(str(x)), F(str(y))) for x, y in V]
FORMS = {'A': (1, 1), 'H A': (1, -1), 'V A': (-1, 1), 'R A': (-1, -1)}
h = F(3, 2)
W = {'T4': (4, [(0, h, 'A')]), 'T6': (6, [(0, h, 'A')]), 'G4': (4, [(0, h, 'A'), (2, -h, 'H A')]),
     'G': (6, [(0, h, 'A'), (3, -h, 'H A')]), 'G8': (8, [(0, h, 'A'), (4, -h, 'H A')]),
     'H': (6, [(0, h, 'A'), (0, -h, 'H A')]), 'R': (6, [(0, h, 'A'), (3, -h, 'R A')]),
     'E': (6, [(h, h, 'A'), (-h, h, 'V A'), (h, -h, 'H A'), (-h, -h, 'R A')])}


def points(P, motifs, reps=range(-3, 4)):
    """Every outline vertex of the border, in plane coordinates (y up; footprint y flips as on the pages)."""
    out = set()
    for k in reps:
        for x, y, form in motifs:
            sx, sy = FORMS[form]
            out |= {(x + P * k + sx * u, y - sy * v) for u, v in MOTIF}
    return out


def matches(name, a, b, d):
    """Does (x, y) -> (a x + d, b y) map the endless border onto itself? Checked on a window of whole periods."""
    P, motifs = W[name]
    inner, outer = points(P, motifs, range(-2, 3)), points(P, motifs, range(-7, 8))
    return all((a * x + d, b * y) in outer for x, y in inner)


def moves(name, a, b):
    P = W[name][0]
    return [d for d in (F(i, 2) for i in range(-4 * P, 4 * P + 1)) if matches(name, a, b, d)]


for name, (P, motifs) in W.items():
    slides = [d for d in moves(name, 1, 1) if d > 0]
    ok(min(slides) == P, (name, 'shortest slide', min(slides)))
for name in ('G4', 'G', 'G8'):
    P = W[name][0]
    glides = [d for d in moves(name, 1, -1) if d > 0]
    ok(min(glides) == F(P, 2) and all((d / P - F(1, 2)).denominator == 1 for d in glides), (name, 'glides (k + 1/2)P'))
    ok(not matches(name, 1, -1, 0), (name, 'flip alone fails'))
    ok(not matches(name, 1, 1, F(P, 2)), (name, 'half-length slide fails'))
# 2-3 P2/P3 witness pair: different shortest slides, each glide half its slide. K-1 P4: G8's slide is longer than G's.
ok(W['G4'][0] != W['G'][0] and min(d for d in moves('G8', 1, -1) if d > 0) > min(d for d in moves('G', 1, -1) if d > 0), 'G4/G/G8')
# 4-5 P3: any 3 cm glide along the middle line squares to a 6 cm slide; G shows a 3 cm slide need not match.
for name in W:
    for d in moves(name, 1, -1):
        ok(matches(name, 1, 1, 2 * d), (name, 'glide twice is a slide', d))
ok(matches('G', 1, -1, 3) and matches('G', 1, 1, 6) and not matches('G', 1, 1, 3), '4-5 P3 witness')
# The guide's other witness claims that the figure draws.
ok(not moves('H', -1, -1) and moves('H', 1, -1) == [d for d in moves('H', 1, 1)], 'H: flip, no half-turn')
ok(not moves('R', 1, -1) and not moves('R', -1, 1) and 3 in moves('R', -1, -1), 'R: half-turns about (1.5 + 3k, 0), no flips')
ok(0 in moves('E', -1, 1) and 0 in moves('E', 1, -1) and 0 in moves('E', -1, -1) and 3 not in moves('E', 1, 1), 'E')
# Footprints 25-30 mm wide: E's same-row neighbours are 3 cm apart, so the motif fits only up to 30 mm.
width = max(u for u, _ in MOTIF) - min(u for u, _ in MOTIF)
ok(F(25, 10) <= width <= 3, ('printed motif width (cm)', width))

# ---------------------------------------------------------------- the guide
g = pymupdf.open(build / 'facilitator-guide.pdf')
G = [text(p) for p in g]
ok(len(G) == 8, ('guide pages', len(G)))
ok('Revised October 23 2026 2 Preparation Materials and readiness' in G[1], 'p. 2 Preparation')
ok('Running the session' in G[2] and 'Concrete answer bank' in G[3] and 'Keys for K-1 and Grades 2-3' in G[4]
   and 'Key for Grades 4-5' in G[5] and 'Why these descriptions are complete' in G[5] and 'Shortest glide theorem' in G[6]
   and 'Starting routes and return visits' in G[7], 'page plan')
for i in range(7):
    ok('Unpiloted / Current base packets / Revised October 23 2026' in G[i], (i + 1, 'guide footer'))
all_g = ' '.join(G)
# Fixes 2 and 3: boards, tape, tracing.
for phrase in ('children build each border in a printed box (17.65 by 6 cm), which holds two and a half to three repeats of a 6 cm border',
               'Move to a long strip only when one repeat is longer than 6 cm',
               'tack its cards down with removable tape', 'always trace the middle line first',
               "A rough outline of each footprint with its arrow is enough, since the arrow's place and direction tell the four forms apart",
               'At K-1 the adult traces and the children move the copy'):
    ok(phrase in G[1], ('p. 2', phrase))
# Box capacity claim: with 29 mm cards a 17.65 cm box holds 2.5 to 3 repeats of every 6 cm witness.
for name in ('T6', 'G', 'H', 'R', 'E'):
    P, motifs = W[name]
    best = max(sum(1 for k in range(-2, 5) for x, _, _ in motifs
                   if F(29, 20) <= x + P * k + F(s, 10) <= F(1765, 100) - F(29, 20)) for s in range(10 * P))
    ok(F(5, 2) <= F(best, len(motifs)) <= 3, (name, 'repeats in a box', best))
# Fix 8 and second run 10: the session plan and the K-1 table.
ok('about five minutes of running around' in G[2] and 'the tables have about 35-40 minutes' in G[2], 'session timing')
for a, b in (('0-5', '5-18'), ('5-18', '18-32'), ('18-32', '32-40')):
    ok(G[2].index(a + ':') < G[2].index(b + ':'), ('timeline order', a, b))
ok('At the K-1 table, start with one repeating row' in G[2] and 'Start K-1 with' not in all_g, 'K-1 table launch')
ok('the border repeats forever both ways; only footprints count, not strip ends or guide lines; and a slide must move the copy' in G[2],
   'K-1 rules carried by the launch (fix 9)')
ok("Checking a child's own border" in G[2] and 'The borders on page 4 are witnesses' in G[2], 'checking section moved')
# Fix 5: centres, size, drawn witnesses on page 4.
ok('Positions below are footprint centres (card centres) in centimetres' in G[3] and 'anchor' not in G[3].split('Border T')[0],
   'centres')
ok('Footprints should be 25-30 mm wide' in G[3], 'size range')
polys = [d for d in g[3].get_drawings() if len(d['items']) == 12 and d.get('fill')]
ok(len(polys) == 3 + 6 + 6 + 6 + 12, ('witness footprints drawn on p. 4', len(polys)))
frames = sorted({(round(d['rect'].x0), round(d['rect'].y0)): d['rect'] for d in g[3].get_drawings()
                 if abs(d['rect'].width - 18 * .3 * CM) < 1 and abs(d['rect'].height - 6 * .3 * CM) < 1}.values(),
                key=lambda r: (r.y0, r.x0))
ok(len(frames) == 5, ('five witness boxes', len(frames)))
per = [sum(1 for p in polys if f.contains(p['rect'])) for f in frames]
ok(per == [3, 6, 6, 6, 12], ('three repeats each, inside its box', per))
for f in frames:
    inside = [p['rect'] for p in polys if f.contains(p['rect'])]
    ok(all(not (a & b).height or (a & b).width < .5 or (a & b).height < .5 for i, a in enumerate(inside) for b in inside[i + 1:]),
       'witness footprints do not overlap')
ok(polys and max(p['rect'].y1 for p in polys) / CM < 26.5, 'figure stays on the page')
ok('three repeats each, at 30% of actual size' in G[3], 'caption')
# Keys: K-1 P1 moved from the route note; changed problems keyed.
ok('K-1 Problem 1: Border T at 4 cm matches after a 4 cm slide and fails after a 2 cm slide.'.replace('K-1 ', '') in G[4]
   and 'Entry key' not in G[7] and 'K-1 continuation' not in all_g, 'K-1 P1 key on page 5')
ok('Problem 4: G8 matches after the flip and a 4 cm slide, where G used 3 cm; the flip alone still fails.' in G[4], 'K-1 P4 key')
ok('Problem 2: Border G and G4 (page 4), with shortest slides 6 and 4 cm' in G[4], '2-3 P2 key')
ok('3 and 6 cm in G, 2 and 4 cm in G4' in G[4] and 'proved on page 7' in G[4], '2-3 P3 key')
ok('A 3 cm glide is the flip over the middle line followed by a 3 cm slide along it' in G[5], '4-5 P3 key')
ok('"Explain why no other move matches" asks for the completeness argument below' in G[5], '4-5 P6 key')
ok('the geometric argument on page 6' in G[6] and 'Why these descriptions are complete' in G[5], 'page 6 reference')
ok('recipe positions on page 4 are card centres' in G[1] and "any two of page 4's borders" in G[1]
   and 'Use the recipes on page 4 as checks' in G[4], 'page 4 references')
# Second run 13: revision residue cut; version note.
ok('older v3 packets' not in all_g and 'older v2 packets' not in all_g and 'retain six problems' not in all_g, 'residue cut')
ok('K-1 v4, Problems 1-7; Grades 2-3 v4 and Grades 4-5 v4, Problems 1-6. K-1 skips v3' in G[6], 'packet basis')
ok('Grades 2-3 six on four pages and Grades 4-5 six on five pages' in G[0], 'status line')
print(f'PASS: {checks} checks on the October 23, 2026 card fixes (student pages, witnesses, guide).')
