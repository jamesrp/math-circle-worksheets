"""Custom exploration pages for AD-09 through AD-16; exact tasks live in data."""
from math import sin,cos,pi,sqrt
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from sheet import FONT, BOLD, INK, GRAY, LIGHT, TEAL, PALE, WHITE, text_markup
from common import start,question,family_data

F=family_data('ad2')

def tag(b,s,x,y,size=10): b.label(s,x,y,size=size,color=GRAY)
def title(b,s,x,y): b.label(s,x,y,size=11,font=BOLD,color=TEAL)
def panel(b,y,h,label='',x=44,w=524):
    b.box(x,y,w,h,stroke=LIGHT,radius=4)
    if label: tag(b,label,x+9,y+7)

def openwork(b,y,h,label='Reasoning / examples / checks'):
    panel(b,y,h,label)

def splitwork(labels):
    def draw(b,y,h):
        w=(524-16*(len(labels)-1))/len(labels)
        for i,label in enumerate(labels):panel(b,y,h,label,44+i*(w+16),w)
    return draw

def ledger(headers,weights=None):
    def draw(b,y,h):
        ws=weights or [1]*len(headers);total=sum(ws);x=44
        panel(b,y,h)
        for i,(label,v) in enumerate(zip(headers,ws)):
            w=524*v/total
            tag(b,label,x+8,y+7)
            if i:b.line(x,y,x,y+h,color=LIGHT,width=.6)
            x+=w
        b.line(44,y+27,568,y+27,color=LIGHT,width=.7)
        # An open ledger, not one row per answer.
    return draw

def qheight(f,p):
    s=ParagraphStyle('measure-ad2',fontName=FONT,fontSize=11.5,leading=11.5*1.32)
    return Paragraph(text_markup(str(p['id'])+'. '+p['text']),s).wrap(524,1000)[1]+8

def pair(b,f,n,draw1=openwork,draw2=openwork,ratio=.5):
    start(b,f,n);qs=f['pages'][n-1]['prompts']
    question(b,f,qs[0]['id']);y=b.y
    available=737-y-qheight(f,qs[1])-17
    h1=available*ratio;h2=available-h1
    if min(h1,h2)<65:raise ValueError((f['id'],n,available))
    draw1(b,y,h1);b.y=y+h1+17
    question(b,f,qs[1]['id']);draw2(b,b.y,h2);b.y+=h2

def clock(b,cx,cy,r,n):
    b.circle(cx,cy,r,fill=None,stroke=LIGHT)
    for k in range(n):
        a=-pi/2+2*pi*k/n;x=cx+r*cos(a);y=cy+r*sin(a)
        b.circle(x,y,10,fill=WHITE,stroke=INK,width=.7)
        b.label(str(k),x,y-6.5,size=10,align='center')
    b.circle(cx,cy,2,fill=GRAY,stroke=GRAY)

def clocks(b,y,h):
    r=min(41,(h-34)/2)
    clock(b,104,y+h/2,r,4);clock(b,222,y+h/2,r,6)
    tag(b,'4 positions',104,y+h-14,9);tag(b,'6 positions',216,y+h-14,9)
    panel(b,y,h,'Reports / times / evidence',292,276)

def reportmatrix(b,y,h):
    c=min(25,(h-35)/4);x=77;top=y+24
    b.grid(x,top,6*c,4*c,6,4)
    for j in range(6):b.label(str(j),x+(j+.5)*c,top-18,size=10,align='center')
    for i in range(4):b.label(str(i),x-13,top+(i+.5)*c-6,size=10,align='center')
    tag(b,'a',47,top+4*c/2-6);tag(b,'b',x+3*c,top-34)
    panel(b,y,h,'Classification and non-repetition argument',270,298)

def counterwork(b,y,h):
    splitwork(['Triangle: rearrange or draw counters','Square: rearrange or draw counters'])(b,y,h)

