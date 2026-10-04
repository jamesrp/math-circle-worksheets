#!/usr/bin/env python3
"""Original exhaustive subset verification of all original printed networks."""
import argparse
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path


def edgekey(e): return ''.join(sorted(e[:2]))


def connected(vertices, edges):
    if not vertices: return False
    reached={vertices[0]}
    changed=True
    while changed:
        changed=False
        for a,b,_ in edges:
            if a in reached or b in reached:
                before=len(reached);reached.update((a,b))
                changed=changed or before!=len(reached)
    return len(reached)==len(vertices)


def path(tree,start,end):
    queue=[(start,[])]
    seen=set()
    while queue:
        v,route=queue.pop(0)
        if v==end:return route
        if v in seen:continue
        seen.add(v)
        for e in tree:
            a,b,w=e
            if v in (a,b):queue.append((b if v==a else a,route+[e]))
    raise AssertionError('Candidate not connected')


def all_sets(edges):
    for mask in range(1<<len(edges)):
        yield [e for i,e in enumerate(edges) if mask&(1<<i)]


def audit(vertices,edges):
    assert len(set(vertices))==len(vertices)
    assert len({edgekey(e) for e in edges})==len(edges)
    assert all(a!=b and a in vertices and b in vertices and isinstance(w,int) and w>0 for a,b,w in edges)
    feasible=[s for s in all_sets(edges) if connected(vertices,s)]
    minimum=min(sum(e[2] for e in s) for s in feasible)
    optima=[s for s in feasible if sum(e[2] for e in s)==minimum]
    trees=[s for s in feasible if len(s)==len(vertices)-1]
    assert all(len(s)==len(vertices)-1 for s in optima)
    for tree in trees:
        valid_certificate=all(max(e[2] for e in path(tree,a,b))<=w for a,b,w in edges if [a,b,w] not in tree)
        assert valid_certificate==(sum(e[2] for e in tree)==minimum)
        lower_swaps=swaps(vertices,edges,tree)
        assert (len(lower_swaps)==0)==valid_certificate
    optimum_sets=[{edgekey(e) for e in s} for s in optima]
    mandatory=set.intersection(*optimum_sets)
    allowed=set.union(*optimum_sets)
    excluded={edgekey(e) for e in edges}-allowed
    cut_certificates={}
    for r in range(1,len(vertices)):
        for side in combinations(vertices,r):
            cut=[e for e in edges if (e[0] in side)!=(e[1] in side)]
            if not cut:continue
            lowest=min(e[2] for e in cut)
            cheapest=[e for e in cut if e[2]==lowest]
            if len(cheapest)==1:
                name=edgekey(cheapest[0]);cut_certificates.setdefault(name,{'side':list(side),'crossing':cut})
                assert name in mandatory
    cycle_certificates={}
    for subset in all_sets(edges):
        if len(subset)<3:continue
        deg=Counter(v for e in subset for v in e[:2])
        active=list(deg)
        if not all(x==2 for x in deg.values()) or not connected(active,subset):continue
        highest=max(e[2] for e in subset)
        expensive=[e for e in subset if e[2]==highest]
        if len(expensive)==1:
            name=edgekey(expensive[0]);cycle_certificates.setdefault(name,subset)
            assert name in excluded
    return {'minimum_cost':minimum,'number_of_optima':len(optima),'optimal_purchases':[[edgekey(e) for e in t] for t in optima],
            'connected_subsets_checked':len(feasible),'subsets_checked':1<<len(edges),'trees_checked':len(trees),
            'all_tree_exchange_certificates_verified':True,'mandatory':sorted(mandatory),'excluded':sorted(excluded),
            'unique_cheapest_cut_certificates':cut_certificates,'strict_heaviest_cycle_certificates':cycle_certificates}


