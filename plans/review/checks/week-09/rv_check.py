"""Week 9 return visit (F09-RV-v1) and its guide (RV9-FAC-v1): a companion check.

Boards, dots, rings and letters are read from week-09-return-visit.pdf with
pdfgeom.py.  Problem 1 (two-bounce wall words) is solved exactly with
Fractions by following the ray and its reflections, not by the guide's image
recipe; Problem 2 (interior starts) and Problem 3 (crossings) by stepping the
ball on the grid.  Each guide sentence is first confirmed to be in the PDF.
Lines starting with MISMATCH or NOTE are the ones to read.
"""
import re
import subprocess
from fractions import Fraction as Fr
from itertools import product
from math import gcd

from billiards import crossings
from pdfgeom import PDF, pages, words

MM = 72 / 25.4
n_checks = 0
problems = []


def check(label, ok, detail=''):
    global n_checks
    n_checks += 1
    print(f"  {'ok      ' if ok else 'MISMATCH'} {label}" + (f': {detail}' if detail else ''))
    if not ok:
        problems.append(label)


def note(label, detail):
    print(f'  NOTE     {label}: {detail}')


def norm(s):
    s = s.replace('“', '"').replace('”', '"').replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', ' ', s).strip()


def text(path):
    raw = subprocess.run(['pdftotext', str(path), '-'], capture_output=True, text=True, check=True).stdout
    return norm(raw), norm(raw.replace('-\n', '')), norm(raw.replace('-\n', '-'))


GT = text(PDF['rv-guide'])


def claim(q, ok, detail=''):
    # pdftotext may drop the hyphen of a word broken at a line end ("3-by-" / "11" -> "3-by11")
    if any(norm(q) in t or norm(q).replace('-', '') in t.replace('-', '') for t in GT):
        check(q[:100] + ('...' if len(q) > 100 else ''), ok, detail)
    else:
        print('  MISSING-QUOTE', q[:90])
        problems.append('quote not found: ' + q[:60])


def bbox(p):
    xs = [q[0] for sp in p.subpaths for q in sp]
    ys = [q[1] for sp in p.subpaths for q in sp]
    return min(xs), min(ys), max(xs), max(ys)


def centre(p):
    x0, y0, x1, y1 = bbox(p)
    return (x0 + x1) / 2, (y0 + y1) / 2


# ------------------------------------------------------------------ boards
PG = pages(PDF['rv'])
WD = words(PDF['rv'])


def boards(page):
    """Each board: outline (thick closed rectangle) with its grid lines, in board units."""
    out = []
    paints = PG[page - 1]
    grids = [p for p in paints if p.kind == 'stroke' and abs(p.stroke_gray - 0.75) < 0.01 and len(p.subpaths) > 2]
    for g in grids:
        x0, y0, x1, y1 = bbox(g)
        def uniq(vals, tol=0.3):
            out = []
            for v in sorted(vals):
                if not out or v - out[-1] > tol:
                    out.append(v)
            return out
        xs = uniq([sp[0][0] for sp in g.subpaths if abs(sp[0][0] - sp[-1][0]) < 1e-3] + [x0, x1])
        ys = uniq([sp[0][1] for sp in g.subpaths if abs(sp[0][1] - sp[-1][1]) < 1e-3] + [y0, y1])
        cw = (x1 - x0) / (len(xs) - 1)
        chh = (y1 - y0) / (len(ys) - 1)
        b = dict(x0=x0, y0=y0, x1=x1, y1=y1, w=len(xs) - 1, h=len(ys) - 1, cell_w=cw, cell_h=chh,
                 uniform=max(abs(b2 - a - cw) for a, b2 in zip(xs, xs[1:])) < 0.05 and
                 max(abs(b2 - a - chh) for a, b2 in zip(ys, ys[1:])) < 0.05)

        def unit(pt):
            return ((pt[0] - x0) / cw, (pt[1] - y0) / chh)
        b['unit'] = unit
        b['dots'], b['rings'] = [], []
        for p in paints:
            if any(p.curved) and p.kind == 'fill':
                cx, cy = centre(p)
                if x0 - 3 <= cx <= x1 + 3 and y0 - 3 <= cy <= y1 + 3:
                    u = unit((cx, cy))
                    (b['rings'] if p.fill_gray > 0.5 else b['dots']).append((round(u[0], 3), round(u[1], 3)))
        b['outline'] = any(p.kind == 'stroke' and all(p.closed) and not any(p.curved) and p.stroke_gray < 0.1 and
                           abs(bbox(p)[0] - x0) < 0.5 and abs(bbox(p)[2] - x1) < 0.5 and
                           abs(bbox(p)[1] - y0) < 0.5 and abs(bbox(p)[3] - y1) < 0.5 for p in paints)
        out.append(b)
    out.sort(key=lambda b: (-round(b['y1'] / 10), b['x0']))
    return out


