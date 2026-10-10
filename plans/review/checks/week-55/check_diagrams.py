"""Diagram check of the delivered Week 55 student PDF (written for this review).

Reads word boxes with `pdftotext -bbox` and pixels from `pdftoppm` renders at
254 dpi (10 px per mm); no writer code is imported.
* Result lanes (pp. 1-7): 19 labels 0..18, cell borders every 12 mm, 18 mm tall.
* Page-8 grids: every dot's number equals its row card plus its column card,
  rows increase upward and columns rightward, dots equally spaced in both
  directions, circles round (equal scaling); the demonstration's bold arrows
  join the dots of the printed route 1, 3, 7, 11.
* Draw order on page 8: whether the grey grid lines show inside the dot circles
  (through the printed numbers), dot by dot.
Run: python3 check_diagrams.py   (writes out_check_diagrams.txt beside itself)
"""
import os
import re
import subprocess
import sys
import tempfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
PDF = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-55', 'week-55-students.pdf')
PT = 25.4 / 72  # mm per point
DPI = 254       # 10 px per mm
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def words(page):
    x = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), PDF, '-'],
                       capture_output=True, text=True, check=True).stdout
    res = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x):
        x0, y0, x1, y1 = map(float, m.groups()[:4])
        res.append(dict(t=m.group(5), x=(x0 + x1) / 2 * PT, y=(y0 + y1) / 2 * PT, h=(y1 - y0)))
    return res


tmp = tempfile.mkdtemp()


def render(page):
    base = os.path.join(tmp, f'p{page}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-gray', '-f', str(page), '-l', str(page), PDF, base], check=True)
    f = [n for n in os.listdir(tmp) if n.startswith(f'p{page}-')][0]
    return Image.open(os.path.join(tmp, f)).convert('L')


def px(im, xmm, ymm):
    return im.getpixel((int(round(xmm * 10)), int(round(ymm * 10))))


def scan(im, x0, y0, dx, dy, maxmm=20, thresh=128):
    """Distance (mm) from (x0,y0) along (dx,dy) to the first dark pixel."""
    for k in range(1, int(maxmm * 10)):
        x = int(round(x0 * 10 + dx * k))
        y = int(round(y0 * 10 + dy * k))
        if im.getpixel((x, y)) < thresh:
            return k / 10
    return None


# ----------------------------------------------------------------- lanes
say('== Result lanes, pages 1-7')
for page in range(1, 8):
    W = words(page)
    small = [w for w in W if re.fullmatch(r'\d+', w['t']) and w['h'] < 9.5]
    rows = {}
    for w in small:
        rows.setdefault(round(w['y']), []).append(w)
    lanes = [sorted(v, key=lambda w: w['x']) for v in rows.values() if len(v) >= 15]
    im = render(page)
    for lane in lanes:
        labels = [int(w['t']) for w in lane]
        xs = [w['x'] for w in lane]
        sp = [b - a for a, b in zip(xs, xs[1:])]
        okl = labels == list(range(19)) and all(abs(s - 12) < 0.15 for s in sp)
        # pixel borders on a row 8 mm below the label centre
        yrow = lane[0]['y'] + 8
        borders, prev = [], False
        for xp in range(int((xs[0] - 9) * 10), int((xs[-1] + 9) * 10)):
            d = im.getpixel((xp, int(yrow * 10))) < 128
            if d and not prev:
                borders.append(xp / 10)
            prev = d
        bsp = [b - a for a, b in zip(borders, borders[1:])]
        # vertical extent, scanned 4 mm right of the "0" label (inside cell 0, clear of the glyph)
        top = scan(im, xs[0] + 4, lane[0]['y'], 0, -1)
        bot = scan(im, xs[0] + 4, lane[0]['y'], 0, 1, 25)
        height = top + bot if top and bot else None
        okb = len(borders) == 20 and all(abs(s - 12) < 0.25 for s in bsp)
        okh = height is not None and abs(height - 18) < 0.4
        check(okl and okb and okh,
              f'p{page} lane at y={lane[0]["y"]:.1f} mm: labels 0..18, {len(borders)} borders '
              f'{min(bsp):.1f}-{max(bsp):.1f} mm apart, height {height:.1f} mm')
    say(f'  p{page}: {len(lanes)} lanes')

