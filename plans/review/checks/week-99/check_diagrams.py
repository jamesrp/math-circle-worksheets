#!/usr/bin/env python3
"""Week 99 (Moving piles): read every pile picture off the delivered PDFs.

Independent of the package's check_math.py.  For every student page it
extracts, from the PDF vector drawings (PyMuPDF), each bin or star node, the
counters inside it (filled = start counter, open = target place), the printed
bin number or node letter, the road/connector lines, and the row label.  It
then cross-checks the same data against the TeX sources (coordinates of every
\\draw ... circle / rectangle) and against the data typed into check_math.py.

Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
import importlib.util
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

HERE = Path(__file__).resolve().parent


def find_repo(start):
    for p in [start, *start.parents]:
        if (p / 'AGENTS.md').exists() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(start))


REPO = find_repo(HERE)
# Reads the version reviewed on October 23 (230e7a3). Week 99 was since converted to problem files
# (0842f62, which removed the per-page student TeX) and revised (8a555d1 card shoulds, f9d1bc1
# critic coulds), so the reviewed PDFs come from archive-before-card-fixes and the per-page TeX from
# archive-before-problem-files (both identical to 230e7a3). DELIVERED is the current print folder;
# source/week-99/checks/card_fixes_2026_10_23.py checks the current packets.
DELIVERED = REPO / 'lowell-math-circle-year-2' / 'week-99'
WEEK = DELIVERED / 'archive-before-card-fixes-2026-10-23'
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-99' / 'archive-before-problem-files-2026-10-23' / 'student'

spec = importlib.util.spec_from_file_location('w99math', HERE / 'check_math.py')
W = importlib.util.module_from_spec(spec)
spec.loader.exec_module(W)

OUT, FAILS = [], []


def say(s=''):
    OUT.append(s)


def check(cond, msg):
    if not cond:
        FAILS.append(msg)
        say('  FAIL: ' + msg)
    return cond


def centre(r):
    return ((r[0] + r[2]) / 2, (r[1] + r[3]) / 2)


def inside(pt, r, pad=0.5):
    return r[0] - pad <= pt[0] <= r[2] + pad and r[1] - pad <= pt[1] <= r[3] + pad


def page_objects(page):
    """Classify vector paths: containers (bins / star nodes), counters, lines."""
    conts, counters, lines = [], [], []
    for d in page.get_drawings():
        r = d['rect']
        w, h = r.width, r.height
        kinds = [it[0] for it in d['items']]
        if all(k == 'c' for k in kinds) and len(kinds) == 4 and w < 14 and abs(w - h) < 0.5:
            filled = d.get('fill') is not None and d['fill'][0] < 0.5
            counters.append({'c': centre(r), 'filled': filled, 'r': w / 2})
        elif d['type'] in ('s', 'fs') and len(kinds) >= 4 and w > 20 and h > 20 and w < 90 and h < 90:
            shape = 'circle' if (all(k == 'c' for k in kinds) and len(kinds) == 4) else 'box'
            conts.append({'rect': tuple(r), 'shape': shape, 'w': w, 'h': h})
        elif len(kinds) == 1 and kinds[0] == 'l':
            p1, p2 = d['items'][0][1], d['items'][0][2]
            lines.append(((p1.x, p1.y), (p2.x, p2.y)))
    return conts, counters, lines


def words(page):
    return [(w[4], ((w[0] + w[2]) / 2, (w[1] + w[3]) / 2), w) for w in page.get_text('words')]


def extract_page(page):
    conts, counters, lines = page_objects(page)
    ws = words(page)
    # assign counters
    for c in conts:
        c['fill'] = 0
        c['open'] = 0
    for k in counters:
        hits = [c for c in conts if inside(k['c'], c['rect'])]
        if not check(len(hits) == 1, f'counter at {k["c"]} lies in {len(hits)} containers'):
            continue
        if k['filled']:
            hits[0]['fill'] += 1
        else:
            hits[0]['open'] += 1
    # label each container: digit below a box, letter beside a circle
    for c in conts:
        cx, cy = centre(c['rect'])
        if c['shape'] == 'box':
            below = [t for t, p, _ in ws if t.isdigit() and abs(p[0] - cx) < 6 and 0 < p[1] - c['rect'][3] < 14]
            c['label'] = below[0] if len(below) == 1 else None
        else:
            near = sorted(((abs(p[0] - cx) + abs(p[1] - cy)), t) for t, p, _ in ws if t in 'ABCO' and len(t) == 1)
            c['label'] = near[0][1] if near and near[0][0] < 45 else None
    return conts, counters, lines, ws


def group_rows(conts):
    """Boxes grouped into rows by centre y (line boards)."""
    boxes = [c for c in conts if c['shape'] == 'box']
    rows = {}
    for b in boxes:
        y = round(centre(b['rect'])[1], 0)
        key = next((k for k in rows if abs(k - y) < 2), y)
        rows.setdefault(key, []).append(b)
    out = []
    for y, bs in sorted(rows.items()):
        bs.sort(key=lambda b: b['rect'][0])
        # split one y-band into separate boards when there is a big x jump (cards)
        board = [bs[0]]
        for b in bs[1:]:
            if b['rect'][0] - board[-1]['rect'][2] > 30:
                out.append((y, board))
                board = [b]
            else:
                board.append(b)
        out.append((y, board))
    return out


def row_label(ws, y, x0):
    cands = [(t, p) for t, p, _ in ws if p[0] < x0 - 5 and abs(p[1] - y) < 16]
    txt = ' '.join(t for t, p in sorted(cands, key=lambda q: (round(q[1][1]), q[1][0])))
    return txt


def connectors_ok(board, lines):
    """Every adjacent pair of bins joined by a line touching both."""
    ok = True
    for a, b in zip(board, board[1:]):
        ya = centre(a['rect'])[1]
        hit = any(abs(p[1] - ya) < 1 and abs(q[1] - ya) < 1 and
                  abs(min(p[0], q[0]) - a['rect'][2]) < 1.5 and abs(max(p[0], q[0]) - b['rect'][0]) < 1.5
                  for p, q in lines)
        ok &= hit
    return ok


def board_repr(board):
    # position row: one bin number per counter, as the guide writes it
    fill = ''.join(str(i) * b['fill'] for i, b in enumerate(board))
    opn = ''.join(str(i) * b['open'] for i, b in enumerate(board))
    return fill, opn


def tex_counters(texfile):
    """(x, y, filled) of every counter-sized circle in a TeX page, inches."""
    s = texfile.read_text()
    res = []
    for m in re.finditer(r'\\(draw|fill)\[([^\]]*)\]\s*\(([-\d.]+),([-\d.]+)\)\s*circle\s*\(([\d.]+)\)', s):
        r = float(m.group(5))
        if r < 0.1:
            opts = m.group(2)
            filled = ('black' in opts) or m.group(1) == 'fill'
            res.append((float(m.group(3)), float(m.group(4)), filled))
    return res


def main():
    pdfs = {'2-3': WEEK / 'week-99-grades-2-3.pdf', '4-5': WEEK / 'week-99-grades-4-5.pdf'}
    extracted = {}
    for band, pdf in pdfs.items():
        doc = fitz.open(pdf)
        say(f'== Grades {band}: {pdf.name}, {doc.page_count} pages')
        for pno in range(doc.page_count):
            page = doc[pno]
            conts, counters, lines, ws = extract_page(page)
            say(f'-- page {pno + 1}: {len(conts)} containers, {len(counters)} counters')
            # TeX cross-check: counter count and filled/open split match
            tex = SRC / f'grades-{band}-{pno + 1}.tex'
            tc = tex_counters(tex)
            check(len(tc) == len(counters), f'{band} p{pno+1}: TeX has {len(tc)} counters, PDF {len(counters)}')
            check(sum(f for *_, f in tc) == sum(k['filled'] for k in counters),
                  f'{band} p{pno+1}: filled counter split differs TeX/PDF')
            # TeX -> PDF coordinate check (1in = 72pt, y flipped)
            for (x, y, f) in tc:
                X, Y = x * 72, (11 - y) * 72
                check(any(abs(k['c'][0] - X) < 0.6 and abs(k['c'][1] - Y) < 0.6 and k['filled'] == f for k in counters),
                      f'{band} p{pno+1}: TeX counter ({x},{y}) not in PDF')
            circles = [c for c in conts if c['shape'] == 'circle']
            if circles:
                # star boards: group by proximity into 4-node stars
                stars = []
                cs = circles[:]
                while cs:
                    seed = cs.pop(0)
                    sc = centre(seed['rect'])
                    grp = [seed] + [c for c in cs if abs(centre(c['rect'])[0] - sc[0]) < 140 and abs(centre(c['rect'])[1] - sc[1]) < 110]
                    for g in grp[1:]:
                        cs.remove(g)
                    stars.append(grp)
                for st in stars:
                    labs = {c['label']: c for c in st}
                    check(sorted(labs) == ['A', 'B', 'C', 'O'], f'{band} p{pno+1}: star labels {sorted(labs)}')
                    radii = {round(c['w'], 1) for c in st} | {round(c['h'], 1) for c in st}
                    check(max(radii) - min(radii) < 0.3, f'{band} p{pno+1}: star nodes unequal/non-round {radii}')
                    # roads: each line joins O's centre to a leaf centre; no leaf-leaf road
                    oc = centre(labs['O']['rect'])
                    roads = set()
                    for p, q in lines:
                        for L in 'ABC':
                            lc = centre(labs[L]['rect'])
                            if (abs(p[0]-oc[0]) < 1 and abs(p[1]-oc[1]) < 1 and abs(q[0]-lc[0]) < 1 and abs(q[1]-lc[1]) < 1) or \
                               (abs(q[0]-oc[0]) < 1 and abs(q[1]-oc[1]) < 1 and abs(p[0]-lc[0]) < 1 and abs(p[1]-lc[1]) < 1):
                                roads.add(L)
                    check(roads == {'A', 'B', 'C'}, f'{band} p{pno+1}: roads O-{sorted(roads)}')
                    head = [t for t, p, _ in ws if abs(p[1] - (min(c['rect'][1] for c in st) - 8)) < 14 and
                            min(c['rect'][0] for c in st) - 10 < p[0] < max(c['rect'][2] for c in st) + 10 and t in ('start', 'target', 'picture')]
                    kind = 'target' if 'target' in head else ('start' if 'start' in head else '?')
                    piles = {L: (labs[L]['fill'], labs[L]['open']) for L in 'AOBC'}
                    st_y = min(c['rect'][1] for c in st)
                    st_x = min(c['rect'][0] for c in st)
                    say(f'   star {kind:6s} y={st_y:5.0f} x={st_x:5.0f} ' + ' '.join(f'{L}:{f}f/{o}o' for L, (f, o) in piles.items()))
                    extracted.setdefault((band, pno + 1), []).append(('star', kind, round(st_y), round(st_x),
                                                                      {L: (labs[L]['fill'] if kind == 'start' else labs[L]['open']) for L in 'AOBC'},
                                                                      {L: (labs[L]['open'] if kind == 'start' else labs[L]['fill']) for L in 'AOBC'}))
            for y, board in group_rows(conts):
                if len(board) < 3:
                    continue
                labels = [b['label'] for b in board]
                expect = [str(i) for i in range(len(board))]
                if board[0]['w'] > 40 or len(board) != 3:  # the small rule diagram has no bin numbers
                    check(labels == expect, f'{band} p{pno+1}: bin labels {labels} at y={y}')
                ws_ = {round(b['w'], 1) for b in board}
                hs_ = {round(b['h'], 1) for b in board}
                gaps = {round(b2['rect'][0] - b1['rect'][2], 1) for b1, b2 in zip(board, board[1:])}
                check(len(ws_) == 1 and len(hs_) == 1 and len(gaps) == 1, f'{band} p{pno+1}: uneven bins at y={y}: {ws_} {hs_} {gaps}')
                conn = connectors_ok(board, lines)
                fill, opn = board_repr(board)
                lab = row_label(ws, y, board[0]['rect'][0])
                big = board[0]['w'] > 40
                if len(board) == 3 and not big:
                    lab = 'rule-diagram'
                say(f'   row y={y:5.0f} x0={board[0]["rect"][0]:5.0f} bins={len(board)} size={board[0]["w"]:.1f}x{board[0]["h"]:.1f}pt '
                    f'gap={next(iter(gaps)):.1f}pt connectors={"all" if conn else "MISSING"} label="{lab}" filled="{fill}" open="{opn}"')
                check(conn or lab == 'rule-diagram', f'{band} p{pno+1}: missing connector at y={y}')
                extracted.setdefault((band, pno + 1), []).append(('row', lab, round(y), round(board[0]['rect'][0]), fill, opn))
        say()

    # rule diagram: 3 small rows, one filled counter in bin 0, 1, 2
    say('== Rule diagram (both bands, page 1)')
    for band in ('2-3', '4-5'):
        rd = [e for e in extracted[(band, 1)] if e[0] == 'row' and e[1] == 'rule-diagram']
        seq = [e[4] for e in sorted(rd, key=lambda e: e[3])]
        say(f'   {band}: start/middle/target counters at {seq}')
        check(seq == ['0', '1', '2'], f'{band} rule diagram {seq}')

    # compare with the data typed into check_math.py
    say()
    say('== Typed data in check_math.py versus the PDFs')

    def line_pairs(band, page):
        rows = [e for e in extracted[(band, page)] if e[0] == 'row' and e[1] != 'rule-diagram']
        rows.sort(key=lambda e: (e[2], e[3]))
        return rows

    for (band, page, prob), pairs in W.LINE_PAIRS.items():
        rows = line_pairs(band, page)
        got = []
        i = 0
        while i < len(rows):
            r = rows[i]
            if r[1] == 'start' and i + 1 < len(rows) and rows[i + 1][1].startswith('target'):
                got.append((r[4], rows[i + 1][5]))
                check(r[5] == '' and rows[i + 1][4] == '', f'{band} p{page}: mixed counters in a row')
                i += 2
            else:
                i += 1
        got = [g for g in got if g != ('', '')]
        ok = check(got == [tuple(p) for p in pairs], f'{band} p{page} {prob}: PDF {got} vs typed {pairs}')
        say(f'   {band} p{page} {prob}: {"OK" if ok else "MISMATCH"} {got}')

    # Grades 2-3 Problem 4: target 2222, five blank start rows
    rows = line_pairs('2-3', 4)
    tgt = [r for r in rows if r[1].startswith('target')]
    starts = [r for r in rows if r[1] == 'start']
    ok = check(len(tgt) == 1 and tgt[0][5] == '2222' and len(starts) == 5 and all(r[4] == '' for r in starts),
               '2-3 p4 target/start rows')
    say(f'   2-3 p4 P4: target {tgt[0][5]!r}, {len(starts)} blank start rows: {"OK" if ok else "MISMATCH"}')

    # Grades 4-5 Problem 4 cards
    rows = line_pairs('4-5', 4)
    cards = [r[4] for r in sorted(rows, key=lambda e: (e[2], e[3]))]
    ok = check(cards == W.CARDS, f'4-5 p4 cards {cards} vs typed {W.CARDS}')
    say(f'   4-5 p4 cards in reading order: {cards}: {"OK" if ok else "MISMATCH"}')

    # stars
    for (band, page), pairs in W.STAR_PAIRS.items():
        st = sorted([e for e in extracted[(band, page)] if e[0] == 'star'], key=lambda e: (e[2], e[3]))
        got = []
        for a, b in zip(st[0::2], st[1::2]):
            check(a[1] == 'start' and b[1] == 'target', f'{band} p{page}: star order {a[1]},{b[1]}')
            check(all(v == 0 for v in a[5].values()) and all(v == 0 for v in b[5].values()), f'{band} p{page}: mixed star counters')
            got.append((a[4], b[4]))
        got = [g for g in got if sum(g[0].values()) + sum(g[1].values()) > 0]
        ok = check(got == pairs, f'{band} p{page} stars {got} vs typed {pairs}')
        say(f'   {band} p{page} stars: {"OK" if ok else "MISMATCH"} {got}')

    # Grades 4-5 Problem 6 and Grades 2-3 Problem 6: blank boards
    for band in ('2-3', '4-5'):
        rows = line_pairs(band, 6)
        ok = check(all(r[4] == '' and r[5] == '' for r in rows) and len(rows) in (2, 3), f'{band} p6 boards')
        say(f'   {band} p6: {len(rows)} blank six-bin boards ({[r[1] for r in rows]}): {"OK" if ok else "MISMATCH"}')

    say()
    say(f'FAILURES: {len(FAILS)}')
    for f in FAILS:
        say('  ' + f)
    text = '\n'.join(OUT) + '\n'
    (HERE / 'check_diagrams.py.out').write_text(text)
    print(text)
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