# ------------------------------------------------------------------ Problem 1: two bounces
def reflect(pt, wall, W, H):
    x, y = pt
    return {'L': (-x, y), 'R': (2 * W - x, y), 'B': (x, -y), 'T': (x, 2 * H - y)}[wall]


def follow(S, d, W, H, tmax=Fr(1)):
    """Follow the ray S + t d (0 < t <= tmax) inside [0,W]x[0,H] with mirror walls, exactly.
    Returns list of (t, point, wall or 'corner')."""
    x, y = S
    dx, dy = d
    t = Fr(0)
    events = []
    while True:
        cand = []
        if dx > 0:
            cand.append(((W - x) / dx, 'R'))
        if dx < 0:
            cand.append(((0 - x) / dx, 'L'))
        if dy > 0:
            cand.append(((H - y) / dy, 'T'))
        if dy < 0:
            cand.append(((0 - y) / dy, 'B'))
        dt = min(c[0] for c in cand)
        walls = [c[1] for c in cand if c[0] == dt]
        if t + dt >= tmax:
            return events, (x + (tmax - t) * dx, y + (tmax - t) * dy)
        t += dt
        x, y = x + dt * dx, y + dt * dy
        if len(walls) == 2:
            events.append((t, (x, y), 'corner'))
            return events, (x, y)
        events.append((t, (x, y), walls[0]))
        if walls[0] in 'LR':
            dx = -dx
        else:
            dy = -dy


def passes(S, d, W, H, P, tmax):
    """Does the folded ray pass through P at some 0 < t < tmax?"""
    x, y = S
    dx, dy = d
    t = Fr(0)
    for _ in range(50):
        cand = []
        if dx > 0:
            cand.append((W - x) / dx)
        if dx < 0:
            cand.append(-x / dx)
        if dy > 0:
            cand.append((H - y) / dy)
        if dy < 0:
            cand.append(-y / dy)
        dt = min(min(cand), tmax - t)
        # P on the open piece from (x,y) to (x+dt dx, y+dt dy)?
        if dx != 0:
            s = (P[0] - x) / dx
        else:
            s = (P[1] - y) / dy
        if 0 < s < dt and (x + s * dx, y + s * dy) == P:
            return True
        t += dt
        if t >= tmax:
            return False
        x, y = x + dt * dx, y + dt * dy
        if x in (0, W):
            dx = -dx
        if y in (0, H):
            dy = -dy
    return False


def two_bounce_words(S, F, W, H):
    """All words XY with a legal route: exactly two wall contacts, in that order, no corner,
    ending at F, not passing F earlier.  Every two-bounce route unfolds to the straight line
    to R_X(R_Y(F)); we find the direction by solving, but legality is judged by following
    the ray, not by the recipe."""
    res = {}
    for X, Y in product('LRBT', repeat=2):
        img = reflect(reflect(F, Y, W, H), X, W, H)
        d = (img[0] - S[0], img[1] - S[1])
        if d == (0, 0):
            continue
        ev, end = follow(S, d, W, H)
        walls = [e[2] for e in ev]
        ok = walls == [X, Y] and end == F and not passes(S, d, W, H, F, Fr(1))
        res[X + Y] = dict(ok=ok, events=ev, end=end, image=img, len2=d[0] ** 2 + d[1] ** 2)
    return res


