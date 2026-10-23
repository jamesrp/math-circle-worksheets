"""Check of the Week 33 critic follow-up, October 23, 2026 (F33-*-v4).

Critic B's should: Problem 1 printed four three-bead boards for exactly four rings, so a
child who filled the fourth knew the list was complete. v4 prints six boards in every band.
Critic B's could: the guide's Grades 4-5 Problem 5 key named AAAAAAAAB, which needs eight
A counters from a six-A, six-B kit; v4 names AAAAABBBB.

Reads the delivered PDFs (current and archived v3). Run: python3 check_critic_fixes.py
(writes out_check_critic_fixes.txt beside itself).
"""
import math
import os
import re
import sys

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
W = os.path.join(ROOT, 'lowell-math-circle-year-2/week-33')
ARC = os.path.join(W, 'archive-before-critic-fixes-2026-10-23')
CM = 72 / 2.54
OUT = []


def ok(cond, msg):
    if not cond:
        raise SystemExit('FAIL ' + msg)
    OUT.append('ok   ' + msg)


def boards(page):
    """Gray ring circles of the bead boards and their white bead circles."""
    rings, beads = [], []
    for d in page.get_drawings():
        r = d['rect']
        gray = d.get('color') and abs(d['color'][0] - 0.675) < 0.01
        if gray and abs(r.width - r.height) < 0.2 and r.width > 60:
            rings.append(r)
        if d.get('fill') == (1.0, 1.0, 1.0) and abs(r.width - 23.8) < 0.3:
            beads.append(r)
    return rings, beads


TAGS = {'k-1': 'K', 'grades-2-3': '23', 'grades-4-5': '45'}
for band, tag in TAGS.items():
    new = pymupdf.open(os.path.join(W, f'week-33-{band}.pdf'))
    old = pymupdf.open(os.path.join(ARC, f'week-33-{band}.pdf'))
    ok(len(new) == len(old) == 6, f'{band}: still 6 pages')
    for i, p in enumerate(new, 1):
        ok(f'Bellingham Math Circle / Week 33 / F33-{tag}-v4' in p.get_text(), f'{band} p. {i}: footer F33-{tag}-v4')
    # Problem 1: six boards (four before), each a three-bead ring.
    rn, bn = boards(new[0])
    ro, bo = boards(old[0])
    small_new = [r for r in rn if r.y0 > 9 * CM]
    small_old = [r for r in ro if r.y0 > 9 * CM]
    ok(len(small_old) == 4 and len(small_new) == 6, f'{band} p. 1: Problem 1 had 4 boards, now 6 ({len(small_old)} -> {len(small_new)})')
    rad = small_new[0].width / 2 / CM
    ok(all(abs(r.width / 2 / CM - 1.75) < 0.01 for r in small_new), f'{band} p. 1: each board radius {rad:.2f} cm')
    beads = [b for b in bn if b.y0 > 9 * CM]
    ok(len(beads) == 18, f'{band} p. 1: 18 bead spots, three on each board')
    chord = rad * math.sqrt(3)
    ok(chord > 3.0, f'{band} p. 1: bead centres {chord:.2f} cm apart on a board (room for a 2.5 cm counter)')
    # Layout: the boards stay below the prompt and above the footer.
    words = new[0].get_text('words')
    prompt_bottom = max(w[3] for w in words if w[1] > 7.5 * CM + 1.65 * CM and w[1] < 10 * CM + 1.65 * CM - 20 and w[4] != 'start')
    start_tops = sorted(w[1] for w in words if w[4] == 'start' and w[1] > prompt_bottom)
    ok(start_tops[0] - prompt_bottom > 0.2 * CM, f'{band} p. 1: first board label {(start_tops[0] - prompt_bottom) / CM:.2f} cm below the prompt')
    footer_top = min(w[1] for w in words if w[4] == 'Bellingham')
    low = max([r.y1 for r in small_new] + [d['rect'].y1 for d in new[0].get_drawings() if d['rect'].y1 < footer_top])
    ok(footer_top - low > 0.5 * CM, f'{band} p. 1: lowest drawing {(footer_top - low) / CM:.2f} cm above the footer')
    # Recording lines: three beside each board.
    lines = [d for d in new[0].get_drawings() if d['rect'].height < 0.1 and d.get('color') and abs(d['color'][0] - 0.775) < 0.01
             and d['rect'].y0 > 9 * CM]
    ok(len(lines) == 18, f'{band} p. 1: 18 recording lines, three beside each board')
    # Every ring overlaps no other ring and no recording line.
    clash = [(a, b) for i, a in enumerate(small_new) for b in small_new[i + 1:] if a.intersects(b)]
    clash += [(a, l['rect']) for a in small_new for l in lines if a.intersects(l['rect'])]
    ok(not clash, f'{band} p. 1: no board touches another board or a recording line')
    # The prompt wording is unchanged.
    flat = lambda p: re.sub(r'\s+', ' ', p.get_text())
    ok(flat(old[0]).replace('-v3', '-v4').replace(' start', '') == flat(new[0]).replace(' start', ''),
       f'{band} p. 1: wording unchanged apart from the footer (two more "start" labels)')
    for i in range(1, 6):
        ok(flat(old[i]).replace(f'F33-{tag}-v3', f'F33-{tag}-v4') == flat(new[i]), f'{band} p. {i + 1}: text unchanged apart from the footer')
        a = old[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 760))
        b = new[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 760))
        ok(a.samples == b.samples, f'{band} p. {i + 1}: pixels above the footer unchanged')

# Guide: the P5 key's example words, against the kit (six A and six B).
G = pymupdf.open(os.path.join(W, 'week-33-facilitator.pdf'))
GO = pymupdf.open(os.path.join(ARC, 'week-33-facilitator.pdf'))
gt = ' '.join(p.get_text() for p in G)
ok('AAAAAAAAB' not in gt and 'AABAABAAB, AAAAABBBB' in gt, 'guide: Grades 4-5 P5 key names AAAAABBBB in place of AAAAAAAAB')


def readouts(w):
    return len({w[i:] + w[:i] for i in range(len(w))})


key = {'ABABAB': 2, 'AABAAB': 3, 'AAAAAB': 6, 'AABAABAAB': 3, 'AAAAABBBB': 9}
for w, n in key.items():
    ok(readouts(w) == n and w.count('A') <= 6 and w.count('B') <= 6,
       f'guide P5 key: {w} has {readouts(w)} readouts and needs {w.count("A")} A and {w.count("B")} B (kit: six of each)')
ok(readouts('AAAAAAAAB') == 9 and 'AAAAAAAAB'.count('A') == 8, 'the replaced AAAAAAAAB also had 9 readouts but needed eight A')
ok(len(G) == len(GO), f'guide: still {len(G)} pages')
for i in range(len(G)):
    a, b = GO[i].get_text(), G[i].get_text()
    ok(a.replace('AAAAAAAAB', 'AAAAABBBB') == b, f'guide p. {i + 1}: text unchanged apart from that word')

print('\n'.join(OUT))
print(f'{len(OUT)} checks passed')
with open(os.path.join(HERE, 'out_check_critic_fixes.txt'), 'w') as f:
    f.write('\n'.join(OUT) + f'\n{len(OUT)} checks passed\n')
