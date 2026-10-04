"""Independent review: graph paths and free reduction. No author imports."""
from itertools import combinations
from collections import deque, Counter
import json
from pathlib import Path

def adjacency(edges):
    g={x:set() for e in edges for x in e}
    for x,y in edges:g[x].add(y);g[y].add(x)
    return g
def shortest_reduced_cover(edges):
    g=adjacency(edges); nodes=set(g); q=deque([('H',None,frozenset('H'),'H')]);seen=set()
    while q:
        v,prev,used,path=q.popleft()
        if v=='H' and used==nodes and len(path)>1:return path
        for nxt in sorted(g[v]):
            if nxt==prev:continue
            state=(nxt,v,used|{nxt})
            if state not in seen:seen.add(state);q.append((*state,path+nxt))
    return None
base=[('H',v) for v in 'ABCD']; outer=list(combinations('ABCD',2));sets=[]
for k in range(7):
    for add in combinations(outer,k):
        witness=shortest_reduced_cover(base+list(add))
        if witness:sets.append((k,add,witness))
minimum=min(r[0] for r in sets);assert minimum==2
optimal=[r for r in sets if r[0]==minimum]
assert len(optimal)==3 and all(len(r[2])-1==6 for r in optimal)
assert all(shortest_reduced_cover(base+[e for e in add if e!=removed]) is None for _,add,_ in optimal for removed in add)
assert len(shortest_reduced_cover(base+[('A','B'),('B','C'),('C','D')]))-1==5
def walks(g,n,v='H',word='H'):
    if n==0:
        if v=='H':yield word
    else:
        for nxt in sorted(g[v]):yield from walks(g,n-1,nxt,word+nxt)
def reduce_edges(word):
    stack=[]
    for e in zip(word,word[1:]):
        if stack and stack[-1]==e[::-1]:stack.pop()
        else:stack.append(e)
    return stack
unit=adjacency([('H',v) for v in 'ABC'])
extended=adjacency([('H',v) for v in 'ABC']+[('A','D'),('B','E'),('C','F')])
walk_results={}
for name,g,expected in [('unit',unit,27),('extended',extended,48)]:
    allwalks=list(walks(g,6));assert len(allwalks)==expected
    assert all(not reduce_edges(w) for w in allwalks)
    pattern=Counter(tuple(i-j for j,i in zip([0]+[k for k,x in enumerate(w) if x=='H' and k>0][:-1],[k for k,x in enumerate(w) if x=='H' and k>0])) for w in allwalks)
    walk_results[name]={'count':len(allwalks),'return_patterns':{str(k):v for k,v in pattern.items()},'four_step_count':len(list(walks(g,4)))}
assert walk_results['unit']['four_step_count']==9 and walk_results['extended']['four_step_count']==12
loops={'a':'HLMH','A':'HMLH','b':'HRSH','B':'HSRH'}
def reduce_letters(word):
    out=[]
    for x in word:
        if out and out[-1]==x.swapcase():out.pop()
        else:out.append(x)
    return ''.join(out)
def expand(word):return 'H'+''.join(loops[x][1:] for x in word)
cards=['a','aa','b','ab','abab','abA','abbA'];matching=[]
for a,b in combinations(cards,2):
    left=reduce_letters(a+b);right=reduce_letters(b+a)
    assert (left==right)==(reduce_edges(expand(a+b))==reduce_edges(expand(b+a)))
    if left==right:matching.append((a,b,left))
assert matching==[('a','aa','aaa'),('ab','abab','ababab'),('abA','abbA','abbbA')]
assert reduce_letters('aAb')=='b'
result={'minimal_additions':minimum,'optimal_additions_and_witnesses':optimal,'tree_walks':walk_results,'commuting_pairs':matching,'all_card_pairs_checked':21,'worked_example':{'input':'aAb','output':'b'}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
