"""Read every board, instruction card and problem statement of the Week 46 student
pages, and confirm that the delivered PDFs show the same thing.

Sources read:
  * the three student TeX files in source/week-46/editable/src/ (exact TikZ
    coordinates of every slot box, token, card and highlighted slot);
  * the delivered PDFs, through `pdftotext -bbox` (position of every R/B letter
    and of every "Problem N:" heading) and through a 100-dpi pdftoppm raster
    (fill colour sampled inside each token);
  * the bonus builder source/week-46-bonus/student/build.py and support.py
    (row coordinates and radii), compared with the bonus PDF text layer.

Writes diagrams.json (used by check_base.py) and prints PASS/FAIL lines.
"""
import json
import re
import subprocess
import tempfile
from pathlib import Path

from common import PDFS, TEX, BONUS_SRC, Report, pdftext

R = Report()
CM = 72 / 2.54

num = r'(-?[0-9.]+)'
RECT = re.compile(r'\\draw\[(gray!65,rounded corners=2pt|line width=1\.4pt)\] \(' + num + ',' + num +
                  r'\) rectangle \(' + num + ',' + num + r'\);')
CIRC = re.compile(r'\\draw\[fill=(red!18|blue!18|white),line width=\.7pt\] \(' + num + ',' + num +
                  r'\) circle \(' + num + r'\);')
LAB = re.compile(r'\\node\[font=\\bfseries\\small\] at \(' + num + ',' + num + r'\) \{([RB])\};')
TXT = re.compile(r'\\node\[anchor=north west,text width=' + num + r'cm,[^\]]*\] at \(' + num + ',' + num +
                 r'\) \{(.*)\};')
ARROW = re.compile(r'\\draw\[-\{Stealth.*?\(' + num + ',' + num + r'\) -- \(' + num + ',' + num +
                   r'\) node\[[^\]]*\] \{(.*?)\};')
LINE = re.compile(r'\\draw\[gray!45\] \(' + num + ',' + num + r'\) -- \(' + num + ',' + num + r'\);')

FILLS = {'red!18': 'R', 'blue!18': 'B', 'white': ''}


def parse_page(src):
    rects, bold, circles, labels, texts, arrows, lines = [], [], [], [], [], [], []
    for ln in src.splitlines():
        m = RECT.search(ln)
        if m:
            kind = m.group(1)
            x1, y1, x2, y2 = map(float, m.groups()[1:])
            (bold if kind.startswith('line') else rects).append((x1, -y1, x2, -y2))
            continue
        m = CIRC.search(ln)
        if m:
            circles.append((FILLS[m.group(1)], float(m.group(2)), -float(m.group(3)), float(m.group(4))))
            continue
        m = LAB.search(ln)
        if m:
            labels.append((float(m.group(1)), -float(m.group(2)), m.group(3)))
            continue
        m = TXT.search(ln)
        if m:
            texts.append((float(m.group(2)), -float(m.group(3)), float(m.group(1)), m.group(4)))
            continue
        m = ARROW.search(ln)
        if m:
            arrows.append(tuple(map(float, m.groups()[:4])) + (m.group(5),))
            continue
        m = LINE.search(ln)
        if m:
            lines.append(tuple(map(float, m.groups())))
    return dict(rects=rects, bold=bold, circles=circles, labels=labels, texts=texts,
                arrows=arrows, lines=lines)


def inside(x, y, r):
    x1, y1, x2, y2 = r
    return x1 - 1e-6 <= x <= x2 + 1e-6 and y1 - 1e-6 <= y <= y2 + 1e-6


