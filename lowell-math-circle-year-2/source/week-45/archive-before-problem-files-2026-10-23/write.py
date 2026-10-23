from common import *
COL={1:'R',2:'R',3:'R',4:'B',5:'B',6:'B'}
OTHER={1:2,2:1,3:4,4:3,5:6,6:5}
def face(b,x,y,n,w=2.1,h=2.8,hide=False):
 fill='red!15' if COL[n]=='R' else 'blue!15'
 b.put(fr'\draw[fill={fill},rounded corners=2pt] ({x},{-y}) rectangle ({x+w},{-y-h});')
 b.text(y+.7, COL[n],x+w/2-.22,.6,17)
 if hide:b.put(fr'\draw[fill=black] ({x+.15},{-y-h+.2}) rectangle ({x+.65},{-y-h+.6});')
 else:b.text(y+h-.6,str(n),x+.2,.7,10)
def cards(b,y):
 for i,(a,c) in enumerate([(1,2),(3,4),(5,6)]):
  x=i*6.1;face(b,x,y,a);face(b,x+2.6,y,c);b.put(fr'\draw[gray] ({x+1.05},{-y-3.05}) -- ({x+1.05},{-y-3.35}) -- ({x+3.65},{-y-3.35}) -- ({x+3.65},{-y-3.05});');b.text(y+3.6,'same card',x+.65,4,11)
def ticket(b,x,y,n):b.box(x,y,1.25,1.25);b.text(y+.28,str(n),x+.4,.5,14)
def intro(b):
 b.text(0,'Each pair below is the two faces of one card. The small marks match the six tickets.',size=13);cards(b,1.6)
 b.text(6.2,'Use matching-size cards. Mix all six tickets and draw with equal chances. Behind a screen, choose the drawn face and set it upward. Keep the ticket secret and cover marks identically; reveal only the face color. Replace the ticket and mix each round.',size=13)
 ticket(b,0,9.8,4);b.arrow(1.7,10.4,3.2,10.4);face(b,3.8,9.4,4,hide=True);b.arrow(6.5,10.6,9,10.6,'turn over');face(b,9.7,9.4,3)
 b.text(12.6,'ticket 4',0,3,11);b.text(12.6,'blue showing',3.4,5,11);b.text(12.6,'red underneath',9.3,7,11)
def bins(b,y,labels=('red underneath','blue underneath'),h=6):
 for i,l in enumerate(labels):
  b.text(y,l,i*9.2,8,13);b.box(i*9.2,y+1.1,8,h)
def changed(b,y=0):
 b.text(y,'Use only tickets 1 and 3, with equal chances. Choose and orient behind the screen, keep the ticket secret, and show its red face with the mark covered. Replace and mix each round.',size=13)
 for x,n in [(0,1),(9.2,3)]:
  ticket(b,x,y+3.4,n);b.arrow(x+1.6,y+4,x+3,y+4);face(b,x+3.5,y+3,n,hide=True)

a=Book(45,'The visible side','K--1','k-1');intro(a)
a.p(1,14,'Sort every ticket by its hidden color. Then find two tickets that show the same color but hide different colors.')
bins(a,17,h=4.5);a.page()
a.p(2,0,'Red is showing; which hidden color has more ways? Try removing one ticket, and find every removal that makes a tie.')
bins(a,3,h=6)
a.p(3,12,'Put all six tickets back; now blue is showing. Find every one-ticket removal that gives a tie between the hidden colors.')
bins(a,15,h=6);a.page();changed(a)
a.p(4,8,'Add just one extra ticket to this chooser: 2, 4, 5, or 6, and show the face named by each draw. Among red-showing rounds, which hidden color has more ways before and after each addition?')
bins(a,11,h=5)
a.p(5,18,'Choose three tickets so red sometimes shows and then always hides blue. Find every choice that works.')
for j in range(3):
 for i in range(3):a.box(j*6.1+i*1.55,21.2,1.25,1.25)
a.page()
a.text(0,'Use all six face tickets again. When a card is removed, remove both its tickets.',size=13)
a.p(6,2,'Remove one card so red showing always hides red. Can you remove a different card so red showing always hides blue?')
cards(a,5)
a.box(0,11,18,4)
a.p(7,17,'Find every two-ticket cup where red showing gives the hidden colors the same chance. Red must sometimes show.')
a.box(0,20,7,2.8);a.box(10,20,7,2.8);a.save()

b=Book(45,'The visible side','Grades 2--3','grades-2-3');intro(b)
b.p(1,14,'Find the showing and hidden colors for all six ticket choices. Which tickets show the same color on both faces?')
for i in range(6):
 x=(i%3)*6.1;y=17+(i//3)*3.4;ticket(b,x,y,i+1);b.box(x+1.65,y,3.8,2.2)
b.page()
b.p(2,0,'You are told only that red is showing. Which hidden color is the better guess? Explain using the tickets that could have produced that clue.')
bins(b,3,h=5)
b.p(3,12,'You are told only that blue is showing. Does the better guess change? Account for every ticket that could give this clue.')
bins(b,15,h=5);b.page();changed(b)
b.p(4,8,'Compare this chooser with drawing from all six face tickets and keeping red-showing rounds. Do they give the same chances for the hidden color?')
bins(b,12,('two-ticket chooser','six-ticket chooser'),h=7)
b.space(22,2);b.page()
b.text(0,'Return to all six face tickets. Removing a card also removes both of its tickets.',size=13)
b.p(5,2,'Remove exactly one card. Can you make red showing hide red for certain? Hide blue for certain? Give the two hidden colors the same chance?')
cards(b,6);b.box(0,11.5,18,5)
b.p(6,19,'Keep the cards and choose two tickets for the cup. Red must sometimes show. Find every pair that makes a red clue give each hidden color the same chance.')
b.space(22,2);b.save()

b=Book(45,'The visible side','Grades 4--5','grades-4-5');intro(b)
b.p(1,14,'Given only a red showing color, determine the chances of the hidden colors exactly. Do the same for a blue showing color.')
bins(b,18,('red showing','blue showing'),h=3.8);b.page()
b.p(2,0,'A friend says, "Red is showing, so only the red/red and red/blue cards remain. Each is one card, so each must have the same chance." Does the selection rule support that argument?')
cards(b,4);b.box(0,10,18,5)
b.p(3,18,'If the chooser also reveals the face mark, what happens to the uncertainty? Explain why covering the mark matters to the original game.')
b.space(22,2);b.page();changed(b)
b.p(4,8,'Does this way of producing a red clue change the chance that red is hidden? Give an exact comparison with the six-face-ticket rule.')
b.box(0,12,18,5)
b.p(5,19,'Could six red-showing rounds prove that the hidden-color chances differ? Give a possible set of hidden-color results that both chooser rules can produce.')
b.space(22.5,1);b.page()
b.text(0,'Use a cup containing a subset of the original six tickets, with no repeats. Each selected ticket has the same chance.',size=13)
b.p(6,2,'Find every subset that makes red showing equally likely to hide red or blue. Your cup must sometimes show red; it may also show blue.')
for i in range(6):ticket(b,i*2.9,5,i+1)
b.box(0,8,18,6)
b.p(7,16,'Can you keep only whole cards and make that red-clue game fair, with red still possible? Keep one, two, or all three cards, and remove both tickets whenever a card goes.')
b.space(20,4);b.save();build()
