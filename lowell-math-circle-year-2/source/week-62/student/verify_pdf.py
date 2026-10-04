#!/usr/bin/env python3
"""Independent Week 62 audit. Reads actual PDF vectors/text and raw TikZ only.
Adapted from the independent reviewer checker; reads actual PDF and TikZ,
not builder JSON or finite-check outputs.
"""
from pathlib import Path
from itertools import combinations, product, permutations
from collections import Counter, deque
import re, json, hashlib, math, argparse
import pymupdf
parser=argparse.ArgumentParser()
parser.add_argument("--pdf",required=True,type=Path)
parser.add_argument("--tex",required=True,type=Path)
parser.add_argument("--report",required=True,type=Path)
args=parser.parse_args()
PDF=args.pdf
TEX=args.tex

def normedge(a,b): return ''.join(sorted((a,b)))
def legal(v,e,c): return all(c[a]!=c[b] for a,b in e)
def colorings(v,e,k):
 return [dict(zip(v,t)) for t in product(range(1,k+1),repeat=len(v)) if all(t[v.index(a)]!=t[v.index(b)] for a,b in e)]
def clique(v,e):
 for k in range(len(v),0,-1):
  groups=[s for s in combinations(v,k) if all(normedge(a,b) in e for a,b in combinations(s,2))]
  if groups:return k,[''.join(s) for s in groups]
 return 0,[]
def cycles(v,e):
 adj={a:[b for b in v if normedge(a,b) in e] for a in v}
 found=set()
 def walk(path):
  for b in adj[path[-1]]:
   if b==path[0] and len(path)>=3:
    c=tuple(path)
    variants=[c[i:]+c[:i] for i in range(len(c))]
    d=c[::-1]; variants += [d[i:]+d[:i] for i in range(len(d))]
    found.add(min(variants))
   elif b not in path:walk(path+[b])
 for a in v:walk([a])
 return sorted(''.join(c)+c[0] for c in found)
def firstfit(v,e,order):
 c={}; trace=[]
 for a in order:
  blocked={c[b] for b in c if normedge(a,b) in e}
  t=next(i for i in range(1,len(v)+1) if i not in blocked)
  c[a]=t; trace.append([a,t,sorted(blocked)])
 assert legal(v,e,c)
 return max(c.values(),default=0),c,trace
def shortrepair(v,e,start,maxslots=2):
 q=deque([(start,[])]);seen={tuple(start[a] for a in v)}
 while q:
  c,moves=q.popleft()
  if len(set(c.values()))<=maxslots:return moves,c
  for a in v:
   for t in range(1,max(start.values())+1):
    if t==c[a]:continue
    nc=dict(c);nc[a]=t;key=tuple(nc[a] for a in v)
    if key not in seen and legal(v,e,nc):
     seen.add(key);q.append((nc,moves+[[a,c[a],t]]))
 return None

def distance_to_segment(p,a,b):
 dx,dy=b[0]-a[0],b[1]-a[1]
 t=max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/(dx*dx+dy*dy)))
 return math.hypot(p[0]-(a[0]+t*dx),p[1]-(a[1]+t*dy)),t

tex=TEX.read_text(); texgraphs=[]
for m in re.finditer(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}',tex,re.S):
 block=m.group()
 coords={a:(float(x),float(y)) for a,x,y in re.findall(r'\\coordinate \(([A-H])\) at \(([-\d.]+),([-\d.]+)\);',block)}
 if not coords:continue
 problem=int(re.findall(r'\\textbf\{Problem (\d+):\}',tex[:m.start()])[-1])
 idx=1+sum(g['problem']==problem for g in texgraphs)
 edges=sorted(normedge(a,b) for a,b in re.findall(r'\\draw\[conflict\] \(([A-H])\) -- \(([A-H])\);',block))
 texgraphs.append({'id':f'P{problem}-{idx}','page':problem,'problem':problem,'coords_cm':coords,'source_edges':edges})
assert len(texgraphs)==18

