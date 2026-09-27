"""Purpose-built diagrams and student workspaces for GA-01--08."""
import math
from sheet import TEAL, NAVY, GRAY, LIGHT, PALE, INK, WHITE, BOLD
from common import start, question, blank, lines, family_data

FAMILIES = family_data('ga1')


def note(book, text, y=None, x=44, width=524):
    book.p(text, x=x, y=y, width=width, size=10.3, color=GRAY)
    book.y += 8


def work(book, height=70, label=''):
    blank(book, height=height, label=label)


def finish_space(book, label='', minimum=55):
    height=730-book.y
    if height<minimum:
        raise ValueError(f'{book.family_id}: insufficient final space ({height:.1f})')
    blank(book, height=height, label=label)


def q(book, f, number):
    return question(book, f, number)


def xy_axes(book,x,y,w,h,xmin,xmax,ymin,ymax,labels=True):
    """Data axes with top-left bounding rectangle; return data-to-page map."""
    def at(a,b):return (x+(a-xmin)*w/(xmax-xmin),y+h-(b-ymin)*h/(ymax-ymin))
    for a in range(math.ceil(xmin),math.floor(xmax)+1):
        px,_=at(a,0);book.line(px,y,px,y+h,color=LIGHT,width=.4)
    for b in range(math.ceil(ymin),math.floor(ymax)+1):
        _,py=at(0,b);book.line(x,py,x+w,py,color=LIGHT,width=.4)
    if ymin<=0<=ymax:
        ax,ay=at(xmin,0);bx,by=at(xmax,0);book.arrow(ax,ay,bx,by,color=GRAY,head=4)
    if xmin<=0<=xmax:
        ax,ay=at(0,ymin);bx,by=at(0,ymax);book.arrow(ax,ay,bx,by,color=GRAY,head=4)
    if labels:
        for a in range(math.ceil(xmin),math.floor(xmax)+1):
            px,py=at(a,ymin);book.label(a,px,py+3,size=8,align='center',color=GRAY)
        for b in range(math.ceil(ymin),math.floor(ymax)+1):
            px,py=at(xmin,b);book.label(b,px-7,py-5,size=8,align='right',color=GRAY)
    return at


def dial(book,cx,cy,r,title,spokes=45,angle_labels=True):
    book.label(title,cx,cy-r-24,font=BOLD,color=TEAL,align='center',size=11)
    book.circle(cx,cy,r,fill=None,stroke=GRAY,width=.8)
    for theta in range(0,360,spokes):
        angle=math.radians(theta)
        ex,ey=cx+r*math.cos(angle),cy-r*math.sin(angle)
        book.line(cx,cy,ex,ey,color=LIGHT,width=.5)
        if angle_labels and theta%90==0:
            tx=cx+(r+15)*math.cos(angle);ty=cy-(r+15)*math.sin(angle)
            if theta==90:ty=cy-r+13
            book.label(str(theta)+'°',tx,ty-5,size=9,align='center',color=GRAY)
    book.circle(cx,cy,2.2,fill=INK)


def two_dials(book,y,height=180):
    r=(height-48)/2
    dial(book,171,y+height/2,r,'TARGET')
    dial(book,440,y+height/2,r,'ROOTS / track one')
    book.y=y+height+12


def route_strip(book,height=70):
    y=book.y;book.box(44,y,524,height)
    book.label('My signed target moves',54,y+7,size=10,color=GRAY)
    book.label('My signed root moves',54,y+height/2+4,size=10,color=GRAY)
    for i in range(1,5):book.line(190+i*71,y,190+i*71,y+height,color=LIGHT,width=.5)
    book.line(44,y+height/2,568,y+height/2,color=LIGHT,width=.5)
    book.y=y+height+12


def paired_argand(book,y,height=185,names=('z','w')):
    size=height-35
    for cx,name in zip([171,440],names):
        x=cx-size/2
        xy_axes(book,x,y+18,size,size,-3,3,-3,3,labels=False)
        book.label(name,cx,y-3,font=BOLD,color=TEAL,align='center')
        book.label('Re',x+size+9,y+18+size/2-5,size=9,color=GRAY)
        book.label('Im',cx+8,y+9,size=9,color=GRAY)
        for a in (-2,-1,1,2):book.label(a,cx+a*size/6,y+18+size/2+3,size=8,align='center',color=GRAY)
        book.label('1 grid step = 1',cx,y+size+24,size=8,align='center',color=GRAY)
    book.y=y+height+12


