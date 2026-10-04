from itertools import product
from math import cos, sin, pi
import json
from pathlib import Path
# Obtain actual vertex maps from planar orthogonal transformations.
result={}
for n in range(3,11):
    z=[complex(cos(2*pi*i/n),sin(2*pi*i/n)) for i in range(n)]
    maps=[]
    for flip in (False,True):
        for k in range(n):
            if not flip and k==0: continue
            image=[(v.conjugate() if flip else v)*z[k] for v in z]
            maps.append([min(range(n),key=lambda j:abs(z[j]-v)) for v in image])
    def asymmetric(w): return not any(all(w[i]==w[m[i]] for i in range(n)) for m in maps)
    good=[w for w in product(range(2),repeat=n) if asymmetric(w)]
    result[n]={"binary_asymmetric_count":len(good),"least_minority":min((min(sum(w),n-sum(w)) for w in good),default=None)}
    assert bool(good)==(n>=6)
    if n<6: assert asymmetric(tuple([0]*(n-2)+[1,2]))
    else: assert asymmetric(tuple(int(i in (0,1,3)) for i in range(n)))
# A successful square has one-counter changes of both kinds.
n=4
w=(0,0,1,2)
def survives(w): return any(all(w[i]==w[(a*i+b)%4] for i in range(4)) for a in (-1,1) for b in range(4) if (a,b)!=(1,0))
changes=[survives(w[:i]+(v,)+w[i+1:]) for i in range(4) for v in range(3) if v!=w[i]]
assert set(changes)=={True,False}
# Two non-equivalent asymmetric eight-rings exist even with category names fixed.
w1=(1,1,0,1,0,0,0,0);w2=(1,1,0,0,1,0,0,0)
assert not any(all(w1[i]==w2[(a*i+b)%8] for i in range(8)) for a in (-1,1) for b in range(8))
result["square_one_counter_both_outcomes"]=True
Path(__file__).with_name("independent-checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result))
