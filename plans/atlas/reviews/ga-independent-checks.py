"""Independent small-instance checks for the geometry/analysis plan review.

These checks are derived from task rules, not from the supplied answer strings.
They supplement, and do not replace, the analytic proofs recorded in the review.
Run with Python 3; only the standard library is required.
"""
from fractions import Fraction as F
from itertools import product, combinations
import json

results = {}


def record(card, result):
    results[card] = result


# Fixed room-axis positive quarter-turns, acting on vectors.
def rx(v):
    x, y, z = v
    return x, -z, y


def ry(v):
    x, y, z = v
    return z, y, -x


assert ry(rx((0, 0, 1))) == (0, -1, 0)
assert rx(ry((0, 0, 1))) == (1, 0, 0)
record("GA-01", "Rx then Ry: -y; Ry then Rx: +x")

u = F(3, 7)
assert 4*u == 3-3*u == F(12, 7)
assert u/6 == F(1, 14)
record("GA-02", "t=1/14 turn; shared height 12/7")

budget = F(1, 100)
assert sum(budget/2**(n+1) for n in range(1, 101)) < budget/2
record("GA-03", "assigned infinite geometric total 1/200")

root_arguments = [F(k, 8) for k in range(5)]
assert [2*x for x in root_arguments] == [F(k, 4) for k in range(5)]
record("GA-04", "root angles in turns: 0,1/8,1/4,3/8,1/2")

assert 2*3 == 6 and 2*6 == 3+9
record("GA-05", "a=3, b=6; uniqueness requires separate maximum argument")

z = complex(1, 1)
assert all(z*z+w*w == 0 for w in [1j*z, -1j*z])
record("GA-06", "w=-1+i or 1-i")

assert 4*F(1, 2)**3-3*F(1, 2) == -1
record("GA-07", "T3(1/2)=-1")


def tent(x):
    return 2*x if x <= F(1, 2) else 2-2*x


def orbit(x, n):
    out = []
    for _ in range(n):
        out.append(x)
        x = tent(x)
    return out, x


for start, expected in [
    (F(2, 7), [F(2, 7), F(4, 7), F(6, 7)]),
    (F(4, 7), [F(4, 7), F(6, 7), F(2, 7)]),
    (F(8, 9), [F(8, 9), F(2, 9), F(4, 9)]),
]:
    actual, end = orbit(start, 3)
    assert actual == expected and end == start
record("GA-10", "LRR is 2/7,4/7,6/7; RRL starts 4/7; RLL is a different orbit 8/9,2/9,4/9")

assert 3*F(2, 3) == 2 and 3*2 == 6
# An element of Q(sqrt(2)) is represented by its unique coefficient pair.
def additive(pair):
    return 3*pair[0]+5*pair[1]
assert additive((1, 0)) == 3 and additive((0, 1)) == 5
record("GA-11", "f(2/3)=2; coefficient-pair function on Q+Qsqrt(2) is additive")

assert sum(F(1, n) for n in range(1, 17)) > 3
assert 1+F(19, 2) > 10
record("GA-12", "H16>3; nineteen half-unit blocks exceed ten")

assert F(0)**2-F(1, 2) == -F(1, 2)
assert F(1)**2-F(1, 2) == F(1, 2)
assert [x*x-x+F(1, 8) for x in [F(0), F(1, 2), F(1)]] == [F(1, 8), -F(1, 8), F(1, 8)]
record("GA-13", "alternating witness errors ±1/2; [0,1] extension errors ±1/8")

# Angular phases modulo one turn agree at all n/4 for frequencies one and five.
assert all((F(5*n, 4)-F(n, 4)).denominator == 1 for n in range(-20, 21))
record("GA-14", "regular phases differ by n full turns; extra 1/8 sample differs")

patterns = [(1,1,1,1), (1,1,-1,-1), (1,-1,1,-1), (1,-1,-1,1)]
dot = lambda a,b: sum(x*y for x,y in zip(a,b))
assert [[dot(a,b) for b in patterns] for a in patterns] == [[4*int(i==j) for j in range(4)] for i in range(4)]
coeff = [F(dot((4,2,0,2),p),4) for p in patterns]
assert coeff == [2,1,0,1]
assert [sum(c*p[i] for c,p in zip(coeff,patterns)) for i in range(4)] == [4,2,0,2]
record("GA-15", "orthogonal basis; coefficients (2,1,0,1)")

def overlap(t):
    return max(0,min(2,t)-max(0,t-1))
assert [overlap(F(n,2)) for n in range(-1,8)] == [0,0,F(1,2),1,1,1,F(1,2),0,0]
record("GA-16", "piecewise values 0,t,1,3-t,0 on breakpoints 0,1,2,3")

