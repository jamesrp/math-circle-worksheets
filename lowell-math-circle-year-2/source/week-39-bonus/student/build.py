from common import *
p=Packet(outdir(),39,'Road detours');c=p.c
p.start('Grades 2-5')
para(c,'Keep a journey as ordered step tiles. Remove only adjacent steps on the same road in opposite directions. New roads join two outer stops and may curve around H; crossings without a dot are not stops.',715,small=True)
problem(c,1,'Add as few roads as possible so a trip from H back to H can visit A, B, C and D and keep every step after shortening. With that many new roads, find the fewest-step trip. Close one new road: can a surviving trip still visit all four outer stops?',652)
def mat(points,edges,r=29):
 for a,b in edges:line(c,*points[a],*points[b],1.5)
 for a,(x,y) in points.items():circle(c,x,y,r,white);label(c,a,x,y-5,13)
points={'H':(306,415),'A':(176,415),'B':(306,545),'C':(436,415),'D':(306,285)}
mat(points,[('H',k) for k in 'ABCD']);workspace(c,220,145);p.end()
p.start('Grades 2-5')
problem(c,2,'On each map, how many different six-step trips start and finish at H? Stops and roads may be revisited. Two trips differ when their road choices differ. Find a count you can check.')
pts1={'H':(155,475),'A':(65,545),'B':(155,605),'C':(245,545)}
pts2={'H':(435,475),'A':(375,540),'B':(495,540),'C':(435,395),'D':(335,610),'E':(535,610),'F':(435,310)}
mat(pts1,[('H',k) for k in 'ABC']);mat(pts2,[('H',k) for k in 'ABC']+[('A','D'),('B','E'),('C','F')])
workspace(c,260,185);p.end()
p.start('Grades 4-5')
para(c,'Letters name whole trips that begin and end at H. A capital letter is the same trip backward. Keep the same start and the same roads.',715,small=True)
pts={'H':(150,555),'L':(80,610),'M':(80,500),'R':(220,610),'S':(220,500)};graph(c,pts,[('H','L'),('L','M'),('M','H'),('H','R'),('R','S'),('S','H')])
para(c,'a = H-L-M-H<br/>A = H-M-L-H<br/>b = H-R-S-H<br/>B = H-S-R-H',620,x=300,width=250,small=True)
for x,t in [(95,'input: a A b'),(500,'output: b')]:label(c,t,x,455,12)
label(c,'process:',270,455,10);label(c,'a A b',330,455,12);line(c,316,459,335,459,1.2)
arrow(c,170,460,215,460);arrow(c,386,460,432,460)
problem(c,3,'Choose two different journey cards. Do one then the other, and trade their order. Which pairs become the same after shortening? Find every matching pair and explain why your list is complete.',418)
words=['a','a a','b','a b','a b a b','a b A','a b b A']
for j,t in enumerate(words):
 x=47+(j%4)*140;y=292-(j//4)*75;c.setStrokeColor(black);c.roundRect(x,y,110,44,4,fill=0,stroke=1);label(c,t,x+55,y+16,15)
workspace(c,180,105);p.end();p.save()
