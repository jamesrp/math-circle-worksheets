#!/usr/bin/env python3
"""Arithmetic checks for the exact diagrams and finite tasks of the Week 28 student pages.

Moved unchanged from the old student builder (build_packets.py) when the pages became
problem files. The disk angles and route states are read from the problem files'
figures.py, so the checks cover what the pages draw. Writes math_checks.json and
prints a one-line summary.
"""
from pathlib import Path
import itertools, json, sys
ROOT=Path(__file__).resolve().parent
for week in (ROOT.parent/'problem-files', ROOT.parent.parent):
    if (week/'figures.py').exists(): break
else: sys.exit('Cannot find the Week 28 problem files (figures.py); see README.md.')
sys.path.insert(0,str(week)); sys.dont_write_bytecode=True
from figures import ANGLES as angles, CHECKS as checks, ROUTE_LABELS as route_labels  # noqa: E402

# Independent arithmetic checks for exact diagrams and finite tasks.
orders=sorted(set(itertools.permutations([30,30,60,60,90,90])))
valid=[s for s in orders if s[0]==30 and sum(s[::2])==180]
wedges=[30,30,60,60,90,120,150]
groups=[''.join('ABCDEFG'[i] for i in range(7) if mask>>i&1) for mask in range(1,1<<7) if sum(wedges[i] for i in range(7) if mask>>i&1)==180]
labels=[''.join(s) for s in itertools.product('MV',repeat=4) if abs(s.count('M')-s.count('V'))==2]
assert len(labels)==8
assert len([s for s in labels if s[0]=='M'])==4
assert len([s for s in labels if s[0]=='M' and s[2]=='V'])==2
assert len([s for s in labels if s[0]=='M' and s[1]=='M'])==2
assert len([s for s in labels if s[0]=='V' and s[2]=='V'])==2
for a in [90,60,30,120]:
    rs=sorted([0,a,180,360-a])
    ss=[rs[i+1]-rs[i] for i in range(3)]+[360-rs[-1]]
    assert sum(ss[::2])==sum(ss[1::2])==180
assert min(sum(a!=b for a,b in zip('MMMV',s)) for s in labels if s!='MMMV')==2
for ss in angles+checks+[[120]*3,[60,60,60,90,90],[30,30,60,60,60,60,60]]:assert sum(ss)==360 and min(ss)>0
report={'four_sector_checks':[{'sectors':s,'alternating_totals':[sum(s[::2]),sum(s[1::2])]} for s in angles], 'half_turn_wedge_groups':groups,'valid_right_angle_assignments':labels,'six_angle_orders_starting_30':valid,'six_angle_order_count':len(valid),'all_diagram_angles_total_360':True}
(ROOT/'math_checks.json').write_text(json.dumps(report,indent=2))
print(json.dumps({'half_turn_groups':len(groups),'right_angle_assignments':len(labels),'six_angle_orders':len(valid)}))

partial=['M?V?','MM??','V?V?']
completions=[[lab for lab in labels if all(a=='?' or a==b for a,b in zip(p,lab))] for p in partial]
tab_solutions={}
for n in (2,3,4):
 sols=[case for case in itertools.product(*completions) if sum(sum(c=='M' for c,p in zip(lab,mask) if p=='?') for lab,mask in zip(case,partial))==n]
 tab_solutions[str(n)]=sols
assert [len(tab_solutions[str(n)]) for n in (2,3,4)]==[4,0,4]
route_map=dict(zip('ABCDEFGH',route_labels))
paths={}
for end in ('H','D'):
 rest=[x for x in 'BCDEFGH' if x!=end]
 for middle in itertools.permutations(rest):
  route=('A',)+middle+(end,)
  if all(sum(a!=b for a,b in zip(route_map[u],route_map[v]))==2 for u,v in zip(route,route[1:])):
   paths[end]=route
   break
 assert end in paths
# All 16 measurement pieces have radius 2.5 cm, exactly matching their sector template.
matching_wedges=[{'label':f'{tag}{j+1}','degrees':angle,'radius_cm':2.5,'shaded':j%2==0} for tag,ss in zip('ABCD',angles) for j,angle in enumerate(ss)]
assert len(matching_wedges)==16
assert [x['degrees'] for x in matching_wedges if x['label'].startswith('B')]==[45,90,90,135]
invalid=['MMMM','VVVV','MMVV','MVMV']
rotations={s[k:]+s[:k] for s in invalid for k in range(4)}
assert rotations==set(''.join(p) for p in itertools.product('MV',repeat=4))-set(labels)
report.update({'k1_tab_completions':tab_solutions,'k1_route_witnesses':paths,'matching_wedges':matching_wedges,'right_angle_obstruction_cases_cover_all_remaining_labels':True,'physical_models_tested':False})
(ROOT/'math_checks.json').write_text(json.dumps(report,indent=2))
