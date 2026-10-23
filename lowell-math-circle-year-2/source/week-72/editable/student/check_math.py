#!/usr/bin/env python3
"""Independent exact state checks for the student investigations."""
from itertools import permutations

def run(word, start=(0,0,0)):
    x,y,z=start
    for c in word:
        if c=='E': x+=1
        elif c=='W': x-=1
        elif c=='N': y+=1; z+=x
        elif c=='S': y-=1; z-=x
        else: raise ValueError(c)
    return x,y,z
assert run('EENE')==(3,1,2)
monotone={''.join(w):run(w)[2] for w in set(permutations('EENN'))}
assert monotone=={'EENN':4,'ENEN':3,'ENNE':2,'NEEN':2,'NENE':1,'NNEE':0}
loops={''.join(w):run(w)[2] for w in permutations('ENWS')}
assert set(loops.values())=={-1,0,1}
for x in [0,2,-3]:
    assert run('EENWWS',(x,0,0))==(x,0,2)
    assert run('NEESWW',(x,0,0))==(x,0,-2)
assert run('EENWNWSS')==(0,0,3)
assert run('NNEE'+'ENWS'*7)==(2,2,7)
assert run('NNEE'+'NESW'*3)==(2,2,-3)
# Translation adds x_start * vertical displacement. Closed loops have displacement 0.
for k in range(-30,31):
    loop='ENWS' if k>=0 else 'NESW'
    assert run('NNEE'+loop*abs(k))==(2,2,k)
print('PASS: worked example, all 6 monotone routes, all 24 four-card loops, translated loops and signed-memory constructions.')

from collections import Counter
assert Counter(loops.values())=={-1:4,0:16,1:4}
# Short concrete witnesses stay inside the printed final board.
for word,wanted in [('EEEENWNW',7),('NNNENESS',-3)]:
    assert run(word)==(2,2,wanted)
    states=[run(word[:j]) for j in range(len(word)+1)]
    assert all(-1<=x<=4 and -1<=y<=4 for x,y,z in states)
    assert all(-10<=z<=10 for x,y,z in states)
# General constructions can add memory before first arriving at the ring.
for k in range(-50,51):
    word=('ENWS' if k>=0 else 'NESW')*abs(k)+'NNEE'
    assert run(word)==(2,2,k)
    assert all(run(word[:j])[:2]!=(2,2) for j in range(len(word)))
# The apparatus is not a bound on memory. Extensions overlap just one tick.
main=list(range(-10,11));left=list(range(-20,-9));right=list(range(10,21))
assert left[-1]==main[0] and main[-1]==right[0]
joined=left[:-1]+main+right[1:]
assert joined==list(range(-20,21))
print('PASS: 24-loop memory multiplicities, short concrete routes, 101 all-integer construction samples, and signed-strip extension convention.')
