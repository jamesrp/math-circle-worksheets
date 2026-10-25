import sys
sys.path.insert(0, '.')
from shapes import *


def allowed(s):
    B, I, pinch, _, _ = dot_status(s)
    return not pinch and not has_hole(s)


def fits(s, w, h):
    a, b = bbox(s)
    return (a <= w and b <= h) or (a <= h and b <= w)


def art(s):
    """ASCII art of a shape: each cell drawn 2x2 chars."""
    c = cells(s)
    xs = [k[0] for k in c]; ys = [k[1] for k in c]
    rows = []
    for y in range(max(ys), min(ys)-1, -1):
        top = ''; bot = ''
        for x in range(min(xs), max(xs)+1):
            v = c.get((x, y), set())
            if len(v) == 4:
                top += '##'; bot += '##'
            elif v == {'S', 'W'}:
                top += '| '; bot += '#\\'
                top = top[:-2] + '\\ '; bot = bot[:-2] + '##'
            elif v == {'S', 'E'}:
                top += ' /'; bot += '##'
            elif v == {'N', 'E'}:
                top += '##'; bot += ' /'
                top = top[:-2] + '\\#'; bot = bot[:-2] + ' \\'
            elif v == {'N', 'W'}:
                top += '##'; bot += '/ '
            else:
                top += '..'; bot += '..'
        rows += [top, bot]
    return '\n'.join(rows)


gens = enumerate_shapes(8)
A = {n: [s for s in gens[n] if allowed(s)] for n in gens}

print('== three halves')
fixed3 = {canon(s, flips=False) for s in A[3]}
fixed3 = set()
for s in A[3]:
    for t in SYMS:
        fixed3.add(canon(transform(s, t), flips=False))
print('free', len(A[3]), 'turns only', len(fixed3))
for s in A[3]:
    print(bbox(s), dot_status(s)[:2], sorted(s))

print('== four halves')
for s in sorted(A[4], key=lambda s: bbox(s)):
    B, I, *_ = dot_status(s)
    print(bbox(s), (B, I), pieces(s))
fixed4 = set()
for s in A[4]:
    for t in SYMS:
        fixed4.add(canon(transform(s, t), flips=False))
print('four halves turns-only count', len(fixed4))
print('four halves fitting 4x3:', sum(fits(s, 4, 3) for s in A[4]), 'of', len(A[4]))
print('four halves fitting 3x3:', sum(fits(s, 3, 3) for s in A[4]))
print('four halves fitting 3x2:', sum(fits(s, 3, 2) for s in A[4]))
print('three halves fitting 3x2:', sum(fits(s, 3, 2) for s in A[3]), ' 2x2:', sum(fits(s, 2, 2) for s in A[3]))

print('== fit of all shapes up to n halves')
for n in range(1, 9):
    for (w, h) in [(4, 3), (4, 4), (5, 4), (5, 5), (6, 6)]:
        print(n, (w, h), sum(fits(s, w, h) for s in A[n]), '/', len(A[n]))

print('== shapes with a dot inside, by number of pieces')
best = {}
for n in range(1, 9):
    for s in A[n]:
        B, I, *_ = dot_status(s)
        f, h = pieces(s)
        p = f + h
        if I >= 1:
            best.setdefault(('I>=1', p), []).append((n, B, I))
        if I >= 2:
            best.setdefault(('I>=2', p), []).append((n, B, I))
for k in sorted(best):
    print(k, len(best[k]), sorted(set(best[k]))[:10])

print('== four-piece shapes with a dot inside')
four = []
for n in range(1, 9):
    for s in A[n]:
        B, I, *_ = dot_status(s)
        f, h = pieces(s)
        if I >= 1 and f + h == 4:
            four.append(s)
            print('halves', n, 'B', B, 'I', I, 'squares', f, 'halves-pieces', h, 'bbox', bbox(s))
print(len(four))

print('== fewest pieces for a shape with I>=1 among shapes whose min pieces is 3:')
print(any(dot_status(s)[1] >= 1 for n in range(1, 7) for s in A[n] if sum(pieces(s)) <= 3))

print('== eight halves with B=6')
for s in A[8]:
    B, I, _, ins, outl = dot_status(s)
    if B <= 6:
        print(B, I, 'pieces', pieces(s), 'bbox', bbox(s), 'inside', ins, 'outline', outl)
        print(art(s))

print('== min outline for given paper (halves even), whole squares only vs any')
for n in range(2, 9, 2):
    allB = min(dot_status(s)[0] for s in A[n])
    sq = [s for s in A[n] if pieces(s)[1] == 0]
    sqB = min(dot_status(s)[0] for s in sq) if sq else None
    print(n, 'halves: min B any', allB, ' whole squares only', sqB)

print('== two inside dots: min pieces, adjacency of the inside dots')
res = {}
for n in range(1, 9):
    for s in A[n]:
        B, I, _, ins, _ = dot_status(s)
        if I >= 2:
            p = sum(pieces(s))
            for a, b in itertools.combinations(ins, 2):
                dx, dy = abs(a[0]-b[0]), abs(a[1]-b[1])
                key = tuple(sorted((dx, dy)))
                res.setdefault(key, []).append((p, n))
for k, v in sorted(res.items()):
    print('inside pair offset', k, 'min pieces', min(x[0] for x in v), 'min halves', min(x[1] for x in v))
