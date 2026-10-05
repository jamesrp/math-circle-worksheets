"""Validate every K-1 solution witness macro (only Arrow/Star purple are printed in the guide)."""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import re, sys
sys.path.insert(0, HERE)
from lattice import *
s = open(SRC + 'k1-geometry.tex').read()
shapes = {m.group(1): cells_in_poly(parse_points(m.group(2))) for m in re.finditer(r'\\newcommand\{\\K(\w+?)Path\}\{([^}]*)\}', s)}
piece = {'Green': GREEN, 'Blue': BLUE, 'Purple': PURPLE}
for m in re.finditer(r'\\newcommand\{\\K(\w+?)(Green|Blue|Purple)Solution\}\{(.*)\}$', s, re.M):
    name, col, body = m.groups()
    tiles = [frozenset(cells_in_poly(parse_points(seg))) for seg in re.findall(r'\\draw\[[^\]]*\]\s*([^;]*);', body)]
    ok_shape = all(normalize(t) in all_orientations(piece[col]) for t in tiles)
    union = set().union(*tiles)
    exact = union == shapes[name] and sum(map(len, tiles)) == len(union)
    print(f'{name:12s} {col:7s} tiles={len(tiles):2d} shapes_ok={ok_shape} exact_tiling={exact}')
