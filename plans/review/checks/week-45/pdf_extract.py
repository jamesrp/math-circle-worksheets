"""Read every diagram in the delivered Week 45 PDFs (base bands and bonus)
straight from the PDF drawing and text layers with PyMuPDF.

Writes pdf_geometry.json (used by check_base.py / check_bonus.py) and prints
PASS/FAIL lines; output saved as pdf_extract.out.
"""
import hashlib
import json
import os
import re
import sys
from collections import Counter

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, PDFS, REFS, Log  # noqa: E402

log = Log()
PT_PER_CM = 72 / 2.54


def close(a, b, tol=0.6):
    return abs(a - b) <= tol


def colour_name(fill):
    if fill is None:
        return None
    r, g, b = (round(v, 2) for v in fill)
    if (r, g, b) == (1.0, 0.85, 0.85):
        return 'R'
    if (r, g, b) == (0.85, 0.85, 1.0):
        return 'B'
    if (r, g, b) == (0.0, 0.0, 0.0):
        return 'black'
    return None


def inside(inner, outer, pad=0.5):
    return (inner[0] >= outer[0] - pad and inner[1] >= outer[1] - pad
            and inner[2] <= outer[2] + pad and inner[3] <= outer[3] + pad)


def centre(r):
    return ((r[0] + r[2]) / 2, (r[1] + r[3]) / 2)


# ---------------------------------------------------------------- hashes
for key in PDFS:
    a = hashlib.md5(open(PDFS[key], 'rb').read()).hexdigest()
    b = hashlib.md5(open(REFS[key], 'rb').read()).hexdigest()
    log.check(a == b, f'{key}: delivered PDF is byte-identical to source reference copy ({a})')

geometry = {}

# ---------------------------------------------------------------- base bands
for band in ['k-1', 'grades-2-3', 'grades-4-5']:
    doc = pymupdf.open(PDFS[band])
    bandgeo = {'pages': []}
    for pno, page in enumerate(doc):
        words = page.get_text('words')
        drawings = page.get_drawings()
        faces, covers, brackets, boxes, arrows = [], [], [], [], []
        for d in drawings:
            name = colour_name(d.get('fill'))
            r = tuple(d['rect'])
            w, h = r[2] - r[0], r[3] - r[1]
            if name in ('R', 'B') and h > 50:
                faces.append({'fill': name, 'rect': r})
            elif name == 'black' and 8 < w < 20 and 8 < h < 20:
                covers.append(r)
            elif d.get('fill') is None and d.get('color') and close(d['color'][0], 0.5, 0.01) \
                    and len(d['items']) == 3 and all(i[0] == 'l' for i in d['items']):
                brackets.append(r)
            elif d.get('fill') is None and d.get('color') and close(d['color'][0], 0.675, 0.01):
                boxes.append(r)
            elif d.get('fill') is None and d.get('color') == (0.0, 0.0, 0.0) and len(d['items']) == 1 \
                    and d['items'][0][0] == 'l' and h < 1:
                arrows.append(r)
        # letters and marks inside faces
        for f in faces:
            inner = [wd for wd in words if inside(wd[:4], f['rect'])]
            f['letters'] = [wd[4] for wd in inner if wd[4] in ('R', 'B') and (wd[3] - wd[1]) > 14]
            f['marks'] = [wd[4] for wd in inner if wd[4].isdigit()]
            f['covered'] = any(inside(c, f['rect']) for c in covers)
            f['w'] = f['rect'][2] - f['rect'][0]
            f['h'] = f['rect'][3] - f['rect'][1]
        # ticket boxes with a single digit label (small squares)
        tickets = []
        for b in boxes:
            bw, bh = b[2] - b[0], b[3] - b[1]
            if bw < 40 and bh < 40:
                inner = [wd[4] for wd in words if inside(wd[:4], b)]
                tickets.append({'rect': b, 'label': inner})
        # bracket pairing: endpoints at face centres
        pairs = []
        for br in brackets:
            left = [f for f in faces if close(centre(f['rect'])[0], br[0], 1.0) and f['rect'][3] < br[1] + 1]
            right = [f for f in faces if close(centre(f['rect'])[0], br[2], 1.0) and f['rect'][3] < br[1] + 1]
            # choose faces directly above (closest bottom edge)
            left = sorted(left, key=lambda f: br[1] - f['rect'][3])[:1]
            right = sorted(right, key=lambda f: br[1] - f['rect'][3])[:1]
            label = [wd[4] for wd in words if wd[1] > br[3] and wd[1] < br[3] + 20 and br[0] - 30 < wd[0] < br[2]]
            pairs.append({'bracket': br, 'left': left[0]['marks'] if left else None,
                          'right': right[0]['marks'] if right else None, 'label': ' '.join(label)})
        problems = [(wd[4], wd[5]) for wd in words if wd[4] == 'Problem']
        text = page.get_text()
        pnums = re.findall(r'Problem (\d+):', text)
        bandgeo['pages'].append({
            'page': pno + 1, 'faces': faces, 'covers': covers, 'tickets': tickets,
            'pairs': pairs, 'boxes': boxes, 'problems': pnums, 'text': text,
            'turn_over': 'turn over' in text,
        })
    geometry[band] = bandgeo

