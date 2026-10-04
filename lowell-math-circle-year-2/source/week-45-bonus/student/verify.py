#!/usr/bin/env python3
from itertools import product
from collections import Counter
from fractions import Fraction
import json
cards={'RR':('R','R'),'RB':('R','B'),'BB':('B','B')}
clues=[]
for name,faces in cards.items():
 for first,second in product(range(2),repeat=2):clues.append((name,first,second,faces[first]+faces[second]))
rr=Counter(name for name,a,b,w in clues if w=='RR');rb=Counter(name for name,a,b,w in clues if w=='RB')
assert rr=={'RR':4,'RB':1};assert rb=={'RB':1};assert len(clues)==12
assert ('G','B')[0]+('G','B')[1]=='GB'

def door(prize,ticket,kind):
 if kind=='informed':
  empty=[d for d in [2,3] if d!=prize];opened=ticket if len(empty)==2 else empty[0]
 else:opened=ticket
 if opened==prize:return (opened,'discard')
 switched=next(d for d in [2,3] if d!=opened)
 return (opened,'switch' if switched==prize else 'stay')
results={}
for kind in ['informed','blind']:
 rows=[(prize,ticket,*door(prize,ticket,kind)) for prize,ticket in product([1,2,3],[2,3])]
 wins=Counter(r[3] for r in rows)
 results[kind]={'rows':rows,'wins':dict(wins)}
assert results['informed']['wins']=={'stay':2,'switch':4}
assert results['blind']['wins']=={'stay':2,'switch':2,'discard':2}
# The worked letters P,Q,R instance maps to prize 3, choice 1 and Host A opens 2.
assert door(3,2,'informed')==(2,'switch')
reports=[]
for counter,t in product(['R1','R2','R3','B'],['H1','H2','F']):
 truth=counter[0];report=truth if t!='F' else ('B' if truth=='R' else 'R');reports.append((counter,t,truth,report))
blue=Counter(truth for counter,t,truth,report in reports if report=='B')
red=Counter(truth for counter,t,truth,report in reports if report=='R')
assert blue=={'R':3,'B':2} and red=={'R':6,'B':1}
design={}
for honest in range(5):
 flip=4-honest;ways={'R':3*flip,'B':honest}
 if ways['R']==ways['B'] and ways['R']>0:design[honest]=ways
assert design=={3:{'R':3,'B':3}}
assert next(r[3] for r in reports if r[:2]==('B','F'))=='R'
print(json.dumps({'same_card_histories':clues,'red_red_card_counts':rr,'red_blue_card_counts':rb,'door_games':results,'blue_report_true_counts':blue,'red_report_true_counts':red,'fair_blue_four_ticket_design':design},indent=2))

# Information leaks alter the conditioned sample space; secrecy is essential.
assert Counter(name for name,a,b,w in clues if w=='RR' and a==0 and b==0)=={'RR':1,'RB':1}
assert [p for p,t,o,r in results['informed']['rows'] if o==3 and t==2]==[2]
assert [p for p,t,o,r in results['informed']['rows'] if o==3 and t==3]==[1,2]
assert {truth for c,t,truth,r in reports if r=='B' and t=='F'}=={'R'}
assert {truth for c,t,truth,r in reports if r=='B' and t.startswith('H')}=={'B'}
