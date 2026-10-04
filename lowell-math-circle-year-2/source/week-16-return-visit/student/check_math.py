"""Independent mathematical checks; answers belong to adults, not student pages."""
from itertools import product
from collections import Counter
from math import sqrt,hypot
import json
from pathlib import Path

# Independent barycentric triangle construction, indexed by bottom-to-top rows.
vertices=[(a,b) for b in range(4) for a in range(4-b)]
xy={v:(v[0]+v[1]/2,v[1]*sqrt(3)/2) for v in vertices}
triangles=[]
for a,b in vertices:
    if a+b<3:
        triangles.append(((a,b),(a+1,b),(a,b+1)))
    if a+b<2:
        triangles.append(((a+1,b),(a+1,b+1),(a,b+1)))
assert len(triangles)==9
for cell in triangles:
    pts=[xy[v] for v in cell]
    assert all(abs(hypot(pts[k][0]-pts[(k+1)%3][0],pts[k][1]-pts[(k+1)%3][1])-1)<1e-12 for k in range(3))
    assert (pts[1][0]-pts[0][0])*(pts[2][1]-pts[0][1])-(pts[1][1]-pts[0][1])*(pts[2][0]-pts[0][0])>0

corners={(0,0):'R',(3,0):'B',(0,3):'Y'}
def choices(v,four):
    a,b=v
    if v in corners:return [corners[v]]
    if b==0:return list('RB')
    if a==0:return list('RY')
    if a+b==3:return list('BY')
    return list('RBYG' if four else 'RBY')
def fills(four):
    for labels in product(*(choices(v,four)for v in vertices)):
        yield dict(zip(vertices,labels))
def celltypes(f):
    return Counter(''.join(sorted(f[v] for v in t)) for t in triangles)
def any3(f):return sum(len({f[v] for v in t})==3 for t in triangles)
def rby(f):return sum({f[v] for v in t}==set('RBY') for t in triangles)
all4=list(fills(True));zero=[f for f in all4 if rby(f)==0]
counts=Counter(any3(f)for f in zero)
assert len(all4)==256 and len(zero)==27 and counts=={3:18,5:9}
# All three different G-containing types exist in every zero-RBY filling;
# recolor each time from the unchanged original, not cumulatively.
for f in zero:
    typ=celltypes(f)
    assert all(typ[t]%2==1 for t in ('BGR','BGY','GRY'))
    for repl in 'RBY':
        rec={v:repl if c=='G' else c for v,c in f.items()}
        assert rby(rec)>0
rows=['RRBB','RGB','YY','Y']
witness={(a,b):rows[b][a] for a,b in vertices}
assert rby(witness)==0 and any3(witness)==3
star={c:sum(len({x,y,c})==3 and set((x,y,c))==set('RBY')for x,y in [('R','B'),('B','Y'),('Y','R')])for c in 'RBYG'}
assert star=={'R':1,'B':1,'Y':1,'G':0}

# Square cyclic vertices 0=lower left,1=lower right,2=upper right,3=upper left.
diagonals=[[(0,1,2),(0,2,3)],[(0,1,3),(1,2,3)]]
squarecounts=Counter()
for f in product('RBY',repeat=4):
    rb=sum({f[i],f[(i+1)%4]}==set('RB')for i in range(4))
    n=[sum({f[i]for i in t}==set('RBY')for t in cells)for cells in diagonals]
    assert n[0]%2==n[1]%2==rb%2
    squarecounts[tuple(n)]+=1
assert squarecounts[(0,2)]>0 and squarecounts[(2,0)]>0

# Positive CCW cyclic words RBY/BYR/YRB, negative RYB/YBR/BRY.
pos={'RBY','BYR','YRB'};neg={'RYB','YBR','BRY'}
pairs=Counter()
for f in fills(False):
    words=[''.join(f[v] for v in t)for t in triangles]
    p=sum(w in pos for w in words);m=sum(w in neg for w in words)
    assert p-m==1
    pairs[p,m]+=1
assert sum(pairs.values())==192
# Printed examples CCW from lower-left: R,B,Y is positive, R,Y,B negative.
assert 'RBY'in pos and 'RYB'in neg
report={
'four_label_fillings':len(all4),'zero_RBY_fillings':len(zero),'zero_RBY_any_three_counts':dict(counts),
'witness_rows':rows,'witness_cell_types':dict(celltypes(witness)),'small_star_RBY_counts':star,
'square_patterns':81,'square_diagonal_count_pairs':{str(k):v for k,v in sorted(squarecounts.items())},
'signed_mesh_fillings':192,'signed_count_pairs':{str(k):v for k,v in sorted(pairs.items())},
'geometry':{'star_outer_side_inches':4.05,'main_four_label_outer_side_inches':4.5,'signed_outer_side_inches':4.2,'main_vertex_spacing_mm':38.1,'signed_vertex_spacing_mm':35.56,'square_side_inches':2.5,'circle_diameter_mm':7.112},
'proof_limit':'Exhaustive small-mesh checks support these printed instances; the general claims require the separate adult arguments.',
'status':'Unpiloted; physical materials and procedure not rehearsed.'}
print(json.dumps(report,indent=2))
if __name__=='__main__':
    (Path(__file__).resolve().parent.parent/'math-check.json').write_text(json.dumps(report,indent=2))