def swaps(vertices,edges,tree):
    total=sum(e[2] for e in tree)
    result=[]
    for ret in tree:
        for buy in edges:
            if buy in tree:continue
            changed=[e for e in tree if e!=ret]+[buy]
            cost=sum(e[2] for e in changed)
            if cost<total and connected(vertices,changed):
                result.append({'return':edgekey(ret),'buy':edgekey(buy),'cost':cost})
    return result


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--report',type=Path);args=parser.parse_args()
    data=json.loads(Path(__file__).with_name('networks.json').read_text())
    report={'scope':'original source verifier; independently cross-checked in fresh math review; not physical rehearsal','fixed_maps':{}}
    for name,g in data.items():
        if name=='price_design':continue
        vertices=[v[0] for v in g['vertices']];edges=g['edges']
        out=audit(vertices,edges)
        assert sum(e[2] for e in edges)<=30 and len(edges)<=10
        if 'expect_cost' in g:
            assert (out['minimum_cost'],out['number_of_optima'])==(g['expect_cost'],g['expect_count'])
        out['available_price_sum']=sum(e[2] for e in edges);out['link_count']=len(edges)
        report['fixed_maps'][name]=out
    first=[e for e in data['swaps']['edges'] if edgekey(e) in {'AB','AD','AC'}]
    second=[e for e in data['swaps']['edges'] if edgekey(e) in {'AB','BC','CD'}]
    report['problem_5']={'first_purchase_cost':sum(e[2] for e in first),'cheaper_single_swaps':swaps(list('ABCD'),data['swaps']['edges'],first),'second_cheaper_single_swaps':swaps(list('ABCD'),data['swaps']['edges'],second)}
    assert report['problem_5']['cheaper_single_swaps']==[{'return':'AD','buy':'CD','cost':9},{'return':'AC','buy':'BC','cost':7},{'return':'AC','buy':'CD','cost':8}]
    assert report['problem_5']['second_cheaper_single_swaps']==[]
    six=report['fixed_maps']['six_cert']
    assert set(six['mandatory'])==set(six['unique_cheapest_cut_certificates'])
    assert set(six['excluded'])==set(six['strict_heaviest_cycle_certificates'])
    design=data['price_design']
    report['problem_7_witnesses']={}
    for label,prices,count in [('unique',[1,1,3,2,3,4],1),('multiple',[1,2,2,1,4,4],2)]:
        edges=[[a,b,w] for (a,b,_),w in zip(design['edges'],prices)]
        out=audit(list('ABCD'),edges)
        assert len(set(prices))<len(prices) and all(1<=w<=4 for w in prices) and out['number_of_optima']==count
        out['edge_prices']=edges;report['problem_7_witnesses'][label]=out
    # All six prices are chosen independently; repetition is permitted.
    shape=[[a,b,1] for a,b,_ in design['edges']]
    feasible_keys=[[edgekey(e) for e in subset] for subset in all_sets(shape) if connected(list('ABCD'),subset)]
    keys=[edgekey(e) for e in shape]
    multiplicities=Counter()
    for prices in product(range(1,5),repeat=6):
        weights=dict(zip(keys,prices))
        totals=[sum(weights[e] for e in subset) for subset in feasible_keys]
        multiplicities[totals.count(min(totals))]+=1
    assert dict(multiplicities)=={1:1956,2:936,3:768,4:144,5:96,6:96,8:72,9:24,16:4}
    report['problem_7_all_assignments']={'assignments':4096,'unique':multiplicities[1],'multiple':4096-multiplicities[1],'optimum_multiplicity_distribution':dict(sorted(multiplicities.items()))}
    assert 6*4<=30
    report['problem_8']={}
    for label,purchase in [('good',{'AB','BC','CD','DE','EF'}),('bad',{'AB','AC','BD','DE','DF'})]:
        edges=data['six_cert']['edges'];tree=[e for e in edges if edgekey(e) in purchase]
        assert len(tree)==5 and connected(list('ABCDEF'),tree)
        report['problem_8'][label]={'cost':sum(e[2] for e in tree),'cheaper_swaps':swaps(list('ABCDEF'),edges,tree),'unused_path_tests':[{'unused':edgekey(e),'price':e[2],'tree_path':[edgekey(x) for x in path(tree,e[0],e[1])],'max_path_price':max(x[2] for x in path(tree,e[0],e[1]))} for e in edges if e not in tree]}
    assert report['problem_8']['good']['cost']==8 and not report['problem_8']['good']['cheaper_swaps']
    assert report['problem_8']['bad']['cost']==14
    assert {(s['return'],s['buy'],s['cost']) for s in report['problem_8']['bad']['cheaper_swaps']}=={('AC','BC',13),('AC','CD',13),('BD','CD',11),('DF','EF',12)}
    text=json.dumps(report,indent=2)+'\n'
    if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(text)
    else:print(text)
    print('All fixed purchases, optima, swaps, cut/cycle and certificate checks passed.')


if __name__=='__main__': main()
