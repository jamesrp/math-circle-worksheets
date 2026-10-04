from pathlib import Path
import fitz, math, json
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parent
RENDERS=ROOT.parent/'build'/'disc-checks';RENDERS.mkdir(parents=True,exist_ok=True)
MATS={1:[(61,188,6,32)],2:[(108,107,6,40)],3:[(108,107,8,40)],4:[(108,107,8,40)],5:[(108,104,10,43)],6:[(108,107,8,40)]}
MM=72/25.4
checks=[]
for band in ['k-1','grades-2-3']:
    doc=fitz.open(ROOT.parent/'build'/(band+'.pdf'))
    for page_number in range(1,7 if band=='k-1' else 2):
        page=doc[page_number-1]
        words=page.get_text('words')
        pix=page.get_pixmap(matrix=fitz.Matrix(85/72,85/72))
        im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
        d=ImageDraw.Draw(im)
        scale=im.width/215.9
        centers=[]; expected_labels=[]; spacings=[]
        if band=='k-1':
            for x,y,n,r in MATS[page_number]:
                spacings.append(2*r*math.sin(math.pi/n))
                for i in range(n):
                    theta=math.radians(90-i*360/n)
                    centers.append((x+r*math.cos(theta),y-r*math.sin(theta)))
                    expected_labels.append((str(i+1), x+(r+12.5+(1 if i+1>=10 else 0))*math.cos(theta), y-(r+12.5+(1 if i+1>=10 else 0))*math.sin(theta)))
        else:
            spacings=[24]
            centers=[(48+24*i,167) for i in range(6)]
            expected_labels=[(str(i+1),48+24*i,181) for i in range(6)]
        label_clearances=[]
        for label,lx,ly in expected_labels:
            candidates=[w for w in words if w[4]==label]
            word=min(candidates,key=lambda w:((w[0]+w[2])/2/MM-lx)**2+((w[1]+w[3])/2/MM-ly)**2)
            box=[v/MM for v in word[:4]]
            assert math.dist(((box[0]+box[2])/2,(box[1]+box[3])/2),(lx,ly))<4
            for x,y in centers:
                dx=max(box[0]-x,0,x-box[2]);dy=max(box[1]-y,0,y-box[3])
                label_clearances.append(math.hypot(dx,dy)-10)
        assert min(label_clearances)>0, (band,page_number,min(label_clearances))
        for x,y in centers:
            d.ellipse(((x-10)*scale,(y-10)*scale,(x+10)*scale,(y+10)*scale),fill=(236,243,250),outline=(30,95,150),width=2)
        im.save(RENDERS/f'{band}-{page_number}-20mm-discs.png')
        checks.append({'band':band,'page':page_number,'disc_diameter_mm':20,'minimum_adjacent_disc_gap_mm':round(min(spacings)-20,3),'minimum_label_disc_clearance_mm':round(min(label_clearances),3)})
# Verify all deliverables remain six US Letter pages, and mathematical checks stayed true.
for band in ['k-1','grades-2-3','grades-4-5']:
    doc=fitz.open(ROOT.parent/'build'/(band+'.pdf'))
    assert len(doc)==6
    assert all(abs(p.rect.width-612)<0.01 and abs(p.rect.height-792)<0.01 for p in doc)
(ROOT/'disc-clearance-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
