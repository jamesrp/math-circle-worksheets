"""AP11–18: custom diagrams, staged investigations and worked guide figures."""
import math
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from sheet import FONT, BOLD, TEAL, GRAY, INK, LIGHT, PALE, WHITE, text_markup
from common import start, question, family_data

FAMILIES = family_data('ap2')


def ph(text):
    style=ParagraphStyle('ap2-measure',fontName=FONT,fontSize=11.5,leading=15.18)
    return Paragraph(text_markup(text),style).wrap(524,1000)[1]+8


def space(b,x,y,w,h,label='Your construction / certificate'):
    b.box(x,y,w,h,label=label)
    if h>75:
        for yy in range(int(y+47),int(y+h-10),27):
            b.line(x+10,yy,x+w-10,yy,LIGHT,.45)


def region(b,f,page,drawers,weights=None):
    start(b,f,page)
    qs=f['pages'][page-1]['prompts']
    weights=weights or [1]*len(qs)
    free=738-b.y-sum(ph(q['id']+'. '+q['text']) for q in qs)-12*len(qs)
    assert free>70*len(qs),(f['id'],page,free)
    for q,draw,weight in zip(qs,drawers,weights):
        question(b,f,q['id']); y=b.y; h=free*weight/sum(weights)
        (draw or space)(b,44,y,524,h)
        b.y=y+h+12


def axes(b,x,y,w,h,xmin,xmax,ymin,ymax,xlabel='x',ylabel='y',equal=True,step=1):
    iw,ih=w-48,h-42
    sx=iw/(xmax-xmin);sy=ih/(ymax-ymin)
    if equal:sx=sy=min(sx,sy)
    left=x+28+(iw-(xmax-xmin)*sx)/2
    top=y+18+(ih-(ymax-ymin)*sy)/2
    def at(a,c):return left+(a-xmin)*sx,top+(ymax-c)*sy
    for a in range(math.ceil(xmin/step)*step,math.floor(xmax/step)*step+1,step):
        xx,_=at(a,0);b.line(xx,top,xx,top+(ymax-ymin)*sy,LIGHT,.35)
        b.label(str(a),xx,top+(ymax-ymin)*sy+5,size=8,align='center',color=GRAY)
    for c in range(math.ceil(ymin/step)*step,math.floor(ymax/step)*step+1,step):
        _,yy=at(0,c);b.line(left,yy,left+(xmax-xmin)*sx,yy,LIGHT,.35)
        b.label(str(c),left-5,yy-5,size=8,align='right',color=GRAY)
    if ymin<=0<=ymax:
        b.line(*at(xmin,0),*at(xmax,0),GRAY,.8)
    if xmin<=0<=xmax:
        b.line(*at(0,ymin),*at(0,ymax),GRAY,.8)
    b.label(xlabel,left+(xmax-xmin)*sx+7,top+(ymax-ymin)*sy-9,size=10,color=GRAY)
    b.label(ylabel,left-10,top-16,size=10,color=GRAY)
    return at


def point(b,at,p,label,dx=7,dy=-8):
    xx,yy=at(*p);b.circle(xx,yy,2.7,TEAL,TEAL)
    b.label(label,xx+dx,yy+dy,size=10,color=INK)


def tube(b,x,y,w,h):
    yc=y+45
    b.poly([(x+8,yc-25),(x+175,yc-25),(x+240,yc-14),(x+410,yc-14)],stroke=GRAY)
    b.poly([(x+8,yc+25),(x+175,yc+25),(x+240,yc+14),(x+410,yc+14)],stroke=GRAY)
    b.arrow(x+20,yc,x+145,yc,TEAL,1.5);b.arrow(x+266,yc,x+395,yc,TEAL,1.5)
    b.label('area 6; mean speed 2',x+18,y,size=11)
    b.label('area 3; mean speed ____',x+251,y,size=11)
    b.label('schematic cross-sections',x+15,yc+33,size=9,color=GRAY)
    space(b,x,y+104,w,h-104,'One second: entering / leaving / discrepancy')


def patches(b,x,y,w,h):
    b.box(x+8,y+17,58,70,stroke=GRAY);b.box(x+66,y+17,116,70,stroke=GRAY)
    b.label('area 1',x+37,y+28,align='center',size=10)
    b.label('area 2',x+124,y+28,align='center',size=10)
    b.label('speed ___',x+37,y+57,align='center',size=9)
    b.label('speed ___',x+124,y+57,align='center',size=9)
    b.label('Narrow-section patches',x+8,y,size=10,color=GRAY)
    space(b,x+204,y,w-204,h,'Two designs / check the 2 and 5 readings')


