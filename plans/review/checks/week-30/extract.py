"""Read every diagram back out of the three base student PDFs.

For each page: problem headings, weight cards (printed number, dot count, and
whether any dot touches the card border), balance boards (left/right pans, the
printed target, any weight disks drawn in each pan), target-number strips,
small text labels, ruled answer lines.  Each element is assigned to the
problem whose heading is the last one above it ('launch' before Problem 1).
Output: extracted.json, extract.out
"""
import json
import os
import re
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, PDF, Log  # noqa: E402

L = Log('extract.out')


def inside(word, r, pad=0.5):
    x0, y0, x1, y1 = word[:4]
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return r[0] - pad <= cx <= r[2] + pad and r[1] - pad <= cy <= r[3] + pad


def page_items(page):
    drs = page.get_drawings()
    words = page.get_text('words')
    num = [w for w in words if re.fullmatch(r'\d+', w[4])]
    cards, pans, circles, strips, rules, grays = [], [], [], [], [], []
    dots = []
    for d in drs:
        r = d['rect']
        kinds = [i[0] for i in d['items']]
        w, h = r.width, r.height
        if d['type'] == 'f' and w < 4.5 and h < 4.5:
            dots.append(r)
        elif d['type'] == 's' and len(kinds) == 8 and 60 < w < 90 and 55 < h < 70:
            cards.append(r)
        elif d['type'] == 's' and len(kinds) == 8 and 200 < w < 240 and 80 < h < 95:
            pans.append(r)
        elif d['type'] == 's' and kinds == ['c'] * 4 and 40 < w < 50:
            circles.append(r)
        elif d['type'] == 's' and kinds == ['l'] * 4 and 45 < w < 56 and 30 < h < 38:
            strips.append(r)
        elif d['type'] == 's' and kinds == ['l'] and w > 400 and h < 1:
            rules.append(r)
        elif d['type'] == 'fs' and 55 < w < 70 and 65 < h < 76:
            grays.append(r)
    heads = []
    for i, wd in enumerate(words):
        if wd[4] == 'Problem' and i + 1 < len(words) and re.fullmatch(r'\d+:', words[i + 1][4]):
            heads.append((wd[1], int(words[i + 1][4][:-1])))
    heads.sort()

    def owner(y):
        o = 'launch'
        for hy, n in heads:
            if y >= hy - 1:
                o = n
        return o

    items = []
    for r in cards:
        lab = [w[4] for w in num if inside(w, r) and w[1] < r.y0 + 25]
        ds = [q for q in dots if r.x0 <= (q.x0 + q.x1) / 2 <= r.x1 and r.y0 <= (q.y0 + q.y1) / 2 <= r.y1]
        touch = [round(r.y1 - q.y1, 2) for q in ds if r.y1 - q.y1 < 1.0]
        items.append(dict(kind='card', y=r.y0, x=r.x0, label=lab, dots=len(ds),
                          bottom_gap_pt=round(min(r.y1 - q.y1 for q in ds), 2) if ds else None,
                          dot_touches_border=bool(touch)))
    pans.sort(key=lambda r: (round(r.y0), r.x0))
    rows = {}
    for r in pans:
        rows.setdefault(round(r.y0), []).append(r)
    for y, rs in rows.items():
        rs.sort(key=lambda r: r.x0)
        left, right = rs[0], rs[1] if len(rs) > 1 else None
        g = [q for q in grays if inside((q.x0, q.y0, q.x1, q.y1), left)]
        tgt = [w[4] for w in num if g and inside(w, g[0])]
        has_target_word = any(w[4] == 'target' and inside(w, left) for w in words)

        def disks(pan):
            out = []
            for c in circles:
                if pan and inside((c.x0, c.y0, c.x1, c.y1), pan):
                    out.append([w[4] for w in num if inside(w, c)])
            return out
        eq = [w for w in words if w[4] == '=' and left.x1 < (w[0] + w[2]) / 2 < (right.x0 if right else 999)
              and left.y0 < (w[1] + w[3]) / 2 < left.y1]
        items.append(dict(kind='board', y=left.y0, target=tgt, target_word=has_target_word,
                          left_disks=disks(left), right_disks=disks(right),
                          right_pan=right is not None, equals=len(eq),
                          left_size=[round(left.width, 1), round(left.height, 1)],
                          right_size=[round(right.width, 1), round(right.height, 1)] if right else None))
    for r in strips:
        items.append(dict(kind='strip', y=r.y0, x=r.x0, label=[w[4] for w in num if inside(w, r)]))
    for r in rules:
        items.append(dict(kind='rule', y=r.y0))
    # small free-standing kit labels (e.g. "1 and 2", "1, 3, 8") at the left margin
    lines = {}
    for w in words:
        if w[0] < 45 and not w[4].startswith('Problem') and not w[4].startswith('Week') \
                and not w[4].startswith('Bellingham') and not w[4].startswith('Keep') \
                and not w[4].startswith('weight') and not w[4].startswith('Target'):
            lines.setdefault((w[5], w[6]), []).append(w)
    for key, ws in lines.items():
        line = [w for w in words if (w[5], w[6]) == key]
        txt = ' '.join(w[4] for w in line)
        if re.fullmatch(r'[\d ,and]+', txt):
            items.append(dict(kind='label', y=line[0][1], text=txt))
    for it in items:
        it['problem'] = owner(it['y'])
    items.sort(key=lambda it: (it['y'], it.get('x', 0)))
    return heads, items


def main():
    out = {}
    for band in ('K', '23', '45'):
        doc = pymupdf.open(PDF[band])
        out[band] = []
        for pno, page in enumerate(doc, 1):
            heads, items = page_items(page)
            out[band].append(dict(page=pno, heads=[n for _, n in heads], items=items))
            L.out(f'== {band} p.{pno}: problems {[n for _, n in heads]}')
            for it in items:
                if it['kind'] == 'card':
                    L.out(f"  P{it['problem']} card label={it['label']} dots={it['dots']} "
                          f"min gap dot->bottom border={it['bottom_gap_pt']}pt")
                elif it['kind'] == 'board':
                    L.out(f"  P{it['problem']} board target={it['target']} left disks={it['left_disks']} "
                          f"right disks={it['right_disks']} right pan={it['right_pan']} '='x{it['equals']} "
                          f"sizes {it['left_size']} {it['right_size']}")
                elif it['kind'] == 'strip':
                    L.out(f"  P{it['problem']} strip box {it['label']}")
                elif it['kind'] == 'label':
                    L.out(f"  P{it['problem']} label '{it['text']}'")
            nr = {}
            for it in items:
                if it['kind'] == 'rule':
                    nr[it['problem']] = nr.get(it['problem'], 0) + 1
            if nr:
                L.out(f'  ruled lines per problem: {nr}')
    with open(os.path.join(HERE, 'extracted.json'), 'w') as f:
        json.dump(out, f, indent=1)
    L.save()


if __name__ == '__main__':
    main()
