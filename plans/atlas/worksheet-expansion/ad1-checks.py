#!/usr/bin/env python3
"""Exact finite audits for AD-01..AD-08. Run from any working directory.
General claims are proved in solutions/design notes; finite tests do not prove them.
Only the standard library is used. Mathematical fixture data live in this plan folder.
"""
import itertools as it
import json
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE/'ad1-data.json').read_text())
F={f['id']:f for f in DATA['families']}
RESULTS={}
def audit(name, value): RESULTS[name]=value

def subsets(items):
    items=tuple(items)
    return [frozenset(items[i] for i in range(len(items)) if m>>i&1) for m in range(1<<len(items))]
def antichain(c): return all(not(a<=b or b<=a) for a,b in it.combinations(c,2))
def connected(vertices, edges):
    vertices=set(vertices)
    if not vertices: return True
    seen={next(iter(vertices))}
    while True:
        new=seen|{v for e in edges if any(u in seen for u in e) for v in e}
        if new==seen: return seen==vertices
        seen=new

def norm(edges): return tuple(sorted(tuple(sorted(e)) for e in edges))
def tree(vertices,edges): return len(edges)==len(vertices)-1 and connected(vertices,edges)
def encode(vertices,edges,largest=False):
    vs=set(vertices); es=set(norm(edges)); msg=[]
    while len(vs)>2:
        deg=Counter(v for e in es for v in e)
        leaf=(max if largest else min)(v for v in vs if deg[v]==1)
        e=next(e for e in es if leaf in e)
        msg.append(next(v for v in e if v!=leaf)); es.remove(e); vs.remove(leaf)
    return tuple(msg)
def decode(vertices,msg):
    vs=set(vertices); seq=list(msg); es=[]
    while seq:
        leaf=min(vs-set(seq)); neighbor=seq.pop(0)
        assert neighbor in vs and neighbor!=leaf
        es.append((leaf,neighbor)); vs.remove(leaf)
    assert len(vs)==2
    es.append(tuple(vs)); return norm(es)
def det(m):
    n=len(m)
    if n==0:return 1
    return sum(((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))) *
               __import__('math').prod(m[i][p[i]] for i in range(n)) for p in it.permutations(range(n)))
def laplacian(vs,edges):
    m=[[0]*len(vs) for _ in vs]
    for a,b in edges:
        i,j=vs.index(a),vs.index(b)
        m[i][i]+=1;m[j][j]+=1;m[i][j]-=1;m[j][i]-=1
    return m
def cofactor(m,k):return [[x for j,x in enumerate(row) if j!=k] for i,row in enumerate(m) if i!=k]

def order_closure(vs,covers):
    rel={(v,v) for v in vs}|set(map(tuple,covers))
    while True:
        r=rel|{(a,d) for a,b in rel for c,d in rel if b==c}
        if r==rel:return r
        rel=r

def bounds(vs,rel,a,b,upper=True):
    if upper:
        common=[x for x in vs if (a,x) in rel and (b,x) in rel]
        best=[x for x in common if all((x,y) in rel for y in common)]
    else:
        common=[x for x in vs if (x,a) in rel and (x,b) in rel]
        best=[x for x in common if all((y,x) in rel for y in common)]
    return best[0] if len(best)==1 else None

def partitions(n):
    # Restricted-growth strings enumerate each set partition exactly once.
    def rec(labels):
        if len(labels)==n:
            yield tuple(labels);return
        for k in range(max(labels,default=-1)+2):yield from rec(labels+[k])
    yield from rec([])
def compatible(part,mod):
    return all(part[(a+b)%mod]==part[(c+d)%mod]
               for a,b,c,d in it.product(range(mod),repeat=4)
               if part[a]==part[c] and part[b]==part[d])
def blocks(part):return [[i for i,v in enumerate(part) if v==k] for k in range(max(part)+1)]

# Schema and prompt completeness.
required={'id','title','core_gate','extension_gate','reading','materials','prep_minutes','timing','launch','satisfying_stop','prior_use','assessment','mathematical_connection','sources','pages','extensions'}
assert DATA['batch']=='ad1' and set(F)=={f'AD-{n:02}' for n in range(1,9)} and len(DATA['families'])==8
prompt_counts={}
for f in F.values():
    assert required<=set(f)
    assert 50<=len(f['index_gate'])<=95
    ids=[]
    for p in f['pages']:
        assert all(isinstance(p[k],str) and p[k] for k in ('title','gate','intro'))
        for q in p['prompts']:
            assert all(q[k] for k in ('id','text','solution','hints'))
            ids.append(q['id'])
    assert len(set(ids))==len(ids)
    prompt_counts[f['id']]=len(ids)
