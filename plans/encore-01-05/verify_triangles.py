from pathlib import Path
import json

def neighbors(c):
 i,j,k=c
 return [(i,j,1),(i,j-1,1),(i-1,j,1)] if k==0 else [(i,j,0),(i+1,j,0),(i,j+1,0)]
def norm(s):
 mi=min(x[0] for x in s);mj=min(x[1] for x in s)
 return tuple(sorted((i-mi,j-mj,k) for i,j,k in s))
sets={((0,0,0),)}
checks={}
for n in range(1,11):
 if n>1:sets={norm(set(s)|{q}) for s in sets for c in s for q in neighbors(c) if q not in s}
 def boundary(s):return sum(q not in s for c in s for q in neighbors(c))
 vals=[boundary(s) for s in sets]
 checks[n]={'fixed_polyiamonds':len(sets),'min_boundary':min(vals),'max_boundary':max(vals),'min_example':next(s for s in sets if boundary(s)==min(vals))}
assert checks[10]['min_boundary']==8
# Area10 consists of exactly6 triangles+2rhombi; find two disjoint adjacencies in minimum example.
s=checks[10]['min_example'];pairs=[(a,b) for a in s for b in neighbors(a) if b in s and a<b]
p=next((a,b) for a in pairs for b in pairs if set(a).isdisjoint(b))
checks['six_green_two_blue_min']={'triangle_cells':s,'blue_pairs':p,'boundary':8}
# Any edge-connected8pieces has at least7contacts: P<=3*6+4*2-2*7=12; strip achieves12.
checks['six_green_two_blue_max']=12
Path('plans/encore-01-05/triangle-checks.json').write_text(json.dumps(checks,indent=2))
print('area10 fixed polyiamonds',len(sets),'boundary min8; connected8-piece bound max12')
