from common import *

def icon(b,x,y,c,s=.35):
 if c=='A':b.put(fr'\draw[fill=orange!22,line width=.8pt] ({x-s},{-y-s}) rectangle ({x+s},{-y+s});')
 if c=='B':b.put(fr'\draw[fill=green!22,line width=.8pt] ({x},{-y}) circle ({s});')
 if c=='C':b.put(fr'\draw[fill=violet!22,line width=.8pt] ({x},{-y+s}) -- ({x+s},{-y-s}) -- ({x-s},{-y-s}) -- cycle;')
 if c=='D':b.put(fr'\draw[fill=cyan!22,line width=.8pt] ({x},{-y+s}) -- ({x+s},{-y}) -- ({x},{-y-s}) -- ({x-s},{-y}) -- cycle;')
 if c=='E':b.put(fr'\draw[fill=yellow!25,line width=.8pt] ({x-s},{-y-s}) -- ({x+s},{-y-s}) -- ({x+s},{-y}) -- ({x},{-y+s}) -- ({x-s},{-y}) -- cycle;')
def row(b,x,y,word='',w=4.7,h=1.8,labels=False):
 for i in range(3):
  b.box(x+i*w/3,y,w/3,h)
  if word:icon(b,x+(i+.5)*w/3,y+h*.43,word[i],min(.38,w/9))
  if word and labels:b.text(y+h*.72,word[i],x+i*w/3+.15,w/3-.2,9)
def mat(b,x,y):
 for i in range(3):b.box(x+i*4.7,y,4.7,6.1);b.text(y+.12,str(i+1),x+i*4.7+.15,1,11)
def tickets(b,x,y,nums):
 for i,n in enumerate(nums):b.box(x+i*1.2,y,1,1);b.text(y+.17,str(n),x+i*1.2+.3,.5,13)
def swapdemo(b,y):
 row(b,0,y,'ABC',4.3,1.7,True);b.arrow(4.7,y+.8,6.1,y+.8,'1 with 3');row(b,6.5,y,'CBA',4.3,1.7,True)
 b.arrow(11.1,y+.8,12.7,y+.8,'2 with 2');row(b,13.2,y,'CBA',4.3,1.7,True)
def swaprule(b,y=0):
 b.text(y,'Start A B C. Mix tickets 1, 2, 3 in the cup; draw and swap its slot with slot 1. Empty the cup, then mix tickets 2, 3; draw and swap its slot with slot 2. At each draw, all tickets in the cup have equal chances. Reset both sets for every new row. A slot may swap with itself.',size=13)
 tickets(b,0,y+3.1,[1,2,3]);b.text(y+3.3,'swap with slot 1',4,5,11)
 tickets(b,9.2,y+3.1,[2,3]);b.text(y+3.3,'swap with slot 2',12,6,11)
 swapdemo(b,y+4.8)
def chooser(b,y):
 b.text(y,'Mix the three picture cards in a cup. Each card has the same chance. Draw the first without looking and keep it out. Draw the second from the two left. Put the last card at the end. Return all cards for a new row.',size=13)
 icon(b,1,y+3,'C');b.arrow(2,y+3,3,y+3);icon(b,4,y+3,'A');b.arrow(5,y+3,6,y+3);row(b,7,y+2.1,'CAB',5,1.8,True)
 b.text(y+4.5,'Example: choose triangle, then square; circle is left.',size=12)

