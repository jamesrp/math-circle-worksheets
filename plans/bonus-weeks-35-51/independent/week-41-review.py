"""Independent math review; no imports of draft checks or builders."""
from collections import Counter, deque
from itertools import product
from pathlib import Path
import json

V={'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
NAMES={(0,0):'H',(1,0):'E',(2,0):'D',(0,1):'B',(1,1):'C',(2,1):'A',(0,2):'G',(1,2):'I',(2,2):'F'}
def follow(word):
    p=(0,0); path=[p]
    for c in word:
        dx,dy=V[c];p=(p[0]+dx,p[1]+dy);path.append(p)
    return path
words={}
for w in ['R','RU','RRR','RULD','RRU']:
    p=follow(w)[-1];period=1 if (p[0]%3,p[1]%3)==(0,0) else 3
    words[w]={'net':p,'period':period,'round_cells':[NAMES[((i*p[0])%3,(i*p[1])%3)] for i in range(period+1)],'all_step_cells':[NAMES[(x%3,y%3)] for x,y in follow(w*period)]}

tours=[]
def visit(path,word):
    p=path[-1]
    if len(path)==9:
        for c,(dx,dy) in V.items():
            q=(p[0]+dx,p[1]+dy)
            if q[0]%3==q[1]%3==0:tours.append((word+c,(q[0]//3,q[1]//3)))
        return
    residues={(x%3,y%3) for x,y in path}
    for c,(dx,dy) in V.items():
        q=(p[0]+dx,p[1]+dy)
        if (q[0]%3,q[1]%3) not in residues:visit(path+[q],word+c)
visit([(0,0)],'')
counts=Counter(pair for _,pair in tours)
printed=['LLDLLDLLD','LLULLULLU','LDDLDDLDD','RULLDDLLU','LUULUULUU','RRDDLULDD','RRUULDLUU','RDDRDDRDD','RRULURRDD','RUURUURUU','RRDRRDRRD','RRURRURRU']
assert all(w in {w for w,_ in tours} for w in printed)
assert len(tours)==96 and len(counts)==12 and (0,0) not in counts

def blocked(p):return (p[0]%3,p[1]%3) in {(0,1),(1,0)}
targets={(3,0),(0,3),(3,3)};dist={(0,0):0};ways={(0,0):1};prev={};queue=deque([(0,0)])
while queue:
    p=queue.popleft()
    if dist[p]>=12:continue
    for c,(dx,dy) in V.items():
        q=(p[0]+dx,p[1]+dy)
        if blocked(q):continue
        if q not in dist:dist[q]=dist[p]+1;ways[q]=ways[p];prev[q]=(p,c);queue.append(q)
        elif dist[q]==dist[p]+1:ways[q]+=ways[p]
obstacles={}
for q in sorted(targets):
    route='';p=q
    while p!=(0,0):p,c=prev[p];route=c+route
    obstacles[str(q)]={'distance':dist[q],'number_shortest':ways[q],'witness':route}
for w,target in [('DRRRU',(3,0)),('LUURU',(0,3)),('LUURRRRU',(3,3))]:
    path=follow(w);assert path[-1]==target and all(not blocked(p) for p in path) and len(w)==dist[target]
result={'printed_words':words,'tour_count':len(tours),'tour_winding_counts':{str(k):counts[k] for k in sorted(counts)},'printed_tour_witnesses_valid':True,'obstacle_targets':obstacles,'printed_obstacle_witnesses_valid':True,'diagram_coordinates':{'single_map_rows_top_to_bottom':['ABC','DHE','FGI'],'obstacle_extent':[-2,4,-2,4],'blocked_residues':[[0,1],[1,0]],'targets':[[3,0],[0,3],[3,3]]}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