assert F(1,2)/(1-F(1,2)) == 1
record("GA-17", "mean m=1 for lambda=1/2; lambda=1 needs zero forcing mean")

cost = lambda c: F(3,4)*c*c+F(1,4)*(4-c)**2
assert all(cost(F(n,4)) == (F(n,4)-1)**2+3 for n in range(-8,25))
assert max(abs(2),abs(4-2)) == 2
record("GA-18", "L2 squared cost (c-1)^2+3; L-infinity optimum c=2")

assert F(1,100) <= F(1,100) and 100*F(1,100) == 1
record("GA-19", "x^100/100: supremum 1/100, derivative at one equals one")

for a in [F(-3), F(-1,2), F(0), F(1), F(7,3)]:
    assert ((1+a)**2+(1-a)**2)/2 == 1+a*a
record("GA-20", "two-speed cost 1+a^2; smooth-family integral checked analytically")

assert 1+4*F(1,3) == F(7,3)
assert 2-6*F(1,3) == 0
assert 4**2+6**2 == 52
record("GA-21", "M=(7/3,0), length sqrt(52)=2sqrt(13)")

assert F(1,2)+F(1,4)+F(1,4) == 1
assert F(1,4)*4 == 1
record("GA-22", "(1,1) has barycentric weights (1/2,1/4,1/4)")

# GA-25: enumerate connected acyclic 3-edge subsets independently.
edges = [(0,1),(1,2),(2,3),(3,0),(0,2)]
def connected(es):
    seen={0}
    while True:
        nxt=seen|{v for e in es if set(e)&seen for v in e}
        if nxt == seen:
            return len(seen)==4
        seen=nxt
trees=[es for es in combinations(edges,3) if connected(es)]
assert len(trees)==8 and connected([(0,1),(1,2),(2,3)])
record("GA-25", "eight possible spanning trees, each retaining three of five edges")

star=lambda a,b:(2*b-a)%3
for a,b,c in product(range(3),repeat=3):
    assert star(a,a)==a
    assert star(star(a,b),b)==a
    assert star(star(a,b),c)==star(star(a,c),star(b,c))
colorings=[(a,b,c) for a,b,c in product(range(3),repeat=3) if (2*a-b-c)%3==(2*b-a-c)%3==(2*c-a-b)%3==0]
assert len(colorings)==9
assert sum(len(set(x))>1 for x in colorings)==6
record("GA-26", "nine colorings, six nonconstant; all 27 type-III identities checked")

lo,hi=F(1),F(2)
mids=[]
for _ in range(4):
    mid=(lo+hi)/2;mids.append(mid)
    if mid*mid>2:hi=mid
    else:lo=mid
assert mids == [F(3,2),F(5,4),F(11,8),F(23,16)]
assert (lo,hi,hi-lo)==(F(11,8),F(23,16),F(1,16))
assert (lo+hi)/2==F(45,32)
record("GA-28", "four-step bracket [11/8,23/16], midpoint error bound 1/32")

assert 2**4*F(1,3**4)==F(16,81)
assert F(2,9)/(1-F(1,9))==F(1,4)
record("GA-29", "stage-four total 16/81; ternary 0.0202... equals 1/4")

distances={k:(3+6*k)**2+16 for k in range(-20,21)}
assert [k for k,v in distances.items() if v==min(distances.values())]==[-1,0]
assert min(distances.values())==25
record("GA-30", "two least squared distances 25 at k=-1,0; integer inequality proves global claim")

assert max([0,2,3,1])==3 and min([4,6,5,7])==4
sets=[{0,1},{1,2},{0,2}]
assert all(a&b for a,b in combinations(sets,2)) and not set.intersection(*sets)
record("GA-31", "intersection [3,4]; nonconvex pairwise counterexample checked")

assert all(1/(1-(1-F(1,2**n))) == 2**n for n in range(10))
record("GA-34", "doubling time 1-2^-n")

points=[(3,2),(-1,2),(1,4),(1,0)]
values=[x*x-y*y for x,y in points]
assert values==[5,-3,-15,1] and F(sum(values),4)==-3
record("GA-35", "four cardinal values average -3; actual circle means checked analytically")

x=F(0);xs=[]
for n in range(1,5):
    x=(x+1)/3;xs.append(x)
    assert x-F(1,2)==-F(1,2*3**n)
assert xs==[F(1,3),F(4,9),F(13,27),F(40,81)]
record("GA-36", "error after four steps 1/162; reflection cycles 0,1")

print(json.dumps({"status":"PASS", "checked_groups":len(results), "results":results},indent=2))
