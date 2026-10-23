#!/usr/bin/env python3
"""Diagram checks for Week 91 (Rotor-router machines), read from the delivered PDFs.

Written for the math-check stage of the review; independent of the package's
own checker. Uses PyMuPDF to read vector drawings and text from:
  lowell-math-circle-year-2/week-91/week-91-students.pdf
  lowell-math-circle-year-2/week-91/week-91-return-visit.pdf
  lowell-math-circle-year-2/week-91/week-91-materials.pdf

It recognises circles (four Bezier arcs), filled counter dots, arrows (a thick
line plus a filled tip; direction from the tail to the tip end), plain lines
and boxes. Then it checks:
- every page: header and footer text, problem numbers consecutive per packet;
- every tree diagram: a complete binary tree of the right depth, connected
  centre to centre, leaves labelled A, B, ... from left to right, all circles
  round (equal width and height);
- students p1 demonstration: arrow directions and counter positions in the
  three pictures (input, move to X, flip);
- return p1 example: card arrows at 1 and 2 in each row, counter positions,
  the entry arrow;
- return pp2-3: road lengths, entry positions, strip lengths;
- materials: board structures, card faces (tree: down-left / down-right;
  road: left / right), card counts.

Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
from pathlib import Path
import sys
import pymupdf as fitz

HERE = Path(__file__).resolve().parent


def find_repo():
    cands = []
    if len(HERE.parents) > 3:
        cands.append(HERE.parents[3])  # plans/review/checks/week-91 -> repo
    cands += [HERE] + list(HERE.parents)
    for p in cands:
        if (p / 'lowell-math-circle-year-2').is_dir() and (p / 'AGENTS.md').is_file():
            return p
    sys.exit('repository not found')


REPO = find_repo()
W = REPO / 'lowell-math-circle-year-2' / 'week-91'
# Re-pointed on 2026-10-23: the card's should fixes (c619ef2) and the footer ids (dfbc5e4) changed the packets, so
# this review check reads the copies as reviewed, in week-91/archive-before-card-fixes-2026-10-23/.
W = W / 'archive-before-card-fixes-2026-10-23'
OUT, FAIL = [], []


def say(s=''):
    OUT.append(s)
    print(s)


def check(cond, msg):
    say(('PASS  ' if cond else 'FAIL  ') + msg)
    if not cond:
        FAIL.append(msg)


def parse(page):
    circles, dots, arrows, lines, boxes = [], [], [], [], []
    dr = page.get_drawings()
    tips = []
    thick = []
    for x in dr:
        kinds = tuple(i[0] for i in x['items'])
        r = x['rect']
        if kinds == ('c', 'c', 'c', 'c'):
            c = ((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2, r.width / 2, r.height / 2)
            if x['type'] == 'f':
                dots.append(c)
            else:
                circles.append(c)
        elif kinds == ('c', 'l', 'c'):
            tips.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))
        elif kinds == ('l',):
            p1, p2 = x['items'][0][1], x['items'][0][2]
            seg = ((p1.x, p1.y), (p2.x, p2.y))
            if x.get('width') and x['width'] > 1.0 and not x.get('dashes', '').strip('[] 0'):
                thick.append(seg)
            else:
                lines.append(seg)
        elif kinds == ('l', 'l', 'l', 'l') or kinds == ('re',):
            boxes.append((r.x0, r.y0, r.x1, r.y1))
    for seg in thick:
        (ax, ay), (bx, by) = seg
        # tip nearest either end
        best = None
        for t in tips:
            da = (t[0] - ax) ** 2 + (t[1] - ay) ** 2
            db = (t[0] - bx) ** 2 + (t[1] - by) ** 2
            for d, end in ((da, 'a'), (db, 'b')):
                if best is None or d < best[0]:
                    best = (d, end)
        if best and best[0] < 25:
            if best[1] == 'b':
                arrows.append(((ax, ay), (bx, by)))
            else:
                arrows.append(((bx, by), (ax, ay)))
        else:
            lines.append(seg)
    words = page.get_text('words')
    return dict(circles=circles, dots=dots, arrows=arrows, lines=lines, boxes=boxes, words=words)


def dirname(a):
    (x0, y0), (x1, y1) = a
    dx, dy = x1 - x0, y1 - y0
    h = 'R' if dx > 1 else ('L' if dx < -1 else '')
    v = 'down' if dy > 1 else ('up' if dy < -1 else '')
    return (v + '-' if v and h else v) + {'R': 'right', 'L': 'left', '': ''}[h]


def label_in(c, words):
    x, y, rx, ry = c
    inside = [w[4] for w in words if x - rx < (w[0] + w[2]) / 2 < x + rx and y - ry < (w[1] + w[3]) / 2 < y + ry]
    return ''.join(inside)


def near(p, q, tol=1.5):
    return abs(p[0] - q[0]) < tol and abs(p[1] - q[1]) < tol


def trees_on(page_data, expected):
    """expected: list of depths for the trees on the page. Returns list of
    (depth, leaf labels, ok) for each tree found."""
    C = page_data['circles']
    L = page_data['lines']
    # adjacency via lines whose endpoints are circle centres
    idx = {i: c for i, c in enumerate(C)}
    adj = {i: set() for i in idx}
    for (a, b) in L:
        ia = [i for i, c in idx.items() if near(a, c[:2])]
        ib = [i for i, c in idx.items() if near(b, c[:2])]
        if ia and ib:
            adj[ia[0]].add(ib[0]); adj[ib[0]].add(ia[0])
    seen = set(); comps = []
    for i in idx:
        if i in seen or not adj[i]:
            continue
        stack = [i]; comp = []
        while stack:
            j = stack.pop()
            if j in seen:
                continue
            seen.add(j); comp.append(j); stack += list(adj[j])
        comps.append(comp)
    results = []
    for comp in sorted(comps, key=lambda c: (round(min(idx[j][1] for j in c) / 50), min(idx[j][0] for j in c))):
        root = min(comp, key=lambda j: idx[j][1])
        # BFS by levels
        levels = [[root]]; parent = {root: None}; ok = True
        while True:
            nxt = []
            for j in levels[-1]:
                ch = sorted([k for k in adj[j] if k != parent[j]], key=lambda k: idx[k][0])
                if ch and len(ch) != 2:
                    ok = False
                for k in ch:
                    parent[k] = j
                    if idx[k][1] <= idx[j][1]:
                        ok = False
                nxt += ch
            if not nxt:
                break
            levels.append(nxt)
        depth = len(levels) - 1
        if any(len(lv) != 2 ** d for d, lv in enumerate(levels)):
            ok = False
        leaves = levels[-1]
        if [idx[k][0] for k in leaves] != sorted(idx[k][0] for k in leaves):
            ok = False
        labels = ''.join(label_in(idx[k], page_data['words']) for k in leaves)
        internal_blank = all(label_in(idx[k], page_data['words']) == '' for lv in levels[:-1] for k in lv)
        round_ = all(abs(idx[k][2] - idx[k][3]) < 0.05 for k in comp)
        results.append((depth, labels, ok and internal_blank, round_))
    return results


def header_footer(doc, name, bands):
    for i, page in enumerate(doc):
        t = page.get_text()
        lines = [l for l in t.splitlines() if l.strip()]
        check(lines[0].startswith('Week 91 / Rotor-router machines / ') and lines[0].endswith(bands[i]),
              f'{name} p{i + 1}: header "{lines[0]}"')
        check(f'Bellingham Math Circle / Week 91 / {name}-v1' in t, f'{name} p{i + 1}: footer id {name}-v1')


def problems(doc, name, expected):
    import re
    found = []
    for page in doc:
        found += [int(n) for n in re.findall(r'Problem (\d+):', page.get_text())]
    check(found == expected, f'{name}: problem numbers {found}')


def students():
    say('== Student packet ==')
    doc = fitz.open(W / 'week-91-students.pdf')
    check(len(doc) == 6, 'students: 6 pages')
    header_footer(doc, 'students', ['Grades 2–3'] * 3 + ['Grades 4–5'] * 2 + ['Grades 2–5'])
    problems(doc, 'students', [1, 2, 3, 4, 5, 6, 7])
    # p1 demonstration
    d = parse(doc[0])
    sw = sorted([c for c in d['circles'] if c[2] > 15], key=lambda c: c[0])
    check(len(sw) == 3 and all(abs(c[2] - c[3]) < 0.05 for c in sw), 'p1 demo: three round switch circles')
    dirs = []
    for c in sw:
        a = [a for a in d['arrows'] if abs((a[0][0] + a[1][0]) / 2 - c[0]) < 3 and abs((a[0][1] + a[1][1]) / 2 - c[1]) < 3]
        dirs.append(dirname(a[0]) if a else None)
    say(f'  demo arrows: {dirs}')
    check(dirs == ['down-left', 'down-left', 'down-right'],
          'p1 demo: input arrow points to X; after the move it still points to X; after the flip to Y')
    xs = [w for w in d['words'] if w[4] == 'X' and w[1] > 250 and w[1] < 300]
    dots = sorted(d['dots'], key=lambda c: c[0])
    # line ends of the X branches
    xends = []
    for c in sw:
        ends = [b if b[1] > a[1] else a for (a, b) in d['lines'] if near(a, c[:2], 3) or near(b, c[:2], 3)]
        ends = sorted(ends)
        xends.append(ends[0] if ends else None)
    pos = []
    for dt, c, xe in zip(dots, sw, xends):
        if xe and near(dt[:2], xe, 3):
            pos.append('at X')
        elif ((dt[0] - c[0]) ** 2 + (dt[1] - c[1]) ** 2) ** .5 < c[2] + 8:
            pos.append('beside switch')
        else:
            pos.append('elsewhere')
    say(f'  demo counters: {pos}')
    check(pos == ['beside switch', 'at X', 'at X'], 'p1 demo: counter beside the card, then at X in the move and flip pictures')
    nb = [b for b in d['boxes']]
    check(len(nb) == 24, f'p1: two 12-box arrival strips ({len(nb)} boxes)')
    # trees
    for pg, exp in [(1, [2, 2]), (2, [2, 2, 2, 2]), (3, [3, 3, 3]), (4, [2, 3])]:
        d = parse(doc[pg])
        tr = trees_on(d, exp)
        say(f'  p{pg + 1} trees: {[(t[0], t[1]) for t in tr]}')
        check(sorted(t[0] for t in tr) == sorted(exp), f'p{pg + 1}: tree depths {sorted(exp)}')
        check(all(t[2] for t in tr), f'p{pg + 1}: every tree complete binary, centre-to-centre, blank switches, leaves left to right')
        check(all(t[1] == 'ABCDEFGH'[:2 ** t[0]] for t in tr), f'p{pg + 1}: leaves labelled A.. left to right')
        check(all(t[3] for t in tr), f'p{pg + 1}: all tree circles round')
    # P3 and P4 target labels
    t3 = doc[2].get_text()
    for o in ['A C B D', 'B D A C', 'A B C D', 'D A B C']:
        check(o in t3, f'p3 target "{o}" printed')
    t4 = doc[3].get_text()
    for o in ['A E C G B F D H', 'H D F B G C E A', 'A E B F C G D H']:
        check(o in t4, f'p4 target "{o}" printed')
    # strips
    for pg, n in [(1, 16), (4, 8), (5, 30)]:
        nb = len(parse(doc[pg])['boxes'])
        check(nb == n, f'p{pg + 1}: {n} record boxes ({nb})')


def road_rows(d):
    """Group circles by row (y), return rows of circles sorted by x."""
    rows = {}
    for c in d['circles']:
        rows.setdefault(round(c[1]), []).append(c)
    return [sorted(v, key=lambda c: c[0]) for k, v in sorted(rows.items())]


def return_visit():
    say('')
    say('== Return packet ==')
    doc = fitz.open(W / 'week-91-return-visit.pdf')
    check(len(doc) == 4, 'return: 4 pages')
    header_footer(doc, 'return-visit', ['Grades 4–5'] * 4)
    problems(doc, 'return-visit', [1, 2, 3, 4, 5, 6])
    d = parse(doc[0])
    rows = road_rows(d)
    check(len(rows) == 3 and all(len(r) == 4 for r in rows), 'p1 example: three rows of a road 0..3 (4 circles each)')
    expect_cards = [('right', 'left'), ('right', 'right'), ('left', 'left')]
    expect_pos = [2, 1, 3]
    for r, ec, ep in zip(rows, expect_cards, expect_pos):
        cards = []
        for c in r[1:3]:
            a = [a for a in d['arrows'] if abs((a[0][0] + a[1][0]) / 2 - c[0]) < 5 and abs((a[0][1] + a[1][1]) / 2 - c[1]) < 2]
            cards.append(dirname(a[0]) if a else None)
        dot = [dt for dt in d['dots'] if abs(dt[1] - r[0][1]) < 30]
        posn = min(range(4), key=lambda i: abs(dot[0][0] - r[i][0])) if dot else None
        lab = [label_in(c, d['words']) for c in r]
        say(f'  row y={r[0][1]:.0f}: cards {cards}, counter nearest circle {posn}, endpoint labels {lab}')
        check(tuple(cards) == ec and posn == ep and lab[0] == '0' and lab[3] == '3',
              f'p1 example row: cards {ec}, counter at {ep}')
    entry = [a for a in d['arrows'] if dirname(a) == 'down']
    check(len(entry) == 1 and abs(entry[0][1][0] - rows[0][2][0]) < 1, 'p1 example: entry arrow points down onto circle 2 of the first row')
    check(len(d['boxes']) == 12, 'p1: 12-box arrival strip')
    for pg, m, entries, nbox in [(1, 4, [1, 2, 3], 8), (2, 5, [1, 2, 4], 5)]:
        d = parse(doc[pg])
        rows = road_rows(d)
        check(len(rows) == 3 and all(len(r) == m + 1 for r in rows), f'p{pg + 1}: three roads 0..{m}')
        got = []
        for r in rows:
            e = [a for a in d['arrows'] if dirname(a) == 'down' and a[1][1] < r[0][1] and r[0][1] - a[1][1] < 25]
            got.append(min(range(m + 1), key=lambda i: abs(e[0][1][0] - r[i][0])) if e else None)
            lab = [label_in(c, d['words']) for c in r]
            check(lab[0] == '0' and lab[-1] == str(m) and all(l == '' for l in lab[1:-1]), f'p{pg + 1}: endpoints labelled 0 and {m}, inside circles blank')
        check(got == entries, f'p{pg + 1}: entry arrows at {entries} (found {got})')
        check(len(d['boxes']) == 3 * nbox, f'p{pg + 1}: three {nbox}-box strips')
        # interior numbers printed under circles
        ph = doc[pg].rect.height
        nums = sorted(int(w[4]) for w in d['words'] if w[4].isdigit() and 1 <= int(w[4]) < m and rows[0][0][1] < w[1] < ph - 60)
        check(nums == sorted(list(range(1, m)) * 3), f'p{pg + 1}: interior numbers 1..{m - 1} under each road')
    d = parse(doc[3])
    check(len(d['boxes']) == 12 + 12, 'p4: three 4-slot state records and a 12-box strip')


def materials():
    say('')
    say('== Materials ==')
    doc = fitz.open(W / 'week-91-materials.pdf')
    check(len(doc) == 7, 'materials: 7 pages')
    header_footer(doc, 'materials', ['Materials'] * 7)
    d = parse(doc[0])
    lab = sorted(label_in(c, d['words']) for c in d['circles'])
    check(len(d['circles']) == 3 and lab == ['', 'X', 'Y'], 'p1: one switch circle and exits X, Y')
    for pg, depth in [(1, 2), (2, 3)]:
        d = parse(doc[pg])
        tr = trees_on(d, [depth])
        check(len(tr) == 1 and tr[0][0] == depth and tr[0][1] == 'ABCDEFGH'[:2 ** depth] and tr[0][2] and tr[0][3],
              f'p{pg + 1}: {2 ** depth}-exit board is a complete depth-{depth} tree, leaves {"ABCDEFGH"[:2 ** depth]}, round circles')
        sw = [c for c in d['circles'] if label_in(c, d['words']) == '']
        diam_mm = [2 * c[2] / 72 * 25.4 for c in sw]
        check(len(sw) == 2 ** depth - 1 and all(abs(x - 24) < 0.05 for x in diam_mm), f'p{pg + 1}: {2 ** depth - 1} switch circles of 24 mm')
    for pg, m in [(3, 4), (4, 5)]:
        d = parse(doc[pg])
        r = sorted(d['circles'], key=lambda c: c[0])
        lab = [label_in(c, d['words']) for c in r]
        check(len(r) == m + 1 and lab[0] == '0' and lab[-1] == str(m) and all(abs(c[1] - r[0][1]) < 0.1 for c in r),
              f'p{pg + 1}: road board 0..{m} on one line')
    d = parse(doc[5])
    halves = sorted(d['boxes'], key=lambda b: (b[1], b[0]))
    tree_h = [b for b in halves if abs((b[3] - b[1]) / 72 * 25.4 - 22) < 0.1]
    road_h = [b for b in halves if abs((b[3] - b[1]) / 72 * 25.4 - 20) < 0.1]
    check(len(tree_h) == 14 and len(road_h) == 8, f'p6: 7 tree cards (14 faces) and 4 road cards (8 faces)')
    ok_t = ok_r = True
    for faces, kind in [(tree_h, 't'), (road_h, 'r')]:
        faces = sorted(faces, key=lambda b: (round(b[1]), b[0]))
        for i in range(0, len(faces), 2):
            pair = faces[i:i + 2]
            ds = []
            for b in pair:
                a = [a for a in d['arrows'] if b[0] < (a[0][0] + a[1][0]) / 2 < b[2] and b[1] < (a[0][1] + a[1][1]) / 2 < b[3]]
                ds.append(dirname(a[0]) if a else None)
            if kind == 't' and ds != ['down-left', 'down-right']:
                ok_t = False
            if kind == 'r' and ds != ['left', 'right']:
                ok_r = False
    check(ok_t, 'p6: every tree card has a down-left face and a down-right face')
    check(ok_r, 'p6: every road card has a left face and a right face')
    d = parse(doc[6])
    bars = [l for l in d['lines'] if abs(l[0][1] - l[1][1]) < 0.01 and 140 < abs(l[0][0] - l[1][0]) < 143]
    check(any(abs(abs(l[0][0] - l[1][0]) / 72 * 25.4 - 50) < 0.05 for l in bars), 'p7: 50 mm scale bar')
    sq = [b for b in d['boxes'] if abs((b[2] - b[0]) / 72 * 25.4 - 15) < 0.05]
    check(len(sq) == 48, f'p7: four 12-square strips of 15 mm squares ({len(sq)})')


def main():
    students()
    return_visit()
    materials()
    say('')
    say(f'{len(FAIL)} failure(s)')
    for f in FAIL:
        say('  ' + f)
    (HERE / 'check_diagrams.py.out').write_text('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