def producttables(b,y,h):
    for k,(label,bits) in enumerate(zip(F['AD-11']['figures']['labels'],F['AD-11']['figures']['coefficient_pairs'])):
        x=44+134*k
        b.box(x,y,110,33,stroke=LIGHT,radius=4)
        b.label(label,x+15,y+9,size=12)
        b.grid(x+45,y+5,48,23,2,1)
        for j,bit in enumerate(bits):b.label(str(bit),x+57+24*j,y+9,size=10,align='center')
    y+=46;h-=46
    c=min(29,(h-24)/5)
    for x,name in [(63,'A: t²=t'),(333,'B: t²=t+1')]:
        title(b,name,x,y)
        b.grid(x,y+22,5*c,5*c,5,5)
        for k,v in enumerate(['×','0','1','t','u']):
            b.label(v,x+(k+.5)*c,y+26,size=10,align='center')
            if k:b.label(v,x+.5*c,y+22+(k+.5)*c-6,size=10,align='center')

def collisions(b,y,h):
    for x,label in [(44,'Rule A'),(314,'Rule B')]:
        panel(b,y,h,label,x,254)
        tag(b,'input',x+14,y+31);tag(b,'× t',x+107,y+31);tag(b,'output',x+183,y+31)
        b.arrow(x+79,y+65,x+172,y+65,color=LIGHT)

def machines(b,y,h):
    ledger(['Chosen input / output reports','Recover a and b; justify uniqueness'],[1,1.3])(b,y,h)

def unitconstruction(b,y,h):
    panel(b,y,h,'Exact construction and its certificate')
    yy=y+h-26;b.line(65,yy,137,yy,width=1.3)
    b.line(65,yy-4,65,yy+4);b.line(137,yy-4,137,yy+4)
    tag(b,'unit = 1',79,yy+6)

def semicircle(b,y,h):
    # Geometric mean construction: actual segment lengths 1 and sqrt(2).
    left=72;right=286;r=(right-left)/2;cx=(left+right)/2
    scale=(right-left)/(1+sqrt(2));foot=left+scale
    base=y+h-30;ht=sqrt((foot-left)*(right-foot))
    b.poly([(cx+r*cos(pi-k*pi/80),base-r*sin(pi-k*pi/80)) for k in range(81)],width=.9)
    b.line(left,base,right,base);b.line(foot,base,foot,base-ht,color=GRAY)
    b.poly([(foot+7,base),(foot+7,base-7),(foot,base-7)],stroke=GRAY,width=.7)
    tag(b,'1',left+scale/2,base+8);tag(b,'√2',foot+(right-foot)/2,base+8)
    tag(b,'h',foot+5,base-ht*.55)
    panel(b,y,h,'Use this diagram, or give your own construction',312,256)

def stairs(b,x,y,size,corners,filled=None):
    cell=size/6
    for i in range(7):
        for j in range(7):
            if filled is not None and (i,j) in filled:b.circle(x+i*cell,y+size-j*cell,cell*.23,fill=TEAL,stroke=TEAL)
            else:b.circle(x+i*cell,y+size-j*cell,1,fill=LIGHT,stroke=LIGHT)
    b.arrow(x-5,y+size,x+size+13,y+size,color=GRAY,head=4)
    b.arrow(x,y+size+5,x,y-13,color=GRAY,head=4)
    tag(b,'i',x+size+14,y+size-7);tag(b,'j',x-5,y-28)
    for k in range(7):
        b.label(str(k),x+k*cell,y+size+5,size=8,align='center',color=GRAY)
        if k:b.label(str(k),x-13,y+size-k*cell-5,size=8,color=GRAY)
    for a,c in corners:
        xx=x+a*cell;yy=y+size-c*cell
        b.poly([(xx-4,yy-4),(xx+4,yy+4)],stroke=INK,width=1.3)
        b.poly([(xx-4,yy+4),(xx+4,yy-4)],stroke=INK,width=1.3)