def branch(b,x,y,w,h):
    mid=y+45
    b.arrow(x+10,mid,x+83,mid,TEAL,1.5)
    b.arrow(x+83,mid,x+166,mid-27,TEAL,1.5)
    b.arrow(x+83,mid,x+166,mid+27,TEAL,1.5)
    b.label('Q=12',x+11,mid-21,size=10)
    b.label('area 2, speed u',x+103,mid-49,size=10)
    b.label('area 1, speed v',x+103,mid+32,size=10)
    at=axes(b,x+266,y,245,h,0,7,0,14,'u','v',False,2)
    b.label('Mark all allowed pairs.',x+290,y-6,size=9,color=GRAY)
    space(b,x,y+112,242,h-112,'Two splits / equation / endpoints')


def tank(b,x,y,w,h):
    ty=y+20;hh=min(118,h-44)
    b.box(x+36,ty+hh*.6,140,hh*.4,fill=PALE,stroke=PALE)
    b.poly([(x+35,ty),(x+35,ty+hh),(x+177,ty+hh),(x+177,ty)],stroke=GRAY)
    b.line(x+35,ty+hh*.6,x+177,ty+hh*.6,TEAL)
    b.arrow(x+1,ty+16,x+52,ty+16,TEAL)
    b.arrow(x+160,ty+hh-15,x+220,ty+hh-15,TEAL)
    b.label('12 / sec',x+2,ty-4,size=10);b.label('9 / sec',x+169,ty+hh+1,size=10)
    b.label('capacity 20',x+105,ty-18,size=10,align='center')
    b.label('initial volume 8',x+102,ty+hh*.62,size=10,align='center')
    b.label('horizontal area 4',x+102,ty+hh+18,size=10,align='center')
    space(b,x+249,y,w-249,h,'Level / first overflow / what else could explain it?')


def gas(b,x,y,w,h):
    for j,(title,txt) in enumerate([('INLET','density 1 · area 6 · speed 2'),('OUTLET','density ___ · area 3 · speed 3')]):
        xx=x+j*272;b.box(xx,y,252,60,label=title)
        b.label(txt,xx+12,y+29,size=10)
    b.arrow(x+244,y+30,x+279,y+30,TEAL)
    space(b,x,y+75,w,h-75,'Mass per second / why the volume test changes')


def crossing_plot(b,x,y,w,h,fence=False,answer=False):
    at=axes(b,x,y,w,h,-1,8,-4,5,equal=True)
    b.line(*at(-1,0),*at(8,0),TEAL,1.6)
    point(b,at,(0,4),'A');point(b,at,(7,-3),'B')
    if fence:
        b.line(*at(4,0),*at(6,0),TEAL,5)
        b.label('allowed crossing',*at(3.2,.9),size=9,color=TEAL)
    if answer:
        b.poly([at(0,4),at(3,0),at(7,-3)],stroke=TEAL,width=1.5)
        b.line(*at(0,4),*at(7,-3),GRAY,.8,dash=[3,3])
        ccx,ccy=at(3,0);b.circle(ccx,ccy,2.7,TEAL,TEAL)
        b.line(ccx-2,ccy+3,ccx-46,ccy+30,GRAY,.7)
        b.box(ccx-108,ccy+23,80,21,fill=WHITE,stroke=LIGHT)
        b.label('C=(3,0)',ccx-101,ccy+27,size=10)
    return at


def crossings(b,x,y,w,h):
    crossing_plot(b,x,y,273,h)
    space(b,x+287,y,w-287,h,'Crossing x / total distance / total time')


def fence(b,x,y,w,h):
    crossing_plot(b,x,y,254,h,True)
    space(b,x+270,y,w-270,h,'Restricted winner / certificate')


def normals(b,x,y,w,h):
    # Generic positive-angle crossing; no coordinate marks or optimal angles.
    cx=x+92;cy=y+62
    b.line(x+5,cy,x+175,cy,GRAY);b.line(cx,y+3,cx,y+122,GRAY,.7,dash=[3,3])
    b.poly([(x+29,y+9),(cx,cy),(x+150,y+121)],stroke=TEAL)
    for a0,a1 in [(-math.pi/2,math.atan2(-53,-63)),(math.atan2(59,58),math.pi/2)]:
        b.poly([(cx+25*math.cos(a0+(a1-a0)*i/20),cy+25*math.sin(a0+(a1-a0)*i/20)) for i in range(21)],stroke=GRAY,width=.7)
    b.label('θ₁',cx-18,cy-41,size=10,align='center')
    b.label('θ₂',cx+15,cy+29,size=10,align='center')
    b.label('vertical normal; schematic',x+3,y+134,size=9,color=GRAY)
    space(b,x+194,y,w-194,h,'Derivative / strict global certificate / angle relation')


