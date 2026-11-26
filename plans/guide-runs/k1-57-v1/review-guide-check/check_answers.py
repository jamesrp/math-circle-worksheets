"""Re-derive every answer the K-1 guide prints, against the final pages N57-K-v1."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pieces import *

t0 = time.time()
print('== halves only ==')
H = enumerate_shapes(8, squares=False)
free_counts = []
rule_ok = True
for n in range(1, 9):
    shapes = [s for s in H[n]]
    gapfree = [s for s in shapes if not has_gap(s)]
    free = {}
    for s in gapfree:
        free.setdefault(canon(s), s)
    allfree = {canon(s) for s in shapes}
    onesided = {canon(s, ROTS) for s in gapfree}
    bad = [s for s in gapfree if (lambda h, b, i: b + 2 * i != h + 2)(*counts(s))]
    rule_ok &= not bad
    print(f'{n} halves: fixed {len(shapes)}, free (all) {len(allfree)}, free gap-free {len(free)}, '
          f'turns-only gap-free {len(onesided)}, rule violations {len(bad)}')
    free_counts.append(len(allfree))
print('polyabolo free counts', free_counts, '(published 1,3,4,14,30,107,318,1116)')

def summary(n, w, h):
    gapfree = [s for s in H[n] if not has_gap(s)]
    free = {}
    for s in gapfree:
        free.setdefault(canon(s), s)
    tally = {}
    nofit = 0
    for s in free.values():
        hh, b, i = counts(s)
        tally[(b, i)] = tally.get((b, i), 0) + 1
        if not fits(s, w, h):
            nofit += 1
    return free, tally, nofit

print('\n== P2: three halves, 3x4-dot boards (2x3 spacings) ==')
free3, t3, nf3 = summary(3, 2, 3)
print('free shapes', len(free3), '(outline, inside) tally', t3, 'not fitting', nf3)
print('mirror images distinct:', len({canon(s, ROTS) for s in H[3] if not has_gap(s)}))

print('\n== P3: four halves, 3x4-dot boards ==')
free4, t4, nf4 = summary(4, 2, 3)
print('free shapes', len(free4), 'tally', t4, 'not fitting', nf4)

print('\n== P7: eight halves, fewer than 8 outline dots, 4x5-dot boards (3x4 spacings) ==')
gap8 = [s for s in H[8] if has_gap(s)]
free8, t8, nf8 = summary(8, 3, 4)
print('gap-free free shapes', len(free8), 'tally', dict(sorted(t8.items())))
few = [s for s in free8.values() if counts(s)[1] < 8]
for s in few:
    print('  answer: counts', counts(s), 'bbox', bbox(s), 'fits 3x4:', fits(s, 3, 4),
          'outline', sorted(outline_dots(normalise(s))), 'inside', sorted(inside_dots(normalise(s))))
print('fixed shapes with a gap:', len(gap8), ' min outline among them:',
      min(counts(s)[1] for s in gap8) if gap8 else None)
# Region-level check: same answers if squares may stand for two halves
print('regions of 8 halves with <8 outline (free):', len({region_key(s) for s in few}))
print(f'[{time.time()-t0:.1f}s]')

print('\n== mixed pieces (squares and halves) ==')
M = enumerate_shapes(6, squares=True)
for n in range(1, 7):
    print(n, 'pieces: fixed', len(M[n]))
print(f'[{time.time()-t0:.1f}s]')

# rule check over mixed shapes
viol = 0; tot = 0
for n in range(1, 7):
    for s in M[n]:
        if has_gap(s):
            continue
        tot += 1
        h, b, i = counts(s)
        if b + 2 * i != h + 2:
            viol += 1
print('dot rule over gap-free mixed shapes of 1-6 pieces:', tot, 'shapes,', viol, 'violations')

print('\n== P4: three pieces, any inside dot? ==')
for n in (1, 2, 3):
    k = sum(1 for s in M[n] if inside_dots(s))
    print(n, 'pieces: shapes with an inside dot:', k)

print('\n== P5: four pieces with a dot inside ==')
four = [s for s in M[4] if inside_dots(s) and not has_gap(s)]
byrot = {}; byall = {}
for s in four:
    byrot.setdefault(canon(s, ROTS), s); byall.setdefault(canon(s), s)
print('turns same:', len(byrot), ' turns and flips same:', len(byall))
rows = []
for s in byrot.values():
    nsq = sum(1 for p in s if piece_kind(p)[0] == 'sq')
    h, b, i = counts(s)
    # squares opposite or adjacent?
    d = list(inside_dots(s))[0]
    sqcells = [piece_kind(p)[1:3] for p in s if piece_kind(p)[0] == 'sq']
    rel = ''
    if nsq == 2:
        (a1, b1), (a2, b2) = sqcells
        rel = 'opposite' if (a1 != a2 and b1 != b2) else 'adjacent'
    rows.append((nsq, rel, 4 - nsq, h, b, i, bbox(s)))
for r in sorted(rows):
    print('  squares %d %-8s half pieces %d  halves %d  outline %d  inside %d  bbox %s' % r)
# fixed placements around one fixed dot
fixed_dot = {key(s) for s in four}
print('fixed placements (translations identified):', len(fixed_dot))

print('\n== P6: two side-by-side dots inside, fewest pieces ==')
def two_adjacent(s):
    ins = inside_dots(s)
    return any((x + 1, y) in ins or (x, y + 1) in ins for (x, y) in ins)
for n in range(1, 7):
    any2 = [s for s in M[n] if len(inside_dots(s)) >= 2 and not has_gap(s)]
    adj = [s for s in any2 if two_adjacent(s)]
    print(n, 'pieces: shapes with >=2 inside dots', len(any2), ' with two side-by-side inside dots', len(adj))
six = [s for s in M[6] if two_adjacent(s) and not has_gap(s)]
free6 = {}
for s in six:
    free6.setdefault(canon(s), s)
print('six-piece free shapes:', len(free6))
desc_ok = True
for s in sorted(free6.values(), key=lambda s: counts(s)):
    h, b, i = counts(s)
    ins = sorted(inside_dots(s))
    # check guide description: shared cells hold squares, other four cells square or inward half
    (x1, y1), (x2, y2) = ins
    print('  halves', h, 'outline', b, 'inside', i, 'bbox', bbox(s), 'fits 5x4 spacings:', fits(s, 5, 4))
# description check on fixed shapes: normalise to horizontal pair
cnt = 0
for s in six:
    ins = sorted(inside_dots(s))
    (x1, y1), (x2, y2) = ins
    if y1 != y2:
        continue
    cnt += 1
    shared = {(x1, y1), (x1, y1 - 1)}
    for p in s:
        k, i_, j_, c = piece_kind(p)
        if (i_, j_) in shared and k != 'sq':
            desc_ok = False
print('horizontal fixed six-piece placements:', cnt, '; shared cells always squares:', desc_ok)
print(f'[{time.time()-t0:.1f}s]')
