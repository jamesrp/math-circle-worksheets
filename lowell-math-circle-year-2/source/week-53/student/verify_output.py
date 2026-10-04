#!/usr/bin/env python3
"""Read the delivered PDF: reconstruct every graph, price, selected link and dot.
Also compare clean rebuilds by extracted text, page dimensions and rendered pixels.
"""
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import pymupdf

# Independent page inventory, in visual order. Unlike diagrams.py, this reader
# reconstructs vertices and edges from PDF drawing paths, not generated TikZ.
INVENTORY=[
 [('convention',.72,True,True,()),('convention',.72,True,True,('XY','YZ')),('convention',.72,False,False,('XY','YZ')),('triangle_one',1.65,True,True,()),('triangle_two',1.65,True,True,())],
 [('four_ties',2.25,True,True,()),('four_ties',.75,False,False,()),('four_ties',.75,False,False,()),('four_ties',.75,False,False,())],
 [('four_trap',2.25,False,True,()),('four_trap',.9,False,False,()),('four_trap',.9,False,False,())],
 [('five_ties',2.25,False,True,()),('five_ties',.78,False,False,()),('five_ties',.78,False,False,()),('five_ties',.78,False,False,())],
 [('swap_demo',.72,False,True,('UV','VW')),('swap_demo',.72,False,True,('UV','UW','VW')),('swap_demo',.72,False,True,('UV','UW')),('swaps',1.9,False,True,('AB','AD','AC')),('swaps',1.9,False,True,('AB','BC','CD'))],
 [('six_cert',1.7,False,True,())],
 [('price_design',1.75,False,True,()),('price_design',1.75,False,True,())],
 [('six_cert',1.25,False,True,('AB','BC','CD','DE','EF')),('six_cert',1.25,False,True,('AB','AC','BD','DE','DF'))],
 [('distinct',2.9,False,True,())]
]


def dist(a,b):return math.hypot(a[0]-b[0],a[1]-b[1])
def center(r):return ((r.x0+r.x1)/2,(r.y0+r.y1)/2)
def key(a,b):return ''.join(sorted((a,b)))
def style(d,width):return d['width'] is not None and abs(d['width']-width)<.02


