"""Diagram check of the delivered Week 58 student and material PDFs (written for this review).

Reads pixels from `pdftoppm` renders at 254 dpi (10 px per mm) and word boxes from
`pdftotext -bbox`; imports no writer code.
* Materials: every 100 mm check bar (tick centre to tick centre); the five sturdy
  25 mm cards and the paper R3; the 100 x 150 mm preference/observer cards; the
  50 x 40 mm X/Y/Z panels; every 150 x 40 mm strip half and its strip number.
* Dot counts: on every preference card (student pp. 1-3, 5; materials pp. 2-5) the
  number of filled value dots equals the printed number beside it.
* Student strips: the red and blue panels of each p.3/p.4 sketch are equal in
  length, the p.4 dashed cut sits on the colour join, and the p.3 launch example's
  dashed line halves its panel; p.1 launch counters are 3 -> 2+1 -> 2+1.
Run: python3 check_diagrams.py   (writes out_check_diagrams.txt beside itself)
"""
import os
import re
import subprocess
import tempfile

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))


def find_root():
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')):
        return cand
    d = HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository not found above ' + HERE)


ROOT = find_root()
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-58')
STU = os.path.join(WEEK, 'week-58-students.pdf')
MAT = os.path.join(WEEK, 'week-58-materials.pdf')
DPI = 254
PX = DPI / 25.4          # px per mm (10)
PTPX = DPI / 72.0        # px per pt
OUT, FAIL = [], []
TMP = tempfile.mkdtemp(prefix='w58diag')


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


_cache = {}


def page(pdf, p):
    key = (pdf, p)
    if key not in _cache:
        base = os.path.join(TMP, '%s-%d' % (os.path.basename(pdf)[:-4], p))
        subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(p), '-l', str(p), '-png',
                        '-singlefile', pdf, base], check=True)
        _cache[key] = np.asarray(Image.open(base + '.png').convert('RGB')).astype(int)
    return _cache[key]


def words(pdf, p):
    t = subprocess.run(['pdftotext', '-bbox', '-f', str(p), '-l', str(p), pdf, '-'],
                       capture_output=True, text=True, check=True).stdout
    res = []
    for m in re.finditer(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)<', t):
        x0, y0, x1, y1 = (float(m.group(i)) * PTPX for i in range(1, 5))
        res.append((x0, y0, x1, y1, m.group(5)))
    return res


def ink(img):
    r, g, b = img[..., 0], img[..., 1], img[..., 2]
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    return (mx < 120) & (mx - mn < 40)


def near(img, rgb, tol):
    return np.all(np.abs(img - np.array(rgb)) <= tol, axis=-1)


def components(mask):
    """Row-run union-find labelling. Returns list of (x0, y0, x1, y1, area)."""
    parent = []

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    prev, boxes = [], []
    for y in range(mask.shape[0]):
        row = mask[y]
        if not row.any():
            prev = []
            continue
        d = np.diff(np.concatenate(([0], row.astype(np.int8), [0])))
        starts, ends = np.where(d == 1)[0], np.where(d == -1)[0]
        cur = []
        for s, e in zip(starts, ends):
            lab = len(parent)
            parent.append(lab)
            boxes.append([s, y, e - 1, y, e - s])
            for ps, pe, pl in prev:
                if ps < e and s < pe:
                    ra, rb = find(lab), find(pl)
                    if ra != rb:
                        parent[rb] = ra
            cur.append((s, e, lab))
        prev = cur
    merged = {}
    for i, b in enumerate(boxes):
        r = find(i)
        if r in merged:
            m = merged[r]
            m[0], m[1], m[2], m[3] = min(m[0], b[0]), min(m[1], b[1]), max(m[2], b[2]), max(m[3], b[3])
            m[4] += b[4]
        else:
            merged[r] = list(b)
    return [tuple(v) for v in merged.values()]


