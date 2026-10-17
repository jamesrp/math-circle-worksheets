#!/usr/bin/env python3
"""Generate self-contained LaTeX/TikZ. All dimensions below are millimeters."""
from pathlib import Path
from math import sqrt
ROOT=Path(__file__).resolve().parent

def text(x,y,w,s,size=12):
    return rf'\node[anchor=north west,inner sep=0pt,text width={w}mm,font=\fontsize{{{size}}}{{{size*1.28}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'
def line(points,style='thick'):
    return '\\draw['+style+'] '+' -- '.join(f'({x},{y})' for x,y in points)+';\n'
def box(x,y,w,h,label='',dashed=True):
    s=rf'\draw[{"dashed," if dashed else ""}gray!65] ({x},{y}) rectangle +({w},{h});'+'\n'
    if label:s+=text(x,y+h+7,w,label,10)
    return s
def workspace(y,h=50):return box(14,y,186,h,dashed=False)
def path(points,color='black',width=0.7):return line(points,f'draw={color},line width={width}mm,line join=round')
def circle(x,y,r=1.4,color='black',label=''):
    s=rf'\filldraw[fill=white,draw={color},line width=.45mm] ({x},{y}) circle ({r}mm);'+'\n'
    if label:s+=rf'\node[font=\small,anchor=south west,inner sep=1pt] at ({x+1},{y+1}) {{{label}}};'+'\n'
    return s
def pose(tx,ty,ox=0,oy=0,L=80,branch=1):
    dx,dy=tx-ox,ty-oy; d=sqrt(dx*dx+dy*dy)
    h=sqrt(L*L-d*d/4)
    ux=dx/2-branch*dy*h/d; uy=dy/2+branch*dx*h/d
    vx=dx-ux; vy=dy-uy
    return {'O':(ox,oy),'X':(ox+ux,oy+uy),'Q':(ox+2*ux,oy+2*uy),'Y':(ox+2*ux+vx,oy+2*uy+vy),'T':(tx,ty),'P':(ox+2*dx,oy+2*dy)}
def mechanism(tx=95,ty=0,scale=1,offset=(0,0),labels=True,ticks=False,bar_width=1.8,joint_radius=1.1):
    p=pose(tx,ty)
    p={k:(offset[0]+scale*x,offset[1]+scale*y) for k,(x,y) in p.items()}
    s=''
    for names in [('O','Q'),('Q','P'),('X','T'),('T','Y')]:s+=line([p[n] for n in names],f'line width={bar_width}mm,gray!45')
    for n,(x,y) in p.items():s+=circle(x,y,joint_radius,'blue!65!black' if n=='T' else 'red!70!black' if n=='P' else 'black',n if labels else '')
    if ticks:
        for a,b in [('O','X'),('X','Q'),('Q','Y'),('Y','P'),('X','T'),('T','Y')]:
            x1,y1=p[a];x2,y2=p[b]; dx=x2-x1;dy=y2-y1; d=sqrt(dx*dx+dy*dy);x=(x1+x2)/2;y=(y1+y2)/2
            s+=line([(x-1.7*dy/d,y+1.7*dx/d),(x+1.7*dy/d,y-1.7*dx/d)],'line width=.55mm')
    return s
def demo(x,y,reverse=False):
    # A non-task elbow, with 6.125 mm and 6.86 mm visible T legs at print size.
    # Each panel is a real simple-open pose, with the same local anchor O.
    s=''; stages=[[(75,-16)],[(75,-16),(100,-16)],[(75,-16),(100,-16),(100,12)]]
    for i,pts in enumerate(stages):
        ox=x+i*62; oy=y; sc=.245
        s+=text(ox,oy+42,59,['Start','Move P' if reverse else 'Move T','Copy'][i],10)
        s+=mechanism(*pts[-1],scale=sc,offset=(ox+3,oy),labels=False,bar_width=.85,joint_radius=.6)
        for a,c in [(1,'blue!70!black'),(2,'red!70!black')]:
            trace=[(ox+3+sc*a*u,oy+sc*a*v) for u,v in pts]
            if len(trace)>1:s+=path(trace,c,.4)
            sx,sy=trace[0]
            s+=rf'\fill[{c}] ({sx},{sy}) circle (.45mm);'+'\n'
            px,py=trace[-1]
            s+=circle(px,py,.65,c)
        for n,a,c in [('O',0,'black'),('T',1,'blue!70!black'),('P',2,'red!70!black')]:
            px=ox+3+sc*a*pts[-1][0];py=oy+sc*a*pts[-1][1]
            # Put the final labels beyond the upright strokes, not on their elbows.
            s+=text(px+2 if a and i else px-3,py-2 if a and i else py-3,10,n,9)
        if i==1:
            a=2 if reverse else 1; px=ox+3+sc*a*pts[-1][0];py=oy+sc*a*pts[-1][1]
            s+=line([(px-5,py-10),(px-1,py-2)],'-{Stealth[length=1.8mm]},thick')
    return s

