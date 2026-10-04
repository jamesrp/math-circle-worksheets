from itertools import product
from collections import defaultdict
from pathlib import Path
import json
def cycles(mapping):
    todo=set(mapping);ans=[]
    while todo:
        v=min(todo);cycle=[]
        while v not in cycle:cycle.append(v);todo.discard(v);v=mapping[v]
        ans.append(cycle)
    return ans
lane={}
for n in [3,4]:
    for rev in [False,True]:
        p={i:(n-1-i if rev else i) for i in range(n)}
        b={(i,s):(p[i],s^rev) for i in range(n) for s in [0,1]}
        lane[f'{n}{"R" if rev else "M"}']={'pieces':cycles(p),'boundary_components':len(cycles(b)),'boundary_per_piece':[sum(set(x[0] for x in bc)<=set(pc) for bc in cycles(b)) for pc in cycles(p)]}
seams={}
for n in range(1,6):
    for w in map(''.join,product('MR',repeat=n)):
        action={(i,s):((i+1)%n,s^(w[i]=='R')) for i in range(n) for s in [0,1]}
        count=len(cycles(action));assert count==(1 if w.count('R')%2 else 2);seams[w]=count
def component_count(adjacency):
    todo=set(adjacency);count=0
    while todo:
        count+=1;stack=[todo.pop()]
        while stack:
            v=stack.pop()
            for q in adjacency[v]:
                if q in todo:todo.remove(q);stack.append(q)
    return count
def mesh(rev,removed):
    nx,ny=12,6
    def v(i,j):return (0,ny-j if rev else j) if i==nx else (i,j)
    edgefaces=defaultdict(list);faces={}
    for i in range(nx):
        for j in range(ny):
            if (i,j) in removed:continue
            p=[v(i,j),v(i+1,j),v(i+1,j+1),v(i,j+1)];faces[(i,j)]=p
            for a,b in zip(p,p[1:]+p[:1]):edgefaces[tuple(sorted((a,b)))].append((i,j))
    facegraph={f:set() for f in faces};boundary=defaultdict(set)
    for (a,b),fs in edgefaces.items():
        if len(fs)==2:facegraph[fs[0]].add(fs[1]);facegraph[fs[1]].add(fs[0])
        else:assert len(fs)==1;boundary[a].add(b);boundary[b].add(a)
    assert all(len(adj)==2 for adj in boundary.values())
    return {'connected_pieces':component_count(facegraph),'boundary_circles':component_count(boundary)}
inside={(i,j) for i in [5,6] for j in [2,3]};notch={(5,5),(6,5)};seamhole={(i,j) for i in [0,11] for j in [2,3]}
punctures={'A':mesh(False,inside),'B':mesh(True,inside),'C':mesh(True,notch),'D':mesh(False,seamhole)}
result={'lanes':lane,'all_seam_sequences_length_1_to_5':seams,'puncture_mesh_checks':punctures}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'lanes':lane,'punctures':punctures,'seam_sequences_checked':len(seams)},indent=2))
