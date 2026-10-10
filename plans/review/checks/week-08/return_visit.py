"""Check the Week 8 return-visit companion (student pages and adult guide).

Reads the delivered student PDF: the counters in each pile start (page 1),
every coin row with its wall, squares and coins (pages 2-3), and every rook
board with its star and token (pages 4-5).  Solves each start by game-tree
search (games.py), and compares with the printed numbers and with the adult
guide's stated answers, after confirming each quoted guide sentence is in the
delivered guide PDF.  Output saved as return_visit.out.
"""
import os
import re
import subprocess
import sys
sys.dont_write_bytecode = True  # never leave __pycache__ beside the packet sources
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfdraw  # noqa: E402
import repo  # noqa: E402
from games import nim_P, nim_winning_moves, coin_P, coin_moves, two_rooks_P, rook_P, rook_moves  # noqa: E402

N_OK = N_BAD = N_NOTE = 0


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('’', "'"), ('“', '"'), ('”', '"'), ('–', '-'), ('−', '-')):
        s = s.replace(a, b)
    s = re.sub(r'\s+', ' ', s).strip()
    return re.sub(r'([,;]) ', r'\1', s)   # math-mode tuples print as (1, 2; 1, 2)


GUIDE = norm(subprocess.run(['pdftotext', repo.RV_GUIDE, '-'], capture_output=True, text=True).stdout)


def quote(q):
    global N_BAD
    if norm(q) not in GUIDE:
        N_BAD += 1
        print('MISMATCH  guide quote not found in delivered PDF: %r' % q)


def check(label, got, want, q=None):
    global N_OK, N_BAD
    if q:
        quote(q)
    if got == want:
        N_OK += 1
        print('OK        %s: %s' % (label, got))
    else:
        N_BAD += 1
        print('MISMATCH  %s: computed %s, page/guide %s' % (label, got, want))


def note(m):
    global N_NOTE
    N_NOTE += 1
    print('NOTE      ' + m)


