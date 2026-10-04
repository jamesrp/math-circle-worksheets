from common import *
p=Packet(outdir(),40,'Loop colors');c=p.c
# Collect path pieces, then merge their true endpoints into complete gap-to-gap
# arcs. A single outline/channel stroke keeps every real join open for coloring.
strand_paths=[]
def stroke_path(points,width=8,channel=5):
 strand_paths.append([tuple(q) for q in points])
def flush_strands(expected):
 adj={}
 for j,pts in enumerate(strand_paths):
  for q in [pts[0],pts[-1]]:adj.setdefault(q,[]).append(j)
 assert all(len(js) in [1,2] for js in adj.values())
 left=set(range(len(strand_paths)));arc_count=0
 while left:
  seed=next((j for j in sorted(left) if len(adj[strand_paths[j][0]])==1 or len(adj[strand_paths[j][-1]])==1),min(left))
  pts=strand_paths[seed]
  if len(adj[pts[-1]])==1 and len(adj[pts[0]])!=1:pts=pts[::-1]
  arc=list(pts);left.remove(seed)
  while True:
   todo=[j for j in adj[arc[-1]] if j in left]
   if not todo:break
   j=todo[0];pts=strand_paths[j]
   if pts[0]!=arc[-1]:pts=pts[::-1]
   arc.extend(pts[1:]);left.remove(j)
  path=c.beginPath();path.moveTo(*arc[0])
  for q in arc[1:]:path.lineTo(*q)
  c.setLineJoin(1);c.setLineCap(1);c.setStrokeColor(black);c.setLineWidth(8);c.drawPath(path,fill=0,stroke=1)
  c.setStrokeColor(white);c.setLineWidth(5);c.drawPath(path,fill=0,stroke=1)
  arc_count+=1
 assert arc_count==expected,(arc_count,expected)
 strand_paths.clear()
def crossing(xl,xr,yt,h=35,colors=None):
 yb=yt-h;g=.16
 def along(t):return (xl+(xr-xl)*t,yt-h*t)
 if colors:
  underin,over,underout=colors
  line(c,*along(0),*along(.5-g),8,underin);line(c,*along(.5+g),*along(1),8,underout);line(c,xr,yt,xl,yb,8,over)
 else:
  stroke_path([along(0),along(.5-g)]);stroke_path([along(.5+g),along(1)]);stroke_path([(xr,yt),(xl,yb)])
def braid(cx,yt,n,w=70,h=35,close=True,cutleft=None,cutright=None):
 xl=cx-w/2;xr=cx+w/2;yb=yt-n*h
 for j in range(n):crossing(xl,xr,yt-j*h,h)
 if close:
  for x,outer,cut in [(xl,xl-30,cutleft),(xr,xr+30,cutright)]:
   stroke_path([(x,yt),(x,yt+15),(outer,yt+15)])
   stroke_path([(outer,yb-15),(x,yb-15),(x,yb)])
   if cut:
    high,low=cut;stroke_path([(outer,yt+15),(outer,high)]);stroke_path([(outer,low),(outer,yb-15)])
   else:stroke_path([(outer,yt+15),(outer,yb-15)])
 return xl-30,xr+30,yb
p.start('Grades 2-5')
para(c,'Use red (R), blue (B), and green (G). Give each whole arc one color; an arc continues through overpasses and stops at underpasses or open ends. At every crossing, the three colors are all the same or all different. Read machines from top inputs to bottom outputs.',715,small=True)
label(c,'input',160,635,11);crossing(120,200,617,55,(RED,BLUE,GREEN))
for x,y,k in [(120,628,'R'),(200,628,'B'),(120,542,'B'),(200,542,'G')]:label(c,k,x,y,12)
label(c,'over B',264,585,10);label(c,'output',160,520,11)
problem(c,1,'Feed every ordered pair of R, B and G into repeated copies of this crossing. How many crossings first return the same left-right pair? Can any pair fail to return? Explain your rule.',493)
braid(465,390,6,80,35,False);flush_strands(8);label(c,'input',465,415);label(c,'output',465,152)
for j,(a,b) in enumerate([(a,b) for a in 'RBG' for b in 'RBG']):
 label(c,f'{a} {b}',90,383-j*27,13);line(c,145,380-j*27,330,380-j*27,.5,GRAY)
