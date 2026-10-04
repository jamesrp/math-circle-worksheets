from draw import *
def shape(x,y,n,kind,side=120):
    s=''; u=side/4
    pts={'triangle':[(0,4),(4,4),(4,0)],'diamond':[(0,2),(2,0),(4,2),(2,4)],'trap':[(.5,.5),(3.5,.5),(3,3.5),(1,3.5)]}.get(kind)
    if pts:
        s+=r'\fill[gray!22] '+' -- '.join(f'({x+a*u},{y+b*u})' for a,b in pts)+' -- cycle;\n'
    for i in range(n+1):
        s+=line(x+i*side/n,y,x+i*side/n,y+side,'gray!70')+line(x,y+i*side/n,x+side,y+i*side/n,'gray!70')
    if n==8:
        for i in range(5):
            s+=line(x+i*side/4,y,x+i*side/4,y+side,'line width=.8pt')+line(x,y+i*side/4,x+side,y+i*side/4,'line width=.8pt')
    if pts:s+=r'\draw[line width=1pt] '+' -- '.join(f'({x+a*u},{y+b*u})' for a,b in pts)+' -- cycle;\n'
    return s

def legend(y=0):
    s=rect(7,y,30,30,'fill=gray!15')+label(44,y+15,'=',16)
    for a in range(2):
        for b in range(2):s+=rect(51+a*15,y+b*15,15,15,'fill=gray!15')
    s+=text(92,y+2,r'1 big square\\ = 4 small squares',w=83,size=12)
    return s

def blanks(y,fine=False):
    return text(10,y,(r'Inside: \rule{15mm}{.3pt} big-square units\\[5mm]Cover: \rule{15mm}{.3pt} big-square units'),w=170,size=13)

for band,name in [('K--1','k-1'),('Grades 2--3','grades-2-3'),('Grades 4--5','grades-4-5')]:
    k=band=='K--1'; upper=band=='Grades 4--5'; pages=[]
    p=text(0,0,'Use whole squares inside the gray shape. Cover all squares with some gray area. A touch at an edge or corner adds no square.',size=12)
    p+=rect(12,25,24,24,'fill=gray!22')+label(24,55,'whole',11)
    p+=r'\fill[gray!22] (63,49)--(87,49)--(87,25)--cycle;'+'\n'+rect(63,25,24,24)+line(63,49,87,25,'line width=1pt')+label(75,55,'partial',11)
    p+=rect(114,25,24,24)+line(114,25,114,49,'line width=1.2pt')+label(126,55,'outside',11)
    p+=prob(1,'Mark all the whole squares inside the triangle. Cover the triangle with as few grid-square tiles as you can.' if k else 'Find an inside cover and an outside cover for the triangle. Use as many whole inside squares and as few outside-cover squares as possible.',65,size=14 if k else 13)
    p+=shape(33,96,4,'triangle')
    p+=text(15,224,r'Inside: \rule{13mm}{.3pt} big squares \qquad Cover: \rule{13mm}{.3pt} big squares',size=12)
    pages.append(p)
    if k:
        p=legend()
        p+=prob(2,'Cover this shape, then split two big tiles into four small tiles each. Choose the two big tiles that let you remove the most small tiles while keeping the gray shape covered.',43,size=14)
        p+=shape(33,87,4,'trap')
    else:
        p=prob(2,'Trap the diamond\'s area between an inside cover and an outside cover. Can you be certain its area is more than 3 big squares? Less than 13?')
        p+=shape(33,38,4,'diamond')+blanks(175)
        p+=text(15,218,'One grid square is 1 big-square unit.',size=12)
    pages.append(p)
    p=legend()
    p+=prob(3,'Use small squares to get more area inside the triangle and less area outside it in your cover. Show which pieces change from the big-square covers.' if k else 'Use the smaller squares to trap the triangle\'s area more tightly. State both bounds in big-square units.',43,size=14 if k else 13)
    p+=shape(33,86 if k else 76,8,'triangle')
    if not k:p+=blanks(207,True)
    pages.append(p)
    p=legend()
    p+=prob(4,'Change the diamond so four outside small squares become partly gray. Keep every big square whole, partial, or outside as it was.' if k else 'Find new bounds for the diamond. Compare the area left uncertain on the big grid and on the small grid.',43,size=14 if k else 13)
    p+=shape(33,86 if k else 76,8,'diamond')
    if not k:p+=blanks(207,True)
    pages.append(p)
    if not upper:
        p=prob(5,('Draw two shapes, one at a time, each with 3 whole and 3 partly gray squares. Make one with less than 4 big squares of gray and one with more than 5.' if k else 'Draw two different shapes, one at a time, with exactly 4 whole gray squares and 4 partly gray squares. Make one area less than 5 big-square units and the other greater than 7.'),size=14 if k else 13)
        p+=shape(33,44,4,'blank')
        p+=prob(6,'Keep the same whole and partial squares. Can you make the larger shape bigger again without filling another whole square?' if k else 'Could your shape\'s area be smaller than 4 big squares? Greater than 8? Decide what the square markings guarantee.',189,size=14 if k else 13)
        p+=text(15,223,'One grid square is 1 big-square unit.',size=12)
    else:
        p=legend()
        p+=prob(5,'Split exactly three big squares into four small squares each. Choose the three that most reduce the gap between your inside and outside bounds.',43)
        p+=shape(33,76,4,'trap')+blanks(207,True)
    pages.append(p)
    if upper:
        p=prob(6,'A big square is split into four small squares. Could the total inside area go down? Could the outside-cover area go up? Explain why your answers work for any of these shapes.')
        p+=legend(37)
        p+=shape(25,88,1,'triangle',30)+label(91,103,r'$\longrightarrow$',20)+shape(125,88,2,'triangle',30)
        p+=prob(7,'The original triangle on page 1 fits with a second copy into its 4-by-4 square. Find its exact area. Explain how that area fits between both pairs of bounds you found.',166)
        p+=text(5,198,'Smaller pictures of the original triangle; not to scale.',w=97,size=9)
        p+=shape(15,211,4,'triangle',23)+shape(62,211,8,'triangle',23)
        p+=text(112,202,r'Exact area: \rule{15mm}{.3pt}\\big-square units',w=70,size=12)
        pages.append(p)
    write(name,48,'Inside and outside covers',band,pages)
buildscript()
# For a diagonal triangle on an n-by-n grid, count cells below and cut by diagonal.
assert 4*3//2==6 and 4*5//2==10
assert 8*7//2/4==7 and 8*9//2/4==9
(ROOT/'checks.txt').write_text('Triangle coarse bounds 6,10; fine bounds 28/4=7,36/4=9; exact area 8. K Problem 2: remove at most 6 small tiles by refining any two corner cells. K Problem 4: each of 8 partial big cells has one outside small cell; four local outward boundary changes suffice. K Problem 5: width-3 rectangles of heights 7/6 and 11/6 have areas 3.5 and 5.5. Grades 2-3 Problem 5: width-4 rectangles of heights 9/8 and 15/8 have areas 4.5 and 7.5. All main grids are 120 mm square. Big unit stays 30 mm by 30 mm.\n')
