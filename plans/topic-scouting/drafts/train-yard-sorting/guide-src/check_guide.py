#!/usr/bin/env python3
"""Recompute every answer printed in the Train-yard sorting facilitator guide.

Independent of the page builder's verify.py: one siding is searched over every
legal move sequence (breadth-first), two sidings likewise, and paths are decoded
by matching each down-step with the most recent unmatched up-step.

Train convention (as on the pages): the leftmost car arrives first.
Run: python3 check_guide.py   (exits non-zero if any assertion fails)
"""
from itertools import permutations, product
from collections import deque

def T(s):
    return tuple(int(c) for c in s.replace(' ', ''))

def S(p):
    return ' '.join(map(str, p))

# ---------------------------------------------------------------- one siding
def drives(train, cap=None):
    """All successful move words (U = into siding, D = out to departure)."""
    n = len(train)
    out = []
    def rec(i, st, need, w):
        if need > n:
            out.append(w); return
        if st and st[-1] == need:
            rec(i, st[:-1], need + 1, w + 'D')
        if i < n and (cap is None or len(st) < cap):
            rec(i + 1, st + (train[i],), need, w + 'U')
    rec(0, (), 1, '')
    return out

def ok1(train, cap=None):
    return bool(drives(train, cap))

def has231(p):
    n = len(p)
    return any(p[k] < p[i] < p[j] for i in range(n) for j in range(i+1, n) for k in range(j+1, n))

def a231(p):
    n = len(p)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if p[k] < p[i] < p[j]:
                    return (p[i], p[j], p[k])
    return None

def height(train):
    """Most cars in the siding during the successful drive (or, for a stuck
    train, while driving by the never-fails rule until stuck)."""
    st, need, i, m = [], 1, 0, 0
    while True:
        if st and st[-1] == need:
            st.pop(); need += 1
        elif i < len(train):
            st.append(train[i]); i += 1; m = max(m, len(st))
        else:
            return m

# ---------------------------------------------------------------- two sidings
def ok2(train, cap=None, return_word=False):
    """First siding A, then second siding B, in series. Moves: a = arrival->A,
    b = A->B, o = B->departure. Breadth-first over all states."""
    n = len(train)
    start = (0, (), (), 1)
    prev = {start: None}
    q = deque([start])
    while q:
        s = q.popleft()
        i, A, B, need = s
        if need > n:
            if not return_word:
                return True
            w = []
            while prev[s]:
                s, m = prev[s]; w.append(m)
            return ''.join(reversed(w))
        nxt = []
        if B and B[-1] == need:
            nxt.append(((i, A, B[:-1], need + 1), 'o'))
        if A and (cap is None or len(B) < cap):
            nxt.append(((i, A[:-1], B + (A[-1],), need), 'b'))
        if i < n and (cap is None or len(A) < cap):
            nxt.append(((i + 1, A + (train[i],), B, need), 'a'))
        for t, m in nxt:
            if t not in prev:
                prev[t] = (s, m); q.append(t)
    return False

def stack_outputs(train):
    """Every order in which one siding can send the whole train out (any order,
    not only 1, 2, 3, ...)."""
    res = set()
    def rec(i, st, out):
        if i == len(train) and not st:
            res.add(tuple(out)); return
        if i < len(train):
            rec(i + 1, st + [train[i]], out)
        if st:
            rec(i, st[:-1], out + [st[-1]])
    rec(0, [], [])
    return res

# ---------------------------------------------------------------- paths
def decode(word):
    stack, lab, k, ups = [], {}, 0, []
    for idx, c in enumerate(word):
        if c == 'U':
            stack.append(idx); ups.append(idx)
        else:
            k += 1; lab[stack.pop()] = k
    return tuple(lab[i] for i in ups)

def mountain(word):
    h = 0
    for c in word:
        h += 1 if c == 'U' else -1
        if h < 0:
            return False
    return h == 0

def mark(train, cap=None):
    return 'Y' if ok1(train, cap) else 'x'

