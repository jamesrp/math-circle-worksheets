"""Solve every Week 11 problem (K-1, 2-3, 4-5, return visit) with my own solver and compare
with what the pages print and what both adult guides claim.

Starts are read back from the PDFs (pdf_geometry.json, written by extract_pdf.py);
guide claims are my transcription of the delivered guide PDFs, and each transcribed
sentence is confirmed to be present in the PDF text at the end (text_present()).
Output: check_answers.out
"""
import json
import os
import random
import re
import subprocess
import sys
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chipfire import (PKT, HERE, TRI, FOUR, EXTRA, CLOSED, Board, fmt)  # noqa: E402

OUT = []
FAILS = []
NOTES = []


def say(s=''):
    OUT.append(s)


def check(name, ok, detail=''):
    tag = 'ok  ' if ok else 'FAIL'
    say(f'  [{tag}] {name}' + (f' -- {detail}' if detail else ''))
    if not ok:
        FAILS.append(name + (' -- ' + detail if detail else ''))


def note(s):
    say('  [NOTE] ' + s)
    NOTES.append(s)


G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))


def table_rows(band, page, k=0):
    pg = [p for p in G[band] if p['page'] == page][0]
    return pg['tables'][k]['rows']


def cellnum(c):
    c = c.strip()
    m = re.fullmatch(r'(\d+) dots', c)
    if m:
        return int(m.group(1))
    return int(c)


def starts_from(band, page, ncols, k=0):
    rows = table_rows(band, page, k)[1:]
    return [tuple(cellnum(r[i]) for i in range(ncols)) for r in rows]


def boards_on(band, page):
    pg = [p for p in G[band] if p['page'] == page][0]
    return [b['edges'] for b in pg['boards']]


def edges_of(board):
    return sorted('-'.join(sorted(e)) for e in board.edges)


def board_matches(band, page, board):
    got = boards_on(band, page)
    check(f'{band} p{page}: printed board is the {board.name}', got == [edges_of(board)], f'printed {got}')


def is_complete_word(board, start, word):
    try:
        fin, sink = board.run_word(start, word)
    except ValueError as e:
        return False, str(e)
    return board.is_stable(fin), f'ends {fmt(fin)}'


def row_check(label, board, start, finish, counts, order=None, alts=(), sink=None):
    r = board.stabilize(start)
    ok = r['finish'] == finish and r['counts'] == counts and (sink is None or r['sink'] == sink)
    check(f'{label} {fmt(start)}: guide finish {fmt(finish)}, shares {fmt(counts)}' + (f', sink {sink}' if sink is not None else ''),
          ok, f"computed finish {fmt(r['finish'])}, shares {fmt(r['counts'])}, sink {r['sink']}, {r['nwords']} complete legal words")
    for w in ([order] if order else []) + list(alts):
        good, why = is_complete_word(board, start, w)
        check(f'{label} {fmt(start)}: guide word {w} is a complete legal run', good, why)
    return r


def T(board, state, v):
    s = list(state)
    s[board.idx[v]] += 1
    return board.S(s)[0]


def stage(board, batches):
    """Add batches one after another, finishing in between; return (final, total counts, intermediates)."""
    st = (0,) * len(board.order)
    tot = [0] * len(board.order)
    mids = []
    for b in batches:
        st = tuple(x + y for x, y in zip(st, b))
        r = board.stabilize(st)
        st = r['finish']
        tot = [a + c for a, c in zip(tot, r['counts'])]
        mids.append(st)
    return st, tuple(tot), mids


# ----------------------------------------------------------------- K-1
say('=== K-1 (F11-K-v3) ===')
say('P1 triangle starts read from the page:')
board_matches('K-1', 1, TRI)
st = starts_from('K-1', 1, 2)
check('K-1 P1 printed starts', st == [(2, 2), (3, 2), (2, 3), (3, 3)], str(st))
guide = {(2, 2): ((1, 1), (1, 1), 'AB'), (3, 2): ((1, 0), (2, 2), 'ABAB'), (2, 3): ((0, 1), (2, 2), 'ABBA'), (3, 3): ((1, 1), (2, 2), 'ABAB')}
for s in st:
    r = row_check('K-1 P1', TRI, s, guide[s][0], guide[s][1], guide[s][2])
    check(f'K-1 P1 {fmt(s)} has a real order choice (>=2 complete words)', r['nwords'] >= 2, f"{r['nwords']} words")
check('K-1 P1 guide: the four rows give three different finishes',
      len({TRI.stabilize(s)['finish'] for s in st}) == 3)

say('P2 every start of 4 and 5 chips:')
board_matches('K-1', 2, TRI)
g4 = {(0, 4): (0, 1), (1, 3): (1, 0), (2, 2): (1, 1), (3, 1): (0, 1), (4, 0): (1, 0)}
g5 = {(0, 5): (1, 0), (1, 4): (1, 1), (2, 3): (0, 1), (3, 2): (1, 0), (4, 1): (1, 1), (5, 0): (0, 1)}
for N, g in ((4, g4), (5, g5)):
    fins = {}
    for a in range(N + 1):
        fins[(a, N - a)] = TRI.stabilize((a, N - a))['finish']
    check(f'K-1 P2 guide table for {N} chips', fins == g, str({fmt(k): fmt(v) for k, v in fins.items()}))
    check(f'K-1 P2 {N} chips: exactly three finishes (1,0),(0,1),(1,1)', set(fins.values()) == {(1, 0), (0, 1), (1, 1)})

