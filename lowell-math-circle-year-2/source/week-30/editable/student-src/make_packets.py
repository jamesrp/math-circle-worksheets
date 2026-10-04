from draw import *

def weights(p,vals,y,x0=0):
    for i,n in enumerate(vals):
        x=x0+i*3.3
        p.rect(x,y,2.65,2.25,'rounded corners=5pt,line width=.7pt')
        p.node(x+1.32,y+.42,n,15)
        for j in range(n):
            xx=x+.65+(j%3)*.65; yy=y+1.05+(j//3)*.38
            p.add(r'\fill ('+f'{xx},{-yy}'+') circle (1.5pt);')
def start(p):
    p.text(0,0,'Keep the target on the left. Each weight may go on either pan or stay off. Use each weight at most once. Equal totals balance.',size=13)
    p.text(0,1.5,'Target 3; weights 1 and 4',size=12)
    weights(p,[1,4],2.2)
    p.line(8.0,3.2,9.3,3.2,'->,line width=.8pt');p.node(12.4,3.1,'put 1 beside the target',12)
    p.pan(0,5.1,3,[1],[4]);p.node(8.5,8.8,'3 + 1 = 4',13)

def blanks(p,targets,y,gap=4.6):
    for i,t in enumerate(targets):p.pan(0,y+i*gap,t)

K=[]
p=Page();start(p);p.prob(1,10,'Use weights 1 and 3 to balance targets 1, 2, 3 and 4.',15);weights(p,[1,3],11.6);blanks(p,[2,4],14.6);K.append(p)
p=Page();p.prob(2,0,'Use weights 1 and 2. Which targets from 1 through 5 can you balance?',15);weights(p,[1,2],1.65);p.targets(range(1,6),4.7,5);blanks(p,[3,4,5],7);K.append(p)
p=Page();p.prob(3,0,'Try weights 1 and 4, then weights 1 and 3. Does either kit balance more targets from 1 through 6?',15);weights(p,[1,4],2);weights(p,[1,3],2,9);p.targets(range(1,7),5,6);blanks(p,[2,5],8);p.ruled(19,4);K.append(p)
p=Page();p.prob(4,0,'Choose two different weights from 1, 2, 3 and 4. Find every kit that can balance all four targets: 1, 2, 3 and 4.',15);weights(p,[1,2,3,4],2);blanks(p,[2,4],6);p.ruled(17,5);K.append(p)
p=Page();p.prob(5,0,'You have weights 1 and 3; choose one more weight from 8, 9 and 10. Which choice balances every target from 5 through 13?',15);weights(p,[1,3],2.1);weights(p,[8,9,10],5.1);p.targets(range(5,14),8.1,5);blanks(p,[5,13],12.3);p.ruled(22,2);K.append(p)
build(30,'Two-pan weight kits','K--1','k-1',K)

G=[]
p=Page();start(p);p.prob(1,10,'Compare the kits 1 and 2, 1 and 3, and 1 and 4. Which targets from 1 through 6 can each kit balance?',14);
for i,kit in enumerate(['1 and 2','1 and 3','1 and 4']):
    p.text(0,12.1+i*2.2,kit,w=3,size=12)
    for j,n in enumerate(range(1,7)):p.rect(3.5+j*2.2,12+i*2.2,1.8,1.2);p.node(4.4+j*2.2,12.6+i*2.2,n,16)
p.pan(0,19.2,2);G.append(p)
p=Page();p.prob(2,0,'You have weights 1 and 3. Choose one more whole-number weight so that the kit balances every target from 1 through 13. Test your choice.',14);weights(p,[1,3],2);p.targets(range(1,14),5,7);blanks(p,[5,8,13],9);G.append(p)
p=Page();p.prob(3,0,'Compare these kits: 1, 3, 8; 1, 3, 9; 1, 3, 10. For each, find the first target it cannot balance.',14)
for i,kit in enumerate(['1, 3, 8','1, 3, 9','1, 3, 10']):p.text(0,2+i*7,kit,size=16);p.ruled(4+i*7,4)
G.append(p)
p=Page();p.prob(4,0,'Use weights 1, 3 and 8 to balance 4 in every possible way. Then find every way to balance 4 with 1, 3 and 9.',14);p.text(0,2.2,'1, 3, 8',size=12);blanks(p,[4,4],3.2);p.text(0,12.4,'1, 3, 9',size=12);p.pan(0,13.4,4);p.ruled(19,4);G.append(p)
p=Page();p.prob(5,0,'Could a different three-weight kit balance every target from 1 through 14? Find one or explain why there cannot be one.',14);p.ruled(3,7)
p.prob(6,13,'Choose a fourth weight to add to 1, 3 and 9. Make the longest possible unbroken run of targets starting at 1, and explain why your kit reaches all of them.',14);p.ruled(16,7);G.append(p)
build(30,'Two-pan weight kits','Grades 2--3','grades-2-3',G)

G=[]
p=Page();start(p);p.prob(1,10,'Choose two different whole-number weights that balance every target from 1 through 4. Find every possible kit.',14);blanks(p,[2,4],13);p.ruled(23,1);G.append(p)
p=Page();p.prob(2,0,'Add one weight to 1 and 3. Which choice balances the longest unbroken run of targets starting at 1? Explain why a smaller or larger choice cannot do better.',14);p.targets(range(1,16),3,8);blanks(p,[5,7],8);p.ruled(20,3);G.append(p)
p=Page();p.prob(3,0,'Can any positive target be balanced in two different ways with weights 1, 3 and 9? Decide for every target this kit can balance.',14);blanks(p,[4,7],3);p.ruled(14,7);G.append(p)
p=Page();p.prob(4,0,'Could any three-weight kit balance every target from 1 through 14? Find one or explain why none can work.',14);p.ruled(3,8)
p.prob(5,15,'Choose three different whole-number weights. How many different positive targets can your kit balance? Can another kit balance more, even if there are gaps?',14);p.ruled(18,5);G.append(p)
p=Page();p.prob(6,0,'Use the kit 1, 3 and 9. Add one weight so that the new kit balances every target in the longest possible run starting at 1, each in exactly one way. Explain why there are neither gaps nor repeated answers.',14);p.ruled(3.5,7)
p.prob(7,14,'With five weights, what is the longest run of whole-number targets starting at 1 that any kit could balance? Give a kit that reaches your bound, and explain why it works.',14);p.ruled(17,6);G.append(p)
build(30,'Two-pan weight kits','Grades 4--5','grades-4-5',G)