audit('schema',dict(families=8,student_pages=sum(len(f['pages']) for f in F.values()),prompt_counts=prompt_counts,total_prompts=sum(prompt_counts.values()),guide_extensions=sum(len(f['extensions']) for f in F.values())))

# AD-01: all presence/absence worlds; duplicates do not affect unary claims.
types=['RC','RS','BC','BS']; worlds=subsets(types)
def rule(w):return 'RS' not in w
def converse(w):return 'BC' not in w
p1=[w for w in worlds if any(x[0]=='R' for x in w) and rule(w) and not converse(w)]
assert min(map(len,p1))==2 and [w for w in p1 if len(w)==2]==[frozenset(['RC','BC'])]
promised=[w for w in worlds if rule(w) and any(x[1]=='S' for x in w)]
claims={'A':lambda w:'RS' not in w,'B':lambda w:'BC' not in w,'C':lambda w:any(x[0]=='R' for x in w),'D':lambda w:any(x[0]=='B' for x in w)}
assert {k:all(fn(w) for w in promised) for k,fn in claims.items()}=={'A':True,'B':False,'C':False,'D':True}
assert min(len(w) for w in promised if not claims['B'](w))==2
assert min(len(w) for w in promised if not claims['C'](w))==1
assert 'RS' in {'RS','RC'} and not (set(['RS','RC'])<=set(['RS','BS','BC']))
assert not ('RS' in {'BS'}) and all(x!='RC' for x in {'BS'})
# Relation-quantifier extension: enumerate all directed relations on 1 or 2 vertices.
relation_examples={}
for n in (1,2):
    vv=range(n);good=[]
    for es in subsets(it.product(vv,repeat=2)):
        if all(any((a,b) in es for b in vv) for a in vv) and not any(all((a,b) in es for a in vv) for b in vv):good.append(es)
    relation_examples[n]=len(good)
assert relation_examples[1]==0 and relation_examples[2]>0
audit('AD-01',dict(world_types_checked=len(worlds),worlds_meeting_page2_promises=len(promised),forced_claims=['A','D'],minimum_counterworld_sizes={'prompt1':2,'B':2,'C':1},arrow_countermodel_counts=relation_examples))

# AD-02: all ordered four-row lists, including repetitions.
words=list(it.product((0,1),repeat=4));checked=0
for rows in it.product(words,repeat=4):
    b=tuple(1-rows[i][i] for i in range(4))
    assert b not in rows and all(b[i]!=rows[i][i] for i in range(4))
    checked+=1
rows=F['AD-02']['figures']['rows']; answer=''.join(str(1-int(rows[i][i])) for i in range(4))
assert answer=='1000'
# All 24 alternative row-to-coordinate bijections on the displayed instance.
for perm in it.permutations(range(4)):
    b=[None]*4
    for row,pos in enumerate(perm):b[pos]=str(1-int(rows[row][pos]))
    assert ''.join(b) not in rows
assert len({a+b for a in ['00','01','10','11'] for b in ['00','01','10','11']})==16
audit('AD-02',dict(binary_four_row_lists_checked=checked,displayed_diagonal_answer=answer,position_assignments_checked=24,complete_four_bit_collection_size=16,infinite_claim='Written arbitrary-index proof, not a finite test.'))

# AD-03: every collection of the sixteen subsets, including empty/full cards.
S=subsets('ABCD');acs=[c for c in subsets(S) if antichain(c)]
assert max(map(len,acs))==6
assert max(len(c) for c in acs if frozenset('A') in c)==4
assert max(len(c) for c in acs if len({len(x) for x in c})>1)==4
chain_text=[['','A','AB','ABC','ABCD'],['B','BC','BCD'],['C','AC','ACD'],['D','AD','ABD'],['BD'],['CD']]
chains=[[frozenset(x) for x in c] for c in chain_text]
flat=[x for c in chains for x in c]
assert len(flat)==16 and set(flat)==set(S)
assert all(all(a<b for a,b in zip(c,c[1:])) for c in chains)
small_chains=[['B','BC','BCD'],['C','CD'],['D','BD']]
assert {frozenset(x) for c in small_chains for x in c}==set(subsets('BCD'))-{frozenset()}
# Check complement reverses containment for all pairs.
U=frozenset('ABCD')
assert all((a<=b)==((U-b)<=(U-a)) for a,b in it.product(S,repeat=2))
audit('AD-03',dict(collections_checked=2**16,antichains=len(acs),maximum=6,maximum_with_A=4,maximum_mixed_card_sizes=4,chain_certificate=chain_text,three_symbol_chain_certificate=small_chains,five_symbol_counting_bound={'largest_binomial':10,'permutations':120}))

