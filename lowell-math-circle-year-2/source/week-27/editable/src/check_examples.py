"""Independent checks of the targeted reference examples.

Uses geometry, ranks and counts directly, without importing packet builders,
answer files or their Hamming-distance/region/matching solution machinery.
"""
from pathlib import Path
from math import hypot
import re,json
WEEK = 27
S=Path(__file__).resolve().parent

def blocking():
 current={'P':'V','Q':'U','V':'P','U':'Q'}
 def likes(order,candidate,partner):return order.index(candidate)<order.index(partner)
 p_order=('U','V')
 outcomes=[]
 for u_order in (('P','Q'),('Q','P')):
  yes=(likes(p_order,'U',current['P']),likes(u_order,'P',current['U']))
  outcomes.append((yes,all(yes)))
 assert outcomes==[((True,True),True),((True,False),False)]
 for band in ('k-1','grades-2-3'):
  tex=(S/(band+'.tex')).read_text().split('\\newpage')[0]
  assert 'P prefers U to V: yes' in tex
  assert 'U prefers P to Q: yes' in tex and 'U prefers P to Q: no' in tex
  assert 'This check is only for P and U' in tex
  assert tex.count('fill=gray!22')==4
 return 'PV/QU: P-U blocks for U:PQ, but not U:QP; one failed check makes no claim of global stability.'

result=blocking()
print(f"PASS Week {WEEK}: {result}")
