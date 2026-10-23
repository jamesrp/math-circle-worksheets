#!/usr/bin/env python3
"""Check every claim changed by the October 23, 2026 review-card fixes (Week 38, v4).

    python3 review/verify_card_shoulds_2026_10_23.py [PDF_DIR] [--bonus DIR]

PDF_DIR holds k-1.pdf, grades-2-3.pdf, grades-4-5.pdf, facilitator-guide.pdf and
materials.pdf (default: reference-pdfs/). --bonus DIR holds week-38-bonus.pdf and
week-38-bonus-facilitator.pdf. The mathematics is recomputed from seam
identifications of lanes; the pages are read back with PyMuPDF. Prints each
check and exits 1 on any failure. The strips page has its own fuller check,
materials-src/check_materials.py.
"""
from itertools import product
import re
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
args = [a for a in sys.argv[1:] if not a.startswith('--')]
PDF = Path(args[0]) if args else HERE.parent / 'reference-pdfs'
BONUS = Path(sys.argv[sys.argv.index('--bonus') + 1]) if '--bonus' in sys.argv else None
FAIL = []


def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg)
    if not ok:
        FAIL.append(msg)


def pages(path):
    return [' '.join(p.get_text().split()) for p in pymupdf.open(path)]


# ---------------------------------------------------------------- mathematics
def cut(n, reversing, cuts):
    """Pieces, boundary circles and one-sided pieces of a band of n lanes after cuts.

    Lane i meets lane n-1-i at a reversing seam (top and bottom swap) or lane i at a
    matching one. cuts[j] says whether the line between lanes j and j+1 is cut.
    """
    ident = (lambda i: (n - 1 - i, 1)) if reversing else (lambda i: (i, 0))
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for j in range(n - 1):
        if not cuts[j]:
            parent[find(j)] = find(j + 1)
    for i in range(n):
        parent[find(i)] = find(ident(i)[0])
    roots = {find(i) for i in range(n)}
    edges = [(i, s) for i in range(n) for s in (0, 1)
             if (s == 0 and (i == 0 or cuts[i - 1])) or (s == 1 and (i == n - 1 or cuts[i]))]
    seen, circles = set(), 0
    for e in edges:
        if e in seen:
            continue
        circles += 1
        while e not in seen:
            seen.add(e)
            j, rev = ident(e[0])
            e = (j, e[1] ^ rev)
    one_sided = 0
    for r in roots:
        start = min(i for i in range(n) if find(i) == r)
        i, flips = start, 0
        while True:
            i, rev = ident(i)
            flips += rev
            if i == start:
                break
        one_sided += flips % 2
    return len(roots), circles, one_sided


PARTS = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]


def pictures(b):
    """Four-dot ring pictures possible with b boundary circles, by placing dots."""
    seen = {tuple(sorted((a.count(k) for k in set(a)), reverse=True)) for a in product(range(b), repeat=4)}
    return [p for p in PARTS if p in seen]


check(cut(1, False, []) == (1, 2, 0) and cut(1, True, []) == (1, 1, 1), 'uncut: A one piece with 2 edges; B one piece with 1 edge, one-sided')
check(cut(2, False, [True]) == (2, 4, 0) and cut(2, True, [True]) == (1, 2, 0), 'middle cut: A 2 pieces, 4 edges; B 1 two-sided piece, 2 edges')
third = cut(3, True, [True, True])
check(third == (2, 3, 1), f'one-third cut of B (fix 3): {third[0]} pieces, {third[1]} edges, {third[2]} one-sided (thin Moebius band + annulus)')
# the lines at 1/3 and 2/3 of the height are one closed cut: a reversing seam sends height h to 1-h
check(abs((1 - 1 / 3) - 2 / 3) < 1e-12, 'the dotted lines at 1/3 and 2/3 meet at a reversing seam: one closed cut, twice round')
check(pictures(3) == PARTS[:4], 'three edges: every four-dot picture but 1+1+1+1')
check(pictures(4) == PARTS and pictures(2) == PARTS[:3] and pictures(1) == PARTS[:1], 'P3/P6 tables: 4 edges all five, 2 edges top three, 1 edge only 4')
# arrow transport (fix 4): one trip round the centre line crosses the seam once
check(cut(1, True, [])[2] == 1, 'B: one trip reverses the transverse arrow, so it returns on the other face (one-sided)')
# bonus fix 1: joining strip 2 to strip 1 dot to square (R) reverses; dot to dot (M) does not
def seam_from_marks(left_top, right_top):
    return 'M' if left_top == right_top else 'R'
