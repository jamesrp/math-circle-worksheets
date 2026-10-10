"""Solve every Week 8 student problem from the data read out of the delivered
PDFs, and compare the results with the pages and with the adult guide.

Run extract_pdf.py first (it writes pdf_geometry.json).  The 4-5 starts that
are printed as text are read from pdftotext.  Every guide sentence used below
is first confirmed to be in the delivered guide PDF; the guide's answers were
transcribed by hand into the EXPECT lines.  Prints OK / MISMATCH / NOTE lines
and a summary (saved as check_answers.out).
"""
import json
import os
import re
import subprocess
import sys
sys.dont_write_bytecode = True  # never leave __pycache__ beside the packet sources
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import repo  # noqa: E402
from games import (rook_P, rook_winning_moves, nim_P, nim_winning_moves,  # noqa: E402
                   multisets, subtraction_P, rook_moves)

N_OK = N_BAD = N_NOTE = 0


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('\u2019', "'"), ('\u2018', "'"), ('\u201c', '"'), ('\u201d', '"'),
                 ('\u2013', '-'), ('\u2014', '-'), ('\u2212', '-'), ('\u00a0', ' ')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip()


def pdftext(path):
    return norm(subprocess.run(['pdftotext', path, '-'], capture_output=True, text=True).stdout)


GUIDE = pdftext(repo.GUIDE)


def quote(q):
    """Fail loudly if a guide sentence I rely on is not in the delivered guide."""
    global N_BAD
    if norm(q) not in GUIDE:
        N_BAD += 1
        print('MISMATCH  guide quote not found in delivered PDF: %r' % q)
        return False
    return True


def check(label, got, want, q=None):
    global N_OK, N_BAD
    if q is not None:
        quote(q)
    if got == want:
        N_OK += 1
        print('OK        %s: %s' % (label, got))
    else:
        N_BAD += 1
        print('MISMATCH  %s: computed %s, page/guide %s' % (label, got, want))


def note(msg):
    global N_NOTE
    N_NOTE += 1
    print('NOTE      ' + msg)


def who(P):
    return '2nd' if P else '1st'


def fmt_moves(ms):
    return sorted(ms)


geo = json.load(open(os.path.join(repo.HERE, 'pdf_geometry.json')))


def boards(band, prob):
    return [it for it in geo[band] if it['kind'] == 'board' and it['problem'] == prob]


def pilesets(band, prob):
    return [it for it in geo[band] if it['kind'] == 'piles' and it['problem'] == prob]


def text_starts(band, prob, nxt):
    t = pdftext(repo.STUDENT[band])
    a = t.index('Problem %d:' % prob)
    b = t.index('Problem %d:' % nxt) if nxt else len(t)
    seg = t[a:b]
    return [tuple(int(v) for v in m.split(', ')) for m in re.findall(r'\d+, \d+, \d+', seg)]


# ===================================================================== K-1
print('=' * 72)
print('K-1')
print('=' * 72)
for it in boards('k-1', None):
    check('K-1 rules picture: dot and arrow tips are legal one-move destinations',
          all(tuple(t) in list(rook_moves(*s)) for s, t in it['arrows']), True)
b = boards('k-1', 1)
check('K-1 P1 boards are 3-by-3 with 1-inch squares', [(x['n'], x['square_in']) for x in b],
      [(3, [1.0, 1.0])] * 2)
check('K-1 P1 left (2,2)', who(rook_P(*b[0]['dots'][0])), '2nd', 'Left: 2nd.')
check('K-1 P1 right (1,2) and its winning moves', (who(rook_P(*b[1]['dots'][0])), rook_winning_moves(*b[1]['dots'][0])),
      ('1st', [(1, 1)]), 'Right: 1st: slide down one square, to (1, 1).')
b = boards('k-1', 2)
check('K-1 P2 boards are 4-by-4 with 1-inch squares', [(x['n'], x['square_in']) for x in b], [(4, [1.0, 1.0])] * 4)
got = [(tuple(x['dots'][0]), who(rook_P(*x['dots'][0])), rook_winning_moves(*x['dots'][0])) for x in b]
check('K-1 P2 four starts (page order)', got,
      [((3, 3), '2nd', []), ((3, 0), '1st', [(0, 0)]), ((2, 2), '2nd', []), ((1, 3), '1st', [(1, 1)])],
      'Page 2 top (far corner): 2nd. Page 2 bottom (bottom row): 1st, slide left onto the star. Page 3 top (2 right, 2 up): 2nd. Page 3 bottom (1 right, 3 up): 1st, slide down two to (1, 1).')
