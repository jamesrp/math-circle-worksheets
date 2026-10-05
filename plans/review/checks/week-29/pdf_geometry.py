"""Read every diagram on the delivered Week 29 student PDFs (base bands and
bonus) with PyMuPDF and check it against its label and the printed text.

Base packets: unit strips (target outlines), rod keys, the 3+4=7 launch
example, target boxes and number-line rulers.  Bonus: the 4,3,4 launch row and
the used/unused sealed-box rows.  Writes pdf_geometry.json; output saved as
pdf_geometry.out.
"""
import json
import re
import sys
import os

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import CM, HERE, PDFS, Log  # noqa: E402

log = Log()
TOL = 0.6  # points


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def words_on(page):
    return [(w[0], w[1], w[2], w[3], w[4]) for w in page.get_text('words')]


def word_at(words, x, y, pad=4):
    """Words whose centre lies within pad points of (x, y)."""
    out = []
    for x0, y0, x1, y1, t in words:
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        if abs(cx - x) <= pad + (x1 - x0) / 2 and abs(cy - y) <= pad:
            out.append(t)
    return out


def boxes(page):
    """Closed 4-line stroked/filled paths: rectangles."""
    out = []
    for d in page.get_drawings():
        it = d['items']
        if len(it) == 4 and all(i[0] == 'l' for i in it):
            r = d['rect']
            out.append({'x0': r.x0, 'y0': r.y0, 'x1': r.x1, 'y1': r.y1, 'w': r.width, 'h': r.height,
                        'lw': d.get('width') or 0, 'fill': d.get('fill')})
        elif len(it) == 1 and it[0][0] == 're':
            r = it[0][1]
            out.append({'x0': r.x0, 'y0': r.y0, 'x1': r.x1, 'y1': r.y1, 'w': r.width, 'h': r.height,
                        'lw': d.get('width') or 0, 'fill': d.get('fill')})
    return out


def segs(page):
    out = []
    for d in page.get_drawings():
        it = d['items']
        if len(it) == 1 and it[0][0] == 'l':
            a, b = it[0][1], it[0][2]
            out.append({'x0': a.x, 'y0': a.y, 'x1': b.x, 'y1': b.y, 'lw': d.get('width') or 0,
                        'color': d.get('color')})
    return out


def interior_lines(sg, b, unit):
    xs = sorted(s['x0'] for s in sg if close(s['x0'], s['x1']) and b['x0'] + 1 < s['x0'] < b['x1'] - 1
                and close(min(s['y0'], s['y1']), b['y0'], 1) and close(max(s['y0'], s['y1']), b['y1'], 1))
    return xs


