from itertools import combinations
from collections import defaultdict
from pathlib import Path
import json
# Independent explicit reconstruction of the replacement drawing.
edges=[('s','A'),('s','B'),('A','B'),('A','C'),('B','C'),('C','D'),('C','E'),('D','E'),('D','t'),('E','t')]
reservation={('s','A'),('A','B'),('B','C'),('C','D'),('D','E'),('E','t')}
def all_routes(es):
    adj=defaultdict(list)
    for a,b in es: adj[a].append(b)
    todo=[('s',('s',),frozenset())]; result=[]
    while todo:
        v,vs,used=todo.pop()
        if v=='t': result.append(used); continue
        todo.extend((w,vs+(w,),used|{(v,w)}) for w in adj[v] if w not in vs)
    return result
routes=all_routes(edges)
collections={k:[c for c in combinations(routes,k) if len(set().union(*c))==sum(map(len,c))] for k in (1,2,3)}
assert len(routes)==9 and len(collections[2])==2 and not collections[3]
assert not all_routes(set(edges)-reservation)
closures=[c for c in combinations(edges,2) if not all_routes(set(edges)-set(c))]
assert closures and all(all_routes(set(edges)-{e}) for e in edges)
residual=[(b,a) if (a,b) in reservation else (a,b) for a,b in edges]
augmentations=all_routes(residual)
assert len(augmentations)==1
cancellations={e for e in reservation if (e[1],e[0]) in augmentations[0]}
assert cancellations=={('A','B'),('D','E')}
# The unaltered exhaustive K-1 board has eight pairs, with eight recording copies.
bowtie=[e for e in edges if e not in {('A','B'),('D','E')}]
bowtie_pairs=[c for c in combinations(bowtie,2) if not all_routes(set(bowtie)-set(c))]
assert len(bowtie_pairs)==8
# Independently check both game winners, including a first/second-player choice.
from functools import lru_cache
@lru_cache(None)
def winning_remaining(es):
    for edge in es:
        remaining=tuple(e for e in es if e!=edge)
        if not all_routes(remaining) or not winning_remaining(remaining):
            return True
    return False
diamond=(('s','A'),('s','B'),('A','t'),('B','t'))
greedy=diamond+(('A','B'),)
assert not winning_remaining(diamond) and winning_remaining(greedy)
winning_openings=[e for e in greedy if not winning_remaining(tuple(x for x in greedy if x!=e))]
assert winning_openings==[('A','B')]
result={'replacement_route_count':len(routes),'maximum_routes':2,'largest_collection_count':len(collections[2]),'minimum_closures':closures,'initial_reserved_route':'s A B C D E t','no_unused_forward_route':True,'required_cancellations':sorted(cancellations),'k1_exhaustive_pairs':len(bowtie_pairs),'k1_game_upper':'second player','k1_game_lower':'first player','k1_game_lower_winning_opening':winning_openings}
Path(__file__).with_name('independent_revision_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