b = boards('k-1', 3)
got = [(tuple(x['dots'][0]), rook_winning_moves(*x['dots'][0])) for x in b]
check('K-1 P3 the winning move on each 5-by-5 (exactly one each)', got,
      [((0, 3), [(0, 0)]), ((3, 1), [(1, 1)]), ((2, 4), [(2, 2)]), ((4, 3), [(3, 3)])],
      'Each board has exactly one winning move. Top left: the star itself (slide down 3). Top right: (1, 1), slide left 2. Bottom left: (2, 2), slide down 2. Bottom right: (3, 3), slide left 1.')
b = boards('k-1', 4)[0]
n = b['n']
red = [(a, c) for a in range(n) for c in range(n) if rook_P(a, c)]
check('K-1 P4 squares to move to on the 6-by-6 (P-positions, star included)', red,
      [(k, k) for k in range(6)], 'The six diagonal squares: the star, and 1 right 1 up, 2 right 2 up, ..., 5 right 5 up.')
note('K-1 P4 board squares are %.2f in, while the guide says "The boards on pages 1-3 and 5 have 1-inch squares".'
     % b['square_in'][0])
quote('The boards on pages 1–3 and 5 have 1-inch squares')
ps = pilesets('k-1', 5)
got = [(tuple(p['counts']), who(nim_P(p['counts'])), [q for q, mv in nim_winning_moves(p['counts'])]) for p in ps]
check('K-1 P5 four two-pile starts (page order)', got,
      [((3, 3), '2nd', []), ((4, 1), '1st', [(1, 1)]), ((2, 2), '2nd', []), ((5, 3), '1st', [(3, 3)])],
      'Top left, 3 and 3: 2nd. Top right, 4 and 1: 1st, take 3 from the 4 to leave 1 and 1. Bottom left, 2 and 2: 2nd. Bottom right, 5 and 3: 1st, take 2 from the 5 to leave 3 and 3.')
ps = pilesets('k-1', 6)
check('K-1 P6 7 and 7: second player wins', (ps[0]['counts'], who(nim_P(ps[0]['counts']))), ([7, 7], '2nd'))
# copying is a strategy that always works: every first-player move from equal piles can be copied
ok = all(nim_P((a, a)) for a in range(0, 8))
check('K-1 P6/P7 equal piles (diagonal squares) are all second-player wins up to 7', ok, True)
b = boards('k-1', 7)[0]
check('K-1 P7 8-by-8 from the far corner', (b['n'], tuple(b['dots'][0]), who(rook_P(*b['dots'][0]))), (8, (7, 7), '2nd'),
      '2nd wins by copying: if the partner slides left 3, slide down 3, and the other way round.')
ps = pilesets('k-1', 8)
got = [(tuple(p['counts']), who(nim_P(p['counts'])),
        sorted(tuple(q) for q, mv in nim_winning_moves(p['counts']))) for p in ps]
check('K-1 P8 three-pile starts (page order) with all winning results', got,
      [((1, 1, 1), '1st', [(0, 1, 1), (1, 0, 1), (1, 1, 0)]), ((1, 1, 2), '1st', [(1, 1, 0)]),
       ((1, 2, 3), '2nd', []), ((2, 2, 3), '1st', [(1, 2, 3), (2, 1, 3), (2, 2, 0)])],
      '1, 1, 1: 1st (take any whole pile, leaving 1 and 1). 1, 1, 2: 1st (take the 2). 1, 2, 3: 2nd. 2, 2, 3: 1st (take the 3; or take 1 from a 2, leaving 1, 2, 3).')
k1_choice = sum(it['1st'] for it in geo['k-1'] if it['kind'] == 'choice-labels')
check('K-1 1st/2nd box pairs = starts in P1, P2, P5, P8 (2+4+4+4)', k1_choice, 14)

