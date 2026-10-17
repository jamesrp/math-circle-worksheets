"""Finite checks for the Week 88--90 planning examples; no PDF authoring."""
import itertools
import json
import math
from pathlib import Path


def cells(shape):
    return {(r + 1, c + 1) for r, width in enumerate(shape) for c in range(width)}


def corners(shape_cells):
    return sorted(p for p in shape_cells if (p[0]+1, p[1]) not in shape_cells and (p[0], p[1]+1) not in shape_cells)


def increasing(table):
    return all(table[p] < table[q] for p in table for q in ((p[0]+1,p[1]),(p[0],p[1]+1)) if q in table)


def slide(outer, inner, table, start):
    assert start in corners(inner)
    outer, inner, table = set(outer), set(inner), dict(table)
    inner.remove(start)
    hole, path = start, [start]
    while True:
        choices = [p for p in ((hole[0],hole[1]+1),(hole[0]+1,hole[1])) if p in table]
        if not choices:
            break
        next_cell = min(choices, key=table.get)
        table[hole] = table.pop(next_cell)
        hole = next_cell
        path.append(hole)
    assert hole in corners(outer)
    outer.remove(hole)
    assert set(table) == outer - inner and increasing(table)
    return outer, inner, table, path


def rectifications(outer, inner, table, starts=(), paths=()):
    if not inner:
        return [{"starts": starts, "paths": paths, "result": sorted(table.items())}]
    results = []
    for start in corners(inner):
        new_outer,new_inner,new_table,path = slide(outer,inner,table,start)
        results.extend(rectifications(new_outer,new_inner,new_table,starts+(start,),paths+(path,)))
    return results


def all_tableaux(outer_shape, inner_shape):
    outer, inner = cells(outer_shape),cells(inner_shape)
    positions = sorted(outer-inner)
    answer=[]
    for values in itertools.permutations(range(1,len(positions)+1)):
        table=dict(zip(positions, values))
        if increasing(table):
            rects=rectifications(outer,inner,table)
            assert len({repr(r["result"]) for r in rects})==1
            answer.append({"start":sorted(table.items()),"rectifications":rects})
    return answer


def differences(row):
    answer=[row]
    while len(row)>1:
        row=[b-a for a,b in zip(row,row[1:])]
        answer.append(row)
    return answer


report={}
d=40
tray=[(20+40*k,20) for k in range(4)]+[(40+40*k,20+20*math.sqrt(3)) for k in range(3)]+[(20+40*k,20+40*math.sqrt(3)) for k in range(4)]
assert all(20-1e-9<=x<=140+1e-9 and 20-1e-9<=y<=90+1e-9 for x,y in tray)
assert all(math.dist(a,b)>=40-1e-9 for a,b in itertools.combinations(tray,2))
report["packing"]={"tray_160_by_110_11_disk_centers_mm":tray,"height_mm":40+40*math.sqrt(3),"kissing_equal":6}
report["packing"]["unequal_equal_outer_rings"]={}
for R,r in [(20,20),(40,20),(20,40)]:
    minimum_angle=2*math.asin(r/(R+r))
    max_number=math.floor(2*math.pi/minimum_angle+1e-10)
    assert 2*(R+r)*math.sin(math.pi/max_number)>=2*r-1e-9
    report["packing"]["unequal_equal_outer_rings"][f"central_radius_{R}_outer_radius_{r}"]={"minimum_angle_degrees":math.degrees(minimum_angle),"maximum":max_number}
report["growth"]={name:differences(row) for name,row in {
    "squares":[n*n for n in range(6)],
    "stairs":[n*(n+1)//2 for n in range(6)],
    "rectangles":[n*(n+1) for n in range(6)],
    "cubes":[n**3 for n in range(6)],
    "two_rules_first_four":[n*n+math.comb(n-1,4) if n>=5 else n*n for n in range(1,7)]
}.items()}
input_row=[2,0,1,0,2]
first=list(itertools.accumulate(input_row))
second=list(itertools.accumulate(first))
assert first==[2,2,3,3,5] and second==[2,4,7,10,15]
report["growth"]["cascade"]={"input":input_row,"first":first,"second":second}
orders=set(itertools.permutations(input_row))
last_totals={order:sum(itertools.accumulate(order)) for order in orders}
assert len(orders)==30 and min(last_totals.values())==9 and max(last_totals.values())==21
report["growth"]["cascade_extrema"]={"distinct_orders":len(orders),"minimum":9,"maximum":21}
for n in range(1,7):
    assert sum(1 for i in range(n) for j in range(n) for k in range(n) if i+j+k<=n-1)==math.comb(n+2,3)
report["tableaux"]={}
for name,outer_shape,inner_shape in [("single_hole",(3,2),(1,)),("five_labels",(3,3,2),(2,1)),("diagonal_three",(3,2,1),(2,1))]:
    tabs=all_tableaux(outer_shape,inner_shape)
    grouped={}
    for tab in tabs:
        key=repr(tab["rectifications"][0]["result"])
        grouped[key]=grouped.get(key,0)+1
    report["tableaux"][name]={"count":len(tabs),"catalog":tabs,"result_multiplicities":grouped}
assert report["tableaux"]["single_hole"]["count"]==5
assert report["tableaux"]["five_labels"]["count"]==16
assert report["tableaux"]["diagonal_three"]["count"]==6
for table in [{(1,2):1,(1,3):4,(2,1):2,(2,2):3},{(1,2):2,(1,3):3,(2,1):1,(2,2):4},{(1,2):1,(1,3):2,(2,1):3,(2,2):4},{(1,3):2,(2,2):1,(2,3):4,(3,1):3,(3,2):5}]:
    assert increasing(table)
for tab in report["tableaux"]["single_hole"]["catalog"]:
    start=dict((tuple(p),v) for p,v in tab["start"])
    rect=tab["rectifications"][0]
    final=dict((tuple(p),v) for p,v in rect["result"])
    hole=tuple(rect["paths"][0][-1])
    while hole!=(1,1):
        neighbors=[p for p in ((hole[0]-1,hole[1]),(hole[0],hole[1]-1)) if p in final]
        source=max(neighbors,key=final.get)
        final[hole]=final.pop(source)
        hole=source
    assert final==start
out=Path(__file__).with_name("growth-math-data.json")
out.write_text(json.dumps(report,indent=2)+"\n")
print("PASS: tray construction; ring bounds 6,9,4; signed differences and cascade; all legal rectifications for 5 + 16 + 6 increasing tableaux.")
print(out)
