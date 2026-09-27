"""Reviewed investigations GA18--24,27: custom diagrams and open workspaces."""
import math
from sheet import TEAL,NAVY,GRAY,LIGHT,PALE,INK,WHITE,BOLD
from common import start,question,blank,family_data

FAMILIES=family_data('ga3')
def q(b,f,n):return question(b,f,n)
def work(b,h=100,label=''):blank(b,height=h,label=label)
def finish(b,label='',minimum=70):
    h=730-b.y
    if h<minimum:raise ValueError(f'{b.family_id} p{b.page_no} workspace {h} < {minimum}')
    work(b,h,label)
def note(b,s):b.p(s,size=10.2,color=GRAY);b.y+=8

def axes(b,x,y,w,h,xr,yr,xt,yt,xlabel='x',ylabel='y',grid=True):
    def at(a,c):return x+(a-xr[0])*w/(xr[1]-xr[0]),y+h-(c-yr[0])*h/(yr[1]-yr[0])
    for a,s in xt:
        xx,_=at(a,0)
        if grid:b.line(xx,y,xx,y+h,color=LIGHT,width=.45)
        b.label(s,xx,y+h+4,size=8.5,align='center',color=GRAY)
    for c,s in yt:
        _,yy=at(0,c)
        if grid:b.line(x,yy,x+w,yy,color=LIGHT,width=.45)
        b.label(s,x-7,yy-5,size=8.5,align='right',color=GRAY)
    if yr[0]<=0<=yr[1]:b.arrow(*at(xr[0],0),*at(xr[1],0),color=GRAY,width=.8,head=4)
    if xr[0]<=0<=xr[1]:b.arrow(*at(0,yr[0]),*at(0,yr[1]),color=GRAY,width=.8,head=4)
    b.label(xlabel,x+w,y+h+20,size=9,align='right',color=GRAY)
    b.label(ylabel,x,y-17,size=9,color=GRAY)
    return at

def landscape(b,y,h=160):
    at=axes(b,76,y+19,468,h-52,(0,1),(-1,7),[(0,'0'),(1/3,'1/3'),(2/3,'2/3'),(1,'1')],[(-1,'−1'),(0,'0'),(3,'3'),(6,'6')],ylabel='f and my candidate c')
    b.line(*at(0,0),*at(2/3,0),color=TEAL,width=2)
    b.line(*at(2/3,6),*at(1,6),color=TEAL,width=2)
    b.circle(*at(2/3,0),3,fill=WHITE,stroke=TEAL,width=1.1)
    for pt in [(0,0),(2/3,6),(1,6)]:b.circle(*at(*pt),2.6,fill=TEAL,stroke=TEAL)
    b.y=y+h+10

def unit_axes(b,y,h=160):
    at=axes(b,78,y+20,462,h-53,(0,1),(0,1),[(0,'0'),(.25,'1/4'),(.5,'1/2'),(.75,'3/4'),(1,'1')],[(0,'0'),(.5,'1/2'),(1,'1')],ylabel='height (fixed scale)')
    b.y=y+h+10;return at

def journey(b,y,h=180,waypoint=False):
    at=axes(b,77,y+20,465,h-54,(0,3),(-3,9),[(i,str(i)) for i in range(4)],[(i,str(i)) for i in [-3,0,3,6,9]],xlabel='time t',ylabel='position y')
    for t,v in [(0,0),(3,6)]+([(1,4)] if waypoint else []):
        b.circle(*at(t,v),3,fill=TEAL,stroke=TEAL)
    b.y=y+h+10