def inspect(pdf):
    data=json.loads(Path(__file__).with_name('networks.json').read_text())
    doc=pymupdf.open(pdf)
    assert len(doc)==9
    pages=[]
    for i,page in enumerate(doc):
        assert tuple(page.rect)==(0,0,612,792)
        text=page.get_text()
        band='Grades 2–5' if i<4 else 'Grades 4–5'
        assert f'Week 53 / Connecting networks / {band}' in text
        assert f'Problem {i+1}:' in text
        assert 'Bellingham Math Circle / Week 53 / W53-networks-v1' in text
        assert str(i+1) in [w[4] for w in page.get_text('words') if w[1]>750]
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines',[]):
                for span in line['spans']:
                    r=pymupdf.Rect(span['bbox'])
                    assert r.x0>=45 and r.x1<=568 and r.y0>=24 and r.y1<=775, (i+1,span['text'],r)
        drawings=page.get_drawings()
        nodes=[d for d in drawings if style(d,.897) and d['type']=='fs' and all(x[0]=='c' for x in d['items'])]
        thin=[d for d in drawings if style(d,.648) and d['type']=='s' and [x[0] for x in d['items']]==['l']]
        thick=[d for d in drawings if style(d,2.391) and d['type']=='s' and [x[0] for x in d['items']]==['l']]
        labels=[w for w in page.get_text('words') if len(w[4])==1 and w[4].isupper()]
        circles=[center(d['rect']) for d in nodes]
        node_names={}
        for n,c in enumerate(circles):
            closest=min(labels,key=lambda w:dist(c,((w[0]+w[2])/2,(w[1]+w[3])/2)))
            assert dist(c,((closest[0]+closest[2])/2,(closest[1]+closest[3])/2))<3
            node_names[n]=closest[4]
        def line_ids(d):
            ends=d['items'][0][1:3]
            ids=[]
            for point in ends:
                found=min(range(len(circles)),key=lambda n:dist(circles[n],point))
                assert dist(circles[found],point)<.08
                ids.append(found)
            return ids
        thin_ids=[line_ids(d) for d in thin]
        thick_ids=[line_ids(d) for d in thick]
        components=[]
        rest=set(range(len(circles)))
        while rest:
            reached={next(iter(rest))}
            changed=True
            while changed:
                changed=False
                for a,b in thin_ids:
                    if a in reached or b in reached:
                        before=len(reached);reached.update((a,b));changed|=len(reached)!=before
            rest-=reached;components.append(reached)
        # TikZ diagrams align by their full bounding box; node centers may
        # differ slightly vertically. Group graph rows before left-right order.
        components.sort(key=lambda c:(round(min(circles[n][1] for n in c)/20),min(circles[n][0] for n in c)))
        assert len(components)==len(INVENTORY[i]),(i+1,len(components))
        price_boxes=[d['rect'] for d in drawings if d['type']=='f' and [x[0] for x in d['items']]==['re'] and d['fill']==(1.,1.,1.)]
        dots=[center(d['rect']) for d in drawings if d['type']=='f' and all(x[0]=='c' for x in d['items'])]
        graph_reports=[]
        for component,(name,scale,dotted,priced,purchase) in zip(components,INVENTORY[i]):
            g=data[name];actual={node_names[n]:circles[n] for n in component}
            assert set(actual)=={v[0] for v in g['vertices']}
            edges={key(node_names[a],node_names[b]) for a,b in thin_ids if a in component}
            bought={key(node_names[a],node_names[b]) for a,b in thick_ids if a in component}
            assert edges=={key(a,b) for a,b,w in g['edges']},(i+1,name,edges)
            assert bought==set(purchase),(i+1,name,bought)
            source={v:(x,y) for v,x,y in g['vertices']}
            anchor=g['vertices'][0][0];sx,sy=source[anchor];ax,ay=actual[anchor]
            cm=72/2.54
            def point(x,y):return ax+(x-sx)*scale*cm,ay-(y-sy)*scale*cm
            for v,x,y in g['vertices']:
                assert dist(actual[v],point(x,y))<.08,(i+1,name,v)
            price_results=[]
            compact=scale<1
            for a,b,w in g['edges']:
                if not priced:continue
                x1,y1=source[a];x2,y2=source[b]
                frac=g.get('label_fractions',{}).get(key(a,b),.5)
                x,y=x1+(x2-x1)*frac,y1+(y2-y1)*frac
                dx,dy=x2-x1,y2-y1;length=math.hypot(dx,dy)
                ox,oy=-dy/length,dx/length
                if abs(dx)<1e-6:ox,oy=-1,0
                if abs(dy)<1e-6:ox,oy=0,-1 if y1<.1 else 1
                off=.18 if compact else .32
                expected=point(x+ox*off/scale,y+oy*off/scale)
                box=min(price_boxes,key=lambda r:dist(center(r),expected))
                assert dist(center(box),expected)<.15,(i+1,name,key(a,b),expected,box)
                inside=[z[4] for z in page.get_text('words') if box.contains(pymupdf.Point((z[0]+z[2])/2,(z[1]+z[3])/2))]
                assert inside==([] if w is None else [str(w)]),(i+1,name,key(a,b),inside,w)
                count=sum(box.contains(pymupdf.Point(d)) for d in dots)
                assert count==(w if dotted else 0),(i+1,name,key(a,b),count,w)
                price_results.append({'link':key(a,b),'price':w,'price_dots':count})
            minimum_spacing=min(dist(actual[a],actual[b]) for a,b in __import__('itertools').combinations(actual,2))/cm*10
            graph_reports.append({'map':name,'available_links':sorted(edges),'bought_links':sorted(bought),'prices':price_results,'minimum_place_spacing_mm':round(minimum_spacing,2)})
        pages.append({'page':i+1,'band':band,'graphs':graph_reports,'thin_links':len(thin),'bought_links':len(thick),'place_circles':len(nodes)})
    return {'pdf':str(pdf.resolve()),'page_count':len(doc),'dimensions_points':[612,792],'pdf_graphs_prices_dots_and_geometry_verified':True,'pages':pages}


def compare(a,b):
    da=pymupdf.open(a);db=pymupdf.open(b);assert len(da)==len(db)
    out=[]
    for i,(pa,pb) in enumerate(zip(da,db)):
        assert pa.get_text()==pb.get_text(),('text',i+1)
        assert pa.rect==pb.rect,('dimensions',i+1)
        va=pa.get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False)
        vb=pb.get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False)
        assert (va.width,va.height,va.samples)==(vb.width,vb.height,vb.samples),('pixels',i+1)
        out.append({'page':i+1,'text_equal':True,'dimensions_equal':True,'pixels_144dpi_equal':True,'pixels_sha256':hashlib.sha256(va.samples).hexdigest()})
    return out


def main():
    p=argparse.ArgumentParser();p.add_argument('pdf',type=Path);p.add_argument('--compare',type=Path);p.add_argument('--report',type=Path);args=p.parse_args()
    report=inspect(args.pdf)
    if args.compare:report['rebuild_comparison']=compare(args.pdf,args.compare)
    text=json.dumps(report,indent=2)+'\n'
    if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(text)
    else:print(text)
    print('Delivered PDF geometry, links, purchases, price labels/dots and page checks passed.')


if __name__=='__main__':main()
