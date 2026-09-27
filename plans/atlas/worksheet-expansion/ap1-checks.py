#!/usr/bin/env python3
"""AP1 finite checks; mathematical arguments are also recorded in task solutions."""
from itertools import product,combinations
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json
out={}
# AP02: individually labeled draws, fixed bag across two draws, replacement.
bags={'A':['R','R','B'],'B':['R','B','B']}
pairs=[(bag,i,j,cs[i]+cs[j])for bag,cs in bags.items()for i,j in product(range(3),repeat=2)]
post={}
for clue,test in [('RR',lambda s:s=='RR'),('RB',lambda s:s=='RB'),('different',lambda s:s in ['RB','BR']),('at_least_red',lambda s:'R'in s)]:
 keep=[v for v in pairs if test(v[3])];post[clue]={'A':sum(v[0]=='A'for v in keep),'total':len(keep),'posterior':str(F(sum(v[0]=='A'for v in keep),len(keep)))}
assert [post[k]['posterior']for k in ['RR','RB','different','at_least_red']]==['4/5','1/2','1/2','8/13']
weighted=[(ticket,i,bags[ticket][i])for ticket in ['A','B','B']for i in range(3)]
assert F(sum(t=='A'and c=='R'for t,i,c in weighted),sum(c=='R'for t,i,c in weighted))==F(1,2)
out['AP-02']={'two_draw_outcomes':pairs,'posterior_counts':post,'weighted_single_red':'1/2'}
# AP03 exact design, no exchangeability beyond stated randomized assignment.
scores=dict(zip('ABCDEF',[0,1,2,4,5,6]));assign=[]
for t in combinations(scores,3):
 s=sum(scores[x]for x in t);assign.append({'treated':''.join(t),'sum':s,'difference':str(F(2*s-18,3))})
assert len(assign)==20 and sum(a['sum']>=15 for a in assign)==1 and sum(a['sum']>=15 or a['sum']<=3 for a in assign)==2
paired=[]
for choice in product(*[('A','F'),('B','E'),('C','D')]):paired.append({'treated':''.join(sorted(choice)),'sum':sum(scores[x]for x in choice)})
assert len(paired)==8 and sum(a['sum']>=15 for a in paired)==1
out['AP-03']={'complete_assignments':assign,'paired_assignments':paired,'one_sided':'1/20','two_sided':'1/10','paired_one_sided':'1/8'}
# AP04 compare frames and all ordered two-draw samples.
pop=[1]*4+[5]*4
hist=Counter(F(a+b,2)for a,b in product(pop,repeat=2));assert hist=={F(1):16,F(3):32,F(5):16}
assert sum(k*v for k,v in hist.items())/64==3
worlds=[[1]*4+[5]*4,[1]*4+[9]*4]
assert [F(sum(w),8)for w in worlds]==[3,5]
assert F(2*1+6*5,8)==4 and F(1+5,2)==3 and F(1,4)*1+F(3,4)*5==4
out['AP-04']={'full_frame_two_draw_mean_counts':{str(k):v for k,v in hist.items()},'hidden_world_means':[3,5],'unequal_strata_mean':4,'unweighted_strata_estimate':3}
# AP05 exhaustive shifts and interval offsets; shortest80% translation intervals.
errors=list(range(-2,3));valid=[]
for a in range(-5,6):
 for b in range(a,6):
  cov=sum(a+e<=0<=b+e for e in errors)
  if cov>=4:valid.append((b-a,a,b,cov))
width=min(t[0]for t in valid);best=[x for x in valid if x[0]==width]
assert width==3 and best==[(3,-2,1,4),(3,-1,2,4)]
for theta in range(-20,21):
 assert sum(theta+e-1<=theta<=theta+e+1 for e in errors)==3
 outcomes=[(e,h)for e in errors for h in ['H','T']]
 hits=sum((theta+e-2<=theta<=theta+e+2)if h=='H' else theta==theta+e+10 for e,h in outcomes)
 assert hits==5
out['AP-05']={'shortest_80_percent_intervals':best,'narrow_coverage':'3/5','coin_procedure_coverage':'1/2','translation_tests':41}
# AP06 exact Newton instance and safeguarded bracket.
f=lambda x:x**3-5*x
df=lambda x:3*x*x-5
N=lambda x:x-f(x)/df(x)
assert N(F(1))==-1 and N(F(-1))==1 and f(0)==0
assert N(F(2))==F(16,7) and f(F(16,7))==F(176,343)
assert f(1)<0<f(3)
L,R,x=F(1),F(3),F(1);steps=[]
for _ in range(8):
 c=N(x)if df(x) else None
 low,high=L+(R-L)/4,R-(R-L)/4
 take=c is not None and low<=c<=high
 z=c if take else (L+R)/2
 old=(L,R)
 if f(z)==0:L=R=z
 elif f(L)*f(z)<0:R=z
 else:L=z
 assert R-L<=F(3,4)*(old[1]-old[0])
 steps.append({'old':[str(v)for v in old],'proposal':str(c),'accepted_newton':take,'used':str(z),'new':[str(L),str(R)]})
 x=z
