"""Week 32 adult guides: confirm each quoted claim is in the delivered PDF and
recompute it independently.  Writes out_check_guides32.txt."""
import sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common32 import *
from math32 import *

OUT = []
FAILS = []


def log(s=''):
    OUT.append(s)


GUIDE = norm(page_text(PDFS['guide']))
BGUIDE = norm(page_text(PDFS['bonus-guide']))


def claim(src, quote, ok, detail=''):
    text = GUIDE if src == 'base' else BGUIDE
    present = norm(quote) in text
    tag = 'PASS' if present and ok else 'FAIL'
    why = [] if present else ['quote not found']
    if not ok:
        why.append('claim false')
    log(f'  [{tag}] ({src}) "{quote}"' + (f' -- {detail}' if detail else '') + (f'  <{"; ".join(why)}>' if why else ''))
    if tag == 'FAIL':
        FAILS.append(quote)


def s(a, b):
    return ','.join(map(str, greedy(a, b)))


# ======================================================================== base
def base():
    log('=' * 70); log('Base adult guide (week-32-facilitator.pdf)'); log('=' * 70)
    log('Overview')
    bad = [(a, b) for a in range(2, 120) for b in range(1, a) if common_divisors(a, b) != common_divisors(a - b, b)]
    claim('base', 'replacing (a,b) by (a-b,b) preserves the entire set of positive common divisors', not bad, 'all b<a<120')
    claim('base', 'The sum of the positive remaining sides strictly decreases, so the process terminates', True,
          '(a-b)+b = a < a+b whenever b > 0')
    bad = [(a, b) for a in range(1, 61) for b in range(1, 61) if greedy(a, b)[-1] != gcd_brute(a, b)]
    claim('base', 'The last square has side gcd(a,b)', not bad, 'cell simulation, all a,b <= 60')
    bad = [(a, b, t) for a in range(1, 19) for b in range(1, 19) for t in range(1, 19)
           if equal_square_tiles(a, b, t) != (a % t == 0 and b % t == 0)]
    claim('base', 'Identical axis-aligned whole-grid squares of side s tile the original rectangle exactly when s divides both side lengths',
          not bad, 'exhaustive placement search, a,b,s <= 18')
    n6x5 = min_squares(6, 5)[0]
    claim('base', 'It does not claim that this dissection minimizes the number of squares among all possible unequal-square tilings',
          True, f'and it does not: 6x5 greedy uses {len(greedy(6,5))}, fewest is {n6x5}')

    log('K-1 key')
    rows = [((6, 4), '4,2,2', 2), ((8, 4), '4,4', 4), ((7, 4), '4,3,1,1,1', 1), ((8, 5), '5,3,2,1,1', 1),
            ((9, 6), '6,3,3', 3), ((10, 6), '6,4,2,2', 2)]
    for (a, b), lst, last in rows:
        area_ok = sum(int(x) ** 2 for x in lst.split(',')) == a * b
        claim('base', f'{a}x{b} {lst} {last}', s(a, b) == lst and greedy(a, b)[-1] == last and area_ok,
              f'computed {s(a,b)}; areas sum to {a*b}: {area_ok}')
    claim('base', 'P1 ends differently; P2 ends the same; P3 ends differently',
          greedy(6, 4)[-1] != greedy(8, 4)[-1] and greedy(7, 4)[-1] == greedy(8, 5)[-1] and greedy(9, 6)[-1] != greedy(10, 6)[-1])
    claim('base', 'For both 6x4 and 8x6 the largest equal square has side 2. Side 2 tiles by 3x2 and 4x3 arrays respectively',
          max(t for t in range(1, 5) if equal_square_tiles(6, 4, t)) == 2 and max(t for t in range(1, 7) if equal_square_tiles(8, 6, t)) == 2
          and (6 // 2, 4 // 2) == (3, 2) and (8 // 2, 6 // 2) == (4, 3))
    claim('base', 'There are exactly two rectangle shapes using four 3x3 squares, up to turning: 3x12 and 6x6',
          rect_shapes_from_squares(4, 3) == [(3, 12), (6, 6)])
    claim('base', 'Their biggest-square sequences are 3,3,3,3 and 6. The last sides do not match',
          s(3, 12) == '3,3,3,3' and s(6, 6) == '6')
    claim('base', 'the numbers of 3-unit tiles along adjacent edges multiply to 4: only 1x4 and 2x2, up to order',
          sorted((m, 4 // m) for m in range(1, 5) if 4 % m == 0 and m <= 4 // m) == [(1, 4), (2, 2)])
    claim('base', 'compare 12x8 with 12x9, which changes only one side', greedy(12, 8)[-1] == 4 and greedy(12, 9)[-1] == 3,
          'lasts 4 and 3')

    log('Grades 2-3 key')
    claim('base', 'P1. 10x6: 6,4,2,2 (last 2). 8x5: 5,3,2,1,1 (last 1)', s(10, 6) == '6,4,2,2' and s(8, 5) == '5,3,2,1,1')
    claim('base', 'P2. 12x8: 8,4,4 (last 4). 12x9: 9,3,3,3 (last 3)', s(12, 8) == '8,4,4' and s(12, 9) == '9,3,3,3')
    claim('base', 'For 12x8, all allowed equal-square sides are 1,2,4; the largest is 4. For 10x6, the sides are 1,2',
          [t for t in range(1, 13) if equal_square_tiles(12, 8, t)] == [1, 2, 4]
          and [t for t in range(1, 11) if equal_square_tiles(10, 6, t)] == [1, 2])
    claim('base', 'P4. 7x6: 6,1,1,1,1,1,1, last 1. 8x6: 6,2,2,2, last 2. 9x6: 6,3,3, last 3',
          s(7, 6) == '6,1,1,1,1,1,1' and s(8, 6) == '6,2,2,2' and s(9, 6) == '6,3,3')
    claim('base', 'Predict 10x6 ends at 2, not 4: after 6 the remainder is 6x4, which gives 4,2,2', s(10, 6) == '6,4,2,2')
    claim('base', 'For example 10x6 ends at 2 and tiles with 15 equal 2x2 squares', greedy(10, 6)[-1] == 2 and 10 * 6 // 4 == 15
          and equal_square_tiles(10, 6, 2))
    S = [3, 6, 9, 12]
    good = sorted({tuple(sorted((a, b), reverse=True)) for a in S for b in S if greedy(a, b)[-1] == 3})
    claim('base', 'One valid trio: 12x3 gives 3,3,3,3; 9x6 gives 6,3,3; 12x9 gives 9,3,3,3',
          s(12, 3) == '3,3,3,3' and s(9, 6) == '6,3,3' and s(12, 9) == '9,3,3,3')
    claim('base', 'Other choices with gcd 3 and three distinct shorter sides also work', True,
          f'true, but only the 3-first rectangle can vary: all last-3 rectangles are {good}; 9x6 and 12x9 are forced')

    log('Grades 4-5 key P1-5')
    claim('base', 'P2. 15x9: 9,6,3,3, last 3. 14x8: 8,6,2,2,2, last 2', s(15, 9) == '9,6,3,3' and s(14, 8) == '8,6,2,2,2')
    claim('base', 'P3. For 12x8: sides 1,2,4. For 15x9: sides 1,3',
          [t for t in range(1, 16) if equal_square_tiles(15, 9, t)] == [1, 3])
    claim('base', 'Both before the cut (14,8) and after it (6,8), the complete common-divisor list is {1,2}',
          common_divisors(14, 8) == common_divisors(6, 8) == [1, 2])
    claim('base', 'At the end, a square of side g remains and the common divisors are precisely the divisors of g', True)

    log('Grades 4-5 P6 table (parsed from the delivered PDF)')
    lay = page_text(PDFS['guide'], 4, layout=True)
    table = {}
    for L in range(9, 16):
        m = re.search(r'^\s*' + str(L) + r'((?:\s+\d){7})\s*$', lay, re.M)
        if m:
            table[L] = list(map(int, m.group(1).split()))
    ok = len(table) == 7
    mism = []
    for L, vals in table.items():
        for S_, v in zip(range(2, 9), vals):
            if distinct_sizes(L, S_) != v:
                mism.append((L, S_, v, distinct_sizes(L, S_)))
    claim('base', 'The following table checks all allowed rectangles', ok and not mism, f'7 rows parsed: {ok}; mismatches {mism}')
    allc = {(L, S_): distinct_sizes(L, S_) for L in range(9, 16) for S_ in range(2, 9)}
    mx = max(allc.values())
    claim('base', 'The unique winner is 13x8, with square sides 8,5,3,2,1,1: five different sizes',
          [k for k, v in allc.items() if v == mx] == [(13, 8)] and mx == 5 and s(13, 8) == '8,5,3,2,1,1')

    def rec_count(a, b):
        if a < b:
            a, b = b, a
        q, r = divmod(a, b)
        return 1 if r == 0 else 1 + rec_count(b, r)
    bad = [(a, b) for a in range(1, 80) for b in range(1, 80) if rec_count(a, b) != distinct_sizes(a, b)]
    claim('base', 'This recurrence independently verifies every cell and every possible tie', not bad,
          'recurrence = distinct sizes for all a,b < 80')
    claim('base', 'For 13x8 this produces 8 -> 5 -> 3 -> 2 -> 1'.replace('->', '→'), sorted(set(greedy(13, 8)), reverse=True) == [8, 5, 3, 2, 1])
    claim('base', 'For 12x7 it produces 7 → 5 → 2 → 1, four sizes', sorted(set(greedy(12, 7)), reverse=True) == [7, 5, 2, 1])
    claim('base', 'divide the 49 candidates among pairs', len(allc) == 49)

    log('Optional extension')
    claim('base', 'For 10x6, the list 6,4,2,2 becomes 12,8,4,4 for 20x12', s(20, 12) == '12,8,4,4')
    bad = [(a, b, k) for a in range(1, 31) for b in range(1, 31) for k in range(2, 5)
           if greedy(k * a, k * b) != [k * t for t in greedy(a, b)]]
    claim('base', 'Every comparison and subtraction scales by 2, so the pattern and number of pieces stay the same', not bad,
          'scaling by 2..4 multiplies every side, all a,b <= 30')

    log('Materials (counts)')
    ctx = (ROOT / 'worksheet-workflow' / 'context.md').read_text()
    m = re.search(r'The K.1 table has (\w+) kindergartners and (\w+) first graders', ctx)
    words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    k1n = words[m.group(1)] + words[m.group(2)] if m else None
    log(f'    worksheet-workflow/context.md: K-1 table has {k1n} children')
    claim('base', 'provide four 3-by-3 cutouts per child for K P5 (12 cutouts for the current KK1 group)', k1n is not None and 4 * k1n == 12,
          f'4 per child x {k1n} children = {4 * (k1n or 0)}; the route update on p5 says sixteen')
    claim('base', 'sixteen matching 3-by-3 cutouts give each of four children a set; eight suffice for two pairs sharing',
          16 == 4 * 4 and 8 == 2 * 4)


# ======================================================================== bonus
def bonus():
    log('=' * 70); log('Bonus adult guide (week-32-bonus-facilitator.pdf)'); log('=' * 70)
    g65, g43 = greedy(6, 5), greedy(4, 3)
    m65, m43 = min_squares(6, 5)[0], min_squares(4, 3)[0]
    claim('bonus', 'a 6-by-5 rectangle needs at least five squares, and five fit; the familiar biggest-square rule uses six',
          m65 == 5 and len(g65) == 6)
    claim('bonus', 'The contrast 4-by-3 needs four and greedy achieves four', m43 == 4 and len(g43) == 4)
    t55 = min_squares(5, 5, {2, 3})[0]; t65 = min_squares(6, 5, {2, 3})[0]; t75 = min_squares(7, 5, {2, 3})[0]
    claim('bonus', 'a 5-by-5 or 7-by-5 rectangle cannot be tiled with only side-2 and side-3 squares, although its area is a sum of 4s and 9s',
          t55 is None and t75 is None and any(4 * u + 9 * v == 25 for u in range(7) for v in range(3))
          and any(4 * u + 9 * v == 35 for u in range(9) for v in range(4)))
    claim('bonus', 'A 6-by-5 can', t65 is not None)
    # recipes
    bad_ratio = []
    seen = {}
    for a in range(1, 61):
        for b in range(1, a + 1):
            r = tuple(recipe(a, b))
            g = gcd_brute(a, b)
            seen.setdefault(r, set()).add((a // g, b // g))
            if a != b and cf_value(list(r)) != (a // g, b // g):
                bad_ratio.append((a, b, r))
    multi = {r: v for r, v in seen.items() if len(v) > 1}
    claim('bonus', 'determines the long/short ratio by the finite continued fraction', not bad_ratio, 'all b <= a <= 60')
    claim('bonus', 'All whole-grid rectangles with that recipe are integer enlargements of its coprime one', not multi,
          'each recipe has one reduced pair, a,b <= 60')
    claim('bonus', 'A square has recipe [1]', all(recipe(a, a) == [1] for a in range(1, 30))
          and all(recipe(a, b) != [1] for a in range(1, 40) for b in range(1, 40) if a != b))
    claim('bonus', 'For a nonsquare rectangle the final count is at least 2',
          all(recipe(a, b)[-1] >= 2 for a in range(1, 61) for b in range(1, 61) if a != b))

    log('Materials')
    stock = {1: 10, 2: 6, 3: 4, 4: 2, 5: 2}
    tasks = {'P1 6x5 greedy': greedy(6, 5), 'P1 6x5 fewest': [3, 3, 2, 2, 2], 'P1 4x3 greedy': greedy(4, 3),
             'P3 5x5 area set': [3, 2, 2, 2, 2], 'P3 6x5': [3, 3, 2, 2, 2], 'P3 7x5 area set': [3, 3, 3, 2, 2],
             'P4 3x2': greedy(3, 2), 'P4 8x3': greedy(8, 3), 'P4 7x4': greedy(7, 4), 'P4 6x4': greedy(6, 4)}
    short = {k: [(t, v.count(t), stock.get(t, 0)) for t in set(v) if v.count(t) > stock.get(t, 0)] for k, v in tasks.items()}
    claim('bonus', 'Suggested stock: ten side-1, six side-2, four side-3 and two each side-4/5 pieces; reuse between trials',
          not any(short.values()), f'each single task fits the stock; shortages {dict((k,v) for k,v in short.items() if v)}')
    together = greedy(6, 5) + [3, 3, 2, 2, 2] + greedy(4, 3) + greedy(4, 3)
    log(f'    (all four P1 tilings kept at once would need {together.count(1)} side-1 pieces, '
        f'{together.count(3)} side-3; the guide says to reuse between trials and to save drawings)')
    claim('bonus', 'Five sets serve eleven children at three fixed tables, one adult per table; the upper trio rotates roles',
          2 + 2 + 1 == 5 and 4 + 4 + 3 == 11)

    log('P1-2')
    wit = [(0, 0, 3), (3, 0, 3), (0, 3, 2), (2, 3, 2), (4, 3, 2)]
    cells = [(x + i, y + j) for x, y, t in wit for i in range(t) for j in range(t)]
    claim('bonus', 'tiles are (0,0,3),(3,0,3),(0,3,2),(2,3,2),(4,3,2). Their interiors are disjoint and areas total 30',
          len(cells) == len(set(cells)) == 30 and all(0 <= x < 6 and 0 <= y < 5 for x, y in cells))
    claim('bonus', 'greedy uses one side-5 square and five side-1 squares, six pieces', g65 == [5, 1, 1, 1, 1, 1])
    claim('bonus', 'greedy uses one side-3 square plus three side-1 squares, four pieces, and this is optimal',
          g43 == [3, 1, 1, 1] and m43 == 4)
    sq = lambda mx: [t * t for t in range(1, mx + 1)]
    from itertools import combinations_with_replacement as cwr
    claim('bonus', 'One or two positive square areas cannot sum to 12',
          not any(sum(c) == 12 for k in (1, 2) for c in cwr(sq(12), k)))
    three12 = sorted({c for c in cwr(sq(3), 3) if sum(c) == 12})
    claim('bonus', 'The only three-piece area decomposition is 4+4+4', three12 == [(4, 4, 4)], f'{three12} (sides <= 3)')
    claim('bonus', 'Thus three cannot fit', not count_tilings_by_size_multiset(4, 3, 3))
    claim('bonus', 'Tile sides can only be 1-5. One square does not have area 30; no two square areas sum to 30',
          not any(sum(c) == 30 for k in (1, 2) for c in cwr(sq(5), k)))
    d3 = sorted({c for c in cwr(sq(5), 3) if sum(c) == 30}); d4 = sorted({c for c in cwr(sq(5), 4) if sum(c) == 30})
    claim('bonus', 'The only three-square area decomposition is 25+4+1', d3 == [(1, 4, 25)], str(d3))
    claim('bonus', 'The only four-square decomposition is 16+9+4+1', d4 == [(1, 4, 9, 16)], str(d4))
    claim('bonus', 'their side sum 7 exceeds both board dimensions 6 and 5', not can_pack(6, 5, [(5, 5), (2, 2)])
          and not can_pack(6, 5, [(4, 4), (3, 3)]))
    claim('bonus', 'so the optimum is exactly five', m65 == 5)

    log('P3')
    claim('bonus', 'Area 25=4u+9v forces four side-2 squares and one side-3 square',
          [(u, v) for u in range(7) for v in range(3) if 4 * u + 9 * v == 25] == [(4, 1)])
    claim('bonus', 'Area 35=4u+9v forces two side-2 and three side-3 squares',
          [(u, v) for u in range(9) for v in range(4) if 4 * u + 9 * v == 35] == [(2, 3)])
    claim('bonus', '6-by-5: possible by two side-3 and three side-2 squares', (3, 3, 2, 2, 2) in count_tilings_by_size_multiset(6, 5, 5, {2, 3}))
    claim('bonus', 'Three horizontal intervals of length 3 need width at least 9, exceeding 7', not can_pack(7, 5, [(3, 3)] * 3))
    mx3 = {w: max(k for k in range(0, 6) if can_pack(w, 5, [(3, 3)] * k)) for w in range(3, 13)}
    claim('bonus', 'A strip of height 5 admits at most floor(width/3) side-3 squares', all(mx3[w] == w // 3 for w in mx3), str(mx3))

    log('P4')
    claim('bonus', 'Recipe 1,2: smallest whole-grid rectangle 3-by-2, square sizes 2,1,1', recipe(3, 2) == [1, 2] and s(3, 2) == '2,1,1')
    claim('bonus', 'Recipe 2,1,2: 8-by-3, sizes 3,3,2,1,1', recipe(8, 3) == [2, 1, 2] and s(8, 3) == '3,3,2,1,1')
    claim('bonus', 'Recipe 1,1,3: 7-by-4, sizes 4,3,1,1,1', recipe(7, 4) == [1, 1, 3] and s(7, 4) == '4,3,1,1,1')
    smallest = {}
    for a in range(1, 40):
        for b in range(1, a + 1):
            smallest.setdefault(tuple(recipe(a, b)), (a, b))
    claim('bonus', 'All fit as subrectangles in the supplied 8-by-4 work grids',
          all(smallest[r][0] <= 8 and smallest[r][1] <= 4 for r in [(1, 2), (2, 1, 2), (1, 1, 3)]),
          f'smallest: {[smallest[r] for r in [(1,2),(2,1,2),(1,1,3)]]}')
    claim('bonus', '6-by-4 has recipe 1,2; 16-by-6 has 2,1,2; 14-by-8 has 1,1,3',
          recipe(6, 4) == [1, 2] and recipe(16, 6) == [2, 1, 2] and recipe(14, 8) == [1, 1, 3])
    claim('bonus', 'For 2,1,2 this gives 2-by-1, then 3-by-2, then 8-by-3', rebuild_from_recipe([2, 1, 2]) == [(2, 1), (3, 2), (8, 3)])
    okrb = all(recipe(*rebuild_from_recipe(list(r))[-1]) == list(r) for r in seen if r != (1,))
    claim('bonus', 'attach q squares of side s beside that remainder. Repeat backward', okrb, 'rebuild then greedy returns the recipe, every recipe seen')
    claim('bonus', 'the last square size suffices', True, 'side lengths = last size x reduced pair')


if __name__ == '__main__':
    base(); bonus()
    log('')
    log(f'{sum(1 for l in OUT if "[PASS]" in l)} passed, {len(FAILS)} failed')
    for f in FAILS:
        log('  FAIL: ' + f)
    text = '\n'.join(OUT) + '\n'
    (Path(__file__).resolve().parent / 'out_check_guides32.txt').write_text(text)
    print(text)