failures = 0
def check(cond, msg):
    global failures
    if not cond:
        failures += 1
        print('FAIL:', msg)

print('=== General facts')
cat = []
for n in range(1, 9):
    perms = list(permutations(range(1, n + 1)))
    good = [p for p in perms if ok1(p)]
    for p in perms:
        check(ok1(p) == (not has231(p)), f'231 rule {p}')
        if n <= 7:
            d = drives(p)
            check(len(d) <= 1, f'unique drive {p}')
    cat.append(len(good))
print('sortable counts 1..8:', cat)
check(cat == [1, 2, 5, 14, 42, 132, 429, 1430], 'Catalan')
print('six-car with a 5-place siding:', sum(ok1(p, 5) for p in permutations(range(1, 7))),
      'fails only:', [S(p) for p in permutations(range(1, 7)) if ok1(p) and not ok1(p, 5)])
for n in range(1, 8):
    words = [''.join(w) for w in product('UD', repeat=2 * n) if w.count('U') == n]
    mts = [w for w in words if mountain(w)]
    trains = {decode(w) for w in mts}
    check(len(trains) == len(mts) == cat[n - 1], f'path bijection {n}')
    for w in mts:
        check(drives(decode(w)) == [w], f'decode drive {w}')
    if n == 4:
        print('4 ups/4 downs:', len(words), 'words,', len(mts), 'mountain paths')
# first-return / biggest-car recurrence
C = [1]
for n in range(1, 9):
    C.append(sum(C[k] * C[n - 1 - k] for k in range(n)))
check(C[1:] == cat, 'recurrence')
print('C5 terms', [C[k] * C[4 - k] for k in range(5)], 'C6 terms', [C[k] * C[5 - k] for k in range(6)])
# position of the largest car splits the train
for n in range(1, 8):
    for p in permutations(range(1, n + 1)):
        j = p.index(n)
        L, R = p[:j], p[j + 1:]
        split_ok = all(a < b for a in L for b in R) and not has231(L) and not has231(R)
        check(split_ok == ok1(p), f'biggest-car split {p}')

print('=== Launch train 2 1')
print('drive of 2 1:', drives((2, 1)))
check(drives((2, 1)) == ['UUDD'], 'launch drive')

print('=== K-1')
K1 = {
 'P1': ['123', '132', '213', '231', '312', '321'],
 'P2': ['2143', '3412', '4321', '1432', '4231', '3124', '4132', '1342'],
 'P4': ['45123', '21543', '54321', '51324', '13524', '32514'],
}
for k, v in K1.items():
    print(k, ' '.join(f'{s}:{mark(T(s))}{"" if ok1(T(s)) else " " + S(a231(T(s)))}(h{height(T(s))})' for s in v))
check([mark(T(s)) for s in K1['P1']] == list('YYYxYY'), 'K1 P1')
check([mark(T(s)) for s in K1['P2']] == list('YxYYxYYx'), 'K1 P2')
check([mark(T(s)) for s in K1['P4']] == list('xYYYxx'), 'K1 P4')
for s in K1['P4']:
    check(ok1(T(s), 5) == ok1(T(s)), 'K1 P4 fits 5-place siding')
p3 = [p + (1,) for p in permutations((2, 3, 4))]
print('P3 x y z 1:', [(S(p), mark(p)) for p in p3])
check([p for p in p3 if ok1(p)] == [(4, 3, 2, 1)], 'K1 P3')
stuck4 = [p for p in permutations(range(1, 5)) if not ok1(p)]
print('P6 stuck four-car trains:', len(stuck4), [S(p) for p in stuck4])
check(len(stuck4) == 10, 'K1 P6 count')
byfirst = {f: [S(p) for p in stuck4 if p[0] == f] for f in range(1, 5)}
print('   by first car:', byfirst)
earlier = {T(s) for s in K1['P2'] if not ok1(T(s))} | {p for p in p3 if not ok1(p)}
print('   already met in P2/P3:', len(earlier), ' new:', [S(p) for p in stuck4 if p not in earlier])
five = list(permutations(range(1, 6)))
print('P5 game: five-car trains that leave in order:', sum(ok1(p) for p in five), 'of', len(five),
      '; all fit a 5-place siding:', all(ok1(p, 5) == ok1(p) for p in five))
