import json
from pathlib import Path
from fractions import Fraction as F
V=[(-26,-22),(26,-22),(26,-8),(16,-8),(16,-13),(-10,-13),(-10,0),(12,0),(12,9),(-10,9),(-10,22),(-26,22)]
D=[[sum((a-b)**2 for a,b in zip(u,v)) for v in V] for u in V]
candidates=[[j for j in range(len(V)) if sorted(D[i])==sorted(D[j])] for i in range(len(V))]
solutions=[]
def extend(m):
    i=len(m)
    if i==len(V):solutions.append(m);return
    for j in candidates[i]:
        if j not in m and all(D[i][k]==D[j][m[k]] for k in range(i)):extend(m+[j])
extend([])
assert solutions==[list(range(len(V)))]
# Since the motif is asymmetric, its signed orientation is actual matching data.
def symmetry(S,P,a,b,d):
    target=set(S)
    return {((a*x+d)%P,b*y,a*sx,b*sy) for x,y,sx,sy in S}==target
configs={
 'translation_only':(6,[(0,1,1,1)]),
 'glide_only':(6,[(0,1,1,1),(3,-1,1,-1)]),
 'horizontal_no_halfturn':(6,[(0,1,1,1),(0,-1,1,-1)]),
 'halfturn_no_reflections':(6,[(0,1,1,1),(3,-1,-1,-1)]),
 'perpendicular_reflections':(6,[(1,1,1,1),(5,1,-1,1),(1,-1,1,-1),(5,-1,-1,-1)])}
out={}
for name,(P,S) in configs.items():
    shifts={0,P}|{(u[0]-v[0])%P for u in S for v in S}
    out[name]={str((a,b)):sorted(d for d in shifts if symmetry(S,P,a,b,d)) for a,b in [(1,1),(1,-1),(-1,1),(-1,-1)]}
assert out['glide_only']['(1, 1)']==[0,6]
assert out['glide_only']['(1, -1)']==[3]
assert not out['horizontal_no_halfturn']['(-1, -1)']
assert out['halfturn_no_reflections']['(-1, -1)'] and not out['halfturn_no_reflections']['(1, -1)'] and not out['halfturn_no_reflections']['(-1, 1)']
assert all(out['perpendicular_reflections'][str(k)] for k in [(1,-1),(-1,1),(-1,-1)])
# An explicitly permitted larger repeat can destroy an old primitive slide.
S=[(F(1,2),1,1,1),(6,1,1,1)]
assert not symmetry(S,12,1,1,6) and symmetry(S,12,1,1,12)
# Exact affine composition of G(x,y)=(x+3,-y).
assert (3+3,(-1)*(-1))==(6,1)
out['motif_distance_automorphisms']=len(solutions)
out['larger_repeat_edit_breaks_old_period']=True
Path(__file__).with_name('independent-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
