"""Read the drawn rings, beads, start arrows and cards straight out of the
delivered Week 33 PDFs (PyMuPDF), and check the diagrams.

Checks:
  * every circle is drawn with equal x/y scaling (square bounding box);
  * beads of each ring lie on its guide circle, equally spaced, first bead at
    12 o'clock (regular n-gon positions);
  * the start arrow points at a bead; the curved direction arrow runs clockwise;
  * bead letters agree with fills (A white, B grey) in the base packets;
  * the launch example's three readouts are what the printed labels say;
  * the 8- and 32-card pages show every word exactly once, in the order the
    guide's card numbers assume (binary order, A before B);
  * each card's reading arrow points left-to-right (from the 'start' label);
  * bonus rings: words read clockwise from the top bead; window example.

Writes pdf_geometry.json next to this script; prints a log (saved as
pdf_extract.out).
"""
import json
import math
import os
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import PDFS, HERE, Log, words, rotations  # noqa: E402

CM = 72 / 2.54
log = Log()


def is_circle(d):
    return len(d['items']) == 4 and all(it[0] == 'c' for it in d['items'])


def grey(c):
    return c is not None and abs(c[0] - c[1]) < .01 and abs(c[1] - c[2]) < .01 and .3 < c[0] < .9


def circ(d):
    r = d['rect']
    return {'cx': (r.x0 + r.x1) / 2, 'cy': (r.y0 + r.y1) / 2,
            'rx': (r.x1 - r.x0) / 2, 'ry': (r.y1 - r.y0) / 2}


def angle(cx, cy, x, y):
    """Math-convention angle in degrees (y up) of (x,y) about (cx,cy)."""
    return math.degrees(math.atan2(-(y - cy), x - cx))


def letters_near(wordsl, x, y, rad):
    out = [w for w in wordsl if w[4] in ('A', 'B', 'C')
           and math.hypot((w[0] + w[2]) / 2 - x, (w[1] + w[3]) / 2 - y) < rad]
    return out