def inverse_crossing(b,x,y,w,h):
    crossing_plot(b,x,y,250,h)
    space(b,x+267,y,w-267,h,'My target s = ____   My lower speed w = ____')


def wave_graph(b,x,y,w,h):
    # Plot only the already supplied reference A, never either resulting sum.
    left=x+35;top=y+12;ww=w-57;hh=h-40
    at=lambda t,v:(left+t*ww/(2*math.pi),top+(3-v)*hh/6)
    for v in range(-3,4):
        xx,yy=at(0,v);b.line(xx,yy,xx+ww,yy,LIGHT,.4);b.label(str(v),xx-7,yy-5,size=8,align='right',color=GRAY)
    for k,t in enumerate([0,math.pi/2,math.pi,3*math.pi/2,2*math.pi]):
        xx,yy=at(t,0);b.line(xx,top,xx,top+hh,LIGHT,.4)
        b.label(['0','π/2','π','3π/2','2π'][k],xx,top+hh+6,size=9,align='center')
    b.line(*at(0,0),*at(2*math.pi,0),GRAY,.8)
    for i in range(120):
        a=i*2*math.pi/120;c=(i+1)*2*math.pi/120
        b.line(*at(a,2*math.sin(a)),*at(c,2*math.sin(c)),GRAY,.7,dash=[2,2])
    b.label('dashed: A only; add your two sum curves',left+5,top+5,size=9,color=GRAY)
    b.label('t',left+ww+12,top+hh-14,size=10)


def coefficient_space(b,x,y,w,h):
    axes(b,x,y,230,h,-1,4,-2,2,'P','Q',True)
    space(b,x+245,y,w-245,h,'Derive I / bound it / attain every value')


def references(b,x,y,w,h):
    for j,title in enumerate(['R(t)=sin t','R(t)=cos t']):
        xx=x+j*269;b.box(xx,y,255,h,label=title)
        b.label('Compatible signals / new readings',xx+12,y+31,size=10,color=GRAY)


def engine(b,x,y,w,h,changed=False):
    yy=y+32
    b.box(x+4,yy,92,46,label='600 K')
    b.box(x+200,yy,94,46,label='engine')
    b.box(x+424,yy,94,46,label='300 K')
    b.arrow(x+96,yy+23,x+200,yy+23,TEAL,1.3)
    b.arrow(x+294,yy+23,x+424,yy+23,TEAL,1.3)
    b.label('Qh=12',x+135,yy+2,size=10,align='center')
    b.label('Qc=____',x+360,yy+2,size=10,align='center')
    b.arrow(x+247,yy+46,x+247,yy+89,TEAL,1.3)
    b.label('W=____',x+267,yy+68,size=10)
    space(b,x,y+133,w,h-133,'My two proposals / entropy calculations / advertised claim')


def cascade(b,x,y,w,h,loss=False):
    # Two separate engines exchange only the middle heat; the middle node stores none.
    yy=y+16;cx=[x+18,x+138,x+252,x+365,x+485]
    labs=['600 K','engine 1','400 K' if loss else 'Tm=____','engine 2','300 K']
    for i,xx in enumerate(cx):
        b.box(xx-16,yy,71 if i%2 else 58,42,stroke=GRAY)
        b.label(labs[i],xx+(19 if i%2 else 13),yy+14,size=9,align='center')
    for i in range(4):
        a=cx[i]+(55 if i%2 else 42);c=cx[i+1]-16
        b.arrow(a,yy+21,c,yy+21,TEAL)
        heat=['12','9' if loss else 'Qm','9' if loss else 'Qm','Qc'][i]
        b.label(heat,(a+c)/2,yy-14,size=10,align='center')
    for xx,lab in [(cx[1]+20,'W1=____'),(cx[3]+20,'W2=____')]:
        b.arrow(xx,yy+42,xx,yy+70,TEAL);b.label(lab,xx,yy+74,size=10,align='center')
    space(b,x,y+119,w,h-119,'Transferred heats / work / reservoir changes')