def stairwork(b,y,h):
    size=min(158,h-40);stairs(b,72,y+24,size,F['AD-13']['figures']['corners'])
    panel(b,y,h,'Boundary argument / witnesses',284,284)

def changegrid(b,y,h):
    size=min(150,h-42);stairs(b,72,y+24,size,[])
    panel(b,y,h,'Chosen changes and their effects',283,285)

def program(b,y,h,filled=False):
    # Every operation has a coefficient pair, including the square before +1.
    hh=43;yt=y+21;yb=y+h-46;mid=y+(h-hh)/2
    nodes=[('z',44,mid),('z²',205,yt),('z²+1',344,yt),('z−2',274,yb),('f(z)',458,mid)]
    for label,x,yy in nodes:
        tag(b,label,x,yy-16)
        b.box(x,yy,110,hh,stroke=LIGHT)
        b.line(x+55,yy,x+55,yy+hh,color=LIGHT,width=.6)
        tag(b,'ordinary',x+7,yy+4,9);tag(b,'ε',x+62,yy+4,9)
    b.arrow(154,mid+hh/2,198,yt+hh/2,color=GRAY,head=4)
    b.arrow(154,mid+hh/2,267,yb+hh/2,color=GRAY,head=4)
    b.arrow(315,yt+hh/2,337,yt+hh/2,color=GRAY,head=4)
    b.arrow(454,yt+hh/2,513,mid-5,color=GRAY,head=4)
    b.arrow(384,yb+hh/2,451,mid+hh/2,color=GRAY,head=4)

def ellipse(b,x,y,w,h,worked=False):
    # Identical scale on x and y: semiaxes 1 and 1/sqrt(2).
    scale=min((w-55)/2,(h-38)*sqrt(2)/2);cx=x+w/2;cy=y+h/2
    b.arrow(cx-scale-16,cy,cx+scale+17,cy,color=GRAY,head=4)
    b.arrow(cx,cy+scale/sqrt(2)+8,cx,cy-scale/sqrt(2)-12,color=GRAY,head=4)
    b.poly([(cx+scale*cos(2*pi*k/100),cy-scale*sin(2*pi*k/100)/sqrt(2)) for k in range(101)],width=1)
    b.circle(cx-scale,cy,3,fill=INK);tag(b,'B',cx-scale-14,cy-17,10)
    tag(b,'1',cx+scale-2,cy+6,9);tag(b,'x',cx+scale+19,cy-7,10);tag(b,'y',cx+6,cy-scale/sqrt(2)-19,10)
    b.label('1/√2',cx+6,cy-scale/sqrt(2),size=8,color=GRAY)

def ellipsework(b,y,h):
    ellipse(b,44,y,257,h);panel(b,y,h,'Exact substitution / point / recovered slope',316,252)

def residuegrid(b,x,y,size):
    c=size/4
    b.grid(x,y,size,size,4,4)
    for k in range(5):
        b.label(str(k),x+k*c,y+size+6,size=9,align='center',color=GRAY)
        b.label(str(k),x-12,y+size-k*c-6,size=9,align='right',color=GRAY)
    tag(b,'x',x+size+10,y+size-5);tag(b,'y',x-3,y-20)

def finitework(b,y,h):
    size=min(145,h-42);residuegrid(b,72,y+21,size)
    panel(b,y,h,'Column calculations / completeness certificate',276,292)

def projectivework(b,y,h):
    panel(b,y,h,'Z ≠ 0: normalize coordinates',44,310)
    panel(b,y,h,'Z = 0: solve, then identify scalings',370,198)

def equations(b,y,h):
    gap=16;hh=(h-gap)/2
    for x,yy,label in [(44,y,'2Q=P'),(314,y,'3Q=P'),(44,y+hh+gap,'3Q=O'),(314,y+hh+gap,'3Q=(2,1)')]:
        panel(b,yy,hh,label,x,254)
        tag(b,'labels → points; why the list is complete',x+9,yy+27,9)

