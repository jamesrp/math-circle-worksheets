#!/usr/bin/env python3
"""Week 51 diagram check: read the delivered PDFs and compare every printed
range band, ruler, comparison picture, join, answer box and bonus diagram with
my own transcription of the rendered pages.

Run from anywhere:  python3 check_diagrams.py  (output also saved to
out_check_diagrams.txt next to this script).
"""
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pdfgeom as g  # noqa: E402

OUT = []
FAIL = []


def say(s=''):
    OUT.append(s)
    print(s)


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        say('  ** MISMATCH: ' + msg)


def r2(v):
    return round(v + 0.0, 2)


# ---------------------------------------------------------------- helpers
def text_centre(t, ot1=True):
    w = (0.5 if ot1 else 0.556) * t['size'] * len(t['text'])
    return t['x'] + w / 2


def find_rulers(page, ot1=True, min_len_mm=25):
    """Horizontal stroked lines carrying >= 7 short vertical ticks."""
    out = []
    segs = page['strokes']
    for s in segs:
        (x0, y0), (x1, y1) = s['p'], s['q']
        if abs(y0 - y1) > 0.01 or g.mm(abs(x1 - x0)) < min_len_mm:
            continue
        xa, xb = sorted((x0, x1))
        ticks = []
        for t in segs:
            (u0, v0), (u1, v1) = t['p'], t['q']
            if abs(u0 - u1) > 0.01:
                continue
            ln = g.mm(abs(v1 - v0))
            if not (1.5 < ln < 6.5):
                continue
            if abs((v0 + v1) / 2 - y0) > 0.3 or not (xa - 0.3 <= u0 <= xb + 0.3):
                continue
            ticks.append(u0)
        ticks = sorted(set(round(v, 3) for v in ticks))
        if len(ticks) < 7:
            continue
        labels = {}
        for t in page['texts']:
            if not re.fullmatch(r'\d+', t['text']):
                continue
            if not (0 < g.mm(y0 - t['y']) < 9):
                continue
            c = text_centre(t, ot1)
            best = min(ticks, key=lambda u: abs(u - c))
            if g.mm(abs(best - c)) < 1.2:
                labels[best] = int(t['text'])
        gaps = [g.mm(b - a) for a, b in zip(ticks, ticks[1:])]
        out.append({'y': y0, 'x0': xa, 'x1': xb, 'ticks': ticks, 'gaps': gaps,
                    'unit': sum(gaps) / len(gaps),
                    'labels': [labels.get(u) for u in ticks]})
    # de-duplicate (a line may be listed twice)
    uniq = {}
    for r in out:
        uniq[(round(r['y'], 2), round(r['x0'], 2))] = r
    return sorted(uniq.values(), key=lambda r: (-r['y'], r['x0']))


def same(a, b, tol=0.05):
    return abs(a - b) <= tol


def ruler_below(rulers, x0, ybottom, maxgap_mm=14):
    cands = [r for r in rulers if same(g.mm(r['x0']), g.mm(x0), 0.05)
             and 0 < g.mm(ybottom - r['y']) < maxgap_mm]
    return max(cands, key=lambda r: r['y']) if cands else None


def text_in(page, bbox, pad=0.5):
    x0, y0, x1, y1 = bbox
    res = []
    for t in page['texts']:
        c = text_centre(t)
        if x0 - pad <= c <= x1 + pad and y0 - pad <= t['y'] <= y1 + pad:
            res.append(t['text'])
    return res


def closed_rects(page):
    return [p for p in page['paths'] if p['closed'] and not p['curved']]


def describe_ruler(r):
    lab = r['labels']
    ok_lab = lab == list(range(len(lab)))
    return ('ruler at y=%.1f mm, 0 at x=%.2f mm, %d ticks, unit %.3f mm '
            '(min %.3f, max %.3f), labels %s'
            % (g.mm(r['y']), g.mm(r['x0']), len(r['ticks']), r['unit'],
               min(r['gaps']), max(r['gaps']),
               '0..%d in order' % (len(lab) - 1) if ok_lab else lab))