def all_two_bounce_routes(S, F, W, H, N=40):
    """Independent search: every direction (a, b) with small integer entries whose folded ray
    reaches F after exactly two contacts (any length).  Confirms that no route is missed."""
    found = set()
    for a in range(-N, N + 1):
        for b in range(-N, N + 1):
            if (a, b) == (0, 0) or gcd(abs(a), abs(b)) != 1:
                continue
            # walk event by event and see whether F is hit after exactly two contacts
            x, y = S
            dx, dy = a, b
            t = Fr(0)
            contacts = []
            for _ in range(3):
                cand = []
                if dx > 0:
                    cand.append(((W - x) / dx, 'R'))
                if dx < 0:
                    cand.append((-x / Fr(dx), 'L'))
                if dy > 0:
                    cand.append(((H - y) / dy, 'T'))
                if dy < 0:
                    cand.append((-y / Fr(dy), 'B'))
                dt = min(c[0] for c in cand)
                # F on this piece?
                s = (F[0] - x) / dx if dx else (F[1] - y) / dy
                if 0 < s <= dt and (x + s * dx, y + s * dy) == F:
                    if len(contacts) == 2:
                        found.add(''.join(contacts))
                    break
                walls = [c[1] for c in cand if c[0] == dt]
                if len(walls) == 2:
                    break
                x, y = x + dt * dx, y + dt * dy
                contacts.append(walls[0])
                if walls[0] in 'LR':
                    dx = -dx
                else:
                    dy = -dy
    return found


print('Return visit, page 1: launch picture and Problem 1 boards')
p1 = PG[0]
# launch picture: three 4-unit boxes (no grid), S dot, R wall, F ring
boxes = sorted([p for p in p1 if p.kind == 'stroke' and abs(p.lw - 0.4) < 0.05 and abs(p.stroke_gray - 0.75) < 0.01
                and all(p.closed)], key=lambda p: bbox(p)[0])
bx0, by0, bx1, by1 = bbox(boxes[2])
u = (bx1 - bx0) / 4
Sx = [centre(p) for p in p1 if p.kind == 'fill' and any(p.curved) and bx0 < centre(p)[0] < bx1 and by0 < centre(p)[1] < by1 and p.fill_gray < 0.5]
Fx = [centre(p) for p in p1 if p.kind == 'fill' and any(p.curved) and bx0 < centre(p)[0] < bx1 and by0 < centre(p)[1] < by1 and p.fill_gray > 0.5]
route = [p for p in p1 if p.kind == 'stroke' and abs(p.lw - 0.9) < 0.05 and 0.2 < p.stroke_gray < 0.4 and bx0 - 1 < bbox(p)[0] and bbox(p)[2] < bx1 + 1]
pts = [((q[0] - bx0) / u, (q[1] - by0) / u) for q in route[0].subpaths[0]]
S0 = tuple(round((c - o) / u, 3) for c, o in zip(Sx[0], (bx0, by0)))
F0 = tuple(round((c - o) / u, 3) for c, o in zip(Fx[0], (bx0, by0)))
pr = [tuple(round(c, 3) for c in q) for q in pts]
check('launch picture: box is square, S=(1,1), contact (4,2) on the right wall, F=(1,3)',
      abs((by1 - by0) - (bx1 - bx0)) < 0.1 and S0 == (1, 1) and F0 == (1, 3) and pr == [(1, 1), (4, 2), (1, 3)],
      f'S {S0}, F {F0}, route {pr}')
check('launch picture: equal angles at the contact (incoming (3,1), outgoing (-3,1))',
      (pr[1][0] - pr[0][0], pr[1][1] - pr[0][1]) == (3, 1) and (pr[2][0] - pr[1][0], pr[2][1] - pr[1][1]) == (-3, 1))
