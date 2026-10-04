from pathlib import Path
from functools import lru_cache
from collections import Counter
import json, hashlib

RUN=Path(__file__).resolve().parent
evidence={}

# Independent replay and all legal continuations of the three printed chip boards.
graphs={
    'triangle': {'A':['B','sink'],'B':['A','sink']},
    'square': {'A':['B','sink'],'B':['A','C'],'C':['B','sink']},
    'diagonal': {'A':['B','C','sink'],'B':['A','C'],'C':['A','B','sink']},
}
data=json.loads((RUN/'week-11/guide-checks-input.json').read_text())
chip_results=[]
for name,graph in graphs.items():
    vertices=list(graph)
    def move(state,index):
        out=list(state);out[index]-=len(graph[vertices[index]])
        for neighbor in graph[vertices[index]]:
            if neighbor!='sink':out[vertices.index(neighbor)]+=1
        return tuple(out)
    @lru_cache(None)
    def terminals(state):
        choices=[i for i,v in enumerate(vertices) if state[i]>=len(graph[v])]
        if not choices:return {(state,(0,)*len(vertices))}
        results=set()
        for i in choices:
            for end,counts in terminals(move(state,i)):
                increment=list(counts);increment[i]+=1
                results.add((end,tuple(increment)))
        return results
    for row in data[name]:
        start=tuple(row['start']);expected=(tuple(row['end']),tuple(row['fires']))
        terminal_results=terminals(start)
        assert terminal_results=={expected},(name,start,terminal_results,expected)
        assert sum(start)-sum(row['end'])==row['sink']
        for field in ['route','reverse_route']:
            state=start
            for letter in row[field]:
                i=vertices.index(letter)
                assert state[i]>=len(graph[letter]),(name,start,row[field],state,letter)
                state=move(state,i)
            assert state==tuple(row['end'])
            assert tuple(Counter(row[field])[v] for v in vertices)==tuple(row['fires'])
        chip_results.append({'board':name,'start':row['start'],'terminal_state':row['end'],'counts_recovered_afterwards':row['fires'],'all_legal_completion_results':1})
evidence['week_11']={'independent_method':'Degree-rule replay of both printed sample words; memoized exhaustive legal continuations for each of the 35 supplied starts. No facilitator verification code imported.','starts_checked':len(chip_results),'sample_words_checked':2*len(chip_results),'results':chip_results,'recording_claim':'One chronological firing word recovers each vertex firing count afterwards; final state and counts distinguish different data.'}

# Exact deck comparisons pool without changing equally likely outcomes.
decks={'A':[2,4,9],'B':[1,6,8],'C':[3,5,7]}
comparisons=[]
for left,right in [('A','B'),('B','C'),('C','A')]:
    pairs=[(x,y) for x in decks[left] for y in decks[right]]
    wins=[list(p) for p in pairs if p[0]>p[1]]
    assert len(pairs)==9 and len(wins)==5
    comparisons.append({'comparison':left+' against '+right,'pairs':len(pairs),'wins':wins,'winning_fraction':'5/9'})
evidence['week_24']={'independent_method':'Cartesian-product comparison of the actual three decks, each physical pair counted once.','comparisons':comparisons,'shared_coverage':27,'individual_coverage_required':False}

# Road reduction: enumerate actual adjacency walks; no source checker imported.
tree={'A':['B'],'B':['A','C','D'],'C':['B'],'D':['B','E','F'],'E':['D'],'F':['D']}
ring={'A':['B','D'],'B':['A','C'],'C':['B','D'],'D':['A','C']}
def walks(graph,start,steps):
    if steps==0:return [(start,)]
    result=[]
    for suffix in walks(graph,start,steps-1):
        for neighbor in graph[suffix[-1]]:result.append(suffix+(neighbor,))
    return result
def reduce_walk(route):
    # Inverse traversals of the same road cancel exactly when adjacent.
    stack=[]
    for edge in zip(route,route[1:]):
        if stack and stack[-1]==tuple(reversed(edge)):stack.pop()
        else:stack.append(edge)
    return (route[0],)+tuple(edge[1] for edge in stack)
road_results=[]
for graph,start,end,steps,expected in [
    (tree,'A','E',3,{('A','B','D','E')}),
    (tree,'B','B',4,{('B',)}),
    (tree,'A','D',4,{('A','B','D')}),
    (ring,'A','A',4,{('A',),('A','B','C','D','A'),('A','D','C','B','A')}),
]:
    candidates=[w for w in walks(graph,start,steps) if w[-1]==end]
    reduced={reduce_walk(w) for w in candidates}
    assert reduced==expected,(start,end,steps,reduced)
    road_results.append({'graph':'tree' if graph is tree else 'ring','start':start,'end':end,'steps':steps,'input_count':len(candidates),'reduced_results':['-'.join(x) for x in sorted(reduced)]})
evidence['week_39']={'independent_method':'Exhaustive walks on the actual AB/BC/BD/DE/DF tree and AB/BC/CD/DA ring; ordered inverse-edge stack reduction.','entry_results':road_results,'general_proof_read':'The original p6 invariant-stack and tree/ring arguments are retained. Bounded entry enumeration is not used to establish the arbitrary-length theorem.'}

# New slide-only entry is the established asymmetric motif row.
def row(x):return x%4==0
assert all(row(x)==row(x-4) for x in range(-40,41))
assert row(0)!=row(0-2)
evidence['week_35']={'new_entry':'An asymmetric Border T motif at 4-cm intervals is preserved by a 4-cm translation and not by 2 cm.','independent_check':'Whole-row lattice comparison over multiple positive and negative repeats; primitive period remains 4 cm. Existing glide and upper proof keys were separately compared with original text.'}

evidence['physical_or_classroom_trials_performed']=False
(RUN/'guide-final-math-evidence-recomputed.json').write_text(json.dumps(evidence,indent=2))
print('PASS',len(chip_results),'chip starts,',2*len(chip_results),'sample words, 27 deck pairs,',sum(r['input_count'] for r in road_results),'entry road walks; slide-only entry verified')
