"""Week 64 figures and canvas page template, carried over unchanged from the old student
builder (student/generate.py, archived in archive-before-problem-files-2026-10-23/).

Coordinates are printed inches from the top-left corner of the drawing area, y down. Each
page is one TikZ picture. Its first figure, page_start(level), opens the picture and draws
the page's header (its grade range differs by page), footer and page number, exactly as
the old page(n, level) did; page_close ends the picture. The drawing helpers below write
lines into OUT as the old builder did, and fig(...) returns what a figure wrote. Problem
files call them by name in their `figure` sections; the rule, prompt and caption wording
lives in the problem files.
"""
import math

OUT = []
STATE = {'page': 0, 'footer': ''}
a = 1+math.sqrt(2)
V = [(1,a),(a,1),(a,-1),(1,-a),(-1,-a),(-a,-1),(-a,1),(-1,a)]


def fig(*drawings):
    """The LaTeX written by a figure. Its arguments are drawing calls, made in order; each
    writes lines into OUT, and fig returns them, every line ending with a newline."""
    out = ''.join(line + '\n' for line in OUT)
    OUT.clear()
    return out


# ---------------------------------------------------------------- drawing primitives (generate.py)

def emit(s): OUT.append(s)
def p(x,y): return f'({x:.5f},{y:.5f})'
def line(x1,y1,x2,y2,style=''):
    emit(r'\draw['+style+'] '+p(x1,y1)+' -- '+p(x2,y2)+';')
def text(x,y,w,s,size=13.3):
    emit(r'\node[anchor=north west,inner sep=0pt,align=left,text width='+str(w)+r'in,font=\fontsize{'+str(size)+'}{'+str(round(size*1.25,2))+r'}\selectfont] at '+p(x,y)+' {'+s+'};')
def label(x,y,s,size=11,anchor='center'):
    emit(r'\node[anchor='+anchor+r',inner sep=1pt,font=\fontsize{'+str(size)+'}{'+str(size+1)+r'}\selectfont] at '+p(x,y)+' {'+s+'};')
def dot(x,y,s='',hollow=False,dx=-.09,dy=-.12):
    emit(r'\draw[fill='+('white' if hollow else 'black')+'] '+p(x,y)+r' circle[radius=.032in];')
    if s: label(x+dx,y+dy,s,11)
def lines(y,count=3,gap=.36):
    for i in range(count): line(.05,y+i*gap,7.25,y+i*gap,'black!25,line width=.35pt')
def scale_bar(x,y):
    line(x,y,x+1,y,'line width=.8pt')
    for xx in [x,x+1]:line(xx,y-.055,xx,y+.055,'line width=.8pt')
    label(x+.5,y-.16,'1 inch',10)


# ---------------------------------------------------------------- page template (generate.py's page and problem)

PREAMBLE = r'''\documentclass[letterpaper,11pt]{article}
\usepackage[margin=.55in]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\hyphenpenalty=10000\exhyphenpenalty=10000
\renewcommand{\familydefault}{\sfdefault}
\tikzset{edge/.style={line width=.65pt,-{Stealth[length=2.1mm,width=1.5mm,open]}},travel/.style={line width=1.35pt,-{Stealth[length=3mm,width=2.1mm]}}}
\begin{document}'''


def page_preamble(week, topic, header, footer):
    STATE.update(page=0, footer=footer)
    OUT.clear()
    return PREAMBLE + '\n'


def page_start(level='Grades 3--5'):
    """Open a page: the picture, its header with this page's grade range, footer and number."""
    STATE['page'] += 1
    emit(r'\noindent\begin{tikzpicture}[x=1in,y=-1in]')
    emit(r'\path[use as bounding box] (0,0) rectangle (7.4,9.68);')
    text(0,0,7.4,'Week 64 / Straight paths on strange surfaces / '+level,10.6)
    text(0,9.48,6.8,'Bellingham Math Circle / Week 64 / '+STATE['footer'],9.5)
    label(7.38,9.54,str(STATE['page']),9.5,'east')
    return fig()


PAGE_OPEN = ''


def page_close(page):
    return r'\end{tikzpicture}'


def page_prompt(n, body, x, y, size):
    return page_text(0, y, r'\textbf{Problem '+str(n)+':} '+body, 7.35, size)


def page_text(x, y, body, w, size):
    text(x, y, w, body, size or 13.3)
    return fig()


# ---------------------------------------------------------------- octagon, square, sectors and L (generate.py)