# ------------------------------------------------------------ base packets
LAUNCH = [('A', 2, 3), ('B', 1, 2), ('A + B', 3, 5)]
P1 = [('A', 4, 6), ('B', 3, 4)]
P2 = [('A', 4, 6), ('B', 3, 4), ('C', 4, 5), ('D', 4, 5), ('E', 6, 8), ('F', 2, 4)]
P_SHARED = [('A', 4, 6), ('B', 4, 6)]
TOTAL9 = [('A', 4, 6), ('B', 3, 5)]
EXPECTED = {
    'k-1': {1: LAUNCH + P1, 2: P2,
            3: [('A', 3, 4), ('B', 3, 4), ('B', 4, 5), ('B', 5, 6)],
            4: P_SHARED, 5: [('long strip', 7, 9), ('short strip', 5, 6)],
            6: TOTAL9},
    'grades-2-3': {1: LAUNCH + P1, 2: P2, 3: [('A', 3, 4)], 4: P_SHARED,
                   5: [('long strip', 13, 15), ('short strip', 10, 12)],
                   6: TOTAL9},
    'grades-4-5': {1: LAUNCH + P1, 2: P2, 3: [('A', 3, 4)], 4: P_SHARED,
                   5: [('long strip', 13, 15), ('short strip', 10, 12)],
                   6: [('A', 7, 10), ('B', 3, 7)]},
}
PROBLEMS = {'k-1': [[1], [2], [3], [4], [5, 6], [7]],
            'grades-2-3': [[1], [2], [3, 4], [5], [6, 7], [8]],
            'grades-4-5': [[1], [2], [3, 4], [5], [6, 7], [8, 9]]}


def bands(page, rulers):
    """Light (0.96) + gray (0.84) filled rectangles that touch: a range band."""
    rects = [p for p in closed_rects(page) if p['fill'] is not None]
    light = [p for p in rects if same(p['fill'][0], 0.96, 0.001) and len(p['fill']) == 1]
    dark = [p for p in rects if same(p['fill'][0], 0.84, 0.001) and len(p['fill']) == 1]
    res = []
    for a in light:
        ax0, ay0, ax1, ay1 = a['bbox']
        for b in dark:
            bx0, by0, bx1, by1 = b['bbox']
            if same(ax1, bx0, 0.01) and same(ay0, by0, 0.01) and same(ay1, by1, 0.01):
                r = ruler_below(rulers, ax0, ay0)
                lab = None
                for t in page['texts']:
                    m = re.fullmatch(r'(.+): (\d+) to (\d+) units', t['text'])
                    if m and same(g.mm(t['x']), g.mm(ax0), 0.6) and 0 < g.mm(t['y'] - ay1) < 8:
                        lab = (m.group(1), int(m.group(2)), int(m.group(3)))
                q = text_in(page, (bx0, by0, bx1, by1))
                res.append({'x0': ax0, 'y': ay0, 'light_end': ax1, 'end': bx1,
                            'ruler': r, 'label': lab, 'q': q})
    return sorted(res, key=lambda d: (-d['y'], d['x0']))


def comparisons(page, rulers):
    """Rows made of a shaded piece followed by a white add-on (fill 1.0)."""
    rects = [p for p in closed_rects(page) if p['fill'] is not None]
    whites = [p for p in rects if len(p['fill']) == 1 and same(p['fill'][0], 1.0, 0.001)]
    rows = []
    for w in whites:
        wx0, wy0, wx1, wy1 = w['bbox']
        left = [p for p in rects if p is not w and same(p['bbox'][2], wx0, 0.01)
                and same(p['bbox'][1], wy0, 0.01) and same(p['bbox'][3], wy1, 0.01)]
        if len(left) != 1:
            continue
        lft = left[0]
        rows.append({'y': wy0, 'piece': lft, 'white': w,
                     'piece_label': text_in(page, lft['bbox']),
                     'white_label': text_in(page, w['bbox'])})
    rows.sort(key=lambda d: -d['y'])
    pics = []
    for i in range(0, len(rows), 2):
        top, bot = rows[i], rows[i + 1]
        r = ruler_below(rulers, top['piece']['bbox'][0], bot['y'], 20)
        pics.append((top, bot, r))
    return pics