claim('use the non-task visual S=(1,1), R-wall contact (4,2), F=(1,3).', S0 == (1, 1) and F0 == (1, 3))

finishes = {}
for page in (1, 2, 3):
    for b, lab in zip(boards(page), ['A', 'B'] * 3):
        ok = (b['w'], b['h']) == (4, 4) and b['uniform'] and abs(b['cell_w'] - b['cell_h']) < 0.01
        finishes.setdefault(lab, []).append((tuple(b['dots']), tuple(b['rings']), round(b['cell_w'] / MM, 2), ok))
for lab, lst in finishes.items():
    check(f'Problem 1 Finish {lab}: {len(lst)} boards, all 4 by 4 with the same S and F',
          len(set(x[:2] for x in lst)) == 1 and all(x[3] for x in lst), str(lst[0]))
SA = tuple(Fr(round(c)) for c in finishes['A'][0][0][0])
FA = tuple(Fr(round(c)) for c in finishes['A'][0][1][0])
FB = tuple(Fr(round(c)) for c in finishes['B'][0][1][0])
check('Problem 1 boards: S=(1,1), Finish A F=(2,3), Finish B F=(3,3); 12.5 mm squares',
      SA == (1, 1) and FA == (2, 3) and FB == (3, 3) and finishes['A'][0][2] == 12.5,
      f'S {SA}, A {FA}, B {FB}, {finishes["A"][0][2]} mm')
W = H = Fr(4)
resA = two_bounce_words(SA, FA, W, H)
resB = two_bounce_words(SA, FB, W, H)
legalA = sorted(k for k, v in resA.items() if v['ok'])
legalB = sorted(k for k, v in resB.items() if v['ok'])
print(f'    Finish A legal words: {legalA}')
print(f'    Finish B legal words: {legalB}')
searchA = all_two_bounce_routes(SA, FA, W, H, N=12)
searchB = all_two_bounce_routes(SA, FB, W, H, N=12)
check('Problem 1: a direct search over directions finds the same words (no route missed)',
      searchA == set(legalA) and searchB == set(legalB), f'{sorted(searchA)} / {sorted(searchB)}')
claim('On the 4-by-4 table with S=(1, 1) and F=(2, 3) (Finish A), the legal words are LR, LT, RL, RT, BL, BR, BT, TB.',
      set(legalA) == set('LR LT RL RT BL BR BT TB'.split()))
claim('With F=(3, 3) (Finish B) they are LR, LT, RL, BR, BT, TB.', set(legalB) == set('LR LT RL BR BT TB'.split()))
claim('On the displayed 4-by-4 examples there are eight and six legal words.', (len(legalA), len(legalB)) == (8, 6))
claim('For the second target the LB/BL image is (−3, −3) and the ray hits (0, 0); the RT/TR image is (5, 5) and the ray '
      'hits (4, 4). These are excluded corner contacts.',
      resB['LB']['image'] == (-3, -3) and resB['LB']['events'][0][1:] == ((0, 0), 'corner') and
      resB['BL']['events'][0][2] == 'corner' and resB['RT']['image'] == (5, 5) and
      resB['RT']['events'][0][1:] == ((4, 4), 'corner') and resB['TR']['events'][0][2] == 'corner')
claim('In the first example LT works and TL does not; BL works and LB does not.',
      resA['LT']['ok'] and not resA['TL']['ok'] and resA['BL']['ok'] and not resA['LB']['ok'])
contacts = {'LR': ((0, Fr(9, 7)), (4, Fr(17, 7))), 'RL': ((4, Fr(5, 3)), (0, Fr(23, 9))),
            'BT': ((Fr(7, 6), 0), (Fr(11, 6), 4)), 'TB': ((Fr(13, 10), 4), (Fr(17, 10), 0)),
            'LT': ((0, Fr(7, 3)), (Fr(5, 4), 4)), 'BL': ((Fr(1, 4), 0), (0, Fr(1, 3))),
            'RT': ((4, Fr(17, 5)), (Fr(13, 4), 4)), 'BR': ((Fr(9, 4), 0), (4, Fr(7, 5)))}
