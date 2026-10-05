"""Counterexamples and other readings behind the located problems in math.md."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import cycles, chord_set


def names(cs):
    return sorted(tuple(sorted(c)) for c in cs)


print('== 1. K-1 P5: the six-pointed star and the three lines need the Problem 4 restart')
star = chord_set(6, 2)            # two triangles, as printed
lines3 = chord_set(6, 3)          # three diameters, as printed
for k in range(1, 6):
    one = chord_set(6, k, restart=False)
    print(f'   6 dots, hop {k}, hopping from the black dot until back (Problems 1-3, 6-7): {names(one)}; '
          f'= printed star: {one == star}; = printed three lines: {one == lines3}')
print(f'   with restarts (Problem 4): hop 2 -> {names(chord_set(6, 2))}, hop 3 -> {names(chord_set(6, 3))}')

print('\n== 2. K-1 guide: "Lands on every dot" means every dot gets a marker before the counter is back')
for n, ks in ((4, (1, 2, 3)), (5, (1, 2, 3)), (6, (1, 2, 3)), (7, range(1, 7))):
    res = {}
    for k in ks:
        pos, markers = 0, set()
        while True:
            pos = (pos + k) % n
            if pos == 0:
                break                      # "back": the partner says back, no marker on the black dot
            markers.add(pos)
        literal = len(markers) == n        # every dot, including the black one, has a marker
        other = len(markers) == n - 1      # every dot other than the black one
        res[k] = (literal, other)
    print(f'   {n} dots: hop -> (every dot marked, every other dot marked): {res}')

print('\n== 3. 4-5 P12 / guide: "a dot that lands on itself gets no line"')
for k in (2, 3):
    selfs = [m for m in range(24) if k * m % 24 == m]
    for m in selfs:
        into = [a for a in range(24) if k * a % 24 == m and a != m]
        print(f'   x{k}: dot {m} lands on itself, yet the lines from dots {into} end at dot {m}')

print('\n== 4. Guide P12 and section 5: where the dents (cusps) of the times-table pictures are')
# distance of each drawn chord (24 dots, unit circle, dot 0 at the top, clockwise) from a point
def pt(m):
    a = math.radians(90 - 15 * m)
    return (math.cos(a), math.sin(a))


def dist_line(p, a, b):
    (x, y), (x1, y1), (x2, y2) = p, a, b
    return abs((x2 - x1) * (y1 - y) - (x1 - x) * (y2 - y1)) / math.hypot(x2 - x1, y2 - y1)


for k, cusps, guide in ((2, {'1/3 of the way to dot 12': (0, -1 / 3)}, {'dot 0': pt(0)}),
                        (3, {'1/2 of the way to dot 6': (0.5, 0), '1/2 of the way to dot 18': (-0.5, 0)},
                         {'dot 0': pt(0), 'dot 12': pt(12)})):
    chords = {frozenset((m, k * m % 24)) for m in range(24) if k * m % 24 != m}
    for label, p in list(cusps.items()) + list(guide.items()):
        near = [tuple(sorted(c)) for c in chords if dist_line(p, *[pt(x) for x in c]) < 0.08]
        through = [c for c in near if p not in [pt(x) for x in c]]
        print(f'   x{k}: chords passing within 0.08 R of {label}: {len(near)} '
              f'(not counting chords that merely end there: {len([c for c in near if min(math.dist(p, pt(x)) for x in c) > 0.05])})')
    # the envelope touches the circle where the chord shrinks to a point: m = k m (mod n)
    print(f'   x{k}: envelope touches the dot circle at the self-landing dots {[m for m in range(24) if k * m % 24 == m]}')

print('\n== 5. K-1 P8: rows needed before the top row comes back with hop 2 on 6 pictures:',
      len(cycles(6, 2)[0]), '(5 blank rows printed)')

print('\n== 6. Guide materials: "Coloured pencils, 6+ colours ... a new colour for each start"')
drawn = {'K-1': [(6, 2), (6, 3), (8, 2), (8, 3)],
         '2-3': [(8, k) for k in (1, 2, 3, 4)] + [(10, k) for k in (2, 3, 4, 5)] + [(12, k) for k in range(2, 7)]
         + [(9, 2), (15, 5), (16, 6), (12, 8), (9, 6), (18, 15), (15, 6), (15, 9), (15, 12)],
         '4-5': [(12, k) for k in range(1, 7)] + [(10, 4), (9, 6), (15, 10), (16, 12), (18, 8), (24, 9), (20, 8), (24, 10)]}
for band, cases in drawn.items():
    print(f'   {band}: most starts on any ring a child draws = {max(len(cycles(n, k)) for n, k in cases)}')