def preamble(week,level,packet,materials=False):
    return r'''\pdfinfoomitdate=1
\pdftrailerid{}
\documentclass[letterpaper,12pt]{article}
\usepackage[margin=0mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,tikz}
\usetikzlibrary{arrows.meta}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\renewcommand{\familydefault}{\sfdefault}
\begin{document}
'''
def page(body,level='Grades 2--5',packet='W85-S-v1',n=1,mat=False):
    s=r'\thispagestyle{empty}\noindent\begin{tikzpicture}[remember picture,overlay,x=1mm,y=1mm,shift={(current page.south west)}]'+'\n'
    s+=text(14,268,190,'Week 85 / Drawing machines / '+level,11)
    s+=line([(14,261),(202,261)],'line width=.25mm')
    s+=text(14,12,182,'Bellingham Math Circle / Week 85 / '+packet,9)
    s+=text(199,12,12,str(n),9)
    s+=body+'\n'+r'\end{tikzpicture}\null\newpage'+'\n'
    return s
def document(pages):return preamble(85,'','')+''.join(pages)+r'\end{document}'+'\n'
def prob(n,s,y=251):return text(14,y,186,rf'\textbf{{Problem {n}:}} '+s,13)

# Coordinates are in the joined mat frame. Inputs fit x110..160,y115..165.
INPUTS={
'A':[(115,125),(150,125),(150,145)],
'B':[(120,120),(150,120),(140,150),(120,120)],
'C':[(115,135),(125,135),(125,150),(145,150),(145,125),(155,125)],
'G':[(120,125),(140,125),(140,145),(120,145),(120,125)],
'H':[(120,125),(150,125),(150,135),(130,135),(130,145),(120,145),(120,125)],
'I':[(120,125),(150,125),(120,155),(120,125)],
'M':[(130,125),(150,125),(140,150),(130,125)]}
OUTPUTS={
'E':[(200,110),(260,110),(260,150),(230,175),(200,150),(200,110)],
'J':[(200,110),(260,110),(260,150),(200,150),(200,110)],
'K':[(190,135),(240,135),(240,125),(270,145),(240,165),(240,155),(190,155),(190,135)]}
DOTS=[(190,110),(220,180),(270,160),(260,100),(210,140)]
def thumbnail(points,x,y,scale=1,output=False):
    origin=(180,90) if output else (100,105)
    return path([(x+(a-origin[0])*scale,y+(b-origin[1])*scale) for a,b in points], 'red!70!black' if output else 'blue!70!black')
def input_insert(letter,x,y):
    s=box(x,y,70,70)+text(x+5,y+65,12,letter,11)
    # Crosses on corners match the reusable mat's input placement marks.
    for a,b in [(0,0),(70,0),(0,70),(70,70)]:
        s+=line([(x+a-2,y+b),(x+a+2,y+b)],'gray')+line([(x+a,y+b-2),(x+a,y+b+2)],'gray')
    # The supplied square/half-square pieces carry the area unit.
    if letter=='L':s+=path([(x+25,y+25),(x+55,y+25),(x+55,y+45),(x+25,y+45),(x+25,y+25)],width=.5)
    else:s+=thumbnail(INPUTS[letter],x,y)
    return s