def analyse_page(doc, pno, band):
    page = doc[pno]
    dr = page.get_drawings()
    wl = page.get_text('words')
    circles = [d for d in dr if is_circle(d)]
    guides = [circ(d) for d in circles if d['fill'] is None and grey(d['color'])]
    beads = []
    for d in circles:
        if d['fill'] is None:
            continue
        c = circ(d)
        c['fill'] = 'grey' if grey(d['fill']) else ('white' if d['fill'][0] > .99 else str(d['fill']))
        beads.append(c)
    # equal scaling of every circle drawn on the page
    for c in guides + beads:
        if abs(c['rx'] - c['ry']) > 0.05:
            log.check(False, f'{band} p{pno+1}: circle at ({c["cx"]:.1f},{c["cy"]:.1f}) not round {c["rx"]:.2f}x{c["ry"]:.2f}')
    # arrowheads (two-curve paths) and their tips; straight shafts; arcs
    heads = []
    for d in dr:
        its = d['items']
        if len(its) == 2 and all(i[0] == 'c' for i in its) and d['rect'].width < 8 and d['rect'].height < 8:
            heads.append((its[0][4].x, its[0][4].y))
    shafts = [d['items'][0] for d in dr if len(d['items']) == 1 and d['items'][0][0] == 'l']
    arcs = [d['items'][0] for d in dr if len(d['items']) == 1 and d['items'][0][0] == 'c']

    def tip_of(p, q):
        """Return (tip, tail) for segment endpoints p, q using arrowheads."""
        best = None
        for h in heads:
            for a, b in ((p, q), (q, p)):
                dd = math.hypot(h[0] - a.x, h[1] - a.y)
                if best is None or dd < best[0]:
                    best = (dd, a, b)
        if best and best[0] < 3:
            return best[1], best[2]
        return None, None

    rings = []
    used = set()
    for g in guides:
        rb = [b for b in beads if abs(math.hypot(b['cx'] - g['cx'], b['cy'] - g['cy']) - g['rx']) < 0.5]
        for b in rb:
            used.add((round(b['cx'], 2), round(b['cy'], 2)))
        n = len(rb)
        angs = [angle(g['cx'], g['cy'], b['cx'], b['cy']) for b in rb]
        # order clockwise from 12 o'clock: decreasing math angle starting at 90
        order = sorted(range(n), key=lambda i: (90.5 - angs[i]) % 360)
        rb = [rb[i] for i in order]
        angs = [angs[i] for i in order]
        steps = [((angs[i] - angs[(i + 1) % n]) % 360) for i in range(n)]
        radial = [math.hypot(b['cx'] - g['cx'], b['cy'] - g['cy']) for b in rb]
        lets = []
        for b in rb:
            L = letters_near(wl, b['cx'], b['cy'], b['rx'])
            lets.append(L[0][4] if L else '-')
        # start arrow: a straight shaft whose tip lands near a bead of this ring
        start = None
        for s in shafts:
            tip, tail = tip_of(s[1], s[2])
            if tip is None:
                continue
            for i, b in enumerate(rb):
                if math.hypot(tip.x - b['cx'], tip.y - b['cy']) < b['rx'] + 6:
                    start = i
        # direction arc: a single-curve path ending in an arrowhead near this ring
        direction = None
        for a in arcs:
            tip, tail = tip_of(a[1], a[4])
            if tip is None:
                continue
            rt = math.hypot(tip.x - g['cx'], tip.y - g['cy'])
            rl = math.hypot(tail.x - g['cx'], tail.y - g['cy'])
            if g['rx'] < rt < g['rx'] + 1.0 * CM and g['rx'] < rl < g['rx'] + 1.0 * CM:
                at = angle(g['cx'], g['cy'], tip.x, tip.y)
                al = angle(g['cx'], g['cy'], tail.x, tail.y)
                direction = 'clockwise' if (al - at) % 360 < 180 else 'counterclockwise'
        rings.append({
            'page': pno + 1, 'center': [g['cx'], g['cy']], 'radius_cm': g['rx'] / CM,
            'n': n, 'bead_radius_cm': [b['rx'] / CM for b in rb][:1],
            'first_bead_angle': angs[0] if n else None,
            'step_angles': steps, 'radial_spread_pt': (max(radial) - min(radial)) if n else 0,
            'letters': ''.join(lets), 'fills': [b['fill'] for b in rb],
            'start_index': start, 'direction': direction,
            'adjacent_center_mm': (2 * g['rx'] * math.sin(math.pi / n) / CM * 10) if n else None,
            'bead_diameter_mm': (2 * rb[0]['rx'] / CM * 10) if n else None,
        })
    # cards: four-segment rectangles with beads inside in one row
    cards = []
    for d in dr:
        its = d['items']
        if len(its) == 4 and all(i[0] == 'l' for i in its) and d['fill'] is None:
            r = d['rect']
            inside = [b for b in beads if r.x0 < b['cx'] < r.x1 and r.y0 < b['cy'] < r.y1]
            if not inside:
                continue
            inside.sort(key=lambda b: b['cx'])
            ys = {round(b['cy'], 1) for b in inside}
            lets = []
            for b in inside:
                L = letters_near(wl, b['cx'], b['cy'], b['rx'])
                lets.append(L[0][4] if L else '-')
            nums = [w[4] for w in wl if w[4].isdigit() and r.x0 < (w[0] + w[2]) / 2 < r.x1 and r.y0 < (w[1] + w[3]) / 2 < r.y1]
            st = [w for w in wl if w[4] == 'start' and r.x0 < (w[0] + w[2]) / 2 < r.x1 and r.y0 < (w[1] + w[3]) / 2 < r.y1]
            arrow = None
            for s in shafts:
                if r.x0 < s[1].x < r.x1 and r.y0 < s[1].y < r.y1:
                    tip, tail = tip_of(s[1], s[2])
                    if tip is not None:
                        arrow = 'right' if tip.x > tail.x else 'left'
            start_over_first = bool(st) and abs((st[0][0] + st[0][2]) / 2 - inside[0]['cx']) < 3
            cards.append({'page': pno + 1, 'rect': [r.x0, r.y0, r.x1, r.y1],
                          'one_row': len(ys) == 1, 'letters': ''.join(lets),
                          'fills': [b['fill'] for b in inside], 'num': nums[0] if nums else None,
                          'arrow': arrow, 'start_over_first': start_over_first})
    return rings, cards