check(seam_from_marks('dot', 'dot') == 'M' and seam_from_marks('dot', 'square') == 'R', 'bonus: dot to dot is M whatever the turn; dot to square is R')
def chain_edges(word):
    """Closed edges of a circle of strips joined by the seams in word, traced side by side."""
    n, seen, circles = len(word), set(), 0
    for e in [(j, s) for j in range(n) for s in (0, 1)]:
        if e in seen:
            continue
        circles += 1
        while e not in seen:
            seen.add(e)
            e = ((e[0] + 1) % n, e[1] ^ (word[e[0]] == 'R'))
    return circles


check(all(chain_edges(w) == (1 if w.count('R') % 2 else 2) for n in range(1, 6) for w in product('MR', repeat=n)),
      'bonus P2: a circle of strips has one edge exactly when the number of R seams is odd (all words up to 5 seams)')

# ---------------------------------------------------------------- student pages
K, T, F = (pages(PDF / f) for f in ('k-1.pdf', 'grades-2-3.pdf', 'grades-4-5.pdf'))
for name, pp, tag in (('K-1', K, 'K'), ('2-3', T, '23'), ('4-5', F, '45')):
    whole = ' '.join(pp)
    check(len(pp) == 7, f'{name}: 7 pages')
    nums = [int(x) for x in re.findall(r'Problem (\d+):', whole)]
    check(nums == list(range(1, 8)), f'{name}: Problems 1-7 in order')
    check(all(f'F38-{tag}-v4' in p for p in pp), f'{name}: footers F38-{tag}-v4')
    check('The rings record' not in whole, f'{name}: "The rings record which dots share an edge." is cut (fix 5)')
    check(('The rectangles are joining recipes.' in whole) == (name == '4-5'), f'{name}: "joining recipes" only in grades 4-5 (fix 5)')
    p3 = next(i for i, p in enumerate(pp) if 'Problem 3:' in p)
    p2 = next(i for i, p in enumerate(pp) if 'Problem 2:' in p)
    check('Dots on one edge go in one ring.' in pp[p3] and 'flat paper washer' in pp[p3]
          and pp[p3].index('flat paper washer') < pp[p3].index('Problem 3:') and 'washer' not in pp[p2],
          f'{name}: the ring sentence and the washer sit above Problem 3, not under Problem 2 (fix 5)')
    check('cross it out' not in whole, f'{name}: no "cross it out" (fix 7)')
    check(pp[p3].count('Write yes or no in each blank') == 1, f'{name}: Problem 3 asks for yes or no in each blank (fix 7)')
    p6 = next(i for i, p in enumerate(pp) if 'Problem 6:' in p)
    if name != '4-5':
        check('Write yes or no in each blank' in pp[p6], f'{name}: Problem 6 asks for yes or no (fix 7)')
        p7 = pp[6]
        check(p7.startswith(f'Week 38 / Seams /') and 'Problem 7: An adult cuts a new B one third of the way across, going round until the cut closes. Which four-dot pictures can you make now? Write yes or no in each blank.' in p7
              and p7.count('new B:') == 5, f'{name}: Problem 7 is the one-third cut with five "new B" blanks (fix 3)')
        check('every cut piece' not in whole and 'no edge trip reaches two dots' not in whole, f'{name}: the old Problem 7 is gone (fix 3)')
    else:
        p7 = pp[6]
        check('Problem 7:' in p7 and 'Problem 6:' not in p7 and p7.count('cut A:') == 5 and p7.count('cut B:') == 5,
              '4-5: Problem 7 has its own page with the pictures and cut A / cut B blanks (fix 6)')
        check('separates connected pieces' not in whole, '4-5: "how your answer separates connected pieces from boundary components" is cut (could 8)')
# the box for 4-5 Problem 2 (fix 5): a stroked rectangle at least 150 x 80 mm on its page
doc = pymupdf.open(PDF / 'grades-4-5.pdf')
pg = doc[next(i for i, p in enumerate(F) if 'Problem 2:' in p)]
MM = 72 / 25.4
boxes = [d['rect'] for d in pg.get_drawings() if d['rect'].width > 150 * MM and d['rect'].height > 80 * MM]
check(len(boxes) == 1, '4-5: Problem 2 has an answer box (fix 5)')

