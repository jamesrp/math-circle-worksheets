"""Week 12 K-1: read every circle, dot, label and printed chord from the PDF and
solve each problem from the extracted data.  Run: python3 check_k1.py > check_k1.out"""
import sys
import os
import math
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfgeo as G

FAIL = []
CLOSER = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + ((': ' + str(detail)) if detail != '' else ''))
    if not ok:
        FAIL.append(name)


def nc_matchings(N, fixed=()):
    def rec(pts):
        if not pts:
            yield ()
            return
        a = pts[0]
        for i in range(1, len(pts)):
            for m in rec(pts[1:i] + pts[i + 1:]):
                yield ((a, pts[i]),) + m
    fixed_pts = {p for e in fixed for p in e}
    rest = [p for p in range(1, N + 1) if p not in fixed_pts]
    out = []
    if len(rest) % 2:
        return out
    for m in rec(rest):
        full = tuple(sorted(tuple(sorted(e)) for e in m + tuple(fixed)))
        if not any(a < c < b < d or c < a < d < b for (a, b), (c, d) in itertools.combinations(full, 2)):
            out.append(full)
    return out


def label_candidates(w, big, dots):
    """(radial excess, circle index, dot index) for every circle/dot whose outward ray passes through the label."""
    out = []
    for ci, c in enumerate(big):
        rd = math.dist((w['cx'], w['cy']), (c['cx'], c['cy']))
        if not (c['r'] < rd < c['r'] + 45):
            continue
        wa = G.clockwise_angle(c['cx'], c['cy'], w['cx'], w['cy'])
        for di, d in enumerate(dots):
            if abs(math.dist((d['cx'], d['cy']), (c['cx'], c['cy'])) - c['r']) > 0.8:
                continue
            da = G.clockwise_angle(c['cx'], c['cy'], d['cx'], d['cy'])
            if abs(((wa - da + 180) % 360) - 180) < 6:
                out.append((rd - c['r'], ci, di))
    return sorted(out)


def assign_labels(big, dots, nums):
    """Greedy by radial excess: each dot slot takes one label; a label displaced from its nearest
    circle goes to its next candidate.  Returns owner list and near-tie notes."""
    cands = [label_candidates(w, big, dots) for w in nums]
    owner = [None] * len(nums)
    taken = set()
    flat = sorted((ex, li, ci, di) for li, cs in enumerate(cands) for ex, ci, di in cs)
    for ex, li, ci, di in flat:
        if owner[li] is None and (ci, di) not in taken:
            owner[li] = ci
            taken.add((ci, di))
    notes = []
    for li, cs in enumerate(cands):
        if owner[li] is None or len(cs) < 2:
            continue
        own = min(ex for ex, ci, di in cs if ci == owner[li])
        other = min(ex for ex, ci, di in cs if ci != owner[li])
        if other < own * 1.5:
            notes.append(f'label "{nums[li]["text"]}" at ({nums[li]["cx"]:.0f},{nums[li]["cy"]:.0f}) is {own / G.MM:.1f} mm outside its own '
                         f'circle (r={big[owner[li]]["r"] / G.MM:.1f} mm) and {other / G.MM:.1f} mm outside another circle\'s dot')
    return owner, notes


def read_circles(page):
    big = [c for c in page.circles if c['stroke'] and not c['fill'] and c['r'] > 20]
    dots = [c for c in page.circles if c['fill'] and c['r'] < 6]
    allnums = [w for w in page.words if w['text'].isdigit() and w['size'] < 10 and w['top'] < 750]
    owner, notes = assign_labels(big, dots, allnums)
    CLOSER.extend(notes)
    unowned = [w['text'] for w, o in zip(allnums, owner) if o is None]
    if unowned:
        print('  labels with no circle:', unowned)
    segs = [s for s in page.segments() if s['scolor'] == (0.0, 0.0, 0.0)]
    used_dots = set()
    out = []
    for ci0, c in sorted(enumerate(big), key=lambda t: (round(t[1]['cy']), t[1]['cx'])):
        nums = [w for w, o in zip(allnums, owner) if o == ci0]
        mine = [k for k, d in enumerate(dots) if abs(math.dist((d['cx'], d['cy']), (c['cx'], c['cy'])) - c['r']) < 0.8]
        used_dots.update(mine)
        n = len(mine)
        ang = sorted((G.clockwise_angle(c['cx'], c['cy'], dots[k]['cx'], dots[k]['cy']), k) for k in mine)
        probs = []
        for idx, (a, k) in enumerate(ang):
            want = idx * 360 / n
            if abs(((a - want + 180) % 360) - 180) > 0.2:
                probs.append(f'dot {idx + 1} at {a:.2f} deg, expected {want:.2f}')
        # labels: each number word assigned to the nearest dot of this circle
        label_of = {}
        for w in nums:
            dmin = min(math.dist((w['cx'], w['cy']), (dots[k]['cx'], dots[k]['cy'])) for k in mine) if mine else 99
            if dmin > 45:
                continue
            k = min(mine, key=lambda k: math.dist((w['cx'], w['cy']), (dots[k]['cx'], dots[k]['cy'])))
            wa = G.clockwise_angle(c['cx'], c['cy'], w['cx'], w['cy'])
            da = G.clockwise_angle(c['cx'], c['cy'], dots[k]['cx'], dots[k]['cy'])
            if abs(((wa - da + 180) % 360) - 180) > 6:
                probs.append(f'label {w["text"]} not radially outside its dot ({wa:.1f} vs {da:.1f})')
            if math.dist((w['cx'], w['cy']), (c['cx'], c['cy'])) <= c['r']:
                probs.append(f'label {w["text"]} inside circle')
            if k in label_of:
                probs.append(f'dot has two labels {label_of[k]} and {w["text"]}')
            label_of[k] = w['text']
        order = [label_of.get(k) for a, k in ang]
        if order != [str(i) for i in range(1, n + 1)]:
            probs.append(f'labels clockwise from top read {order}')
        # chords
        idx_of = {k: i + 1 for i, (a, k) in enumerate(ang)}
        chords = []
        for s in segs:
            ends = []
            for p in (s['a'], s['b']):
                hit = [k for k in mine if math.dist(p, (dots[k]['cx'], dots[k]['cy'])) < 0.8]
                ends.append(hit[0] if hit else None)
            if None not in ends:
                chords.append(tuple(sorted((idx_of[ends[0]], idx_of[ends[1]]))))
        # min gap between neighbouring dots (centre to centre) and label clearance from dot
        gap = 2 * c['r'] * math.sin(math.pi / n) if n else 0
        out.append(dict(cx=c['cx'], cy=c['cy'], r=c['r'], n=n, chords=sorted(chords), problems=probs, gap=gap))
    stray = [k for k in range(len(dots)) if k not in used_dots]
    return out, stray


