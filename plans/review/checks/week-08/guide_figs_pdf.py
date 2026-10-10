"""Read the answer pictures out of the delivered adult guide PDF and check them.

For every small board drawn in the guide it finds the grid, the shaded (red)
squares, the star, the grey start dot and the arrow, and compares them with the
game-tree search: a board with a start dot must shade exactly the winning
move(s) and point the arrow there; a board without a dot must shade the
second-player squares (rook game, or queen game for the two queen pictures).
Output saved as guide_figs_pdf.out.
"""
import os
import sys
sys.dont_write_bytecode = True  # never leave __pycache__ beside the packet sources

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfdraw  # noqa: E402
import repo  # noqa: E402
from games import rook_P, rook_winning_moves  # noqa: E402

pages = pdfdraw.read(repo.GUIDE)
n_ok = n_bad = n_note = 0
for pg, (W, H, paths) in enumerate(pages, 1):
    grids = []
    for p in paths:
        if p['stroke'] and not p['fill'] and all(abs(c - 0.3) < 0.02 for c in p['sc']) and len(p['sub']) >= 8:
            ss = [s for s in p['sub'] if len(s) == 2]
            xs = sorted({round(s[0][0], 4) for s in ss if abs(s[0][0] - s[1][0]) < 1e-4})
            ys = sorted({round(s[0][1], 4) for s in ss if abs(s[0][1] - s[1][1]) < 1e-4})
            grids.append({'x0': xs[0], 'x1': xs[-1], 'y0': ys[0], 'y1': ys[-1], 'n': len(xs) - 1,
                          's': (xs[-1] - xs[0]) / (len(xs) - 1), 'sy': (ys[-1] - ys[0]) / (len(ys) - 1)})
    reds = [pdfdraw.bbox(p) for p in paths if p['fill'] and not p['stroke']
            and abs(p['fc'][0] - 1) < 0.02 and abs(p['fc'][1] - 0.55) < 0.02]
    dots = [pdfdraw.bbox(p) for p in paths if p['fill'] and p['curves'] == 4 and abs(p['fc'][0] - 0.65) < 0.02]
    stars = []
    for p in paths:
        if not p['fill'] and len(p['sub']) == 1 and len(p['sub'][0]) == 11:
            pts = p['sub'][0][:10]
            stars.append((sum(x for x, y in pts) / 10, sum(y for x, y in pts) / 10))
    lines = [p['sub'][0] for p in paths if p['stroke'] and not p['fill'] and len(p['sub']) == 1
             and len(p['sub'][0]) == 2 and p['lw'] * 72 > 1.0 and all(c < 0.05 for c in p['sc'])]
    for g in sorted(grids, key=lambda g: (round(g['y0'], 1), g['x0'])):
        def cellof(x, y):
            return int((x - g['x0']) // g['s']), int((g['y1'] - y) // g['s'])

        def ins(x, y):
            return g['x0'] - 1e-3 <= x <= g['x1'] + 1e-3 and g['y0'] - 1e-3 <= y <= g['y1'] + 1e-3
        red = sorted(cellof((b[0] + b[2]) / 2, (b[1] + b[3]) / 2) for b in reds if ins((b[0] + b[2]) / 2, (b[1] + b[3]) / 2))
        dot = [cellof((b[0] + b[2]) / 2, (b[1] + b[3]) / 2) for b in dots if ins((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)]
        star = [cellof(x, y) for x, y in stars if ins(x, y)]
        arr = []
        for a, b in lines:
            if ins(*a) and ins(*b):
                # the line stops short of the target's centre by the arrow head; extend by half a square
                dx, dy = b[0] - a[0], b[1] - a[1]
                L = (dx * dx + dy * dy) ** 0.5
                tip = (b[0] + dx / L * 0.3 * g['s'], b[1] + dy / L * 0.3 * g['s'])
                arr.append((cellof(*a), cellof(*tip)))
        n = g['n']
        if dot:
            st = dot[0]
            want = sorted(rook_winning_moves(*st))
            kind = 'start %s: shaded = winning move(s) %s' % (st, want)
            ok = red == want and all(t in want for _, t in arr) and len(arr) == len(want)
        else:
            rook = sorted((a, b) for a in range(n) for b in range(n) if rook_P(a, b))
            queen = sorted((a, b) for a in range(n) for b in range(n) if rook_P(a, b, True))
            ok = red in (rook, queen)
            kind = 'no start: shaded = %s second-player squares incl. (0,0)' % ('queen' if red == queen else 'rook')
        tag = 'OK      ' if ok else 'MISMATCH'
        if ok:
            n_ok += 1
        else:
            n_bad += 1
        print('%s page %d: %d-by-%d (square %.3f x %.3f in), star %s, dot %s, shaded %d %s, arrows %s -- %s' % (
            tag, pg, n, n, g['s'], g['sy'], star, dot, len(red), red if len(red) <= 8 else '(%d squares)' % len(red), arr, kind))
        if (0, 0) in red and not star:
            n_note += 1
            print('NOTE     page %d: the %d-by-%d picture shades the corner square (0,0) but draws no star on it, '
                  'so it shows %d shaded squares' % (pg, n, n, len(red)))
print('Summary: %d OK, %d MISMATCH, %d NOTE' % (n_ok, n_bad, n_note))
