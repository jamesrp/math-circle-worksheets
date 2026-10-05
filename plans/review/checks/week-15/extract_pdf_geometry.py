"""Extract site circles, site labels and probe crosses from the delivered student PDFs
and convert them back to map coordinates, independently of the generator."""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import fitz, json, sys
from collections import defaultdict
BASE=_os.path.join(ROOT, 'lowell-math-circle-year-2/week-15/')
S=0.966666667  # inches per unit claimed by source; we re-derive scale from frame below
def to_map(xpt,ypt,frame):
    (x0,y0,x1,y1)=frame
    sx=(x1-x0)/6; sy=(y1-y0)/6
    return ((xpt-x0)/sx-3, 3-(ypt-y0)/sy), sx, sy
out={}
for band in ['k-1','grades-2-3','grades-4-5']:
    doc=fitz.open(BASE+f'week-15-{band}.pdf')
    pages=[]
    for pno,page in enumerate(doc):
        dr=page.get_drawings()
        # frame: the largest rectangle-ish path of width ~5.8in
        frame=None
        for d in dr:
            r=d['rect']
            if abs(r.width-5.8*72)<2 and abs(r.height-5.8*72)<2:
                frame=(r.x0,r.y0,r.x1,r.y1)
        sites=[];crosses=[];other=[]
        for d in dr:
            r=d['rect']
            w,h=r.width,r.height
            cx,cy=(r.x0+r.x1)/2,(r.y0+r.y1)/2
            if d.get('fill') is not None and d['fill']==(1.0,1.0,1.0) and abs(w-2*0.062*S*72)<1.5 and abs(w-h)<0.5:
                sites.append(to_map(cx,cy,frame)[0])
            elif abs(w-0.09*S*72)<1.2 and abs(h-0.09*S*72)<1.2 and d.get('fill') is None:
                crosses.append(to_map(cx,cy,frame)[0])
            else:
                other.append((d.get('type'),round(r.x0,1),round(r.y0,1),round(r.x1,1),round(r.y1,1),d.get('fill'),d.get('dashes')))
        # labels near sites
        words=page.get_text('words')
        labels=[(w[4],to_map((w[0]+w[2])/2,(w[1]+w[3])/2,frame)[0]) for w in words if frame and frame[0]<w[0]<frame[2] and frame[1]<w[1]<frame[3]]
        _,sx,sy=to_map(0,0,frame)
        pages.append(dict(page=pno+1,frame_in=( (frame[2]-frame[0])/72,(frame[3]-frame[1])/72),sx=sx,sy=sy,
            sites=[(round(x,3),round(y,3)) for x,y in sites],crosses=[(round(x,3),round(y,3)) for x,y in crosses],
            labels=[(t,(round(x,2),round(y,2))) for t,(x,y) in labels],other=other))
    out[band]=pages
json.dump(out,open(_os.path.join(HERE, 'pdf_geometry.json'),'w'),indent=1)
for band,pages in out.items():
    print('=====',band)
    for p in pages:
        print(p['page'],'frame in',[round(v,3) for v in p['frame_in']],'scale pt/unit',round(p['sx'],3),round(p['sy'],3))
        print('  sites',p['sites'])
        print('  labels',p['labels'])
        print('  crosses',len(p['crosses']),sorted(p['crosses']))
        if p['other']:print('  other',p['other'])
