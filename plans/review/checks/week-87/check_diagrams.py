#!/usr/bin/env python3
"""Read back the delivered Week 87 PDFs and check diagrams against the text.

Reads lowell-math-circle-year-2/week-87/*.pdf with PyMuPDF (text words and
vector drawings), never the builder.  Checks:
  every student page : header, footer id, page number, consecutive problems.
  cards              : reconstruct every printed ranking card (V-label, 1st,
                       2nd, 3rd letters) on shared, upper and materials pages.
  number lines       : read tick positions and every favorite line + V label,
                       and convert to tick values (line pp. 1-4, upper p. 2).
  line p. 1 launch   : lane circles -> favorite values; X/Y marker positions;
                       per-voter distance table; tally contents.
  upper p. 2         : V1 favorite and D/E/F tile positions -> distances.
  materials          : 100 mm scale, card/tile/token/marker sizes, lane pitch
                       and alignment with the numbered line, tally wells and
                       target clearances, knockout mat boxes.
  guide              : pdftotext; every sentence math.md quotes is present.
Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
import itertools
import math
import re
import subprocess
import sys
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')
import pymupdf as fitz  # noqa: E402

HERE = Path(__file__).resolve().parent


def find_repo():
    # Committed copy: plans/review/checks/week-87/ -> repo is four folders up.
    cands = []
    if len(HERE.parents) > 3:
        cands.append(HERE.parents[3])
    cands += list(HERE.parents)
    for c in cands:
        if (c / 'lowell-math-circle-year-2' / 'week-87').is_dir():
            return c
    raise SystemExit('repository not found above ' + str(HERE))


REPO = find_repo()
WK = REPO / 'lowell-math-circle-year-2' / 'week-87'
# Re-pointed on 2026-10-23: the card's shoulds and small coulds (79d58c1) and the footer ids (dfbc5e4) changed the
# packets, so this review check reads the copies as reviewed, in week-87/archive-before-card-fixes-2026-10-23/.
WK = WK / 'archive-before-card-fixes-2026-10-23'
MM = 72 / 25.4
OUT, FAILS = [], []


def say(s=''):
    OUT.append(s)
    print(s)


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def words(page):
    return [(w[0], w[1], w[2], w[3], w[4]) for w in page.get_text('words')]


def lines_text(page):
    """Text grouped into visual lines (by rounded y)."""
    rows = {}
    for x0, y0, x1, y1, s in words(page):
        rows.setdefault(round(y0), []).append((x0, s))
    return [' '.join(s for _, s in sorted(v)) for k, v in sorted(rows.items())]


def segs(page):
    out = []
    for d in page.get_drawings():
        for it in d['items']:
            if it[0] == 'l':
                out.append((it[1].x, it[1].y, it[2].x, it[2].y))
    return out


def shapes(page):
    return [(d['rect'], ''.join(it[0] for it in d['items'])) for d in page.get_drawings()]


# ------------------------------------------------------------ headers etc.
def header_footer(pdf, band, ident):
    doc = fitz.open(pdf)
    probs = []
    for i, page in enumerate(doc):
        lt = lines_text(page)
        check(lt[0] == f'Week 87 / Voting and agendas / {band}', f'{pdf.name} p{i+1} header "{lt[0]}"')
        foot = [l for l in lt if l.startswith('Bellingham Math Circle')]
        pno = [w[4] for w in words(page) if w[1] > 740 and w[0] > 500]
        check(foot and foot[0] == f'Bellingham Math Circle / Week 87 / {ident}' and pno == [str(i + 1)],
              f'{pdf.name} p{i+1} footer "{foot[0] if foot else None}", page number {pno}')
        txt = page.get_text()
        probs += [int(n) for n in re.findall(r'Problem (\d+):', txt)]
        check('Name' not in txt and 'Date' not in txt, f'{pdf.name} p{i+1} no Name/Date fields')
    return doc, probs


# ------------------------------------------------------------ cards
def read_cards(page):
    """Return list of (x, y, label, 'XYZ') for every ranking card on the page."""
    W = words(page)
    cards = []
    labels = [w for w in W if re.fullmatch(r'V\d', w[4])]
    for lab in labels:
        rows = []
        for tag in ['1st', '2nd', '3rd']:
            cand = [w for w in W if w[4] == tag and abs(w[0] - lab[0]) < 2 and 0 < w[1] - lab[1] < 200]
            if not cand:
                break
            tw = min(cand, key=lambda w: w[1] - lab[1])
            let = [w for w in W if re.fullmatch(r'[A-F]', w[4]) and abs(w[1] - tw[1]) < 6 and 0 < w[0] - tw[0] < 40]
            rows.append(let[0][4] if let else ' ')
        if len(rows) == 3:
            cards.append((round(lab[0]), round(lab[1]), lab[4], ''.join(rows)))
    return sorted(cards, key=lambda c: (c[1], c[0]))


def card_groups(page):
    cs = read_cards(page)
    groups = {}
    for c in cs:
        groups.setdefault(c[1], []).append(c)
    return [[(c[2], c[3]) for c in sorted(g)] for _, g in sorted(groups.items())]


# ------------------------------------------------------------ number lines
def number_lines(page):
    """Find each 0..10 number line: returns list of dicts with tick x's and favorites."""
    W = words(page)
    S = segs(page)
    res = []
    zeros = [w for w in W if w[4] == '0']
    for z in zeros:
        row = [w for w in W if abs(w[1] - z[1]) < 1 and re.fullmatch(r'\d+', w[4])]
        vals = sorted(row, key=lambda w: w[0])
        if [w[4] for w in vals] != [str(i) for i in range(11)]:
            continue
        # axis: horizontal segment just above the labels
        axis = [s for s in S if abs(s[1] - s[3]) < 0.1 and 0 < z[1] - s[1] < 12 and s[0] < z[2] + 6]
        ax = max(axis, key=lambda s: s[1])
        ay = ax[1]
        ticks = sorted({round(s[0], 2) for s in S if abs(s[0] - s[2]) < 0.1 and min(s[1], s[3]) < ay < max(s[1], s[3])
                        and abs(s[1] - s[3]) < 20 and ax[0] - 1 <= s[0] <= ax[2] + 1})
        favlines = [s for s in S if abs(s[0] - s[2]) < 0.1 and max(s[1], s[3]) < ay and ay - max(s[1], s[3]) < 7]
        labs = [w for w in W if re.fullmatch(r'V\d', w[4]) and 0 < ay - w[3] < 80]
        favs = {}
        for lab in labs:
            cand = [s for s in favlines if abs(s[0] - lab[2]) < 3 and 0 < min(s[1], s[3]) - lab[3] < 15]
            if cand:
                s = min(cand, key=lambda s: min(s[1], s[3]) - lab[3])
                ti = min(range(len(ticks)), key=lambda i: abs(ticks[i] - s[0]))
                favs[lab[4]] = (ti, abs(ticks[ti] - s[0]))
        res.append({'y': ay, 'ticks': ticks, 'favs': favs, 'nfavlines': len(favlines)})
    return sorted(res, key=lambda r: r['y'])


