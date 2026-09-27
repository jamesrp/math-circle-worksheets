"""Custom diagrams and workspaces for the editor's final geometry batch."""
import math
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from sheet import FONT,BOLD,TEAL,GRAY,LIGHT,PALE,INK,WHITE,text_markup
from common import start,question,blank,family_data
F=family_data('ga4')

def ph(t):return Paragraph(text_markup(t),ParagraphStyle('m',fontName=FONT,fontSize=11.5,leading=15.18)).wrap(524,1000)[1]+8

def space(b,x,y,w,h,label='Your construction / explanation'):
    b.box(x,y,w,h,label=label)

def staged(b,f,n,draws,weights=None):
    start(b,f,n);qs=f['pages'][n-1]['prompts'];weights=weights or [1]*len(qs)
    free=736-b.y-sum(ph(q['id']+'. '+q['text']) for q in qs)-12*len(qs)
    assert free>=130,(f['id'],n,free)
    for q,draw,wt in zip(qs,draws,weights):
        question(b,f,q['id']);y=b.y;h=free*wt/sum(weights)
        (draw or space)(b,44,y,524,h);b.y=y+h+12

def note(b,t,x,y,w=524,size=10):b.p(t,x=x,y=y,width=w,size=size,color=GRAY)

def axes(b,x,y,w,h,xlim,ylim,ticks=True):
    lo,hi=xlim;bottom,top=ylim
    def at(a,c):return x+(a-lo)*w/(hi-lo),y+h-(c-bottom)*h/(top-bottom)
    for k in range(math.ceil(lo),math.floor(hi)+1):
        px,_=at(k,0);b.line(px,y,px,y+h,LIGHT,.45)
        if ticks:b.label(k,px,y+h+4,size=8,align='center',color=GRAY)
    for k in range(math.ceil(bottom),math.floor(top)+1):
        _,py=at(0,k);b.line(x,py,x+w,py,LIGHT,.45)
        if ticks:b.label(k,x-7,py-5,size=8,align='right',color=GRAY)
    if bottom<=0<=top:b.arrow(*at(lo,0),*at(hi,0),color=GRAY,head=4)
    if lo<=0<=hi:b.arrow(*at(0,bottom),*at(0,top),color=GRAY,head=4)
    return at

def numline(b,x,y,w,lo,hi,step=1):
    b.line(x,y,x+w,y,GRAY,.8)
    for i in range(round((hi-lo)/step)+1):
        a=lo+i*step;xx=x+(a-lo)*w/(hi-lo);b.line(xx,y-4,xx,y+4,GRAY,.7)
        b.label(f'{a:g}',xx,y+8,size=9,align='center',color=GRAY)

def interval_log(b,x,y,w,h):
    rh=h/4
    for i in range(4):
        yy=y+i*rh
        b.label('Test '+str(i+1)+': ______',x,yy+4,size=10)
        b.line(x+128,yy+17,x+w-12,yy+17,GRAY,.8)
        b.label('surviving endpoints: _____________________',x+128,yy+29,size=9,color=GRAY)

def bracket_table(b,x,y,w,h):
    rows=[['Test','Exact square','Kept bracket']]+[[str(i),'',''] for i in range(1,5)]
    b.table(rows,x=x,y=y,widths=[64,160,300],row_height=max(28,h/5),size=10)

def newton_log(b,x,y,w,h):
    b.box(x,y,w,h,label='Start / next values / exact explanation')
    for j in range(2):
        yy=y+35+j*(h-48)/2;b.label('x = '+str(j),x+12,yy,size=11)
        b.line(x+74,yy+16,x+w-15,yy+16,LIGHT,.6)

def cubic_line(b,x,y,w,h):
    numline(b,x+20,y+24,w-40,-2,-1,.25)
    b.box(x,y+59,w,h-59,label='Signs / retained bracket / guarantee')

