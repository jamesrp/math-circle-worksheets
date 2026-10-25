"""Check every answer used on the Week 91 K-1 pages by simulation."""
from itertools import product, permutations
from math import comb

def switch(first, n):
    """One switch: 'X' or 'Y' first arrow; returns arrival word."""
    a, out = first, []
    for _ in range(n):
        out.append(a)
        a = 'Y' if a == 'X' else 'X'
    return ''.join(out)

def tree(start, n):
    """start = (top, left, right), each 'L' or 'R'. Returns arrival word."""
    top, left, right = start
    out = []
    flip = {'L': 'R', 'R': 'L'}
    for _ in range(n):
        side = top; top = flip[top]
        if side == 'L':
            out.append('A' if left == 'L' else 'B'); left = flip[left]
        else:
            out.append('C' if right == 'L' else 'D'); right = flip[right]
    return ''.join(out)

STARTS = [''.join(s) for s in product('LR', repeat=3)]

# Problem 1: no two in a row, any start, 10 counters
for f in 'XY':
    w = switch(f, 10)
    assert all(w[i] != w[i+1] for i in range(9)), w
    print('P1', f, w)

# Problem 2: piles
targets2 = [(2,1),(3,3),(2,3),(5,2),(5,4),(3,5)]
for x, y in targets2:
    ok = [f for f in 'XY' if (switch(f, x+y).count('X'), switch(f, x+y).count('Y')) == (x, y)]
    print('P2', f'X{x} Y{y} ({x+y} counters):', ok or 'impossible')

# Problem 3: coin with 7 tosses, six printed rows
words = [''.join(w) for w in product('XY', repeat=7)]
dbl = sum(any(w[i]==w[i+1] for i in range(6)) for w in words)
five2 = sum(w.count('X') in (5, 2) for w in words)       # 5 on one exit, 2 on the other
p = five2 / len(words)
print('P3 7 tosses: two-in-a-row', dbl, '/', len(words), '; 5 and 2 either way', five2, '/', len(words),
      '=', round(p, 3), '; seen within 6 rows:', round(1 - (1 - p)**6, 3))
assert dbl == 126 and five2 == 42
# the switch never gives 5 and 2 from 7 counters, from either start
assert all(switch(f, 7).count('X') in (4, 3) for f in 'XY')

# Problem 4: guess counter k after seeing counter 1
for k in [5, 8, 7, 4]:
    for f in 'XY':
        w = switch(f, k)
        assert w[k-1] == (f if k % 2 else ('Y' if f=='X' else 'X'))
    print('P4 counter', k, 'lands', 'same as counter 1' if k % 2 else 'on the other exit')

# Problem 5: first four counters on four different exits, every start
for s in STARTS:
    w = tree(s, 48)
    for i in range(len(w)-3):
        assert len(set(w[i:i+4])) == 4
    assert w[4:8] == w[:4]
    print('P5', s, w[:8])

# Problem 6: piles after 6, 8 or 12 counters (the pictures printed by build.py)
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from build import P6, P2, P9
assert P2 == targets2 and P9 == ['AD', 'DC', 'CB', 'BA']
def piles(w):
    return tuple(w.count(c) for c in 'ABCD')
for n, t in P6:
    assert sum(t) == n
    ok = [s for s in STARTS if piles(tree(s, n)) == t]
    print('P6', n, 'counters', dict(zip('ABCD', t)), ok or 'impossible')
for n in (6, 8, 12):
    print(f'P6 all reachable after {n}:', sorted(set(piles(tree(s, n)) for s in STARTS)))

# Spare cards: the board's cards after a trial usually do not show the start.
def board_after(start, n):
    flip = {'L': 'R', 'R': 'L'}
    top, left, right = start
    for _ in range(n):
        side = top; top = flip[top]
        if side == 'L': left = flip[left]
        else: right = flip[right]
    return top + left + right
for n in (1, 2, 4, 5, 6, 8):
    same = [s for s in STARTS if board_after(s, n) == s]
    print(f'board shows the start after {n} counters for', len(same), 'of 8 starts')

# Problem 7: B first to get two; B last to get two
def second_time(w, c):
    seen = 0
    for i, ch in enumerate(w, 1):
        if ch == c:
            seen += 1
            if seen == 2:
                return i
first, last = [], []
for s in STARTS:
    w = tree(s, 8)
    t = {c: second_time(w, c) for c in 'ABCD'}
    if t['B'] == min(t.values()): first.append((s, t['B']))
    if t['B'] == max(t.values()): last.append((s, t['B']))
print('P7 B first to two:', first)
print('P7 B last to two:', last)

# Problem 8: first counter on C
print('P8 first on C:', [s for s in STARTS if tree(s,1) == 'C'])

# Problem 9: first two counters
for pair in ['AD', 'DC', 'CB', 'BA']:
    print('P9', pair[0], 'then', pair[1], ':', [s for s in STARTS if tree(s,2) == pair] or 'impossible')

# Older packet's targets to avoid (first two letters)
print('orders:', {s: tree(s,4) for s in STARTS})
