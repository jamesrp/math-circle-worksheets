#!/usr/bin/env python3
"""Read back the delivered Week 100 student PDF and check its diagrams and data.

Independent of the package's own check_math.py and build.py.  Reads
lowell-math-circle-year-2/week-100/week-100-grades-3-5.pdf with PyMuPDF
(vector drawings + words) and:
  page 1  worked X/Y/Z example: groups, labels, cards -> distances.
  page 1  Problem 1 world: groups, labels, cards -> hierarchy, laminarity,
          labels increasing outward, full distance table (vs the guide's table).
  page 1  cut-out letter cards (shapes regular?) and label cards (counts).
  page 3  Problem 3 world: same reconstruction; must equal the page 1 world.
  page 2  the six printed triples.
  page 4  the ten clue cards;  page 5 the replacement clue card.
  page 7  the number cards and the three distance rules (text).
Writes pdf_extract.json (data for check_math.py) and check_diagrams.py.out.
Run: python3 check_diagrams.py
"""
import json
import math
import re
import sys
import warnings
from itertools import combinations
from pathlib import Path

warnings.filterwarnings('ignore')
import pymupdf as fitz  # noqa: E402

HERE = Path(__file__).resolve().parent


def find_repo():
    # Committed copy: plans/review/checks/week-100/ -> repo is four folders up
    # (parents[3] of the folder).  Run-folder copy: search upward.
    cands = []
    if len(HERE.parents) > 3:
        cands.append(HERE.parents[3])
    cands += [HERE] + list(HERE.parents)
    for c in cands:
        if (c / 'lowell-math-circle-year-2' / 'week-100').is_dir():
            return c
    raise SystemExit('repository not found above ' + str(HERE))


REPO = find_repo()
PDF = REPO / 'lowell-math-circle-year-2' / 'week-100' / 'week-100-grades-3-5.pdf'
MM = 72 / 25.4
OUT, FAILS = [], []


def say(s=''):
    OUT.append(str(s))
    print(s)


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def mm(r):
    return [v / MM for v in (r.x0, r.y0, r.x1, r.y1)]


def inside(a, b, tol=0.05):
    return a[0] >= b[0] - tol and a[1] >= b[1] - tol and a[2] <= b[2] + tol and a[3] <= b[3] + tol


def disjoint(a, b):
    return a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1]


def read_world(page, region):
    """Return cards {letter: rect}, groups [(rect, label)] inside region (mm)."""
    draws = page.get_drawings()
    words = page.get_text('words')
    cards, groups, labelboxes = [], [], []
    for d in draws:
        r = mm(d['rect'])
        if not inside(r, region, tol=1):
            continue
        w, h = r[2] - r[0], r[3] - r[1]
        n = len(d['items'])
        if d['type'] == 'fs' and n == 8 and 9 < w < 11 and 9 < h < 11:
            cards.append(r)
        elif d['type'] == 's' and n == 8 and w > 15:
            groups.append(r)
        elif d['type'] == 'f' and w < 5 and h < 5:
            labelboxes.append(r)
    letters = {}
    for c in cards:
        hits = [w[4] for w in words if inside(mm(fitz.Rect(w[:4])), c)]
        assert len(hits) == 1, hits
        letters[hits[0]] = c
    labelled = []
    for g in groups:
        # label word: centre on the group's top edge, near its right end
        cand = []
        for w in words:
            wr = mm(fitz.Rect(w[:4]))
            cx, cy = (wr[0] + wr[2]) / 2, (wr[1] + wr[3]) / 2
            if re.fullmatch(r'\d+', w[4]) and abs(cy - g[1]) < 1.5 and g[0] < cx < g[2]:
                cand.append((w[4], cx))
        assert len(cand) == 1, (g, cand)
        labelled.append((g, int(cand[0][0])))
    return letters, labelled