def fav_values(nl):
    return [nl['favs'][k][0] for k in sorted(nl['favs'])]


def even(ticks, step=None, tol=0.05):
    d = [b - a for a, b in zip(ticks, ticks[1:])]
    return max(d) - min(d) < tol and (step is None or abs(d[0] - step) < tol)


def row_pairs(page, left_re, region):
    """Join each word matching left_re with the words to its right on the same baseline."""
    W = [w for w in words(page) if region[0] <= w[0] <= region[2] and region[1] <= w[1] <= region[3]]
    out = []
    for w in W:
        if re.fullmatch(left_re, w[4]):
            row = sorted([v for v in W if abs((v[1] + v[3]) / 2 - (w[1] + w[3]) / 2) < 2.5 and v[0] >= w[0]], key=lambda v: v[0])
            out.append(''.join(v[4] for v in row))
    return out


# =========================================================== shared
say('=== Shared packet (week-87-shared.pdf) ===')
doc, probs = header_footer(WK / 'week-87-shared.pdf', 'Grades 2–5', 'W87-S-v1')
check(len(doc) == 3, f'3 pages ({len(doc)})')
check(probs == [1, 2, 3], f'problem numbers {probs}')
g1 = card_groups(doc[0])
say(f'     p1 card rows: {g1}')
check(g1 == [[('V1', 'DFE'), ('V2', 'EFD'), ('V3', 'FED')], [('V1', 'ABC'), ('V2', 'BCA'), ('V3', 'CAB')]],
      'p1: example cards DFE/EFD/FED; Problem 1 cards ABC/BCA/CAB')
