from common import *

def row(b,x,y,word='',cell=1.35,labels=False):
 for i in range(3):
  b.box(x+i*cell,y,cell,cell)
  if labels:b.text(y+.07,str(i+1),x+i*cell+.12,.6,9)
  if word:b.token(x+(i+.5)*cell,y+cell*.56,word[i],r=min(.42,cell*.3))
def pairrows(b,x,y,a,c,cell=1.35):row(b,x,y,a,cell);row(b,x,y+cell+.35,c,cell)
def card(b,x,y,pos,col,w=2.2):
 b.box(x,y,w,1.5)
 d=(w-.3)/3
 for j in range(3):
  xx=x+.15+j*d
  b.box(xx,y+.15,d,.78)
  if j==pos-1:
   b.put(fr'\draw[line width=1.4pt] ({xx},{-y-.15}) rectangle ({xx+d},{-y-.93});')
   b.token(xx+d/2,y+.54,col,r=min(.24,d*.35))
 b.text(y+1.05,str(pos)+r'$\to$'+col,x+.16,w-.2,9)
def history(b,x,y,h):
 for i,(p,c) in enumerate(h):card(b,x+i*2.6,y,p,c)
def intro(b):
 b.text(0,'Each instruction names a slot and a color. Set that slot to that color on both boards, even if it is already that color. Slots are 1, 2, 3 from left to right.',size=13)
 pairrows(b,0,2.5,'RBR','BRB',1.4);card(b,6,3.4,2,'B');b.arrow(4.7,4.1,5.6,4.1);b.arrow(8.7,4.1,10,4.1);pairrows(b,10.5,2.5,'RBR','BBB',1.4)
def toggle(b):
 b.text(0,'A toggle changes red to blue or blue to red in its slot, on both boards. It never sets a chosen color.',size=13)
 pairrows(b,0,2.4,'RBR','BRB',1.4);b.arrow(4.8,4,9.5,4,'toggle slot 2');pairrows(b,10.3,2.4,'RRR','BBB',1.4)
