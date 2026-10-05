"""Check K-1 outlines: area, lattice alignment, and tilings with the kit pieces."""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import re, sys
sys.path.insert(0, HERE)
from lattice import *

s = open(SRC + 'k1-geometry.tex').read()
shapes = {}
for m in re.finditer(r'\\newcommand\{\\K(\w+?)Path\}\{([^}]*)\}', s):
    shapes[m.group(1)] = parse_points(m.group(2))

for name, poly in shapes.items():
    lat = [to_lattice(*p) for p in poly]
    nonint = [p for p in lat if p[0].denominator != 1 or p[1].denominator != 1]
    cells = cells_in_poly(poly)
    area = poly_area_triangles(poly)
    up = sum(1 for c in cells if c[0] == 'U'); dn = len(cells) - up
    print(f'== {name}: vertices {[(int(u),int(v)) for u,v in lat]} nonlattice={nonint}')
    print(f'   area(triangles)={area:.3f} cells={len(cells)} up={up} down={dn}')
    res = {}
    for pname, piece in [('green', GREEN), ('blue', BLUE), ('red', RED), ('yellow', YELLOW), ('purple', PURPLE)]:
        pls = placements(piece, cells)
        if len(cells) % len(piece):
            res[pname] = 'area-indivisible'
            continue
        sols = count_tilings(cells, pls)
        res[pname] = len(sols)
    print('   single-colour exact tilings:', res)
    # max packings for single colour
    mp = {}
    for pname, piece in [('blue', BLUE), ('purple', PURPLE), ('red', RED)]:
        pls = placements(piece, cells)
        mp[pname] = max_packing(cells, pls)[0] if pls else 0
    print('   max single-colour packing:', mp)

# Mixed tilings with the stated K-1 kit (6 blues, 12 greens, 3 purples, a few reds/yellows)
print()
print('Mixed tilings (any pieces) counts, ignoring kit limits:')
for name in ['Sailboat', 'Cat', 'Hexagon', 'Diamond', 'LongHexagon', 'Mountain']:
    cells = cells_in_poly(shapes[name])
    piece_pls = {n: placements(p, cells) for n, p in [('G', GREEN), ('B', BLUE), ('R', RED), ('Y', YELLOW), ('P', PURPLE)]}
    sols = tilings_multi(cells, piece_pls)
    # count distinct multisets of piece usage
    from collections import Counter
    usage = Counter(tuple(sorted(Counter(n for n, _ in sol).items())) for sol in sols)
    print(f'  {name}: {len(sols)} tilings; min pieces {min(len(x) for x in sols)}; usage kinds {len(usage)}')
    # tilings possible within one child kit: <=6B,<=12G,<=3P, reds/yellows "a few" (say <=3)
    ok = [sol for sol in sols if sum(1 for n, _ in sol if n == 'B') <= 6 and sum(1 for n, _ in sol if n == 'G') <= 12 and sum(1 for n, _ in sol if n == 'P') <= 3]
    print(f'     within 6B/12G/3P kit: {len(ok)}')