t1 = ' '.join(lines_text(doc[0]))
ch = row_pairs(doc[0], r'V\d', (200, 190, 330, 260))
say(f'     p1 choices: {ch}')
check(ch == ['V1→D', 'V2→E', 'V3→E'] and 'E wins, 2 to 1' in t1, 'p1 example choices V1 D, V2 E, V3 E; "E wins, 2 to 1"')
# tally boxes on p1: D box contains V1, E box contains V2 V3
W = words(doc[0])
boxes = [r for r, k in shapes(doc[0]) if k == 'llll' and r.width < 60 and r.height > 60]
inbox = {}
for r in boxes:
    lab = [w[4] for w in W if r.x0 < w[0] < r.x1 and r.y0 < w[1] < r.y0 + 12]
    toks = sorted(w[4] for w in W if r.x0 < w[0] < r.x1 and r.y0 + 12 < w[1] < r.y1 and re.fullmatch(r'V\d', w[4]))
    if lab and lab[0] in 'DE':
        inbox[lab[0]] = toks
check(inbox == {'D': ['V1'], 'E': ['V2', 'V3']}, f'p1 tally boxes {inbox}')
g2 = card_groups(doc[1])
check(g2 == [[('V1', 'DFE'), ('V2', 'EFD'), ('V3', 'FED')]], f'p2 knockout example cards {g2}')
t2 = ' '.join(lines_text(doc[1]))
check('D vs E: E wins' in t2 and 'E vs F: F wins' in t2 and 'F was waiting' in t2, 'p2 knockout example text')
g3 = card_groups(doc[2])
check(g3 == [[('V1', '   '), ('V2', '   '), ('V3', '   ')]] * 2, 'p3 two blank sets of three cards')

# =========================================================== upper
say()
say('=== Upper packet (week-87-upper.pdf) ===')
doc, probs = header_footer(WK / 'week-87-upper.pdf', 'Grades 4–5', 'W87-U-v1')
check(len(doc) == 2 and probs == [1, 2], f'2 pages, problems {probs}')
gu = card_groups(doc[0])
say(f'     p1 card rows: {gu}')
check(gu == [[('V1', 'ABC'), ('V2', 'ACB'), ('V3', 'BAC')], [('V1', 'ACB'), ('V2', 'CBA'), ('V3', 'BAC')]],
      'upper P1 sets ABC/ACB/BAC and ACB/CBA/BAC')
gu2 = card_groups(doc[1])
say(f'     p2 card rows: {gu2}')
check(gu2 == [[('V1', 'DEF')], [('V1', 'ABC'), ('V2', 'BCA'), ('V3', 'CAB')]], 'upper p2: example card DEF; Problem 2 cards ABC/BCA/CAB')
nls = number_lines(doc[1])
check(len(nls) == 1, 'upper p2: one small number line')
nl = nls[0]
check(even(nl['ticks']) and len(nl['ticks']) == 11, 'upper p2 ticks evenly spaced 0..10')
check(nl['favs'].get('V1', (None,))[0] == 1, f'upper p2: V1 favorite at {nl["favs"].get("V1")}')
W = words(doc[1])
tiles = {}
for r, k in shapes(doc[1]):
    if k == 'llll' and abs(r.width - 6 * MM) < 0.5:
        lab = [w[4] for w in W if r.x0 <= w[0] and w[2] <= r.x1 + 1 and r.y0 <= w[1] <= r.y1]
        if lab:
            cx = (r.x0 + r.x1) / 2
            ti = min(range(11), key=lambda i: abs(nl['ticks'][i] - cx))
            tiles[lab[0]] = (ti, round(abs(nl['ticks'][ti] - cx), 2))
say(f'     D/E/F tiles (tick, offset pt): {tiles}')
check({k: v[0] for k, v in tiles.items()} == {'D': 0, 'E': 4, 'F': 9} and all(v[1] < 0.5 for v in tiles.values()),
      'upper p2: D at 0, E at 4, F at 9 -> distances 1, 3, 8 from V1 at 1')
t = ' '.join(lines_text(doc[1]))
check('D: 1 step' in t and 'E: 3 steps' in t and 'F: 8 steps' in t, 'upper p2 distance text 1/3/8')

