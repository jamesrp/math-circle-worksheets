from draw import *

def start(p):
    p.text(0,0,'Stretch a thread from O to another dot T. A dot exactly on the thread between O and T blocks T. B marks a blocker. Keep O fixed while you test.',size=13)
    p.dots(1,2.6,4,.9,[(4,2)],[(4,2),(2,1)])
    p.node(4.9,4.15,'T',12);p.node(2.4,5.3,'B',12);p.node(2.8,7,'hidden',12)
    p.dots(10,2.6,4,.9,[(3,2)],[(3,2)])
    p.node(13.05,4.15,'T',12);p.node(11.8,7,'visible',12)

def coord(p,y):
    p.text(0,y,'(4, 2) means 4 across and 2 up from O.',size=13)
    p.dots(1,y+1.3,4,.7,[],[(4,2)])
    p.line(1,y+4.1,3.8,y+4.1,'->,line width=.9pt')
    p.line(3.8,y+4.1,3.8,y+2.7,'->,line width=.9pt')
    p.node(2.4,y+4.95,'4 across',11);p.node(5.0,y+3.4,'2 up',11);p.node(5.9,y+2.15,'(4, 2)',12)

K=[]
p=Page();start(p);p.prob(1,8.4,'Which dots can you see from O? Circle every visible dot.',15);p.dots(4,11.5,4,2);K.append(p)
p=Page();p.prob(2,0,'Which circled targets are hidden? Find the blocker nearest O for each hidden target.',15);p.dots(4,3.2,4,2,[],[(4,4),(4,2),(2,4),(3,3)]);p.dots(4,14.5,4,2,[],[(4,0),(0,4),(2,2),(4,3)]);K.append(p)
p=Page();p.prob(3,0,'Find every target with exactly one dot between it and O. Then find every target with exactly two.',15);p.dots(3,4,6,2);p.ruled(20,3);K.append(p)
p=Page();p.prob(4,0,'Find a visible dot in each row above O and a row with only visible dots. Can you also find a hidden dot in every row?',15);p.dots(3,4,6,2);p.ruled(20,3);K.append(p)
p=Page();p.prob(5,0,'Which first dot after O hides the most other dots? Find every first dot that ties for the most.',15);p.dots(3,4,6,2);p.ruled(20,3);K.append(p)
build(31,'Hidden orchard','K--1','k-1',K)

G=[]
p=Page();start(p);p.prob(1,8.4,'Circle every dot visible from O. For three hidden dots, mark their first blocker.',14);p.dots(3,11,6,2);G.append(p)
p=Page();coord(p,0);p.prob(2,6.3,'Test these targets: (6, 4), (6, 3), (5, 3), (5, 2), (4, 4) and (4, 1). Find every dot between O and each target.',14);p.dots(3,9.5,6,2);G.append(p)
p=Page();p.prob(3,0,'Find all targets on this grid with exactly one blocker. Then find all targets with exactly two blockers.',14);p.dots(3,3,6,2);p.ruled(19,4);G.append(p)
p=Page();p.prob(4,0,'Which dots lie on the same straight line from O as (1, 1)? Make groups for (1, 1), (2, 1), (3, 2), (1, 2) and (1, 0).',14);p.dots(3,3,6,2);p.ruled(19,4);G.append(p)
p=Page();p.prob(5,0,'Find a number rule that predicts whether a dot is visible from O. Use it to predict (12, 8), (10, 7), (15, 5) and (11, 1). Explain how the rule matches a straight thread.',14);p.ruled(3,8)
p.prob(6,14,'A grid continues as far as you like. Give a row containing infinitely many visible dots, and explain why each one is visible.',14);p.ruled(17,6);G.append(p)
build(31,'Hidden orchard','Grades 2--3','grades-2-3',G)

G=[]
p=Page();start(p);p.prob(1,8.4,'Find three visible targets and three hidden targets with different numbers of blockers. Mark each blocker.',14);p.dots(3,11,6,2);G.append(p)
p=Page();coord(p,0);p.prob(2,6.3,'For each target, find the first dot after O on its line and every blocker: (6, 4), (6, 3), (5, 3), (6, 6), (6, 0) and (0, 6).',14);p.dots(3,9.5,6,2);G.append(p)
p=Page();p.prob(3,0,'Predict the first dot and number of blockers for (12, 8), (15, 10), (21, 14), (25, 15) and (13, 8). Explain a rule that works for any target with whole-number coordinates.',14);p.ruled(3,8)
p.prob(4,14,'A target is (a, b), with a and b positive whole numbers. Explain why a common divisor larger than 1 always produces a blocker. Does every blocker produce a common divisor?',14);p.ruled(17,6);G.append(p)
p=Page();p.prob(5,0,'List all the targets (a, b) whose two coordinates are each from 1 through 6 that have the same first visible dot as (6, 4). Repeat for (6, 3) and (6, 6). Explain why no target can belong to two different groups.',14);p.dots(3,3.5,6,2);p.ruled(19,4);G.append(p)
p=Page();p.prob(6,0,'Let d be the greatest whole number that divides both coordinates of a target. How does d determine the first dot after O and the number of blockers? Explain why there can be no extra dots between the ones your rule finds.',14);p.ruled(3.2,8)
p.prob(7,14,'Find an entire row of visible dots, an infinite collection of hidden dots, and a target with exactly 99 blockers. Explain each choice.',14);p.ruled(17,6);G.append(p)
build(31,'Hidden orchard','Grades 4--5','grades-4-5',G)
