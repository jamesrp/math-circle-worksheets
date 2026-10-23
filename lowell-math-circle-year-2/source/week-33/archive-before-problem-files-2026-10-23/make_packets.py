from draw import *
from itertools import product

def start(p):
    p.text(0,0,'Each bead may be A or B; one-color rings are allowed. Read clockwise from the start arrow. The bead order is the readout. Rings count as the same when turning makes them match. Keep them face up; do not flip them over.',size=13)
    for x,i,word in [(2.5,0,'AAB'),(8.5,1,'ABA'),(14.5,2,'BAA')]:
        p.ring(x,4.6,3,'AAB',1.3,i,.29);p.node(x,6.65,word,15)
    p.line(4.4,4.6,6.45,4.6,'->,line width=.8pt');p.line(10.4,4.6,12.45,4.6,'->,line width=.8pt')
    p.text(4.4,3.1,'move start',w=3,size=10);p.text(10.4,3.1,'move start',w=3,size=10)

def mats(p,n,y):
    p.ring(4.4,y,n,None,3.65,0,.42)
    p.ring(14.0,y,n,None,3.65,0,.42)

def card(p,x,y,word,w=8.8,h=3.9,num=None):
    p.rect(x,y,w,h,'line width=.65pt')
    n=len(word); small=w<6
    step=.73 if small else 1.5
    radius=.245 if small else .47
    left=x+(w-(n-1)*step)/2
    cy=y+(1.0 if small else 1.7)
    for i,c in enumerate(word):
        X=left+i*step
        p.add(r'\draw[fill='+('white' if c=='A' else 'gray!60')+'] ('+f'{X},{-cy}'+') circle ('+str(radius)+'cm);')
        p.node(X,cy,c,9 if small else 15)
    p.node(left,y+.3,'start',7 if small else 10)
    p.line(left-radius,y+h-.45,left+(n-1)*step+radius,y+h-.45,'->,line width=.6pt')
    if num is not None:p.node(x+w-.25,y+.3,num,7 if small else 9)

def threecards(p,problem,text):
    p.prob(problem,0,text,14)
    for i,t in enumerate(product('AB',repeat=3)):
        card(p,(i%2)*9.5,2.5+(i//2)*5.1,''.join(t),num=i+1)

def fivecards(p,problem,text):
    p.prob(problem,0,text,14)
    for i,t in enumerate(product('AB',repeat=5)):
        card(p,(i%4)*4.7,2.5+(i//4)*2.65,''.join(t),w=4.4,h=2.3,num=i+1)

K=[]
p=Page();start(p);p.prob(1,8,'Make every different three-bead ring using A and B.',15);mats(p,3,15);p.ruled(22,2);K.append(p)
p=Page();threecards(p,2,'Put cards in the same group when they make the same ring. Do all groups have the same number of cards?');K.append(p)
p=Page();p.prob(3,0,'Find every different four-bead ring with two A beads and two B beads.',15);mats(p,4,8);mats(p,4,18);K.append(p)
p=Page();p.prob(4,0,'Make four-bead rings with one, two, three or four different readouts. Which are possible?',15);mats(p,4,8);mats(p,4,18);K.append(p)
p=Page();p.prob(5,0,'Find every different five-bead ring with two A beads and three B beads. How many different readouts does each have?',15);mats(p,5,8);mats(p,5,18);K.append(p)
p=Page();p.prob(6,0,'Use both A and B on a six-bead ring. Find rings with two, three and six different readouts.',15);mats(p,6,8);mats(p,6,18);K.append(p)
build(33,'Prime-length necklaces','K--1','k-1',K)

G=[]
p=Page();start(p);p.prob(1,8,'Make every different three-bead ring using A and B. Find all its readouts as you move the start.',14);mats(p,3,15);p.ruled(22,2);G.append(p)
p=Page();threecards(p,2,'Group cards that make the same ring. How many groups are there, and how many cards are in each group?');G.append(p)
p=Page();p.prob(3,0,'Make four-bead rings with exactly one, two, three or four different readouts. For each impossible number, explain why it cannot happen.',14);mats(p,4,8);mats(p,4,18);G.append(p)
p=Page();fivecards(p,4,'Group these five-bead cards by the rings they make. Find the size of each group and the total number of different rings.');G.append(p)
p=Page();p.prob(5,0,'Can a five-bead ring using both A and B have fewer than five different readouts? Find one or explain why it cannot happen.',14);mats(p,5,8);p.ruled(14,3)
p.prob(6,18,'Someone divides 32 by 5 to count the five-bead rings. What went wrong? Find a calculation that counts them correctly.',14);p.ruled(21,3);G.append(p)
build(33,'Prime-length necklaces','Grades 2--3','grades-2-3',G)

G=[]
p=Page();start(p);p.prob(1,8,'Find every three-bead ring using A and B. How many different readouts does each ring have?',14);mats(p,3,15);p.ruled(22,2);G.append(p)
p=Page();threecards(p,2,'Group the eight cards by rotation. Explain how their group sizes give the number of different rings, and why dividing eight by three does not work.');G.append(p)
p=Page();p.prob(3,0,'Find four-bead rings with one, two, three or four different readouts, or explain why a requested number is impossible. What feature lets a mixed ring repeat early?',14);mats(p,4,8);mats(p,4,18);G.append(p)
p=Page();fivecards(p,4,'Group the 32 cards by rotation. Use the group sizes to count five-bead rings, and explain why these group sizes differ from the four-bead case.');G.append(p)
p=Page();p.prob(5,0,'A prime number has exactly two positive divisors: 1 and itself. What numbers of different readouts are possible for a ring of prime length that uses at least two colors? Find a rule and explain it.',14);p.ruled(3,8)
p.prob(6,14,'How many five-bead rings can be made when each bead may be any of three colors? Find a counting rule for c colors and any prime length p, and explain what it tells you about divisibility.',14);p.ruled(17,6);G.append(p)
build(33,'Prime-length necklaces','Grades 4--5','grades-4-5',G)
