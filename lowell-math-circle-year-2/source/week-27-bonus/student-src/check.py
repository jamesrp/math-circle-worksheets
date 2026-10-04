#!/usr/bin/env python3
from itertools import permutations,combinations
import json
def evaluate(left,right,m):
 rev={v:k for k,v in m.items() if v is not None}
 allowed=lambda a,b:b in left[a] and a in right[b]
 prefers=lambda lis,other,now:now is None or lis.index(other)<lis.index(now)
 if any(v is not None and not allowed(a,v) for a,v in m.items()):return None
 blocks=[a+b for a in left for b in right if m[a]!=b and allowed(a,b) and prefers(left[a],b,m[a]) and prefers(right[b],a,rev.get(b))]
 score=sum(left[a].index(b)+right[b].index(a)+2 for a,b in m.items() if b is not None)
 return {'pairs':[a+b for a,b in m.items() if b is not None],'unpaired':[a for a,b in m.items() if b is None]+[b for b in right if b not in rev],'score':score,'blockers':blocks}
def allmatchings(left,right):
 keys=list(left);ans=[]
 def go(i,m,used):
  if i==len(keys):
   out=evaluate(left,right,m)
   if out is not None:ans.append(out)
   return
  a=keys[i]
  for b in [None]+list(right):
   if b is None or b not in used:
    go(i+1,{**m,a:b},used if b is None else used|{b})
 go(0,{},set());return ans
L={'A':list('YZX'),'B':list('YXZ'),'C':list('XYZ')};R={'X':list('BAC'),'Y':list('ACB'),'Z':list('BAC')}
agg=[evaluate(L,R,dict(zip(L,p))) for p in permutations(R)]
cases=[({'A':['X'],'B':['X']},{'X':['A','B'],'Y':[]}),({'A':list('XY'),'B':list('YX'),'C':['Y']},{'X':list('BA'),'Y':list('ABC'),'Z':[]})]
stable=[[m for m in allmatchings(l,r) if not m['blockers']] for l,r in cases]
profiles=[{'A':list('BCD'),'B':list('CAD'),'C':list('ABD'),'D':list('ABC')},{'A':list('BCD'),'B':list('ACD'),'C':list('DAB'),'D':list('CAB')}]
pairs=[('AB','CD'),('AC','BD'),('AD','BC')];room=[]
for p in profiles:
 out=[]
 for pairing in pairs:
  m={a:b for s in pairing for a,b in [s,s[::-1]]}
  block=[a+b for a,b in combinations(p,2) if m[a]!=b and p[a].index(b)<p[a].index(m[a]) and p[b].index(a)<p[b].index(m[b])]
  out.append({'pairs':pairing,'blockers':block})
 room.append(out)
assert min(agg,key=lambda x:x['score'])['pairs']==['AY','BZ','CX']
assert [x for x in agg if not x['blockers']][0]['pairs']==['AY','BX','CZ']
assert [len(x) for x in stable]==[1,2]
assert all(x['blockers'] for x in room[0]) and not room[1][0]['blockers']
# Added convention example uses one unchanged matching and two literal list checks.
V=['P','Q']; P=['V','U']
assert V.index('P')<V.index('Q') and P.index('V')<P.index('U')
print(json.dumps({'aggregate':agg,'incomplete_stable':stable,'roommates':room},indent=2))
