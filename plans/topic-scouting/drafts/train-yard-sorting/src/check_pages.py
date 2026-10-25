#!/usr/bin/env python3
"""Answer key for every train, path and insertion task printed in the packets."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify import greedy, has231, path_to_train, two_sidings, is_mountain

def t(s): return tuple(int(c) for c in s.split())

def max_height(p):
    """Most cars in the siding if one keeps driving by the never-fails method,
    even past the point where the train is stuck (the mat holds 5)."""
    st, need, i, m = [], 1, 0, 0
    while True:
        if st and st[-1] == need:
            st.pop(); need += 1
        elif i < len(p):
            st.append(p[i]); i += 1; m = max(m, len(st))
        else:
            return m


def show(label, trains):
    print(label)
    for s in trains:
        p = t(s)
        g = greedy(p)
        assert (g is not None) == (not has231(p))
        h = max_height(p)
        assert h <= 5
        print(f'  {s:<18} {"works " + g if g else "STUCK":<24} siding needs {h}')

K1 = {
 'K-1 P1': ['1 2 3','1 3 2','2 1 3','2 3 1','3 1 2','3 2 1'],
 'K-1 P2': ['2 1 4 3','3 4 1 2','4 3 2 1','1 4 3 2','4 2 3 1','3 1 2 4','4 1 3 2','1 3 4 2'],
 'K-1 P4': ['4 5 1 2 3','2 1 5 4 3','5 4 3 2 1','5 1 3 2 4','1 3 5 2 4','3 2 5 1 4'],
}
G23 = {
 '2-3 P3': ['3 2 1 5 4','4 1 3 2 5','2 4 3 5 1','1 2 5 3 4','4 5 3 2 1','3 1 5 4 2','5 2 1 4 3','1 5 3 4 2'],
 '2-3 P5': ['4 2 5 1 3','1 4 2 3 5','3 4 5 2 1','5 3 4 1 2','5 4 1 3 2','2 1 5 3 4'],
}
G45 = {
 '4-5 P2': ['3 1 2 5 4','2 4 1 5 3','1 3 5 4 2','5 1 4 2 3','3 6 1 2 4 5','2 1 4 6 3 5',
            '1 7 2 6 3 5 4','3 2 1 7 6 4 5','4 1 3 2 8 6 7 5','4 3 1 2 8 5 7 6'],
}
for d in (K1, G23, G45):
    for k, v in d.items(): show(k, v)

# K-1 P3: trains ending in car 1
from itertools import permutations
print('K-1 P3 trains x y z 1:')
for p in permutations((2,3,4)):
    q = p + (1,)
    print('  ', q, 'works' if greedy(q) else 'stuck')
print('K-1 P6: four-car trains that cannot leave in order:',
      sum(1 for p in permutations(range(1,5)) if not greedy(p)))

# 2-3 P6: where can car 5 go
print('2-3 P6 insertion of car 5:')
for s in ['2 1 4 3','4 3 2 1','1 3 2 4','3 1 2 4']:
    p = t(s)
    ok = []
    for i in range(5):
        q = p[:i] + (5,) + p[i:]
        ok.append('Y' if greedy(q) else '.')
        rule = all(a < b for a in p[:i] for b in p[i:])
        assert rule == bool(greedy(q))
    print(f'  {s}: slots {"".join(ok)}')

# 4-5 P4 worked example and P5 paths
print('Worked example 1 3 2 ->', greedy((1,3,2)))
for w in ['UDUUUDDUDD','UUUDDUUDDD','UUDUUDDDUD','UUUUDDDUDD']:
    assert is_mountain(w)
    print('  path', w, '-> train', path_to_train(w))

# 4-5 P8 two sidings
print('4-5 P8 two sidings (siding length 5):')
for s in ['2 3 1','3 4 1 2','2 5 3 4 1']:
    print('  ', s, two_sidings(t(s), cap=5))

# 2-3 P7 and 4-5 P7: counts (siding long enough to hold every car)
from verify import sortable_bfs
four = [p for p in permutations(range(1, 5)) if greedy(p)]
gaps = sum(sum(1 for i in range(5) if greedy(p[:i] + (5,) + p[i:])) for p in four)
print('2-3 P7: five-car trains that leave in order =', 
      sum(1 for p in permutations(range(1, 6)) if greedy(p)),
      '; allowed gaps summed over the 14 four-car trains =', gaps)
print('4-5 P7: six-car trains, long siding:',
      sum(1 for p in permutations(range(1, 7)) if sortable_bfs(p)),
      '; with a 5-car siding:',
      sum(1 for p in permutations(range(1, 7)) if sortable_bfs(p, cap=5)))
print('4-5 P8: seven-car trains that fail with two long sidings:',
      sum(1 for p in permutations(range(1, 8)) if not two_sidings(p)))
for s in ['2 3 1', '3 4 1 2', '2 5 3 4 1']:
    assert two_sidings(t(s))

# Answer positions in the two-column check grids
print('Answer layout (rows, columns):')
for d in (K1, G23, G45):
    for k, v in d.items():
        if k.endswith('P1'):
            continue
        m = ['Y' if greedy(t(s)) else 'x' for s in v]
        rows = [''.join(m[i:i + 2]) for i in range(0, len(m), 2)]
        print(f'  {k}: rows {" ".join(rows)}  left {"".join(m[0::2])}  right {"".join(m[1::2])}')
