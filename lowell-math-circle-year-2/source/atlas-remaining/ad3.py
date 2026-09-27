"""AD17–24: custom investigation boards; exact text and keys live in data."""
from math import sin, cos, pi
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from sheet import FONT, BOLD, INK, GRAY, LIGHT, TEAL, PALE, WHITE, text_markup
from common import start, question, family_data

F=family_data('ad3')

def tag(b,s,x,y,size=10):b.label(s,x,y,size=size,color=GRAY)
def title(b,s,x,y):b.label(s,x,y,size=11,font=BOLD,color=TEAL)
def panel(b,y,h,label='',x=44,w=524):
    b.box(x,y,w,h,stroke=LIGHT,radius=4)
    if label:tag(b,label,x+9,y+7)
def work(b,y,h):panel(b,y,h,'Examples / argument / exact checks')
def split(labels):
    def draw(b,y,h):
        w=(524-16*(len(labels)-1))/len(labels)
        for i,label in enumerate(labels):panel(b,y,h,label,44+i*(w+16),w)
    return draw
def ledger(headers,weights=None):
    def draw(b,y,h):
        weights0=weights or [1]*len(headers);x=44;total=sum(weights0)
        panel(b,y,h)
        for label,weight in zip(headers,weights0):
            if x>44:b.line(x,y,x,y+h,color=LIGHT,width=.6)
            tag(b,label,x+8,y+7);x+=524*weight/total
        b.line(44,y+27,568,y+27,color=LIGHT,width=.7)
    return draw
def qheight(q):
    style=ParagraphStyle('ad3-measure',fontName=FONT,fontSize=11.5,leading=15.18)
    return Paragraph(text_markup(q['id']+'. '+q['text']),style).wrap(524,1000)[1]+8
def pair(b,f,n,draw1=work,draw2=work,ratio=.5):
    start(b,f,n);qs=f['pages'][n-1]['prompts'];question(b,f,qs[0]['id']);y=b.y
    available=737-y-qheight(qs[1])-17
    h1=available*ratio;h2=available-h1
    if min(h1,h2)<65:raise ValueError((f['id'],n,available))
    draw1(b,y,h1);b.y=y+h1+17
    question(b,f,qs[1]['id']);draw2(b,b.y,h2);b.y+=h2

def numberline(b,y,h):
    left,right=62,550;cy=y+35
    b.arrow(left,cy,right,cy,color=GRAY,head=5)
    for k in range(-4,11):
        x=left+12+(k+4)*(right-left-30)/14
        b.line(x,cy-4,x,cy+4,color=GRAY,width=.7)
        b.label(str(k),x,cy+7,size=9,align='center',color=GRAY)
        if k in (-3,9):
            b.circle(x,cy,4,fill=WHITE,stroke=TEAL,width=1.2)
            b.label('x₀' if k==-3 else 'y₀',x,cy-25,size=10,align='center',color=TEAL)
    ledger(['Rule / round','x','y','What seems unchanged?'],[1.1,1,1,2])(b,y+72,h-72)

def coordinate_grid(b,x,y,w,h,k=None,worked=False):
    # Exact equal scale; the displayed input square is dotted, image arrows solid.
    scale=min((w-36)/9,(h-37)/5);ox=x+22+scale;oy=y+15+4*scale
    def pt(a,c):return ox+a*scale,oy-c*scale
    b.grid(ox-scale,oy-4*scale,9*scale,5*scale,9,5)
    b.arrow(*pt(-1,0),*pt(8.3,0),color=GRAY,head=4)
    b.arrow(*pt(0,-1),*pt(0,4.2),color=GRAY,head=4)
    for a in [0,2,4,6,8]:b.label(str(a),pt(a,0)[0],oy+4,size=8,align='center',color=GRAY)
    for c in [2,4]:b.label(str(c),ox-6,pt(0,c)[1]-5,size=8,align='right',color=GRAY)
    for u,v in [((0,0),(1,0)),((1,0),(1,1)),((1,1),(0,1)),((0,1),(0,0))]:b.line(*pt(*u),*pt(*v),color=GRAY,width=1,dash=[2,2])
    if k is not None:
        b.arrow(*pt(0,0),*pt(2,1),color=TEAL,head=5)
        b.arrow(*pt(0,0),*pt(k,2),color=INK,head=5)
        tag(b,'u',pt(2,1)[0]+3,pt(2,1)[1],9);tag(b,'v',pt(k,2)[0]+3,pt(k,2)[1]-13,9)
        if worked:b.poly([pt(0,0),pt(2,1),pt(k+2,3),pt(k,2)],closed=True,stroke=TEAL,width=1.3)