# --- checks on base bands
catalogues = {}
for band, bg in geometry.items():
    allfaces = [f for p in bg['pages'] for f in p['faces']]
    log.check(all(len(f['letters']) == 1 and f['letters'][0] == f['fill'] for f in allfaces),
              f'{band}: every one of {len(allfaces)} card faces shows a single letter R/B matching its fill colour')
    sizes = Counter((round(f['w'], 2), round(f['h'], 2)) for f in allfaces)
    log.check(len(sizes) == 1, f'{band}: all card faces have one size {dict(sizes)} pt '
                               f'(= {list(sizes)[0][0]/PT_PER_CM:.2f} x {list(sizes)[0][1]/PT_PER_CM:.2f} cm; matching-size cards)')
    log.check(all((len(f['marks']) == 1) != f['covered'] for f in allfaces),
              f'{band}: every face has exactly one visible mark or a black cover, never both or neither')
    # catalogue diagrams = pages with 6 uncovered faces in a row and 3 brackets
    cats = []
    for p in bg['pages']:
        rows_by_y = {}
        for f in p['faces']:
            if not f['covered']:
                rows_by_y.setdefault(round(f['rect'][1], 1), []).append(f)
        six = [r for r in rows_by_y.values() if len(r) == 6]
        if six and len(p['pairs']) == 3:
            row = six[0]
            row.sort(key=lambda f: f['rect'][0])
            colours = {int(f['marks'][0]): f['fill'] for f in row}
            partner = {}
            for pr in p['pairs']:
                a, b = int(pr['left'][0]), int(pr['right'][0])
                partner[a] = b
                partner[b] = a
                log.check(pr['label'] == 'same card', f'{band} p{p["page"]}: bracket under faces {a},{b} is labelled "same card"')
            ys = {round(f['rect'][1], 2) for f in row}
            log.check(len(ys) == 1, f'{band} p{p["page"]}: catalogue faces lie on one row')
            log.check([int(f['marks'][0]) for f in row] == [1, 2, 3, 4, 5, 6],
                      f'{band} p{p["page"]}: catalogue marks read 1..6 left to right')
            cats.append({'page': p['page'], 'colour': colours, 'partner': partner})
    log.check(len(cats) >= 2, f'{band}: {len(cats)} full catalogue diagrams found (pages {[c["page"] for c in cats]})')
    log.check(all(c['colour'] == cats[0]['colour'] and c['partner'] == cats[0]['partner'] for c in cats),
              f'{band}: all catalogue diagrams agree')
    cat = cats[0]
    log.note(f'{band}: catalogue colours {cat["colour"]}, partners {cat["partner"]}')
    catalogues[band] = cat
    # launch example: ticket 4 -> covered face -> 'turn over' -> face with mark
    p1 = bg['pages'][0]
    t4 = [t for t in p1['tickets'] if t['label'] == ['4'] and t['rect'][1] < 400]
    cov = [f for f in p1['faces'] if f['covered']]
    turned = [f for f in p1['faces'] if not f['covered'] and cov and close(f['rect'][1], cov[0]['rect'][1], 1)]
    ok = (len(t4) == 1 and len(cov) == 1 and len(turned) == 1 and p1['turn_over'])
    log.check(ok, f'{band} p1: launch example has ticket 4, one covered face and one turned-over face')
    if ok:
        shown, under = cov[0]['fill'], turned[0]
        log.check(shown == cat['colour'][4], f'{band} p1: launch shows ticket 4 face colour {shown} = catalogue colour of face 4')
        um = int(under['marks'][0])
        log.check(um == cat['partner'][4] and under['fill'] == cat['colour'][um],
                  f'{band} p1: turned-over face is mark {um} ({under["fill"]}) = catalogue partner of 4')
        lab = p1['text']
        log.check(('blue showing' in lab) == (shown == 'B') and ('red underneath' in lab) == (under['fill'] == 'R'),
                  f'{band} p1: launch captions "blue showing"/"red underneath" match the drawn faces')
    # chooser page: tickets 1 and 3 -> covered R faces
    chp = [p for p in bg['pages'] if 'Use only tickets 1 and 3' in p['text']]
    log.check(len(chp) == 1, f'{band}: one chooser page')
    if chp:
        p = chp[0]
        ts = sorted(p['tickets'], key=lambda t: t['rect'][0])
        cf = sorted([f for f in p['faces'] if f['covered']], key=lambda f: f['rect'][0])
        labels = [t['label'] for t in ts if t['rect'][1] < 200]
        log.check(labels == [['1'], ['3']] and len(cf) == 2,
                  f'{band} p{p["page"]}: chooser diagram shows ticket 1 and ticket 3, each with a covered face')
        log.check([f['fill'] for f in cf] == [cat['colour'][1], cat['colour'][3]] == ['R', 'R'],
                  f'{band} p{p["page"]}: chooser faces are red, as catalogue faces 1 and 3 are')
    # problem numbering
    nums = [int(n) for p in bg['pages'] for n in p['problems']]
    log.check(nums == list(range(1, len(nums) + 1)), f'{band}: problems numbered consecutively {nums}')

