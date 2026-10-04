"""Recompute every answer printed in the Week 4 adult guide from the student pages.

It reads the TikZ in final/src/*.tex (the sources of the final student PDFs): ring dots, start dots,
labels, the drawn stars, the K-1 pictures, the code letters and the wheel letters, all from their
coordinates. It does not import or trust gen.py, tikzlib.py, check.py or the reviews. Each answer is
recomputed by simulating the rule on the page, and then compared with CLAIMS, which holds exactly what
facilitator.tex prints. Run: python3 check_answers.py   (exits non-zero on any mismatch)."""
import math
import os
import re
import sys
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, '..', 'src'))
DIC = '/usr/share/hunspell/en_US'
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUM = r'(-?\d+(?:\.\d+)?)'
PT = rf'\({NUM},{NUM}\)'
FAIL = []

# ----------------------------------------------------------------------------- what the guide prints
CLAIMS = {
    # K-1
    'K P1': {1: True, 2: False, 3: True},                # ring of 4: hop lands on every dot?
    'K P2': {1: True, 2: True, 3: True},                 # ring of 5
    'K P3': {1: True, 2: False, 3: False},               # ring of 6
    'K P1-3 dots reached': {(4, 1): 4, (4, 2): 2, (4, 3): 4, (5, 1): 5, (5, 2): 5, (5, 3): 5,
                            (6, 1): 6, (6, 2): 3, (6, 3): 2},
    'K P4': [(6, 2, 2), (6, 3, 3), (8, 2, 2), (8, 3, 1)],  # (dots, hop, starts) in page order
    'K P5': [[1, 4], [2, 3], [1, 5], [2, 4], [3]],          # pentagon, 5-star, hexagon, 6-star, 3 lines
    'K P6': {1: True, 2: True, 3: True},
    'K P7': {4: True, 5: True, 6: True},
    'K ring': ['sun', 'moon', 'heart', 'tree', 'fish', 'house'],
    'K P8': [['heart', 'house', 'sun'], ['fish', 'moon', 'heart'], ['sun', 'tree', 'fish']],
    'K P9': [('sun', 1, 'moon', 5), ('moon', 2, 'tree', 4), ('fish', 3, 'moon', 3), ('heart', 4, 'sun', 2)],
    'K P10': (3, {'moon': 'fish', 'heart': 'house', 'fish': 'moon', 'house': 'heart'}),
    # 2-3
    'M P1': [(8, 1, 1), (8, 2, 2), (8, 3, 1), (8, 4, 4)],
    'M P2': [(10, 2, 2), (10, 3, 1), (10, 4, 2), (10, 5, 5)],
    'M P3': [(12, 2, 2), (12, 3, 3), (12, 4, 4), (12, 5, 1), (12, 6, 6)],
    'M P4': ('D', ['STAR', 'FOX', 'WHEEL', 'PENCIL', 'I CAN DRAW A STAR']),
    'M P6': [(9, 2, 1), (15, 5, 5), (16, 6, 2), (12, 8, 4)],
    'M P7': {9: [6], 16: [], 18: [15], 15: [6, 9, 12]},
    'M P8': [('H', 'A STAR CAN HAVE TEN POINTS'), ('Q', 'MEET ME BY THE BIG TREE')],
    'M P9': {'D': 'X', 'H': 'T', 'N': 'N', 'W': 'E'},
    # 4-5
    'U P1': [(12, k, p) for k, p in zip(range(1, 7), (1, 2, 3, 4, 1, 6))],
    'U P2': [(10, 4, 2), (9, 6, 3), (15, 10, 5), (16, 12, 4), (18, 8, 2), (24, 9, 3)],
    'U P3': [(20, 8, 4), (24, 10, 2), (30, 12, 6), (36, 27, 9), (17, 5, 1), (100, 35, 5), (60, 45, 15)],
    'U P4': [('J', 'I DREW A STAR WITH TWELVE POINTS'), ('S', 'WE MEET AT NOON BY THE BIG TREE'),
             ('X', 'BALLOON')],
    'U P4 last': {'D': 'JOLLY', 'J': 'DIFFS', 'K': 'CHEER'},   # every setting giving a dictionary word
    'U P6': [('H', 'K', 'R'), ('D', 'F', 'I'), ('T', 'M', 'F'), ('P', 'L', 'A'), ('H', 'T', 'A')],
    'U P8': [5, 7, 11, 13, 17, 19],
    'U P9': [(15, [6, 9]), (20, [5, 15]), (14, [6, 8]), (21, [6, 15])],   # page order: TL, TR, BL, BR
    'U P11 C': 'ACEGIKMOQSUWY',
    'U P11': 'BDFHJLPRTVXZ',
    'U P12': {2: dict(self=[0], twice=[(8, 16)], lines=22), 3: dict(self=[0, 12], twice=[(3, 9), (6, 18), (15, 21)], lines=19)},
    'wheel': (5.5, 4.0),
    'K dot diameter': 0.8,
}