print('   five-car ending in 1 that work:', [S(p) for p in five if p[-1] == 1 and ok1(p)])
print('   five-car starting with 5 that work:', sum(1 for p in five if p[0] == 5 and ok1(p)))

print('=== Grades 2-3')
G23 = {
 'P3': ['32154', '41325', '24351', '12534', '45321', '31542', '52143', '15342'],
 'P5': ['42513', '14235', '34521', '53412', '54132', '21534'],
}
for k, v in G23.items():
    print(k, ' '.join(f'{s}:{mark(T(s))}{"" if ok1(T(s)) else " " + S(a231(T(s)))}(h{height(T(s))})' for s in v))
check([mark(T(s)) for s in G23['P3']] == list('YYxYxxYx'), '23 P3')
check([mark(T(s)) for s in G23['P5']] == list('xYxxYY'), '23 P5')
four_good = [p for p in permutations(range(1, 5)) if ok1(p)]
print('P2: can', len(four_good), 'cannot', 24 - len(four_good))
print('   by first car (can):', {f: sum(1 for p in four_good if p[0] == f) for f in range(1, 5)})
def gaps(p):
    return [i for i in range(len(p) + 1) if ok1(p[:i] + (5,) + p[i:])]
for s in ['2143', '4321', '1324', '3124']:
    p = T(s)
    g = gaps(p)
    rule = [i for i in range(5) if all(a < b for a in p[:i] for b in p[i:])]
    check(g == rule, f'gap rule {s}')
    print(f'P6 {s}: gaps {g} -> ' + ', '.join(S(p[:i] + (5,) + p[i:]) for i in g))
tot = 0
rows = []
for p in four_good:
    g = len(gaps(p)); tot += g; rows.append(f'{S(p)}:{g}')
print('P7 gap counts:', ', '.join(rows), ' sum =', tot)
check(tot == 42, 'gap sum')
bypos = [sum(1 for p in five if ok1(p) and p.index(5) == j) for j in range(5)]
print('P7 by position of car 5:', bypos, sum(bypos))
check(bypos == [14, 5, 4, 5, 14], 'pos of 5')
# removing car 5 keeps a train that works
for p in five:
    if ok1(p):
        check(ok1(tuple(c for c in p if c != 5)), 'remove 5')
# counterexamples to likely wrong rules
print('stuck with no three neighbours forming middle-big-small:',
      [S(p) for p in permutations(range(1, 5)) if not ok1(p) and
       not any(p[i + 2] < p[i] < p[i + 1] for i in range(len(p) - 2))])

print('=== Grades 4-5')
G45P2 = ['31254', '24153', '13542', '51423', '361245', '214635', '1726354', '3217645',
         '41328675', '43128576']
for s in G45P2:
    p = T(s)
    print(f'P2 {s}: {mark(p)} {S(a231(p)) if a231(p) else drives(p)[0]} h{height(p)}')
m = [mark(T(s)) for s in G45P2]
print('   rows:', [''.join(m[i:i + 2]) for i in range(0, 10, 2)])
for s in G45P2:
    check(height(T(s)) <= 5, 'P2 fits 5 places')
print('P4 the 14 four-car paths:')
for p in four_good:
    print('  ', S(p), drives(p)[0])
words5 = ['UDUUUDDUDD', 'UUUDDUUDDD', 'UUDUUDDDUD', 'UUUUDDDUDD']
dec = [decode(w) for w in words5]
for w, d in zip(words5, dec):
    check(mountain(w) and drives(d) == [w], 'P5')
    print('P5', w, '->', S(d))
