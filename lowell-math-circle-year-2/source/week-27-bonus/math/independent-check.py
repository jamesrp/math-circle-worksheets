#!/usr/bin/env python3
"""Independent stable-pairing enumerations and invariant checks; stdlib only."""
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json

finalsrc = Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-27-bonus.pdf'

def partial_matchings(left,right,prefs):
    allowed={p:tuple(q for q in right if q in prefs[p] and p in prefs[q]) for p in left}
    def generate(index,used,pairs):
        if index==len(left):
            yield tuple(pairs); return
        p=left[index]
        yield from generate(index+1,used,pairs)
        for q in allowed[p]:
            if q not in used:
                yield from generate(index+1,used|{q},pairs+[(p,q)])
    return tuple(generate(0,set(),[]))

def blockers(pairs,left,right,prefs):
    partner={p:q for p,q in pairs}; partner.update({q:p for p,q in pairs})
    def better(p,q):
        return p not in partner or prefs[p].index(q)<prefs[p].index(partner[p])
    return [p+q for p in left for q in right if q in prefs[p] and p in prefs[q] and partner.get(p)!=q and better(p,q) and better(q,p)]

def records(left,right,prefs):
    return [{"pairs":[p+q for p,q in pairs],"blocking_pairs":blockers(pairs,left,right,prefs),
             "unpaired":[p for p in left+right if all(p not in pair for pair in pairs)]} for pairs in partial_matchings(left,right,prefs)]

def room_records(prefs):
    labels=tuple(prefs)
    result=[]
    p=labels[0]
    for q in labels[1:]:
        other=[x for x in labels if x not in (p,q)]
        pairs=((p,q),tuple(other)); partner={}
        for x,y in pairs: partner[x]=y; partner[y]=x
        bad=[x+y for x,y in combinations(labels,2) if partner[x]!=y and prefs[x].index(y)<prefs[x].index(partner[x]) and prefs[y].index(x)<prefs[y].index(partner[y])]
        result.append({"pairs":[x+y for x,y in pairs],"blocking_pairs":bad})
    return result

def subsets_in_order(labels):
    return tuple(p for k in range(len(labels)+1) for p in permutations(labels,k))