def output_insert(letter,x,y):
    s=box(x,y,110,100)+text(x+5,y+95,12,letter,11)
    for a,b in [(0,0),(110,0),(0,100),(110,100)]:
        s+=line([(x+a-2,y+b),(x+a+2,y+b)],'gray')+line([(x+a,y+b-2),(x+a,y+b+2)],'gray')
    if letter=='D':
        for j,(a,b) in enumerate(DOTS):s+=circle(x+a-180,y+b-90,1.6,'red!70!black',str(j+1))
    elif letter=='F':s+=path([(x+40,y+35),(x+80,y+35),(x+80,y+65),(x+40,y+65),(x+40,y+35)],width=.5)
    else:s+=thumbnail(OUTPUTS[letter],x,y,output=True)
    return s

def shared():
    p=[]
    b=text(14,250,186,'Keep O fixed. Move tracer T; pencil P draws the copy. Stop if the bars get stuck. Place the named insert on the matching mat corners, with a fresh clear overlay over the drawing zones.',12)
    b+=demo(14,173)
    b+=prob(1,'Use inserts A, B and C. Trace each path with T. What changes in the copies, and what stays the same?',y=151)
    for k,x in zip('ABC',[18,80,142]):
        b+=text(x,123,55,k,11);b+=thumbnail(INPUTS[k],x,68,.72)
    b+=workspace(28,39);p.append(page(b,n=1))
    b=prob(2,'On target D, make P visit every dot by moving only T. On target E, make P follow the outline. Leave T\'s paths on your overlays.')
    for letter,x in [('D',20),('E',116)]:
        b+=text(x,214,80,letter,11)
        if letter=='D':
            for j,(a,c) in enumerate(DOTS):b+=circle(x+.7*(a-180),132+.7*(c-90),1.3,'red!70!black',str(j+1))
        else:b+=thumbnail(OUTPUTS['E'],x,132,.7,True)
    b+=workspace(29,81);p.append(page(b,n=2))
    b=prob(3,'Can you position the machine so that O, T and P do not lie on one straight line? Find a rule for their distances that survives every position you try.')
    b+=mechanism(95,12,.5,(40,128))
    b+=workspace(28,78);p.append(page(b,n=3))
    b=prob(4,'Make different paths for T whose copies stay inside the small solid box on insert F. Find a rectangle T can trace whose copy follows that box\'s outline.')
    b+=text(84,169,10,'F',12)+box(53,104,110,100,'',True)
    b+=path([(93,139),(133,139),(133,169),(93,169),(93,139)],width=.5)
    b+=workspace(28,66);p.append(page(b,n=4))
    return document(p)

def upper():
    p=[]
    b=text(14,250,186,'Use the assembled machine and joined mat. Keep the four-sided frame open and uncrossed. Each new copy goes on a fresh clear overlay. An adult resets the anchor or swaps the tips when a problem calls for it.',12)
    b+=prob(1,'The six marked lengths are equal. Must P always be twice as far from O as T? Explain using the joined bars.',y=218)
    b+=mechanism(90,8,.72,(24,81),True,True)
    b+=workspace(28,38);p.append(page(b,'Grades 4--5','W85-U-v1',1))
    b=text(14,250,186,'One square piece is one square unit. Two matching triangle pieces make one square unit.',12)
    # A half-square dissection with explicit intermediate movement.
    for ox,label in [(26,'Two halves'),(88,'Join edges'),(151,'1 square unit')]:
        b+=text(ox-7,229,61,label,10)
    b+=path([(24,199),(34,199),(24,209),(24,199)])+path([(39,204),(49,204),(49,194),(39,204)])
    b+=path([(86,199),(96,199),(86,209),(86,199)])+path([(98,211),(98,201),(88,211),(98,211)])
    b+=line([(99,216),(96,211)],'-{Stealth[length=2mm]},thick')
    b+=box(151,199,10,10,'',False)+line([(151,209),(161,199)],'gray')
    b+=prob(2,'Use inserts G, H and I with the square and triangle pieces. How many square units cover each original and its copy? Find a rule for all three.',y=183)
    for k,x in zip('GHI',[21,83,145]):
        b+=text(x,149,55,k,11);b+=thumbnail(INPUTS[k],x,98,.7)
    b+=workspace(28,58);p.append(page(b,'Grades 4--5','W85-U-v1',2))
    b=text(14,250,186,'For this page, move P while T draws. Keep O fixed.',12)
    b+=demo(14,181,True)
    b+=prob(3,'Trace J and K with P. What copies does T make? Find a rectangle for P that makes T follow the small solid box on insert L.',y=159)
    for k,x in zip('JK',[20,86]):
        b+=text(x,128,60,k,11);b+=thumbnail(OUTPUTS[k],x,70,.55,True)
    b+=box(154,70,38.5,38.5,'',True)+path([(167.75,83.75),(184.25,83.75),(184.25,94.75),(167.75,94.75),(167.75,83.75)],width=.4)
    b+=text(156,106,10,'L',11)
    b+=workspace(24,20);p.append(page(b,'Grades 4--5','W85-U-v1',3))
    b=prob(4,r'Trace triangle M with anchor O, then with anchor O\(^{\prime}\), keeping M in the same place. What changes in the two copies? Find a new place for M that makes the second copy land exactly on the first.')
    b+=text(18,214,175,'Move T; P draws. The adult moves the anchor between copies.',11)
    # Locator is explicitly a placement diagram; physical mat carries full dimensions.
    b+=box(23,125,172,64,'',True)
    for x,label in [(39,'O'),(55,r'O\(^{\prime}\)')]:b+=circle(x,157,1.7,'black',label)
    b+=path([(111,145),(127,145),(119,165),(111,145)],'blue!70!black')
    b+=text(114,181,30,'M',11)
    b+=workspace(28,78);p.append(page(b,'Grades 4--5','W85-U-v1',4))
    return document(p)