def octagon(cx,cy,width,numbers=False,labelsize=11,ticks=False):
    s=width/(2*a)
    T=lambda v:(cx+s*v[0],cy-s*v[1])
    vs=[T(v) for v in V]
    emit(r'\draw[line width=.85pt] '+' -- '.join(p(*v) for v in vs)+' -- cycle;')
    # The global orientations of the two arrows in each pair agree.
    # Top/bottom A right; NE/SW B down-right; right/left C up; SE/NW D up-right.
    edges=[(7,0,'A'),(0,1,'B'),(2,1,'C'),(3,2,'D'),(4,3,'A'),(5,4,'B'),(5,6,'C'),(6,7,'D')]
    # With ticks (October 23, 2026): seven numbered ticks at eighths of each edge, counted
    # from the arrow's tail, so matching points of paired edges carry the same numbers; the
    # arrow is shortened to clear ticks 3 and 5, and the letter moves out past the numbers.
    lo,hi,out=(.40,.60,.31) if ticks else (.37,.63,.13)
    for i,j,c in edges:
        x1,y1=vs[i];x2,y2=vs[j]
        q1=(x1+lo*(x2-x1),y1+lo*(y2-y1));q2=(x1+hi*(x2-x1),y1+hi*(y2-y1))
        line(*q1,*q2,'edge')
        mx=(x1+x2)/2;my=(y1+y2)/2;d=math.hypot(mx-cx,my-cy)
        if ticks:
            nx,ny=(mx-cx)/d,(my-cy)/d
            for k in range(1,8):
                tx,ty=x1+k/8*(x2-x1),y1+k/8*(y2-y1)
                line(tx,ty,tx+.06*nx,ty+.06*ny,'line width=.5pt')
                label(tx+.15*nx,ty+.15*ny,str(k),7)
        label(mx+out*(mx-cx)/d,my+out*(my-cy)/d,c,labelsize)
    if numbers:
        for i,(x,y) in enumerate(vs):
            d=math.hypot(x-cx,y-cy)
            label(x+.19*(x-cx)/d,y+.19*(y-cy)/d,str(i+1),12)
    return T

def square(cx,cy,side,numbers=False):
    q=side/2; vs=[(cx+q,cy-q),(cx+q,cy+q),(cx-q,cy+q),(cx-q,cy-q)]
    emit(r'\draw[line width=.85pt] '+' -- '.join(p(*v) for v in vs)+' -- cycle;')
    for i,j,c in [(3,0,'E'),(1,0,'F'),(2,1,'E'),(2,3,'F')]:
        x1,y1=vs[i];x2,y2=vs[j]
        line(x1+.38*(x2-x1),y1+.38*(y2-y1),x1+.62*(x2-x1),y1+.62*(y2-y1),'edge')
        mx=(x1+x2)/2;my=(y1+y2)/2;d=math.hypot(mx-cx,my-cy)
        label(mx+.13*(mx-cx)/d,my+.13*(my-cy)/d,c,11)
    if numbers:
        for i,(x,y) in enumerate(vs):
            dx=.15 if x>cx else -.15;dy=.15 if y>cy else -.15
            label(x+dx,y+dy,str(i+9),12)

def path_arrow(T,start,delta,length=None):
    x,y=T(start);dx,dy=delta
    if length is None:
        tx,ty=T((start[0]+dx,start[1]+dy))
    else:
        norm=math.hypot(dx,dy);tx=x+length*dx/norm;ty=y-length*dy/norm
    line(x,y,tx,ty,'travel')

def sector(cx,cy,angle,radius,num,left,right,left_head,right_head):
    # All corners have their two boundary rays oriented identically on the page.
    # Each tuple gives the edge letter and arrow direction at this vertex.
    half=math.radians(angle/2)
    dx=radius*math.sin(half);dy=radius*math.cos(half)
    pts=[(cx,cy),(cx-dx,cy+dy)]
    for k in range(1,49):
        th=-half+k*2*half/48
        pts.append((cx+radius*math.sin(th),cy+radius*math.cos(th)))
    emit(r'\draw[line width=.7pt] '+' -- '.join(p(*v) for v in pts)+' -- cycle;')
    for sign,letter,toward in [(-1,left,left_head),(1,right,right_head)]:
        vx=sign*dx;vy=dy
        lo=(cx+.35*vx,cy+.35*vy);hi=(cx+.73*vx,cy+.73*vy)
        line(*(hi if toward else lo),*(lo if toward else hi),'edge')
        # Labels sit inside the piece, away from the cut line.
        label(cx+.74*vx-sign*.075,cy+.74*vy+.12,letter,11)
    label(cx,cy+radius*.58,str(num),14)