# ===================================================================== 2-3
print('=' * 72)
print('Grades 2-3')
print('=' * 72)
b = boards('grades-2-3', 1)
got = [(tuple(x['dots'][0]), who(rook_P(*x['dots'][0])), rook_winning_moves(*x['dots'][0])) for x in b]
check('2-3 P1 four 5-by-5 starts', [x['n'] for x in b] + got,
      [5, 5, 5, 5, ((4, 4), '2nd', []), ((4, 2), '1st', [(2, 2)]), ((3, 3), '2nd', []), ((1, 4), '1st', [(1, 1)])],
      'Top left (4, 4): 2nd. Top right (4, 2): 1st, only by sliding left 2 to (2, 2). Bottom left (3, 3): 2nd. Bottom right (1, 4): 1st, only by sliding down 3 to (1, 1).')
b = boards('grades-2-3', 2)[0]
red = [(a, c) for a in range(8) for c in range(8) if (a, c) != (0, 0) and rook_P(a, c)]
green = [(a, c) for a in range(8) for c in range(8) if (a, c) != (0, 0) and not rook_P(a, c)]
check('2-3 P2 8-by-8: red squares, number green', (b['n'], red, len(green)), (8, [(k, k) for k in range(1, 8)], 56),
      'Red: the 7 diagonal squares (1, 1) to (7, 7). The other 56 squares are green.')
b = boards('grades-2-3', 3)[0]
check('2-3 P3 corner of 8-by-8', (b['n'], tuple(b['dots'][0]), who(rook_P(*b['dots'][0]))), (8, (7, 7), '2nd'))
# copy strategy check: from (k,k) after any opponent move, the copy reply returns to the diagonal
ok = True
for k in range(1, 8):
    for m in rook_moves(k, k):
        a, c = m
        reply = (min(a, c), min(a, c))
        ok &= reply in rook_moves(a, c) and rook_P(*reply)
check('2-3 P3 / 4-5 P1 copy reply is always legal and returns to the diagonal', ok, True)
ps = pilesets('grades-2-3', 4)
got = [(tuple(p['counts']), p['label'], who(nim_P(p['counts'])), [q for q, mv in nim_winning_moves(p['counts'])]) for p in ps]
check('2-3 P4 two-pile starts (drawn count, printed label)', got,
      [((4, 4), '4 and 4', '2nd', []), ((6, 2), '6 and 2', '1st', [(2, 2)]),
       ((5, 3), '5 and 3', '1st', [(3, 3)]), ((7, 7), '7 and 7', '2nd', [])],
      '4 and 4: 2nd. 6 and 2: 1st, take 4 from the 6. 5 and 3: 1st, take 2 from the 5. 7 and 7: 2nd.')
b = boards('grades-2-3', 5)[0]
check('2-3 P5 dot -> piles (right, up)', (b['n'], tuple(b['dots'][0])), (8, (5, 2)), '5 and 2.')
# board game from (a,b) is isomorphic to Nim(a,b): same successor structure
iso = all(sorted(rook_moves(a, c)) == sorted(q for q, mv in __import__('games').nim_moves((a, c))) for a in range(8) for c in range(8))
check('2-3 P5 / 4-5 P2 board moves = two-pile moves for every square of an 8-by-8', iso, True)
t = pdftext(repo.STUDENT['grades-2-3'])
check('2-3 P6 text', 'piles of 52 and 37 counters' in t, True)
check('2-3 P6 52 and 37', (who(nim_P((52, 37))), [q for q, mv in nim_winning_moves((52, 37))]), ('1st', [(37, 37)]),
      'Take 15 from the 52, leaving 37 and 37 (the only winning first move).')
ps = pilesets('grades-2-3', 7)
got = [(tuple(p['counts']), p['label'], who(nim_P(p['counts'])),
        sorted(tuple(q) for q, mv in nim_winning_moves(p['counts']))) for p in ps]