# ----------------------------------------------------------------- page 8
say('\n== Page 8 grids')
W = words(8)
im8 = render(8)
nums = [w for w in W if re.fullmatch(r'\d+', w['t'])]
# dots are numbers inside 9 mm circles. Locate each circle from chords that avoid
# the numeral: a horizontal chord 3 mm below the word centre gives the centre x,
# a vertical chord 2.5 mm right of that gives the centre y (dark < 100 ignores grey lines).
def crossings(im, x0, y0, dx, dy, maxmm=6.5):
    for k in range(0, int(maxmm * 10)):
        if im.getpixel((int(round(x0 * 10 + dx * k)), int(round(y0 * 10 + dy * k)))) < 100:
            return k / 10
    return None


dots = []
for w in nums:
    yb = w['y'] + 3.0
    l, r = crossings(im8, w['x'], yb, -1, 0), crossings(im8, w['x'], yb, 1, 0)
    if l is None or r is None:
        continue
    cx = w['x'] + (r - l) / 2
    xr = cx + 2.5
    u, d = crossings(im8, xr, w['y'], 0, -1), crossings(im8, xr, w['y'], 0, 1)
    if u is None or d is None:
        continue
    cy = w['y'] + (d - u) / 2
    hl, hr = crossings(im8, cx, cy + 2.5, -1, 0), crossings(im8, cx, cy + 2.5, 1, 0)
    vu, vd = crossings(im8, cx + 2.5, cy, 0, -1), crossings(im8, cx + 2.5, cy, 0, 1)
    if None in (hl, hr, vu, vd):
        continue
    rh = ((((hl + hr) / 2) ** 2 + 2.5 ** 2) ** .5)
    rv = ((((vu + vd) / 2) ** 2 + 2.5 ** 2) ** .5)
    if 4.0 < rh < 5.0 and 4.0 < rv < 5.0:
        dots.append(dict(v=int(w['t']), x=cx, y=cy, dh=2 * rh, dv=2 * rv))
say(f'  dots found: {len(dots)} (expected 6 + 9 + 12 = 27)')
check(len(dots) == 27, 'all 27 dots located')
check(all(abs(d['dh'] - d['dv']) < 0.3 for d in dots), 'every dot circle is round (equal scaling)')
say(f'  dot diameters: {min(d["dh"] for d in dots):.1f}-{max(d["dh"] for d in dots):.1f} mm')

# group the dots into grids by position
grids = {'demo': [d for d in dots if d['y'] < 100],
         'left': [d for d in dots if d['y'] >= 100 and d['x'] < 140],
         'right': [d for d in dots if d['y'] >= 100 and d['x'] >= 140]}
labelwords = [w for w in nums if not any(abs(w['x'] - d['x']) < 5 and abs(w['y'] - d['y']) < 5 for d in dots)]
for name, gd in grids.items():
    xs = sorted({round(d['x'], 0) for d in gd})
    ys = sorted({round(d['y'], 0) for d in gd})
    cols = sorted(xs)
    rows_top_down = sorted(ys)
    # row labels: numbers left of the grid on each row line; column labels below the grid
    rowlab = {}
    for y in rows_top_down:
        cand = [w for w in labelwords if abs(w['y'] - y) < 1.5 and w['x'] < min(xs) - 4 and w['x'] > min(xs) - 15]
        rowlab[y] = int(cand[0]['t']) if len(cand) == 1 else None
    collab = {}
    for x in cols:
        cand = [w for w in labelwords if abs(w['x'] - x) < 1.5 and 0 < w['y'] - max(ys) < 14]
        collab[x] = int(cand[0]['t']) if len(cand) == 1 else None
    A_bottom_up = [rowlab[y] for y in reversed(rows_top_down)]
    B_left_right = [collab[x] for x in cols]
    say(f'  {name}: rows (bottom->top) {A_bottom_up}, columns {B_left_right}')
    check(None not in A_bottom_up and A_bottom_up == sorted(A_bottom_up), f'{name}: A increases bottom to top')
    check(None not in B_left_right and B_left_right == sorted(B_left_right), f'{name}: B increases left to right')
    bad = []
    for d in gd:
        y = min(rows_top_down, key=lambda t: abs(t - d['y']))
        x = min(cols, key=lambda t: abs(t - d['x']))
        if rowlab[y] is None or collab[x] is None or d['v'] != rowlab[y] + collab[x]:
            bad.append(d)
    check(not bad and len(gd) == len(cols) * len(rows_top_down), f'{name}: every dot = row card + column card')
    dx = [b - a for a, b in zip(cols, cols[1:])]
    dy = [b - a for a, b in zip(rows_top_down, rows_top_down[1:])]
    say(f'    spacing x {dx} mm, y {dy} mm')
    check(max(dx + dy) - min(dx + dy) <= 1.01, f'{name}: equal spacing across and up')