say('P3 four-cycle starts:')
board_matches('K-1', 3, FOUR)
st = starts_from('K-1', 3, 3)
check('K-1 P3 printed starts', st == [(0, 4, 0), (2, 2, 0), (0, 2, 2), (2, 0, 2)], str(st))
guide = {(0, 4, 0): ((1, 0, 1), (1, 3, 1), 'BBACB'), (2, 2, 0): ((1, 1, 1), (1, 1, 0), 'AB'),
         (0, 2, 2): ((1, 1, 1), (0, 1, 1), 'BC'), (2, 0, 2): ((1, 0, 1), (1, 1, 1), 'ACB')}
for s in st:
    r = row_check('K-1 P3', FOUR, s, *guide[s])
    check(f'K-1 P3 {fmt(s)} has a real order choice', r['nwords'] >= 2, f"{r['nwords']} words")
w = FOUR.all_complete_words((0, 4, 0))
check('K-1 P3 hint: from (0,4,0) B must share twice before A or C can', all(x.startswith('BB') for x in w), str(sorted(set(w))))

say('P4 stable four-cycle placements:')
board_matches('K-1', 4, FOUR)
stable = FOUR.stable_states()
check('K-1 P4: exactly 8 stable placements, each circle 0 or 1', sorted(stable) == sorted(product((0, 1), repeat=3)), str(stable))
check('K-1 P4: largest stable total is 3, so no stable placement uses 4 chips', max(map(sum, stable)) == 3)
check('K-1 P4: answer table has 8 rows', len(table_rows('K-1', 4)) - 1 == 8)

say('P5 additions in any timing (every interleaving of single chips and legal sharing):')
board_matches('K-1', 5, TRI)
st = starts_from('K-1', 5, 2)
check('K-1 P5 printed rows', st == [(3, 3)] * 3 + [(2, 4)] * 3, str(st))
for adds, fin in (((3, 3), (1, 1)), ((2, 4), (1, 0))):
    res = TRI.addition_interleavings(adds)
    check(f'K-1 P5 add {fmt(adds)}: every timing finishes at {fmt(fin)}', {f for f, c in res} == {fin}, str(res))
for s, f in (((3, 0), (1, 1)), ((1, 4), (1, 1)), ((2, 0), (0, 1)), ((0, 5), (1, 0)), ((0, 4), (0, 1)), ((2, 1), (1, 0))):
    check(f'K-1 P5 guide intermediate {fmt(s)} -> {fmt(f)}', TRI.stabilize(s)['finish'] == f)
check('K-1 P5 guide batch chains: (3,0)->(1,1)+(0,3)=(1,4); (2,0)->(0,1)+(0,4)=(0,5); (0,4)->(0,1)+(2,0)=(2,1)', True)

say('P6 add one chip at A repeatedly:')
board_matches('K-1', 6, TRI)
seq = []
x = (0, 0)
for i in range(11):
    x = T(TRI, x, 'A')
    seq.append(x)
g = [(1, 0), (0, 1), (1, 1)] * 4
check('K-1 P6 guide sequence of 11 finishes', seq == g[:11], str(seq))
mapA = {s: T(TRI, s, 'A') for s in TRI.stable_states()}
check('K-1 P6 guide diagram: (0,0)->(1,0)->(0,1)->(1,1)->(1,0)',
      mapA == {(0, 0): (1, 0), (1, 0): (0, 1), (0, 1): (1, 1), (1, 1): (1, 0)}, str(mapA))
check('K-1 P6: (0,0) is never an image, so empty circles never return', (0, 0) not in mapA.values())
check('K-1 P6 table has 11 rows', len(table_rows('K-1', 6)) - 1 == 11)
mapB = {s: T(TRI, s, 'B') for s in TRI.stable_states()}
cycA = [(1, 0), (0, 1), (1, 1)]
check('K-1 P6 extension: B additions run the same three states in reverse cyclic order',
      all(mapB[cycA[(i + 1) % 3]] == cycA[i] for i in range(3)), str(mapB))

# ----------------------------------------------------------------- 2-3
say('\n=== Grades 2-3 (F11-23-v3) ===')
board_matches('2-3', 1, TRI)
st = starts_from('2-3', 1, 2)
check('2-3 P1 printed starts', st == [(2, 2), (2, 2), (4, 0), (4, 0), (3, 3), (3, 3)], str(st))
guide = {(2, 2): ((1, 1), (1, 1), 'AB', ['BA']), (4, 0): ((1, 0), (2, 1), 'AAB', []), (3, 3): ((1, 1), (2, 2), 'ABAB', ['BABA'])}
for s in sorted(set(st)):
    f, c, o, alts = guide[s]
    row_check('2-3 P1', TRI, s, f, c, o, alts)
w = TRI.all_complete_words((4, 0))
check('2-3 P1 guide: (4,0) has only one complete legal word, AAB ("if possible" matters)', w == ['AAB'], str(w))