def cylinder_template(b,f):
    start(b,f,1);question(b,f,1)
    top=b.y+9;left=90;w=432;h=288
    assert top+h<657,(top,h)
    b.box(left,top,w,h,stroke=GRAY,width=1)
    b.line(left,top,left,top+h,TEAL,1.6)
    b.line(left+w,top,left+w,top+h,TEAL,1.6)
    b.circle(left,top+h,4,TEAL,TEAL);b.label('A',left+9,top+h-21,font=BOLD)
    b.circle(left+w/2,top,4,TEAL,TEAL);b.label('B',left+w/2+10,top+9,font=BOLD)
    b.label('6 inches / around the cylinder',left+w/2,top+h/2-18,align='center',size=10,color=GRAY)
    b.label('4 inches / height',left+w/2,top+h/2+2,align='center',size=10,color=GRAY)
    b.label('Join these edges',left+5,top+12,size=9,color=TEAL)
    b.label('Join these edges',left+w-5,top+12,size=9,color=TEAL,align='right')
    b.y=top+h+12;question(b,f,2)
    assert 736-b.y>25,(f['id'],b.y)
    blank(b,height=736-b.y,label='Length / second route / what still needs proof')

def lifted_map(b,x,y,w,h):
    scale=min((w-48)/18,(h-60)/4);gridh=4*scale;gridw=18*scale
    at=axes(b,x+(w-gridw)/2,y+14,gridw,gridh,(-9,9),(0,4),False)
    for k in [-6,0,6]:b.line(*at(k,0),*at(k,4),color=GRAY,width=.9,dash=[4,3])
    for k in [-9,-3,3,9]:
        px,py=at(k,4);b.circle(px,py,3.5,TEAL,TEAL);b.label('B '+str(k),px,py-17,size=9,align='center')
    px,py=at(0,0);b.circle(px,py,3.5,TEAL,TEAL);b.label('A (0,0)',px+10,py-19,size=9)
    b.label('Copies continue in both directions; height is always 4.',x+w/2,y+gridh+22,size=9,align='center',color=GRAY)
    if h-gridh>74:b.box(x,y+gridh+45,w,h-gridh-45,label='Chosen copies / lengths')

def destination_log(b,x,y,w,h):
    numline(b,x+18,y+22,w-36,0,6,1)
    b.label('Choose d and mark the winning horizontal displacement.',x,y+52,size=10,color=GRAY)
    b.box(x,y+77,w,h-77,label='Comparisons / switch / tie')

def intervals(b,x,y,w,h):
    sets=[(0,4),(2,6),(3,5),(1,7)];left=x+30;right=x+w-20;rh=min(28,(h-50)/4)
    for i,(a,c) in enumerate(sets):
        yy=y+14+i*rh;b.label(chr(65+i),x,yy-6,size=10)
        for k in range(8):
            px=left+(right-left)*k/7;b.line(px,yy-5,px,yy+5,LIGHT,.45)
            if i==0:b.label(k,px,yy-21,size=8,align='center',color=GRAY)
        px=left+(right-left)*a/7;qx=left+(right-left)*c/7;b.line(px,yy,qx,yy,TEAL,2)
        b.circle(px,yy,2.4,TEAL,TEAL);b.circle(qx,yy,2.4,TEAL,TEAL)
    top=y+14+4*rh
    if top<y+h-35:b.box(x,top,w,y+h-top,label='Common part / your attempted counterexample')

def draw_intervals(b,x,y,w,h):
    b.box(x,y,w,h,label='Draw and label your chosen intervals')
    for i in range(3):b.line(x+20,y+38+i*(h-48)/3,x+w-20,y+38+i*(h-48)/3,LIGHT,.5)

def plane_window(b,x,y,w,h):
    side=min(h-24,195);at=axes(b,x+28,y+7,side,side,(-2,2),(-2,2))
    # Only the common square and axes are supplied; learner adds all constraints.
    b.box(x+28,y+7,side,side,stroke=GRAY)
    b.box(x+side+55,y,w-side-55,h,label='Pair witnesses / no common point')

def point_sets(b,x,y,w,h):
    for i,(name,vals) in enumerate([('A',[0,1]),('B',[1,2]),('C',[0,2])]):
        xx=x+i*174;b.label(name,xx+78,y,size=10,font=BOLD,align='center')
        numline(b,xx+15,y+35,126,0,2,1)
        for v in vals:b.circle(xx+15+63*v,y+35,4,TEAL,TEAL)
    b.box(x,y+77,w,h-77,label='Pair intersections / triple intersection / exact scope')

def prediction_table(b,x,y,w,h):
    b.table([['Band','Before: boundary loops','After: pieces / loops per piece'],['P','',''],['M','','']],x=x,y=y,widths=[58,194,272],size=10,row_height=h/3)

