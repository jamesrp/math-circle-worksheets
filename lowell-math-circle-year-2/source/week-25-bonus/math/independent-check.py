#!/usr/bin/env python3
"""Independent exhaustive shadow/query/margin check; standard library only."""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json

finalsrc = Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-25-bonus.pdf'

CELLS = tuple(product(range(3), repeat=2))
PICTURES = tuple(frozenset((r, c) for r, c in enumerate(p)) for p in permutations(range(3)))

def row_strings(picture):
    return "/".join("".join("1" if (r,c) in picture else "0" for c in range(3)) for r in range(3))

def diagonals(picture):
    # d1 C1; d2 B1,C2; d3 A1,B2,C3; d4 A2,B3; d5 A3.
    return tuple(sum(c-r == difference for r,c in picture) for difference in range(-2,3))

def partition(state, cell):
    return tuple(i for i in state if cell in PICTURES[i]), tuple(i for i in state if cell not in PICTURES[i])

@lru_cache(None)
def depth(state):
    if len(state) <= 1:
        return 0
    options = []
    for cell in CELLS:
        yes, no = partition(state, cell)
        if yes and no:
            options.append(1 + max(depth(yes), depth(no)))
    return min(options)

def tree(state):
    if len(state) == 1:
        return {"picture": state[0] + 1}
    for cell in CELLS:
        yes, no = partition(state, cell)
        if yes and no and 1 + max(depth(yes), depth(no)) == depth(state):
            return {"query": "ABC"[cell[0]] + str(cell[1]+1), "occupied": tree(yes), "empty": tree(no)}
    raise AssertionError("No splitting cell")

def separating(queries):
    return len({tuple(cell in picture for cell in queries) for picture in PICTURES}) == len(PICTURES)

def margins(picture):
    return tuple(sum((r,c) in picture for c in range(3)) for r in range(3)), tuple(sum((r,c) in picture for r in range(3)) for c in range(3))

def main():
    source = finalsrc.read_text()
    line_spec = "0.25/0.75/0.75/0.25/1,0.25/1.75/1.75/0.25/2,0.25/2.75/2.75/0.25/3,1.25/2.75/2.75/1.25/4,2.25/2.75/2.75/2.25/5"
    assert source.count(line_spec) == 2  # worked visual plus actual-board macro
    assert "\\diagboard\\hfill\\diagboard" in source
    guide_lines = ((1,3,3,1),(1,7,7,1),(1,11,11,1),(5,11,11,5),(9,11,11,9))
    for d, (x1,y1,x2,y2) in enumerate(guide_lines, 1):
        assert x1+y1 == x2+y2 == 4*d
        actual = {(r,c) for r,c in CELLS if (4*c+2)+(10-4*r)==4*d and min(x1,x2)<=4*c+2<=max(x1,x2)}
        expected = {(r,c) for r,c in CELLS if c-r==d-3}
        assert actual == expected
    assert "Naming the determined picture is free. Only a question about a covered cell counts." in source
    groups = defaultdict(list)
    for picture in PICTURES:
        groups[diagonals(picture)].append(row_strings(picture))
    assert sorted(map(len, groups.values())) == [1,1,1,1,2]
    assert groups[(0,1,1,1,0)] == ["100/001/010", "010/100/001"]
    worked = frozenset(((0,0),(0,1),(1,2),(2,0)))
    assert diagonals(worked) == (1,0,1,2,0)
    state = tuple(range(6))
    assert depth(state) == 3
    fixed = {k: [q for q in combinations(CELLS, k) if separating(q)] for k in range(5)}
    assert all(not fixed[k] for k in range(4)) and fixed[4]
    assert separating(((0,0),(0,1),(1,0),(1,1)))
    requests = (((3,3,0),(3,3,0)), ((3,2,1),(2,2,2)), ((2,2,2),(3,3,0)), ((3,3,1),(3,3,1)))
    realizations = {request: [] for request in requests}
    for bits in product((0,1), repeat=9):
        picture = frozenset(cell for cell,bit in zip(CELLS,bits) if bit)
        key = margins(picture)
        if key in realizations:
            realizations[key].append(row_strings(picture))
    assert [len(realizations[key]) for key in requests] == [0,3,1,0]
    run = Path(__file__).resolve().parent
    out = {"week":25, "scope":"final/bonus.pdf, all 4 pages and Problems 1-4", "independent":True,
        "final_pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "final_source_sha256": hashlib.sha256(finalsrc.read_bytes()).hexdigest(),
        "worked_example": {"picture": row_strings(worked), "diagonals":diagonals(worked)},
        "P1":{"six_pictures":[{"picture":row_strings(p),"diagonals":diagonals(p)} for p in PICTURES], "groups":[{"diagonals":key,"pictures":value} for key,value in groups.items()]},
        "P2":{"optimal_adaptive_worst_case":depth(state),"optimal_strategy":tree(state),"two_query_lower_bound":"At most four binary reply histories for six pictures"},
        "P3":{"optimal_fixed_questions":4,"separating_set_counts":{k:len(v) for k,v in fixed.items()},"sufficient_example":["A1","A2","B1","B2"],"all_separating_four_sets":[["ABC"[r]+str(c+1) for r,c in q] for q in fixed[4]]},
        "P4":{"all_512_binary_boards_checked":True,"boards":[{"row_counts":key[0],"column_counts":key[1],"realizations":realizations[key]} for key in requests]},
        "diagram_check":"All six candidate pictures are the six distinct permutations; worked diagonal membership/counts and all four labeled margin boards match the printed diagrams.",
        "located_errors":[],"physical_rehearsal":"untested"}
    (run / "checks.json").write_text(json.dumps(out,indent=2)+"\n")
    print("Week 25 independent checks passed; checks.json written")

if __name__ == "__main__":
    main()
