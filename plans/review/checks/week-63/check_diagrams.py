"""Read every diagram in the delivered Week 63 student and materials PDFs back
from their content streams and check it against the mathematics.

Student PDF: example rows and their yes/no checks (p. 1), the outcome-card
example (p. 2), all blank boards (pp. 1, 3, 7, 9), working boxes (pp. 2, 4-6),
the placement-to-arrow bridge (p. 7) and the four arrow diagrams of the removal
examples (p. 8): letters, arrow directions, regularity of the polygons and the
rows they encode.  Materials PDF: card, home-cell, label and outcome-card
sizes, shape regularity, and the full A-C and A-D outcome decks.
Run: python3 check_diagrams.py   (writes out_check_diagrams.txt beside itself)
"""
import math
import os as _os
import sys

HERE = _os.path.dirname(_os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfgeom63 as G  # noqa: E402
from rows63 import rows, matches, reduce_row, row_from_arrows  # noqa: E402

OUT = []
FAIL = []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


MM = G.MM
S = G.read(G.STUDENT_PDF)
M = G.read(G.MATERIALS_PDF)


def letters(page, size=None, tol=0.2):
    return [t for t in page['texts'] if len(t['s']) == 1 and t['s'].isupper()
            and (size is None or abs(t['size'] - size) < tol)]


def boards(page, cell_w_mm=12, cell_h_mm=10):
    """Group 12x10 mm cells into horizontal boards; read home labels above
    and card letters inside."""
    cells = [r for r in G.rects(page) if abs(r['w'] - cell_w_mm * MM) < 0.3 and abs(r['h'] - cell_h_mm * MM) < 0.3]
    cells.sort(key=lambda r: (-r['y0'], r['x0']))
    groups = []
    for c in cells:
        for g in groups:
            if abs(g[-1]['y0'] - c['y0']) < 0.5 and abs(g[-1]['x1'] - c['x0']) < 0.5:
                g.append(c)
                break
        else:
            groups.append([c])
    out = []
    small = [t for t in page['texts'] if len(t['s']) == 1 and t['size'] < 9]
    big = [t for t in page['texts'] if len(t['s']) == 1 and t['size'] > 9]
    for g in groups:
        homes, cards = '', ''
        for c in g:
            above = [t for t in small if c['x0'] < t['cx'] < c['x1'] and c['y1'] < t['cy'] < c['y1'] + 6 * MM]
            inside = [t for t in big if c['x0'] < t['cx'] < c['x1'] and c['y0'] < t['cy'] < c['y1']]
            homes += above[0]['s'] if len(above) == 1 else '?'
            cards += inside[0]['s'] if len(inside) == 1 else ('' if not inside else '?')
        out.append({'homes': homes, 'cards': cards, 'x0': g[0]['x0'], 'y0': g[0]['y0'], 'cells': g})
    return out


# ------------------------------------------------------------- page 1
say('== Student p. 1')
b1 = boards(S[0])
ex = [b for b in b1 if b['cards']]
blank = [b for b in b1 if not b['cards']]
say('example boards:', [(b['homes'], b['cards']) for b in ex])
check(len(ex) == 2 and all(b['homes'] == 'UVWX' and b['cards'] == 'VUWX' for b in ex),
      'p. 1 convention: both pictures show VUWX in U/V/W/X homes')
chk = max(ex, key=lambda b: b['x0'])
yn = sorted([t for t in S[0]['texts'] if t['s'] in ('yes', 'no')], key=lambda t: t['x'])
cols = []
for t in yn:
    cell = min(chk['cells'], key=lambda c: abs((c['x0'] + c['x1']) / 2 - t['cx']))
    cols.append((chk['homes'][chk['cells'].index(cell)], t['s']))
want = [(h, 'yes' if h == c else 'no') for h, c in zip('UVWX', 'VUWX')]
check(cols == want, f'p. 1 yes/no under each home {cols}')
check(any(t['s'] == '2 home matches' for t in S[0]['texts']) and len(matches('VUWX', 'UVWX')) == 2,
      'p. 1 record "2 home matches" is correct')
check(len(blank) == 10 and all(b['homes'] == 'ABC' for b in blank), f'P1: {len(blank)} blank A-B-C boards (2 answers)')

# ------------------------------------------------------------- page 2
say('\n== Student p. 2')
r2 = G.rects(S[1])
card = [r for r in r2 if abs(r['w'] - 56 * MM) < 0.3 and abs(r['h'] - 27 * MM) < 0.3]
check(len(card) == 1, 'p. 2 whole outcome card is 56 x 27 mm (same as materials cards)')
cells = sorted([r for r in r2 if abs(r['w'] - 9 * MM) < 0.3 and abs(r['h'] - 10 * MM) < 0.3], key=lambda r: r['x0'])
homes = ''.join(next(t['s'] for t in letters(S[1]) if c['x0'] < t['cx'] < c['x1'] and t['cy'] > c['y1']) for c in cells)
cards = ''.join(next(t['s'] for t in letters(S[1]) if c['x0'] < t['cx'] < c['x1'] and c['y0'] < t['cy'] < c['y1']) for c in cells)
ids = [t['s'] for t in S[1]['texts'] if t['s'] == 'VUWX']
say('outcome example homes', homes, 'cards', cards, 'IDs', ids)
check(homes == 'UVWX' and cards == 'VUWX' and len(ids) == 2, 'p. 2 outcome example is VUWX with ID and record VUWX')
props = [t['s'] for t in S[1]['texts'] if t['s'].endswith(': yes') or t['s'].endswith(': no')]
check(sorted(props) == ['W in home W: yes', 'X in home X: yes'] and matches('VUWX', 'UVWX') == {'W', 'X'},
      f'p. 2 property checks {props} are true for VUWX')


def rounded_boxes(page):
    out = []
    for p in page['paths']:
        if p['curved'] and p['closed']:
            x0, y0, x1, y1 = G.bbox(p['pts'])
            if x1 - x0 > 100:
                out.append(((x1 - x0) / MM, (y1 - y0) / MM))
    return out


for i, want in [(1, (173, 70)), (3, (173, 95)), (4, (173, 97)), (5, (173, 127))]:
    bx = rounded_boxes(S[i])
    check(len(bx) == 1 and abs(bx[0][0] - want[0]) < 0.5 and abs(bx[0][1] - want[1]) < 0.5,
          f'p. {i + 1} working box {[(round(a, 1), round(b, 1)) for a, b in bx]} mm')

# ------------------------------------------------------------- pages 3 and 9
say('\n== Student pp. 3 and 9 blank boards')
b3 = boards(S[2])
check(len(b3) == 16 and all(b['homes'] == 'ABCD' and not b['cards'] for b in b3), f'P3: {len(b3)} blank A-D boards (9 answers)')
b9 = boards(S[8])
check(len(b9) == 16 and all(b['homes'] == 'ABCDE' and not b['cards'] for b in b9), f'P9: {len(b9)} blank A-E boards (11 per branch)')


# ------------------------------------------------------------- arrow diagrams
def arrow_graph(page, circ_subset):
    """Return {source letter: target letter} for arrowheads ending on circles in circ_subset."""
    named = []
    for c in circ_subset:
        inside = [t for t in letters(page) if math.hypot(t['cx'] - c['cx'], t['cy'] - c['cy']) < c['r']]
        if len(inside) != 1:
            return None
        named.append((inside[0]['s'], c))
    edges = []
    for a in page['arrows']:
        tx, ty = a['tip']
        tgt = min(named, key=lambda nc: abs(math.hypot(tx - nc[1]['cx'], ty - nc[1]['cy']) - nc[1]['r']))
        gap = math.hypot(tx - tgt[1]['cx'], ty - tgt[1]['cy']) - tgt[1]['r']
        if abs(gap) > 2.0:
            continue
        back = (-a['dir'][0], -a['dir'][1])
        best = None
        for nm, c in named:
            if nm == tgt[0]:
                continue
            vx, vy = c['cx'] - tx, c['cy'] - ty
            ang = math.degrees(math.acos(max(-1, min(1, (vx * back[0] + vy * back[1]) / math.hypot(vx, vy)))))
            if best is None or ang < best[0]:
                best = (ang, nm)
        edges.append((best[1], tgt[0], round(best[0], 1), round(gap, 2)))
    return named, edges


def regular(centres):
    cx = sum(p[0] for p in centres) / len(centres)
    cy = sum(p[1] for p in centres) / len(centres)
    radii = [math.hypot(p[0] - cx, p[1] - cy) for p in centres]
    angs = sorted(math.atan2(p[1] - cy, p[0] - cx) for p in centres)
    pts = [(cx + r * math.cos(a), cy + r * math.sin(a)) for r, a in zip(radii, angs)]
    order = sorted(centres, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    sides = [math.hypot(order[i][0] - order[i - 1][0], order[i][1] - order[i - 1][1]) for i in range(len(order))]
    return max(radii) - min(radii), max(sides) - min(sides), sum(sides) / len(sides)


say('\n== Student p. 7')
p7 = S[6]
b7 = boards(p7)
place = [b for b in b7 if b['cards']]
say('placement boards', [(b['homes'], b['cards']) for b in place])
check(len(place) == 1 and place[0]['homes'] == 'PQRST' and place[0]['cards'] == 'QRSTP', 'p. 7 placement row QRSTP in P..T homes')
check(any(t['s'] == 'P is in home T' for t in p7['texts']), 'p. 7 "P is in home T" printed (true for QRSTP)')
circ = G.circles(p7)
top = [c for c in circ if c['cy'] > 550]
named, edges = arrow_graph(p7, top)
say('p. 7 cycle edges (source, target, angle deg, tip gap pt):', edges)
emap = {s: t for s, t, _, _ in edges}
check(emap == {'P': 'T', 'T': 'S', 'S': 'R', 'R': 'Q', 'Q': 'P'}, 'p. 7 drawn arrows = card->home arrows of QRSTP')
dr, ds, side = regular([(c['cx'], c['cy']) for _, c in named])
check(dr < 0.05 and ds < 0.05, f'p. 7 pentagon regular: radius spread {dr:.3f} pt, side spread {ds:.3f} pt, side {side / MM:.1f} mm')
ws = [c for c in circ if c['cy'] < 550]
work = [b for b in b7 if not b['cards']]
check(len(work) == 4 and all(b['homes'] == 'ABCD' for b in work) and len(ws) == 16, 'P7: four A-D workspaces with 16 circles (3 answers)')
wl = sorted(t['s'] for c in ws for t in letters(p7) if math.hypot(t['cx'] - c['cx'], t['cy'] - c['cy']) < c['r'])
check(wl == sorted('ABCD' * 4), 'P7 workspace circles lettered A-D in each')

say('\n== Student p. 8')
p8 = S[7]
circ = G.circles(p8)
hdr = sorted([t for t in p8['texts'] if t['s'] == 'Input'], key=lambda t: -t['y'])
ysplit = hdr[1]['y']
panels = {}
for c in circ:
    key = ('top' if c['cy'] > ysplit else 'bottom', 'input' if c['cx'] < 306 else 'output')
    panels.setdefault(key, []).append(c)
want = {
    ('top', 'input'): {'P': 'U', 'U': 'P', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'Q'},
    ('top', 'output'): {'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'Q'},
    ('bottom', 'input'): {'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'U', 'U': 'P'},
    ('bottom', 'output'): {'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'P'},
}
drawn = {}
used = 0
for key in sorted(panels):
    sub = panels[key]
    page_sub = dict(p8)
    named, edges = arrow_graph(p8, sub)
    # keep only arrows whose target is in this panel
    ed = [(s, t, a, g) for s, t, a, g in edges]
    say(key, 'circles', sorted(n for n, _ in named), 'edges', ed)
    drawn[key] = {s: t for s, t, _, _ in ed}
    used += len(ed)
    check(drawn[key] == want[key], f'p. 8 {key} arrows {drawn[key]}')
    cyc = [c for n, c in named if not (key == ('top', 'input') and n in 'PU')]
    dr, ds, side = regular([(c['cx'], c['cy']) for c in cyc])
    check(dr < 0.05 and ds < 0.05, f'p. 8 {key} polygon regular (radius spread {dr:.3f} pt, side spread {ds:.3f} pt, side {side / MM:.1f} mm)')
check(used == len(p8['arrows']) - 4, f'all {used} loop arrowheads assigned (plus 4 panel arrows)')
ti = row_from_arrows(drawn[('top', 'input')], 'PQRSTU')
bi = row_from_arrows(drawn[('bottom', 'input')], 'PQRSTU')
check(reduce_row(ti, 'PQRSTU', 'U')[2] == row_from_arrows(drawn[('top', 'output')], 'QRST'),
      f'top: removing the U-P pair from {ti} gives the drawn output')
check(reduce_row(bi, 'PQRSTU', 'U')[2] == row_from_arrows(drawn[('bottom', 'output')], 'PQRST'),
      f'bottom: bypassing U in {bi} gives the drawn output')
mid = [t['s'] for t in p8['texts'] if 'becomes' in t['s'] or 'point' in t['s'] or 'Remove' in t['s']]
say('p. 8 middle texts:', mid)

# ------------------------------------------------------------- materials
say('\n== Materials p. 1')
m1 = M[0]
r1 = G.rects(m1)
cards = [r for r in r1 if abs(r['w'] - 30 * MM) < 0.3 and abs(r['h'] - 40 * MM) < 0.3]
homes = [r for r in r1 if abs(r['w'] - 35 * MM) < 0.3 and abs(r['h'] - 45 * MM) < 0.3]
check(len(cards) == 10 and len(homes) == 10, f'{len(cards)} cards 30x40 mm, {len(homes)} home cells 35x45 mm')
hl = [(t['s'], (t['y'] - h['y0']) / MM) for h in homes for t in letters(m1)
      if h['x0'] < t['cx'] < h['x1'] and h['y0'] < t['cy'] < h['y1']]
check(len(hl) == 10 and all(b > 40 for _, b in hl),
      'every home letter baseline sits above the 40 mm card top (visible when cards are bottom-aligned)')
say('home letter baselines above cell bottom (mm):',
    sorted({round((t['y'] - h['y0']) / MM, 2) for h in homes for t in letters(m1) if h['x0'] < t['cx'] < h['x1'] and h['y0'] < t['cy'] < h['y1']}))
shapes = [p for p in m1['paths'] if p['op'] in ('B', 'f', 'b') and abs(p['fill'] - 0.88) < 0.01]
for p in shapes:
    pts = p['pts']
    if p['curved']:
        x0, y0, x1, y1 = G.bbox(pts)
        say(f'  circle {(x1 - x0) / MM:.2f} x {(y1 - y0) / MM:.2f} mm')
        continue
    uniq = []
    for q in pts:
        if not any(abs(q[0] - u[0]) < 1e-3 and abs(q[1] - u[1]) < 1e-3 for u in uniq):
            uniq.append(q)
    sides = [math.hypot(uniq[i][0] - uniq[i - 1][0], uniq[i][1] - uniq[i - 1][1]) / MM for i in range(len(uniq))]
    say(f'  {len(uniq)}-gon sides (mm): {[round(s, 2) for s in sides]}')
    check(max(sides) - min(sides) < 0.01, f'{len(uniq)}-gon has equal sides (equal scaling)')


def outcome_cards(page):
    out = []
    small = letters(page)
    for r in G.rects(page):
        if abs(r['w'] - 56 * MM) < 0.3 and abs(r['h'] - 27 * MM) < 0.3:
            inner = [c for c in G.rects(page) if abs(c['w'] - 9 * MM) < 0.3 and abs(c['h'] - 10 * MM) < 0.3
                     and r['x0'] <= c['x0'] and c['x1'] <= r['x1'] and r['y0'] <= c['y0'] and c['y1'] <= r['y1']]
            inner.sort(key=lambda c: c['x0'])
            hs = ''.join(next((t['s'] for t in small if c['x0'] < t['cx'] < c['x1'] and c['y1'] < t['cy'] < r['y1']), '?') for c in inner)
            cs = ''.join(next((t['s'] for t in small if c['x0'] < t['cx'] < c['x1'] and c['y0'] < t['cy'] < c['y1']), '') for c in inner)
            idt = [t['s'] for t in page['texts'] if r['x0'] < t['cx'] < r['x1'] and r['y0'] < t['y'] < r['y0'] + 6 * MM]
            out.append({'homes': hs, 'cards': cs, 'id': idt[0] if idt else ''})
    return out


say('\n== Materials p. 2')
oc = outcome_cards(M[1])
full = [o for o in oc if o['cards']]
blank = [o for o in oc if not o['cards']]
say('A-C outcomes:', [(o['homes'], o['cards'], o['id']) for o in full])
check(sorted(o['cards'] for o in full) == rows('ABC') and all(o['homes'] == 'ABC' and o['id'] == o['cards'] for o in full),
      'six A-C outcome cards are exactly the six rows, IDs match')
check(len(blank) == 12 and all(o['homes'] == 'ABCDE' for o in blank), f'{len(blank)} blank A-E outcome records')
labs = [r for r in G.rects(M[1]) if abs(r['w'] - 34 * MM) < 0.3 and abs(r['h'] - 16 * MM) < 0.3]
labt = sorted(t['s'] for t in M[1]['texts'] if 'in home' in t['s'])
check(len(labs) == 5 and labt == [f'{h} in home {h}' for h in 'ABCDE'], f'five 34x16 mm group labels {labt}')

say('\n== Materials p. 3')
oc3 = outcome_cards(M[2])
check(len(oc3) == 24 and sorted(o['cards'] for o in oc3) == rows('ABCD')
      and all(o['homes'] == 'ABCD' and o['id'] == o['cards'] for o in oc3), '24 A-D outcome cards are exactly the 24 rows, IDs match')

say('\nFAILURES:', len(FAIL))
for f in FAIL:
    say('  ' + f)
open(_os.path.join(HERE, 'out_check_diagrams.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
