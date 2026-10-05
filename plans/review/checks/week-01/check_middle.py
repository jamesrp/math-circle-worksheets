"""Grades 2-3: boards, outlines, up/down counts, exact max packings, witness diagrams."""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import re, sys
sys.path.insert(0, HERE)
from lattice import *

s = open(SRC + 'middle-geometry.tex').read()
defs = {}
for m in re.finditer(r'\\expandafter\\def\\csname (\w+)\\endcsname\{', s):
    start = m.end(); depth = 1; k = start
    while depth:
        if s[k] == '{': depth += 1
        elif s[k] == '}': depth -= 1
        k += 1
    defs[m.group(1)] = s[start:k - 1]

boards = sorted(n[len('MiddleGrid'):] for n in defs if n.startswith('MiddleGrid'))
results = {}
for b in boards:
    g = defs['MiddleGrid' + b]
    paths = parse_paths(g)
    grid = [(seg, pts) for seg, pts in paths if 'gridline' in g[g.find(seg) - 20:g.find(seg)]]
    # separate gridline cells and the outline: outline is the last \draw[outline]
    cells_drawn = set()
    outline = None
    for mm in re.finditer(r'\\draw\[(\w+)\]\s*([^;]*);', g):
        style, seg = mm.group(1), mm.group(2)
        pts = parse_points(seg)
        if style == 'gridline':
            cells_drawn.add(cell_from_vertices([to_lattice(*p) for p in pts]))
        elif style == 'outline':
            outline = pts
    cells = cells_in_poly(outline)
    up = sum(1 for c in cells if c[0] == 'U'); dn = len(cells) - up
    lat = [to_lattice(*p) for p in outline]
    bp, bw = max_packing(cells, placements(BLUE, cells))
    pls_p = placements(PURPLE, cells)
    pp, pw = max_packing(cells, pls_p) if pls_p else (0, [])
    results[b] = dict(area=len(cells), up=up, down=dn, blue=bp, purple=pp)
    print(f'{b:10s} outline={[(int(u),int(v)) for u,v in lat]}')
    print(f'           grid==outline cells: {cells_drawn == cells}  area={len(cells)} up={up} down={dn} '
          f'maxBlue={bp} (gaps {len(cells)-2*bp}) maxPurple={pp} (gaps {len(cells)-4*pp})')
    # check witness drawings
    for color, piece in [('blue', BLUE), ('purple', PURPLE)]:
        w = defs.get('MiddlePacking' + b + color)
        if w is None:
            continue
        tiles = []
        for mm in re.finditer(r'\\draw\[tile[^\]]*\]\s*([^;]*);', w):
            poly = parse_points(mm.group(1))
            tc = cells_in_poly(poly)
            tiles.append(frozenset(tc))
        shapes_ok = all(normalize(t) in all_orientations(piece) for t in tiles)
        disjoint = sum(len(t) for t in tiles) == len(set().union(*tiles)) if tiles else True
        inside = all(t <= cells for t in tiles)
        print(f'           witness {color}: {len(tiles)} tiles, shapes ok={shapes_ok}, disjoint={disjoint}, inside={inside}')

# Purple placements at the sharp corners of Three B
print()
cB = None
g = defs['MiddleGridThreeB']
outline = [parse_points(mm.group(2)) for mm in re.finditer(r'\\draw\[(\w+)\]\s*([^;]*);', g) if mm.group(1) == 'outline'][0]
cB = cells_in_poly(outline)
pls = placements(PURPLE, cB)
covered = set().union(*pls) if pls else set()
print('ThreeB purple placements:', len(pls), 'cells never coverable by a purple:', sorted(cB - covered))
print('ThreeB all purple placements:', [sorted(p) for p in pls])

# Grades 2-3 Problem 2 claims: Triangle n: maximum blues n(n-1)/2, gaps n
for n in range(2, 6):
    r = results['Triangle%d' % n]
    print(f'T{n}: up={r["up"]} down={r["down"]} maxBlue={r["blue"]} gaps={r["area"]-2*r["blue"]}')
