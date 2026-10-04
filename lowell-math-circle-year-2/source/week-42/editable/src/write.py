from common import *

def rules(b):
 b.text(0,'Use the same bag of three red counters and one blue. Draw twice in order, independently, giving every counter the same chance each time. Return and mix after each draw.',size=13)
 b.pair(.5,2,'B','R');b.arrow(4.5,2.65,6,2.65);b.shape(7,2.65,'square')
 b.text(2.05,'A sample rule: BR gives a square.',9,8.5,12)
 b.text(3.7,'A rule gives each color pair a square, a circle, or no shape. A fair rule must sometimes give each shape, and give them equal chances when a shape comes out.',size=13)
def ruleboard(b,y):
 for i,(a,c) in enumerate([('R','R'),('R','B'),('B','R'),('B','B')]):
  x=0 if i<2 else 9.3; yy=y+(i%2)*2.8
  b.pair(x,yy,a,c);b.arrow(x+3.8,yy+.68,x+4.8,yy+.68);b.box(x+5.1,yy,2,1.35)
def pairs_grid(b,y=6):
 labels=['R1','R2','R3','B']; cols=['R','R','R','B'];x=3;d=3
 b.text(y-2.1,'First draw down the side; second draw across the top.',size=12)
 for i in range(4):
  b.token(x+i*d+d/2,y-.7,cols[i],labels[i],.45)
  b.token(x-.8,y+i*d+d/2,cols[i],labels[i],.45)
  for j in range(4):b.box(x+j*d,y+i*d,d,d)
 b.put(fr'\draw[line width=1.4pt] ({x+3*d},{-y-d}) rectangle ({x+4*d},{-y-2*d});')
 b.token(x+3*d+.7,y+d+1.5,'R','R2',.42);b.token(x+3*d+2.2,y+d+1.5,'B','B',.42)
 b.text(y+12.35,'Each box names one equally likely pair of labeled counters.',size=12)

def storyslot(b,x,y):
 b.box(x,y,3.6,1.65);b.put(fr'\draw[gray!50] ({x+1.8},{-y}) -- ({x+1.8},{-y-1.65});')
 b.arrow(x+3.8,y+.82,x+4.45,y+.82);b.box(x+4.65,y+.3,1.05,1.05)
def markedpair(b,x,y,a,c):
 b.box(x,y,5.5,2.7)
 b.token(x+1.35,y+1.35,a[0],a,.52);b.token(x+4.15,y+1.35,c[0],c,.52)

b=Book(42,'Fair results from a bag','K--1','k-1')
b.text(0,'For random draws, use the same bag. Every counter has the same chance each time; put it back and mix after each draw.',size=13)
b.bag(0,1.7,'RRRB');b.pair(7,1.7,'R','B');b.arrow(5,2.4,6.4,2.4)
b.text(3.6,'Red, then blue makes this pair. Keep the order.',size=13)
b.p(1,5,'Choose draws yourself to make every different color pair. Which pairs disappear if you take the blue counter out of the bag?')
for x,y in [(0,8),(9,8),(0,13),(9,13)]:
 b.box(x,y,7.4,3.5);b.put(fr'\draw[gray!50] ({x+3.7},{-y}) -- ({x+3.7},{-y-3.5});')
