"""
Draws every board (and the grade 4-5 start/finish pictures) to figures/*.png for visual checking,
checks that every actual-size board fits on a US Letter page, and writes coordinates.txt:
outline vertices in inches (origin = bottom-left corner of the board's bounding box, y upward),
holes, the rhombi of every pictured tiling, and a row-by-row character picture of each board.
Run: python3 render.py
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import tri
import lozenge as L
import instances as I

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, 'figures')
os.makedirs(FIG, exist_ok=True)

KIND_COLOR = {'R': '#7fb3ff', 'L': '#3d7be0', 'S': '#bcd6ff'}


def shift_of(region):
    return tri.min_corner(region)


def draw(region, fname, holes=(), tiling=None, title=None, pieces=None, base=None):
    sx, sy = shift_of(base if base is not None else region)
    fig, ax = plt.subplots(figsize=(4, 4))
    allcells = (base if base is not None else region)
    for t in allcells:
        pts = [tri.cart(c) for c in tri.corners(t)]
        pts = [(x - sx, y - sy) for x, y in pts]
        fc = 'black' if t in holes else 'white'
        ax.add_patch(Polygon(pts, closed=True, fc=fc, ec='#bbbbbb', lw=0.6))
    if tiling is not None:
        for rh in tiling:
            pts = [(x - sx, y - sy) for x, y in L.rhombus_cart(rh)]
            ax.add_patch(Polygon(pts, closed=True, fc=KIND_COLOR[L.kind(rh)], ec='black', lw=1.5))
    if pieces is not None:
        col = {'G': '#4caf50', 'B': '#3d7be0', 'R': '#e53935', 'Y': '#fdd835', 'P': '#8e24aa'}
        for p, pl in pieces:
            pts = [(x - sx, y - sy) for x, y in tri.piece_vertices(list(pl))]
            ax.add_patch(Polygon(pts, closed=True, fc=col[p], ec='black', lw=1.5, alpha=0.85))
    for loop in tri.boundary_vertices(region):
        pts = [tri.cart(p) for p in loop]
        pts = [(x - sx, y - sy) for x, y in pts]
        ax.add_patch(Polygon(pts, closed=True, fill=False, ec='black', lw=2))
    w, h = tri.bbox_inches(allcells)
    ax.set_xlim(-0.2, max(w, h) + 0.2)
    ax.set_ylim(-0.2, max(w, h) + 0.2)
    ax.set_aspect('equal')
    ax.axis('off')
    if title:
        ax.set_title(title, fontsize=8)
    fig.savefig(os.path.join(FIG, fname), dpi=80, bbox_inches='tight')
    plt.close(fig)


def fmt(v):
    return tri.fmt_num(v)


def char_picture(region, holes=()):
    """rows from top to bottom; each character is half an inch wide: '^' up-triangle, 'v' down-triangle, '#' hole."""
    sx, sy = shift_of(region | set(holes))
    allc = set(region) | set(holes)
    rows = {}
    for t in allc:
        i, j, o = t
        cs = [tri.cart(c) for c in tri.corners(t)]
        cx = sum(c[0] for c in cs) / 3 - sx
        pos = int(round(cx * 2))
        ch = '#' if t in holes else ('^' if o == 0 else 'v')
        rows.setdefault(j, {})[pos] = ch
    lines = []
    for j in sorted(rows, reverse=True):
        r = rows[j]
        mx = max(r)
        lines.append('    ' + ''.join(r.get(p, ' ') for p in range(0, mx + 1)))
    return lines


out = []
out.append('All coordinates in inches. Origin = bottom-left corner of the board\'s bounding box; x to the right, y up.')
out.append('Every outline vertex is a grid point. Grid points of a board are (x0 + i + j/2, j*0.8660) for whole numbers i, j,')
out.append('where x0 is the x-offset given for the board. Grid lines run horizontally and at 60 and 120 degrees through the grid points.')
out.append('Character pictures: one character per half inch; ^ = up-pointing small triangle, v = down-pointing, # = cut-out (hole).')
out.append('')

B = I.boards()
PAGE_W, PAGE_H = 7.5, 9.3  # usable area at 0.5in side margins, header/footer allowed for
fit_report = []
for k, R in B.items():
    base = I.HOLE_BASE.get(k)
    holes = I.HOLES.get(k, set())
    full = base if base is not None else R
    sx, sy = shift_of(full)
    w, h = tri.bbox_inches(full)
    fits = w <= PAGE_W and h <= PAGE_H
    fit_report.append((k, w, h, fits))
    out.append('[%s]  %d small triangles (%d up, %d down); bounding box %.2f in wide x %.2f in tall' % (k, len(R), *tri.counts(R), w, h))
    # x0: x offset of lattice in shifted coords
    x0 = (0 - sx) % 1.0
    loops = tri.boundary_vertices(full)
    for loop in loops:
        pts = [tri.cart(p) for p in loop]
        out.append('  outline: ' + ' '.join('(%s, %s)' % (fmt(x - sx), fmt(y - sy)) for x, y in pts))
    out.append('  grid x-offset x0 = %s' % fmt(x0 if abs(x0 - 1) > 1e-9 else 0))
    for t in sorted(holes, key=tri.order_key):
        pts = [tri.cart(c) for c in tri.corners(t)]
        out.append('  hole (%s triangle, print solid dark): ' % ('up' if t[2] == 0 else 'down') + ' '.join('(%s, %s)' % (fmt(x - sx), fmt(y - sy)) for x, y in pts))
    out.extend(char_picture(R, holes))
    out.append('')
    draw(R, k + '.png', holes=holes, base=base, title=k)

# grade 4-5 pictured tilings
out.append('=== Grades 4-5: pictured ways of covering the regular hexagon (board 45-P5), same coordinate frame as board 45-P5 ===')
out.append('Each rhombus is listed by its 4 corners. Kinds: R = lying, leans right; L = lying, leans left; S = standing diamond.')
H = I.H222
sx, sy = shift_of(H)
named = {}
for part, (s, t) in I.P5_PAIRS.items():
    named['45-P5%s-start' % part] = s
    named['45-P5%s-finish' % part] = t
named['45-P6-start'] = I.P6_START
for name, words in named.items():
    T = I.tiling_by_words(2, 2, 2, words)
    out.append('[%s] chains (left, right) = %s' % (name, ', '.join(words)))
    for rh in sorted(T, key=lambda r: sorted(L.rhombus_cart(r))):
        pts = L.rhombus_cart(rh)
        out.append('  %s: ' % L.kind(rh) + ' '.join('(%s, %s)' % (fmt(x - sx), fmt(y - sy)) for x, y in pts))
    out.append('')
    draw(H, name + '.png', tiling=T, title='%s  %s' % (name, words))

# the flip picture (yellow-hexagon shape, both fillings)
R1, ts1 = L.tilings(1, 1, 1)
out.append('=== Flip picture (grades 4-5 Problem 2): the yellow-hexagon shape (board 45-P1a frame) filled both ways ===')
sx1, sy1 = shift_of(R1)
for n, T in enumerate(ts1):
    out.append('[flip-%d]' % (n + 1))
    for rh in sorted(T, key=lambda r: sorted(L.rhombus_cart(r))):
        pts = L.rhombus_cart(rh)
        out.append('  %s: ' % L.kind(rh) + ' '.join('(%s, %s)' % (fmt(x - sx1), fmt(y - sy1)) for x, y in pts))
    draw(R1, 'flip-%d.png' % (n + 1), tiling=T)
out.append('')

# example chain for grades 4-5 Problem 3: hexagon with sides 1,3,1 (not used anywhere else), chain R L R R
R131, ts131 = L.tilings(1, 3, 1)
T = [t for t in ts131 if L.ribbons(t, 1, 3, 1) == ('RLRR',)][0]
sxe, sye = shift_of(R131)
w, h = tri.bbox_inches(R131)
out.append('=== Grades 4-5 Problem 3 example picture: hexagon with sides 1 (bottom), 3 (lower right), 1 (upper right); %.2f x %.2f in at actual size ===' % (w, h))
for loop in tri.boundary_vertices(R131):
    out.append('  outline: ' + ' '.join('(%s, %s)' % (fmt(x - sxe), fmt(y - sye)) for x, y in [tri.cart(p) for p in loop]))
m = L.partner_map(T)
chain = []
cur = (0, 0, 0)
for step in range(4):
    p = m[cur]
    chain.append(frozenset((cur, p)))
    cur = (cur[0], cur[1] + 1, 0) if p == (cur[0], cur[1], 1) else (cur[0] - 1, cur[1] + 1, 0)
for rh in sorted(T, key=lambda r: sorted(L.rhombus_cart(r))):
    pts = L.rhombus_cart(rh)
    tag = ('chain, letter %s' % L.kind(rh)) if rh in chain else 'not in chain'
    out.append('  %s (%s): ' % (L.kind(rh), tag) + ' '.join('(%s, %s)' % (fmt(x - sxe), fmt(y - sye)) for x, y in pts))
out.append('  chain from bottom to top: ' + ' '.join(L.kind(r) for r in chain))
out.append('')
draw(R131, '45-P3-example.png', tiling=T, title='chain R L R R')

# flip-spot key for grades 4-5 Problems 5 and 6
out.append('=== Grades 4-5 Problems 5-6 key picture: the 7 inner grid points of board 45-P5 where a flip can happen ===')
LETTER = {(0, 2): 'A', (1, 2): 'B', (0, 3): 'C', (-1, 3): 'D', (-1, 2): 'E', (0, 1): 'F', (1, 1): 'G'}
for p, ch in sorted(LETTER.items(), key=lambda kv: kv[1]):
    x, y = tri.cart(p)
    out.append('  %s at (%s, %s)' % (ch, fmt(x - sx), fmt(y - sy)))
out.append('')

# answer figures for adults (not for student pages)
ans = []
for k, abc in [('ans-45-P1c', (1, 2, 2)), ('ans-K1-P3c', (3, 1, 1))]:
    R, ts = L.tilings(*abc)
    for n, T in enumerate(ts):
        w = L.ribbons(T, *abc)
        draw(R, '%s-%d.png' % (k, n + 1), tiling=T, title='%s way %d  chains %s' % (k, n + 1, w))
for n in (3, 4, 5, 6, 7):
    R = I.TRI[n]
    g, ex = tri.min_greens(R, ['B'])
    draw(R, 'ans-tri%d-blues.png' % n, pieces=ex, title='side %d: blues + %d greens' % (n, g))
    g, ex = tri.min_greens(R, ['P'])
    draw(R, 'ans-tri%d-purples.png' % n, pieces=ex, title='side %d: purples + %d greens' % (n, g))
for k in ('23-P6a', '23-P6b', '23-P1d'):
    g, ex = tri.min_greens(B[k], ['B'])
    draw(B[k], 'ans-%s.png' % k, pieces=ex, title='%s: blues + %d greens' % (k, g))
for k in ('K1-P4a', 'K1-P4b', 'K1-P4c'):
    m, ex = tri.min_pieces(B[k], ['Y', 'R', 'B', 'G'])
    draw(B[k], 'ans-%s.png' % k, pieces=ex, title='%s: %d blocks' % (k, m))
draw(I.SMALLEST_3GAP, 'ans-23-P7.png', title='smallest board needing 3 greens')
n, sols = tri.count_tilings(I.H222, ['P'], collect=True)
for i, s in enumerate(sols):
    draw(I.H222, 'ans-hex-purples-%d.png' % (i + 1), pieces=s)
n, sols = tri.count_tilings(B['K1-P5b'], ['R'], collect=True)
draw(B['K1-P5b'], 'ans-K1-P5b.png', pieces=sols[0], title='big red from 4 reds')

with open(os.path.join(HERE, 'coordinates.txt'), 'w') as f:
    f.write('\n'.join(out) + '\n')

print('Page fit (usable area %.1f x %.1f in):' % (PAGE_W, PAGE_H))
allfit = True
for k, w, h, fits in fit_report:
    print('  %-8s %.2f x %.2f  %s' % (k, w, h, 'fits' if fits else 'DOES NOT FIT'))
    allfit &= fits
print('ALL BOARDS FIT AT ACTUAL SIZE' if allfit else 'SOME BOARD DOES NOT FIT')
print('wrote coordinates.txt and %d figures' % len(os.listdir(FIG)))