def claim(key, value):
    ok = CLAIMS[key] == value
    print(f"{'ok ' if ok else 'BAD'} {key}: {value}")
    if not ok:
        FAIL.append((key, CLAIMS[key], value))


# ----------------------------------------------------------------------------- reading the pages
def load(name):
    """Pictures of a packet in page order: dict(page, prob, body, cont)."""
    body = open(os.path.join(SRC, name + '.tex')).read().split('\\begin{document}')[1]
    out, prob = [], None
    for pg, text in enumerate(body.split('\\newpage'), 1):
        for m in re.finditer(r'\\prob\{(\d+)\}|\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}', text, re.S):
            if m.group(1):
                prob = int(m.group(1))
                continue
            cont = text[max(0, m.start() - 40):m.start()].endswith('\\vspace{0.12in}\\noindent')
            out.append(dict(page=pg, prob=prob, body=m.group(2), cont=cont))
    return out


def probtext(name, n):
    body = open(os.path.join(SRC, name + '.tex')).read()
    m = re.search(r'\\prob\{%d\}(.*?)\\par' % n, body, re.S)
    return m.group(1)


def nodes(b):
    return [(opt, float(x), float(y), t) for opt, x, y, t in
            re.findall(rf'\\node\[([^\]]*)\] at {PT} \{{(.*?)\}};', b)]


def circles(b):
    return [(cmd, opt, float(x), float(y), float(r)) for cmd, opt, x, y, r in
            re.findall(rf'\\(fill|filldraw|draw)(?:\[([^\]]*)\])? {PT} circle \({NUM}\)', b)]


def cw_index(x, y, cx, cy, n):
    a = (90 - math.degrees(math.atan2(y - cy, x - cx))) % 360
    i = a / (360 / n)
    assert abs(i - round(i)) < 0.02, (x, y, n)
    return round(i) % n


def rings(b):
    """Every ring in a picture: centre, radius, dots in clockwise order from the top, start dot."""
    cs = circles(b)
    out = []
    for cmd, opt, cx, cy, R in cs:
        if cmd != 'draw' or not opt or not re.match(r'black!(25|35)', opt):
            continue
        dots = [c for c in cs if c[0] in ('fill', 'filldraw') and abs(math.hypot(c[2] - cx, c[3] - cy) - R) < 2e-3]
        n = len(dots)
        idx = {cw_index(x, y, cx, cy, n): (cmd2, opt2, x, y, r) for cmd2, opt2, x, y, r in dots}
        assert sorted(idx) == list(range(n)), (n, sorted(idx))
        black = [i for i, d in idx.items() if d[0] == 'fill']
        out.append(dict(cx=cx, cy=cy, R=R, n=n, dots=idx, black=black, dot_r=dots[0][4]))
    return out


def arrows_clockwise(b):
    arcs = re.findall(r'arc\[start angle=(-?[\d.]+), end angle=(-?[\d.]+)', b)
    return all(float(e) < float(s) for s, e in arcs) and ('-{Stealth' in b if arcs else True)


def segments(b):
    """Straight black lines of a drawn star: list of (p, q)."""
    segs = []
    for opt, path in re.findall(r'\\draw\[(black, line width=[^\]]*)\] ([^;]*);', b):
        pts = [(float(x), float(y)) for x, y in re.findall(PT, path)]
        closed = path.rstrip().endswith('cycle')
        for i in range(len(pts) - 1):
            segs.append((pts[i], pts[i + 1]))
        if closed:
            segs.append((pts[-1], pts[0]))
    return segs