def words(page):
    out = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), repo.RV_STUDENT, '-'],
                         capture_output=True, text=True).stdout
    return [(float(a) / 72, float(b) / 72, float(c) / 72, float(d) / 72, t) for a, b, c, d, t in
            re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', out)]


def circles(paths, grey):
    out = []
    for p in paths:
        if p['fill'] and p['curves'] == 4 and all(abs(c - grey) < 0.02 for c in p['fc']):
            x0, y0, x1, y1 = pdfdraw.bbox(p)
            out.append(((x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2))
    return out


def starts_labels(ws):
    res = []
    for k, w in enumerate(ws):
        if w[4] == 'Start' and k + 1 < len(ws) and ws[k + 1][4].isdigit():
            res.append((int(ws[k + 1][4]), w[0], w[1]))
    return res


pages = pdfdraw.read(repo.RV_STUDENT)
who = lambda P: 'second' if P else 'first'  # noqa: E731

# ------------------------------------------------------------ page 1 ---
print('=' * 72)
print('Problem 1: last counter loses (page 1)')
print('=' * 72)
W, H, paths = pages[0]
ws = words(1)
labs = starts_labels(ws)
cnt = circles(paths, 0.875)
piles1 = {}
printed = {}
for (n, x, y) in labs:
    mine = [c for c in cnt if x <= c[0] <= x + 1.5 and y < c[1] < y + 0.9]
    cols = sorted({round(c[0], 2) for c in mine})
    # pile columns are .48 in apart starting .36 in from the card's left (source); read printed numbers too
    nums = [w for w in ws if y + 0.75 < w[1] < y + 1.0 and x <= w[0] <= x + 1.4 and w[4].isdigit()]
    printed[n] = tuple(int(w[4]) for w in sorted(nums))
    count = []
    for w in sorted(nums):
        cx = (w[0] + w[2]) / 2
        count.append(sum(1 for c in mine if abs(c[0] - cx) < 0.12))
    piles1[n] = tuple(count)
check('page 1: drawn counters per pile equal the printed numbers, Starts 1-12',
      all(piles1[n] == printed[n] for n in piles1), True)
print('          starts:', [piles1[n] for n in sorted(piles1)])
res = [who(nim_P(piles1[n], misere=True)) for n in sorted(piles1)]
check('P1 winners, Starts 1-12 (misere search)', res,
      ['second', 'first', 'first', 'second', 'first', 'second', 'first', 'second', 'first', 'first', 'second', 'first'],
      'On page 1, starts 1–12 favour respectively second, first, first, second, first, second, first, second, first, first, second, first.')
leave = {2: (1,), 3: (1,), 5: (2, 2), 7: (1,), 9: (1, 1, 1), 10: (2, 2), 12: (2, 3, 1)}
quote('Winning first moves in starts 2,3,5,7,9,10,12 can leave respectively (1), (1), (2,2), (1), (1,1,1), (2,2), (2,3,1).')
ok = True
for n, target in leave.items():
    res_list = [tuple(x for x in q if x) for q, mv in nim_winning_moves(piles1[n], misere=True)]
    ok &= sorted(target) in [sorted(r) for r in res_list]
check('P1 the guide\'s winning first moves are winning moves', ok, True)
# two-pile rule from the guide
quote('One pile of one loses. One pile larger than one wins by leaving exactly one. Two piles (1,1) win: take either singleton and leave one for the opponent.')
ok = True
for a in range(0, 15):
    for b in range(0, 15):
        if a + b == 0:
            continue
        P = nim_P((a, b), misere=True)
        rule = (sorted((a, b)) == [0, 1]) or (a == b and a >= 2)
        ok &= P == rule
check('P1 two-pile rule: second player wins exactly at {0,1} and equal piles >= 2 (piles 0-14)', ok, True,
      'Unequal two-pile starts with a larger pile win: if the small pile is at least two, equalise; if it is one, remove the larger pile completely, leaving one.')
# general misere rule as stated in the destination
ok = True
from itertools import combinations_with_replacement as cwr  # noqa: E402
for k in (1, 2, 3, 4):
    for s in cwr(range(0, 9 if k < 4 else 6), k):
        if sum(s) == 0:
            continue
        P = nim_P(s, misere=True)
        if max(s) <= 1:
            rule = sum(s) % 2 == 1
        else:
            x = 0
            for v in s:
                x ^= v
            rule = x == 0
        ok &= P == rule
check('destination: misere P-positions = odd singletons, or xor 0 with a pile > 1 (1-4 piles)', ok, True,
      'If all nonempty piles have size one, the next player loses exactly when their number is odd. If at least one pile exceeds one, the losing positions are the ordinary zero-xor positions.')
# one-large-pile strategy
ok = True
for s in cwr(range(0, 10), 4):
    big = [v for v in s if v >= 2]
    if len(big) != 1:
        continue
    singles = sum(1 for v in s if v == 1)
    target = list(s)
    i = s.index(big[0])
    target[i] = 1 if singles % 2 == 0 else 0
    ok &= nim_P(target, misere=True)
check('guide: one large pile -> reduce to one if singletons even, remove if odd; opponent loses (4 piles 0-9)', ok, True,
      'reduce it to one when the existing singleton count is even, or remove it when that count is odd.')
quote('If only one large pile remains, its size determines which final singletons to leave')
note('RV guide, Problem 1 "General rule": "If only one large pile remains, its size determines which final singletons '
     'to leave" - the choice depends only on the parity of the singleton count (as the rest of the sentence says), never on the large pile\'s size.')

# ------------------------------------------------------------ pages 2-3 ---
print('=' * 72)
print('Problem 2: coin row (pages 2-3)')
print('=' * 72)
coin_rows = {}
for pg in (2, 3):
    W, H, paths = pages[pg - 1]
    ws = words(pg)
    walls = []
    for p in paths:
        if p['stroke'] and not p['fill'] and len(p['sub']) == 1 and len(p['sub'][0]) == 2 and p['lw'] * 72 > 2.0:
            (x0, y0), (x1, y1) = p['sub'][0]
            if abs(x0 - x1) < 1e-3:
                walls.append((x0, min(y0, y1), max(y0, y1)))
    coins = circles(paths, 0.675)
    labs = starts_labels(ws)
    for (x, y0, y1) in walls:
        s = y1 - y0
        # vertical square lines in this row
        vl = sorted({round(p['sub'][0][0][0], 4) for p in paths if p['stroke'] and not p['fill'] and len(p['sub']) == 1
                     and len(p['sub'][0]) == 2 and abs(p['sub'][0][0][0] - p['sub'][0][1][0]) < 1e-4
                     and abs(min(p['sub'][0][0][1], p['sub'][0][1][1]) - y0) < 1e-3 and x - 1e-3 <= p['sub'][0][0][0] <= x + 12 * s + 0.01})
        mine = [c for c in coins if x < c[0] < x + 12 * s and y0 < c[1] < y1]
        squares = sorted(int((c[0] - x) // s) + 1 for c in mine)
        offs = max([abs(c[0] - (x + (int((c[0] - x) // s) + .5) * s)) for c in mine] + [0])
        numbers = [w[4] for w in sorted(ws, key=lambda w: w[0]) if y1 < w[1] < y1 + 0.35 and x - 0.05 < w[0] < x + 12 * s]
        lab = [n for (n, lx, ly) in labs if abs(lx - x - 0.0) < 0.3 and 0 < y0 - ly < 0.5]
        key = (pg, lab[0] if lab else 'unlabelled at x=%.2f y=%.2f' % (x, y0))
        coin_rows[key] = squares
        print('          page %d row %-26s squares %d of %.3f in (lines %d), numbers %s, coins on %s%s' % (
            pg, key[1], round((vl[-1] - vl[0]) / s) if vl else -1, s, len(vl),
            ''.join(numbers) == ''.join(str(i) for i in range(1, 13)), squares,
            '' if offs < 0.01 else ' (coin off-centre %.3f)' % offs))
starts2 = {k[1]: v for k, v in coin_rows.items() if isinstance(k[1], int)}
check('coin starts read from the page', [tuple(starts2[n]) for n in range(1, 15)],
      [(1, 2), (1, 4), (4, 5), (4, 6), (7, 8), (7, 10), (1, 2, 3), (1, 4, 6), (2, 3, 5), (2, 4, 7), (3, 4, 7), (3, 5, 9),
       (4, 7, 11), (4, 7, 12)])
res = [who(coin_P(tuple(starts2[n]))) for n in range(1, 15)]
check('P2 winners Starts 1-6 (search)', res[:6], ['second', 'first', 'second', 'first', 'second', 'first'],
      'Page 2 starts 1–6 favour second, first, second, first, second, first.')
check('P2 winners Starts 7-14 (search)', res[6:], ['second', 'first', 'second', 'first', 'second', 'first', 'second', 'first'],
      'Page 3 starts 7–14 favour second, first, second, first, second, first, second, first.')
gaps = [(c[0] - 1, c[2] - c[1] - 1) for c in (tuple(starts2[n]) for n in range(7, 15))]
check('P2 recorded gap pairs (a, b) for Starts 7-14', gaps, [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4)])
# worked example
ex = [v for k, v in coin_rows.items() if not isinstance(k[1], int)]
print('          unlabelled rows (worked example and play strips):', ex)
check('worked example: (4,10) -> (2,10) is a legal slide', (2, 10) in list(coin_moves((4, 10))), True,
      'The non-task visual moves square 4 to 2 while the coin at 10 stays fixed; no jump occurs.')
# general paired-gap rule vs search for up to 4 coins on 12 squares
from itertools import combinations  # noqa: E402
ok = True
for k in (1, 2, 3, 4):
    for c in combinations(range(1, 13), k):
        g = []
        cc = list(c)
        if len(cc) % 2:
            g.append(cc[0] - 1)
            cc = cc[1:]
        for i in range(0, len(cc), 2):
            g.append(cc[i + 1] - cc[i] - 1)
        x = 0
        for v in g:
            x ^= v
        ok &= (x == 0) == coin_P(c)
check('destination: pair from the right, xor of recorded gaps = 0 <=> second player (1-4 coins, 12 squares)', ok, True,
      'Pair coins from the right. Record empty squares inside each pair, plus the gap before an unpaired leftmost coin if there is one. The position loses exactly when these gap sizes have xor zero.')
ok = all(coin_P((a, b)) == (b == a + 1) for a, b in combinations(range(1, 13), 2))
check('two coins: second player exactly when adjacent', ok, True, 'For two coins, adjacency alone decides a losing start.')
ok = all(coin_P(c) == (c[0] - 1 == c[2] - c[1] - 1) for c in combinations(range(1, 13), 3))
check('three coins: second player exactly when a = b', ok, True)

# ------------------------------------------------------------ pages 4-5 ---
print('=' * 72)
print('Problem 3: two rook boards (pages 4-5)')
print('=' * 72)


def stars(paths):
    out = []
    for p in paths:
        if p['fill'] and not p['curves'] and len(p['sub']) == 1 and len(p['sub'][0]) == 11 \
                and all(abs(c - 0.9) < 0.02 for c in p['fc']):
            pts = p['sub'][0][:10]
            out.append((sum(x for x, y in pts) / 10, sum(y for x, y in pts) / 10))
    return out


boards_by_page = {}
for pg in (4, 5):
    W, H, paths = pages[pg - 1]
    ws = words(pg)
    segs = [p['sub'] for p in paths if p['stroke'] and not p['fill'] and not p['curves']]
    vlines, hlines = [], []
    for sub in segs:
        for s in sub:
            if len(s) == 2:
                (x0, y0), (x1, y1) = s
                if abs(x0 - x1) < 1e-4:
                    vlines.append((x0, min(y0, y1), max(y0, y1)))
                elif abs(y0 - y1) < 1e-4:
                    hlines.append((y0, min(x0, x1), max(x0, x1)))
    dots = circles(paths, 0.675)
    bl = []
    for (sx, sy) in stars(paths):
        left = max(v for v in vlines if v[0] < sx and v[1] < sy < v[2])
        bottom = min(h for h in hlines if h[0] > sy and h[1] < sx < h[2])
        s = 2 * (sx - left[0])
        x0, yb = left[0], bottom[0]
        nv = sorted({round(v[0], 3) for v in vlines if x0 - 1e-3 <= v[0] <= x0 + 4 * s + 1e-3 and v[1] < yb - s / 2 < v[2]})
        nh = sorted({round(h[0], 3) for h in hlines if yb - 4 * s - 1e-3 <= h[0] <= yb + 1e-3 and h[1] < x0 + s / 2 < h[2]})
        mine = [d for d in dots if x0 < d[0] < x0 + 4 * s and yb - 4 * s < d[1] < yb]
        tok = [(int((d[0] - x0) // s), int((yb - d[1]) // s)) for d in mine]
        above = [w[4] for w in ws if abs((w[0] + w[2]) / 2 - (x0 + 2 * s)) < 0.15 and 0 < yb - 4 * s - w[3] < 0.15]
        bl.append({'x0': x0, 'yb': yb, 's': s, 'lines': (len(nv), len(nh)), 'token': tok, 'label': above})
    boards_by_page[pg] = bl
    for b in sorted(bl, key=lambda b: (round(b['yb'], 1), b['x0'])):
        print('          page %d board at (%.2f, %.2f) square %.3f in, lines %s, label %s, token %s' % (
            pg, b['x0'], b['yb'], b['s'], b['lines'], b['label'], b['token']))
# page 5 starts: label "Start N" above-left of an A board
ws = words(5)
labs = starts_labels(ws)
pairs = {}
for (n, lx, ly) in labs:
    near = sorted([b for b in boards_by_page[5] if abs(b['x0'] - lx) < 0.1 and 0 < b['yb'] - ly < 2.0], key=lambda b: b['x0'])
    A = near[0]
    B = min([b for b in boards_by_page[5] if abs(b['yb'] - A['yb']) < 0.01 and b['x0'] > A['x0']], key=lambda b: b['x0'])
    pairs[n] = (tuple(A['token'][0]), tuple(B['token'][0]), A['label'], B['label'])
got = [(pairs[n][0], pairs[n][1]) for n in range(1, 7)]
check('page 5 pairs read from the page', got,
      [((1, 2), (1, 2)), ((1, 1), (2, 2)), ((1, 0), (2, 3)), ((1, 3), (2, 2)), ((0, 2), (1, 3)), ((0, 1), (1, 3))])
quote('In coordinates measured right/up from each star they are (1,2;1,2), (1,1;2,2), (1,0;2,3), (1,3;2,2), (0,2;1,3), (0,1;1,3).')
check('page 5 board labels A (left) and B (right)', all(pairs[n][2] == ['A'] and pairs[n][3] == ['B'] for n in pairs), True)
res = [who(two_rooks_P(*a, *b)) for a, b in got]
check('P3 winners Starts 1-6 (search)', res, ['second', 'second', 'second', 'first', 'second', 'first'],
      'Starts 1–6 favour second, second, second, first, second, first.')
check('P3 "each board alone first-player" in Starts 3 and 5 (so they already answer the invention task)',
      [(rook_P(*got[i][0]), rook_P(*got[i][1])) for i in (2, 4)], [(False, False), (False, False)])
check('P3 guide example (0,3;1,2): different starts, each alone first, together second',
      (rook_P(0, 3), rook_P(1, 2), two_rooks_P(0, 3, 1, 2)), (False, False, True),
      'A further distinct cancelling pair is (0,3;1,2), both individually first-player wins with value 3.')
# worked example on page 4: before / after A / after B
p4 = sorted(boards_by_page[4], key=lambda b: (round(b['yb'], 1), b['x0']))
small = [b for b in p4 if b['s'] < 0.3]
big = [b for b in p4 if b['s'] > 0.5]
tok = [tuple(b['token'][0]) if b['token'] else None for b in small]
check('page 4 worked turns: Before (A, B), after A left 2, after B down 2', tok,
      [(2, 2), (1, 3), (0, 2), (1, 3), (0, 2), (1, 1)],
      'The worked non-task turns change A from (2,2) to (0,2), then B from (1,3) to (1,1); only one board moves each turn.')
check('worked turns are single legal moves', ((0, 2) in list(rook_moves(2, 2)), (1, 1) in list(rook_moves(1, 3))), (True, True))
check('page 4 play boards: two 4-by-4 boards of 0.85 in, no token', [(round(b['s'], 3), b['lines'], b['token']) for b in big],
      [(0.85, (5, 5), []), (0.85, (5, 5), [])], 'Page 4 has two independent 4-by-4 rook boards with 0.85-inch squares (3.4 inches square), one token each.')
# general: the four distances act as four Nim piles
ok = True
for x in range(5):
    for y in range(5):
        for u in range(5):
            for v in range(5):
                ok &= two_rooks_P(x, y, u, v) == (x ^ y ^ u ^ v == 0)
check('state: second player exactly when x xor y xor u xor v = 0 (all 4-by-4 pairs and beyond, 0-4)', ok, True)
check('same totals: (0,2)+(2,0) loses, (1,1)+(2,0) wins', (two_rooks_P(0, 2, 2, 0), two_rooks_P(1, 1, 2, 0)), (True, False),
      'A token at (0,2) has coordinate xor 2, while a token at (1,1) has xor 0; both distances total two. Pair either with (2,0). The first combined position has xor zero and loses, the second has xor 2 and wins.')
ok = all(two_rooks_P(a, a, b, b) for a in range(6) for b in range(6))
check('two losing components together still lose (diagonal + diagonal, 0-5)', ok, True)
ok = all(two_rooks_P(a, b, a, b) for a in range(6) for b in range(6))
check('two identical starts always lose (copying)', ok, True)
n_inv = sum(1 for a in range(4) for b in range(4) for c in range(4) for d in range(4)
            if (a, b) < (c, d) and not rook_P(a, b) and not rook_P(c, d) and two_rooks_P(a, b, c, d))
print('          (for interest) unordered pairs of different off-diagonal 4-by-4 starts that cancel: %d' % n_inv)

# materials arithmetic
check('materials: 12 x 0.85 = 10.2, 4 x 0.85 = 3.4, 4 x 0.65 = 2.6 < 2.9',
      (round(12 * .85, 2), round(4 * .85, 2), 4 * .65 < 2.9), (10.2, 3.4, True))
check('largest printed pile has four counters', max(max(v) for v in piles1.values()), 4,
      'The largest printed pile has four counters')

print('=' * 72)
print('Summary: %d OK, %d MISMATCH, %d NOTE' % (N_OK, N_BAD, N_NOTE))
