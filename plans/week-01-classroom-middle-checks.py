#!/usr/bin/env python3
"""Exact small-blue / purple-chevron packing checks for revised Week 1.

Coordinates (u,v) mean (u+v/2, sqrt(3)*v/2) small-block edges.
A blue covers two adjacent whole triangle cells; a purple is exactly the
physical chevron polygon used in common.tex. Only translations and six
60-degree rotations are admitted, with no cuts, overlaps, or outside cells.
The dynamic program considers both covering and leaving its next cell empty,
so it certifies maximum covered area rather than only testing exact tilings.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parent
base = runpy.run_path(str(ROOT / 'week-01-k1-shape-checks.py'))
cells, rotate = base['cells'], base['rotate']
BLUE = base['PIECES']['blue']
PURPLE = base['PIECES']['purple']

def triangle(n): return [(0,0),(n,0),(0,n)]

BOARDS = {
    'OneA': triangle(3),
    # The former Board B (2 x 1) extended by two more complete rows.
    'OneB': [(0,0),(2,0),(2,3),(0,3)],
    # Clip its top-right down-pointing cell: six up and five down remain.
    'OneC': [(0,0),(2,0),(2,2),(1,3),(0,3)],
    'OneD': base['SHAPES']['LongHexagon'],
    **{'Triangle'+str(n): triangle(n) for n in range(2,6)},
    'ThreeA': [(0,0),(3,0),(3,1),(2,2),(-1,2),(0,1)],
    'ThreeB': base['SHAPES']['Diamond'],
    'ThreeC': base['SHAPES']['Arrow'],
    'ThreeD': base['SHAPES']['LongHexagon'],
    'ThreeE': [(0,0),(2,0),(2,1),(1,2),(-1,2),(-1,1),(0,1)],
    'ThreeF': [(0,0),(3,0),(1,2),(0,2)],
}

def placements(board, piece):
    result = {}
    rotated = piece
    vertices = {p for c in board for p in c}
    lo = min(x for p in vertices for x in p)-6
    hi = max(x for p in vertices for x in p)+6
    for _ in range(6):
        for u in range(lo,hi+1):
            for v in range(lo,hi+1):
                poly = [(x+u,y+v) for x,y in rotated]
                cover = cells(poly)
                if cover and cover <= board:
                    result[cover] = poly
        rotated = [rotate(p) for p in rotated]
    return result

def solve(board, piece):
    ps = placements(board, piece)
    cs = sorted(board)
    ix = {c:i for i,c in enumerate(cs)}
    masks = {sum(1 << ix[c] for c in p):poly for p,poly in ps.items()}
    bycell = {i:[m for m in masks if m & (1<<i)] for i in range(len(cs))}
    @lru_cache(None)
    def best(rem):
        if not rem: return 0, ()
        candidates = [i for i in range(len(cs)) if rem & (1<<i)]
        i = min(candidates, key=lambda i:sum(m & rem == m for m in bycell[i]))
        ans = best(rem ^ (1<<i))
        for mask in bycell[i]:
            if mask & rem == mask:
                score, chosen = best(rem ^ mask)
                score += mask.bit_count()
                if score > ans[0]: ans = score, (mask,)+chosen
        return ans
    covered, chosen = best((1<<len(cs))-1)
    polygons = [masks[m] for m in chosen]
    covered_cells = [c for poly in polygons for c in cells(poly)]
    assert len(covered_cells) == covered == len(set(covered_cells))
    assert set(covered_cells) <= board
    return {'pieces':len(chosen),'gaps':len(board)-covered,
            'placements':polygons, 'legal_placements':len(masks)}

def check_board(poly):
    board = cells(poly)
    area2 = abs(sum(a*d-c*b for (a,b),(c,d) in zip(poly,poly[1:]+poly[:1])))
    assert area2 == len(board), 'Whole-cell board required'
    for (a,b),(c,d) in zip(poly,poly[1:]+poly[:1]):
        assert a==c or b==d or a+b==c+d
    reached = {next(iter(board))}
    while True:
        nxt = reached | {c for c in board if any(len(set(c)&set(d))==2 for d in reached)}
        if nxt==reached: break
        reached=nxt
    assert reached==board, 'Edge-connected board required'
    boundary=Counter(tuple(sorted(e)) for c in board for e in combinations(c,2))
    degree=Counter(p for e,n in boundary.items() if n==1 for p in e)
    assert all(n==2 for n in degree.values()), 'Simple boundary required'
    return board

def up(c):
    return sum(p[1]==min(v[1] for v in c) for p in c)==2

def independent_blue_matching(board):
    """Independent bipartite augmenting-path verification of blue optimum."""
    ups=[c for c in board if up(c)]
    downs=[c for c in board if not up(c)]
    adj={c:[d for d in downs if len(set(c)&set(d))==2] for c in ups}
    matched={}
    def augment(c,seen):
        for d in adj[c]:
            if d in seen: continue
            seen.add(d)
            if d not in matched or augment(matched[d],seen):
                matched[d]=c
                return True
        return False
    return sum(augment(c,set()) for c in ups)

def main():
    data={}
    # Every orientation of the physical purple can be replaced by two blues.
    p=PURPLE
    for _ in range(6):
        assert solve(cells(p),BLUE)['gaps']==0
        p=[rotate(v) for v in p]
    for name,poly in BOARDS.items():
        board=check_board(poly)
        blue=solve(board,BLUE)
        purple=solve(board,PURPLE)
        assert blue['pieces']==independent_blue_matching(board)
        assert blue['gaps']<=purple['gaps']
        data[name]={'polygon':poly,'cells':[list(c) for c in sorted(board)],
                    'total':len(board),'up':sum(up(c) for c in board),
                    'down':sum(not up(c) for c in board),'blue':blue,'purple':purple}
        print(name, 'total/up/down:', data[name]['total'],data[name]['up'],data[name]['down'],
              'blue pieces/gaps:',blue['pieces'],blue['gaps'],
              'purple pieces/gaps:',purple['pieces'],purple['gaps'])
    expected={
        'OneA':(9,6,3,3),'OneB':(12,6,6,0),
        'OneC':(11,6,5,1),'OneD':(10,5,5,0),
    }
    for n,x in expected.items():
        d=data[n]
        assert (d['total'],d['up'],d['down'],d['blue']['gaps'])==x
    for n in range(2,6):
        d=data['Triangle'+str(n)]
        assert d['blue']['gaps']==n and d['blue']['pieces']==n*(n-1)//2
    for n in ['ThreeA','ThreeC']:
        assert data[n]['blue']['gaps']==data[n]['purple']['gaps']==0
    for n in ['ThreeB','ThreeD']:
        assert data[n]['blue']['gaps']==0 < data[n]['purple']['gaps']
    assert 0<data['ThreeE']['blue']['gaps']==data['ThreeE']['purple']['gaps']
    assert 0<data['ThreeF']['blue']['gaps']<data['ThreeF']['purple']['gaps']
    (ROOT/'week-01-classroom-middle-checks.json').write_text(json.dumps(data,indent=2)+'\n')

if __name__=='__main__': main()