check(len(set(dec)) == 4, 'P5 distinct')
print('P7: five', cat[4], ' six', cat[5])
print('P8 two sidings:')
for s in ['231', '3412', '25341']:
    p = T(s)
    w = ok2(p, return_word=True)
    check(bool(w), f'P8 {s}')
    via = [o for o in stack_outputs(p) if not has231(o)]
    print(f'   {s}: works; a shortest drive {w}; first-siding outputs with no 2-3-1: {len(via)}, e.g. '
          + ', '.join(S(o) for o in sorted(via, reverse=True)[:3]))
    check(tuple(sorted(p, reverse=True)) in via, f'P8 {s} reverse route')
for n in range(1, 7):
    check(all(ok2(p) for p in permutations(range(1, n + 1))), f'two sidings n={n}')
seven = list(permutations(range(1, 8)))
bad = [p for p in seven if not ok2(p)]
print('seven-car trains failing with two long sidings:', len(bad))
check(len(bad) == 22, '22')
print('   ', ' / '.join(S(p) for p in bad))
print('   all end in car 1:', all(p[-1] == 1 for p in bad))
# characterisation used in the guide: two sidings work iff some output of the
# first siding has no 2-3-1 pattern
for n in range(1, 7):
    for p in permutations(range(1, n + 1)):
        check(ok2(p) == any(not has231(o) for o in stack_outputs(p)), 'two-siding criterion')
for p in bad[:22]:
    check(not any(not has231(o) for o in stack_outputs(p)), 'criterion on failures')
print('failing with 5-place sidings (not the page rule):', sum(1 for p in seven if not ok2(p, 5)))

print('=== Extra claims in the guide')
printed = (K1['P1'] + K1['P2'] + K1['P4'] + G23['P3'] + G23['P5'] + G45P2 +
           ['2143', '4321', '1324', '3124', '231', '3412', '25341'])
check(all(len(x) >= 3 for x in printed), 'launch train 2 1 is not a printed train')
check(max(height(T(x)) for x in G45P2) == 4, '4-5 P2 needs at most four places')
check([sum(1 for p in four_good if p.index(4) == j) for j in range(4)] == [5, 2, 2, 5], '4-5 P1 by position of 4')
check({f: sum(1 for p in four_good if p[0] == f) for f in range(1, 5)} == {1: 5, 2: 2, 3: 2, 4: 5}, 'by first car')
def first_siding(train, moves):
    """Apply 'in'/'out' moves to one siding; return the order cars leave."""
    st, out, i = [], [], 0
    for m in moves.split():
        if m == 'in':
            st.append(train[i]); i += 1
        else:
            out.append(st.pop())
    assert i == len(train) and not st
    return tuple(out)
for tr, mv, want in [('231', 'in in out out in out', (3, 2, 1)),
                     ('3412', 'in in out out in in out out', (4, 3, 2, 1)),
                     ('25341', 'in in out in in out out out in out', (5, 4, 3, 2, 1))]:
    got = first_siding(T(tr), mv)
    check(got == want and ok1(got), f'P8 drive {tr}')
    print(f'   P8 {tr}: first siding sends out {S(got)}; second siding sorts it: {ok1(got)}')
# K-1 P6 reasons: start with 2 works only if 1 is next; start with 3 only if 4 is last
for p in permutations(range(1, 5)):
    if p[0] == 2:
        check(ok1(p) == (p[1] == 1), 'start 2')
    if p[0] == 3:
        check(ok1(p) == (p[3] == 4), 'start 3')
# 2-3 P4 tempting rules fail
check(ok1((1, 2, 3)) and ok1((3, 2, 1)), 'tempting rules')
# 4-5 P5 by lettered cars equals decode (same algorithm, stated for completeness)
print('extra claims checked')

print('=== Revision checks (final guide)')
def first_trouble(train):
    """Drive by the never-fails rule. Return (x, y, m) at the first moment a car
    y is parked on a smaller car x, with m the car needed then, or None."""
    st, need, i = [], 1, 0
    while True:
        if st and st[-1] == need:
            st.pop(); need += 1
        elif i < len(train):
            y = train[i]
            if st and st[-1] < y:
                return (st[-1], y, need)
            st.append(y); i += 1
        else:
            return None