def binary_tree(b,x,y,w,h,title,answers=False):
    b.label(title,x+w/2,y,size=11,font=BOLD,align='center')
    ys=[y+33,y+max(79,h*.44),y+h-30]
    levels=[[.5],[.23,.77],[.08,.38,.62,.92]]
    for d in [1,2]:
        for i,t in enumerate(levels[d]):
            px=x+w*levels[d-1][i//2];xx=x+w*t
            b.line(px,ys[d-1]+6,xx,ys[d]-9,LIGHT,.8)
            b.label('____', (px+xx)/2, (ys[d-1]+ys[d])/2-10,size=9,align='center')
    b.label('e0',x+w/2,ys[0]-8,size=10,align='center')
    for d in [1,2]:
        for t in levels[d]:b.label('____',x+w*t,ys[d]-5,size=10,align='center')
    b.label('Edges: probability. Nodes: new state.',x+w/2,y+h-7,size=8.5,color=GRAY,align='center')


def two_trees(b,x,y,w,h):
    binary_tree(b,x,y,252,h,'X then Z')
    binary_tree(b,x+272,y,252,h,'Z then X')


def repeat_questions(b,x,y,w,h):
    for j,lab in enumerate(['Z → Z','Z → X → Z']):
        xx=x+j*270;space(b,xx,y,254,h,lab+'  /  selected paths and total')


def matrix_space(b,x,y,w,h):
    for j,lab in enumerate(['P0P+','P+P0']):
        xx=x+j*270;b.label(lab,xx,y,size=11,font=BOLD)
        b.grid(xx+32,y+28,112,64,2,2)
        b.label('apply to e0 → __________',xx+10,y+104,size=10)
        b.label('squared norm → __________',xx+10,y+128,size=10)
    if h>180:space(b,x,y+164,w,h-164,'Match each order to its selected outcomes')


def basis_tree(b,x,y,w,h):
    binary_tree(b,x,y,250,h,'Y then Z')
    space(b,x+266,y,w-266,h,'Both intermediate branches / compare with X')


def unit_choice(b,x,y,w,h):
    at=axes(b,x,y,218,min(h,194),-1,1,-1,1,'','',True)
    center=at(0,0);edge=at(1,0)
    b.circle(*center,edge[0]-center[0],fill=None,stroke=GRAY,width=.7)
    b.label('Choose and draw a basis.',x+109,y+min(h,194)-9,size=9,color=GRAY,align='center')
    space(b,x+234,y,w-234,h,'Probability for general θ / sharp bound')


def spin_row(b,x,y,step=35,spins=None,labels=True):
    for i in range(3):b.line(x+i*step,y,x+(i+1)*step,y,GRAY,1)
    for i in range(4):
        b.circle(x+i*step,y,11,WHITE,GRAY)
        if spins:b.label(spins[i],x+i*step,y-7,size=12,align='center')
        if labels:b.label(str(i+1),x+i*step,y+14,size=8,align='center',color=GRAY)


def spin_attempts(b,x,y,w,h):
    for r in range(2):
        for col in range(2):
            xx=x+18+col*268;yy=y+20+r*(h/2)
            spin_row(b,xx,yy)
            b.label('a=___   weight=___',xx+130,yy-5,size=10)
    b.label('Compare equal + counts with different neighbors.',x+4,y+h-10,size=9,color=GRAY)


def spin_catalog(b,x,y,w,h):
    b.table([['a','How many?','Weight each','Total weight']]+[[str(i),'','',''] for i in range(4)],x=x,y=y,widths=[36,82,88,99],size=10,row_height=max(25,(h-16)/5))
    space(b,x+321,y,w-321,h,'Organized records / alignment probability')


def link_record(b,x,y,w,h):
    spin_row(b,x+27,y+27,step=71)
    for i in range(3):b.label('___',x+62+i*71,y+3,size=10,align='center')
    b.label('first spin ___',x+270,y+22,size=10)
    space(b,x,y+79,w,h-79,'Reconstruction / why one-to-one / weighted count')


def sampler(b,x,y,w,h):
    for i,lab in enumerate(['Fair first spin','Link 12','Link 23','Link 34']):
        xx=x+i*133;b.box(xx,y,121,54,label=lab)
        b.label('choice: ____',xx+10,y+29,size=10)
    space(b,x,y+70,w,h-70,'My small-ticket design / probability of an arbitrary row')


def ring(b,x,y,w,h):
    side=min(94,h-65);xx=x+31;yy=y+21
    ps=[(xx,yy),(xx+side,yy),(xx+side,yy+side),(xx,yy+side)]
    for i in range(4):b.line(*ps[i],*ps[(i+1)%4],GRAY)
    for i,(a,c) in enumerate(ps):
        b.circle(a,c,11,WHITE,GRAY)
        b.label(str(i+1),a,c+(-28 if i<2 else 16),size=9,align='center',color=GRAY)
    for i in range(4):
        a,c=ps[i];aa,cc=ps[(i+1)%4];b.label('___',(a+aa)/2+(-23 if i==3 else 0),(c+cc)/2+(9 if i==2 else -18),size=10,align='center')
    b.label('Spin values go inside the circles.',x+2,y+side+53,size=9,color=GRAY)
    space(b,x+211,y,w-211,h,'Closing rule / class inventory / total and probability')


def rejection(b,x,y,w,h):
    labs=['draw all choices','test closure','accept OR redraw']
    for i,lab in enumerate(labs):
        xx=x+i*180;b.box(xx,y,162,46,label=lab)
        if i<2:b.arrow(xx+162,y+23,xx+180,y+23,TEAL)
    space(b,x,y+63,w,h-63,'Proposal probability / acceptance / conditional probability')


def spacetime(b,x,y,w,h,primed=False,worked=False):
    if primed:
        at=axes(b,x,y,w,h,-8,2,0,13,'x′','t′',True)
        if worked:
            events=[(0,0),(0,4),(-7.5,12.5)]
            b.poly([at(*p) for p in events],stroke=TEAL,width=1.5)
            b.line(*at(0,0),*at(-7.5,12.5),GRAY,1.2)
            for p,l in zip(events,['O′','T′','R′']):point(b,at,p,l)
    else:
        at=axes(b,x,y,w,h,-5,5,0,10,'x','t',True)
        point(b,at,(0,0),'O',7,-15);point(b,at,(0,10),'R',7,1)
        if worked:
            b.poly([at(0,0),at(3,5),at(0,10)],stroke=TEAL,width=1.5)
            b.line(*at(0,0),*at(0,10),GRAY,1.2);point(b,at,(3,5),'T')
    return at


def turn_region(b,x,y,w,h):
    spacetime(b,x,y,248,h)
    space(b,x+268,y,w-268,h,'My route / full legal region / test points')


def transformed(b,x,y,w,h):
    spacetime(b,x,y,250,h,True)
    space(b,x+271,y,w-271,h,'Event coordinates / A and both B intervals')


def orbit_cards(b,x,y,w,h):
    for i,(r,v) in enumerate([(1,6),(4,3),(9,2)]):
        xx=x+i*178;b.box(xx,y,166,43,label=f'true r={r}    true v={v}')
    cx=x+87;cy=y+106;rad=min(43,(h-61)/2)
    b.circle(cx,cy,rad,fill=None,stroke=GRAY)
    b.circle(cx,cy,3,TEAL,TEAL)
    b.line(cx,cy,cx+rad,cy,TEAL);b.label('r',cx+rad/2,cy-17,size=10)
    b.circle(cx+rad,cy,3,WHITE,TEAL);b.arrow(cx+rad,cy,cx+rad,cy-rad,TEAL)
    b.label('true v',cx+rad+8,cy-rad/2-6,size=10)
    b.label('one orbit, schematic',cx,y+h-12,size=9,color=GRAY,align='center')
    space(b,x+195,y+59,w-195,h-59,'Each witness / common center certificate')


def mass_lines(b,x,y,w,h):
    for i,lab in enumerate(['radius 4 observation','radius 9 observation','common masses']):
        yy=y+20+i*33;b.label(lab,x,yy-15,size=10)
        b.line(x+172,yy,x+w-7,yy,GRAY,.7)
        for m in range(30,43,2):
            xx=x+172+(m-30)*(w-179)/12
            b.line(xx,yy-3,xx,yy+3,GRAY,.7);b.label(str(m),xx,yy+5,size=8,align='center',color=GRAY)
    if h>150:space(b,x,y+119,w,h-119,'Necessity and constructive sufficiency')


def error_lines(b,x,y,w,h):
    for i,lab in enumerate(['M=36: possible readings','M=64: possible readings']):
        yy=y+30+i*57;b.label(lab,x,yy-21,size=10)
        b.line(x+181,yy,x+w-7,yy,GRAY,.8)
        b.label('label center and endpoints',x+195,yy+7,size=9,color=GRAY)
    space(b,x,y+117,w,h-117,'Disjointness condition / what happens at equality')


def projection(b,x,y,w,h):
    for i,lab in enumerate(['true speed v','multiply by q','observed w']):
        xx=x+i*180;b.box(xx,y,162,45,label=lab)
        if i<2:b.arrow(xx+162,y+22,xx+180,y+22,TEAL)
    space(b,x,y+62,w,h-62,'Different models / the whole family / lower bound')


def render_students(book,family_id):
    f=FAMILIES[family_id]
    layouts={
        'AP-11':[(tube,patches),(branch,None),(tank,gas)],
        'AP-12':[(crossings,None),(normals,fence),(inverse_crossing,None)],
        'AP-13':[(wave_graph,None),(coefficient_space,None),(references,None)],
        'AP-14':[(engine,None),(cascade,None),(lambda *a:cascade(*a,loss=True),None)],
        'AP-15':[(two_trees,None),(repeat_questions,matrix_space),(basis_tree,unit_choice)],
        'AP-16':[(spin_attempts,spin_catalog),(link_record,sampler),(ring,rejection)],
        'AP-17':[(turn_region,None),(None,None),(transformed,None)],
        'AP-18':[(orbit_cards,None),(mass_lines,error_lines),(projection,None)],
    }
    weights={
        'AP-11':[[1.15,.85],[1.3,.7],[1.1,.9]],
        'AP-12':[[1.15,.85],[1,1],[1.2,.8]],
        'AP-13':[[1.4,.6],[1.05,.95],[1,1]],
        'AP-14':[[1.3,.7],[1.2,.8],[1.2,.8]],
        'AP-15':[[1.5,.5],[.8,1.2],[1,1]],
        'AP-16':[[.9,1.1],[1,1],[1,1]],
        'AP-17':[[1.35,.65],[1,1],[1.3,.7]],
        'AP-18':[[1.2,.8],[1.05,.95],[1,1]],
    }
    for i,drawers in enumerate(layouts[family_id],1):
        region(book,f,i,drawers,weights[family_id][i-1])


def render_key_figures(b,fid):
    if fid=='AP-12':
        b.new_page(fid,'Worked route certificate','Facilitator diagram / reveals the solution')
        crossing_plot(b,62,153,468,378,answer=True)
        b.p('Solid: the fastest route crosses at C=(3,0), with two length-5 legs and time 5/3+5/4=35/12. Dashed: the direct line crosses at x=4; its time is 25√2/12, which is larger.',y=563,size=11.5)
        b.p('The diagram supports the comparison. Strict positivity of T″ on all real x, together with T′(3)=0, is the global uniqueness certificate. Equal horizontal and vertical coordinate units are used.',y=641,size=11.5)
    elif fid=='AP-16':
        b.new_page(fid,'Worked link-count audit','Facilitator table / reveals the enumerations')
        b.p('Four labeled spins; open links 12,23,34, or ring links 12,23,34,41. The first spin has two choices. The link record determines all later spins.',y=150,size=11.5)
        b.table([['a','Open count','Open weight','Ring count','Ring weight']]+[[str(a),str([2,6,6,2][a]) if a<4 else '—',str([2,12,24,16][a]) if a<4 else '—',str([2,0,12,0,2][a]),str([2,0,48,0,32][a])]for a in range(5)],y=230,widths=[44,120,120,120,120],size=11,row_height=42)
        b.p('Open total: 54. Ring total: 82. The ring accepts exactly the records with an even number of D links; the accepted probability is 82/162=41/81.',y=516,size=11.5)
        b.p('The ring proposal gives each valid configuration weight 2^a/162 before conditioning. Dividing by 41/81 gives exactly 2^a/82. Redrawing all choices after rejection matters.',y=597,size=11.5)
    elif fid=='AP-17':
        b.new_page(fid,'Worked spacetime comparison','Coordinates are events; drawn Euclidean lengths are not clock readings')
        spacetime(b,55,157,245,347,worked=True)
        spacetime(b,314,157,245,347,primed=True,worked=True)
        b.p('Original (t,x): O=(0,0), T=(5,3), R=(10,0). Primed (t′,x′): O′=(0,0), T′=(4,0), R′=(25/2,−15/2). Both diagrams use equal units on their own two axes.',y=545,size=11.5)
        b.p('Primed A: (25/2)²−(15/2)²=100, so proper time 10. Primed B: first leg 4; return has differences (17/2,−15/2), interval square 16, and proper time 4. Total 8.',y=620,size=11.5)
