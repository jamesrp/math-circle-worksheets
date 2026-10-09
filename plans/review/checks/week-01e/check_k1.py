"""K-1 packet (F01E-K-v1): every problem, from the boards as drawn in the delivered PDF.
Writes check_k1.out."""
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import *

log = Log(os.path.join(HERE, 'check_k1.out'))
BAND = 'k-1'
ALL = lambda R: greens(R) + blues(R) + reds(R) + yellows(R)
ONE = {'green': greens, 'blue': blues, 'red': reds, 'yellow': yellows}


def mix_str(m):
    y, r, b, g = m
    return ', '.join(f'{n} {k}' for n, k in ((y, 'yellow'), (r, 'red'), (b, 'blue'), (g, 'green')) if n)


def one_colour_report(name, R):
    parts = []
    for col, f in ONE.items():
        n = count_tilings(R, f(R))
        parts.append(f'{col}: {n} tilings' + (f' of {len(R) // {"green": 1, "blue": 2, "red": 3, "yellow": 6}[col]} pieces' if n else ''))
    log(f'  {name}: {describe(R)}; ' + '; '.join(parts))


def fewest_report(name, R):
    mn, cnt, mixes, by_y = fewest(R, ALL(R))
    log(f'  {name}: {describe(R)}; fewest {mn} pieces in {cnt} tilings; mixes: ' +
        ' | '.join(mix_str(m) for m in sorted(mixes)) + f'; most {len(R)} (all greens)')
    log('     fewest by number of yellows: ' + ', '.join(f'{y}Y->{v[0]}' for y, v in sorted(by_y.items())))
    return mn, cnt, mixes


def game_report(name, R, centre_note=True):
    w, good, moves = winner(R)
    ht = half_turn_centre(R)
    s = f'  {name}: {describe(R)}; {len(moves)} first moves; winner {w}'
    if w == '1st':
        s += f'; winning first moves: {len(good)}'
        if ht and ht[1] == 'edge':
            (si, sj), _ = ht
            selfimg = [m for m in moves if frozenset(frozenset((si - v[0], sj - v[1]) for v in c) for c in m) == m]
            s += f'; self-symmetric (centre) blue is winning: {selfimg[0] in good if selfimg else None}; winners == [centre]: {good == selfimg}'
    s += f'; half-turn symmetric: {bool(ht)}' + (f' about a lattice {ht[1]} midpoint' if ht and ht[1] == 'edge' else (' about a lattice point' if ht else ''))
    log(s)
    return w, good, moves


log('K-1 packet, delivered PDF', os.path.relpath(PP.PDFS[BAND], PP.ROOT))

# ---------------------------------------------------------------- page 1
log('\nProblem 1 (page 1): fill each shape with small pieces of its colour; then the biggest pieces')
outs = [o for o in outlines(BAND, 1) if o.path['op'] == 'S' and o.ok]
big = [o for o in outs if o.lw > 1.5]
icons = [o for o in outs if o.lw < 1.5]
for o in sorted(big, key=lambda o: (-round(o.centre[1], 1), o.centre[0])):
    fill = [f for f in outlines(BAND, 1) if f.path['op'] in ('f', 'f*') and abs(f.centre[0] - o.centre[0]) < 1e-3 and abs(f.centre[1] - o.centre[1]) < 1e-3]
    col = colour_name(fill[0].fill) if fill else None
    log(f' printed shape, tint {col}, {BD.classify(o)}, unit {o.unit:.4f} in')
    one_colour_report('   tilings by one colour', o.R)
    if len(yellows(o.R)):
        mx, packs = max_packing(o.R, yellows(o.R))
        log(f'   max yellows that fit: {mx} ({len(packs)} placements); cells left uncovered: {len(o.R) - 6 * mx}')
