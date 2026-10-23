#!/usr/bin/env python3
"""Check the statements changed in the October 23, 2026 guide corrections (Week 25).

Standard library only; nothing is imported from the packet or guide builders.
Run from anywhere: python3 review/verify_card_fixes_2026_10_23.py
"""
from collections import defaultdict, deque
from itertools import combinations

def pic(s):
    return tuple(tuple(int(ch) for ch in row) for row in s.split('/'))

def margins(a):
    return tuple(map(sum, a)), tuple(map(sum, zip(*a)))

def switches(a):
    r, c = len(a), len(a[0])
    for i, j in combinations(range(r), 2):
        for k, l in combinations(range(c), 2):
            if a[i][k] == a[j][l] and a[i][l] == a[j][k] and a[i][k] != a[i][l]:
                b = [list(row) for row in a]
                for x, y in ((i, k), (i, l), (j, k), (j, l)):
                    b[x][y] = 1 - b[x][y]
                b = tuple(map(tuple, b))
                emptied = sum(a[x][y] == 1 and b[x][y] == 0 for x in range(r) for y in range(c))
                assert emptied == 2 and margins(b) == margins(a)
                yield b

def dist(a):
    d = {a: 0}
    q = deque([a])
    while q:
        x = q.popleft()
        for y in switches(x):
            if y not in d:
                d[y] = d[x] + 1
                q.append(y)
    return d

def to_empty(a, b):
    return sum(x == 1 and y == 0 for ra, rb in zip(a, b) for x, y in zip(ra, rb))

checks = []

# 1. Grades 2-3 P4 held hint: the counter-counting lower bound is valid.
start, target = pic('1100/0011'), pic('0011/1100')
assert to_empty(start, target) == 4            # A1, A2, B3, B4 must be emptied
d = dist(start)
assert d[target] == 2 and target not in set(switches(start))
checks.append('P4: A1, A2, B3, B4 must be emptied; each switch empties exactly two cells; distance is 2 and no single switch reaches the target')

pairs = 0
for r, c in [(2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (2, 6)]:
    groups = defaultdict(list)
    for n in range(1 << (r * c)):
        a = tuple(tuple((n >> (i * c + j)) & 1 for j in range(c)) for i in range(r))
        groups[margins(a)].append(a)
    for aa in groups.values():
        if len(aa) < 2:
            continue
        for a in aa:
            da = dist(a)
            for b in aa:
                assert da[b] >= (to_empty(a, b) + 1) // 2
                pairs += 1
checks.append(f'bound "switches >= (cells to empty)/2" holds on all {pairs} ordered same-count pairs on 2x3, 2x4, 2x5, 3x3, 3x4 and 2x6 boards')

# The bound can be strict beyond two rows (so the hint claims only "at least").
diag = pic('1000/0100/0010/0001'); shift = pic('0100/0010/0001/1000')
assert to_empty(diag, shift) == 4 and dist(diag)[shift] == 3
checks.append('beyond two rows the bound is only a lower bound: the 4x4 diagonal to its cyclic shift empties 4 cells and needs 3 switches')

# 2. New launch picture A1, A2, B1 on a 2-by-3 board.
launch = pic('110/100')
rows, cols = margins(launch)
assert (rows, cols) == ((2, 1), (2, 1, 0))
same = [a for n in range(64) for a in [tuple(tuple((n >> (i * 3 + j)) & 1 for j in range(3)) for i in range(2))] if margins(a) == (rows, cols)]
assert same == [launch]
checks.append('launch A1, A2, B1: rows 2, 1 and columns 2, 1, 0; it is the only picture with these counts')

old = pic('101/010')
olds = [a for n in range(64) for a in [tuple(tuple((n >> (i * 3 + j)) & 1 for j in range(3)) for i in range(2))] if margins(a) == margins(old)]
assert len(olds) == 3
# Margins of every printed student task (from facilitator-src/verify_math.py cases).
tasks = [([1,1],[1,1]),([1,1],[1,0,1]),([2,1],[1,1,1]),([1,2],[1,1,1]),([1,1,1],[1,1,1]),([3,1],[2,1,1]),
         ([2,1,0],[2,1,0]),([2,1,1],[2,1,1]),([2,2],[2,1,1]),([1,0,1],[1,0,1]),([2,2],[1,1,1,1]),
         ([3,3],[1]*6),([3,3],[2,1,0,1,1,1])]
assert ([2,1],[1,1,1]) in tasks and ([2,1],[2,1,0]) not in tasks
checks.append('old launch A1, A3, B2 (rows 2, 1; columns 1, 1, 1) has 3 pictures and is a printed task; the new 2-by-3 counts are not a printed task')

# 3. Supplies: largest side-by-side comparison per pair is two six-counter pictures.
largest = max(sum(map(sum, pic(s))) for s in ['111/110/100', '111000/000111', '110100/100011'])
assert largest == 6
assert 2 * 2 * largest == 24 and 2 * (4 + 4) == 16
checks.append('largest printed pictures have 6 counters; two pairs each comparing two of them need 24; four-counter partner tasks need 8 per pair')

for c in checks:
    print('PASS', c)
print(f'PASS: {len(checks)} Week 25 correction checks')
