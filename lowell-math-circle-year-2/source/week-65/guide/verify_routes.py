#!/usr/bin/env python3
"""Independently verify every route answer printed in the adult guide."""
import itertools,json
D={'E':(1,0),'N':(0,1),'W':(-1,0),'S':(0,-1)}
samples={4:'ENWS',6:'EENWWS',8:'EENNWWSS'}
for length,route in samples.items():
 assert len(route)==length and route[0]=='E'
 x=y=0
 for i,d in enumerate(route):
  dx,dy=D[d];x+=dx;y+=dy
  assert -3<=x<=3 and -3<=y<=3
  nextdir=route[i+1] if i+1<len(route) else 'E'
  assert D[nextdir]!=(-dx,-dy)
 assert (x,y)==(0,0)
# Visible four-room map: two diagonal rooms do not share a side.
adj={'Home':['A','B'],'A':['Home','Star'],'B':['Home','Star'],'Star':['A','B']}
def routes(n):
 out=[]
 def walk(path):
  if len(path)==n+1:
   if path[-1]=='Star':out.append(path)
   return
  for q in adj[path[-1]]:walk(path+[q])
 walk(['Home']);return out
r2=routes(2);r4=routes(4)
assert len(r2)==2 and len(r4)==8
expected=[['Home',a,b,c,'Star'] for a in ['A','B'] for b in ['Home','Star'] for c in ['A','B']]
assert sorted(r4)==sorted(expected)
left='ABCDEFGHA';right='AHGFEDCBA'
assert left[4]==right[4]=='E'
assert left[8]==right[8]=='A'
assert all(v!='A' for v in left[1:8]) and all(v!='A' for v in right[1:8])
report={'square_grid_examples':samples,'square_examples_within_printed_grid':True,'final_east_heading_legal':True,'octagon_fourth_position':'E','octagon_first_full_returns':[8,8],'two_door_routes':r2,'four_door_routes':r4}
print(json.dumps(report,indent=2))
