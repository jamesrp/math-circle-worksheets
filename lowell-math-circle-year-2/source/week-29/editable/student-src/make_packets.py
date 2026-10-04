from draw import *

def start(p):
    p.text(0,0,'Put whole rods end to end. Leave no gaps or overlaps. You may use a length more than once. Changing the order of the same rods does not make a new way.',size=13)
    p.rodkey([3,4],2)
    p.strip(0,3.6,7,label=False); p.rect(0,3.6,3,1,'line width=1.5pt');p.rect(3,3.6,4,1,'line width=1.5pt');p.node(1.5,4.1,3);p.node(5,4.1,4);p.node(9,4.1,'3 + 4 = 7',14)

K=[]
p=Page();start(p);p.prob(1,5.7,'Which lengths can you build with 3-rods and 4-rods?',15)
for i,n in enumerate([1,2,5,6,8,9,10]):p.strip(0,7.1+i*2.05,n)
K.append(p)
p=Page();p.prob(2,0,'Find every way to make 12 and 15 with 3-rods and 4-rods.',15)
for y,n in [(2,12),(5.5,12),(11,15),(14.5,15)]:p.strip(0,y,n)
p.ruled(19,3);K.append(p)
p=Page();p.prob(3,0,'Use 3-rods and 5-rods. Which lengths can you build?',15);p.rodkey([3,5],1.65)
for i,n in enumerate([4,7,8,9,10,11,12]):p.strip(0,3.4+i*2.6,n)
K.append(p)
p=Page();p.prob(4,0,'Use 3-rods and 4-rods to build every length from 6 through 18. Could you keep going forever?',15)
p.targets(range(6,19),2,7);p.text(0,5.7,'Mark a target on a ruler and build from 0 to the mark.',size=12);p.ruler(0,7,18);p.ruler(0,11,18);p.ruled(16,5);K.append(p)
p=Page();p.prob(5,0,'Use 2-rods and 4-rods to build lengths from 1 through 12. Show why some lengths cannot be built.',15);p.rodkey([2,4],1.8);p.targets(range(1,13),4,6);p.ruler(0,9,12);p.ruler(0,13,12);p.ruled(18,4);K.append(p)
p=Page()
p.prob(6,0,'Choose two rod lengths from 2, 3, 4 and 5. Which pairs can build every target from 6 through 12?',15);p.rodkey([2,3,4,5],2);p.targets(range(6,13),4,7);p.ruler(0,7,12);p.ruler(0,11,12);p.ruled(16,6);K.append(p)
build(29,'Two-length builders','K--1','k-1',K)

G=[]
p=Page();start(p);p.prob(1,5.7,'Use 3-rods and 4-rods. Find all the lengths from 1 through 16 that can be built, and mark the ones that cannot.',14);p.targets(range(1,17),8,8);p.text(0,11.5,'Mark a target on a ruler and build from 0 to the mark.',size=12);p.ruler(0,13,16);p.ruler(0,17,16);p.ruled(21,2);G.append(p)
p=Page();p.prob(2,0,'Find every way to make 12, 16 and 24 with 3-rods and 4-rods. Rod order does not count.',14)
for i,n in enumerate([12,16,24]):p.node(.5,2.4+i*7,n,18);p.ruled(4+i*7,4)
G.append(p)
p=Page();p.prob(3,0,'Use 3-rods and 5-rods. Find all the impossible lengths from 1 through 20. Is there a last impossible length?',14);p.rodkey([3,5],1.9);p.targets(range(1,21),4,7);p.ruled(10,11);G.append(p)
p=Page();p.prob(4,0,'For each pair of rods, build a small collection that convinces someone that every target after a certain length can be made. Say where the gaps stop.',14);p.rodkey([3,4],2);p.ruled(5,6);p.rodkey([3,5],13);p.ruled(16,6);G.append(p)
p=Page();p.prob(5,0,'Use 4-rods and 7-rods. Find the last impossible length, and explain why there are no later gaps.',14);p.rodkey([4,7],1.8);p.targets(range(12,29),4,8);p.ruled(10,4)
p.prob(6,15,'Someone says every pair of rod lengths eventually has no more gaps. Test 2 and 4, then 4 and 7. Is the claim true?',14);p.ruled(18,5);G.append(p)
build(29,'Two-length builders','Grades 2--3','grades-2-3',G)

G=[]
p=Page();start(p);p.prob(1,5.7,'For 3-rods and 4-rods, find every impossible positive length. Explain why your list is complete.',14);p.targets(range(1,21),8,7);p.ruled(14,9);G.append(p)
p=Page();p.prob(2,0,'Find the last impossible length for each pair: 3 and 5; 4 and 5; 4 and 7. For each pair, give a finite collection of builds that settles every longer target.',14)
for i,s in enumerate(['3 and 5','4 and 5','4 and 7']):p.text(0,2.4+i*7,s,bold=False);p.ruled(4+i*7,4)
G.append(p)
p=Page();p.prob(3,0,'Which lengths from 18 through 29 can be built with 4-rods and 7-rods? Convince someone without checking twelve separate cases.',14);p.targets(range(18,30),3,6);p.ruled(8,6)
p.prob(4,17,'Can 4-rods and 7-rods make 17? Explain your answer.',14);p.ruled(20,3);G.append(p)
p=Page();p.prob(5,0,'Which pairs have infinitely many impossible lengths: 2 and 4; 3 and 6; 4 and 6; 3 and 5; 4 and 7? Find a rule that separates them and explain it.',14);p.ruled(3,8)
p.prob(6,14,'Find two different ways to build 24 with 3-rods and 4-rods, then find all the ways. Which replacement of rods changes one way into another?',14);p.ruled(17,6);G.append(p)
p=Page();p.prob(7,0,'Predict the last impossible length for 5-rods and 7-rods, then test your prediction. Compare the answer with your earlier pairs and propose a rule for pairs that eventually have no gaps.',14);p.targets(range(19,32),3,7);p.ruled(8,5)
p.prob(8,16,'Invent paper rods of two different whole-number lengths a and b that have no common divisor larger than 1. Explain why some finite group of builds must settle every sufficiently long target.',14);p.ruled(19,4);G.append(p)
build(29,'Two-length builders','Grades 4--5','grades-4-5',G)