def analyse_page(band, pno, pg):
    """Group slot boxes into rows, rows into stacked pairs, and find cards."""
    # tokens: circle + its letter (letter must sit at the circle centre)
    tokens = []
    for fill, x, y, r in pg['circles']:
        lab = [l for (lx, ly, l) in pg['labels'] if abs(lx - x) < 1e-6 and abs(ly - y) < 1e-6]
        R.check(len(lab) == (1 if fill else 0) and (not lab or lab[0] == fill),
                f'{band} p{pno}: token at ({x:.2f},{y:.2f}) fill {fill or "white"} has letter {lab}')
        tokens.append(dict(c=fill, x=x, y=y, r=r))
    # cards: outer box of height 1.5 with three inner boxes
    cards = []
    outers = [r for r in pg['rects'] if abs((r[3] - r[1]) - 1.5) < 1e-6]
    for o in outers:
        inner = sorted([r for r in pg['rects'] if r is not o and inside(r[0], r[1], o) and inside(r[2], r[3], o)])
        bolds = [b for b in pg['bold'] if inside(b[0], b[1], o) and inside(b[2], b[3], o)]
        toks = [t for t in tokens if inside(t['x'], t['y'], o)]
        texts = [t for t in pg['texts'] if inside(t[0], t[1], o)]
        ok = len(inner) == 3 and len(bolds) == 1 and len(toks) == 1 and len(texts) == 1
        R.check(ok, f'{band} p{pno}: card at ({o[0]:.2f},{o[1]:.2f}) has 3 slots, 1 bold slot, 1 token, 1 label')
        if not ok:
            continue
        b = bolds[0]
        slot = [k for k, r in enumerate(inner) if all(abs(r[i] - b[i]) < 1e-6 for i in range(4))]
        tslot = [k for k, r in enumerate(inner) if inside(toks[0]['x'], toks[0]['y'], r)]
        m = re.fullmatch(r'([123])\$\\to\$([RB])', texts[0][3])
        R.check(bool(m) and slot == tslot and len(slot) == 1 and int(m.group(1)) == slot[0] + 1
                and m.group(2) == toks[0]['c'],
                f'{band} p{pno}: card label {texts[0][3]!r} matches bold slot {slot} and token {toks[0]["c"]}')
        # token sits wholly inside its slot box
        r_in = inner[slot[0]]
        t = toks[0]
        R.check(r_in[0] <= t['x'] - t['r'] and t['x'] + t['r'] <= r_in[2] and
                r_in[1] <= t['y'] - t['r'] and t['y'] + t['r'] <= r_in[3],
                f'{band} p{pno}: card token lies inside its highlighted slot')
        cards.append(dict(x=o[0], y=o[1], slot=slot[0] + 1, color=toks[0]['c'],
                          width=round(o[2] - o[0], 3)))
    card_boxes = set()
    for o in outers:
        card_boxes.add(o)
        for r in pg['rects']:
            if inside(r[0], r[1], o) and inside(r[2], r[3], o):
                card_boxes.add(r)
    # square slot boxes not in cards, grouped into rows of three abutting squares
    sq = sorted([r for r in pg['rects'] if r not in card_boxes and abs((r[2] - r[0]) - (r[3] - r[1])) < 1e-6],
                key=lambda r: (round(r[1], 3), r[0]))
    rows, used = [], set()
    for r in sq:
        if r in used:
            continue
        w = r[2] - r[0]
        nxt = [s for s in sq if abs(s[1] - r[1]) < 1e-6 and abs(s[0] - r[2]) < 1e-6]
        if not nxt:
            continue
        n2 = [s for s in sq if abs(s[1] - r[1]) < 1e-6 and abs(s[0] - nxt[0][2]) < 1e-6]
        if not n2:
            continue
        trio = [r, nxt[0], n2[0]]
        if any(abs((s[2] - s[0]) - w) > 1e-6 for s in trio):
            continue
        used.update(trio)
        word = ''
        for s in trio:
            ts = [t for t in tokens if inside(t['x'], t['y'], s)]
            word += ts[0]['c'] if ts else '.'
        # slot number labels (1,2,3) inside the boxes, if any
        nums = [t[3] for s in trio for t in pg['texts'] if inside(t[0] + .01, t[1] + .01, s) and t[3] in '123']
        rows.append(dict(x=r[0], y=r[1], cell=round(w, 3), word=word, slotlabels=nums))
    # stack rows into pairs (same x, same cell, next row below)
    pairs, taken = [], set()
    for i, a in enumerate(rows):
        if i in taken:
            continue
        below = [j for j, b in enumerate(rows) if j not in taken and j != i and abs(b['x'] - a['x']) < 1e-6
                 and abs(b['cell'] - a['cell']) < 1e-6 and 0 < b['y'] - a['y'] <= a['cell'] + 0.4]
        if below:
            j = min(below, key=lambda j: rows[j]['y'])
            taken.update({i, j})
            pairs.append(dict(x=a['x'], y=a['y'], cell=a['cell'], top=a['word'], bottom=rows[j]['word'],
                              slotlabels=a['slotlabels'] + rows[j]['slotlabels']))
    singles = [rows[i] for i in range(len(rows)) if i not in taken]
    other = [r for r in pg['rects'] if r not in card_boxes and r not in used]
    return dict(tokens=tokens, cards=cards, pairs=pairs, singles=singles, other_boxes=other,
                texts=pg['texts'], arrows=pg['arrows'], lines=pg['lines'])


