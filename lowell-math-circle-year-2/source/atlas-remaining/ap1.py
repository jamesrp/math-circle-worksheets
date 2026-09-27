"""AP1 custom investigation pages; mathematical data stays in plans/."""
import math
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from sheet import FONT, BOLD, TEAL, GRAY, INK, LIGHT, PALE, WHITE, text_markup
from common import start, question, family_data
FAMILIES=family_data('ap1')


def ph(text):
    p=Paragraph(text_markup(text),ParagraphStyle('measure',fontName=FONT,fontSize=11.5,leading=11.5*1.32))
    return p.wrap(524,1000)[1]+8


def write_space(b,x,y,w,h,label='Your construction / explanation'):
    b.box(x,y,w,h,label=label)
    if h>80:
        for yy in range(int(y+48),int(y+h-10),27):b.line(x+10,yy,x+w-10,yy,LIGHT,.45)


def region(b,f,page,drawers,weights=None):
    """Allocate real working space after measuring every complete prompt."""
    start(b,f,page)
    qs=f['pages'][page-1]['prompts'];weights=weights or [1]*len(qs)
    free=738-b.y-sum(ph(q['id']+'. '+q['text'])for q in qs)-12*len(qs)
    assert free>60*len(qs),(f['id'],page,free)
    heights=[free*w/sum(weights)for w in weights]
    for q,draw,h in zip(qs,drawers,heights):
        question(b,f,q['id']);y=b.y
        if draw is None:write_space(b,44,y,524,h)
        else:draw(b,44,y,524,h)
        b.y=y+h+12


def numberline(b,x,y,w,lo,hi,label='',center=None,ticks=True):
    b.line(x,y,x+w,y,GRAY,.8)
    if ticks:
        for k in range(lo,hi+1):
            xx=x+(k-lo)*w/(hi-lo);b.line(xx,y-3,xx,y+3,GRAY,.7);b.label(str(k),xx,y+6,size=9,align='center',color=GRAY)
    if center is not None:
        xx=x+(center-lo)*w/(hi-lo);b.circle(xx,y,3,TEAL,TEAL)
    if label:b.label(label,x,y-20,size=10,color=GRAY)


def chips(b,x,y,items,cardw=65,gap=12):
    for i,t in enumerate(items):
        xx=x+i*(cardw+gap);b.box(xx,y,cardw,42,stroke=GRAY);b.label(t,xx+cardw/2,y+11,size=12,align='center')


def bag_cards(b,x,y,w,h):
    for col,(name,vals)in enumerate([('A',['A1 · R','A2 · R','A3 · B']),('B',['B1 · R','B2 · B','B3 · B'])]):
        xx=x+col*270;b.label('Bag '+name,xx,y,size=11,font=BOLD)
        chips(b,xx,y+24,vals,72,9)
        b.box(xx,y+79,254,max(40,h-79),label='Equal-weight outcomes that survive')


def pair_grids(b,x,y,w,h):
    cell=min(51,(h-35)/3);side=3*cell
    for j,name in enumerate(['A','B']):
        xx=x+40+j*266;yy=y+40
        b.label('Bag '+name,xx+side/2,y-2,font=BOLD,align='center')
        b.grid(xx,yy,side,side,3,3)
        for i in range(3):
            b.label(name+str(i+1),xx+(i+.5)*cell,yy-17,size=9,align='center')
            b.label(name+str(i+1),xx-7,yy+(i+.5)*cell-5,size=9,align='right')
    b.label('Rows: first counter     Columns: second counter',x+262,y+h-13,size=9,color=GRAY,align='center')


def weighted_tickets(b,x,y,w,h):
    chips(b,x+55,y,['A ticket','B ticket 1','B ticket 2'],128,15)
    for j in range(3):
        xx=x+119+j*143;b.arrow(xx,y+44,xx,y+64,GRAY)
        b.box(xx-62,y+68,124,h-68,label='Counter outcomes')


def learner_bags(b,x,y,w,h):
    for j,title in enumerate(['Red changes nothing','Red favors A most']):
        xx=x+j*268;b.box(xx,y,256,h,label=title)
        for k in range(2):
            bx=xx+18+k*117;b.box(bx,y+30,103,h-59,label='A'if k==0 else'B',radius=8)
        b.label('Common size: ______',xx+15,y+h-21,size=10)