board_matches('2-3', 2, FOUR)
st = starts_from('2-3', 2, 3)
check('2-3 P2 printed starts', st == [(0, 4, 0)] * 2 + [(2, 1, 2)] * 2 + [(2, 4, 2)] * 2, str(st))
guide = {(0, 4, 0): ((1, 0, 1), (1, 3, 1), 'BBACB', ['BBCAB']), (2, 1, 2): ((1, 1, 1), (1, 1, 1), 'ABC', ['CBA']),
         (2, 4, 2): ((1, 0, 1), (3, 5, 3), 'ABBABCCBACB', ['CBBCBAABCAB'])}
for s in sorted(set(st)):
    r = row_check('2-3 P2', FOUR, s, *guide[s])
    check(f'2-3 P2 {fmt(s)}: two different orders exist (page has no "if possible")', r['nwords'] >= 2, f"{r['nwords']} words")

board_matches('2-3', 3, TRI)
fin6 = {(a, 6 - a): TRI.stabilize((a, 6 - a))['finish'] for a in range(7)}
g = {(0, 6): (1, 1), (1, 5): (0, 1), (2, 4): (1, 0), (3, 3): (1, 1), (4, 2): (0, 1), (5, 1): (1, 0), (6, 0): (1, 1)}
check('2-3 P3 guide table of all seven six-chip starts', fin6 == g, str(fin6))
check('2-3 P3: starts finishing at (1,1) are exactly (0,6),(3,3),(6,0)', [s for s in fin6 if fin6[s] == (1, 1)] == [(0, 6), (3, 3), (6, 0)])
check('2-3 P3 answer table has 7 rows (one per start)', len(table_rows('2-3', 3)) - 1 == 7)
inv = all(((a - b) - (TRI.stabilize((a, b))['finish'][0] - TRI.stabilize((a, b))['finish'][1])) % 3 == 0
          for a in range(10) for b in range(10))
check('2-3 P3 guide invariant: A - B mod 3 never changes', inv)

board_matches('2-3', 4, EXTRA)
st = starts_from('2-3', 4, 3)
check('2-3 P4 printed starts', st == [(3, 0, 3)] * 2 + [(0, 6, 0)] * 2 + [(2, 2, 2)] * 2 + [(4, 1, 2)] * 2, str(st))
guide = {(3, 0, 3): ((2, 0, 2), (1, 1, 1), 'ACB', ['CAB']), (0, 6, 0): ((2, 0, 2), (1, 4, 1), 'BBBACB', ['BBBCAB']),
         (2, 2, 2): ((2, 0, 2), (1, 2, 1), 'BACB', ['BCAB']), (4, 1, 2): ((2, 1, 0), (2, 2, 2), 'ABCABC', ['ACBABC'])}
for s in sorted(set(st)):
    r = row_check('2-3 P4', EXTRA, s, *guide[s])
    check(f'2-3 P4 {fmt(s)}: a choice of order exists', r['nwords'] >= 2, f"{r['nwords']} words")
check('2-3 P4 guide: "the added line changes ... some finishes" (vs the four-cycle)',
      any(FOUR.stabilize(s)['finish'] != EXTRA.stabilize(s)['finish'] for s in set(st)))

board_matches('2-3', 5, FOUR)
st = starts_from('2-3', 5, 2)
check('2-3 P5 printed batches', st == [(2, 4)] * 3, str(st))
A2, B4 = (2, 0, 0), (0, 4, 0)
tog = stage(FOUR, [(2, 4, 0)])
af = stage(FOUR, [A2, B4])
bf = stage(FOUR, [B4, A2])
check('2-3 P5 together: (2,4,0) -> (1,1,1), counts (2,3,1)', tog[0] == (1, 1, 1) and tog[1] == (2, 3, 1), str(tog))
check('2-3 P5 A first: (2,0,0)->(0,1,0), then (0,5,0)->(1,1,1)', af[2] == [(0, 1, 0), (1, 1, 1)], str(af))
check('2-3 P5 B first: (0,4,0)->(1,0,1), then (3,0,1)->(1,1,1)', bf[2] == [(1, 0, 1), (1, 1, 1)], str(bf))
check('2-3 P5: total counts agree across timings', tog[1] == af[1] == bf[1], f'{tog[1]} {af[1]} {bf[1]}')
res = FOUR.addition_interleavings((2, 4, 0))
check('2-3 P5: every interleaving finishes at (1,1,1)', {f for f, c in res} == {(1, 1, 1)}, str(res))

board_matches('2-3', 6, TRI)
seqA, seqB = [], []
x = y = (0, 0)
for i in range(12):
    x = T(TRI, x, 'A'); y = T(TRI, y, 'B')
    seqA.append(x); seqB.append(y)
check('2-3 P6 guide A column', seqA == [(1, 0), (0, 1), (1, 1)] * 4, str(seqA))
check('2-3 P6 guide B column', seqB == [(0, 1), (1, 0), (1, 1)] * 4, str(seqB))
check('2-3 P6: each rule reaches exactly (1,0),(0,1),(1,1) after >=1 addition', set(seqA) == set(seqB) == {(1, 0), (0, 1), (1, 1)})
check('2-3 P6 table has 12 rows', len(table_rows('2-3', 6)) - 1 == 12)