def drawing_to_chords(segs):
    """Dots are the ends of the lines (every dot gets a line). Return n and the chord set."""
    vs = sorted({(round(x, 3), round(y, 3)) for s in segs for x, y in s})
    cx = sum(x for x, _ in vs) / len(vs)
    cy = sum(y for _, y in vs) / len(vs)
    n = len(vs)
    idx = {v: cw_index(v[0], v[1], cx, cy, n) for v in vs}
    assert sorted(idx.values()) == list(range(n))
    ch = {frozenset((idx[(round(p[0], 3), round(p[1], 3))], idx[(round(q[0], 3), round(q[1], 3))])) for p, q in segs}
    return n, ch


# ----------------------------------------------------------------------------- the rules, simulated
def walk(n, k, s=0):
    """Dots the counter lands on from s, hopping k clockwise, until it is back at s."""
    seen, j = [s], (s + k) % n
    while j != s:
        seen.append(j)
        j = (j + k) % n
    return seen


def draw(n, k, choose=min):
    """The packet rule: start, hop until back; while a dot has no line, start again there with the same
    hop. Returns (number of starts, set of chords). `choose` picks which empty dot to restart at."""
    lined, chords, starts, s = set(), set(), 0, 0
    while True:
        starts += 1
        for a in walk(n, k, s):
            b = (a + k) % n
            if a != b:
                chords.add(frozenset((a, b)))
                lined |= {a, b}
        empty = [d for d in range(n) if d not in lined]
        if not empty:
            return starts, chords
        s = choose(empty)


def starts(n, k):
    a, ch1 = draw(n, k, min)
    b, ch2 = draw(n, k, max)
    assert a == b and ch1 == ch2   # the count does not depend on where you restart
    return a


def chords(n, k):
    return draw(n, k)[1]


def shape(n, k):
    g = gcd(n, k)
    m, j = n // g, (k // g) % (n // g)
    j = min(j, m - j)
    names = {3: 'triangle', 4: 'square', 5: 'pentagon', 6: 'hexagon', 8: 'octagon'}
    one = 'segment' if m == 2 else (names.get(m, f'{m}-gon') if j == 1 else f'{{{m}/{j}}} star')
    return f"{g} x {one}"


# ----------------------------------------------------------------------------- K-1 pictures
def classify(cmds, cx, cy):
    if any('ellipse' in c for c in cmds):
        return 'fish'
    if sum('line cap=round' in c for c in cmds) == 8:
        return 'sun'
    paths = [c for c in cmds if ' -- ' in c]
    closed = [c for c in paths if c.rstrip(';').rstrip().endswith('cycle')]
    if len(paths) == 2 and len(closed) == 1:
        return 'tree'
    if len(paths) == 3 and len(closed) == 1:
        return 'house'
    if len(paths) == 1:
        pts = [(float(x), float(y)) for x, y in re.findall(PT, paths[0])]
        mx = sum(x for x, _ in pts) / len(pts)
        span = max(x for x, _ in pts) - min(x for x, _ in pts)
        return 'heart' if abs(mx - cx) < 0.03 * span else 'moon'
    raise ValueError(cmds)


