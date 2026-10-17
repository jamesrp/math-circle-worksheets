from pathlib import Path
from math import dist
import json
import pymupdf as fitz
ROOT=Path(__file__).resolve().parent
P=lambda s: set(tuple(sorted(e)) for e in s.split())
path=lambda s:P(' '.join(a+b for a,b in zip(s,s[1:])))
ring=lambda s:path(s)|{tuple(sorted((s[0],s[-1])))}
example=[('demo'+str(i),'wxyz',P('wx xy xz'),8) for i in range(1,4)]
pages={
 'shared':[
 example+[('P5','abcde',path('abcde'),22),('P7','abcdefg',path('abcdefg'),20)],
 [('T1','abcdefg',P('ab bc cd de cf fg'),22),('T2','abcdefgh',P('ab bc cd de cf fg fh'),22)],
 [('R3','abc',ring('abc'),22),('R4','abcd',ring('abcd'),22)],
 [('R5','abcde',ring('abcde'),22),('R6','abcdef',ring('abcdef'),22)]],
 'upper':[
 example+[('P5','abcde',path('abcde'),22),('P7','abcdefg',path('abcdefg'),20)],
 [('E4','abcd',ring('abcd'),22),('E5','abcde',ring('abcde'),22)],
 [('D1','abcdef',set(),22),('D2','abcdef',set(),22)],
 [('fold-input','wxyz',path('wxyz'),8),('fold-compare','wxyz',path('wxyz'),8),('fold-output','xyz',path('xyz'),8)],
 [('Q6','abcdef',ring('abcdef'),22)], [('Q8','abcdefgh',ring('abcdefgh'),22)]],
 'materials':[
 [(t,'abcdef',P('ab bc ca cd de af'),22) for t in ['F1-original','F1-copy']],
 [(t,'abcde',ring('abcde')|P('ac'),22) for t in ['F2-original','F2-copy']],
 []]}
output=[]
for name,pgs in pages.items():
 d=fitz.open(ROOT.parent/'draft'/f'{name}.pdf')
 assert len(d)==len(pgs)
 for i,(p,specs) in enumerate(zip(d,pgs)):
  if name=='materials' and i==2:continue # cut-out counters, not graph vertices
  draws=p.get_drawings();circles=[x['rect'] for x in draws if [a[0] for a in x['items']]==['c']*4]
  words=p.get_text('words');offset=0
  assert len(circles)==sum(len(s[1]) for s in specs),(name,i,len(circles))
  for title,labels,expected,diam in specs:
   cs=circles[offset:offset+len(labels)];offset+=len(labels)
   centers={v:((r.x0+r.x1)/2,(r.y0+r.y1)/2) for v,r in zip(labels,cs)}
   for v,r in zip(labels,cs):
    assert abs(r.width*25.4/72-diam)<.02 and abs(r.height*25.4/72-diam)<.02
    cx,cy=centers[v]
    matches=[w[4] for w in words if abs((w[0]+w[2])/2-cx)<2 and 0<=w[1]-r.y1<=12 and len(w[4])==1]
    assert matches==[v],(name,i,title,v,matches)
   actual=set()
   for dr in draws:
    for item in dr['items']:
     if item[0]!='l':continue
     ends=[]
     for pt in item[1:3]:ends.append([v for v,c in centers.items() if dist(tuple(pt),c)<.02])
     if all(len(x)==1 for x in ends):actual.add(tuple(sorted((ends[0][0],ends[1][0]))))
   assert actual==expected,(name,i,title,actual,expected)
   mind=min(dist(a,b) for a,b in __import__('itertools').combinations(centers.values(),2))*25.4/72
   if diam>=20:assert mind>=27.99
   output.append({'pdf':name,'page':i+1,'board':title,'labels':labels,'edges':[''.join(e) for e in sorted(actual)],'dot_diameter_mm':diam,'minimum_center_distance_mm':round(mind,3)})
(ROOT/'pdf-graph-results.json').write_text(json.dumps(output,indent=2)+'\n')
print(f'{len(output)} printed graph instances: labels, every road, vertex diameters and center spacings verified directly from final PDF drawing objects.')
