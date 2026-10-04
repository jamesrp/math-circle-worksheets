from itertools import product
from collections import Counter
from pathlib import Path
import json
def ternary(w):
    if len(set(w))==1:return None
    lone='R' if w.count('R')==1 else 'B'
    return 'SCT'[w.index(lone)]
def basic(w):
    ans=[]
    for i in [0,2]:
        pair=w[i:i+2]
        if pair=='BR':ans.append('S')
        elif pair=='RB':ans.append('C')
    return ans
def recycled(w):
    ans=basic(w)
    if not ans and w in ['RRBB','BBRR']:ans=['C' if w=='RRBB' else 'S']
    return ans
bags={}
for r,b in [(1,1),(2,1),(3,1),(1,3)]:
    bag=['R']*r+['B']*b
    three=Counter(ternary(''.join(q)) for q in product(bag,repeat=3))
    four=[ ''.join(q) for q in product(bag,repeat=4)]
    base=Counter(s for w in four for s in basic(w));rec=Counter(s for w in four for s in recycled(w))
    assert three['S']==three['C']==three['T'] and base['S']==base['C'] and rec['S']==rec['C']
    bags[f'{r}R{b}B']={'three_identity_count':len(bag)**3,'three_outputs':{str(k):v for k,v in three.items()},'four_identity_count':len(four),'basic_total':sum(base.values()),'recycled_total':sum(rec.values()),'basic_shape_counts':dict(base),'recycled_shape_counts':dict(rec)}
ticket_types=['SS','SC','CS','CC']
supports=Counter()
for tickets in product(ticket_types,repeat=4):
    if all(sum(t[pos]=='S' for t in tickets)==2 for pos in [0,1]):supports[len(set(tickets))]+=1
result={'bag_checks':bags,'unweighted_six_word_class_counts':dict(Counter((w.count('R'),ternary(w)) for w in map(''.join,product('RB',repeat=3)) if ternary(w))), 'balanced_basic_count_histogram':dict(Counter(len(basic(w)) for w in map(''.join,product('RB',repeat=4)))), 'balanced_recycle_count_histogram':dict(Counter(len(recycled(w)) for w in map(''.join,product('RB',repeat=4)))),'fair_marginal_ticket_ordered_assignments_by_support_size':dict(supports)}
# JSON stringify tuple-key class table explicitly.
result['unweighted_six_word_class_counts']={str(k):v for k,v in result['unweighted_six_word_class_counts'].items()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