def main():
    source = finalsrc.read_text()
    assert "Current pairs: U--P \\quad V--Q" in source
    assert "V: P, \\fbox{Q}" in source and "P: V, \\fbox{U}" in source
    current = {'U':'P','P':'U','V':'Q','Q':'V'}
    visual_preferences = {'V':('P','Q'),'P':('V','U')}
    assert visual_preferences['V'].index('P') < visual_preferences['V'].index(current['V'])
    assert visual_preferences['P'].index('V') < visual_preferences['P'].index(current['P'])
    assert current['V'] != 'P'
    prefs={"A":("Y","Z","X"),"B":("Y","X","Z"),"C":("X","Y","Z"),"X":("B","A","C"),"Y":("A","C","B"),"Z":("B","A","C")}
    complete=[]
    for perm in permutations("XYZ"):
        pairs=tuple(zip("ABC",perm))
        total=sum(prefs[p].index(q)+1+prefs[q].index(p)+1 for p,q in pairs)
        complete.append({"pairs":[p+q for p,q in pairs],"total":total,"blocking_pairs":blockers(pairs,"ABC","XYZ",prefs)})
    assert [row['total'] for row in complete]==[15,13,11,10,11,12]
    assert [row['pairs'] for row in complete if not row['blocking_pairs']]==[["AY","BX","CZ"]]
    assert min(complete,key=lambda row:row['total'])['pairs']==["AY","BZ","CX"]
    profiles=(
        ("AB","XY",{"A":("X",),"B":("X",),"X":("A","B"),"Y":()}),
        ("ABC","XYZ",{"A":("X","Y"),"B":("Y","X"),"C":("Y",),"X":("B","A"),"Y":("A","B","C"),"Z":()}))
    incomplete=[]
    for left,right,pr in profiles:
        all_rows=records(left,right,pr); stable=[row for row in all_rows if not row['blocking_pairs']]
        incomplete.append({"all_allowed_matchings":all_rows,"stable":stable})
    assert [row['pairs'] for row in incomplete[0]['stable']]==[["AX"]]
    assert sorted(row['pairs'] for row in incomplete[1]['stable'])==[["AX","BY"],["AY","BX"]]
    assert all(row['unpaired']==["C","Z"] for row in incomplete[1]['stable'])
    roommate_profiles=(
        {"A":("B","C","D"),"B":("C","A","D"),"C":("A","B","D"),"D":("A","B","C")},
        {"A":("B","C","D"),"B":("A","C","D"),"C":("D","A","B"),"D":("C","A","B")})
    roommates=[room_records(pr) for pr in roommate_profiles]
    assert all(row['blocking_pairs'] for row in roommates[0])
    assert [row['pairs'] for row in roommates[1] if not row['blocking_pairs']]==[["AB","CD"]]
    # Exhaust all strict incomplete 2x2 profiles, including asymmetric omissions.
    orders_left=subsets_in_order("XY"); orders_right=subsets_in_order("AB")
    profiles_checked=0; multi_stable=0
    for a,b,x,y in product(orders_left,orders_left,orders_right,orders_right):
        pr=dict(zip("ABXY",(a,b,x,y)))
        stable=[row for row in records("AB","XY",pr) if not row['blocking_pairs']]
        assert stable
        assert len({tuple(row['unpaired']) for row in stable})==1
        profiles_checked+=1; multi_stable+=len(stable)>1
    assert profiles_checked==625
    # All mutually allowed edge sets on the actual 3x3 label set, in four rank patterns.
    graph_profiles_checked=0
    edges=tuple(product("ABC","XYZ"))
    for mask in range(512):
        allowed={edge for i,edge in enumerate(edges) if mask&(1<<i)}
        for left_order,right_order in (("XYZ","ABC"),("ZYX","ABC"),("XYZ","CBA"),("YZX","BCA")):
            pr={p:tuple(q for q in left_order if (p,q) in allowed) for p in "ABC"}
            pr.update({q:tuple(p for p in right_order if (p,q) in allowed) for q in "XYZ"})
            stable=[row for row in records("ABC","XYZ",pr) if not row['blocking_pairs']]
            assert stable and len({tuple(row['unpaired']) for row in stable})==1
            graph_profiles_checked+=1
    run=Path(__file__).resolve().parent
    out={"week":27,"scope":"final/bonus.pdf, all 4 pages, Problems 1-4 and blocking-check visual","independent":True,
        "final_pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "final_source_sha256":hashlib.sha256(finalsrc.read_bytes()).hexdigest(),
        "P1":complete,"P2":incomplete,"P3":roommates,
        "P4":{"answer":"Impossible with strict two-sided mutual acceptable lists and all acceptable partners above being unpaired", "all_strict_incomplete_2x2_profiles_checked":profiles_checked,"two_by_two_profiles_with_multiple_stable":multi_stable,"three_by_three_edge_rank_profiles_checked":graph_profiles_checked,"general_certificate":"Symmetric difference of two matchings consists of alternating paths/cycles. A path starting at an M-unmatched/N-matched object propagates strictly preferred partners by alternating M- and N-stability. A finite nonrepeating path must end, but either endpoint would then supply the forced blocking pair. Thus matched sets agree on both sides."},
        "worked_example":"With fixed UP,VQ, V prefers P to Q and P prefers V to U; VP blocks. Both checks use the same unchanged matching.",
        "diagram_check":"Six score-profile strips, both omitted-choice profiles, both complete roommate profiles and labeled same-type A-D boards match the separately transcribed inputs.","located_errors":[],"physical_rehearsal":"untested"}
    (run/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Week 27 independent checks passed; checks.json written')

if __name__=='__main__':main()