# =========================================================== line
say()
say('=== Line packet (week-87-line.pdf) ===')
doc, probs = header_footer(WK / 'week-87-line.pdf', 'Grades 3–5', 'W87-L-v1')
check(len(doc) == 4 and probs == [1, 2, 3, 4], f'4 pages, problems {probs}')
expected = {0: [[0, 2, 4, 7, 10]], 1: [[0, 0, 0, 8, 10], [1, 4, 4, 4, 9], [0, 1, 6, 9, 10]], 2: [[]], 3: [[1, 3, 7, 9], []]}
for pn, exp in expected.items():
    nls = [n for n in number_lines(doc[pn]) if len(n['ticks']) == 11 and n['ticks'][-1] - n['ticks'][0] > 150 * MM]
    got = [fav_values(n) for n in nls]
    offs = max([o for n in nls for _, o in n['favs'].values()] or [0])
    check(got == exp and all(even(n['ticks'], 16 * MM) for n in nls) and offs < 0.3,
          f'line p{pn+1} working number lines (16 mm ticks): favorites {got}, max line-to-tick offset {offs:.2f} pt')
    for n in nls:
        check(n['nfavlines'] == len(n['favs']), f'   every favorite line on p{pn+1} y={n["y"]:.0f} has its own label ({n["nfavlines"]} lines)')
# p2: label-to-line association of "Winning location"
W = words(doc[1])
wl = sorted(w[1] for w in W if w[4] == 'Winning')
nls = number_lines(doc[1])
say(f'     p2 "Winning location" y = {[round(v) for v in wl]}; number-line axes y = {[round(n["y"]) for n in nls]}')

# p1 launch lanes
page = doc[0]
W = words(page)
S = segs(page)
circ = [r for r, k in shapes(page) if k == 'cccc' and abs(r.width - 6 * MM) < 0.3]
lanes = []
for i in range(5):
    lab = [w for w in W if w[4] == f'V{i+1}' and w[0] < 60 and w[1] < 330]
    ly = lab[0][3]
    axis = [s for s in S if abs(s[1] - s[3]) < 0.1 and 0 < s[1] - ly < 15 and s[2] - s[0] > 200]
    ay = axis[0][1]
    ticks = sorted({round(s[0], 2) for s in S if abs(s[0] - s[2]) < 0.1 and min(s[1], s[3]) < ay < max(s[1], s[3]) and max(s[1], s[3]) - min(s[1], s[3]) < 7})
    c = [r for r in circ if abs((r.y0 + r.y1) / 2 - ay) < 1]
    cx = (c[0].x0 + c[0].x1) / 2
    ti = min(range(len(ticks)), key=lambda j: abs(ticks[j] - cx))
    inner = [w[4] for w in W if c[0].x0 <= w[0] and w[2] <= c[0].x1 + 1 and c[0].y0 <= w[1] <= c[0].y1]
    lanes.append((ti, round(abs(ticks[ti] - cx), 2), len(ticks), inner))
say(f'     launch lanes (tick, offset, #ticks, circle text): {lanes}')
check([l[0] for l in lanes] == [0, 1, 5, 8, 10] and all(l[1] < 0.3 and l[2] == 11 for l in lanes),
      'line p1 launch favorites 0,1,5,8,10 on their own lanes')
small = [n for n in number_lines(page) if n['ticks'][-1] - n['ticks'][0] < 100 * MM]
check(len(small) == 1 and even(small[0]['ticks'], 8 * MM), 'line p1 launch reference line (8 mm ticks)')
st = small[0]['ticks']
lane_ticks_x0 = 30 * MM
check(abs(st[0] - lane_ticks_x0) < 0.3, 'launch reference line aligned with lanes (tick 0 at the same x)')
xm = [r for r, k in shapes(page) if k == 'llll' and abs(r.width - 6 * MM) < 0.3 and r.y0 > small[0]['y']]
ym = [r for r, k in shapes(page) if k == 'llll' and abs(r.width - 8 * MM) < 0.3 and r.y0 > small[0]['y']]
xv = min(range(11), key=lambda j: abs(st[j] - (xm[0].x0 + xm[0].x1) / 2))
yv = min(range(11), key=lambda j: abs(st[j] - (ym[0].x0 + ym[0].x1) / 2))
check((xv, yv) == (2, 8), f'launch proposal markers X at {xv}, Y (diamond) at {yv}')
t = ' '.join(lines_text(page))
tab = row_pairs(page, r'V\d:', (330, 190, 560, 340))
say(f'     launch table: {tab}')
check(tab == ['V1:2/8→X', 'V2:1/7→X', 'V3:3/3→Tie', 'V4:6/0→Y', 'V5:8/2→Y'], 'launch distance table text')
t = t.replace(' ', '')
boxes = [r for r, k in shapes(page) if k == 'llll' and abs(r.width - 18 * 1.15 * MM) < 0.5]
inbox = {}
for r in boxes:
    lab = [w[4] for w in W if r.x0 < w[0] < r.x1 and r.y0 <= w[1] < r.y0 + 10]
    toks = sorted(w[4] for w in W if r.x0 < w[0] < r.x1 and r.y0 + 10 < w[1] < r.y1 and re.fullmatch(r'V\d', w[4]))
    inbox[lab[0]] = toks