check('2-3 P7 three-pile starts (drawn count, printed label)', got,
      [((1, 1, 1), '1, 1, 1', '1st', [(0, 1, 1), (1, 0, 1), (1, 1, 0)]), ((1, 1, 2), '1, 1, 2', '1st', [(1, 1, 0)]),
       ((2, 2, 3), '2, 2, 3', '1st', [(1, 2, 3), (2, 1, 3), (2, 2, 0)]), ((1, 2, 3), '1, 2, 3', '2nd', [])],
      '1, 1, 1: 1st (take any pile). 1, 1, 2: 1st (take the 2). 2, 2, 3: 1st (take the 3, or 1 from a 2). 1, 2, 3: 2nd:')
# the reply table for 1,2,3
quote('They take the 1: take 1 from the 3. The 2: take 2 from the 3. 1 from the 2: take the 3. The 3: take 1 from the 2. 1 from the 3: take the 1. 2 from the 3: take the 2.')
table = {  # opponent's move (pile index in (1,2,3), amount) -> guide's reply (pile index, amount)
    (0, 1): (2, 1), (1, 2): (2, 2), (1, 1): (2, 3), (2, 3): (1, 1), (2, 1): (0, 1), (2, 2): (1, 2)}
ok = True
covered = set()
for q, mv in __import__('games').nim_moves((1, 2, 3)):
    covered.add(mv)
    r = table[mv]
    after = list(q)
    ok &= after[r[0]] >= r[1]
    after[r[0]] -= r[1]
    nz = sorted(x for x in after if x)
    ok &= len(nz) == 2 and nz[0] == nz[1] and nim_P(after)
check('2-3 P7 guide reply table covers all 6 moves from 1,2,3 and each reply leaves two equal piles', (ok, len(covered)), (True, 6))
S = multisets(1, 3)
P = [s for s in S if nim_P(s)]
check('2-3 P8 starts with piles 1-3: count, second-player starts', (len(S), P), (10, [(1, 2, 3)]),
      'Only 1, 2, 3 (of the 10 starts).')
S = multisets(1, 6)
P = [s for s in S if nim_P(s)]
distinct = [s for s in S if len(set(s)) == 3]
check('2-3 P9 starts with piles 1-6: count, distinct, second-player starts', (len(S), len(distinct), P),
      (56, 20, [(1, 2, 3), (1, 4, 5), (2, 4, 6), (3, 5, 6)]),
      '1, 2, 3; 1, 4, 5; 2, 4, 6; 3, 5, 6 (4 of the 56 starts). Crossing out starts with two equal piles leaves 20 to test.')
ok = all(not nim_P(s) for s in multisets(1, 30) if len(set(s)) < 3)
check('"two equal piles: go first and take the third" - every start with a repeated pile (1-30) is 1st', ok, True)

# ===================================================================== 4-5
print('=' * 72)
print('Grades 4-5')
print('=' * 72)
b = boards('grades-4-5', None)[0]
check('4-5 rules picture arrows legal', all(tuple(t) in list(rook_moves(*s)) for s, t in b['arrows']), True)
b = boards('grades-4-5', 1)[0]
red = [(a, c) for a in range(8) for c in range(8) if (a, c) != (0, 0) and rook_P(a, c)]
check('4-5 P1 8-by-8 red squares', (b['n'], red, 63 - len(red)), (8, [(k, k) for k in range(1, 8)], 56),
      'Red: the diagonal (1, 1) to (7, 7); 56 green')
b = boards('grades-4-5', 2)[0]
check('4-5 P2 dot', (b['n'], tuple(b['dots'][0])), (8, (6, 3)), '6 and 3 (the dot is 6 right, 3 up).')
check('4-5 P2 23 and 17; 30 and 30',
      (who(nim_P((23, 17))), [q for q, mv in nim_winning_moves((23, 17))], who(nim_P((30, 30)))),
      ('1st', [(17, 17)], '2nd'), '23 and 17: first player, take 6 from the 23. 30 and 30: second player, by copying.')
