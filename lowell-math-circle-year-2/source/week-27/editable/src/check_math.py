import itertools,random,json
from pathlib import Path

def blockers(L,R,m):
 inv={v:k for k,v in m.items()}
 return [(a,x) for a in L for x in R if m[a]!=x and L[a].index(x)<L[a].index(m[a]) and R[x].index(a)<R[x].index(inv[x])]
def stable(L,R):
 return [dict(zip(L,p)) for p in itertools.permutations(R) if not blockers(L,R,dict(zip(L,p))) ]
def da(L,R,reverse=False):
 held={}; tried={p:[] for p in L}; log=[]
 while len(held)<len(L):
  free=[p for p in L if p not in held.values()];p=free[-1] if reverse else free[0]
  r=next(x for x in L[p] if x not in tried[p]); tried[p].append(r); old=held.get(r)
  if old is None or R[r].index(p)<R[r].index(old): held[r]=p
  log.append([p,r,held[r],old])
 return {p:r for r,p in held.items()},log
rng=random.Random(27)
for tries in range(100000):
 L={p:rng.sample(list('XYZ'),3) for p in 'ABC'};R={r:rng.sample(list('ABC'),3) for r in 'XYZ'}
 if len(stable(L,R))==3: break
three=(L,R)
for tries in range(100000):
 L={p:rng.sample(list('WXYZ'),4) for p in 'ABCD'};R={r:rng.sample(list('ABCD'),4) for r in 'WXYZ'}
 m,log=da(L,R);mr,logr=da(R,L)
 if len(stable(L,R))>=2 and len(log)>=8 and len(logr)>=7 and m!={v:k for k,v in mr.items()}: break
four=(L,R)
profiles={
 'k_unique_mutual':({'A':list('XY'),'B':list('YX')},{'X':list('AB'),'Y':list('BA')}),
 'k_unique_shared':({'A':list('XY'),'B':list('XY')},{'X':list('AB'),'Y':list('AB')}),
 'k_two_stable':({'A':list('XY'),'B':list('YX')},{'X':list('BA'),'Y':list('AB')}),
 'k_unique_cross':({'A':list('YX'),'B':list('XY')},{'X':list('BA'),'Y':list('AB')}),
 'k_one_blocker':({'A':list('YX'),'B':list('YX')},{'X':list('AB'),'Y':list('AB')}),
 'middle_unique':({'A':list('XYZ'),'B':list('XZY'),'C':list('YXZ')},{'X':list('CBA'),'Y':list('ACB'),'Z':list('BAC')}),
 'middle_three':three,
 'middle_four':({'A':list('WXYZ'),'B':list('XWZY'),'C':list('YZWX'),'D':list('ZYXW')},{'W':list('BACD'),'X':list('ABDC'),'Y':list('DCAB'),'Z':list('CDBA')}),
 'older_four':four,
}
ans={}
for name,(L,R) in profiles.items():
 m,log=da(L,R);mr,logr=da(R,L)
 ans[name]={'left':L,'right':R,'stable':stable(L,R),'left_proposals':log,'left_result':m,'right_proposals':logr,'right_result':mr}
# Check all 16 two-pair profiles and exactly which single-strip reversals repair straight pairing.
small=[]
for bits in itertools.product([0,1],repeat=4):
 L={p:list('XY')[::(-1 if b else 1)] for p,b in zip('AB',bits[:2])}; R={p:list('AB')[::(-1 if b else 1)] for p,b in zip('XY',bits[2:])}
 small.append((bits,len(stable(L,R))))
assert sum(count==2 for bits,count in small)==2
for key in ['k_one_blocker','k_unique_cross']:
 L,R=profiles[key];rep=[]
 for p in [*L,*R]:
  LL={q:v[:] for q,v in L.items()};RR={q:v[:] for q,v in R.items()}
  (LL if p in LL else RR)[p].reverse()
  if not blockers(LL,RR,{'A':'X','B':'Y'}):rep.append(p)
 ans[key]['single_strip_repairs']=rep
# A stable 3-pair instance with 3 last choices exists; no stable 3-pair instance can have >3.
# Exhaust all 46,656 profiles and 6 matchings to verify the extension's maximum.
perms=list(itertools.permutations('XYZ'));rperms=list(itertools.permutations('ABC'))
maxlast=0
for ls in itertools.product(perms,repeat=3):
 L=dict(zip('ABC',ls))
 for rs in itertools.product(rperms,repeat=3):
  R=dict(zip('XYZ',rs))
  for m in stable(L,R):
   inv={v:k for k,v in m.items()}
   count=sum(L[a][-1]==m[a] for a in L)+sum(R[r][-1]==inv[r] for r in R)
   maxlast=max(maxlast,count)
assert maxlast==3
ans['last_choice_maximum']=maxlast
Path(__file__).with_name('math_checks.json').write_text(json.dumps(ans,indent=2))
print(json.dumps({k:{'left':v['left'],'right':v['right'],'stable':v['stable'],'proposals':len(v['left_proposals'])} for k,v in ans.items() if isinstance(v,dict)},indent=2))
print('Maximum last choices:',maxlast)
