from itertools import product
from math import lcm
import json

def period(w):return next(s for s in range(1,len(w)+1) if all(w[i]==w[(i+s)%len(w)] for i in range(len(w))))
def edits(w,s):
 valid=[v for v in product('RB',repeat=len(w)) if all(v[i]==v[(i+s)%len(w)] for i in range(len(w)))]
 costs=[sum(a!=b for a,b in zip(w,v)) for v in valid]
 k=min(costs);return k,[''.join(v) for v,d in zip(valid,costs) if d==k]
def bad(w):return sum(w[i]==w[(i+1)%len(w)] for i in range(len(w)))
assert period('RBB')==3 and period('RBBB')==4
assert lcm(period('RBB'),period('RBBB'))==12
assert lcm(period('RB'),period('RBB'))==6
assert lcm(period('RB'),period('RBBBBBBB'))==8
repairs={}
for w,s,k in [('RBBBRB',3,2),('RBBBBRRB',2,3),('RRBBRB',2,2)]:
 got,vs=edits(w,s);assert got==k;repairs[w]={'slide':s,'minimum':got,'all_optimal_repairs':vs}
rings={n:min(bad(w) for w in product('AB',repeat=n)) for n in [5,6,7,8]};assert rings=={5:1,6:0,7:1,8:0}
print(json.dumps({'layer_period':12,'recolorings':repairs,'minimum_equal_neighbors':rings},indent=2))

# Revised conventions and finite material counts.
assert sum(a != b for a,b in zip('RBB','RRB')) == 1
assert 'RRB'*2 == 'RRBRRB'
assert ('RBB'*8+'RBBB'*6).count('R') == 14
assert ('RBB'*8+'RBBB'*6).count('B') == 34
assert ('RB'*12+'RBBBBBBB'*3).count('R') == 15
assert ('RB'*12+'RBBBBBBB'*3).count('B') == 33
assert 6*48 == 288
