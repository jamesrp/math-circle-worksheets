from draw import *
def ring(x,y,vals=None,span=42,r=7,gaps=False,letters=True,squares=False):
    vals=vals if vals is not None else [None]*4; n=len(vals)
    pts=[(x,y),(x+span,y),(x+span,y+span),(x,y+span)] if n==4 else [(x+span/2,y),(x+span,y+span),(x,y+span)]
    s=''; names='ABCD'
    for i,(a,b) in enumerate(pts):
        c,d=pts[(i+1)%n]; dist=math.hypot(c-a,d-b); vx=(c-a)/dist;vy=(d-b)/dist
        edge=(r/max(abs(vx),abs(vy))+1) if squares else (r+1)
        s+=line(a+vx*edge,b+vy*edge,c-vx*edge,d-vy*edge,'-{Stealth[length=2mm]}')
        if gaps:
            if n==4: offs=[(0,-5),(8,0),(0,5),(-8,0)][i]
            else:offs=[(7,-2),(0,6),(-7,-2)][i]
            s+=label((a+c)/2+offs[0],(b+d)/2+offs[1],str(abs(vals[i]-vals[(i+1)%n])),11)
    for i,(a,b) in enumerate(pts):
        if squares:s+=rect(a-r,b-r,r*2,r*2,'fill=white,rounded corners=1mm')
        else:s+=circle(a,b,r,'fill=white')
        if letters:s+=label(a,b+r+4 if (i>=2 if n==4 else i>=1) else b-r-4,names[i],9)
        if vals[i] is not None:s+=label(a,b,str(vals[i]),13)
    return s

def record(x,y,vals=None):
    vals=vals or ['']*4;s=''
    for i,v in enumerate(vals):
        s+=rect(x+i*14,y,14,11)+label(x+i*14+7,y+5.5,str(v),12)
        s+=label(x+i*14+7,y-4,'ABCD'[i],9)
    return s

def intro():
    s=text(0,0,'Use whole-number heights, including 0. Follow each arrow: the gap between its two old heights becomes the new height at its tail. Make every new tower before changing any old tower.',size=12)
    s+=label(41,37,'old',12)+label(144,37,'new',12)
    s+=ring(20,52,[1,4,2,0],42,7,True)+line(78,73,105,73,'-{Stealth[length=3mm]}')+ring(122,52,[3,2,2,1],42,7)
    s+=text(15,111,'Edge A to B has gap 3, so new A is 3.\\ All four gaps use the old ring.',size=12)
    return s