def seam_pair(b,x,y,w,h):
    for j,(title,rev) in enumerate([('P / matching ends',False),('M / half-turn ends',True)]):
        xx=x+j*268;ww=256;hh=min(80,h-48)
        b.label(title,xx,y,size=10,font=BOLD,color=TEAL)
        b.box(xx,y+25,ww,hh,stroke=GRAY)
        b.line(xx,y+25+hh/2,xx+ww,y+25+hh/2,color=GRAY,dash=[5,3])
        b.label('U',xx+ww/2,y+29,align='center');b.label('L',xx+ww/2,y+29+hh/2,align='center')
        for side in [0,1]:
            px=xx+6+side*(ww-12)
            if side and rev:b.arrow(px,y+31,px,y+hh+19,color=TEAL,width=1.4)
            else:b.arrow(px,y+hh+19,px,y+31,color=TEAL,width=1.4)
        if h>143:b.box(xx,y+hh+42,ww,h-hh-42,label='Seam journey / pieces')

def three_lanes(b,x,y,w,h):
    hh=min(111,h-60);b.box(x+18,y+8,w-36,hh,stroke=GRAY)
    for j,lab in enumerate(['U','C','L']):
        yy=y+8+j*hh/3
        if j:b.line(x+18,yy,x+w-18,yy,color=GRAY,dash=[5,3])
        b.label(lab,x+38,yy+hh/6-6,font=BOLD)
        b.label(['L','C','U'][j],x+w-38,yy+hh/6-6,font=BOLD,align='right')
    b.label('Labels on the right show which left lane the seam meets.',x+w/2,y+hh+25,size=9,align='center',color=GRAY)
    b.box(x,y+hh+48,w,h-hh-48,label='Your journeys / surface types / boundary loops')

def time_graph(b,x,y,w,h):
    sideh=min(125,h-30);at=axes(b,x+25,y+8,w-50,sideh,(0,4),(-1,3))
    b.label('t',x+w-13,y+sideh+3,size=10,color=GRAY)
    b.label('value y',x+36,y-10,size=9,color=GRAY)
    if h>sideh+60:b.box(x,y+sideh+34,w,h-sideh-34,label='Chosen start / candidate / verification')

def boundary_terms(b,x,y,w,h):
    b.box(x,y,w,h,label='Finite endpoint T first; then justify T → ∞')
    b.label('At T: ____________________',x+16,y+36,size=11)
    b.label('At 0: ____________________',x+280,y+36,size=11)
    b.line(x+12,y+68,x+w-12,y+68,LIGHT,.6)

def peak_graph(b,x,y,w,h):
    sideh=min(114,h-40);at=axes(b,x+25,y+8,w-50,sideh,(0,4),(0,1),False)
    for k in range(5):px,py=at(k,0);b.label(k,px,py+5,size=8,align='center',color=GRAY)
    b.label('1',x+17,y+3,size=8,align='right',color=GRAY)
    b.label('value y',x+36,y-10,size=9,color=GRAY)
    b.label('time t',x+w-25,y+sideh+21,size=9,color=GRAY,align='right')
    b.box(x,y+sideh+44,w,h-sideh-44,label='Transform / candidate / verification')

def targets(b,x,y,w,h):
    b.table([['Chosen height H','Arrival time','Why it is before 1'],['','',''],['','',''],['','','']],x=x,y=y,widths=[140,154,230],row_height=h/4,size=10)

def doubling_strip(b,x,y,w,h):
    numline(b,x+15,y+21,w-30,0,1,.25)
    b.label('Mark arrival times for your chosen powers of 2.',x,y+52,size=10,color=GRAY)
    b.box(x,y+78,w,h-78,label='Derivative check / nth arrival / gaps')

def asymptote_work(b,x,y,w,h):
    ww=240;hh=min(125,h-35)
    for j,title in enumerate(['Before time 1','After time 1']):
        xx=x+j*284;b.box(xx,y,ww,hh,label=title)
        b.line(xx+ww/2,y+27,xx+ww/2,y+hh-10,GRAY,.7,dash=[3,3]);b.label('t = 1',xx+ww/2+7,y+30,size=9,color=GRAY)
    if h>hh+35:b.box(x,y+hh+12,w,h-hh-12,label='What a real-valued continuation would require')

