#!/usr/bin/env python3
"""Check K–1 mats by exact covers of unit triangles; save geometry and witnesses.

Lattice (u,v) maps to (u+v/2, sqrt(3)*v/2) in small-block edge units.
All polygon edges follow lattice lines. Children see only their boundaries.
"""
from collections import Counter
import json
from pathlib import Path


def cells(poly):
    def inside(x, y):
        result = False
        for (a,b),(c,d) in zip(poly, poly[1:]+poly[:1]):
            if (b > y) != (d > y) and x < (c-a)*(y-b)/(d-b)+a:
                result = not result
        return result
    out = set()
    for u in range(min(p[0] for p in poly)-1, max(p[0] for p in poly)+1):
        for v in range(min(p[1] for p in poly)-1, max(p[1] for p in poly)+1):
            for tri in [((u,v),(u+1,v),(u,v+1)),
                        ((u+1,v),(u+1,v+1),(u,v+1))]:
                if inside(sum(p[0] for p in tri)/3, sum(p[1] for p in tri)/3):
                    out.add(tuple(sorted(tri)))
    return frozenset(out)


def rotate(p):
    u,v = p
    return -v,u+v


def cover(poly, piece, limit=2):
    board = cells(poly)
    placements = {}
    rotated = piece
    for _ in range(6):
        for u in range(-8,9):
            for v in range(-8,9):
                p = [(x+u,y+v) for x,y in rotated]
                cs = cells(p)
                if cs and cs <= board:
                    placements[cs] = p
        rotated = [rotate(p) for p in rotated]
    bycell = {c:[p for p in placements if c in p] for c in board}
    answers = []
    def search(rem, chosen):
        if not rem:
            answers.append([placements[p] for p in chosen])
            return
        c = min(rem, key=lambda c:sum(p <= rem for p in bycell[c]))
        for p in bycell[c]:
            if p <= rem:
                search(rem-p, chosen+[p])
                if len(answers) >= limit:
                    return
    search(board, [])
    return answers


SHAPES = {
    'Sailboat': [(0,0),(3,0),(3,1),(2,1),(0,3),(0,1),(-1,1)],
    'Cat': [(-1,0),(1,0),(1,1),(0,2),(0,1),(-1,1),(-2,2),(-2,1)],
    'Hexagon': [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)],
    'Diamond': [(0,0),(2,0),(2,2),(0,2)],
    'Arrow': [(0,0),(2,0),(2,1),(1,2),(-1,2),(0,1)],
    'Star': [(1,0),(1,1),(0,1),(-1,2),(-1,1),(-2,1),(-1,0),(-1,-1),(0,-1),(1,-2),(1,-1),(2,-1)],
    'LongHexagon': [(0,0),(2,0),(2,1),(1,2),(-1,2),(-1,1)],
    'Mountain': [(0,0),(3,0),(0,3)],
}
PIECES = {
    'green': [(0,0),(1,0),(0,1)],
    'blue': [(0,0),(1,0),(1,1),(0,1)],
    'purple': [(0,0),(1,0),(1,1),(0,2),(-1,2),(0,1)],
}


def check():
    data = {}
    for name,poly in SHAPES.items():
        # Each edge must follow a lattice direction, preventing partial cells.
        for (a,b),(c,d) in zip(poly,poly[1:]+poly[:1]):
            assert a == c or b == d or a+b == c+d
        area2 = abs(sum(a*d-c*b for (a,b),(c,d) in zip(poly,poly[1:]+poly[:1])))
        assert area2 == len(cells(poly))
        # Connected by full edges, with one simple boundary and no holes.
        board = cells(poly)
        reached = {next(iter(board))}
        while True:
            nxt = reached | {c for c in board if any(len(set(c)&set(d)) == 2 for d in reached)}
            if nxt == reached: break
            reached = nxt
        assert reached == board
        boundary = Counter(tuple(sorted((t[i],t[(i+1)%3]))) for t in board for i in range(3))
        degree = Counter(v for e,n in boundary.items() if n == 1 for v in e)
        assert all(n == 2 for n in degree.values())
        answers = {color:cover(poly,piece) for color,piece in PIECES.items()}
        assert answers['green']
        for color,solutions in answers.items():
            for sol in solutions:
                covered = [c for tile in sol for c in cells(tile)]
                assert len(covered) == len(set(covered)) == len(board)
                assert set(covered) == board
        data[name] = {'polygon':poly, 'triangle_count':len(board), 'solutions':answers}
        print(name, len(board), {k:len(v[0]) for k,v in answers.items() if v})
    assert data['Arrow']['solutions']['purple'] and data['Star']['solutions']['purple']
    assert data['LongHexagon']['solutions']['blue']
    assert len(data['Hexagon']['solutions']['blue']) == 2
    assert data['Diamond']['solutions']['blue'] and data['Diamond']['solutions']['green']
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')


if __name__ == '__main__':
    check()