LAYOUTS={
 'AD-09':[(clocks,ledger(['Changed report','First time','Why it works'])),(reportmatrix,ledger(['Eight / twelve: classification','Tests / return period'])),(splitwork(['Necessity','Construction and uniqueness']),ledger(['Given reports','Your compatible reports']))],
 'AD-10':[(counterwork,splitwork(['Match → equation','Equation → match'])),(ledger(['x, y','m, n','Matching total','Check']),splitwork(['Reverse machine','Examples and missing proof'])),(splitwork(['Inequalities and positivity','Descent, base case and completeness']),ledger(['First total above the threshold','Next match / exact certificate']))],
 'AD-11':[(producttables,collisions),(splitwork(['Rule A: modulus and roots','Rule B: modulus and roots']),openwork),(machines,splitwork(['Decode with B','Test the same reports with A']))],
 'AD-12':[(unitconstruction,ledger(['Exact cubes','Bounds and what they certify'])),(splitwork(['Line-line / line-circle','Two circles / degenerate cases']),openwork),(ledger(['Classification / both directions','Check the supplied requests']),semicircle)],
 'AD-13':[(stairwork,openwork),(changegrid,stairwork),(splitwork(['Spanning and independence','Reduction and cutoff counterexample']),openwork)],
 'AD-14':[(ledger(['Chosen factors','Ordinary coefficient','ε coefficient']),splitwork(['Unit classification','Cancellation and a counterexample'])),(program,splitwork(['Two polynomials / common dual output','An ordinary input that distinguishes them'])),(openwork,splitwork(['Product rule','Chain rule / second order']))],
 'AD-15':[(ellipsework,ledger(['Your challenge','Decode the supplied point'])),(openwork,ellipsework),(ledger(['p, q and a triple','Completeness / exceptional point']),openwork)],
 'AD-16':[(finitework,finitework),(projectivework,openwork),(ledger(['Chosen point','Repeated sums / checks'],[1,3]),openwork)]}

def render_students(b,family_id):
    f=F[family_id]
    for n,(a,c) in enumerate(LAYOUTS[family_id],1):
        ratio=.52 if (family_id,n) in [('AD-11',1),('AD-15',1)] else .5
        if (family_id,n)==('AD-12',3):ratio=.43
        pair(b,f,n,a,c,ratio)
    if family_id=='AD-16':
        start(b,f,4);question(b,f,'7');equations(b,b.y,737-b.y)

def render_key_figures(b,family_id):
    if family_id!='AD-13':return
    if b.y>300:b.new_page(family_id,'Worked boundary certificates','Facilitator / the marks below are solution data')
    else:
        b.h('Worked boundary certificates');b.y+=12
    b.p('A filled dot is a survivor. A cross is a forbidden corner. The axes continue beyond these windows.',size=11)
    y=b.y+40
    corners=F[family_id]['figures']['corners'];moved=[(3,0),(3,1),(1,3),(0,4)]
    def survivors(cs):return {(i,j) for i in range(7) for j in range(7) if not any(i>=a and j>=c for a,c in cs)}
    title(b,'Original',67,y-18);title(b,'Move (2,1) right',337,y-18)
    stairs(b,75,y+20,176,corners,survivors(corners));stairs(b,341,y+20,176,moved,survivors(moved))
    b.y=y+232
    b.p('The move frees (2,1) and (2,2). At i≥3 the corner (3,0) still forbids everything, and at j≥4 the corner (0,4) still forbids everything. Thus the new region is finite.',size=11);b.y+=13
    b.p('In the original grid, right and up both kill exactly (0,3), (1,2) and (2,0). Their monomials are y³, xy² and x². Among monomials whose shifted images survive, those images are distinct. Thus cancellation cannot add other joint-kernel elements.',size=11);b.y+=14
