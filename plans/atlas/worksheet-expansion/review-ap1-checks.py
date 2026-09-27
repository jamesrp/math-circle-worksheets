#!/usr/bin/env python3
"""Independent reviewer calculations for AP1; complements the author's audit."""
from fractions import Fraction as Q
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json
r={}
# AP02: compute likelihoods directly, rather than reuse labeled-grid enumeration.
likelihoods={'RR':(Q(4,9),Q(1,9)),'RB':(Q(2,9),Q(2,9)),'different':(Q(4,9),Q(4,9)),'at_least_red':(Q(8,9),Q(5,9))}
post={k:str(a/(a+b)) for k,(a,b) in likelihoods.items()}
assert post=={'RR':'4/5','RB':'1/2','different':'1/2','at_least_red':'8/13'}
assert Q(1,3)*Q(2,3)==Q(2,3)*Q(1,3)
for n in range(1,15):
    assert max(Q(a,a+b) for a in range(1,n+1) for b in range(1,n+1))==Q(n,n+1)
r['AP-02']={'posteriors':post,'fixed_size_optima_checked_through':14}
# AP03: complementary pairs, plus the tied-outcome guide extension.
v=(0,1,2,4,5,6);pair_sums=[]
for b,c in combinations(range(1,6),2):
    s=v[0]+v[b]+v[c];pair_sums.append((s,sum(v)-s))
all_sums=[s for pair in pair_sums for s in pair]
assert len(all_sums)==20 and Counter(all_sums)[15]==1 and Counter(all_sums)[3]==1
pair_design=[a+b+c for a,b,c in product((0,6),(1,5),(2,4))]
assert sorted(pair_design)==[3,5,7,9,9,11,13,15]
tied=[sum((0,0,1,1,2,2)[i] for i in inds) for inds in combinations(range(6),3)]
assert max(tied)==5 and tied.count(5)==2
r['AP-03']={'complementary_sum_pairs':pair_sums,'paired_sums':sorted(pair_design),'tied_extension_tail':'1/10'}
# AP04: generating-value pair laws, including varied-block extension.
full=Counter(Q(a+b,2) for a,b in product((1,5),repeat=2))
block=Counter(Q(a+b,2) for a,b in product((0,2),(4,6)))
assert full=={Q(1):1,Q(3):2,Q(5):1}
assert block=={Q(2):1,Q(3):2,Q(4):1}
r['AP-04']={'full_mean_law':{str(k):str(Q(v,4)) for k,v in full.items()},'varied_block_law':{str(k):str(Q(v,4)) for k,v in block.items()},'unequal_block_weighted_mean':str(Q(2*1+6*5,8))}
# AP05: reflect coverage into error space; check all endpoint choices in expanded range.
best=[]
for width in range(0,7):
    for a in range(-20,21):
        errors_in=[e for e in range(-2,3) if -a-width<=e<=-a]
        if len(errors_in)>=4:best.append((width,a,a+width))
assert [x for x in best if x[0]==min(t[0] for t in best)]==[(3,-2,1),(3,-1,2)]
assert all(not(-1<=e<=1) for e in (-2,2))
r['AP-05']={'minimum_width':3,'minimizers':[[-2,1],[-1,2]],'changed_error_coverage':0}
# AP06: an independently simplified Newton map and exact contraction threshold.
N=lambda x:2*x**3/(3*x*x-5)
assert N(Q(1))==-1 and N(Q(-1))==1
assert N(N(Q(2)))==Q(8192,3661)
assert Q(9,4)<=N(Q(2))<=Q(11,4)
assert N(Q(2))**3-5*N(Q(2))==Q(176,343)
assert 2*Q(3,4)**18>=Q(1,100)>2*Q(3,4)**19
r['AP-06']={'second_step_from2':str(N(N(Q(2)))),'guarded_brackets':[['1','3'],['2','3'],['2','16/7']],'width18_bound':str(2*Q(3,4)**18),'width19_bound':str(2*Q(3,4)**19)}
# AP08: choose the suffix for each of 15 history pairs, using actual words.
histories=['','R','RR','B','RB','RRB'];certs=[]
accept=lambda s:s.count('R')%3==0 and s.count('B')%2==0
for a,b in combinations(histories,2):
    suffix='R'*((-a.count('R'))%3)+'B'*((-a.count('B'))%2)
    assert accept(a+suffix) and not accept(b+suffix)
    certs.append([a,b,suffix])
assert [accept(s) for s in ['RRR','BBB','RBRBRBB','']]==[True,False,True,True]
r['AP-08']={'pairwise_suffix_certificates':certs}
# AP09: direct 2x2 matrix products and change-of-basis multiplication.
mm=lambda a,b:[[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
K=[[2,-1],[-1,2]];V=[[1,1],[1,-1]];Vi=[[Q(1,2),Q(1,2)],[Q(1,2),Q(-1,2)]]
assert mm(mm(Vi,K),V)==[[1,0],[0,3]]
for m in range(2,8):
    k=Q(m*m-1,2);A=[[1+k,-k],[-k,1+k]]
    assert mm(mm(Vi,A),V)==[[1,0],[0,m*m]]
r['AP-09']={'diagonalized_stiffness':[[1,0],[0,3]],'integer_frequency_tuning_checked':[2,3,4,5,6,7]}
# AP10: generate full labeled binary construction trees, preserving duplicates until evaluation.
def trees(n):
    if n==1:return [Q(1)]
    ans=[]
    for a in range(1,n):
        for x in trees(a):
            for y in trees(n-a):ans += [x+y,x*y/(x+y)]
    return ans
v3=trees(3);v4=trees(4)
assert set(v3)=={Q(1,3),Q(2,3),Q(3,2),Q(3)} and Q(1) not in v3 and Q(1) in v4
assert Q(2)*Q(2)/(Q(2)+Q(2))==1 and Q(1,2)+Q(1,2)==1
r['AP-10']={'three_spring_stiffnesses':list(map(str,sorted(set(v3)))),'four_spring_stiffnesses':list(map(str,sorted(set(v4))))}
r['status']='PASS; independent calculations supplement the written review of all prompts and general proofs.'
Path(__file__).with_name('review-ap1-checks-results.json').write_text(json.dumps(r,indent=2)+'\n')
print(r['status'])