st = text_starts('grades-4-5', 3, 4)
check('4-5 P3 printed starts', st, [(1, 1, 1), (1, 1, 2), (1, 2, 3), (2, 2, 5), (1, 3, 4), (1, 4, 5)])
got = [(s, who(nim_P(s)), sorted(tuple(q) for q, mv in nim_winning_moves(s))) for s in st]
check('4-5 P3 winners and every winning result', got,
      [((1, 1, 1), '1st', [(0, 1, 1), (1, 0, 1), (1, 1, 0)]), ((1, 1, 2), '1st', [(1, 1, 0)]), ((1, 2, 3), '2nd', []),
       ((2, 2, 5), '1st', [(2, 2, 0)]), ((1, 3, 4), '1st', [(1, 3, 2)]), ((1, 4, 5), '2nd', [])],
      '1, 1, 1: first. 1, 1, 2: first (take the 2). 1, 2, 3: second. 2, 2, 5: first (take the 5). 1, 3, 4: first, only by taking 2 from the 4 (leaving 1, 3, 2). 1, 4, 5: second.')
S = multisets(1, 7)
P = [s for s in S if nim_P(s)]
check('4-5 P4 piles 1-7: count and second-player starts', (len(S), P),
      (84, [(1, 2, 3), (1, 4, 5), (1, 6, 7), (2, 4, 6), (2, 5, 7), (3, 4, 7), (3, 5, 6)]),
      'Seven of the 84 starts: 1, 2, 3; 1, 4, 5; 1, 6, 7; 2, 4, 6; 2, 5, 7; 3, 4, 7; 3, 5, 6.')
quote('Starts to leave: 1, 2, 3; 1, 4, 5; 1, 6, 7; 2, 4, 6; 2, 5, 7; 3, 4, 7; 3, 5, 6.')
t = pdftext(repo.STUDENT['grades-4-5'])
a = t.index('Problem 5:')
mid = t.index('The first player can always win from each of these starts.')
e = t.index('Make these starts with counters')
second = [tuple(int(v) for v in m.split(', ')) for m in re.findall(r'\d+, \d+, \d+', t[a:mid])]
first = [tuple(int(v) for v in m.split(', ')) for m in re.findall(r'\d+, \d+, \d+', t[mid:e])]
check('4-5 P5 printed "second player" starts are all P', (second, all(nim_P(s) for s in second)),
      ([(1, 2, 3), (1, 4, 5), (2, 4, 6), (3, 5, 6), (2, 5, 7)], True))
check('4-5 P5 printed "first player" starts are all N', (first, all(not nim_P(s) for s in first)),
      ([(1, 2, 4), (2, 3, 5), (2, 4, 7), (3, 4, 6)], True))


def stacks(n):
    return [1 << i for i in range(n.bit_length()) if n >> i & 1]


def odd_sizes(s):
    from collections import Counter
    c = Counter(x for p in s for x in stacks(p))
    return sorted(k for k, v in c.items() if v % 2)


# the stack rule, tested against the game-tree search (no xor used)
ok = all((odd_sizes(s) == []) == nim_P(s) for s in multisets(0, 31))
check('4-5 P5 rule "every stack size an even number of times" <=> second player wins, all 3-pile starts 0-31', ok, True)
ok = all((odd_sizes(s) == []) == nim_P(s) for s in multisets(0, 9, 4))
check('same rule for all 4-pile starts 0-9 (the guide: "any number of piles")', ok, True)
check('4-5 P5 odd stack sizes in the first-player starts', [odd_sizes(s) for s in first], [[1, 2, 4], [4], [1], [1]],
      'In each first-player start some size is odd: 1, 2, 4 (all once); 2, 3, 5 (one 4); 2, 4, 7 and 3, 4, 6 (one 1).')
check('4-5 P5 guide splits 1,4,5 and 2,5,7', ([stacks(x) for x in (1, 4, 5)], [stacks(x) for x in (2, 5, 7)]),
      ([[1], [4], [1, 4]], [[2], [1, 4], [1, 2, 4]]))
st = text_starts('grades-4-5', 6, 7)
check('4-5 P6 printed starts', st, [(3, 5, 7), (6, 10, 12), (13, 9, 7), (11, 14, 21)])
got = [(s, who(nim_P(s)), sorted(tuple(q) for q, mv in nim_winning_moves(s))) for s in st]
check('4-5 P6 winners and every winning result', got,
      [((3, 5, 7), '1st', [(2, 5, 7), (3, 4, 7), (3, 5, 6)]), ((6, 10, 12), '2nd', []),
       ((13, 9, 7), '1st', [(13, 9, 4)]), ((11, 14, 21), '1st', [(11, 14, 5)])],
      '3, 5, 7: first; take 1 from any pile. 6, 10, 12: second (4+2 | 8+2 | 8+4). 13, 9, 7: first; only move: take 3 from the 7, leaving 13, 9, 4. 11, 14, 21: first; only move: take 16 from the 21, leaving 11, 14, 5.')