def hierarchy(letters, groups):
    """Members of each group; check groups never cross; labels increase outward."""
    mem = []
    for g, lab in groups:
        s = frozenset(k for k, c in letters.items() if inside(c, g))
        # a card must be wholly inside or wholly outside each loop
        bad = [k for k, c in letters.items() if not inside(c, g) and not disjoint(c, g)]
        check(not bad, f'loop labelled {lab} around {sorted(s)}: no card straddles it')
        mem.append((s, lab, g))
    ok = True
    for (s1, l1, g1), (s2, l2, g2) in combinations(mem, 2):
        if inside(g1, g2) or inside(g2, g1) or disjoint(g1, g2):
            pass
        else:
            ok = False
            say(f'  loops cross: {sorted(s1)}@{l1} and {sorted(s2)}@{l2}')
        if inside(g1, g2):
            ok &= l1 < l2 and s1 <= s2
        if inside(g2, g1):
            ok &= l2 < l1 and s2 <= s1
        if disjoint(g1, g2):
            ok &= not (s1 & s2)
    check(ok, 'loops nested or disjoint, labels strictly increase outward')
    allcards = frozenset(letters)
    check(any(s == allcards for s, _, _ in mem), 'one loop contains all the cards')
    return [(sorted(s), lab) for s, lab, _ in mem]


def distances(letters, groups):
    d = {}
    for a, b in combinations(sorted(letters), 2):
        common = [(len(s), lab) for s, lab in groups if a in s and b in s]
        # smallest common group = fewest cards (groups are nested)
        d[a + b] = min(common)[1]
    return d