def starts_table(b,x,y,w,h):
    b.table([['Your start a','Forward interval','Long-time / endpoint behavior'],['Positive:','',''],['Zero:','',''],['Negative:','','']],x=x,y=y,widths=[115,159,250],row_height=h/4,size=10)

def sampling_circle(b,x,y,w,h):
    side=min(h-28,185);at=axes(b,x+30,y+8,side,side,(-2,4),(-1,5))
    cx,cy=at(1,2);b.circle(cx,cy,side/3,fill=None,stroke=GRAY)
    b.circle(cx,cy,2.5,TEAL,TEAL)
    for a,c in [(3,2),(-1,2),(1,4),(1,0)]:b.circle(*at(a,c),3,WHITE,TEAL)
    b.box(x+side+54,y,w-side-54,h,label='Values / average / your second circle')

def rotated_cross(b,x,y,w,h):
    r=min(65,(h-40)/2);cx=x+90;cy=y+h/2;b.circle(cx,cy,r,fill=None,stroke=GRAY)
    theta=.48
    for j in range(4):
        t=theta+j*math.pi/2;px=cx+r*math.cos(t);py=cy-r*math.sin(t)
        b.line(cx,cy,px,py,LIGHT,.7);b.circle(px,py,3,WHITE,TEAL)
    b.circle(cx,cy,2,TEAL,TEAL);b.label('(a,b)',cx,cy+r+10,size=9,align='center',color=GRAY)
    b.box(x+190,y,w-190,h,label='Displacements / cancellation / exact identity')

def sampling_compare(b,x,y,w,h):
    for j,offset in enumerate([0,math.pi/4]):
        cx=x+73+j*173;cy=y+62;r=45;b.circle(cx,cy,r,fill=None,stroke=GRAY)
        b.line(cx-r,cy,cx+r,cy,LIGHT,.6);b.line(cx,cy-r,cx,cy+r,LIGHT,.6)
        for k in range(4):
            t=offset+k*math.pi/2;b.circle(cx+r*math.cos(t),cy-r*math.sin(t),3,WHITE,TEAL)
        b.label('Cardinal' if j==0 else 'Rotated 45°',cx,y+116,size=9,align='center',color=GRAY)
    b.box(x+354,y,w-354,min(h,145),label='Sample values')
    if h>163:b.box(x,y+157,w,h-157,label='What the first test did not prove')

def feedback_graphs(b,x,y,w,h):
    side=min(155,h-30)
    for j,lab in enumerate(['f(x)=(x+1)/3','g(x)=1−x']):
        xx=x+22+j*273;at=axes(b,xx,y+25,side,side,(0,1),(0,1),False)
        b.line(*at(0,0),*at(1,1),color=GRAY,dash=[4,3]);b.label(lab,xx+side/2,y,size=10,align='center',color=TEAL)
        b.label('0',xx,y+side+28,size=8);b.label('1',xx+side,y+side+28,size=8,align='center')
    # Only the diagonal is supplied. Learners draw each machine and feedback.
    if h>side+60:b.box(x,y+side+52,w,h-side-52,label='Starting value / four updates / fixed points')

def unit_square(b,x,y,w,h):
    side=min(172,h-22);at=axes(b,x+25,y+8,side,side,(0,1),(0,1),False)
    b.box(x+25,y+8,side,side,stroke=GRAY);b.line(*at(0,0),*at(1,1),color=GRAY,dash=[4,3])
    b.label('0',x+22,y+side+17,size=9);b.label('1',x+25+side,y+side+17,size=9,align='center')
    b.box(x+side+54,y,w-side-54,h,label='Attempt / endpoint comparison / proof')

def parameter_log(b,x,y,w,h):
    numline(b,x+20,y+22,w-40,-1,1,.5)
    b.label('Choose parameters; find the cases that behave differently.',x,y+52,size=10,color=GRAY)
    b.box(x,y+78,w,h-78,label='Fixed points / exact error formula / complete classification')

