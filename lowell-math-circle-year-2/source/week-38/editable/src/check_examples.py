"""Independent checks of the targeted reference examples.

Uses geometry, ranks and counts directly, without importing packet builders,
answer files or their Hamming-distance/region/matching solution machinery.
"""
from pathlib import Path
from math import hypot
import re,json
WEEK = 38
S=Path(__file__).resolve().parent

def washer():
 C=(58,121);dots={'P':(58,92),'Q':(87,121),'R':(58,134)}
 radii={k:hypot(p[0]-C[0],p[1]-C[1]) for k,p in dots.items()}
 assert radii=={'P':29.0,'Q':29.0,'R':13.0}
 groups=[['P','Q'],['R']]
 assert all(len({radii[k] for k in g})==1 for g in groups)
 assert len(groups)==2 and len(dots)==3
 for band in ('k-1','grades-2-3','grades-4-5'):
  tex=(S/(band+'.tex')).read_text()
  assert tex.index('flat paper washer')<tex.index('\\textbf{Problem 3:}')
  assert 'Dots on one edge go in one ring' in tex
  assert tex.count('circle (29)')==2 and tex.count('circle (13)')==2
 return 'P,Q lie on radius 29 outer edge; R lies on radius 13 inner edge; rings represent memberships, not pieces.'

result=washer()
print(f"PASS Week {WEEK}: {result}")
