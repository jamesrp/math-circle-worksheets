"""Compare every printed Week 52 diagram (read from the delivered PDFs) with a
hand transcription made from the rendered pages and with the designs that the
problem text and the guide's answers refer to.

Checks: grid size (rows x columns), equal cell spacing in x and y (square
cells), every side bar spanning the grid, one joint circle per grid point,
brace cells and their orientation, R/C labels centred on their strips, link
pictures (which dots exist and which links are drawn), and the K-1 triangle
and square on page 1.
Run: python3 check_diagrams.py  (writes out_check_diagrams.txt beside itself)
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
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


ALL6 = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)}
# Hand transcription from the 80 dpi renders: page -> list of (name, rows, cols, braces, labelled)
STUDENT = {
    2: [('P2 left', 1, 1, set(), False), ('P2 right', 1, 1, set(), False)],
    3: [('P4A', 2, 2, {(1, 1)}, False), ('P4B', 2, 2, {(1, 1), (2, 2)}, False),
        ('P4C', 2, 2, {(1, 1), (1, 2), (2, 1)}, False), ('P4D', 2, 2, {(1, 1), (1, 2), (2, 1), (2, 2)}, False)],
    4: [('P5 board %d' % k, 2, 2, set(), False) for k in range(1, 5)],
    5: [('P6 board %d' % k, 2, 3, set(), False) for k in range(1, 5)],
    6: [('example frame', 1, 3, {(1, 2)}, False), ('example labels', 1, 3, {(1, 2)}, True),
        ('P7A', 2, 3, {(1, 1), (1, 2), (2, 1), (2, 2)}, True), ('P7B', 2, 3, {(1, 1), (1, 2), (1, 3), (2, 1)}, True)],
    7: [('P8A', 3, 3, {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}, True),
        ('P8B', 3, 3, {(1, 1), (1, 2), (1, 3), (2, 1), (3, 1)}, True)],
    8: [('P9', 2, 3, {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2)}, True)] +
       [('P10 board %d' % k, 2, 3, ALL6, True) for k in range(1, 5)],
    9: [('P11A', 3, 3, {(1, 1), (1, 2), (2, 1), (2, 2)}, True),
        ('P11B', 3, 3, {(1, 1), (1, 2), (2, 2), (3, 3)}, True)],
    10: [('P12', 4, 5, set(), True)],
    11: [('P13 left', 3, 3, set(), True), ('P13 right', 3, 3, set(), True)],
    12: [('P14', 4, 4, set(), True)],
}
STUDENT_LINKS = {
    6: [('example links', 1, 3, {(1, 2)}), ('P7A blank', 2, 3, set()), ('P7B blank', 2, 3, set())],
    7: [('P8A blank', 3, 3, set()), ('P8B blank', 3, 3, set())],
    8: [('P9 links', 2, 3, {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2)})],
    9: [('P11A blank', 3, 3, set()), ('P11B blank', 3, 3, set())],
}
GUIDE = {
    4: [('handoff grid', 2, 3, {(1, 1), (1, 2), (2, 3)}, True)],
    8: [('P14 counterexample', 4, 4, {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (4, 4)}, True)],
}
GUIDE_LINKS = {
    4: [('handoff links', 2, 3, {(1, 1), (1, 2), (2, 3)})],
    6: [('P7A answer', 2, 3, {(1, 1), (1, 2), (2, 1), (2, 2)}), ('P7B answer', 2, 3, {(1, 1), (1, 2), (1, 3), (2, 1)}),
        ('P8A answer', 3, 3, {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}),
        ('P8B answer', 3, 3, {(1, 1), (1, 2), (1, 3), (2, 1), (3, 1)})],
    7: [('P11A answer', 3, 3, {(1, 1), (1, 2), (2, 1), (2, 2)}), ('P11B answer', 3, 3, {(1, 1), (1, 2), (2, 2), (3, 3)})],
}


def compare(doc_name, pages, grids_t, links_t):
    for pno in range(1, len(pages) + 1):
        grids, pics = pages[pno - 1]
        want = grids_t.get(pno, [])
        check(len(grids) == len(want), '%s p%d: %d grids found, %d transcribed' % (doc_name, pno, len(grids), len(want)))
        for g, (name, m, n, br, lab) in zip(grids, want):
            cells = {(c[0], c[1]) for c in g['cells']}
            orients = {c[2] for c in g['cells']}
            sq = max(g['dx'] + g['dy']) - min(g['dx'] + g['dy']) < 0.05
            ok = (g['m'], g['n']) == (m, n) and cells == br and g['full'] and g['joints'] == (m + 1) * (n + 1) \
                and not g['stray_braces'] and sq and (g['labels_ok'] if lab else not g['labelled'])
            say('     %-20s %dx%d cell %.2fpt braces %s orient %s labels %s' % (
                name, g['m'], g['n'], g['dx'][0], ','.join('%d%d' % c for c in sorted(cells)) or '-',
                ''.join(sorted(orients)) or '-', g['labels_ok']))
            check(ok, '%s p%d %s matches transcription (size, braces, square cells, full bars, joints, labels)' % (doc_name, pno, name))
        wl = links_t.get(pno, [])
        check(len(pics) == len(wl), '%s p%d: %d link pictures found, %d transcribed' % (doc_name, pno, len(pics), len(wl)))
        for p, (name, m, n, links) in zip(pics, wl):
            names = sorted(['R%d' % i for i in range(1, m + 1)] + ['C%d' % j for j in range(1, n + 1)])
            say('     %-20s dots %s links %s' % (name, ' '.join(p['names']), ','.join('%d%d' % l for l in sorted(p['links'])) or '-'))
            check(p['names'] == names and p['links'] == links and not p['unmatched'],
                  '%s p%d %s: all dots present and links exactly as transcribed' % (doc_name, pno, name))


def main():
    say('Week 52 diagram check (delivered PDFs)')
    say('=' * 60)
    sp = geom52.read(geom52.STUDENT_PDF, 'student')
    gp = geom52.read(geom52.GUIDE_PDF, 'guide')
    check(len(sp) == 12 and len(gp) == 10, 'student 12 pages, guide 10 pages')
    compare('student', sp, STUDENT, STUDENT_LINKS)
    compare('guide', gp, GUIDE, GUIDE_LINKS)

    say('\n[page 1] K-1 triangle and square (thick 2pt outlines)')
    doc = pymupdf.open(str(geom52.STUDENT_PDF))
    polys = []
    for d in doc[0].get_drawings():
        if d['type'] == 's' and (d.get('width') or 0) > 1.5:
            segs = [((it[1].x, it[1].y), (it[2].x, it[2].y)) for it in d['items'] if it[0] == 'l']
            polys.append(segs)
    tri = [p for p in polys if len(p) == 3][0]
    sqr = [p for p in polys if len(p) == 4][0]
    ts = [math.dist(a, b) for a, b in tri]
    ss = [math.dist(a, b) for a, b in sqr]
    say('     triangle sides (pt):', [round(x, 2) for x in ts], ' = %.1f mm' % (ts[0] * 25.4 / 72))
    say('     square sides (pt):  ', [round(x, 2) for x in ss], ' = %.1f mm' % (ss[0] * 25.4 / 72))
    check(max(ts) - min(ts) < 0.05, 'triangle is equilateral (equal x/y scaling)')
    check(max(ss) - min(ss) < 0.05, 'square has four equal sides')
    angs = []
    for (a, b), (c, d) in zip(sqr, sqr[1:] + sqr[:1]):
        u = (b[0] - a[0], b[1] - a[1]); v = (d[0] - c[0], d[1] - c[1])
        angs.append(abs(u[0] * v[0] + u[1] * v[1]))
    check(max(angs) < 0.05, 'square corners are right angles')
    ratio = ts[0] / ss[0]
    say('     triangle side / square side = %.3f (kit: both use the same 60 mm side bar)' % ratio)
    check(abs(ratio - 1) < 0.02, 'triangle and square drawn with the same bar length as the kit')

    say('\n' + ('ALL CHECKS PASSED' if not FAIL else 'FAILURES: %d' % len(FAIL)))
    for f in FAIL:
        say('  - ' + f)
    with open(os.path.join(HERE, 'out_check_diagrams.txt'), 'w') as fh:
        fh.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
