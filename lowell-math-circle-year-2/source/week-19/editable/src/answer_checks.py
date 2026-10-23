"""Week 19 answer checks: exhaustive enumeration of legal collections on two, three and four symbols.

Carried over unchanged from the old student builder (build_packets.py, archived in
../../archive-before-problem-files-2026-10-23/). It writes answer_checks.json and returns the checks.
"""
from pathlib import Path
import itertools,json
ROOT=Path(__file__).resolve().parent


def run():
    # Mathematical verification is kept in the source folder, never in student pages.
    def legal(c):
        return all((a&b)!=a and (a&b)!=b for a,b in itertools.combinations(c,2))
    checks={}
    for n in [2,3,4]:
        cards=list(range(1<<n))
        ants=[tuple(c for c in cards if (mask>>c)&1) for mask in range(1<<len(cards))]
        ants=[a for a in ants if legal(a)]
        largest=max(map(len,ants))
        checks[n]={'maximum':largest,'all_nonempty_collections':len(ants)-1,'largest_collections':[a for a in ants if len(a)==largest]}
        if n==3:
            checks[n]['two_card_collections']=[a for a in ants if len(a)==2]
            checks[n]['remove_any_one_still_three']=all(any(len(a)==3 and d not in a for a in ants) for d in cards)
            checks[n]['starting_collection_maxima']={str(s):max(len(a) for a in ants if set(s)<=set(a)) for s in [(7,),(1,),(3,),(1,6)]}
        if n==4:checks[n]['starting_collection_maxima']={str(s):max(len(a) for a in ants if set(s)<=set(a)) for s in [(15,),(1,14),(3,5),(1,)]}
    chains={2:[[0,1,3],[2]],3:[[0,1,3,7],[4,5],[2,6]],4:[[0,1,3,7,15],[8,9,11],[4,5,13],[12],[2,6,14],[10]]}
    for n,rows in chains.items():
        assert sorted(sum(rows,[]))==list(range(1<<n))
        assert all((a&b)==a for row in rows for a,b in zip(row,row[1:]))
        assert len(rows)==checks[n]['maximum']
    assert [checks[n]['maximum'] for n in [2,3,4]]==[2,3,6]
    assert len(checks[4]['largest_collections'])==1
    assert checks[4]['starting_collection_maxima']['(1,)']==4
    (ROOT/'answer_checks.json').write_text(json.dumps(checks,indent=2))
    return checks


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
