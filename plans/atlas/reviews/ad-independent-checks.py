#!/usr/bin/env python3
"""Independent exact finite checks for AD-01..24; no dependency on card solutions.

Run from any working directory. Prints JSON. Enumeration domains are explicit;
these checks are not proofs of infinite extensions or classroom validation.
"""
from fractions import Fraction as Q
from itertools import combinations, product, permutations
import json

out = {}
def record(key, domain, result):
    out[key] = {"domain": domain, "result": result}

# AD-01: object type bits encode red and round. Enumerate all presence/absence worlds.
worlds = [set(i for i in range(4) if mask >> i & 1) for mask in range(16)]
countermodels = [sorted(w) for w in worlds
    if all(not(i & 1) or i & 2 for i in w)
    and not all(not(i & 2) or i & 1 for i in w)]
assert [2] in countermodels
record('AD-01', 'All 16 presence/absence worlds of four predicate types', countermodels)

# AD-02: diagonal construction, then all 16^4 possible four-row lists.
rows = ['0000','0110','1011','1101']
missing = ''.join(str(1-int(rows[i][i])) for i in range(4))
assert missing == '1000' and missing not in rows
for a in product(range(16), repeat=4):
    b = sum((1-((a[i] >> i) & 1)) << i for i in range(4))
    assert b not in a
record('AD-02', '65536 ordered lists of four 4-bit rows', {'example':missing,'all_diagonal_constructions_missing':True})

# AD-03: exhaustive antichains in B4 and explicit chain partition certificate.
comparable = [(a,b) for a,b in combinations(range(16),2) if a & b in (a,b)]
best = 0
for mask in range(1<<16):
    n = mask.bit_count()
    if n > best and all(not((mask>>a&1) and (mask>>b&1)) for a,b in comparable):
        best = n
chains = [[0,1,3,7,15],[2,6,14],[4,5,13],[8,9,11],[10],[12]]
assert best == 6 and sorted(sum(chains,[])) == list(range(16))
assert all(all(a & b == a for a,b in zip(c,c[1:])) for c in chains)
record('AD-03', 'All 65536 subcollections of the 16 subsets of a 4-set', {'maximum':best,'chain_partition':chains})

# AD-04: encode/decode all 16 messages; independent enumeration of all trees of K4.
def decode(code):
    remaining=set(range(1,5)); code=list(code); es=[]
    while code:
        leaf=min(remaining-set(code)); es.append(tuple(sorted((leaf,code[0]))))
        remaining.remove(leaf); code.pop(0)
    es.append(tuple(sorted(remaining)))
    return tuple(sorted(es))
def connected(es, vertices=range(1,5)):
    seen={next(iter(vertices))}
    while True:
        new=seen|{b for a,b in es if a in seen}|{a for a,b in es if b in seen}
        if new==seen: return seen==set(vertices)
        seen=new
def encode(es):
    es=set(es); result=[]
    while len(es)>1:
        degrees={v:sum(v in e for e in es) for v in range(1,5)}
        leaf=min(v for v,d in degrees.items() if d==1)
        edge=next(e for e in es if leaf in e); result.append(next(v for v in edge if v!=leaf)); es.remove(edge)
    return tuple(result)
codes=list(product(range(1,5),repeat=2))
trees={tuple(sorted(es)) for es in combinations(combinations(range(1,5),2),3) if connected(es)}
assert len(trees)==16 and {decode(c) for c in codes}==trees
assert all(encode(decode(c))==c for c in codes)
record('AD-04','All 16 messages and all 20 three-edge subsets of K4',{'count':len(trees),'code_2_4':decode((2,4))})

# AD-05: restricted spanning trees and a determinant by the permutation formula.
edges=[(1,2),(2,3),(3,4),(1,4),(1,3)]
restricted=[es for es in combinations(edges,3) if connected(es)]
def det(a):
    n=len(a); total=0
    for p in permutations(range(n)):
        term=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        for i in range(n): term*=a[i][p[i]]
        total+=term
    return total
assert len(restricted)==det([[3,-1,-1],[-1,2,-1],[-1,-1,3]])==8
record('AD-05','All 10 three-edge subsets of the stated five-edge graph',{'trees':restricted,'cofactor_determinant':8})

# AD-06: exact meet and join in M3 from the order relation.
def leq(a,b): return a==b or a=='0' or b=='1'
tiles=['0','a','b','c','1']
def meet(a,b): return next(x for x in tiles if leq(x,a) and leq(x,b) and all(not(leq(y,a) and leq(y,b)) or leq(y,x) for y in tiles))
def join(a,b): return next(x for x in tiles if leq(a,x) and leq(b,x) and all(not(leq(a,y) and leq(b,y)) or leq(x,y) for y in tiles))
for a,b in product(tiles,repeat=2): meet(a,b);join(a,b)
lhs=meet('a',join('b','c'));rhs=join(meet('a','b'),meet('a','c'))
assert (lhs,rhs)==('a','0')
record('AD-06','All 25 ordered pairs in M3, plus displayed distributivity witness',{'lhs':lhs,'rhs':rhs})

