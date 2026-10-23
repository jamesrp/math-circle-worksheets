#!/usr/bin/env python3
"""Independent Week 90 finite verification. Python standard library only.

Coordinates are zero-based. Enumerates *all* legal corner choices recursively,
checks every intermediate row/column inequality, reverses every single slide,
and compares complete labeled outputs. Finite tests do not prove confluence.
No writer checker or generated mathematical data is imported.
"""
from collections import Counter
from itertools import permutations
import json


def diagram(rows):
    return {(r, c) for r, length in enumerate(rows) for c in range(length)}


def partition_shape(cells):
    if not cells:
        return ()
    lengths = tuple(sum(r == rr for rr, cc in cells) for r in range(max(r for r,c in cells)+1))
    assert cells == diagram(lengths)
    assert all(a >= b for a,b in zip(lengths, lengths[1:]))
    return lengths


def increasing(t):
    return all(v < w for (r,c),v in t.items() for (s,d),w in t.items()
               if (r == s and c < d) or (c == d and r < s))


def corners(inner):
    return sorted((r,c) for r,c in inner if (r+1,c) not in inner and (r,c+1) not in inner)


def fillings(outer, inner):
    cells = sorted(outer-inner)
    for labels in permutations(range(1,len(cells)+1)):
        t = dict(zip(cells, labels))
        if increasing(t):
            yield t


def reverse(t, start, end):
    t = dict(t)
    hole = end
    labels = []
    while hole != start:
        r,c = hole
        choices = [p for p in [(r-1,c),(r,c-1)] if p in t]
        assert choices, (start,end,hole)
        p = max(choices, key=t.get)
        labels.append(t[p])
        t[hole] = t.pop(p)
        hole = p
    return t, labels


def slide(outer, inner, t, start, larger=False):
    assert start in corners(inner)
    original = dict(t)
    t = dict(t)
    hole = start
    moves = []
    states = [(hole, dict(t))]
    while True:
        r,c = hole
        choices = [p for p in [(r,c+1),(r+1,c)] if p in t]
        if not choices:
            break
        p = (max if larger else min)(choices, key=t.get)
        moves.append(t[p])
        t[hole] = t.pop(p)
        assert sum(p) == sum(hole)+1
        hole = p
        assert sorted(t.values()) == sorted(original.values())
        if not larger:
            assert increasing(t), (original, states, hole, t)
        states.append((hole, dict(t)))
    new_outer, new_inner = outer-{hole}, inner-{start}
    partition_shape(new_outer)
    partition_shape(new_inner)
    assert set(t) == new_outer-new_inner
    if not larger:
        restored, revmoves = reverse(t, start, hole)
        assert restored == original
        assert revmoves == moves[::-1]
    return new_outer, new_inner, t, hole, moves, states


def rectify_all(outer, inner, t, order=()):
    if not inner:
        yield order, t
        return
    for start in corners(inner):
        o,i,q,_,_,_ = slide(outer,inner,t,start)
        yield from rectify_all(o,i,q,order+(start,))


def rows(t):
    shape = partition_shape(set(t))
    return '/'.join(''.join(str(t[(r,c)]) for c in range(n)) for r,n in enumerate(shape))


CATALOGS = {
 'A': ((3,2),(1,), ['1234','1324','1423','2314','2413'],
       ['12/34','13/24','134/2','123/4','124/3']),
 'D': ((3,2,1),(2,1), ['123','132','213','231','312','321'],
       ['1/2/3','13/2','12/3','12/3','13/2','123']),
 'B': ((3,3,2),(2,1), ['12345','12435','12534','13425','13524','21345','21435','21534',
        '23415','23514','31425','31524','32415','32514','41523','42513'],
       ['13/25/4','14/25/3','145/2/3','134/2/5','135/2/4','12/35/4','12/34/5','125/34',
        '124/3/5','125/3/4','13/24/5','135/24','123/4/5','123/45','134/25','124/35'])}


