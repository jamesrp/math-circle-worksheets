#!/usr/bin/env python3
"""Independent CRITIC-MATH checks. Does not import or call writer checkers."""
import itertools,json,math,hashlib,argparse
from pathlib import Path
import pymupdf as fitz
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--pdf',type=Path,required=True,help='Student PDF to inspect')
parser.add_argument('--towns',type=Path,default=HERE/'towns.json',help='Bundled authoritative drawn-town data')
parser.add_argument('--out',type=Path,default=HERE,help='Directory for the independent JSON result')
args=parser.parse_args()
DATA=json.loads(args.towns.read_text())
PDF=fitz.open(args.pdf)
OUT=args.out
OUT.mkdir(parents=True,exist_ok=True)
res={'pdf_sha256':hashlib.sha256(args.pdf.read_bytes()).hexdigest(),'towns_sha256':hashlib.sha256(args.towns.read_bytes()).hexdigest()}

def routes(edges,start,directed):
    full=(1<<len(edges))-1
    found=[]
    def visit(v,mask,path):
        if mask==full:
            found.append(path);return
        for i,(a,b) in enumerate(edges):
            if mask>>i&1: continue
            if a==v: visit(b,mask|1<<i,path+[b])
            elif not directed and b==v: visit(a,mask|1<<i,path+[a])
    visit(start,0,[start])
    return found
res['directed']=[]
for t in DATA['directed']:
    r={s:routes(t['edges'],s,True) for s in t['vertices']}
    deg={s:[sum(b==s for a,b in t['edges']),sum(a==s for a,b in t['edges'])] for s in t['vertices']}
    res['directed'].append({'id':t['id'],'in_out':deg,'routes_by_start':r})
res['undirected']=[]
for t in DATA['undirected']:
    r=routes(t['edges'],t['start'],False)
    first={b:[] for a,b in t['edges'] if a==t['start']}
    first.update({a:[] for a,b in t['edges'] if b==t['start']})
    for path in r:first[path[1]].append(path)
    res['undirected'].append({'id':t['id'],'start':t['start'],'routes_by_first_destination':first})
# Check concrete arrow-action demonstration by state transition, separate from Euler search.
D=DATA['demonstration']
for i,st in enumerate(D['states']):
    assert st['used']==list(range(i))
    assert st['token']==['X','Y','Z'][i]
    if i:
        a,b=D['edges'][i-1]
        assert D['states'][i-1]['token']==a and st['token']==b
res['arrow_demo']={'token_sequence':['X','Y','Z'],'remaining_counters':[2,1,0]}

def words(n):return (''.join(x) for x in itertools.product('01',repeat=n))
def linear_windows(s,k):return [s[i:i+k] for i in range(max(0,len(s)-k+1))]
def circular_windows(s,k):return [''.join(s[(i+j)%len(s)] for j in range(k)) for i in range(len(s))]
target=set(words(3))
lin={n:[s for s in words(n) if set(linear_windows(s,3))==target] for n in range(1,11)}
circ={n:[s for s in words(n) if set(circular_windows(s,3))==target] for n in range(1,9)}
necklaces=sorted({min(s[i:]+s[:i] for i in range(len(s))) for s in circ[8]})
res['windows']={'linear_example':{'input':'0110','windows':linear_windows('0110',2)},'circular_example':{'clockwise':'011','windows':circular_windows('011',2)},'linear_lower_bound':'L-2 >= 8, so L >= 10','linear_counts':{str(n):len(v) for n,v in lin.items()},'linear_minimizers':lin[10],'circular_lower_bound':'L windows, one per tile, so L >= 8','circular_counts':{str(n):len(v) for n,v in circ.items()},'circular_minimizers':circ[8],'necklaces_mod_rotation':necklaces,'witness_linear':linear_windows('0001011100',3),'witness_circle':circular_windows('00010111',3)}
# Parse rendered vector shapes, then label each island by its actual PDF text.
def center(d):return tuple((d['rect'][k]+d['rect'][k+2])/2 for k in (0,1))
def dist(a,b):return math.hypot(a[0]-b[0],a[1]-b[1])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def diff(a,b):return (a[0]-b[0],a[1]-b[1])
def segdist(p,a,b):
    v=diff(b,a);w=diff(p,a);q=max(0,min(1,dot(w,v)/dot(v,v))) if dot(v,v) else 0
    return dist(p,(a[0]+q*v[0],a[1]+q*v[1]))