geo = {}
for band in ('k-1', 'grades-2-3', 'grades-4-5'):
    doc = pymupdf.open(PDFS[band])
    geo[band] = []
    for pno, page in enumerate(doc, 1):
        W = words_on(page)
        bx = boxes(page)
        sg = segs(page)
        pg = {'page': pno, 'strips': [], 'keys': [], 'targets': [], 'rulers': [], 'thick': []}
        unit = CM
        for b in bx:
            # unit strips and rod keys: height 1 cm, width whole cm
            if close(b['h'], unit) and b['w'] > unit * 0.9 and close(b['w'] / unit, round(b['w'] / unit), 0.03):
                n = round(b['w'] / unit)
                inner = interior_lines(sg, b, unit)
                spaced = all(close(x, b['x0'] + (i + 1) * unit) for i, x in enumerate(inner))
                if b['lw'] > 1.2:
                    pg['thick'].append({'n': n, 'x0': round(b['x0'], 2)})
                    continue
                if b['fill'] is not None and b['fill'][0] < 0.99:
                    lab = word_at(W, (b['x0'] + b['x1']) / 2, (b['y0'] + b['y1']) / 2)
                    pg['keys'].append({'n': n, 'label': lab, 'cells': len(inner) + 1, 'spaced': spaced})
                else:
                    lab = word_at(W, b['x1'] + 0.4 * unit, (b['y0'] + b['y1']) / 2, 6)
                    centre = word_at(W, (b['x0'] + b['x1']) / 2, (b['y0'] + b['y1']) / 2)
                    pg['strips'].append({'n': n, 'label': lab, 'centre_text': centre, 'cells': len(inner) + 1,
                                         'spaced': spaced, 'x0': round(b['x0'], 2), 'y0': round(b['y0'], 2)})
            elif close(b['w'], 1.8 * unit) and close(b['h'], 1.2 * unit):
                lab = word_at(W, (b['x0'] + b['x1']) / 2, (b['y0'] + b['y1']) / 2, 8)
                pg['targets'].append(lab)
        # rulers: long horizontal line with ticks
        horiz = [s for s in sg if close(s['y0'], s['y1']) and abs(s['x1'] - s['x0']) > 5 * unit and s['lw'] > 0.6]
        for h in horiz:
            y = h['y0']
            ticks = sorted(s['x0'] for s in sg if close(s['x0'], s['x1']) and min(s['y0'], s['y1']) < y < max(s['y0'], s['y1'])
                           and abs(s['y1'] - s['y0']) < 0.5 * unit)
            if len(ticks) < 3:
                continue
            spacing = [ticks[i + 1] - ticks[i] for i in range(len(ticks) - 1)]
            labels = []
            for t in ticks:
                lab = word_at(W, t, y + 0.45 * unit, 5)
                labels.append(lab[0] if lab else None)
            pg['rulers'].append({'ticks': len(ticks), 'min_sp': min(spacing), 'max_sp': max(spacing),
                                 'labels': labels, 'zero_x': round(ticks[0], 2)})
        geo[band].append(pg)

        # the plain 7-cm strip under the thick 3 | 4 outlines is the launch example, not a target
        if pg['thick']:
            ex = [s for s in pg['strips'] if s['n'] == 7 and abs(s['x0'] - pg['thick'][0]['x0']) < 1]
            for s in ex:
                pg['strips'].remove(s)
                eq = word_at(W, s['x0'] + 9 * unit, s['y0'] + unit / 2, 50)
                in3 = word_at(W, s['x0'] + 1.5 * unit, s['y0'] + unit / 2)
                in4 = word_at(W, s['x0'] + 5 * unit, s['y0'] + unit / 2)
                log.check(s['cells'] == 7 and s['spaced'] and ''.join(eq) == '3+4=7' and in3 == ['3'] and in4 == ['4'],
                          f"{band} p{pno} launch example base: 7 cm, 7 cells, inner labels 3 and 4, text {''.join(eq)!r}")
        # ---- checks on this page ----
        for s in pg['strips']:
            log.check(s['label'] == [str(s['n'])] and s['cells'] == s['n'] and s['spaced'],
                      f"{band} p{pno} strip at y={s['y0']}: {s['n']} cm long, {s['cells']} equal 1 cm cells, label {s['label']}")
        for k in pg['keys']:
            log.check(k['label'] == [str(k['n'])] and k['cells'] == k['n'] and k['spaced'],
                      f"{band} p{pno} rod key: {k['n']} cm, {k['cells']} cells, label {k['label']}")
        for r in pg['rulers']:
            want = [str(i) for i in range(r['ticks'])]
            log.check(close(r['min_sp'], unit, 0.3) and close(r['max_sp'], unit, 0.3) and r['labels'] == want,
                      f"{band} p{pno} ruler: {r['ticks']} ticks 0..{r['ticks'] - 1}, spacing {r['min_sp']:.2f}-{r['max_sp']:.2f} pt (1 cm = {unit:.2f})")
        if pg['thick']:
            log.check([t['n'] for t in pg['thick']] == [3, 4] and pg['thick'][1]['x0'] - pg['thick'][0]['x0'] - 3 * unit < TOL,
                      f"{band} p{pno} launch example: thick outlines {[t['n'] for t in pg['thick']]} butted end to end")

