"""Independent exact checks of early probability cards and survey examples.

The checks establish only the enumerated instances. General arguments remain in
the cards and review reports; no simulation is promoted to a proof.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from collections import Counter
from pathlib import Path
import json

def connected(edges,n):
    seen={0}
    while True:
        more=seen|{v for u,v in edges if u in seen}|{u for u,v in edges if v in seen}
        if more==seen: return len(seen)==n
        seen=more

def main():
    results={}
    # AP-01: exact harmonic boundary solution for five track vertices.
    p=[Q(i,4) for i in range(5)]
    assert all(2*p[i]==p[i-1]+p[i+1] for i in range(1,4))
    results['AP-01']={'domain':'track 0..4, fair independent steps','p':list(map(str,p)),
                      'note':'Almost-sure absorption and uniqueness are separately proved in the card.'}
    # AP-02: distinguish a sampled-red event from contains-red reporting.
    cases=[('A','r'),('A','r'),('A','b'),('B','r'),('B','b'),('B','b')]
    red=[x for x in cases if x[1]=='r']
    assert Q(sum(x[0]=='A' for x in red),len(red))==Q(2,3)
    results['AP-02']={'uniform_posterior':'2/3','contains_red_posterior':'1/2',
                      'unequal_selection_posterior':str((Q(1,3)*Q(2,3))/(Q(1,3)*Q(2,3)+Q(2,3)*Q(1,3)))}
    # AP-03: all six assignments, exact one- and two-sided tail counts.
    scores=[0,1,3,4]
    differences=[Q(sum(scores[i] for i in pair),2)-Q(sum(scores[i] for i in range(4) if i not in pair),2) for pair in combinations(range(4),2)]
    assert differences==list(map(Q,[-3,-1,0,0,1,3]))
    assert Q(sum(x>=3 for x in differences),6)==Q(1,6)
    assert Q(sum(abs(x)>=3 for x in differences),6)==Q(1,3)
    results['AP-03']={'differences':list(map(str,differences)),'one_sided':'1/6','two_sided':'1/3'}
    # AP-04: independent uniform draws with replacement from eight cards.
    population=[1]*4+[5]*4
    counts=Counter(Q(a+b,2) for a,b in product(population,repeat=2))
    distribution={str(k):str(Q(v,64)) for k,v in sorted(counts.items())}
    assert distribution=={'1':'1/4','3':'1/2','5':'1/4'}
    assert sum(k*Q(v,64) for k,v in counts.items())==3
    results['AP-04']={'distribution':distribution,'expectation':'3','restricted_bias':'-2'}
    # AP-05: all errors; coverage is translation independent by cancellation.
    coverage={width:Q(sum(abs(e)<=width for e in [-2,-1,0,1,2]),5) for width in [1,2]}
    assert coverage=={1:Q(3,5),2:Q(1)}
    results['AP-05']={'width_1_coverage':'3/5','width_2_coverage':'1',
                      'note':'The card supplies the algebraic translation argument for all integer targets.'}
    # Independent combinatorial checks of two survey anchors.
    masks=range(16)
    incomparable=lambda a,b: (a&b)!=a and (a&b)!=b
    max_size=0; maximizing=[]
    for subset in range(1<<16):
        size=subset.bit_count()
        if size<max_size: continue
        chosen=[a for a in masks if subset>>a&1]
        if all(incomparable(a,b) for a,b in combinations(chosen,2)):
            if size>max_size: max_size=size;maximizing=[]
            maximizing.append(chosen)
    assert max_size==6
    results['survey-05-antichains']={'domain':'all 65536 families of subsets of a four-element set','maximum':6,'maximizers':maximizing}
    edges=[(0,1),(1,2),(2,3),(3,0),(0,2)]
    trees=[es for es in combinations(edges,3) if connected(es,4)]
    assert len(trees)==8
    results['survey-05-spanning-trees']={'domain':'all 3-edge subsets of a square plus diagonal','count':8,'witnesses':trees}
    out=Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(results,indent=2)+'\n')
    print(f'{len(results)} exact instance checks passed; results in {out.name}')

if __name__=='__main__': main()