def graph(book,graph_data,y,height=90,boundary_override=None):
    coords=graph_data['nodes']; xs=[v[0] for v in coords.values()];ys=[v[1] for v in coords.values()]
    mx=max(xs); my=max(ys)
    pos={key:(76+460*pt[0]/mx, y+height/2-((pt[1]-my/2)*45 if my else 0)) for key,pt in coords.items()}
    for a,b in graph_data['edges']:book.line(*pos[a],*pos[b],color=GRAY,width=1.4)
    boundary=boundary_override or graph_data['boundary']
    for key,(x,py) in pos.items():
        if key in boundary:
            book.box(x-17,py-17,34,34,fill=PALE,stroke=TEAL)
            book.label(boundary[key],x,py-7,align='center',font=BOLD,size=12)
        else:
            book.circle(x,py,19,stroke=TEAL,width=1.2)
            book.label(key,x,py+24,align='center',font=BOLD,size=11,color=GRAY)
    book.y=y+height+18


def time_axes(book,y,height=140,xmax=5,ymax=10):
    y+=12
    xy_axes(book,76,y+5,460,height-28,0,xmax,0,ymax)
    book.label('height y',52,y-11,size=10,color=GRAY)
    book.label('time t',552,y+height-11,size=10,align='right',color=GRAY)
    book.y=y+height+15


def word_slots(book,height=58):
    y=book.y
    book.box(44,y,524,height)
    book.label('My word, read left to right',54,y+6,size=10,color=GRAY)
    for i in range(6):
        book.box(230+50*i,y+13,39,32)
    book.y=y+height+12


def rotation_mat(book,y):
    cx,cy=135,y+66
    book.arrow(cx,cy,cx+80,cy,color=TEAL,width=1.4)
    book.arrow(cx,cy,cx-45,cy+32,color=TEAL,width=1.4)
    book.arrow(cx,cy,cx,cy-52,color=TEAL,width=1.4)
    book.label('+x / right',cx+47,cy+10,size=9)
    book.label('+y / away',cx-67,cy+35,size=9)
    book.label('+z / up',cx+10,cy-59,size=9)
    book.p('ROOM AXES STAY FIXED',x=300,y=y+10,width=240,size=11,font=BOLD,color=TEAL)
    book.p('Reset faces: R toward +x; B toward +z.',x=300,y=y+32,width=245,size=10.5)
    for i,label in enumerate(('X','Y','X−','Y−')):
        book.box(307+58*i,y+63,44,34,fill=PALE,stroke=LIGHT)
        book.label(label,329+58*i,y+69,size=13,align='center',font=BOLD)
    book.y=y+122


def profile(book,heights,y,height=135,period=6):
    steps=len(heights)-1
    x0,w=61,490
    for k in range(7):
        py=y+height-k*height/6
        book.line(x0,py,x0+w,py,color=LIGHT,width=.45)
        book.label(k,x0-9,py-5,size=8,align='right',color=GRAY)
    for k in range(steps+1):
        x=x0+k*w/steps
        book.line(x,y,x,y+height,color=LIGHT,width=.45)
        book.label(k,x,y+height+3,size=8,align='center',color=GRAY)
    pts=[(x0+k*w/steps,y+height-v*height/6) for k,v in enumerate(heights)]
    book.poly(pts,stroke=TEAL,width=1.8)
    for k,(x,py) in enumerate(pts):
        book.circle(x,py,2.6,fill=TEAL,stroke=TEAL)
        if k<6:book.label(heights[k],x,py-15,size=9,align='center',color=TEAL)
    span=3*w/steps
    by=y+height+36
    book.line(x0,by,x0+span,by,width=1.2,color=NAVY)
    for x in (x0,x0+span):book.line(x,by-5,x,by+5,width=1.2,color=NAVY)
    book.label('Keep this separation: 3 spacings',x0+span+12,by-6,size=9,color=GRAY)
    book.y=by+22


def design_fence(book,y,height=112):
    x0,w=64,478
    book.grid(x0,y,w,height,6,6)
    for k in range(7):book.label(k,x0+k*w/6,y+height+3,size=8,align='center',color=GRAY)
    book.label('Repeat the first height at post 6.',x0,y+height+19,size=9,color=GRAY)
    by=y+height+44
    book.line(x0,by,x0+w/2,by,color=NAVY,width=1.2)
    for px in (x0,x0+w/2):book.line(px,by-4,px,by+4,color=NAVY,width=1.2)
    book.label('3 spacings on this grid',x0+w/2+12,by-5,size=9,color=GRAY)
    book.y=by+18


