from itertools import permutations,combinations,product
from pathlib import Path
import json
# Independently enumerate signed coordinate-permutation matrices in SO(3).
V=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
rots=[]
for axes in permutations(range(3)):
    parity=(-1)**sum(axes[i]>axes[j] for i in range(3) for j in range(i+1,3))
    for signs in product((-1,1),repeat=3):
        if parity*signs[0]*signs[1]*signs[2]!=1:continue
        W=[tuple(signs[i]*v[axes[i]] for i in range(3)) for v in V]
        if all(w in V for w in W):rots.append(tuple(V.index(w) for w in W))
assert len(set(rots))==12
def equivalent(a,b):return any(all(a[i]==b[q[i]] for i in range(4)) for q in rots)
assert equivalent('ABCD','ADBC') and not equivalent('ABCD','ACBD')
merges={a+b:equivalent('ABCD'.replace(b,a),'ACBD'.replace(b,a)) for a,b in combinations('ABCD',2)}
assert all(merges.values())
words=set(permutations('ABCD'))
classes=[]
while words:
    seed=next(iter(words));orbit={w for w in words if equivalent(seed,w)}
    classes.append(len(orbit));words-=orbit
assert sorted(classes)==[12,12]
repeated=set(permutations('AABC'))
assert all(equivalent('AABC',w) for w in repeated)
results=[]
for i in [0,1]:
    for j in [0,2]:
        a=list('AABC');b=list('ABAC');a[i]='D';b[j]='D';results.append(equivalent(a,b))
assert sorted(results)==[False,False,True,True]
out={'proper_vertex_mappings':len(set(rots)),'distinct_label_orbit_sizes':classes,'repeated_label_orbit_size':len(repeated),'all_six_merges_match':merges,'restore_one_distinct_label_outcomes':results,'physical_pretest_performed':False}
Path(__file__).with_name('independent-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
