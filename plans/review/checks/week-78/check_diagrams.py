"""Read back the delivered Week 78 student PDF geometry and the guide text.

- Finds every 0..8 board (square frame), checks equal x/y scaling and an even
  1-unit grid, maps every filled dot (junction) and open circle (target) to
  board coordinates and reads its letter label; compares with the problems'
  stated data (independently transcribed from the rendered pages).
- Opening diagram: arm directions, junction, P and Q positions.
- Guide: reads the delivered facilitator PDF with pdftotext and confirms the
  printed answers that check_math.py recomputes.
Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
import os
import re
import subprocess
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
WEEK = os.path.join(REPO, 'lowell-math-circle-year-2', 'week-78')
STU = os.path.join(WEEK, 'week-78-students.pdf')
GUI = os.path.join(WEEK, 'week-78-facilitator.pdf')
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


# Expected boards per page, in reading order: list of {label: (x,y)} with kind
EXPECT = {
    1: [('P1 top-left', {'A': (4, 4)}, 'J'), ('P1 top-right', {'A': (4, 4)}, 'J'),
        ('P1 bottom-left', {'A': (2, 2), 'B': (6, 5)}, 'J'),
        ('P1 bottom-right', {'A': (2, 2), 'B': (5, 6)}, 'J')],
    2: [('P2 a', {'A': (2, 5), 'B': (6, 2)}, 'J'), ('P2 b', {'A': (3, 2), 'B': (3, 6)}, 'J'),
        ('P2 c', {'A': (2, 4), 'B': (6, 4)}, 'J'), ('P2 d', {'A': (2, 2), 'B': (6, 6)}, 'J')],
    3: [('P4 left', {'P': (2, 5), 'Q': (6, 2)}, 'T'), ('P4 right', {'P': (2, 2), 'Q': (6, 5)}, 'T'),
        ('P5 left', {'P': (2, 4), 'Q': (6, 4)}, 'T'), ('P5 middle', {'P': (3, 2), 'Q': (3, 6)}, 'T'),
        ('P5 right', {'P': (2, 2), 'Q': (5, 5)}, 'T')],
    4: [('P6', {'A': (2, 7)}, 'J'), ('P7', {}, 'J')],
}

doc = pymupdf.open(STU)
check(doc.page_count == 4, f'student PDF has {doc.page_count} pages (expected 4)')
for pno in range(4):
    page = doc[pno]
    dr = page.get_drawings()
    frames = [d for d in dr if d['type'] == 's' and len(d['items']) == 4
              and all(i[0] == 'l' for i in d['items']) and d['rect'].width > 100]
    frames.sort(key=lambda d: (round(d['rect'].y0 / 20), d['rect'].x0))
    grids = [d for d in dr if d['type'] == 's' and len(d['items']) > 8 and d['rect'].width > 100]
    dots = [d for d in dr if 'cccc' == ''.join(i[0] for i in d['items']) and d['rect'].width < 8]
    words = page.get_text('words')
    exp = EXPECT[pno + 1]
    check(len(frames) == len(exp), f'p{pno+1}: {len(frames)} boards (expected {len(exp)})')
    for fr, (name, pts, kind) in zip(frames, exp):
        r = fr['rect']
        u = r.width / 8
        check(abs(r.width - r.height) < 0.05, f'p{pno+1} {name}: frame {r.width:.2f} x {r.height:.2f} pt, equal scaling')
        # grid lines inside this frame
        g = [d for d in grids if abs(d['rect'].x0 - r.x0) < 1 and abs(d['rect'].y0 - r.y0) < 1]
        xs = sorted({round(i[1].x, 2) for d in g for i in d['items'] if i[0] == 'l' and abs(i[1].x - i[2].x) < .01})
        ys = sorted({round(i[1].y, 2) for d in g for i in d['items'] if i[0] == 'l' and abs(i[1].y - i[2].y) < .01})
        even = len(xs) == 9 and len(ys) == 9 and max(abs((xs[k + 1] - xs[k]) - u) for k in range(8)) < .05 \
            and max(abs((ys[k + 1] - ys[k]) - u) for k in range(8)) < .05
        check(even, f'p{pno+1} {name}: 9x9 grid lines, 1-unit spacing {u:.2f} pt in both axes')
        # tick labels 0..8 under the frame
        ticks = sorted((w[4], (w[0] + w[2]) / 2) for w in words
                       if w[4] in '02468' and len(w[4]) == 1 and r.y1 < w[1] < r.y1 + 14 and r.x0 - 5 < (w[0] + w[2]) / 2 < r.x1 + 5)
        tick_ok = all(abs(((cx - r.x0) / u) - int(t)) < .1 for t, cx in ticks) and len(ticks) == 5
        check(tick_ok, f'p{pno+1} {name}: x tick labels 0,2,4,6,8 at matching grid lines')
        found = {}
        for d in dots:
            c = d['rect']
            cx, cy = (c.x0 + c.x1) / 2, (c.y0 + c.y1) / 2
            if not (r.x0 - 1 <= cx <= r.x1 + 1 and r.y0 - 1 <= cy <= r.y1 + 1):
                continue
            X, Y = (cx - r.x0) / u, (r.y1 - cy) / u
            k = 'T' if d['type'] == 'fs' else 'J'
            # nearest label to the upper right
            lab = min((w for w in words if w[4] in ('A', 'B', 'P', 'Q')),
                      key=lambda w: (w[0] - cx) ** 2 + (w[3] - cy) ** 2)
            found[lab[4]] = (round(X, 2), round(Y, 2), k)
        want = {L: (float(x), float(y), kind) for L, (x, y) in pts.items()}
        check(found == want, f'p{pno+1} {name}: marks {found} (expected {want})')

say('\n== Opening diagram (page 1)')
page = doc[0]
dr = page.get_drawings()
small = [d for d in dr if d['type'] == 's' and len(d['items']) > 8 and 80 < d['rect'].width < 95][0]
xs = sorted({i[1].x for i in small['items'] if i[0] == 'l' and abs(i[1].x - i[2].x) < .01})
ys = sorted({i[1].y for i in small['items'] if i[0] == 'l' and abs(i[1].y - i[2].y) < .01})
u = xs[1] - xs[0]
check(abs((ys[1] - ys[0]) - u) < .05 and len(xs) == 6 and len(ys) == 6, f'opening grid 0..5, unit {u:.2f} pt both axes')
x0, y0 = xs[0], ys[-1]
to = lambda p: (round((p.x - x0) / u, 2), round((y0 - p.y) / u, 2))
arms = [d for d in dr if d['type'] == 's' and len(d['items']) == 1 and d['items'][0][0] == 'l' and d['width'] and d['width'] > 1]
segs = sorted((to(d['items'][0][1]), to(d['items'][0][2])) for d in arms)
say('     arm segments (grid units):', segs)
dirs = set()
for a, b in segs:
    dx, dy = b[0] - a[0], b[1] - a[1]
    dirs.add((round(dx / max(abs(dx), abs(dy)), 2), round(dy / max(abs(dx), abs(dy)), 2)))
check(all(a == (2.0, 2.0) for a, _ in segs) and dirs == {(1.0, 0.0), (0.0, 1.0), (-1.0, -1.0)},
      f'opening arms start at (2,2) and point east, north, southwest: {sorted(dirs)}')
marks = []
for d in dr:
    if ''.join(i[0] for i in d['items']) == 'cccc' and d['rect'].width < 8:
        c = d['rect']
        X, Y = to(pymupdf.Point((c.x0 + c.x1) / 2, (c.y0 + c.y1) / 2))
        if -1 <= X <= 6 and -1 <= Y <= 6 and c.y1 < 250:
            marks.append((X, Y, d['type']))
check(sorted(marks) == [(2.0, 2.0, 'f'), (4.0, 2.0, 'f'), (4.0, 4.0, 'fs')],
      f'opening marks: junction (2,2) filled, P (4,2) filled, Q (4,4) open: {sorted(marks)}')

say('\n== Guide text (pdftotext)')
gt = subprocess.run(['pdftotext', '-layout', GUI, '-'], capture_output=True, text=True).stdout
flat = re.sub(r'\s+', ' ', gt)
for s in ['Single point (5,4)', 'East ray from (6,4); north ray from (4,6)', 'Southwest ray from (4,4)',
          '(2,2) and (6,5) meet only at (3,2)', '(2,2) and (5,6) meet only at (2,3)',
          'One point, (6,5)', '(3,y) for every y≥6', '(x,4) for every x≥6', '(2−t,2−t) for every t≥0',
          'force junction (2,2)', 'force junction (5,5)', '(2−t,4), t≥0', '(3,2−t), t≥0', '(5+t,5+t), t≥0',
          'meet only at (10,7)', 'same row, column or diagonal']:
    check(s.replace(' ', '') in flat.replace(' ', ''), f'guide prints: "{s}"')
say(f"\n{len(FAIL)} failures")
with open(os.path.join(HERE, 'check_diagrams.py.out'), 'w') as f:
    f.write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