log(' pictures of the 3x Upscale pieces (bottom row), each rescaled to 3 small edges per side:')
for o in sorted(icons, key=lambda o: o.centre[0]):
    # icon drawn without a grid at scale 0.18 per small edge: re-snap at unit/3
    fr = Frame(o.unit / 3, o.theta, o.page_poly[0])
    lp = [fr.to_lat(q)[0] for q in o.page_poly]
    R = cells_in_lattice_polys([lp])
    fill = [f for f in outlines(BAND, 1) if f.path['op'] in ('f', 'f*') and abs(f.centre[0] - o.centre[0]) < 1e-3]
    col = colour_name(fill[0].fill) if fill else None
    log(f'  3x {col} piece: sides {[round(s) for s in lattice_poly_sides(lp)[0]]}, scale {o.unit / 3:.3f} in per small edge')
    one_colour_report('   tilings by one colour', R)
    if len(yellows(R)):
        mx, packs = max_packing(R, yellows(R))
        log(f'   max yellows that fit: {mx} ({len(packs)} placements); cells left uncovered: {len(R) - 6 * mx}')

# ---------------------------------------------------------------- page 2
log('\nProblem 2 (page 2): the placement game')
for o in stroked_boards(BAND, 2, min_lw=1.5):
    log(f' board {BD.classify(o)} (unit {o.unit:.3f} in)')
    w, good, moves = game_report('  ', o.R)
    log(f'   possible game lengths: {sorted(game_lengths(o.R))}')

# ---------------------------------------------------------------- page 3
log('\nProblem 3 (page 3): fewest and most pieces')
for o in stroked_boards(BAND, 3, min_lw=1.5):
    log(f' picture {BD.classify(o)} (unit {o.unit:.3f} in)')
    fewest_report('  ', o.R)
    ys = yellows(o.R)
    if ys:
        for y in ys:
            rest = o.R - y
            log(f'   with a yellow placed, the rest splits into pieces of sizes {sorted(len(c) for c in components(rest))}; '
                f'fewest with that yellow: {1 + fewest(rest, ALL(rest))[0]}')

# ---------------------------------------------------------------- page 4
log('\nProblem 4 (page 4): the placement game on three more boards')
for o in stroked_boards(BAND, 4, min_lw=1.5):
    log(f' board {BD.classify(o)} (unit {o.unit:.3f} in)')
    w, good, moves = game_report('  ', o.R)
    log(f'   possible game lengths: {sorted(game_lengths(o.R))}')

# ---------------------------------------------------------------- page 5
log('\nProblem 5 (page 5): only reds, then only blues')
for o in stroked_boards(BAND, 5, min_lw=1.5):
    log(f' shape {BD.classify(o)} (unit {o.unit:.3f} in)')
    for col in ('red', 'blue'):
        Ts = all_tilings(o.R, ONE[col](o.R))
        log(f'   {col}: {len(Ts)} tilings' + (f', {len(next(iter(Ts)))} pieces each' if Ts else ' (X)'))

# ---------------------------------------------------------------- page 6
log('\nProblem 6 (page 6): fewest and most pieces')
for o in stroked_boards(BAND, 6, min_lw=1.5):
    log(f' picture {BD.classify(o)} (unit {o.unit:.3f} in)')
    mn, cnt, mixes = fewest_report('  ', o.R)
    for T in min_tilings(o.R, ALL(o.R), mn):
        log('     a fewest tiling: ' + ', '.join(sorted(kind_of(p) for p in T)))
        break

# ---------------------------------------------------------------- page 7
log('\nProblem 7 (page 7): the yellow hexagon with 2 reds, then 3 blues')
o = stroked_boards(BAND, 7, min_lw=1.5)[0]
log(f' outline {BD.classify(o)} (unit {o.unit:.3f} in)')
for col in ('red', 'blue'):
    Ts = all_tilings(o.R, ONE[col](o.R))
    log(f'   {col}: {len(Ts)} tilings of {len(next(iter(Ts)))} pieces')
small = [b for b in stroked_boards(BAND, 7, max_lw=1.0) if b.grid]
rows = {}
for b in small:
    rows.setdefault(round(b.centre[1], 1), []).append(b)
for y, bs in sorted(rows.items(), reverse=True):
    log(f'  recording hexagons in the row at y={y}: {len(bs)} ({BD.classify(bs[0])})')

log.save()
