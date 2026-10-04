#!/usr/bin/env python3
from collections import Counter
from itertools import product
from fractions import Fraction
from math import comb,factorial
import json

def histories(colors,n,rule='same'):
 out=[]
 def walk(bag,story,draws,step):
  if step==n:out.append((tuple(story),tuple(draws),tuple(bag)));return
  for name,color in bag:
   new=list(bag)
   if rule!='none':
    c=color if rule=='same' else ('B' if color=='R' else 'R')
    new.append((c+str(step+1),c))
   walk(new,story+[name],draws+[color],step+1)
 walk([(c+'0',c) for c in colors],[],[],0)
 return out
counts={}
for rule in ['same','other','none']:
 h=histories('RB',2,rule);totals=Counter(d.count('R') for s,d,b in h)
 counts[rule]={'history_count':len(h),'red_draw_counts':dict(sorted(totals.items())),'one_each_chance':str(Fraction(totals[1],len(h)))}
assert counts['same']['red_draw_counts']=={0:2,1:2,2:2}
assert counts['other']['red_draw_counts']=={0:1,1:4,2:1}
assert counts['none']['red_draw_counts']=={0:1,1:2,2:1}
forecast={}
for w in map(''.join,product('RB',repeat=4)):
 p=Fraction(1+w.count('R'),6);forecast.setdefault(str(p),[]).append(w)
assert set(forecast)=={'1/6','1/3','1/2','2/3','5/6'}
checks={}
for n in [2,3,4,5]:
 h=histories('RBG',n)
 composition=Counter(tuple(d.count(c) for c in 'RBG') for s,d,b in h)
 assert len(h)==factorial(n+2)//2
 assert len(composition)==comb(n+2,2)
 assert set(composition.values())=={factorial(n)}
 checks[n]={'histories':len(h),'added_count_vectors':len(composition),'histories_per_vector':factorial(n)}
three=histories('RBG',2)
assert [(s[0],s[1]) for s,d,b in three]==[(a,b) for a in ['R0','B0','G0'] for b in ['R0','B0','G0',a[0]+'1']]
assert all(all(sum(c==t for name,c in bag)>=1 for t in 'RBG') for s,d,bag in three)
print(json.dumps({'two_color_rule_comparison':counts,'forecast_examples':{p:w[:2] for p,w in forecast.items()},'three_color_checks':checks,'two_draw_added_vectors':{str(k):v for k,v in Counter(tuple(d.count(c) for c in 'RBG') for s,d,b in three).items()}},indent=2))
