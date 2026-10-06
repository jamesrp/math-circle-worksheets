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
