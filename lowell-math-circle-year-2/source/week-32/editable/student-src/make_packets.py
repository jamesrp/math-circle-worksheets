from draw import *

def start(p):
    p.text(0,0,'Keep square edges on grid lines. Cover rectangles with no gaps, overlaps, or overhang. For the biggest-square rule, cover the largest square at one end, then repeat on the rectangle left over.',size=13)
    p.gridrect(.5,2.5,5,2,.7)
    p.line(4.4,3.2,5.4,3.2,'->,line width=.8pt')
    p.gridrect(6,2.5,5,2,.7);p.rect(6,2.5,1.4,1.4,'fill=gray!20,line width=1.2pt');p.node(6.7,3.2,2,12)
    p.line(10,3.2,11,3.2,'->,line width=.8pt')
    p.gridrect(11.7,2.5,3,2,.7)
    p.text(5.8,4.5,'cover a 2 by 2 square',w=5,size=11)
    p.text(11.4,4.5,'3 by 2 remains',w=5,size=11)

K=[]
p=Page();start(p);p.prob(1,6,'Cover both rectangles with the biggest-square rule. Which square comes last?',15);p.gridrect(1,8.5,6,4);p.gridrect(1,15.5,8,4);K.append(p)
p=Page();p.prob(2,0,'Predict whether the last squares will match. Test both rectangles with the biggest-square rule.',15);p.gridrect(1,3,7,4);p.gridrect(1,12,8,5);K.append(p)
p=Page();p.prob(3,0,'Try the biggest-square rule on these rectangles. Will they end with the same size square?',15);p.gridrect(1,3,9,6);p.gridrect(1,14,10,6);K.append(p)
p=Page();p.prob(4,0,'Cover each rectangle with squares that are all the same size. Find the biggest square size that works.',15);p.gridrect(1,3,6,4);p.gridrect(1,12,8,6);K.append(p)
p=Page();p.prob(5,0,'Find every rectangle you can make with four 3 by 3 squares, counting turns as the same shape. Will their last squares match under the biggest-square rule?',15)
for i in range(4):p.gridrect(1+i*4.1,3,3,3)
p.workgrid(1,9,12,8);p.ruled(21,2);K.append(p)
build(32,'Squares inside rectangles','K--1','k-1',K)

G=[]
p=Page();start(p);p.prob(1,6,'Use the biggest-square rule on both rectangles. Record the square sizes in the order you use them.',14);p.gridrect(1,8.5,10,6);p.gridrect(1,17,8,5)
for y in [10,12,18.5,20.5]:p.line(12,y,18.5,y,'gray!45,line width=.35pt')
G.append(p)
p=Page();p.prob(2,0,'Try the biggest-square rule on these rectangles. How does changing one side change the last square?',14);p.gridrect(1,3,12,8);p.gridrect(1,14,12,9);G.append(p)
p=Page();p.prob(3,0,'Cover each rectangle with identical squares. Find every whole-number square size that works, and decide which is biggest.',14);p.gridrect(1,3,12,8);p.gridrect(1,14,10,6);G.append(p)
p=Page();p.prob(4,0,'Try the biggest-square rule on these rectangles and sort them by the side length of their last square. Predict the last square for a 6 by 10 rectangle and explain your prediction.',14);p.gridrect(.5,3.5,7,6);p.gridrect(10,3.5,8,6);p.gridrect(.5,12.5,9,6);p.ruled(21,3);G.append(p)
p=Page();p.prob(5,0,'How is the last square from the biggest-square rule related to the biggest identical squares that can cover the original rectangle? Explain using a rectangle you have tried.',14);p.ruled(3,4)
p.prob(6,8,'Make three rectangles with different first squares and the same last square of side 3. Choose each starting side from 3, 6, 9 and 12.',14);p.workgrid(1,11.5,12,12);G.append(p)
build(32,'Squares inside rectangles','Grades 2--3','grades-2-3',G)

G=[]
p=Page();start(p);p.prob(1,6,'Apply the biggest-square rule to both rectangles. Record every square size, including repeated sizes, and compare the last squares.',14);p.gridrect(1,8.5,10,6);p.gridrect(1,17,8,5)
for y in [10,12,18.5,20.5]:p.line(12,y,18.5,y,'gray!45,line width=.35pt')
G.append(p)
p=Page();p.prob(2,0,'Predict the last square in each rectangle, then test. Find a rule that predicts the last square from the two starting side lengths.',14);p.gridrect(1,3,15,9);p.gridrect(1,15,14,8);G.append(p)
p=Page();p.prob(3,0,'For each rectangle, find every size of identical whole-grid square that can cover it. Explain why your list is complete.',14);p.gridrect(1,3,12,8);p.gridrect(1,14,15,9);G.append(p)
p=Page();p.prob(4,0,'A 14 by 8 rectangle loses an 8 by 8 square and leaves a 6 by 8 rectangle. Which whole-number lengths measure both edges exactly before the cut? Which work afterward? Explain why these two lists always match after a biggest-square cut.',14)
p.gridrect(.5,4.5,14,8,.62);p.rect(.5,4.5,8*.62,8*.62,'fill=gray!15,line width=1.1pt');p.node(2.98,6.98,'8 by 8',13);p.line(9.6,7,10.7,7,'->,line width=.8pt');p.gridrect(11.5,4.5,6,8,.62);p.ruled(11.7,3)
p.prob(5,16,'Explain why the last square from the biggest-square rule is the largest whole-grid square that can tile the starting rectangle using identical copies.',14);p.ruled(19,4);G.append(p)
p=Page();p.prob(6,0,'Choose a longer side from 9 through 15 and a shorter side from 2 through 8. Which rectangle produces the most different square sizes under the biggest-square rule? Find every rectangle that ties.',14);p.workgrid(1,3.5,15,8);p.workgrid(1,14.5,15,8);G.append(p)
build(32,'Squares inside rectangles','Grades 4--5','grades-4-5',G)