def mirror(b,y,h=230,short=False,worked=False):
    # One numerical unit has identical horizontal and vertical physical length.
    unit=(h-44)/6;x=83+(11*30-11*unit)/2
    at=axes(b,x,y+15,11*unit,6*unit,(-4,7),(-2,4),[(i,str(i)) for i in [-4,-3,-2,0,2,4,5,6,7]],[(i,str(i)) for i in [-2,-1,0,1,3,4]],ylabel='equal coordinate scale')
    right=2 if short else 5
    b.line(*at(-3,0),*at(right,0),color=NAVY,width=3.5)
    for px in [-3,right]:b.circle(*at(px,0),2.5,fill=NAVY,stroke=NAVY)
    for name,pt in [('A',(-2,3)),('B',(6,1))]:
        xx,yy=at(*pt);b.circle(xx,yy,3,fill=TEAL,stroke=TEAL);b.label(name,xx+6,yy-15,size=10,font=BOLD)
    if worked:
        m=2 if short else 4
        b.poly([at(-2,3),at(m,0),at(6,1)],stroke=TEAL,width=1.7)
        b.line(*at(6,1),*at(6,-1),color=GRAY,width=.7,dash=[3,3])
        b.circle(*at(6,-1),3,fill=WHITE,stroke=TEAL)
        b.label('B′',at(6,-1)[0]+6,at(6,-1)[1]-4,size=10)
        b.line(*at(-2,3),*at(6,-1),color=GRAY,width=.8,dash=[3,3])
        b.circle(*at(m,0),3.5,fill=TEAL,stroke=TEAL)
        b.label('M = ('+str(m)+',0)',at(m,0)[0]-4,at(m,0)[1]+9,size=9,align='right')
    b.y=y+h+13

def peg_board(b,x,y,size,points=None,title=''):
    if title:b.label(title,x+size/2,y-20,size=10.5,font=BOLD,align='center',color=TEAL)
    at=axes(b,x,y,size,size,(0,6),(0,6),[(0,'0'),(3,'3'),(6,'6')],[(0,'0'),(3,'3'),(6,'6')])
    if points:
        for name,(u,v) in points.items():
            xx,yy=at(u,v);b.circle(xx,yy,3,fill=INK,stroke=INK)
            dx=6 if u<5 else -7;align='left' if dx>0 else 'right'
            dy=6 if v>=6 else (-17 if v else -18)
            b.label(name,xx+dx,yy+dy,size=10,font=BOLD,align=align)
    return at

def boards(b,y,size=124):
    f=FAMILIES['GA-22']
    peg_board(b,80,y+22,size,f['figures']['boards'][0],'Board I')
    peg_board(b,347,y+22,size,f['figures']['boards'][1],'Board II')
    b.y=y+size+59

def sphere(b,cx,cy,r=76,alpha=math.pi/2,variable=False):
    # Orthographic projection from the positive octant. Unit coordinate vectors
    # project into an orthonormal image plane; all three selected arcs are visible.
    def at(v):
        x,y,z=v
        return cx+r*(y-x)/math.sqrt(2),cy+r*(x+y-2*z)/math.sqrt(6)
    def path(fn):return [at(fn(math.pi*2*i/180)) for i in range(181)]
    b.circle(cx,cy,r,fill=None,stroke=LIGHT,width=.8)
    b.poly(path(lambda t:(math.cos(t),math.sin(t),0)),stroke=LIGHT,width=.8)
    b.poly(path(lambda t:(math.cos(t),0,math.sin(t))),stroke=LIGHT,width=.6)
    c,s=math.cos(alpha),math.sin(alpha)
    legs=[lambda t:(math.cos(alpha*t),math.sin(alpha*t),0),lambda t:(c*math.cos(math.pi*t/2),s*math.cos(math.pi*t/2),math.sin(math.pi*t/2)),lambda t:(math.sin(math.pi*t/2),0,math.cos(math.pi*t/2))]
    for fn in legs:
        b.poly([at(fn(i/70)) for i in range(71)],stroke=TEAL,width=1.7)
        b.arrow(*at(fn(.43)),*at(fn(.58)),color=TEAL,width=1.2,head=5)
    for name,vec,dx,dy in [('A',(1,0,0),-18,3),('B',(c,s,0),9,3),('C',(0,0,1),5,-20)]:
        xx,yy=at(vec);b.circle(xx,yy,3,fill=INK,stroke=INK);b.label(name,xx+dx,yy+dy,size=11,font=BOLD)
    if variable:b.label('schematic: longitude α',cx,cy+r+11,size=9,align='center',color=GRAY)
    return at