got = {k: tuple(e[1] for e in resA[k]['events']) for k in contacts}
claim('Contact pairs are LR: (0, 9/7) then (4, 17/7); RL: (4, 5/3) then (0, 23/9); BT: (7/6, 0) then (11/6, 4); TB: '
      '(13/10, 4) then (17/10, 0).', all(got[k] == contacts[k] for k in ('LR', 'RL', 'BT', 'TB')),
      str({k: got[k] for k in ('LR', 'RL', 'BT', 'TB')}))
claim('Adjacent words are LT: (0, 7/3) then (5/4, 4); BL: (1/4, 0) then (0, 1/3); RT: (4, 17/5) then (13/4, 4); BR: '
      '(9/4, 0) then (4, 7/5).', all(got[k] == contacts[k] for k in ('LT', 'BL', 'RT', 'BR')),
      str({k: got[k] for k in ('LT', 'BL', 'RT', 'BR')}))
L2 = {'LR': 53, 'RL': 85, 'BT': 37, 'TB': 101, 'LT': 25, 'BL': 25, 'RT': 41, 'BR': 41}
claim('their squared lengths are LR 53, RL 85, BT 37, TB 101, LT 25, BL 25, RT 41, BR 41, so LT and BL tie for shortest '
      'in that family.', all(resA[k]['len2'] == v for k, v in L2.items()), str({k: resA[k]['len2'] for k in L2}))

# general statements, by brute force over lattice and half-lattice S, F in several rectangles
same_wall = opp = adj = adj_corner = True
cnt = 0
for Wd, Ht in ((4, 4), (5, 3), (6, 4), (3, 5)):
    Wf, Hf = Fr(Wd), Fr(Ht)
    vals_x = [Fr(k, 2) for k in range(1, 2 * Wd)]
    vals_y = [Fr(k, 2) for k in range(1, 2 * Ht)]
    for sx, sy, fx, fy in product(vals_x, vals_y, vals_x, vals_y):
        if sx == fx or sy == fy:
            continue
        cnt += 1
        r = two_bounce_words((sx, sy), (fx, fy), Wf, Hf)
        same_wall &= not any(r[w + w]['ok'] for w in 'LRBT' if w + w in r)
        opp &= all(r[w]['ok'] for w in ('LR', 'RL', 'BT', 'TB'))
        for a, b in (('L', 'B'), ('L', 'T'), ('R', 'B'), ('R', 'T')):
            n_ok = r[a + b]['ok'] + r[b + a]['ok']
            corner = any(e[2] == 'corner' for e in r[a + b]['events'])
            adj &= n_ok == (0 if corner else 1)
claim('Same-wall words are impossible.', same_wall, f'{cnt} pairs S, F tested')
claim('Opposite-wall orders LR, RL, BT, TB always work.', opp)
claim('For each adjacent pair of walls, exactly one order works unless the candidate hits their corner, when neither works.', adj)

print('\nReturn visit, pages 4-5: Problem 2 (interior starts)')
b4 = boards(4)
launch = [b for b in b4 if b['w'] == 3]
main = [b for b in b4 if b['w'] == 6][0]
check('Problem 2 board: 6 wide, 4 high, square 22 mm units', (main['w'], main['h']) == (6, 4) and main['uniform'] and
      abs(main['cell_w'] / MM - 22) < 0.05 and abs(main['cell_h'] / MM - 22) < 0.05, f"{main['cell_w'] / MM:.2f} mm")
ws = [w for w in WD[4] if re.fullmatch('[A-O]', w[0])]
letters = {}
for (x, y) in main['dots']:
    px = main['x0'] + x * main['cell_w']
    py = main['y0'] + y * main['cell_h']
    near = [w for w in ws if 0 < w[1] - px < 12 and 0 < py - w[4] < 14]
    if len(near) == 1:
        letters[near[0][0]] = (round(x), round(y))
