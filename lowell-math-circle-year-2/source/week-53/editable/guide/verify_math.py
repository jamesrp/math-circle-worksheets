"""Independent guide enumeration from manually transcribed final student maps.

Uses union-find, not the student writer's checker or the independent review's
closure routine. Full catalogs/report are generated outside the source folder.
"""
import argparse
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path

GRAPHS = {
    'xyz': ('XYZ', {'XY':2, 'YZ':4, 'XZ':3}),
    'p1_left': ('ABC', {'AB':1, 'BC':2, 'AC':3}),
    'p1_right': ('ABC', {'AB':1, 'BC':2, 'AC':2}),
    'p2': ('ABCD', {'AB':1, 'BC':1, 'AC':1, 'CD':2, 'AD':3}),
    'p3': ('ABCD', {'AB':1, 'BC':2, 'AC':3, 'CD':4, 'AD':5}),
    'p4': ('ABCDE', {'AB':1, 'BC':1, 'AC':1, 'CD':2, 'DE':2,
                    'CE':3, 'AD':5, 'BE':6}),
    'uvw': ('UVW', {'UV':2, 'VW':4, 'UW':3}),
    'p5': ('ABCD', {'AB':1, 'BC':2, 'CD':3, 'AD':4, 'AC':5}),
    'p6_p8': ('ABCDEF', {'AB':1, 'BC':2, 'AC':3, 'CD':2,
                         'DE':1, 'EF':2, 'DF':4, 'BD':5, 'CE':6}),
    'p9': ('ABCD', {'AB':1, 'BC':2, 'CD':3, 'AD':4, 'AC':5, 'BD':6}),
}
EXPECTED = {
    'xyz': (5, [('XY','XZ')], 4,3),
    'p1_left': (3, [('AB','BC')], 4,3),
    'p1_right': (3, [('AB','BC'),('AB','AC')], 4,3),
    'p2': (4, [('AB','AC','CD'),('AB','BC','CD'),('AC','BC','CD')],14,8),
    'p3': (7, [('AB','BC','CD')],14,8),
    'p4': (6, [('AB','AC','CD','DE'),('AB','BC','CD','DE'),
               ('AC','BC','CD','DE')],134,45),
    'uvw': (5, [('UV','UW')],4,3),
    'p5': (6, [('AB','BC','CD')],14,8),
    'p6_p8': (8, [('AB','BC','CD','DE','EF')],164,55),
    'p9': (6, [('AB','BC','CD')],38,16),
}

def status(vertices, edges):
    parent = {v:v for v in vertices}
    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    cyclic = False
    for a,b in edges:
        ra,rb = root(a),root(b)
        if ra == rb:
            cyclic = True
        else:
            parent[ra] = rb
    return len({root(v) for v in vertices}) == 1, cyclic

def purchases(vertices, weights):
    edges = list(weights)
    return [frozenset(e for i,e in enumerate(edges) if mask & (1<<i))
            for mask in range(1<<len(edges))
            if status(vertices, (e for i,e in enumerate(edges)
                                  if mask & (1<<i)))[0]]

def cost(weights, selection):
    return sum(weights[e] for e in selection)

def swaps(vertices, weights, tree):
    tree = frozenset(tree)
    total = cost(weights,tree)
    result = []
    for remove in sorted(tree):
        for buy in sorted(set(weights)-tree):
            proposal = tree-{remove}|{buy}
            if weights[buy] < weights[remove] and status(vertices,proposal)[0]:
                result.append({'return':remove,'buy':buy,
                    'new_cost':total-weights[remove]+weights[buy],
                    'result':sorted(proposal)})
    return result

def path(tree, a, b):
    adj = {}
    for x,y in tree:
        adj.setdefault(x,[]).append(y)
        adj.setdefault(y,[]).append(x)
    def walk(v, previous, record):
        if v == b:
            return record
        for w in adj.get(v,[]):
            if w != previous:
                found = walk(w,v,record+[''.join(sorted((v,w)))])
                if found is not None:
                    return found
        return None
    result = walk(a,None,[])
    assert result is not None
    return result

