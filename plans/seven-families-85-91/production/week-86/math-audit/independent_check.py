"""Independent finite-horizon game solver. Does not import/read author's verifier."""
from itertools import product, combinations
from functools import lru_cache
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent

def graph(vertices, edges):
    adj={v:{v} for v in vertices}
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    return adj

def parse(edges): return [tuple(e) for e in edges.split()]
def ring(n):
    vs='abcdefghijklmno'[:n]
    return graph(vs,[(vs[i],vs[(i+1)%n]) for i in range(n)])

def solve(adj,k=1):
    """W_C[h],W_R[h] are states capture-forced within h future cop turns.
    Captured states cost zero. C existentially picks one simultaneous move;
    R universally chooses its reply. Staying is in every adjacency set.
    Fixed point is exactly finite reachability winning region. A surviving
    state has an R successor outside that region after each possible C move.
    """
    vs=tuple(sorted(adj));states=list(product(product(vs,repeat=k),vs))
    moves={cs:tuple(product(*(sorted(adj[c]) for c in cs))) for cs in product(vs,repeat=k)}
    wc={s:0 for s in states if s[1] in s[0]};wr=dict(wc);h=0
    while True:
        h+=1
        nc={s:h for s in states if s not in wc and any((ds,s[1]) in wr for ds in moves[s[0]])}
        wc.update(nc)
        nr={s:h for s in states if s not in wr and all((s[0],r) in wc for r in adj[s[1]])}
        wr.update(nr)
        if not nc and not nr:break
    worst={''.join(cs):max(wc.get((cs,r),float('inf')) for r in vs) for cs in moves}
    best=min(worst.values())
    return {'best':best,'best_starts':[c for c,t in worst.items() if t==best],
            'worst_by_start':worst,'cop_turn_winning_states':len(wc),'states':len(states)}

def folds(adj):
    return [(v,u) for v in sorted(adj) for u in sorted(adj[v]-{v}) if adj[v]<=adj[u]]

def removed(adj,v):return {u:ns-{v} for u,ns in adj.items() if u!=v}

def terminal_fold_maps(adj):
    @lru_cache(None)
    def explore(remaining):
        a={v:adj[v]&set(remaining) for v in remaining}; opts=folds(a)
        if not opts:return {remaining}
        return set().union(*(explore(tuple(x for x in remaining if x!=v)) for v,u in opts))
    return sorted(''.join(x) for x in explore(tuple(sorted(adj))))

def fold_sequence(adj,seq):
    steps=[]
    for v,u in seq:
        assert (v,u) in folds(adj)
        steps.append({'fold':v+'->'+u,'Nv':sorted(adj[v]),'Nu':sorted(adj[u])})
        adj=removed(adj,v)
    return {'steps':steps,'remaining':sorted(adj),'remaining_neighborhoods':{v:sorted(ns) for v,ns in adj.items()},'legal_folds':folds(adj)}

res={}
for n in range(1,16):
    vs='abcdefghijklmno'[:n];a=graph(vs,list(zip(vs,vs[1:])));sol=solve(a)
    assert sol['best']==n//2
    res['P'+str(n)]=sol
T1=graph('abcdefg',parse('ab bc cd de cf fg'))
T2=graph('abcdefgh',parse('ab bc cd de cf fg fh'))
F1=graph('abcdef',parse('ab bc ca cd de af'))
F2=graph('abcde',parse('ab bc cd de ea ac'))
for name,a in [('T1',T1),('T2',T2),('F1',F1),('F2',F2)]:
    res[name]=solve(a);res[name]['initial_folds']=folds(a);res[name]['terminal_fold_maps']=terminal_fold_maps(a)
assert res['T1']['best']==2 and res['T2']['best']==2
assert res['F1']['best']<float('inf') and res['F2']['best']==float('inf')
for n in range(3,9):
    res['R'+str(n)]=solve(ring(n));assert (res['R'+str(n)]['best']<float('inf'))==(n==3)
    # Invariant: before each cop turn R is outside N[C]. Every C move
    # leaves some legal R reply outside new N[C] when n>=4.
    if n>=4:
        a=ring(n)
        for c in a:
            assert any(r not in a[c] for r in a)
            for r in a:
                if r in a[c]:continue
                for d in a[c]:
                    assert d!=r
                    assert any(s not in a[d] for s in a[r])
for n in (4,5):
    a=ring(n);base=[(u,v) for u in a for v in a if u<v and v in a[u]]
    chords=[(u,v) for u in a for v in a if u<v and v not in a[u]]
    results=[]
    for cnt in range(len(chords)+1):
        for extra in combinations(chords,cnt):
            b=graph(a,base+list(extra));sol=solve(b)
            results.append({'extra':[''.join(e) for e in extra],'best':sol['best']})
    winning=[x for x in results if x['best']<float('inf')]
    minimum=min(len(x['extra']) for x in winning)
    res['chords_C'+str(n)]={'minimum':minimum,'minimum_winners':[x for x in winning if len(x['extra'])==minimum],'all_subsets':results}
assert res['chords_C4']['minimum']==1 and res['chords_C5']['minimum']==2
assert len(res['chords_C4']['minimum_winners'])==2 and len(res['chords_C5']['minimum_winners'])==5
res['D1_example']={'edges':'ab bc ca cd de af','solution':solve(F1)}
res['D2_example']={'edges':'ab bc cd de ef fa','solution':solve(ring(6))}
res['F1_sequence']=fold_sequence(F1,[('f','a'),('e','d'),('d','c'),('a','b'),('b','c')])
res['F2_sequence']=fold_sequence(F2,[('b','a')])
res['worked_fold']=fold_sequence(graph('wxyz',parse('wx xy yz')),[('w','x')])
for n in range(3,13):
    sol=solve(ring(n),2);assert sol['best']<float('inf');res['two_cops_C'+str(n)]=sol
    # Independently check blocker+sweeper against every robber reply.
    # Both cops start a=0; stationary cop remains 0; moving cop advances
    # 1,2,...,n-1. Maintain possible uncaptured robber positions.
    a={i:{i,(i-1)%n,(i+1)%n} for i in range(n)}
    possible=set(range(1,n));history=[sorted(possible)]
    for s in range(1,n):
        possible.discard(s)
        possible={q for r in possible for q in a[r] if q not in {0,s}}
        history.append(sorted(possible))
    assert not possible
    res['blocker_sweep_C'+str(n)]=history
res['pdf_sha256']={n:hashlib.sha256((ROOT.parent/'draft'/f'{n}.pdf').read_bytes()).hexdigest() for n in ['shared','upper','materials']}
(ROOT/'results.json').write_text(json.dumps(res,indent=2,allow_nan=True)+'\n')
for key in ['P5','P7','T1','T2','R3','R4','R5','R6','F1','F2','chords_C4','chords_C5','two_cops_C6','two_cops_C8']:
    val=res[key];print(key, {k:v for k,v in val.items() if k in ['best','best_starts','worst_by_start','minimum','minimum_winners','initial_folds','terminal_fold_maps']})
print('All independent assertions passed.')
