"""Brute-force checks of the general statements in the adult guide (sections 1, 4 and 5).

Everything is simulated (hops, chord sets, segment crossings), never derived from gcd, and then
compared with the formula the guide states."""
import math
import os
import sys
from fractions import Fraction
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import cycles, chord_set, A

BAD = []


def check(name, ok):
    print(('ok  ' if ok else 'BAD ') + name)
    if not ok:
        BAD.append(name)


NMAX = 60
# pieces = gcd, every piece n/g dots, piece through 0 = multiples of g, pieces are turns of the first
ok1 = ok2 = ok3 = ok4 = True
for n in range(2, NMAX + 1):
    for k in range(1, n):
        cs = cycles(n, k)
        g = gcd(n, k)
        ok1 &= len(cs) == g
        ok2 &= all(len(c) == n // g for c in cs)
        ok3 &= set(cs[0]) == set(range(0, n, g))
        ok4 &= all(set(c) == {(x + c[0]) % n for x in cs[0]} for c in cs)
check(f'pieces = gcd(n,k) for 2<=n<={NMAX}, 1<=k<n', ok1)
check('every piece has n/g dots', ok2)
check('the piece through 0 is the multiples of g', ok3)
check('every piece is the first turned 0..g-1 dots', ok4)

# hop k and hop n-k draw the same lines; no other hop draws the same lines
ok = all(chord_set(n, k) == chord_set(n, n - k) for n in range(3, NMAX + 1) for k in range(1, n))
check('hop k and hop n-k draw the same lines', ok)
ok = all({h for h in range(1, n) if chord_set(n, h) == chord_set(n, k)} == {k, n - k}
         for n in range(3, NMAX + 1) for k in range(1, n))
check('only hops k and n-k draw a given picture', ok)

# one piece for every hop iff n prime; phi(n) one-piece hops, phi(n)/2 pictures
def prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


ok = all((all(len(cycles(n, k)) == 1 for k in range(1, n)) == prime(n)) for n in range(2, NMAX + 1))
check('every hop one piece <=> n prime', ok)
ok = True
for n in range(3, NMAX + 1):
    one = [k for k in range(1, n) if len(cycles(n, k)) == 1]
    pics = {chord_set(n, k) for k in one}
    phi = sum(1 for k in range(1, n + 1) if gcd(n, k) == 1)
    ok &= len(one) == phi and len(pics) == phi // 2
check('phi(n) hops give one piece, phi(n)/2 pictures (n>=3)', ok)
print('    12 dots one-piece hops:', [k for k in range(1, 12) if len(cycles(12, k)) == 1],
      'pictures:', len({chord_set(12, k) for k in (1, 5, 7, 11)}))

# star polygon {m/j}: a polygon (no crossings inside a piece) iff j = +-1 mod m, a segment when m = 2
def P(n, i):
    a = math.pi / 2 - 2 * math.pi * i / n
    return (math.cos(a), math.sin(a))


def cross(p, q, r, s):
    """Proper crossing of segments pq and rs (not at shared endpoints)."""
    def o(a, b, c):
        v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        return 0 if abs(v) < 1e-12 else (1 if v > 0 else -1)
    if min(math.dist(p, r), math.dist(p, s), math.dist(q, r), math.dist(q, s)) < 1e-9:
        return False
    return o(p, q, r) * o(p, q, s) < 0 and o(r, s, p) * o(r, s, q) < 0


ok = True
for n in range(3, 31):
    for k in range(1, n):
        g = gcd(n, k)
        m, j = n // g, (k // g) % (n // g)
        piece = cycles(n, k)[0]
        segs = [(P(n, a), P(n, (a + k) % n)) for a in piece]
        selfcross = any(cross(*segs[x], *segs[y]) for x in range(len(segs)) for y in range(x + 1, len(segs)))
        polygon = (j % m in (1, m - 1))
        if m == 2:
            ok &= len(set(frozenset(s) for s in segs)) == 1
        else:
            ok &= (not selfcross) == polygon
check('a piece is a plain polygon exactly when j = +-1 (mod m); a single segment when m = 2 (n<=30)', ok)

# guide (4-5 intro): the pieces of a drawing cross each other, so counting connected parts gives 1 every time
ok = True
worst = None
for n in range(3, 31):
    for k in range(1, n):
        cs = cycles(n, k)
        if len(cs) < 2:
            continue
        segs = [[(P(n, a), P(n, (a + k) % n)) for a in c] for c in cs]
        # union-find over pieces: two pieces touch if a segment of one crosses a segment of the other
        parent = list(range(len(cs)))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for x in range(len(cs)):
            for y in range(x + 1, len(cs)):
                if any(cross(*s, *t) or (math.dist(s[0], s[1]) > 1.99 and math.dist(t[0], t[1]) > 1.99)
                       for s in segs[x] for t in segs[y]):
                    parent[find(x)] = find(y)
        comps = len({find(x) for x in range(len(cs))})
        if comps != 1:
            ok = False
            worst = (n, k, comps)
check(f'every drawing with 2+ pieces is one connected figure (n<=30){"" if ok else " counterexample " + str(worst)}', ok)

# the wheel: composition, undo, full cycles, affine codes
ok = all(all(A[(A.index(c) + s + t) % 26] == A[(A.index(A[(A.index(c) + s) % 26]) + t) % 26] for c in A)
         for s in range(26) for t in range(26))
check('two settings make one (add, mod 26)', ok)
ok = all({x for x in [(s * j) % 26 for j in range(26)]} == set(range(0, 26, gcd(26, s) or 26))
         and len({(s * j) % 26 for j in range(26)}) == 26 // gcd(26, s) for s in range(26))
check('repeating setting s from A visits 26/gcd(26,s) letters', ok)
ok = all((len({(a * x + b) % 26 for x in range(26)}) == 26) == (gcd(a, 26) == 1) for a in range(26) for b in range(26))
check('affine code x -> ax+b can be undone exactly when gcd(a,26) = 1', ok)

# fallback game (guide p.3): pass by 2 among 5 people reaches everyone; among 4 people two never get it
print('    pass by 2 among 5 reaches', len(cycles(5, 2)[0]), 'people; among 4 reaches', len(cycles(4, 2)[0]),
      '; passes reaching all 4:', [k for k in range(1, 4) if len(cycles(4, k)[0]) == 4])

# K-1: counters for the big rings (0.8 in dots, ring radius 2.05 in)
for n in (4, 5, 6, 7):
    chord = 2 * 2.05 * math.sin(math.pi / n)
    print(f'    K-1 big ring of {n}: dot centres {chord:.3f} in apart; a 1-inch counter on one dot clears the '
          f'next dot by {chord - 0.5 - 0.4:.3f} in')
print('SUMMARY:', 'all checks agree' if not BAD else BAD)
