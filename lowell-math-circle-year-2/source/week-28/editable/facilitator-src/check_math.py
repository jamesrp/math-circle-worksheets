"""Fresh, independent finite checks; standard library only. No student builder imported."""
from itertools import permutations, product, combinations
from collections import defaultdict
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent

def interleaves(h,p,q):
 a,b=sorted(h[x] for x in p);c,d=sorted(h[x] for x in q)
 return a<c<b<d or c<a<d<b
# Exhaust physical layering orders, instead of assuming the 3-to-1 theorem.
stacks={}
rejected=[]
for order in permutations(range(1,5)):
 h={s:order.index(s) for s in order}
 if interleaves(h,(1,2),(3,4)) or interleaves(h,(2,3),(4,1)):
  rejected.append(order);continue
 labels=''.join('V' if b else 'M' for b in (h[4]>h[1],h[2]>h[1],h[2]>h[3],h[4]>h[3]))
 assert labels not in stacks
 stacks[labels]=order
valid=sorted(stacks)
assert len(valid)==8
assert set(valid)=={''.join(x) for x in product('MV',repeat=4) if x.count('M') in (1,3)}
partial=['M?V?','MM??','V?V?']
comp=[[s for s in valid if all(a=='?' or a==b for a,b in zip(mask,s))] for mask in partial]
tab={}
for m in (2,3,4):
 tab[str(m)]=[ss for ss in product(*comp) if sum(s.count('M') for s in ss)==m+3]
assert [len(tab[str(m)]) for m in (2,3,4)]==[4,0,4]
route_labels=dict(zip('ABCDEFGH',['MMMV','MMVM','MVMM','VMMM','MVVV','VMVV','VVMV','VVVM']))
dist=lambda a,b:sum(x!=y for x,y in zip(a,b))
adj={a:[b for b in route_labels if dist(route_labels[a],route_labels[b])==2] for a in route_labels}
paths={};route_count={}
for end in ('H','D'):
 paths[end]=[]
 for p in permutations([x for x in route_labels if x not in ('A',end)]):
  seq=('A',)+p+(end,)
  if all(b in adj[a] for a,b in zip(seq,seq[1:])):paths[end].append(seq)
 assert paths[end]
 route_count[end]=len(paths[end])
weights=dict(zip('ABCDEFG',[30,30,60,60,90,120,150]))
groups=sorted(''.join(p) for n in range(1,8) for p in combinations(weights,n) if sum(weights[k] for k in p)==180)
assert len(groups)==10
angles=[[90]*4,[45,90,90,135],[60,120,120,60],[30,60,150,120]]
alt=lambda x:[sum(x[::2]),sum(x[1::2])]
added={}
for a in (90,60,30,120):
 sols=[]
 for x in range(1,360):
  if x in (0,a,180):continue
  rs=sorted([0,a,180,x]);sectors=[rs[i+1]-rs[i] for i in range(3)]+[360-rs[-1]]
  if alt(sectors)==[180,180]:sols.append(x)
 assert sols==[360-a]
 added[str(a)]=sols
orders=sorted(set(permutations([30,30,60,60,90,90])))
good=[x for x in orders if alt(x)==[180,180]]
rooted=[x for x in good if x[0]==30]
assert len(good)==36 and len(rooted)==12
upper=[[45,90,90,135],[30,30,60,60,90,90],[30,30,30,60,90,120],[45]*8]
assert [alt(x) for x in upper]==[[135,225],[180,180],[150,210],[180,180]]
invalid=set(''.join(x) for x in product('MV',repeat=4))-set(valid)
reps=['MMMM','VVVV','MMVV','MVMV']
assert {s[i:]+s[:i] for s in reps for i in range(4)}==invalid
# D witness: flattened ray angles 0,30,-30,120; S1[0,30], S2[-30,30],
# S3[-30,120], S4[0,120]. Non-extreme crease joins must be adjacent.
d_stack=(3,4,1,2);h={x:d_stack.index(x) for x in d_stack}
assert abs(h[4]-h[1])==1 and abs(h[1]-h[2])==1
assert ''.join('V' if b else 'M' for b in (h[4]>h[1],h[2]>h[1],h[2]>h[3],h[4]>h[3]))=='MVVV'
report={'checked_date':'2026-10-03','method':'Independent finite enumeration; no student source imported',
 'valid_labels_with_bottom_to_top_stacks':stacks,'rejected_stack_orders':rejected,
 'k1_p2_valid_cases':['A','C','E'],'k1_p3':[s for s in valid if s[0]=='M'],
 'k1_p4_completions':comp,'k1_p4_row_solutions':tab,
 'k1_p6_adjacency':adj,'k1_p6_route_witnesses':{k:v[0] for k,v in paths.items()},'k1_p6_route_counts':route_count,
 'grades23_p1_groups':groups,'shared_angle_totals':[alt(x) for x in angles],
 'grades23_p4_added_ray_degrees_clockwise_from_top':added,
 'grades23_p6_total_rooted_orders':len(good),'grades45_p6_orders':rooted,'upper_p3_totals':[alt(x) for x in upper],
 'unequal_D_witness':{'labels':'MVVV','stack_bottom_to_top':d_stack,'flattened_ray_angles':[0,30,-30,120]},
 'physical_models_tested':False}
(ROOT/'independent-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: 8 labels, 4/0/4 tab rows, 2 route endpoints, 10 wedge groups, 4 unique added rays, 36/12 orders; physical pretest outstanding')