def polydist(p,vs):
    inside=False
    for a,b in zip(vs,vs[1:]+vs[:1]):
        if (a[1]>p[1])!=(b[1]>p[1]) and p[0] < a[0]+(b[0]-a[0])*(p[1]-a[1])/(b[1]-a[1]): inside=not inside
    return 0 if inside else min(segdist(p,a,b) for a,b in zip(vs,vs[1:]+vs[:1]))
def circles(draws,diam):
    return [d for d in draws if d['fill']==(1.,1.,1.) and len(d['items'])==4 and all(v[0]=='c' for v in d['items']) and abs(d['rect'].width-diam)<.02 and abs(d['rect'].height-diam)<.02]
def spans(p):
    return [sp for b in p.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for sp in l['spans']]
def spcenter(sp):
    b=sp['bbox'];return ((b[0]+b[2])/2,(b[1]+b[3])/2)
# Regions avoid depending on draw sequence or writer output classifications.
assignments=[('directed',1,0, (0,160,306,390)),('directed',2,0,(306,160,612,390)),('directed',3,0,(0,390,306,700)),('directed',4,0,(306,390,612,700)),('directed',5,1,(0,80,612,350)),('directed',6,1,(0,350,612,700)),('directed',7,2,(0,80,612,350)),('directed',8,2,(0,350,612,700)),('undirected',1,3,(0,90,612,370)),('undirected',2,3,(0,370,612,700)),('undirected',3,4,(0,70,612,330)),('undirected',4,4,(0,330,612,700))]
res['rendered_towns']=[]
all_mins=[]
for kind,tid,pi,region in assignments:
    t=next(t for t in DATA[kind] if t['id']==tid)
    p=PDF[pi];dr=p.get_drawings();ss=spans(p)
    def inreg(d):
        x,y=center(d);return region[0]<x<region[2] and region[1]<y<region[3]
    islands=[d for d in circles(dr,21.6) if inreg(d)]
    counters=[d for d in circles(dr,10.08) if inreg(d)]
    streets=[d for d in dr if inreg(d) and d['type']=='s' and len(d['items'])==1 and d['items'][0][0]=='l' and abs(d['width']-1.1955)<.01]
    arrows=[d for d in dr if inreg(d) and d['fill']==(0.,0.,0.) and len(d['items'])==4 and all(v[0]=='l' for v in d['items']) and abs(d['width']-1.1955)<.01]
    iv={}
    for d in islands:
        cs=center(d)
        near=[sp for sp in ss if sp['text'] in t['vertices'] and dist(cs,spcenter(sp))<5]
        assert len(near)==1,(kind,tid,cs,near)
        iv[near[0]['text']]=cs
    assert set(iv)==set(t['vertices']),(kind,tid,iv)
    assert len(streets)==len(t['edges']) and len(counters)==len(t['edges']),(kind,tid,len(streets),len(counters))
    assert len(arrows)==(len(streets) if kind=='directed' else 0)
    # All rendered coordinates use the source's inch scale with a translation only.
    origins=[(iv[v][0]-72*xy[0],iv[v][1]+72*xy[1]) for v,xy in t['vertices'].items()]
    max_origin_drift=max(dist(a,b) for a in origins for b in origins)
    assert max_origin_drift<.02,(kind,tid,max_origin_drift)
    scales=[]
    for a,b in itertools.combinations(t['vertices'],2):
        scales.append(dist(iv[a],iv[b])/dist(t['vertices'][a],t['vertices'][b]))
    rendered_edges=[]; arrow_checks=[]
    for d in streets:
        _,aa,bb=d['items'][0];aa=tuple(aa);bb=tuple(bb)
        a=min(iv,key=lambda v:dist(aa,iv[v]));b=min(iv,key=lambda v:dist(bb,iv[v]))
        assert dist(aa,iv[a])<.005 and dist(bb,iv[b])<.005
        if kind=='directed':
            near_arrows=[ad for ad in arrows if segdist(center(ad),aa,bb)<1.5]
            # Each arrow is longitudinally near .86 of this edge, separating collinear neighbor streets.
            near_arrows=[ad for ad in near_arrows if .78 < dot(diff(center(ad),aa),diff(bb,aa))/dot(diff(bb,aa),diff(bb,aa)) < .91]
            assert len(near_arrows)==1,(kind,tid,a,b,len(near_arrows))
            ad=near_arrows[0];vs=[tuple(v[1]) for v in ad['items']]
            # First polygon point is tip: verify maximal projection in the street's actual draw direction.
            u=diff(bb,aa);projs=[dot(diff(v,aa),u)/dot(u,u) for v in vs]
            assert projs[0]>max(projs[1:])+1e-5
            assert (a,b) in [tuple(e) for e in t['edges']],(kind,tid,a,b)
            arrow_checks.append({'edge':a+b,'tip_fraction':projs[0]})
        else:assert frozenset((a,b)) in [frozenset(e) for e in t['edges']]
        rendered_edges.append(a+b)
        mid=((aa[0]+bb[0])/2,(aa[1]+bb[1])/2)
        assert min(dist(mid,center(cd)) for cd in counters)<.005
    # Actual printed star nearest island, include independent placement check.
    star=None
    if kind=='undirected':
        st=[sp for sp in ss if sp['text']=='⋆' and region[0]<spcenter(sp)[0]<region[2] and region[1]<spcenter(sp)[1]<region[3]]
        assert len(st)==1
        star=min(iv,key=lambda v:dist(iv[v],spcenter(st[0])))
        assert star==t['start'],(kind,tid,star,t['start'])
    cc=min(dist(center(a),center(b))-54 for a,b in itertools.combinations(counters,2))/72
    ci=min(dist(center(a),center(b))-27-10.8-b['width']/2 for a in counters for b in islands)/72
    # Compare every arrow's full filled polygon plus stroke against every full counter disk and every drawn island disk.
    ac=ai=None
    if arrows:
        ac=min(polydist(center(cd),[tuple(v[1]) for v in ad['items']])-27-ad['width']/2 for cd in counters for ad in arrows)/72
        ai=min(polydist(center(isl),[tuple(v[1]) for v in ad['items']])-10.8-isl['width']/2-ad['width']/2 for isl in islands for ad in arrows)/72
        assert ac>0 and ai>0,(kind,tid,ac,ai)
    assert cc>=0 and ci>0,(kind,tid,cc,ci)
    # Counter footprints stay clear of an unrelated street, and all islands are distinct.
    cs=min(segdist(center(cd),tuple(sd['items'][0][1]),tuple(sd['items'][0][2]))-27-sd['width']/2 for cd in counters for sd in streets if dist(center(cd),((sd['items'][0][1].x+sd['items'][0][2].x)/2,(sd['items'][0][1].y+sd['items'][0][2].y)/2))>.005)/72
    assert cs>0,(kind,tid,cs)
    rec={'kind':kind,'id':tid,'page':pi+1,'rendered_edges':rendered_edges,'star':star,'scale_pdf_points_per_inch':[min(scales),max(scales)],'max_origin_drift_points':max_origin_drift,'islands':len(islands),'counters':len(counters),'arrows':len(arrows),'arrow_direction_checks':arrow_checks,'clearance_inches':{'counter_counter':cc,'counter_island_including_stroke':ci,'arrow_counter_including_stroke':ac,'arrow_island_including_strokes':ai,'counter_unrelated_street_including_stroke':cs}}
    res['rendered_towns'].append(rec)