# AD-04: independently enumerate trees as edge subsets and compare all code words.
counts={}
for n in range(2,7):
    vs=list(range(1,n+1));E=list(it.combinations(vs,2))
    trees={norm(es) for es in it.combinations(E,n-1) if tree(vs,es)}
    words=list(it.product(vs,repeat=n-2));decoded=set()
    for msg in words:
        es=decode(vs,msg);assert tree(vs,es);assert encode(vs,es)==msg
        assert Counter(v for e in es for v in e)==Counter({v:msg.count(v)+1 for v in vs})
        decoded.add(es)
    assert decoded==trees and len(trees)==n**(n-2)
    assert all(decode(vs,encode(vs,es))==es for es in trees)
    counts[n]=len(trees)
assert encode([1,2,3,4],[(1,2),(1,3),(3,4)])==(1,3)
assert encode([1,2,3,4],[(1,3),(2,3),(2,4)])==(3,2)
assert decode([1,2,3,4],(3,1))==norm([(2,3),(1,3),(1,4)])
assert decode([1,2,3,4,5],(4,4,2))==norm([(1,4),(3,4),(2,4),(2,5)])
assert decode([1,2,3,4,5],(1,2,3))==norm([(1,4),(1,2),(2,3),(3,5)])
assert encode([1,2,3,4],[(1,2),(1,3),(3,4)],largest=True)==(3,1)
audit('AD-04',dict(exhaustive_tree_and_code_counts=counts,degree_occurrence_identity='Every enumerated tree',general_claim='Written inductive inverse proof, not extrapolation.'))

# AD-05: enumerate all edge subsets, closures, added-road cases, cofactors and minors.
vs=list('ABCD');E=F['AD-05']['figures']['edges'];trees=[norm(es) for es in subsets(map(tuple,E)) if tree(vs,es)]
assert len(trees)==8
uses={''.join(e):sum(tuple(sorted(e)) in es for es in trees) for e in E}
assert uses=={'AB':5,'BC':5,'CD':5,'DA':5,'AC':4}
L=laplacian(vs,E);cofactors=[det(cofactor(L,k)) for k in range(4)]
assert cofactors==[8]*4 and det(L)==0
K=E+[['B','D']];treesK=[norm(es) for es in subsets(map(tuple,K)) if tree(vs,es)]
bydiag=Counter(sum(e in es for e in [('A','C'),('B','D')]) for es in treesK)
assert dict(bydiag)=={0:4,1:8,2:4}
assert all(sum(tuple(sorted(e)) in es for es in treesK)==8 for e in K)
B=[[0]*5 for _ in range(3)]
for j,(a,b) in enumerate(E):
    if a!='D':B[vs.index(a)][j]=-1
    if b!='D':B[vs.index(b)][j]=1
minor_squares=[]
for cols in it.combinations(range(5),3):
    v=det([[row[j] for j in cols] for row in B]);is_tree=tree(vs,[E[j] for j in cols])
    assert v*v==int(is_tree);minor_squares.append(v*v)
assert sum(minor_squares)==8
audit('AD-05',dict(original_trees=[[''.join(e) for e in es] for es in trees],edge_appearances=uses,closure_survivors={e:8-v for e,v in uses.items()},K4_trees=len(treesK),K4_by_number_of_diagonals=dict(bydiag),laplacian=L,principal_cofactors=cofactors,full_determinant=det(L),incidence_minor_squares=minor_squares))

# AD-06: exhaustive pair bounds and distributivity tests.
ss=subsets('ABC')
assert all(x&(y|z)==(x&y)|(x&z) for x,y,z in it.product(ss,repeat=3))
d=F['AD-06']['figures']['diamond'];vs=d['vertices'];rel=order_closure(vs,d['covers'])
J={(a,b):bounds(vs,rel,a,b) for a,b in it.product(vs,repeat=2)}
M={(a,b):bounds(vs,rel,a,b,False) for a,b in it.product(vs,repeat=2)}
assert None not in J.values() and None not in M.values()
fail=[(x,y,z) for x,y,z in it.product(vs,repeat=3) if M[x,J[y,z]]!=J[M[x,y],M[x,z]]]
assert set(fail)==set(it.permutations('abc'))
bow=F['AD-06']['figures']['nonlattice'];vv=bow['vertices'];rr=order_closure(vv,bow['covers'])
assert bounds(vv,rr,'p','q') is None and bounds(vv,rr,'r','s',False) is None
for arrow in [('r','s'),('s','r')]:
    repaired=order_closure(vv,bow['covers']+[list(arrow)])
    assert all(bounds(vv,repaired,a,b) is not None and bounds(vv,repaired,a,b,False) is not None for a,b in it.product(vv,repeat=2))