# Expected diagram content from the printed problem text
EXPECT = {
    ('k-1', 1): {'strips': [1, 2, 5, 6, 8, 9, 10], 'keys': [3, 4], 'example7': True},
    ('k-1', 2): {'strips': [12, 12, 15, 15]},
    ('k-1', 3): {'strips': [4, 7, 8, 9, 10, 11, 12], 'keys': [3, 5]},
    ('k-1', 4): {'targets': list(range(6, 19)), 'rulers': [18, 18]},
    ('k-1', 5): {'targets': list(range(1, 13)), 'rulers': [12, 12], 'keys': [2, 4]},
    ('k-1', 6): {'targets': list(range(6, 13)), 'rulers': [12, 12], 'keys': [2, 3, 4, 5]},
    ('grades-2-3', 1): {'targets': list(range(1, 17)), 'rulers': [16, 16], 'keys': [3, 4], 'example7': True},
    ('grades-2-3', 3): {'targets': list(range(1, 21)), 'keys': [3, 5]},
    ('grades-2-3', 4): {'keys': [3, 4, 3, 5]},
    ('grades-2-3', 5): {'targets': list(range(12, 29)), 'keys': [4, 7]},
    ('grades-4-5', 1): {'targets': list(range(1, 21)), 'keys': [3, 4], 'example7': True},
    ('grades-4-5', 3): {'targets': list(range(18, 30))},
    ('grades-4-5', 5): {'targets': list(range(19, 32))},
}
for band in geo:
    for pg in geo[band]:
        e = EXPECT.get((band, pg['page']), {})
        got_t = [int(t[0]) for t in pg['targets'] if t]
        got_s = [s['n'] for s in pg['strips']]
        got_k = [k['n'] for k in pg['keys']]
        got_r = [r['ticks'] - 1 for r in pg['rulers']]
        log.check(got_t == e.get('targets', []), f"{band} p{pg['page']} target boxes {got_t}")
        log.check(got_s == e.get('strips', []), f"{band} p{pg['page']} strips {got_s}")
        log.check(got_k == e.get('keys', []), f"{band} p{pg['page']} rod keys {got_k}")
        log.check(got_r == e.get('rulers', []), f"{band} p{pg['page']} rulers end at {got_r}")
        log.check(bool(pg['thick']) == e.get('example7', False), f"{band} p{pg['page']} 3+4=7 example present: {bool(pg['thick'])}")

# Ruler fits on the page (Letter width 612 pt) and its zero lines up with strips/keys
for band in geo:
    for pg in geo[band]:
        for r in pg['rulers']:
            right = r['zero_x'] + (r['ticks'] - 1) * CM
            log.check(right < 612 - 20, f"{band} p{pg['page']} ruler right end {right:.1f} pt inside page")

# ---------------- Bonus ----------------
doc = pymupdf.open(PDFS['bonus'])
bonus = {}
for pno in (1, 3):
    page = doc[pno - 1]
    W = words_on(page)
    bx = [b for b in boxes(page) if b['fill'] is not None and b['fill'][0] < 0.99 and b['h'] < 15]
    rows = {}
    for b in bx:
        rows.setdefault(round(b['y0']), []).append(b)
    out = []
    for y in sorted(rows):
        rs = sorted(rows[y], key=lambda b: b['x0'])
        labs = [word_at(W, (b['x0'] + b['x1']) / 2, (b['y0'] + b['y1']) / 2, 3) for b in rs]
        widths = [b['w'] for b in rs]
        contiguous = all(close(rs[i]['x1'], rs[i + 1]['x0']) for i in range(len(rs) - 1))
        out.append({'y': y, 'labels': labs, 'widths': [round(w, 2) for w in widths], 'contiguous': contiguous,
                    'x1': rs[-1]['x1'], 'h': rs[0]['h']})
    bonus[pno] = out
    for row in out:
        lab = [int(l[0]) for l in row['labels']]
        unit = row['widths'][0] / lab[0]
        prop = all(close(w / unit, l, 0.02) for w, l in zip(row['widths'], lab))
        tot = word_at(W, row['x1'] + 0.9 * 0.38 * CM + 4, row['y'] + row['h'] / 2, 12)
        log.check(prop and row['contiguous'], f"bonus p{pno} rod row {lab}: widths {row['widths']} proportional "
                  f"(unit {unit / CM:.2f} cm), butted end to end; text right of row {tot}")
        row['lengths'] = lab
        row['unit_cm'] = round(unit / CM, 3)
        row['right_text'] = tot
r1 = bonus[1][0]
log.check(r1['lengths'] == [4, 3, 4], 'bonus p1 launch row reads 4,3,4 left to right (word printed "4, 3, 4")')
used, unused = bonus[3][0]['lengths'], bonus[3][1]['lengths']
log.check(sorted(used + unused) == [3, 3, 3, 3, 4, 4, 4], f'bonus p3 used {used} + unused {unused} = the sealed box (four 3s, three 4s)')
log.check(sum(used) == 13 and '13' in bonus[3][0]['right_text'], f'bonus p3 used total {sum(used)}, printed {bonus[3][0]["right_text"]}')
log.check(sum(unused) == 11 and '11' in bonus[3][1]['right_text'], f'bonus p3 unused total {sum(unused)}, printed {bonus[3][1]["right_text"]}')

# Bonus answer slots per column (P1) and P2
txt = doc[0].get_text()
log.info('bonus P1 has 6 slots per target column and P2 has 12 slots (from student-src/bonus.tex \\wordrows and the 6x2 table)')

json.dump({'base': geo, 'bonus': {str(k): v for k, v in bonus.items()}}, open(HERE / 'pdf_geometry.json', 'w'), indent=1, default=str)
log.done()
