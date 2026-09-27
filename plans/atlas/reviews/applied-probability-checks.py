"""Independent exact checks for the AP planning volume.
Finite domains are explicit; these checks supplement, not replace, proofs in
applied-probability-review.md. Uses only Python's standard library.
"""
from collections import Counter, deque
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product

passed = []
def record(name):
    passed.append(name)

scores = (0, 1, 3, 4)
differences = [F(sum(p), 2) - F(sum(scores)-sum(p), 2)
               for p in combinations(scores, 2)]
assert differences == [-3, -1, 0, 0, 1, 3]
assert sum(d >= 3 for d in differences) == 1
assert sum(abs(d) >= 3 for d in differences) == 2
record("AP-03: all six randomized assignments")

population = [1]*4 + [5]*4
mean_counts = Counter(F(a+b, 2) for a, b in product(population, repeat=2))
assert mean_counts == {F(1): 16, F(3): 32, F(5): 16}
assert sum(m*n for m,n in mean_counts.items()) / 64 == 3
record("AP-04: all 64 ordered labeled two-draw samples")

for theta in range(-10, 11):
    assert sum(abs(theta-(theta+e)) <= 1 for e in range(-2, 3)) == 3
    assert sum(abs(theta-(theta+e)) <= 2 for e in range(-2, 3)) == 5
record("AP-05: all five errors at 21 integer targets; translation proof remains in report")

words = [w for n in range(4) for w in product((0,1), repeat=n)]
valid_two_state = 0
for transitions in product((0,1), repeat=4):
    for accepting in product((False,True), repeat=2):
        correct = True
        for w in words:
            state = 0
            for symbol in w:
                state = transitions[2*state+symbol]
            if accepting[state] != (sum(w) % 3 == 0):
                correct = False
                break
        valid_two_state += correct
assert valid_two_state == 0
record("AP-08: all 64 two-state complete binary DFAs, strings of length at most three")

assert F(6,2)+F(6,6) == 4
assert F(6,2+6) == F(3,4)
record("AP-10: exact series and parallel extensions")

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]
def madd(a,b):
    return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
def mscale(q,a):
    return [[q*x for x in row] for row in a]
def power(a,n):
    ans = [[F(1),F(0)],[F(0),F(1)]]
    for _ in range(n): ans = matmul(ans,a)
    return ans
def trace(a):
    return a[0][0]+a[1][1]
