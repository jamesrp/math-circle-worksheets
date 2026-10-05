"""Grades 4-5 Problem 12: times tables on 24 numbered dots.

Checks the printed numbering (label i beside dot i, clockwise from 0 at the top), then counts the
lines m -> 2m and m -> 3m (mod 24): dots that land on themselves, lines drawn twice, distinct lines,
and which self-landing dots are still the end of some other dot's line. Finally locates the cusps
of the envelope (cardioid / nephroid) numerically."""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE

G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))
page = G['U'][8]
BAD = []

rings = [c for c in page['circles'] if c['fill'] is None and c['rx'] > 100]
dots = [c for c in page['circles'] if c['fill'] == 0.0 and c['rx'] < 5]
nums = [w for w in page['words'] if w['t'].isdigit() and w['y0'] > 120 and w['y1'] < 730]
for ring in sorted(rings, key=lambda r: r['cy']):
    cx, cy, R = ring['cx'], ring['cy'], ring['rx']
    mine = [d for d in dots if abs(math.hypot(d['cx'] - cx, d['cy'] - cy) - R) < 0.5]
    labs = [w for w in nums if abs(math.hypot((w['x0'] + w['x1']) / 2 - cx, (w['y0'] + w['y1']) / 2 - cy) - R) < 25]
    ok = True
    for w in labs:
        i = int(w['t'])
        lx, ly = (w['x0'] + w['x1']) / 2, (w['y0'] + w['y1']) / 2
        d = min(mine, key=lambda d: math.hypot(d['cx'] - lx, d['cy'] - ly))
        ang = (90 - math.degrees(math.atan2(cy - d['cy'], d['cx'] - cx))) % 360
        if abs(ang - 15 * i) > 0.05 and abs(ang - 15 * i - 360) > 0.05:
            ok = False
            print('   label', i, 'is nearest a dot at', round(ang, 2), 'deg')
    print(f'ring at ({cx:.0f},{cy:.0f}): {len(mine)} dots, labels {sorted(int(w["t"]) for w in labs) == list(range(24))} '
          f'(0..23 each once), every label beside dot number*15 deg clockwise from the top: {ok}')
    if not ok or len(mine) != 24:
        BAD.append('numbering')

n = 24
for k in (2, 3):
    arrows = [(m, k * m % n) for m in range(n)]
    selfs = [m for m, t in arrows if m == t]
    lines = [frozenset(a) for a in arrows if a[0] != a[1]]
    twice = sorted(tuple(sorted(l)) for l in set(lines) if lines.count(l) == 2)
    ends = {m: sorted(a for a, t in arrows if t == m and a != m) for m in selfs}
    print(f'x{k}: dots landing on themselves {selfs}; lines drawn twice {twice}; distinct lines {len(set(lines))}; '
          f'other dots whose line ends at a self-landing dot: {ends}')
    print(f'    dots that are the end of no line at all: {[m for m in range(n) if not any(m in l for l in lines)]}')
    print(f'    13 -> {k * 13 % n}' if k == 2 else '')

# envelope of chords theta -> k*theta: contact point (k e^{i t} + e^{i k t}) / (k + 1); cusps where its speed is 0
for k in (2, 3):
    f = lambda t: (k * cmath.exp(1j * t) + cmath.exp(1j * k * t)) / (k + 1)
    cusps = []
    N = 3600
    for j in range(N):
        t = 2 * math.pi * j / N
        v = abs(f(t + 1e-6) - f(t - 1e-6)) / 2e-6
        if v < 1e-3:
            cusps.append(round(math.degrees(t), 2))
    # theta measured from dot 0; dot m sits at theta = 15 m degrees
    print(f'x{k}: envelope cusps at theta = {cusps} deg -> dots {[c / 15 for c in cusps]}; on the circle: '
          f'{[round(abs(f(math.radians(c))), 6) for c in cusps]}')
print('SUMMARY:', 'all checks agree' if not BAD else BAD)


def draw_completed(path):
    """Draw both completed pages (24 dots, dot 0 at the top, clockwise) with the envelope cusps
    marked in red and the fixed dots ringed in blue, as a PNG to look at."""
    import pymupdf
    doc = pymupdf.open()
    pg = doc.new_page(width=640, height=330)
    for col, k in enumerate((2, 3)):
        cx, cy, R = 160 + 320 * col, 165, 140

        def P(m, r=R):
            a = math.radians(90 - 15 * m)
            return pymupdf.Point(cx + r * math.cos(a), cy - r * math.sin(a))
        pg.draw_circle(pymupdf.Point(cx, cy), R, color=(0.7, 0.7, 0.7), width=0.5)
        for m in range(24):
            t = k * m % 24
            if t != m:
                pg.draw_line(P(m), P(t), color=(0, 0, 0), width=0.6)
            pg.draw_circle(P(m), 2, color=(0, 0, 0), fill=(0, 0, 0))
            pg.insert_text(P(m, R + 10) + (-4, 3), str(m), fontsize=7)
        for m in range(24):
            if k * m % 24 == m:
                pg.draw_circle(P(m), 6, color=(0, 0, 1), width=1.2)
        for j in range(k - 1):
            th = (math.pi + 2 * math.pi * j) / (k - 1)          # (k-1) theta = pi (mod 2 pi)
            r = R * (k - 1) / (k + 1)
            pt = pymupdf.Point(cx + r * math.sin(th), cy - r * math.cos(th))
            pg.draw_circle(pt, 4, color=(1, 0, 0), width=1.5)
        pg.insert_text(pymupdf.Point(cx - R, 20), f'x{k}', fontsize=12)
    pg.get_pixmap(dpi=110).save(path)


draw_completed(os.path.join(HERE, 'times_tables_completed.png'))
print('wrote times_tables_completed.png (red: envelope cusps; blue: dots that land on themselves)')
