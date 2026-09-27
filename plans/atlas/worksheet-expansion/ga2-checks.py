#!/usr/bin/env python3
"""Exact finite and symbolic checks for GA2; general arguments remain in the keys."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
out={}

# GA09: formal derivatives in the basis sin(theta), cos(theta).
def derivative(v,speed):
    sine,cosine=v
    return (-speed*cosine,speed*sine)
v=(F(1),F(0))
xx=derivative(derivative(v,F(1)),F(1))
travel={}
for c in [-2,-1,0,1,2]:
    t=derivative(v,F(-c));tt=derivative(t,F(-c))
    assert (tt==xx)==(abs(c)==1)
    assert t!=xx
    travel[str(c)]={'wave':tt==xx,'heat':t==xx}
for a in [0,1,4]:
    assert (-a==-1)==(a==1)
    assert a*a!=-1
for b in [F(-3),F(-1),F(0),F(1,2),F(2)]:
    # Time factor cos t+b sin t; coefficient ordering remains sine,cosine.
    factor=(b,F(1))
    assert derivative(derivative(factor,1),1)==tuple(-x for x in factor)
    assert sum(x*x for x in derivative(factor,1))==1+b*b
for k in range(1,21):
    assert derivative(derivative(v,k),k)==(-k*k,0)
out['GA-09']={'traveling_mode_law_classification':travel,'spatial_modes_checked':20,
 'scope':'Formal differentiation establishes the displayed parameter conditions. The fixed-end and mode-independence arguments are written in the solutions; no general PDE theorem is inferred.'}

# GA10: compose inverse affine maps independently of forward iteration.
def inverse_word(word):
    a,b=F(1),F(0)
    for letter in reversed(word):
        if letter=='L':a,b=a/2,b/2
        else:a,b=-a/2,1-b/2
    return a,b

def tent(x):return 2*x if x<=F(1,2) else 2-2*x

def word_period(word):
    return next(d for d in range(1,len(word)+1)
                if len(word)%d==0 and word==word[:d]*(len(word)//d))

counts={};programs=0;points4=[]
for n in range(1,11):
    starts=set();periods=Counter()
    for letters in product('LR',repeat=n):
        w=''.join(letters);a,b=inverse_word(w);x=b/(1-a)
        assert 0<=x<=1 and abs(a)==F(1,2**n)
        assert x not in starts
        starts.add(x);y=x;orbit=[];labels=''
        for i in range(n):
            assert y not in [F(1,2),F(1)]
            orbit.append(y);labels+='L' if y<F(1,2) else 'R';y=tent(y)
        assert labels==w and y==x
        least=next(i for i in range(1,n+1) if orbit[i%n]==x)
        assert least==word_period(w)
        periods[least]+=1;programs+=1
        if n==4:points4.append((w,x,least))
    counts[str(n)]={str(p):c for p,c in sorted(periods.items())}
assert counts['4']=={'1':2,'2':2,'4':12}
assert counts['6']=={'1':2,'2':2,'3':6,'6':54}
cycles4=[list(map(F,row)) for row in [
 ['2/17','4/17','8/17','16/17'],['2/15','4/15','8/15','14/15'],
 ['6/17','12/17','10/17','14/17']]]
assert {x for cyc in cycles4 for x in cyc}=={x for w,x,p in points4 if p==4}
for cyc in cycles4:
    assert [tent(x) for x in cyc]==cyc[1:]+cyc[:1]
out['GA-10']={'exact_programs_checked':programs,'period_counts_among_fixed_points':counts,
 'least_period_four_cycles':[[str(x) for x in cyc] for cyc in cycles4],
 'scope':'Finite enumeration checks every word through length ten. The affine self-map proof, periodic-boundary exclusion and least-period proof in the key cover all finite lengths.'}

# GA12: strict sums, block certificates and finite geometric identities.
H16=sum(F(1,n) for n in range(1,17))
assert H16>3
for n in range(1,25):
    Gn=sum(F(1,2**j) for j in range(n))
    assert Gn==2-F(1,2**(n-1))
assert next(n for n in range(1,20) if F(1,2**(n-1))<F(1,100))==8
block_count=0
for N in range(1,65):
    block=sum(F(1,n) for n in range(N+1,2*N+1))
    assert block>=F(1,2)
    assert (block>F(1,2))==(N>1)
    block_count+=1
for budget in [F(j,3) for j in range(1,61)]:
    k=max(1,int(2*(budget-1))+1)
    assert 1+F(k,2)>budget
for n in range(1,31):
    partial_sums=[i%2 for i in range(1,n+1)]
    avg=F(sum(partial_sums),n)
    assert avg==(F(1,2) if n%2==0 else F(n+1,2*n))
out['GA-12']={'H16':str(H16),'H16_minus_3':str(H16-3),
 'tail_start_values_checked':block_count,'geometric_epsilon_1_100_least_payments':8,
 'harmonic_budget_10_guarantee':2**19,
 'scope':'Finite checks verify strict inequalities and indexing. The repeated-block rule and geometric remainder prove the infinite statements; sparse deletion changes the payment rule.'}

# GA13: exact quadratic extrema, not a sampled graph maximum.
def quadratic_error(a,b,left,right):
    points=[left,right]
    vertex=a/2
    if left<=vertex<=right:points.append(vertex)
    return max(abs(x*x-a*x-b) for x in points)
intervals=0
for center in [F(-3),F(-1,2),F(0),F(2),F(7,3)]:
    for radius in [F(1,4),F(1,2),F(1),F(3,2),F(3)]:
        left,right=center-radius,center+radius
        a,b=2*center,-center*center+radius*radius/2
        assert quadratic_error(a,b,left,right)==radius*radius/2
        assert [x*x-a*x-b for x in [left,center,right]]==[
            radius*radius/2,-radius*radius/2,radius*radius/2]
        assert quadratic_error(a,b+radius*radius/2,left,right)==radius*radius
        # Independent all-three-location certificate for many competing lines.
        for da,db in product([F(-1),F(-1,4),F(0),F(1,4),F(1)],repeat=2):
            err=quadratic_error(a+da,b+db,left,right)
            assert err>=radius*radius/2
            assert (err==radius*radius/2)==(da==db==0)
        intervals+=1
assert quadratic_error(F(4),F(-7,2),F(1),F(3))==F(1,2)
values=[1,4,-2,1,0]
assert min(values)==-2 and max(values)==4 and (max(values)+min(values))/2==1
out['GA-13']={'exact_interval_certificates':intervals,'competing_lines_per_interval':25,
 'scope':'Endpoint/vertex extrema are exact. Finite competitors do not prove minimax; the three-point lower bound, equality conditions and affine transfer in the key do.'}

# GA14: exact phase congruences, including the extra observation that fails.
def integer(x):return x.denominator==1

def same_sine_turns(a,b):
    return integer(a-b) or integer(a+b-F(1,2))
assert same_sine_turns(F(1,12),F(5,12))
assert not same_sine_turns(F(1,8),F(5,8))
for k in range(513):
    regular=all(same_sine_turns(F(k*n,4),F(n,4)) for n in range(-8,9))
    assert regular==(k%4==1)
    extra=regular and same_sine_turns(F(k,8),F(1,8))
    assert extra==(k%8==1)
    assert all(same_sine_turns(F(k*n,2),F(n,2)) for n in range(-8,9))
    full=all(integer(F((k-1)*n,2)) for n in range(-8,9))
    assert full==(k%2==1)
observed=[F(0),F(1,4),F(1,2),F(3,4),F(1),F(1,8)]
def perturb(t):
    answer=F(1)
    for s in observed:answer*=t-s
    return answer
assert all(perturb(t)==0 for t in observed)
assert perturb(F(1,3))!=0
out['GA-14']={'integer_frequencies_checked':513,'regular_alias_class':'k=1 mod 4',
 'after_extra_one_eighth':'k=1 mod 8','half_rate_full_arrow_alias_class':'odd k',
 'failed_extra_time':'1/12','finite_record_nonzero_polynomial_check':str(perturb(F(1,3))),
 'scope':'Congruence proofs cover every integer frequency. Polynomial vanishing proves nonuniqueness for any finite record of an unrestricted continuous signal.'}

# GA15: four- and eight-character cancellation; translate actual grid entries.
H=[(1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def decode(v):return tuple(F(dot(v,p),4) for p in H)
def encode(c):return tuple(sum(c[j]*H[j][i] for j in range(4)) for i in range(4))
assert [[dot(a,b) for b in H] for a in H]==[[4*int(i==j) for j in range(4)] for i in range(4)]
assert decode((5,0,1,2))==(F(2),F(1,2),F(1),F(3,2))
assert encode((F(3),F(-1),F(1,2),F(1,2)))==(3,1,4,4)
patterns=0
for v in product(range(-2,3),repeat=4):
    c=decode(v);assert encode(c)==v
    column=(v[1],v[0],v[3],v[2]);row=(v[2],v[3],v[0],v[1])
    assert decode(column)==(c[0],c[1],-c[2],-c[3])
    assert decode(row)==(c[0],-c[1],c[2],-c[3])
    patterns+=1
bits=list(product((0,1),repeat=3))
H8=[[(-1)**dot(a,x) for x in bits] for a in bits]
assert [[dot(a,b) for b in H8] for a in H8]==[[8*int(i==j) for j in range(8)] for i in range(8)]
for p in [F(i,2) for i in range(11)]:
    for q in [F(i,2) for i in range(7)]:
        v=(p,5-p,q,3-q)
        assert min(v)>=0 and sum(v)==8 and dot(v,H[1])==2
out['GA-15']={'four_square_patterns_and_swaps_checked':patterns,
 'target_weights':[str(x) for x in decode((5,0,1,2))],
 'eight_character_gram_matrix':'8 times identity',
 'scope':'Exact Gram matrices and explicit coordinate reconstruction verify the basis claims; the key proves them for all real inputs.'}

# GA16: direct interval intersection versus cases; exact areas and third convolution.
def overlap(a,b,t):return max(F(0),min(a,t)-max(F(0),t-b))
def cases(a,b,t):
    a,b=max(a,b),min(a,b)
    if t<=0 or t>=a+b:return F(0)
    if t<=b:return t
    if t<=a:return b
    return a+b-t

def linear_integral(y0,y1,width):return (y0+y1)*width/2
pairs=0;samples=0
for a,b in product([F(i,2) for i in range(1,9)],repeat=2):
    for i in range(-4,int(4*(a+b))+5):
        t=F(i,4)
        assert overlap(a,b,t)==cases(a,b,t)==overlap(b,a,t)
        assert overlap(a,b,t)==max(F(0),min(a,b,t,a+b-t))
        samples+=1
    knots=sorted(set([F(0),a,b,a+b]))
    area=sum(linear_integral(overlap(a,b,x),overlap(a,b,y),y-x)
             for x,y in zip(knots,knots[1:]))
    assert area==a*b;pairs+=1
for S,Ht in product([F(i,2) for i in range(1,17)],[F(i,2) for i in range(1,9)]):
    if S>=2*Ht:
        a,b=Ht,S-Ht
        assert a>0 and b>0 and a+b==S and min(a,b)==Ht

def triangle(x):return max(F(0),min(x,2-x))
def third_integral(t):
    lo,hi=t-1,t
    cuts=sorted(set([lo,hi]+[x for x in [F(0),F(1),F(2)] if lo<x<hi]))
    return sum(linear_integral(triangle(x),triangle(y),y-x) for x,y in zip(cuts,cuts[1:]))
def third_formula(t):
    if t<=0 or t>=3:return F(0)
    if t<=1:return t*t/2
    if t<=2:return (-2*t*t+6*t-3)/2
    return (3-t)**2/2
for i in range(-8,33):
    t=F(i,8)
    assert third_integral(t)==third_formula(t)
# One-sided derivative polynomials at all joins.
derivative_pieces=[lambda t:F(0),lambda t:t,lambda t:-2*t+3,lambda t:t-3,lambda t:F(0)]
for i,t in enumerate(map(F,[0,1,2,3])):
    assert derivative_pieces[i](t)==derivative_pieces[i+1](t)
out['GA-16']={'positive_window_pairs_checked':pairs,'exact_displacements_checked':samples,
 'unit_triple_convolution_exact_samples':41,'first_derivative_joins_checked':4,
 'scope':'Endpoint cases and piecewise integration in the key prove all real displacements and widths; sampled values supplement those arguments.'}

# GA17: verify function equations as polynomial coefficient identities.
def integral(poly,weight=0):return sum(c/F(i+weight+1) for i,c in enumerate(poly))
def add_constant(poly,c):return (poly[0]+c,)+poly[1:]
def add_x(poly,c):
    p=list(poly)+[F(0)]*max(0,2-len(poly));p[1]+=c;return tuple(p)
polys=[tuple(map(F,p)) for p in [(0,0,1),(-1,2),(-F(1,3),0,1),(1,-2,3,-4),(0,),(-F(2,3),1)]]
checks=0
for f in polys:
    mean=integral(f)
    for lam in map(F,[-3,0,F(1,2),1,2,3,F(9,10)]):
        if lam!=1:
            m=mean/(1-lam);u=add_constant(f,lam*m)
            assert integral(u)==m and add_constant(u,-lam*integral(u))==f
        elif mean==0:
            for C in map(F,[-2,0,F(1,3),5]):
                u=add_constant(f,C);assert integral(u)==C
                assert add_constant(u,-integral(u))==f
        else:
            assert (1-lam)==0 and mean!=0
        M=integral(f,1)
        if lam!=3:
            m=M/(1-lam/3);u=add_x(f,lam*m)
            assert integral(u,1)==m
            residual=add_x(u,-lam*integral(u,1))
            assert residual[:len(f)]==f and all(c==0 for c in residual[len(f):])
        elif M==0:
            for C in map(F,[-2,0,F(1,3),5]):
                u=add_x(f,C);assert integral(u,1)==C/3
        else:assert M!=0
        checks+=1
for n in range(1,21):
    delta=F(1,n);lam=1-delta
    for epsilon in [F(-1,10),F(0),F(1,100),F(1)]:
        forcing=(-F(1,3)+epsilon,F(0),F(1))
        m=integral(forcing)/delta
        u=add_constant(forcing,lam*m)
        assert u==(-F(1,3)+epsilon/delta,F(0),F(1))
assert F(1,100)/F(1,10)==F(1,10) and F(1,100)/F(1,100)==1
out['GA-17']={'polynomial_forcing_dial_checks':checks,'sensitivity_pairs_checked':80,
 'constant_kernel_critical_parameter':1,'xt_kernel_critical_parameter':3,
 'scope':'Coefficient identities verify the examples. Integrating the original equation proves necessity for every continuous forcing; reconstruction and the forced scalar value prove sufficiency and uniqueness.'}

# Structural audit and selected printed-key regression checks.
d=json.loads((HERE/'ga2-data.json').read_text())
assert d['batch']=='ga2'
assert [f['id'] for f in d['families']]==['GA-09','GA-10','GA-12','GA-13','GA-14','GA-15','GA-16','GA-17']
required=['id','title','core_gate','index_gate','extension_gate','reading','materials','timing','launch','satisfying_stop','prior_use','assessment','mathematical_connection']
page_count=prompt_count=extension_count=0
for f in d['families']:
    assert all(isinstance(f[k],str) and f[k].strip() for k in required)
    assert isinstance(f['prep_minutes'],int) and f['prep_minutes']>=0
    assert f['sources'] and f['figures']
    for s in f['sources']:
        assert all(isinstance(s[k],str) and s[k].strip() for k in ['title','url','locator','adaptation','checked'])
    ids=[]
    for p in f['pages']:
        page_count+=1
        assert all(p[k].strip() for k in ['title','gate','intro'])
        for q in p['prompts']:
            assert all(q[k].strip() for k in ['id','text','solution'])
            assert q['hints'] and all(h.strip() for h in q['hints'])
            ids.append(q['id']);prompt_count+=1
    assert ids==[str(i) for i in range(1,len(ids)+1)]
    for e in f['extensions']:
        extension_count+=1
        assert all(e[k].strip() for k in ['prompt','solution','gate'])
assert (page_count,prompt_count,extension_count)==(25,50,8)
by_id={f['id']:f for f in d['families']}
assert 'separately, a wave evolution with zero initial velocity' in by_id['GA-09']['pages'][2]['prompts'][1]['text']
assert '4/15→8/15→14/15→2/15' in by_id['GA-10']['pages'][0]['prompts'][0]['solution']
assert 'k≡1 modulo 8' in by_id['GA-14']['pages'][1]['prompts'][1]['solution']
assert '(2,1/2,1,3/2)' in by_id['GA-15']['pages'][0]['prompts'][1]['solution']
assert '5−t' in by_id['GA-16']['pages'][0]['prompts'][1]['solution']
assert 'critical' in by_id['GA-17']['pages'][2]['prompts'][1]['solution']
results={'batch':'ga2','status':'passed','data_sha256':hashlib.sha256((HERE/'ga2-data.json').read_bytes()).hexdigest(),
 'coverage':{'families':8,'student_pages':page_count,'keyed_prompts':prompt_count,'solved_extensions':extension_count},'mathematics':out}
(HERE/'ga2-checks-results.json').write_text(json.dumps(results,indent=2)+'\n')
print(f'GA2 checks passed: {page_count} pages, {prompt_count} prompts, {extension_count} extensions; all eight mathematical audits passed.')