# Read convention demonstrations from actual vector shapes and printed labels.
res['rendered_conventions']={}
p=PDF[0];dr=p.get_drawings();ss=spans(p)
demo_islands=sorted(circles(dr,14.4),key=lambda d:center(d)[0])
rings=sorted([d for d in dr if len(d['items'])==4 and all(i[0]=='c' for i in d['items']) and d['fill'] is None and abs(d['rect'].width-23.04)<.02],key=lambda d:center(d)[0])
demo_counters=circles(dr,5.76)
assert len(demo_islands)==9 and len(rings)==3 and len(demo_counters)==3
for i in range(3):
    isl=demo_islands[3*i:3*i+3]
    labels=[]
    for d in isl:
        near=[sp for sp in ss if sp['text'] in ['X','Y','Z'] and dist(center(d),spcenter(sp))<5]
        assert len(near)==1
        labels.append(near[0]['text'])
    assert labels==['X','Y','Z']
    assert dist(center(rings[i]),center(isl[i]))<.005
    xleft=center(isl[0])[0];xright=center(isl[2])[0]
    cnt=[d for d in demo_counters if xleft<center(d)[0]<xright]
    assert len(cnt)==2-i
    demo_lines=[d for d in dr if d['type']=='s' and len(d['items'])==1 and d['items'][0][0]=='l' and abs(d['width']-.797)<.01 and xleft-.01 <= center(d)[0] <= xright+.01 and abs(center(d)[1]-center(isl[0])[1])<.01]
    assert len(demo_lines)==2
    demo_lines.sort(key=lambda d:center(d)[0])
    for j,d in enumerate(demo_lines):
        assert bool(d['dashes']!='[] 0')==(j<i)
    darr=[d for d in dr if d['fill']==(0.,0.,0.) and abs(d['width']-.797)<.01 and xleft<center(d)[0]<xright]
    assert len(darr)==2-i
    for d in darr:
        vs=[tuple(v[1]) for v in d['items']]
        assert vs[0][0]>max(v[0] for v in vs[1:])
