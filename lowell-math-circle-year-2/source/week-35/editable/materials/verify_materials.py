#!/usr/bin/env python3
"""Measure the Week 35 kit PDF and check the cards against the guide's borders.

Usage: python3 materials/verify_materials.py [path/to/materials.pdf]
(default: build/materials.pdf). Needs PyMuPDF. Every size is read back from
the PDF's vector drawings in points and converted to millimetres. Each
card's footprint outline is compared vertex by vertex with
src/mathematical-checks.json, the student builder's motif.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement
from pathlib import Path
import json
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
V = json.loads((ROOT / 'src' / 'mathematical-checks.json').read_text())['motif_vertices']
MM = 25.4 / 72
TOL = 0.05
SCALE = 10.0
CW, CH = 29.0, 26.0


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def same_points(a, b, tol=0.02):
    return len(a) == len(b) and all(any(close(p[0], q[0], tol) and close(p[1], q[1], tol) for q in b) for p in a)


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build' / 'materials.pdf'
    doc = pymupdf.open(pdf)
    assert len(doc) == 1 and (round(doc[0].rect.width), round(doc[0].rect.height)) == (612, 792)
    page = doc[0]
    cards, outlines, shafts, heads, scale = [], [], [], [], []
    for d in page.get_drawings():
        r = [v * MM for v in d['rect']]
        kinds = [it[0] for it in d['items']]
        if kinds == ['l', 'l', 'l', 'l'] and 's' in d['type'] and close(r[2] - r[0], CW) and close(r[3] - r[1], CH):
            cards.append(r)
        elif len(kinds) == 12 and all(k == 'l' for k in kinds) and 'f' in d['type']:
            outlines.append(([(it[1].x * MM, it[1].y * MM) for it in d['items']], r))
        elif kinds == ['l'] and d['type'] == 's':
            if close(r[1], r[3]) and close(r[2] - r[0], 100.0):
                scale.append(r)
            elif close(r[1], r[3]) and r[2] - r[0] < 10:
                shafts.append(r)
        elif 'f' in d['type'] and r[2] - r[0] < 4:
            heads.append(r)
    assert len(scale) == 1
    print('PASS page: one US Letter portrait page with one 100.00 mm scale line.')

    assert len(cards) == 48, len(cards)
    a = [(x, y) for x, y in V]
    m = [(x, -y) for x, y in V]
    forms = Counter()
    for c in cards:
        cx, cy = (c[0] + c[2]) / 2, (c[1] + c[3]) / 2
        mine = [o for o in outlines if c[0] < (o[1][0] + o[1][2]) / 2 < c[2] and c[1] < (o[1][1] + o[1][3]) / 2 < c[3]]
        assert len(mine) == 1
        pts, bb = mine[0]
        assert close(bb[2] - bb[0], 26.0) and close(bb[3] - bb[1], 22.0), bb
        assert close((bb[0] + bb[2]) / 2, cx) and close((bb[1] + bb[3]) / 2, cy)
        rel = [((x - cx) / SCALE, (y - cy) / SCALE) for x, y in pts]
        kind = 'A' if same_points(rel, a) else 'mirror A' if same_points(rel, m) else None
        assert kind, rel
        sy = 1 if kind == 'A' else -1
        sh = [s for s in shafts if c[0] < s[0] < c[2] and c[1] < s[1] < c[3]]
        assert len(sh) == 1 and close(sh[0][0], cx - 2.5) and close(sh[0][1], cy - sy * 8.6), (sh, cx, cy)
        hd = [h for h in heads if c[0] < h[0] < c[2] and c[1] < h[1] < c[3]]
        assert len(hd) == 1 and abs(hd[0][2] - (cx + 5.5)) < 0.5 and hd[0][0] > sh[0][0], hd
        set_no = 1 if cy < 150 else 2
        forms[(set_no, kind)] += 1
    assert forms == Counter({(1, 'A'): 12, (1, 'mirror A'): 12, (2, 'A'): 12, (2, 'mirror A'): 12}), forms
    print('PASS cards: 48 cards of 29.00 x 26.00 mm in two sets; each set has 12 A and 12 mirror A '
          '(the student motif flipped over a horizontal line), read back vertex by vertex. Every footprint '
          'is 26.00 x 22.00 mm, centred on its card, with its arrow pointing right along the top bar (A) '
          'or bottom bar (mirror A).')

    # Shared cut lines: cards in a set abut, so straight cuts separate them.
    for set_no in (1, 2):
        cs = sorted((c for c in cards if (((c[1] + c[3]) / 2 < 150) == (set_no == 1))), key=lambda c: (c[1], c[0]))
        xs = sorted({round(c[0], 2) for c in cs}) + [round(max(c[2] for c in cs), 2)]
        ys = sorted({round(c[1], 2) for c in cs}) + [round(max(c[3] for c in cs), 2)]
        assert len(xs) == 7 and len(ys) == 5
        assert all(close(xs[i + 1] - xs[i], CW) for i in range(6)) and all(close(ys[i + 1] - ys[i], CH) for i in range(4))
    print('PASS cutting: each set is one 6 x 4 block of abutting cards (174.00 x 104.00 mm): '
          '3 cuts across and 5 cuts down each strip.')

    # The guide's witnesses (page 4 since October 23, 2026), centres in mm, h = 15 mm; form -> card.
    # G at 4 and 8 cm: the 2-3 P2 pair of glide borders and the K-1 P4 longer slide.
    card_of = {'A': 'A', 'R A': 'A', 'H A': 'mirror', 'V A': 'mirror'}
    recipes = {
        'T (4 cm)': (40, [(0, 15, 'A')]), 'T (6 cm)': (60, [(0, 15, 'A')]),
        'G': (60, [(0, 15, 'A'), (30, -15, 'H A')]), 'G (4 cm)': (40, [(0, 15, 'A'), (20, -15, 'H A')]),
        'G (8 cm)': (80, [(0, 15, 'A'), (40, -15, 'H A')]), 'H': (60, [(0, 15, 'A'), (0, -15, 'H A')]),
        'R': (60, [(0, 15, 'A'), (30, -15, 'R A')]),
        'E': (60, [(15, 15, 'A'), (-15, 15, 'V A'), (15, -15, 'H A'), (-15, -15, 'R A')]),
    }

    def window(name, length, shift):
        period, motifs = recipes[name]
        out = []
        for k in range(-3, int(length // period) + 4):
            for x, y, f in motifs:
                cx = x + period * k + shift
                if cx - CW / 2 >= 0 and cx + CW / 2 <= length:
                    out.append((cx, y, card_of[f]))
        return out

    def best(name, length):
        period = recipes[name][0]
        return max((Counter(c[2] for c in window(name, length, s / 2)) for s in range(2 * period)),
                   key=lambda n: (n['A'] + n['mirror'], n['A']))

    for name in recipes:
        cs = window(name, 400, 0)
        for p, q in combinations(cs, 2):
            assert abs(p[0] - q[0]) >= CW or abs(p[1] - q[1]) >= CH, (name, p, q)
        assert all(abs(y) + CH / 2 <= 30 for _, y, _ in cs)
    print('PASS fit: in all eight witness borders (T at 4 and 6 cm, G at 6, 4 and 8 cm, H, R, E with h = 15 mm) no two cards '
          'overlap, and every card stays within the 6 cm board (28 mm from the middle line at most).')

    board, strip = 176.5, 280.0
    need = {n: (best(n, board), best(n, strip)) for n in recipes}
    worst_board = max(max(b['A'], b['mirror']) for b, _ in need.values())
    worst_strip = max(max(s['A'], s['mirror']) for _, s in need.values())
    # Two borders side by side, every pairing of witnesses.
    pairs_board = max(max(need[x][0]['A'] + need[y][0]['A'], need[x][0]['mirror'] + need[y][0]['mirror'])
                      for x, y in combinations_with_replacement(recipes, 2))
    two_t = need['T (4 cm)'][1]['A'] + need['T (6 cm)'][1]['A']
    assert worst_board <= 12 and worst_strip <= 12 and pairs_board <= 12 and two_t <= 12
    for n, (b, s) in need.items():
        print(f'  {n:9s} printed board: {b["A"]:2d} A, {b["mirror"]:2d} mirror;  280 mm strip: '
              f'{s["A"]:2d} A, {s["mirror"]:2d} mirror')
    print(f'PASS problem needs: a set fills one witness border on a 280 mm strip (at most {worst_strip} cards of '
          f'one kind) and any two witnesses side by side on the printed boards (at most {pairs_board}). '
          f'Two slide-only borders on 280 mm strips (K-1 P2, 2-3 P1, 4-5 P1) use {two_t} A cards.')
    r_t = need['R'][1]['A'] + need['T (6 cm)'][1]['A']
    # Corrected October 23, 2026 (Critic L could 8): the K-1 table works as two pairs, one set each, so Set 2 is not
    # spare there. Both P6 borders repeat every 6 cm, which the guide builds in the printed boxes.
    print(f'NOTE: K-1 P6 on two 280 mm strips with R and a 6 cm slide border would use {r_t} A cards, more than a set; '
          f'both repeat every 6 cm, so they go in the printed boxes, where two borders use at most {pairs_board}.')


if __name__ == '__main__':
    main()