def score_trials(b,x,y,w,h):
    chips(b,x,y,[f'{a} = {v}'for a,v in FAMILIES['AP-03']['figures']['participants'].items()],77,12)
    b.box(x,y+58,w,h-58,label='Your three trained groups / sums / comparison')


def complement_pairs(b,x,y,w,h):
    b.box(x,y,w,h,label='Paired assignments / sum on each side — organize the list your way')


def coin_tree(b,x,y,w,h):
    b.label('One from (A,F), then (B,E), then (C,D)',x+w/2,y,size=10,align='center')
    ys=[y+25,y+55,y+95,y+140]
    ys=[y+22+(h-65)*i/3 for i in range(4)]
    prev=[x+w/2]
    for depth in range(1,4):
        cur=[x+w*(i+.5)/(2**depth)for i in range(2**depth)]
        for i,cx in enumerate(cur):b.line(prev[i//2],ys[depth-1],cx,ys[depth],LIGHT,.8)
        if depth<3:
            for i,cx in enumerate(cur):b.circle(cx,ys[depth],9,WHITE,GRAY);b.label(('A','F') [i%2]if depth==1 else('B','E')[i%2],cx,ys[depth]-6,size=9,align='center')
        else:
            for i,cx in enumerate(cur):b.label(('C','D')[i%2],cx,ys[depth]-2,size=10,align='center');b.label('sum ___',cx,ys[depth]+19,size=9,align='center')
        prev=cur


def hidden_worlds(b,x,y,w,h):
    rowh=(h-35)/3
    for row,title in enumerate(['Known','World 1','World 2']):
        yy=y+row*rowh;b.label(title,x,yy+13,size=10,color=GRAY)
        for i in range(8):
            xx=x+72+i*56;b.box(xx,yy,47,min(45,rowh-8),stroke=LIGHT)
            if row==0:b.label('1'if i<4 else'?',xx+24,yy+14,size=14,align='center')
            elif i<4:b.label('1',xx+24,yy+14,size=14,align='center')
            if row==0:b.label(str(i+1),xx+24,yy-13,size=9,align='center',color=GRAY)
    b.label('Whole means: World 1 __________    World 2 __________',x+72,y+h-18,size=10)


def two_draw_map(b,x,y,w,h):
    b.label('Group equal-value outcomes instead of listing all identifiers.',x,y,size=10,color=GRAY)
    b.grid(x+20,y+30,210,h-45,2,2)
    b.label('Draw 1 / draw 2',x+124,y+8,size=9,align='center')
    b.box(x+252,y+30,w-252,h-45,label='Means / weights / expected value')


def distributions(b,x,y,w,h):
    for j,title in enumerate(['FULL','RESTRICTED']):
        xx=x+j*270;ww=230;top=y+22;bottom=y+h-29
        b.label(title,xx+ww/2,y,font=BOLD,size=11,align='center')
        b.line(xx+23,top,xx+23,bottom,GRAY,.7);b.line(xx+23,bottom,xx+ww,bottom,GRAY,.7)
        for val in [0,.25,.5,.75,1]:
            yy=bottom-val*(bottom-top);b.line(xx+20,yy,xx+ww,yy,LIGHT,.45)
            b.label(str(val),xx+17,yy-5,size=8,align='right',color=GRAY)
        for k,label in enumerate(['1','3','5']):b.label(label,xx+65+k*71,bottom+7,size=10,align='center')
    b.label('Estimate',x+w/2,y+h-12,size=9,color=GRAY,align='center')


def block_survey(unequal=False):
    def draw(b,x,y,w,h):
        left=['1']*(2 if unequal else 4);right=['5']*(6 if unequal else 4)
        for j,(title,vals)in enumerate([('Block L',left),('Block R',right)]):
            xx=x+j*270;b.label(title,xx,y,size=11,font=BOLD)
            cw=32 if len(vals)>4 else 46
            chips(b,xx,y+22,vals,cw,7)
            b.box(xx,y+79,254,h-79,label='One draw / its contribution')
    return draw


def interval_audit(b,x,y,w,h):
    b.label('My practice secret θ = ______     Label each scale before placing its strip.',x,y,size=10)
    step=(h-27)/5
    for i,e in enumerate([-2,-1,0,1,2]):
        yy=y+28+(i+.45)*step;b.label('E = '+str(e),x,yy-7,size=10)
        b.line(x+82,yy,x+430,yy,LIGHT,.8)
        for k in range(9):b.line(x+82+k*43.5,yy-3,x+82+k*43.5,yy+3,LIGHT,.5)
        b.label('catch? ___',x+449,yy-7,size=10)


def offset_strips(b,x,y,w,h):
    b.box(x,y,w,h,label='Compare candidate intervals above or below the same offset scale')
    numberline(b,x+25,y+h/2,w-50,-4,4,'Offsets from X',center=0)


def coin_audit(b,x,y,w,h):
    rh=(h-24)/5
    for j,title in enumerate(['HEADS','TAILS']):b.label(title,x+190+j*192,y,size=10,font=BOLD,align='center')
    for i,e in enumerate([-2,-1,0,1,2]):
        yy=y+23+i*rh;b.label('E = '+str(e),x+12,yy+rh/2-5,size=10)
        for j in range(2):b.box(x+90+j*216,yy,207,rh)


def curve_graph(b,x,y,w,h):
    # An actual sampled cubic, with no preprinted tangent or iteration.
    left=x+35;top=y+8;ww=w-53;hh=h-43
    tx=lambda t:left+(t+3)*ww/6;ty=lambda z:top+(14-z)*hh/28
    for k in range(-3,4):
        b.line(tx(k),top,tx(k),top+hh,LIGHT,.45);b.label(str(k),tx(k),top+hh+7,size=9,align='center')
    for k in [-10,-5,0,5,10]:
        b.line(left,ty(k),left+ww,ty(k),LIGHT,.45);b.label(str(k),left-7,ty(k)-5,size=8,align='right')
    b.line(left,ty(0),left+ww,ty(0),GRAY,.9);b.line(tx(0),top,tx(0),top+hh,GRAY,.9)
    pts=[(tx(t),ty(t*t*t-5*t))for t in [-3+6*i/600 for i in range(601)]]
    b.poly(pts,stroke=TEAL,width=1.5)
    b.label('x',left+ww+8,ty(0)-13,size=10);b.label('f(x)',tx(0)+7,top-2,size=10)
    b.label('Curve supplied; add your own tangents and exact values.',left,y+h-12,size=9,color=GRAY)


def two_cycle(b,x,y,w,h):
    # Neutral record: do not reveal a cycle length before the learner finds it.
    b.box(x,y,w,h)
    cy=y+43;r=20;xs=[x+65+i*130 for i in range(4)]
    for i,cx in enumerate(xs):
        b.circle(cx,cy,r,WHITE,GRAY);b.label('x'+str(i),cx,y+8,size=10,align='center',color=GRAY)
        if i<3:b.arrow(cx+r+5,cy,xs[i+1]-r-5,cy,TEAL)
    b.label('Next-guess formula / proof of later steps',x+12,y+82,size=10,color=GRAY)


def safeguard_record(b,x,y,w,h):
    for j in range(2):
        yy=y+j*(h/2);b.box(x,yy,w,h/2-5)
        b.label('Update '+str(j+1)+': bracket __________  current x ______  Newton proposal ______',x+10,yy+8,size=10)
        b.label('Accepted? ______   chosen point ______   sign ______   new bracket __________',x+10,yy+35,size=10)


def machine_blank(n):
    def draw(b,x,y,w,h):
        b.box(x,y,w,h,label='Your machine: mark start, YES rooms and R/B arrows')
        if n==2:coords=[(.3,.52),(.7,.52)]
        elif n==3:coords=[(.22,.38),(.78,.38),(.5,.76)]
        else:coords=[]  # Let learners choose the number and arrangement of rooms.
        rad=min(25,h/(5 if n>2 else 3.2))
        for xx,yy in coords:b.circle(x+w*xx,y+h*yy,rad,WHITE,GRAY)
    return draw


def bad_machine(b,x,y,w,h):
    cx1=x+145;cx2=x+360;cy=y+59;r=21
    b.arrow(x+60,cy,cx1-r-3,cy,GRAY)
    b.circle(cx1,cy,r,WHITE,INK);b.circle(cx1,cy,r-4,None,INK);b.circle(cx2,cy,r,WHITE,INK)
    b.arrow(cx1+r+2,cy,cx2-r-2,cy,INK);b.label('R',x+252,cy-17,size=11,align='center')
    for cx,lbl in [(cx1,'B'),(cx2,'R, B')]:
        b.poly([(cx-13,cy-r+3),(cx-34,cy-r-17),(cx+34,cy-r-17),(cx+13,cy-r+3)],stroke=GRAY)
        b.arrow(cx+23,cy-r-8,cx+13,cy-r+3,GRAY,head=4)
        b.label(lbl,cx,cy-r-32,size=10,align='center')
    b.label('START / YES',cx1,cy+26,size=9,align='center');b.label('OTHER',cx2,cy+26,size=9,align='center')
    if h>121:b.box(x,y+112,w,h-112,label='Shortest failing string / what short tests leave open')


def suffix_space(b,x,y,w,h):
    rows=[['Histories','Common suffix','Two answers'],['empty / R','',''],['empty / RR','',''],['R / RR','','']]
    rh=min(34,h/4)
    b.table(rows,x=x,y=y,widths=[175,175,174],size=10,row_height=rh)
    if h>4*rh+28:b.box(x,y+4*rh+8,w,h-4*rh-8,label='Why every smaller machine fails')


def spring(b,x1,y,x2,amp=7,turns=7):
    length=x2-x1;pts=[(x1,y),(x1+length*.12,y)]
    for i in range(turns*2+1):pts.append((x1+length*(.17+.66*i/(turns*2)),y+(amp if i%2 else-amp)))
    pts.extend([(x1+length*.88,y),(x2,y)]);b.poly(pts,stroke=INK,width=1)


def wall(b,x,y,h=34):
    b.line(x,y-h/2,x,y+h/2,INK,1.6)
    for k in range(5):b.line(x-7,y-h/2+k*h/4+7,x,y-h/2+k*h/4,GRAY,.7)


def masses(b,x,y,w,h):
    cy=y+27;left=x+12;right=x+w-12;m1=x+w*.34;m2=x+w*.66
    wall(b,left,cy);wall(b,right,cy)
    spring(b,left,cy,m1-17);spring(b,m1+17,cy,m2-17);spring(b,m2+17,cy,right)
    for j,cx in enumerate([m1,m2]):b.box(cx-17,cy-14,34,28,fill=PALE,stroke=INK);b.label(str(j+1),cx,cy-8,size=12,align='center')
    for xx in [(left+m1)/2,(m1+m2)/2,(m2+right)/2]:b.label('k=1',xx,cy-31,size=9,align='center')
    for j in range(2):numberline(b,x+52,y+81+j*54,w-72,-3,3,'x'+('₁'if j==0 else'₂')+' from its own rest mark',center=0)
    if h>178:b.box(x,y+176,w,h-176,label='Chosen pairs → force pairs / shared multiplier?')


def decomposition(b,x,y,w,h):
    hh=min(98,h*.58)
    for xx,label in [(x,'Equal-motion piece'),(x+190,'Opposite-motion piece'),(x+380,'Chosen pair')]:b.box(xx,y,144,hh,label=label)
    b.label('+',x+166,y+hh/2-9,size=18,align='center');b.label('=',x+356,y+hh/2-9,size=18,align='center')
    if h>hh+27:b.box(x,y+hh+12,w,h-hh-12,label='How to recover both pieces / why unique')


def two_springs(b,x,y,w,h):
    # Explicit fixed and translating bars distinguish force balance and compatibility.
    cy=y+68;mid=x+w/2
    b.label('END-TO-END',x+126,y,size=10,font=BOLD,align='center')
    wall(b,x+10,cy);spring(b,x+10,cy,x+100);b.circle(x+104,cy,3,INK,INK);spring(b,x+108,cy,x+198);b.arrow(x+198,cy,x+242,cy,TEAL)
    b.label('A: k=2',x+57,cy+15,size=9,align='center');b.label('B: k=6',x+153,cy+15,size=9,align='center');b.label('total F=6',x+215,cy-20,size=9,align='center')
    lx=x+291;rx=x+466
    b.label('SIDE-BY-SIDE',x+399,y,size=10,font=BOLD,align='center')
    wall(b,lx,cy,69);b.line(rx,cy-35,rx,cy+35,INK,2)
    spring(b,lx,cy-20,rx);spring(b,lx,cy+20,rx);b.arrow(rx,cy,x+w,cy,TEAL)
    b.label('A: k=2',lx+87,cy-39,size=9,align='center');b.label('B: k=6',lx+87,cy+29,size=9,align='center')
    b.label('F=6',rx+29,cy-19,size=9,align='center')
    b.line(rx-11,cy-43,rx+13,cy-43,GRAY,.8);b.line(rx-11,cy+43,rx+13,cy+43,GRAY,.8)
    if h>140:b.box(x,y+133,w,h-133,label='Label forces and extensions / explain what is shared')


def network_frames(b,x,y,w,h):
    b.box(x,y,w,h,label='Try networks here; continue on scrap paper. Record each extension.')


def dual_frames(b,x,y,w,h):
    for col,title in enumerate(['Original constructions','Their duals / general rule']):b.box(x+268*col,y,256,h,label=title)

def two_arrangements(b,x,y,w,h):
    for col,title in enumerate(['Arrangement 1 / certificate','Arrangement 2 / certificate']):b.box(x+268*col,y,256,h,label=title)


def render_students(book,family_id):
    f=FAMILIES[family_id];b=book
    if family_id=='AP-02':
        region(b,f,1,[bag_cards,None],[1.2,1]);region(b,f,2,[pair_grids,None],[1.4,1]);region(b,f,3,[weighted_tickets,learner_bags],[1,1.25])
    elif family_id=='AP-03':
        region(b,f,1,[score_trials,complement_pairs],[.9,1.25]);region(b,f,2,[None,None,None],[1,1,1]);region(b,f,3,[coin_tree,None],[1.6,1])
    elif family_id=='AP-04':
        region(b,f,1,[hidden_worlds,None],[1.5,1]);region(b,f,2,[two_draw_map,distributions],[1,1.4]);region(b,f,3,[block_survey(),block_survey(True)],[1,1])
    elif family_id=='AP-05':
        region(b,f,1,[interval_audit,None],[1.8,1]);region(b,f,2,[offset_strips,None],[1.25,1]);region(b,f,3,[coin_audit,None,None],[1.2,1,1])
    elif family_id=='AP-06':
        region(b,f,1,[curve_graph,two_cycle],[1.65,1]);region(b,f,2,[None,None]);region(b,f,3,[safeguard_record,None],[1,1.35])
    elif family_id=='AP-08':
        region(b,f,1,[machine_blank(2),bad_machine],[1.25,1]);region(b,f,2,[machine_blank(3),suffix_space],[1,1]);region(b,f,3,[machine_blank(6),None],[1.15,1])
    elif family_id=='AP-09':
        region(b,f,1,[masses,None],[1.65,1]);region(b,f,2,[decomposition,None],[1.2,1]);region(b,f,3,[None,None,None],[1.1,1,1])
    elif family_id=='AP-10':
        region(b,f,1,[two_springs,None],[1.45,1]);region(b,f,2,[network_frames,None],[1.4,1]);region(b,f,3,[dual_frames,two_arrangements],[1,1])
    else:raise KeyError(family_id)


def network(b,ast,x,y,w,h):
    """Horizontal terminal embedding of a recursively series-parallel graph."""
    if not isinstance(ast,list):spring(b,x,y+h/2,x+w,amp=min(6,h/4));return
    kind,a,c=ast
    if kind=='S':
        network(b,a,x,y,w*.48,h);network(b,c,x+w*.52,y,w*.48,h);b.line(x+w*.48,y+h/2,x+w*.52,y+h/2,INK,1)
    else:
        b.line(x,y+h*.25,x,y+h*.75,INK,1.5);b.line(x+w,y+h*.25,x+w,y+h*.75,INK,1.5)
        network(b,a,x,y,w,h/2);network(b,c,x,y+h/2,w,h/2)


def key_heading(b,family_id,title,subtitle):
    if b.y<225:
        b.y+=14;b.h(title);b.y+=7;b.p(subtitle,size=10.5,color=GRAY);b.y+=14
    else:b.new_page(family_id,title,subtitle)

def render_key_figures(b,family_id):
    if family_id=='AP-02':
        key_heading(b,family_id,'Worked outcome map','Facilitator key: replacement draws from one fixed bag')
        for j,name in enumerate(['A','B']):
            xx=66+j*267;yy=b.y+45;cell=62;vals=FAMILIES[family_id]['figures']['bags'][name]
            b.label('Bag '+name,xx+93,yy-37,font=BOLD,align='center')
            for r in range(3):
                for c in range(3):
                    out=vals[r]['color']+vals[c]['color'];b.box(xx+c*cell,yy+r*cell,cell,cell,fill=PALE if out=='RR' else WHITE)
                    b.label(out,xx+(c+.5)*cell,yy+(r+.5)*cell-7,size=13,align='center')
            for i in range(3):b.label(name+str(i+1),xx+(i+.5)*cell,yy-17,size=9,align='center');b.label(name+str(i+1),xx-8,yy+(i+.5)*cell-5,size=9,align='right')
        b.y=yy+222;b.p('All 18 cells have probability 1/18. RR leaves four A cells and one B cell: 4/5. The first draw is the row; replacement permits a counter to appear twice. A different report selects a different event in this same space.',size=11.5);b.y+=15
    elif family_id=='AP-08':
        key_heading(b,family_id,'A machine with a reason','Facilitator key: states record red count modulo 3 and blue count modulo 2')
        y=b.y+80;xs=[125,305,485]
        for row in range(2):
            for col in range(3):
                cx=xs[col];cy=y+row*145;b.circle(cx,cy,29,WHITE,INK)
                if row==col==0:b.circle(cx,cy,24,None,INK)
                b.label(f'({col},{row})',cx,cy-7,size=12,align='center')
                if col<2:b.arrow(cx+32,cy,xs[col+1]-32,cy,TEAL);b.label('R',(cx+xs[col+1])/2,cy-19,size=10,align='center')
            yy=y+row*145
            b.poly([(514,yy),(542,yy),(542,yy-55),(70,yy-55),(70,yy),(93,yy)],stroke=TEAL);b.arrow(79,yy,93,yy,TEAL,head=5);b.label('R',302,yy-72,size=10,align='center')
        for cx in xs:
            b.arrow(cx-8,y+33,cx-8,y+112,GRAY);b.arrow(cx+8,y+112,cx+8,y+33,GRAY);b.label('B',cx+20,y+66,size=10)
        b.arrow(45,y,92,y,INK);b.y=y+196
        b.p('The double ring marks the only YES room. R advances the red remainder around a row; B changes rows. The start is (0,0). Each history pair is distinguished by completing the first to (0,0): a different remainder pair cannot also become (0,0) after the same suffix.',size=11.5);b.y+=15
    elif family_id=='AP-10':
        b.new_page(family_id,'All three-unit-spring responses','Facilitator key: every leaf is an ideal unit spring')
        yy=b.y+20
        asts=FAMILIES[family_id]['figures']['key_three_asts'];labels=['k = 3; extension = 2','k = 1/3; extension = 18','k = 3/2; extension = 4','k = 2/3; extension = 9']
        for i,(ast,lbl)in enumerate(zip(asts,labels)):
            row,col=divmod(i,2);xx=63+col*269;y=yy+row*160
            network(b,ast,xx,y,220,90);b.label(lbl,xx+110,y+111,size=10,align='center')
        b.y=yy+328;b.p('Extensions shown use total force 6. A final series or parallel join splits three leaves into one plus two. The two-leaf part is itself series or parallel; these four cases exhaust the permitted networks.',size=11.5);b.y+=22
        for i,ast in enumerate(FAMILIES[family_id]['figures']['four_spring_key_asts']):network(b,ast,63+i*269,b.y,220,86)
        b.y+=105;b.p('Four springs: two parallel pairs in series, or two series pairs in parallel. Both have k=1 and extension 6 under force 6. The drawings above suppress rest lengths; common vertical connectors are rigid bars constrained to translate.',size=11.5);b.y+=15
