"""Check the Week 35 footprint motif and write mathematical-checks.json.

Moved unchanged from the end of the old student builder (archived as
archive-before-problem-files-2026-10-23/build_packets.py in the project) when the
pages became problem files. materials/build_materials.py reads the motif from the
JSON this writes. The drawing itself is motif() in the problem files' figures.py.
"""
from pathlib import Path
import json
SRC=Path(__file__).resolve().parent

# Vertex-distance signature and signed area checks distinguish the motif's mirror.
V=[(-1.3,-1.1),(1.3,-1.1),(1.3,-.4),(.8,-.4),(.8,-.65),(-.5,-.65),(-.5,0),(.6,0),(.6,.45),(-.5,.45),(-.5,1.1),(-1.3,1.1)]
# A polygon symmetry must permute vertices preserving the cyclic edge-length word.
l=[round((V[i][0]-V[(i+1)%len(V)][0])**2+(V[i][1]-V[(i+1)%len(V)][1])**2,8) for i in range(len(V))]
rot=[k for k in range(1,len(V)) if all(l[i]==l[(i+k)%len(V)] for i in range(len(V)))]
ref=[k for k in range(len(V)) if all(l[i]==l[(k-i)%len(V)] for i in range(len(V)))]
assert not rot and not ref
(SRC/'mathematical-checks.json').write_text(json.dumps({'motif_vertices':V,'nonidentity_cyclic_edge_word_rotations':rot,'edge_word_reflections':ref,'note':'No polygon isometry can exist without preserving the cyclic edge-length word. All motifs are original.'},indent=2))
