from draw import *
BS=chr(92)
def path(x,y,pts,opts='line width=1.1pt'):
    return BS+'draw['+opts+'] '+' -- '.join(f'({x+a},{y+120-b})' for a,b in pts)+';\n'
def stairs(n):
    pts=[(0,0)]
    for i in range(n):pts.extend([((i+1)*160/n,i*120/n),((i+1)*160/n,(i+1)*120/n)])
    return pts

def diagram(y=45,paths=(),corridor=None,diag=True):
    x=10;s=''
    if corridor:
        d=corridor;pts=[(0,120),(0,120-d),(160-d/.75,0),(160,0),(160,d),(d/.75,120)]
        s+=BS+'fill[gray!20] '+' -- '.join(f'({x+a},{y+b})' for a,b in pts)+' -- cycle;\n'
    s+=rect(x,y,160,120,'gray!25,line width=.4pt')
    if diag:s+=line(x,y+120,x+160,y,'densely dotted,line width=.8pt')
    for pts,opts in paths:s+=path(x,y,pts,opts)
    s+=circle(x,y+120,1.4,'fill=black')+circle(x+160,y,1.4,'fill=black')
    s+=label(x-4,y+124,'S',11)+label(x+164,y-2,'F',11)
    s+=label(x+80,y+128,'160 mm',11)+(BS+'node[rotate=90,font='+BS+'small] at ('+str(x-7)+','+str(y+60)+') {120 mm};'+chr(10))
    return s

def calibration(y=221):
    return line(10,y,110,y,'line width=.7pt')+line(10,y-2,10,y+2)+line(110,y-2,110,y+2)+label(60,y+6,'100 mm',10)

def example():
    s=text(0,0,'A staircase goes only right and up. Measure along all its pieces.',size=12)
    s+=rect(15,26,40,30,'gray!60')
    pts=[(15,56),(25,56),(25,36),(55,36),(55,26)]
    for a,b in zip(pts,pts[1:]):s+=line(*a,*b,'line width=1pt')
    for x,y,t in [(20,61,'A: 10'),(17,45,'C: 20'),(40,31,'B: 30'),(63,30,'D: 10')]:s+=label(x,y,t,9)
    s+=line(73,43,86,43,'-{Stealth[length=2mm]}')
    s+=rect(96,28,10,7,'fill=gray!15')+rect(106,28,30,7,'fill=gray!15')
    s+=label(101,31.5,'A',9)+label(121,31.5,'B',9)+label(145,31.5,'40 mm',10)
    s+=rect(96,48,20,7,'fill=gray!15')+rect(116,48,10,7,'fill=gray!15')
    s+=label(106,51.5,'C',9)+label(121,51.5,'D',9)+label(145,51.5,'30 mm',10)
    s+=label(117,23,'right pieces',10)+label(116,43,'up pieces',10)
    return s

