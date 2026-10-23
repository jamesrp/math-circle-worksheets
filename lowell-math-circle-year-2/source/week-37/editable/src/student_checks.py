#!/usr/bin/env python3
"""Exact checks of the tetrahedron configurations the Week 37 student pages use.

Moved unchanged from the old student builder (build_packets.py) when the pages became
problem files. Writes mathematical-checks.json.
"""
from pathlib import Path
import itertools,json
SRC=Path(__file__).resolve().parent

# Exact integer regular tetrahedron: all six squared distances are 8.
V=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
def det(a,b,c):return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def orient(q):return det(*[tuple(V[q[i]][j]-V[q[0]][j] for j in range(3)) for i in [1,2,3]])
base=orient((0,1,2,3));rots=[q for q in itertools.permutations(range(4)) if orient(q)==base]
def equivalent(a,b):return any(all(a[i]==b[q[i]] for i in range(4)) for q in rots)
assert len(rots)==12
assert equivalent('ABCD','ADBC')
assert not equivalent('ABCD','ACBD')
assert equivalent('ABCC','ACBC')
assert equivalent('AABC','ABAC')
repeated={}
for i,j in itertools.combinations('ABCD',2):
 a='ABCD'.replace(j,i);b='ACBD'.replace(j,i);repeated[i+j]=equivalent(a,b)
assert all(repeated.values())
(SRC/'mathematical-checks.json').write_text(json.dumps({'regular_integer_vertices':V,'proper_rotations':rots,'proper_rotation_count':12,'true_copy_example':['ABCD','ADBC'],'mirror_pair_not_rotation_equivalent':['ABCD','ACBD'],'repeated_label_pair_equivalent':['ABCC','ACBC'],'all_label_merges_remove_this_pair_chirality':repeated,'physical_pretest_performed':False},indent=2))