def check_base(name):
    pdf = g.WEEK / ('week-51-%s.pdf' % name)
    pages = g.read_pdf(pdf)
    say('=' * 78)
    say('%s  (%d pages)' % (pdf.relative_to(g.ROOT), len(pages)))
    seen_problems = []
    for pno, page in enumerate(pages, 1):
        say('-- page %d' % pno)
        heads = [t['text'] for t in page['texts'] if t['y'] > g.PT_PER_MM * 265]
        foots = [t['text'] for t in page['texts'] if t['y'] < g.PT_PER_MM * 20]
        say('  header: %s | footer: %s' % (heads, foots))
        probs = [int(m.group(1)) for t in page['texts']
                 for m in [re.fullmatch(r'Problem (\d+):', t['text'].strip())] if m]
        say('  problems on page: %s' % probs)
        check(probs == PROBLEMS[name][pno - 1], '%s p%d problem numbers %s' % (name, pno, probs))
        seen_problems += probs
        rulers = find_rulers(page)
        for r in rulers:
            say('  ' + describe_ruler(r))
            check(all(same(gp, 10.0, 0.01) for gp in r['gaps']),
                  '%s p%d ruler unit not 10 mm' % (name, pno))
            check(r['labels'] == list(range(len(r['labels']))),
                  '%s p%d ruler labels %s' % (name, pno, r['labels']))
        found = []
        for b in bands(page, rulers):
            r = b['ruler']
            if r is None:
                say('  band at x=%.1f has no ruler below' % g.mm(b['x0']))
                check(False, '%s p%d band without ruler' % (name, pno))
                continue
            L = g.mm(b['light_end'] - r['x0']) / r['unit']
            U = g.mm(b['end'] - r['x0']) / r['unit']
            start = g.mm(b['x0'] - r['x0'])
            say('  band %-28s drawn %.3f..%.3f units; starts %.3f mm from ruler 0; "?" in gray: %s'
                % (b['label'], L, U, start, '?' in b['q']))
            check(b['label'] is not None and same(L, b['label'][1], 0.01)
                  and same(U, b['label'][2], 0.01) and same(start, 0, 0.05),
                  '%s p%d band %s drawn %.3f..%.3f' % (name, pno, b['label'], L, U))
            found.append(b['label'])
        exp = EXPECTED[name][pno]
        check(sorted(found) == sorted(exp), '%s p%d bands %s vs expected %s' % (name, pno, found, exp))
        # comparison pictures (shared-A page)
        for top, bot, r in comparisons(page, rulers):
            def row(rw):
                p0 = g.mm(rw['piece']['bbox'][0] - r['x0']) / 10
                p1 = g.mm(rw['piece']['bbox'][2] - r['x0']) / 10
                w1 = g.mm(rw['white']['bbox'][2] - r['x0']) / 10
                return p0, p1, w1
            t0, t1, tw = row(top)
            b0, b1, bw = row(bot)
            say('  comparison: top %s %.2f..%.2f + white %s to %.2f | bottom %s %.2f..%.2f + white %s to %.2f | drawn gap %.2f'
                % (top['piece_label'], t0, t1, top['white_label'], tw,
                   bot['piece_label'], b0, b1, bot['white_label'], bw, tw - bw))
            check(same(t0, 0) and same(b0, 0), 'comparison does not start at ruler 0')
            check(same(tw - t1, float(top['white_label'][0]), 0.01)
                  and same(bw - b1, float(bot['white_label'][0]), 0.01),
                  'white add-on length differs from its label')
            check(4 <= t1 <= 6 and 4 <= b1 <= 6, 'drawn A/B setting outside 4..6')
            if top['piece_label'] == bot['piece_label'] == ['A']:
                check(same(t1, b1), 'repeated A drawn with two lengths')
        # launch joins (fills 0.94 / 0.85)
        rects = [p for p in closed_rects(page) if p['fill'] is not None and len(p['fill']) == 1]
        ja = [p for p in rects if same(p['fill'][0], 0.94, 0.001)]
        jb = [p for p in rects if same(p['fill'][0], 0.85, 0.001)]
        if ja:
            ab = [b for b in bands(page, rulers) if b['label'] and b['label'][0] == 'A + B'][0]
            r0 = ab['ruler']['x0']
            for a in sorted(ja, key=lambda p: -p['bbox'][1]):
                b = [q for q in jb if same(q['bbox'][0], a['bbox'][2], 0.01)][0]
                lenA = g.mm(a['bbox'][2] - a['bbox'][0]) / 10
                lenB = g.mm(b['bbox'][2] - b['bbox'][0]) / 10
                num = [t['text'] for t in page['texts'] if re.fullmatch(r'\d', t['text'])
                       and a['bbox'][1] - g.PT_PER_MM <= t['y'] <= a['bbox'][3]
                       and t['x'] > b['bbox'][2]]
                say('  launch join: A %.2f + B %.2f = %.2f units, printed total %s; join starts %.2f mm right of the A+B ruler 0, so its end sits at %.2f on that ruler'
                    % (lenA, lenB, lenA + lenB, num, g.mm(a['bbox'][0] - r0),
                       g.mm(b['bbox'][2] - r0) / 10))
                check(num == ['%d' % round(lenA + lenB)], 'launch join total label')
        # answer boxes: stroked, unfilled, closed rectangles taller than 10 mm
        for p in closed_rects(page):
            x0, y0, x1, y1 = p['bbox']
            if p['fill'] is None and g.mm(y1 - y0) > 10 and g.mm(x1 - x0) > 50:
                say('  open box: %.2f mm wide (%.2f units) x %.2f mm, left edge x=%.2f mm, inner texts %s'
                    % (g.mm(x1 - x0), g.mm(x1 - x0) / 10, g.mm(y1 - y0), g.mm(x0),
                       text_in(page, p['bbox'], 1)))
            if p['fill'] is not None and len(p['fill']) == 1 and same(p['fill'][0], 0.875, 0.001) \
                    and g.mm(y1 - y0) > 12:
                box = [q for q in closed_rects(page) if q['fill'] is None
                       and same(q['bbox'][1], y0, 0.01) and same(q['bbox'][3], y1, 0.01)]
                bx = box[0]['bbox'][0]
                lo, hi = g.mm(x0 - bx) / 10, g.mm(x1 - bx) / 10
                say('  shaded target part: x=%.2f..%.2f mm, i.e. %.2f..%.2f units from the box\'s left edge'
                    % (g.mm(x0), g.mm(x1), lo, hi))
                check(same(lo, 7, 0.01) and same(hi, 9, 0.01), 'P3 target band is not 7..9')
        nums_below = [(r2(g.mm(t['x'])), t['text']) for t in page['texts']
                      if t['text'] in ('0', '7', '9') and same(t['size'], 9.96, 0.05)]
        if nums_below:
            say('  10-pt labels (x mm, text): %s' % nums_below)
        for t in page['texts']:
            if 'A + B = 12' in t['text']:
                say('  label "%s" at x=%.1f mm' % (t['text'], g.mm(t['x'])))
    check(seen_problems == list(range(1, len(seen_problems) + 1)),
          '%s problems not consecutive: %s' % (name, seen_problems))


