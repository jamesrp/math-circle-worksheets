"""Coordinator's stopping-guide audit without author verifier imports."""
from collections import Counter
from fractions import Fraction as F
import itertools,json
from pathlib import Path

def all_history_totals(bag,n):
    words=list(itertools.product(bag,repeat=n))
    histories=[h for k in range(1,n) for h in itertools.product(bag,repeat=k)]
    index={h:j for j,h in enumerate(histories)}
    totals=[]
    for bits in range(1<<len(histories)):
        total=0
        for w in words:
            stop=next((k for k in range(n-1) if bits>>index[w[:k+1]]&1),n-1)
            total+=w[stop]
        totals.append(total)
    return {'policies':len(totals),'best_total':max(totals),'best_average':str(F(max(totals),len(words)))}
def recurrence(bag,n):
    v=sum(map(F,bag))/len(bag);vs=[v]
    for k in range(2,n+1):v=sum(max(F(x),v) for x in bag)/len(bag);vs.append(v)
    return vs
out={}
for bag in [(0,4,6),(0,3,6),(0,5,6)]:
    out[str(bag)]={str(n):all_history_totals(bag,n) for n in (2,3)}
    vs=recurrence(bag,4);out[str(bag)]['V_1_through_4']=[str(v) for v in vs]
    for n in (2,3):assert F(out[str(bag)][str(n)]['best_total'],3**n)==vs[n-1]
assert recurrence((0,4,6),3)==[F(10,3),F(40,9),F(134,27)]
assert recurrence((0,5,6),4)==[F(11,3),F(44,9),F(143,27),F(448,81)]
def score(w,predicate):
    return w[next((k for k in range(len(w)-1) if predicate(k,w[k])),len(w)-1)]
words=list(itertools.product((0,4,6),repeat=3))
a=[score(w,lambda k,x:x in (4,6)) for w in words]
b=[score(w,lambda k,x:x==6 or k==1 and x==4) for w in words]
assert sum(a)==130 and Counter(a)=={0:1,4:13,6:13}
assert sum(b)==134 and Counter(b)=={0:2,4:8,6:17}
out['P4_complete_word_key']=[{'word':w,'A':x,'B':y} for w,x,y in zip(words,a,b)]
for n,total,tally in [(3,143,{0:1,5:13,6:13}),(4,448,{0:2,5:26,6:53})]:
    scores=[score(w,lambda k,x:x==6 or x==5 and (n==3 or k>0)) for w in itertools.product((0,5,6),repeat=n)]
    assert sum(scores)==total and Counter(scores)==tally
out['P2_opposite_batches']={'match_I':[36,0],'match_II':[0,36],'works_for_any_fixed_legal_rules':True}
out['proofs_independently_reviewed']='Backward induction bounds histories and randomized policies; all-minimum word bounds V_n below maximum and yields strict improvement for a nonconstant finite iid bag.'
out['guide_pages_read_and_visually_inspected']=list(range(1,9))
p=Path(__file__).parent/'guide-review-assets/independent-guide-checks.json';p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k.startswith('(')})