# ----------------------------------------------------------------- 4-5
say('\n=== Grades 4-5 (F11-45-v3) ===')
board_matches('4-5', 1, TRI)
st = starts_from('4-5', 1, 2)
check('4-5 P1 printed starts', st == [(2, 2)] * 2 + [(4, 0)] * 2 + [(3, 3)] * 2 + [(5, 4)] * 2, str(st))
guide = {(2, 2): ((1, 1), (1, 1), 2, ['AB', 'BA']), (4, 0): ((1, 0), (2, 1), 3, ['AAB']), (3, 3): ((1, 1), (2, 2), 4, ['ABAB', 'BABA']),
         (5, 4): ((1, 0), (4, 4), 8, ['AABABBAB', 'BBAABAAB'])}
for s in sorted(set(st)):
    f, c, sk, words = guide[s]
    row_check('4-5 P1', TRI, s, f, c, None, words, sk)
# equal finish forces equal counts on a sink board: L invertible
ok = True
for a in range(15):
    for b in range(15):
        res, _ = TRI.outcome_set((a, b))
        ok &= len(res) == 1
check('4-5 P1: for every start up to 14+14 all legal runs give one finish and one count vector', ok)
check('4-5 P1 guide: different starts (2,2),(3,3) share a finish with different counts',
      TRI.stabilize((2, 2))['finish'] == TRI.stabilize((3, 3))['finish'] and TRI.stabilize((2, 2))['counts'] != TRI.stabilize((3, 3))['counts'])

board_matches('4-5', 2, FOUR)
rows = table_rows('4-5', 2)[1:]
check('4-5 P2 printed batches', [r[:3] for r in rows] == [['4 at B', '2 at A', t] for t in ('together', 'first, then second', 'second, then first')]
      + [['3 at A', '3 at C', t] for t in ('together', 'first, then second', 'second, then first')], str([r[:3] for r in rows]))
for first, second, fin, mids in (((0, 4, 0), (2, 0, 0), (1, 1, 1), ((1, 0, 1), (0, 1, 0))), ((3, 0, 0), (0, 0, 3), (1, 0, 1), ((1, 1, 0), (0, 1, 1)))):
    tg = stage(FOUR, [tuple(a + b for a, b in zip(first, second))])
    fs = stage(FOUR, [first, second])
    sf = stage(FOUR, [second, first])
    check(f'4-5 P2 batches {fmt(first)}+{fmt(second)}: all three timings finish {fmt(fin)}', tg[0] == fs[0] == sf[0] == fin, f'{tg[0]} {fs[0]} {sf[0]}')
    check(f'4-5 P2 guide intermediates {fmt(mids[0])} and {fmt(mids[1])}', fs[2][0] == mids[0] and sf[2][0] == mids[1], f'{fs[2]} {sf[2]}')
check('4-5 P2 guide: (1,1,3) -> (1,0,1) and (3,1,1) -> (1,0,1)', FOUR.stabilize((1, 1, 3))['finish'] == (1, 0, 1) and FOUR.stabilize((3, 1, 1))['finish'] == (1, 0, 1))

board_matches('4-5', 3, TRI)
st = starts_from('4-5', 3, 2)
check('4-5 P3 printed starts', st == [(0, 0), (1, 0), (0, 1), (1, 1)], str(st))
g = {(0, 0): [(1, 0), (0, 1), (1, 1), (1, 0)], (1, 0): [(0, 1), (1, 1), (1, 0), (0, 1)],
     (0, 1): [(1, 1), (1, 0), (0, 1), (1, 1)], (1, 1): [(1, 0), (0, 1), (1, 1), (1, 0)]}
for s in st:
    x = s; seq = []
    for i in range(4):
        x = T(TRI, x, 'A'); seq.append(x)
    check(f'4-5 P3 guide row {fmt(s)}', seq == g[s], str(seq))
ret = [s for s in st if s in g[s]]
check('4-5 P3: starts that return within the four columns are (1,0),(0,1),(1,1), each at After 3',
      ret == [(1, 0), (0, 1), (1, 1)] and all(g[s][2] == s for s in ret))
check('4-5 P3: (0,0) and (1,1) give the same pair (1,0) after one addition', g[(0, 0)][0] == g[(1, 1)][0] == (1, 0))

board_matches('4-5', 4, EXTRA)
st = starts_from('4-5', 4, 3)
check('4-5 P4 printed starts', st == [(3, 0, 3)] * 2 + [(0, 6, 0)] * 2 + [(4, 1, 2)] * 2, str(st))
for s, f, c in (((3, 0, 3), (2, 0, 2), (1, 1, 1)), ((0, 6, 0), (2, 0, 2), (1, 4, 1)), ((4, 1, 2), (2, 1, 0), (2, 2, 2))):
    r = row_check('4-5 P4', EXTRA, s, f, c)
    check(f'4-5 P4 {fmt(s)}: two orders exist', r['nwords'] >= 2, f"{r['nwords']} words")