def render_01(book,f):
    start(book,f,1);rotation_mat(book,book.y)
    q(book,f,1);work(book,72,'My word / reversed word: red and blue predictions')
    q(book,f,2);finish_space(book,'Reset / words / final direction that proves a difference',70)
    start(book,f,2)
    q(book,f,3);word_slots(book,58)
    q(book,f,4);work(book,106,'One-card words / same-axis pairs / different-axis pairs')
    q(book,f,5);finish_space(book,'A test of the whole orientation',70)
    start(book,f,3)
    q(book,f,6)
    y=book.y;dial(book,171,y+78,55,'MY TWO ANGLES',spokes=90)
    book.box(300,y+10,268,140,label='Same-center explanation')
    book.y=y+169
    q(book,f,7)
    y=book.y+10;x0=64;step=48
    book.arrow(x0,y+22,x0+10*step,y+22,color=GRAY)
    for i in range(-5,6):
        x=x0+(i+5)*step;book.line(x,y+17,x,y+27,color=GRAY,width=.8)
        book.label(i,x,y+31,size=9,align='center')
    for name,value in [('A',0),('B',2)]:
        x=x0+(value+5)*step;book.circle(x,y+22,3,fill=TEAL,stroke=TEAL)
        book.label(name,x,y+1,size=11,font=BOLD,align='center',color=TEAL)
    book.y=y+66;finish_space(book,'A then B / B then A / the assumption that matters',90)


def render_02(book,f):
    start(book,f,1);profile(book,f['figures']['profile']['heights'],book.y,105)
    q(book,f,1);lines(book,n=1)
    q(book,f,2);design_fence(book,book.y,102)
    start(book,f,2)
    q(book,f,3)
    y=book.y
    for x,label in [(44,'START: red higher'),(316,'AFTER HALF A TURN')]:
        book.box(x,y,252,128,label=label)
    book.y=y+140
    work(book,95,'Why the change must pass through a match')
    q(book,f,4);finish_space(book,'Posts / positions between posts',70)
    start(book,f,3)
    q(book,f,5);work(book,76,'At the middle and at the seam')
    q(book,f,6);work(book,132,'Three ramp intervals: choose u and compare the two heights')
    q(book,f,7);finish_space(book,'What the trail example shows',60)


def render_03(book,f):
    start(book,f,1);q(book,f,1)
    y=book.y+13;book.arrow(64,y+31,548,y+31,color=GRAY)
    for v,label in [(0,'0'),(.5,'1/2'),(1,'1')]:
        x=80+450*v;book.circle(x,y+31,3,fill=TEAL,stroke=TEAL)
        book.label(label,x,y+39,size=10,align='center')
    book.label('Choose two additional points.',64,y,size=10,color=GRAY)
    book.y=y+70;work(book,83,'Centers and positive widths; cost of all five')
    q(book,f,2);finish_space(book,'My rule for point number n / why the future still has a budget',130)
    start(book,f,2)
    q(book,f,3);work(book,126,'Coverage of p_n / partial sum and tail')
    q(book,f,4);work(book,106,'My rule for a new positive budget B')
    q(book,f,5);finish_space(book,'Assigned cost and union length are different quantities',65)
    start(book,f,3);q(book,f,6)
    y=book.y
    for row in range(1,6):
        py=y+(row-1)*25
        book.label('q='+str(row),50,py+5,size=10,color=GRAY)
        for p in range(row+1):
            x=115+p*70;book.box(x,py,62,24)
            book.label(f'{p}/{row}',x+31,py+5,size=10,align='center')
    book.y=y+136
    work(book,54,'My three fractions and where they appear')
    q(book,f,7);finish_space(book,'Use the supplied theorem; distinguish existence from a formula',80)


def render_04(book,f):
    start(book,f,1);q(book,f,1);two_dials(book,book.y,190)
    q(book,f,2);route_strip(book,70)
    finish_space(book,'My endpoint prediction and check',50)
    start(book,f,2);q(book,f,3)
    work(book,177,'Could two separated legal alternatives exchange continuously?')
    q(book,f,4);finish_space(book,'The same target at start and finish',150)
    start(book,f,3);q(book,f,5);route_strip(book,58);route_strip(book,58)
    work(book,65,'Return rule, including negative k')
    q(book,f,6);finish_space(book,'Legal roots / first return / explanation',130)


