"""Targeted geometry and example checks for the introduction follow-up.
Run with PyMuPDF from the repository root. No output files are changed.
"""
from pathlib import Path
from collections import Counter,deque
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[2]
Y=ROOT/'lowell-math-circle-year-2'
def paths(page):
 return Counter((round(d['rect'].width,2),round(d['rect'].height,2),len(d['items'])) for d in page.get_drawings())
# Closing gaps does not scale, add, or remove any Week 6 physical piece outline.
p=Y/'week-06/week-06-grades-4-5.pdf'
a=fitz.open(p.parent/'archive-before-intro-followup'/p.name);b=fitz.open(p)
assert len(a)==len(b)==9
assert paths(a[1])==paths(b[1])
assert 'code game' not in b[0].get_text().lower()
assert 'keeper hides' in b[1].get_text()
# Every retained work rectangle stays the same physical size after reflow.
for week,bands,pages in [(22,['k-1','grades-2-3','grades-4-5'],[0]),(35,['grades-2-3','grades-4-5'],[0,1])]:
 for band in bands:
  p=Y/f'week-{week:02}'/f'week-{week:02}-{band}.pdf'
  a=fitz.open(p.parent/'archive-before-intro-followup'/p.name);b=fitz.open(p)
  assert len(a)==len(b)
  def boards(d):
   return Counter((round(x['rect'].width,2),round(x['rect'].height,2)) for i in pages for x in d[i].get_drawings() if x['rect'].width>300 and x['rect'].height>100)
  assert boards(a)==boards(b),(week,band,boards(a),boards(b))
# Week 22 complete split: disjoint memberships; interiors share their midpoint.
K,L,M,N=(1,0),(3,0),(3,1.5),(1,1.5)
mid=lambda a,b:tuple((x+y)/2 for x,y in zip(a,b))
assert mid(K,M)==mid(L,N)==(2,.75)
# Week 69: actual grid routes, including both candidate arrival sides.
grid={(x,y) for x in range(4) for y in range(3)}
def distances(s):
 d={s:0};q=deque([s])
 while q:
  x,y=q.popleft()
  for t in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
   if t in grid and t not in d:d[t]=d[(x,y)]+1;q.append(t)
 return d
red=[(0,0),(1,0),(2,0),(3,0)]
blue=[(3,0),(3,1),(3,2)]
green=[(3,2),(2,2),(1,2),(0,2),(0,1),(0,0)]
for route in [red,blue,green]:assert distances(route[0])[route[-1]]==len(route)-1
D=distances((1,0));assert min(D[p] for p in green)==1 and min(D[p] for p in blue)==2
# Week 45 shared public input, distinct host actions and outcomes.
choice,prize,ticket=1,2,2
empty=[d for d in [1,2,3] if d not in [choice,prize]]
opened_a=empty[0];switch=next(d for d in [1,2,3] if d not in [choice,opened_a])
assert opened_a==3 and switch==prize and ticket==prize
print('PASS: Week 6 piece outlines, Week 22/35 work-board dimensions, crossing, both road distances, both host outcomes.')