check('4-5 P6 splits of 6, 10, 12', [stacks(x) for x in (6, 10, 12)], [[2, 4], [2, 8], [4, 8]])
check('4-5 materials: "Problem 6 needs 46"', max(sum(s) for s in st), 46, '60 (Problem 6 needs 46)')

# P7: the guide's step (b) rebuild, tested on every unbalanced 3-pile start up to 63
ok = True
for s in multisets(0, 63):
    od = odd_sizes(s)
    if not od:
        continue
    big = od[-1]
    i = next(k for k, p in enumerate(s) if big in stacks(p))
    new = set(stacks(s[i])) ^ set(od)
    v = sum(new)
    t2 = list(s)
    t2[i] = v
    ok &= v < s[i] and odd_sizes(t2) == [] and nim_P(t2)
check('4-5 P7 guide step (b): switching every odd size in a pile holding the biggest odd stack is a legal move to a balanced, second-player start (all starts 0-63)', ok, True)
ok = all(odd_sizes(q) != [] for s in multisets(0, 31) if not odd_sizes(s) for q, mv in __import__('games').nim_moves(s))
check('4-5 P7 guide step (a): every move from a balanced start unbalances it (0-31)', ok, True)

b = boards('grades-4-5', 8)
check('4-5 P8 queen rule picture arrows legal queen moves', all(tuple(t) in list(rook_moves(*s, queen=True)) for s, t in b[0]['arrows']) and
      any(s[0] - t[0] == s[1] - t[1] > 0 for s, t in b[0]['arrows']), True)
red8 = [(a, c) for a in range(8) for c in range(8) if (a, c) != (0, 0) and rook_P(a, c, True)]
check('4-5 P8 queen game 8-by-8 red squares', (b[1]['n'], red8, 63 - len(red8)),
      (8, [(1, 2), (2, 1), (3, 5), (4, 7), (5, 3), (7, 4)], 57),
      'Red: (1, 2), (2, 1), (3, 5), (5, 3), (4, 7), (7, 4). The other 57 squares are green.')
b = boards('grades-4-5', 9)[0]
red20 = [(a, c) for a in range(20) for c in range(20) if (a, c) != (0, 0) and rook_P(a, c, True)]
pairs = sorted({tuple(sorted(x)) for x in red20})
check('4-5 P9 queen game 20-by-20: red squares (as pairs) and count', (b['n'], pairs, len(red20)),
      (20, [(1, 2), (3, 5), (4, 7), (6, 10), (8, 13), (9, 15), (11, 18)], 14),
      '14 red squares: (1, 2), (3, 5), (4, 7), (6, 10), (8, 13), (9, 15), (11, 18) and their mirror images. The next pair, (12, 20), is just off the board.')
check('next P-position beyond the board is (12, 20)', rook_P(12, 20, True) and rook_P(20, 12, True), True)
# no row/column/diagonal holds two reds; the row-by-row procedure from the guide reproduces the reds
rows = {}
for (a, c) in red20:
    rows.setdefault(c, []).append(a)
ok = all(len(v) == 1 for v in rows.values())
diag = {}
for (a, c) in red20:
    diag.setdefault(a - c, []).append((a, c))
ok &= all(len(v) == 1 for v in diag.values())
check('4-5 P9 at most one red square per row and per diagonal', ok, True)
found = [(0, 0)]
proc = []
for y in range(1, 20):   # row 0's red square is the star itself
    for x in range(20):
        if all(x != fx and x - y != fx - fy for fx, fy in found):
            if (x, y) != (0, 0):
                found.append((x, y))
                proc.append((x, y))
            break
check('4-5 P9 guide procedure (row by row, first square not in the column or diagonal of a red already found)',
      sorted(proc), sorted(red20))
