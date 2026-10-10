"""Week 32 student pages: read every board back from the delivered PDFs and
recompute every answer independently.  Writes out_check_students32.txt."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common32 import *
from math32 import *

OUT = []
FAILS = []


def log(s=''):
    OUT.append(s)


def check(name, cond, detail=''):
    tag = 'PASS' if cond else 'FAIL'
    log(f'  [{tag}] {name}' + (f' -- {detail}' if detail else ''))
    if not cond:
        FAILS.append(name)


def page_boards(band, pg):
    rects, gv, gh = boards(PDFS[band], pg)
    words = page_words(PDFS[band], pg)
    res = []
    for r in rects:
        g = board_grid(r, gv, gh)
        top = 792 - r['yt']; bot = 792 - r['yb']
        above = [w['t'] for w in words if top - 22 < w['cy'] < top and r['x0'] <= w['cx'] <= r['x1'] and w['t'].isdigit()]
        left = [w['t'] for w in words if r['x0'] - 22 < w['cx'] < r['x0'] and top <= w['cy'] <= bot and w['t'].isdigit()]
        inside = ' '.join(w['t'] for w in words if r['x0'] < w['cx'] < r['x1'] and top < w['cy'] < bot)
        below = ' '.join(w['t'] for w in words if r['x0'] - 10 <= w['cx'] <= r['x1'] + 10 and bot < w['cy'] < bot + 25)
        res.append(dict(r=r, g=g, top=top, bot=bot, above=above, left=left, inside=inside, below=below,
                        shaded=r['op'] in ('B', 'f') and r['fill'] != (0.0,), dash=r['dash']))
    res.sort(key=lambda b: (round(b['top']), b['r']['x0']))
    return res, free_grids(gv, gh), words


def main_boards(band, pg):
    """Outlined, unshaded boards (not the launch example strip on page 1)."""
    bs, fg, words = page_boards(band, pg)
    return [b for b in bs if not b['shaded'] and b['top'] > 200 or (pg > 1 and not b['shaded'])], fg, bs


def labelled(b):
    w = int(b['above'][0]) if len(b['above']) == 1 else None
    h = int(b['left'][0]) if len(b['left']) == 1 else None
    return w, h


def board_line(b):
    g = b['g']
    return (f"{g['cols']}x{g['rows']} cells, spacing {g['ux']/CM:.3f} x {g['uy']/CM:.3f} cm, "
            f"labels top={b['above']} left={b['left']}")


def check_board(name, b, w, h, unit_cm=1.0):
    g = b['g']
    lw, lh = labelled(b)
    check(f'{name}: {w} wide by {h} tall, labelled {w} and {h}, square cells of {unit_cm} cm',
          g['cols'] == w and g['rows'] == h and lw == w and lh == h and g['even']
          and abs(g['ux'] - g['uy']) < 0.05 and abs(g['ux'] / CM - unit_cm) < 0.01,
          board_line(b))


def text_has(band, pg, phrase):
    t = norm(page_text(PDFS[band], pg))
    return norm(phrase) in t


def launch_example(band):
    log(f'{band} p1 launch example')
    bs, fg, words = page_boards(band, 1)
    ex = [b for b in bs if b['top'] < 200]
    plain = [b for b in ex if not b['shaded']]
    shaded = [b for b in ex if b['shaded']]
    check('three example rectangles and one shaded square', len(plain) == 3 and len(shaded) == 1,
          f'{len(plain)} plain, {len(shaded)} shaded')
    a, bb, c = sorted(plain, key=lambda b: b['r']['x0'])
    check_board('example start', a, 5, 2, 0.7)
    check_board('example middle', bb, 5, 2, 0.7)
    check_board('example remainder', c, 3, 2, 0.7)
    s = shaded[0]
    check('shaded square is 2x2 at the left end of the middle rectangle, labelled 2',
          s['g']['cols'] == 2 and s['g']['rows'] == 2 and abs(s['r']['x0'] - bb['r']['x0']) < 0.1
          and abs(s['r']['yt'] - bb['r']['yt']) < 0.1 and abs(s['r']['yb'] - bb['r']['yb']) < 0.1 and s['inside'] == '2',
          f"inside text {s['inside']!r}")
    check('rule on 5x2: first square 2, remainder 3x2', greedy(5, 2)[0] == 2 and (5 - 2, 2) == (3, 2))
    check('captions say "cover a 2 by 2 square" and "3 by 2 remains"',
          text_has(band, 1, 'cover a 2 by 2 square') and text_has(band, 1, '3 by 2 remains'))


def seq(a, b):
    return ','.join(map(str, greedy(a, b)))


# ======================================================================== K-1
def k1():
    band = 'k-1'
    log('=' * 70); log('K-1'); log('=' * 70)
    launch_example(band)
    log('K-1 P1 (p1): "Cover both rectangles with the biggest-square rule. Which square comes last?"')
    bs, fg, _ = page_boards(band, 1)
    m = [b for b in bs if b['top'] > 200]
    check_board('P1 board A', m[0], 6, 4); check_board('P1 board B', m[1], 8, 4)
    log(f'    6x4: {seq(6,4)} (last {greedy(6,4)[-1]});  8x4: {seq(8,4)} (last {greedy(8,4)[-1]})')
    check('P1 answers 2 and 4', greedy(6, 4)[-1] == 2 and greedy(8, 4)[-1] == 4)

    log('K-1 P2 (p2): "Predict whether the last squares will match. Test both rectangles"')
    bs, fg, _ = page_boards(band, 2)
    check_board('P2 board A', bs[0], 7, 4); check_board('P2 board B', bs[1], 8, 5)
    log(f'    7x4: {seq(7,4)};  8x5: {seq(8,5)}')
    check('P2 last squares match (1 and 1)', greedy(7, 4)[-1] == greedy(8, 5)[-1] == 1)

    log('K-1 P3 (p3): "Will they end with the same size square?"')
    bs, fg, _ = page_boards(band, 3)
    check_board('P3 board A', bs[0], 9, 6); check_board('P3 board B', bs[1], 10, 6)
    log(f'    9x6: {seq(9,6)};  10x6: {seq(10,6)}')
    check('P3 last squares differ (3 and 2)', greedy(9, 6)[-1] == 3 and greedy(10, 6)[-1] == 2)

    log('K-1 P4 (p4): "Cover each rectangle with squares that are all the same size. Find the biggest square size that works."')
    bs, fg, _ = page_boards(band, 4)
    check_board('P4 board A', bs[0], 6, 4); check_board('P4 board B', bs[1], 8, 6)
    for w, h in [(6, 4), (8, 6)]:
        ok = [s for s in range(1, min(w, h) + 1) if equal_square_tiles(w, h, s)]
        log(f'    {w}x{h}: equal squares that tile (by search) {ok}')
        check(f'P4 {w}x{h} biggest equal square is 2', max(ok) == 2)

    log('K-1 P5 (p5): "Find every rectangle you can make with four 3 by 3 squares, counting turns as the same shape. '
        'Will their last squares match under the biggest-square rule?"')
    bs, fg, _ = page_boards(band, 5)
    check('P5 shows four 3x3 squares', len(bs) == 4 and all(b['g']['cols'] == 3 and b['g']['rows'] == 3 for b in bs))
    for i, b in enumerate(bs):
        check_board(f'P5 square {i+1}', b, 3, 3)
    shapes = rect_shapes_from_squares(4, 3)
    log(f'    rectangles tiled by exactly four 3x3 squares (search over all area-36 rectangles): {shapes}')
    check('P5 exactly two shapes, 3x12 and 6x6', shapes == [(3, 12), (6, 6)])
    lasts = {s: greedy(*s)[-1] for s in shapes}
    log(f'    greedy: 3x12 -> {seq(3,12)}; 6x6 -> {seq(6,6)}')
    check('P5 last squares do not match (3 vs 6)', lasts[(3, 12)] == 3 and lasts[(6, 6)] == 6)
    fewer = sorted({sh for n in (1, 2, 3) for sh in rect_shapes_from_squares(n, 3)})
    log(f'    other reading (fewer than four squares): extra shapes {fewer}')
    check('P5 one free work grid', len(fg) == 1)
    g = fg[0]
    log(f'    work grid {g["cols"]} x {g["rows"]} cells at {g["ux"]/CM:.3f} cm (squares above at {bs[0]["g"]["ux"]/CM:.3f} cm)')
    check('P5 work grid uses the same 1 cm cells as the 3x3 squares', abs(g['ux'] - bs[0]['g']['ux']) < 0.05 and g['even'])
    each = {s: can_pack(g['cols'], g['rows'], [s]) for s in shapes}
    both = can_pack(g['cols'], g['rows'], shapes)
    log(f'    fits on the {g["cols"]}x{g["rows"]} work grid one at a time: {each}; both at once: {both}')
    check('P5 each answer fits the work grid', all(each.values()))
    check('P5 work grid holds the complete answer (both rectangles at once)', both,
          f'3x12 must lie along the 12-cell side, leaving {g["rows"]}-3={g["rows"]-3} rows; 6x6 needs 6')
    for rows in range(g['rows'], 13):
        if can_pack(g['cols'], rows, shapes):
            log(f'    smallest work grid {g["cols"]} wide that holds both: {g["cols"]} x {rows}')
            break


# ======================================================================== 2-3
def g23():
    band = '2-3'
    log('=' * 70); log('Grades 2-3'); log('=' * 70)
    launch_example(band)
    log('2-3 P1 (p1): record the square sizes in order')
    bs, fg, _ = page_boards(band, 1)
    m = [b for b in bs if b['top'] > 200]
    check_board('P1 board A', m[0], 10, 6); check_board('P1 board B', m[1], 8, 5)
    log(f'    10x6: {seq(10,6)};  8x5: {seq(8,5)}')
    check('P1 lists 6,4,2,2 and 5,3,2,1,1', seq(10, 6) == '6,4,2,2' and seq(8, 5) == '5,3,2,1,1')

    log('2-3 P2 (p2): "How does changing one side change the last square?"')
    bs, fg, _ = page_boards(band, 2)
    check_board('P2 board A', bs[0], 12, 8); check_board('P2 board B', bs[1], 12, 9)
    log(f'    12x8: {seq(12,8)};  12x9: {seq(12,9)}')
    check('P2 last squares 4 and 3', greedy(12, 8)[-1] == 4 and greedy(12, 9)[-1] == 3)

    log('2-3 P3 (p3): "Find every whole-number square size that works, and decide which is biggest."')
    bs, fg, _ = page_boards(band, 3)
    check_board('P3 board A', bs[0], 12, 8); check_board('P3 board B', bs[1], 10, 6)
    for (w, h), want in [((12, 8), [1, 2, 4]), ((10, 6), [1, 2])]:
        ok = [s for s in range(1, min(w, h) + 1) if equal_square_tiles(w, h, s)]
        log(f'    {w}x{h}: {ok}')
        check(f'P3 {w}x{h} sizes {want}', ok == want)

    log('2-3 P4 (p4): sort by last square; predict 6 by 10')
    bs, fg, _ = page_boards(band, 4)
    check_board('P4 board A', bs[0], 7, 6); check_board('P4 board B', bs[1], 8, 6); check_board('P4 board C', bs[2], 9, 6)
    for w in (7, 8, 9, 10):
        log(f'    {w}x6: {seq(w,6)} (last {greedy(w,6)[-1]})')
    check('P4 lasts 1,2,3 and 6x10 -> 2 (not the extrapolated 4)',
          [greedy(w, 6)[-1] for w in (7, 8, 9)] == [1, 2, 3] and greedy(6, 10)[-1] == 2)

    log('2-3 P5 (p5): last square vs biggest identical squares')
    bad = [(a, b) for a in range(1, 26) for b in range(1, 26)
           if greedy(a, b)[-1] != max(s for s in range(1, min(a, b) + 1) if equal_square_tiles(a, b, s))]
    check('P5 last square = largest identical tile for every a,b <= 25 (search)', not bad, str(bad[:5]))

    log('2-3 P6 (p5): "Make three rectangles with different first squares and the same last square of side 3. '
        'Choose each starting side from 3, 6, 9 and 12."')
    S = [3, 6, 9, 12]
    rects = sorted({tuple(sorted((a, b), reverse=True)) for a in S for b in S})
    good = [(a, b) for a, b in rects if greedy(a, b)[-1] == 3]
    byfirst = {}
    for a, b in good:
        byfirst.setdefault(greedy(a, b)[0], []).append((a, b))
    log(f'    rectangles with last square 3, grouped by first square: {byfirst}')
    check('P6 possible: first squares 3, 6, 9 available', sorted(byfirst) == [3, 6, 9])
    check('P6 6-first and 9-first rectangles are forced (6x9 and 9x12)', byfirst[6] == [(9, 6)] and byfirst[9] == [(12, 9)])
    bs, fg, _ = page_boards(band, 5)
    check('P6 one free work grid', len(fg) == 1)
    g = fg[0]
    log(f'    work grid {g["cols"]} x {g["rows"]} cells at {g["ux"]/CM:.3f} cm')
    trios = [(x, y, z) for x in byfirst[3] for y in byfirst[6] for z in byfirst[9]]
    packs = {t: can_pack(g['cols'], g['rows'], list(t)) for t in trios}
    minarea = min(sum(a * b for a, b in t) for t in trios)
    log(f'    any valid trio drawable at once on the grid: {any(packs.values())}; smallest trio area {minarea} vs grid {g["cols"]*g["rows"]}')
    check('P6 work grid holds a complete answer (three rectangles at once)', any(packs.values()),
          f'every valid trio needs at least {minarea} cells; the grid has {g["cols"]*g["rows"]}')
    check('P6 each needed rectangle fits the grid on its own', all(can_pack(g['cols'], g['rows'], [r]) for r in good))
    for rows in range(g['rows'], 25):
        hit = [t for t in trios if can_pack(g['cols'], rows, list(t))]
        if hit:
            log(f'    smallest work grid {g["cols"]} wide that holds a valid trio: {g["cols"]} x {rows}, e.g. {hit[0]}')
            break


# ======================================================================== 4-5
def g45():
    band = '4-5'
    log('=' * 70); log('Grades 4-5'); log('=' * 70)
    launch_example(band)
    log('4-5 P1 (p1): every square size including repeats; compare last squares')
    bs, fg, _ = page_boards(band, 1)
    m = [b for b in bs if b['top'] > 200]
    check_board('P1 board A', m[0], 10, 6); check_board('P1 board B', m[1], 8, 5)
    check('P1 lists 6,4,2,2 / 5,3,2,1,1; last 2 vs 1', seq(10, 6) == '6,4,2,2' and seq(8, 5) == '5,3,2,1,1')

    log('4-5 P2 (p2): predict, test, find a rule')
    bs, fg, _ = page_boards(band, 2)
    check_board('P2 board A', bs[0], 15, 9); check_board('P2 board B', bs[1], 14, 8)
    log(f'    15x9: {seq(15,9)};  14x8: {seq(14,8)}')
    check('P2 last squares 3 and 2 (= gcd)', greedy(15, 9)[-1] == 3 and greedy(14, 8)[-1] == 2)

    log('4-5 P3 (p3): every identical whole-grid square size; completeness')
    bs, fg, _ = page_boards(band, 3)
    check_board('P3 board A', bs[0], 12, 8); check_board('P3 board B', bs[1], 15, 9)
    for (w, h), want in [((12, 8), [1, 2, 4]), ((15, 9), [1, 3])]:
        ok = [s for s in range(1, max(w, h) + 1) if equal_square_tiles(w, h, s)]
        check(f'P3 {w}x{h} sizes {want}', ok == want, str(ok))

    log('4-5 P4 (p4): 14 by 8 loses an 8 by 8 square')
    bs, fg, _ = page_boards(band, 4)
    plain = [b for b in bs if not b['shaded']]
    sh = [b for b in bs if b['shaded']]
    check_board('P4 before-cut rectangle', plain[0], 14, 8, 0.62)
    check_board('P4 after-cut rectangle', plain[1], 6, 8, 0.62)
    s = sh[0]
    check('P4 shaded 8x8 square at the left end, labelled "8 by 8"',
          s['g']['cols'] == 8 and s['g']['rows'] == 8 and abs(s['r']['x0'] - plain[0]['r']['x0']) < 0.1
          and abs(s['r']['yt'] - plain[0]['r']['yt']) < 0.1 and abs(s['r']['yb'] - plain[0]['r']['yb']) < 0.1
          and s['inside'].startswith('8 by 8'), s['inside'])
    check('P4 biggest-square cut of 14x8 is 8x8 leaving 6x8', greedy(14, 8)[0] == 8)
    check('P4 common measures before {1,2} and after {1,2}', common_divisors(14, 8) == common_divisors(6, 8) == [1, 2])
    bad = [(a, b) for a in range(2, 80) for b in range(1, a) if common_divisors(a, b) != common_divisors(a - b, b)]
    check('P4 "always match": common divisors of (a,b) = of (a-b,b) for all b<a<80', not bad)

    log('4-5 P5 (p4): last square = largest identical tiling square')
    bad = [(a, b) for a in range(1, 31) for b in range(1, 31)
           if greedy(a, b)[-1] != max(s for s in range(1, min(a, b) + 1) if equal_square_tiles(a, b, s))]
    check('P5 true for all a,b <= 30', not bad)

    log('4-5 P6 (p5): longer side 9..15, shorter 2..8: most different square sizes; every rectangle that ties')
    table = {(L, S): distinct_sizes(L, S) for L in range(9, 16) for S in range(2, 9)}
    best = max(table.values())
    winners = [k for k, v in table.items() if v == best]
    log('    distinct sizes:   S=' + ' '.join(f'{S:>2}' for S in range(2, 9)))
    for L in range(9, 16):
        log(f'      L={L:>2}           ' + ' '.join(f'{table[(L,S)]:>2}' for S in range(2, 9)))
    log(f'    max {best} at {winners}; {seq(13,8)}')
    pieces = {(L, S): len(greedy(L, S)) for L in range(9, 16) for S in range(2, 9)}
    pb = max(pieces.values())
    log(f'    (other reading, most pieces: max {pb} at {[k for k,v in pieces.items() if v==pb]})')
    check('P6 49 candidates', len(table) == 49)
    check('P6 unique winner 13x8 with 5 sizes', winners == [(13, 8)] and best == 5)
    log('    note: the page asks "Find every rectangle that ties", but nothing ties with the winner')
    bs, fg, _ = page_boards(band, 5)
    check('P6 two free 15x8 work grids at 1 cm', len(fg) == 2 and all(g['cols'] == 15 and g['rows'] == 8 and g['even']
                                                             and abs(g['ux'] / CM - 1) < 0.01 for g in fg))
    check('P6 every candidate fits one work grid', all(L <= 15 and S <= 8 for L, S in table))


# ======================================================================== bonus
def bonus():
    band = 'bonus'
    log('=' * 70); log('Bonus companion (Grades 2-5)'); log('=' * 70)
    log('Bonus P1 (p1): greedy on the left board, fewest squares on the right')
    bs, fg, _ = page_boards(band, 1)
    dims = [(b['g']['cols'], b['g']['rows']) for b in bs]
    check('P1 boards are 6x5, 6x5, 4x3, 4x3 (1 cm square cells)', dims == [(6, 5), (6, 5), (4, 3), (4, 3)]
          and all(b['g']['even'] and abs(b['g']['ux'] - b['g']['uy']) < 0.05 and abs(b['g']['ux'] / CM - 1) < 0.01 for b in bs), str(dims))
    log('    boards carry no side-length labels (children count cells); P2 calls the first one "6 x 5"')
    for w, h in [(6, 5), (4, 3)]:
        g = greedy(w, h); n, wit = min_squares(w, h)
        log(f'    {w}x{h}: greedy {g} ({len(g)} squares); fewest {n}: {wit}')
    check('P1 6x5 greedy 6, fewest 5', len(greedy(6, 5)) == 6 and min_squares(6, 5)[0] == 5)
    check('P1 4x3 greedy 4, fewest 4', len(greedy(4, 3)) == 4 and min_squares(4, 3)[0] == 4)
    log('Bonus P2: fewest for 6 x 5 and why fewer cannot fit')
    for k in (1, 2, 3, 4):
        check(f'P2 no tiling of 6x5 with {k} squares', not count_tilings_by_size_multiset(6, 5, k))
    log(f'    5-square size multisets that tile 6x5: {sorted(count_tilings_by_size_multiset(6, 5, 5))}')
    check('P2 text names the 6 x 5 rectangle', text_has(band, 1, 'fewest number of squares for the 6 x 5 rectangle'))

    log('Bonus P3 (p2): only 2x2 and 3x3; which of 5x5, 6x5, 7x5 can be filled')
    bs, fg, _ = page_boards(band, 2)
    for b, (w, h) in zip(bs, [(5, 5), (6, 5), (7, 5)]):
        check(f'P3 board {w}x{h} drawn {b["g"]["cols"]}x{b["g"]["rows"]}, caption "{b["below"]}"',
              (b['g']['cols'], b['g']['rows']) == (w, h) and norm(b['below']) == f'{w} x {h}' and b['g']['even'])
    for w, h, want in [(5, 5, False), (6, 5, True), (7, 5, False)]:
        n, wit = min_squares(w, h, {2, 3})
        log(f'    {w}x{h}: tileable={n is not None} {wit}')
        check(f'P3 {w}x{h} tileable is {want}', (n is not None) == want)

    log('Bonus P4 (p3): recipes')
    bs, fg, words = page_boards(band, 3)
    ex = [b for b in bs if not b['dash']]
    sides = sorted(round(b['g']['cols']) for b in ex)
    check('P4 example shows squares 2,2,1,1 in a 5x2 strip (recipe 2,2)',
          sorted((b['g']['cols'], b['g']['rows']) for b in ex) == [(1, 1), (1, 1), (2, 2), (2, 2)]
          and recipe(5, 2) == [2, 2] and greedy(5, 2) == [2, 2, 1, 1])
    ws = [b for b in bs if b['dash']]
    check('P4 three dashed 8x4 work grids at 1 cm', len(ws) == 3 and all((b['g']['cols'], b['g']['rows']) == (8, 4) for b in ws))
    found = {}
    for a in range(1, 40):
        for b in range(1, a + 1):
            found.setdefault(tuple(recipe(a, b)), []).append((a, b))
    for r in [(1, 2), (2, 1, 2), (1, 1, 3)]:
        lst = found.get(r, [])
        fits = [x for x in lst if x[0] <= 8 and x[1] <= 4]
        log(f'    recipe {r}: rectangles up to 39 long {lst[:5]}...; fit 8x4: {fits}; cf value {cf_value(list(r))}')
        check(f'P4 recipe {r} has a rectangle fitting the 8x4 grid, and larger ones exist', fits and len(lst) > 1)


def page_bounds():
    log('=' * 70); log('All bands: every outlined board and work grid lies inside the printable page'); log('=' * 70)
    for band in ('k-1', '2-3', '4-5', 'bonus'):
        for pg in range(1, npages(PDFS[band]) + 1):
            rects, gv, gh = boards(PDFS[band], pg)
            xs = [r['x0'] for r in rects] + [r['x1'] for r in rects] + [v[0] for v in gv]
            ys = [r['yb'] for r in rects] + [r['yt'] for r in rects] + [h[0] for h in gh]
            if xs:
                check(f'{band} p{pg} drawings within 0.4 in of the page edge',
                      min(xs) >= 28.8 and max(xs) <= 612 - 28.8 and min(ys) >= 28.8 and max(ys) <= 792 - 28.8,
                      f'x {min(xs):.0f}-{max(xs):.0f} pt, y {min(ys):.0f}-{max(ys):.0f} pt')


if __name__ == '__main__':
    log('Week 32 student pages, delivered PDFs in ' + str(WEEK.relative_to(ROOT)))
    for band in ('k-1', '2-3', '4-5', 'bonus'):
        log(f'  {band}: {npages(PDFS[band])} pages')
    k1(); g23(); g45(); bonus(); page_bounds()
    log('')
    log(f'{sum(1 for l in OUT if "[PASS]" in l)} passed, {len(FAILS)} failed')
    for f in FAILS:
        log('  FAIL: ' + f)
    text = '\n'.join(OUT) + '\n'
    (Path(__file__).resolve().parent / 'out_check_students32.txt').write_text(text)
    print(text)