def image_trials(b,y,h):
    for x,k in [(44,1),(314,5)]:
        title(b,'k = '+str(k),x+4,y)
        coordinate_grid(b,x,y+18,254,h-21,k)
def collapse_grid(b,y,h):
    coordinate_grid(b,44,y,266,h)
    panel(b,y,h,'Collision / all preimages',328,240)

def basisledger(b,y,h):ledger(['Chosen source vector','Its image under T','Target-basis coordinates'],[1.05,1,1.25])(b,y,h)
def blocks(b,y,h):
    for x,left,right in [(53,'k','0'),(229,'k','k'),(405,'0','k')]:
        b.label(left,x+15,y+8,size=14);b.arrow(x+46,y+18,x+105,y+18,color=GRAY,head=5)
        b.label(right,x+119,y+8,size=14)
    panel(b,y+43,h-43,'Construction / independence / spanning')
def orders(b,y,h):
    panel(b,y,h,'Products / chosen matrices / vector test',269,299)
    for i,(order,m1,m2) in enumerate([('NB','B','N'),('BN','N','B')]):
        yy=y+27+82*i;tag(b,order,48,yy-20,10)
        for x,label in [(48,'v'),(116,m1),(184,m2)]:
            b.box(x,yy,47,32,stroke=LIGHT)
            b.label(label,x+23.5,yy+8,size=11,align='center')
        b.arrow(96,yy+16,111,yy+16,color=GRAY,head=4)
        b.arrow(164,yy+16,179,yy+16,color=GRAY,head=4)
        b.arrow(232,yy+16,257,yy+16,color=GRAY,head=4)
def jacobi(b,y,h):
    labels=['[[A,B],D]','[[B,D],A]','[[D,A],B]']
    split(labels)(b,y,h)

def inventories(b,y,h):
    rows=[('People',F['AD-21']['figures']['people']),('Badges',F['AD-21']['figures']['badges'])]
    for j,(name,items) in enumerate(rows):
        yy=y+j*41;tag(b,name,46,yy+10,9)
        step=78 if j==0 else 66
        for i,(label,color) in enumerate(items):
            x=114+i*step;b.box(x,yy,step-6,34,stroke=LIGHT,fill=PALE)
            b.label(label,x+(step-6)/2,yy+3,size=10,align='center')
            b.label(color,x+(step-6)/2,yy+18,size=8,align='center',color=GRAY)
    panel(b,y+88,h-88,'Your catalog: choose a layout; keep both names')
def tokens(b,y,h):ledger(['Token name','Person record','Badge record','Catalog destination'],[.9,1,1,1.3])(b,y,h)
def square_diagram(b,x,y,size,selected=(),face_fill=False):
    pts={'A':(x,y),'B':(x+size,y),'C':(x+size,y+size),'D':(x,y+size),'O':(x+size/2,y+size/2)}
    if face_fill:
        for face in ['OAB','OCD']:b.poly([pts[t] for t in face],closed=True,fill=PALE,stroke=PALE)
    for edge in F['AD-22']['figures']['edges']:
        b.line(*pts[edge[0]],*pts[edge[1]],color=TEAL if edge in selected else GRAY,width=2.4 if edge in selected else .8)
    for label,(xx,yy) in pts.items():
        b.circle(xx,yy,3,fill=INK,stroke=INK)
        offsets={'A':(-13,-16),'B':(7,-16),'C':(7,3),'D':(-13,3),'O':(11,-5)}
        dx,dy=offsets[label];tag(b,label,xx+dx,yy+dy,10)
def face_board(b,y,h):
    size=min(137,h-34);square_diagram(b,66,y+17,size)
    x=244;w=324
    tag(b,'Available face cards (not selected edges)',x,y+1,9)
    for i,face in enumerate(['OAB','OCD']):
        b.box(x+137*i,y+24,116,37,fill=PALE,stroke=LIGHT)
        b.label(face,x+58+137*i,y+35,size=12,align='center')
    panel(b,y+74,h-74,'Chosen marks / parity / move record',x,w)
def face_classify(b,y,h):
    size=min(116,h-35);square_diagram(b,64,y+18,size)
    panel(b,y,h,'Invariant and a move sequence',218,350)
