"""Custom student diagrams and workspaces for GA-09,10,12--17."""
import math
from sheet import TEAL, NAVY, GRAY, LIGHT, PALE, INK, WHITE, BOLD
from common import start, question, blank, lines, family_data

FAMILIES=family_data('ga2')


def q(book,f,n):return question(book,f,n)
def work(book,height=100,label=''):blank(book,height=height,label=label)
def finish(book,label='',minimum=65):
    height=730-book.y
    if height<minimum:raise ValueError(f'{book.family_id} final work area too short: {height}')
    work(book,height,label)
def note(book,text):
    book.p(text,size=10.2,color=GRAY);book.y+=8


def axes(book,x,y,w,h,xrange,yrange,xticks,yticks,xlabel='x',ylabel='y'):
    xmin,xmax=xrange;ymin,ymax=yrange
    def at(a,b):return (x+(a-xmin)*w/(xmax-xmin),y+h-(b-ymin)*h/(ymax-ymin))
    for value,label in xticks:
        px,_=at(value,0);book.line(px,y,px,y+h,color=LIGHT,width=.4)
        book.label(label,px,y+h+4,size=8.5,align='center',color=GRAY)
    for value,label in yticks:
        _,py=at(0,value);book.line(x,py,x+w,py,color=LIGHT,width=.4)
        book.label(label,x-8,py-5,size=8.5,align='right',color=GRAY)
    if ymin<=0<=ymax:
        book.arrow(*at(xmin,0),*at(xmax,0),color=GRAY,head=4,width=.8)
    if xmin<=0<=xmax:
        book.arrow(*at(0,ymin),*at(0,ymax),color=GRAY,head=4,width=.8)
    book.label(xlabel,x+w,y+h+21,size=9,align='right',color=GRAY)
    book.label(ylabel,x,y-17,size=9,color=GRAY)
    return at


def curve(book,at,func,left,right,color=TEAL,width=1.5,steps=200):
    points=[at(left+(right-left)*i/steps,func(left+(right-left)*i/steps)) for i in range(steps+1)]
    book.poly(points,stroke=color,width=width)


def wave_axis(book,y,height=135,fixed=False,initial=True):
    # Horizontal numerical coordinates are multiples of pi; labels say x.
    xr=(0,1) if fixed else (-1,3)
    ticks=([(0,'0'),(.25,'π/4'),(.5,'π/2'),(.75,'3π/4'),(1,'π')] if fixed else
           [(-1,'−π'),(0,'0'),(.5,'π/2'),(1,'π'),(1.5,'3π/2'),(2,'2π'),(3,'3π')])
    at=axes(book,70,y+21,478,height-55,xr,(-2,2),ticks,[(-2,'−2'),(-1,'−1'),(0,'0'),(1,'1'),(2,'2')],ylabel='profile height')
    if initial:curve(book,at,lambda x:math.sin(math.pi*x),*xr,width=1.3)
    if fixed:
        for x in (0,1):book.circle(*at(x,0),3,fill=TEAL,stroke=TEAL)
    book.y=y+height+12


def parabola(book,y,height=210,shifted=False):
    xr=(1,3) if shifted else (-1,1);yr=(0,10) if shifted else (-.5,1.5)
    xt=([(1,'1'),(1.5,'1.5'),(2,'2'),(2.5,'2.5'),(3,'3')] if shifted else
        [(-1,'−1'),(-.5,'−1/2'),(0,'0'),(.5,'1/2'),(1,'1')])
    yt=([(0,'0'),(2,'2'),(4,'4'),(6,'6'),(8,'8'),(10,'10')] if shifted else
        [(-.5,'−1/2'),(0,'0'),(.5,'1/2'),(1,'1'),(1.5,'3/2')])
    at=axes(book,83,y+19,457,height-56,xr,yr,xt,yt,ylabel='height')
    curve(book,at,lambda x:x*x,*xr)
    book.y=y+height+12


def orbit_line(book,y,label='Exact states and current-half labels',height=88):
    book.box(44,y,524,height,label=label)
    book.y=y+height+12


def tent_graph(book,y,height=138):
    size=height-26
    at=axes(book,81,y+10,size,size,(0,1),(0,1),[(0,'0'),(.5,'1/2'),(1,'1')],[(0,'0'),(.5,'1/2'),(1,'1')],xlabel='current x',ylabel='T(x)')
    book.poly([at(0,0),at(.5,1),at(1,0)],stroke=TEAL,width=1.6)
    book.line(*at(0,0),*at(1,1),color=LIGHT,width=.8,dash=[3,3])
    book.box(285,y+4,283,height-1,label='My chosen four-letter program')
    for j in range(4):book.box(307+57*j,y+38,40,35,stroke=GRAY)
    book.label('Current half, before each update',297,y+92,size=9,color=GRAY)
    book.y=y+height+27