def audit():
    report = {'method':'manual final-map transcription; union-find exhaustive subsets; no student checker imports',
              'graphs':{},'swaps':{},'cuts':[],'cycles':[], 'inverse':{}}
    trees_checked = 0
    for name,(vertices,weights) in GRAPHS.items():
        connected = purchases(vertices,weights)
        trees = [s for s in connected if not status(vertices,s)[1]]
        minimum = min(cost(weights,s) for s in connected)
        optima = {s for s in connected if cost(weights,s)==minimum}
        target,sets,nc,nt = EXPECTED[name]
        assert (minimum,len(connected),len(trees)) == (target,nc,nt), name
        assert optima == {frozenset(s) for s in sets}, name
        details = []
        for tree in trees:
            legal = swaps(vertices,weights,tree)
            inequalities = {e:{'path':path(tree,*e),
                'largest':max(weights[f] for f in path(tree,*e)),
                'price':weights[e]} for e in weights if e not in tree}
            passes = all(d['price'] >= d['largest'] for d in inequalities.values())
            assert passes == (not legal) == (tree in optima), (name,tree)
            details.append({'links':sorted(tree),'cost':cost(weights,tree),
                'improving':legal,'unused_path_tests':inequalities})
        # For each strict-minimum cut, all optima include that edge.
        for k in range(1,len(vertices)):
            for side in combinations(vertices,k):
                crossing = [e for e in weights if (e[0] in side)!=(e[1] in side)]
                low = min(weights[e] for e in crossing)
                cheap = [e for e in crossing if weights[e]==low]
                if len(cheap)==1:
                    assert all(cheap[0] in s for s in optima)
        assert max(cost(weights,s) for s in connected) <= 30
        assert len(weights) <= 10
        trees_checked += len(trees)
        report['graphs'][name] = {'subsets':2**len(weights),
            'connected':len(connected),'trees':len(trees),'minimum':minimum,
            'optima':sorted(sorted(s) for s in optima),
            'all_connected_purchases':[{'links':sorted(s),'cost':cost(weights,s)}
                                       for s in connected],
            'all_trees_with_swaps':details}
    assert trees_checked == 152
    report['trees_checked'] = trees_checked
    v,w = GRAPHS['p6_p8']
    assert all(status(v,set(w)-{e})[0] for e in w)  # no available bridge
    report['six_place_bridges'] = []
    for side,expected in [('A','AB'),('AB','BC'),('ABC','CD'),('E','DE'),('F','EF')]:
        crossing = {e:w[e] for e in w if (e[0] in side)!=(e[1] in side)}
        assert min(crossing,key=crossing.get) == expected
        assert sum(x==min(crossing.values()) for x in crossing.values()) == 1
        report['cuts'].append({'side':side,'crossing':crossing,'forced':expected})
    for loop,excluded in [('ABC','AC'),('DEF','DF'),('BCD','BD'),('CDE','CE')]:
        cycle = [''.join(sorted((loop[i],loop[(i+1)%3]))) for i in range(3)]
        assert w[excluded] > max(w[e] for e in cycle if e != excluded)
        report['cycles'].append({'vertices':loop,'edges':cycle,'excluded':excluded})
    for name,graph,selection,expected in [
        ('p5_left','p5',('AB','AD','AC'),[('AC','BC',7),('AC','CD',8),('AD','CD',9)]),
        ('p5_right','p5',('AB','BC','CD'),[]),
        ('p8_top','p6_p8',('AB','BC','CD','DE','EF'),[]),
        ('p8_bottom','p6_p8',('AB','AC','BD','DE','DF'),
         [('AC','BC',13),('AC','CD',13),('BD','CD',11),('DF','EF',12)])]:
        vs,ws = GRAPHS[graph]
        found = swaps(vs,ws,selection)
        assert [(s['return'],s['buy'],s['new_cost']) for s in found] == expected
        report['swaps'][name] = {'input':selection,'cost':cost(ws,selection),'improving':found}
    order = ['AB','BC','AC','AD','BD','CD']
    connected = purchases('ABCD',dict.fromkeys(order,1))
    assert len(connected)==38
    assert sum(not status('ABCD',s)[1] for s in connected)==16
    distribution = Counter()
    designs = []
    for prices in product(range(1,5),repeat=6):
        ws = dict(zip(order,prices))
        values = [(cost(ws,s),s) for s in connected]
        minimum = min(c for c,s in values)
        optima = [sorted(s) for c,s in values if c==minimum]
        distribution[len(optima)] += 1
        designs.append({'prices':prices,'minimum':minimum,'optima':optima})
    assert dict(distribution)=={1:1956,2:936,3:768,4:144,5:96,6:96,8:72,9:24,16:4}
    assert sum(distribution.values())==4096
    for prices,expected in [((1,1,3,2,3,4),[('AB','BC','AD')]),
                           ((1,2,2,1,4,4),[('AB','AD','BC'),('AB','AD','AC')])]:
        item = next(d for d in designs if d['prices']==prices)
        assert item['minimum']==4
        assert {frozenset(s) for s in item['optima']}=={frozenset(s) for s in expected}
    report['inverse'] = {'edge_order':order,'assignments':4096,'unique':1956,
        'multiple':2140,'distribution':dict(sorted(distribution.items())),
        'all_assignments':designs}
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--report',type=Path,required=True)
    args = parser.parse_args()
    report = audit()
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: 152 trees; all connected subsets; all specified swaps; 4096 inverse assignments; cuts/cycles and no bridges.')

if __name__ == '__main__':
    main()