for band,name in [('K--1','k-1'),('Grades 2--3','grades-2-3'),('Grades 4--5','grades-4-5')]:
    k=band=='K--1';upper=band=='Grades 4--5';pages=[]
    p=example()+prob(1,'Make two different staircases from S to F. Use string to compare their lengths.',73,size=14 if k else 13)
    p+=diagram(104,diag=False)
    pages.append(p)
    p=prob(2,'Follow both staircases with string. Compare the two pieces of string.' if k else 'Compare the lengths of these two staircases. Find their exact lengths using the width and height.',size=14 if k else 13)
    p+=diagram(42,[(stairs(1),'line width=1.8pt'),([(0,0),(0,60),(80,60),(80,120),(160,120)],'dashed,line width=1.4pt')])
    if k:p+=text(9,184,'Circle: same length / solid longer / dashed longer',size=12)
    else:p+=text(9,184,('Solid: '+BS+'rule{20mm}{.3pt} mm     Dashed: '+BS+'rule{20mm}{.3pt} mm'),size=12)
    p+=calibration()
    pages.append(p)
    p=prob(3,'Make a staircase that stays inside the gray strip, closer to the shortcut than this one reaches. Compare the staircase lengths with string.' if k else 'Make a staircase inside the gray strip, with a smaller greatest vertical gap from the diagonal than this path. Compare the two staircase lengths with the diagonal\'s length.',size=14 if k else 13)
    p+=diagram(45,[(stairs(4),'line width=1.1pt')],corridor=15)
    p+=text(10,184,'The straight diagonal is 200 mm long.'+('' if k else ' The strip reaches 15 mm vertically above and below it.'),w=174,size=12)+calibration()
    pages.append(p)
    p=prob(4,'Make a staircase inside the gray strip with as few turns as you can. Its pieces may follow the edge of the strip.' if k else 'Find the fewest turns possible for an S-to-F staircase inside the gray strip. Its pieces may follow the strip\'s boundary. Explain why fewer turns cannot work.',size=14 if k else 13)
    p+=diagram(45,corridor=15)
    if not k:p+=text(10,184,'The gray strip reaches 15 mm vertically above and below the dotted diagonal, clipped by the rectangle.',w=174,size=12)
    p+=calibration()
    pages.append(p)
    if k:
        p=prob(5,'A path may now go left as well as right and up. Make two different S-to-F paths that use the same amount of string and more than a staircase.',size=14)
        p+=diagram(40)
        p+=prob(6,'Can a path with a leftward piece use less string than a staircase?',180,size=14)
        p+=calibration(225)
    elif not upper:
        p=prob(5,'Allow leftward pieces as well as rightward and upward pieces. Make two very different S-to-F paths of length 360 mm. Could such a path be shorter than 280 mm? Explain your answer.')
        p+=diagram(45)
        p+=text(10,187,'A straight diagonal is 200 mm long.',size=12)+calibration()
    else:
        p=prob(5,'Fit a staircase inside this narrower gray strip. Can the new staircase be shorter than the one you drew in the wider strip? Explain your answer.')
        p+=diagram(45,corridor=8)
        p+=text(10,184,'The strip reaches 8 mm vertically above and below the diagonal, clipped by the rectangle.',w=174,size=12)+calibration()
    pages.append(p)
    if upper:
        p=prob(6,'Find this path\'s exact length. It goes left once. Explain which part of your argument about right-and-up staircases no longer applies.')
        route=[(0,0),(80,0),(80,40),(40,40),(40,80),(160,80),(160,120)]
        p+=diagram(42,[(route,'line width=1.2pt')])
        # Mark the route's essential segment lengths without requiring ruler accuracy.
        for x,y,t in [(50,157,'80'),(96,142,'40'),(70,128,'40'),(44,102,'40'),(110,76,'120'),(177,61,'40')]:p+=label(x,y,t,10)
        p+=prob(7,'A staircase may use more and smaller right-and-up pieces. Could any finite number of pieces give the same length as the 200 mm diagonal? Explain which distances can shrink and which length stays the same.',184)
        pages.append(p)
    write(name,50,'Staircases and lengths',band,pages)
buildscript()
for n in [1,2,4,8]:
    ps=stairs(n);length=sum(abs(a-c)+abs(b-d) for (a,b),(c,d) in zip(ps,ps[1:]));assert length==280
assert 120**2+160**2==200**2
# An eight-horizontal-piece centered staircase fits the narrow 8 mm corridor.
ps=[(0,0),(0,7.5)]
for i in range(1,9):
    ps.append((20*i,15*i-7.5));ps.append((20*i,min(120,15*i+7.5)))
assert ps[-1]==(160,120) and max(abs(b-.75*a) for a,b in ps)==7.5
(ROOT/'checks.txt').write_text('All monotone stairs have length 280 mm. Diagonal 200 mm. An 8-horizontal-piece centered staircase fits the 8 mm vertical corridor, with maximum deviation 7.5 mm. Left-once path length 360 mm.\n')
