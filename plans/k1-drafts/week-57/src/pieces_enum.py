"""Enumerate shapes made of up to 6 pieces (unit squares or halves, at most one piece
per cell, i.e. the fewest-pieces tiling of the region) and check the closing-in facts
used on the K-1 pages: three pieces never close in a dot; four pieces close in a dot in
exactly six ways; two dots need at least six pieces; which two-dot shapes use six.
"""
import sys
sys.path.insert(0, '.')
from shapes import (dot_status, has_hole, canon, normalize, half_quarters, ACROSS, bbox)

STATES = ['F', 'SW', 'SE', 'NE', 'NW']


def quarters_of(cell, st):
    x, y = cell
    if st == 'F':
        return [(x, y, d) for d in 'SENW']
    return half_quarters(x, y, st)


def region(shape):
    q = []
    for c, st in shape:
        q += quarters_of(c, st)
    return frozenset(q)


def touches(qset, newq):
    S = qset
    for (x, y, d) in newq:
        dx, dy, e = ACROSS[d]
        if (x+dx, y+dy, e) in S:
            return True
    return False


def grow(maxp):
    start = [frozenset({((0, 0), st)}) for st in STATES]
    seen = {}
    level = {}
    for s in start:
        level[canon(region(s))] = s
    allv = {1: dict(level)}
    for p in range(2, maxp+1):
        nxt = {}
        for key, s in allv[p-1].items():
            used = {c for c, _ in s}
            R = region(s)
            xs = [c[0] for c in used]; ys = [c[1] for c in used]
            for x in range(min(xs)-1, max(xs)+2):
                for y in range(min(ys)-1, max(ys)+2):
                    if (x, y) in used:
                        continue
                    for st in STATES:
                        nq = quarters_of((x, y), st)
                        if touches(R, nq):
                            ns = frozenset(set(s) | {((x, y), st)})
                            k = canon(region(ns))
                            if k not in nxt:
                                nxt[k] = ns
        allv[p] = nxt
    return allv


def ok(R):
    B, I, pinch, _, _ = dot_status(R)
    return not pinch and not has_hole(R)


allv = grow(6)
for p in range(1, 7):
    shapes = [s for s in allv[p].values() if ok(region(s))]
    withdot = [s for s in shapes if dot_status(region(s))[1] >= 1]
    two = [s for s in shapes if dot_status(region(s))[1] >= 2]
    print(p, 'pieces: regions', len(shapes), ' with a dot inside', len(withdot), ' with two inside', len(two))
    if p == 4:
        for s in withdot:
            R = region(s)
            B, I, *_ = dot_status(R)
            print('   four-piece closer: halves', len(R)//2, 'outline', B, 'inside', I,
                  'squares', sum(1 for _, st in s if st == 'F'))
    if p == 6:
        for s in two:
            R = region(s)
            B, I, _, ins, outl = dot_status(R)
            print('   six-piece two-dot shape: halves', len(R)//2, 'outline', B, 'inside', I, ins,
                  'squares', sum(1 for _, st in s if st == 'F'), 'bbox', bbox(R))