check(inbox == {'X': ['V1', 'V2'], 'Y': ['V4', 'V5'], 'Tie': ['V3']}, f'launch tally {inbox}')
check('Tiedvote:2to2;V3inTie.' in t, 'launch tally caption')

# =========================================================== materials
say()
say('=== Materials (week-87-materials.pdf) ===')
doc, _ = header_footer(WK / 'week-87-materials.pdf', 'Materials', 'W87-M-v1')
check(len(doc) == 5, '5 pages')
p = doc[0]
gm = card_groups(p)
check(gm == [[('V1', 'ABC'), ('V2', 'BCA'), ('V3', 'CAB')]], f'materials p1 fixed cards {gm}')
S = segs(p)
bar = [s for s in S if abs(s[1] - s[3]) < 0.1 and abs((s[2] - s[0]) - 100 * MM) < 0.2]
check(len(bar) == 1, '100 mm scale bar is 100 mm')
sh = shapes(p)
check(sum(1 for r, k in sh if k == 'llll' and abs(r.width - 45 * MM) < .3 and abs(r.height - 80 * MM) < .3) == 3, 'three 45x80 mm cards')
check(sum(1 for r, k in sh if k == 'llll' and abs(r.width - 28 * MM) < .3 and abs(r.height - 28 * MM) < .3) == 6, 'six 28 mm option tiles')
tok = [r for r, k in sh if k == 'cccc']
check(len(tok) == 5 and all(abs(r.width - 18 * MM) < .3 for r in tok), 'five 18 mm vote tokens')
W = words(p)
check(sorted(w[4] for w in W if len(w[4]) == 1 and w[1] > 380 and w[1] < 480) == list('AABBCC'), 'option tiles A,A,B,B,C,C')
for pn in (1, 2):
    p = doc[pn]
    gm = card_groups(p)
    sl = sorted(w[4] for w in words(p) if re.fullmatch(r'[ABC]', w[4]))
    sq = [r for r, k in shapes(p) if k == 'llll' and abs(r.width - 21 * MM) < .3]
    check(gm == [[('V1', '   '), ('V2', '   '), ('V3', '   ')]] and sl == list('AAAAAABBBBBBCCCCCC') and len(sq) == 18,
          f'materials p{pn+1}: one blank set of three cards and 18 slips (6 each of A,B,C), 21 mm')
    slot = (80 - 10) / 3
    check(21 < slot, f'   slip (21 mm) fits a card slot ({slot:.1f} mm tall)')
