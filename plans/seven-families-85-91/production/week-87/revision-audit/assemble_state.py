"""Digital assembly using actual PDF piece crops; no physical rehearsal claim."""
from pathlib import Path
import pymupdf as f
r=Path(__file__).resolve().parent.parent
s=f.open(r/'final/materials.pdf');d=f.open();p=d.new_page(width=430*72/25.4,height=220*72/25.4)
def rect(vals):return f.Rect(*[v*72/25.4 for v in vals])
def put(pg,clip,target):p.show_pdf_page(rect(target),s,pg,clip=rect(clip))
put(4,[14,43,198,182],[10,40,194,179])
put(3,[23,43,193,133],[225,40,395,130])
for i,v in enumerate([0,1,5,8,10]):
 x,y=29+16*v,57+19*i
 put(4,[28.5+34*i,196.5,41.5+34*i,209.5],[x-6.5,y-6.5,x+6.5,y+6.5])
# Fixed proposal markers remain below the numbered line throughout.
put(4,[42,229,55,242],[54.5,160.5,67.5,173.5])
put(4,[81,226,99,244],[148,158,166,176])
# Separate labels stay in the mat's label slots.
put(4,[126,227,149,250],[242.5,45.5,265.5,68.5])
put(4,[162,227,185,250],[297.5,45.5,320.5,68.5])
# X: V1,V2; Y: V4,V5; Tie: V3, all actual 18 mm vote tokens.
for i,x,y in [(0,238,85),(1,270,85),(3,293,85),(4,325,85),(2,364,101)]:
 sx=34+35*i
 put(0,[sx-9,180,sx+9,198],[x-9,y-9,x+9,y+9])
p.insert_text((20,20),'Digital assembly: unchanged favorites and proposals; separate tally labels and vote tokens',fontsize=12)
p.insert_text((20,580),'Untested with physical cut pieces. Example result: X 2, Y 2, Tie 1.',fontsize=12)
p.get_pixmap(matrix=f.Matrix(1,1)).save(r/'revision-renders/assembled-state.png')