log.check(all(c['colour'] == catalogues['k-1']['colour'] and c['partner'] == catalogues['k-1']['partner']
              for c in catalogues.values()), 'all three bands use the same card catalogue')

# answer slots that encode a count
k1 = geometry['k-1']['pages']
p3 = k1[2]
small = [b for b in p3['boxes'] if b[1] > 590 and (b[2] - b[0]) < 40]
groups = []
for b in sorted(small, key=lambda r: r[0]):
    if groups and b[0] - groups[-1][-1][2] < 15:
        groups[-1].append(b)
    else:
        groups.append([b])
log.check([len(g) for g in groups] == [3, 3, 3], f'k-1 p3 P5: answer slots are {len(groups)} groups of sizes {[len(g) for g in groups]}')
p4 = k1[3]
big = [b for b in p4['boxes'] if b[1] > 540]
log.check(len(big) == 2, f'k-1 p4 P7: {len(big)} answer boxes')
g23 = geometry['grades-2-3']['pages'][0]
labs = sorted(int(t['label'][0]) for t in g23['tickets'] if t['rect'][1] > 400 and t['label'])
log.check(labs == [1, 2, 3, 4, 5, 6], f'2-3 p1 P1: ticket labels {labs}')
g45 = geometry['grades-4-5']['pages'][3]
labs = sorted(int(t['label'][0]) for t in g45['tickets'] if t['label'])
log.check(labs == [1, 2, 3, 4, 5, 6], f'4-5 p4 P6: ticket labels {labs}')
log.check(not g45['faces'], '4-5 p4 P6: ticket row carries numbers only (no colours given away)')

