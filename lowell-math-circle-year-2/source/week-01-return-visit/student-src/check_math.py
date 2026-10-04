"""Independent finite checks for the writer's three mathematical kernels.

This is writer-stage verification data, not an adult facilitator guide.
Axial lattice coordinates (a,b) mean Cartesian (a+b/2, sqrt(3)*b/2).
No answers or complete enumerations are printed in the student packet.
"""
from itertools import product, combinations
from collections import Counter
from pathlib import Path
import json

DIRECTIONS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))

def signed_triangle_area(vertices):
    return sum(a*d-b*c for (a,b),(c,d) in zip(vertices, vertices[1:]+vertices[:1]))

def inside(point, polygon):
    x,y=point
    return all((c-a)*(y-b)-(d-b)*(x-a) >= -1e-8
               for (a,b),(c,d) in zip(polygon, polygon[1:]+polygon[:1]))

def edges(triangle):
    return {tuple(sorted(edge)) for edge in zip(triangle,triangle[1:]+triangle[:1])}

def triangles_in(polygon):
    result=[]
    for a,b in product(range(-5,8),repeat=2):
        for triangle in (((a,b),(a+1,b),(a,b+1)),
                         ((a+1,b),(a+1,b+1),(a,b+1))):
            centroid=tuple(sum(v[i] for v in triangle)/3 for i in (0,1))
            if inside(centroid,polygon): result.append(triangle)
    return result

def inventory_example(polygon):
    triangles=triangles_in(polygon)
    assert len(triangles)==10
    neighboring_pairs=[(i,j) for i,j in combinations(range(10),2)
                       if edges(triangles[i]) & edges(triangles[j])]
    rhombi=next((p,q) for p,q in combinations(neighboring_pairs,2) if not set(p)&set(q))
    groups=[list(pair) for pair in rhombi]
    paired={v for pair in rhombi for v in pair}
    groups += [[i] for i in range(10) if i not in paired]
    block_edges=[]
    for group in groups:
        counts=Counter(edge for i in group for edge in edges(triangles[i]))
        block_edges.append({edge for edge,count in counts.items() if count==1})
    counts=Counter(edge for block in block_edges for edge in block)
    perimeter=sum(count==1 for count in counts.values())
    shared=sum(count==2 for count in counts.values())
    assert perimeter==26-2*shared
    assert len(groups)==8
    return {"perimeter":perimeter,"full_sides_shared":shared,
            "triangle_cells":triangles,"block_cell_groups":groups}

# Convex compact hexagon, successive side lengths 2,1,1,2,1,1.
compact=inventory_example([(0,0),(2,0),(2,1),(1,2),(-1,2),(-1,1)])
# Strip of five unit rhombi, two retained as rhombi and three split into triangles.
stretched=inventory_example([(0,0),(5,0),(5,1),(0,1)])
assert compact["perimeter"]==8
assert stretched["perimeter"]==12

# Any edge-connected arrangement of eight blocks has >=7 shared sides:
# sum of the individual boundaries 6*3+2*4 = 26, hence perimeter <=12.
# It has even perimeter. A boundary of <=6 unit edges cannot enclose 10
# elementary triangles: exhaustive closed lattice walks have max area 6.
max_area={}
for length in range(1,7):
    largest=0
    for moves in product(DIRECTIONS,repeat=length):
        vertices=[(0,0)]
        for a,b in moves:
            x,y=vertices[-1]
            vertices.append((x+a,y+b))
        if vertices[-1] != (0,0): continue
        largest=max(largest,abs(signed_triangle_area(vertices[:-1])))
    max_area[length]=largest
assert max_area[6]==6

# Around a point, each green corner takes one 60-degree sector; each blue
# corner takes one or two. All allowed mixes are realizable as radial fans
# of unit-edge wedges; this check enumerates the necessary sector equation.
corner_mixes=[]
for green,blue in product(range(7),repeat=2):
    obtuse=6-green-blue
    if 0 <= obtuse <= blue:
        corner_mixes.append({"green":green,"blue":blue,"obtuse_blue_corners":obtuse})
assert len(corner_mixes)==16

# A regular one-unit-side hexagon is six elementary triangle sectors. A blue rhombus
# is an adjacent pair. Tilings therefore correspond to matchings of C6.
tilings=[]
for bits in product((0,1),repeat=6):
    selected={i for i,v in enumerate(bits) if v}
    if any((i+1)%6 in selected for i in selected): continue
    matching_turns=[k for k in range(1,6) if {(i+k)%6 for i in selected}==selected]
    tilings.append({"blue_pairs_start_at_sector":sorted(selected),
                    "matching_turns_in_clockwise_steps":matching_turns})
assert len(tilings)==18
assert {tuple(t["matching_turns_in_clockwise_steps"]) for t in tilings} == {
    (), (3,), (2,4), (1,2,3,4,5)}

checks={"problem_1":{"fixed_inventory":{"green":6,"blue":2},
          "minimum_boundary":8,"maximum_boundary":12,
          "compact_example":compact,"stretched_example":stretched,
          "maximum_enclosed_triangle_area_by_closed_unit_walk_length":max_area},
        "problem_2":{"realizable_corner_mixes":corner_mixes,"number_of_mixes":16},
        "problem_3":{"unit_hexagon_tilings":tilings,"number_of_tilings":18,
          "possible_nonidentity_turn_sets":[[],[3],[2,4],[1,2,3,4,5]]},
        "limits":"Digital mathematical checks only. Tabletop rehearsal and classroom piloting are untested."}
output=Path(__file__).resolve().parent.parent / "render" / "mathematical-checks.json"
output.parent.mkdir(exist_ok=True)
output.write_text(json.dumps(checks,indent=2)+"\n")
print(f"Verified boundary 8..12, 16 corner mixes, and 18 unit-hexagon tilings; data at {output}")