label(c,'first return after ___ crossings',226,418,11)
p.end()
p.start('Grades 4-5')
problem(c,2,'Each picture joins left output to left input, and right output to right input, outside the crossing strip. Count every valid coloring, including one-color choices. Which pictures have equal counts but different numbers of separate cords? Explain why your counts are complete.')
for cx,yt,n in [(115,557,1),(306,557,2),(495,557,3),(190,323,4),(435,323,6)]:
 _,_,yb=braid(cx,yt,n);flush_strands(n);label(c,f'{n} crossing'+('s' if n!=1 else ''),cx,yb-42,12);label(c,'colorings: ___   cords: ___',cx,yb-62,10)
p.end()
p.start('Grades 4-5')
para(c,'To join two closed diagrams, cut the marked crossing-free pieces and join upper ends to upper ends, lower ends to lower ends. Joined ends must have the same color.',715,small=True)
problem(c,3,'How many valid colorings does each joined picture have? Predict the count if three three-crossing loops are joined. Explain your counts.',660)
# A non-task cut/join example of two plain loops, with explicit intermediate ends.
for x in [75,135]:c.setStrokeColor(black);c.setLineWidth(1.5);c.ellipse(x-20,552,x+20,592)
for x,start in [(75,-24),(135,156)]:
 c.setStrokeColor(GRAY);c.setLineWidth(3);c.arc(x-20,552,x+20,592,start,48)
 for a in [start,start+48]:
  a=math.radians(a);line(c,x+17*math.cos(a),572+17*math.sin(a),x+23*math.cos(a),572+23*math.sin(a),1.1)
label(c,'input',105,535,10)
for x,side in [(265,1),(335,-1)]:
 # Rectangle-like loops have a missing crossing-free side segment.
 ox=x+side*20;pts=[(ox,580),(ox,592),(x-side*20,592),(x-side*20,552),(ox,552),(ox,564)];
 for a,b in zip(pts,pts[1:]):line(c,*a,*b,1.5)
 circle(c,ox,580,2,black);circle(c,ox,564,2,black)
line(c,285,580,315,580,.7,GRAY,[3,2]);line(c,285,564,315,564,.7,GRAY,[3,2]);label(c,'cut / join',300,535,10)
poly(c,[(450,552),(450,592),(550,592),(550,552)]);label(c,'output',500,535,10)
arrow(c,180,573,210,573);arrow(c,390,573,420,573)
# Connected sum: removed vertical side sections are replaced by two joining strands.
def joined_trefoils(yt):
 high,low=yt-32,yt-58
 _,r,_=braid(135,yt,3,70,35,True,cutright=(high,low))
 l,_,_=braid(475,yt,3,70,35,True,cutleft=(high,low))
 stroke_path([(r,high),(l,high)]);stroke_path([(r,low),(l,low)]);flush_strands(6)
joined_trefoils(445);label(c,'three crossings + three crossings',306,310,11);label(c,'colorings: __________',306,288,11)
yt=244;high,low=yt-32,yt-58;_,r,yb=braid(135,yt,3,70,35,True,cutright=(high,low))
l=410;rr=525;top=yt+15;bottom=yb-15
stroke_path([(l,high),(l,top),(rr,top),(rr,bottom),(l,bottom),(l,low)])
stroke_path([(r,high),(l,high)]);stroke_path([(r,low),(l,low)])
flush_strands(3)
label(c,'three crossings + plain loop',306,109,11);label(c,'colorings: __________',306,85,11)
p.end();p.save()
