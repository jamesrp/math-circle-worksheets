#!/usr/bin/env python3
"""Independent exact checks for the Week 64 facilitator guide (standard library)."""
from fractions import Fraction as F
from math import sqrt

class Q2:
    """Elements c + d sqrt(2), with exact rational coefficients."""
    def __init__(self, c=0, d=0):
        self.c, self.d = F(c), F(d)
    @staticmethod
    def cast(x):
        return x if isinstance(x, Q2) else Q2(x)
    def __add__(self, other):
        o = self.cast(other)
        return Q2(self.c + o.c, self.d + o.d)
    __radd__ = __add__
    def __neg__(self):
        return Q2(-self.c, -self.d)
    def __sub__(self, other):
        return self + (-self.cast(other))
    def __rsub__(self, other):
        return self.cast(other) - self
    def __mul__(self, other):
        o = self.cast(other)
        return Q2(self.c * o.c + 2 * self.d * o.d,
                  self.c * o.d + self.d * o.c)
    __rmul__ = __mul__
    def __truediv__(self, other):
        o = self.cast(other)
        den = o.c * o.c - 2 * o.d * o.d
        return self * Q2(o.c / den, -o.d / den)
    def __eq__(self, other):
        o = self.cast(other)
        return (self.c, self.d) == (o.c, o.d)
    def __float__(self):
        return float(self.c) + float(self.d) * sqrt(2)
    def __repr__(self):
        return f"({self.c})+({self.d})sqrt(2)"

a, b = Q2(1, 1), Q2(2, 1)
V = [(1,a),(a,1),(a,-1),(1,-a),(-1,-a),(-a,-1),(-a,1),(-1,a)]
V = [(Q2.cast(x), Q2.cast(y)) for x,y in V]
oct_pairs = set()
for i in range(8):
    j = (i + 1) % 8
    dx, dy = V[j][0] - V[i][0], V[j][1] - V[i][1]
    assert dx*dx + dy*dy == 4
    n, m = (i + 5) % 8, (i + 4) % 8
    shift = (V[n][0]-V[i][0], V[n][1]-V[i][1])
    assert (V[j][0]+shift[0], V[j][1]+shift[1]) == V[m]
    oct_pairs.update((frozenset((i,n)), frozenset((j,m))))
chain = [0,5,2,7,4,1,6,3,0]
assert set(chain) == set(range(8))
assert all(frozenset((s,t)) in oct_pairs for s,t in zip(chain,chain[1:]))
assert 8 * 135 == 1080 and 1 - 4 + 1 == -2
assert b/a == Q2(0,1)
for y in [Q2(F(8,5)), Q2(F(29,20)), b/2]:
    assert 2*(b-y) + 2*y == 2*b
    p = (b-y, y)
    q = (p[0]-b, p[1]-b)
    assert q == (-y,y-b)
    assert (y-b, y) == (y-b,(y-b)+b)
assert 2*(b-b/2) == b and 2*(b/2) == b
seam_start = (-b/2, b/2)
copy2_exit_local = (b/2, -b/2)
assert (copy2_exit_local[0]-b, copy2_exit_local[1]+b) == seam_start
assert 3*b/2 - (-b/2) == 2*b
print("PASS: exact octagon sides, endpoint translations, corner class, loop formulas.")

r = dict(A="B", B="A", C="C")
u = dict(A="C", B="B", C="A")
def orbit(start, position, velocity):
    """Event-driven exact flow; sample integer-time local returns."""
    square = start
    x, y = map(F, position)
    initial = x, y
    p, q = map(F, velocity)
    t, next_block = F(0), F(1)
    events, blocks = [], [square]
    while t < 20:
        tr = (1-x)/p if p else None
        tu = (1-y)/q if q else None
        candidates = [next_block-t] + [z for z in (tr,tu) if z is not None]
        dt = min(candidates)
        x += dt*p
        y += dt*q
        t += dt
        if x == 1 and y == 1:
            return "corner", t, square, events, blocks
        if x == 1:
            square = r[square]
            x = F(0)
            events.append((t,"right",square))
        if y == 1:
            square = u[square]
            y = F(0)
            events.append((t,"up",square))
        if t == next_block:
            assert (x,y) == initial
            blocks.append(square)
            if square == start:
                return "return", t, square, events, blocks
            next_block += 1
    raise AssertionError("Unexpectedly long orbit")

for start in "ABC":
    for velocity, expected in [((1,0), 1 if start=="C" else 2),
                               ((0,1), 1 if start=="B" else 2)]:
        result = orbit(start,(F(1,2),F(1,4)),velocity)
        assert result[:2] == ("return", F(expected))
    result = orbit(start,(F(1,2),F(1,4)),(1,1))
    assert result[:2] == ("return", F(3))
    result = orbit(start,(F(1,4),F(1,2)),(2,1))
    assert result[:2] == ("return", F(1 if start=="A" else 2))

for direction, expected in [((1,2),("return",F(1))),
                             ((2,3),("corner",F(1,4))),
                             ((3,1),("return",F(3))),
                             ((3,2),("return",F(2)))]:
    result = orbit("A",(F(1,2),F(1,4)),direction)
    assert result[:2] == expected
    print(f"P9 {direction}: {result}")
print("PASS: all P6-P9 trajectories, corner stops, and first returns.")

lnk = set()
for s in "ABC":
    for left,right in [("BL","BR"),("TL","TR")]:
        lnk.add(frozenset(((s,right),(r[s],left))))
    for bottom,top in [("BL","TL"),("BR","TR")]:
        lnk.add(frozenset(((s,top),(u[s],bottom))))
cchain = [("A","BL"),("B","BR"),("B","TR"),("A","TL"),
          ("C","BL"),("C","BR"),("A","TR"),("B","TL"),
          ("B","BL"),("A","BR"),("C","TR"),("C","TL"),("A","BL")]
assert len(set(cchain)) == 12
assert all(frozenset((s,t)) in lnk for s,t in zip(cchain,cchain[1:]))
assert 12 * 90 == 1080 and 1 - 6 + 3 == -2
print("PASS: L has one 12-sector corner class, angle 1080 degrees and genus 2.")
