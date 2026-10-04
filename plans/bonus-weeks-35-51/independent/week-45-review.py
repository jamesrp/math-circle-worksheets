"""Independent equal-history conditional counts. No author imports."""
from itertools import product
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json
cards=['RR','RB','BB']; histories=[(c,i,j,c[i]+c[j]) for c in cards for i,j in product(range(2),repeat=2)]
retained={clue:Counter(c for c,i,j,out in histories if out==clue) for clue in ['RR','RB','BR','BB']}
assert retained=={'RR':Counter(RR=4,RB=1),'RB':Counter(RB=1),'BR':Counter(RB=1),'BB':Counter(BB=4,RB=1)}
long_counts={}
for n in range(1,9):
    counts=Counter(c for c in cards for seq in product(range(2),repeat=n) if all(c[i]=='R' for i in seq))
    assert counts==Counter(RR=2**n,RB=1);long_counts[n]=dict(counts)
hosts=[]
for prize,ticket in product([1,2,3],[2,3]):
    empty=[d for d in [2,3] if d!=prize]
    A=ticket if len(empty)==2 else empty[0]
    hosts.append({'prize':prize,'ticket':ticket,'A_opens':A,'A_switch_wins':prize not in [1,A],'B_opens':ticket,'B_empty':ticket!=prize,'B_switch_wins':prize not in [1,ticket]})
assert sum(h['A_switch_wins'] for h in hosts)==4
B=[h for h in hosts if h['B_empty']];assert len(B)==4 and sum(h['B_switch_wins'] for h in B)==2
specific={}
for host in ['A','B']:
    selected=[h for h in hosts if h[host+'_opens']==3 and (host=='A' or h['B_empty'])]
    specific[host]={'count':len(selected),'switch':sum(h[host+'_switch_wins'] for h in selected)}
assert specific=={'A':{'count':3,'switch':2},'B':{'count':2,'switch':1}}
noisy=[(color,t, color if t!='F' else ('B' if color=='R' else 'R')) for identity in ['R1','R2','R3','B'] for color in [identity[0]] for t in ['H1','H2','F']]
report={clue:dict(Counter(c for c,t,out in noisy if out==clue)) for clue in ['R','B']}
assert report=={'R':{'R':6,'B':1},'B':{'R':3,'B':2}}
designs=[]
for tickets in product([True,False],repeat=4):
    counts=Counter(color for identity in ['R1','R2','R3','B'] for color in [identity[0]] for honest in tickets if (color if honest else ('B' if color=='R' else 'R'))=='B')
    if counts['R']==counts['B'] and counts['R']>0:designs.append(tickets)
assert len(designs)==4 and all(sum(t)==3 for t in designs)
assert 'GB'[0]+'GB'[1]=='GB'
assert next(d for d in ['Q','R'] if d!='R')=='Q'
assert next(out for c,t,out in noisy if c=='B' and t=='F')=='R'
result={'same_card_histories':histories,'retained':{k:dict(v) for k,v in retained.items()},'n_red_counts':long_counts,'host_histories':hosts,'specific_door_3':specific,'noisy_report_counts':report,'fair_four_ticket_designs':designs,'worked_examples':['GB + L then R -> GB','choose P/prize R -> informed opens Q','hidden B + F -> report R']}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