def erode(mask, k):
    """True where the k x k block starting there is entirely True."""
    s = np.zeros((mask.shape[0] + 1, mask.shape[1] + 1), dtype=np.int32)
    s[1:, 1:] = np.cumsum(np.cumsum(mask, 0), 1)
    blk = s[k:, k:] - s[:-k, k:] - s[k:, :-k] + s[:-k, :-k]
    out = np.zeros_like(mask)
    out[:blk.shape[0], :blk.shape[1]] = blk == k * k
    return out


def run_centres(line):
    """Centres of True runs in a 1-D boolean array."""
    d = np.diff(np.concatenate(([0], line.astype(np.int8), [0])))
    st, en = np.where(d == 1)[0], np.where(d == -1)[0]
    return [((s + e - 1) / 2.0, e - s) for s, e in zip(st, en)]


def edge_in(line, lo, hi):
    """Centre of the ink run(s) inside window [lo, hi) of a 1-D array (mean of ink pixels)."""
    lo, hi = max(0, int(lo)), min(len(line), int(hi))
    idx = np.where(line[lo:hi])[0]
    if len(idx) == 0:
        return None
    return lo + idx.mean()


def bars(img):
    """Find 100 mm check bars: long thin horizontal ink runs with vertical end ticks."""
    m = ink(img)
    found = []
    for comp in components(m):
        x0, y0, x1, y1, area = comp
        w, h = (x1 - x0 + 1) / PX, (y1 - y0 + 1) / PX
        if 95 < w < 106 and 3 < h < 5.5 and area < 0.15 * (x1 - x0 + 1) * (y1 - y0 + 1):
            yc = (y0 + y1) // 2
            probe = m[yc - int(1.2 * PX)]  # 1.2 mm above the bar line: only the ticks
            cs = [c for c, n in run_centres(probe[x0:x1 + 1])]
            if len(cs) == 2:
                found.append((x0 + cs[0], x0 + cs[1], (cs[1] - cs[0]) / PX))
    return found


# --------------------------------------------------------------------------
say('== Materials: 100 mm check bars')
for p in range(1, 11):
    b = bars(page(MAT, p))
    check(len(b) == 1 and abs(b[0][2] - 100) < 0.3,
          'materials p.%d: one check bar, tick centres %.2f mm apart' % (p, b[0][2] if b else -1))

say('')
say('== Materials p.1: 25 mm cards')
img = page(MAT, 1)
m = ink(img)
icons = [c for c in components(near(img, (185, 63, 68), 30) | near(img, (41, 107, 164), 30))
         if (c[2] - c[0]) / PX > 5]
