import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import pymupdf, json
BASE=_os.path.join(ROOT, 'lowell-math-circle-year-2/week-15/')
res={}
for band in ['k-1','grades-2-3','grades-4-5']:
    doc=pymupdf.open(BASE+f'week-15-{band}.pdf')
    for pno,page in enumerate(doc):
        dr=page.get_drawings()
        frame=[d['rect'] for d in dr if abs(d['rect'].width-417.6)<2 and abs(d['rect'].height-417.6)<2 and d.get('fill') is None]
        if not frame: continue
        f=frame[0]
        sx=f.width/6; sy=f.height/6
        cr=[]
        for d in dr:
            items=d['items']
            if len(items)==2 and all(it[0]=='l' for it in items):
                (_,p1,p2),(_,q1,q2)=items
                L1=(p1,p2);L2=(q1,q2)
                # horizontal one and vertical one
                h=[L for L in (L1,L2) if abs(L[0].y-L[1].y)<1e-3]
                v=[L for L in (L1,L2) if abs(L[0].x-L[1].x)<1e-3]
                if h and v:
                    cx=v[0][0].x; cy=h[0][0].y
                    hl=abs(h[0][0].x-h[0][1].x)/sx; vl=abs(v[0][0].y-v[0][1].y)/sy
                    cr.append((round((cx-f.x0)/sx-3,4),round(3-(cy-f.y0)/sy,4),round(hl,3),round(vl,3)))
        if cr:
            res[f'{band} p{pno+1}']=cr
            print(band,'page',pno+1,len(cr),'crosses')
            for c in cr: print('   ',c)