rho = [[F(1),F(0)],[F(0),F(0)]]
z0 = rho
z1 = [[F(0),F(0)],[F(0),F(1)]]
xp = [[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
xm = [[F(1,2),F(-1,2)],[F(-1,2),F(1,2)]]
def branch(p,r):
    return matmul(matmul(p,r),p)
def dephase(ps,r):
    return madd(branch(ps[0],r),branch(ps[1],r))
assert sum(trace(branch(z1,branch(x,rho))) for x in (xp,xm)) == F(1,2)
assert trace(branch(z1,rho)) == 0
assert dephase((z0,z1),dephase((xp,xm),rho)) == [[F(1,2),0],[0,F(1,2)]]
assert dephase((xp,xm),dephase((z0,z1),rho)) == [[F(1,2),0],[0,F(1,2)]]
record("AP-15: exact projective branches and both unconditional output states")

counts = Counter(sum(s[i] == s[i+1] for i in range(3))
                 for s in product((-1,1),repeat=4))
assert [counts[a] for a in range(4)] == [2,6,6,2]
assert sum(counts[a]*2**a for a in range(4)) == 54
assert F(counts[3]*8,54) == F(8,27)
record("AP-16: all 16 open-chain spin configurations")

def factory(red, blue):
    plans = [(a,b,3*a+4*b) for a in range(red+1) for b in range(blue+1)
             if 2*a+b <= red and a+2*b <= blue]
    return max(p[2] for p in plans), plans
assert factory(5,4)[0] == 10
assert factory(4,4)[0] == 8
r,b = F(2,3),F(5,3)
assert 2*r+b == 3 and r+2*b == 4
assert 5*r+4*b == 10
assert 4*r+4*b == F(28,3)
record("AP-20: all feasible integer plans for both budgets and exact dual certificate")

offers = ((2,5),(1,4),(1,4))
feasible = []
for mask in product((0,1),repeat=3):
    cost = sum(t*offer[0] for t,offer in zip(mask,offers))
    reward = sum(t*offer[1] for t,offer in zip(mask,offers))
    if cost <= 2: feasible.append((mask,reward))
assert sorted(v for _,v in feasible) == [0,4,4,5,8]
vnext = [0,0,0]
tables=[]
for cost,reward in reversed(offers):
    v = [max(vnext[e],reward+vnext[e-cost] if e >= cost else -1)
         for e in range(3)]
    tables.append(v); vnext=v
assert tables == [[0,4,4],[0,4,8],[0,4,8]]
record("AP-21: all eight offer subsets and backward values")

p=q=F(1,3)
assert 2*p == 1-p == 2*q == 1-q == F(2,3)
record("AP-22: exact matching lower/upper payoff certificates")

nash=[]
costs=[]
for n in range(4):
    costs.append(n*n+2*(3-n))
    a_improves = n > 0 and 2 < n
    b_improves = n < 3 and n+1 < 2
    if not a_improves and not b_improves: nash.append(n)
assert costs == [6,5,6,9] and nash == [1,2]
record("AP-23: all four route occupancies and both unilateral deviation types")

assert Counter(sum(w) for w in product((0,1),repeat=2)) == {0:1,1:2,2:1}
record("AP-24: all four ordered offspring outcomes")

initial=(3,4,0)
seen={initial}
queue=deque([initial])
while queue:
    a,b,c=queue.popleft()
    nxt=[]
    if a >= 1 and b >= 2:nxt.append((a-1,b-2,c+1))
    if c >= 1:nxt.append((a+1,b+2,c-1))
    for s in nxt:
        assert s[0]+s[2] == 3 and s[1]+2*s[2] == 4
        if s not in seen:seen.add(s);queue.append(s)
assert seen == {(3,4,0),(2,2,1),(1,0,2)}
record("AP-25: entire reachable reaction-state graph")

identity=[[F(1),F(0)],[F(0),F(1)]]
full=[[F(0),F(1)],[F(-1),F(1)]]
half=[[F(0),F(1)],[F(-1,2),F(1)]]
assert power(full,6) == identity
assert power(half,4) == mscale(F(-1,4),identity)
record("AP-26: exact matrix identities for every real initial pair")

for a,b in product(range(9),repeat=2):
    y0=a+b
    y1=F(a,2)+F(b,4)
    assert 4*y1-y0 == a
    assert 2*y0-4*y1 == b
record("AP-27: inverse formulas on 81 nonnegative integer states; symbolic proof in report")

code=("00000","11100","10011","01111")
def dist(a,b):return sum(x!=y for x,y in zip(a,b))
assert [dist(a,b) for a,b in combinations(code,2)] == [3,3,4,4,3,3]
for received in map("".join,product("01",repeat=5)):
    candidates=[c for c in code if dist(c,received) <= 1]
    assert len(candidates) <= 1
assert [c for c in code if dist(c,"10111") <= 1] == ["10011"]
assert 4*5 > 2**4
record("AP-28: all 32 received five-bit strings and all six codeword distances")

@lru_cache(None)
def leaf_depths(n):
    if n == 1:return ((0,),)
    ans=[]
    for left in range(1,n):
        for a in leaf_depths(left):
            for b in leaf_depths(n-left):
                ans.append(tuple(d+1 for d in a+b))
    return tuple(ans)
costs=[sum(w*d for w,d in zip(weights,depths))
       for depths in leaf_depths(4) for weights in set(permutations((4,2,1,1)))]
assert min(costs) == 14
assert set(tuple(sorted(ds)) for ds in leaf_depths(4)) == {(2,2,2,2),(1,2,3,3)}
record("AP-29: all five ordered full four-leaf tree shapes and all distinct weight assignments")

v=F(3,2)
i=F(6-v,2)
assert i == F(9,4) and i == v+v/2
assert 6*i == 2*i*i+v*v+v*v/2 == F(27,2)
for meter in (F(1,10),F(1),F(2),F(10),F(100)):
    v=6*meter/(3*meter+2)
    assert (6-v)/2 == v+v/meter
record("AP-30: loaded-circuit currents, power, and five positive meter resistances")

print("\n".join(passed))
print(f"{len(passed)} independent exact checks passed.")