def cases(b,y):
 for i,(a,c) in enumerate([('RBR','RRR'),('RRB','BRR'),('BRB','BRB'),('RRR','BBB')]):
  x=(i%2)*9.2;yy=y+(i//2)*7.2;pairrows(b,x,yy,a,c,1.65);b.box(x+5.8,yy+1,2.2,1.6)
def cardsix(b,y):
 for i,(p,c) in enumerate([(1,'R'),(2,'R'),(3,'R'),(1,'B'),(2,'B'),(3,'B')]):card(b,(i%3)*5.7,y+(i//3)*2.3,p,c,3.8)

b=Book(46,'Two boards forget their starts','K--1','k-1');intro(b)
b.p(1,6.5,'Make these boards match using as few instructions as you can. Can any other starts need more instructions?')
row(b,3.5,10,'RBR',3.6,True);row(b,3.5,15,'BRB',3.6,True)
b.box(0,21,18,2);b.page()
b.p(2,0,'How few instructions can make each pair match? Try every pair.')
cases(b,3)
b.p(3,19,'Invent a pair that needs exactly two instructions to match. Can you invent a pair that needs four?')
b.space(22,2);b.page()
b.p(4,0,'Choose three instructions that make any two starts match. Could just two instructions always do it?')
for x in [0,6.1,12.2]:b.box(x,3,5.4,3)
b.box(0,8,18,5)
b.p(5,15,'Use these two instructions. Make one starting pair that ends matching and another that ends different.')
history(b,2,17.5,[(1,'R'),(3,'B')]);pairrows(b,0,20,'','',1.3);pairrows(b,10,20,'','',1.3);b.page()
b.text(0,'Mix these six cards in a cup. Draw one, use it on both boards, then put it back and mix.',size=13);cardsix(b,2.5)
b.p(6,8,'Try six draws from these starts, then start again. Could matching take more than three draws?')
row(b,3.5,11,'RRR',3.6,True);row(b,3.5,15.3,'BBB',3.6,True)
b.p(7,21,'Keep drawing after the boards match. Can any instruction make them different again?');b.save()

b=Book(46,'Two boards forget their starts','Grades 2--3','grades-2-3');intro(b)
b.p(1,6.5,'Find the fewest instructions needed to make these boards match. Build pairs needing fewer instructions. Can any pair need more?')
row(b,3.5,10,'RBR',3.6,True);row(b,3.5,15,'BRB',3.6,True);b.space(21,3);b.page()
b.text(0,'Put a small marker above a slot when an instruction first names it. Leave the marker there for the rest of the story.',size=13)
b.p(2,2,'Which stories guarantee that any two starting boards will finish matching? Explain why your answer holds for every starting pair.')
for y,h in [(5,[(1,'R'),(1,'B'),(3,'R')]),(10,[(2,'R'),(3,'B'),(1,'R')]),(15,[(2,'B'),(2,'R'),(2,'B')])]:history(b,0,y,h);row(b,10,y,'',2.3,True)
b.p(3,20,'Can some starting pairs match before all three slots have markers? Make one example that does and one that does not.')
b.page();b.text(0,'Mix six instruction cards in a cup. Draw, use the instruction on both boards, replace, and mix.',size=13);cardsix(b,2.5)
b.p(4,8,'A friend says three draws must make every pair match. Make a three-draw story that tests that claim. Could even ten draws fail?')
b.box(0,11.5,18,4)
b.p(5,18,'Find the shortest instruction story that guarantees a match for every starting pair. Explain why no shorter story can give that guarantee.')
b.space(22,2);b.page();toggle(b)
b.p(6,7,'Use only shared toggles on these starting pairs. Which can be made to match, and why?')
for i,(a,c) in enumerate([('RBR','RRR'),('RRB','BRR'),('BRB','BRB')]):pairrows(b,i*6.1,10,a,c,1.65)
b.p(7,17,'What changes if a story may use both color-setting instructions and toggles? Invent a story that makes every starting pair match, and a story that fails for at least one pair. Show a pair where it fails.')
b.box(0,21,18,2.5);b.save()

b=Book(46,'Two boards forget their starts','Grades 4--5','grades-4-5');intro(b)
b.p(1,6.5,'How does the fewest number of instructions needed for a match depend on the starting pair? Develop a rule that works for every pair.')
cases(b,9);b.page()
b.p(2,0,'For each instruction story, how many different final boards can come from the eight possible starts? Determine exactly which starting colors still matter.')
for y,h in [(3,[(1,'R'),(1,'B'),(3,'R')]),(8,[(2,'R'),(3,'B'),(1,'R')]),(13,[(2,'B'),(2,'R'),(2,'B')])]:history(b,0,y,h);b.box(9,y,9,3.7)
b.p(3,19,'Explain exactly when an instruction story forgets every starting color. Could two particular boards agree before that happens?')
b.space(22,2);b.page();toggle(b)
b.p(4,7,'Can shared toggles erase a disagreement between two starting boards? Give an argument for every possible sequence of toggles.')
b.space(11,4)
b.p(5,16,'Allow both color-setting instructions and toggles. Find a condition on the whole instruction story that guarantees every start gives the same finish, and explain both directions.')
b.space(20,4);b.page()
b.text(0,'Draw independently from six equally likely cards, replacing each one. Thus each slot has the same chance, and each new color is red or blue with the same chance.',size=13);cardsix(b,2.5)
b.p(6,8,'Suppose the chosen slots are 1, 3, 1, 2, in that order. Among the 16 equally likely color stories, which final boards have the greatest chance? Explain without assuming any starting colors.')
b.box(0,12,18,5)
b.p(7,18,'Would your argument work for any slot story that visits all three slots? Does it mean four random instructions must forget the start?')
b.space(22,2);b.save();build()
