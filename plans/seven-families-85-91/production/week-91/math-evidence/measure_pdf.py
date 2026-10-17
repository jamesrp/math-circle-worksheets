from pathlib import Path
import pymupdf
r=Path(__file__).resolve().parents[1]
lines=[]
mm=72/25.4
expected=[[(108,95,16),(55,175,16),(161,175,16)],[(140,45,12),(84,100,12),(196,100,12)]+[(x,173,15) for x in (56,112,168,224)],[(140,43,12),(84,82,12),(196,82,12)]+[(x,123,12) for x in (56,112,168,224)]+[(x,175,11) for x in (42,70,98,126,154,182,210,238)],[(x,105,18 if i in (0,4) else 15) for i,x in enumerate((40,90,140,190,240))],[(x,105,16 if i in (0,5) else 14) for i,x in enumerate((35,77,119,161,203,245))]]
for stem,count in [('students',6),('return-visit',4),('materials',7)]:
 d=pymupdf.open(r/'draft'/f'{stem}.pdf');assert len(d)==count
 for i,p in enumerate(d):
  dims=(279.4,215.9) if stem=='materials' and 1<=i<=4 else (215.9,279.4)
  assert abs(p.rect.width/mm-dims[0])<.01 and abs(p.rect.height/mm-dims[1])<.01
  lines.append(f'{stem} p{i+1}: page size {p.rect.width/mm:.3f} x {p.rect.height/mm:.3f}mm')
  if stem=='materials' and i<5:
   curves=[a['rect'] for a in p.get_drawings() if len(a['items'])==4 and all(it[0]=='c' for it in a['items'])]
   assert len(curves)==len(expected[i]),(i,len(curves))
   for box,(x,y,radius) in zip(curves,expected[i]):
    assert abs((box.x0+box.x1)/2/mm-x)<.02
    assert abs((box.y0+box.y1)/2/mm-y)<.02
    assert abs(box.width/mm-2*radius)<.02 and abs(box.height/mm-2*radius)<.02
   lines.append(f'  All {len(curves)} actual PDF circle centers/diameters agree with specified geometry to 0.02mm.')
  if stem=='materials' and i==6:
   horizontals=[a for a in p.get_drawings() if len(a['items'])==1 and a['items'][0][0]=='l']
   assert any(abs(a['rect'].width/mm-50)<.01 and abs(a['rect'].y0/mm-254)<.02 for a in horizontals)
   lines.append('  Actual PDF 50mm scale line confirmed.')
(r/'math-evidence/pdf-measurements.txt').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines))