def lshape(cx,top,side,starts=None,direction=None,labels=True):
    # Absolute L coordinates: A=(0,0), B=(1,0), C=(0,1).
    left=cx-side
    T=lambda v:(left+side*v[0],top+side*(2-v[1]))
    for ox,oy,c in [(0,0,'A'),(1,0,'B'),(0,1,'C')]:
        for k in range(1,8):
            st='black!20,line width=.25pt' if k%2 else 'black!32,line width=.35pt'
            line(*T((ox+k/8,oy)),*T((ox+k/8,oy+1)),st)
            line(*T((ox,oy+k/8)),*T((ox+1,oy+k/8)),st)
        # Square label lives in the top-left little cell.
        xx,yy=T((ox+.055,oy+.965)); label(xx,yy,c,11,'north west')
    boundary=[(0,0),(2,0),(2,1),(1,1),(1,2),(0,2)]
    emit(r'\draw[line width=.95pt] '+' -- '.join(p(*T(v)) for v in boundary)+' -- cycle;')
    line(*T((1,0)),*T((1,1)),'line width=.8pt')
    line(*T((0,1)),*T((1,1)),'line width=.8pt')
    # Matching boundary points are translations; internal sides are ordinary seams.
    edges=[((0,0),(1,0),'p',(0,-.14)),((0,2),(1,2),'p',(0,.14)),
           ((1,0),(2,0),'q',(0,-.14)),((1,1),(2,1),'q',(0,.14)),
           ((0,0),(0,1),'r',(-.14,0)),((2,0),(2,1),'r',(.14,0)),
           ((0,1),(0,2),'s',(-.14,0)),((1,1),(1,2),'s',(.14,0))]
    for v,w,c,offset in edges:
        b=T(v);e=T(w)
        line(b[0]+.39*(e[0]-b[0]),b[1]+.39*(e[1]-b[1]),b[0]+.61*(e[0]-b[0]),b[1]+.61*(e[1]-b[1]),'edge')
        m=((v[0]+w[0])/2,(v[1]+w[1])/2)
        xx,yy=T(m);label(xx+offset[0],yy-offset[1],c,12)
    if starts:
        for sq,xy,name in starts:
            ox,oy={'A':(0,0),'B':(1,0),'C':(0,1)}[sq]
            v=(ox+xy[0],oy+xy[1]); x,y=T(v);dot(x,y,name,dx=-.10,dy=.11)
            if direction:
                directions=direction if isinstance(direction,list) else [direction]
                for d in directions:path_arrow(T,v,(d[0]/8,d[1]/8))
    return T


# ---------------------------------------------------------------- the pages' figures (generate.py, page by page)

def crossing_example():
    """Page 1: a non-task convention example, kept separate from every target path."""
    T1=octagon(1.72,2.60,1.63,labelsize=9)
    T2=octagon(5.45,2.60,1.63,labelsize=9)
    S=(.70,-.50); hit=(a,-.50+.45*(a-.70)); resumed=(-a,hit[1]);end=(-.62,hit[1]+.45*(a-.62))
    dot(*T1(S),'S',dx=-.10,dy=.13)
    line(*T1(S),*T1(hit),'travel')
    dot(*T1(hit),'X',hollow=True,dx=.14,dy=-.07)
    dot(*T2(resumed),'X',hollow=True,dx=-.14,dy=-.07)
    line(*T2(resumed),*T2(end),'travel')
    label(3.7,2.60,'same point',11)


def three_trips():
    """Page 1: the working octagon with the marked starts P, Q and R."""
    T=octagon(3.7,6.98,3.94,ticks=True)
    for xy,name in [((-.65,0),'P'),((-.3,1.60),'Q'),((.20,-1.45),'R')]:
        dot(*T(xy),name,dx=-.10,dy=-.13);path_arrow(T,xy,(1,0),length=.43)


def development_example():
    """Page 3: a non-task example of developing a single crossing into a translated copy."""
    T1=octagon(2.95,2.43,1.40,labelsize=8)
    T2=octagon(4.35,2.43,1.40,labelsize=8)
    S=(.15,-.65); hit=(a,-.65+.20*(a-.15)); res=(-a,hit[1]);end=(-.50,hit[1]+.20*(a-.50))
    dot(*T1(S),'S',dx=-.08,dy=.12)
    line(*T1(S),*T1(hit),'line width=1.35pt')
    line(*T2(res),*T2(end),'travel')
    label(2.95,1.94,'1',10)
    label(4.35,1.94,'2',10)


def corner_pieces():
    """Page 5: the eight octagon corners and four square corners, with a one-inch bar.
    The edge letters and arrow directions are inherited from page 3, with no angle answers printed."""
    pieces=[('A','B',True,False),('B','C',True,True),('C','D',False,True),('D','A',False,True),('A','B',False,True),('B','C',False,False),('C','D',True,False),('D','A',True,False)]
    for k,info in enumerate(pieces):
        sector(1.78+(k%2)*3.80,1.95+(k//2)*1.43,135,1.10,k+1,*info)
    for k,info in enumerate([('E','F',True,True),('F','E',False,True),('E','F',False,False),('F','E',True,False)]):
        sector(.94+k*1.81,7.90,90,.75,k+9,*info)
    scale_bar(.28,9.03)


def direction_arrows():
    """Page 9: the four trial directions, each on a small grid with its label."""
    for i,(dx,dy) in enumerate([(1,2),(2,3),(3,1),(3,2)]):
        cx=.88+i*1.87; by=2.12; unit=.16
        for k in range(4):
            line(cx-.30+k*unit,by-.50,cx-.30+k*unit,by,'black!18,line width=.25pt')
            line(cx-.30,by-k*unit,cx+.18,by-k*unit,'black!18,line width=.25pt')
        dot(cx-.30,by)
        line(cx-.30,by,cx-.30+unit*dx,by-unit*dy,'travel')
        label(cx-.04,2.33,f'{dx} right, {dy} up',11)
