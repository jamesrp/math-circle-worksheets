"""Which H122 tilings are identified by symmetries of the board that keep the bold bottom edge at the bottom?"""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import re, sys
sys.path.insert(0, HERE)
from lattice import *
tsrc = open(SRC + 'tilings.tex').read()
cards = {}
for L in 'ABCDEF':
    m = re.search(r'\\newcommand\{\\Tiling' + L + r'\}\{(.*)\}$', tsrc, re.M)
    cards[L] = frozenset(frozenset(cells_in_poly(parse_points(seg))) for seg in re.findall(r'\\draw\[tile\]\s*([^;]*);', m.group(1)))
inv = {v: k for k, v in cards.items()}

def map_tiling(t, f):
    return frozenset(frozenset(cell_from_vertices([f(p) for p in cell_vertices(c)]) for c in tile) for tile in t)

# vertical mirror x -> 1 - x in xy; in lattice (u,v): x = u + v/2 -> 1 - u - v/2 = u' + v/2  => u' = 1 - u - v, v' = v
mirror = lambda p: (1 - p[0] - p[1], p[1])
# 180-degree rotation about board centre (0.5, 2h): (x,y) -> (1-x, 4h-y); v' = 4 - v, u' = 1 - x - (4-v)/2 ... compute
def rot180(p):
    u, v = p
    x = u + v / 2
    x2, v2 = 1 - x, 4 - v
    return (x2 - v2 / 2, v2)
for name, f in [('left-right mirror (keeps bold edge at bottom)', mirror), ('180-degree rotation (moves bold edge to top)', rot180)]:
    print(name + ':', {L: inv.get(map_tiling(cards[L], f), '?') for L in 'ABCDEF'})