doc=pymupdf.open(PDF);checks=[]
for pi,page in enumerate(doc,1):
 graphs=[g for g in texgraphs if g['page']==pi]
 drawings=page.get_drawings()
 circles=[d for d in drawings if len(d['items'])==4 and all(it[0]=='c' for it in d['items']) and abs(d['rect'].width-56.692913)<0.05 and abs(d['rect'].height-56.692913)<0.05]
 spans=[s for block in page.get_text('dict')['blocks'] if 'lines' in block for line in block['lines'] for s in line['spans']]
 labels=[]
 for d in circles:
  hits=[s['text'] for s in spans if s['text'] in 'ABCDEFGH' and len(s['text'])==1 and d['rect'].contains(pymupdf.Rect(s['bbox']))]
  assert len(hits)==1,(pi,hits)
  r=d['rect']; labels.append((hits[0],((r.x0+r.x1)/2,(r.y0+r.y1)/2),r.width))
 offset=0
 for g in graphs:
  n=len(g['coords_cm']); items=labels[offset:offset+n];offset+=n
  assert set(a for a,_,_ in items)==set(g['coords_cm'])
  centers={a:pt for a,pt,_ in items};v=sorted(centers)
  pdfedges=[]
  for d in drawings:
   if abs(d['width']-1.14570)>0.01 or len(d['items'])!=1 or d['items'][0][0]!='l':continue
   _,a,b=d['items'][0]
   names=[]
   for pt in (a,b):
    match=[name for name,c in centers.items() if math.hypot(pt.x-c[0],pt.y-c[1])<0.05]
    names.append(match[0] if len(match)==1 else None)
   if all(names):pdfedges.append(normedge(*names))
  pdfedges=sorted(pdfedges)
  assert pdfedges==g['source_edges'],(g['id'],pdfedges,g['source_edges'])
  # Affine match independent PDF geometry to the supplied actual source coordinates.
  ptscale=72/2.54
  tx=[centers[a][0]-ptscale*g['coords_cm'][a][0] for a in v]
  ty=[centers[a][1]+ptscale*g['coords_cm'][a][1] for a in v]
  assert max(tx)-min(tx)<0.02 and max(ty)-min(ty)<0.02
  e=set(pdfedges)
  geometry=[]
  for ab in e:
   a,b=ab
   for z in v:
    if z in ab:continue
    dist,t=distance_to_segment(centers[z],centers[a],centers[b])
    if 0<t<1 and dist<28.346457:geometry.append([ab,z,round(dist*25.4/72,3)])
  assert not geometry,(g['id'],geometry)
  counts={};sample={}
  for k in range(1,5):
   cs=colorings(v,e,k);counts[k]=len(cs);sample[k]=cs[0] if cs else None
  chi=next(k for k in counts if counts[k])
  omega,cgroups=clique(v,e);cyc=cycles(v,e)
  d={'id':g['id'],'page':pi,'vertices':v,'source_coords_cm':g['coords_cm'],'pdf_centers_pt':centers,'pdf_edges':pdfedges,'pdf_circle_diameter_mm':round(items[0][2]*25.4/72,6),'nonendpoint_circle_intersections':geometry,'chromatic_number':chi,'clique_number':omega,'maximum_cliques':cgroups,'fixed_label_coloring_counts_1_to_4':counts,'sample_minimum_schedule':sample[chi],'all_simple_cycles':cyc,'odd_cycles':[c for c in cyc if (len(c)-1)%2]}
  if g['problem']==6:
   nonedges=[normedge(*ab) for ab in combinations(v,2) if normedge(*ab) not in e]
   additions=[]
   for k in range(len(nonedges)+1):
    for add in combinations(nonedges,k):
     ec=e|set(add)
     if not colorings(v,ec,2):
      blocked=[]
      for ab in add:
       for z in v:
        if z not in ab:
         dist,t=distance_to_segment(centers[z],centers[ab[0]],centers[ab[1]])
         if 0<t<1 and dist<28.346457:blocked.append([ab,z])
      additions.append({'edges':add,'odd_cycles':[c for c in cycles(v,ec) if (len(c)-1)%2],'straight_line_nonendpoint_circle_intersections':blocked})
    if additions:break
   assert k==(1 if g['id']=='P6-1' else 3)
   assert len(additions)==(6 if g['id']=='P6-1' else 20)
   assert all(not x['straight_line_nonendpoint_circle_intersections'] for x in additions)
   distances=[]
   for a,b in combinations(v,2):
    for z in v:
     if z in (a,b):continue
     dist,t=distance_to_segment(centers[z],centers[a],centers[b])
     distances.append(dist*25.4/72)
   assert min(distances)>12.99
   d['any_connection_minimum_third_site_center_distance_mm']=min(distances)
   d['minimum_added_edges']=k;d['all_minimum_additions']=additions
  if g['problem'] in (7,8):
   hist=Counter();examples={}
   for order in permutations(v):
    k,c,t=firstfit(v,e,order);hist[k]+=1
    if k not in examples:examples[k]={'order':''.join(order),'schedule':c,'trace':[{'vertex':a,'slot':s,'prior_neighbor_slots':bs} for a,s,bs in t]}
   d['firstfit_order_histogram']=dict(sorted(hist.items()));d['firstfit_examples']=examples
   d['maximum_degree']=max(sum(a in ab for ab in e) for a in v)
   if g['problem']==7:
    _,start,_=firstfit(v,e,tuple('ADBC'))
    d['ADBC_result']=start;d['shortest_legal_single_card_repair_to_2_slots']=shortrepair(v,e,start)
  if g['problem']==9:
   for k in (3,4):
    cs=colorings(v,e,k)
    canonical={tuple(next(i+1 for i,b in enumerate(dict.fromkeys(c[a] for a in v)) if b==c[a]) for a in v) for c in cs}
    d[f'unlabeled_partition_count_at_most_{k}']=len(canonical)
    d[f'fixed_label_assignments_using_every_slot_of_{k}']=sum(len(set(c.values()))==k for c in cs)
  checks.append(d)
 assert offset==len(labels),(pi,offset,len(labels))
 text=page.get_text()
 assert f"Problem {pi}:" in text,(pi,text)
 assert "Week 62 / Conflict networks / Grades" in text
 assert "Grades 2–5" in text if pi<=3 else "Grades 4–5" in text
 assert "Bellingham Math Circle / Week 62 / W62-S-v1" in text
 if pi==4:
  assert "at least three different circles" in text and "Only the" in text and "start repeats, at the end." in text
 if pi==7:
  assert "During the order, do not move a placed card." in text
  assert "After an order is finished, you may move cards. Can you use fewer slots?" in text
 if pi in (1,7):assert "circle marks:" not in text