def assign(page, items, key='y'):
    """Attach each item to the section (shared text or problem) above it."""
    heads = sorted([(t[1], t[3]) for t in page['texts'] if t[2] > 10], key=lambda h: h[0])
    out = {}
    for it in items:
        y = it[key] if isinstance(it, dict) else it[1]
        above = [h for h in heads if h[0] <= y + 1e-6]
        h = above[-1][1] if above else '(top)'
        m = re.match(r'\\textbf\{Problem (\d+):\}', h)
        out.setdefault('P' + m.group(1) if m else 'rule: ' + h[:40], []).append(it)
    return out


def ppm(path, page, dpi=100):
    with tempfile.TemporaryDirectory() as d:
        base = Path(d) / 'p'
        subprocess.run(['pdftoppm', '-r', str(dpi), '-f', str(page), '-l', str(page), str(path), str(base)],
                       check=True)
        f = sorted(Path(d).glob('p*.ppm'))[0]
        data = f.read_bytes()
    parts = data.split(maxsplit=4)
    w, h = int(parts[1]), int(parts[2])
    pix = parts[4]
    return w, h, pix


def pixel(img, x, y):
    w, h, pix = img
    i = (int(y) * w + int(x)) * 3
    return tuple(pix[i:i + 3])


def colour(rgb):
    r, g, b = rgb
    if r > b + 25:
        return 'R'
    if b > r + 25:
        return 'B'
    if min(rgb) > 235:
        return ''
    return '?'


def bbox_words(path, page):
    out = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), str(path), '-'],
                         check=True, capture_output=True, text=True).stdout
    return [(float(a), float(b), float(c), float(d), w) for a, b, c, d, w in
            re.findall(r'xMin="([0-9.]+)" yMin="([0-9.]+)" xMax="([0-9.]+)" yMax="([0-9.]+)">([^<]*)<', out)]


