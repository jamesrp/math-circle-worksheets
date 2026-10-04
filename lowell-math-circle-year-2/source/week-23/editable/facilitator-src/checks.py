from itertools import product, permutations, combinations
from collections import defaultdict
import json
from pathlib import Path

def run(v,net):
 a=list(v);h='';trace=[tuple(a)]
 for i,j in net:
  i-=1;j-=1;s=a[i]>a[j];h+='S' if s else 'N'
  if s:a[i],a[j]=a[j],a[i]
  trace.append(tuple(a))
 return tuple(a),h,trace
P3=list(permutations(range(1,4)));P4=list(permutations(range(1,5)));B4=list(product(range(2),repeat=4))
pairs3=list(combinations(range(1,4),2));pairs4=list(combinations(range(1,5),2))
T=[(1,2),(2,3)];R=[(2,3),(1,2)];S3=T+[(1,2)];Q=[(1,3),(1,2),(2,3)]
S4=[(1,2),(3,4),(1,3),(2,4),(2,3)];N4=[(1,2),(2,3),(3,4),(1,2),(2,3),(1,2)]
W=[(1,2),(1,3),(2,3),(2,4)];Bad=[(1,2),(3,4),(1,3),(2,3),(2,4)]
def fails(net,starts):return {''.join(map(str,v)):''.join(map(str,run(v,net)[0])) for v in starts if run(v,net)[0]!=tuple(sorted(v))}
def sorts(net,starts):return not fails(net,starts)
for n,starts in [(S3,P3),(Q,P3),(S4,P4),(S4,B4),(N4,P4),(N4,B4)]:assert sorts(n,starts)
assert not any(sorts(n,P3) for n in product(pairs3,repeat=2))
assert not any(sorts(n,P4) for n in product(pairs4,repeat=4))
assert not any(sorts(n,P4) for n in product([(1,2),(2,3),(3,4)],repeat=5))
repairs=[]
for n in [T,R,[(1,3),(1,2)]]:repairs.append([p for p in pairs3 if sorts(n+[p],P3)])
assert repairs==[[(1,2)],[(2,3)],[(2,3)]]
M3=[[(1,2),(3,4),(1,3),(2,4)],[(1,3),(2,4),(1,2),(3,4)],[(1,2),(3,4),(1,4),(2,3)]]
mrep=[[p for p in pairs4 if sorts(n+[p],P4)] for n in M3]
assert mrep==[[(2,3)],[(2,3)],[]]
assert run((2,4,1,3),M3[2])[0]==(2,1,4,3)
left=list(set(permutations((0,0,1))));right=list(set(permutations((0,1,1))))
assert sorts(T,left) and fails(T,right)=={'110':'101'}
assert sorts(R,right) and fails(R,left)=={'100':'010'}
hist={}
for label,net in [('two',T),('three',S3)]:
 g=defaultdict(list)
 for v in P3:g[run(v,net)[1]].append(''.join(map(str,v)))
 hist[label]=dict(g)
assert hist['two']=={'NN':['123'],'NS':['132','231'],'SN':['213'],'SS':['312','321']}
assert hist['three']=={'NNN':['123'],'NSN':['132'],'SNN':['213'],'NSS':['231'],'SSN':['312'],'SSS':['321']}
short={str(net):next(iter(fails(net,P3))) for net in product(pairs3,repeat=2)}
out={'three_inputs':[{'start':v,'T':run(v,T)[0],'R':run(v,R)[0],'Q':run(v,Q)[0],'T_record':run(v,T)[1],'S3_record':run(v,S3)[1]} for v in P3], 'two_bar_witnesses':short,'four_binary_audit':[{'input':v,'output':run(v,S4)[0]} for v in B4],'M4_failures':fails(W,B4),'U5_bad_failures':fails(Bad,B4),'K4_selective_failures':{'left_on_right':fails(T,right),'right_on_left':fails(R,left)},'histories':hist,'neighbor_reverse_trace':run((4,3,2,1),N4)[2],'enumerated_no_sorters':{'3_lanes_2_bars':9,'4_lanes_4_bars':1296,'4_neighbor_lanes_5_bars':243},'repaired_3':repairs,'repaired_4':mrep}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
