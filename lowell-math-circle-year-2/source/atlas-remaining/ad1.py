"""Custom, staged student workspaces for AD-01 through AD-08."""
from math import cos,sin,pi
import json
from sheet import DATA,INK,GRAY,LIGHT,TEAL,PALE,WHITE,BOLD
from common import start,question,blank,lines,family_data

F=family_data('ad1')
CHECK=json.loads((DATA/'ad1-checks-results.json').read_text())

def tag(b,s,x,y,size=10):b.label(s,x,y,size=size,color=GRAY)
def heading(b,s,x,y):b.label(s,x,y,size=11,font=BOLD,color=TEAL)
def ruleline(b,x,y,w):b.line(x,y,x+w,y,color=LIGHT,width=.7)
def openwork(b,y,h,label=''):
    if label:tag(b,label,49,y+5)
    b.box(44,y,524,h,stroke=LIGHT,radius=5);b.y=y+h+12

def setcard(b,items,x,y,w=114,h=39,caption=True):
    b.box(x,y,w,h,stroke=LIGHT,radius=4)
    s='∅' if not items else '  '.join(items)
    b.label(s,x+w/2,y+(h-16)/2,size=13,align='center')

def deck(b,cards,x,y,cols=4,cw=120,ch=37,gap=10):
    for i,items in enumerate(cards):setcard(b,items,x+(i%cols)*(cw+gap),y+(i//cols)*(ch+gap),cw,ch)
    return y+((len(cards)+cols-1)//cols)*(ch+gap)-gap

def property_card(b,typ,x,y,w=112,h=54):
    b.box(x,y,w,h,stroke=LIGHT,radius=4)
    cx=x+23;cy=y+h/2
    if typ['shape']=='circle':b.circle(cx,cy,13,fill=PALE,stroke=INK)
    else:b.box(cx-13,cy-13,26,26,fill=PALE,stroke=INK)
    b.label(typ['color'][0].upper(),cx,cy-7,size=11,align='center',font=BOLD)
    b.label(typ['color'],x+45,y+12,size=10)
    b.label(typ['shape'],x+45,y+28,size=10)

def property_bank(b,f,y):
    for i,t in enumerate(f['figures']['card_types']):property_card(b,t,44+i*134,y,w=122)
    return y+66

def worlds(b,y,labels,h=105):
    gap=16;w=(524-gap*(len(labels)-1))/len(labels)
    for i,label in enumerate(labels):
        x=44+i*(w+gap);b.box(x,y,w,h,stroke=LIGHT,radius=12);tag(b,label,x+10,y+7)
    return y+h+12

def bitgrid(b,rows,x,y,cell=29,diagonal=False):
    n=len(rows);m=len(rows[0])
    for i,row in enumerate(rows):
        b.label(str(i+1),x-15,y+i*cell+7,size=10,align='right',color=GRAY)
        for j,bit in enumerate(row):
            if diagonal and i==j:b.box(x+j*cell,y+i*cell,cell,cell,fill=PALE,stroke=LIGHT)
            if bit is not None:b.label(str(bit),x+j*cell+cell/2,y+i*cell+(cell-14)/2,size=12,align='center')
    b.grid(x,y,m*cell,n*cell,m,n)
    for j in range(m):b.label(str(j+1),x+j*cell+cell/2,y-18,size=10,align='center',color=GRAY)
    return y+n*cell

def bitstrip(b,x,y,n=4,cell=35,label=''):
    if label:tag(b,label,x,y-18)
    b.grid(x,y,n*cell,cell,n,1)

def graph(b,vertices,x,y,w=170,h=120,edges=(),reference=(),layout='ring',overpass=False):
    if layout=='square':
        xy={vertices[0]:(x+16,y+18),vertices[1]:(x+w-16,y+18),vertices[2]:(x+w-16,y+h-18),vertices[3]:(x+16,y+h-18)}
    else:
        xy={v:(x+w/2+.38*w*cos(-pi/2+2*pi*i/len(vertices)),y+h/2+.36*h*sin(-pi/2+2*pi*i/len(vertices))) for i,v in enumerate(vertices)}
    for a,c in reference:
        b.line(*xy[a],*xy[c],color=LIGHT,width=.55,dash=[2,2])
    for a,c in edges:
        b.line(*xy[a],*xy[c],color=INK,width=1.5)
    if overpass and len(edges)>=6:
        # Clear the intersection and redraw just AC across it; the gap marks BD as the overpass.
        xa,ya=xy[vertices[0]];xc,yc=xy[vertices[2]]
        mx=(xa+xc)/2;my=(ya+yc)/2
        b.circle(mx,my,5,fill=WHITE,stroke=WHITE,width=0)
        dx=(xc-xa);dy=(yc-ya);d=(dx*dx+dy*dy)**.5
        b.line(mx-7*dx/d,my-7*dy/d,mx+7*dx/d,my+7*dy/d,color=INK,width=1.5)
    for v,(xx,yy) in xy.items():
        b.circle(xx,yy,9,fill=WHITE,stroke=INK,width=1)
        b.label(str(v),xx,yy-6.5,size=10,align='center')
    return xy

def treeframe(b,x,y,w=165,h=118,edges=(),n=4,label='',order=None):
    if label:heading(b,label,x,y)
    return graph(b,order or list(range(1,n+1)),x,y+18,w,h-18,edges=edges)

def roadframe(b,x,y,w=124,h=95,edges=(),reference=(),label='',all_six=False):
    if label:tag(b,label,x,y-14)
    return graph(b,list('ABCD'),x,y,w,h,edges=edges,reference=reference,layout='square',overpass=all_six)

def orderdiagram(b,kind,x,y,w=220,h=165,annotate=False):
    if kind=='diamond':
        data=F['AD-06']['figures']['diamond'];xy={'0':(x+w/2,y+h),'1':(x+w/2,y),'a':(x+18,y+h/2),'b':(x+w/2,y+h/2),'c':(x+w-18,y+h/2)}
    else:
        data=F['AD-06']['figures']['nonlattice'];xy={'0':(x+w/2,y+h),'1':(x+w/2,y),'p':(x+35,y+h*.66),'q':(x+w-35,y+h*.66),'r':(x+35,y+h*.33),'s':(x+w-35,y+h*.33)}
    for a,c in data['covers']:
        xa,ya=xy[a];xc,yc=xy[c];dx,dy=xc-xa,yc-ya;norm=(dx*dx+dy*dy)**.5
        b.arrow(xa+11*dx/norm,ya+11*dy/norm,xc-11*dx/norm,yc-11*dy/norm,width=.8,color=GRAY,head=4)
    for v,(xx,yy) in xy.items():
        b.circle(xx,yy,11,fill=WHITE,stroke=INK);b.label(v,xx,yy-7,size=12,align='center')
    return xy

def recipe_workspace(b,y,h=126):
    # Calculations have dedicated intermediate-result slots; no result is supplied.
    for x,title,lower in [(44,'Recipe L','MEET with X'),(314,'Recipe R','JOIN the two results')]:
        b.box(x,y,254,h,stroke=LIGHT,radius=4);heading(b,title,x+10,y+7)
        if title.endswith('L'):
            tag(b,'JOIN(Y, Z)',x+12,y+32);b.box(x+125,y+28,110,32)
            b.arrow(x+179,y+65,x+179,y+78,color=GRAY)
            tag(b,lower,x+12,y+88);b.box(x+125,y+84,110,32)
        else:
            tag(b,'MEET(X, Y)',x+10,y+31);tag(b,'MEET(X, Z)',x+131,y+31)
            b.box(x+12,y+50,106,27);b.box(x+133,y+50,106,27)
            tag(b,lower,x+12,y+88);b.box(x+159,y+86,80,30)
    b.y=y+h+12

def ring(b,x,y,size=110):
    xy=graph(b,[0,1,2,3],x,y,size,size,layout='ring')
    coords=[xy[k] for k in range(4)]
    for i,(a,c) in enumerate(zip(coords,coords[1:]+coords[:1])):
        dx,dy=c[0]-a[0],c[1]-a[1];d=(dx*dx+dy*dy)**.5
        b.arrow(a[0]+13*dx/d,a[1]+13*dy/d,c[0]-13*dx/d,c[1]-13*dy/d,color=LIGHT,head=4)
    tag(b,'clockwise: add 1',x,y+size+6)

def bags(b,parts,x,y,w=524,h=65):
    gap=12;cw=(w-gap*(len(parts)-1))/len(parts)
    for i,part in enumerate(parts):
        xx=x+i*(cw+gap);b.box(xx,y,cw,h,stroke=LIGHT,radius=16)
        b.label('  '.join(map(str,part)),xx+cw/2,y+h/2-8,size=16,align='center')

def addtable(b,x,y,filled=True):
    table=F['AD-08']['figures']['addition_table']
    rows=[['+','0','1','2','3']]+[[str(i)]+[str(v) if filled else '' for v in row] for i,row in enumerate(table)]
    b.table(rows,x=x,y=y,widths=[32]*5,row_height=27,size=11)

def render_students(b,family_id):
    f=F[family_id];globals()['render_'+family_id.replace('-','_')](b,f)

def render_AD_01(b,f):
    start(b,f,1);question(b,f,1)
    y=property_bank(b,f,b.y);b.y=worlds(b,y,['My smallest world','A different attempt'],112)
    question(b,f,2);y=b.y
    for i,t in enumerate(f['figures']['card_types']):
        x=44+i*134;property_card(b,t,x,y,w=122)
        b.label('keeps / breaks',x+61,y+64,size=10,align='center',color=GRAY)
    b.y=y+88;lines(b,n=2,spacing=24)
    start(b,f,2);question(b,f,3)
    openwork(b,b.y,112,'Draw and label any counterworlds here')
    b.table([['Forced claims','Claims that can fail'],['','']],y=b.y,widths=[262,262],row_height=[28,42]);b.y+=12
    question(b,f,4);y=b.y
    property_bank(b,f,y)
    for i in range(4):b.label('forbidden / required / optional',44+i*134+61,y+62,size=8.3,align='center',color=GRAY)
    b.y=y+89;lines(b,n=2,spacing=22)
    start(b,f,3);question(b,f,5);y=b.y
    b.y=worlds(b,y,['One blue square','Empty tray'],100)
    property_card(b,f['figures']['card_types'][3],111,y+30,w=115,h=50)
    lines(b,n=2,spacing=22)
    question(b,f,6);b.y=worlds(b,b.y,['Only the first statement is true','Only the second statement is true'],133)
    lines(b,n=2,spacing=22)

def render_AD_02(b,f):
    start(b,f,1);question(b,f,1);y=b.y+20
    bitgrid(b,f['figures']['rows'],71,y,cell=36)
    bitstrip(b,321,y+12,label='My missing pattern')
    tag(b,'One witness place for each row',321,y+79)
    b.table([['row','1','2','3','4'],['place','','','','']],x=321,y=y+97,widths=[47,31,31,31,31],row_height=26,size=10)
    b.y=y+166;question(b,f,2);y=b.y+20
    bitgrid(b,[[None]*4 for _ in range(4)],71,y,cell=28)
    bitstrip(b,321,y+8,label='My answer to a partner')
    b.p('My guaranteed method:',x=321,y=y+63,width=226,size=11)
    b.lines(321,y+104,228,2,25);b.y=y+145
    start(b,f,2);question(b,f,3);y=b.y+20
    bitgrid(b,f['figures']['rows'],71,y,cell=31,diagonal=True)
    bitstrip(b,322,y+10,label='Opposite bits')
    b.lines(322,y+93,229,2,26);b.y=y+143
    question(b,f,4);y=b.y
    heading(b,'A complete collection, organized my way',44,y);y+=26
    openwork(b,y,151,'Organize your words here; continue on scrap paper if needed')
    start(b,f,3);question(b,f,5);y=b.y
    heading(b,'A proposed infinite list',44,y)
    rows=[['row / place','1','2','3','...'],['1','s1(1)','s1(2)','s1(3)','...'],['2','s2(1)','s2(2)','s2(3)','...'],['3','s3(1)','s3(2)','s3(3)','...'],['...','...','...','...','...']]
    b.table(rows,x=44,y=y+25,widths=[78,58,58,58,36],row_height=28,size=10)
    b.p('My rule for position i:',x=362,y=y+30,width=201,size=11)
    b.lines(362,y+78,206,3,28);b.y=y+185
    question(b,f,6);openwork(b,b.y,130,'New list: new witnesses');lines(b,n=2,spacing=25)

def render_AD_03(b,f):
    start(b,f,1);question(b,f,1);y=b.y
    b.y=deck(b,f['figures']['cards'],44,y,cols=4,cw=123.5,ch=36,gap=10)+12
    question(b,f,2);b.y=worlds(b,b.y,['A mixed-size collection','Why my selected pairs are legal'],105)
    start(b,f,2);question(b,f,3);y=b.y
    for i in range(6):
        tag(b,str(i+1),44,y+i*47+12);b.box(64,y+i*47,504,37,stroke=LIGHT,radius=4)
    b.y=y+6*47+8;question(b,f,4);lines(b,n=3,spacing=27)
    start(b,f,3);question(b,f,5);y=b.y
    setcard(b,['A'],44,y,85,60);b.p('Keep this card',x=46,y=y+70,width=104,size=10.5,color=GRAY)
    b.box(149,y,419,127,label='My new collection',stroke=LIGHT,radius=5);b.y=y+145
    question(b,f,6);y=b.y
    openwork(b,y,143,'Build a chain certificate for the remaining cards')
    lines(b,n=2,spacing=24)

def render_AD_04(b,f):
    start(b,f,1);question(b,f,1);y=b.y
    for i,(name,edges) in enumerate([('My tree',[]),('Tree X',f['figures']['example_trees']['X']),('Tree Y',f['figures']['example_trees']['Y'])]):
        x=44+i*178;treeframe(b,x,y,164,116,edges=edges,label=name,order=([1,3,2,4] if name=='Tree Y' else None))
        bitstrip(b,x+31,y+126,n=2,cell=32)
        tag(b,'message',x+57,y+162)
        tag(b,'removed: ___ then ___',x+18,y+181)
    b.y=y+210;question(b,f,2);y=b.y
    treeframe(b,57,y,190,122,label='Reconstruct (3, 1)')
    b.p('Surviving labels / next leaf / next edge',x=278,y=y+8,width=284,size=10.5,color=GRAY)
    b.lines(278,y+55,284,3,30);b.y=y+139
    start(b,f,2);question(b,f,3);y=b.y
    bitstrip(b,61,y+20,n=2,cell=39,label='My chosen message')
    treeframe(b,44,y+80,217,143,label='Decoded tree')
    b.table([['surviving labels','remaining message'],['',''],['',''],['','']],x=299,y=y+7,widths=[139,130],row_height=[29,46,46,46],size=10.5)
    b.y=y+237;question(b,f,4);y=b.y
    treeframe(b,64,y,204,124,label='A repeated-label message')
    treeframe(b,342,y,204,124,label='A different-label message')
    b.y=y+139;lines(b,n=1)
    start(b,f,3);question(b,f,5);y=b.y
    treeframe(b,44,y+6,237,187,n=5,label='Decode (4, 4, 2)')
    b.table([['vertex','occurrences','degree']]+[[str(i),'',''] for i in range(1,6)],x=310,y=y+5,widths=[59,107,92],row_height=29,size=10.5)
    b.y=y+211;question(b,f,6);y=b.y
    bitstrip(b,62,y+20,n=3,cell=37,label='A message with exactly two leaves')
    treeframe(b,318,y,236,138,n=5,label='Its tree')
    b.lines(44,y+99,241,2,27);b.y=y+157

def render_AD_05(b,f):
    E=f['figures']['edges'];K=E+[f['figures']['added_edge']]
    start(b,f,1);question(b,f,1);y=b.y
    roadframe(b,58,y+14,209,140,edges=E,label='Available roads')
    roadframe(b,335,y+14,209,140,reference=E,label='Trace your chosen roads')
    b.y=y+170;question(b,f,2);y=b.y+12
    for i in range(12):roadframe(b,44+(i%4)*134,y+(i//4)*90,122,77,reference=E)
    b.y=y+269
    start(b,f,2);question(b,f,3);y=b.y
    roadframe(b,47,y+22,232,176,edges=E,label='Choose one road to close')
    b.table([['closed road','survivors']]+[[''.join(e),''] for e in E],x=325,y=y+3,widths=[129,114],row_height=30,size=11)
    b.y=y+214;question(b,f,4);y=b.y
    b.y=worlds(b,y,['AB closed / AC not used','AB closed / AC used'],124)
    lines(b,n=2,spacing=26)
    start(b,f,3);question(b,f,5);y=b.y
    roadframe(b,62,y+19,191,146,edges=K,all_six=True,label='Six roads; no crossing vertex')
    b.table([['diagonals used','number of trees'],['none',''],['exactly one',''],['both','']],x=302,y=y+7,widths=[139,127],row_height=37,size=10.7)
    b.y=y+187;question(b,f,6);y=b.y
    roadframe(b,52,y+12,215,142,reference=K,label='One closure')
    roadframe(b,330,y+12,215,142,reference=K,label='Relabel it')
    b.y=y+178;lines(b,n=2,spacing=23)
    start(b,f,4);question(b,f,7);y=b.y
    b.table([['vertex','degree']]+[[v,''] for v in 'ABCD'],x=44,y=y,widths=[66,72],row_height=29,size=11)
    heading(b,'L',219,y);b.grid(214,y+25,156,136,4,4)
    heading(b,'Delete D',412,y);b.grid(410,y+25,135,136,3,3)
    b.y=y+179;question(b,f,8);y=b.y
    heading(b,'Delete A',44,y);b.grid(44,y+25,138,129,3,3)
    b.p('Determinant work and comparison:',x=215,y=y,width=353,size=11,color=GRAY)
    b.lines(215,y+38,353,5,25);b.y=y+174

def render_AD_06(b,f):
    start(b,f,1);question(b,f,1);y=b.y
    b.y=deck(b,f['figures']['set_cards'],44,y,4,123.5,31,10)+13
    recipe_workspace(b,b.y,126);question(b,f,2);lines(b,n=3,spacing=27)
    start(b,f,2);question(b,f,3);y=b.y
    orderdiagram(b,'diamond',53,y+20,221,154)
    b.table([['pair','JOIN','MEET'],['same tile','',''],['two middle tiles','',''],['0 and a tile','',''],['1 and a tile','','']],x=309,y=y+1,widths=[127,66,66],row_height=[29,36,36,36,36],size=10)
    b.y=y+197;question(b,f,4);recipe_workspace(b,b.y,126);lines(b,n=1)
    start(b,f,3);question(b,f,5);y=b.y
    orderdiagram(b,'nonlattice',70,y+20,212,170)
    b.p('Common upper bounds of p and q:',x=322,y=y+11,width=246,size=11)
    b.lines(322,y+57,246,2,28)
    b.p('Common lower bounds of r and s:',x=322,y=y+114,width=246,size=11)
    b.lines(322,y+157,246,2,28)
    b.y=y+214;question(b,f,6);y=b.y
    b.box(323,y+10,245,155,label='Redraw the upward diagram',stroke=LIGHT,radius=4)
    b.p('My added comparison and proof:',x=44,y=y+8,width=258,size=11)
    b.lines(44,y+49,248,5,25);b.y=y+180

def render_AD_07(b,f):
    start(b,f,1);question(b,f,1);y=b.y
    for i,rule in enumerate(f['figures']['rules']):
        x=44+i*178;b.box(x,y,166,49,stroke=LIGHT,radius=4)
        b.label(' + '.join(rule['inputs'])+'  →  '+rule['output'],x+83,y+15,size=15,align='center')
    b.table([['start','first new token','next new token','finished set'],['{a, d}','','',''],['{a, d}','','','']],y=y+63,widths=[93,139,139,153],row_height=[31,46,46],size=10.5)
    b.y=y+201;question(b,f,2);openwork(b,b.y,112,'Smallest starting collections and a reason the list is complete');lines(b,n=1)
    start(b,f,2);question(b,f,3);y=b.y
    b.y=deck(b,f['figures']['subset_cards'],44,y,4,123.5,30,8)+12
    b.y=worlds(b,b.y,['Closed collection 1','Closed collection 2','Their union'],70)
    question(b,f,4);y=b.y
    b.circle(137,y+75,54,fill=None,stroke=LIGHT);b.circle(204,y+75,54,fill=None,stroke=LIGHT)
    tag(b,'intersection: shared tokens',63,y+133)
    b.p('Why a rule cannot break closure:',x=304,y=y+5,width=263,size=11)
    b.lines(304,y+48,264,4,25);b.y=y+155
    start(b,f,3);question(b,f,5);y=b.y
    b.box(44,y,187,107,label='My starting set S',stroke=LIGHT,radius=4)
    b.arrow(245,y+54,283,y+54,color=GRAY)
    b.box(298,y,270,107,label='Any closed set containing S',stroke=LIGHT,radius=4)
    b.y=y+121;lines(b,n=3,spacing=25)
    question(b,f,6);y=b.y
    setcard(b,['a'],256,y,100,40)
    b.arrow(264,y+49,176,y+83,color=GRAY);b.arrow(348,y+49,439,y+83,color=GRAY)
    tag(b,'replace a by b',71,y+65);tag(b,'replace a by c',430,y+65)
    b.box(73,y+93,197,47,label='terminal set');b.box(345,y+93,197,47,label='terminal set')
    b.y=y+150;lines(b,n=1)

def render_AD_08(b,f):
    start(b,f,1);question(b,f,1);y=b.y
    ring(b,44,y+9,114);addtable(b,203,y)
    b.box(397,y,171,135,label='My two bags',stroke=LIGHT,radius=10)
    b.y=y+155;question(b,f,2);y=b.y
    bags(b,[[],[]],44,y+5,w=238,h=98)
    b.table([['+','bag ___','bag ___'],['bag ___','',''],['bag ___','','']],x=321,y=y+6,widths=[82,82,83],row_height=36,size=10.5)
    b.y=y+130;lines(b,n=2,spacing=25)
    start(b,f,2);question(b,f,3);y=b.y
    bags(b,f['figures']['repair_partitions'][0],44,y,h=61)
    b.p('Add the same number to both:     ___ ~ ___     becomes     ___ ~ ___',y=y+75,size=11)
    b.y=y+107;lines(b,n=1)
    question(b,f,4);y=b.y
    bags(b,f['figures']['repair_partitions'][1],44,y,h=61)
    b.p('Forced same-bag steps:',y=y+78,size=11,color=GRAY)
    b.lines(44,y+121,524,2,30);b.y=y+166
    start(b,f,3);question(b,f,5);openwork(b,b.y,195,'All valid partitions, with a reason there are no others')
    question(b,f,6);y=b.y
    b.table([['input','f(input)']]+[[str(i),str(v)] for i,v in enumerate(f['figures']['extra_operation'])],x=44,y=y,widths=[77,87],row_height=27,size=11)
    b.p('Same input bag, outputs to compare:',x=245,y=y+4,width=321,size=11)
    b.box(249,y+38,120,48,label='input pair');b.arrow(378,y+63,417,y+63,color=GRAY)
    b.box(427,y+38,137,48,label='output pair')
    b.lines(245,y+117,319,2,27);b.y=y+151

def render_key_figures(b,family_id):
    # Additional pages only where a worked representation materially helps the guide.
    if family_id=='AD-03':
        b.new_page(family_id,'A complete chain certificate','Worked representation / every card appears exactly once')
        y=137
        for row in CHECK['AD-03']['chain_certificate']:
            for i,s in enumerate(row):
                setcard(b,list(s),44+i*107,y,86,44)
                if i+1<len(row):b.arrow(135+i*107,y+22,148+i*107,y+22,color=GRAY,head=5)
            y+=68
        b.p('At most one selected card can come from each row. The six two-symbol cards attain this six-row bound.',y=y+7,size=12)
        b.y=y+76
    elif family_id=='AD-04':
        b.new_page(family_id,'Read the message backward','Worked five-label decoding / message (4, 4, 2)')
        rows=F[family_id]['figures']['guide_decode_rows']
        b.table(rows,y=136,widths=[154,115,139,116],row_height=43,size=11)
        treeframe(b,157,379,296,218,n=5,edges=F[family_id]['figures']['guide_decoded_edges'],label='Reconstructed labeled tree',order=[1,4,3,2,5])
        b.p('Degrees 1, 2, 1, 3, 1 equal message occurrences plus one. Reading construction backward attaches one new leaf each time.',y=620,size=12);b.y+=15
    elif family_id=='AD-05':
        b.new_page(family_id,'The complete road catalog','Worked eight-tree classification / original five-road graph')
        trees=CHECK['AD-05']['original_trees'];without=[t for t in trees if 'AC' not in t];withac=[t for t in trees if 'AC' in t]
        heading(b,'Without AC',44,138)
        for i,t in enumerate(without):roadframe(b,44+(i%2)*272,175+(i//2)*119,232,103,edges=[list(e) for e in t])
        heading(b,'With AC',44,432)
        for i,t in enumerate(withac):roadframe(b,44+(i%2)*272,470+(i//2)*111,232,98,edges=[list(e) for e in t])
        b.y=708
    elif family_id=='AD-06':
        b.new_page(family_id,'Existing operations, different results','Worked five-element diamond counterexample')
        orderdiagram(b,'diamond',170,158,260,186)
        b.table(F[family_id]['figures']['guide_recipe_rows'],y=404,widths=[262,262],row_height=[34,48,48],size=12)
        b.p('Both routes are legal. Their different answers disprove the identity; they do not make JOIN or MEET undefined.',y=566,size=12);b.y+=18
    elif family_id=='AD-08':
        b.new_page(family_id,'Every valid four-ring renaming','Worked classification / addition modulo four')
        for i,part in enumerate(CHECK['AD-08']['valid_addition_partitions']['4']):
            y=146+i*115;bags(b,part,44,y,h=72)
        b.table(F[family_id]['figures']['guide_quotient_rows'],x=180,y=513,widths=[84]*3,row_height=37,size=13)
        b.p('E={0,2}; O={1,3}. An adjacent identification forces all four together. An opposite identification forces parity unless further merged.',y=650,size=12);b.y+=15
