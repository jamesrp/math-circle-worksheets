"""Independent checks of Week 4 represented examples (standard library)."""
from collections import deque
from itertools import combinations
from math import gcd
from pathlib import Path
import json

def meeting(n,a,b,u,v):
    return next((t for t in range(1,n+1) if (a+u*t-b-v*t)%n==0),None)
def hops(n,r,s):
    d={0:0};q=deque([0])
    while q:
        x=q.popleft()
        for h in [r,s]:
            y=(x+h)%n
            if y not in d:d[y]=d[x]+1;q.append(y)
    return d
out={}
# Actual non-task conventions.
assert ((11+2)%12,(6+5)%12)==(1,11)
positions=[0]
for step in [4,4,3,4]:positions.append((positions[-1]+step)%12)
assert positions==[0,4,8,11,3]
assert "BRBB" in {"RBBB"[i:]+"RBBB"[:i] for i in range(4)}
assert meeting(12,0,0,2,5)==4 and (2*4)%12==8
assert next(t for t in range(1,13) if 2*t%12==5*t%12==0)==12
assert meeting(12,0,1,2,5) is None
assert meeting(12,0,3,2,5)==3 and 2*3%12==6
assert hops(12,4,3)[1]==4 and (4+3+3+3)%12==1
assert sorted(hops(12,4,6))==[0,2,4,6,8,10]
assert hops(12,3,4)[1]==4 and hops(12,3,4)[2]==4
assert 1 not in hops(12,4,6) and hops(12,4,6)[2]==3
assert (4+4+3+3)%12==2 and (4+4+6)%12==2
for n in range(3,15):
    for u in range(n):
        for v in range(n):
            for offset in range(n):
                t=meeting(n,0,offset,u,v)
                assert (t is not None)==(offset%gcd(n,u-v)==0)
            assert meeting(n,0,0,u,v)==n//gcd(n,u-v)
            assert len(hops(n,u,v))==n//gcd(n,u,v)
def rotations(s):return {s[i:]+s[:i] for i in range(len(s))}
reps=['BBBRRR','BBRBRR','BBRRBR','BRBRBR']
sets=[rotations(s) for s in reps]
assert [len(s) for s in sets]==[6,6,6,2]
allpatterns={''.join('R' if i in c else 'B' for i in range(6)) for c in combinations(range(6),3)}
assert set.union(*sets)==allpatterns and sum(map(len,sets))==20
assert reps[2][::-1] in sets[1] and reps[2] not in sets[1]
assert len({min(rotations(s)|rotations(s[::-1])) for s in allpatterns})==3
out={'meeting_examples':[4,None,3],'two_hop_examples':{'4_or_3':hops(12,4,3),'4_or_6':hops(12,4,6)},'necklace_reps':reps,'class_sizes':[6,6,6,2],'reflection_classes':3}
Path(__file__).with_name('week04-represented-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('Week 4 meeting, choice-hop, and necklace examples independently verified')