def cross_check_pdf(band, pages):
    """Every token letter in the TeX appears in the PDF at the same place (after
    one translation per page), and the raster fill under it has that colour."""
    for pno, pg in enumerate(pages, 1):
        words = bbox_words(PDFS[band], pno)
        letters = [w for w in words if w[4] in ('R', 'B')]
        toks = [t for t in pg['tokens'] if t['c']]
        R.check(len(letters) == len(toks), f'{band} p{pno}: PDF has {len(letters)} R/B letters, TeX {len(toks)} tokens')
        if not toks or len(letters) != len(toks):
            continue
        # translation from TikZ cm (y down) to PDF points (y down)
        lp = sorted([((a + c) / 2, (b + d) / 2, w) for a, b, c, d, w in letters], key=lambda p: (round(p[1]), p[0]))
        tp = sorted([(t['x'] * CM, t['y'] * CM, t['c']) for t in toks], key=lambda p: (round(p[1]), p[0]))
        dx = lp[0][0] - tp[0][0]
        dy = lp[0][1] - tp[0][1]
        worst = 0
        okl = True
        for (px, py, pl), (tx, ty, tl) in zip(sorted(lp, key=lambda p: (round(p[1] - dy), p[0])),
                                              sorted(tp, key=lambda p: (round(p[1]), p[0]))):
            worst = max(worst, abs(px - tx - dx), abs(py - ty - dy))
            okl &= pl == tl
        R.check(okl and worst < 1.5, f'{band} p{pno}: every PDF letter sits on its TeX token '
                f'(max offset {worst:.2f} pt), same letters')
        img = ppm(PDFS[band], pno)
        bad = []
        for t in toks:
            # sample inside the circle, left of the letter (60% of radius)
            px = (t['x'] - 0.6 * t['r']) * CM + dx
            py = t['y'] * CM + dy
            c = colour(pixel(img, px * 100 / 72, py * 100 / 72))
            if c != t['c']:
                bad.append((t, c))
        R.check(not bad, f'{band} p{pno}: raster fill matches the letter for all {len(toks)} tokens {bad[:2]}')


def problem_text(src):
    return [re.sub(r'\s+', ' ', m) for m in re.findall(r'\\textbf\{Problem \d+:\} ([^}]*)\}', src)]


# delivered PDFs are the reference copies in the source packages
import hashlib
from common import SRC
md5 = lambda f: hashlib.md5(Path(f).read_bytes()).hexdigest()
for key, ref in [('k-1', SRC / 'reference-pdfs' / 'k-1.pdf'), ('grades-2-3', SRC / 'reference-pdfs' / 'grades-2-3.pdf'),
                 ('grades-4-5', SRC / 'reference-pdfs' / 'grades-4-5.pdf'), ('guide', SRC / 'reference-pdfs' / 'facilitator-guide.pdf'),
                 ('bonus', BONUS_SRC / 'reference-pdfs' / 'week-46-bonus.pdf'),
                 ('bonus-guide', BONUS_SRC / 'reference-pdfs' / 'week-46-bonus-facilitator.pdf')]:
    R.check(md5(PDFS[key]) == md5(ref), f'{key}: delivered PDF is byte-identical to {ref.name} in the source package')

result = {}
for band in ['k-1', 'grades-2-3', 'grades-4-5']:
    src = TEX[band].read_text()
    body = src.split(r'\begin{document}')[1]
    raw_pages = body.split(r'\newpage')
    pages = [analyse_page(band, i + 1, parse_page(p)) for i, p in enumerate(raw_pages)]
    pdf_pages = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', str(PDFS[band])], capture_output=True,
                                                                text=True).stdout).group(1))
    R.check(pdf_pages == len(pages), f'{band}: TeX has {len(pages)} pages, PDF has {pdf_pages}')
    # problem numbering and text agree between TeX and PDF
    nums = [int(n) for n in re.findall(r'Problem (\d+):', body)]
    R.check(nums == list(range(1, len(nums) + 1)), f'{band}: problems numbered {nums}')
    pdf_txt = re.sub(r'\s+', ' ', pdftext(PDFS[band], layout=False)).replace('ﬁ', 'fi')
    for k, t in enumerate(problem_text(body), 1):
        plain = t.replace('--', '–').replace(r'$\to$', '→')
        flat = re.sub(r'[^A-Za-z0-9]', '', plain)
        R.check(flat in re.sub(r'[^A-Za-z0-9]', '', pdf_txt), f'{band} P{k}: TeX statement appears in PDF text')
    cross_check_pdf(band, pages)
    bandout = []
    for pno, pg in enumerate(pages, 1):
        sec = {}
        for kind in ['pairs', 'singles', 'cards']:
            for k, items in assign(pg, pg[kind]).items():
                sec.setdefault(k, {}).setdefault(kind, []).extend(items)
        arrows = [(a, t) for a in pg['arrows'] for t in [a[4]]]
        bandout.append(dict(page=pno, sections=sec, arrows=[a[4] for a in pg['arrows']],
                            answer_boxes=len([b for b in pg['other_boxes']]),
                            ruled_lines=len(pg['lines'])))
    result[band] = dict(pages=bandout, problems=problem_text(body),
                        rules=[t[3] for p in raw_pages for t in parse_page(p)['texts']
                               if t[2] > 10 and not t[3].startswith(r'\textbf')])

