#!/usr/bin/env python3
"""Independent outline-level computations; final packet checks remain separate."""
from itertools import product, permutations, combinations
from collections import Counter, deque
from functools import lru_cache
from fractions import Fraction
import json
from pathlib import Path
R={}
# affine geometry and first-player mirroring
pts=list(product(range(3),repeat=2))
third=lambda a,b:tuple((-a[i]-b[i])%3 for i in range(2))
lines={frozenset((a,b,third(a,b))) for a,b in combinations(pts,2)}
assert len(lines)==12
caps=[s for s in combinations(pts,4) if not any(l<=set(s) for l in lines)]
assert len(caps)==54 and not any(not any(l<=set(s) for l in lines) for s in combinations(pts,5))
@lru_cache(None)
def avoid(a,b,turn):
 owned=[set(a),set(b)]
 wins=False
 for p in pts:
  if p in owned[0]|owned[1]: continue
  new=owned[turn]|{p}
  if any(l<=new for l in lines):continue
  sets=[tuple(sorted(owned[0])),tuple(sorted(owned[1]))];sets[turn]=tuple(sorted(new))
  if not avoid(*sets,1-turn): wins=True
 return wins
assert avoid((),(),0) is True
cap27=[(x,y,(x*x+y*y)%3) for x,y in pts]
assert not any(all(sum(p[i] for p in tri)%3==0 for i in range(3)) for tri in combinations(cap27,3))
R['36']={'lines':12,'four_caps':54,'avoid_game_first_can_force_win':True,'verified_27_card_nine_cap':cap27}
# proper tetrahedral symmetries: permutations parity
parity=lambda p:sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2
perms=list(permutations(range(4))); rot=[p for p in perms if parity(p)==0]
edges=list(combinations(range(4),2))
def move(S,p):return frozenset(tuple(sorted((p[a],p[b]))) for a,b in S)
patterns={}
for name,S in [('path',[(0,1),(1,2),(2,3)]),('star',[(0,1),(0,2),(0,3)]),('triangle',[(0,1),(0,2),(1,2)])]:
 stabilizers=[p for p in perms if move(S,p)==frozenset(S)]
 patterns[name]={'stabilizer_size':len(stabilizers),'has_odd_stabilizer':any(parity(p) for p in stabilizers)}
assert patterns['path']=={'stabilizer_size':2,'has_odd_stabilizer':False}
R['37']=patterns
# braid color transfer and closure components
colors=range(3)
def crossing(a,b):return b,(2*b-a)%3
counts={}
for n in [1,2,3,4,6]:
 count=0
 for a,b in product(colors,repeat=2):
  state=(a,b)
  for _ in range(n):state=crossing(*state)
  count+=state==(a,b)
 counts[str(n)]={'colorings':count,'components':1 if n%2 else 2}
assert [counts[str(n)]['colorings'] for n in [1,2,3,4,6]]==[3,3,9,3,9]
R['40']=counts
# torus Hamiltonian tours, rooted and directed
neigh=lambda p:[((p[0]+dx)%3,(p[1]+dy)%3,dx,dy) for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]]
windings=Counter()
def tours(p,visited,dx,dy):
 if len(visited)==9:
  for x,y,u,v in neigh(p):
   if (x,y)==(0,0):windings[((dx+u)//3,(dy+v)//3)]+=1
  return
 for x,y,u,v in neigh(p):
  if (x,y) not in visited:tours((x,y),visited|{(x,y)},dx+u,dy+v)
tours((0,0),{(0,0)},0,0)
assert (0,0) not in windings
R['41']={'directed_rooted_nine_step_tours':sum(windings.values()),'winding_counts':{str(k):v for k,v in sorted(windings.items())}}
# reinforcement independent rational law
laws={}
for rule in ['copy','opposite','constant']:
 states={(1,1,0):Fraction(1)}
 for i in range(2):
  new=Counter()
  for (r,b,nr),pr in states.items():
   for red,cnt in [(1,r),(0,b)]:
    dr=int(rule=='copy' and red or rule=='opposite' and not red)
    db=int(rule=='copy' and not red or rule=='opposite' and red)
    new[(r+dr,b+db,nr+red)]+=pr*Fraction(cnt,r+b)
  states=new
 laws[rule]={str(k):str(sum(pr for (r,b,nr),pr in states.items() if nr==k)) for k in range(3)}
assert laws['opposite']=={'0':'1/6','1':'2/3','2':'1/6'}
R['44']=laws
# repeated same card: ordered face histories 3*4=12
hist=Counter()
for card in ['RR','RB','BB']:
 for sides in product(range(2),repeat=2):hist[(''.join(card[i] for i in sides),card)]+=1
assert hist[('RR','RR')]==4 and hist[('RR','RB')]==1
R['45']={'two_red_same_card_RR': '4/5','history_counts':{str(k):v for k,v in hist.items()}}
# cover and rotating resets
R['46']={'coverage_by_n':{str(n):sum(len(set(h))==3 for h in product(range(3),repeat=n)) for n in [3,4,5]}}
assert R['46']['coverage_by_n']=={'3':6,'4':36,'5':150}
starts=tuple(product(range(2),repeat=3))
def action(s,a):return (0,)+s[1:] if a=='Z' else s[-1:]+s[:-1]
q=deque([(starts,'')]);seen={starts};answer=None
while q:
 states,word=q.popleft()
 if len(set(states))==1:answer=word;break
 for a in ['Z','T']:
  after=tuple(action(s,a) for s in states)
  if after not in seen:seen.add(after);q.append((after,word+a))
assert len(answer)==5
R['46']['shortest_reset_rotate_word']=answer
# binary Ducci
D=lambda s:tuple(abs(s[(i+1)%len(s)]-s[i]) for i in range(len(s)))
for s in product(range(2),repeat=8):
 t=s
 for _ in range(8):t=D(t)
 assert t==(0,)*8
six=(1,0,0)*2;t=six;trail=[]
while t not in trail:trail.append(t);t=D(t)
assert any(t)
R['49']={'binary_eight_all_erased_by_round_8':True,'six_cycle':trail[trail.index(t):]}
Path('plans/bonus-weeks-35-51/coordinator-kernel-checks.json').write_text(json.dumps(R,indent=2))
print('Outline-level checks passed for finite geometry, chirality, braids, torus tours, urns, conditioning, reset machines and binary rings.')
