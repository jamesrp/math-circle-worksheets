#!/usr/bin/env python3
"""Root review checks derived independently from mathematical definitions."""
from itertools import permutations, combinations, product
from collections import Counter
from pathlib import Path
import json, math
checks={}
for n in (3,4):
    rows=list(permutations(range(n)))
    squares=[]
    def extend(sofar):
        if len(sofar)==n:
            squares.append(tuple(sofar));return
        for row in rows:
            if all(all(old[c]!=row[c] for old in sofar) for c in range(n)):
                extend(sofar+[row])
    extend([])
    trades=Counter(); peaks=Counter();diagonal=0
    for s in squares:
        t=sum(s[a][c]==s[b][d] and s[a][d]==s[b][c]
              for a,b in combinations(range(n),2) for c,d in combinations(range(n),2))
        trades[t]+=1
        diagonal+=len({s[i][i] for i in range(n)})==n and len({s[i][n-i-1] for i in range(n)})==n
        k=sum(all(not(0<=r<n and 0<=c<n) or s[r][c]<s[a][b]
                   for r,c in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)))
              for a in range(n) for b in range(n))
        peaks[k]+=1
    checks[f'latin_{n}']={'total':len(squares),'intercalates':dict(trades),'both_diagonals':diagonal,'local_peaks':dict(peaks)}
patterns=[''.join(v) for v in product('RB',repeat=6) if v.count('R')==3]
def rotations(w):return [w[i:]+w[:i] for i in range(len(w))]
checks['six_bead_necklaces']={'labeled':len(patterns),'rotations':len({min(rotations(w)) for w in patterns}),
                            'rotations_and_reflections':len({min(rotations(w)+rotations(w[::-1])) for w in patterns})}
for n in (3,4,5,6,7,8,9):
    results=Counter()
    for p in product(range(2),repeat=n):
        lamps=tuple((p[i]+p[(i-1)%n]+p[(i-2)%n])%2 for i in range(n))
        results[lamps]+=1
    checks[f'triple_ring_{n}']={'reachable':len(results),'press_choices_each':sorted(set(results.values()))}
for n in (3,4,5,6):
    ps=list(permutations(range(n)))
    squares={tuple(p[p[i]] for i in range(n)) for p in ps}
    def criterion(q):
        visited=set();lens=Counter()
        for i in range(n):
            if i in visited:continue
            j=i;k=0
            while j not in visited:
                visited.add(j);k+=1;j=q[j]
            lens[k]+=1
        return all(length%2 or count%2==0 for length,count in lens.items())
    assert all((p in squares)==criterion(p) for p in ps)
    checks[f'machine_square_roots_{n}']={'target_permutations':len(ps),'rootable_targets':len(squares),'criterion_all_verified':True}
Path(__file__).with_name('independent-small-cases.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
