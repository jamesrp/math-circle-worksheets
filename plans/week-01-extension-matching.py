#!/usr/bin/env python3
"""Generate and independently verify the grade 6–7 Hall-deficit reserve board.

Axial coordinates (i,j) are physical (i+j/2, sqrt(3)*j/2).
Uses only the standard library. Writes JSON beside this file.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
import json
from math import sqrt
from pathlib import Path


CELLS = [
    ('A','U',0,0), ('B','U',1,0), ('C','U',0,1),
    ('D','U',0,2), ('E','U',1,2), ('F','U',1,3), ('G','U',2,2),
    ('H','D',0,0), ('I','D',-1,1), ('J','D',0,1),
    ('K','D',-1,2), ('L','D',0,2), ('M','D',1,1), ('N','D',1,2),
]


def vertices(kind,i,j):
    return [(i,j),(i+1,j),(i,j+1)] if kind=='U' else [(i+1,j),(i+1,j+1),(i,j+1)]


def main():
    cells=[{'label':label,'orientation':kind,'i':i,'j':j,
            'vertices':vertices(kind,i,j)} for label,kind,i,j in CELLS]
    by_label={c['label']:c for c in cells}
    adjacency={c['label']:sorted(d['label'] for d in cells
                  if len(set(c['vertices'])&set(d['vertices']))==2) for c in cells}
    visited={'A'};queue=deque(['A'])
    while queue:
        for label in adjacency[queue.popleft()]:
            if label not in visited:
                visited.add(label);queue.append(label)
    assert len(visited)==14
    assert sum(map(len,adjacency.values()))==26  # The adjacency graph is a tree.
    assert Counter(c['orientation'] for c in cells)=={'U':7,'D':7}

    subset=['A','B','F','G']
    neighbors=sorted(set().union(*(set(adjacency[label]) for label in subset)))
    assert neighbors==['H','N'] and len(subset)-len(neighbors)==2

    # Complete search for maximum matching: either leave a selected cell unmatched,
    # or pair it with each side-neighbor. Small enough to verify without libraries.
    @lru_cache(None)
    def maximum_matching(remaining):
        if not remaining:
            return 0
        remaining=set(remaining);label=min(remaining)
        best=maximum_matching(tuple(sorted(remaining-{label})))
        for partner in set(adjacency[label])&remaining:
            best=max(best,1+maximum_matching(tuple(sorted(remaining-{label,partner}))))
        return best
    maximum=maximum_matching(tuple(sorted(by_label)))
    assert maximum==5
    ups=[c['label'] for c in cells if c['orientation']=='U']
    deficits=[]
    for size in range(len(ups)+1):
        for group in combinations(ups,size):
            reachable=set().union(*(set(adjacency[label]) for label in group))
            deficits.append(len(group)-len(reachable))
    assert max(deficits)==2

    packing=[['A','H'],['C','I'],['D','K'],['E','M'],['F','N']]
    used=set()
    for pair in packing:
        x,y=pair
        assert y in adjacency[x]
        assert not used.intersection(pair)
        used.update(pair)
    uncovered=sorted(set(by_label)-used)
    assert uncovered==['B','G','J','L']

    # Confirm that the boundary is a single simple cycle, rather than a region
    # with a hole or pinched point. Each boundary vertex has degree two.
    edge_counts=Counter()
    for cell in cells:
        v=cell['vertices']
        edge_counts.update(tuple(sorted((v[k],v[(k+1)%3]))) for k in range(3))
    boundary=[edge for edge,count in edge_counts.items() if count==1]
    boundary_adj={}
    for x,y in boundary:
        boundary_adj.setdefault(x,[]).append(y)
        boundary_adj.setdefault(y,[]).append(x)
    assert all(len(neighbors)==2 for neighbors in boundary_adj.values())
    start=min(boundary_adj);cycle=[start];previous=None;current=start
    while True:
        candidates=[v for v in boundary_adj[current] if v!=previous]
        nxt=candidates[0]
        if nxt==start:
            break
        cycle.append(nxt);previous,current=current,nxt
    assert len(cycle)==len(boundary_adj)==len(boundary)

    xy=[(i+j/2,j*sqrt(3)/2) for cell in cells for i,j in cell['vertices']]
    width=max(x for x,y in xy)-min(x for x,y in xy)
    height=max(y for x,y in xy)-min(y for x,y in xy)
    assert abs(width-4)<1e-10 and abs(height-2*sqrt(3))<1e-10
    result={
        'title':'Equal totals, four unavoidable green fillers',
        'coordinate_basis':'(i+j/2, sqrt(3)*j/2)',
        'unit_edge_inches':1,
        'width_in_unit_edges':width,'height_in_unit_edges':height,
        'cells':cells,'boundary':cycle,'boundary_edges':boundary,'adjacency':adjacency,
        'up_count':7,'down_count':7,
        'deficient_up_subset':subset,'neighbor_subset':neighbors,'deficit':2,
        'maximum_up_subset_deficit':max(deficits),
        'maximum_blue_rhombi':maximum,'minimum_green_fillers':4,
        'optimal_blue_pairs':packing,'green_cells':uncovered,
        'lower_bound_explanation':
          'A and B can each pair only with H; F and G can each pair only with N. '
          'Thus at least two up cells remain uncovered. Every blue covers one up '
          'and one down cell, and the board starts with seven of each, so the '
          'number of uncovered down cells equals the number of uncovered up cells. '
          'At least four green fillers are therefore necessary; the five-blue '
          'packing attains four.',
        'generalization':
          'For a balanced region with n up and n down cells, any up subset S '
          'with |S|-|N(S)|=d forces at least d up gaps and d down gaps, hence '
          'at least 2d green fillers. The exact minimum is 2 times the maximum '
          'such deficit (including the empty subset). This last equality is '
          'the deficiency form of Hall\'s matching theorem; the elementary '
          'subset argument alone proves the lower bound, not its attainability.',
    }
    out=Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(f'{out}: 7 up + 7 down; maximum 5 blues; minimum 4 greens; '
          f'{width:g} by {height:.6f} unit edges; connected simple boundary verified.')


if __name__=='__main__':
    main()