# Exhaustively challenge universal bipartite/first-fit bounds on every labeled graph n<=5.
universal=[]
for n in range(6):
 v=list('ABCDE'[:n]); possible=[normedge(*ab) for ab in combinations(v,2)]
 examined=0;orders=0
 for mask in range(1<<len(possible)):
  e={ab for i,ab in enumerate(possible) if (mask>>i)&1}
  two=bool(colorings(v,e,2));odd=any((len(c)-1)%2 for c in cycles(v,e))
  assert two==(not odd)
  delta=max((sum(a in ab for ab in e) for a in v),default=-1)
  for order in permutations(v):
   k,c,_=firstfit(v,e,order)
   assert k<=delta+1
   orders+=1
  examined+=1
 universal.append({'n':n,'all_graphs_checked':examined,'all_orders_checked':orders})

out={'method':'Independently extracted actual PDF circle centers, labels and conflict strokes, then matched raw TikZ coordinates. No writer verification/data loaded. Brute-force all assignments, vertex subsets, simple cycles, nonedge subsets and all relevant vertex permutations.','pdf_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),'tex_sha256':hashlib.sha256(TEX.read_bytes()).hexdigest(),'pdf_pages':len(doc),'page_dimensions_pt':[list(p.rect) for p in doc],'graphs':checks,'universal_finite_checks':universal}
args.report.parent.mkdir(parents=True,exist_ok=True)
args.report.write_text(json.dumps(out,indent=2)+'\n')
print('Read and checked all',len(doc),'pages and',len(checks),'actual graph diagrams.')
for d in checks:
 print(d['id'], 'edges=',','.join(d['pdf_edges']) or '(none)', 'chi=',d['chromatic_number'],'omega=',d['clique_number'],'counts=',d['fixed_label_coloring_counts_1_to_4'], 'firstfit=',d.get('firstfit_order_histogram',''))
 if 'minimum_added_edges' in d:print(' minimal additions:',d['minimum_added_edges'],[a['edges'] for a in d['all_minimum_additions']])
print('Universal finite checks:',universal)