# ---------- print a readable inventory -------------------------------------------
for band, d in result.items():
    print(f'\n=== {band} ===')
    for k, p in enumerate(d['problems'], 1):
        print(f'  P{k}: {p}')
    for pg in d['pages']:
        print(f'  page {pg["page"]}: answer boxes {pg["answer_boxes"]}, ruled lines {pg["ruled_lines"]}, '
              f'arrow labels {pg["arrows"]}')
        for sec, items in pg['sections'].items():
            for kind, its in items.items():
                if kind == 'pairs':
                    s = ', '.join(f'{i["top"]}/{i["bottom"]} (cell {i["cell"]})' for i in its)
                elif kind == 'singles':
                    s = ', '.join(f'{i["word"]} (cell {i["cell"]}, labels {"".join(i["slotlabels"])})' for i in its)
                else:
                    s = ', '.join(f'{i["slot"]}->{i["color"]}' for i in sorted(its, key=lambda c: (round(c["y"], 2), c["x"])))
                print(f'    {sec} {kind}: {s}')

# ---------- specific diagram expectations (read from the rendered pages) ----------


def sec(band, page, name):
    return result[band]['pages'][page - 1]['sections'].get(name, {})


def stories(cards):
    rowsy = {}
    for c in cards:
        rowsy.setdefault(round(c['y'], 2), []).append(c)
    return [[(c['slot'], c['color']) for c in sorted(v, key=lambda c: c['x'])] for k, v in sorted(rowsy.items())]


for band in result:
    top = [k for k in sec(band, 1, '') or []]
    intro = [v for k, v in result[band]['pages'][0]['sections'].items() if k.startswith('rule')][0]
    pr = [(p['top'], p['bottom']) for p in sorted(intro['pairs'], key=lambda p: p['x'])]
    cs = [(c['slot'], c['color']) for c in intro.get('cards', [])]
    R.check(pr == [('RBR', 'BRB'), ('RBR', 'BBB')] and cs == [(2, 'B')],
            f'{band} launch: RBR/BRB --(2->B)--> RBR/BBB  (got {pr}, {cs})')
    from common import run
    R.check(run('RBR', [(2, 'B')]) == 'RBR' and run('BRB', [(2, 'B')]) == 'BBB',
            f'{band} launch picture is the correct result of 2->B')

six = [(1, 'R'), (2, 'R'), (3, 'R'), (1, 'B'), (2, 'B'), (3, 'B')]
for band, page in [('k-1', 4), ('grades-2-3', 3), ('grades-4-5', 4)]:
    rule = [v for k, v in result[band]['pages'][page - 1]['sections'].items() if k.startswith('rule')][0]
    got = sorted((c['slot'], c['color']) for c in rule['cards'])
    R.check(got == sorted(six) and len(set(c['width'] for c in rule['cards'])) == 1,
            f'{band} p{page}: the six draw cards are exactly 1R,2R,3R,1B,2B,3B, all the same size')

stories_expected = [[(1, 'R'), (1, 'B'), (3, 'R')], [(2, 'R'), (3, 'B'), (1, 'R')], [(2, 'B'), (2, 'R'), (2, 'B')]]
R.check(stories(sec('grades-2-3', 2, 'P2')['cards']) == stories_expected,
        f'2-3 P2 stories read {stories(sec("grades-2-3", 2, "P2")["cards"])}')
R.check(stories(sec('grades-4-5', 2, 'P2')['cards']) == stories_expected,
        f'4-5 P2 stories read {stories(sec("grades-4-5", 2, "P2")["cards"])}')
