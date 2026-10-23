#!/usr/bin/env python3
"""Read back the delivered Week 82 PDFs and check that diagrams match the text.

Student packet (week-82-students.pdf):
- page count and size; header, footer and consecutive problem numbering.
- p. 1 opening: for each of the three pictures, read every connecting line's
  two endpoints and map them to the printed top label (1-5) and bottom label
  (A-F) whose box centre is nearest; compare with the captions.
- p. 1 Problem 1: R1-R3 on one line, B1-B3 on another.
- p. 2 Problem 2: the cards of lines A, B and C in left-to-right order, the
  continuation text, and that C's star panel lies entirely to the right of
  the dashed box around C's endless row.
- p. 3 Problem 3: D's red cards and blue cards on one horizontal line, every
  red card and the red box left of the blue box; E's cards in order and
  alternating colours, with the continuation arrow after the last card.
- p. 4 Problem 4: four sketch boxes, equal sizes.
- p. 5 cards: 24 labels R1-R12, B1-B12, once each, colour of each card frame.
- p. 6: four stars and the four panel texts.
Facilitator guide: pdftotext; checks the page references and every sentence
that math.md quotes.
Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
Needs pdfplumber and poppler's pdftotext.
"""
import re
import subprocess
from pathlib import Path

import pdfplumber

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-82'
STU = WEEK / 'week-82-students.pdf'
GUI = WEEK / 'week-82-facilitator.pdf'
# Re-pointed on 2026-10-23: the card's shoulds and coulds (e8ee578) and the critic follow-up (abf6c2f) changed the
# packet and guide, so this review check reads the copies as reviewed (W82-Q-draft-v1, after da1f30b), in
# week-82/archive-before-card-fixes-2026-10-23/.
STU, GUI = (WEEK / 'archive-before-card-fixes-2026-10-23' / f.name for f in (STU, GUI))
OUT, FAIL = [], []
RED = (0.64706, 0.17647, 0.17256)
BLUE = (0.13333, 0.32549, 0.59216)


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def colour(c):
    sc = c.get('stroking_color')
    if isinstance(sc, (list, tuple)) and len(sc) == 3:
        if all(abs(a - b) < 1e-3 for a, b in zip(sc, RED)):
            return 'red'
        if all(abs(a - b) < 1e-3 for a, b in zip(sc, BLUE)):
            return 'blue'
    return 'black'


def words(page):
    return page.extract_words(keep_blank_chars=False, use_text_flow=True)


def centre(o):
    return ((o['x0'] + o['x1']) / 2, (o['top'] + o['bottom']) / 2)


def boxes_with_labels(page, ws, region):
    """Curves (rounded boxes) in region (x0, top, x1, bottom) and the word inside each."""
    x0, t0, x1, b0 = region
    res = []
    for c in page.curves:
        if c['x0'] >= x0 and c['x1'] <= x1 and c['top'] >= t0 and c['bottom'] <= b0 and c['x1'] - c['x0'] > 12:
            inside = [w['text'] for w in ws if c['x0'] < centre(w)[0] < c['x1'] and c['top'] < centre(w)[1] < c['bottom']]
            res.append((c, inside))
    return res