def matrix_grid(b,x,y,rows,cols,cell=20,values=None):
    b.grid(x,y,len(cols)*cell,len(rows)*cell,len(cols),len(rows))
    for j,s in enumerate(cols):b.label(s,x+(j+.5)*cell,y-17,size=8,align='center',color=GRAY)
    for i,s in enumerate(rows):b.label(s,x-7,y+(i+.5)*cell-5,size=8,align='right',color=GRAY)
    if values is not None:
        for i,row in enumerate(values):
            for j,v in enumerate(row):b.label(str(v),x+(j+.5)*cell,y+(i+.5)*cell-6,size=9,align='center')
def boundaries(b,y,h):
    edges=F['AD-22']['figures']['edges'];cell=min(21,(h-45)/8)
    title(b,'∂₁',57,y);title(b,'∂₂',391,y)
    matrix_grid(b,70,y+39,['A','B','C','D','O'],edges,cell)
    matrix_grid(b,422,y+39,edges,['OAB','OCD'],cell)
    # Space below the first matrix for bases and the matrix-product check.
    yy=y+44+5*cell
    if y+h-yy>30:panel(b,yy,y+h-yy,'Bases / product check',44,306)
def module_pair(b,y,h):
    for x,name,counts in [(44,'P = M(3,1)',[3,1]),(314,'Q = M(1,3)',[1,3])]:
        panel(b,y,h,name,x,254)
        for j,count in enumerate(counts):
            xx=x+12+121*j;b.box(xx,y+34,109,48,stroke=LIGHT)
            for k in range(count):b.circle(xx+21+27*k,y+59,6,fill=WHITE,stroke=GRAY)
            tag(b,'r control' if j==0 else 's control',xx+17,y+87,9)
        tag(b,'Circles mark basis directions.',x+10,y+108,9)
        tag(b,'Test e₁ and e₂; explain the invariant.',x+10,y+h-22,9)
def complement(b,y,h):
    ledger(['Module M(a,b)','Complement you choose','Free result / minimality'],[1,1.2,1.5])(b,y,h)
def ring(b,cx,cy,r,n=6,word=None):
    b.circle(cx,cy,r,fill=None,stroke=LIGHT)
    for i in range(n):
        t=-pi/2+2*pi*i/n;x=cx+r*cos(t);yy=cy+r*sin(t)
        b.circle(x,yy,8,fill=PALE if word and word[i]=='1' else WHITE,stroke=INK,width=.8)
        if word is not None:b.label(word[i],x,yy-6,size=9,align='center')
    b.line(cx,cy-r-11,cx,cy-r-18,color=GRAY)
def necklace(b,y,h):
    r=min(53,(h-51)/2);ring(b,113,y+h/2+5,r)
    tag(b,'temporary top mark',57,y+3,9);tag(b,'record clockwise',66,y+h-15,9)
    panel(b,y,h,'Open catalog / why complete?',202,366)
def fixedturns(b,y,h):
    cell=(h-30)/6;x=44;widths=[55,232,237]
    b.box(x,y,524,h,stroke=LIGHT)
    for offset,label in [(0,'j'),(55,'Position cycles'),(287,'Fixed patterns / reason')]:
        tag(b,label,x+offset+7,y+6)
        if offset:b.line(x+offset,y,x+offset,y+h,color=LIGHT,width=.6)
    b.line(44,y+27,568,y+27,color=LIGHT,width=.7)
    for i in range(6):
        yy=y+29+i*cell;b.label(str(i),67,yy+cell/2-6,size=10,align='center')
        if i:b.line(44,yy,568,yy,color=LIGHT,width=.5)