audit('AD-06',dict(set_triples_checked=8**3,diamond_pairs_checked=25,diamond_triples_checked=125,distributivity_counterexamples=fail,nonlattice_failures=['join(p,q)','meet(r,s)'],single_comparison_repairs_checked=2))

# AD-07: branch over every legal addition order for every start.
fg=F['AD-07']['figures'];tokens=fg['tokens'];rules=[(frozenset(r['inputs']),r['output']) for r in fg['rules']]
def runs(s):
    nxt={s|{out} for ins,out in rules if ins<=s and out not in s}
    if not nxt:return [(s,)]
    return [(s,)+tail for n in nxt for tail in runs(n)]
allS=subsets(tokens);closures={};run_count=0
for s in allS:
    paths=runs(s);ends={p[-1] for p in paths};assert len(ends)==1
    closures[s]=next(iter(ends));run_count+=len(paths)
    assert all(len(p)<=5-len(s) for p in paths)
closed={s for s in allS if closures[s]==s}
expected={frozenset(s) for s in ('','b','c','cd','ab','bcd','abcd')};assert closed==expected
assert all(s<=closures[s] and closures[closures[s]]==closures[s] for s in allS)
assert all(closures[s]<=closures[t] for s,t in it.product(allS,repeat=2) if s<=t)
assert all(s&t in closed for s,t in it.product(closed,repeat=2))
assert frozenset('ab')|frozenset('c') not in closed
full=frozenset('abcd');gens=[s for s in allS if closures[s]==full]
assert {s for s in gens if len(s)==min(map(len,gens))}=={frozenset('ac'),frozenset('ad')}
audit('AD-07',dict(starts_checked=16,completed_legal_runs_checked=run_count,closed_sets=sorted([''.join(sorted(s)) for s in closed],key=lambda x:(len(x),x)),closures={''.join(sorted(s)):''.join(sorted(t)) for s,t in closures.items()},minimum_generators=['ac','ad'],all_closure_axioms_checked=True,all_closed_intersections_checked=True))

# AD-08: all Bell(4)=15 and Bell(6)=203 set partitions; every representative tuple.
valid={};partition_counts={}
for n in (4,6):
    pp=list(partitions(n));partition_counts[n]=len(pp)
    good=[p for p in pp if compatible(p,n)];valid[n]=[blocks(p) for p in good]
assert partition_counts=={4:15,6:203}
assert len(valid[4])==3 and len(valid[6])==4
expected4={((0,),(1,),(2,),(3,)),((0,2),(1,3)),((0,1,2,3),)}
assert {tuple(map(tuple,p)) for p in valid[4]}==expected4
expected6={((0,),(1,),(2,),(3,),(4,),(5,)),((0,3),(1,4),(2,5)),((0,2,4),(1,3,5)),((0,1,2,3,4,5),)}
assert {tuple(map(tuple,p)) for p in valid[6]}==expected6
machine=fg=F['AD-08']['figures']['extra_operation']
with_machine=[p for p in partitions(4) if compatible(p,4) and all(p[machine[a]]==p[machine[b]] for a,b in it.product(range(4),repeat=2) if p[a]==p[b])]
assert len(with_machine)==2
# Least coarsenings of the displayed repair partitions.
for original,expected in [((0,1,0,2),((0,2),(1,3))),((0,0,1,2),((0,1,2,3),))]:
    candidates=[p for p in partitions(4) if compatible(p,4) and all(p[a]==p[b] for a,b in it.product(range(4),repeat=2) if original[a]==original[b])]
    finest=max(candidates,key=lambda p:len(set(p)))
    assert tuple(map(tuple,blocks(finest)))==expected
audit('AD-08',dict(partitions_checked=partition_counts,valid_addition_partitions=valid,extra_machine_survivors=[blocks(p) for p in with_machine],all_representative_choices_checked=True,least_repairs_checked=2))

RESULTS['status']='all exact checks passed'
RESULTS['scope_note']='General arguments are written in ad1-data.json; these finite audits corroborate exact instances and classifications.'
(HERE/'ad1-checks-results.json').write_text(json.dumps(RESULTS,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':RESULTS['status'],'families':len(F),'student_prompts':sum(prompt_counts.values()),'output':str(HERE/'ad1-checks-results.json')},indent=2))
