"""Read the printed data of the delivered Week 84 student PDF.

For every page: header, footer, problem labels, every stroked box (solid or
dashed) with its size in inches and the words and coloured disks inside it.
Writes pdf_geometry.json (used by check_math.py) and pdf_extract.out.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, PDFS, Log, colour_name, fitz  # noqa: E402

log = Log('Week 84 student PDF: printed data')
doc = fitz.open(PDFS['students'])
pages = []


def inside(r, x, y, pad=0.5):
    return r[0] - pad <= x <= r[2] + pad and r[1] - pad <= y <= r[3] + pad


def lines_of(words):
    """Group words into printed lines (same baseline), left to right."""
    rows = []
    for w in sorted(words, key=lambda w: (round(w[3]), w[0])):
        if rows and abs(rows[-1][0] - w[3]) < 2.5:
            rows[-1][1].append(w)
        else:
            rows.append([w[3], [w]])
    return [' '.join(x[4] for x in sorted(r[1], key=lambda w: w[0])) for r in rows]


for pno, page in enumerate(doc, start=1):
    words = page.get_text('words')  # x0,y0,x1,y1,word,block,line,wno
    H = page.rect.height
    header = ' '.join(w[4] for w in words if w[3] < 40)
    footer = ' '.join(w[4] for w in words if w[1] > H - 50)
    body = [w for w in words if 40 <= w[3] and w[1] <= H - 50]
    probs = re.findall(r'Problem (\d+):', ' '.join(w[4] for w in body))
    boxes, disks = [], []
    for d in page.get_drawings():
        r = [round(v, 2) for v in d['rect']]
        w, h = r[2] - r[0], r[3] - r[1]
        if d.get('fill') is not None and d.get('color') is None and 8 < w < 80 and abs(w - h) < 0.6:
            disks.append({'cx': round((r[0] + r[2]) / 2, 2), 'cy': round((r[1] + r[3]) / 2, 2),
                          'diam_in': round(w / 72, 3), 'colour': colour_name(d['fill'])})
        elif d.get('color') is not None and w > 50 and h > 20:
            dashes = d.get('dashes') or ''
            boxes.append({'rect': r, 'w_in': round(w / 72, 3), 'h_in': round(h / 72, 3),
                          'dashed': bool(re.search(r'\[\s*[\d.]', str(dashes)))})
    # attach the white letter printed on each disk
    for dk in disks:
        dk['letter'] = ''.join(w[4] for w in words
                               if abs((w[0] + w[2]) / 2 - dk['cx']) < 6 and abs((w[1] + w[3]) / 2 - dk['cy']) < 12
                               and w[4] in ('B', 'R'))
    for b in boxes:
        bw = [w for w in words if inside(b['rect'], (w[0] + w[2]) / 2, (w[1] + w[3]) / 2)]
        b['lines'] = lines_of(bw)
        b['disks'] = sorted([dk for dk in disks if inside(b['rect'], dk['cx'], dk['cy'])],
                            key=lambda dk: (dk['cy'], dk['cx']))
        # digit labels printed directly under the disks (position numbers)
        # (skip the box title line, e.g. "Deal 1", printed within 20 pt of the top edge)
        b['labels'] = [w[4] for w in sorted(bw, key=lambda w: w[0])
                       if w[4] in ('1', '2', '3') and (w[1] + w[3]) / 2 > b['rect'][1] + 20]
    boxes.sort(key=lambda b: (round(b['rect'][1]), b['rect'][0]))
    pages.append({'page': pno, 'header': header, 'footer': footer, 'problems': probs,
                  'size_in': [round(page.rect.width / 72, 2), round(H / 72, 2)],
                  'body_lines': lines_of(body), 'boxes': boxes,
                  'disks_outside_boxes': [dk for dk in disks
                                          if not any(inside(b['rect'], dk['cx'], dk['cy']) for b in boxes)]})

for p in pages:
    log(f"\n--- page {p['page']}  ({p['size_in'][0]} x {p['size_in'][1]} in)")
    log('header:', p['header'])
    log('footer:', p['footer'])
    log('problem labels:', p['problems'] or '-')
    for b in p['boxes']:
        dk = ''.join(d['colour'] + ('' if d['letter'] == d['colour'] else '?' + d['letter']) for d in b['disks'])
        log(f"  box {'dashed' if b['dashed'] else 'solid '} {b['w_in']:.2f} x {b['h_in']:.2f} in"
            f" at ({b['rect'][0]:.0f},{b['rect'][1]:.0f})  disks={dk or '-'}  text={' | '.join(b['lines'])}")

json.dump(pages, open(os.path.join(HERE, 'pdf_geometry.json'), 'w'), indent=1)
log.write(os.path.join(HERE, 'pdf_extract.out'))
