#!/usr/bin/env python3
from itertools import product
from collections import Counter
import json
D={'A':[2,4,9],'B':[1,6,8],'C':[3,5,7]}
triples=Counter(max(zip(t,D),key=lambda p:p[0])[1] for t in product(*D.values()))
sums={k:Counter(x+y for x,y in product(v,repeat=2)) for k,v in D.items()}
pairs={}
for a,b in [('A','B'),('B','C'),('C','A')]:
 c=Counter('first' if sum(x)>sum(y) else 'second' if sum(x)<sum(y) else 'tie' for x in product(D[a],repeat=2) for y in product(D[b],repeat=2))
 pairs[a+b]=dict(c)
payoffs={a:{b:sum(2*(x>y)+(x==y) for x,y in product(D[a],D[b]))/9 for b in D} for a in D}
assert triples=={'A':10,'B':10,'C':7}
assert pairs['AB']=={'first':37,'second':44}
assert pairs['BC']=={'first':39,'second':38,'tie':4}
assert pairs['CA']=={'first':39,'second':38,'tie':4}
assert 6 in D['B'] and 4 in D['A']
assert (2*(6>4)+(6==4), 2*(4>6)+(4==6)) == (2,0)
print(json.dumps({'champions':triples,'sum_multiplicities':sums,'two_draw_pairs':pairs,'single_draw_points':payoffs},indent=2))