LAYOUTS={
 'AD-17':[(numberline,split(['Rule A: weighted certificate','Rule B: weighted certificate'])),(ledger(['Exact formula','First round / preceding round'],[1,1.2]),ledger(['Chosen pair','All pairs / boundary cases'],[1,2])),(ledger(['Parameter case','Limit / proof'],[1,2]),split(['Parameter equations','Order of the markers']))],
 'AD-18':[(image_trials,collapse_grid),(split(['Nonzero first column','Zero column / collapse criterion']),ledger(['All area-preserving choices','Inverse and orientation'],[1,1.3])),(ledger(['Coordinate-arrow images','Product certificate'],[1,1.1]),split(['A₃ length test','Both unit lengths: proof']))],
 'AD-19':[(ledger(['Chosen inputs / targets','All preimages'],[1,1.3]),basisledger),(blocks,split(['Indecomposable blocks','Uniqueness / converse'])),(basisledger,split(['Independent bases','Same basis on both sides']))],
 'AD-20':[(orders,ledger(['Products / equations','Complete commuting family'],[1.2,1])),(split(['Bilinearity / alternation','Trace / zero bracket']),split(['[[N,C],C]','[N,[C,C]]'])),(jacobi,split(['Necessary tests / sufficiency','Inside trace-zero matrices']))],
 'AD-21':[(inventories,ledger(['New color of w','Effect / maximality'],[1,2])),(tokens,split(['Existence: define the map','Uniqueness / empty set'])),(split(['Duplicate an entry','Remove an entry']),split(['Maps in both directions','Composites / uniqueness']))],
 'AD-22':[(face_board,ledger(['Outer marks a,b,c,d','Spokes / completeness proof'],[1,1.7])),(face_classify,split(['Outer square: purchases','AB+BC+OC+OA: purchases'])),(boundaries,ledger(['Chosen face set S','Surviving coordinates / proof'],[1,2]))],
 'AD-23':[(module_pair,split(['Idempotent decomposition','Finite dimensions / classification'])),(complement,split(['The same addition to P and Q','Free / nonfree additions'])),(ledger(['Equivalent formal descriptions','Which are actual classes?'],[1,1.1]),split(['Isomorphism to Z²','Universal extension / uniqueness']))],
 'AD-24':[(necklace,ledger(['Your necklace','Distinct turns / counting check'],[1,1.8])),(fixedturns,split(['Count by turns','Count by orbits'])),(split(['An actual reflected pair','Complete revised catalog']),ledger(['General fixed-pattern formula','Eight positions / four red'],[1.3,1]))]
}

def render_students(b,family_id):
    f=F[family_id]
    for n,(a,c) in enumerate(LAYOUTS[family_id],1):
        ratio=.5
        if (family_id,n) in [('AD-18',1),('AD-20',1),('AD-21',1),('AD-22',3),('AD-23',1),('AD-24',2)]:ratio=.56
        pair(b,f,n,a,c,ratio)

def key_start(b,fid,title0,needed):
    if b.y+needed>730:b.new_page(fid,title0,'Facilitator / worked certificate')
    else:b.h(title0);b.y+=14

def render_key_figures(b,family_id):
    if family_id=='AD-18':
        key_start(b,family_id,'The chosen image squares',230);y=b.y
        for x,k,area in [(44,1,3),(314,5,-1)]:
            title(b,'k = '+str(k)+'; signed area '+str(area),x,y)
            coordinate_grid(b,x,y+22,254,162,k,True)
        b.y=y+194
        b.p('The same base u=(2,1) has signed heights 3/√5 and −1/√5. The second traversal reverses orientation. Both axes use the same scale.',size=11);b.y+=12
    elif family_id=='AD-22':
        key_start(b,family_id,'Boundary matrices and quotient coordinates',365);y=b.y
        edge=F[family_id]['figures']['edges']
        d1=[[1,0,0,1,1,0,0,0],[1,1,0,0,0,1,0,0],[0,1,1,0,0,0,1,0],[0,0,1,1,0,0,0,1],[0,0,0,0,1,1,1,1]]
        d2=[[1,0],[0,0],[0,1],[0,0],[1,0],[1,0],[0,1],[0,1]]
        title(b,'∂₁',53,y);title(b,'∂₂',405,y)
        matrix_grid(b,70,y+36,['A','B','C','D','O'],edge,24,d1)
        matrix_grid(b,440,y+36,edge,['OAB','OCD'],24,d2)
        b.y=y+245
        b.p('The four triangular cycles T₁,T₂,T₃,T₄ form a kernel basis because their outer-edge coordinates are the four unit vectors. Available moves span T₁,T₃. The unfilled-face coordinates b and d identify the four classes in F2².',size=11);b.y+=12
        b.p('The zero class consists of every pattern erasable using the available cards, not just the empty edge pattern. Buying OBC and ODA erases the outer square; buying OBC alone erases T₁+T₂.',size=11);b.y+=12
    elif family_id=='AD-24':
        key_start(b,family_id,'A complete rotation catalog',240);y=b.y
        for i,word in enumerate(['000111','001011','001101','010101']):
            cx=105+134*i;ring(b,cx,y+72,39,word=word)
            b.label(word,cx,y+124,size=10,align='center')
            b.label('orbit '+('2' if i==3 else '6'),cx,y+143,size=9,align='center',color=GRAY)
        b.y=y+172
        b.p('Colors are encoded by the printed 0/1 labels. The two middle necklaces merge under reflection. Fixed counts for turns j=0,…,5 are 20,0,2,0,2,0; their mean is 4. The orbit sizes total 20 labeled strings.',size=11);b.y+=12
