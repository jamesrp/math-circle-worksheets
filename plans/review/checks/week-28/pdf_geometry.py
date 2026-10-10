"""Read every disk, wedge, shaded sector and label from the delivered PDFs.

All geometry comes from the vector drawings in the PDFs themselves (pdfplumber),
not from the authors' builders.  Each disk is reported as its ray directions
(degrees clockwise from straight up), ray-number labels, M/V labels, degree
labels and shaded sectors.  The script then compares the drawings with my own
reading of each printed problem (EXPECTED below) and writes everything to
pdf_geometry.json.  A short cross-check confirms that the TikZ sources give
the same ray angles.
"""
import json
import math
import re
from collections import defaultdict

import pdfplumber

from common import PDFS, REFS, TEX, Log, md5, HERE, CM

TOL = 0.6  # degrees


def ang(cx, cy, x, y):
    """Clockwise angle from straight up; y grows downward."""
    a = math.degrees(math.atan2(x - cx, -(y - cy))) % 360
    return 0.0 if a > 359.99 else a


def adiff(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def circles(page):
    out = []
    for c in page.curves:
        w, h = c['x1'] - c['x0'], c['bottom'] - c['top']
        if abs(w - h) > 0.6 or w < 20:
            continue
        if c.get('fill') and not c.get('stroke'):
            continue
        cx, cy, r = (c['x0'] + c['x1']) / 2, (c['top'] + c['bottom']) / 2, w / 2
        # every control/end point must lie inside the bounding circle region
        if len(c['pts']) > 8:
            continue  # polylines (wedges, sectors) are not circles
        out.append((cx, cy, r))
    # deduplicate
    ded = []
    for cc in out:
        if not any(abs(cc[0] - d[0]) < 0.5 and abs(cc[1] - d[1]) < 0.5 for d in ded):
            ded.append(cc)
    return ded


def polygons(page):
    """Filled polylines: (apex, arc start, arc end, n points, grey level)."""
    out = []
    for c in page.curves:
        if len(c['pts']) < 20 or not c.get('fill'):
            continue
        pts = c['pts']
        col = c.get('non_stroking_color')
        if isinstance(col, (list, tuple)):
            col = col[0] if len(col) == 1 else tuple(col)
        out.append({'pts': pts, 'grey': col})
    return out


def wedge_angle(pts):
    ax, ay = pts[0]
    pts = [pts[0]] + [p for p in pts[1:] if math.hypot(p[0] - ax, p[1] - ay) > 0.5]
    a1 = ang(ax, ay, *pts[1])
    a2 = ang(ax, ay, *pts[-1])
    # orientation: sweep from pts[1] to pts[-1] through the middle point
    am = ang(ax, ay, *pts[len(pts) // 2])
    cw = (a2 - a1) % 360
    if (am - a1) % 360 <= cw:
        lo, span = a1, cw
    else:
        lo, span = a2, (a1 - a2) % 360
    radii = [math.hypot(x - ax, y - ay) for x, y in pts[1:]]
    return lo, span, min(radii), max(radii)


def disk_data(page, words):
    discs = []
    for (cx, cy, r) in circles(page):
        rays = defaultdict(lambda: {'from_center': False, 'segments': 0, 'maxlen': 0, 'dash_pattern': False})
        for l in page.lines:
            (x1, y1), (x2, y2) = l['pts'][0], l['pts'][-1]
            d1, d2 = math.hypot(x1 - cx, y1 - cy), math.hypot(x2 - cx, y2 - cy)
            if max(d1, d2) > r + 0.8:
                continue
            if min(d1, d2) < 0.6:
                far = (x2, y2) if d2 > d1 else (x1, y1)
                a = ang(cx, cy, *far)
                key = round(a, 1)
                rays[key]['from_center'] = True
                dash = l.get('dash')
                if dash and dash[0]:
                    rays[key]['dash_pattern'] = True
            else:
                a1, a2 = ang(cx, cy, x1, y1), ang(cx, cy, x2, y2)
                if adiff(a1, a2) > 0.5:
                    continue  # tick marks / boundary-ish segments not radial
                key = round(a1, 1)
            rays[key]['segments'] += 1
            rays[key]['maxlen'] = max(rays[key]['maxlen'], max(d1, d2))
        # merge near-equal keys
        merged = []
        for k in sorted(rays):
            if merged and adiff(merged[-1][0], k) < TOL:
                merged[-1][1]['segments'] += rays[k]['segments']
                merged[-1][1]['from_center'] |= rays[k]['from_center']
                merged[-1][1]['dash_pattern'] |= rays[k]['dash_pattern']
                continue
            merged.append([k, dict(rays[k])])
        ray_list = [{'angle': k, 'dashed': v['segments'] > 1 or not v['from_center'] or v.get('dash_pattern', False)}
                    for k, v in merged]
        # tick marks: short radial segments just outside the circle
        ticks = []
        for l in page.lines:
            (x1, y1), (x2, y2) = l['pts'][0], l['pts'][-1]
            d1, d2 = math.hypot(x1 - cx, y1 - cy), math.hypot(x2 - cx, y2 - cy)
            if r - 1 < min(d1, d2) and max(d1, d2) < r + 5 and abs(d1 - d2) > 1:
                ticks.append(round(ang(cx, cy, x1, y1), 1))
        discs.append({'cx': cx, 'cy': cy, 'r': r, 'rays': ray_list, 'ticks': sorted(set(ticks)),
                      'nums': {}, 'mv': [], 'deg': [], 'name': None, 'shaded': [], 'other': []})
    # assign words
    for w in words:
        x, y = (w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2
        best = None
        for d in discs:
            dist = math.hypot(x - d['cx'], y - d['cy'])
            if best is None or dist < best[0]:
                best = (dist, d)
        if best is None:
            continue
        dist, d = best
        t = w['text']
        a = ang(d['cx'], d['cy'], x, y)
        if dist < d['r'] * 0.97 and t in ('M', 'V', 'MV'):
            if t == 'MV':  # two labels printed touching (guide D diagram)
                d['mv'].append(('M', a, dist, x, y, w))
                d['mv'].append(('V', a, dist, x, y, w))
            else:
                d['mv'].append((t, a, dist, x, y, w))
        elif dist < d['r'] * 0.97 and re.match(r'^\d+(\u25e6|°|◦)?$', t):
            d['deg'].append((int(re.match(r'\d+', t).group()), a))
        elif d['r'] * 0.97 <= dist < d['r'] + 14 and re.match(r'^[1-8]$', t):
            d['nums'][t] = a
        elif re.match(r'^[A-H]$', t) and dist < d['r'] * 1.9 and x < d['cx'] and y < d['cy']:
            if d['name'] is None or dist < d['name'][1]:
                d['name'] = (t, dist)
        else:
            d['other'].append((t, round(a, 1), round(dist / d['r'], 2)))
    for d in discs:
        d['name'] = d['name'][0] if d['name'] else None
    return discs


def finalize(d, poly):
    rays = sorted(r['angle'] for r in d['rays'])
    d['ray_angles'] = rays
    n = len(rays)
    d['sectors'] = [round((rays[(i + 1) % n] - rays[i]) % 360, 2) or 360.0 for i in range(n)] if n else []
    # ray numbers -> ray index
    numbering = {}
    for t, a in d['nums'].items():
        k = min(range(n), key=lambda i: adiff(rays[i], a)) if n else None
        numbering[int(t)] = (k, round(adiff(rays[k], a), 1) if n else None)
    d['numbering'] = numbering
    # M/V labels: nearest ray by angle (labels sit on the ray near the rim)
    labels = {}
    for t, a, dist, x, y, w in d['mv']:
        k = min(range(n), key=lambda i: adiff(rays[i], a))
        if t == 'M' and any(tt == 'V' and ww is w for tt, _, _, _, _, ww in d['mv']):
            # combined "MV" word: split by character positions
            chars = [c for c in w['chars']]
            for c in chars:
                cxx, cyy = (c['x0'] + c['x1']) / 2, (c['top'] + c['bottom']) / 2
                aa = ang(d['cx'], d['cy'], cxx, cyy)
                kk = min(range(n), key=lambda i: adiff(rays[i], aa))
                labels.setdefault(kk, []).append((c['text'], round(adiff(rays[kk], aa), 1)))
            continue
        if t == 'V' and any(tt == 'M' and ww is w for tt, _, _, _, _, ww in d['mv']):
            continue
        labels.setdefault(k, []).append((t, round(adiff(rays[k], a), 1)))
    d['labels'] = labels
    # word in ray-number order when numbers exist, else clockwise from top
    order = list(range(n))
    if numbering and all(i in numbering for i in range(1, n + 1)):
        order = [numbering[i][0] for i in range(1, n + 1)]
    word = ''
    for k in order:
        lab = labels.get(k)
        word += lab[0][0] if lab and len(lab) == 1 else ('?' if not lab else '*')
    d['word'] = word
    # degree labels: sector containing the label angle
    deg = {}
    for v, a in d['deg']:
        for i in range(n):
            if (a - rays[i]) % 360 < (rays[(i + 1) % n] - rays[i]) % 360 or n == 1:
                deg.setdefault(i, []).append(v)
    d['deg_by_sector'] = deg
    # shaded sectors (grey polylines with apex at centre)
    shaded = []
    for p in poly:
        ax, ay = p['pts'][0]
        if math.hypot(ax - d['cx'], ay - d['cy']) < 0.6:
            lo, span, rmin, rmax = wedge_angle(p['pts'])
            k = min(range(n), key=lambda i: adiff(rays[i], lo))
            shaded.append({'sector': k, 'start': round(lo, 1), 'span': round(span, 1),
                           'rmax': round(rmax, 2), 'grey': p['grey']})
    d['shaded'] = shaded
    return d


def extract(key):
    pages = []
    with pdfplumber.open(str(PDFS[key])) as pdf:
        for pn, page in enumerate(pdf.pages):
            words = page.extract_words(return_chars=True)
            poly = polygons(page)
            discs = [finalize(d, poly) for d in disk_data(page, words)]
            discs.sort(key=lambda d: (round(d['cy'] / 20), d['cx']))
            # free wedges: filled polylines whose apex is not a disk centre
            wedges = []
            for p in poly:
                ax, ay = p['pts'][0]
                if any(math.hypot(ax - d['cx'], ay - d['cy']) < 0.6 for d in discs):
                    continue
                lo, span, rmin, rmax = wedge_angle(p['pts'])
                lbl = None
                for w in words:
                    x, y = (w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2
                    if math.hypot(x - ax, y - ay) < rmax and ang(ax, ay, x, y) - lo % 360 >= -1e9:
                        a = ang(ax, ay, x, y)
                        if (a - lo) % 360 <= span and re.match(r'^[A-G]$', w['text']):
                            lbl = w['text']
                wedges.append({'label': lbl, 'span': round(span, 2), 'rmin_cm': round(rmin / CM, 3),
                               'rmax_cm': round(rmax / CM, 3), 'grey': p['grey'],
                               'apex': (round(ax, 1), round(ay, 1))})
            # open polylines (e.g. the half-turn template): report span about lowest edge midpoint
            others = []
            for c in page.curves:
                if len(c['pts']) >= 20 and not c.get('fill'):
                    pts = c['pts']
                    (x0, y0), (x1, y1) = pts[0], pts[-1]
                    others.append({'n': len(pts), 'start': (round(x0, 1), round(y0, 1)),
                                   'end': (round(x1, 1), round(y1, 1)),
                                   'bbox_cm': [round((c['x1'] - c['x0']) / CM, 3), round((c['bottom'] - c['top']) / CM, 3)]})
            pages.append({'page': pn + 1, 'discs': discs, 'wedges': wedges, 'open_curves': others,
                          'words': [w['text'] for w in words]})
    return pages


def slim(d):
    return {k: d[k] for k in ('name', 'r', 'ray_angles', 'sectors', 'numbering', 'word', 'deg_by_sector',
                              'shaded', 'ticks')} | {'r_cm': round(d['r'] / CM, 3)}


# ---------------------------------------------------------------------------
RIGHT = [0.0, 90.0, 180.0, 270.0]
EXPECTED = {
    # my reading of each printed diagram: (page, list of (name, ray angles, word or None))
    'k-1': {
        1: [(None, RIGHT, '????')] * 4,
        2: [('A', RIGHT, 'MMMV'), ('B', RIGHT, 'MMMM'), ('C', RIGHT, 'MVVV'),
            ('D', RIGHT, 'MMVV'), ('E', RIGHT, 'MMVM'), ('F', RIGHT, 'MVMV')],
        3: [(None, RIGHT, 'M???')] * 6,
        4: [('A', RIGHT, 'M?V?'), (None, RIGHT, 'MM??'), (None, RIGHT, 'V?V?'),
            ('B', RIGHT, 'M?V?'), (None, RIGHT, 'MM??'), (None, RIGHT, 'V?V?'),
            ('C', RIGHT, 'M?V?'), (None, RIGHT, 'MM??'), (None, RIGHT, 'V?V?')],
        5: [(None, RIGHT, '????')] * 10,
        6: [('A', RIGHT, 'MMMV'), ('B', RIGHT, 'MMVM'), ('C', RIGHT, 'MVMM'), ('D', RIGHT, 'VMMM'),
            ('E', RIGHT, 'MVVV'), ('F', RIGHT, 'VMVV'), ('G', RIGHT, 'VVMV'), ('H', RIGHT, 'VVVM')],
    },
    'grades-2-3': {
        2: [('A', RIGHT, None), ('B', [0, 45, 135, 225], None), ('C', [0, 60, 180, 300], None),
            ('D', [0, 30, 90, 240], None)],
        3: [('A', RIGHT, '????'), ('B', [0, 45, 135, 225], '????'), ('C', [0, 60, 180, 300], '????'),
            ('D', [0, 30, 90, 240], '????')],
        4: [('A', [0, 90, 180], None), ('B', [0, 60, 180], None), ('C', [0, 30, 180], None),
            ('D', [0, 120, 180], None)],
        5: [(None, RIGHT, '????')] * 10,
        6: [(None, [0], None)] * 4,
    },
    'grades-4-5': {
        1: [('A', RIGHT, '????'), ('B', [0, 45, 135, 225], '????'), ('C', [0, 60, 180, 300], '????'),
            ('D', [0, 30, 90, 240], '????')],
        2: [('A', [0, 120, 240], None), ('B', [0, 60, 120, 180, 270], None),
            ('C', [0, 30, 60, 120, 180, 240, 300], None)],
        3: [('A', [0, 45, 135, 225], None), ('B', [0, 30, 60, 120, 180, 270], None),
            ('C', [0, 30, 60, 90, 150, 240], None), ('D', [0, 45, 90, 135, 180, 225, 270, 315], None)],
        4: [(None, RIGHT, '????')] * 10,
        5: [('A', RIGHT, 'MMMM'), ('B', RIGHT, 'VVVV'), ('C', RIGHT, 'MMVV'), ('D', RIGHT, 'MVMV')],
        6: [(None, [0], None)],
    },
}


def main():
    log = Log()
    out = {}
    log.head('Delivered PDFs equal the reference copies in the source packages')
    for k in PDFS:
        log.check(md5(PDFS[k]) == md5(REFS[k]), f'{PDFS[k].name} == {REFS[k].relative_to(REFS[k].parents[3])}')

    for key in ('k-1', 'grades-2-3', 'grades-4-5'):
        pages = extract(key)
        out[key] = [{'page': p['page'], 'discs': [slim(d) for d in p['discs']], 'wedges': p['wedges'],
                     'open_curves': p['open_curves']} for p in pages]
        log.head(f'{key}: disk diagrams against the problem text')
        for pg, exp in EXPECTED[key].items():
            discs = pages[pg - 1]['discs']
            log.check(len(discs) == len(exp), f'{key} p{pg}: {len(discs)} disks (expected {len(exp)})')
            for d, (name, rays, word) in zip(discs, exp):
                tag = f'{key} p{pg} disk {name or "?"}'
                ok_r = len(d['ray_angles']) == len(rays) and all(adiff(a, b) < TOL for a, b in zip(d['ray_angles'], rays))
                log.check(ok_r, f'{tag}: rays {d["ray_angles"]} == {rays}')
                if name is not None:
                    log.check(d['name'] == name, f'{tag}: letter {d["name"]}')
                if word is not None:
                    log.check(d['word'] == word, f'{tag}: labels read {d["word"]} (expected {word})')
                if d['numbering']:
                    n = len(rays)
                    good = all(d['numbering'].get(i, (None, 99))[0] == i - 1 and d['numbering'][i][1] < 2
                               for i in range(1, n + 1))
                    log.check(good, f'{tag}: ray numbers 1..{n} clockwise from the top ray')
                # labels sit on their rays
                for k, labs in d['labels'].items():
                    for t, off in labs:
                        if off > 2:
                            log.check(False, f'{tag}: label {t} is {off} deg off ray {k + 1}')

    # ---- detailed diagram facts used by check_base.py --------------------
    k1 = out['k-1']
    log.head('K-1 Problem 4 tabs (rectangles with one letter each)')
    with pdfplumber.open(str(PDFS['k-1'])) as pdf:
        p = pdf.pages[3]
        words = p.extract_words()
        rows = defaultdict(list)
        for r in p.rects:
            if 20 < r['x1'] - r['x0'] < 30 and 20 < r['bottom'] - r['top'] < 30:
                inside = [w['text'] for w in words if r['x0'] < (w['x0'] + w['x1']) / 2 < r['x1']
                          and r['top'] < (w['top'] + w['bottom']) / 2 < r['bottom']]
                rows[round(r['top'])].append(''.join(inside))
        tabs = [''.join(sorted(v)) for _, v in sorted(rows.items())]
        out['k-1-p4-tabs'] = tabs
        log.check(tabs == ['MMVVVV', 'MMMVVV', 'MMMMVV'], f'tab rows A,B,C = {tabs}')

    g23 = out['grades-2-3']
    log.head('Grades 2-3 Problem 1 wedges')
    w1 = sorted(g23[0]['wedges'], key=lambda w: w['label'] or '')
    spans = {w['label']: w['span'] for w in w1}
    log.check(spans == {'A': 30.0, 'B': 30.0, 'C': 60.0, 'D': 60.0, 'E': 90.0, 'F': 120.0, 'G': 150.0},
              f'wedge angles {spans}')
    radii = {round(w['rmax_cm'], 2) for w in w1} | {round(w['rmin_cm'], 2) for w in w1}
    log.check(radii == {2.25}, f'all seven wedges have radius {radii} cm (guide: 2.25 cm)')
    tmpl = g23[0]['open_curves']
    log.info(f'half-turn template curves: {tmpl}')
    log.check(any(abs(c['bbox_cm'][0] - 4.5) < 0.02 and abs(c['bbox_cm'][1] - 2.25) < 0.02 for c in tmpl),
              'half-turn template is a semicircle of radius 2.25 cm (width 4.5 cm, height 2.25 cm)')

    log.head('Grades 2-3 Problem 2 shaded sectors')
    for d, nm in zip(g23[1]['discs'], 'ABCD'):
        sh = sorted(s['sector'] for s in d['shaded'])
        log.check(sh == [0, 2], f'disk {nm}: shaded sectors {[s + 1 for s in sh]} (1 and 3), sectors {d["sectors"]}, r={d["r_cm"]} cm')
    log.head('Grades 2-3 Problem 2 sector names A1..D4 sit in sectors 1..4 clockwise from the top ray')
    raw23 = extract('grades-2-3')
    for d, nm in zip(raw23[1]['discs'], 'ABCD'):
        rays = d['ray_angles']
        got = {}
        for t, a, rr in d['other']:
            if re.match(r'^[A-D][1-4]$', t):
                k = [i for i in range(4) if (a - rays[i]) % 360 < (rays[(i + 1) % 4] - rays[i]) % 360][0]
                got[t] = k + 1
        want = {f'{nm}{i}': i for i in range(1, 5)}
        log.check(got == want, f'disk {nm}: {got}')
    log.head('Guide p12 six-wedge samples: ray numbers 1..6 clockwise from top')
    for d in extract('guide')[12]['discs']:
        ok = all(d['numbering'].get(i, (None, 99))[0] == i - 1 and d['numbering'][i][1] < 3 for i in range(1, 7))
        log.check(ok, f'rays {d["ray_angles"]} numbering {d["numbering"]}')

    log.head('Grades 2-3 Problem 4 ticks every 30 degrees')
    for d, nm in zip(g23[3]['discs'], 'ABCD'):
        log.check(d['ticks'] == [float(30 * i) for i in range(12)], f'disk {nm}: ticks {d["ticks"]}')
    log.head('Grades 2-3 Problem 6 wedges match the 2.4 cm disks')
    w6 = g23[5]['wedges']
    lab6 = sorted((w['label'], w['span']) for w in w6)
    log.check(lab6 == [('A', 30.0), ('A', 30.0), ('B', 60.0), ('B', 60.0), ('C', 90.0), ('C', 90.0)], f'wedges {lab6}')
    log.check({round(w['rmax_cm'], 2) for w in w6} == {2.4} and all(abs(d['r_cm'] - 2.4) < 0.01 for d in g23[5]['discs']),
              'wedge radius 2.4 cm = disk radius 2.4 cm')

    g45 = out['grades-4-5']
    log.head('Grades 4-5 degree labels sit in sectors of that size')
    for pg in (1, 2, 3):
        for d in g45[pg - 1]['discs']:
            lab = d['deg_by_sector']
            ok = all(lab.get(i) == [round(s)] for i, s in enumerate(d['sectors']))
            log.check(ok, f'4-5 p{pg} disk {d["name"]}: labels {dict(sorted(lab.items()))} vs drawn {d["sectors"]}')
    log.head('Grades 4-5 Problem 3 shading = odd-position sectors')
    for d in g45[2]['discs']:
        sh = sorted(s['sector'] for s in d['shaded'])
        log.check(sh == list(range(0, len(d['sectors']), 2)), f'disk {d["name"]}: shaded {[s + 1 for s in sh]}')

    # ---- circles are circles (equal scaling) ------------------------------
    log.head('Equal scaling: every disk outline has a square bounding box')
    for key in ('k-1', 'grades-2-3', 'grades-4-5'):
        with pdfplumber.open(str(PDFS[key])) as pdf:
            worst = 0
            for page in pdf.pages:
                for c in page.curves:
                    w, h = c['x1'] - c['x0'], c['bottom'] - c['top']
                    if len(c['pts']) <= 8 and w > 20:
                        worst = max(worst, abs(w - h))
            log.check(worst < 0.05, f'{key}: max |width-height| of disk outlines = {worst:.3f} pt')

    # ---- guide diagrams -------------------------------------------------------
    log.head('Guide diagrams')
    gp = extract('guide')
    out['guide'] = [{'page': p['page'], 'discs': [slim(d) for d in p['discs']]} for p in gp]
    # PDF page 4 = printed p3 witnesses; page 8 = printed p7 catalog; page 12 = p11; page 13 = p12
    w3 = [d['word'] for d in gp[3]['discs']]
    log.check(w3 == ['VVVM', 'VVMV', 'VMVV', 'MVVV'], f'guide p3 four witnesses read {w3}')
    cat = [(d['name'], d['word']) for d in gp[7]['discs']]
    log.info(f'guide p7 catalog read {cat}')
    log.check([w for _, w in cat] == ['MMMV', 'MMVM', 'MVMM', 'VMMM', 'MVVV', 'VMVV', 'VVMV', 'VVVM'],
              'guide p7 catalog disks A-H carry the words printed beneath them')
    p11 = gp[11]['discs']
    for d in p11:
        log.info(f'guide p11 disk rays {d["ray_angles"]} word {d["word"]} dashed {[r["angle"] for r in d["rays"] if r["dashed"]]}')
    log.check([d['word'] for d in p11[:4]] == ['VVVM', '????', 'VVVM', 'MVVV'],
              'guide p11 P3 witnesses: A VVVM, B unlabeled, C VVVM, D MVVV')
    log.check([d['ray_angles'] for d in p11[:4]] == [RIGHT, [0, 45, 135, 225], [0, 60, 180, 300], [0, 30, 90, 240]],
              'guide p11 P3 disks have the printed ray angles')
    log.check([d['ray_angles'] for d in p11[4:8]] == [RIGHT, [0, 60, 180, 300], [0, 30, 180, 330], [0, 120, 180, 240]],
              'guide p11 P4 completions: rays incl. added 270, 300, 330, 240')
    added = [[r['angle'] for r in d['rays'] if r['dashed']] for d in p11[4:8]]
    log.check(added == [[270.0], [300.0], [330.0], [240.0]], f'guide p11 dashed (added) rays {added}')
    p12 = gp[12]['discs']
    r12 = [d['ray_angles'] for d in p12]
    log.check(r12 == [[0, 30, 60, 120, 180, 270], [0, 30, 60, 120, 210, 300], [0, 30, 60, 150, 210, 270],
                      [0, 30, 60, 150, 240, 300]], f'guide p12 six-wedge samples rays {r12}')

    # ---- TikZ sources agree with the PDFs ---------------------------------------
    log.head('TikZ sources give the same ray angles as the PDFs')
    for key in ('k-1', 'grades-2-3', 'grades-4-5'):
        tex = TEX[key].read_text()
        pages_src = tex.split('\\newpage')
        mismatches = 0
        for pn, chunk in enumerate(pages_src):
            rays_src = defaultdict(list)
            for x1, y1, x2, y2 in re.findall(r'\\draw\[black,line width=\.65pt\] \(([\d.]+),([\d.]+)\) -- \(([\d.]+),([\d.]+)\);', chunk):
                x1, y1, x2, y2 = map(float, (x1, y1, x2, y2))
                rays_src[(x1, y1)].append(round(ang(x1, y1, x2, y2), 1))
            pdf_discs = out[key][pn]['discs'] if pn < len(out[key]) else []
            src_sets = sorted(sorted(v) for v in rays_src.values())
            pdf_sets = sorted(sorted(round(a, 1) for a in d['ray_angles']) for d in pdf_discs if d['ray_angles'])
            same = len(src_sets) == len(pdf_sets) and all(
                len(a) == len(b) and all(adiff(x, y) < 0.3 for x, y in zip(a, b)) for a, b in zip(src_sets, pdf_sets))
            if not same:
                mismatches += 1
                log.info(f'{key} page {pn + 1}: src {src_sets} pdf {pdf_sets}')
        log.check(mismatches == 0, f'{key}: TikZ ray sets equal PDF ray sets on every page')

    (HERE / 'pdf_geometry.json').write_text(json.dumps(out, indent=1, default=str))
    log.done()


if __name__ == '__main__':
    main()