def frames(b):
    """Picture frames (white circles of a picture ring, and 1.2pt boxes) with the icon drawn in each."""
    fr = []
    for cmd, opt, x, y, r in circles(b):
        if cmd == 'filldraw' and 'line width=1.4pt' in (opt or ''):
            fr.append(['ring', x, y, r, []])
    for x0, y0, x1, y1 in re.findall(rf'\\draw\[line width=1.2pt\] {PT} rectangle {PT};', b):
        x0, y0, x1, y1 = map(float, (x0, y0, x1, y1))
        fr.append(['box', (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2, []])
    for c in re.findall(r'\\(?:draw|fill)(?:\[[^\]]*\])? [^;]*;', b):
        if 'rectangle' in c or 'black!' in c or 'fill=white' in c or 'arc[' in c:
            continue
        m = re.search(PT, c)
        x, y = float(m.group(1)), float(m.group(2))
        for f in fr:
            if abs(x - f[1]) < f[3] and abs(y - f[2]) < f[3]:
                f[4].append(c)
                break
    return [(kind, x, y, classify(c, x, y) if c else None) for kind, x, y, r, c in fr]


def picture_ring(b):
    rg = [r for r in rings(b) if r['n'] == 6 and r['dot_r'] > 0.3]
    assert len(rg) == 1
    r = rg[0]
    fr = {(round(x, 3), round(y, 3)): name for kind, x, y, name in frames(b) if kind == 'ring'}
    order = [fr[(round(d[2], 3), round(d[3], 3))] for i, d in sorted(r['dots'].items())]
    assert arrows_clockwise(b)
    return order, r


# ============================================================================= K-1
def check_k1():
    print('\n== K-1 ==')
    pics = load('k-1')
    by = lambda p: [q for q in pics if q['prob'] == p]
    dot_d = None
    reached = {}
    for p, key in ((1, 'K P1'), (2, 'K P2'), (3, 'K P3'), (6, 'K P6'), (7, 'K P7')):
        big = [r for q in by(p) for r in rings(q['body']) if r['dot_r'] > 0.3]
        small = [(rings(q['body'])[0], q) for q in by(p) if rings(q['body']) and rings(q['body'])[0]['dot_r'] < 0.2]
        assert len(big) == 1 and big[0]['black'] == [0]
        n = big[0]['n']
        dot_d = 2 * big[0]['dot_r']
        res = {}
        for r, q in small:
            k = int(re.search(r'hop (\d+)', q['body']).group(1))
            assert r['n'] == n and r['black'] == [0] and arrows_clockwise(q['body'])
            res[k] = len(set(walk(n, k))) == n
            reached[(n, k)] = len(set(walk(n, k)))
            print(f"   {n} dots hop {k}: lands on {sorted(set(walk(n, k)))}, back after {len(walk(n, k))} hops, draws {shape(n, k) if res[k] else 'part'}")
        claim(key, res)
    claim('K P1-3 dots reached', {k: v for k, v in reached.items() if k[0] <= 6})
    claim('K dot diameter', round(dot_d, 2))
    # Problem 4
    res = []
    for q in by(4):
        r = rings(q['body'])[0]
        k = int(re.search(r'hop (\d+)', q['body']).group(1))
        assert r['black'] == [0]
        res.append((r['n'], k, starts(r['n'], k)))
        print(f"   P4 {r['n']} dots hop {k}: {shape(r['n'], k)}")
    claim('K P4', res)
    # Problem 5: pictures, hops 1 to 5 that draw each one (with the restart rule of P4)
    res = []
    for q in by(5):
        segs = segments(q['body'])
        if not segs:
            continue
        n, ch = drawing_to_chords(segs)
        res.append([h for h in range(1, 6) if h % n and chords(n, h) == ch])
    claim('K P5', res)
    # Problem 8
    (q8,) = by(8)
    order, _ = picture_ring(q8['body'])
    claim('K ring', order)
    boxes = sorted([(round(-y, 2), x, name) for kind, x, y, name in frames(q8['body']) if kind == 'box'])
    grid = {}
    for y, x, name in boxes:
        grid.setdefault(y, []).append(name)
    rows = [grid[y] for y in sorted(grid)]
    assert len(rows) == 6 and all(v is None for r in rows[1:] for v in r)
    hop = int(re.search(r'Hop (\d+) changes', probtext('k-1', 8)).group(1))
    cur, out = rows[0], []
    while True:
        cur = [order[(order.index(c) + hop) % 6] for c in cur]
        out.append(cur)
        if cur == rows[0]:
            break
    assert len(out) <= 5
    claim('K P8', out)
    # Problem 9
    res = []
    for q in by(9):
        if 'hop' not in q['body']:
            order9, _ = picture_ring(q['body'])
            assert order9 == order
            continue
        icons = [name for kind, x, y, name in sorted(frames(q['body']), key=lambda t: t[1])]
        k = int(re.search(r'\{hop (\d+)\}', q['body']).group(1))
        a, b, c = icons
        assert order[(order.index(a) + k) % 6] == b and c == a
        back = [h for h in range(1, 6) if order[(order.index(b) + h) % 6] == a]
        assert len(back) == 1
        res.append((a, k, b, back[0]))
    claim('K P9', res)
    # Problem 10
    pics10 = by(10)
    order10, _ = picture_ring(pics10[0]['body'])
    assert order10 == order
    ex = [name for kind, x, y, name in sorted(frames(pics10[1]['body']), key=lambda t: t[1])]
    secret = [h for h in range(1, 6) if order[(order.index(ex[0]) + h) % 6] == ex[1]]
    assert len(secret) == 1
    s = secret[0]
    fr = frames(pics10[2]['body'])
    asked = [name for kind, x, y, name in fr if name]
    assert sum(1 for f in fr if f[3] is None) == len(asked)
    claim('K P10', (s, {a: order[(order.index(a) + s) % 6] for a in asked}))


# ============================================================================= wheel and codes
def wheel_model(name):
    """Read both printed wheels; return the shift rule they implement and their diameters."""
    pics = load(name)
    wheels = []
    for q in pics:
        lets = re.findall(rf'\\node\[[^\]]*rotate=(-?[\d.]+)\] at {PT} \{{\\underline\{{([A-Z])\}}\}};', q['body'])
        if not lets:
            continue
        (cmd, opt, cx, cy, R), = [c for c in circles(q['body']) if c[0] == 'draw' and 'line width=1.4pt' in (c[1] or '')]
        ang = {}
        for rot, x, y, L in lets:
            ang[L] = (90 - math.degrees(math.atan2(float(y) - cy, float(x) - cx))) % 360  # clockwise from top
        assert len(ang) == 26
        assert all(abs(ang[A[i]] - 360 * i / 26) < 0.01 for i in range(26))   # A..Z clockwise, evenly spaced
        wheels.append((2 * R, ang))
    (D_out, outer), (D_in, inner) = sorted(wheels, reverse=True)

    def encode(word, setting):
        turn = outer[setting] - inner['A']         # turn the inner wheel so inner A sits at the outer setting
        res = ''
        for c in word:
            if c not in A:
                res += c
                continue
            a = (inner[c] + turn) % 360
            res += min(A, key=lambda L: min(abs(outer[L] - a), 360 - abs(outer[L] - a)))
        return res

    assert encode('CAT', 'D') == 'FDW' and 'FDW' in probtext(name, 4)
    for s in A:   # the wheel is the shift by the setting's place in the alphabet
        assert all(encode(c, s) == A[(A.index(c) + A.index(s)) % 26] for c in A)
    return encode, (round(D_out, 2), round(D_in, 2))


def codes(name, prob):
    """Code messages of a problem, rebuilt from the letter positions; wrapped lines joined."""
    msgs = []
    for q in load(name):
        if q['prob'] != prob:
            continue
        lets = [(float(x), t) for opt, x, y, t in nodes(q['body']) if 'ttfamily' in opt]
        if not lets:
            continue
        lets.sort()
        pitch = min(b[0] - a[0] for a, b in zip(lets, lets[1:])) if len(lets) > 1 else 1
        line = lets[0][1]
        for (x0, _), (x1, t) in zip(lets, lets[1:]):
            line += ' ' * (round((x1 - x0) / pitch) - 1) + t
        if q['cont']:
            msgs[-1] += ' ' + line
        else:
            msgs.append(line)
    return msgs


def words():
    """en_US hunspell word list, expanded with its suffix and prefix rules; lower-case entries only."""
    rules = {}
    for line in open(DIC + '.aff', encoding='latin-1'):
        p = line.split()
        if len(p) >= 5 and p[0] in ('SFX', 'PFX'):
            rules.setdefault(p[1], []).append((p[0], '' if p[2] == '0' else p[2], p[3].split('/')[0], p[4]))
    out = set()
    for line in list(open(DIC + '.dic', encoding='latin-1'))[1:]:
        w, _, fl = line.strip().partition('/')
        if not w or (w != w.lower() and w != 'I'):
            continue
        out.add(w.upper())
        for f in fl:
            for kind, strip, add, cond in rules.get(f, []):
                add = '' if add == '0' else add
                if kind == 'SFX' and re.search(cond + '$', w) and w.endswith(strip):
                    out.add((w[:len(w) - len(strip)] + add).upper())
                if kind == 'PFX' and re.match(cond, w) and w.startswith(strip):
                    out.add((add + w[len(strip):]).upper())
    return out


def crack(msg, encode, W):
    """All settings that turn the code back into English words (the decode of a setting s is the
    encode with the setting that turns the wheel back)."""
    hits = []
    for s in A[1:]:
        back = A[(26 - A.index(s)) % 26]
        plain = encode(msg, back)
        ws = plain.split()
        if all(w in W for w in ws):
            hits.append((s, plain))
    return hits


# ============================================================================= 2-3
def check_23(W):
    print('\n== Grades 2-3 ==')
    pics = load('grades-2-3')
    encode, size = wheel_model('grades-2-3')
    claim('wheel', size)

    def ring_answers(p):
        res = []
        for q in pics:
            if q['prob'] != p:
                continue
            r, = rings(q['body'])
            lab = ' '.join(t for _, _, _, t in nodes(q['body']))
            m = re.search(r'(?:(\d+) dots, )?hop (\d+)', lab)
            n = int(m.group(1)) if m.group(1) else r['n']
            k = int(m.group(2))
            assert n == r['n']
            res.append((n, k, starts(n, k)))
            print(f"   P{p} {n} dots hop {k}: {starts(n, k)} starts, {shape(n, k)}")
        return res

    for p in (1, 2, 3, 6):
        claim(f'M P{p}', ring_answers(p))
    # P7: a hop bigger than 3 (and smaller than the ring) giving exactly 3 starts
    res = {}
    for q in pics:
        if q['prob'] == 7 and rings(q['body']):
            r, = rings(q['body'])
            n = r['n']
            assert f'{n} dots' in q['body']
            res[n] = [k for k in range(4, n) if starts(n, k) == 3]
    claim('M P7', res)
    # P4: decode with the setting named in the problem
    setting = re.search(r'Set your wheel to ([A-Z])', probtext('grades-2-3', 4)).group(1)
    back = A[(26 - A.index(setting)) % 26]
    claim('M P4', (setting, [encode(c, back) for c in codes('grades-2-3', 4)]))
    # P8: crack
    res = []
    for c in codes('grades-2-3', 8):
        hits = crack(c, encode, W)
        print(f"   P8 {c}: {hits}")
        assert len(hits) == 1
        res.append(hits[0])
    claim('M P8', res)
    # P9: second setting that gives the word back
    firsts = re.findall(r'first setting ([A-Z])', ''.join(q['body'] for q in pics if q['prob'] == 9))
    res = {}
    for f in firsts:
        ok = [s for s in A if all(encode(encode(c, f), s) == c for c in A)]
        assert len(ok) == 1
        res[f] = ok[0]
    claim('M P9', res)


# ============================================================================= 4-5
def check_45(W):
    print('\n== Grades 4-5 ==')
    pics = load('grades-4-5')
    encode, size = wheel_model('grades-4-5')
    claim('wheel', size)
    for p in (1, 2):
        res = []
        for q in pics:
            if q['prob'] != p:
                continue
            r, = rings(q['body'])
            lab = ' '.join(t for _, _, _, t in nodes(q['body']))
            m = re.search(r'(?:(\d+) dots, )?hop (\d+)', lab)
            n = int(m.group(1)) if m.group(1) else r['n']
            k = int(m.group(2))
            assert n == r['n']
            res.append((n, k, starts(n, k)))
            print(f"   P{p} {n} dots hop {k}: {starts(n, k)} pieces, {shape(n, k)}")
        claim(f'U P{p}', res)
    # P3: list, and the two check rings
    (q3,) = [q for q in pics if q['prob'] == 3]
    cases = [(int(a), int(b)) for _, _, _, t in nodes(q3['body']) for a, b in re.findall(r'^(\d+) dots, hop (\d+)$', t)]
    ring_ns = sorted(r['n'] for r in rings(q3['body']))
    assert ring_ns == sorted(n for n, _ in cases[:2])
    res = [(n, k, starts(n, k)) for n, k in dict.fromkeys(cases)]
    for n, k, s in res:
        print(f"   P3 {n} dots hop {k}: {s} pieces, {shape(n, k)}")
    claim('U P3', res)
    # P4: crack the codes; the last one has two (or more) words
    cs = codes('grades-4-5', 4)
    res = []
    for c in cs[:-1]:
        hits = crack(c, encode, W)
        print(f"   P4 {c}: {hits}")
        assert len(hits) == 1
        res.append(hits[0])
    claim('U P4', res)
    hits = crack(cs[-1], encode, W)
    claim('U P4 last', dict(hits))
    # P6: combining settings
    (q6,) = [q for q in pics if q['prob'] == 6]
    cells = sorted([(round(-y, 2), x, t) for opt, x, y, t in nodes(q6['body']) if re.fullmatch('[A-Z]', t)])
    boxes = [(round(-(float(y0) + float(y1)) / 2, 2), (float(x0) + float(x1)) / 2)
             for x0, y0, x1, y1 in re.findall(rf'\\draw\[line width=1pt\] {PT} rectangle {PT};', q6['body'])]
    rows = {}
    for y, x, t in cells:
        rows.setdefault(y, {})[round(x, 2)] = t
    for y, x in boxes:
        rows.setdefault(y, {})[round(x, 2)] = None
    res = []
    for y in sorted(rows):
        a, b, c = [rows[y][x] for x in sorted(rows[y])]
        if c is None:
            c = encode(encode('A', a), b)
            assert all(encode(encode(L, a), b) == encode(L, c) for L in A)
        else:
            (b,) = [s for s in A if encode(encode('A', a), s) == c]
        res.append((a, b, c))
    claim('U P6', res)
    # P8: rings from 4 to 20 where every hop smaller than the ring reaches every dot
    (q8,) = [q for q in pics if q['prob'] == 8 and nodes(q['body'])]
    ns = [int(t) for _, _, _, t in nodes(q8['body'])]
    claim('U P8', [n for n in ns if all(starts(n, k) == 1 for k in range(1, n))])
    # P9: erased drawings
    res = []
    for q in pics:
        if q['prob'] == 9:
            n, ch = drawing_to_chords(segments(q['body']))
            hops = [h for h in range(1, n) if chords(n, h) == ch]
            # no other ring size gives these lines: the tips are the dots, so n is forced
            res.append((n, hops))
            print(f"   P9 {n} dots, hops {hops}: {shape(n, hops[0])}")
    claim('U P9', res)
    # P11: setting C from A, and the settings that visit all 26 letters
    t11 = probtext('grades-4-5', 11)
    s = re.search(r'Set the wheel to ([A-Z])', t11).group(1)
    seq, L = 'A', encode('A', s)
    while L != 'A':
        seq += L
        L = encode(L, s)
    claim('U P11 C', seq)
    full = ''
    for s in A:
        seen, L = {'A'}, encode('A', s)
        while L != 'A':
            seen.add(L)
            L = encode(L, s)
        if len(seen) == 26:
            full += s
    claim('U P11', full)
    # P10: two settings in a row are always one setting
    assert all(any(all(encode(encode(L, a), b) == encode(L, c) for L in A) for c in A) for a in A for b in A)
    # P12: times tables on the two numbered rings
    (q12,) = [q for q in pics if q['prob'] == 12 and 'texttimes' in q['body']]
    rg = rings(q12['body'])
    labels = [(t, x, y) for opt, x, y, t in nodes(q12['body']) if 'texttimes' in t]
    nums = [(int(t), x, y) for opt, x, y, t in nodes(q12['body']) if t.isdigit()]
    res = {}
    for t, lx, ly in labels:
        mult = int(t.replace('\\texttimes', ''))
        r = min(rg, key=lambda r: math.hypot(r['cx'] - lx, r['cy'] - ly))
        n = r['n']
        for num, x, y in nums:   # the printed numbers run 0..n-1 clockwise from the top
            if abs(math.hypot(x - r['cx'], y - r['cy']) - r['R']) < 0.3:
                assert cw_index(x, y, r['cx'], r['cy'], n) == num
        lines = [(m, mult * m % n) for m in range(n)]
        selfs = [m for m, t2 in lines if m == t2]
        pairs = {}
        for m, t2 in lines:
            if m != t2:
                pairs[frozenset((m, t2))] = pairs.get(frozenset((m, t2)), 0) + 1
        twice = sorted(tuple(sorted(p)) for p, c in pairs.items() if c == 2)
        res[mult] = dict(self=selfs, twice=twice, lines=len(pairs))
        assert 13 * 2 % n == 2
    claim('U P12', res)


# ============================================================================= numbers quoted in the prose
def check_prose():
    print('\n== Numbers in the prose ==')
    pics = load('grades-2-3')
    encode, _ = wheel_model('grades-2-3')
    facts = {
        'idea: 12 dots hop 8 is 4 triangles': shape(12, 8) == '4 x triangle',
        'launch: 5 dots hop 2 reaches every dot (five-pointed star)': shape(5, 2) == '1 x {5/2} star',
        'K-1: 6 dots hop 2 is back after 3 hops': len(walk(6, 2)) == 3,
        'K-1: 4 dots hop 3 from the top lands on the left dot (dot 3)': walk(4, 3)[1] == 3,
        'K-1: hop 4 on 5 dots is one step back': walk(5, 4)[1] == 4,
        'K-1 P6-7: hops 2,5 one star, hops 3,4 the other': shape(7, 2) == shape(7, 5) != shape(7, 3) == shape(7, 4),
        'fallback: pass by 2 among 5 reaches all': len(walk(5, 2)) == 5,
        'fallback: pass by 2 among 4 misses two': len(walk(4, 2)) == 2,
        'fallback: pass by 1 or 3 among 4 reaches all': len(walk(4, 1)) == len(walk(4, 3)) == 4,
        '2-3 P4: coding VWDU again with D gives YZGX': encode('VWDU', 'D') == 'YZGX',
        '2-3 P7: 18 dots hops 6, 9, 12 give 6, 9, 6 starts': [starts(18, k) for k in (6, 9, 12)] == [6, 9, 6],
        '2-3 P8: setting Q codes E as U': encode('E', 'Q') == 'U',
        '2-3 P8: setting Z (I to H) fails on ZAHY': encode('ZAHY', 'B') not in words_cache,
        '2-3 P9: D is 3 places and X is 23': (A.index('D'), A.index('X')) == (3, 23),
        '4-5 P4: R from I means setting J': encode('I', 'J') == 'R',
        '4-5 P6: T then M is 31 places, 31 - 26 = 5 = F': A.index('T') + A.index('M') == 31 and A[31 - 26] == 'F',
        '4-5 P7: first piece on 12 dots hop 8 is 0, 8, 4': walk(12, 8) == [0, 8, 4],
        '4-5 P7: back after 3 hops, 24 = two laps': len(walk(12, 8)) == 3 and 3 * 8 == 2 * 12,
        '4-5 P10: H then T is a full turn': A.index('H') + A.index('T') == 26,
        '4-5 P11: N goes A, N, A': encode('A', 'N') == 'N' and encode('N', 'N') == 'A',
        'math: one-piece hops on 12 are 1, 5, 7, 11': [k for k in range(1, 12) if starts(12, k) == 1] == [1, 5, 7, 11],
        'math: they make two pictures': len({frozenset(chords(12, k)) for k in (1, 5, 7, 11)}) == 2,
        'materials: counters 20+20+20+1 = 61': 20 + 20 + 20 + 1 == 61,
        'materials: fasteners 4+3+3 = 10, pencils 5+5+4 = 14, rulers 2+4+3 = 9': (4 + 3 + 3, 5 + 5 + 4, 2 + 4 + 3) == (10, 14, 9),
    }
    for k, v in facts.items():
        print(f"{'ok ' if v else 'BAD'} {k}")
        if not v:
            FAIL.append((k, True, v))


if __name__ == '__main__':
    W = words()
    words_cache = W
    print(f'{len(W)} dictionary words')
    check_k1()
    check_23(W)
    check_45(W)
    check_prose()
    if FAIL:
        print('\nMISMATCHES:')
        for f in FAIL:
            print('  ', f)
        sys.exit(1)
    print('\nAll printed answers match the recomputation.')
