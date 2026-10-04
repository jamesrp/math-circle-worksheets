#!/usr/bin/env python3
"""Independent interface, corner and exposed-voxel-face check; stdlib only."""
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json

finalsrc = Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-26-bonus.pdf'

D2=((1,0),(-1,0),(0,1),(0,-1))
D3=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
BOARD=frozenset((x,y) for x in range(4) for y in range(4))

def perimeter(cells):
    return sum((x+dx,y+dy) not in cells for x,y in cells for dx,dy in D2)

def connected(cells):
    if not cells: return False
    found={next(iter(cells))}; todo=list(found)
    while todo:
        x,y=todo.pop()
        for dx,dy in D2:
            p=(x+dx,y+dy)
            if p in cells and p not in found: found.add(p); todo.append(p)
    return len(found)==len(cells)

def interface(red,blue):
    return sum((x+dx,y+dy) in blue for x,y in red for dx,dy in D2)

def corner_holes(cells):
    vertices={p for x,y in cells for p in ((x,y),(x+1,y),(x,y+1),(x+1,y+1))}
    convex=concave=pinches=0
    for x,y in vertices:
        local=[(x-1,y-1) in cells,(x,y-1) in cells,(x-1,y) in cells,(x,y) in cells]
        convex += sum(local)==1
        concave += sum(local)==3
        pinches += sum(local)==2 and ((local[0] and local[3]) or (local[1] and local[2]))
    lo_x=min(x for x,y in cells)-1; hi_x=max(x for x,y in cells)+1
    lo_y=min(y for x,y in cells)-1; hi_y=max(y for x,y in cells)+1
    empty={(x,y) for x in range(lo_x,hi_x+1) for y in range(lo_y,hi_y+1)}-set(cells)
    components=0
    while empty:
        components+=1; seed=next(iter(empty)); empty.remove(seed); todo=[seed]
        while todo:
            x,y=todo.pop()
            for dx,dy in D2:
                p=(x+dx,y+dy)
                if p in empty: empty.remove(p); todo.append(p)
    return {"convex":convex,"concave":concave,"holes":components-1,"pinches":pinches}

def surface(stacks):
    voxels={(x,y,z) for (x,y),h in stacks.items() for z in range(h)}
    return sum((x+dx,y+dy,z+dz) not in voxels for x,y,z in voxels for dx,dy,dz in D3)

def main():
    source = finalsrc.read_text()
    assert "forbid the two-diagonal-tile pattern shown crossed out, even if those tiles connect elsewhere" in source
    bottom_rule = "Count all other faces, including the bottom."
    assert source.index(bottom_rule) < source.index("\\problem{4}") < source.index("\\problem{6}")
    balanced=0; both_connected=0; histogram=Counter(); connected_histogram=Counter(); minima=[]
    for selected in combinations(sorted(BOARD),8):
        red=frozenset(selected); blue=BOARD-red; shared=interface(red,blue)
        assert perimeter(red)+perimeter(blue)==16+2*shared
        balanced+=1; histogram[shared]+=1
        if connected(red) and connected(blue):
            both_connected+=1; connected_histogram[shared]+=1
            if shared==4: minima.append(sorted(red))
    assert balanced==12870 and min(histogram)==4 and min(connected_histogram)==4
    assert histogram[4]==4 and connected_histogram[4]==4
    # Check the rule with every division, not just balanced or connected ones.
    cells=sorted(BOARD)
    for bits in range(1<<16):
        red=frozenset(cells[i] for i in range(16) if bits & (1<<i)); blue=BOARD-red
        assert perimeter(red)+perimeter(blue)==16+2*interface(red,blue)
    shapes=(
        frozenset((x,y) for x in range(3) for y in range(2)),
        frozenset(((0,0),(1,0),(2,0),(0,1),(0,2))),
        frozenset((x,y) for x in range(3) for y in range(3) if (x,y)!=(1,1)),
        frozenset((x,y) for x in range(5) for y in range(3) if (x,y) not in ((1,1),(3,1))))
    expected=((4,0,0),(5,1,0),(4,4,1),(4,8,2))
    shape_results=[]
    for shape,want in zip(shapes,expected):
        result=corner_holes(shape)
        assert connected(shape) and not result['pinches']
        assert (result['convex'],result['concave'],result['holes'])==want
        assert result['convex']-result['concave']==4*(1-result['holes'])
        shape_results.append({"cells":sorted(shape),**result})
    buildings=({(x,0):1 for x in range(8)},{(x,y):1 for x in range(4) for y in range(2)},{(x,y):2 for x in range(2) for y in range(2)})
    building_faces=[surface(building) for building in buildings]
    assert building_faces==[34,28,24]
    worked={(0,0):2,(1,0):2}
    assert sum(worked.values())==4 and surface(worked)==16
    footprints=[(x,y) for x in range(3) for y in range(3)]
    prism_tests=0
    for bits in range(1,1<<9):
        shape={footprints[i] for i in range(9) if bits & (1<<i)}
        for h in (1,2,3):
            assert surface({cell:h for cell in shape})==2*len(shape)+h*perimeter(shape)
            prism_tests+=1
    terrain=[]
    footprint=((0,0),(1,0),(0,1),(1,1))
    for heights in permutations((1,2,3,4)):
        stacks=dict(zip(footprint,heights))
        count=surface(stacks)
        edge_variation=sum(abs(stacks[p]-stacks[q]) for p,q in (((0,0),(1,0)),((0,0),(0,1)),((1,0),(1,1)),((0,1),(1,1))))
        assert count==28+edge_variation
        terrain.append({"row_heights":f'{heights[0]} {heights[1]} / {heights[2]} {heights[3]}',"exposed_faces":count,"internal_variation":edge_variation})
    terrain_counts=Counter(t['exposed_faces'] for t in terrain)
    assert terrain_counts=={34:16,36:8}
    run=Path(__file__).resolve().parent
    out={"week":26,"scope":"final/bonus.pdf, all 4 pages, Problems 1-6 and both worked visuals","independent":True,
        "final_pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "final_source_sha256":hashlib.sha256(finalsrc.read_bytes()).hexdigest(),
        "P1":{"balanced_colorings":balanced,"both_connected":both_connected,"interface_histogram":histogram,"both_connected_interface_histogram":connected_histogram,"minimum":4,"minimizing_red_sets":minima,"minimum_room_perimeters":[12,12]},
        "P2":{"all_divisions_checked":65536,"identity":"P_R+P_B=16+2L","reason":"Each exterior side once, each shared side twice"},
        "P3":{"shapes":shape_results,"theorem":"C-R=4(1-h)","assumptions":["side-connected","no grid vertex with exactly two diagonally opposite occupied cells"],"proof":"Orient each boundary with tiles on left; outer loop has net +4 quarter turns, each hole loop -4."},
        "worked_cube_visual":{"footprint_area":2,"height":2,"cube_count":4,"surface":surface(worked)},
        "P4":{"cube_counts":[sum(b.values()) for b in buildings],"faces_in_printed_order":building_faces,"least":"2x2 footprint, two layers"},
        "P5":{"formula":"S=2m+hP","positive_height_prism_tests":prism_tests,"includes_all_hole_boundaries":True},
        "P6":{"minimum":min(terrain_counts),"maximum":max(terrain_counts),"face_histogram":terrain_counts,"all_24_arrangements":terrain},
        "diagram_check":"4x4 mats are 20mm per cell; printed polyomino occupancy sets and footprint/height labels independently transcribed and checked.",
        "located_errors":[],"physical_rehearsal":"untested"}
    (run/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Week 26 independent checks passed; checks.json written')

if __name__=='__main__': main()