assert steps[0]['used']=='2' and steps[1]['used']=='16/7'
n=next(n for n in range(100)if 2*F(3,4)**n<F(1,100));assert n==19
out['AP-06']={'hybrid_steps':steps,'updates_for_width_below_001':n,'proof_bound':'2*(3/4)^n'}
# AP08 enumerate every two-state DFA with fixed start0; acceptance includes empty.
strings=[''.join(w)for k in range(7)for w in product('RB',repeat=k)]
def accepts(s,tr,acc):
 q=0
 for c in s:q=tr[2*q+'RB'.index(c)]
 return bool(acc>>q&1)
short_ok=[]
for tr in product(range(2),repeat=4):
 for acc in range(4):
  if all(accepts(s,tr,acc)==(s.count('R')%3==0)for s in strings if len(s)<=2):
   short_ok.append({'transitions':tr,'accept_mask':acc,'shortest_failure':next(s for s in strings if accepts(s,tr,acc)!=(s.count('R')%3==0))})
assert len(short_ok)==1 and short_ok[0]['shortest_failure']=='RRR'
for s in strings:
 q=0
 for c in s:q=(q+(c=='R'))%3
 assert(q==0)==(s.count('R')%3==0)
 q=(0,0)
 for c in s:q=((q[0]+1)%3,q[1])if c=='R'else(q[0],1-q[1])
 assert(q==(0,0))==(s.count('R')%3==0 and s.count('B')%2==0)
states=list(product(range(3),range(2)))
for a,b in combinations(states,2):
 suf='R'*((-a[0])%3)+'B'*((-a[1])%2)
 end=lambda q:((q[0]+suf.count('R'))%3,(q[1]+suf.count('B'))%2)
 assert end(a)==(0,0) and end(b)!=(0,0)
out['AP-08']={'two_state_DFAs_checked':64,'matching_all_length_at_most2':short_ok,'three_and_six_state_test_strings':len(strings),'six_state_distinguished_pairs':15}
# AP09 algebra identities checked at rational pairs, formula proof in solutions.
force=lambda x,y:(-2*x+y,x-2*y)
for u,v in product([F(i,2)for i in range(-8,9)],repeat=2):
 a,c=(u+v)/2,(u-v)/2
 assert(a+c,a-c)==(u,v)
 F1,F2=force(u,v)
 assert u*F2-v*F1==u*u-v*v
 assert F1+F2==-(u+v) and F1-F2==-3*(u-v)
for k in [F(1,2),F(1),F(3,2),F(4)]:
 mat=lambda u,v:(-(1+k)*u+k*v,k*u-(1+k)*v)
 assert mat(1,1)==(-1,-1)and mat(1,-1)==(-(1+2*k),1+2*k)
out['AP-09']={'rational_identity_points':289,'start':[3,1],'modal_coefficients':[2,1],'unit_spring_eigenvalues':[1,3],'retuned_k':'3/2','retuned_eigenvalues':[1,4],'general_nonrepeat_argument':'irrational sqrt(3), supplied/proved in prose; no finite numerical test substitutes for it'}
# AP10 all recursively series-parallel unit networks, classified by rational stiffness.
@lru_cache(None)
def nets(n):
 if n==1:return {F(1):'1'}
 ans={}
 for a in range(1,n):
  for x,tx in nets(a).items():
   for y,ty in nets(n-a).items():
    ans.setdefault(x+y,f'P({tx},{ty})');ans.setdefault(x*y/(x+y),f'S({tx},{ty})')
 return ans
assert set(nets(3))=={F(1,3),F(2,3),F(3,2),F(3)} and F(1)not in nets(3) and F(1)in nets(4)
assert F(2*6,2+6)==F(3,2) and 2+6==8
out['AP-10']={'three_spring_networks':{str(k):v for k,v in sorted(nets(3).items())},'four_spring_target':nets(4)[F(1)],'load6_extensions_three_springs':{str(k):str(6/k)for k in sorted(nets(3))}}
out['status']='All exact assertions passed; derivations and scope limitations also in per-prompt solutions. No classroom pilots.'
Path(__file__).with_name('ap1-checks-results.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all8 AP1 families, exact finite cases and identity checks.')

# Keep the printed optimal rules tied to the exact offset calculation.
if (Path(__file__).parent / "ap1-data.json").exists():
    _data=json.loads((Path(__file__).parent / "ap1-data.json").read_text())
    _coverage=next(f for f in _data["families"] if f["id"]=="AP-05")["pages"][1]["prompts"][0]["solution"]
    assert "[X−2,X+1]" in _coverage and "[X−1,X+2]" in _coverage
    assert "[−2,X+1]" not in _coverage
