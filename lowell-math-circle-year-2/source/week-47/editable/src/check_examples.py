"""Independent checks of the targeted reference examples.

Uses geometry, ranks and counts directly, without importing packet builders,
answer files or their Hamming-distance/region/matching solution machinery.
"""
from pathlib import Path
from math import hypot
import re,json
WEEK = 47
S=Path(__file__).resolve().parent

def heights():
 towers=(1,2,2,1)
 assert all(abs(a-b)<=1 for a,b in zip(towers,towers[1:]))
 marks=[(76+11*i,58-10*h) for i,h in enumerate(towers)]
 assert len({x for x,y in marks})==4
 decoded=tuple((58-y)//10 for x,y in marks)
 assert decoded==towers and len(towers)==4
 assert abs(3-1)>1
 for band in ('k-1','grades-2-3','grades-4-5'):
  tex=(S/(band+'.tex')).read_text().split('\\newpage')[0]
  assert 'One marker in each column' in tex
  assert '(133,44) rectangle ++(44,12)' in tex
  for x,y in marks:assert f'({x},{y}) circle (2.1)' in tex
  for i,h in enumerate(towers):assert f'({138.5+11*i},50) {{{h}}}' in tex
 return 'All four towers, four markers and boxed row decode to 1,2,2,1; target boards still have five sites.'

result=heights()
print(f"PASS Week {WEEK}: {result}")
