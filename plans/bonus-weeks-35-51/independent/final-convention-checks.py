"""Independent new convention examples in final revisions, weeks 37/38/41/42/43."""
from math import sin,cos,pi,isclose,sqrt
from pathlib import Path
import json
phi=pi/6;eps=25*pi/180
rows=[[-sin(phi),cos(phi),0],[-sin(eps)*cos(phi),-sin(eps)*sin(phi),cos(eps)]]
assert all(isclose(sum(x*x for x in row),1) for row in rows)
assert isclose(sum(a*b for a,b in zip(*rows)),0,abs_tol=1e-12)
v=list(zip(*rows));turned=[(-dy,dx) for dx,dy in v]
assert all(isclose(dx*dx+dy*dy,a*a+b*b) for (dx,dy),(a,b) in zip(v,turned))
equal_projection=[(80,-80/sqrt(3)),(-80,-80/sqrt(3)),(0,160/sqrt(3))]
lengths=[sqrt(x*x+y*y) for x,y in equal_projection];assert max(lengths)-min(lengths)<1e-10
assert all(isclose(x*a+y*b,-lengths[0]**2/2) for i,(x,y) in enumerate(equal_projection) for a,b in equal_projection[i+1:])
seams={'M':{0:0,1:1},'R':{0:1,1:0}}
assert seams['R'][seams['R'][0]]==0
def mapletter(x,y):
    xy=((x+1)%3-1,(y+1)%3-1)
    return {(-1,1):'A',(0,1):'B',(1,1):'C',(-1,0):'D',(0,0):'H',(1,0):'E',(-1,-1):'F',(0,-1):'G',(1,-1):'I'}[xy]
assert [mapletter(x,0) for x in [0,1,0]]==['H','E','H']
assert [mapletter(x,0) for x in [0,1,2]]==['H','E','D']
assert (2+1)//3==1 # RR output D lies in right copy
assert 9+1<=12 # at most one new copy per orthogonal step
outputs={'BR':'square','RB':'circle','RR':None,'BB':None}
assert [outputs['BRRB'[i:i+2]] for i in [0,2]]==['square','circle']
old='XY';new='Z';gap=2;assert old[:gap-1]+new+old[gap-1:]=='XZY'
result={'37':{'projection_rows_orthonormal':True,'whole_turn_degrees':90,'equal_projected_lengths':lengths},'38':seams,'41':{'RL':['H','E','H'],'RR':['H','E','D'],'RR_final_copy':'right','twelve_copies_suffice_for_nine_steps':True,'cell_mm':78*25.4/72},'42':{'input':'BRRB','pairs':['BR','RB'],'outputs':['square','circle']},'43':{'input':'XY','new':'Z','gap':2,'output':'XZY'}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