missing_rows = [y for y in range(1, 20) if y not in rows]
note('4-5 P9: rows %s of the 20-by-20 have no red square (their P-position lies right of the board); '
     'the guide procedure then finds no square in those rows, which is consistent.' % missing_rows)

# ===================================================================== guide, general
print('=' * 72)
print('Adult guide: general statements, launch, fallbacks')
print('=' * 72)
# launch: token on top-right of a 4-by-4 (3,3); adult slides two left -> (1,3); child's options
check('launch: legal moves from (1,3) on the 4-by-4', sorted(rook_moves(1, 3)), sorted([(0, 3), (1, 2), (1, 1), (1, 0)]),
      'One child slides the token (one square left, or one, two or three squares down).')
check('fallback take 1, 2 or 3 from 20: P-positions are multiples of 4 and 20 is P',
      ([n for n in range(0, 41) if subtraction_P(n)], subtraction_P(20)), (list(range(0, 41, 4)), True),
      '(Leave a multiple of 4; from 20 you would rather go second.)')
check('materials: tokens 3+3+2 = 8, +1 launch +3 spare', 3 + 3 + 2 + 1 + 3, 12, '8 + 1 launch + 3 spare = 12')
check('materials: Letter margin beside an 8-inch board', (8.5 - 8) / 2, 0.25)
check('queen strategy list in "How to win" matches the search', sorted({tuple(sorted(x)) for x in
      [(a, c) for a in range(25) for c in range(25) if (a, c) != (0, 0) and rook_P(a, c, True)] if max(x) <= 20}),
      [(1, 2), (3, 5), (4, 7), (6, 10), (8, 13), (9, 15), (11, 18), (12, 20)],
      'Leave the token on one of these squares or its mirror image: (1, 2), (3, 5), (4, 7), (6, 10), (8, 13), (9, 15), (11, 18), (12, 20).')
# Wythoff: floor(n phi), floor(n phi^2), Beatty
import math
phi = (1 + 5 ** 0.5) / 2
wy = [(math.floor(k * phi), math.floor(k * phi * phi)) for k in range(0, 40)]
ok = all(rook_P(a, c, True) and rook_P(c, a, True) for a, c in wy if c < 60)
cnt = sum(1 for a in range(60) for c in range(60) if rook_P(a, c, True))
cnt2 = sum(1 for a, c in wy for _ in ([0] if a == c else [0, 1]) if a < 60 and c < 60)
check('Wythoff closed form floor(n phi), floor(n phi^2) gives exactly the P-positions on a 60-by-60', (ok, cnt == cnt2), (True, True))
vals = sorted([a for a, c in wy[1:]] + [c for a, c in wy[1:]])
check('Beatty: the two sequences cover 1..60 exactly once', [v for v in vals if v <= 60], list(range(1, 61)))

# Misere Nim strategy as worded in the guide (fallback and "Where it goes next")
quote('play normal Nim until your move would leave only piles of size 1, then leave an odd number of them.')


def guide_misere_move(s):
    """'Play as in ordinary Nim until your move would leave only piles of 1, then leave an odd number of them.'"""
    from games import nim_moves
    normal = [q for q, mv in nim_moves(s) if nim_P(q)]
    for q in normal:
        if max(q) >= 2:
            return q
    for q, mv in nim_moves(s):
        if max(q) <= 1 and sum(q) % 2 == 1:
            return q
    return None


ok = True
bad = []
for s in multisets(0, 12, 3) + multisets(0, 6, 4):
    if sum(s) == 0 or nim_P(s, misere=True):
        continue
    q = guide_misere_move(s)
    if q is None or not nim_P(q, misere=True):
        ok = False
        bad.append(s)
check('misere: the guide\'s worded strategy wins from every misere first-player start (3 piles 0-12, 4 piles 0-6)', (ok, bad[:5]), (True, []))
# Moore's Nim_k: P iff every binary digit count is divisible by k+1 (checked for k=2, 4 piles up to 7)
from functools import lru_cache
from itertools import combinations


