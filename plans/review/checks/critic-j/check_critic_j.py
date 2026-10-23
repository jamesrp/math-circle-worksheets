#!/usr/bin/env python3
"""Check the October 23, 2026 follow-ups to Critic J's coulds (Weeks 12, 25, 54, 55, 57, 71).

Usage: python3 plans/review/checks/critic-j/check_critic_j.py   (from the repository root)

Key page maps. A problem-file week's key view repeats answers from its print guide, and a few
of them cite student pages by their number in the full band packet; the first-route and
return packets number their pages afresh. A survey of every key and hint in the 54 weeks with
published route packets found eight such citations whose page moves in a route packet, in
Weeks 12, 13, 14, 25 and 42 (the other page numbers it found name guide pages). Those keys now
carry a page map (week.toml [guide] page_map = true). This script reads the published files
only: each map row must cover every page of its route packet, each route page's text must be
the named full-packet page's (or a subset of its lines, when the route leaves out a problem
that shares the page), and each of the eight citations must land on the route page named here.

K-1 band views. Weeks 54, 55 and 57 print one shared packet whose pages are headed for older
children; their guides route K-1, adult-led, through pp. 1-3, pp. 1-3 and copies of p. 4. The
page indexes name those routes, and the K-1 slices must be exactly those pages.

Week 57 guide p. 1 (W57-FAC-v4): the K-1 route's page reference names guide p. 3 and the
student p. 4 grids. Week 71 guide p. 2 (GGT71-FAC-v3): "So XYX with X and Y meeting at a
corner happens only at corners under 90 degrees", since ACA, CAC, BDB and DBD come from
parallel walls and occur in every room.
"""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
Y = ROOT / 'lowell-math-circle-year-2'
FAIL = []
FILES = {'K–1': 'k-1', 'Grades 2–3': 'grades-2-3', 'Grades 4–5': 'grades-4-5'}


def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg)
    if not ok:
        FAIL.append(msg)


def text(pdf, page=None, layout=False):
    args = ['pdftotext'] + (['-layout'] if layout else []) + (['-f', str(page), '-l', str(page)] if page else [])
    return subprocess.run(args + [str(pdf), '-'], capture_output=True, text=True, check=True).stdout


def lines(pdf, page):
    return [l.strip() for l in text(pdf, page).splitlines()
            if l.strip() and not re.search(r'Bellingham Math Circle|^\d+$', l.strip())]


def pages(pdf):
    out = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True, check=True).stdout
    return int(re.search(r'Pages:\s+(\d+)', out).group(1))


def span(s):
    a, _, b = s.partition('–')
    return list(range(int(a), int(b or a) + 1))


def page_map(week):
    """{(band file, route): {route page: full page}} read from the published key."""
    key = text(Y / 'band-views' / f'week-{week}' / f'week-{week}-key.pdf', layout=True)
    out = {}
    for band, route, runs in re.findall(r'^\s*(K–1|Grades \d–\d) (first|return)\s{2,}(.+)$', key, re.M):
        m = {}
        for own, was in re.findall(r'pp?\. (\d+(?:–\d+)?) = pp?\. (\d+(?:–\d+)?)', runs):
            m.update(zip(span(own), span(was)))
        out[(FILES[band], route)] = m
    return out


# week, key id, band file, route, cited full-packet pages, the route pages they must map to,
# and words on the route page that show it is the cited one.
CITATIONS = [
    (12, 'W12-G-v4', 'k-1', 'return', [4, 5], [3, 4], 'Problem 4', '"Pages 4 and 5 hold 16 frames"'),
    (13, 'F13-G-v4', 'k-1', 'return', [5], [3], 'Problem 5', '"K–1 page 5 has a large working board"'),
    (14, 'F14-G-v4', 'grades-2-3', 'return', [8], [6], 'Problem 7 (continued)', '"Student page 8"'),
    (25, 'W25-G-v4', 'grades-2-3', 'return', [4], [2], 'Problem 4', '"the student page 4 example"'),
    (25, 'W25-G-v4', 'grades-4-5', 'return', [5], [3], 'Problem 3 (continued)', '"Student page 5 has three blank grids"'),
    (25, 'W25-G-v4', 'grades-4-5', 'return', [7], [5], 'Problem 4 (continued)', '"Page 7 has three blank grids"'),
    (42, 'W42-G-v4', 'k-1', 'return', [4], [2], 'Problem 4', '"pictures on page 4" (K–1 Problems 4 and 5)'),
]