def main():
    doc = fitz.open(PDF)
    say(f'PDF: {PDF.relative_to(REPO)}  pages={len(doc)}')
    data = {}

    # page 1 worked example
    p1 = doc[0]
    letters, groups = read_world(p1, [10, 60, 135, 110])
    say(f'p1 worked example cards={sorted(letters)} groups={[(lab) for _, lab in groups]}')
    gh = hierarchy(letters, groups)
    dx = distances(letters, gh)
    say(f'  hierarchy {gh}  distances {dx}')
    check(dx == {'XY': 3, 'XZ': 6, 'YZ': 6}, 'worked example: X-Z = 6, X-Y = 3 as printed')
    data['worked'] = {'groups': gh, 'dist': dx}

    # page 1 Problem 1 world
    letters, groups = read_world(p1, [140, 95, 265, 170])
    say(f'p1 Problem 1 world cards={sorted(letters)}')
    w1 = hierarchy(letters, groups)
    d1 = distances(letters, w1)
    say(f'  hierarchy {w1}')
    say(f'  distances {d1}')
    data['world1'] = {'groups': w1, 'dist': d1}
    guide_table = {  # transcribed from facilitator guide p.3 (Problem 1 table)
        'AB': 2, 'AC': 8, 'AD': 4, 'AE': 8, 'AF': 8, 'BC': 8, 'BD': 4, 'BE': 8, 'BF': 8,
        'CD': 8, 'CE': 2, 'CF': 8, 'DE': 8, 'DF': 8, 'EF': 8}
    check(d1 == guide_table, 'Problem 1 world distances equal the guide table (p.3)')

    # page 3 world
    p3 = doc[2]
    letters, groups = read_world(p3, [140, 40, 270, 120])
    w3 = hierarchy(letters, groups)
    d3 = distances(letters, w3)
    check(d3 == d1 and sorted(map(str, w3)) == sorted(map(str, w1)),
          'Problem 3 world is the same world as Problem 1')

    # letter cards & label cards on page 1
    draws = p1.get_drawings()
    shapes = []
    for d in draws:
        r = mm(d['rect'])
        if r[1] > 175 and 5 < r[2] - r[0] < 12:
            pts = []
            for it in d['items']:
                for q in it[1:]:
                    if hasattr(q, 'x'):
                        pts.append((q.x / MM, q.y / MM))
            shapes.append((d['items'][0][0], len(d['items']), r, pts))
    names = []
    for kind, n, r, pts in shapes:
        if kind == 'c':
            names.append('circle')
            continue
        verts = []
        for p in pts:
            if not any(abs(p[0] - v[0]) < 1e-3 and abs(p[1] - v[1]) < 1e-3 for v in verts):
                verts.append(p)
        k = len(verts)
        sides = [math.dist(verts[i], verts[(i + 1) % k]) for i in range(k)]
        names.append(f'{k}-gon sides {[round(s, 2) for s in sides]}')
    say('p1 letter-card shapes (A..F): ' + '; '.join(names))
    words = p1.get_text('words')
    labs = [w[4] for w in words if 165 < w[1] / MM < 200 and w[0] / MM > 185 and re.fullmatch(r'\d', w[4])]
    counts = {v: labs.count(v) for v in sorted(set(labs))}
    say(f'p1 label cards: {counts}')
    data['label_cards'] = {k: v for k, v in counts.items()}

    # page 2 triples
    t2 = doc[1].get_text()
    trip = re.findall(r'A–B = (\d)\s+A–C = (\d)\s+B–C = (\d)', t2)
    say(f'p2 triples (AB,AC,BC) in reading order: {trip}')
    check(len(trip) == 6, 'six triples on page 2')
    data['triples'] = [list(map(int, t)) for t in trip]

    # page 4 clue cards, page 5 card
    t4 = doc[3].get_text()
    clues = re.findall(r'([A-E])–([A-E]) = (\d)', t4)
    say(f'p4 clue cards: {clues}')
    check(len(clues) == 10 and len({a + b for a, b, _ in clues}) == 10, 'ten distinct pair clues')
    data['clues'] = {a + b: int(v) for a, b, v in clues}
    t5 = doc[4].get_text()
    c5 = re.findall(r'([A-E])–([A-E]) = (\d)', t5)
    say(f'p5 replacement card: {c5}')
    data['p5card'] = c5

    # page 7 number cards & rules
    t7 = doc[6].get_text()
    nums = [w[4] for w in doc[6].get_text('words') if 160 < w[1] / MM < 200 and re.fullmatch(r'\d', w[4])]
    say(f'p7 number cards: {nums}')
    check(nums == [str(i) for i in range(8)], 'number cards 0..7')
    for pat in ['One card is even and the other is odd: distance 8.',
                'Both are even or both are odd, with different remainders after division by 4: distance 4.',
                'They have the same remainder after division by 4: distance 2.']:
        check(pat in t7.replace('\n', ' '), f'p7 rule printed: "{pat}"')

    # guide: sentences quoted in math.md are present verbatim
    g = fitz.open(PDF.parent / 'week-100-facilitator.pdf')
    gtext = [' '.join(pg.get_text().split()) for pg in g]
    # The guide as reviewed, before the October 23, 2026 card fixes, for sentences those fixes rewrote.
    rtext = [' '.join(pg.get_text().split()) for pg in fitz.open(PDF.parent / 'archive-before-card-fixes-2026-10-23' / 'week-100-facilitator.pdf')]
    stext = ' '.join(' '.join(pg.get_text().split()) for pg in doc)
    rstext = ' '.join(' '.join(pg.get_text().split()) for pg in fitz.open(PDF.parent / 'archive-before-card-fixes-2026-10-23' / 'week-100-grades-3-5.pdf'))
    for pg, q in [(5, 'Exactly one largest distance is impossible by the nested-group argument on page 1.'),
                  (5, 'The divisibility proof on page 1 explains the wider 2-adic connection.'),
                  (5, 'Problems 6–7, page 6: beyond a few examples'),
                  (5, 'Problems 8–9, page 7: the eight-number world'),
                  (1, 'it divides their sum'),
                  (1, 'both contain'),
                  (2, 'labels 2, 4 and 8'),
                  (2, 'Print extra copies of student pages 1, 4, 5 and 7 for cutting cards')]:
        if q not in gtext[pg - 1] and q in rtext[pg - 1]:
            check(True, f'guide p.{pg} as reviewed (archived; the card fixes rewrote it) contains "{q}"')
            continue
        check(q in gtext[pg - 1], f'guide p.{pg} contains "{q}"')
    for q in ['Change exactly one of the ten clues to a different value chosen from 2, 4, 8, so that a world is possible.',
              'Use cards A through F and labels 2, 4, 8. One player builds a world in secret.']:
        if q not in stext and q in rstext:
            check(True, f'student packet as reviewed (archived; the card fixes rewrote it) contains "{q}"')
            continue
        check(q in stext, f'student packet contains "{q}"')
    # does student page 1 contain any argument the guide could mean?
    p1t = gtext and ' '.join(doc[0].get_text().split())
    check(all(w not in p1t for w in ('divid', 'both contain', 'prov', 'because')),
          'student page 1 has no divisibility or nesting argument (only rules and the X/Y/Z example)')

    (HERE / 'pdf_extract.json').write_text(json.dumps(data, indent=1))
    say()
    say('FAILS: ' + (', '.join(FAILS) if FAILS else 'none'))
    (HERE / 'check_diagrams.py.out').write_text('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
