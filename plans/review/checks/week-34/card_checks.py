"""Spot checks for the numbers in the Week 34 review card (plans/review/week-34.md).

Rings are tuples of kinds; the motions are the n turns and n flips of a regular n-ring.
"""
from itertools import product


def motions(n):
    for k in range(n):
        yield ('turn', k), [(i + k) % n for i in range(n)]
    for k in range(n):
        yield ('flip', k), [(k - i) % n for i in range(n)]


def matches(ring):
    n = len(ring)
    return [m for m, perm in motions(n)
            if m != ('turn', 0) and all(ring[perm[i]] == ring[i] for i in range(n))]


def distinguishing(ring):
    return not matches(ring)


# Fix 1: on 3- to 5-rings, two-kind patterns that use both kinds and have no matching turn.
mixed = [r for n in (3, 4, 5) for r in product('AB', repeat=n) if len(set(r)) == 2]
no_turn = [r for r in mixed if not any(m[0] == 'turn' for m in matches(r))]
print('mixed two-kind patterns on 3-5 rings:', len(mixed))
print('  with no matching turn:', len(no_turn))
print('  with a matching turn:', [''.join(r) for r in mixed if r not in no_turn])
print('  distinguishing:', sum(map(distinguishing, mixed)))

# Fix 4: odd-ring witnesses.
for w in ('AABABBB', 'AABABBBBB'):
    print(w, 'distinguishing:', distinguishing(tuple(w)))

# App fit: share of random two-kind patterns that are distinguishing.
for n in (6, 8, 12):
    rings = list(product('AB', repeat=n))
    share = sum(map(distinguishing, rings)) / len(rings)
    print(f'n={n}: {share:.1%} of two-kind patterns are distinguishing')
