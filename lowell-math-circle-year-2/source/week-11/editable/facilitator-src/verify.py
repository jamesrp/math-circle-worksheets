"""Independent final-instance check. No import from worksheet builders or draft checks."""
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
G={'triangle':((1,-1),(0,-1)), 'square':((1,-1),(0,2),(1,-1)), 'diagonal':((1,2,-1),(0,2),(0,1,-1))}
STARTS={'triangle':[(2,2),(3,2),(2,3),(3,3),(4,0),(5,4),(2,4)]+[(a,N-a) for N in (4,5,6) for a in range(N+1)], 'square':[(0,4,0),(2,2,0),(0,2,2),(2,0,2),(2,1,2),(2,4,2),(2,4,0),(3,0,3),(0,12,0),(6,0,6),(4,4,4),(0,8,0)], 'diagonal':[(3,0,3),(0,6,0),(2,2,2),(4,1,2)]}
def run(graph,start,reverse=False):
    x=list(start);c=[0]*len(x);route=[]
    while any(x[i]>=len(graph[i]) for i in range(len(x))):
        choices=[i for i in range(len(x)) if x[i]>=len(graph[i])]
        v=choices[-1 if reverse else 0];route.append(chr(65+v));x[v]-=len(graph[v]);c[v]+=1
        for w in graph[v]:
            if w>=0:x[w]+=1
    return {'end':x,'fires':c,'sink':sum(start)-sum(x),'route':''.join(route)}
results={}
for name,g in G.items():
    @lru_cache(None)
    def all_results(s):
        legal=[i for i in range(len(s)) if s[i]>=len(g[i])]
        if not legal:return {(s,(0,)*len(s))}
        ans=set()
        for i in legal:
            t=list(s);t[i]-=len(g[i])
            for j in g[i]:
                if j>=0:t[j]+=1
            for fin,counts in all_results(tuple(t)):
                c=list(counts);c[i]+=1;ans.add((fin,tuple(c)))
        return ans
    results[name]=[]
    for s in sorted(set(STARTS[name])):
        r=run(g,s);a=all_results(s)
        assert a=={(tuple(r['end']),tuple(r['fires']))},(name,s,a,r)
        results[name].append({'start':s,**r,'reverse_route':run(g,s,True)['route']})
results['addition_A']={}
for start in [(0,0),(1,0),(0,1),(1,1)]:
    x=list(start);rows=[]
    for _ in range(12):
        x[0]+=1;x=run(G['triangle'],x)['end'];rows.append(x[:])
    results['addition_A'][str(start)]=rows
for x,y in [((0,4,0),(2,0,0)),((3,0,0),(0,0,3))]:
    expected=run(G['square'],[a+b for a,b in zip(x,y)])['end']
    for u,v in [(x,y),(y,x)]:
        a=run(G['square'],u)['end'];assert run(G['square'],[a+b for a,b in zip(a,v)])['end']==expected
results['stable_square']=[[a,b,c] for a in (0,1) for b in (0,1) for c in (0,1)]
(P/'checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
