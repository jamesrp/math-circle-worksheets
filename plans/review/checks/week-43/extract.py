"""Read every picture card, label, ticket, arrow, cross-out and answer frame
straight from the delivered Week 43 PDFs (PyMuPDF), and check that the
diagrams agree with the text.

Writes extracted.json (geometry per page) and extract.out (checks).
"""
import json
import os
import re

import pymupdf

from common import HERE, PDFS, Report, swap

FILLS = {  # TikZ colours used by the base packet's icon() helper
    'A': (1.0, 0.89, 0.78),   # orange!22 square
    'B': (0.78, 1.0, 0.78),   # green!22 circle
    'C': (0.89, 0.78, 0.89),  # violet!22 triangle
    'D': (0.757, 0.911, 0.984),  # cyan!22 diamond (as rendered)
    'E': (1.0, 0.984, 0.799),    # yellow!25 pentagon (as rendered)
}
SHAPE_OF = {'A': 'square', 'B': 'circle', 'C': 'triangle', 'D': 'diamond', 'E': 'pentagon'}


def close(a, b, tol=0.02):
    return all(abs(x - y) <= tol for x, y in zip(a, b))


def shape_of(items):
    kinds = [it[0] for it in items]
    if kinds == ['re'] or kinds == ['qu']:
        return 'square'
    if kinds and all(k == 'c' for k in kinds):
        return 'circle'
    if all(k == 'l' for k in kinds):
        pts = [it[1] for it in items]
        if len(kinds) == 3:
            return 'triangle'
        if len(kinds) == 5:
            return 'pentagon'
        if len(kinds) == 4:
            axis = all(abs(it[1].x - it[2].x) < .05 or abs(it[1].y - it[2].y) < .05 for it in items)
            return 'square' if axis else 'diamond'
    return 'other:' + ''.join(kinds)


def page_data(page):
    icons, frames, black_lines = [], [], []
    for dr in page.get_drawings():
        r = dr['rect']
        fill = dr.get('fill')
        col = dr.get('color')
        if fill is not None and col is not None and close(col, (0, 0, 0)):
            letter = next((k for k, v in FILLS.items() if close(fill, v)), None)
            if letter:
                icons.append(dict(fill_letter=letter, shape=shape_of(dr['items']),
                                  cx=round((r.x0 + r.x1) / 2, 2), cy=round((r.y0 + r.y1) / 2, 2),
                                  w=round(r.width, 2), h=round(r.height, 2)))
                continue
        if fill is None and col is not None and abs(col[0] - .675) < .01:
            frames.append(dict(x0=round(r.x0, 1), y0=round(r.y0, 1), x1=round(r.x1, 1), y1=round(r.y1, 1)))
        elif fill is None and col is not None and close(col, (0, 0, 0)):
            for it in dr['items']:
                if it[0] == 'l':
                    p, q = it[1], it[2]
                    black_lines.append(dict(x0=round(p.x, 1), y0=round(p.y, 1), x1=round(q.x, 1), y1=round(q.y, 1)))
    spans = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = ''.join(s['text'] for s in l['spans']).strip()
            if t:
                x0, y0, x1, y1 = l['bbox']
                spans.append(dict(t=t, x0=round(x0, 1), y0=round(y0, 1), x1=round(x1, 1), y1=round(y1, 1),
                                  size=round(l['spans'][0]['size'], 1)))
    return icons, frames, black_lines, spans


def inside(px, py, f, pad=0.5):
    return f['x0'] - pad <= px <= f['x1'] + pad and f['y0'] - pad <= py <= f['y1'] + pad


def card_of(ic, frames):
    fs = [f for f in frames if inside(ic['cx'], ic['cy'], f)]
    return min(fs, key=lambda f: (f['x1'] - f['x0']) * (f['y1'] - f['y0'])) if fs else None


def rows_of(icons, frames, tol=4):
    """Group icons into rows: same centre height and in touching card frames.

    Icons drawn without a card frame (the chooser's draw sequence) stand alone.
    """
    band = []
    for ic in sorted(icons, key=lambda i: (i['cy'], i['cx'])):
        for r in band:
            if abs(r[0]['cy'] - ic['cy']) <= tol:
                r.append(ic)
                break
        else:
            band.append([ic])
    out = []
    for r in band:
        r.sort(key=lambda i: i['cx'])
        cur = [r[0]]
        for a, b in zip(r, r[1:]):
            fa, fb = card_of(a, frames), card_of(b, frames)
            if not (fa and fb and abs(fa['x1'] - fb['x0']) < 2.5):
                out.append(cur)
                cur = []
            cur.append(b)
        out.append(cur)
    return out