def render_05(book,f):
    start(book,f,1);q(book,f,1);graph(book,f['figures']['path'],book.y,70)
    work(book,46,'Check all three averages')
    q(book,f,2);graph(book,f['figures']['shortcut'],book.y,110)
    finish_space(book,'Prediction / new values / simultaneous check',90)
    start(book,f,2);q(book,f,3)
    work(book,115,'My attempted graph: square fixed nodes, circle averaging nodes')
    q(book,f,4);work(book,109,'Follow a largest value along a path to a fixed square')
    q(book,f,5);finish_space(book,'A component without a fixed square',62)
    start(book,f,3);q(book,f,6)
    work(book,165,'What subtraction does to the boundary and averaging rules')
    q(book,f,7);finish_space(book,'Bound first / then solve / compare the changes',155)


def render_06(book,f):
    start(book,f,1);q(book,f,1);paired_argand(book,book.y,190)
    q(book,f,2);finish_space(book,'All solutions / no missing cases / where branches meet',110)
    start(book,f,2);q(book,f,3)
    y=book.y
    book.box(44,y,252,110,label='Both coordinates real')
    book.box(316,y,252,110,label='z real, w complex')
    book.y=y+122;lines(book,n=2)
    q(book,f,4);finish_space(book,'Without the origin / an exact route if the origin is allowed',150)
    start(book,f,3);q(book,f,5)
    work(book,153,'Product / inverse coordinate formulas / parameter restriction')
    q(book,f,6);finish_space(book,'Construct a pair / verify the equation / describe a continuous route',150)


def angle_machine_circle(book,y,height=135):
    cx,cy,r=165,y+height/2,52
    dial(book,cx,cy,r,'INPUT x = cos θ',spokes=90,angle_labels=False)
    for theta in (0,60,90,120,180):
        a=math.radians(theta);x=cx+r*math.cos(a);py=cy-r*math.sin(a)
        book.line(cx,cy,x,py,color=TEAL,width=.9)
        ly=cy-r+8 if theta==90 else cy-(r+18)*math.sin(a)-5
        book.label(str(theta)+'°',cx+(r+18)*math.cos(a),ly,size=9,align='center')
    book.box(300,y+2,268,height-4,label='My chosen tests and equations')
    book.y=y+height+12


def render_07(book,f):
    start(book,f,1);q(book,f,1);angle_machine_circle(book,book.y,148)
    work(book,48,'Candidate: P(x) =')
    q(book,f,2);finish_space(book,'A new test / equal-input check / limits of the evidence',95)
    start(book,f,2);q(book,f,3)
    work(book,157,'Build the first polynomials / justify the induction step')
    q(book,f,4);finish_space(book,'Why five tests pass / a failing input / the role of proof',160)
    start(book,f,3);q(book,f,5)
    y=book.y
    for x,txt in [(70,'input x'),(239,'first machine'),(422,'second machine')]:
        book.box(x,y+8,112,41,label=txt)
    book.arrow(182,y+29,229,y+29,color=TEAL)
    book.arrow(351,y+29,412,y+29,color=TEAL)
    book.y=y+63;work(book,94,'My expansion and the other order')
    q(book,f,6);finish_space(book,'First on the cosine interval / then as a polynomial identity',140)


def render_08(book,f):
    start(book,f,1);q(book,f,1);time_axes(book,book.y,130)
    work(book,92,'Exact checks for every t, including t = 0')
    q(book,f,2);finish_space(book,'One instantaneous slope / a complete solution check',85)
    start(book,f,2);q(book,f,3);time_axes(book,book.y,108)
    work(book,49,'My c and my piecewise formula')
    q(book,f,4)
    y=book.y;book.box(44,y,252,76,label='h < 0: difference quotient and limit')
    book.box(316,y,252,76,label='h > 0: difference quotient and limit')
    book.y=y+88
    q(book,f,5);finish_space(book,'Initial condition / signs before c / equation after c',64)
    start(book,f,3);q(book,f,6);work(book,167,'Sign of the derivative / possible zero times')
    q(book,f,7);finish_space(book,'Positive interval / chain rule / continuity at c / all cases',155)
    start(book,f,4);q(book,f,8);work(book,140,'Differentiate the product and use the initial value')
    q(book,f,9);finish_space(book,'Ratio near zero / negative-rate counterexample / logical conclusion',120)


RENDERERS={f'GA-{i:02}':fn for i,fn in enumerate((render_01,render_02,render_03,render_04,render_05,render_06,render_07,render_08),1)}


def render_students(book, family_id):
    RENDERERS[family_id](book,FAMILIES[family_id])
