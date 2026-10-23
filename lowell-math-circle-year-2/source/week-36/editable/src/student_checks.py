#!/usr/bin/env python3
"""Exact checks of the nine-tile plane the Week 36 student pages use.

Moved unchanged from the old student builder (build_packets.py) when the pages became
problem files. Writes mathematical-checks.json.
"""
from pathlib import Path
import itertools,json
SRC=Path(__file__).resolve().parent

pts=list(itertools.product(range(3),repeat=2))
def ok(t):return all(len({p[k] for p in t}) in [1,3] for k in [0,1])
lines=[tuple(t) for t in itertools.combinations(pts,3) if ok(t)]
def cap(t):return not any(set(l)<=set(t) for l in lines)
caps={n:sum(cap(t) for t in itertools.combinations(pts,n)) for n in [3,4,5]}
parts=[ls for ls in itertools.combinations(lines,3) if len(set().union(*map(set,ls)))==9]
assert len(lines)==12 and caps[4]==54 and caps[5]==0 and len(parts)==4
# Every maximal legal collection has four tiles; no arbitrary tile ban is used.
maximal_sizes=[]
for n in range(10):
 for t in itertools.combinations(pts,n):
  if cap(t) and not any(cap(t+(p,)) for p in pts if p not in t):maximal_sizes.append(n)
assert set(maximal_sizes)=={4}
(SRC/'mathematical-checks.json').write_text(json.dumps({'lines':lines,'line_free_counts':caps,'partitions_into_three_lines':parts,'maximal_legal_collection_sizes':sorted(set(maximal_sizes))},indent=2))