def student():
    pdf = pdfplumber.open(STU)
    pages = pdf.pages
    check(len(pages) == 6, f'student packet has 6 pages (found {len(pages)})')
    check(all(round(p.width) == 612 and round(p.height) == 792 for p in pages), 'all pages US Letter 612 x 792 pt')
    texts = [p.extract_text() or '' for p in pages]
    for i, t in enumerate(texts, 1):
        check(t.startswith('Week 82 / Endless class lines / Grades 3–5'), f'p. {i} header')
        check('Bellingham Math Circle / Week 82 /' in t.replace('BellinghamMathCircle/Week82/', 'Bellingham Math Circle / Week 82 /')
              or 'BellinghamMathCircle/Week82' in t, f'p. {i} footer')
    nums = [int(n) for t in texts for n in re.findall(r'Problem (\d+):', t)]
    check(nums == [1, 2, 3, 4], f'problems numbered consecutively {nums}')

    # ---- p. 1 opening
    p = pages[0]
    ws = words(p)
    say('== p. 1 opening pictures ==')
    tops = [w for w in ws if w['text'] in '12345' and 150 < w['top'] < 165]
    bots = [w for w in ws if w['text'] in 'ABCDEF' and len(w['text']) == 1 and 200 < w['top'] < 215]
    lines = [l for l in p.lines if 150 < l['top'] < 220]
    panels = [(60, 200), (220, 360), (380, 540)]
    expected = [
        ({'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E'}, 'Complete match keeps order'),
        ({'1': 'B', '2': 'A', '3': 'C', '4': 'D', '5': 'E'}, 'Complete match does not keep order'),
        ({'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E'}, '5 kids and 6 no complete match possible'),
    ]
    for (xa, xb), (exp, cap) in zip(panels, expected):
        tl = [w for w in tops if xa < w['x0'] < xb]
        bl = [w for w in bots if xa < w['x0'] < xb]
        mp = {}
        for l in [l for l in lines if xa < l['x0'] < xb]:
            (ax, ay), (bx, by) = l['pts'][0], l['pts'][-1]
            up, dn = ((ax, ay), (bx, by)) if ay < by else ((bx, by), (ax, ay))
            t = min(tl, key=lambda w: abs(centre(w)[0] - up[0]))
            b = min(bl, key=lambda w: abs(centre(w)[0] - dn[0]))
            check(abs(centre(t)[0] - up[0]) < 1.5 and abs(centre(b)[0] - dn[0]) < 1.5,
                  f'   line ends at box centres: {t["text"]}-{b["text"]}')
            mp[t['text']] = b['text']
        tops_txt = sorted(w['text'] for w in tl)
        bots_txt = sorted(w['text'] for w in bl)
        unused = sorted(set(bots_txt) - set(mp.values()))
        say(f'   "{cap}": top {tops_txt}, bottom {bots_txt}, lines {mp}, bottom left out {unused}')
        check(mp == exp, f'"{cap}": lines are {exp}')
        complete = len(mp) == len(tops_txt) == len(bots_txt) and len(set(mp.values())) == len(mp)
        order = all((a < b) == (mp[a] < mp[b]) for a in mp for b in mp if a != b)
        if 'possible' in cap:
            check(not complete and len(bots_txt) == 6 and unused == ['F'], f'"{cap}": 5 top, 6 bottom, F unmatched')
            lo = [w for w in ws if w['text'] in ('leftout', 'left') and w['top'] > 215]
            fw = [w for w in bl if w['text'] == 'F'][0]
            check(lo and abs(centre(lo[0])[0] - centre(fw)[0]) < 6 and lo[0]['top'] > fw['bottom'],
                  '"left out" printed directly under F')
        else:
            check(complete, f'"{cap}": complete')
            check(order == ('does not' not in cap), f'"{cap}": order keeping = {order}')

    say('== p. 1 Problem 1 ==')
    r = sorted([w for w in ws if re.fullmatch(r'R\d', w['text'])], key=lambda w: w['x0'])
    b = sorted([w for w in ws if re.fullmatch(r'B\d', w['text'])], key=lambda w: w['x0'])
    check([w['text'] for w in r] == ['R1', 'R2', 'R3'] and len({round(w['top']) for w in r}) == 1, 'R1 R2 R3 on one line')
    check([w['text'] for w in b] == ['B1', 'B2', 'B3'] and len({round(w['top']) for w in b}) == 1, 'B1 B2 B3 on one line below')

    # ---- p. 2 Problem 2
    say('== p. 2 Problem 2 ==')
    p = pages[1]
    ws = words(p)
    rows = {}
    for lab, (t0, b0) in {'A': (135, 200), 'B': (220, 290), 'C': (300, 370)}.items():
        boxes = boxes_with_labels(p, ws, (100, t0, 400, b0))
        seq = [''.join(i) for c, i in sorted(boxes, key=lambda x: x[0]['x0'])]
        rows[lab] = seq
        cont = ' '.join(w['text'] for w in ws if t0 < w['top'] < b0 and w['text'] in ('numbers', 'continue', 'forever'))
        say(f'   line {lab}: cards {seq}; continuation text "{cont}"')
    check(rows['A'][:3] == ['1', '2', '3'], 'A: 1 2 3 then "numbers continue forever"')
    check(rows['B'][:4] == ['⋆', '1', '2', '3'], 'B: star 1 2 3 then "numbers continue forever"')
    dashed = [c for c in p.curves if c.get('dash') and c['dash'][0]]
    star_panel = [c for c in p.curves if c['x0'] > 400 and c['top'] > 290 and not c.get('fill')]
    check(len(dashed) == 1 and len(star_panel) == 1, 'C: one dashed box around the endless row and one star panel')
    d, s = dashed[0], star_panel[0]
    inside = [w['text'] for w in ws if d['x0'] < w['x0'] and w['x1'] < d['x1'] and d['top'] < w['top'] < d['bottom']]
    panel_txt = [w['text'] for w in ws if s['x0'] < w['x0'] and w['x1'] < s['x1'] and s['top'] < w['top'] < s['bottom']]
    say(f'   C dashed box x {d["x0"]:.1f}-{d["x1"]:.1f} holds {inside}; star panel x {s["x0"]:.1f}-{s["x1"]:.1f} holds {panel_txt}')
    check(s['x0'] > d['x1'] and '⋆' not in inside and '⋆' in panel_txt and 'EVERY' in panel_txt,
          'C: star panel ("after EVERY numbered kid") lies wholly to the right of the boxed endless row')

    # ---- p. 3 Problem 3
    say('== p. 3 Problem 3 ==')
    p = pages[2]
    ws = words(p)
    dcards = [(c, i) for c, i in boxes_with_labels(p, ws, (90, 100, 560, 160)) if c['x1'] - c['x0'] < 60]
    dboxes = [c for c in p.curves if c.get('dash') and c['dash'][0]]
    reds = sorted([(c, ''.join(i)) for c, i in dcards if colour(c) == 'red'], key=lambda x: x[0]['x0'])
    blues = sorted([(c, ''.join(i)) for c, i in dcards if colour(c) == 'blue'], key=lambda x: x[0]['x0'])
    say(f'   D red cards {[t for _, t in reds]}, blue cards {[t for _, t in blues]}')
    check([t for _, t in reds] == ['R1', 'R2', 'R3'] and [t for _, t in blues] == ['B1', 'B2', 'B3'], 'D: red R1-R3 and blue B1-B3 cards')
    check(len({round(c['top'], 1) for c, _ in reds + blues}) == 1, 'D: all six cards on one horizontal line')
    rb = [c for c in dboxes if colour(c) == 'red'][0]
    bb = [c for c in dboxes if colour(c) == 'blue'][0]
    check(rb['x1'] < bb['x0'] and max(c['x1'] for c, _ in reds) < bb['x0'], 'D: whole red box (and its arrow) is left of the blue box')
    check(all(rb['x0'] <= c['x0'] and c['x1'] <= rb['x1'] for c, _ in reds) and all(bb['x0'] <= c['x0'] and c['x1'] <= bb['x1'] for c, _ in blues),
          'D: each colour\'s cards are inside its own dashed box')
    ecards = sorted(boxes_with_labels(p, ws, (100, 270, 460, 330)), key=lambda x: x[0]['x0'])
    eseq = [''.join(i) for _, i in ecards]
    ecol = [colour(c) for c, _ in ecards]
    say(f'   E cards {eseq} colours {ecol}')
    check(eseq == ['R1', 'B1', 'R2', 'B2', 'R3', 'B3'] and ecol == ['red', 'blue'] * 3, 'E: R1 B1 R2 B2 R3 B3 alternating red/blue')
    arrow = [l for l in p.lines if 280 < l['top'] < 320 and l['x0'] > ecards[-1][0]['x1']]
    check(len(arrow) == 1, 'E: continuation arrow after B3 ("R4, B4, R5, B5, ... pairs continue forever")')
    check('R4, B4, R5, B5,' in texts[2] and 'pairs continue forever' in texts[2], 'E: continuation text')
    check('The whole blue row starts after EVERY red kid.' in texts[2] and 'There is no last red kid.' in texts[2], 'D: caption')

    # ---- p. 4
    say('== p. 4 Problem 4 ==')
    p = pages[3]
    bx = [c for c in p.curves if c['x1'] - c['x0'] > 300]
    sizes = {(round(c['x1'] - c['x0'], 1), round(c['bottom'] - c['top'], 1)) for c in bx}
    gaps = [round(bx[i + 1]['top'] - bx[i]['bottom'], 1) for i in range(len(bx) - 1)]
    say(f'   {len(bx)} boxes, sizes {sizes}, vertical gaps {gaps} pt')
    check(len(bx) == 4 and len(sizes) == 1, 'four equal sketch boxes (two pairs of arrangements)')

    # ---- p. 5 cards
    say('== p. 5 cards ==')
    p = pages[4]
    ws = words(p)
    cards = boxes_with_labels(p, ws, (0, 0, 612, 792))
    labs = [''.join(i) for _, i in cards]
    want = [f'R{n}' for n in range(1, 13)] + [f'B{n}' for n in range(1, 13)]
    check(sorted(labs) == sorted(want) and len(labs) == 24, '24 cards R1-R12 and B1-B12, each once')
    check(all(colour(c) == ('red' if l.startswith('R') else 'blue') for (c, _), l in zip(cards, labs)), 'R cards red, B cards blue')
    say('   card frame sizes (pt):', sorted({(round(c['x1'] - c['x0'], 1), round(c['bottom'] - c['top'], 1)) for c, _ in cards}))

    # ---- p. 6
    say('== p. 6 stars and panels ==')
    t6 = texts[5]
    check(t6.count('⋆') == 4, f'four star cards (found {t6.count("⋆")})')
    check(t6.count('This kid comes after EVERY kid') == 2 and t6.count('This whole row starts after EVERY kid') == 2,
          'two "this kid" panels and two "this whole row" panels')
    return texts