def shape(b,kind,cx,cy,s=1):
    if kind=='circle':b.circle(cx,cy,37*s,fill=None,stroke=TEAL,width=1.8)
    elif kind=='segment':
        b.line(cx-67*s,cy,cx+67*s,cy,color=TEAL,width=1.8)
        for px in [cx-67*s,cx+67*s]:b.circle(px,cy,2.5,fill=TEAL,stroke=TEAL)
    elif kind=='Y':
        for dx,dy in [(0,-41),(-36,36),(36,36)]:b.line(cx,cy,cx+dx*s,cy+dy*s,color=TEAL,width=1.8)
        b.circle(cx,cy,3,fill=INK,stroke=INK)
    elif kind in ['eight','two']:
        rad=26*s;sep=rad if kind=='eight' else 1.35*rad
        for cc in [cx-sep,cx+sep]:b.circle(cc,cy,rad,fill=None,stroke=TEAL,width=1.8)
        if kind=='eight':b.circle(cx,cy,3,fill=INK,stroke=INK)

def flood_grid(b,x,y,size,level=None,worked=False,title='',endpoints=True):
    if title:b.label(title,x+size/2,y-20,size=10.5,font=BOLD,align='center',color=TEAL)
    def at(a,c):return x+(a+1)*size/2,y+(1-c)*size/2
    if worked:
        if level<0:
            # Each lobe runs along its exact curved boundary and the square edge.
            limit=math.sqrt(1+level)
            for sign in [-1,1]:
                pts=[at(-limit+2*limit*i/120,sign*math.sqrt((-limit+2*limit*i/120)**2-level)) for i in range(121)]
                pts += [at(limit,sign),at(-limit,sign)]
                b.poly(pts,closed=True,fill=PALE,stroke=TEAL,width=1)
        elif level==0:
            for sign in [-1,1]:b.poly([at(0,0),at(-1,sign),at(1,sign)],closed=True,fill=PALE,stroke=TEAL,width=1)
        else:
            # Horizontal strips form one closed region; arcs meet the vertical edges.
            def edge(v):return min(1,math.sqrt(v*v+level))
            ys=[-1+2*i/160 for i in range(161)]
            pts=[at(-edge(v),v) for v in ys]+[at(edge(v),v) for v in reversed(ys)]
            b.poly(pts,closed=True,fill=PALE,stroke=TEAL,width=1)
    for v in [-1,-.5,0,.5,1]:
        b.line(*at(v,-1),*at(v,1),color=LIGHT,width=.45)
        b.line(*at(-1,v),*at(1,v),color=LIGHT,width=.45)
    b.box(x,y,size,size,stroke=GRAY,width=.8)
    b.line(*at(-1,0),*at(1,0),color=GRAY,width=.7)
    b.line(*at(0,-1),*at(0,1),color=GRAY,width=.7)
    for v,t in [(-1,'−1'),(0,'0'),(1,'1')]:b.label(t,at(v,-1)[0],y+size+4,size=8,align='center',color=GRAY)
    b.label('x',x+size+7,y+size/2-6,size=9,color=GRAY)
    b.label('y',x+size/2-17,y+5,size=9,color=GRAY)
    if endpoints:
        for name,py in [('U',y),('D',y+size)]:
            b.circle(x+size/2,py,2.4,fill=INK,stroke=INK)
            b.label(name,x+size/2+6,py-6 if name=='U' else py-17,size=9,font=BOLD)
    return at


def render_18(b,f):
    start(b,f,1);q(b,f,1);landscape(b,b.y,146)
    work(b,54,'My rule / candidates / exact comparison')
    q(b,f,2);finish(b,'A bound for every real c / all equality cases',85)
    start(b,f,2);q(b,f,3);work(b,195,'Absolute error: my cases, lower bound and every minimizer')
    q(b,f,4);finish(b,'Worst error: proof / all minimizers / repaired claim',165)
    start(b,f,3);q(b,f,5)
    b.table([['rule','minimizing height(s)','condition on p'],['Q','',''],['A','',''],['W','','']],widths=[55,255,214],row_height=38,size=10.5);b.y+=12
    work(b,96,'Why these cases are complete')
    q(b,f,6);finish(b,'My h / constructed width / uniqueness / absolute-loss comparison',100)