# ---------------------------------------------------------------- guide and strips
G = pages(PDF / 'facilitator-guide.pdf')
g = ' '.join(G)
check(len(G) == 7, 'guide: 7 pages (6 plus the route note)')
check('260 × 45 mm' in g and '400 mm' not in g and '600 mm' not in g and 'week-38-materials.pdf' in g
      and 'sheet 1 fourteen times' in g and 'sheet 2 three times' in g, 'guide p. 2: printed 260 x 45 mm strips and print counts (fix 2)')
check('On B the arrow comes back on the other face; that is one-sidedness, not a flip.' in G[1]
      and 'On B the arrow comes back on the other face; that is one-sidedness, not a flip.' in G[4]
      and 'Write U and L on the back' in G[1], 'guide pp. 2 and 5: one-sidedness, not a flip; U and L on both faces (fix 4)')
check('three edges' in G[2].lower() or 'Three closed edges in all' in G[2], 'guide p. 3: K-1 Problem 7 key has three edges')
check('1+1+1+1 is no' in G[2] and 'no for 1+1+1+1' in G[3] and 'goes round the new B twice' in G[3], 'guide pp. 3-4: Problem 7 keys for the one-third cut (fix 3)')
check('use the flat washer above it on page 3' in G[1], 'guide p. 2: the launch points to the washer on page 3')
rows = re.findall(r'(\d+)–(\d+) min(?!u)', G[1])
check(rows and int(rows[-1][1]) == 40 and int(rows[0][0]) == 0 and 'Suggested first visit, 35–40 minutes at the tables' in G[1],
      f'guide p. 2: the timetable fills 35-40 minutes at the tables (could 9): {rows}')
check('bonus Problem 1' in G[6], 'guide p. 7: quick grades 2-3 and 4-5 go on to bonus Problem 1 (could 10)')
check('F38-K-v4, F38-23-v4 and F38-45-v4' in G[5] and 'W38-M-v1' in G[5], 'guide p. 6: key alignment v4 and the strips')
M = pages(PDF / 'materials.pdf')
check(len(M) == 2 and all('W38-M-v1' in p for p in M) and 'Print 14 copies' in M[0] and 'Print 3 copies' in M[1], 'strips: two pages, W38-M-v1, print counts')

# ---------------------------------------------------------------- bonus
if BONUS:
    S = pages(BONUS / 'week-38-bonus.pdf')
    check('align the ends' in S[1] and 'align the same marks' not in S[1]
          and 'M joins dot to dot; R half-turns strip 2, then joins dot to square.' in S[1]
          and all('W38-BONUS-v2' in p for p in S), 'bonus p. 2: "align the ends", the M/R caption, footer v2 (fix 1)')
    pg = pymupdf.open(BONUS / 'week-38-bonus.pdf')[1]
    # the R row of the middle column: marks at x 260 and 344 (PDF y up 596 +- 12)
    H = pg.rect.height
    marks = {}
    for d in pg.get_drawings():
        r = d['rect']
        cx, cy = (r.x0 + r.x1) / 2, H - (r.y0 + r.y1) / 2
        if 250 < cx < 354 and r.width < 8 and r.height < 8:
            kind = 'dot' if any(it[0] == 'c' for it in d['items']) else 'square'
            marks[(round(cx), round(cy))] = kind
    m_row = (marks.get((260, 662)), marks.get((344, 662)), marks.get((260, 638)), marks.get((344, 638)))
    r_row = (marks.get((260, 608)), marks.get((344, 608)), marks.get((260, 584)), marks.get((344, 584)))
    check(m_row == ('dot', 'dot', 'square', 'square'), f'bonus p. 2: M row joins dot to dot, square to square {m_row}')
    check(r_row == ('dot', 'square', 'square', 'dot'), f'bonus p. 2: R row joins dot to square, square to dot {r_row} (fix 1)')
    B = ' '.join(pages(BONUS / 'week-38-bonus-facilitator.pdf'))
    check('KK11' not in B and '3333' not in B and ' 445' not in B and 'K–1 / 2–3 / 4–5' in B, 'bonus guide: K-1 / 2-3 / 4-5 for KK11 / 3333 / 445 (could 11)')
    check('M joins dot to dot; R, after a half-turn, joins dot to square' in B and 'same-mark alignment' not in B
          and B.count('W38-BONUS-FAC-v2') == 2, 'bonus guide: the launch and materials say how M and R join; footer v2 (fix 1)')

print(f'{len(FAIL)} failure(s)')
sys.exit(1 if FAIL else 0)