def fill_ok(letters, fills):
    return all((l == 'A' and f == 'white') or (l == 'B' and f == 'grey') for l, f in zip(letters, fills))


out = {}
for band in ('k-1', 'grades-2-3', 'grades-4-5'):
    doc = pymupdf.open(PDFS[band])
    out[band] = {'pages': len(doc), 'rings': [], 'cards': []}
    for pno in range(len(doc)):
        rings, cards = analyse_page(doc, pno, band)
        out[band]['rings'] += rings
        out[band]['cards'] += cards
    print(f'\n== {band}: {len(doc)} pages, {len(out[band]["rings"])} rings, {len(out[band]["cards"])} cards')
    for r in out[band]['rings']:
        n = r['n']
        reg = all(abs(s - 360 / n) < 0.2 for s in r['step_angles']) and abs(r['first_bead_angle'] - 90) < 0.2 and r['radial_spread_pt'] < 0.3
        log.check(reg, f'{band} p{r["page"]}: {n}-bead ring r={r["radius_cm"]:.2f}cm regular (steps {sorted(set(round(s,2) for s in r["step_angles"]))}), first bead at 12 o\'clock')
        log.check(r['start_index'] is not None, f'{band} p{r["page"]}: start arrow points at bead index {r["start_index"]} (0 = top)')
        log.check(r['direction'] == 'clockwise', f'{band} p{r["page"]}: direction arc is {r["direction"]}')
        if n:
            log.check(r['adjacent_center_mm'] > r['bead_diameter_mm'], f'{band} p{r["page"]}: beads do not overlap (centres {r["adjacent_center_mm"]:.1f} mm apart, bead {r["bead_diameter_mm"]:.1f} mm)')
        if set(r['letters']) != {'-'}:
            log.check(fill_ok(r['letters'], r['fills']), f'{band} p{r["page"]}: letters {r["letters"]} agree with fills')
            word = r['letters']
            s = r['start_index']
            ro = word[s:] + word[:s]
            r['readout'] = ro
            print(f'     launch ring word from top = {word}; start at bead {s}; clockwise readout = {ro}')
    # launch labels under the three example rings (AAB, ABA, BAA)
    doc0 = doc[0]
    labs = [w for w in doc0.get_text('words') if w[4] in ('AAB', 'ABA', 'BAA')]
    labs.sort(key=lambda w: w[0])
    ex = sorted([r for r in out[band]['rings'] if r['page'] == 1 and r['n'] == 3 and 'readout' in r], key=lambda r: r['center'][0])
    log.check([w[4] for w in labs] == [r['readout'] for r in ex],
              f'{band} launch: printed labels {[w[4] for w in labs]} = computed readouts {[r["readout"] for r in ex]}')
    log.check(len({r['letters'] for r in ex}) == 1, f'{band} launch: all three pictures show the same fixed ring ({ex[0]["letters"]})')
    # cards
    for npg, length in ((None, 3), (None, 5)):
        cs = [c for c in out[band]['cards'] if len(c['letters']) == length]
        if not cs:
            continue
        cs.sort(key=lambda c: int(c['num']))
        expected = words('AB', length)
        got = [c['letters'] for c in cs]
        log.check(got == expected, f'{band}: {len(cs)} {length}-bead cards; card k shows word k in A<B binary order (all {2**length} words once)')
        log.check(all(c['one_row'] and c['arrow'] == 'right' and c['start_over_first'] for c in cs),
                  f'{band}: every {length}-bead card has one row, "start" above the first bead and a left-to-right arrow')
        log.check(all(fill_ok(c['letters'], c['fills']) for c in cs), f'{band}: every {length}-bead card letter agrees with its fill')
        log.check([int(c['num']) for c in cs] == list(range(1, 2 ** length + 1)), f'{band}: card numbers 1..{2**length}')

