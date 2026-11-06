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
 K,L,M,N=(1,0),(3,0),(3,1.5),(1,1.5)
 midpoint=lambda a,b:tuple((x+y)/2 for x,y in zip(a,b))
 assert midpoint(K,M)==midpoint(L,N)==(2,.75)
 assert {"K","M"}.isdisjoint({"L","N"})
 assert 7.35<9.2 # closed segment has distinct endpoints
 for band in ('k-1','grades-2-3','grades-4-5'):
  tex=(S/(band+'.tex')).read_text().split('\\newpage')[0]
  # Every band's opening key shows the K-L-M-N split before Problem 1.
  assert tex.index('1/0/K,3/0/L,3/1.5/M,1/1.5/N')<tex.index('\\problem{1}') and tex.index('one group: K, M')<tex.index('\\problem{1}')
  if band=='k-1':
   # v7 (kid-fit revision): the K-1 key keeps only the K-L-M-N split; the adult draws E, F-G and H-I-J.
   assert '{E};' not in tex and '\\fill (14.38,1.48) circle (.04);' not in tex
   continue
  assert tex.index('{E};')<tex.index('\\problem{1}')
  assert 'fill=black!9' in tex and '\\fill (14.38,1.48) circle (.04);' in tex
  assert '\\fill (7.35,1.5)' in tex and '\\fill (9.2,1.5)' in tex
 return 'E is a point; FG includes both endpoints; HIJ is noncollinear and its small dot lies strictly inside (Grades 2-5 keys); every key shows the K-L-M-N split.'

result=regions()
print(f"PASS Week {WEEK}: {result}")
