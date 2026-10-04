#!/usr/bin/env python3
"""Independent finite enumerations supporting this adult guide; no random simulation."""
from pathlib import Path
from itertools import product, permutations, combinations
from collections import Counter
from math import factorial
from fractions import Fraction
import json,hashlib
H=Path(__file__).resolve().parent
week=json.loads((H/'guide.json').read_text())['week']
report={'week':week,'method':'Exhaustive exact enumeration; separate from student checker','checks':{}}
C=report['checks']
if week==42:
 w=Counter(a+b for a,b in product('RRRB',repeat=2));assert w=={'RR':9,'RB':3,'BR':3,'BB':1};C['color_weights']=dict(w)
 fair=[]
 for rule in product(range(3),repeat=4):
  weights=[sum(w[c] for c,r in zip(['RR','RB','BR','BB'],rule) if r==k) for k in range(3)]
  if weights[1]==weights[2]>0:fair.append((rule,weights))
 assert len(fair)==2 and all(v[0]==10 for r,v in fair);C['all_fair_rules_0_skip_1_square_2_circle']=fair
 rates=[]
 for r in range(5):rates.append(sum(a!=b for a,b in product('R'*r+'B'*(4-r),repeat=2)))
 assert rates==[0,6,8,6,0];C['mixed_pair_counts_by_red_count']=rates
 for a,b,rb,br in [('RRRB','RBBB',9,1),('RRRB','RRRRRRBB',6,6),('RRBB','RB',2,2)]:
  v=Counter(x+y for x,y in product(a,b));assert v['RB']==rb and v['BR']==br;C[a+' then '+b]=dict(v)
 v=Counter('RRRB'[a]+'RRRB'[b] for a,b in permutations(range(4),2));assert v=={'RR':6,'RB':3,'BR':3};C['without_replacement']=dict(v)
elif week==43:
 def shuffle(start,s):
  a=list(start)
  for i,j in enumerate(s):a[i],a[j-1]=a[j-1],a[i]
  return ''.join(a)
 for start in ('ABC','BAC','CBA'):
  v={str(s):shuffle(start,s) for s in product((1,2,3),(2,3))};assert len(set(v.values()))==6;C['six_story_map_from_'+start]=v
 v=Counter(shuffle('ABC',s) for s in product((1,2,3),repeat=3));assert v=={'ABC':4,'ACB':5,'BAC':5,'BCA':5,'CAB':4,'CBA':4};C['wrong_range_counts']=dict(v)
 assert {shuffle('ABC',(i,3)) for i in (2,3)}=={'BCA','CAB'}
 for n in (4,5):
  start='ABCDE'[:n];v=Counter(shuffle(start,s) for s in product(*(range(i,n+1) for i in range(1,n))))
  assert len(v)==factorial(n) and set(v.values())=={1};C[f'{n}_card_histories']=len(v)
elif week==44:
 for n in range(1,6):
  states=[(('R1','B1'),())]
  for k in range(n):states=[(bag+(picked[0]+str(k+2),),h+(picked,)) for bag,h in states for picked in bag]
  v=Counter(sum(p[0]=='R' for p in h) for bag,h in states);assert v=={r:factorial(n) for r in range(n+1)};C[f'n_{n}_identity_totals']=dict(v)
  words=Counter(''.join(p[0] for p in h) for bag,h in states)
  for word,count in words.items():
   r=word.count('R');assert Fraction(count,len(states))==Fraction(factorial(r)*factorial(n-r),factorial(n+1))
  C[f'n_{n}_color_words']=dict(sorted(words.items()))
 assert {s for s in product('RB',repeat=4) if s.count('R')==2}==set(map(tuple,['RRBB','RBRB','RBBR','BRRB','BRBR','BBRR']))
elif week==45:
 show={1:'R',2:'R',3:'R',4:'B',5:'B',6:'B'};hidden={1:'R',2:'R',3:'B',4:'R',5:'B',6:'B'}
 def weights(s,clue='R'):return Counter(hidden[t] for t in s if show[t]==clue)
 def fair(s,clue='R'):
  v=weights(s,clue);return v['R']==v['B']>0
 all_t=set(range(1,7));assert weights(all_t)=={'R':2,'B':1};assert weights(all_t,'B')=={'R':1,'B':2}
 v=[s for n in range(7) for s in combinations(range(1,7),n) if fair(s)]
 assert len(v)==16 and all(3 in s and len(set(s)&{1,2})==1 for s in v);C['all_fair_subsets']=v
 v=[s for s in combinations(range(1,7),3) if weights(s)['B']>0 and weights(s)['R']==0]
 assert v==[(3,4,5),(3,4,6),(3,5,6)];C['three_ticket_red_hides_blue']=v
 for clue,expected in [('R',{1,2}),('B',{5,6})]:assert {t for t in all_t if fair(all_t-{t},clue)}==expected
 for t in (2,4,5,6):
  C['add_'+str(t)]={'red_clue':dict(weights({1,3,t})),'unconditional':dict(Counter(hidden[i] for i in {1,3,t}))}
 cards=[{1,2},{3,4},{5,6}]
 for n in range(1,4):
  for cs in combinations(cards,n):assert not fair(set.union(*cs))
 C['whole_card_fair_selections']=0
elif week==46:
 boards=list(product('RB',repeat=3))
 def run(b,s):
  b=list(b)
  for i,c in s:b[i]=('B' if b[i]=='R' else 'R') if c=='T' else c
  return tuple(b)
 ops=list(product(range(3),'RB'));count=0
 for n in range(5):
  for s in product(ops,repeat=n):
   u=3-len({i for i,c in s});assert len({run(b,s) for b in boards})==2**u;count+=1
 C['overwrite_stories_checked_at_all_8_starts']=count
 ops=list(product(range(3),'RBT'));count=0
 for n in range(4):
  for s in product(ops,repeat=n):
   assert (len({run(b,s) for b in boards})==1)==(len({i for i,c in s if c!='T'})==3);count+=1
 C['mixed_stories_checked_at_all_8_starts']=count
 for b in boards:
  v=Counter(run(b,list(zip([0,2,0,1],cs))) for cs in product('RB',repeat=4));assert len(v)==8 and set(v.values())=={2}
 C['all_starts_fixed_1312_story']='Each of 8 outputs has 2 of 16 color histories'
 stories=[[(0,'R'),(0,'B'),(2,'R')],[(1,'R'),(2,'B'),(0,'R')],[(1,'B'),(1,'R'),(1,'B')]]
 v=[sorted(''.join(x) for x in {run(b,s) for b in boards}) for s in stories]
 assert v==[['BBR','BRR'],['RRB'],['BBB','BBR','RBB','RBR']];C['printed_story_outputs']=v
 for a,b in product(boards,repeat=2):
  d=sum(x!=y for x,y in zip(a,b))
  possible=[n for n in range(4) if any(run(a,s)==run(b,s) for s in product(list(product(range(3),'RB')),repeat=n))]
  assert min(possible)==d
 C['all_64_pair_minima']='Equal Hamming distance'
report['student_sha256']={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in H.parent.glob('*.pdf') if f.name!='facilitator-guide.pdf'}
(H/'checks.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print('PASS week',week,json.dumps(C,ensure_ascii=False))