def render_19(b,f):
    start(b,f,1);q(b,f,1);work(b,140,'My ε,M / a,n / universal rule / supplied numerical target')
    q(b,f,2);unit_axes(b,b.y,152)
    finish(b,'My two n values / exact norms / what the drawing cannot prove',70)
    start(b,f,2);q(b,f,3);work(b,176,'Partner’s C / defeating polynomial / the quantifier argument')
    q(b,f,4);finish(b,'Uniform heights / derivative endpoint / comparison with g_n',185)
    start(b,f,3);q(b,f,5);work(b,167,'Sharp constant / possible equality / near-attaining inputs')
    q(b,f,6);finish(b,'Bound for all continuous inputs / an attaining input / comparison',140)


def render_20(b,f):
    start(b,f,1);q(b,f,1);journey(b,b.y,184)
    work(b,55,'My two speed pairs / exact bills / legal endpoint equation')
    q(b,f,2);finish(b,'Candidate / excess-cost certificate / uniqueness',100)
    start(b,f,2);q(b,f,3);work(b,128,'Any finite schedule / exact excess / equality conditions')
    q(b,f,4);journey(b,b.y,155,waypoint=True)
    finish(b,'New lower bound / attaining schedule / changed hypothesis',100)
    start(b,f,3);q(b,f,5);work(b,166,'Integral identity / equality on each piece / joins and endpoints')
    q(b,f,6);finish(b,'Effort of y_a / distance minimum / every attaining a / uniqueness',135)


def render_21(b,f):
    start(b,f,1);mirror(b,b.y,221)
    q(b,f,1);work(b,45,'Chosen contacts / lengths / conjecture')
    q(b,f,2);finish(b,'Exact F(m) / midpoint test / exact comparison',75)
    start(b,f,2);q(b,f,3);mirror(b,b.y,241)
    q(b,f,4);finish(b,'Lower bound / when equality holds / why the contact is unique',150)
    start(b,f,3);q(b,f,5);work(b,119,'Best legal contact / exact length / why the old bound is insufficient')
    q(b,f,6);finish(b,'Strict decrease and increase / constrained optimum / uniqueness',175)


def render_22(b,f):
    start(b,f,1);q(b,f,1)
    y=b.y;peg_board(b,74,y+5,96)
    b.box(222,y,346,123,label='My point choices / split / actual contact')
    b.y=y+135;q(b,f,2);boards(b,b.y,104)
    finish(b,'The two splits and why their hulls meet',50)
    start(b,f,2);q(b,f,3);work(b,226,'All board types / collinear cases / why the list is exhaustive')
    q(b,f,4);finish(b,'Coincident labels / a three-point counterexample / proof',165)
    start(b,f,3);q(b,f,5);boards(b,b.y,112)
    work(b,100,'Board I: exact crossing / two nonnegative weight systems')
    q(b,f,6);finish(b,'Board II: weights / signed relation / a signed-coefficient obstruction',100)


