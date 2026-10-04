from itertools import permutations,product,combinations
from collections import Counter
from pathlib import Path
import json
def parity(p):return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1
shapes=[[(0,0),(18,0),(18,26),(39,26),(39,41),(18,41),(18,54),(55,54),(55,70),(0,70)],[(0,0),(65,0),(65,18),(18,18),(18,65),(0,65)],[(0,0),(18,0),(18,52),(40,52),(40,70),(-22,70),(-22,52),(0,52)]]
flat=[]
for points in shapes:
    n=len(points)
    d=lambda i,j:sum((points[i][k]-points[j][k])**2 for k in [0,1])
    syms=[]
    for sign in [1,-1]:
        for shift in range(n):
            f=lambda i:(sign*i+shift)%n
            if all(d(i,j)==d(f(i),f(j)) for i in range(n) for j in range(n)):syms.append((sign,shift))
    flat.append({'outline_symmetries':syms,'face_up_mirror_match':any(s==-1 for s,_ in syms),'overturn_match':True})
edges=list(combinations(range(4),2));even=[p for p in permutations(range(4)) if parity(p)==1];odd=[p for p in permutations(range(4)) if parity(p)==-1]
def act(red,p):return {tuple(sorted((p[a],p[b]))) for a,b in red}
tetra=[]
for inds in combinations(range(6),3):
    red={edges[i] for i in inds};degrees=tuple(sorted(sum(v in e for e in red) for v in range(4)))
    oddaut=[p for p in odd if act(red,p)==red]
    tetra.append({'red':sorted(red),'degrees':degrees,'chiral':not oddaut})
caseedges=[{(0,1),(1,2),(2,3)},{(0,1),(0,2),(0,3)},{(0,1),(0,2),(1,2)}]
proper=[(p,s) for p in permutations(range(3)) for s in product([-1,1],repeat=3) if parity(p)*s[0]*s[1]*s[2]==1]
corner=[]
for colors,lengths in [('RBG',[60]*3),('RRG',[60]*3),('RRR',[60]*3),('RRR',[30,60,90])]:
    source=[]
    for i,(c,l) in enumerate(zip(colors,lengths)):
        q=[0,0,0];q[i]=l;source.append((c,tuple(q)))
    mirror={(c,(q[1],q[0],q[2])) for c,q in source}
    matches=[]
    for p,s in proper:
        transformed=[]
        for c,q in source:
            z=[0,0,0]
            for i in range(3):z[p[i]]=s[i]*q[i]
            transformed.append((c,tuple(z)))
        if set(transformed)==mirror:matches.append((p,s))
    corner.append({'colors':colors,'lengths':lengths,'mirror_matching_proper_rotations':matches})
result={'flat_outlines':flat,'tetra_proper_rotations':len(even),'tetra_improper_permutations':len(odd),'three_red_patterns_chiral_count':sum(t['chiral'] for t in tetra),'patterns_by_degree':dict(Counter(str(t['degrees']) for t in tetra)),'printed_tetra_chirality':[not any(act(red,p)==red for p in odd) for red in caseedges],'corner_proper_rotations':len(proper),'corner_cases':corner}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
