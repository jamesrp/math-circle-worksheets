from common import *
p=Packet(outdir(),38,'Seams and cuts');c=p.c
p.start('Grades 2-5')
para(c,'Keep bands on the table. An adult makes every cut. Rectangles are joining recipes: join matching corner marks. M matches the end order; R reverses it. A closed edge trip stops on its first return to its start.',715,small=True)
def recipe(x,y,w,h,n,rev,caption=None,cuts=True,hole=None):
 c.setStrokeColor(black);c.setLineWidth(1);c.rect(x,y,w,h)
 if cuts:
  for j in range(1,n):line(c,x,y+h*j/n,x+w,y+h*j/n,.8,GRAY,[3,3])
 for xx,topdot in [(x,True),(x+w,not rev)]:
  for yy,dot in [(y+h,topdot),(y,not topdot)]:
   if dot:circle(c,xx,yy,3,black)
   else:
    c.setFillColor(white);c.setStrokeColor(black);c.rect(xx-3,yy-3,6,6,fill=1,stroke=1)
 for j in range(n if cuts else 0):
  label(c,str(j+1),x-14,y+h*(1-(j+.5)/n)-4,10)
  label(c,str(n-j if rev else j+1),x+w+14,y+h*(1-(j+.5)/n)-4,10)
 if hole:
  c.saveState();clip=c.beginPath();clip.rect(x,y,w,h);c.clipPath(clip,stroke=0,fill=0);c.setFillColor(Color(.7,.7,.7));c.setStrokeColor(black)
  if hole=='inside':c.circle(x+w/2,y+h/2,12,fill=1,stroke=1)
  if hole=='notch':c.circle(x+w/2,y+h,12,fill=1,stroke=1)
  if hole=='seam':
   c.circle(x,y+h/2,12,fill=1,stroke=1);c.circle(x+w,y+h/2,12,fill=1,stroke=1)
  c.restoreState()
 if caption:label(c,caption,x+w/2,y-22,12)
problem(c,1,'Make all four bands. Predict how many connected pieces the dotted cuts will make. Have an adult cut every lane boundary, then trace all the closed edges on each piece. Can one cut result contain both a one-edge piece and a two-edge piece?',642)
for y,n,r in [(480,3,False),(350,3,True),(220,4,False),(90,4,True)]:recipe(70,y,470,74,n,r,f'{n} lanes / '+('R' if r else 'M'))
p.end()
p.start('Grades 2-5')
para(c,'Keep each mark attached to its corner. Join short ends.',715,small=True)
label(c,'before joining',112,682,10);label(c,'align the same marks',304,682,10);label(c,'seam record',494,682,10)
def endmark(x,y,dot):
 if dot:circle(c,x,y,3,black)
 else:
  c.setFillColor(white);c.setStrokeColor(black);c.rect(x-3,y-3,6,6,fill=1,stroke=1)
for yy,k in [(650,'M'),(596,'R')]:
 for x,num in [(45,1),(116,2)]:
  c.setStrokeColor(black);c.rect(x,yy-14,50,28);label(c,str(num),x+25,yy-4,10)
 for xx in [95,116]:endmark(xx,yy+14,True);endmark(xx,yy-14,False)
 arrow(c,180,yy,225,yy)
 for side in [0,1]:
  y1=yy+(12 if side==0 else -12);y2=yy+(12 if (side==0)^(k=='R') else -12)
  line(c,260,y1,344,y2,.8,GRAY);endmark(260,y1,side==0);endmark(344,y2,side==0)
 label(c,k,302,yy-29,10)
 arrow(c,367,yy,410,yy)
 for x,num in [(424,1),(522,2)]:
  c.setStrokeColor(black);c.rect(x,yy-12,42,24);label(c,str(num),x+21,yy-4,10)
 arrow(c,470,yy+7,518,yy+7);label(c,k,494,yy-6,10)
problem(c,2,'Join three strips into a circle using each seam recipe below. Find a rule predicting the number of closed edges. Design a four-strip circle with one closed edge, and another with two. Explain why the rule covers every choice of seams.',554)
for yy,word in [(425,'MMM'),(322,'MMR'),(219,'MRR'),(116,'RRR')]:
 for j,k in enumerate(word):
  x=80+j*160;c.setStrokeColor(black);c.rect(x,yy-22,110,44);label(c,f'strip {j+1}',x+55,yy-4,11)
  if j<2:label(c,k,x+135,yy-4,13);arrow(c,x+114,yy+9,x+156,yy+9)
 # Last seam travels back to strip 1; explicit start/end arrows, not a crossed road.
 c.setStrokeColor(GRAY);c.setLineWidth(.8);c.line(512,yy-28,512,yy-47);c.line(512,yy-47,80,yy-47);arrow(c,80,yy-47,80,yy-27)
 label(c,word[-1],300,yy-64,13)
p.end()
p.start('K-3')
para(c,'An adult removes the shaded paper before joining. Holes and notches stay small, separate, and narrower than the strip.',715,small=True)
problem(c,3,'Trace every closed edge of bands A, B, C and D. How many does each have? Design a connected band with four closed edges using at most three holes.',665)
for x,y,r,h,k in [(75,445,False,'inside','A / M'),(345,445,True,'inside','B / R'),(75,245,True,'notch','C / R'),(345,245,False,'seam','D / M')]:recipe(x,y,180,80,1,r,k,False,h)
workspace(c,175,105);p.end();p.save()