def matdrawing():
    s=''
    for x,label in [(40,'O'),(60,r'O\(^{\prime}\)')]:
        s+=circle(x,140,2,'black',label)
        s+=line([(x-4,140),(x+4,140)],'thick')+line([(x,136),(x,144)],'thick')
    s+=box(100,105,70,70,'Input insert corners',True)
    s+=box(110,115,50,50,'',True)
    s+=box(180,90,110,100,'Output target corners',True)
    s+=text(110,102,60,'T zone',10)+text(181,84,100,'P zone / clear overlay',10)
    for x,y in [(100,105),(170,105),(100,175),(170,175),(180,90),(290,90),(180,190),(290,190)]:
        s+=line([(x-3,y),(x+3,y)],'thick')+line([(x,y-3),(x,y+3)],'thick')
    for x in (204,228):
        for y in (80,205):
            s+=circle(x,y,2,'gray')+line([(x-3,y),(x+3,y)],'gray')+line([(x,y-3),(x,y+3)],'gray')
    s+=line([(70,50),(170,50)],'thick')+line([(70,47),(70,53)],'thick')+line([(170,47),(170,53)],'thick')
    s+=text(94,45,70,'100 mm calibration',10)
    return s

def materials():
    p=[];lev='Materials / actual size';pid='W85-M-v1'
    b=text(14,251,186,r'\textbf{Adult fabrication template.} Print at 100\%, with no scaling. Rigid strips are 182 by 18 mm or 102 by 18 mm. Crosses mark hole centers. Hole diameter follows the chosen pivot or coaxial sleeve, not the printed circle. Prototype hardware and physical clearances are untested.',11)
    for y,names,length in [(171,['O','X','Q'],182),(127,['Q','Y','P'],182),(83,['X','T'],102),(39,['T','Y'],102)]:
        b+=box(16,y,length,18,'',False)
        for j,n in enumerate(names):
            x=27+80*j
            b+=circle(x,y+9,1.5,'black',n)
            b+=line([(x-3,y+9),(x+3,y+9)],'gray')+line([(x,y+6),(x,y+12)],'gray')
        b+=text(16,y-3,182,'80 mm between neighboring hole centers',9)
    p.append(page(b,lev,pid,1,True))
    b=text(14,251,186,r'\textbf{Adult assembly and print setup.} Join O--X--Q as one long bar and Q--Y--P as the other. Join short bars X--T and T--Y. Fix O. X, Q and Y rotate. The T hinge must share its axis with the tracer pencil; P must carry its pencil on the P axis. Use spacers so all bars rotate freely.',11)
    b+=mechanism(90,0,.6,(24,119),True,True)
    b+=text(14,109,186,r'Keep X--Q--Y--T in the simple, noncrossed shape shown. Adult assembly must guard against collapse, sharp hardware, slipping anchors and off-axis tips. The line drawing is topology, not a tested stack of spacers or a sleeve specification.',11)
    b+=text(14,77,186,r'Center the two-sheet mat on a board at least 450 by 400 mm. Match the paper edges and tape the backs. Cover the unprinted center seam with the bridge strip on page 5, aligning all four crosses. The joined sheets are 431.8 by 279.4 mm (nominally 432 by 279). Check the 100 mm line before use.',11)
    b+=text(14,39,186,r'Before children use it, rehearse the whole T zone, both tracing directions and the anchor change. Check support, hand clearance, branch stability and coaxial tips. None of these physical tests has been done for this draft.',11)
    p.append(page(b,lev,pid,2,True))
    for isright in [False,True]:
        shift=-215.9 if isright else 0
        s=rf'\begin{{scope}}\clip (8,24) rectangle (207.9,247);\begin{{scope}}[xshift={shift}mm]'+'\n'+matdrawing()+r'\end{scope}\end{scope}'+'\n'
        s+=text(14,250,185,('Right' if isright else 'Left')+' mat sheet. Butt the inside paper edge to the other sheet; attach the bridge strip over the seam.',11)
        s+=text(14,30,185,r'Print at 100\%. Keep the sheet edges until after joining.',10)
        p.append(page(s,lev,pid,len(p)+1,True))
    b=text(14,251,186,'Cut the bridge on its outside rectangle. Align its four crosses with the joined sheets. Its center covers the unprinted seam. Cut inserts A and B on their 70 mm borders; place their corners on the mat\'s input corners.',11)
    # The bridge frame spans x194..238 and y70..215 in the mat.
    b+=rf'\begin{{scope}}\clip (151,73) rectangle (195,218);\begin{{scope}}[xshift=-43mm,yshift=3mm]'+matdrawing()+r'\end{scope}\end{scope}'+'\n'
    b+=box(151,73,44,145,'',False)+text(154,216,38,'Bridge',10)
    b+=input_insert('A',18,139)+input_insert('B',18,47)
    p.append(page(b,lev,pid,5,True))
    b=text(14,251,186,'Cut the 110 by 100 mm targets. Place their corners on the output target corners of the joined mat, under a clear drawing overlay.',11)
    b+=output_insert('D',51,132)+output_insert('E',51,23)
    p.append(page(b,lev,pid,6,True))
    b=text(14,251,186,'F goes on the output corners. G and H go on the input corners. Use one insert at a time and preserve each copy on its own overlay.',11)
    b+=output_insert('F',50,126)+input_insert('G',22,32)+input_insert('H',121,32)
    p.append(page(b,lev,pid,7,True))
    b=text(14,251,186,'C, I, L and M go on the input corners. Keep M in its original place during the first anchor change. Move it only when the problem asks for a new place.',11)
    b+=input_insert('I',22,133)+input_insert('L',121,133)+input_insert('M',22,35)+input_insert('C',121,35)
    p.append(page(b,lev,pid,8,True))
    b=text(14,251,186,'Place J or K on the output corners. An adult swaps the tip roles: move P while T draws.',11)
    b+=output_insert('J',51,132)+output_insert('K',51,23)
    p.append(page(b,lev,pid,9,True))
    b=text(14,251,186,'Cut 48 squares and 16 half-square triangles. Each square has 10 mm sides. Keep the triangles as separate pieces. These units are for one original and its copy at a time.',12)
    for j in range(4):
        for i in range(12):b+=box(39+10*i,159+10*j,10,10,'',False)
    for i in range(8):b+=box(59+10*i,115,10,10,'',False)+line([(59+10*i,115),(69+10*i,125)],'thick')
    b+=text(14,92,186,'Also supply clear overlays large enough to cover both drawing zones, a 150 mm ruler, a straightedge, and removable tape. Pencil marks stay on overlays, so the mat and targets can be reused.',11)
    b+=text(14,57,186,'Material check per pair: one assembled machine; one board; one joined mat with bridge; inserts A--M; 48 squares; 16 triangles; ruler; straightedge; overlays. Physical fit and operation remain untested.',11)
    p.append(page(b,lev,pid,10,True))
    return document(p)

if __name__=='__main__':
    for name,fn in [('shared',shared),('upper',upper),('materials',materials)]:
        (ROOT/(name+'.tex')).write_text(fn())