pages = G.load('week-12-k-1.pdf')
expected = {
    1: [(4, [(1, 2), (3, 4)]), (4, [(1, 4), (2, 3)]), (6, [])] + [(6, [])] * 6,
    2: [(6, [])] * 7,
    3: [(8, [])] + [(8, [e]) for e in [(1, 4), (1, 4), (1, 6), (1, 6), (1, 3), (1, 5)]],
    4: [(8, [])] * 7,
    5: [(10, [])] + [(n, []) for n in [3, 4, 5, 6, 7]],
    6: [(8, [])] * 5,
}
for pno, page in enumerate(pages, 1):
    circles, stray = read_circles(page)
    print(f'--- page {pno}: {len(circles)} circles, stray dots {len(stray)}')
    for c in circles:
        print(f'  circle at ({c["cx"]:.1f},{c["cy"]:.1f}) r={c["r"] / G.MM:.1f} mm, {c["n"]} dots, chords {c["chords"]}, '
              f'neighbour spacing {c["gap"] / G.MM:.1f} mm' + (f', PROBLEMS {c["problems"]}' if c['problems'] else ''))
    check(f'page {pno}: every circle regular, labelled 1..n clockwise from the top', all(not c['problems'] for c in circles) and not stray)
    # match expected structure in reading order (large first, then small row by row)
    big_first = sorted(circles, key=lambda c: (-round(c['r']), round(c['cy'] / 5), c['cx']))
    got = [(c['n'], c['chords']) for c in big_first]
    exp = expected[pno]
    if pno == 1:
        got = [(c['n'], c['chords']) for c in sorted(circles, key=lambda c: (c['n'] != 4, -c['r'], round(c['cy'] / 5), c['cx']))]
    check(f'page {pno}: circles and printed chords as transcribed', sorted(map(str, got)) == sorted(map(str, exp)), got)

print()
print('Labels almost as close to another circle as to their own (layout note, not a mathematical error):')
for x in CLOSER:
    print('  ' + x)
print()
print('== Solve the problems from the extracted circles')
c1, _ = read_circles(pages[0])
four = [c for c in c1 if c['n'] == 4]
check('page 1 example: both printed four-dot drawings are legal noncrossing pairings and different',
      all(tuple(c['chords']) in nc_matchings(4) for c in four) and four[0]['chords'] != four[1]['chords'],
      [c['chords'] for c in four])
check('page 1 example: the two printed pairings are all of them', sorted(tuple(c['chords']) for c in four) == sorted(nc_matchings(4)))
p1 = len(nc_matchings(6))
check(f'P1/P2: six-dot pairings = {p1}; page 1 has 1 large + 6 small, page 2 has 1 large + 6 small', p1 == 5)
c3, _ = read_circles(pages[2])
for c in sorted([c for c in c3 if c['chords']], key=lambda c: (round(c['cy']), c['cx'])):
    comps = nc_matchings(8, c['chords'])
    print(f'  P3 printed chord {c["chords"][0]}: {len(comps)} completion(s) {["|".join(f"{a}{b}" for a, b in m) for m in comps]}')
dup = {}
for c in c3:
    if c['chords']:
        dup[c['chords'][0]] = dup.get(c['chords'][0], 0) + 1
comps = {e: len(nc_matchings(8, [e])) for e in dup}
check('P3: each printed chord appears as often as it has completions, or once when it has none',
      all(dup[e] == max(1, comps[e]) for e in dup), (dup, comps))
check('P4: 14 eight-dot pairings, 7 circles printed (large mat + 6 records) plus blank paper', len(nc_matchings(8)) == 14)
c5, _ = read_circles(pages[4])
for c in sorted(c5, key=lambda c: c['n']):
    print(f'  P5 circle with {c["n"]} dots: {len(nc_matchings(c["n"]))} noncrossing pairings')
check('P5: printed dot counts are 10,3,4,5,6,7', sorted(c['n'] for c in c5) == [3, 4, 5, 6, 7, 10])
c6, _ = read_circles(pages[5])
ok = all(any(b - a == 1 or (a, b) == (1, 8) for a, b in m) for m in nc_matchings(8))
check('P6: every eight-dot noncrossing pairing joins circular neighbours (answer: no)', ok)
print()
print('FAILED:', FAIL if FAIL else 'none')
