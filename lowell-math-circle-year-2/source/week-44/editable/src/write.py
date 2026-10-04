from common import *

def rules(b):
 b.text(0,'Start with one red and one blue. Draw, return it, add one counter of that color, and mix. For random play, each counter has the same chance; for possible stories, choose the draws yourself.',size=13)
 b.bag(0,2.5,'RB');b.arrow(3.4,3.2,5,3.2,'draw R');b.token(5.8,3.2,'R');b.arrow(6.7,3.2,10,3.2,'return + copy');b.bag(11,2.5,'RRB')
def strip(b,x,y,n,w=1.8):
 for i in range(n):b.box(x+i*w,y,w,1.8)
def bowl(b,x,y,w=7,h=3):b.box(x,y,w,h)
def identities(b,y):
 b.text(y,'Marks distinguish counters of the same color. Start with R1 and B1. The first added counter gets mark 2; the next gets mark 3.',size=13)
 b.token(.6,y+2.5,'R','R1');b.arrow(1.4,y+2.5,3,y+2.5)
 for x,c,l in [(4,'R','R1'),(5.2,'B','B1'),(6.4,'R','R2')]:b.token(x,y+2.5,c,l)
 b.arrow(7.3,y+2.5,9,y+2.5);b.token(10,y+2.5,'R','R2')
 b.text(y+3.5,'draw R1',0,3,11);b.text(y+3.5,'return it and add R2',3.5,5,11);b.text(y+3.5,'next draw could be R2',9,8,11)
def tree(b,y):
 b.text(y,'first draw',0,3,12);b.text(y,'second draw',8,5,12);b.text(y,'bag colors only',13,4.8,12)
 for row,c in enumerate(['R','B']):
  yy=y+2+row*7;b.token(2,yy+1.8,c,c+'1',.6)
  for j in range(3):
   b.arrow(3,yy+1.8,7.5,yy+j*1.9);b.box(8,yy+j*1.9-.7,3,1.4);b.arrow(11.4,yy+j*1.9,12.5,yy+j*1.9);b.box(13,yy+j*1.9-.7,4.8,1.4)

b=Book(44,'The bag that copies','K--1','k-1');rules(b)
b.p(1,5.5,'Make every different bag you can reach after two draws. Which bags can come from two different draw stories?')
for x,y in [(0,8),(9,8),(0,13)]:bowl(b,x,y,8,4)

strip(b,0,21.5,2,3.5);strip(b,10,21.5,2,3.5);b.page()
b.p(2,0,'Which bags can you make after three draws? Make a story for each possible bag, and cross out any impossible bag.')
for i,colors in enumerate(['RRRRB','RRBBB','RRRRR','RBBBB']):
 x=(i%2)*9.2;y=3+(i//2)*9;b.bag(x,y,colors);strip(b,x,y+4.2,3,2.5)
b.page()
b.p(3,0,'Find every four-draw story ending with this bag. Can you also make every four-draw bag with more blue than red?')
b.bag(0,2.3,'RRRBBB')
for i in range(6):strip(b,(i%2)*9.2,7+(i//2)*4.6,4,1.9)

b.page()
b.p(4,0,'Find every possible bag just before the last draw for each finish. Could copying ever lose all the blue counters?')
b.text(1.8,'after four draws',0,6,12);b.text(1.8,'before the last draw',8,10,12)
for i,colors in enumerate(['RRRRRB','RRRRBB','RRRBBB']):
 y=3+i*6.5;b.bag(0,y,colors);b.arrow(5,y+1.2,7,y+1.2);bowl(b,8,y,10,4.5)
b.save()

b=Book(44,'The bag that copies','Grades 2--3','grades-2-3');rules(b)
b.p(1,5.4,'Find every two-draw color story and its final bag. Which final bags have more than one story?')
for i in range(4):
 x=(i%2)*9.2;y=8+(i//2)*6.3;strip(b,x,y,2,2.2);bowl(b,x,y+2.3,7.8,3)
b.space(22,2);b.page();identities(b,0)
b.p(2,5.2,'Each counter in the bag has the same chance of being drawn. Complete every marked two-draw story. Ignore marks when comparing final bags: which red/blue counts have the most stories?')
tree(b,8);b.page()
b.p(3,0,'Compare two rules, both starting with R1 and B1. Which numbers of red draws have the greatest chance after two draws? Give an exact reason.')
b.text(3.3,'return and add a copy',0,8,14);b.text(3.3,'return only',10,8,14)
for x in [0,10]:b.token(x+1,5,'R','R1');b.token(x+2.4,5,'B','B1');bowl(b,x,7,8,8)
b.p(4,17,'A copying bag ends with three red and two blue. Find all possible three-draw color stories. Could they have different chances?')
b.space(21,3);b.page()
b.p(5,0,'Use the copying rule for four draws. Find two different color stories for each final bag below, or explain why there is only one.')
for i,colors in enumerate(['RRRRRB','RRRRBB','RRRBBB']):
 y=3+i*5.7;b.bag(0,y,colors);strip(b,7,y,4,2.2);strip(b,7,y+2.4,4,2.2)
b.p(6,21,'A friend says one color must eventually vanish from a copying bag. Can that happen?')
b.save()

b=Book(44,'The bag that copies','Grades 4--5','grades-4-5');rules(b)
identities(b,5.2)
b.p(1,10.5,'Find all the two-draw marked stories. Use them to decide whether zero, one, or two red draws has the greatest chance.')
b.box(0,14,18,7);b.space(22,2);b.page()
b.p(2,0,'Keep the starting bag R1, B1, but return each draw without adding a copy. How does the chance of zero, one, or two red draws change? Explain the difference exactly.')
b.box(0,4,18,7)
b.p(3,13,'Return to copying. Compare the color stories RRB, RBR, and BRR. Does their order change their chance? Give an exact reason for your answer.')
for i,s in enumerate(['RRB','RBR','BRR']):
 b.text(17,s,i*6.1,5.7,14);b.box(i*6.1,18.2,5.7,4.8)
b.page()
b.p(4,0,'Three copying draws have 24 equally likely marked histories. How many give zero, one, two, or three red draws? Explain how you know your counts cover every possibility.')
for i in range(4):
 x=(i%2)*9.2;y=4+(i//2)*8.2;b.text(y,str(i)+' red draws',x,8,14);b.box(x,y+1.2,8,5.7)
b.space(22,2);b.page()
b.p(5,0,'Predict the chances of zero, one, two, three, or four red draws after four copying draws. Check your prediction exactly without making a 120-row list.')
b.box(0,4,18,8)
b.p(6,14,'What do you predict about red-draw totals after five draws, or after more draws? Explore your prediction; an exact argument for every length is a further question.')
b.space(18,6);b.save();build()