def render_23(b,f):
    start(b,f,1);q(b,f,1)
    y=b.y;sphere(b,153,y+84,71)
    b.box(272,y,296,174,label='My initial arrow / prediction / vectors at B,C,A')
    b.label('Arrows show route direction only.',65,y+163,size=9,color=GRAY)
    b.y=y+191;q(b,f,2);finish(b,'Retraced and reversed routes / my experiment / rule distinction',100)
    start(b,f,2);q(b,f,3)
    b.table([['initial arrow','at B / next-frame form','at C / next-frame form','back at A'],['+y','','',''],['+z','','','']],widths=[78,165,165,116],size=9.5,row_height=52);b.y+=12
    q(b,f,4);finish(b,'Every a,b / length / signed angle / inverse and retracing proofs',135)
    start(b,f,3);q(b,f,5);work(b,176,'Transport +y / transport +z / combine for arbitrary a,b')
    q(b,f,6);finish(b,'My α and vector / π/3 test / norm / fixed-vector obstruction',130)
    start(b,f,4);q(b,f,7)
    y=b.y;sphere(b,143,y+82,70,alpha=math.pi/3,variable=True)
    b.box(264,y,304,176,label='Lune area / northern half / proved rotation / scope')
    b.y=y+188;q(b,f,8);finish(b,'Tangency test / a restoring route / what curvature alone does not force',150)


def render_24(b,f):
    start(b,f,1);q(b,f,1)
    y=b.y
    for kind,cx,title in [('circle',163,'circle'),('segment',424,'closed segment')]:
        shape(b,kind,cx,y+45);b.label(title,cx,y+90,size=10,align='center',color=GRAY)
    b.y=y+113;q(b,f,2)
    y=b.y
    for kind,cx,title in [('Y',132,'Y: center joined'),('eight',307,'figure-eight: joined'),('two',483,'two separate loops')]:
        shape(b,kind,cx,y+46,.95);b.label(title,cx,y+91,size=9.5,align='center',color=GRAY)
    b.y=y+116;finish(b,'My punctures / remaining pieces / all possible cases',65)
    start(b,f,2);q(b,f,3);work(b,201,'Strategic point / matched puncture / connectedness argument')
    q(b,f,4);finish(b,'Y / figure-eight / two loops: the invariant and contradiction',185)
    start(b,f,3);q(b,f,5);work(b,155,'Candidate maps / repeated images / failed homeomorphism condition')
    q(b,f,6)
    y=b.y
    shape(b,'circle',154,y+49,35/37)
    pts=[(430+70*math.cos(2*math.pi*i/160),y+49-35*math.sin(2*math.pi*i/160)) for i in range(161)]
    b.poly(pts,stroke=TEAL,width=1.8)
    b.label('unit circle',154,y+90,size=10,align='center',color=GRAY)
    b.label('ellipse: horizontal semiaxis 2',430,y+90,size=10,align='center',color=GRAY)
    b.label('Both pictures use the same coordinate scale.',44,y+112,size=9,color=GRAY)
    b.y=y+133;finish(b,'My map / inverse / both compositions / continuity',105)


def render_27(b,f):
    start(b,f,1);q(b,f,1)
    y=b.y
    for x,level in [(63,'−1/4'),(241,'0'),(419,'1/4')]:flood_grid(b,x,y+25,125,title='c = '+level)
    b.y=y+181
    work(b,52,'My extra levels / tested points / boundary inequalities')
    q(b,f,2);finish(b,'Common levels: routes or all-route obstructions / first joining',110)
    start(b,f,2);q(b,f,3);work(b,208,'All real levels / endpoints / paths within every claimed component')
    q(b,f,4)
    y=b.y;flood_grid(b,66,y+23,143,title='My forced crossing')
    b.box(248,y,320,188,label='Chosen a / lower bound / legal attaining route')
    b.y=y+200
    if b.y<685:finish(b,'Boundary choices a=0 and a=±1',35)
    start(b,f,3);q(b,f,5)
    b.table([['function','critical point(s) / Hessian','event near zero'],['x²−y²','',''],['x²+y²','','']],widths=[88,252,184],row_height=49,size=10);b.y+=12
    work(b,69,'Nondegeneracy / index / justification of the component event')
    q(b,f,6);finish(b,'Exact zero-level comparison / gradient and Hessian / theorem hypothesis',145)

RENDERERS={'GA-18':render_18,'GA-19':render_19,'GA-20':render_20,'GA-21':render_21,'GA-22':render_22,'GA-23':render_23,'GA-24':render_24,'GA-27':render_27}
def render_students(book,family_id):RENDERERS[family_id](book,FAMILIES[family_id])

