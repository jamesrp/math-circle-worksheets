"""Read every card diagram back out of the delivered Week 24 student PDFs
(vector drawings + text), independently of the generator build_packets.py.

For each page it records: the problem number, every card (its rectangle, the
numeral printed in it or None for a blank card, the number of filled dots in it),
and the deck each card belongs to (the label letter beside or above it), plus
unlabeled card pools.  It checks that every dotted card's dot count equals its
numeral and that cards have one size per layout.

Output: decks.json (machine-readable) and out_extract_decks.txt (summary).
Needs PyMuPDF.  Run from anywhere: python3 extract_decks.py
"""
import json
import os
import re
import sys
from collections import defaultdict

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))  # plans/review/checks/week-24 -> repo
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):  # still in the tmp run folder
    ROOT = HERE
    while not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
        parent = os.path.dirname(ROOT)
        if parent == ROOT:
            sys.exit('repository not found above ' + HERE)
        ROOT = parent
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-24')
BANDS = {'k-1': 'week-24-k-1.pdf', 'grades-2-3': 'week-24-grades-2-3.pdf',
         'grades-4-5': 'week-24-grades-4-5.pdf'}

OUT = []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def inside(pt, r, pad=0.5):
    return r[0] - pad <= pt[0] <= r[2] + pad and r[1] - pad <= pt[1] <= r[3] + pad


def page_data(page):
    cards, dots = [], []
    for d in page.get_drawings():
        kinds = ''.join(it[0] for it in d['items'])
        if d['type'] == 's' and kinds == 'lclclclc':          # rounded rectangle = card
            r = d['rect']
            cards.append({'rect': [r.x0, r.y0, r.x1, r.y1]})
        elif d.get('fill') == (0.0, 0.0, 0.0) and kinds == 'cccc':  # filled dot
            r = d['rect']
            dots.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2, r.x1 - r.x0))
    words = page.get_text('words')
    text = ' '.join(w[4] for w in words)
    m = re.search(r'Problem (\d+):', text)
    prob = int(m.group(1)) if m else None
    used = set()
    for c in cards:
        nums = [i for i, w in enumerate(words)
                if inside(((w[0] + w[2]) / 2, (w[1] + w[3]) / 2), c['rect']) and w[4].isdigit()]
        used.update(nums)
        if len(nums) > 1:
            say('  WARNING: more than one numeral in a card', [words[i][4] for i in nums])
        c['value'] = int(words[nums[0]][4]) if nums else None
        c['dots'] = sum(1 for (x, y, _) in dots if inside((x, y), c['rect']))
    stray = [d for d in dots if not any(inside(d[:2], c['rect']) for c in cards)]
    # deck labels: single capital letters that are not inside a card and are below the prompt
    labels = []
    for i, w in enumerate(words):
        if re.fullmatch(r'[A-H]', w[4]) and i not in used and w[1] > 100 and w[3] < 740:
            # exclude the letters that are part of the prompt sentence (prompt words have size < 17pt,
            # same line as other prompt words); labels stand alone, so test for neighbours on the line
            same_line = [v for v in words if abs(v[1] - w[1]) < 1 and v is not w
                         and not re.fullmatch(r'[A-H]', v[4]) and not v[4].isdigit()]
            if not same_line:
                labels.append({'letter': w[4], 'cx': (w[0] + w[2]) / 2, 'cy': (w[1] + w[3]) / 2,
                               'top': w[1], 'bottom': w[3]})
    return prob, cards, labels, stray


