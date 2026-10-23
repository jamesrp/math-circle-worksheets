"""Check the October 23, 2026 card fixes to Week 53 (W53-networks-v2, W53-guide-v2).

Reads the delivered student PDF with this folder's pdfgeom.py and the label
analysis of check_diagrams.py (no writer code imported), with the transcription
updated for v2: five record maps on Problems 2 and 4, dots on Problems 3 and 4.
  * must 1: on pp. 6 and 8 every price numeral is nearest its own link (other
    links at least 1.5 times farther), no white label box paints over another
    link or sits under a place circle; on every full-size map no label box
    touches its own link either, so each link is printed unbroken;
  * the costs and swaps of Problem 8 and the keys of Problems 2-6, recomputed
    from the prices that the printed numerals give (nearest-link assignment);
  * must 2: dots beside every numeral on pp. 1-4 (at most six), pp. 1-4 headed
    Grades K-5; should 3: five record maps on Problems 2 and 4; should 4: the
    Problem 6 answer headings; the guide routes K-1 through pp. 1-4.

Run: python3 check_card_fixes.py [students.pdf] [facilitator.pdf]
(defaults: the print PDFs); writes out_check_card_fixes.txt beside itself.
"""
import itertools
import os as _os
import sys

HERE = _os.path.dirname(_os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import pdfgeom  # noqa: E402
import check_diagrams as cd  # noqa: E402

OUT, FAIL = [], []


def say(*a):
    s = ' '.join(str(x) for x in a)
    OUT.append(s)
    print(s)


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


# v2 transcription: the v1 one with five record maps on pp. 2 and 4.
T2 = {k: list(v) for k, v in cd.T.items()}
T2[2] = [cd.T[2][0]] + [('P2 record %d' % k, dict(cd.T[2][1][1]), set()) for k in range(1, 6)]
T2[4] = [cd.T[4][0]] + [('P4 record %d' % k, dict(cd.T[4][1][1]), set()) for k in range(1, 6)]
COMPACT = {1: 3, 5: 3}  # the small X/Y/Z and U/V/W examples (pp. 1 and 5), unchanged from v1


def own_link_clear(page, pageno):
    """Full-size maps: no white price box touches its own link (box grown by half the stroke)."""
    verts = [c for c in page['curves'] if c['op'] == 'B' and c['rx'] > 5]

    def vat(p):
        return next((i for i, c in enumerate(verts) if abs(p[0] - c['cx']) < 0.6 and abs(p[1] - c['cy']) < 0.6), None)
    links = [l for l in page['lines'] if vat(l['p']) is not None and vat(l['q']) is not None]
    digits = [t for t in page['texts'] if len(t['s']) == 1 and t['s'].isdigit()]
    bad = []
    for r in page['rects']:
        if r['fill'] != 1.0:
            continue
        ts = [t for t in digits if r['x0'] - 0.5 <= t['x'] <= r['x1'] and r['y0'] - 0.5 <= t['y'] <= r['y1']]
        if not ts:
            continue
        cx, cy = (r['x0'] + r['x1']) / 2, (r['y0'] + r['y1']) / 2
        small = min(verts, key=lambda c: (c['cx'] - cx) ** 2 + (c['cy'] - cy) ** 2)['rx'] < 10
        if small and pageno in COMPACT:
            continue
        for l in links:
            if cd.seg_hits_rect(*l['p'], *l['q'], r, pad=l['width'] / 2):
                bad.append('p%d label %s touches a link' % (pageno, ts[0]['s']))
    return bad


def trees(price):
    vs = sorted(set(''.join(price)))
    es = sorted(price)
    for S in itertools.combinations(es, len(vs) - 1):
        if connected(vs, S):
            yield frozenset(S)


def connected(vs, S):
    reach, grow = {vs[0]}, True
    while grow:
        grow = False
        for e in S:
            if (e[0] in reach) != (e[1] in reach):
                reach |= set(e)
                grow = True
    return reach == set(vs)


def cost(price, S):
    return sum(price[e] for e in S)


def swaps(price, bought):
    vs = sorted(set(''.join(price)))
    legal, illegal = [], []
    for out in bought:
        for inn in set(price) - set(bought):
            S = (set(bought) - {out}) | {inn}
            if cost(price, S) < cost(price, bought):
                (legal if connected(vs, S) else illegal).append((out, inn, cost(price, S)))
    return sorted(legal), sorted(illegal)


def main():
    student = sys.argv[1] if len(sys.argv) > 1 else pdfgeom.STUDENT_PDF
    guide = sys.argv[2] if len(sys.argv) > 2 else pdfgeom.GUIDE_PDF
    say('Week 53 card fixes, October 23, 2026')
    say('=' * 60)
    say('student PDF: ' + _os.path.relpath(student, pdfgeom.ROOT))
    pages = pdfgeom.read(student)
    check(len(pages) == 9, '9 pages')
    cd.T = T2
    findings = []
    for n, page in enumerate(pages, 1):
        lines = []
        findings += ['p%d %s' % (n, f) for f in cd.analyse(n, page, lines)]
        if n in (6, 8):
            for l in lines:
                say('   ', l)
    check(not findings, 'every printed map matches the v2 transcription; every numeral is nearest its own link '
          '(others >= 1.5x farther), no box over another link or under a circle' + ('' if not findings else ': ' + '; '.join(findings)))
    bad = [b for n, page in enumerate(pages, 1) for b in own_link_clear(page, n)]
    check(not bad, 'on every full-size map each label box clears its own link' + ('' if not bad else ': ' + '; '.join(bad)))

    say('\n[must 2, shoulds 3-4] headers, dots, record maps, headings')
    import pymupdf
    doc = pymupdf.open(student)
    heads = [next(l for l in p.get_text().splitlines() if l.startswith('Week 53 / ')).rsplit('/ ', 1)[1] for p in doc]
    check(heads == ['Grades K–5'] * 4 + ['Grades 4–5'] * 5, 'pp. 1-4 headed Grades K-5, pp. 5-9 Grades 4-5: %s' % heads)
    check(all('W53-networks-v2' in p.get_text() for p in doc), 'footer W53-networks-v2 on every page')
    dots_ok = True
    for n in (1, 2, 3, 4):
        page = pages[n - 1]
        dots = [c for c in page['curves'] if c['op'] in ('f', 'F') and c['rx'] < 3]
        digits = [t for t in page['texts'] if len(t['s']) == 1 and t['s'].isdigit()]
        for r in page['rects']:
            if r['fill'] != 1.0:
                continue
            ts = [t for t in digits if r['x0'] - 0.5 <= t['x'] <= r['x1'] and r['y0'] - 0.5 <= t['y'] <= r['y1']]
            if not ts:
                continue
            nd = sum(1 for d in dots if r['x0'] <= d['cx'] <= r['x1'] and r['y0'] <= d['cy'] <= r['y1'])
            if nd != int(ts[0]['s']) or nd > 6:
                dots_ok = False
                say('     p%d label %s has %d dots' % (n, ts[0]['s'], nd))
    check(dots_ok, 'every price on pp. 1-4 has as many dots as its numeral, at most six')
    check(len(T2[2]) == 6 and len(T2[4]) == 6, 'Problems 2 and 4 print five record maps each (checked against the PDF above)')
    t6 = ' '.join(doc[5].get_text().split())
    check('In every cheapest purchase:' in t6 and 'In no cheapest purchase:' in t6 and 'Cannot be bought' not in t6,
          'Problem 6 answer areas headed "In every cheapest purchase:" and "In no cheapest purchase:"')

    say('\n[keys] recomputed from the printed prices')
    price = {n: {k: v for k, v in T2[p][0][1].items()} for n, p in (('P2', 2), ('P3', 3), ('P4', 4), ('P6', 6))}
    for name, (mn, cnt) in {'P2': (4, 3), 'P3': (7, 1), 'P4': (6, 3), 'P6': (8, 1)}.items():
        ts = list(trees(price[name]))
        m = min(cost(price[name], S) for S in ts)
        opt = [S for S in ts if cost(price[name], S) == m]
        check((m, len(opt)) == (mn, cnt), '%s: minimum %d with %d cheapest purchase(s)' % (name, m, len(opt)))
    p6 = price['P6']
    ts = list(trees(p6))
    opt = [S for S in ts if cost(p6, S) == 8]
    every = set.intersection(*map(set, opt))
    none = set(p6) - set.union(*map(set, opt))
    check(every == {'AB', 'BC', 'CD', 'DE', 'EF'} and none == {'AC', 'BD', 'CE', 'DF'},
          'P6: in every %s; in none %s' % (sorted(every), sorted(none)))
    p8 = {k: v for k, v in T2[8][0][1].items()}
    check(p8 == p6, 'P8 prints the P6 prices')
    top, bottom = T2[8][0][2], T2[8][1][2]
    check(cost(p8, top) == 8 and cost(p8, bottom) == 14, 'P8 costs: top %d, bottom %d' % (cost(p8, top), cost(p8, bottom)))
    lt, it = swaps(p8, top)
    lb, ib = swaps(p8, bottom)
    say('     bottom legal cheaper swaps (return, buy, new cost):', lb)
    say('     bottom cheaper swaps that disconnect:', ib)
    check(not lt, 'P8 top: no cheaper legal swap')
    check(sorted(c for _, _, c in lb) == [11, 12, 13, 13] and len(ib) == 5,
          'P8 bottom: four cheaper legal swaps (13, 13, 11, 12) and five that disconnect')

    say('\n[guide] ' + _os.path.relpath(guide, pdfgeom.ROOT))
    g = ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(guide))
    for phrase in ('W53-guide-v2', 'Student pp. 1–4 are headed Grades K–5', 'Young pairs work pp. 1–4',
                   'pp. 1–4 twice for young pairs', '(17 sheets)'):
        check(phrase in g, 'guide says "%s"' % phrase)
    check('possibly p. 2' not in g and 'accepted prior concrete activity' not in g, 'the one-page K-1 route is gone')

    say('\n' + ('ALL CHECKS PASSED' if not FAIL else 'FAILURES: %d' % len(FAIL)))
    for f in FAIL:
        say('  - ' + f)
    with open(_os.path.join(HERE, 'out_check_card_fixes.txt'), 'w') as fh:
        fh.write('\n'.join(OUT) + '\n')
    return not FAIL


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
