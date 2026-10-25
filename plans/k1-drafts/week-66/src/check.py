"""Verify every count the K-1 pages rely on (run: python3 check.py)."""
from lamps import DIST, DIST_BIG, formula, words_exact, wrong_order, T
from problems import *

def few(t):
    s = T(*t)
    assert DIST[s] == DIST_BIG[s] == formula(*t)
    return DIST[s]

for (lit, w), d in DIST.items():
    assert d == formula(lit, w) == DIST_BIG[(lit, w)]
print('walk formula = BFS on all', len(DIST), 'seven-lamp targets (and on a 13-lamp street)')

for name, lst in (('P1', P1), ('P2', P2), ('P3', P3), ('P4', P4), ('P5', P5)):
    for t in lst:
        f = few(t)
        ws = words_exact(t[0], t[1], f)
        extra = ''
        if t[0] and min(t[0]) < 0 < max(t[0]):
            extra = f'  first-end split {wrong_order(t[0], t[1])}'
        print(f'{name} lit={list(t[0])} w={t[1]}: {f}  ways={len(ws)} {ws}{extra}')

for name, top, nb in (('P6', P6_TOP, P6), ('P7', P7_TOP, P7)):
    print(f'{name} top lit={list(top[0])} w={top[1]}: {few(top)}  ways={len(words_exact(top[0], top[1], few(top)))}')
    for m, t in nb:
        print(f'   {m} -> lit={list(t[0])} w={t[1]}: {few(t)}  {words_exact(t[0], t[1], few(t))[:3]}')

for t, towers in P8:
    res = {n: len(words_exact(t[0], t[1], n)) for n in towers}
    print(f'P8 lit={list(t[0])} w={t[1]}: fewest {few(t)}; words of each exact length {res}')

# collisions with the older shared packet and launch (and mirror images)
older = [((1,), 1), ((-1, 1), 1), ((0, 2), 0), ((-2, 0, 2), -2), ((-2, 0, 2), 0), ((-2, 0, 2), 2),
         ((-1, 0, 1), 0), ((-1, 0, 1), -1), ((-1, 0, 1), 1), ((-1, 1), 0), ((-1,), 0), ((-1,), -1)]
def mirror(t):
    return (tuple(sorted(-x for x in t[0])), -t[1])
avoid = set(older) | {mirror(t) for t in older}
EXAMPLE_P5 = ((0,), 1)   # Problem 5 notation example: flip, then step right
mine = [EXAMPLE_P5] + P1 + P2 + P3 + P4 + P5 + [P6_TOP, P7_TOP] + [t for _, t in P6 + P7] + [t for t, _ in P8]
mine = [(tuple(sorted(l)), w) for l, w in mine]
clash = [t for t in mine if t in avoid]
print('pictures that repeat an older/launch target or its mirror:', clash)
dups = sorted({t for t in mine if mine.count(t) > 1})
print('pictures used more than once in this packet:', dups)
assert all(max([abs(x) for x in l] + [abs(w)]) <= 3 for l, w in mine)

# record space: 12 squares under each picture, 8 squares in each Problem 5 row
from pages import SQ_COLS, SQ_ROWS, ROW_N, ROW_LINES
assert max(few(t) for t in P1 + P2 + P3 + P4 + [P6_TOP, P7_TOP] + [t for _, t in P6 + P7]) <= SQ_COLS * SQ_ROWS
assert max(few(t) for t in P5) <= ROW_N
assert all(len(words_exact(t[0], t[1], few(t))) <= ROW_LINES for t in P5)
assert few(EXAMPLE_P5) == 2 and 'FR' in words_exact(*EXAMPLE_P5, 2)
print('record space fits; Problem 5 example is FR, fewest 2')
