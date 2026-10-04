#!/usr/bin/env python3
"""Independently recover incidences and face angles of small closed solids."""
from collections import Counter
from itertools import combinations, product
from math import acos, degrees, sqrt, isclose
from pathlib import Path
import json

def check(name, vertices, faces, expected):
    edges = Counter()
    angles = [0.0] * len(vertices)
    for face in faces:
        for i, v in enumerate(face):
            before, after = face[i-1], face[(i+1) % len(face)]
            edges[tuple(sorted((v, after)))] += 1
            a = [vertices[before][j]-vertices[v][j] for j in range(3)]
            b = [vertices[after][j]-vertices[v][j] for j in range(3)]
            dot = sum(x*y for x,y in zip(a,b))
            lengths = sqrt(sum(x*x for x in a) * sum(x*x for x in b))
            angles[v] += degrees(acos(max(-1, min(1, dot/lengths))))
    assert set(edges.values()) == {2}, (name, edges)
    counts = (len(vertices), len(edges), len(faces))
    assert counts == expected, (name, counts, expected)
    assert counts[0]-counts[1]+counts[2] == 2
    defects = [360-a for a in angles]
    assert isclose(sum(defects), 720, abs_tol=1e-8)
    assert all(d > 0 for d in defects)
    return dict(name=name, vertices=vertices, faces=faces, V=counts[0], E=counts[1], F=counts[2],
                edge_incidence=2, defects_degrees=[round(d,8) for d in defects],
                total_defect_degrees=round(sum(defects),8))

tetra = [(1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1)]
cube = list(product((0,1), repeat=3))
index = {v:i for i,v in enumerate(cube)}
cube_faces = []
for axis in range(3):
    other = [a for a in range(3) if a != axis]
    for value in (0,1):
        face=[]
        for p,q in ((0,0),(1,0),(1,1),(0,1)):
            v=[0,0,0]; v[axis]=value; v[other[0]]=p; v[other[1]]=q
            face.append(index[tuple(v)])
        cube_faces.append(face)
octa=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
octa_faces=list(product((0,1),(2,3),(4,5)))
prism=[(0,0,0),(1,0,0),(.5,sqrt(3)/2,0),(0,0,1),(1,0,1),(.5,sqrt(3)/2,1)]
pyramid=[(0,0,0),(1,0,0),(1,1,0),(0,1,0),(.5,.5,sqrt(.5))]
models=[
    check('regular tetrahedron',tetra,list(combinations(range(4),3)),(4,6,4)),
    check('cube',cube,cube_faces,(8,12,6)),
    check('regular octahedron',octa,octa_faces,(6,12,8)),
    check('right equilateral triangular prism',prism,[(0,1,2),(3,4,5),(0,1,4,3),(1,2,5,4),(2,0,3,5)],(6,9,5)),
    check('square pyramid with equilateral sides',pyramid,[(0,1,2,3),(0,1,4),(1,2,4),(2,3,4),(3,0,4)],(5,8,5)),
    check('cube with each face diagonally subdivided',cube,
          [t for f in cube_faces for t in ((f[0],f[1],f[2]),(f[0],f[2],f[3]))],(8,18,12)),
]
regular_candidates=[(n,q) for n in range(3,21) for q in range(3,21) if q*(n-2) < 2*n]
assert regular_candidates == [(3,3),(3,4),(3,5),(4,3),(5,3)]
out={'method':'Edges reconstructed from face cycles; face angles independently computed from 3D coordinates.',
     'models':models,'regular_candidates_n_q':regular_candidates,'status':'mathematical examples checked; physical fit and piloting unperformed'}
Path(__file__).with_name('kernel-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('Verified six closed sphere models, all edge incidences and defect totals; five regular local candidates.')
