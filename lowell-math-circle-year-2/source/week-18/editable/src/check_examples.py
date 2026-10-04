"""Independent checks of the targeted reference examples.

Uses geometry, ranks and counts directly, without importing packet builders,
answer files or their Hamming-distance/region/matching solution machinery.
"""
from pathlib import Path
from math import hypot
import re,json
WEEK = 18
S=Path(__file__).resolve().parent

def transmission():
 start=(0,1,0,1);finish=(0,1,1,1)
 changed=[i+1 for i,(a,b) in enumerate(zip(start,finish)) if a!=b]
 assert changed==[3] and len(start)==len(finish)==4
 assert sum(a!=b for a,b in zip(start,start))==0
 for band in ('k-1','grades-2-3','grades-4-5'):
  tex=(S/(band+'.tex')).read_text().split('\\newpage')[0]
  assert 'Start row' in tex and 'Final row' in tex and 'only this row' in tex
  assert tex.count('(11,6) -- (11,16)')==1
  assert tex.count('(9,12.25) -- (11.8,12.25)')==1
  if band=='grades-4-5':
   digits=re.findall(r'\\ttfamily[^\n]*?\{([01])\};',tex)
   assert digits==list('010101110111'),digits
  else:
   fills=re.findall(r'\\draw\[line width=\.9pt,fill=(black|white)\]',tex)
   assert fills==['black' if b=='1' else 'white' for b in '010101110111'],fills
 return '0101 -> 0111 changes only position 3; no-change is legal; receiver row alone crosses folder.'

result=transmission()
print(f"PASS Week {WEEK}: {result}")
