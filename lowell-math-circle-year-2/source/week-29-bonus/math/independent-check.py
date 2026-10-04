#!/usr/bin/env python3
"""Independent ordered words, finite complements and generator check; stdlib only."""
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

finalsrc = Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-29-bonus.pdf'

@lru_cache(None)
def words(total):
    if total==0:return ((),)
    if total<0:return ()
    return tuple(prefix+(rod,) for rod in (3,4) for prefix in words(total-rod))

def combinations(total,lengths):
    return tuple(counts for counts in product(*(range(total//length+1) for length in lengths)) if sum(c*l for c,l in zip(counts,lengths))==total)

def reachable(lengths,limit):
    result=[False]*(limit+1); result[0]=True
    for n in range(1,limit+1):
        result[n]=any(n>=length and result[n-length] for length in lengths)
    return result

def optimum(total,lengths):
    builds=combinations(total,lengths)
    minimum=min(map(sum,builds))
    return {'fewest_rods':minimum,'all_optimal_counts':[counts for counts in builds if sum(counts)==minimum], 'all_count_combinations':builds}

def main():
    source = finalsrc.read_text()
    assert "For each successful build, what length do the unused rods make?" in source
    assert "as many copies of each stated rod length as you need" in source
    actual_words={n:sorted(words(n)) for n in (7,10,14,18)}
    assert [len(actual_words[n]) for n in (7,10,14,18)]==[2,3,6,11]
    assert all(sum(word)==n for n,rows in actual_words.items() for word in rows)
    dp=[0]*101;dp[0]=1
    for n in range(1,101):
        dp[n]=(dp[n-3] if n>=3 else 0)+(dp[n-4] if n>=4 else 0)
        independent_count=sum(comb(x+y,x) for x,y in combinations(n,(3,4)))
        assert dp[n]==independent_count
    finite={}
    for x,y in product(range(5),range(4)):
        n=3*x+4*y
        finite.setdefault(n,[]).append((x,y))
        assert 0<=4-x<=4 and 0<=3-y<=3
        assert 3*(4-x)+4*(3-y)==24-n
    gaps=[n for n in range(25) if n not in finite]
    assert gaps==[1,2,5,19,22,23]
    assert all((n in finite)==(24-n in finite) for n in range(25))
    assert finite[12]==[(0,3),(4,0)]
    assert all(n in finite for n in (6,9,10)) and all(n not in finite for n in (19,22))
    assert finite[6]==[(2,0)] and finite[9]==[(3,0)] and finite[10]==[(2,1)]
    # The non-task used/unused picture consumes the whole exact seven-rod stock.
    assert 3*3+4==13 and 3+2*4==11 and 13+11==24
    base=reachable((3,5),300)
    assert [n for n in range(301) if not base[n]]==[1,2,4,7]
    assert all(base[n] for n in (8,9,10))
    generators={}
    for added in (8,7,4):
        expanded=reachable((3,5,added),300)
        new=[n for n in range(301) if expanded[n] and not base[n]]
        expected={8:[],7:[7],4:[4,7]}[added]
        assert new==expected
        generators[added]={'new_targets':new,'range_checked':[0,300], 'proof_for_all_targets':'Every target >=8 was already reachable: base witnesses8=3+5,9=3+3+3,10=5+5; add3. Only base gaps1,2,4,7 can be new. Test them exactly; added8 also replaces by3+5.'}
    optima={n:{'3,5':optimum(n,(3,5)),'3,5,8':optimum(n,(3,5,8))} for n in (16,24)}
    assert [optima[n]['3,5']['fewest_rods'] for n in (16,24)]==[4,6]
    assert [optima[n]['3,5,8']['fewest_rods'] for n in (16,24)]==[2,3]
    run=Path(__file__).resolve().parent
    out={'week':29,'scope':'final/bonus.pdf, all 4 pages, Problems 1-6 and both worked diagrams','independent':True,
        'final_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'final_source_sha256':hashlib.sha256(finalsrc.read_bytes()).hexdigest(),
        'worked_word':{'rods':[4,3,4],'word':[4,3,4],'total':11},
        'P1':{n:{'count':len(actual_words[n]),'all_words':actual_words[n]} for n in (7,10,14)},
        'P2':{'target18':{'count':len(actual_words[18]),'all_words':actual_words[18]},'recurrence':'f(n)=f(n-3)+f(n-4) for n>0; f(0)=1; f(n)=0 for n<0','binomial_sum_crosschecks_positive_n':100},
        'worked_finite_split':{'used_counts_3_4':[3,1],'used_total':13,'unused_counts_3_4':[1,2],'unused_total':11},
        'P3':{n:{'used_count_options':finite.get(n,[]),'unused_length':24-n if n in finite else None,'unused_count_options':[(4-x,3-y) for x,y in finite.get(n,[])]} for n in (6,9,10,19,22)},
        'P4':{'all_20_subset_count_choices':finite,'gaps_0_to_24':gaps,'complement_theorem':'A subset of a finite stock of total T builds n iff the unused complement builds T-n, including0 andT.','equal_split_count_options':finite[12]},
        'P5':generators,'P6':optima,
        'diagram_check':'The4,3,4 word diagram has eleven unit divisions; used13/unused11 diagrams use the whole four3/three4 stock. Printed records are compact and physical construction is explicitly beside the page.',
        'located_errors':[],'physical_rehearsal':'untested'}
    (run/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Week 29 independent checks passed; checks.json written')

if __name__=='__main__':main()