b.bag(1,19,'RRR');b.bag(10,19,'RRRB')
b.page()
b.text(0,'Use three red counters and one blue again. A rule gives each color pair a square, a circle, or no shape. The same color pair always gets the same answer.',size=13)
b.pair(.5,2.7,'B','R');b.arrow(4.5,3.4,6,3.4);b.shape(7,3.4,'square')
b.text(2.9,'A sample rule: BR gives a square.',9,8.5,12)
b.p(2,5,'Make a rule that sometimes gives each shape and gives them the same chance. Try it on six random pairs.')
ruleboard(b,8)
b.text(15,'Use a cross to record no shape.',size=13)
b.box(0,17,18,5.5);b.page()
b.text(0,'The red counters have marks R1, R2, R3. Each marked pair below has the same chance.',size=12)
b.p(3,1.5,'Does your rule give each shape to the same number of pictures? Find every rule that does and sometimes gives each shape.',size=13)
labels=['R1','R2','R3','B']
for i,(a,c) in enumerate((a,c) for a in labels for c in labels):
 markedpair(b,(i%3)*6.1,3.5+(i//3)*3.35,a,c)
b.page()
b.p(4,0,'Keep your rule for these bags. Which can give each shape, and do the shapes have the same chance?')
for x,y,cs in [(0,3,'RBBB'),(10,3,'RRBB'),(0,8,'RRRR'),(10,8,'BBBB')]:b.bag(x,y,cs)
b.box(0,13,18,3.5)
b.p(5,18,'Choose a four-counter bag that makes shapes come out as often as possible. Could any four-counter bag give a shape on every pair?')
b.box(0,21,7.8,2.3);b.box(9.8,21,7.8,2.3);b.page()
b.p(6,0,'Choose pairs and draw six-pair stories using your rule for each target. Can six random pairs force a shape to appear?')
for y,lab in [(3,'no shapes'),(9.7,'exactly one square and no circles'),(16.4,'exactly three circles and no squares')]:
 b.text(y,lab,size=13)
 for i in range(6):storyslot(b,(i%3)*6.1,y+1.1+(i//3)*2.3)
b.save()

b=Book(42,'Fair results from a bag','Grades 2--3','grades-2-3');rules(b)
b.p(1,6,'Invent a fair rule. Try it on six pairs, then decide whether your results are enough to settle that it is fair.')
ruleboard(b,8.4);b.box(0,15.1,18,3.5);b.space(20,3)
b.page()
b.p(2,0,'The counters are marked R1, R2, R3, and B. Use all the equally likely labeled pairs to check your rule exactly.')
b.pair(0,2.1,'R','B',('R2','B'));b.arrow(4,2.8,5.2,2.8);b.text(2.1,'row R2, column B',5.7,10,13)
pairs_grid(b,5.8);b.space(20.3,3)
b.page()
b.p(3,0,'Keep your rule for each bag below. Which bags give the two shapes the same chance? Show a reason that does not depend on a lucky run.')
b.bag(1,3,'RRBB','two red, two blue');b.bag(10,3,'RBBB','one red, three blue');b.space(7,4)
b.p(4,12,'You want shapes to come out often. Would you choose the three-red bag or the two-red bag? Give an exact reason.')
b.bag(1,15,'RRRB');b.bag(10,15,'RRBB');b.space(19,4)
b.page()
b.p(5,0,'Change bags between draws: use the left bag first and the right bag second. Does your rule still give the shapes the same chance?')
b.bag(0,3,'RRRB','first draw');b.bag(11,3,'RBBB','second draw');b.arrow(5.5,3.8,10,3.8);b.space(7,4)
b.p(6,12,'Can your rule promise at least one shape within six pairs? Make a six-pair story that settles your answer.')
b.box(0,14.4,18,3.5)
b.p(7,19,'Can any fair rule give a shape on every pair from the original three-red, one-blue bag? Explain your answer.')
b.space(22,2);b.save()

b=Book(42,'Fair results from a bag','Grades 4--5','grades-4-5');rules(b)
b.p(1,6,'Design a fair rule for this bag. It must use only the colors and their order, and it must sometimes give each shape.')
ruleboard(b,8.3)
b.p(2,15,'Check your rule using every equally likely pair of the labeled counters R1, R2, R3, B. Explain why the shape chances match.')
b.pair(0,18,'R','B',('R2','B'));b.text(18.25,'R2 then B is one labeled pair.',5,12,12);b.space(21,3)
b.page()
b.p(3,0,'Keep your rule for these bags. Does it work for every fixed bag containing both colors, even if its contents are hidden? Explain your answer.')
b.bag(0,3,'RRRRRBB','five red, two blue');b.bag(10,3,'RRRBBBB','three red, four blue');b.space(7.3,5)
b.p(4,13,'A different color-only rule must give a shape on every pair from the three-red, one-blue bag. Can it be fair? If skipping is allowed, what is the smallest number of the 16 labeled pairs it must skip?')
b.space(18,6);b.page()
b.p(5,0,'Use one bag for the first draw and another for the second. Decide exactly when your rule stays fair in the three cases below.')
for y,a,c in [(3,'RRRB','RBBB'),(8,'RRRB','RRRRRRBB'),(14,'RRBB','RB')]:
 b.bag(0,y,a,'first');b.bag(10,y,c,'second');b.arrow(5,y+.75,9,y+.75)
b.space(20,4);b.page()
b.p(6,0,'Return both counters only after drawing a pair. Then mix before the next pair. Does your rule still work with the three-red, one-blue bag? Explain using the labeled outcomes.')
b.bag(0,3,'RRRB');b.pair(8,3,'R','B',('R1','B'));b.space(6.5,5)
b.p(7,12,'A friend says, "My rule is fair, so six pairs must give equal numbers of squares and circles." Another says, "At least one shape must appear." Decide which claims follow from fairness.')
b.space(17,7);b.save()
build()