# ---------------------------------------------------------------- bonus
doc = pymupdf.open(PDFS['bonus'])
FILL = {'#e9a09f': 'R', '#aac5e6': 'B', '#b8d6aa': 'G'}


def hexcol(c):
    return '#%02x%02x%02x' % tuple(round(v * 255) for v in c) if c else None


bonus = {'pages': []}
for pno, page in enumerate(doc):
    words = page.get_text('words')
    toks = []
    for d in page.get_drawings():
        if d.get('fill') and hexcol(d['fill']) in FILL and sum(1 for i in d['items'] if i[0] == 'c') >= 4:
            r = tuple(d['rect'])
            lab = [wd[4] for wd in words if inside(wd[:4], r, 1)]
            toks.append({'fill': FILL[hexcol(d['fill'])], 'rect': r, 'label': lab,
                         'w': r[2] - r[0], 'h': r[3] - r[1]})
    bonus['pages'].append({'page': pno + 1, 'tokens': toks, 'text': page.get_text(),
                           'words': [list(w[:5]) for w in words]})
allt = [t for p in bonus['pages'] for t in p['tokens']]
log.check(all(len(t['label']) == 1 and t['label'][0][0] == t['fill'] for t in allt),
          f'bonus: every one of {len(allt)} tokens has a label whose letter matches its fill colour')
log.check(all(close(t['w'], t['h'], 0.05) for t in allt), 'bonus: every token is a circle (equal x and y extent)')

bp1 = bonus['pages'][0]
tk = sorted(bp1['tokens'], key=lambda t: (round(t['rect'][1]), t['rect'][0]))
row_y = sorted({round(centre(t['rect'])[1]) for t in tk})
rows = [[t['label'][0] for t in sorted([t for t in tk if round(centre(t['rect'])[1]) == y], key=lambda t: t['rect'][0])] for y in row_y]
log.note(f'bonus p1 token rows (top to bottom): {rows}')
log.check(rows[0] == ['G', 'B', 'G', 'B'], 'bonus p1: launch card G/B; output two clues G then B')
log.check(rows[1:] == [['R', 'R'], ['R', 'B'], ['B', 'B']], 'bonus p1: table card rows RR, RB, BB')
ws = bp1['words']


def word_x(s, ws):
    return [w[0] for w in ws if w[4] == s]


# L face caption under first launch token
lf = [w for w in ws if w[4] == 'L' and any(x[4] == 'face' and close(x[1], w[1], 1) and x[0] > w[0] for x in ws)]
gtok = [t for t in tk if t['label'] == ['G']]
gtok.sort(key=lambda t: t['rect'][0])
log.check(len(lf) == 1 and abs(centre(gtok[0]['rect'])[0] - (lf[0][0] + 12)) < 15,
          'bonus p1: "L face" caption sits under the G token, "R face" under the B token')
hdr = re.findall(r'(L|R) then (L|R)', bp1['text'])
log.check(hdr == [('L', 'L'), ('L', 'R'), ('R', 'L'), ('R', 'R')], f'bonus p1: table columns {hdr}')

bp2 = bonus['pages'][1]
txt2 = bp2['text']
pairs2 = re.findall(r'\n([123])\n([23])\n', txt2)
log.note(f'bonus p2 prize/ticket rows read from text: {pairs2}')
log.check(pairs2.count(('1', '2')) >= 1, 'bonus p2: prize-ticket rows found')
# Count rows per table by x position
rows_a, rows_b = [], []
num = [w for w in bp2['words'] if w[4] in ('1', '2', '3') and 420 < w[1] < 700]
for w in num:
    (rows_a if w[0] < 300 else rows_b).append(w)