res['rendered_conventions']['arrow_action']={'labels_per_panel':['XYZ']*3,'walker':['X','Y','Z'],'unused_counters':[2,1,0],'used_streets_dashed':True,'unused_arrows_point_X_to_Z':True}
p=PDF[5];dr=p.get_drawings();ss=spans(p)
frames=sorted([d for d in dr if d['type']=='s' and abs(d['width']-1.4944)<.01],key=lambda d:center(d)[0])
digits=[sp for sp in ss if sp['text'] in ['0','1'] and 90<sp['bbox'][1]<120]
assert len(frames)==3 and len(digits)==12
rows=[sorted(digits,key=lambda sp:spcenter(sp)[0])[4*i:4*i+4] for i in range(3)]
for i,(fr,row) in enumerate(zip(frames,rows)):
    assert ''.join(sp['text'] for sp in row)=='0110'
    inside=[sp for sp in row if fitz.Point(spcenter(sp)) in fr['rect']]
    assert ''.join(sp['text'] for sp in inside)==['01','11','10'][i]
    labels=[sp['text'] for sp in ss if sp['text'] in ['01','11','10'] and abs(spcenter(sp)[0]-center(fr)[0])<30 and sp['bbox'][1]>130 and sp['bbox'][1]<155]
    assert labels==[['01'],['11'],['10']][i]