icons.sort(key=lambda c: (c[1] // 50, c[0]))
check(len(icons) == 6, 'p.1 has 6 card icons (R1,R2,R3,B1,B2 and paper R3): %d' % len(icons))
for c in icons:
    cx, cy = (c[0] + c[2]) / 2, (c[1] + c[3]) / 2
    # icon centre is 12.5 mm from the card's left edge and 15.5 mm above its bottom edge
    left = edge_in(m[int(cy)], cx - 14.5 * PX, cx - 10.5 * PX)
    right = edge_in(m[int(cy)], cx + 10.5 * PX, cx + 14.5 * PX)
    col = m[:, int(cx + 8.5 * PX)]
    top = edge_in(col, cy - 11.5 * PX, cy - 7.5 * PX)
    bot = edge_in(col, cy + 13.5 * PX, cy + 17.5 * PX)
    if None in (left, right, top, bot):
        check(False, 'card outline found around icon at (%.0f, %.0f) mm' % (cx / PX, cy / PX))
        continue
    w, h = (right - left) / PX, (bot - top) / PX
    check(abs(w - 25) < 0.3 and abs(h - 25) < 0.3, 'card at (%.0f, %.0f) mm is %.2f x %.2f mm' % (cx / PX, cy / PX, w, h))
lab = [w[4] for w in words(MAT, 1)]
check(all(l in lab for l in ('R1', 'R2', 'B1', 'B2')) and lab.count('R3') == 3,
      'p.1 labels: R1, R2, R3, B1, B2 and the paper R3 (R3 appears in the note too)')

say('')
say('== Materials pp.2-5: 100 x 150 mm cards and 50 x 40 mm panels')
for p in (2, 3, 4, 5):
    img = page(MAT, p)
    m = ink(img)
    ws = words(MAT, p)
    names = [w for w in ws if w[4] in ('A', 'B', 'C', 'U', 'V') and (w[3] - w[1]) > 15]
    for w in names:
        cx = (w[0] + w[2]) / 2
        cy = (w[1] + w[3]) / 2           # name at card y = 135 (of 150)
        top_e, bot_e = cy - 15 * PX, cy + 135 * PX
        left = edge_in(m[int(cy + 75 * PX - 15 * PX)], cx - 52 * PX, cx - 48 * PX)
        right = edge_in(m[int(cy + 60 * PX)], cx + 48 * PX, cx + 52 * PX)
        left2 = edge_in(m[int(cy + 60 * PX)], cx - 52 * PX, cx - 48 * PX)
        col = m[:, int(cx + 46 * PX)]
        top = edge_in(col, top_e - 2 * PX, top_e + 2 * PX)
        bot = edge_in(col, bot_e - 2 * PX, bot_e + 2 * PX)
        if None in (left2, right, top, bot):
            check(False, 'p.%d card %s outline found' % (p, w[4]))
            continue
        cw, ch = (right - left2) / PX, (bot - top) / PX
        check(abs(cw - 100) < 0.4 and abs(ch - 150) < 0.4, 'p.%d card %s is %.2f x %.2f mm' % (p, w[4], cw, ch))
    if p == 5:
        panels = [w for w in ws if w[4] in ('X', 'Y', 'Z') and (w[3] - w[1]) > 6 * PX]
        check(len(panels) == 3, 'p.5 has three large panel letters X, Y, Z')
        for w in panels:
            cx, cy = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
            row, col = m[int(cy)], m[:, int(cx + 15 * PX)]
            l, r = edge_in(row, cx - 27 * PX, cx - 23 * PX), edge_in(row, cx + 23 * PX, cx + 27 * PX)
            t, b = edge_in(col, cy - 22 * PX, cy - 18 * PX), edge_in(col, cy + 18 * PX, cy + 22 * PX)
            check(None not in (l, r, t, b) and abs((r - l) / PX - 50) < 0.4 and abs((b - t) / PX - 40) < 0.4,
                  'p.5 panel %s is %.2f x %.2f mm' % (w[4], (r - l) / PX, (b - t) / PX))

say('')
say('== Materials pp.6-10: strip halves')
seen = []
for p in range(6, 11):
    img = page(MAT, p)
    m = ink(img)
    fills = [c for c in components(near(img, (240, 213, 214), 6) | near(img, (208, 222, 235), 6))
             if (c[2] - c[0]) / PX > 50]
    fills.sort(key=lambda c: c[1])
    ws = words(MAT, p)
    check(len(fills) == 4, 'p.%d has 4 coloured halves' % p)
    for c in fills:
        cy = (c[1] + c[3]) // 2
        cx = (c[0] + c[2]) // 2
        l = edge_in(m[cy], c[0] - 1.5 * PX, c[0] + 1)
        r = edge_in(m[cy], c[2], c[2] + 1.5 * PX)
        t = edge_in(m[:, cx], c[1] - 1.5 * PX, c[1] + 1)
        b = edge_in(m[:, cx], c[3], c[3] + 1.5 * PX)
        colour = 'red' if img[cy, cx][0] > img[cy, cx][2] else 'blue'
        # label just above: "Strip n / colour half / 150 x 40 mm"
        above = [w for w in ws if c[1] - 6 * PX < w[3] <= c[1] + 1 and w[0] < c[0] + 80 * PX]
        txt = ' '.join(w[4] for w in sorted(above, key=lambda w: w[0]))
        mm = re.search(r'Strip (\d+) / (red|blue) half / 150 . 40 mm', txt)
        ok = (None not in (l, r, t, b) and abs((r - l) / PX - 150) < 0.4 and abs((b - t) / PX - 40) < 0.4
              and mm is not None and mm.group(2) == colour)
        check(ok, 'p.%d %s half %.2f x %.2f mm, label "%s"' % (p, colour, (r - l) / PX if l and r else -1,
                                                             (b - t) / PX if t and b else -1, txt))
        if mm:
            seen.append((int(mm.group(1)), mm.group(2)))
check(sorted(seen) == sorted([(n, c) for n in range(1, 11) for c in ('red', 'blue')]),
      'strips 1-10 each have exactly one red and one blue half (10 strips per copy set)')

# --------------------------------------------------------------------------
say('')
say('== Value dots beside each printed number')


def dot_rows(pdf, p):
    img = page(pdf, p)
    m = ink(img)
    dots = [c for c in components(erode(m, 12)) if c[4] > 4]
    centres = [((c[0] + c[2]) / 2 + 6, (c[1] + c[3]) / 2 + 6) for c in dots]
    digits = [w for w in words(pdf, p) if re.fullmatch(r'\d+', w[4])]
    res = []
    for w in digits:
        wy = (w[1] + w[3]) / 2
        # dots in the same row, to the right of the digit, within 40 mm, pitch 4 mm
        row = sorted(x for x, y in centres if abs(y - wy) < 2.0 * PX and w[2] < x < w[2] + 40 * PX)
        chain = []
        for x in row:
            if not chain and x - w[2] < 12 * PX:
                chain.append(x)
            elif chain and abs((x - chain[-1]) / PX - 4) < 0.4:
                chain.append(x)
        res.append((w[4], len(chain), w[0] / PX, wy / PX))
    return res, len(dots)


for pdf, pages, tag in ((STU, (1, 2, 3, 5), 'student'), (MAT, (2, 3, 4, 5), 'materials')):
    for p in pages:
        rows, nd = dot_rows(pdf, p)
        # only digits that sit on preference cards (single digits with a dot row or a 0)
        card = [r for r in rows if r[1] > 0 or r[0] == '0']
        used = sum(r[1] for r in card)
        check(all(int(r[0]) == r[1] for r in card) and used == nd and len(card) > 0,
              '%s p.%d: %s (number, dots) and all %d dots accounted for'
              % (tag, p, [(r[0], r[1]) for r in card], nd))

# --------------------------------------------------------------------------
say('')
say('== Student strip sketches and launch examples')
for p in (3, 4):
    img = page(STU, p)
    m = ink(img)
    reds = [c for c in components(near(img, (240, 213, 214), 6)) if (c[2] - c[0]) / PX > 50]
    blues = [c for c in components(near(img, (208, 222, 235), 6)) if (c[2] - c[0]) / PX > 50]
    check(len(reds) == len(blues) == (2 if p == 3 else 1), 'p.%d: %d sketch strips' % (p, len(reds)))
    for rc, bc in zip(sorted(reds, key=lambda c: c[1]), sorted(blues, key=lambda c: c[1])):
        cy = (rc[1] + rc[3]) // 2 + int(6 * PX)
        l = edge_in(m[cy], rc[0] - 1.5 * PX, rc[0] + 1)
        j = edge_in(m[cy], rc[2], bc[0] + 1)
        r = edge_in(m[cy], bc[2], bc[2] + 1.5 * PX)
        check(rc[2] < bc[0] and abs((j - l) - (r - j)) / PX < 0.3,
              'p.%d sketch: red %.2f mm, blue %.2f mm (equal halves of a 300 mm strip)' % (p, (j - l) / PX, (r - j) / PX))
        if p == 4:
            # dashed cut: ink columns above/below the strip
            above = m[int(rc[1] - 2 * PX):int(rc[1] - 0.3 * PX)]
            cols = np.where(above.any(axis=0))[0]
            cols = cols[(cols > rc[0]) & (cols < bc[2])]
            cutx = cols.mean() if len(cols) else -1
            check(len(cols) and abs(cutx - j) / PX < 0.4,
                  'p.4 dashed cut at %.2f mm from the left end of a %.2f mm sketch; join at %.2f mm'
                  % ((cutx - l) / PX, (r - l) / PX, (j - l) / PX))

img = page(STU, 3)
m = ink(img)
grey = [c for c in components(near(img, (230, 230, 230), 4)) if (c[2] - c[0]) / PX > 10 and (c[3] - c[1]) / PX > 8]
grey.sort(key=lambda c: c[0])
check(len(grey) == 4, 'p.3 launch: input panel, cut panel and two output pieces found (%d grey boxes)' % len(grey))
if len(grey) == 4:
    say('   grey boxes (x0..x1 mm):', [('%.1f' % (c[0] / PX), '%.1f' % (c[2] / PX)) for c in grey])
    widths = [(c[2] - c[0] + 1) / PX for c in grey]
    cp = grey[1]
    above = m[int(cp[1] - 2 * PX):int(cp[1] - 0.3 * PX)]
    cols = np.where(above.any(axis=0))[0]
    cols = cols[(cols > cp[0]) & (cols < cp[2])]
    dash = cols.mean() if len(cols) else -1
    check(abs(widths[0] - widths[1]) < 0.3 and len(cols) and abs(dash - (cp[0] + cp[2]) / 2) / PX < 0.3,
          'p.3 launch: dashed line at %.2f mm of a %.2f mm panel (equal halves; input panel %.2f mm)'
          % ((dash - cp[0]) / PX, widths[1], widths[0]))
    check(abs(widths[2] - widths[3]) < 0.3,
          'p.3 launch: the two output pieces are equal (%.2f, %.2f mm)' % (widths[2], widths[3]))
    say('   note: output pieces are drawn %.1f mm each, the halves they come from %.1f mm (schematic)'
        % (widths[2], widths[1] / 2))

img = page(STU, 1)
counters = [c for c in components(erode(near(img, (224, 224, 224), 4), 25)) if c[4] > 20]
counters.sort(key=lambda c: c[0])
xs = [((c[0] + c[2]) / 2 + 12) / PX for c in counters]  # +12 px: erosion offset
# source x positions (students.tex): input 2,16,30; divider trays [61,88]: 69,80 and [94,117]: 105;
# choice trays [133,159]: 141,152 (chooser) and [166,185]: 175.5 (remainder)
src = [2, 16, 30, 69, 80, 105, 141, 152, 175.5]
rel = [x - xs[0] + src[0] for x in xs] if xs else []
check(len(counters) == 9 and all(abs(r - t) < 0.3 for r, t in zip(rel, src)),
      'p.1 launch counters at the source positions: input 3 -> trays 2|1 -> chooser 2 | remainder 1 (%s)'
      % ['%.1f' % r for r in rel])
trays = [c for c in components(ink(img)) if 15 < (c[2] - c[0]) / PX < 30 and 12 < (c[3] - c[1]) / PX < 18]
trays.sort(key=lambda c: c[0])
inside = [sum(1 for x in xs if t[0] / PX < x < t[2] / PX) for t in trays]
check(inside == [2, 1, 2, 1], 'p.1 launch: counters inside the four drawn trays: %s' % inside)

say('')
say('failures: %d' % len(FAIL))
for f in FAIL:
    say('  - ' + f)
with open(os.path.join(HERE, 'out_check_diagrams.txt'), 'w') as fh:
    fh.write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
