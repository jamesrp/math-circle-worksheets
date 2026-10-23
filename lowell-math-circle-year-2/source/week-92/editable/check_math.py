"""Independent exact checks of the Week 92 kernels and final printed instances.

No graphics/author helper is imported. The piecewise-linear extrema are recomputed
from the definition, and dyadic coverage is checked by all affine breakpoints.
General proofs remain in the facilitator guide; finite tests are not those proofs.
"""
from fractions import Fraction as Q
import json


def T(x):
    return 2*x if x <= 8 else 32-2*x


def image(a,b):
    samples=[T(a),T(b)]
    if a <= 8 <= b:
        samples.append(Q(16))
    return min(samples),max(samples)


def orbit(a,b,n):
    values=[(a,b)]
    for _ in range(n):
        a,b=image(a,b)
        values.append((a,b))
    return values


pairs=[(a,b) for a in range(17) for b in range(a+1,17) if T(a)==T(b)]
assert pairs==[(a,16-a) for a in range(8)]
assert [T(Q(x)) for x in [0,1,2,4]]==[0,2,4,8]
assert image(5,10)==(10,16)
assert [image(*x) for x in [(1,4),(10,15),(6,11),(2,14)]]==[(2,8),(2,12),(10,16),(4,16)]
assert orbit(1,2,4)==[(1,2),(2,4),(4,8),(8,16),(0,16)]
assert orbit(7,9,4)==[(7,9),(14,16),(0,4),(0,8),(0,16)]
assert T(6)==T(10)==12 and image(6,10)==(12,16)
assert T(Q(799,100))==T(Q(801,100))

width_tests=0
for i in range(129):
    for j in range(i,129):
        a,b=Q(i,8),Q(j,8)
        lo,hi=image(a,b)
        assert hi-lo >= b-a
        if b <= 8 or a >= 8:
            assert hi-lo==2*(b-a)
        else:
            assert hi-lo==2*max(8-a,b-8)
        width_tests+=1

for n in [3,4,6]:
    q=Q(2,2**n)
    assert all(b<=2 for a,b in orbit(Q(0),q,n))
    assert orbit(Q(0),q,n)[-1]==(0,2)
    # Any selected strictly larger endpoint breaks the guarantee; the algebraic
    # proof covers all larger endpoints in the guide.
    assert orbit(Q(0),q+Q(1,2**(n+4)),n)[-1][1]>2

dyadic_tests=0
for n in range(1,10):
    for k in range(2**n):
        a,b=Q(16*k,2**n),Q(16*(k+1),2**n)
        assert orbit(a,b,n)[-1]==(0,16)
        dyadic_tests+=1

assert T(Q(32,3))==Q(32,3)
assert all(orbit(Q(k),Q(k),5)[-1]==(0,0) for k in range(17))

print(json.dumps({
    'status':'pass','whole_number_merging_pairs':pairs,
    'interval_width_cases':width_tests,'dyadic_cells':dyadic_tests,
    'precision_endpoints':{'3':'1/4','4':'1/8','6':'1/32'},
    'limitations':'Finite checks support printed examples; general interval statements require the supplied proofs. Physical rehearsal and classroom use untested.'
},indent=2))