res['rendered_conventions']['linear_windows']={'printed_row_per_panel':['0110']*3,'framed_and_labeled':['01','11','10']}
p=PDF[6];dr=p.get_drawings();ss=spans(p)
buttoncircles=[d for d in circles(dr,21.6) if d['rect'].y0<180]
assert len(buttoncircles)==3
base=next(d for d in dr if d['type']=='s' and len(d['items'])==4 and all(v[0]=='c' for v in d['items']) and abs(d['rect'].width-77.76)<.01)
origin=center(base)
clockwise=sorted(buttoncircles,key=lambda d:math.atan2(center(d)[0]-origin[0],origin[1]-center(d)[1])%(2*math.pi))
top=min(range(3),key=lambda i:center(clockwise[i])[1])
clockwise=clockwise[top:]+clockwise[:top]
actualword=''
for d in clockwise:
    near=[sp for sp in ss if sp['text'] in ['0','1'] and dist(center(d),spcenter(sp))<5]
    assert len(near)==1
    actualword+=near[0]['text']
assert actualword=='011'
arc=next(d for d in dr if d['type']=='s' and abs(d['width']-1.3948)<.01)
assert dist(tuple(arc['items'][0][1]),center(clockwise[2]))<.03
assert dist(tuple(arc['items'][-1][-1]),center(clockwise[0]))<.03
for item in arc['items']:
    assert item[0]=='c'
    a,b,c,d=[tuple(v) for v in item[1:]]
    for t in [0,.25,.5,.75,1]:
        q=tuple((1-t)**3*a[k]+3*(1-t)**2*t*b[k]+3*(1-t)*t*t*c[k]+t**3*d[k] for k in [0,1])
        v=tuple(3*(1-t)**2*(b[k]-a[k])+6*(1-t)*t*(c[k]-b[k])+3*t*t*(d[k]-c[k]) for k in [0,1])
        r=diff(q,origin)
        assert r[0]*v[1]-r[1]*v[0]>0 # clockwise orientation in PDF's downward-y coordinates
callout=next(d for d in dr if d['type']=='s' and abs(d['width']-1.29515)<.01 and d['rect'].y0<200)
inside=[sp['text'] for sp in ss if fitz.Point(spcenter(sp)) in callout['rect']]
assert inside==['10']
outer_arrow=next(d for d in dr if d['fill']==(0.,0.,0.) and d['rect'].x0<220 and d['rect'].y0<110)
vs=[tuple(v[1]) for v in outer_arrow['items']]
r=diff(vs[0],origin);v=diff(vs[0],vs[2])
assert r[0]*v[1]-r[1]*v[0]>0
res['rendered_conventions']['circular_windows']={'clockwise_buttons':actualword,'marked_wraparound_arc':'10','clockwise_arrow':True,'boxed_wraparound':'10','outputs':['01','11','10']}
for pi in [5,6]:
    p=PDF[pi];dr=p.get_drawings();ss=spans(p)
    printed=[sp for sp in ss if sp['text'] in target]
    assert sorted(sp['text'] for sp in printed)==sorted(target)
    cards=[d for d in dr if len(d['items'])==1 and d['items'][0][0]=='re' and abs(d['rect'].width-97.2)<.02]
    assert len(cards)==8
    for cd in cards:
        inside=[sp['text'] for sp in printed if fitz.Point(spcenter(sp)) in cd['rect']]
        assert len(inside)==1
res['rendered_conventions']['password_cards']={'page_6':sorted(target),'page_7':sorted(target),'all_eight_distinct_cards':True}
assert len(PDF)==7 and all(abs(p.rect.width-612)<.01 and abs(p.rect.height-792)<.01 for p in PDF)
res['coverage']={'pages':7,'shared_investigations':3,'directed_towns':8,'undirected_towns':4,'active_edges':sum(len(t['edges']) for typ in ['directed','undirected'] for t in DATA[typ]),'all_page_sizes_US_Letter':True,'physical_rehearsal':'untested','classroom_piloting':'untested'}

(OUT/'independent-check.json').write_text(json.dumps(res,indent=2))
for kind in ['directed','undirected']:
    for r in res[kind]:print(kind,json.dumps(r))
print('WINDOWS',json.dumps(res['windows']))
for r in res['rendered_towns']:print('GEOMETRY',r['kind'],r['id'],'page',r['page'],r['clearance_inches'])
print('PASSED independent enumeration and all 12 actual rendered town checks.')
