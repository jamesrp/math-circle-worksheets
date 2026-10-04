#!/usr/bin/env python3
from itertools import product

def gap(s):return tuple(abs(s[(i+1)%len(s)]-s[i]) for i in range(len(s)))
def directed(s):return tuple(s[(i+1)%len(s)]-s[i] for i in range(len(s)))
def trajectory(s,op,m):
    ans=[s]
    for _ in range(m):s=op(s);ans.append(s)
    return ans

if __name__=='__main__':
    assert gap((1,3,2,0))==(2,1,2,1)
    assert directed((1,3,3,1))==(2,0,-2,0)
    for target,count in [((1,1,1,1),6),((1,2,1,2),4)]:
        pred=[v for v in product(range(4),repeat=4) if min(v)==0 and gap(v)==target]
        assert len(pred)==count;print('Target',target,'normalized predecessors:',pred)
    s=(1,0,0,1,0,0);run=trajectory(s,gap,10)
    assert (0,0,0,0,0,0) not in run and run[1]==run[4]
    print('Six ring:',run[:5])
    maxlife=0
    for s in product((0,1),repeat=8):
        run=trajectory(s,gap,8);assert run[8]==(0,)*8
        maxlife=max(maxlife,next(i for i,v in enumerate(run) if v==(0,)*8))
    assert maxlife==8
    run=trajectory((1,0,0,0,0,0,0,0),gap,8)
    assert any(run[7]) and not any(run[8]);print('All 256 eight-starts vanish by 8; witness lasts 8.')
    for st in ((0,1,0,1),(0,0,1,1)):
        run=trajectory(st,directed,8);print('Directed',st,run[:6])
    assert trajectory((0,1,0,1),directed,5)[5]==(16,-16,16,-16)

    first=trajectory((0,1,0,1),directed,5)
    second=trajectory((0,0,1,1),directed,5)
    assert max(abs(x) for state in first for x in state)==16
    assert max(abs(x) for state in second for x in state)==4
    assert all(sum(state)==0 for state in first[1:]+second[1:])
    print("Five-round comparison: first reaches 16; second only 4. Directed outputs sum to zero.")