b=Book(43,'Shuffling picture cards','K--1','k-1')
b.p(1,0,'Make every different row using these three cards once each.')
row(b,1,1.7,'ABC',6,2.2,True);mat(b,2,5)
for i in range(6):row(b,(i%2)*9,13+(i//2)*3.3,w=7.8,h=2.5)
b.page();chooser(b,0)
b.p(2,6,'For each crossed-out first card, find every row still possible. Could two different first-two draws make the same row?')
for i,c in enumerate('ABC'):
 y=9+i*4.5;icon(b,.7,y+.7,c,.4)
 b.put(fr'\draw[line width=1pt] (0,{-y}) -- (1.4,{-y-1.4});')
 for j in range(4):row(b,2+(j%2)*8,y+(j//2)*1.9,w=7,h=1.55)
b.page();swaprule(b)
b.p(3,7.3,'Start with A B C and choose tickets to make every row. Can any row be made by two different ticket stories?')
mat(b,2,10)
for i in range(6):
 x=(i%3)*6.1;y=17+(i//3)*3.2
 tickets(b,x,y,['','']);row(b,x+2.6,y,w=3.1,h=1.4)
b.page()
b.p(4,0,'Remove one ticket from the first set, leaving the second set alone. Which rows become impossible for each missing ticket?')
for i,u in enumerate([1,2,3]):
 y=3+i*4.8;tickets(b,0,y,[v for v in [1,2,3] if v!=u])
 for j in range(2):row(b,4+j*7,y,w=6.4,h=2.2)
b.p(5,18,'Start with these two different rows and give both the same two-ticket story. Can they ever finish alike?')
row(b,0,21,'ABC',6,2,True);row(b,10,21,'CBA',6,2,True)
b.save()

b=Book(43,'Shuffling picture cards','Grades 2--3','grades-2-3')
chooser(b,0)
b.p(1,6,'Find every possible final row. Could the chooser give any row more chance than another? Use the possible choices to decide.')
for i in range(6):row(b,(i%2)*9,9+(i//2)*3.6,w=7.8,h=2.6)
b.space(21,3);b.page();swaprule(b)
b.p(2,7.3,'Start with A B C. Match each two-ticket story to the final row it makes. Does this give each row the same chance?')
for i,(u,v) in enumerate([(1,2),(2,2),(3,2),(1,3),(2,3),(3,3)]):
 x=(i%2)*9.2;y=9.7+(i//2)*4.3;tickets(b,x,y,[u,v]);row(b,x,y+1.3,w=7.8,h=2.5)
b.page()
b.p(3,0,'Start with B A C and use the same two-swap rule. Can you still make every row? Find the ticket story for each target.')
for i,word in enumerate(['ABC','ACB','BAC','BCA','CAB','CBA']):
 x=(i%2)*9.2;y=3+(i//2)*4.9;row(b,x,y,word,6.4,2,True);b.box(x,y+2.4,2,1.5);b.box(x+2.5,y+2.4,2,1.5)
b.p(4,19,'A friend says six random shuffles must show all six rows once. Can you make a possible six-shuffle story that settles this?')
b.space(22,2);b.page()
b.text(0,'Change the rule: use tickets 1, 2, 3 at every swap. Swap slot 1, then slot 2, then slot 3 with the chosen slot. Replace the ticket and mix after each draw.',size=13)
swapdemo(b,3)
row(b,0,5.2,'CBA',4.3,1.4,True);b.arrow(4.8,5.9,7,5.9,'3 with 1');row(b,7.5,5.2,'ABC',4.3,1.4,True)
b.p(5,7,'Start with A B C each time. Find several different three-ticket stories that give the same final row.')
for i in range(3):tickets(b,1,10+i*3.1,['','','']);row(b,9,9.6+i*3.1,w=7.5,h=2.1)
b.p(6,20,'There are 27 equally likely three-ticket stories. Could this rule give all six rows the same chance?')
b.space(23,1);b.save()

b=Book(43,'Shuffling picture cards','Grades 4--5','grades-4-5');chooser(b,0)
b.p(1,6,'Does this chooser give every order of A, B, C the same chance? Settle the question using every possible choice story.')
for i in range(6):row(b,(i%2)*9,9+(i//2)*3.6,w=7.8,h=2.5)
b.space(21,3);b.page();swaprule(b)
b.p(2,7.3,'Does this two-swap rule give every order the same chance? Find all its choice stories and their final orders.')
b.box(0,10,18,4.5)
b.p(3,15,'Start with C B A instead. Explain whether the chance of each final order changes, without listing every story again.')
row(b,0,18,'CBA',6,2,True);b.space(21,3);b.page()
b.text(0,'A new rule starts with A B C. Draw from 1, 2, 3 at each step: swap slot 1 with its choice, then slot 2 with its choice, then slot 3 with its choice. Replace and mix after each choice.',size=13)
b.p(4,3,'Can this rule give all six orders the same chance? Find an exact reason; a short run of random shuffles cannot settle the question.')
b.box(0,6,18,8)
b.p(5,15,'Another rule forbids swapping a slot with itself. Swap slot 1 with slot 2 or 3, then swap slots 2 and 3. Find every possible final order. Is this a fair shuffle of all six orders?')
row(b,0,19,'ABC',6,2,True);b.space(22,2);b.page()
b.p(6,0,'Design a four-card ticket-and-swap shuffle on paper that gives every order the same chance, with exactly one choice story per order. Explain why it meets both goals.')
for i,c in enumerate('ABCD'):
 b.box(i*4.5,3.1,4.5,2.5);icon(b,i*4.5+2.25,4,c,.45);b.text(4.9,c,i*4.5+2,.8,11)
b.box(0,7,18,4.5)
b.p(7,13,'Design a fair five-card version on paper with exactly one story for each final order. Specify the ticket sets and resets; how many equally likely stories does your rule have?')
for i,c in enumerate('ABCDE'):
 b.box(i*3.6,16.4,3.6,2.5);icon(b,i*3.6+1.8,17.3,c,.45);b.text(18.2,c,i*3.6+1.55,.8,11)
b.box(0,20,18,3.2);b.save()
build()