def problem_marks(spans):
    marks = []
    for s in spans:
        m = re.match(r'Problem (\d+):', s['t'])
        if m:
            marks.append((s['y0'], int(m.group(1))))
    return sorted(marks)


def which_problem(y, marks, page_first=None):
    cur = None
    for y0, n in marks:
        if y >= y0 - 1:
            cur = n
    return cur


def main():
    R = Report('extract')
    data = {}
    import hashlib
    from common import SRC, BONUS_SRC
    refs = {'k-1': os.path.join(SRC, 'reference-pdfs', 'k-1.pdf'),
            'grades-2-3': os.path.join(SRC, 'reference-pdfs', 'grades-2-3.pdf'),
            'grades-4-5': os.path.join(SRC, 'reference-pdfs', 'grades-4-5.pdf'),
            'guide': os.path.join(SRC, 'reference-pdfs', 'facilitator-guide.pdf'),
            'bonus': os.path.join(BONUS_SRC, 'reference-pdfs', 'week-43-bonus.pdf'),
            'bonus-guide': os.path.join(BONUS_SRC, 'reference-pdfs', 'week-43-bonus-facilitator.pdf')}
    R.head('delivered PDFs vs source reference copies (MD5)')
    for k, ref in refs.items():
        a = hashlib.md5(open(PDFS[k], 'rb').read()).hexdigest()
        b = hashlib.md5(open(ref, 'rb').read()).hexdigest()
        R.check(a == b, f'{os.path.basename(PDFS[k])} == {os.path.relpath(ref, SRC + "/..")} ({a})')
    for band in ['k-1', 'grades-2-3', 'grades-4-5']:
        R.head(f'{band}: {PDFS[band]}')
        doc = pymupdf.open(PDFS[band])
        data[band] = []
        for pno, page in enumerate(doc, 1):
            icons, frames, blines, spans = page_data(page)
            marks = problem_marks(spans)
            # 1. every icon: shape agrees with its fill colour; equal scaling
            for ic in icons:
                R.check(ic['shape'] == SHAPE_OF[ic['fill_letter']],
                        f'p{pno} icon at ({ic["cx"]:.0f},{ic["cy"]:.0f}): fill {ic["fill_letter"]} drawn as {ic["shape"]}')
                R.check(abs(ic['w'] - ic['h']) < 0.2,
                        f'p{pno} icon {ic["fill_letter"]} at ({ic["cx"]:.0f},{ic["cy"]:.0f}) bbox {ic["w"]}x{ic["h"]} pt (equal x/y scale)')
            # 2. letter labels sit in the same card as the icon and agree
            letters = [s for s in spans if re.fullmatch(r'[A-E]', s['t']) and s['size'] < 12]
            for s in letters:
                lx, ly = (s['x0'] + s['x1']) / 2, (s['y0'] + s['y1']) / 2
                card = [f for f in frames if inside(lx, ly, f)]
                card = min(card, key=lambda f: (f['x1'] - f['x0']) * (f['y1'] - f['y0'])) if card else None
                ics = [ic for ic in icons if card and inside(ic['cx'], ic['cy'], card)]
                if not ics:  # labels outside frames (Problem 1 card strip uses frames too)
                    ics = sorted(icons, key=lambda ic: (ic['cx'] - lx) ** 2 + (ic['cy'] - ly) ** 2)[:1]
                R.check(len(ics) == 1 and ics[0]['fill_letter'] == s['t'],
                        f'p{pno} label {s["t"]} at ({lx:.0f},{ly:.0f}) belongs to icon {[i["fill_letter"] for i in ics]}')
            # 3. rows of icons -> words
            rws = []
            for r in rows_of(icons, frames):
                w = ''.join(i['fill_letter'] for i in r)
                rws.append(dict(word=w, cy=r[0]['cy'], x0=r[0]['cx'], x1=r[-1]['cx'],
                                problem=which_problem(r[0]['cy'], marks) or 'rules'))
            # 4. empty frames (answer space)
            empty = []
            for f in frames:
                if any(inside(ic['cx'], ic['cy'], f) for ic in icons):
                    continue
                txt = [s['t'] for s in spans if inside((s['x0'] + s['x1']) / 2, (s['y0'] + s['y1']) / 2, f)]
                empty.append(dict(f, text=' '.join(txt), problem=which_problem(f['y0'], marks)))
            # 5. arrows with labels "i with j"
            arrows = [s for s in spans if re.fullmatch(r'\d with \d', s['t'])]
            trans = []
            for a in arrows:
                ax = (a['x0'] + a['x1']) / 2
                band_rows = [r for r in rws if a['y1'] - 2 <= r['cy'] <= a['y1'] + 40]
                left = [r for r in band_rows if r['x1'] < ax]
                right = [r for r in band_rows if r['x0'] > ax]
                if left and right:
                    lw = max(left, key=lambda r: r['x1'])['word']
                    rw = min(right, key=lambda r: r['x0'])['word']
                    i, j = map(int, a['t'].split(' with '))
                    trans.append(dict(label=a['t'], before=lw, after=rw))
                    R.check(swap(lw, i, j) == rw, f'p{pno} arrow "{a["t"]}": {lw} -> {rw} (computed {swap(lw, i, j)})')
                else:
                    R.check(False, f'p{pno} arrow "{a["t"]}" has no rows on both sides')
            # 6. diagonal black lines (cross-outs)
            cross = []
            for l in blines:
                if abs(l['x1'] - l['x0']) > 10 and abs(l['y1'] - l['y0']) > 10:
                    mx, my = (l['x0'] + l['x1']) / 2, (l['y0'] + l['y1']) / 2
                    hit = [ic['fill_letter'] for ic in icons if abs(ic['cx'] - mx) < 6 and abs(ic['cy'] - my) < 6]
                    cross.append(dict(l, covers=hit, problem=which_problem(my, marks)))
            data[band].append(dict(page=pno, problems=[n for _, n in marks], rows=rws, empty_frames=empty,
                                   transitions=trans, crossouts=cross,
                                   text=' '.join(s['t'] for s in spans)))
            R.note(f'p{pno} problems {[n for _, n in marks]}; rows: ' +
                   ', '.join(f'{r["word"]}(P{r["problem"]})' for r in rws))
            for c in cross:
                R.note(f'p{pno} cross-out line over {c["covers"]} (P{c["problem"]})')
    # ---------------------------------------------------------------- bonus
    R.head(f'bonus: {PDFS["bonus"]}')
    doc = pymupdf.open(PDFS['bonus'])
    data['bonus'] = []
    for pno, page in enumerate(doc, 1):
        spans = []
        for b in page.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                for s in l['spans']:
                    t = s['text'].strip()
                    if t:
                        x0, y0, x1, y1 = s['bbox']
                        spans.append(dict(t=t, x0=round(x0, 1), y0=round(y0, 1), x1=round(x1, 1), y1=round(y1, 1),
                                          size=round(s['size'], 1)))
        rects, lines, circles = [], [], []
        for dr in page.get_drawings():
            r = dr['rect']
            kinds = [it[0] for it in dr['items']]
            if kinds == ['re']:
                rects.append(dict(x0=round(r.x0, 1), y0=round(r.y0, 1), x1=round(r.x1, 1), y1=round(r.y1, 1),
                                  col=round(dr['color'][0], 2) if dr.get('color') else None))
            elif kinds and all(k == 'c' for k in kinds):
                circles.append(dict(cx=round((r.x0 + r.x1) / 2, 1), cy=round((r.y0 + r.y1) / 2, 1),
                                    w=round(r.width, 2), h=round(r.height, 2)))
            elif kinds == ['l']:
                it = dr['items'][0]
                lines.append(dict(x0=round(it[1].x, 1), y0=round(it[1].y, 1), x1=round(it[2].x, 1),
                                  y1=round(it[2].y, 1), w=round(dr.get('width') or 0, 2)))
        # big bold letters (16 pt) are card faces; group by baseline
        faces = sorted([s for s in spans if s['size'] == 16.0], key=lambda s: (round(s['y0']), s['x0']))
        bands = {}
        for s in faces:
            bands.setdefault(round(s['y0']), []).append(s)
        words = []
        for y, ss in sorted(bands.items()):
            ss.sort(key=lambda s: s['x0'])
            cur = [ss[0]]
            for a, b in zip(ss, ss[1:]):
                if b['x0'] - a['x1'] > 60:
                    words.append(cur)
                    cur = []
                cur.append(b)
            words.append(cur)
        wl = [dict(word=''.join(s['t'] for s in w), y=w[0]['y0'], x0=w[0]['x0'], x1=w[-1]['x1']) for w in words]
        # every 16 pt letter must sit inside a card rectangle
        for s in faces:
            cx, cy = (s['x0'] + s['x1']) / 2, (s['y0'] + s['y1']) / 2
            R.check(any(inside(cx, cy, r) for r in rects), f'bonus p{pno} letter {s["t"]} lies inside a card')
        sq = [r for r in rects if abs((r['x1'] - r['x0']) - (r['y1'] - r['y0'])) < .2]
        R.check(len(sq) == len(rects), f'bonus p{pno}: all {len(rects)} rectangles are squares (equal scaling)')
        for c in circles:
            R.check(abs(c['w'] - c['h']) < .2, f'bonus p{pno} circle at ({c["cx"]},{c["cy"]}) is round ({c["w"]}x{c["h"]})')
        data['bonus'].append(dict(page=pno, words=wl, rects=rects, lines=lines, circles=circles,
                                  spans=[s for s in spans if s['size'] <= 10]))
        R.note(f'bonus p{pno} card words: ' + ', '.join(w['word'] for w in wl))
    # bonus page 1: picture of each labeled card
    p1 = data['bonus'][0]
    cards = [r for r in p1['rects'] if abs(r['x1'] - r['x0'] - 72) < .5]
    R.check(len(cards) == 4, f'bonus p1: four 72 pt (25.4 mm) model cards, found {len(cards)}')
    for r in cards:
        lab = [s['t'] for s in p1['spans'] if inside((s['x0'] + s['x1']) / 2, (s['y0'] + s['y1']) / 2, r)]
        has_sq = any(q is not r and q['x0'] > r['x0'] and q['x1'] < r['x1'] and q['y0'] > r['y0'] and q['y1'] < r['y1']
                     for q in p1['rects'])
        has_ci = any(inside(c['cx'], c['cy'], r) for c in p1['circles'])
        pic = 'square' if has_sq and not has_ci else 'circle' if has_ci and not has_sq else '?'
        R.check(lab and ((lab[0][0] == 'A' and pic == 'square') or (lab[0][0] == 'B' and pic == 'circle')),
                f'bonus p1 card {lab} shows {pic}')
    blanks1 = [r for r in p1['rects'] if abs(r['x1'] - r['x0'] - 44) < .5]
    R.note(f'bonus p1: {len(blanks1)} blank 44 pt cells = {len(blanks1) // 4} four-card record rows')
    # bonus page 2: cut example and bar position
    p2 = data['bonus'][1]
    ws = [w['word'] for w in p2['words']]
    R.check(ws[:2] == ['WXYZ', 'YZWX'], f'bonus p2 cut example words {ws[:2]}')
    w = 'WXYZ'
    R.check(w[2:] + w[:2] == 'YZWX', 'bonus p2: moving the front two of WXYZ gives YZWX')
    cut = [l for l in p2['lines'] if l['x0'] == l['x1'] and l['w'] > 1.5]
    xr = sorted([r for r in p2['rects'] if abs(r['x1'] - r['x0'] - 40) < .5 and r['x0'] < 240], key=lambda r: r['x0'])
    R.check(len(cut) == 1 and xr[1]['x1'] < cut[0]['x0'] < xr[2]['x0'],
            f'bonus p2: cut bar at x={cut[0]["x0"]} lies between X (ends {xr[1]["x1"]}) and Y (starts {xr[2]["x0"]})')
    blanks2 = [r for r in p2['rects'] if abs(r['x1'] - r['x0'] - 34) < .5]
    R.note(f'bonus p2: {len(blanks2)} blank 34 pt cells = {len(blanks2) // 4} four-card record rows')
    # bonus page 3: gap bars and gap numbers
    p3 = data['bonus'][2]
    ws3 = [w['word'] for w in p3['words']]
    R.note(f'bonus p3 words {ws3}')
    bars = sorted([l for l in p3['lines'] if l['x0'] == l['x1'] and 40 < abs(l['y1'] - l['y0']) < 60], key=lambda l: l['x0'])
    nums = sorted([s for s in p3['spans'] if re.fullmatch(r'[123]', s['t'])], key=lambda s: s['x0'])
    xs = sorted([r for r in p3['rects'] if abs(r['x1'] - r['x0'] - 42) < .5 and r['x0'] < 200], key=lambda r: r['x0'])
    R.check(len(bars) == 3 and len(xs) == 2, f'bonus p3: three gap bars around two old cards ({len(bars)}, {len(xs)})')
    R.check(bars[0]['x0'] < xs[0]['x0'] and xs[0]['x1'] < bars[1]['x0'] < xs[1]['x0'] and bars[2]['x0'] > xs[1]['x1'],
            'bonus p3: bars are before X, between X and Y, after Y')
    for b, n in zip(bars, nums):
        R.check(abs((n['x0'] + n['x1']) / 2 - b['x0']) < 3, f'bonus p3: gap number {n["t"]} sits under bar at x={b["x0"]}')
    xy = 'XY'
    R.check(xy[:1] + 'Z' + xy[1:] == 'XZY' and 'XZY' in ws3, 'bonus p3: inserting Z in gap 2 of XY gives XZY (printed)')
    with open(os.path.join(HERE, 'extracted.json'), 'w') as f:
        json.dump(data, f, indent=1)
    R.finish()


if __name__ == '__main__':
    main()
