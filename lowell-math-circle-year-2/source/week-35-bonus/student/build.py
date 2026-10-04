from common import *
p=Packet(outdir(),35,'Footprint borders');c=p.c
p.start('Grades 2-5')
para(c,'Borders continue endlessly in both directions. Only the footprints and their colors count. A slide must match every footprint in both rows; rows keep their places.',715,small=True)
problem(c,1,'Repeat each row below on a long strip. Find the shortest slide that matches both rows together. Design a different pair with shortest shared slide 6 slots, and another with shortest shared slide 8 slots. Neither row may match after a one-slot slide.',653)
for y,colors in [(500,['R','B','B']),(365,['R','B','B','B'])]:
 for i,k in enumerate(colors):
  x=180+i*70;motif(c,x,y,42,color=RED if k=='R' else BLUE);label(c,k,x,y-39,12)
 line(c,135,y-58,135+len(colors)*70,y-58);label(c,'repeat',135+len(colors)*35,y-78)
workspace(c,250,175);p.end()
p.start('Grades 2-5')
problem(c,2,'Recolor the fewest footprints in each displayed block, then repeat the same repair endlessly so its requested slide becomes a match. Keep positions and forms fixed. Find equally short repairs when possible, and explain why fewer changes cannot work.')
for title,xs,word in [('input block',[70,94,118],'RBB'),('one-slot edit',[236,260,284],'RRB'),('repeat repaired block',[390,414,438,474,498,522],'RRBRRB')]:
 label(c,title,sum(xs)/len(xs),601,10)
 for x,k in zip(xs,word):
  motif(c,x,576,16,color=RED if k=='R' else BLUE);label(c,k,x,555,9)
c.setStrokeColor(GRAY);c.setLineWidth(.7);c.rect(250,563,20,26)
arrow(c,143,576,209,576);arrow(c,312,576,362,576)
for y,word,shift in [(448,'RBBBRB',3),(307,'RBBBBRRB',2),(166,'RRBBRB',2)]:
 label(c,f'slide {shift} slots',306,y+55,12)
 for i,k in enumerate(word):
  x=70+i*58;motif(c,x,y,31,color=RED if k=='R' else BLUE);label(c,k,x,y-28,11)
 line(c,52,y-53,550,y-53,.6,Color(.75,.75,.75))
 label(c,'changes: ______',470,y-78,11)
p.end()
p.start('K-3')
para(c,'Use the two mirror forms below. Card edges are only holders; forms count.',715,small=True)
motif(c,250,648,36);motif(c,355,648,36,mirror=True);label(c,'A',250,610,11);label(c,'mirror A',355,610,11)
problem(c,3,'On the table, make necklaces with 5, 6, 7 and 8 cards. Every pair of neighbors, including the last and first, must use opposite forms. Which can be finished? For the others, make as few equal-neighbor joins as possible. Record the forms in the circles.',586)
for cx,cy,n in [(170,392,5),(445,392,6),(170,180,7),(445,180,8)]:
 for j in range(n):
  a=math.pi/2+2*math.pi*j/n;x=cx+74*math.cos(a);y=cy+74*math.sin(a)
  b=math.pi/2+2*math.pi*(j+1)/n;line(c,x,y,cx+74*math.cos(b),cy+74*math.sin(b),.8,GRAY);circle(c,x,y,16)
 label(c,f'{n} cards',cx,cy-5,12)
p.end();p.save()