check('Problem 2: 15 lettered dots A-O at the interior points, A-E at height 3, F-J at 2, K-O at 1',
      len(letters) == 15 and all(letters[c] == (1 + i % 5, 3 - i // 5) for i, c in enumerate('ABCDEFGHIJKLMNO')),
      str(letters))


def interior_walk(x, y, Wd, Ht, limit=10000):
    dx = dy = 1
    x0, y0 = x, y
    for step in range(1, limit):
        x += dx
        y += dy
        if x in (0, Wd) and y in (0, Ht):
            return 'C', step
        if x in (0, Wd):
            dx = -dx
        if y in (0, Ht):
            dy = -dy
        if (x, y, dx, dy) == (x0, y0, 1, 1):
            return 'L', step
    return None, None


res2 = {c: interior_walk(*letters[c], 6, 4) for c in letters}
print('    ' + ', '.join(f'{c} {res2[c][0]} {res2[c][1]}' for c in sorted(res2)))
claim('the corner-finishing dots are (1, 1), (1, 3), (2, 2), (3, 1), (3, 3), (4, 2), (5, 1), (5, 3).',
      {v for c, v in letters.items() if res2[c][0] == 'C'} == {(1, 1), (1, 3), (2, 2), (3, 1), (3, 3), (4, 2), (5, 1), (5, 3)})
claim('On the printed letter map the corner starts are A,C,E,G,I,K,M,O; the looping starts are B,D,F,H,J,L,N.',
      sorted(c for c in res2 if res2[c][0] == 'C') == list('ACEGIKMO') and
      sorted(c for c in res2 if res2[c][0] == 'L') == list('BDFHJLN'))
claim('Every looping dot returns northeast after 24 diagonal unit steps.',
      all(res2[c][1] == 24 for c in res2 if res2[c][0] == 'L'))
claim('a corner is reached iff x − y is even. Of the 15 dots, eight reach corners and seven never do.',
      all((res2[c][0] == 'C') == ((letters[c][0] - letters[c][1]) % 2 == 0) for c in res2))


def state_at(x, y, Wd, Ht, n):
    dx = dy = 1
    for _ in range(n):
        x += dx
        y += dy
        if x in (0, Wd):
            dx = -dx
        if y in (0, Ht):
            dy = -dy
    return x, y, dx, dy


claim('At H=(3,2), the traveller is back at its dot after 12 steps facing SE, and first returns NE after 24',
      letters['H'] == (3, 2) and state_at(3, 2, 6, 4, 12) == (3, 2, 1, -1) and res2['H'] == ('L', 24))
gen = True
for a in range(1, 9):
    for b in range(1, 9):
        for x in range(1, a):
            for y in range(1, b):
                kind, n = interior_walk(x, y, a, b)
                gen &= (kind == 'C') == ((x - y) % gcd(a, b) == 0)
                if kind == 'L':
                    gen &= n == 2 * a * b // gcd(a, b)
claim('the corner condition becomes x − y divisible by gcd(a, b) for integer northeast starts, and a non-corner '
      'full-state return is 2 lcm(a, b).', gen)
for b in launch:
    pass
# launch strip: (2,1) NE, then (3,2) NW, then (2,3) SW on a 3-by-3 board
p4 = PG[3]
lb = sorted(launch, key=lambda b: b['x0'])
dots_l = [b['dots'] for b in lb]
check('Problem 2 launch strip: three 3 by 3 boards; the token dot at (2,1), (3,2), (2,3)',
      len(lb) == 3 and all((b['w'], b['h']) == (3, 3) for b in lb) and dots_l == [[(2.0, 1.0)], [(3.0, 2.0)], [(2.0, 3.0)]],
      str(dots_l))
b5 = boards(5)
check('Problem 2 workspace: two 6 by 4 boards of 18 mm squares',
      len(b5) == 2 and all((b['w'], b['h']) == (6, 4) and abs(b['cell_w'] / MM - 18) < 0.05 and
                           abs(b['cell_h'] / MM - 18) < 0.05 for b in b5))

print('\nReturn visit, pages 6-7: Problem 3 (crossings)')
b6 = boards(6)
sizes = [(b['w'], b['h']) for b in b6]
labels6 = [w for w in WD[6] if w[0] in ('wide,', 'high')]
check('Problem 3 boards: 2 by 3, 3 by 4, 4 by 5, 4 by 6, 12.5 mm squares, S dot at the bottom left',
      sorted(sizes) == [(2, 3), (3, 4), (4, 5), (4, 6)] and
      all(abs(b['cell_w'] / MM - 12.5) < 0.05 and abs(b['cell_h'] / MM - 12.5) < 0.05 and b['dots'] == [(0.0, 0.0)]
          for b in b6), str(sizes))
t6 = norm(subprocess.run(['pdftotext', '-f', '6', '-l', '6', str(PDF['rv']), '-'], capture_output=True, text=True).stdout)
check('Problem 3 labels name the drawn sizes', all(f'{w} wide, {h} high' in t6 for w, h in sizes))
cr = {s: crossings(*s) for s in sizes}
print('    ' + '; '.join(f'{w} by {h}: {cr[(w, h)]["count"]} at {cr[(w, h)]["lattice"]}' for w, h in sizes))
claim('The ordinary 45-degree paths on 2-by-3, 3-by-4 and 4-by-5 tables have respectively 1,3 and 6 interior crossing '
      'points. A 4-by-6 table has one', [cr[s]['count'] for s in ((2, 3), (3, 4), (4, 5), (4, 6))] == [1, 3, 6, 1])
claim('For 2-by-3 the point is (1, 1). For 3-by-4 they are (1, 1), (1, 3), (2, 2). For 4-by-5 they are (1, 1), (1, 3), '
      '(2, 2), (2, 4), (3, 1), (3, 3). In 4-by-6 the single point is (2, 2).',
      cr[(2, 3)]['lattice'] == [(1, 1)] and cr[(3, 4)]['lattice'] == [(1, 1), (1, 3), (2, 2)] and
      cr[(4, 5)]['lattice'] == [(1, 1), (1, 3), (2, 2), (2, 4), (3, 1), (3, 3)] and cr[(4, 6)]['lattice'] == [(2, 2)])
b7 = boards(7)
check('Problem 3 workspace: 12 by 12 grid of 12.5 mm squares with S at the bottom left',
      len(b7) == 1 and (b7[0]['w'], b7[0]['h']) == (12, 12) and b7[0]['dots'] == [(0.0, 0.0)] and
      abs(b7[0]['cell_w'] / MM - 12.5) < 0.05)
ten = [(a, b) for a in range(1, 13) for b in range(1, 13) if crossings(a, b)['count'] == 10]
claim('With positive integer dimensions at most 12, all solutions are 3-by-11, 11-by-3, 5-by-6, 6-by-5, 10-by-12 and '
      '12-by-10.', sorted(ten) == sorted([(3, 11), (11, 3), (5, 6), (6, 5), (10, 12), (12, 10)]), str(ten))
formula = all(crossings(a, b)['count'] == (a // gcd(a, b) - 1) * (b // gcd(a, b) - 1) // 2 and
              crossings(a, b)['retraced'] == 0 and not crossings(a, b)['centre']
              for a in range(1, 31) for b in range(1, 31))
claim('There are (u−1)(v−1)/2 distinct interior transverse crossing points before the first terminal corner. No segment '
      'is retraced.', formula)
claim('The positive factor pairs give reduced rectangles 2-by-21, 3-by-11, 5-by-6 and their swaps.',
      sorted((u, v) for u in range(1, 40) for v in range(u, 40) if gcd(u, v) == 1 and (u - 1) * (v - 1) == 20) ==
      [(2, 21), (3, 11), (5, 6)])

print(f'\n{n_checks} checks, {len(problems)} mismatches')
for p in problems:
    print('  MISMATCH:', p)