@lru_cache(maxsize=None)
def moore_P(s, k):
    s = tuple(sorted(s))
    moves = set()
    idx = [i for i in range(len(s)) if s[i] > 0]
    for r in range(1, k + 1):
        for sub in combinations(idx, r):
            def rec(j, cur):
                if j == len(sub):
                    if cur != s:
                        moves.add(tuple(sorted(cur)))
                    return
                i = sub[j]
                for v in range(0, s[i] + 1):
                    c2 = list(cur)
                    c2[i] = v
                    rec(j + 1, tuple(c2))
            rec(0, s)
    return all(not moore_P(m, k) for m in moves)


ok = True
for s in multisets(0, 7, 4):
    rule = all(sum((x >> b) & 1 for x in s) % 3 == 0 for b in range(4))
    ok &= rule == moore_P(s, 2)
check("Moore's Nim_2 rule (digit counts divisible by 3), all 4-pile starts 0-7", ok, True)

# ===================================================================== guide figures
print('=' * 72)
print('Adult guide figures (shaded squares, arrows) read from figs/*.tex')
print('=' * 72)
FIG = os.path.join(repo.SRC, 'guide-src', 'figs')


def read_fig(name):
    s = open(os.path.join(FIG, name + '.tex')).read()
    step = float(re.search(r'grid\[step=([\d.]+)\]', s).group(1))
    fills = [(round(float(a) / step), round(float(b) / step))
             for a, b in re.findall(r'\\fill\[ans\] \(([\d.]+),([\d.]+)\)', s)]
    dot = [(int(float(a) / step), int(float(b) / step))
           for a, b in re.findall(r'\\filldraw\[fill=black!35[^\]]*\] \(([\d.]+),([\d.]+)\)', s)]
    arr = [((int(float(a) / step), int(float(b) / step)), (int(float(c) / step), int(float(d) / step)))
           for a, b, c, d in re.findall(r'Stealth[^\]]*\][^(]*\(([\d.]+),([\d.]+)\) -- \(([\d.]+),([\d.]+)\)', s)]
    label = re.findall(r'\\scriptsize (1st|2nd)', s)
    star = 'node[star' in s
    return {'fills': sorted(fills), 'dot': dot, 'arrows': arr, 'label': label, 'star': star}


figs = {
    'k1-p1-1': (2, 2), 'k1-p1-2': (1, 2), 'k1-p2-1': (3, 3), 'k1-p2-2': (3, 0), 'k1-p2-3': (2, 2), 'k1-p2-4': (1, 3),
    'k1-p3-1': (0, 3), 'k1-p3-2': (3, 1), 'k1-p3-3': (2, 4), 'k1-p3-4': (4, 3),
    'm-p1-1': (4, 4), 'm-p1-2': (4, 2), 'm-p1-3': (3, 3), 'm-p1-4': (1, 4)}
for name, start in figs.items():
    f = read_fig(name)
    wm = rook_winning_moves(*start)
    want = {'dot': [start], 'fills': sorted(wm), 'arrows': [(start, m) for m in wm]}
    got = {'dot': f['dot'], 'fills': f['fills'], 'arrows': f['arrows']}
    if f['label']:
        want['label'] = [who(rook_P(*start))]
        got['label'] = f['label']
    check('guide figure %s (start %s)' % (name, start), got, want)
f = read_fig('k1-p4')
check('guide figure k1-p4 shading', f['fills'], [(k, k) for k in range(6)])
f = read_fig('diag8')
check('guide figure diag8 shading (star square + 7 diagonal)', f['fills'], [(k, k) for k in range(8)])
f = read_fig('queen8')
check('guide figure queen8 shading (star square + 6)', f['fills'], sorted([(0, 0)] + red8))
f = read_fig('queen20')
check('guide figure queen20 shading (corner square + 14)', f['fills'], sorted([(0, 0)] + red20))
if not f['star']:
    note('guide figure queen20 shades the corner square (0,0) but draws no star there, so the picture shows %d shaded '
         'squares beside the text "14 red squares"; diag8 and queen8 also shade the star square but draw the star on it.'
         % len(f['fills']))
quote('14 red squares')
quote('red = the square to move to, or the squares where you would rather go second.')

print('=' * 72)
print('Summary: %d OK, %d MISMATCH, %d NOTE' % (N_OK, N_BAD, N_NOTE))
