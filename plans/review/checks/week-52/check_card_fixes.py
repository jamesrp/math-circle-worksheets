"""Check the October 23, 2026 card fixes to Week 52 (F52-S-v3, F52-FAC-v3).

Mathematics, by the same independent certificates as check_math.py (exact rank
mod two primes for "holds", an explicit finite motion for "flexes"):
  * must 2: Problem 13 as reworded, "braces in six different cells, with a brace
    in every row and column", always holds; with doubled braces it need not;
  * should 4: the 2-by-3 designs that brace every row and column but still flex
    are exactly six, each with three braces, and every empty cell repairs each;
  * must 1 and should 6: the kit and print counts in the revised guide.
Delivered pages, read from the PDF with PyMuPDF (geom52.py):
  * pages 3-4 headed Grades K-3; the frame rules open pages 3, 5 and 10;
  * Problem 13's printed wording; two 4-by-4 boards for Problem 14;
  * the page 1 triangle and square drawn with equal bars (could 9).

Run: python3 check_card_fixes.py [students.pdf] [facilitator.pdf]
(defaults: the print PDFs); writes out_check_card_fixes.txt beside itself.
"""
import itertools
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import check_math as cm  # noqa: E402
import geom52  # noqa: E402
import pymupdf  # noqa: E402

OUT = []
FAIL = []


def say(*a):
    s = ' '.join(str(x) for x in a)
    OUT.append(s)
    print(s)


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def kit(m, n):
    """Side bars, braces (one per cell) and pins of a complete m-by-n grid."""
    return m * (n + 1) + n * (m + 1), m * n, (m + 1) * (n + 1)


