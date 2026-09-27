"""GA-26/29/25: explicit knot, interval and planar-maze worksheet drawings."""
from fractions import Fraction
from html import escape
import math
from sheet import data, INK, GRAY, LIGHT, PALE, TEAL, NAVY, WHITE, BOLD, FONT
from reportlab.lib import colors

D=data('geometry-data.json')
FAMILIES={f['id']:f for f in D['families']}
FIG=D['diagrams']
CODES={0:colors.HexColor('#B8493E'),1:colors.HexColor('#2F6FA2'),2:colors.HexColor('#408B53')}


def txt(b,s,y,x=44,w=524,size=11.8):return b.p(s,x=x,y=y,width=w,size=size,leading=size*1.3)
def head(b,s,y):return b.h(s,y=y,size=13.5)
def space(b,y,h=65,label='My explanation',x=44,w=524):b.box(x,y,w,h,label=label)
def prompt(b,no,s,y,x=44,w=524):return txt(b,f'{no}.  {s}',y,x,w)
def grid(b,x,y,step=70,kept=None,ghost=False,faces=False):
    vs={c:(x+(i%3)*step,y+(i//3)*step)for i,c in enumerate('ABCDEFGHI')}
    es=FIG['grid_full']['edges']
    for e in es:
        if kept is None or e in kept:b.line(*vs[e[0]],*vs[e[1]],color=INK,width=2.1)
        elif ghost:b.line(*vs[e[0]],*vs[e[1]],color=LIGHT,width=.6,dash=[2,3])
    for c,(px,py)in vs.items():
        b.circle(px,py,4.8,fill=WHITE,stroke=INK,width=1.4)
        # Labels offset to avoid intersecting roads, especially the central room.
        b.label(c,px-10,py-16,size=10.5,font=BOLD,color=NAVY)
    if faces:
        for name,dx,dy in [('NW',.5,.5),('NE',1.5,.5),('SW',.5,1.5),('SE',1.5,1.5)]:
            b.label(name,x+dx*step,y+dy*step-6,size=11,align='center',color=GRAY)
        b.label('OUTSIDE',x+step,y+2*step+23,size=10.5,align='center',color=TEAL)
    return vs

def dual(b,x,y,step=64,edges=None):
    vs={'NW':(x,y),'NE':(x+2*step,y),'SW':(x,y+step),'SE':(x+2*step,y+step),'OUT':(x+step,y+2*step)}
    for a,c in edges or []:
        if (a,c)==('NE','OUT'):
            nx,ny=vs[a];ox,oy=vs[c]
            b.poly([(nx,ny),(nx+28,ny+22),(nx+28,oy),(ox,oy)],stroke=TEAL,width=2)
        else:b.line(*vs[a],*vs[c],color=TEAL,width=2)
    for name,(px,py)in vs.items():
        b.circle(px,py,12,fill=WHITE,stroke=TEAL)
        b.label(name,px,py-5.5,size=9.5,align='center',font=BOLD)
    return vs

def braid(b,cx,y,width=180,height=None,word=None,strands=2,closed=False,cap='',start=False,colored=None):
    """Trace exact straight-line braid slabs; white halo redraws only the overpass."""
    word=word if word is not None else [(0,1)]*3
    n=len(word)
    h=height or (width*.81 if closed else width*.72)
    total_h=h
    if closed:
        scale_x=width/4; scale_y=h/3.6
        def pos(a,j):return cx+a*scale_x,y+(.3+j)*scale_y
        xs=[-1,1]; slabs=3
    else:
        scale_x=width/max(1,strands-1); scale_y=h/max(1,n)
        xs=[i-(strands-1)/2 for i in range(strands)];slabs=n or 1
        def pos(a,j):return cx+a*scale_x,y+j*scale_y
    if cap:b.label(cap,cx,y-25,size=12,font=BOLD,align='center')
    state=list(colored)if colored is not None else None
    initial=state.copy()if state else None
    crosses=[]
    for j,(g,sgn)in enumerate(word):
        # color by input/output sections, split the underpass at the crossing
        old=state.copy()if state else None
        if state:
            a,c=state[g:g+2]
            state[g:g+2]=[(2*a-c)%3,a]if sgn==1 else[c,(2*c-a)%3]
        for k,a in enumerate(xs):
            kk=g+1 if k==g else g if k==g+1 else k
            p=pos(a,j);q=pos(xs[kk],j+1)
            if k in [g,g+1]:
                mid=((p[0]+q[0])/2,(p[1]+q[1])/2)
                over=(k==g and sgn==1)or(k==g+1 and sgn==-1)
                if over:crosses.append((p,q))
                if old is not None:
                    b.line(*p,*mid,color=CODES[old[k]],width=3.2)
                    b.line(*mid,*q,color=CODES[state[kk]],width=3.2)
                else:b.line(*p,*q,color=GRAY,width=2.7)
            else:b.line(*p,*q,color=CODES[old[k]]if old else GRAY,width=2.7)
        p=pos(xs[g],j);q=pos(xs[g+1],j+1)
        if sgn==-1:p,q=pos(xs[g+1],j),pos(xs[g],j+1)
        # A short white halo across the overpass opens a genuine gap below it.
        mx,my=(p[0]+q[0])/2,(p[1]+q[1])/2
        dx,dy=q[0]-p[0],q[1]-p[1];length=math.hypot(dx,dy);ux,uy=dx/length,dy/length
        pa=(mx-9*ux,my-9*uy);qa=(mx+9*ux,my+9*uy)
        b.line(*pa,*qa,color=WHITE,width=9)
        over_col=old[g if sgn==1 else g+1]if old is not None else None
        b.line(*pa,*qa,color=CODES[over_col]if over_col is not None else GRAY,width=2.7 if old is None else 3.2)
    if not word:
        for k,a in enumerate(xs):b.line(*pos(a,0),*pos(a,1),color=CODES[state[k]]if state else GRAY,width=2.7)
    if closed:
        for side,k in [(-1,0),(1,1)]:
            points=[pos(side,0),pos(2*side,-.3),pos(2*side,3.3),pos(side,3)]
            b.poly(points,stroke=CODES[initial[k]]if initial else GRAY,width=2.7)
        if start:
            dot=pos(-2,1.5);b.circle(*dot,r=4,fill=INK,stroke=INK)
            b.label('start',dot[0]-6,dot[1]-24,size=9,align='right',color=INK)
    else:
        for k,a in enumerate(xs):
            if initial is not None:
                b.label('RBG'[initial[k]],*pos(a,-.15),size=11,font=BOLD,align='center')
                px,py=pos(a,slabs+.08);b.label('RBG'[state[k]],px,py,size=11,font=BOLD,align='center')
    return total_h

def curl(b,x,y,w=150,h=80,color=None):
    pts=[[-2,-1],[-1,-1],[1,1],[0,2],[-1,1],[1,-1],[2,-1]]
    p=lambda a:(x+(a[0]+2)*w/4,y+(2-a[1])*h/3)
    b.poly([p(a)for a in pts],stroke=CODES[color]if color is not None else GRAY,width=2.7)
    # overpass from(-1,-1)to(1,1)
    a,c=p([-.30,-.30]),p([.30,.30]);b.line(*a,*c,color=WHITE,width=9);b.line(*a,*c,color=CODES[color]if color is not None else GRAY,width=2.7)

def cross_example(b,cx,y,colors_3,cap):
    # over is rising diagonal on printed page; letters identify all three sections.
    over,under_left,under_right=colors_3
    b.line(cx-26,y-19,cx+26,y+19,color=GRAY,width=2.7)
    b.line(cx-26,y+19,cx+26,y-19,color=GRAY,width=2.7)
    b.line(cx-10,y+7.3,cx+10,y-7.3,color=WHITE,width=9)
    b.line(cx-10,y+7.3,cx+10,y-7.3,color=GRAY,width=2.7)
    b.label(over,cx-36,y+15,size=11,font=BOLD)
    b.label(under_left,cx-36,y-31,size=11,font=BOLD)
    b.label(under_right,cx+32,y+15,size=11,font=BOLD)
    b.label(cap,cx,y+35,size=10.5,align='center')

def numberline(b,y,stage=None,x=65,w=485,labels=True,caption='',blank=False):
    st=stage
    if st is None:intervals=[(0,81)]
    else:intervals=[tuple(map(Fraction,ab))for ab in data('geometry-checks-results.json')['cantor']['stages'][st]['intervals']]
    xx=lambda v:x+float(v)*w/81
    if blank:
        b.line(x,y,x+w,y,color=LIGHT,width=3)
    else:
        for a,c in intervals:
            b.line(xx(a),y,xx(c),y,color=INK,width=3)
            b.circle(xx(a),y,1.8,fill=INK,stroke=INK,width=.3)
            b.circle(xx(c),y,1.8,fill=INK,stroke=INK,width=.3)
    if labels:
        for v in range(0,82,9):
            b.line(xx(v),y-5,xx(v),y+5,color=GRAY,width=.5)
            b.label(str(v),xx(v),y+9,size=9,align='center',color=GRAY)
    if caption:b.label(caption,x,y-22,size=10.5,font=BOLD)

def address_tree(b,y=190):
    left,right=58,554
    prev=[(306,y)]
    b.circle(306,y,3,fill=INK,stroke=INK)
    for level in range(1,5):
        pts=[]
        count=2**level;step=(right-left)/count
        for i in range(count):
            px=left+(i+.5)*step;py=y+level*29
            parent=prev[i//2];b.line(*parent,px,py,color=LIGHT,width=.9)
            if level==1:b.label('L'if i==0 else'R',(px+parent[0])/2,(py+parent[1])/2-11,size=11,font=BOLD)
            if level<4:b.circle(px,py,2.5,fill=WHITE,stroke=GRAY)
            else:b.box(px-12,py-4,24,15)
            pts.append((px,py))
        prev=pts


def maze_students(b):
    fid='GA-25'
    b.new_page(fid,'Keep the rooms. Lose the loops.','Trace routes · count to 12 · try movable road strips','1 / PLAY')
    b.rule('Keep all nine rooms connected. Remove roads until there is no loop. A loop returns to its start without reusing a road or visiting another room twice. Going out and back on one road is not a loop.',y=117)
    prompt(b,'25.1–2','Make two different successful mazes. Mark every road you remove.',204)
    b.label('First maze',175,251,size=12,font=BOLD,align='center');b.label('Another maze',438,251,size=12,font=BOLD,align='center')
    grid(b,87,293,step=84);grid(b,350,293,step=84)
    b.label('Roads removed: ______',175,483,size=11.8,align='center');b.label('Roads removed: ______',438,483,size=11.8,align='center')
    prompt(b,'25.3','Can you succeed by removing fewer? Give your partner something to check, not only “I tried.”',533)
    space(b,584,140,'My construction and my reason')

    b.new_page(fid,'A certificate for every maze','Keep your first maze nearby. Check both rules, then build a certificate.','2 / EXPLAIN')
    prompt(b,'25.4','This design has eight roads. Does it satisfy BOTH rules? Mark what goes wrong.',117)
    grid(b,94,190,step=57,kept=FIG['grid_perimeter']['kept'])
    space(b,176,137,'What fails?',x=306,w=262)
    prompt(b,'25.5','Draw your kept roads over the faint guides; leave missing roads faint. Cross out a one-road room and its road. Repeat until one room remains. Record the room order.',342)
    grid(b,94,423,step=60,kept=[],ghost=True)
    for i in range(8):b.box(300+(i%4)*61,428+(i//4)*54,43,38,label=str(i+1))
    b.label('Last room: ______',300,552,size=11.5)
    prompt(b,'25.6','Each step loses how many rooms? How many roads? Explain how this forces the road count for every nine-room maze.',590)
    space(b,638,60,'My paired room-and-road argument')
    txt(b,'Go further (25.7): Why must another one-road room always exist? Try following a path as far as it can go.',713,size=11.5)

    b.new_page(fid,'Repair the maze one swap at a time','A road is named by its endpoints: for example, AB.','3 / CHANGE')
    b.rule('One swap: restore one missing road, then remove a different road. After each whole swap, every room must be reachable and no loop may remain. Use only the original grid roads.',y=117)
    prompt(b,'25.8–9','Turn Maze A into Maze B. Find a shortest swap plan.',195)
    b.label('Maze A',178,242,size=12,font=BOLD,align='center');b.label('Maze B',435,242,size=12,font=BOLD,align='center')
    grid(b,106,280,step=68,kept=FIG['grid_TA']['kept'],ghost=True)
    grid(b,366,280,step=68,kept=FIG['grid_TB']['kept'],ghost=True)
    b.table([['Swap','Restore road','Remove road']]+[[str(i),'','']for i in range(1,7)],y=444,widths=[62,231,231],size=11.5,row_height=25)
    prompt(b,'25.10','Why can no plan use fewer swaps?',637)
    space(b,664,55,'A lower bound')
    txt(b,'25.11 · What loop appears after you restore a road? Which road can you remove?',730,size=11.5)

    b.new_page(fid,'Turn your maze inside out','Optional: the same picture can describe a different network.','4 / DISCOVER')
    b.rule('Draw your kept roads as bold WALLS over the faint guides. Missing roads stay faint: they are OPENINGS. Water crosses openings, never bold walls or wall corners. OUTSIDE wraps around all four sides.',y=117)
    prompt(b,'25.12','Color where water from OUTSIDE can flow. Does it reach every courtyard?',213)
    grid(b,90,290,step=83,kept=[],ghost=True,faces=True)
    dual(b,361,302,step=69)
    b.label('Your maze as walls',173,502,size=11,align='center')
    b.label('Your map of regions',430,472,size=11,align='center')
    prompt(b,'25.14','On the right, draw one link for each removed road, joining its two neighboring regions. What network appears?',535)
    space(b,585,52,'I notice…')
    prompt(b,'25.13','Try another maze. Can a courtyard stay trapped? Explain your prediction with a picture or words.',655)
    space(b,700,42,'A reason, not only two examples')


def cantor_students(b):
    fid='GA-29'
    b.new_page(fid,'Which places escape the eraser?','Start with thirds and whole-number positions. Keep the boundary dots.','1 / PLAY')
    b.rule('Start with the path from 0 to 81. Each round erases the MIDDLE THIRD of EVERY surviving piece. Keep both boundary dots of each erased gap. Draw two rounds on the blank copies.',y=117)
    numberline(b,226,caption='Start')
    numberline(b,278,caption='Round 1',blank=True)
    numberline(b,330,caption='Round 2',blank=True)
    prompt(b,'29.2','Which places will EVER be erased? Give a first round, or a reason the place stays safe forever.',373)
    rows=[['Place','First erased in round… OR safe forever','Why?']]+[[str(i),'','']for i in [9,15,18,27,40,54]]
    b.table(rows,y=422,widths=[54,255,215],size=11.3,row_height=31)
    prompt(b,'29.3','Zoom in on a surviving piece. Find a place that lasts two rounds but is erased in the third.',653)
    space(b,697,44,'My place and the gap that catches it')

    b.new_page(fid,'Give every piece an address','A new representation: follow L for left, R for right.','2 / ORGANIZE')
    b.rule('At each split choose the left piece (L) or right piece (R). Start with the whole 0-to-81 path. Four letters name one piece after four rounds.',y=117)
    address_tree(b,190)
    numberline(b,340,stage=4,caption='All the pieces after round 4')
    prompt(b,'29.4–5','Find the endpoints for two addresses, then recover the missing address.',379)
    b.table([['Four-letter address','Left endpoint','Right endpoint'],['LLRR','',''],['RLRL','',''],['','20','21']],y=412,widths=[220,152,152],size=11.7,row_height=31)
    prompt(b,'29.6','Write EVERY four-letter address beginning LR. How do you know none is missing?',551)
    for i in range(4):b.box(44+i*133,596,121,33)
    prompt(b,'29.7','Explain the number of pieces without counting the picture. Could two different addresses name the same piece?',644)
    space(b,685,60,'My count and why different addresses cannot collide')

    b.new_page(fid,'Win two challenges at once','More pieces does not have to mean more total length.','3 / CERTIFY')
    prompt(b,'29.8','Add only surviving lengths; leave out the gaps. Complete the table.',117)
    rows=[['Round','Pieces','Length of one piece','Total surviving length'],['0','1','81','81']]+[[str(i),'','','']for i in range(1,7)]
    b.table(rows,y=158,widths=[64,95,170,195],size=11.5,row_height=32)
    prompt(b,'29.9','Keep MORE THAN 50 pieces with total length LESS THAN 10. Which is the first round that wins both challenges? Why can no earlier round work?',436)
    space(b,497,81,'My round and certificate')
    prompt(b,'29.10','Name five exact places that will NEVER be erased. Explain what protects them after a million rounds.',601)
    for i in range(5):b.box(44+i*106,647,96,30)
    space(b,687,56,'Why these places stay safe')

    b.new_page(fid,'The list that always misses a point','Optional infinity page: use endless addresses and careful “every row” reasoning.','4 / GO DEEPER')
    b.rule('FACT TO USE: an endless L/R address selects nested closed pieces shrinking to length 0. Exactly one point lies in all of them. Paper cutting alone does not prove this fact.',y=117)
    prompt(b,'29.12','Why do two different endless addresses lead to different points?',195)
    space(b,228,48,'Look where their addresses first differ.')
    prompt(b,'29.13','Make a new address: differ from row 1 at letter 1, row 2 at letter 2, and so on. Fill six new letters.',295)
    rows=[['Row','First six letters; the address continues']]+[[str(i+1),' '.join(s[:6])+' …']for i,s in enumerate(FIG['cantor_list']['rows'])]
    b.table(rows,x=44,y=343,widths=[47,272],size=11.3,row_height=25)
    b.label('My new address begins',461,365,size=11,align='center')
    for i in range(6):b.box(377+(i%3)*60,397+(i//3)*50,45,33)
    prompt(b,'29.14','Six letters beat six rows, not an endless list! Give a rule for EVERY later letter. Why does your new address still name a surviving point?',537)
    space(b,598,61,'A rule that works for every row n')
    txt(b,'29.15 · Two different questions: How can the survivors fit inside an arbitrarily small total length, yet defeat every list?',681)
    b.box(44,722,255,24,label='Length reason (continue on back)');b.box(313,722,255,24,label='List reason (continue on back)')


def knot_students(b):
    fid='GA-26'
    b.new_page(fid,'Almost the same. The same knot?','Trace carefully before coloring. Each drawing is one closed cord.','1 / PLAY')
    b.rule('A solid bridge goes OVER; a gap goes UNDER. You may bend, stretch or slide the cord. You may not open an end or pass one strand through another.',y=117)
    braid(b,175,228,width=202,closed=True,cap='A',start=True)
    braid(b,438,228,width=202,closed=True,word=[(0,1),(0,-1),(0,1)],cap='B')
    prompt(b,'26.1–2','Follow the whole cord in each picture. What changed? Which can become a plain circle? Predict, then try closed cords if you have them.',426)
    space(b,489,88,'My prediction and what I tried')
    prompt(b,'26.3','Start at the dot on A. Trace to the next UNDERPASS. Begin a new section just after it. At an OVERPASS, stay in the same section. Continue until you return to the starting section.',603)
    space(b,681,61,'How many sections? Mark them on A above.')

    b.new_page(fid,'One color or three. Never two.','Use three pencils, or write R, B and G on the sections.','2 / INVESTIGATE')
    b.rule('Color each whole section between underpasses. At a crossing, its overpass and two underpass ends must be ALL THE SAME or ALL DIFFERENT. The overpass keeps its color.',y=117)
    cross_example(b,138,240,('R','R','R'),'allowed')
    cross_example(b,306,240,('R','B','G'),'allowed')
    cross_example(b,474,240,('R','R','B'),'not allowed')
    prompt(b,'26.5','Can you color A with more than one color? Can you do the same for B? Check the outside joins, too.',304)
    braid(b,175,381,width=186,closed=True,cap='A')
    braid(b,438,381,width=186,closed=True,word=[(0,1),(0,-1),(0,1)],cap='B')
    prompt(b,'26.6','For B, try two different top colors. Follow the forced colors down. Do the bottom colors match the top colors they must join?',558)
    b.lines(44,613,524,n=1)
    prompt(b,'26.7','Count every legal coloring of each FIXED drawing. Color names matter.',628)
    b.table([['Drawing','Total colorings','Using more than one color'],['A','',''],['B','',''],['Plain circle','','']],y=660,widths=[115,140,269],size=11.2,row_height=21)

    b.new_page(fid,'Do the colors survive a real move?','Complete every section. The gap always belongs to the underpass.','3 / CHECK')
    prompt(b,'26.8','Curl or uncurl. Start red on the left. What color reaches the right? Could a different completion work?',117)
    curl(b,82,178,w=166,h=75)
    b.arrow(282,220,328,220,color=GRAY)
    b.line(373,238,539,238,color=GRAY,width=2.7)
    b.label('R',63,243,size=12,font=BOLD)
    b.label('uncurl',305,239,size=10,align='center',color=GRAY)
    b.lines(44,280,524,n=1)
    prompt(b,'26.9','Slide two crossings away. Start red on the left and blue on the right. Compare the bottom colors. Then try equal starting colors.',300)
    braid(b,175,370,width=138,height=108,word=[(0,1),(0,-1)],strands=2)
    braid(b,438,370,width=138,height=108,word=[],strands=2)
    b.arrow(280,423,331,423,color=GRAY)
    for xx,t in [(106,'R'),(244,'B'),(369,'R'),(507,'B')]:b.label(t,xx,349,size=11,font=BOLD,align='center')
    b.table([['Top colors','Bottom, before slide','Bottom, after slide'],['R B','',''],['R R','','']],y=500,widths=[118,203,203],size=11.3,row_height=25)
    prompt(b,'26.10','Why do equal and different starting colors cover EVERY choice after renaming colors? Is each completion forced?',594)
    space(b,640,45,'My reason')
    txt(b,'26.11 · Can B’s first two crossings slide away? Sketch what remains on the back. Why is changing one crossing a different action?',704,size=11.5)

    b.new_page(fid,'One last move. A knot certificate.','Optional: organize cases, then use a supplied fact about all deformations.','4 / EXPLAIN')
    prompt(b,'26.12','Use the SAME top colors in both pictures. Complete the sections and compare the bottom colors, left to right.',117)
    braid(b,174,179,width=166,height=101,word=[(0,1),(1,1),(0,1)],strands=3)
    braid(b,438,179,width=166,height=101,word=[(1,1),(0,1),(1,1)],strands=3)
    b.arrow(281,229,331,229,color=GRAY)
    b.table([['Top colors','Bottom, left picture','Bottom, right picture'],['R R R','',''],['R R B','',''],['R B R','',''],['B R R','',''],['R B G','','']],y=307,widths=[118,203,203],size=11.2,row_height=24)
    prompt(b,'26.13','Why do these five patterns cover all starting colors after renaming? Could a section have two possible completions?',467)
    space(b,510,43,'My cases and uniqueness argument')
    b.rule('FACTS TO USE: every allowed cord deformation can be drawn as these three kinds of local move and ordinary redrawing. Every version pairs each coloring before with exactly one afterward. Our checks illustrate this fact.',y=570)
    prompt(b,'26.14','Why can A, with 9 colorings, never become a circle with 3?',660)
    space(b,688,36,'My obstruction')
    txt(b,'26.15 · Does our argument prove that matching counts mean the same knot? Why?',729,size=11.5)


def render_students(book,family_id):
    {'GA-25':maze_students,'GA-29':cantor_students,'GA-26':knot_students}[family_id](book)


def render_facilitator(b,family_id):
    f=FAMILIES[family_id]
    b.new_page(family_id,f['title'],'Facilitator preparation, staged hints and complete solutions')
    b.flow_h('What counts as a satisfying result')
    b.flow_p(f['assessment']['satisfying_stop'],size=11.5)
    b.flow_p(f['assessment']['verdict']+' '+f['assessment']['risk'],size=11.5)
    b.flow_h('Prerequisites')
    for k,v in f['prerequisites'].items():b.flow_p(k.replace('_',' ').capitalize()+': '+v,size=11.5)
    b.flow_h('Materials, preparation and pace')
    b.flow_p('; '.join(f['materials'])+f". Preparation: about {f['prep_minutes']} minutes.",size=11.5)
    if 'preparation_details'in f:b.flow_p(f['preparation_details'],size=11.5)
    b.flow_p(f['timing'],size=11.5)
    b.flow_p(f['prior_use'],size=11.5)
    b.new_page(family_id,f['title']+' — solutions','Prompt numbers match the student pages; back-pocket questions are noted.')
    if family_id=='GA-25':
        b.label('Maze A',175,b.y,size=12,font=BOLD,align='center');b.label('Complementary region tree',438,b.y,size=12,font=BOLD,align='center')
        yy=b.y+45;grid(b,95,yy,step=70,kept=FIG['grid_TA']['kept'],ghost=True,faces=True)
        dual(b,368,yy+8,step=65,edges=[('NW','NE'),('SW','SE'),('NE','OUT'),('SE','OUT')])
        b.y=yy+191
    elif family_id=='GA-26':
        yy=b.y+35;braid(b,173,yy,width=205,closed=True,colored=[0,1],cap='A: one of six nonconstant colorings')
        braid(b,437,yy,width=205,closed=True,word=[(0,1),(0,-1),(0,1)],colored=[0,0],cap='B: only constant colorings')
        b.y=yy+190
        b.flow_p('Color key: R = red, B = blue, G = green. The letters in the tables give the same information in monochrome.',size=11.5)
    elif family_id=='GA-29':
        for n in range(5):numberline(b,b.y+28+42*n,stage=n,caption=f'Round {n}',labels=False)
        b.y+=244
    for no,answer in f['solutions'].items():
        b.flow_h(no+(' · optional back-pocket extension'if no in ['25.15','29.11']else''))
        b.flow_p(answer,size=11.5)
    b.flow_h('Offer hints only after exploration')
    for hint in f['hints']:b.flow_p(hint['for']+': '+hint['text'],size=11.5)
    if 'invariance_variants'in f:
        b.flow_h('All knot-move variants, not only the pictured braid')
        b.flow_p(f['invariance_variants'],size=11.5)
    b.flow_h('Sources and checked scope')
    for s in f['sources']:
        b.flow_p(s['title']+'. '+s['locator']+'. '+s['use'],size=11.5)
        b.flow_p('<link href="'+escape(s['url'],quote=True)+'" color="#126E78">'+escape(s['url'])+'</link>',size=10.5,rich=True)
    b.flow_p('Exact checks: plans/atlas/worksheet-trial/geometry-checks.py and geometry-checks-results.json. '+f['assessment']['not_claimed'],size=11.5)
