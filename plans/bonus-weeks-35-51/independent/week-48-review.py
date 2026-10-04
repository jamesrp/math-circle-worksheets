from fractions import Fraction as F
from pathlib import Path
import json,math
def rect_intersection_area(a,b):
    return max(F(0),min(a[2],b[2])-max(a[0],b[0]))*max(F(0),min(a[3],b[3])-max(a[1],b[1]))
shifts={}
for sx,sy in [(F(0),F(0)),(F(1,2),F(0)),(F(1,2),F(1,2))]:
    areas={}
    for i in range(-2,4):
        for j in range(-2,4):
            cell=(sx+i,sy+j,sx+i+1,sy+j+1)
            area=sum(rect_intersection_area(cell,r) for r in [(0,0,2,1),(1,1,2,2)])
            if area:areas[str((i,j))]=area
    assert sum(areas.values())==3
    shifts[str((sx,sy))]={'inside':sum(a==1 for a in areas.values()),'cover':len(areas),'cell_areas':{k:str(v) for k,v in areas.items()}}
def area(p):return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0] for i in range(len(p))))/2
def poly(t):return [(F(0),F(0)),(F(2),F(0)),(F(2),F(2)),(2-t,F(2)),(2-t,t),(F(0),t)]
witnesses={}
for t in [F(1,4),F(3,4)]:
    p=poly(t);assert area(p)==4*t-t*t
    witnesses[str(t)]={'area':str(area(p)),'cell_areas':[str(t),str(2*t-t*t),str(t)],'perimeter':sum(math.dist(a,b) for a,b in zip(p,p[1:]+p[:1]))}
wave_checks={}
t=F(1,4);amp=F(1,8)
for N in [1,4,20]:
    wave=[(F(j,4*N),t+amp*[0,1,0,-1][j%4]) for j in range(4*N+1)]
    p=poly(t)[:-1]+list(reversed(wave))
    length=sum(math.dist(a,b) for a,b in zip(p,p[1:]+p[:1]));expected=7+math.sqrt(1+N*N/4)
    assert area(p)==F(15,16) and abs(length-expected)<1e-10 and min(y for x,y in wave)>0 and max(y for x,y in wave)<1
    wave_checks[N]={'area':str(area(p)),'perimeter':length,'formula':expected,'height_range':[str(min(y for x,y in wave)),str(max(y for x,y in wave))]}
result={'shifted_grid_checks':shifts,'certificate_intersections':[[4,8],'empty',[4,4]],'corridor_witnesses':witnesses,'wave_checks':wave_checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
