"""Checks for the grades 2-3 pages. Run: python3 check_23.py"""
import sys, itertools
from collections import Counter
import tri
import instances as I

B = I.boards()
ok = True


def claim(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg)
    ok = ok and cond


def info(R):
    up, dn = tri.counts(R)
    m, _ = tri.max_matching(R)
    return up, dn, m, len(R) - 2 * m


print('=== Grades 2-3 Problem 1: cover with blue rhombi only ===')
for k, want in [('23-P1a', True), ('23-P1b', False), ('23-P1c', False), ('23-P1d', True)]:
    R = B[k]
    up, dn, m, g = info(R)
    n = tri.count_tilings(R, ['B'])
    claim((n > 0) == want, '%s: %d triangles (%d up, %d down), area %s; blue coverings = %d; at best %d triangles stay uncovered'
          % (k, len(R), up, dn, 'even' if len(R) % 2 == 0 else 'odd', n, g))

print('\n=== Fewest greens with blue rhombi on the big triangles (Problems 2 and 4), sides 1..7 ===')
for n in range(1, 8):
    R = I.TRI[n]
    up, dn, m, g = info(R)
    # every row has exactly one more up than down
    rows_ok = all(sum(1 for t in R if t[1] == j and t[2] == 0) - sum(1 for t in R if t[1] == j and t[2] == 1) == 1 for j in range(n))
    claim(g == n and up - dn == n and rows_ok,
          'triangle side %d: %d triangles, %d up, %d down (each of the %d rows has one more up than down); most blues = %d; fewest greens = %d'
          % (n, len(R), up, dn, n, m, g))

# in a best packing every green is an up-triangle (greens = up - down forces this)
for n in (3, 4, 5, 7):
    R = I.TRI[n]
    m, match = tri.max_matching(R)
    covered = set()
    for a, b in match:
        covered |= {a, b}
    left = R - covered
    claim(all(t[2] == 0 for t in left), 'triangle side %d: in a best packing found by the matching, all %d uncovered triangles point up' % (n, len(left)))

# an explicit best packing for side 3: the 3 corner triangles uncovered
R = I.TRI[3]
corners3 = {(0, 0, 0), (2, 0, 0), (0, 2, 0)}
claim(tri.count_tilings(R - corners3, ['B']) > 0, 'triangle side 3: leaving the three corner triangles as greens works (the rest is a small hexagon = 3 blues)')

print('\n=== Grades 2-3 Problem 3: big hexagon with two small triangles cut out ===')
for k in 'abcd':
    R = B['23-P3' + k]
    holes = I.MUT[k]
    up, dn, m, g = info(R)
    n = tri.count_tilings(R, ['B'])
    kinds = sorted('up' if t[2] == 0 else 'down' for t in holes)
    claim((n > 0) == (up == dn), '23-P3%s: holes are %s; leaves %d up, %d down; blue coverings = %d -> %s'
          % (k, ' + '.join(kinds), up, dn, n, 'POSSIBLE' if n else 'IMPOSSIBLE (%d greens needed at best)' % g))
# Gomory-style fact for this hexagon: removing ANY one up and ANY one down always leaves a coverable board
H = I.H222
res = Counter()
for a, b in itertools.combinations(sorted(H), 2):
    R = H - {a, b}
    m, _ = tri.max_matching(R)
    res[(a[2] != b[2], 2 * m == len(R))] += 1
claim(res[(True, False)] == 0 and res[(False, True)] == 0,
      'big hexagon: of all %d ways to cut out two triangles, all %d one-up-one-down cuts can be covered and none of the %d same-direction cuts can'
      % (sum(res.values()), res[(True, True)], res[(False, False)]))

print('\n=== Grades 2-3 Problem 5: purple chevrons (and greens) on the big triangles ===')
for n in range(2, 8):
    R = I.TRI[n]
    gP, exP = tri.min_greens(R, ['P'])
    gPB, _ = tri.min_greens(R, ['P', 'B'])
    up, dn, m, gB = info(R)
    # the argument: greens >= n (up-down) and greens = area - 4*(chevrons), so greens has the same remainder as the area when divided by 4
    predicted = min(x for x in range(n, len(R) + 1) if (len(R) - x) % 4 == 0)
    claim(gP == predicted and gPB == gB, 'triangle side %d: chevrons + greens need %d greens (blues alone need %d; blues and chevrons together need %d); predicted by "at least %d and area minus greens divisible by 4": %d'
          % (n, gP, gB, gPB, n, predicted))
for n, want in [(3, 5), (4, 4), (6, 8)]:
    gP, _ = tri.min_greens(I.TRI[n], ['P'])
    claim(gP == want, 'board 23-P5%s (side %d): fewest greens with purples = %d' % ({3: 'a', 4: 'b', 6: 'c'}[n], n, gP))
claim(tri.count_tilings(I.H222, ['P']) == 2, 'big hexagon can be covered by 6 purple chevrons in exactly 2 ways (adult extension)')
# a chevron always splits into two blues (exactly one way)
claim(tri.count_tilings(set(tri.PURPLE), ['B']) == 1, 'a purple chevron is covered by two blue rhombi in exactly one way')

print('\n=== Grades 2-3 Problem 6: the two "hourglass" boards ===')
for k, neck, want_g in [('23-P6a', 2, 2), ('23-P6b', 1, 4)]:
    R = B[k]
    up, dn, m, g = info(R)
    lower = I.TRI[3]
    upper = R - lower
    contact = sum(1 for t in lower for s in tri.neighbors(t) if s in upper)
    lu, ld = tri.counts(lower)
    uu, ud = tri.counts(upper)
    claim(up == dn and g == want_g and contact == neck,
          '%s: %d up, %d down (equal!) but blues leave at least %d greens; the two halves touch along %d small edge(s); lower half %d up/%d down, upper half %d up/%d down'
          % (k, up, dn, g, contact, lu, ld, uu, ud))

print('\n=== Grades 2-3 Problem 7: smallest one-piece board needing at least 3 greens ===')


def grow(polys):
    out = set()
    for P in polys:
        for t in P:
            for nb in tri.neighbors(t):
                if nb not in P:
                    out.add(tri.normalize(set(P) | {nb}))
    return out


polys = {tri.normalize([(0, 0, 0)]), tri.normalize([(0, 0, 1)])}
first = None
for size in range(1, 9):
    hits = [P for P in polys if len(P) - 2 * tri.max_matching(set(P))[0] >= 3]
    if hits and first is None:
        first = size
        free = {min(tri.orientations(P)) for P in hits}
        target = min(tri.orientations(I.SMALLEST_3GAP))
        claim(size == 7 and len(free) == 1 and target in free,
              'smallest one-piece board needing >= 3 greens has %d triangles; there is exactly %d such shape up to turning/flipping: the side-3 triangle with one corner blue removed (5 up, 2 down)' % (size, len(free)))
    polys = grow(polys)
claim(tri.counts(I.SMALLEST_3GAP) == (5, 2), 'that shape has 5 up and 2 down triangles')

print('\nALL GRADES 2-3 CHECKS PASSED' if ok else '\nSOME GRADES 2-3 CHECKS FAILED')
sys.exit(0 if ok else 1)