def inverse_cards(book):
    y=book.y
    for x,label,formula in [(44,'L','y/2'),(316,'R','1−y/2')]:
        book.box(x,y,252,48,fill=PALE,stroke=LIGHT)
        book.label(label,x+18,y+14,size=14,font=BOLD,color=TEAL)
        book.label(formula,x+82,y+13,size=15)
    book.y=y+60


def circle_dial(book,cx,cy,r,title,initial=False):
    book.label(title,cx,cy-r-22,size=11,font=BOLD,align='center',color=TEAL)
    book.circle(cx,cy,r,stroke=GRAY,width=.8)
    book.line(cx-r,cy,cx+r,cy,color=LIGHT,width=.6)
    book.line(cx,cy-r,cx,cy+r,color=LIGHT,width=.6)
    book.label('up',cx,cy-r+6,size=8,align='center',color=GRAY)
    book.label('right',cx+r+4,cy-5,size=8,color=GRAY)
    book.circle(cx,cy,2,fill=INK)
    if initial:book.arrow(cx,cy,cx+r,cy,color=TEAL,width=1.5)


def pair_dials(book,y,height=120,initial=False):
    r=(height-38)/2
    for cx,title in [(169,'k = 1'),(433,'k = 5')]:circle_dial(book,cx,y+height/2+3,r,title,initial)
    book.y=y+height+12


