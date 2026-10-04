from itertools import product
from pathlib import Path
import json, math

def preserves(w,s):return all(w[i]==w[(i+s)%len(w)] for i in range(len(w)))
def period(w):return next(s for s in range(1,len(w)+1) if preserves(w,s))
repairs={}
for original,s in [('RBBBRB',3),('RBBBBRRB',2),('RRBBRB',2)]:
    legal=[''.join(w) for w in product('RB',repeat=len(original)) if preserves(w,s)]
    cost=lambda w:sum(a!=b for a,b in zip(w,original))
    best=min(map(cost,legal));repairs[original]={'shift':s,'minimum':best,'all_optima':sorted(w for w in legal if cost(w)==best)}
assert [repairs[w]['minimum'] for w in repairs]==[2,3,2]
necklaces={}
for n in range(5,9):
    histogram={}
    for w in product('AB',repeat=n):
        same=sum(w[i]==w[(i+1)%n] for i in range(n));histogram[same]=histogram.get(same,0)+1
    necklaces[n]={'minimum_equal_joins':min(histogram),'histogram':histogram}
verts=[(-36,-50),(-10,-50),(-10,-8),(22,-8),(22,15),(-10,15),(-10,30),(36,30),(36,50),(-36,50)]
def distances(i,j):return sum((verts[i][k]-verts[j][k])**2 for k in [0,1])
symmetries=[]
for sign in [1,-1]:
    for offset in range(len(verts)):
        f=lambda i:(sign*i+offset)%len(verts)
        if all(distances(i,j)==distances(f(i),f(j)) for i in range(len(verts)) for j in range(len(verts))):symmetries.append((sign,offset))
assert symmetries==[(1,0)]
result={'periods':{w:period(w) for w in ['RBB','RBBB','RB','RBBBBBBB']},'shared_3_4':math.lcm(3,4),'shared_2_3':math.lcm(2,3),'shared_2_8':math.lcm(2,8),'repair_results':repairs,'necklace_results':necklaces,'footprint_isometries':symmetries}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