# AD-07: closure under the three implications; check all orders and all sets.
rules=[({'a'},{'b'}),({'b','c'},{'d'}),({'d'},{'c'})]
def closure(s, order):
    s=set(s)
    while True:
        before=set(s)
        for i in order:
            a,b=rules[i]
            if a<=s:s|=b
        if s==before:return s
sets=[{v for i,v in enumerate('abcd') if n>>i&1} for n in range(16)]
for s in sets: assert all(closure(s,p)==closure(s,(0,1,2)) for p in permutations(range(3)))
closed=[s for s in sets if closure(s,(0,1,2))==s]
assert len(closed)==7 and all(a&b in closed for a,b in product(closed,repeat=2))
record('AD-07','All 16 starts, six repeated rule-sweep orders, and intersections of all seven closed sets',sorted(''.join(sorted(s)) for s in closed))

# AD-08: all set partitions of four residues, without duplicate bag renaming.
def partitions(n, current=()):
    if len(current)==n: yield current;return
    for v in range(max(current,default=-1)+2): yield from partitions(n,current+(v,))
parts=list(partitions(4))
legal=[p for p in parts if all(p[(a+b)%4]==p[(c+d)%4] for a,b,c,d in product(range(4),repeat=4) if p[a]==p[c] and p[b]==p[d])]
assert len(parts)==15 and legal==[(0,0,0,0),(0,1,0,1),(0,1,2,3)]
record('AD-08','All 15 partitions; all 256 representative quadruples per partition',legal)

assert [t for t in range(12) if t%3==2 and t%4==1]==[5]
compatible=sorted({(t%4,t%6) for t in range(12)})
assert len(compatible)==12 and (1,2) not in compatible
record('AD-09','Residues of all 12 times; all 24 four/six residue pairs',{'time':5,'compatible_four_six':compatible})

m,n=1,1;pell=[]
for _ in range(7):
    assert m*(m+1)//2==n*n and (2*m+1)**2-2*(2*n)**2==1
    pell.append([m,n,n*n]);m,n=3*m+4*n+1,2*m+3*n+1
record('AD-10','First seven recurrence outputs; algebraic preservation proved in review prose',pell)

# AD-11: F2[t]/(t²+t+1), binary integers encoding coefficients.
def mul(a,b):
    c=0
    for i in range(2):
        for j in range(2):
            if (a>>i&1) and (b>>j&1):c^=1<<(i+j)
    if c&4:c^=7
    return c
for a,b,c in product(range(4),repeat=3):
    assert mul(mul(a,b),c)==mul(a,mul(b,c))
    assert mul(a,b^c)==mul(a,b)^mul(a,c)
inverses={a:next(b for b in range(4) if mul(a,b)==1) for a in range(1,4)}
assert inverses=={1:1,2:3,3:2}
record('AD-11','All 64 triples for multiplicative associativity/distributivity; all inverses',{'table':[[mul(a,b) for b in range(4)] for a in range(4)],'inverses':inverses})

record('AD-12','Exact rational-root candidate test for x^3-2; general tower argument checked in prose',{'rational_root_candidates':[-2,-1,1,2],'values':[x**3-2 for x in [-2,-1,1,2]]})
survivors=[(i,j) for i,j in product(range(21),repeat=2) if not(i>=2 or (i>=1 and j>=1) or j>=3)]
assert survivors==[(0,0),(0,1),(0,2),(1,0)]
record('AD-13','441 grid positions in [0,20]^2; global bounding argument checked separately',survivors)

def dual(a,b): return (a[0]*b[0],a[0]*b[1]+a[1]*b[0])
assert dual((Q(2),Q(3)),(Q(1,2),Q(-3,4)))==(1,0)
record('AD-14','Exact rational multiplication of the displayed inverse and nilpotent',{'inverse':['1/2','-3/4'],'epsilon_squared':dual((0,1),(0,1))})

samples=[]
for t in [Q(-3,2),Q(-1),Q(0),Q(1,2),Q(2)]:
    x,y=(1-t*t)/(1+t*t),2*t/(1+t*t)
    assert x*x+y*y==1 and y/(x+1)==t
    samples.append([str(t),str(x),str(y)])
record('AD-15','Five exact rational slopes; general inverse identity checked separately',samples)