for week in sorted({c[0] for c in CITATIONS}):
    kid = next(c[1] for c in CITATIONS if c[0] == week)
    key = Y / 'band-views' / f'week-{week}' / f'week-{week}-key.pdf'
    check(text(key).count(f'Week {week} / {kid}') == pages(key), f'Week {week} key: footer {kid} on all {pages(key)} pages')
    maps = page_map(week)
    check(len(maps) == 6, f'Week {week} key: a page map row for each band and route ({len(maps)})')
    for (stem, route), m in sorted(maps.items()):
        full = Y / f'week-{week}' / f'week-{week}-{stem}.pdf'
        rp = Y / 'band-views' / f'week-{week}' / f'week-{week}-{stem}-{route}.pdf'
        n = pages(rp)
        ok = sorted(m) == list(range(1, n + 1))
        for r, f in m.items():
            R, F = lines(rp, r), lines(full, f)
            ok = ok and (R == F or (set(R) <= set(F) and len(R) > 2))
        check(ok, f'Week {week} {stem} {route}: {n} route pages, each the full-packet page the key names')
for week, kid, stem, route, cited, want, words, quote in CITATIONS:
    m = page_map(week)[(stem, route)]
    got = [r for f in cited for r, g in m.items() if g == f]
    rp = Y / 'band-views' / f'week-{week}' / f'week-{week}-{stem}-{route}.pdf'
    check(got == want and all(words in text(rp, r) for r in want),
          f'Week {week} {stem} {route}: {quote} (full p. {", ".join(map(str, cited))}) is route p. {", ".join(map(str, got))}')

# K-1 band views for the shared packets of Weeks 54, 55 and 57: the guides route K-1, adult-led,
# through pages headed for older children; each slice must be exactly those packet pages, and
# the menu must name the route.
for week, routed in ((54, [1, 2, 3]), (55, [1, 2, 3]), (57, [4])):
    packet = Y / f'week-{week}' / f'week-{week}-students.pdf'
    sl = Y / 'band-views' / f'week-{week}' / f'week-{week}-k-1.pdf'
    same = sl.exists() and pages(sl) == len(routed) and all(lines(sl, i + 1) == lines(packet, p) for i, p in enumerate(routed))
    check(same, f'Week {week} K–1 slice: packet pages {routed}')
    menu = ' '.join(text(Y / 'band-views' / f'week-{week}' / f'week-{week}-menu.pdf').split())
    check('K–1: pp. ' in menu and 'the guide’s adult-led route' in menu, f'Week {week} menu: K–1 named as the guide\'s adult-led route')


def words(pdf):
    return ' '.join(re.sub(r'(?<=[a-z])- (?=[a-z])', '', ' '.join(text(pdf).split())).split())