def is231(train, t):
    x, y, m = t
    return m < x < y and train.index(x) < train.index(y) < train.index(m)
# Must-fix 1 / K-1 key: a train is stuck exactly when the never-fails drive parks
# a bigger car on a smaller one while the needed car has not arrived yet, and that
# moment is a middle, largest, smallest triple.
for n in range(1, 8):
    for p in permutations(range(1, n + 1)):
        t = first_trouble(p)
        check((t is None) == ok1(p), f'first trouble iff stuck {p}')
        if t:
            x, y, m = t
            check(m not in p[:p.index(y)], f'needed car not yet arrived {p}')
            check(is231(p, t), f'first trouble is a 2-3-1 {p}')
# ... while a wrong move (3 parked on 1) strands the good train 1 3 2
def stuck_after(train, prefix):
    """Can the drive still finish in order after the moves in prefix?"""
    st, out, i = [], [], 0
    for c in prefix:
        if c == 'U':
            st.append(train[i]); i += 1
        else:
            out.append(st.pop())
    if out != list(range(1, len(out) + 1)):
        return True
    need = len(out) + 1
    def rec(i, st, need):
        if need > len(train): return True
        if st and st[-1] == need and rec(i, st[:-1], need + 1): return True
        if i < len(train) and rec(i + 1, st + [train[i]], need): return True
        return False
    return not rec(i, st, need)
check(ok1((1, 3, 2)) and stuck_after((1, 3, 2), 'UU'), '1 3 2 with 3 parked on 1 is stranded')
print('   1 3 2 works, but after 1 in, 3 in (3 parked on 1) it is stranded:', stuck_after((1, 3, 2), 'UU'))

# Printed triples: each is the drive's first trouble (x, y, m)
printed_triples = {
    # K-1 Problems 2 and 4: "y waits on x"
    '3412': (3, 4), '4231': (2, 3), '1342': (3, 4),
    '45123': (4, 5), '13524': (3, 5), '32514': (2, 5),
    # Grades 2-3 Problems 3 and 5
    '24351': (2, 4, 1), '45321': (4, 5, 1), '31542': (3, 5, 2), '15342': (3, 4, 2),
    '42513': (2, 5, 1), '34521': (3, 4, 1), '53412': (3, 4, 1),
    # Grades 4-5 Problem 2
    '24153': (2, 4, 1), '13542': (3, 5, 2), '361245': (3, 6, 1), '214635': (4, 6, 3),
    '41328675': (6, 7, 5),
}
for s, want in printed_triples.items():
    t = first_trouble(T(s))
    check(t is not None and t[:len(want)] == want, f'printed triple {s} {want} vs drive {t}')
    check(is231(T(s), t), f'triple is 2-3-1 {s}')
print('   drive triples:', ', '.join(f'{s}:{S(first_trouble(T(s)))}' for s in printed_triples))
# the old draft triples were valid 2-3-1s too (any triple is right)
for s, t in [('45321', (4, 5, 3)), ('42513', (4, 5, 1)), ('34521', (3, 4, 2))]:
    check(is231(T(s), t), f'draft triple {s} still a 2-3-1')

# K-1 key: marks row by row, left box then right box, as on the pages
def rows(trains):
    m = ['\u2713' if ok1(T(x)) else '\u2717' for x in trains]
    return ' / '.join(' '.join(m[i:i + 2]) for i in range(0, len(m), 2))
k1rows = {k: rows(v) for k, v in K1.items()}
print('   K-1 key rows:', k1rows)
check(k1rows['P1'] == '\u2713 \u2713 / \u2713 \u2717 / \u2713 \u2713', 'K-1 key P1 rows')
check(k1rows['P2'] == '\u2713 \u2717 / \u2713 \u2713 / \u2717 \u2713 / \u2713 \u2717', 'K-1 key P2 rows')
check(k1rows['P4'] == '\u2717 \u2713 / \u2713 \u2713 / \u2717 \u2717', 'K-1 key P4 rows')

