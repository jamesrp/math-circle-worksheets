"""Exact finite audits for AP3. General proofs live in ap3-data.json.

The enumeration here is independent of the formula presentations in the key:
linear constraints are intersected, reaction states are searched by legal moves,
parent identities are enumerated, and all received words are compared.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter, deque
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'ap3-data.json').read_text())
expected=['AP-19','AP-20','AP-22','AP-24','AP-25','AP-27','AP-28','AP-30']
assert [f['id'] for f in data['families']]==expected
required={'id','title','core_gate','index_gate','extension_gate','reading','materials','prep_minutes','timing','launch','satisfying_stop','prior_use','assessment','mathematical_connection','sources','pages','extensions','figures'}
for f in data['families']:
    assert required<=f.keys()
    qs=[q for p in f['pages'] for q in p['prompts']]
    assert [q['id'] for q in qs]==list(map(str,range(1,7)))
    assert all(q['text'] and q['solution'] and q['hints'] for q in qs)
    assert len(f['extensions'])==1
results={'schema':{'families':8,'pages':24,'prompts':48,'keyed_extensions':8}}

# AP19: forward time synthesis, linear inversion and sharp bounded noise.
T=F(5)
survey_cases=0
for u in [F(i,60) for i in range(1,50)]:
    v=T/6-u
    assert v>0
    for x in map(F,range(1,12)):
        S=min(x,6)*u+max(x-6,0)*v
        if x<=6:
            uu=S/x; vv=T/6-uu
            assert 0<S<x*T/6
        else:
            vv=(T-S)/(12-x); uu=T/6-vv
            assert (x-6)*T/6<S<T
        assert (uu,vv)==(u,v)
        for e in [F(-1,10000),F(0),F(1,10000)]:
            if x<=6: du=e/x; dv=-e/x
            else: du=e/(12-x); dv=-e/(12-x)
            assert abs(du)==abs(dv)==abs(e)/min(x,12-x)
        survey_cases+=1
assert [F(6,1)/(5-F(6,s)) for s in [2,3,4]]==[F(3),F(2),F(12,7)]
noise_intervals=[]
for x,report in [(F(3),F(3,2)),(F(6),F(3))]:
    us=[(report+e)/x for e in [F(-1,20),F(1,20)]]
    vs=sorted(T/6-u for u in us)
    noise_intervals.append({'x':str(x),'u':list(map(str,us)),'v':list(map(str,vs)),
        'H1':list(map(str,[1/us[1]**2,1/us[0]**2])),
        'H2':list(map(str,[1/vs[1]**2,1/vs[0]**2]))})
assert noise_intervals[0]['H2']==['400/49','3600/361']
assert noise_intervals[1]['H2']==['14400/1681','1600/169']
assert min(range(1,12),key=lambda x:F(1,min(x,12-x)))==6
results['AP-19']={'forward_inverse_instances':survey_cases,'noise_intervals':noise_intervals,'best_integer_receiver':6,'general_continuous_placement_proof':'ε/min(x,12−x), proved in key'}

# AP20: exhaustive integer plans and independent vertex intersection for LP.
def integer_plans(R,B):
    return [(x,y,3*x+4*y) for x in range(R+B+1) for y in range(R+B+1) if 2*x+y<=R and x+2*y<=B]
plans={}
for R,B in [(5,4),(4,4),(4,5)]:
    ps=integer_plans(R,B); best=max(z for x,y,z in ps)
    plans[f'{R},{B}']={'feasible':ps,'optimum':best,'attainers':[(x,y) for x,y,z in ps if z==best]}
assert [plans[k]['optimum'] for k in ['5,4','4,4','4,5']]==[10,8,11]
def vertices(R,B):
    lines=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(2),F(1),R),(F(1),F(2),B)]
    out=set()
    for (a,b,c),(d,e,f) in combinations(lines,2):
        det=a*e-b*d
        if not det: continue
        x=(c*e-b*f)/det; y=(a*f-c*d)/det
        if x>=0 and y>=0 and 2*x+y<=R and x+2*y<=B: out.add((x,y))
    return out
for R in [F(i,2) for i in range(25)]:
    val=max(3*x+4*y for x,y in vertices(R,F(4)))
    formula=4*R if R<=2 else (2*R+20)/3 if R<=8 else F(12)
    assert val==formula
assert max(3*x+4*y for x,y in vertices(F(4),F(4)))==F(28,3)
results['AP-20']={'integer_audits':plans,'independent_vertex_capacity_tests':25,'fractional_4_4':'28/3','piecewise_capacity_formula':'4R; (2R+20)/3; 12 on R≤2, 2≤R≤8, R≥8'}

# AP22: joint-outcome expectations and every grid strategy/tolerance.
grid=sorted(set(F(i,n) for n in range(1,31) for i in range(n+1)))
def payoff(p,q): return 2*p*q+(1-p)*(1-q)
row_guarantees={p:min(payoff(p,q) for q in [F(0),F(1)]) for p in grid}
col_caps={q:max(payoff(p,q) for p in [F(0),F(1)]) for q in grid}
assert max(row_guarantees.values())==min(col_caps.values())==F(2,3)
assert [p for p,v in row_guarantees.items() if v==F(2,3)]==[F(1,3)]
assert [q for q,v in col_caps.items() if v==F(2,3)]==[F(1,3)]
tolerance_tests=0
for eps in [F(i,60) for i in range(21)]:
    for p in grid:
        assert (row_guarantees[p]>=F(2,3)-eps)==(F(1,3)-eps/2<=p<=F(1,3)+eps)
        assert (col_caps[p]<=F(2,3)+eps)==(F(1,3)-eps<=p<=F(1,3)+eps/2)
        tolerance_tests+=2
assert sum([F(2,3),F(1,3),F(1,3)])==F(4,3)
assert payoff(F(1),F(3,4))==F(3,2)
for A,B in product([F(1,3),F(1),F(2),F(3),F(7,2)],repeat=2):
    p=B/(A+B); assert A*p==B*(1-p)==A*B/(A+B)
results['AP-22']={'strategy_probabilities':len(grid),'tolerance_membership_tests':tolerance_tests,'value':'2/3','shared_ticket_expectation':'4/3','parameter_checks':25}

# AP24: enumerate ordered parent identities, not merely a binomial formula.
def transition(N,i):
    cnt=Counter(sum(parent<i for parent in draws) for draws in product(range(N),repeat=N))
    return [F(cnt[j],N**N) for j in range(N+1)]
transitions={}
parent_strings=0
for N in range(2,7):
    mat=[transition(N,i) for i in range(N+1)]
    parent_strings+=(N+1)*N**N
    for i,row in enumerate(mat):
        assert sum(row)==1 and sum(j*p for j,p in enumerate(row))==i
        assert row[0]+row[N]>=F(1,N**N)
    if N in [2,3]:
        transitions[str(N)]=[[str(p) for p in row] for row in mat]
        dist=[F(j==1) for j in range(N+1)]
        for k in range(13):
            assert sum(j*p for j,p in enumerate(dist))==1
            assert sum(dist[1:N])==(F(1,2) if N==2 else F(2,3))**k
            if N==2: assert dist[0]==dist[2]==(1-F(1,2)**k)/2
            dist=[sum(dist[i]*mat[i][j] for i in range(N+1)) for j in range(N+1)]
M=[transition(3,i) for i in range(4)]
# Candidate fixation probabilities solve all first-step equations, independent of the expectation derivation.
fix=[F(0),F(1,3),F(2,3),F(1)]
assert all(sum(M[i][j]*fix[j] for j in range(4))==fix[i] for i in range(4))
results['AP-24']={'ordered_parent_strings_enumerated':parent_strings,'N2_N3_transition_rows':transitions,'finite_time_distributions_checked':26,'general_absorption_bound':'(1−N^(−N))^k; general proof in key','N3_fixation_from_one_red':'1/3'}

# AP25: BFS by consumed/produced inventories; compare with invariant classes.
def reachable(start,reactions):
    seen={start}; todo=deque([start])
    while todo:
        s=todo.popleft()
        for consume,produce in reactions:
            if all(s[i]>=consume[i] for i in range(len(s))):
                t=tuple(s[i]-consume[i]+produce[i] for i in range(len(s)))
                if t not in seen: seen.add(t);todo.append(t)
    return seen
reaction=[((1,2,0),(0,0,1)),((0,0,1),(1,2,0))]
reaction_tests=0
for a,b,c in product(range(7),repeat=3):
    actual=reachable((a,b,c),reaction)
    M=a+c;N=b+2*c
    predicted={(M-z,N-2*z,z) for z in range(min(M,N//2)+1)}
    assert actual==predicted
    reaction_tests+=1
start_states=sorted(reachable((4,7,1),reaction),key=lambda s:s[2])
assert start_states==[(5,9,0),(4,7,1),(3,5,2),(2,3,3),(1,1,4)]
for wa,wb,wc in product(range(-5,6),repeat=3):
    assert (wa+2*wb==wc)==(sum(w*s for w,s in zip((wa,wb,wc),(1,2,0)))==sum(w*s for w,s in zip((wa,wb,wc),(0,0,1))))
double=[((2,0),(0,2)),((0,2),(2,0))]
assert reachable((5,0),double)=={(5,0),(3,2),(1,4)}
catalyst=[((1,1),(0,2)),((0,2),(1,1))]
for a,b in product(range(7),repeat=2):
    expected_states={(a,0)} if b==0 else {(a+b-z,z) for z in range(1,a+b+1)}
    assert reachable((a,b),catalyst)==expected_states
results['AP-25']={'core_BFS_inventories':reaction_tests,'initial_state_chain':start_states,'weight_tests':11**3,'catalytic_BFS_inventories':49,'two_A_two_B_states':[[5,0],[3,2],[1,4]]}

# AP27: synthesize outputs then recover, including nonnegative boundaries.
obs_tests=0
for a,b in product(map(F,range(9)),repeat=2):
    for r,s in product([F(1,4),F(1,2),F(49,100),F(3,4)],repeat=2):
        if r==s: continue
        y0=a+b; y1=r*a+s*b
        aa=(y1-s*y0)/(r-s);bb=(r*y0-y1)/(r-s)
        assert (aa,bb)==(a,b)
        obs_tests+=1
for y0 in map(F,range(-2,11)):
    for y1 in [F(i,4) for i in range(-4,25)]:
        a=4*y1-y0;b=2*y0-4*y1
        assert (a>=0 and b>=0)==(y0>=0 and y0/4<=y1<=y0/2)
assert F(4)*F(1,2)+F(4)*F(49,100)==F(99,25)
assert F(1,100)/(F(1,2)-F(1,4))==F(1,25)
assert F(1,100)/(F(1,2)-F(49,100))==1
gaps={k:F(3,4)**k-F(1,2)**k for k in range(1,51)}
assert max(gaps,key=gaps.get)==2 and gaps[2]==F(5,16)
assert F(1,100)/gaps[2]==F(4,125)
for k in range(1,50):
    assert gaps[k+1]-gaps[k]==F(1,4)*F(1,2)**k*(2-F(3,2)**k)
results['AP-27']={'forward_inverse_cases':obs_tests,'nonnegative_reading_tests':13*29,'delay_gaps_checked':50,'optimal_positive_integer_delay':2,'best_error_bound':'4/125','global_delay_proof':'Sign of consecutive difference, in key'}

# AP28: all pair distances, all received words, and every four-word length-four codebook.
def distance(a,b):return sum(x!=y for x,y in zip(a,b))
code=['00000','11100','10011','01111']
pairs=[distance(a,b) for a,b in combinations(code,2)]
assert pairs==[3,3,4,4,3,3]
words=[''.join(w) for w in product('01',repeat=5)]
balls=[{w for w in words if distance(c,w)<=1} for c in code]
assert all(len(ball)==6 for ball in balls)
assert all(not a&b for a,b in combinations(balls,2))
covered=set.union(*balls);uncovered=sorted(set(words)-covered)
assert len(covered)==24 and len(uncovered)==8 and '00110' in uncovered
for received,idx in [('10111',2),('01000',0),('11100',1),('11000',1)]:
    assert [i for i,c in enumerate(code) if distance(c,received)<=1]==[idx]
short=[''.join(w) for w in product('01',repeat=4)]
valid4=[cs for cs in combinations(short,4) if min(distance(a,b) for a,b in combinations(cs,2))>=3]
assert not valid4
even=['000','011','101','110']
assert all(distance(a,b)==2 for a,b in combinations(even,2))
assert [i for i,c in enumerate(even) if distance(c,'001')==1]==[0,1,2]
def syndrome(w):return ((int(w[0])+int(w[1])+int(w[3]))%2,(int(w[1])+int(w[2])+int(w[4]))%2)
kernel=[w for w in words if syndrome(w)==(0,0)]
assert len(kernel)==8 and '10010' in kernel
assert all(syndrome(w)!=(0,0) for c in kernel for w in words if distance(w,c)==1)
detected_errors=[w for w in words if syndrome(w)!=(0,0)]
missed_nonzero_errors=[w for w in kernel if w!='00000']
assert len(detected_errors)==24 and len(missed_nonzero_errors)==7
for c,e in product(kernel,words):
    received=''.join(str(int(x)^int(y)) for x,y in zip(c,e))
    assert syndrome(received)==syndrome(e)
results['AP-28']={'pair_distances':pairs,'covered_received_words':24,'uncovered_words':uncovered,'four_word_length4_codebooks_checked':1820,'valid_length4_codebooks':0,'parity_kernel_size':8,'detected_error_patterns':24,'missed_nonzero_kernel_errors':missed_nonzero_errors,'syndrome_identity_tests':256}

# AP30: solve Kirchhoff balance as X=(V/a)/(1/a+1/b+m/R).
circuit_tests=0
for R in sorted(set(F(i,j) for i in range(1,16) for j in range(1,8))):
    for m in range(1,7):
        X=F(3)/(F(3,2)+F(m)/R)
        Iin=(6-X)/2; Ilower=X; Imeter=X/R
        assert Iin==Ilower+m*Imeter
        assert X==6*R/(3*R+2*m)
        assert 6*Iin==2*Iin**2+Ilower**2+m*R*Imeter**2
        error=(2-X)/2
        for eps in [F(1,100),F(1,10),F(1,2),F(9,10)]:
            threshold=2*m*(1-eps)/(3*eps)
            assert (error<=eps)==(R>=threshold)
        circuit_tests+=1
assert 2*(1-F(1,100))/(3*F(1,100))==66
assert 6*F(66)/(3*66+2)==F(99,50)
for V,a,b,R in product([F(1,2),F(1),F(2),F(3)],repeat=4):
    X=(V/a)/(1/a+1/b+1/R)
    V0=V*b/(a+b);Rs=a*b/(a+b)
    assert X==V0*R/(R+Rs) and (V0-X)/V0==Rs/(R+Rs)
results['AP-30']={'loaded_network_tests':circuit_tests,'all_energy_balances_exact':True,'general_resistance_tests':4**4,'one_percent_R_one_meter':66,'one_percent_R_two_meters':132}

results['status']='all exact finite audits passed; general proofs and model scope are in the keyed designs'
(ROOT/'ap3-checks-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v if k in ['schema','status'] else 'passed' for k,v in results.items()},ensure_ascii=False,indent=2))
