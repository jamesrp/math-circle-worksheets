#!/usr/bin/env python3
"""Exact checks supporting GA-01--08; not substitutes for the written proofs.

Run from any directory. Results are written alongside this file.
No third-party packages, random seeds, network, or PDF generation are used.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / 'ga1-data.json').read_text())
FAMILIES = {f['id']: f for f in DATA['families']}
RESULTS = {}


def record(name, **details):
    RESULTS[name] = {'passed': True, **details}


required = ('id title core_gate extension_gate reading materials prep_minutes timing '
            'launch satisfying_stop prior_use assessment mathematical_connection sources '
            'pages extensions figures index_gate').split()
assert list(FAMILIES) == [f'GA-{i:02}' for i in range(1, 9)]
counts = {}
for fid, family in FAMILIES.items():
    assert all(k in family for k in required)
    for key in required:
        if key not in ('prep_minutes', 'sources', 'pages', 'extensions', 'figures'):
            assert isinstance(family[key], str) and family[key].strip(), (fid, key)
    assert isinstance(family['prep_minutes'], (int, float))
    prompt_ids = []
    for page in family['pages']:
        assert all(isinstance(page[k], str) and page[k] for k in ('title', 'gate', 'intro'))
        for q in page['prompts']:
            prompt_ids.append(q['id'])
            assert all(isinstance(q[k], str) and q[k].strip() for k in ('id', 'text', 'solution'))
            assert q['hints'] and all(isinstance(h, str) and h for h in q['hints'])
    assert prompt_ids == [str(i) for i in range(1, len(prompt_ids)+1)], fid
    for ext in family['extensions']:
        assert all(isinstance(ext[k], str) and ext[k] for k in ('prompt', 'solution', 'gate'))
    for src in family['sources']:
        assert all(isinstance(src[k], str) and src[k] for k in ('title', 'url', 'locator', 'adaptation', 'checked'))
    counts[fid] = {'pages': len(family['pages']), 'prompts': len(prompt_ids)}
assert 'Calculus is essential' in FAMILIES['GA-08']['core_gate']
record('schema_and_complete_keys', family_counts=counts,
       pages=sum(v['pages'] for v in counts.values()),
       prompts=sum(v['prompts'] for v in counts.values()))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def mv(a, v):
    return tuple(sum(a[i][j]*v[j] for j in range(3)) for i in range(3))


IDENT = ((1,0,0),(0,1,0),(0,0,1))
X = ((1,0,0),(0,0,-1),(0,1,0))
Y = ((0,0,1),(0,1,0),(-1,0,0))
def power(a, n):
    ans = IDENT
    for _ in range(n): ans = matmul(a, ans)
    return ans


MOVES = {'X': X, 'Y': Y, 'X−': power(X,3), 'Y−': power(Y,3)}
def word_matrix(word):
    ans = IDENT
    for m in word: ans = matmul(MOVES[m], ans)
    return ans


red, blue = (1,0,0), (0,0,1)
assert (mv(word_matrix(['X','Y']),red), mv(word_matrix(['X','Y']),blue)) == ((0,0,-1),(0,-1,0))
assert (mv(word_matrix(['Y','X']),red), mv(word_matrix(['Y','X']),blue)) == ((0,1,0),(1,0,0))
winners = {}
for n in range(1,4):
    winners[n] = [w for w in product(MOVES, repeat=n)
                  if mv(word_matrix(w),blue)==blue and mv(word_matrix(w),red)!=red]
assert not winners[1] and not winners[2] and winners[3]
assert ('Y','X','Y−') in winners[3]
assert mv(word_matrix(['Y','X','Y−']),red)==(0,1,0)
assert mv(word_matrix(['X','Y','X−']),red)==(0,-1,0)
commute = [(a,b) for a,b in product(range(4), repeat=2)
           if matmul(power(X,a),power(Y,b))==matmul(power(Y,b),power(X,a))]
assert commute==[(a,b) for a,b in product(range(4),repeat=2) if a==0 or b==0 or a==b==2]
for a,b in product(MOVES,repeat=2):
    if a[0]!=b[0]: assert word_matrix([a,b])!=word_matrix([b,a])
assert 2*2-(2*0-0)==4 and 2*0-(2*2-0)==-4
record('GA-01', words_exhausted=sum(4**n for n in range(1,4)),
       minimum_hidden_twist_length=3, shortest_words=winners[3], commuting_power_pairs=commute,
       proof_scope='Finite shortest-word and power classification; same-center real-angle commutativity is proved in prose.')


heights = FAMILIES['GA-02']['figures']['profile']['heights'][:6]
diff = [heights[i]-heights[(i+3)%6] for i in range(6)]
assert diff==[-4,3,-2,4,-3,2]
crossings=[]
for k in range(3):
    d0,d1 = diff[k],diff[k+1]
    u=F(-d0,d1-d0)
    assert 0<u<1
    x=k+u
    ha=heights[k]+u*(heights[k+1]-heights[k])
    hb=heights[k+3]+u*(heights[(k+4)%6]-heights[k+3])
    assert ha==hb
    crossings.append((x,x+3,ha,x/6))
assert crossings==[(F(4,7),F(25,7),F(20,7),F(2,21)),
                   (F(8,5),F(23,5),F(13,5),F(4,15)),
                   (F(7,3),F(16,3),F(2),F(7,18))]
assert all(diff[i+3]==-diff[i] for i in range(3))
def step(t): return int((t%1)>=F(1,2))
for k in range(200): assert step(F(k,200)) != step(F(k,200)+F(1,2))
record('GA-02', opposite_post_differences=diff, all_antipodal_ramp_pairs=crossings,
       proof_scope='Each of three affine pieces has exactly one interior root. General existence uses the written continuity/exchange argument; jump test includes endpoints.')


for B in [F(1,100),F(1,10**9),F(7,3)]:
    for n in range(1,51):
        cost=sum(B/2**(k+1) for k in range(1,n+1))
        assert cost == B/F(2)*(1-F(1,2**n))
        assert cost + B/F(2**(n+1)) == B/2 < B
fractions_list=[]
for q in range(1,102):
    for p in range(q+1):
        fractions_list.append((p,q))
        idx=(q-1)*(q+2)//2+p+1
        assert fractions_list[idx-1]==(p,q)
assert fractions_list[7]==(2,3) and fractions_list[31]==(4,7)
assert fractions_list[5187]==(37,101)
record('GA-03', exact_partial_sum_and_tail_checks=150,
       enumeration_rows=101, enumerated_positions=len(fractions_list),
       sample_indices={'2/3':8,'4/7':32,'37/101':5188},
       proof_scope='The written nth-point argument and geometric limit prove all-countable coverage; density and the supplied interval-cover lower bound are separate arguments.')


routes=[[270,-180,270],[540,-180,360],[540,-180],[-360],[180,-180]]
for route in routes:
    root_angle=F(0)
    target_angle=F(0)
    for move in route:
        target_angle+=move;root_angle+=F(move,2)
        assert 2*root_angle==target_angle
    k=int(target_angle/360)
    assert target_angle==k*360
    assert (root_angle%360==0)==(k%2==0)
for m in range(1,13):
    for k in range(-12,13):
        assert (F(360*k,m)%360==0)==(k%m==0)
assert [F(120,3)+F(360*j,3) for j in range(3)]==[40,160,280]
record('GA-04', signed_routes=routes, mth_root_return_cases=300,
       proof_scope='Angle arithmetic checks explicit routes. Uniqueness of a continuous choice uses the written constant finite-valued ratio argument, not sampled frames.')


def solve_linear(A,b):
    n=len(b)
    m=[[F(x) for x in row]+[F(rhs)] for row,rhs in zip(A,b)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if m[i][k])
        m[k],m[pivot]=m[pivot],m[k]
        lead=m[k][k];m[k]=[x/lead for x in m[k]]
        for i in range(n):
            if i!=k:
                lead=m[i][k]
                m[i]=[x-lead*y for x,y in zip(m[i],m[k])]
    return [row[-1] for row in m]


def harmonic(nodes,edges,boundary):
    neighbors={v:[] for v in nodes}
    for a,b in edges:neighbors[a].append(b);neighbors[b].append(a)
    interior=[v for v in nodes if v not in boundary]
    A=[];rhs=[]
    for v in interior:
        A.append([len(neighbors[v])*(v==w)-neighbors[v].count(w) for w in interior])
        rhs.append(sum(boundary.get(w,0) for w in neighbors[v]))
    result={**{k:F(v) for k,v in boundary.items()}, **dict(zip(interior,solve_linear(A,rhs)))}
    for v in interior:
        assert result[v]*len(neighbors[v])==sum(result[w] for w in neighbors[v])
    return result


graph_figures=FAMILIES['GA-05']['figures']
path=graph_figures['path'];short=graph_figures['shortcut']
sol0=harmonic(path['nodes'],path['edges'],path['boundary'])
sol1=harmonic(short['nodes'],short['edges'],short['boundary'])
sol2=harmonic(short['nodes'],short['edges'],{'L':0,'R':16})
assert [sol0[v] for v in 'abc']==[3,6,9]
assert [sol1[v] for v in 'abc']==[F(9,2),6,F(15,2)]
assert [sol2[v] for v in 'abc']==[6,8,10]
assert [sol2[v]-sol1[v] for v in 'abc']==[F(3,2),2,F(5,2)]
finite_graphs=0
for n in range(2,6):
    all_edges=list(combinations(range(n),2))
    for mask in range(1<<len(all_edges)):
        edges=[e for i,e in enumerate(all_edges) if (mask>>i)&1]
        reached={0}
        while True:
            more={v for a,b in edges if a in reached or b in reached for v in (a,b)}
            if more<=reached:break
            reached|=more
        if len(reached)<n:continue
        vals=harmonic(range(n),edges,{0:0,n-1:12})
        moved=harmonic(range(n),edges,{0:0,n-1:16})
        assert all(0<=v<=12 for v in vals.values())
        assert all(0<=moved[v]-vals[v]<=4 for v in vals)
        finite_graphs+=1
assert finite_graphs==771
record('GA-05', path=sol0, shortcut=sol1, raised_boundary=sol2,
       connected_labeled_graphs_checked=finite_graphs,
       proof_scope='Finite checks support instances. The written maximum propagation proves the arbitrary finite-graph bound; subtraction gives at most one solution, without claiming existence from uniqueness alone.')


# Gaussian rationals as exact pairs.
def C(a=0,b=0):return (F(a),F(b))
def cadd(z,w):return (z[0]+w[0],z[1]+w[1])
def cneg(z):return (-z[0],-z[1])
def csub(z,w):return cadd(z,cneg(w))
def cmul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cdiv(z,w):
    norm=w[0]**2+w[1]**2
    assert norm
    return ((z[0]*w[0]+z[1]*w[1])/norm,(z[1]*w[0]-z[0]*w[1])/norm)
I=C(0,1)
complex_checks=0
for a,b,c,d in product(range(-2,3),repeat=4):
    z,w=C(a,b),C(c,d)
    equation=cadd(cmul(z,z),cmul(w,w))
    factored=cmul(csub(w,cmul(I,z)),cadd(w,cmul(I,z)))
    assert equation==factored
    assert (equation==C())==(w==cmul(I,z) or w==cneg(cmul(I,z)))
    u,v=csub(w,cmul(I,z)),cadd(w,cmul(I,z))
    assert cdiv(cadd(u,v),C(2))==w
    assert cdiv(csub(v,u),C(0,2))==z
    complex_checks+=1
def one_pair(u):
    v=cdiv(C(1),u)
    z,w=cdiv(csub(v,u),C(0,2)),cdiv(cadd(u,v),C(2))
    assert cadd(cmul(z,z),cmul(w,w))==C(1)
    return z,w
assert one_pair(C(2))==(C(0,F(3,4)),C(F(5,4)))
assert one_pair(I)==(C(-1),C())
for s in [F(k,20) for k in range(21)]:
    z=C(1-2*s) if s<=F(1,2) else C(2*s-1)
    w=cmul(I,z) if s<=F(1,2) else cneg(cmul(I,z))
    assert cadd(cmul(z,z),cmul(w,w))==C()
record('GA-06', exact_factorization_and_coordinate_checks=complex_checks,
       constant_one_examples=[one_pair(C(2)),one_pair(I)],
       proof_scope='Written factorization is exhaustive over C. No-switch and local-disc obstruction are topological proofs; finite Gaussian-rational checks do not establish those claims.')


def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return p
def padd(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def pscale(a,s):return trim([s*x for x in a])
def pmul(a,b):
    ans=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return trim(ans)
def compose(a,b):
    ans=[0]
    for coef in reversed(a):ans=padd(pmul(ans,b),[coef])
    return ans
def peval(a,x):
    ans=0
    for coef in reversed(a):ans=ans*x+coef
    return ans
T=[[1],[0,1]]
for n in range(1,37):T.append(padd(pmul([0,2],T[-1]),pscale(T[-2],-1)))
assert T[2]==[-1,0,2] and T[3]==[0,-3,0,4]
assert T[6]==[-1,0,18,0,-48,0,32]
assert compose(T[2],T[3])==compose(T[3],T[2])==T[6]
for m,n in product(range(7),repeat=2):assert compose(T[m],T[n])==T[m*n]
fake=padd(T[3],pmul([0,1],pmul([-1,0,1],[F(-1,4),0,1])))
for x in [F(-1),F(-1,2),F(0),F(1,2),F(1)]:assert peval(fake,x)==peval(T[3],x)
assert peval(fake,F(1,4))!=peval(T[3],F(1,4))
# The extra term at x=sqrt(2)/2 is -x/8 = -sqrt(2)/16.
assert (F(1,2)-1)*(F(1,2)-F(1,4))==F(-1,8)
assert solve_linear([[1,1],[1,4]],[1,-8])==[4,-3]
record('GA-07', T2=T[2],T3=T[3],T6=T[6], exact_compositions=49,
       fake_polynomial=fake,
       proof_scope='Exact coefficient arithmetic verifies each displayed identity. The general angle identity is established by the supplied cosine addition formula and induction; all-real extension uses the stated polynomial root bound.')


def sqrt_fraction(q):
    from math import isqrt
    a,b=isqrt(q.numerator),isqrt(q.denominator)
    assert a*a==q.numerator and b*b==q.denominator
    return F(a,b)


ode_checks=0
for c in [F(0),F(3,2),F(2),F(17,7)]:
    for t in [F(k,14) for k in range(85)]+[c]:
        y=max(t-c,0)**2
        dydt=2*max(t-c,0)
        assert dydt==2*sqrt_fraction(y)
        ode_checks+=1
    for h in [F(1,2**k) for k in range(1,15)]:
        right=(h*h)/h
        assert right==h
        if c and h<c:assert F(0)/(-h)==0
for a in [F(k*k,16) for k in range(17)]:
    root=sqrt_fraction(a)
    valid_quadratic=all(2*a*t==2*root*t for t in [F(1),F(2),F(7,3)])
    assert valid_quadratic==(a in (0,1))
    valid_quartic=all(4*a*t**3==2*root*t**2 for t in [F(1),F(2)])
    assert valid_quartic==(a==0)
for n in range(1,51):
    h=F(1,n*n)
    assert 2*sqrt_fraction(h)/h==2*n
record('GA-08', rational_piecewise_checks=ode_checks,
       join_quotients={'left':'0','right':'h','limit':'0'},
       lipschitz_ratios='For h=1/n², ratio=2n, unbounded.',
       complete_classification='Forever zero, or zero on [0,c] and (t-c)² on [c,∞), c≥0.',
       proof_scope='The written monotonicity, zero-set, chain-rule and join arguments prove the classification. Rational samples verify instances only. Product-rule proof handles y′=y; nonincreasing/nonnegative proof handles y′=−2√y.')


out={
    'batch':'ga1',
    'status':'all exact checks passed; written proofs require independent review',
    'data_sha256':hashlib.sha256((HERE/'ga1-data.json').read_bytes()).hexdigest(),
    'checks':RESULTS,
}
(HERE/'ga1-checks-results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,default=str)+'\n')
print(json.dumps({'status':'passed','families':len(FAMILIES),
                  'student_pages':sum(v['pages'] for v in counts.values()),
                  'keyed_prompts':sum(v['prompts'] for v in counts.values()),
                  'check_groups':len(RESULTS)},indent=2))
