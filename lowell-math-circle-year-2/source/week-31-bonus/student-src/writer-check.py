#!/usr/bin/env python3
from pathlib import Path
from math import gcd
import json
def vis(a,b,c):return gcd(abs(a-c),b)==1
rows={str(b):['B' if vis(a,b,0) and vis(a,b,1) else '1' if vis(a,b,0) or vis(a,b,1) else '0' for a in range(7)] for b in (3,6)}
assert rows=={'3':['1','1','B','1','1','B','1'],'6':['1','1','1','0','0','1','1']}
assert all(vis(a,4,0) or vis(a,4,1) for a in range(-100,101))
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
triangles={'A':[(0,0),(1,0),(0,1)],'B':[(0,0),(1,2),(3,1)],'C':[(0,0),(2,0),(0,2)],'D':[(0,0),(2,1),(1,1)]}
triangle_results={}
for name,t in triangles.items():
    inside=[];boundary=[]
    for x in range(4):
        for y in range(4):
            p=(x,y)
            if p in t:continue
            signs=[cross(t[i],t[(i+1)%3],p) for i in range(3)]
            if all(v>0 for v in signs) or all(v<0 for v in signs):inside.append(p)
            elif (all(v>=0 for v in signs) or all(v<=0 for v in signs)) and 0 in signs:boundary.append(p)
    triangle_results[name]={'area':abs(cross(*t))/2,'interior':inside,'extra_boundary':boundary}
assert triangle_results['B']['interior']==[(1,1),(2,1)]
assert triangle_results['C']['extra_boundary']==[(0,1),(1,0),(1,1)]
assert triangle_results['A']['area']==triangle_results['D']['area']==.5
row=[(1,0),(0,1)]
while True:
    new=[row[0]];changed=False
    for u,v in zip(row,row[1:]):
        s=(u[0]+v[0],u[1]+v[1])
        if max(s)<=6:new.append(s);changed=True
        new.append(v)
    row=new
    if not changed:break
expected={(a,b) for a in range(1,7) for b in range(1,7) if gcd(a,b)==1}
assert expected<=set(row)
assert (4,3) in row and (3,4) in row and (4,2) not in row
assert all(gcd(a,b)==1 for a,b in row)
assert all(u[0]*v[1]-u[1]*v[0]==1 for u,v in zip(row,row[1:]))
report={'lookout_rows':rows,'triangles':triangle_results,'all_positive_primitive_directions_up_to_6_reached':len(expected),'final_growth_row':row,'worked_example_sum':[3,2]}
(Path(__file__).resolve().parent.parent/'writer-check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
