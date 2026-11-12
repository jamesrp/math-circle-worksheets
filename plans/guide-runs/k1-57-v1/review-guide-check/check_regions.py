"""Count half-shapes by covered region (how the region is cut into halves does not matter)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pieces import *

H = enumerate_shapes(8, squares=False)
pub = [1, 3, 4, 14, 30, 107, 318, 1116]
for n in range(1, 9):
    regs = {}
    for s in H[n]:
        regs.setdefault(region_key(s), s)
    gf = {k: s for k, s in regs.items() if not has_gap(s)}
    tally = {}
    for s in gf.values():
        h, b, i = counts(s)
        tally[(b, i)] = tally.get((b, i), 0) + 1
    rot = {region_key(s, ROTS) for s in H[n] if not has_gap(s)}
    line = f'{n} halves: free regions {len(regs)} (published {pub[n-1]}), gap-free {len(gf)}, turns-only {len(rot)}, (outline,inside) {dict(sorted(tally.items()))}'
    if n in (3, 4):
        line += f', all fit 2x3 spacings: {all(fits(s, 2, 3) for s in gf.values())}'
    if n == 8:
        line += f', all answers (<8) fit 3x4: {all(fits(s, 3, 4) for s in gf.values() if counts(s)[1] < 8)}'
    print(line)