R.check(stories(sec('k-1', 3, 'P5')['cards']) == [[(1, 'R'), (3, 'B')]], 'K-1 P5 story is 1->R, 3->B')

result['expected_story_sets'] = stories_expected
json.dump(result, open(Path(__file__).with_name('diagrams.json'), 'w'), indent=1)

# ---------- bonus: builder coordinates vs PDF ---------------------------------------
print('\n=== bonus ===')
bsrc = (BONUS_SRC / 'student' / 'build.py').read_text()
rows = re.findall(r"row\(c,(\d+),(\d+)(?:,\[([^\]]*)\])?,step=(\d+),rad=(\d+)\)", bsrc)
for r in rows:
    print('  row', r)
big = [r for r in rows if r[4] == '31']
R.check(len(big) == 4 and all(r[2] == '' for r in big), 'bonus: four blank working rows with radius 31 pt')
diam_mm = 2 * 31 / 72 * 25.4
R.check(abs(diam_mm - 21.9) < 0.05, f'bonus: working circles are {diam_mm:.2f} mm across (guide: 21.9 mm)')
R.check(84 - 62 > 0, 'bonus: working circles do not overlap (step 84 pt > diameter 62 pt)')
words = [bbox_words(PDFS['bonus'], p) for p in (1, 2, 3)]
p1 = [w for w in words[0] if w[4] in ('R', 'B') and 150 < w[1] < 275]  # picture band only
p1 = sorted(p1, key=lambda w: (round(w[1]), w[0]))
left = ''.join(w[4] for w in p1 if w[0] < 300)
right = ''.join(w[4] for w in p1 if w[0] > 300)
R.check(left == 'RBRBRB' and right == 'RRRBBB', f'bonus P1 picture: RBR/BRB -> RRR/BBB (PDF reads {left} | {right})')
from common import run as _run


def copy(board, i, j):
    b = list(board)
    b[j - 1] = b[i - 1]
    return ''.join(b)


R.check(copy('RBR', 1, 2) == 'RRR' and copy('BRB', 1, 2) == 'BBB', 'bonus P1 picture is the correct result of COPY 1 to 2')
p3 = sorted([w for w in words[2] if w[4] in ('R', 'B')], key=lambda w: w[0])
R.check(''.join(w[4] for w in p3) == 'RBBBBR', f'bonus P3 picture: RBB --T--> BBR (PDF reads {"".join(w[4] for w in p3)})')
R.check('RBB'[1:] + 'RBB'[0] == 'BBR', 'bonus P3 picture is the correct left rotation')
img = ppm(PDFS['bonus'], 1)
# fill colours of the 12 picture tokens on bonus p1 (builder coordinates, y up)
bad = []
for (x, y, vals) in [(74, 613, 'RBR'), (74, 550, 'BRB'), (391, 613, 'RRR'), (391, 550, 'BBB')]:
    for k, v in enumerate(vals):
        cx, cy = x + 58 * k - 10, 792 - y
        c = colour(pixel(img, cx * 100 / 72, cy * 100 / 72))
        if c != v:
            bad.append((x, y, k, v, c))
R.check(not bad, f'bonus p1: raster fill of the 12 picture tokens matches their letters {bad}')
img3 = ppm(PDFS['bonus'], 3)
bad = []
for (x, y, vals) in [(87, 607, 'RBB'), (390, 607, 'BBR')]:
    for k, v in enumerate(vals):
        cx, cy = x + 58 * k - 10, 792 - y
        c = colour(pixel(img3, cx * 100 / 72, cy * 100 / 72))
        if c != v:
            bad.append((x, y, k, v, c))
R.check(not bad, f'bonus p3: raster fill of the 6 picture tokens matches their letters {bad}')
nums = [int(n) for n in re.findall(r'Problem (\d+):', pdftext(PDFS['bonus']))]
R.check(nums == [1, 2, 3], f'bonus: problems numbered {nums}')

R.summary('extract_diagrams')