def main():
    student = sys.argv[1] if len(sys.argv) > 1 else str(geom52.STUDENT_PDF)
    guide = sys.argv[2] if len(sys.argv) > 2 else str(geom52.GUIDE_PDF)
    say('Week 52 card fixes, October 23, 2026')
    say('=' * 60)

    say('\n[must 2] Problem 13: braces in six different cells covering every row and column')
    sets = list(itertools.combinations(cm.cells(3, 3), 6))
    cov = [S for S in sets if cm.covers(3, 3, S)]
    res = [cm.decide(3, 3, list(S)) for S in cov]
    check(len(sets) == 84 and len(cov) == 78, '84 six-cell sets, 78 cover every row and column')
    check(all(r == 'holds' for r in res), 'all 78 hold (rank certificate): the reworded claim is true')
    doubled = [(i, i, o) for i in (1, 2, 3) for o in '/\\']
    check(cm.covers(3, 3, doubled) and cm.decide(3, 3, doubled) == 'flexes',
          'doubled braces in 11, 22, 33: six braces cover every row and column and flex (finite motion)')
    placements = list(itertools.combinations([(i, j, o) for (i, j) in cm.cells(3, 3) for o in '/\\'], 6))
    cov2 = [P for P in placements if cm.covers(3, 3, P)]
    flex2 = [P for P in cov2 if cm.decide(3, 3, list(P)) == 'flexes']
    say(f'     covering six-brace placements with doubling allowed: {len(cov2)}, of which {len(flex2)} flex')
    check(len(flex2) > 0, 'so "different cells" is needed for the answer Yes')

    say('\n[should 4] 2-by-3 designs that brace every row and column and still flex')
    found = [S for k in range(7) for S in itertools.combinations(cm.cells(2, 3), k)
             if cm.covers(2, 3, S) and cm.decide(2, 3, list(S)) == 'flexes']
    say('     ', [cm.fmt(S) for S in found])
    check(len(found) == 6 and all(len(S) == 3 for S in found), 'exactly six, each with three braces')
    check(all(len({j for (i, j) in S}) == 3 and len({i for (i, j) in S}) == 2 for S in found),
          'each braces every column in one row only and uses both rows')
    check(all(cm.decide(2, 3, list(S) + [c]) == 'holds' for S in found for c in cm.cells(2, 3) if c not in S),
          'in each, every empty cell makes it hold')
    check(((1, 1), (1, 2), (2, 3)) in found, 'the guide figure 11, 12, 23 is one of the six')
    check(cm.decide(2, 3, []) == 'flexes' and cm.decide(2, 3, [(1, 1), (1, 2), (2, 3)]) == 'flexes'
          and cm.decide(2, 3, [(1, 1), (1, 2), (1, 3), (2, 1)]) == 'holds',
          'should 5 stock test on one 2-by-3: unbraced and 11, 12, 23 move; 11, 12, 13, 21 holds')

    say('\n[must 1, should 6] kits and printing in the revised guide')
    tri_sq = (3 + 4, 1, 3 + 4)
    check(kit(1, 1) == (4, 1, 4) and kit(2, 2) == (12, 4, 9) and kit(2, 3) == (17, 6, 12), 'per-kit counts')
    rows = {'K-1 triangle and square': (2, tri_sq), 'K-1 2-by-2': (2, kit(2, 2)), 'Grades 2-3 2-by-2': (2, kit(2, 2)),
            'upper 2-by-3 with spare': (2, kit(2, 3)), 'demonstration square': (1, kit(1, 1))}
    table = {'K-1 triangle and square': (14, 2, 14), 'K-1 2-by-2': (24, 8, 18), 'Grades 2-3 2-by-2': (24, 8, 18),
             'upper 2-by-3 with spare': (34, 12, 24), 'demonstration square': (4, 1, 4)}
    check(all(tuple(n * x for x in k) == table[name] for name, (n, k) in rows.items()), 'each printed table row')
    base = tuple(sum(v[i] for v in table.values()) for i in range(3))
    spares = (8, 4, 12)
    total = tuple(b + s for b, s in zip(base, spares))
    check(base == (100, 31, 78) and total == (108, 35, 90), f'base totals {base}, with spares {total}')
    check(table['K-1 2-by-2'] == (24, 8, 18), 'card: a 2-by-2 for each K-1 pair is 24 sides, 8 braces, 18 pins')
    ext = tuple(a - b for a, b in zip(kit(2, 3), kit(2, 2)))
    check(ext == (5, 2, 3) and all(e <= s for e, s in zip(ext, spares)),
          'extending a 2-by-2 to a 2-by-3 takes 5 sides, 2 braces, 3 pins, within the loose spares')
    check(2 * 4 + 2 * 2 + 2 + 5 + 3 == 22, 'printing: K-1 8 + Grades 2-3 4 + 2 + upper 5 + return 3 = 22 sheets')

    say('\n[pages] the delivered student PDF: ' + os.path.relpath(student, geom52.ROOT))
    doc = pymupdf.open(student)
    check(len(doc) == 12, '12 pages')
    heads = []
    for page in doc:
        line = next(l for l in page.get_text().splitlines() if l.startswith('Week 52 / '))
        heads.append(line.rsplit('/ ', 1)[1])
    say('     headers:', heads)
    check(heads == ['Grades K–1'] * 2 + ['Grades K–3'] * 2 + ['Grades 3–5'] * 5 + ['Grades 4–5'] * 3,
          'pages 1-2 K-1, 3-4 K-3, 5-9 3-5, 10-12 4-5')
    text = [' '.join(p.get_text().split()) for p in doc]
    flat = 'Keep the frames flat. Moving or turning the whole frame does not change its shape.'
    check(all(flat in text[i] for i in (2, 4, 9)), 'the frame rule opens pages 3, 5 and 10')
    check('use at most one diagonal brace in each cell' in text[2] and
          all('Use at most one brace in each cell.' in text[i] for i in (4, 9)), 'the one-brace rule on pages 3, 5 and 10')
    check('Drawings are recording maps' not in text[0], 'page 1 no longer narrates the drawings')
    check('A 3-by-3 grid has braces in six different cells, with a brace in every row and column. Must it hold its shape?'
          in text[10], 'Problem 13 prints the reworded claim')
    p14 = [g for g in geom52.read_page(doc[11], 'student')[0] if (g['m'], g['n']) == (4, 4)]
    check(len(p14) == 2 and all(g['full'] and g['joints'] == 25 and not g['cells'] for g in p14),
          'Problem 14 has two blank 4-by-4 boards')
    check(all(max(g['dx'] + g['dy']) - min(g['dx'] + g['dy']) < 0.05 for g in p14), 'with square cells')
    thick = [d for d in doc[0].get_drawings() if d.get('width') and abs(d['width'] - 2.0) < 0.05]
    sides = []
    for d in thick:
        segs = [math.dist(it[1], it[2]) for it in d['items'] if it[0] == 'l']
        segs += [v for it in d['items'] if it[0] == 're' for v in (it[1].width, it[1].height) * 2]
        segs = [v for v in segs if v > 1]
        sides.append(('square' if len(segs) == 4 else 'triangle' if len(segs) == 3 else '?', segs))
    say('     page 1 bar lengths (mm):', [(n, [round(v * 25.4 / 72, 2) for v in s]) for n, s in sides])
    lengths = [v for _, s in sides for v in s]
    check(sorted(n for n, _ in sides) == ['square', 'triangle'] and max(lengths) - min(lengths) < 0.1, 'triangle and square drawn with equal bars')

    say('\n[guide] the delivered guide PDF: ' + os.path.relpath(guide, geom52.ROOT))
    g = ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(guide))
    for phrase in ('K–1: 2-by-2 cell grid 2 24 8 18', 'Base totals 100 31 78', 'Prepare altogether 108 35 90',
                   'K–1: 2 copies each of pages 1–4', 'Total 22 student sheets', 'K–1 P1–3, then P4 and P5',
                   'Leave the test to the tables', 'There are six such designs, each with three braces',
                   'parent with K–1', 'organizer with 4–5', 'F52-S-v3',
                   'Build and test one 2-by-3', 'braced in 11, 12, 23 it should still move'):
        check(phrase in g, f'guide says "{phrase}"')

    say('\n' + ('ALL CHECKS PASSED' if not FAIL else 'FAILURES: %d' % len(FAIL)))
    for f in FAIL:
        say('  - ' + f)
    with open(os.path.join(HERE, 'out_check_card_fixes.txt'), 'w') as fh:
        fh.write('\n'.join(OUT) + '\n')
    return not FAIL


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