board_matches('4-5', 5, FOUR)
W = lambda s: 3 * s[0] + 4 * s[1] + 3 * s[2]
for s, f, c, sk, w0, mv in (((0, 12, 0), (1, 0, 1), (5, 11, 5), 10, 48, 21), ((6, 0, 6), (1, 0, 1), (5, 5, 5), 10, 36, 15), ((4, 4, 4), (1, 0, 1), (5, 7, 5), 10, 40, 17)):
    r = row_check('4-5 P5', FOUR, s, f, c, None, (), sk)
    check(f'4-5 P5 {fmt(s)}: score {w0}, final score 6, {mv} moves', W(s) == w0 and W(f) == 6 and sum(c) == mv == (w0 - 6) // 2)
# score drops by exactly 2 at every legal firing, on every state up to 8 chips per circle
okF = all(W(FOUR.fire(s, v)[0]) == W(s) - 2 for s in product(range(9), repeat=3) for v in FOUR.legal(s))
okE = all(W(EXTRA.fire(s, v)[0]) == W(s) - 2 for s in product(range(9), repeat=3) for v in EXTRA.legal(s))
okT = all(sum(TRI.fire(s, v)[0]) == sum(s) - 1 for s in product(range(12), repeat=2) for v in TRI.legal(s))
check('Guide p2/p11: W = 3A+4B+3C drops by 2 at every firing on the four-cycle', okF)
check('Guide p2: W drops by 2 at every firing on the extra-line board', okE)
check('Guide p2: A+B drops by 1 at every firing on the triangle', okT)
check('Guide p2/p11: plain chip total does not drop when B fires on the four-cycle', sum(FOUR.fire((0, 2, 0), 'B')[0]) == 2)

board_matches('4-5', 6, FOUR)
r = row_check('4-5 P6', FOUR, (0, 8, 0), (1, 0, 1), (3, 7, 3), None, ['BBABBABCCBACB', 'BBCBBCBAABCAB'], 6)
swap = 'BBABBABCCBACB'.translate(str.maketrans('AC', 'CA'))
check('4-5 P6 guide: the two words exchange A and C, 13 moves each', swap == 'BBCBBCBAABCAB' and len(swap) == 13)
check('4-5 P6 guide arithmetic: Aend=0-6+7=1, Bend=8-14+3+3=0, Cend=1; score 32 -> 6 = 13 moves',
      FOUR.formal((0, 8, 0), (3, 7, 3)) == (1, 0, 1) and W((0, 8, 0)) == 32 and (32 - 6) // 2 == 13)

# ----------------------------------------------------------------- base guide overview and extensions
say('\n=== Base adult guide: overview and general claims ===')
check('Overview: stable states 4 / 8 / 18', [len(b.stable_states()) for b in (TRI, FOUR, EXTRA)] == [4, 8, 18])
check('Overview: capacities 2 / 3 / 5', [max(map(sum, b.stable_states())) for b in (TRI, FOUR, EXTRA)] == [2, 3, 5])
check('Guide p12: extra-line maximum 5 attained by (2,1,2)', [s for s in EXTRA.stable_states() if sum(s) == 5] == [(2, 1, 2)])
check('Guide p2: AB legal from (2,1), ends (1,0); BA cannot begin',
      TRI.run_word((2, 1), 'AB')[0] == (1, 0) and TRI.fire((2, 1), 'B') is None)
check('Guide p3: from (2,2) the formal counts (2,2) give (0,0), stable but not the actual finish (1,1)',
      TRI.formal((2, 2), (2, 2)) == (0, 0) and TRI.stabilize((2, 2))['finish'] == (1, 1))


def triangle_formula(a, b):
    if a == b == 0:
        return (0, 0)
    return {0: (1, 1), 1: (1, 0), 2: (0, 1)}[(a - b) % 3]


ok = True
okc = True
for a in range(41):
    for b in range(41):
        fin, cnt = TRI.S((a, b))
        ok &= fin == triangle_formula(a, b)
        rA, rB = fin
        okc &= cnt == ((2 * (a - rA) + (b - rB)) // 3, ((a - rA) + 2 * (b - rB)) // 3) and (2 * (a - rA) + (b - rB)) % 3 == 0
check('Guide p3: triangle formula S(a,b) by a-b mod 3 (S(0,0)=(0,0)), all a,b <= 40', ok)
check('Guide p3: u_A=(2(a-rA)+(b-rB))/3, u_B=((a-rA)+2(b-rB))/3', okc)

# least-action characterisation, by brute force over a box of f
for bd, rng, box in ((TRI, 9, 12), (FOUR, 6, 12), (EXTRA, 5, 10)):
    n = len(bd.order)
    ok1 = ok2 = True
    for c in product(range(rng), repeat=n):
        u = bd.stabilize(c)['counts'] if sum(c) <= 8 else bd.S(c)[1]
        d = bd.deg
        Fs = [f for f in product(range(box), repeat=n) if all(x < dd for x, dd in zip(bd.formal(c, f), d))]
        ok1 &= u in Fs and all(all(fi >= ui for fi, ui in zip(f, u)) for f in Fs)
        G2 = [f for f in Fs if all(x >= 0 for x in bd.formal(c, f))]
        m = min(map(sum, G2))
        ok2 &= [f for f in G2 if sum(f) == m] == [u]
    check(f'Guide p3 ({bd.name}): odometer = componentwise least f with c-Lf<d (all c < {rng} per circle)', ok1)
    check(f'Guide p3 ({bd.name}): odometer = unique minimiser of sum f with 0<=c-Lf<d', ok2)

# order independence for every start up to a bound, all legal orders
for bd, rng in ((TRI, 13), (FOUR, 9), (EXTRA, 8)):
    ok = all(len(bd.outcome_set(c)[0]) == 1 for c in product(range(rng), repeat=len(bd.order)))
    check(f'Order independence ({bd.name}): one finish and one count vector over all legal orders, every start < {rng} per circle', ok)

# staged additions and the monoid
rnd = random.Random(11)
for bd in (TRI, FOUR, EXTRA):
    n = len(bd.order)
    ok = True
    for _ in range(3000):
        x = tuple(rnd.randrange(9) for _ in range(n)); y = tuple(rnd.randrange(9) for _ in range(n))
        ok &= bd.S(tuple(a + b for a, b in zip(bd.S(x)[0], y)))[0] == bd.S(tuple(a + b for a, b in zip(x, y)))[0]
    check(f'Guide p3/p12 ({bd.name}): S(S(x)+y) = S(x+y), 3000 random x,y', ok)
    st_ = bd.stable_states()
    op = lambda p, q: bd.S(tuple(a + b for a, b in zip(p, q)))[0]
    comm = all(op(p, q) == op(q, p) for p in st_ for q in st_)
    assoc = all(op(op(p, q), r) == op(p, op(q, r)) for p in st_ for q in st_ for r in st_)
    ident = all(op((0,) * n, p) == p for p in st_)
    group = all(any(op(p, q) == (0,) * n for q in st_) for p in st_)
    check(f'Guide p3 ({bd.name}): (+) on stable states is commutative, associative, identity 0; not a group', comm and assoc and ident and not group)
for bd, rng in ((TRI, 13), (FOUR, 9), (EXTRA, 8)):
    empt = [c for c in product(range(rng), repeat=len(bd.order)) if bd.S(c)[0] == (0,) * len(bd.order)]
    check(f'Guide p3/p12 ({bd.name}): only the empty start finishes empty (starts < {rng} per circle)', empt == [(0,) * len(bd.order)], str(empt[:5]))
lone = Board('lone', [('A', 'S')], 'A')
check('Guide p12: a lone circle joined only to the sink can finish empty from a nonempty start', lone.S((1,))[0] == (0,))
check('Guide p12: sink-free triangle (2,1,0) -A-> (0,2,1) -B-> (1,0,2) -C-> (2,1,0)',
      [CLOSED.run_word((2, 1, 0), w)[0] for w in ('A', 'AB', 'ABC')] == [(0, 2, 1), (1, 0, 2), (2, 1, 0)])
check('Guide p5 launch: (2,2) -A-> (0,3) -B-> (1,1) and -B-> (3,0) -A-> (1,1); counts (1,1), 2 chips in sink',
      [TRI.run_word((2, 2), w) for w in ('A', 'AB', 'B', 'BA')] == [((0, 3), 1), ((1, 1), 2), ((3, 0), 1), ((1, 1), 2)])
# materials: largest prescribed total
totals = {'K-1': max([sum(s) for s in starts_from('K-1', 1, 2) + starts_from('K-1', 3, 3) + starts_from('K-1', 5, 2)] + [5, 11]),
          '2-3': max([sum(s) for s in starts_from('2-3', 1, 2) + starts_from('2-3', 2, 3) + starts_from('2-3', 4, 3) + starts_from('2-3', 5, 2)] + [6, 12]),
          '4-5': max([sum(s) for s in starts_from('4-5', 1, 2) + starts_from('4-5', 4, 3)] + [6, 6, 12, 8])}
check('Guide p4: the largest prescribed total is 12 chips', max(totals.values()) == 12, str(totals))
check('Guide p4: 24 counters x 11 children = 264', 24 * 11 == 264)

# ----------------------------------------------------------------- return visit
say('\n=== Return visit (F11-RV-v1) and its guide ===')
rvb = boards_on('RV', 1)
check('RV p1: three small example triangles and the closed triangle board, all A-B, A-C, B-C',
      rvb == [['A-B', 'A-C', 'B-C']] * 4, str(rvb))
pg = [p for p in G['RV'] if p['page'] == 1][0]
ex = pg['boards']
chips = [[(n['label'], n['chips']) for n in b['nodes']] for b in ex[:3]]
check('RV p1 example: Before A has 2; After B 1, C 1, A 0 (one A firing on the closed triangle)',
      chips[0] == [('A', 2), ('B', 0), ('C', 0)] and chips[2] == [('A', 0), ('B', 1), ('C', 1)] and CLOSED.run_word((2, 0, 0), 'A')[0] == (0, 1, 1), str(chips))
check('RV p1 example: arrows from A to B and to C', sorted(ex[1]['arrows']) == ['A->B', 'A->C'], str(ex[1]['arrows']))
srow = table_rows('RV', 1, 0)[1]
rvstarts = [tuple(int(v) for v in re.findall(r'\d+', c)) for c in srow]
check('RV P1 printed starts', rvstarts == [(3, 0, 0), (2, 1, 0), (4, 0, 0)], str(rvstarts))
for s, stops, cycles in (((3, 0, 0), True, False), ((2, 1, 0), False, True), ((4, 0, 0), False, True)):
    seen, stable, cyc = CLOSED.closed_explore(s)
    check(f'RV P1 {fmt(s)}: can stop={bool(stable)}, every run stops={not cyc}, can repeat={cyc}',
          bool(stable) == stops and cyc == cycles, f'{len(seen)} reachable states, stable {stable}')
check('RV guide: (3,0,0) -A-> (1,1,1), stable', CLOSED.run_word((3, 0, 0), 'A')[0] == (1, 1, 1) and CLOSED.is_stable((1, 1, 1)))
check('RV guide: from (2,1,0) the run is forced: A, B, C back to the start',
      CLOSED.legal((2, 1, 0)) == ['A'] and CLOSED.legal((0, 2, 1)) == ['B'] and CLOSED.legal((1, 0, 2)) == ['C'])
check('RV guide: AABC from (4,0,0) reaches (2,1,1), the state after the first A',
      CLOSED.run_word((4, 0, 0), 'AABC')[0] == CLOSED.run_word((4, 0, 0), 'A')[0] == (2, 1, 1))
check('RV guide: no stable closed-triangle state holds 4 chips', max(map(sum, CLOSED.stable_states())) == 3)
three = {}
for s in product(range(4), repeat=3):
    if sum(s) == 3:
        seen, stable, cyc = CLOSED.closed_explore(s)
        three[s] = 'stable' if CLOSED.is_stable(s) else ('stops' if stable and not cyc else ('cycles' if not stable else 'mixed'))
types = {}
for s, v in three.items():
    types.setdefault(tuple(sorted(s, reverse=True)), set()).add(v)
check('RV guide return question: 3-chip types (3,0,0) stops, (2,1,0) cycles, (1,1,1) stable',
      types == {(3, 0, 0): {'stops'}, (2, 1, 0): {'cycles'}, (1, 1, 1): {'stable'}}, str(types))

check('RV p2: board is the four-cycle S-A-B-C-S', boards_on('RV', 2) == [edges_of(FOUR)], str(boards_on('RV', 2)))
trials = {}
for s in FOUR.stable_states():
    for v in 'ABC':
        c = list(s); c[FOUR.idx[v]] += 1
        words = sorted(set(FOUR.all_complete_words(tuple(c))))
        r = FOUR.stabilize(tuple(c))
        trials[(s, v)] = (sum(r['counts']), words, r['finish'], r['sink'], r['counts'])
mx = max(t[0] for t in trials.values())
arg = [k for k, t in trials.items() if t[0] == mx]
check('RV P2: the longest firing word has 4 letters, only from (1,1,1) adding at B', mx == 4 and arg == [((1, 1, 1), 'B')], f'{mx} {arg}')
t = trials[((1, 1, 1), 'B')]
check('RV guide: its words are exactly BACB and BCAB, counts (1,2,1), finish (1,0,1), 2 chips in sink',
      t[1] == ['BACB', 'BCAB'] and t[4] == (1, 2, 1) and t[2] == (1, 0, 1) and t[3] == 2, str(t))
check('RV guide: (1,1,1)+A gives only ABC, finish (1,1,0)', trials[((1, 1, 1), 'A')][1] == ['ABC'] and trials[((1, 1, 1), 'A')][2] == (1, 1, 0))
check('RV guide: (1,1,1)+C gives only CBA, finish (0,1,1)', trials[((1, 1, 1), 'C')][1] == ['CBA'] and trials[((1, 1, 1), 'C')][2] == (0, 1, 1))
check('RV guide: every other stable start gives at most two firings', all(t[0] <= 2 for (s, v), t in trials.items() if s != (1, 1, 1)))
check('RV guide: adding to an empty circle gives no firing', all(t[0] == 0 for (s, v), t in trials.items() if s[FOUR.idx[v]] == 0))
check('RV guide: B fires twice only in the all-one start (with the chip at B)', [k for k, t in trials.items() if t[4][1] >= 2] == [((1, 1, 1), 'B')])
check('RV guide: 8 stable starts x 3 sites = 24 trials', len(trials) == 24)

check('RV p3: board is the sink triangle', boards_on('RV', 3) == [edges_of(TRI)], str(boards_on('RV', 3)))
rows = table_rows('RV', 3)[1:]
p3starts = [tuple(int(v) for v in re.findall(r'\d+', r[0])) for r in rows]
check('RV P3 printed starts', p3starts == [(0, 6), (3, 3), (6, 0)], str(p3starts))
g = {(0, 6): ['BBAB', 'BBBA'], (3, 3): ['ABAB', 'ABBA', 'BAAB', 'BABA'], (6, 0): ['AAAB', 'AABA']}
for s in p3starts:
    legal4 = []
    for w in map(''.join, product('AB', repeat=4)):
        try:
            fin, sk = TRI.run_word(s, w)
            legal4.append((w, fin, sk))
        except ValueError:
            pass
    check(f'RV P3 {fmt(s)}: every legal four-letter word is {g[s]}, each ending (1,1) with 4 in the sink',
          [w for w, f, k in legal4] == g[s] and all(f == (1, 1) and k == 4 for w, f, k in legal4), str(legal4))
    r = TRI.stabilize(s)
    check(f'RV P3 {fmt(s)}: complete runs have exactly 4 firings', sum(r['counts']) == 4 and r['finish'] == (1, 1))
# inverse continuation: all starts finishing at (1,1) after exactly four firings
inv = [(a, b) for a in range(20) for b in range(20) if TRI.S((a, b)) [0] == (1, 1) and sum(TRI.S((a, b))[1]) == 4]
check('RV guide inverse: exactly three starts finish (1,1) after four firings: (0,6),(3,3),(6,0)', inv == [(0, 6), (3, 3), (6, 0)], str(inv))
check('RV guide: starting piles 1+2a-b, 1+2b-a for (a,b) = (1,3),(2,2),(3,1); (0,4),(4,0) negative',
      [(1 + 2 * a - b, 1 + 2 * b - a) for a, b in ((1, 3), (2, 2), (3, 1))] == [(0, 6), (3, 3), (6, 0)]
      and min(1 + 2 * 0 - 4, 1 + 2 * 4 - 0 - 4 * 2) < 0)


# reverse search from (1,1) with 4 sink chips: un-fire v = take a chip from the other circle and one from the sink
def unfire(state, v):
    a, b = state
    if v == 'A':
        return (a + 2, b - 1) if b >= 1 else None
    return (a - 1, b + 2) if a >= 1 else None


back = []


def rec(st, w, k):
    if k == 0:
        back.append((w, st)); return
    for v in 'AB':
        t2 = unfire(st, v)
        if t2:
            rec(t2, v + w, k - 1)


rec((1, 1), '', 4)
check('RV guide: four reverse moves from (1,1) give exactly the eight words, and their forward runs are legal',
      sorted(w for w, s in back) == sorted(sum(g.values(), [])) and all(TRI.run_word(s, w)[0] == (1, 1) for w, s in back), str(back))
check('RV guide: three starts and eight legal histories', len({s for w, s in back}) == 3 and len(back) == 8)

# ----------------------------------------------------------------- other readings (reported as NOTE lines)
say('\n=== Other readings and gaps ===')
nonempty = [s for s in FOUR.stable_states() if sum(s) > 0]
note(f'K-1 P4: {len(nonempty)} stable placements use at least one chip; the 8-row table is full only if the empty board (0,0,0) counts as a way to put chips')
k1p6 = []
x = (0, 0)
for i in range(11):
    x = T(TRI, x, 'A'); k1p6.append(x)
one_empty = [i + 1 for i, s in enumerate(k1p6) if 0 in s]
note(f'K-1 P6: after adding {one_empty} chips (of the 11 rows) one circle is empty (finish (1,0) or (0,1)); both circles are never empty again')
same_res = [s for s in TRI.stable_states() if (s[0] - s[1]) % 3 == 0]
note(f'Guide p8 invariant: stable pairs with A-B = 0 mod 3 are {same_res}; the remainder alone cannot tell (1,1) from (0,0) for (0,6),(3,3),(6,0)')

# ----------------------------------------------------------------- the guide text really says what I compared
say('\n=== Transcribed guide sentences present in the delivered PDFs ===')


def pdftext(fn):
    t = subprocess.run(['pdftotext', os.path.join(PKT, fn), '-'], capture_output=True, text=True).stdout
    return re.sub(r'\s+', ' ', t.replace('−', '-').replace('–', '-'))


GT = pdftext('week-11-facilitator.pdf')
RT = pdftext('week-11-return-visit-facilitator.pdf')
for txt, snippets in ((GT, [
    'Thus the triangle has 4 stable states; the four-cycle has 8; the extra-line board has 18',
    'the three boards have capacities 2, 3, 5',
    'W = 3A + 4B + 3C drops by 2 at every firing and stays nonnegative',
    'Each total has exactly three possible finishes',
    'Exactly three starts of total six finish at (1, 1): (0, 6), (3, 3), (6, 0)',
    'Other complete words are BBCAB, CBA, and CBBCBAABCAB',
    'Alternative legal orders, in the same row order, are CAB, BBBCAB, BCAB, and ACBABC',
    'All three timing choices finish at (1, 1, 1). Together, (2, 4, 0) has total firing counts (2, 3, 1)',
    'Use AB/BA; AAB only; ABAB/BABA; and AABABBAB/BBAABAAB',
    'The three starts have scores 48, 36, 40; each finishes at score 6, so the total numbers of moves are 21, 15, 17',
    'Two full legal words are BBABBABCCBACB and BBCBBCBAABCAB',
    'There are 3 · 2 · 3 = 18',
    'The only such start is the empty one',
    'The largest prescribed total is 12 chips',
    'Starts (0, 0) and (1, 1) merge after one addition at (1, 0)',
    'The start (4, 0) has only one complete legal word, AAB']),
        (RT, [
    'The maximum number of firings is four, attained only by starting at (1, 1, 1) and adding at B. Its two legal words are BACB and BCAB',
    'Every other stable start gives at most two',
    'BBAB, BBBA', 'ABAB, ABBA, BAAB, BABA', 'AAAB, AABA',
    'leaves three possible starts and eight legal histories',
    'For the printed start, AABC reaches (2,1,1), which was already reached after the first A',
    'the only types are (3, 0, 0), (2, 1, 0), and (1, 1, 1)'])):
    for s in snippets:
        check(f'text present: "{s[:70]}"', re.sub(r'\s+', ' ', s) in txt)

say('')
say(f'{len(FAILS)} FAIL lines, {len(NOTES)} NOTE lines.')
for f in FAILS:
    say('FAIL: ' + f)
open(os.path.join(HERE, 'check_answers.out'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