# ------------------------------------------------------------------ bonus
def check_bonus():
    pdf = g.WEEK / 'week-51-bonus.pdf'
    pages = g.read_pdf(pdf, ot1=False)
    say('=' * 78)
    say('%s  (%d pages)' % (pdf.relative_to(g.ROOT), len(pages)))
    # page 1: grids and table
    p = pages[0]
    say('-- page 1')
    vert = sorted(set((round(s['p'][0], 2), round(min(s['p'][1], s['q'][1]), 2),
                       round(max(s['p'][1], s['q'][1]), 2))
                      for s in p['strokes'] if abs(s['p'][0] - s['q'][0]) < 0.01
                      and abs(s['p'][1] - s['q'][1]) > 1))
    horz = sorted(set((round(s['p'][1], 2), round(min(s['p'][0], s['q'][0]), 2),
                       round(max(s['p'][0], s['q'][0]), 2))
                      for s in p['strokes'] if abs(s['p'][1] - s['q'][1]) < 0.01
                      and abs(s['p'][0] - s['q'][0]) > 1))
    # group grids by their vertical extent
    def grid_from(lo_y, hi_y):
        xs = sorted(x for x, a, b in vert if same(a, lo_y, 0.5) and same(b, hi_y, 0.5))
        return xs
    big_v = [v for v in vert if g.mm(v[2] - v[1]) > 90]
    small_v = [v for v in vert if 17.2 < g.mm(v[2] - v[1]) < 18.2]
    for nm, vs in (('working grid', big_v), ('launch grid', small_v)):
        xs = sorted(v[0] for v in vs)
        y0, y1 = vs[0][1], vs[0][2]
        hs = sorted(h[0] for h in horz if same(h[1], xs[0], 0.5) and same(h[2], xs[-1], 0.5))
        dx = [g.mm(b - a) for a, b in zip(xs, xs[1:])]
        dy = [g.mm(b - a) for a, b in zip(hs, hs[1:])]
        say('  %s: %d columns x %d rows; column widths %s mm; row heights %s mm'
            % (nm, len(xs) - 1, len(hs) - 1, [r2(v) for v in dx], [r2(v) for v in dy]))
        if nm == 'working grid':
            check(len(xs) == 6 and len(hs) == 6 and all(same(v, 20.0, 0.01) for v in dx + dy),
                  'bonus working grid is not 5x5 of 20 mm squares')
        else:
            check(len(xs) == 4 and len(hs) == 3 and all(same(v, dx[0], 0.01) for v in dx + dy),
                  'bonus launch grid is not 3 wide x 2 high of equal squares')
            lab3 = [t for t in p['texts'] if t['text'] == '3' and t['y'] < hs[0]]
            lab2 = [t for t in p['texts'] if t['text'] == '2' and t['x'] < xs[0]]
            say('  launch labels: "3" centred at x=%.1f (grid centre %.1f) below grid; "2" at y=%.1f (grid mid %.1f) left of grid'
                % (text_centre(lab3[0], False), (xs[0] + xs[-1]) / 2, lab2[0]['y'] + 4,
                   (hs[0] + hs[-1]) / 2))
    boxes = [q for q in closed_rects(p) if q['stroke'] is not None]
    cols = sorted(set(round(q['bbox'][0], 1) for q in boxes))
    rows = sorted(set(round(q['bbox'][1], 1) for q in boxes))
    heads = [t['text'] for t in p['texts'] if t['text'] in ('A', 'B', 'Area')]
    say('  answer table: %d boxes, %d columns x %d rows, headers %s' % (len(boxes), len(cols), len(rows), heads))
    check(len(cols) == 3 and len(rows) == 5, 'bonus table is not 3x5')
    # page 2: cards and rulers
    p = pages[1]
    say('-- page 2')
    cards = [t['text'] for t in sorted(p['texts'], key=lambda t: (-t['y'], t['x']))
             if re.fullmatch(r'\d+ to \d+', t['text'])]
    say('  cards (row by row): %s' % cards)
    check(cards == ['2 to 7', '4 to 9', '5 to 6', '1 to 4', '3 to 8', '5 to 9',
                    '1 to 4', '6 to 8', '7 to 9'], 'bonus p2 cards')
    for r in find_rulers(p, ot1=False):
        say('  ' + describe_ruler(r) + '  (%.3f pt)' % (r['unit'] * g.PT_PER_MM))
    # page 3: bands
    p = pages[2]
    say('-- page 3')
    rulers = find_rulers(p, ot1=False)
    got = []
    for r in rulers:
        tag = [t['text'] for t in p['texts'] if t['text'] in ('A', 'B')
               and 0 < g.mm(t['y'] - r['y']) < 12 and same(g.mm(t['x']), g.mm(r['x0']), 1)]
        fills = [q for q in p['fills'] if 0 < g.mm(q['bbox'][1] - r['y']) < 2
                 and r['x0'] - 1 <= q['bbox'][0] <= r['x1']]
        lo = (fills[0]['bbox'][0] - r['x0']) / (r['unit'] * g.PT_PER_MM)
        hi = (fills[0]['bbox'][2] - r['x0']) / (r['unit'] * g.PT_PER_MM)
        say('  %s %s; band %.3f..%.3f' % (tag, describe_ruler(r), lo, hi))
        got.append((tag[0], round(lo, 3), round(hi, 3)))
    exp = [('A', 3, 7), ('B', 5, 9), ('A', 2, 4), ('B', 6, 8), ('A', 3, 5), ('B', 5, 7)]
    check(got == exp, 'bonus p3 bands %s' % got)