def render_students(b,fid):
    f=F[fid]
    if fid=='GA-28':
        staged(b,f,1,[interval_log,None],[1,1]);staged(b,f,2,[bracket_table,None],[1.2,1]);staged(b,f,3,[newton_log,cubic_line])
    elif fid=='GA-30':
        cylinder_template(b,f);staged(b,f,2,[lifted_map,None],[1.2,1]);staged(b,f,3,[destination_log,None])
    elif fid=='GA-31':
        staged(b,f,1,[intervals,draw_intervals],[1.2,1]);staged(b,f,2,[None,draw_intervals]);staged(b,f,3,[plane_window,point_sets],[1.2,1])
    elif fid=='GA-32':
        staged(b,f,1,[prediction_table,None]);staged(b,f,2,[seam_pair,None],[1.2,1]);staged(b,f,3,[three_lanes,None],[1.2,1])
    elif fid=='GA-33':
        staged(b,f,1,[time_graph,None],[1.2,1]);staged(b,f,2,[boundary_terms,None]);staged(b,f,3,[peak_graph,None],[1.2,1])
    elif fid=='GA-34':
        staged(b,f,1,[targets,doubling_strip]);staged(b,f,2,[asymptote_work,None]);staged(b,f,3,[starts_table,None],[1.2,1])
    elif fid=='GA-35':
        staged(b,f,1,[sampling_circle,rotated_cross]);staged(b,f,2,[None,sampling_compare],[1,1.2]);staged(b,f,3,[None,None],[1.2,1])
    elif fid=='GA-36':
        staged(b,f,1,[feedback_graphs,None],[1.3,1]);staged(b,f,2,[unit_square,None],[1.2,1]);staged(b,f,3,[parameter_log,None],[1.2,1])
    else:raise KeyError(fid)

def render_key_figures(b,fid):
    if fid not in ['GA-30','GA-31','GA-32','GA-35']:return
    b.new_page(fid,F[fid]['title'],'Worked diagrams / facilitator only',part='worked diagrams')
    if fid=='GA-30':
        b.h('The two winning lifts',y=b.y);y=b.y+22;at=axes(b,117,y,378,126,(-9,9),(0,6),False)
        for k in [-9,-3,3,9]:
            px,py=at(k,4);b.circle(px,py,4,TEAL,TEAL);b.label(f'({k},4)',px,py-20,size=10,align='center')
            b.line(*at(0,0),px,py,color=TEAL if abs(k)==3 else LIGHT,width=2 if abs(k)==3 else .8)
        b.p('Displacements ±3 give length 5. Displacements ±9 already give √97. The integer bound |3+6k|≥3 excludes every other winding, including copies outside this drawing.',y=y+145,size=11)
    elif fid=='GA-31':
        b.h('Three pair witnesses, no triple witness',y=128)
        at=axes(b,100,185,320,320,(-2,2),(-2,2))
        # Boundary x+y=-1 meets the square at (-2,1) and (1,-2).
        b.poly([at(-2,-2),at(1,-2),at(-2,1)],closed=True,fill=PALE,stroke=TEAL)
        b.line(*at(0,-2),*at(0,2),TEAL,1.4);b.line(*at(-2,0),*at(2,0),TEAL,1.4)
        for p,lab in [((0,0),'A∩B'),((0,-1),'A∩C'),((-1,0),'B∩C')]:
            px,py=at(*p);b.circle(px,py,4,TEAL,TEAL);b.label(lab,px+9,py-20,size=10)
        b.p('A allows the right half; B allows the upper half. C is the shaded triangle x+y≤−1 inside the square. Its upper-right boundary stays away from A∩B.',y=540)
    elif fid=='GA-32':
        b.h('Cut components are cycles of lane names',y=b.y)
        b.table([['Cut','Seam cycles','Result'],['Plain band, center','U→U; L→L','Two annuli'],['Half-turn, center','U→L→U','One annulus'],['Half-turn, three lanes','U→L→U; C→C','One annulus + one Möbius band']],y=b.y+6,widths=[176,148,200],size=11)
        b.p('One reversing seam gives a Möbius band. Two reversing seams give an annulus. These classify surfaces; linking in space is a separate question.',y=b.y+12,size=11)
    else:
        b.h('The quartic distinguishes three averages',y=b.y)
        b.table([['p=x²y² on the unit circle','Average'],['Four cardinal samples','0'],['Four samples rotated 45°','1/4'],['Every angle, equally weighted','1/8']],y=b.y+10,widths=[380,144],size=12)
        b.p('A single finite sample pattern can miss the function between its points. For quadratics the symmetry calculation proves the exact formula; for this quartic the full-circle calculation uses cos²θ sin²θ=(1−cos4θ)/8.',y=b.y+12,size=11)
    b.y+=9