def grid_picture(book,x,y,size,values=None,title='',coordinates=False):
    if title:book.label(title,x+size/2,y-20,size=10.5,font=BOLD,align='center',color=TEAL)
    book.grid(x,y,size,size,2,2)
    if values is not None:
        for i,value in enumerate(values):
            px=x+(i%2+.5)*size/2;py=y+(i//2+.5)*size/2-7
            book.label(value,px,py,size=13,align='center')
    if coordinates:
        for i,value in enumerate(['00','01','10','11']):
            book.label(value,x+(i%2)*size/2+4,y+(i//2)*size/2+3,size=8,color=GRAY)


def sign_cards(book,y):
    for i,(name,values) in enumerate(FAMILIES['GA-15']['figures']['cards'].items()):
        grid_picture(book,65+i*130,y+20,66,['+' if v==1 else '−' for v in values],name)
    book.y=y+100


def overlap_axes(book,y,height=155,worked=False):
    at=axes(book,73,y+20,475,height-55,(-1,6),(0,3),[(i,str(i)) for i in range(-1,7)],[(i,str(i)) for i in range(4)],xlabel='right endpoint t',ylabel='overlap h(t)')
    if worked:book.poly([at(-1,0),at(0,0),at(2,2),at(3,2),at(5,0),at(6,0)],stroke=TEAL,width=1.7)
    book.y=y+height+12


def cut_windows(book,y):
    # Exact common scale: 72 points = one inch = one unit.
    book.label('Cut/trace the windows; 1 unit = 1 inch',44,y,size=9,color=GRAY)
    for x,length,title,left_label,right_label in [(60,3,'fixed','0','3'),(366,2,'moving','t−2','t')]:
        by=y+32;w=72*length
        book.box(x,by,w,29,fill=PALE,stroke=GRAY)
        book.label(title,x+w/2,y+14,size=9,font=BOLD,align='center',color=TEAL)
        for i in range(1,length):book.line(x+72*i,by,x+72*i,by+29,color=LIGHT,width=.7)
        book.label(left_label,x,by+33,size=9,align='center')
        book.label(right_label,x+w,by+33,size=9,align='center')
    by=y+103
    book.line(54,by,558,by,color=GRAY,width=.8)
    for i in range(8):
        x=54+i*72;book.line(x,by-4,x,by+4,color=GRAY,width=.7)
        book.label(i-1,x,by+7,size=9,align='center')
    book.y=by+31


def forcing_graphs(book,y,height=134):
    for i,(title,func) in enumerate([('f(x) = x²',lambda x:x*x),('f(x) = 2x−1',lambda x:2*x-1)]):
        x=73+i*269
        at=axes(book,x,y+28,207,height-63,(0,1),(-1,2),[(0,'0'),(.5,'1/2'),(1,'1')],[(-1,'−1'),(0,'0'),(1,'1'),(2,'2')],ylabel=title)
        curve(book,at,func,0,1)
    book.y=y+height+12


def render_09(book,f):
    start(book,f,1);q(book,f,1)
    wave_axis(book,book.y,146)
    note(book,'Teal curve: initial sin x. My choices: c = ______   a = ______. Add later profiles.')
    q(book,f,2);finish(book,'Derivatives / legal parameters / counterexamples',115)
    start(book,f,2);q(book,f,3)
    wave_axis(book,book.y,146,fixed=True)
    note(book,'Initial shape shown. My b values: ______ and ______. Add and label later profiles.')
    work(book,60,'Wave law / boundary check / initial data')
    q(book,f,4);finish(book,'Match the initial velocity / choose a later observation',120)
    start(book,f,3);q(book,f,5);work(book,131,'My k / time factors / derivative comparison')
    q(book,f,6);wave_axis(book,book.y,140,fixed=True,initial=False)
    finish(book,'My nonzero d / two evolutions / scalar-multiple test',95)


def render_10(book,f):
    start(book,f,1);tent_graph(book,book.y,124)
    q(book,f,1);orbit_line(book,book.y,height=75)
    q(book,f,2);finish(book,'Boundary trajectories / periodic-orbit explanation',80)
    start(book,f,2);inverse_cards(book)
    q(book,f,3);work(book,143,'My inverse composition / fixed point / forward verification')
    q(book,f,4);finish(book,'Programs / exact states / first returns',120)
    start(book,f,3);q(book,f,5);work(book,225,'Open cycle inventory / how I avoid repeats')
    q(book,f,6);finish(book,'Correct the count and explain what is being counted',100)
    start(book,f,4);q(book,f,7);work(book,235,'Existence in [0,1] / forward labels / distinct starting points')
    q(book,f,8);finish(book,'Least period argument / completeness of the inventory',100)


def render_12(book,f):
    start(book,f,1);q(book,f,1)
    y=book.y
    for x,label in [(44,'My target below 2'),(316,'My target above 2')]:book.box(x,y,252,108,label=label)
    book.y=y+120
    q(book,f,2)
    y=book.y+20;left=66;scale=230
    paid=0
    for j in range(5):
        amount=2**(-j);w=amount*scale
        book.box(left+paid*scale,y,w,31,fill=PALE,stroke=GRAY)
        if j<4:book.label('1' if j==0 else '1/'+str(2**j),left+(paid+amount/2)*scale,y+9,size=9,align='center')
        paid+=amount
    book.box(left+paid*scale,y,(2-paid)*scale,31,stroke=GRAY)
    for val in [0,1,2]:book.label(val,left+val*scale,y+36,size=9,align='center')
    book.y=y+60;finish(book,'Finite formula / gap / my ε / strict accuracy test',120)
    start(book,f,2);q(book,f,3)
    y=book.y
    for i in range(16):
        x=44+(i%4)*133;py=y+(i//4)*33
        book.box(x,py,125,29,stroke=GRAY)
        book.label('1' if i==0 else '1/'+str(i+1),x+62.5,py+8,align='center',size=11)
    book.y=y+144;work(book,64,'My grouping and strict inequality')
    q(book,f,4);finish(book,'Partner’s B / stopping rule / why it always works',115)
    start(book,f,3);q(book,f,5);work(book,199,'Start after any N / groups / extra budget / comparison with G')
    q(book,f,6);finish(book,'An infinite selection / its finite budget / why this changes the rule',120)


def render_13(book,f):
    start(book,f,1);q(book,f,1);parabola(book,book.y,218)
    q(book,f,2);finish(book,'Endpoint line / an interior challenge / whole-interval error',100)
    start(book,f,2);q(book,f,3)
    book.table([['x','signed residual x²−(ax+b)','consequence of budget E'],['−1','',''],['0','',''],['1','','']],widths=[45,246,233],size=10,row_height=29)
    book.y+=12;work(book,100,'Lower bound / attaining line / verification for every x')
    q(book,f,4);finish(book,'Equality conditions and uniqueness',115)
    start(book,f,3);q(book,f,5);parabola(book,book.y,170,shifted=True)
    note(book,'The test graph is x² on [1,3]. My general interval: h = ______, r = ______ > 0.')
    q(book,f,6);finish(book,'5–6: general certificate / endpoint secant / whole residual range',110)


def render_14(book,f):
    start(book,f,1);pair_dials(book,book.y,97,initial=True)
    q(book,f,1)
    book.table([['t','tip: k=1','tip: k=5','height: k=1','height: k=5'],['0','','','',''],['1/4','','','',''],['1/2','','','',''],['3/4','','','','']],widths=[48,119,119,119,119],size=9.5,row_height=27)
    book.y+=12;q(book,f,2);finish(book,'Another scheduled time / proof for every integer n',75)
    start(book,f,2);q(book,f,3);pair_dials(book,book.y,122)
    work(book,64,'My extra time / two heights / an extra time that fails')
    q(book,f,4);finish(book,'All integer frequencies / necessity / sufficiency / extra photograph',120)
    start(book,f,3);q(book,f,5);work(book,191,'Height record / full-arrow record / which frequencies survive?')
    q(book,f,6);finish(book,'A second continuous signal / matching measurements / why it is different',150)


def render_15(book,f):
    start(book,f,1);sign_cards(book,book.y)
    q(book,f,1)
    y=book.y+15;grid_picture(book,52,y,80,coordinates=True)
    book.box(158,y-2,410,88,label='My weights / partner’s reconstruction')
    book.y=y+101
    q(book,f,2)
    y=book.y+16;grid_picture(book,52,y,82,[5,0,1,2],title='Supplied picture')
    book.box(158,y-3,410,730-(y-3),label='Weights / verify every square')
    book.y=742
    start(book,f,2);q(book,f,3)
    y=book.y+18;grid_picture(book,60,y,92,coordinates=True,title='Detector signs')
    book.box(179,y-2,389,118,label='What my detector does to each card / scale')
    book.y=y+129
    q(book,f,4);finish(book,'Arbitrary entries / reconstruction / uniqueness',160)
    start(book,f,3);q(book,f,5)
    y=book.y+22;grid_picture(book,66,y,88,[5,0,1,2],title='Before')
    grid_picture(book,218,y,88,title='My chosen swap')
    book.box(348,y-3,220,111,label='Coefficient prediction / why')
    book.y=y+124
    q(book,f,6);finish(book,'Every allowed nonnegative picture / extra readings',140)


def render_16(book,f):
    start(book,f,1);q(book,f,1);cut_windows(book,book.y)
    overlap_axes(book,book.y,143)
    q(book,f,2);finish(book,'Endpoint cases / full formula / check every join',80)
    start(book,f,2);q(book,f,3);work(book,192,'My widths / all endpoint cases / swapping the roles')
    q(book,f,4);finish(book,'My S and H / existence condition / every ordered pair',155)
    start(book,f,3);q(book,f,5);work(book,180,'Indicator inequalities / window location / endpoint convention')
    q(book,f,6);finish(book,'Area pieces / all positive a,b / information preserved',155)


def render_17(book,f):
    start(book,f,1);forcing_graphs(book,book.y,132)
    q(book,f,1);work(book,100,'My f and λ / predicted outcomes / candidate shift and actual mean')
    q(book,f,2);finish(book,'A necessary scalar equation / an impossibility certificate',100)
    start(book,f,2);q(book,f,3);work(book,195,'Critical case / necessity / construction / every solution')
    q(book,f,4);finish(book,'All other dials / direct verification / uniqueness',165)
    start(book,f,3);q(book,f,5);work(book,138,'Choose the adjustment / all solutions / a nonzero perturbation')
    q(book,f,6)
    book.table([['ε','δ','solution difference'],['1/100','1/10',''],['1/100','1/100','']],widths=[95,95,334],size=10.5,row_height=30)
    book.y+=12;finish(book,'General difference / exact tolerance condition',115)


RENDERERS={'GA-09':render_09,'GA-10':render_10,'GA-12':render_12,'GA-13':render_13,
           'GA-14':render_14,'GA-15':render_15,'GA-16':render_16,'GA-17':render_17}

def render_students(book,family_id):RENDERERS[family_id](book,FAMILIES[family_id])


def render_key_figures(book,family_id):
    if family_id!='GA-16':return
    book.new_page(family_id,'Worked overlap graphs',FAMILIES[family_id]['title'],part='facilitator figure')
    book.p('The 3-by-2 windows: the parameter t is the moving right endpoint. The graph below is a solution figure; keep it out of the student launch.',size=11)
    book.y+=17;overlap_axes(book,book.y,195,worked=True)
    book.p('Corners at t=0,2,3,5; peak 2. Two triangular areas of 2 and a plateau area of 2 give total area 6.',size=11);book.y+=28
    y=book.y
    at=axes(book,73,y+20,475,143,(-.5,3.5),(0,1),[(i,str(i)) for i in range(4)],[(0,'0'),(.25,'1/4'),(.5,'1/2'),(.75,'3/4'),(1,'1')],xlabel='t',ylabel='three unit windows: k(t)')
    def triple(t):
        if t<=0 or t>=3:return 0
        if t<=1:return t*t/2
        if t<=2:return (-2*t*t+6*t-3)/2
        return (3-t)**2/2
    curve(book,at,triple,-.5,3.5,steps=240)
    book.y=y+203
    book.p('The third-window graph joins with matching value and first derivative at 0,1,2,3. Its second derivative jumps there. The peak is 3/4 at t=3/2.',size=11)