# Grades 2-3 Problem 7 extension: 132 with a long siding, 131 on the five-place mat
six = list(permutations(range(1, 7)))
long6, mat6 = sum(ok1(p) for p in six), sum(ok1(p, 5) for p in six)
lost = [S(p) for p in six if ok1(p) and not ok1(p, 5)]
print('   six cars: long siding', long6, ' five-place mat', mat6, ' lost', lost)
check(long6 == 132 and mat6 == 131 and lost == ['6 5 4 3 2 1'], '2-3 P7 extension')
check([sum(1 for p in six if ok1(p) and p.index(6) == j) for j in range(6)] == [42, 14, 10, 10, 14, 42], 'by where car 6 sits')

# Theorem 3: insertion counts C_n as the total of allowed gaps over working (n-1)-trains
for n in range(2, 8):
    prev = [p for p in permutations(range(1, n)) if ok1(p)]
    g = sum(1 for p in prev for i in range(n) if ok1(p[:i] + (n,) + p[i:]))
    check(g == cat[n - 1], f'insertion total n={n}')
    check(all(sum(1 for i in range(n) if ok1(p[:i] + (n,) + p[i:])) ==
              sum(1 for i in range(n) if all(a < b for a in p[:i] for b in p[i:])) for p in prev),
          f'insertion gap rule n={n}')
print('   insertion totals n=2..7 equal Catalan numbers: checked')

# 4-5 Problem 7: first-car split gives the same terms; first car f <-> first return at step 2f
for n, want in [(5, [14, 5, 4, 5, 14]), (6, [42, 14, 10, 10, 14, 42])]:
    good = [p for p in permutations(range(1, n + 1)) if ok1(p)]
    byf = [sum(1 for p in good if p[0] == f) for f in range(1, n + 1)]
    check(byf == want, f'first-car split n={n}')
    for p in good:
        w = drives(p)[0]
        h, k = 0, None
        for idx, c in enumerate(w):
            h += 1 if c == 'U' else -1
            if h == 0:
                k = idx + 1; break
        check(k == 2 * p[0], f'first return at 2f {p}')
print('   first-car split 5: [14,5,4,5,14], 6: [42,14,10,10,14,42]; first return at step 2 x first car: checked')

# 4-5 Problem 1 sharing by first car: 5, 2, 2, 5 (already above); 6 trains per first car
check(all(sum(1 for p in permutations(range(1, 5)) if p[0] == f) == 6 for f in range(1, 5)), 'six per first car')

# Launch figure: 2 1, partway after 2 in, 1 in, 1 out -> siding [2], departed [1]
st, out = [], []
tr = [2, 1]
for c in 'UUD':
    if c == 'U': st.append(tr.pop(0))
    else: out.append(st.pop())
check(st == [2] and out == [1] and tr == [], 'launch partway state')
print('   launch partway (2 in, 1 in, 1 out): siding', st, 'departed', out)

# Print: arrival-track length on the mat (from the mat's TikZ source)
import re, os
mat = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', '..',
                   'plans', 'topic-scouting', 'drafts', 'train-yard-sorting', 'src', 'track-mat.tex')
mat = os.path.normpath(mat)
if os.path.exists(mat):
    src = open(mat).read()
    xr = float(re.search(r'\\fill\[black!7\] \(-2,167\) rectangle \(([\d.]+),196\)', src).group(1))
    xs = float(re.search(r'\\draw\[black!55, line width=1pt\] \(([\d.]+),167\) -- \(' + str(xr), src).group(1))
    page = 279.4
    arr = min(xr, page) - xs
    print(f'   arrival track on paper: {arr:.1f} mm; 25 mm squares: {int(arr // 25)}, 2 cm cubes: {int(arr // 20)}'
          ' (less after printer margins)')
    check(4 <= arr // 25 <= 5 and arr // 20 >= 5, 'arrival track about four or five cars')
else:
    print('   track-mat.tex not found; arrival-track length not rechecked')

print()
print('ALL CHECKS PASSED' if failures == 0 else f'{failures} CHECKS FAILED')
raise SystemExit(1 if failures else 0)
