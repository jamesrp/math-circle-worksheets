from pathlib import Path
from collections import Counter
import fitz,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
WEEK=json.loads((Path(__file__).resolve().parent/'content.json').read_text())['week']
mm=lambda p:p*25.4/72

def lines(page):
 for p in page.get_drawings():
  for item in p['items']:
   if item[0]=='l':
    a,b=item[1:];yield (mm(a.x),mm(a.y),mm(b.x),mm(b.y))

def spacings(page,vertical,length):
 coords=set()
 for x,y,X,Y in lines(page):
  if vertical and abs(x-X)<.01 and abs(abs(y-Y)-length)<.02:coords.add(round(x,2))
  if not vertical and abs(y-Y)<.01 and abs(abs(x-X)-length)<.02:coords.add(round(y,2))
 return [round(b-a,2) for a,b in zip(sorted(coords),sorted(coords)[1:])]
records={}
for n in [WEEK]:
 f=ROOT; k=fitz.open(f/'k-1.pdf'); dimensions={}
 if n==47:
  dimensions['main_site_spacings_mm']=spacings(k[0],True,80)
  dimensions['main_level_spacings_mm']=spacings(k[0],False,100)
  assert all(abs(x-22)<.02 for x in dimensions['main_site_spacings_mm'])
  assert all(abs(x-20)<.02 for x in dimensions['main_level_spacings_mm'])
  assert dimensions['main_site_spacings_mm'] and dimensions['main_level_spacings_mm']
 elif n==48:
  dimensions['coarse_cell_widths_mm']=spacings(k[0],True,120)
  dimensions['fine_cell_widths_mm']=spacings(k[2],True,120)
  assert all(abs(x-30)<.02 for x in dimensions['coarse_cell_widths_mm'])
  assert all(abs(x-15)<.02 for x in dimensions['fine_cell_widths_mm'])
  assert len(dimensions['coarse_cell_widths_mm'])==4 and len(dimensions['fine_cell_widths_mm'])==8
 elif n==49:
  for pageidx in [1,3]:
   rects=[p['rect'] for p in k[pageidx].get_drawings() if abs(mm(p['rect'].width)-40)<.03 and abs(mm(p['rect'].height)-40)<.03]
   centers=[(round(mm((r.x0+r.x1)/2),2),round(mm((r.y0+r.y1)/2),2)) for r in rects]
   dimensions[f'page{pageidx+1}_40mm_station_centers']=centers
   assert len(centers)==(8 if pageidx==1 else 6)
 elif n==50:
  b=[p['rect'] for p in k[1].get_drawings() if abs(mm(p['rect'].width)-160)<.03 and abs(mm(p['rect'].height)-120)<.03]
  assert b;dimensions['main_board_mm']=[round(mm(b[0].width),3),round(mm(b[0].height),3)]
  lengths=[abs(X-x) for x,y,X,Y in lines(k[1]) if abs(y-Y)<.01]
  assert any(abs(x-100)<.02 for x in lengths);dimensions['calibration_mm']=min(lengths,key=lambda a:abs(a-100))
 else:
  # The final whole-pair page has long160mm rulers and9-unit90mm work rulers.
  ls=list(lines(k[5]));lens=[abs(X-x) for x,y,X,Y in ls if abs(y-Y)<.01]
  assert any(abs(x-160)<.02 for x in lens);dimensions['main_ruler_mm']=min(lens,key=lambda a:abs(a-160))
  # Tick centers along the first full ruler have10mm spacing.
  ys=Counter(round((y+Y)/2,2) for x,y,X,Y in ls if abs(x-X)<.01 and abs(abs(Y-y)-4)<.02)
  y0=next(y for y,count in ys.items() if count==17)
  xs=sorted(set(round(x,2) for x,y,X,Y in ls if abs(x-X)<.01 and abs(abs(Y-y)-4)<.02 and abs((y+Y)/2-y0)<.02))
  dimensions['unit_spacings_mm']=[round(b-a,2) for a,b in zip(xs,xs[1:])]
  assert all(abs(x-10)<.02 for x in dimensions['unit_spacings_mm'])
 pdf=f/'facilitator-guide.pdf';g=fitz.open(pdf)
 assert len(g)==3
 for p in g:
  assert p.rect.width==612 and p.rect.height==792
  for block in p.get_text('dict')['blocks']:
   if 'lines' not in block:continue
   for line in block['lines']:
    for s in line['spans']:
     assert all(c not in s['text'] for c in ['\ufffd','\u25a0']),s['text']
     # Header/footer may live outside the body box, but all content fits page margins.
     x0,y0,x1,y1=s['bbox'];assert x0>=45 and x1<=565 and y0>=15 and y1<=772,(n,s['text'],s['bbox'])
 records[n]={'pages':len(g),'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'dimensions':dimensions}
 print(n,json.dumps(records[n]))
 (f/'facilitator-qa').mkdir(exist_ok=True)
 (f/'facilitator-qa/pdf-checks.json').write_text(json.dumps(records[n],indent=2)+'\n')
print('All digital page and dimension checks passed; no physical tests were performed.')
