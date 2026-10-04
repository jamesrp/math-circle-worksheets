#!/usr/bin/env python3
"""Independent finite checks for Weeks 29-33; standard library only.
Run: python3 check_math.py. This never changes student files or the guide.
"""
import itertools, math
from collections import defaultdict

def rods(a,b,n):
 return [(x,y) for x in range(n//a+1) for y in range(n//b+1) if a*x+b*y==n]
for a,b,last in [(3,4,5),(3,5,7),(4,5,11),(4,7,17),(5,7,23)]:
 assert not rods(a,b,last)
 assert all(rods(a,b,n) for n in range(last+1,last+a+1))
assert [pair for pair in itertools.combinations(range(2,6),2) if all(rods(*pair,n) for n in range(6,13))]==[(2,3),(2,5),(3,4)]
assert rods(3,4,12)==[(0,3),(4,0)]
assert rods(3,4,15)==[(1,3),(5,0)]
assert rods(3,4,16)==[(0,4),(4,1)]
assert rods(3,4,24)==[(0,6),(4,3),(8,0)]

def weights(ws):
 d=defaultdict(list)
 for signs in itertools.product([-1,0,1],repeat=len(ws)):
  d[sum(x*y for x,y in zip(signs,ws))].append(signs)
 return d
for ws,ans in [((1,2),[1,2,3]),((1,3),[1,2,3,4]),((1,4),[1,3,4,5]),((1,3,8),list(range(1,13))),((1,3,9),list(range(1,14))),((1,3,10),list(range(1,5))+list(range(6,15)))]:
 d=weights(ws);assert sorted(x for x in d if x>0)==ans
assert len(weights((1,3,8))[4])==2
assert len(weights((1,3,9))[4])==1
assert sorted(x for x in weights((1,4,16)) if x>0)==[1,3,4,5,11,12,13,15,16,17,19,20,21]
for m in range(2,6):
 d=weights([3**i for i in range(m)]);s=(3**m-1)//2
 assert sorted(d)==list(range(-s,s+1)) and all(len(v)==1 for v in d.values())

def blockers(a,b):
 # Collinearity plus bounding box, not the gcd criterion being checked.
 return [(x,y) for x in range(a+1) for y in range(b+1)
         if (x,y)!=(0,0) and (x,y)!=(a,b) and x*b==y*a]
for a in range(7):
 for b in range(7):
  if a or b:assert len(blockers(a,b))==math.gcd(a,b)-1
for n,total in [(4,13),(6,25)]:
 assert sum(not blockers(a,b) for a in range(n+1) for b in range(n+1) if a or b)==total
assert [(a,b) for a in range(7) for b in range(7) if (a or b) and len(blockers(a,b))==1]==[(0,2),(2,0),(2,2),(2,4),(2,6),(4,2),(4,6),(6,2),(6,4)]
assert [(a,b) for a in range(7) for b in range(7) if (a or b) and len(blockers(a,b))==2]==[(0,3),(3,0),(3,3),(3,6),(6,3)]

def squares(a,b):
 seq=[]
 while a and b:
  a,b=max(a,b),min(a,b);seq.append(b);a-=b
 return seq
for a in range(1,16):
 for b in range(1,16):
  seq=squares(a,b);assert seq[-1]==math.gcd(a,b) and sum(s*s for s in seq)==a*b
search={(a,b):squares(a,b) for a in range(9,16) for b in range(2,9)}
mx=max(len(set(s)) for s in search.values())
assert mx==5 and [ab for ab,s in search.items() if len(set(s))==mx]==[(13,8)]
assert squares(13,8)==[8,5,3,2,1,1]

def rotations(w):return {w[i:]+w[:i] for i in range(len(w))}
def necklaces(n,colors='AB'):
 d=defaultdict(list)
 for i,letters in enumerate(itertools.product(colors,repeat=n),1):
  w=''.join(letters);d[min(rotations(w))].append(i)
 return dict(d)
assert necklaces(3)=={'AAA':[1],'AAB':[2,3,5],'ABB':[4,6,7],'BBB':[8]}
assert necklaces(5)=={'AAAAA':[1],'AAAAB':[2,3,5,9,17],'AAABB':[4,7,13,18,25],'AABAB':[6,10,11,19,21],'AABBB':[8,15,20,26,29],'ABABB':[12,14,22,23,27],'ABBBB':[16,24,28,30,31],'BBBBB':[32]}
assert sorted(len(v) for v in necklaces(4).values())==[1,1,2,4,4,4]
assert len(necklaces(5,'ABC'))==51
for w,size in [('ABABAB',2),('AABAAB',3),('AAAAAB',6)]:assert len(rotations(w))==size
assert 'AABBAB' not in rotations('AABABB') and 'AABBAB' in rotations('AABABB'[::-1])
print('PASS: rod certificates and exact small combinations; signed-weight ranges and uniqueness; geometric blocker counts; all 49 rectangle-search cases; printed necklace partitions and three-color count.')