def assign(cards, labels):
    """Row label: a label to the left whose centre lies in the card's vertical span (nearest).
    Otherwise inherit from the card directly above if the gap is < 0.3 in, else a label just
    above (gap < 0.5 in, horizontal offset < 60 pt).  Otherwise the card is in an unlabeled pool."""
    for li, l in enumerate(labels):
        l['id'] = li
    for c in sorted(cards, key=lambda c: c['rect'][1]):
        x0, y0, x1, y1 = c['rect']
        row = [l for l in labels if y0 <= l['cy'] <= y1 and l['cx'] < x0]
        if row:
            c['label'] = max(row, key=lambda l: l['cx'])['id']
            continue
        above_cards = [d for d in cards if d is not c and d['rect'][3] <= y0 + 0.5
                       and min(x1, d['rect'][2]) - max(x0, d['rect'][0]) > 0.5 * (x1 - x0)
                       and y0 - d['rect'][3] < 0.3 * 72]
        if above_cards:
            d = max(above_cards, key=lambda d: d['rect'][3])
            c['label'] = d.get('label')
            continue
        cx = (x0 + x1) / 2
        above = [l for l in labels if l['bottom'] <= y0 + 0.5 and y0 - l['bottom'] < 0.5 * 72
                 and abs(l['cx'] - cx) < 60]
        c['label'] = min(above, key=lambda l: abs(l['cx'] - cx) + (y0 - l['bottom']))['id'] if above else None


def reading_order(cs):
    return sorted(cs, key=lambda c: (round(c['rect'][1] / 10), c['rect'][0]))


def main():
    result = {}
    bad = 0
    for band, fn in BANDS.items():
        doc = pymupdf.open(os.path.join(WEEK, fn))
        say(f'=== {band}: {fn} ({doc.page_count} pages)')
        pages = []
        for pno, page in enumerate(doc, 1):
            prob, cards, labels, stray = page_data(page)
            assign(cards, labels)
            decks = defaultdict(list)
            pool = []
            for c in reading_order(cards):
                (decks[c['label']] if c['label'] is not None else pool).append(c)
            dl = []
            for lid, cs in sorted(decks.items(), key=lambda kv: (round(labels[kv[0]]['cy'] / 10), labels[kv[0]]['cx'])):
                dl.append({'label': labels[lid]['letter'], 'values': [c['value'] for c in cs],
                           'dots': [c['dots'] for c in cs], 'xy': [round(labels[lid]['cx']), round(labels[lid]['cy'])]})
            unlabeled = [l['letter'] for l in labels if not any(c.get('label') == l['id'] for c in cards)]
            sizes = sorted({(round(c['rect'][2] - c['rect'][0], 1), round(c['rect'][3] - c['rect'][1], 1)) for c in cards})
            say(f'page {pno}: Problem {prob}; {len(cards)} cards; card sizes (pt) {sizes}')
            for d in dl:
                dot_note = ''
                if any(d['dots']):
                    dot_note = ' dots ' + str(d['dots'])
                say(f'   deck {d["label"]} at {d["xy"]}: {d["values"]}{dot_note}')
            if pool:
                say(f'   unlabeled pool: {[c["value"] for c in pool]}' +
                    (' dots ' + str([c['dots'] for c in pool]) if any(c['dots'] for c in pool) else ''))
            if unlabeled:
                say('   WARNING labels with no card:', unlabeled); bad += 1
            if stray:
                say('   WARNING dots outside any card:', len(stray)); bad += 1
            # dot audit: every card that carries dots must carry exactly `value` dots
            for c in cards:
                if c['dots'] and c['dots'] != c['value']:
                    say('   FAIL dot count', c['dots'], '!= numeral', c['value']); bad += 1
            dotted = [c for c in cards if c['value'] is not None and c['dots']]
            if band == 'k-1':
                undotted = [c['value'] for c in cards if c['value'] is not None and not c['dots']]
                if undotted:
                    say('   NOTE K-1 numeral cards without dots:', undotted)
            pages.append({'page': pno, 'problem': prob, 'decks': dl,
                          'pool': [c['value'] for c in pool], 'dotted_cards_ok': len(dotted)})
        result[band] = pages
    json.dump(result, open(os.path.join(HERE, 'decks.json'), 'w'), indent=1)
    say('dot-count or label problems found:', bad)
    open(os.path.join(HERE, 'out_extract_decks.txt'), 'w').write('\n'.join(OUT) + '\n')
    print('\n'.join(OUT))


if __name__ == '__main__':
    main()
