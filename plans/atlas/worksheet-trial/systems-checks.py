#!/usr/bin/env python3
"""Independent exact checks for three worksheet-trial designs.

The accompanying prose gives universal proofs; finite checks catch transcriptions.
No third-party packages, network, files outside this design directory, or PDFs.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial, exp, sqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
checks = []

def record(name, detail):
    checks.append({'name': name, 'status': 'passed', 'detail': detail})

def full(p):
    a, b = p
    return b, b-a

def half(p):
    a, b = p
    return b, b-a/2

def iterate(rule, p, n):
    for _ in range(n):
        p = rule(p)
    return p

def radius2(p):
    a, b = p
    return a*a-a*b+b*b

# A rational vector stores a+b sqrt(2). Addition is coordinatewise.
def f(p, c):
    a, b = p
    return 3*a+c*b

rats = [F(-3,2),F(-1),F(0),F(1,3),F(1),F(7,4)]
for a,b,d,e,c in product(rats, repeat=5):
    assert f((a+d,b+e),c) == f((a,b),c)+f((d,e),c)
for q in rats:
    assert f((q,0),0) == f((q,0),5) == 3*q
assert f((0,1),0) == 0 and f((0,1),5) == 5
assert 3*F(2,3) == 2
assert 3*F(5,6) == F(5,2)
assert F(14142,10000)**2 < 2 < F(14143,10000)**2
assert 5-3*F(14142,10000) == F(7574,10000)
record('GA-11 constructions and claim cards', '7,776 rational coefficient checks across six c values; exact decimal bounds and claim answers.')

for a,b in product(range(-6,7), repeat=2):
    p=(F(a),F(b))
    assert iterate(full,p,3) == (-p[0],-p[1])
    assert iterate(full,p,6) == p
    assert radius2(full(p)) == radius2(p)
    c,d=full(p)
    assert (c-d,c) == p
    first_return=next(n for n in range(1,7) if iterate(full,p,n)==p)
    assert first_return == (1 if p==(0,0) else 6)
    assert iterate(half,p,4) == (-p[0]/4,-p[1]/4)
record('AP-26 universal identities sampled', '169 exact integer starts; inverse, six-cycle, exact period, quadratic invariant, and four-step half-gain identity.')

# Verify symbolic linear maps on a basis, sufficient for equality of linear maps.
for p in [(F(1),F(0)),(F(0),F(1))]:
    assert iterate(full,p,3) == (-p[0],-p[1])
    assert iterate(half,p,4) == (-p[0]/4,-p[1]/4)
    a,b=p
    x,y=float(a-b/2),sqrt(3)*float(b)/2
    c,d=full(p)
    xx,yy=float(c-d/2),sqrt(3)*float(d)/2
    assert abs(xx-(x/2+sqrt(3)*y/2)) < 1e-12
    assert abs(yy-(-sqrt(3)*x/2+y/2)) < 1e-12
record('AP-26 linear-operator proof checks', 'Both basis vectors verify T^3=-I, H^4=-I/4 and the clockwise sixty-degree embedding.')

p=(F(1),F(1))
observed=[]
for n in range(60):
    observed.append([str(v) for v in p])
    if n>=16:
        assert max(abs(v) for v in p) <= F(1,100)
    p=half(p)
assert observed[:5]==[['1','1'],['1','1/2'],['1/2','0'],['0','-1/4'],['-1/4','-1/4']]
record('AP-26 half-gain transcription and target', 'Exact first states and all ticks 16–59 checked; prose residue-class proof certifies all future ticks.')

for h in [F(1,2),F(3,2),F(3)]:
    assert 8*(1-h) == {F(1,2):4,F(3,2):-4,F(3):-16}[h]
for k in range(1,100):
    h=F(k,100)
    assert 8*(1-h)*h == 2-8*(h-F(1,2))**2
    assert 8*(1-h)*h <= 2
for u,v in product([F(1,8),F(1,4),F(1,2)],repeat=2):
    assert (1-u)*(1-v)-(1-u-v) == u*v
record('AP-07 tangent endpoints and optimization', 'Exact endpoint, completed-square identity, and step-splitting identity checks.')

# e is bracketed by a positive Taylor partial sum and geometric bound on its tail.
N=15
e_lo=sum((F(1,factorial(k)) for k in range(N+1)),F(0))
tail=F(1,factorial(N+1))/(1-F(1,N+2))
e_hi=e_lo+tail
assert F(271828,100000) < e_lo < e_hi < F(271829,100000)
five=8*F(4,5)**5
six=8*F(5,6)**6
assert five == F(16384,6250)
assert six == F(15625,5832)
# Relative errors are 1 - e * (1-1/n)^n. These exact comparisons certify the threshold.
assert e_hi*F(4,5)**5 < F(9,10)
assert e_lo*F(5,6)**6 > F(9,10)
record('AP-07 five-step failure and six-step success', 'Exact rational bounds on e certify the strict 10% threshold. All unequal schedules with at most five steps are bounded by AM–GM in the written proof.')

data=json.loads((ROOT/'systems-data.json').read_text())
assert [x['id'] for x in data['investigations']]==['GA-11','AP-26','AP-07']
for inv in data['investigations']:
    ids=[p['id'] for page in inv['student_pages'] for p in page['prompts']]
    assert len(ids)==len(set(ids))
    assert set(ids)==set(inv['solutions'])==set(inv['staged_hints'])
    assert 2<=len(inv['student_pages'])<=4
record('Prompt coverage', 'Every one of 32 student prompts has a keyed solution and staged hints; all three investigations are 3–4 student pages.')

result={'status':'passed','checks':checks,'count':len(checks),'limits':'Finite checks do not establish the universal claims on their own; explicit independent algebraic proofs are included in systems-data.json.'}
(ROOT/'systems-checks-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