def check_catalogs():
    report = {}
    for name,(orows,irows,codes,expected) in CATALOGS.items():
        outer,inner = diagram(orows),diagram(irows)
        generated = list(fillings(outer,inner))
        actual_codes = [''.join(map(str,t.values())) for t in generated]
        assert actual_codes == codes, (name,actual_codes)
        entries = []
        for idx,t in enumerate(generated):
            outcomes = list(rectify_all(outer,inner,t))
            wanted_orders = [((0,0),)] if name=='A' else [((0,1),(1,0),(0,0)),((1,0),(0,1),(0,0))]
            assert sorted(order for order,result in outcomes) == wanted_orders
            assert {rows(result) for order,result in outcomes} == {expected[idx]}
            entries.append({'card':name+str(idx+1),'start_reading_order':codes[idx],
                            'finished_rows':expected[idx], 'shape':partition_shape(set(outcomes[0][1])),
                            'full_corner_orders':len(outcomes)})
        report[name] = entries
    assert len(set(x['finished_rows'] for x in report['B'])) == 16
    assert Counter(x['finished_rows'] for x in report['D']) == {'1/2/3':1,'13/2':2,'12/3':2,'123':1}
    assert Counter(tuple(x['shape']) for x in report['B']) == {(2,2,1):5,(3,1,1):6,(3,2):5}
    return report


def check_reverse_examples():
    results=[]
    for name,idx,corner,exitcell,moves in [('A',2,(0,0),(0,2),[1,3]),('A',4,(0,0),(1,1),[1,4]),
        ('B',4,(0,1),(1,2),[1,4]),('B',4,(1,0),(2,1),[2,5])]:
        orows,irows,codes,_ = CATALOGS[name]
        outer,inner = diagram(orows),diagram(irows)
        t=dict(zip(sorted(outer-inner),map(int,codes[idx-1])))
        o,i,q,e,m,s=slide(outer,inner,t,corner)
        assert (e,m)==(exitcell,moves)
        results.append({'card':name+str(idx),'start':corner,'exit':e,'forward':m,'reverse':m[::-1]})
    return results


def check_visuals():
    # Page 1 full operation and page 6 its exact reversal.
    outer,inner=diagram((2,2)),diagram((1,))
    start={(0,1):2,(1,0):1,(1,1):3}
    o,i,t,e,m,states=slide(outer,inner,start,(0,0))
    assert m==[1,3] and e==(1,1) and rows(t)=='12/3'
    assert states[1] == ((1,0),{(0,0):1,(0,1):2,(1,1):3})
    assert reverse(t,(0,0),e)==(start,[3,1])
    # Page 3 unchanged two-label input; finish lower slide, then open upper.
    outer,inner=diagram((3,2)),diagram((2,1))
    start={(0,2):1,(1,1):2}
    o,i,t,e,m,states=slide(outer,inner,start,(1,0))
    assert e==(1,1) and m==[2] and t=={(0,2):1,(1,0):2}
    assert i=={(0,0),(0,1)} and corners(i)==[(0,1)]


def check_larger():
    o,i,codes,_=CATALOGS['A']; outer,inner=diagram(o),diagram(i)
    expected=['312/4','213/4','214/3','243/1','24/13']
    for code,answer in zip(codes,expected):
        start=dict(zip(sorted(outer-inner),map(int,code)))
        _,_,t,_,_,_=slide(outer,inner,start,(0,0),larger=True)
        assert rows(t)==answer and not increasing(t)
    # Larger is not always destructive: a single-row skew tableau has no choice.
    o,i=diagram((4,)),diagram((1,)); t={(0,1):1,(0,2):2,(0,3):3}
    assert rows(slide(o,i,t,(0,0),True)[2])=='123'
    return expected


def partitions(n, cap=None):
    if n==0:
        yield ()
    else:
        for k in range(min(n,cap or n),0,-1):
            for rest in partitions(n-k,k):
                yield (k,)+rest


def check_extra_small_shapes():
    """Regression evidence: all skew shapes with outer size <=6 and 1..4 labels.
    Complete recursive choices, including zero-step slides. Not a universal proof.
    """
    starts=orders=0
    for size in range(1,7):
        for shape in partitions(size):
            outer=diagram(shape)
            for m in range(size+1):
                for ishape in partitions(m):
                    inner=diagram(ishape)
                    if not inner<=outer or not 1<=size-m<=4:
                        continue
                    for t in fillings(outer,inner):
                        results=list(rectify_all(outer,inner,t))
                        assert len({rows(q) for order,q in results})==1
                        starts+=1; orders+=len(results)
    return {'standard_skew_starts':starts,'complete_corner_sequences':orders,
            'scope':'outer size <=6, 1..4 labels; finite regression only'}


def main():
    result={'catalogs':check_catalogs(),'single_slide_reversals':check_reverse_examples(),
            'larger_A_outputs':check_larger(),'broader_finite_check':check_extra_small_shapes()}
    check_visuals()
    result['worked_visuals']='forward, successive-corner bridge, exact reverse passed'
    result['status']='PASS; finite checks do not prove the general rectification theorem'
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
