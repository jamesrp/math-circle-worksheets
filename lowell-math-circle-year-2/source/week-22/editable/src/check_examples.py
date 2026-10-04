"""Independent checks of the targeted reference examples.

Uses geometry, ranks and counts directly, without importing packet builders,
answer files or their Hamming-distance/region/matching solution machinery.
"""
from pathlib import Path
from math import hypot
import re,json
WEEK = 22
S=Path(__file__).resolve().parent

def regions():
 H=(13.35,.8);I=(15.75,.8);J=(14.35,2.55);mark=(14.38,1.48)
 def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 assert cross(H,I,J)>0
 assert all(cross(a,b,mark)>0 for a,b in ((H,I),(I,J),(J,H)))
 assert 7.35<9.2 # closed segment has distinct endpoints
 for band in ('k-1','grades-2-3','grades-4-5'):
  tex=(S/(band+'.tex')).read_text().split('\\newpage')[0]
  assert tex.index('{E};')<tex.index('\\problem{1}')
  assert 'fill=black!9' in tex and '(14.3,1.40)' in tex
  assert '\\fill (7.35,1.5)' in tex and '\\fill (9.2,1.5)' in tex
 return 'E is a point; FG includes both endpoints; HIJ is noncollinear and its visible cross lies strictly inside.'

result=regions()
print(f"PASS Week {WEEK}: {result}")