# --- bonus companion ---------------------------------------------------------
doc = pymupdf.open(PDFS['bonus'])
out['bonus'] = {'pages': len(doc), 'rings': []}
print(f'\n== bonus: {len(doc)} pages')
for pno in range(len(doc)):
    page = doc[pno]
    dr = page.get_drawings()
    wl = page.get_text('words')
    circles = [d for d in dr if is_circle(d)]
    guides = [circ(d) for d in circles if d['fill'] is None and grey(d['color'])]
    beads = [circ(d) for d in circles if d['fill'] is not None]
    for c in guides + beads:
        if abs(c['rx'] - c['ry']) > 0.05:
            log.check(False, f'bonus p{pno+1}: circle not round')
    for g in guides:
        rb = [b for b in beads if abs(math.hypot(b['cx'] - g['cx'], b['cy'] - g['cy']) - g['rx']) < 0.5]
        n = len(rb)
        angs = [angle(g['cx'], g['cy'], b['cx'], b['cy']) for b in rb]
        order = sorted(range(n), key=lambda i: (90.5 - angs[i]) % 360)
        rb = [rb[i] for i in order]
        angs = [angs[i] for i in order]
        steps = [((angs[i] - angs[(i + 1) % n]) % 360) for i in range(n)]
        lets = []
        for b in rb:
            L = letters_near(wl, b['cx'], b['cy'], b['rx'])
            lets.append(L[0][4] if L else '-')
        # label under ring (a..f)
        lab = [w[4] for w in wl if w[4] in 'abcdef' and len(w[4]) == 1
               and abs((w[0] + w[2]) / 2 - g['cx']) < 5 and 0 < (w[1] - g['cy']) < g['rx'] + 30]
        reg = all(abs(s - 360 / n) < 0.2 for s in steps) and abs(angs[0] - 90) < 0.2
        rec = {'page': pno + 1, 'n': n, 'radius_cm': g['rx'] / CM, 'letters': ''.join(lets),
               'label': lab[0] if lab else None, 'regular': reg,
               'bead_diameter_mm': 2 * rb[0]['rx'] / CM * 10,
               'adjacent_center_mm': 2 * g['rx'] * math.sin(math.pi / n) / CM * 10}
        out['bonus']['rings'].append(rec)
        log.check(reg, f'bonus p{pno+1}: {n}-ring r={rec["radius_cm"]:.2f}cm regular, first spot at 12 o\'clock; '
                       f'spot {rec["bead_diameter_mm"]:.1f} mm, adjacent centres {rec["adjacent_center_mm"]:.1f} mm; '
                       f'label={rec["label"]} letters={rec["letters"]}')
    if pno == 3:
        # window example: five beads not on a grey guide circle
        lone = [b for b in beads if b['rx'] < 10]
        cx = sum(b['cx'] for b in lone) / len(lone)
        cy = sum(b['cy'] for b in lone) / len(lone)
        angs = [angle(cx, cy, b['cx'], b['cy']) for b in lone]
        order = sorted(range(len(lone)), key=lambda i: (90.5 - angs[i]) % 360)
        lets = ''
        for i in order:
            L = letters_near(wl, lone[i]['cx'], lone[i]['cy'], lone[i]['rx'])
            lets += L[0][4] if L else '-'
        st = [w for w in wl if w[4] == 'start'][0]
        sx, sy = st[2], (st[1] + st[3]) / 2
        near = min(order, key=lambda i: math.hypot(lone[i]['cx'] - sx, lone[i]['cy'] - sy))
        sidx = order.index(near)
        win = (lets[sidx:] + lets[:sidx])[:3]
        out['bonus']['window_example'] = {'word_from_top': lets, 'start_index': sidx, 'first_window': win}
        log.check(win == 'BAB', f'bonus p4 window example: ring {lets} (clockwise from top), start at index {sidx}; first window {win} (page shows BAB)')
        log.note(f'bonus p4 window example: start bead is the last bead in drawing order, so B-A-B crosses the top-of-list gap; '
                 f'its 3-windows are {[ ((lets[sidx:]+lets[:sidx])*2)[i:i+3] for i in range(5)]}')

with open(os.path.join(HERE, 'pdf_geometry.json'), 'w') as f:
    json.dump(out, f, indent=1)
log.summary()