# demonstration bold arrows: the route 1 -> 3 -> 7 -> 11
demo = grids['demo']
byv = {}
for d in demo:
    byv.setdefault(d['v'], []).append(d)
one = byv[1][0]; three = byv[3][0]; eleven = byv[11][0]
seven_top = min(byv[7], key=lambda d: d['y'])
route = [one, three, seven_top, eleven]


def thick_between(a, b):
    """Fraction of dark pixels on the open segment between two circles (outside both)."""
    n = dark = 0
    for k in range(1, 100):
        t = k / 100
        x = a['x'] + (b['x'] - a['x']) * t
        y = a['y'] + (b['y'] - a['y']) * t
        if ((x - a['x']) ** 2 + (y - a['y']) ** 2) ** .5 < 5.2 or ((x - b['x']) ** 2 + (y - b['y']) ** 2) ** .5 < 5.2:
            continue
        n += 1
        dark += px(im8, x, y) < 100
    return dark / max(n, 1)


for a, b in zip(route, route[1:]):
    check(thick_between(a, b) > 0.95, f'demo bold arrow joins {a["v"]} -> {b["v"]}')
seven_bottom = max(byv[7], key=lambda d: d['y'])
five = byv[5][0]
for a, b in [(one, five), (seven_bottom, eleven), (five, seven_top), (three, seven_bottom)]:
    check(thick_between(a, b) < 0.2, f'no bold arrow between {a["v"]} and {b["v"]} (grey grid line only)')

# draw order: grey grid line visible inside a dot?
say('\n== Page 8 draw order: grey grid lines inside the dot circles')
exposed = []
for name, gd in grids.items():
    cols = sorted({round(d['x'], 0) for d in gd})
    rows_td = sorted({round(d['y'], 0) for d in gd})
    for d in gd:
        # darkest pixel in a 0.6 mm window above / right of the numeral, inside the circle
        up = min(px(im8, d['x'] + k / 10, d['y'] - 3.4) for k in range(-3, 4))
        right = min(px(im8, d['x'] + 3.4, d['y'] + k / 10) for k in range(-3, 4))
        has_up = round(d['y'], 0) != rows_td[0]
        has_right = round(d['x'], 0) != cols[-1]
        show_up = up < 235
        show_right = right < 235
        if show_up or show_right:
            exposed.append((name, d['v'], show_up, show_right))
        check(show_up == has_up and show_right == has_right,
              f'{name} dot {d["v"]}: line inside circle above={show_up} (grey {up}), right={show_right} (grey {right}); '
              f'predicted by draw order: above={has_up}, right={has_right}')
say(f'  dots with a grey line drawn through the numeral area: {len(exposed)} of {len(dots)}')
say('  (the grid lines are drawn after the earlier dots, so each dot shows the segments to its')
say('   upper and right neighbours; only the top-right dot of each grid is clean)')

say('\nSUMMARY:', 'all checks passed' if not FAIL else f'{len(FAIL)} FAIL(s)')
for f in FAIL:
    say('  FAIL:', f)
open(os.path.join(HERE, 'out_check_diagrams.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
sys.exit(1 if FAIL else 0)