def hashes():
    say('=' * 78)
    say('Reference copies inside the source packages (byte comparison with print PDFs):')
    pairs = [('week-51-k-1.pdf', g.SRC / 'editable/reference-pdfs/k-1.pdf'),
             ('week-51-grades-2-3.pdf', g.SRC / 'editable/reference-pdfs/grades-2-3.pdf'),
             ('week-51-grades-4-5.pdf', g.SRC / 'editable/reference-pdfs/grades-4-5.pdf'),
             ('week-51-facilitator.pdf', g.SRC / 'editable/reference-pdfs/facilitator-guide.pdf'),
             ('week-51-bonus.pdf', g.BONUS_SRC / 'reference-pdfs/week-51-bonus.pdf'),
             ('week-51-bonus-facilitator.pdf', g.BONUS_SRC / 'reference-pdfs/week-51-bonus-facilitator.pdf')]
    for a, b in pairs:
        ha = hashlib.sha256((g.WEEK / a).read_bytes()).hexdigest()[:16]
        hb = hashlib.sha256(b.read_bytes()).hexdigest()[:16] if b.exists() else 'missing'
        say('  %-32s %s  %s' % (a, ha, 'identical' if ha == hb else 'DIFFERENT (%s)' % hb))


def main():
    for nm in ('k-1', 'grades-2-3', 'grades-4-5'):
        check_base(nm)
    check_bonus()
    hashes()
    say('=' * 78)
    say('MISMATCHES: %d' % len(FAIL))
    for f in FAIL:
        say('  ' + f)
    (Path(__file__).resolve().parent / 'out_check_diagrams.txt').write_text('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