# Guide wording: only the named sentence and the footer id may differ from the guide archived
# before these follow-ups. Week 57 p. 1: the K-1 route's page reference. Week 71 p. 2: the
# extension's XYX claim is about X and Y meeting at a corner (ACA, CAC, BDB and DBD bounce
# between parallel walls and occur in every room).
A = 'archive-before-critic-j-fixes-2026-10-23'
GUIDES = [
    (57, 'W57-FAC-v3', 'W57-FAC-v4', 10, 'p. 1: the K–1 route is on guide p. 3 with student p. 4 grids',
     'K–1 has an adult-led route with four or five squares on the existing grids (p. 3), not a Week 57 theorem packet.',
     'K–1 has an adult-led route with four or five squares on extra copies of the student p. 4 grids (guide p. 3), not a Week 57 theorem packet.'),
    (71, 'GGT71-FAC-v2', 'GGT71-FAC-v3', 4, 'p. 2: XYX at a corner needs X and Y to meet there',
     'So XYX happens only at corners under 90◦ : here ABA, BAB, CDC and DCD.',
     'So XYX with X and Y meeting at a corner happens only at corners under 90◦ : here ABA, BAB, CDC and DCD.'),
]
def three_letter_words(seed=71, shots=4000, bounces=12):
    """Sample billiard shots in the guide's side-4 60-degree rhombus (A bottom, B left, C top,
    D right) and return the three-letter words seen; shots passing within 1e-9 of a corner stop."""
    import math, random
    r3 = math.sqrt(3)
    V = [(0, 0), (4, 0), (6, 2 * r3), (2, 2 * r3)]
    walls = {'A': (V[0], V[1]), 'D': (V[1], V[2]), 'C': (V[2], V[3]), 'B': (V[3], V[0])}
    rnd, seen = random.Random(seed), set()
    for _ in range(shots):
        while True:
            x, y = rnd.uniform(0, 6), rnd.uniform(0, 2 * r3)
            if y > 1e-6 and y < 2 * r3 - 1e-6 and x > y / r3 + 1e-6 and x < 4 + y / r3 - 1e-6:
                break
        a = rnd.uniform(0, 2 * math.pi)
        dx, dy, last, word = math.cos(a), math.sin(a), None, ''
        for _ in range(bounces):
            best = None
            for name, ((x1, y1), (x2, y2)) in walls.items():
                if name == last:
                    continue
                ex, ey = x2 - x1, y2 - y1
                den = dx * ey - dy * ex
                if abs(den) < 1e-12:
                    continue
                s = ((x1 - x) * ey - (y1 - y) * ex) / den
                u = ((x1 - x) * dy - (y1 - y) * dx) / den
                if s > 1e-12 and -1e-9 <= u <= 1 + 1e-9 and (best is None or s < best[0]):
                    best = (s, name, u, ex, ey)
            s, name, u, ex, ey = best
            if min(u, 1 - u) < 1e-9:
                break
            x, y = x + s * dx, y + s * dy
            L = math.hypot(ex, ey); tx, ty = ex / L, ey / L
            d = dx * tx + dy * ty
            dx, dy = 2 * d * tx - dx, 2 * d * ty - dy
            word, last = word + name, name
        seen |= {word[i:i + 3] for i in range(len(word) - 2)}
    return seen


W = three_letter_words()
check(all(w in W for w in ('ACA', 'CAC', 'BDB', 'DBD', 'ABA', 'BAB', 'CDC', 'DCD'))
      and not any(w in W for w in ('ADA', 'DAD', 'BCB', 'CBC')),
      'Week 71 rhombus sample: parallel-wall XYX and 60-degree-corner XYX occur, 120-degree-corner XYX never')

for week, old_id, new_id, n, what, old_s, new_s in GUIDES:
    g, old = Y / f'week-{week}' / f'week-{week}-facilitator.pdf', Y / f'week-{week}' / A / f'week-{week}-facilitator.pdf'
    check(new_s in words(g) and old_s not in words(g) and old_s in words(old), f'Week {week} guide {what}')
    check(text(g).count(new_id) == pages(g) == n, f'Week {week} guide: footer {new_id} on all {n} pages')
    check(words(g).replace(new_s, old_s).replace(new_id, old_id) == words(old), f'Week {week} guide: nothing else changed since {old_id}')
print('PASS' if not FAIL else f'{len(FAIL)} FAILED')
raise SystemExit(1 if FAIL else 0)