def render_key_figures(b,fid):
    if fid=='GA-21':
        b.new_page(fid,'Worked mirror contacts',FAMILIES[fid]['title'],part='facilitator figures')
        b.p('Full mirror: the reflected straight segment crosses at m=4. Equality in the triangle inequality gives the unique minimum 4√5.',size=11);b.y+=12
        mirror(b,b.y,227,worked=True)
        b.p('Short mirror: the same reflected crossing is unavailable. Strict decrease to m=4 makes the legal endpoint m=2 uniquely best, with length 5+√17.',size=11);b.y+=12
        mirror(b,b.y,227,short=True,worked=True)
    elif fid=='GA-23':
        b.new_page(fid,'Worked transport ledger',FAMILIES[fid]['title'],part='facilitator figure')
        b.p('This page contains return directions. Keep it out of the launch. Coordinate directions are ambient x,y,z; a corner changes the frame, not the arriving vector.',size=11);b.y+=12
        b.table([['start at A','after AB, at B','after BC, at C','after CA, at A'],['+y','−x = −N_BC','−x = −T_CA','+z'],['+z','+z = T_BC','−y = −N_CA','−y']],widths=[90,148,148,138],size=11,row_height=43);b.y+=25
        b.p('Thus a·y+b·z returns as −b·y+a·z: a +π/2 rotation in the tangent plane, preserving a²+b².',size=11);b.y+=15
        y=b.y;sphere(b,153,y+93,81)
        b.box(282,y+10,286,180,label='A’s tangent plane: worked basis returns')
        cx,cy=414,y+107
        b.arrow(cx-95,cy,cx+98,cy,color=GRAY,width=.8)
        b.arrow(cx,cy+66,cx,cy-70,color=GRAY,width=.8)
        b.label('+y',cx+91,cy+8,size=10);b.label('+z',cx+6,cy-75,size=10)
        b.arrow(cx,cy,cx,cy-58,color=TEAL,width=2,head=7)
        b.arrow(cx,cy,cx-75,cy,color=NAVY,width=2,head=7)
        b.label('start +y → +z',292,y+158,size=9,color=TEAL)
        b.label('start +z → −y',431,y+158,size=9,color=NAVY)
        b.y=y+212
        b.p('For longitude α, the same calculation gives (a cos α−b sin α)·y+(a sin α+b cos α)·z. The triangle area is α: half a lune of area 2α. This calculation proves the relation for this family, not the general Gauss–Bonnet theorem.',size=11)
    elif fid=='GA-27':
        b.new_page(fid,'Worked wet regions and barrier route',FAMILIES[fid]['title'],part='facilitator figure')
        b.p('Shading includes its boundary. All regions are clipped to the closed square. The touching point at zero is retained, so the two wedges form one connected set.',size=11);b.y+=22
        y=b.y
        for x,c,label in [(63,-.25,'−1/4'),(241,0,'0'),(419,.25,'1/4')]:flood_grid(b,x,y+24,125,level=c,worked=True,title='c = '+label)
        b.y=y+185
        b.p('For c<0, wet points of one sign of y connect vertically to the corresponding square edge and then along that edge. For c≥0, radial contraction to the origin stays wet because f(rp)=r²f(p). At c=−1 only U,D remain; below −1 nothing is wet. At c≥1 the whole square is wet.',size=11);b.y+=22
        y=b.y;at=flood_grid(b,84,y+25,181,title='Example: forced a=1/2')
        b.poly([at(0,1),at(.5,1),at(.5,-1),at(0,-1)],stroke=TEAL,width=2)
        b.circle(*at(.5,0),3,fill=INK,stroke=INK)
        b.label('(a,0)',at(.5,0)[0]+6,at(.5,0)[1]-5,size=9)
        b.p('The crossing forces c≥a². The top-edge / vertical / bottom-edge route attains c=a²: edge heights are at most 0 and vertical heights are a²−y²≤a². This remains legal at a=0 and a=±1.',x=318,y=y+30,width=250,size=11)
        b.y=y+235