def table_rows(ws_):
    by_y = {}
    for w in ws_:
        by_y.setdefault(round(w[1]), []).append(w)
    return [tuple(w[4] for w in sorted(v, key=lambda w: w[0])) for k, v in sorted(by_y.items())]


ta, tb = table_rows(rows_a), table_rows(rows_b)
want = [('1', '2'), ('1', '3'), ('2', '2'), ('2', '3'), ('3', '2'), ('3', '3')]
log.check(ta == want and tb == want, f'bonus p2: both host tables list all six prize-ticket stories {ta}')
# demo: P has dot, R has star (prize), Host A opens Q
log.check('Host A opens Q' in txt2 and 'input: choose P, prize R' in txt2,
          'bonus p2: demo captions "choose P, prize R" and "Host A opens Q"')
star = [w for w in bp2['words'] if w[4] == '*']
Rlab = [w for w in bp2['words'] if w[4] == 'R' and 220 < w[1] < 260 and w[0] < 300]
log.check(len(star) == 1 and Rlab and abs(star[0][0] - Rlab[0][0]) < 30,
          'bonus p2: prize star is on door R in the input picture')
pic = sorted([w for w in bp2['words'] if 220 < w[1] < 260], key=lambda w: w[0])
inp = [w[4] for w in pic if w[0] < 234 and w[4] != '*']
out = [w[4] for w in pic if w[0] > 283]
log.check(inp == ['P', 'Q', 'R'] and out == ['P', 'empty', 'R'],
          f'bonus p2: input doors {inp}, output doors {out} (Q opened, P and R closed)')
dots = [d for d in doc[1].get_drawings() if d.get('fill') == (0.0, 0.0, 0.0) and (d['rect'][2] - d['rect'][0]) < 6 and d['rect'][1] < 270]
log.check(len(dots) == 2 and all(abs(centre(d['rect'])[0] - centre(w[:4])[0]) < 3 for d, w in zip(sorted(dots, key=lambda d: d['rect'][0]), [w for w in pic if w[4] == 'P'])),
          'bonus p2: the initial-choice dot is under door P in both pictures')

bp3 = bonus['pages'][2]
tk3 = sorted(bp3['tokens'], key=lambda t: (round(t['rect'][1]), t['rect'][0]))
labs3 = [t['label'][0] for t in tk3]
log.note(f'bonus p3 tokens top to bottom: {labs3}')
log.check(labs3 == ['B', 'R', 'R1', 'R2', 'R3', 'B'], 'bonus p3: demo hidden B -> report R; table rows R1, R2, R3, B')
hdr3 = [w[4] for w in sorted(bp3['words'], key=lambda w: w[0]) if w[4] in ('counter', 'H1', 'H2', 'F') and 360 < w[1] < 400]
log.check(hdr3 == ['counter', 'H1', 'H2', 'F'], f'bonus p3: table columns {hdr3}')
log.check('ticket F: flip color' in bp3['text'], 'bonus p3: demo ticket is F (flip)')
slots = [w[4] for w in sorted(bp3['words'], key=lambda w: w[0]) if 640 < w[1] < 670]
log.check(slots == ['1', '2', '3', '4'], f'bonus p3: four numbered slots for the four redesigned tickets {slots}')

geometry['bonus'] = bonus
geometry['catalogue'] = {k: {'colour': v['colour'], 'partner': v['partner']} for k, v in catalogues.items()}


def strip(o):
    if isinstance(o, dict):
        return {k: strip(v) for k, v in o.items() if k not in ('text', 'words')}
    if isinstance(o, list):
        return [strip(v) for v in o]
    if isinstance(o, tuple):
        return [strip(v) for v in o]
    if isinstance(o, float):
        return round(o, 3)
    return o


json.dump(strip(geometry), open(os.path.join(HERE, 'pdf_geometry.json'), 'w'), indent=1)
log.summary()
