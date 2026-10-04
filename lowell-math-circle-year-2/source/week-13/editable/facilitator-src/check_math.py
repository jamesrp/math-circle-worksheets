"""Independent explicit graph and exhaustive search for the final v2 networks."""
import itertools,json
from functools import lru_cache
from pathlib import Path
R=Path(__file__).parent
E={
'diamond':'sA sB At Bt',
'greedy':'sA sB AB At Bt',
'bowtie':'sA sB AC BC CD CE Dt Et',
'doubletrap':'sA sB AB AC BC CD CE DE Dt Et',
'funnel':'sA sB AC BC CD Dt',
'wide':'sA sB sC AD BD CD DE DF Et Ft',
'parallel':'sA sB sC At Bt Ct',
'bottleneck':'sA sB sC AD BD CD DE DF EG FG GH GI GJ Ht It Jt',
'endpoint':'sA sC AD CD DE DF EG FG GH GI GJ Ht It Jt',
'backward':'sA sB AC BD Ct Dt BA CD CB',
'staircase':'sA sB sC AD BD BE CE CF Dt Et Ft'}
E={k:tuple((w[0],w[1]) for w in v.split()) for k,v in E.items()}
def paths(es):
 result=[];stack=[('s',)]
 while stack:
  p=stack.pop()
  if p[-1]=='t':result.append(p);continue
  stack += [p+(v,) for u,v in es if u==p[-1] and v not in p]
 return result
def edges(p):return frozenset(zip(p,p[1:]))
def analyze(es):
 ps=paths(es);pe=[edges(p) for p in ps];packs=[]
 for k in range(1,5):
  pack=[c for c in itertools.combinations(range(len(ps)),k) if sum(len(pe[i]) for i in c)==len(set().union(*(pe[i] for i in c)))]
  if not pack:break
  packs=pack
 for k in range(1,len(es)+1):
  cuts=[c for c in itertools.combinations(es,k) if not paths([e for e in es if e not in c])]
  if cuts:break
 assert len(packs[0])==k
 return {'route_count':len(ps),'maximum':k,'collections':[[ps[i] for i in p] for p in packs],'minimum_closures':cuts}
D={name:analyze(es) for name,es in E.items()}
for name in ('wide','greedy'):
 D[name]['deletions_preserving_two']=[e for e in E[name] if any(edges(p).isdisjoint(edges(q)) for p,q in itertools.combinations(paths([x for x in E[name] if x!=e]),2))]
@lru_cache(None)
def win(es):
 return any(not paths(rem) or not win(rem) for e in es for rem in [tuple(x for x in es if x!=e)])
for name in ['diamond','greedy']:
 es=E[name];D[name]['first_wins']=win(es);D[name]['winning_openings']=[e for e in es if not paths(tuple(x for x in es if x!=e)) or not win(tuple(x for x in es if x!=e))]
D['backward']['splits']=[]
for flags in itertools.product([0,1],repeat=4):
 S={'s'}|{v for v,f in zip('ABCD',flags) if f};out=[e for e in E['backward'] if e[0] in S and e[1] not in S];inc=[e for e in E['backward'] if e[0] not in S and e[1] in S]
 if len(out)==2 and inc:D['backward']['splits'].append({'S':sorted(S),'out':out,'in':inc})
for name,reserved in [('greedy',[('s','A','B','t')]),('doubletrap',[('s','A','B','C','D','E','t')]),('staircase',[('s','B','D','t'),('s','C','E','t')]),('bottleneck',[('s','A','D','E','G','H','t'),('s','C','D','F','G','J','t')])]:
 used=set().union(*(edges(p) for p in reserved));res=[(v,u) if (u,v) in used else (u,v) for u,v in E[name]]
 reach={'s'}
 while True:
  new=reach|{v for u,v in res if u in reach}
  if new==reach:break
  reach=new
 D[name]['residual_reachable']=sorted(reach);D[name]['augmentations']=paths(res)
 assert not paths([e for e in E[name] if e not in used])
D['added_DG']=analyze(E['bottleneck']+(('D','G'),))
assert [D[n]['maximum'] for n in E]==[2,2,2,2,1,2,3,2,2,2,3]
assert D['doubletrap']['augmentations']==[('s','B','A','C','E','D','t')]
assert len(D['bowtie']['minimum_closures'])==8
assert D['bottleneck']['residual_reachable']==['A','B','C','D','s']
assert D['greedy']['winning_openings']==[('A','B')]
(R/'math-checks.json').write_text(json.dumps(D,indent=2)+'\n')
print(json.dumps({k:{f:v for f,v in d.items() if f not in ['collections','minimum_closures']} for k,d in D.items()},indent=2))