def mats(y=60):return ring(20,y,None,52,20,squares=True)+ring(113,y,None,52,20,squares=True)
for band,name in [('K--1','k-1'),('Grades 2--3','grades-2-3'),('Grades 4--5','grades-4-5')]:
    k=band=='K--1';upper=band=='Grades 4--5';pages=[]
    p=intro()+prob(1,'Build these starts and keep making new rings. Stop when all four towers are 0.' if k else 'Run each start until all four heights are 0. Which lasts longest?',133,size=14 if k else 13)
    for x,vs in zip([13,60,107,154],[[1,1,0,0],[1,0,1,0],[2,1,0,1],[0,0,0,2]]):p+=ring(x,177,vs,25,5,letters=False)
    pages.append(p)
    p=prob(2,'Choose heights from 0 to 4. Find a start that lasts as many moves as you can; count the move that makes all four towers 0.' if k else 'Choose starting heights from 0 to 5. Find a ring that lasts as many moves as you can. Count the move that first makes all four heights 0.',size=14 if k else 13)
    p+=text(0,25,'An all-zero start takes 0 moves. Use these big mats for all four-station starts.',size=11)
    p+=label(46,43,'old',12)+label(139,43,'new',12)+mats(71)
    p+=record(20,176)+text(97,176,r'Moves to zero: \rule{17mm}{.3pt}',w=85,size=12)
    p+=record(20,213)+text(97,213,r'Moves to zero: \rule{17mm}{.3pt}',w=85,size=12)
    pages.append(p)
    if k:
        p=prob(3,'Find different starts that become all zeros in one move.',size=14)
        p+=ring(20,47,None,40,8)+ring(117,47,None,40,8)
        p+=prob(4,'Find different starts that first become all zeros on the second move.',120,size=14)
        p+=ring(20,167,None,40,8)+ring(117,167,None,40,8)
    else:
        p=prob(3,'Could each ring be the result of one move? Find an old ring that makes it, or explain why no old ring can work.')
        p+=ring(28,53,[2,0,2,0],40,8)+ring(120,53,[1,1,1,0],40,8)
        p+=ring(28,147,[1,1,1,1],40,8)+ring(120,147,[0,0,0,2],40,8)
    pages.append(p)
    p=prob(5 if k else 4,'Try both starts with the same gap rule. Stop at all zeros or when the whole ring repeats.' if k else 'Use the gap rule on both rings. Keep going until the whole ring repeats or becomes all zeros. Does the number of stations change what can happen?',size=14 if k else 13)
    p+=ring(30,45,[1,0,0,0],28,6)+ring(127,45,[1,0,0],28,6)
    p+=label(46,91,'old',12)+label(139,91,'new',12)
    p+=ring(20,119,[None]*3,52,20,squares=True)+ring(113,119,[None]*3,52,20,squares=True)
    pages.append(p)
    if k:
        p=prob(6,'Put 0, 1, 2, and 4 around the four stations. Find an order that lasts longer than the other orders you try.',size=14)
        p+=ring(23,53,[0,1,2,4],42,9)+ring(123,53,[0,1,4,2],42,9)
        for y in [136,174,212]:p+=record(15,y)+text(95,y,r'Moves to zero: \rule{17mm}{.3pt}',w=80,size=12)
    elif not upper:
        p=prob(5,'Try different orders of 0, 1, 2, and 4. Which order lasts longest? Two rings count as different here only when their A, B, C, D heights differ.')
        for x,vs in [(25,[0,1,2,4]),(123,[0,1,4,2])]:p+=ring(x,48,vs,42,9)
        p+=prob(6,'Can a new tower be taller than every old tower? Can the tallest height stay the same for a move? Give an explanation or an example for each claim.',127)
        p+=ring(25,181,[0,1,2,4],42,8)+ring(123,181,None,42,8)
    else:
        p=prob(5,'Replace even heights by E and odd heights by O. Use this two-letter gap rule. Which letter rings are possible after four moves? Explain why you have checked every kind of start.')
        p+=text(5,34,'E and E give E.     O and O give E.',size=12)
        p+=text(5,44,'E and O give O.     O and E give O.',size=12)
        p+=ring(25,72,['E','O','E','E'],39,8)+line(81,92,104,92,'-{Stealth[length=3mm]}')+ring(123,72,['O','O','E','E'],39,8)
        p+=ring(25,170,None,42,9)+ring(123,170,None,42,9)
    pages.append(p)
    if upper:
        p=prob(6,'Compare these two starts through several moves. What happens if all starting heights are doubled? Does your explanation also work for tripling?')
        p+=ring(25,43,[1,4,2,0],38,8)+ring(123,43,[2,8,4,0],38,8)
        p+=prob(7,'Could any new height exceed the largest starting height? Explain why your answer holds however many moves are made.',110)
        p+=prob(8,'Do four nonnegative whole-number heights always reach all zeros? Explain why every such start finishes, or find a start that never reaches zero.',164)
        pages.append(p)
    write(name,49,'Four-tower differences',band,pages)
buildscript()
from itertools import product
def D(s):return tuple(abs(s[i]-s[(i+1)%len(s)]) for i in range(len(s)))
def rounds(s):
    seen=set();n=0
    while any(s) and s not in seen:seen.add(s);s=D(s);n+=1
    return n,not any(s)
assert D((1,4,2,0))==(3,2,2,1)
assert rounds((0,1,2,4))==(7,True)
assert all(rounds(s)[1] for s in product(range(6),repeat=4))
assert not rounds((1,0,0))[1]
for s in product(range(2),repeat=4):
    for _ in range(4):s=D(s)
    assert all(x%2==0 for x in s)
(ROOT/'checks.txt').write_text('All 1296 starts in 0..5 terminate. (0,1,2,4) needs 7 moves. Three-station (1,0,0) repeats. All 16 parity patterns are even after four rounds.\n')