curves={p:[(x,y) for x,y in product(range(p),repeat=2) if (y*y-x*x*x+x)%p==0] for p in [5,7]}
assert all(len(v)==7 for v in curves.values())
record('AD-16','All 25 pairs over F5 and all 49 pairs over F7',{'affine_points':curves,'discriminants':{'5':64%5,'7':64%7},'projective_points_at_infinity':1})

x,y=Q(0),Q(8);iterations=[]
for i in range(6):
    assert x+y==8 and y-x==Q(8,2**i)
    iterations.append([str(x),str(y)]);x,y=(3*x+y)/4,(x+3*y)/4
record('AD-17','Six exact states of the synchronous update, before/after three steps',iterations)

def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def sub(a,b):return [[x-y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]
def add(a,b):return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]
def scale(k,a):return [[k*x for x in row] for row in a]
def bracket(a,b):return sub(mm(a,b),mm(b,a))
S=[[1,1],[0,1]];V=[[1,0],[1,1]]
assert mm(V,S)==[[1,1],[1,2]] and det(mm(V,S))==1
record('AD-18','Displayed shear, coordinate swap, flattening and shear composition',{'determinants':[det(S),det([[0,1],[1,0]]),det([[1,0],[0,0]])],'composition':mm(V,S)})

T=[[1,1,0],[0,1,1]];B=[[1,0,1],[0,0,-1],[0,1,1]]
assert det(B)==1 and mm(T,B)==[[1,0,0],[0,1,0]]
record('AD-19','Exact rational basis transformation for Q^3→Q^2',{'basis_determinant':det(B),'transformed_matrix':mm(T,B)})

E=[[0,1],[0,0]];F=[[0,0],[1,0]];H=[[1,0],[0,-1]];Z=[[0,0],[0,0]]
assert bracket(E,F)==H and bracket(H,E)==scale(2,E) and bracket(H,F)==scale(-2,F)
assert bracket(bracket(H,E),F)==scale(2,H) and bracket(H,bracket(E,F))==Z
for a,b,c in product([E,F,H],repeat=3):
    assert add(add(bracket(bracket(a,b),c),bracket(bracket(b,c),a)),bracket(bracket(c,a),b))==Z
record('AD-20','All 27 triples of the three basis matrices for Jacobi; general cancellation checked in prose',{'nonassociative_left':scale(2,H),'nonassociative_right':Z})

people={'Ada':'red','Bo':'red','Cy':'blue'};badges={'r':'red','s':'blue','t':'blue','u':'green'}
catalog=[(a,b) for a,b in product(people,badges) if people[a]==badges[b]]
assert len(catalog)==4
record('AD-21','All 12 person/badge pairs; arbitrary-domain universal property proved in prose',catalog)

edge_names=['AB','BC','CD','DA','AC'];cycles=[]
for mask in range(32):
    if all(sum(bool(mask>>i&1) for i,e in enumerate(edge_names) if v in e)%2==0 for v in 'ABCD'):cycles.append(mask)
t1=0b10011;t2=0b11100
assert sorted(cycles)==sorted([0,t1,t2,t1^t2])
classcounts=[]
for boundaries in [[0],[0,t1],[0,t1,t2,t1^t2]]:
    classcounts.append(len({tuple(sorted(c^b for b in boundaries)) for c in cycles}))
assert classcounts==[4,2,1]
record('AD-22','All 32 edge masks and all boundary additions for three face choices',{'cycles':cycles,'class_counts':classcounts})

record('AD-23','Exact finite arithmetic only; module classification and group completion checked in prose',{'difference':[2-1,1-2],'not_actual_module':True})

def rotate(t,k):return t[k:]+t[:k]
def orbit(t,reflect=False):
    return {rotate(s,k) for s in ([t,t[::-1]] if reflect else [t]) for k in range(len(t))}
necklaces={}
for q,n in [(2,4),(3,3)]:
    words=list(product(range(q),repeat=n))
    rc=len({min(orbit(t)) for t in words});dc=len({min(orbit(t,True)) for t in words})
    fixes=[sum(rotate(t,k)==t for t in words) for k in range(n)]
    necklaces[f'{q}_colors_{n}_beads']={'rotations':rc,'dihedral':dc,'rotation_fixed_counts':fixes}
assert necklaces['2_colors_4_beads']=={'rotations':6,'dihedral':6,'rotation_fixed_counts':[16,2,4,2]}
assert necklaces['3_colors_3_beads']['rotations']==11 and necklaces['3_colors_3_beads']['dihedral']==10
record('AD-24','All 16 binary length-four and 27 ternary length-three strings',necklaces)

assert len(out)==24
print(json.dumps(out,indent=2,sort_keys=True))
