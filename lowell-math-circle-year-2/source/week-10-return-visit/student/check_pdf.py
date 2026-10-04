#!/usr/bin/env python3
"""Optional PyMuPDF output and full-page rendering check."""
import argparse
import json
from pathlib import Path
import re
import tempfile
from math import hypot
import fitz

DATA=json.loads((Path(__file__).resolve().parent/'towns.json').read_text())

def segment_distance(p,a,b):
    dx,dy=b.x-a.x,b.y-a.y
    t=max(0,min(1,((p.x-a.x)*dx+(p.y-a.y)*dy)/(dx*dx+dy*dy)))
    return hypot(p.x-a.x-t*dx,p.y-a.y-t*dy)

def center(rect):
    return rect.tl+(rect.br-rect.tl)/2

def active_graph_check(page,graph_data,directed):
    drawings=page.get_drawings()
    circles=[d for d in drawings if len(d['items'])==4 and all(x[0]=='c' for x in d['items'])]
    counters=[center(d['rect']) for d in circles if abs(d['rect'].width-10.08)<.1]
    islands=[center(d['rect']) for d in circles if abs(d['rect'].width-21.6)<.1]
    assert len(counters)==sum(len(t['edges']) for t in graph_data),'actual counter count'
    assert len(islands)==sum(len(t['vertices']) for t in graph_data),'actual island count'
    nodeindex=edgeindex=0
    actual_graphs=[]
    for t in graph_data:
        nodes=dict(zip(t['vertices'],islands[nodeindex:nodeindex+len(t['vertices'])]))
        nodeindex+=len(t['vertices'])
        origin=next(iter(nodes))
        for v in nodes:
            expectedx=72*(t['vertices'][v][0]-t['vertices'][origin][0])
            expectedy=-72*(t['vertices'][v][1]-t['vertices'][origin][1])
            assert abs(nodes[v].x-nodes[origin].x-expectedx)<.03,'actual x scale'
            assert abs(nodes[v].y-nodes[origin].y-expectedy)<.03,'actual y scale'
        for a,b in t['edges']:
            expected=nodes[a]+(nodes[b]-nodes[a])/2
            actual=counters[edgeindex]; edgeindex+=1
            assert hypot(actual.x-expected.x,actual.y-expected.y)<.03,'actual street midpoint'
        actual_graphs.append((t,nodes))
    result={'actual_counter_count':len(counters),'actual_island_count':len(islands)}
    if directed:
        arrows=[d for d in drawings if d.get('fill')==(0.,0.,0.) and
                min(hypot(d['rect'].x0-c.x,d['rect'].y0-c.y) for c in islands)<70]
        assert len(arrows)==len(counters),'actual arrow count'
        n=0
        for t,nodes in actual_graphs:
            for a,b in t['edges']:
                arrow=arrows[n];n+=1
                tip=arrow['items'][0][1]
                dx,dy=nodes[b].x-nodes[a].x,nodes[b].y-nodes[a].y
                parameter=((tip.x-nodes[a].x)*dx+(tip.y-nodes[a].y)*dy)/(dx*dx+dy*dy)
                perpendicular=abs((tip.x-nodes[a].x)*dy-(tip.y-nodes[a].y)*dx)/hypot(dx,dy)
                assert .84<parameter<.87 and perpendicular<.03,(t['id'],a,b,'actual arrow direction')
                assert all(x[0]=='l' for x in arrow['items']),'arrow footprint shape'
        counter_clearance=min(segment_distance(c,item[1],item[2])-27-d['width']/2
                              for d in arrows for item in d['items'] for c in counters)
        island_clearance=min(segment_distance(c,item[1],item[2])-10.8-d['width']/2
                             for d in arrows for item in d['items'] for c in islands)
        assert counter_clearance>1,'actual arrow covered by .75-inch counter'
        assert island_clearance>1,'actual arrow covered by island'
        result.update({'actual_arrow_count':len(arrows),
                       'minimum_counter_arrow_clearance_pt':round(counter_clearance,3),
                       'minimum_island_arrow_clearance_pt':round(island_clearance,3)})
    return result

parser=argparse.ArgumentParser()
parser.add_argument('pdf',type=Path)
parser.add_argument('--render-dir',type=Path)
args=parser.parse_args()
out=args.render_dir or Path(tempfile.mkdtemp(prefix='week10-pdf-qa-'))
out.mkdir(parents=True,exist_ok=True)
doc=fitz.open(args.pdf)
assert len(doc)==7,(len(doc),'expected seven pages')
problems=(1,1,1,2,2,3,3)
bands=('K–5','2–5','2–5','2–5','2–5','4–5','4–5')
towns=(['1','2','3','4'],['5','6'],['7','8'],['1','2'],['3','4'],[],[])
records=[]
for i,page in enumerate(doc):
    assert tuple(round(x,3) for x in page.rect)==(0.,0.,612.,792.)
    text=page.get_text()
    expected=f'Problem {problems[i]}:' if i in (0,3,5) else f'Problem {problems[i]} continued.'
    assert expected in text,(i+1,'wrong problem')
    assert f'Grades {bands[i]}' in text,(i+1,'wrong band')
    assert re.findall(r'Town (\d+)',text)==towns[i],(i+1,'town labels')
    assert 'Bellingham Math Circle / Week 10 / F10-RV-v1' in text,(i+1,'footer')
    if i==5:
        prefix=text.split('Problem 3:')[0]
        figures=[line.strip() for line in prefix.splitlines()]
        assert all(figures.count(word)==1 for word in ('01','11','10')),(i+1,'window-example outputs')
    assert 'Name' not in text and 'Date' not in text
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line['spans']:
                r=fitz.Rect(span['bbox'])
                assert page.rect.contains(r),(i+1,span['text'],tuple(r))
    for drawing in page.get_drawings():
        assert page.rect.contains(drawing['rect']),(i+1,'off-page vector',tuple(drawing['rect']))
    page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(out/f'page-{i+1:02}.png')
    (out/f'page-{i+1:02}.txt').write_text(text)
    record={'page':i+1,'problem':problems[i],'band':bands[i],
            'town_labels':towns[i],'text_characters':len(text),'vector_drawings':len(page.get_drawings())}
    if i<3:
        graph_data=DATA['directed'][:4] if i==0 else DATA['directed'][4:6] if i==1 else DATA['directed'][6:]
        record.update(active_graph_check(page,graph_data,True))
    elif i<5:
        graph_data=DATA['undirected'][:2] if i==3 else DATA['undirected'][2:]
        record.update(active_graph_check(page,graph_data,False))
    records.append(record)
alltext='\n'.join(page.get_text() for page in doc)
assert all(alltext.count(f'Problem {n}:')==1 for n in (1,2,3)),'duplicate numbered problems'
(out/'pdf-check.json').write_text(json.dumps({'pdf':str(args.pdf.resolve()),'pages':records},indent=2)+'\n')
print(f'PASS: seven pages; labels, bands, bounds and vectors checked. Renders: {out}')
