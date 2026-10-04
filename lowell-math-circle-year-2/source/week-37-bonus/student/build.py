from common import *
p=Packet(outdir(),37,'Mirror twins');c=p.c
p.start('K-3')
para(c,'Only the tile outline counts. A face dot keeps track of which side is up.',715,small=True)
problem(c,1,'Use each flat tile and its mirror twin. Keep the dotted faces upward: which pairs can match by slides and turns? Then allow turning a tile over. Does the answer change?',664)
shapes=[[(0,0),(18,0),(18,26),(39,26),(39,41),(18,41),(18,54),(55,54),(55,70),(0,70)],[(0,0),(65,0),(65,18),(18,18),(18,65),(0,65)],[(0,0),(18,0),(18,52),(40,52),(40,70),(-22,70),(-22,52),(0,52)]]
for yy,pts in zip([465,315,165],shapes):
 for xx,flip in [(185,False),(445,True)]:
  poly(c,[(xx+(-x if flip else x),yy+y) for x,y in pts]);circle(c,xx+(-9 if flip else 9),yy+9,3,black)
 label(c,'mirror',320,yy+30,11)
p.end()
p.start('Grades 4-5')
para(c,'Use rigid regular tetrahedral frames. Letters locate edges while building; they do not count in a match. Red sleeves stay attached.',715,small=True)
problem(c,2,'Build each edge pattern and its mirror. Which pairs can match by moving and turning? Swap one red sleeve to a plain edge to make a pair whose matching answer changes. Seek a reason that settles every possible turn.',665)
def tetra(cx,cy,reds,flip=False):
 pts={'A':(cx,cy+65),'B':(cx-65,cy-45),'C':(cx+65,cy-45),'D':(cx,cy+1)}
 if flip:pts={k:(2*cx-x,y) for k,(x,y) in pts.items()}
 for a,b in [('A','B'),('A','C'),('B','C'),('A','D'),('B','D'),('C','D')]:
  col=RED if ''.join(sorted(a+b)) in reds else Color(.58,.58,.58);line(c,*pts[a],*pts[b],4 if col==RED else 1.3,col,[4,3] if 'D' in (a,b) else None)
 for a,(x,y) in pts.items():circle(c,x,y,8,white);label(c,a,x,y-3,10)
for yy,reds in [(490,{'AB','BC','CD'}),(325,{'AB','AC','AD'}),(160,{'AB','AC','BC'})]:
 tetra(175,yy,reds);tetra(440,yy,reds,True);label(c,'mirror',308,yy,11)
p.end()
p.start('Grades 2-5')
para(c,'Each corner has three rigid arms meeting at right angles. Move and turn a whole model; keep its arms attached. Color names, not letter direction, count.',715,small=True)
phi,eps=math.radians(30),math.radians(25)
v=[(-35*math.sin(phi),-35*math.sin(eps)*math.cos(phi)),(35*math.cos(phi),-35*math.sin(eps)*math.sin(phi)),(0,35*math.cos(eps))];ox,oy=90,603
for bits in [(a,b,d) for a in [0,1] for b in [0,1] for d in [0,1]]:
 for j in range(3):
  if bits[j]:continue
  x=ox+sum(bits[k]*v[k][0] for k in range(3));y=oy+sum(bits[k]*v[k][1] for k in range(3))
  line(c,x,y,x+v[j][0],y+v[j][1],.8,GRAY)
for dx,dy in v:line(c,ox,oy,ox+dx,oy+dy,4,GRAY)
circle(c,ox,oy,3,black);label(c,'cube corner',115,658,10)
for cx,cy,turn in [(290,603,False),(494,625,True)]:
 for dx,dy in v:
  if turn:dx,dy=-dy,dx
  line(c,cx,cy,cx+dx,cy+dy,4,GRAY)
 circle(c,cx,cy,3,black)
label(c,'three arms',313,658,10);label(c,'whole-model turn',494,675,10)
arrow(c,175,618,245,618);arrow(c,367,618,432,618)
problem(c,3,'Build a corner and its mirror with three different arm colors, then with two alike, then with all alike. Which pairs can match by turning? Can unequal arm lengths make a mirror pair impossible to match when all arms have the same color?',560)
def corner(cx,cy,cols,lens=(1,1,1),flip=False):
 dirs=[(80,-80/math.sqrt(3)),(-80,-80/math.sqrt(3)),(0,160/math.sqrt(3))]
 if flip:dirs=[dirs[1],dirs[0],dirs[2]]
 for d,k,s in zip(dirs,cols,lens):
  x=cx+d[0]*s;y=cy+d[1]*s;line(c,cx,cy,x,y,9,{'R':RED,'B':BLUE,'G':GREEN}[k]);circle(c,x,y,6,white);label(c,k,x,y+13,11)
 circle(c,cx,cy,6,black)
corner(175,360,['R','B','G']);corner(440,360,['R','B','G'],flip=True);label(c,'mirror',308,357)
for xx,cols in [(175,['R','R','G']),(440,['R','R','R'])]:corner(xx,175,cols)
workspace(c,90,35);p.end();p.save()