def guide():
    say('== facilitator guide ==')
    t = subprocess.run(['pdftotext', '-layout', str(GUI), '-'], capture_output=True, text=True, check=True).stdout
    flat = re.sub(r'\s+', ' ', t)
    pages = t.split('\f')
    check(len([x for x in pages if x.strip()]) == 4, 'guide has 4 pages')
    quotes = [
        'numbered kid cards (student page 5), stars and after-every-kid panels (page 6)',
        'as on student pages 2–3',
        'five-to-five with the first two partners exchanged',
        '(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)',
        'Only the first keeps every pair in order.',
        'kid 1 receives the star and kid m ≥ 2 receives original m − 1',
        'The image of the appended last kid would have to be last, but every ordinary numbered kid has a successor.',
        'Their positions in E are 2n − 1 and 2n.',
        'No order-preserving match can send B1 to a kid with only finitely many predecessors',
        'An endless row of pairs has type 2 · ω = ω',
        'Each construction uses one row and at most two stars.',
        'ask about the first kid of block B',
        'Surreal addition is a distinct commutative operation',
    ]
    for q in quotes:
        check(q in flat, 'guide text: "' + q + '"')
    return flat


def main():
    say('Week 82 diagram and text read-back; repository:', REPO.name)
    texts = student()
    guide()
    stu_txt = subprocess.run(['pdftotext', str(STU), '-'], capture_output=True, text=True, check=True).stdout
    stu_flat = re.sub(r'\s+', ' ', stu_txt.replace('\ufb00', 'ff'))
    say('== student wording used in math.md ==')
    for q in ['A complete match gives each kid a partner in the other class, with nobody left out.',
              'Find every match between these two class lines. Which matches keep order?',
              'Can you match every kid? Can a match keep order?',
              'Find two different arrangements that can be matched while keeping order.',
              'Labels only identify kids.']:
        check(q in stu_flat, 'student text: "' + q + '"')
    check(stu_flat.count('Can a match keep order?') == 2, '"Can a match keep order?" appears in Problems 2 and 3')
    check('complete match' not in stu_flat.split('Problem 1:')[1], '"complete" is not used after the opening paragraph')
    say('')
    say(f'{len(FAIL)} failures')
    text = '\n'.join(OUT) + '\n'
    (HERE / 'check_diagrams.py.out').write_text(text)
    print(text)
    raise SystemExit(1 if FAIL else 0)


if __name__ == '__main__':
    main()