# p4 tally + knockout
p = doc[3]
sh = shapes(p)
mat = [r for r, k in sh if k == 'llll' and abs(r.width - 170 * MM) < .3 and abs(r.height - 90 * MM) < .3]
wells = sorted([r for r, k in sh if k == 'llll' and abs(r.width - 54 * MM) < .3 and abs(r.height - 54 * MM) < .3], key=lambda r: r.x0)
targ = [r for r, k in sh if k == 'cccc']
check(len(mat) == 1 and len(wells) == 3 and len(targ) == 15, 'tally mat 170x90 mm with three 54 mm wells, 15 targets')
mins_edge, mins_gap = [], []
for wr in wells:
    ts = [r for r in targ if wr.contains(r)]
    check(len(ts) == 5 and all(abs(r.width - 18 * MM) < .3 for r in ts), '   well holds five 18 mm targets')
    mins_edge.append(min(min(r.x0 - wr.x0, wr.x1 - r.x1, r.y0 - wr.y0, wr.y1 - r.y1) for r in ts) / MM)
    cs = [((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2) for r in ts]
    mins_gap.append(min(math.dist(a, b) for a, b in itertools.combinations(cs, 2)) / MM - 18)
check(abs(min(mins_edge) - 2) < 0.05 and abs(min(mins_gap) - 4.627) < 0.05,
      f'targets: boundary clearance {min(mins_edge):.2f} mm, min gap {min(mins_gap):.3f} mm (guide: 2 mm, at least 4.6 mm)')
W = words(p)
slots = [r for r, k in sh if k == 'llll' and abs(r.width - 30 * MM) < .3]
check(len(slots) == 2 and 30 > 28 and 30 > 23, 'two 30 mm Option slots (fit 28 mm tiles and 23 mm X/Y labels)')
for name, w, h in [('First pair', 61, 39), ('Waiting', 33, 39), ('Out', 29, 85), ('First winner', 33, 39), ('Final pair', 61, 39), ('Winner', 29, 39)]:
    first = name.split()[0]
    hits = [r for r, k in sh if k == 'llll' and abs(r.width - w * MM) < .3 and abs(r.height - h * MM) < .3
            and any(ww[4] == first and r.x0 < ww[0] < r.x0 + 10 and r.y0 < ww[1] < r.y0 + 10 for ww in W)]
    fits = (w >= 28 * (2 if name in ('First pair', 'Final pair') else 1)) and (h >= 28 * (2 if name == 'Out' else 1))
    check(len(hits) >= 1 and fits, f'   knockout box "{name}" {w}x{h} mm holds the 28 mm tiles it needs (side clearance {(w - 28 * (2 if "pair" in name else 1)) / 2:.1f} mm)')
# p5 board
p = doc[4]
S = segs(p)
nls = number_lines(p)
check(len(nls) == 1 and even(nls[0]['ticks'], 16 * MM), 'board number line ticks 16 mm apart')
lane_axes = sorted({round(s[1], 1) for s in S if abs(s[1] - s[3]) < .1 and abs((s[2] - s[0]) - 160 * MM) < .3 and s[1] < nls[0]['y'] - 5})
check(len(lane_axes) == 5 and even(lane_axes, 19 * MM, 0.15), f'five lanes, 19 mm pitch {[round(v / MM, 1) for v in lane_axes]}')
ok = True
for ay in lane_axes:
    lt = sorted({round(s[0], 2) for s in S if abs(s[0] - s[2]) < .1 and min(s[1], s[3]) < ay < max(s[1], s[3])})
    ok &= len(lt) == 11 and max(abs(a - b) for a, b in zip(lt, nls[0]['ticks'])) < 0.1
check(ok, 'every lane tick lines up with the numbered line')
sh = shapes(p)
fm = [r for r, k in sh if k == 'cccc']
check(len(fm) == 5 and all(abs(r.width - 13 * MM) < .3 for r in fm), 'five 13 mm favorite markers (< 16 mm tick pitch, < 19 mm lane pitch)')
lab = [r for r, k in sh if k == 'llll' and abs(r.width - 23 * MM) < .3]
check(len(lab) == 2, 'two 23 mm X/Y tally labels')
xb = [r for r, k in sh if k == 'llll' and abs(r.width - 13 * MM) < .3]
yd = [r for r, k in sh if k == 'llll' and abs(r.width - 18 * MM) < .3]
check(len(xb) == 1 and len(yd) == 1, 'X proposal 13 mm square, Y proposal 18 mm diamond')
check((13 / 2 + 18 / 2) < 16, '   X and Y fit on adjacent ticks (6.5 + 9 < 16 mm)')

# =========================================================== guide
say()
say('=== Facilitator guide (pdftotext) ===')
gt = subprocess.run(['pdftotext', '-layout', str(WK / 'week-87-facilitator.pdf'), '-'], capture_output=True, text=True).stdout
flat = re.sub(r'\s+', ' ', gt.replace('-\n', ''))
quotes = [
    'The cyclic profile of Problem 1 is already a valid three-distinct-card agenda-dependent example; children may reproduce or relabel it, or invent another and test their claim.',
    'Do not require every child to enumerate all possible profiles.',
    'Location 4 beats every other integer location.',
    'Exactly the tick locations 3,4,5,6,7 never lose.',
    'Testing every five-favorite multiset on these eleven ticks checks 3,003 arrangements',
]
for q in quotes:
    check(re.sub(r'\s+', ' ', q) in flat, f'guide contains: "{q[:70]}..."')
check(len(fitz.open(WK / 'week-87-facilitator.pdf')) == 6, 'guide has 6 pages')

say()
say(f'{len(FAILS)} failures')
(HERE / 'check_diagrams.py.out').write_text('\n'.join(OUT) + '\n')
sys.exit(1 if FAILS else 0)
