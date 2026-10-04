#!/usr/bin/env python3
"""Independent exhaustive transition and history checks (standard library only)."""
from itertools import product
from collections import Counter

def states_after(word):
    ans=set()
    for start in product('RB',repeat=3):
        s=start
        for op in word:
            s=('R',s[1],s[2]) if op=='S' else (s[1],s[2],s[0])
        ans.add(s)
    return ans

if __name__=='__main__':
    for m in (3,4):
        covered=sum(set(h)=={1,2,3} for h in product((1,2,3),repeat=m))
        assert covered=={3:6,4:36}[m]
        print(f'{m} draws: {covered}/{3**m} covering histories')
    for n in range(6):
        words=[''.join(w) for w in product('ST',repeat=n) if len(states_after(w))==1]
        assert bool(words)==(n==5)
        if words: print('Shortest universal words:',words)
    # Any copies preserve monochromatic starts; one reset plus two copies suffice.
    for st in product('RB',repeat=3):
        s=list(st);s[0]='R';s[1]=s[0];s[2]=s[0];assert s==list('RRR')
    print('All 8 starts checked for S, COPY 1 to 2, COPY 1 to 3.')
