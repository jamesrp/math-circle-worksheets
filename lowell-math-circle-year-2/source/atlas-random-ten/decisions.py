"""Four concrete worksheet investigations; shared canvas owned by root.

Student content is deliberately laid out by investigation rather than dumped
from the plan. Solutions and staged hints appear only in the facilitator book.
"""
from pathlib import Path
import json, math
from sheet import DATA, FONT, BOLD, ITALIC, INK, NAVY, TEAL, GRAY, PALE, LIGHT, WHITE

DESIGN=json.loads((DATA/'decisions-data.json').read_text())
FAMILIES={w['id']:w for w in DESIGN['worksheets']}

def q(b,w,key,y=None,size=11.5):
    block=next(z for p in w['pages'] for z in p['blocks'] if z['id']==key)
    if y is None:y=b.y
    n=key.split('.')[-1]
    bottom=b.p(n+'. '+block['prompt'],y=y,size=size,leading=15)
    b.y=bottom+7
    return b.y

def start(b,w,i):
    pg=w['pages'][i]
    b.new_page(w['id'],pg['title'],w['title'],part=f'INVESTIGATE {i+1}/3')
    b.rule(pg['intro']);b.y+=12
    return b.y

def blank_lines(b,n=2,spacing=21,y=None):
    if y is None:y=b.y+10
    b.lines(44,y,524,n,spacing);b.y=y+(n-1)*spacing+12
    return b.y

def road(b,x,y,w=242,h=74,quick=(),steady=(),blank=False):
    # All labels are inside their own broad route strips; no crossing text.
    b.box(x,y,w,h,fill=None,stroke=LIGHT,radius=5)
    b.label('QUICK',x+9,y+8,size=9,font=BOLD,color=TEAL)
    b.line(x+62,y+23,x+w-12,y+23,width=1.4)
    b.label('STEADY',x+9,y+43,size=9,font=BOLD,color=GRAY)
    b.line(x+62,y+58,x+w-12,y+58,width=1.2,dash=[5,3])
    for names,yy in [(quick,y+23),(steady,y+58)]:
        for j,t in enumerate(names):
            xx=x+93+j*48;b.circle(xx,yy,11,fill=WHITE);b.label(t,xx,yy-7,size=10,font=BOLD,align='center')

def crowds(b,y,cost_boxes=False):
    for i in range(4):
        x=44+i*139
        b.box(x,y,107,38,fill=WHITE,radius=4)
        b.label(f'{i} on QUICK',x+53.5,y+11,size=10.5,align='center')
        if cost_boxes:b.label('total: ______',x+53.5,y+46,size=10.5,align='center')
    b.y=y+(73 if cost_boxes else 50)

def costline(b,x,y,w=242):
    b.label('R: ___   G: ___   B: ___',x+7,y,size=10.5)
    b.label('total: ____',x+w-8,y,size=10.5,align='right')

def render_23(b,w):
    start(b,w,0)
    q(b,w,'23.1')
    road(b,44,b.y,524,74);b.y+=84
    b.table([['QUICK crowd','QUICK names','R cost','G cost','B cost','Total','Stopped?'],
             ['0','','','','','',''],['1','','','','','',''],['2','','','','','',''],['3','','','','','','']],
            widths=[55,106,57,57,57,70,122],size=10,row_height=[34,25,25,25,25]);b.y+=10
    q(b,w,'23.2')
    b.p('Use the four rows above. Leave “Stopped?” until you have tested the possible moves.',size=10.3,color=GRAY);b.y+=10
    q(b,w,'23.3');crowds(b,b.y+5)
    start(b,w,1)
    q(b,w,'23.4')
    y=b.y;b.label('BEFORE',44,y,size=9,font=BOLD,color=GRAY);b.label('AFTER',326,y,size=9,font=BOLD,color=GRAY)
    road(b,44,y+17,242,74,('R',),('G','B'));road(b,326,y+17,242,74,('R','G'),('B',))
    costline(b,44,y+98);costline(b,326,y+98);b.y=y+123;blank_lines(b,2)
    q(b,w,'23.5');crowds(b,b.y+2,cost_boxes=True);blank_lines(b,2)
    q(b,w,'23.6');y=b.y;road(b,44,y);road(b,326,y);b.y=y+86;blank_lines(b,2)
    start(b,w,2)
    q(b,w,'23.7');crowds(b,b.y);blank_lines(b,1)
    q(b,w,'23.8');y=b.y+14
    points=[(306,y+2),(453,y+66),(453,y+168),(306,y+228),(159,y+168),(159,y+66)]
    for (x,yy),name in zip(points,['R','RG','G','GB','B','RB']):
        b.box(x-34,yy,68,29,fill=WHITE,radius=4);b.label(name,x,yy+6,size=12,font=BOLD,align='center')
        b.label('total: ____',x,yy+35,size=10,align='center')
    b.y=y+282
    q(b,w,'23.9');blank_lines(b,2)

def offers(b,y,costs=None,pay=None):
    costs=costs or [2,2,3,1,2];pay=pay or [5,6,9,4,8]
    for i,(c,r) in enumerate(zip(costs,pay)):
        x=44+i*106.5
        b.box(x,y,98,76,fill=PALE,stroke=LIGHT,radius=5)
        b.label(f'DAY {i+1}',x+49,y+8,size=11,font=BOLD,align='center',color=TEAL)
        b.label(f'cost {c} battery',x+49,y+31,size=10.2,align='center')
        b.label(f'earn {r} points',x+49,y+53,size=10.2,align='center')
    b.y=y+87

def comparebox(b,x,y,w,h,title,take='',skip=''):
    b.box(x,y,w,h,fill=None,stroke=LIGHT,radius=5)
    b.label(title,x+9,y+8,size=10.5,font=BOLD,color=TEAL)
    b.label('TAKE: '+(take or '________________'),x+9,y+32,size=10.3)
    b.label('SKIP: '+(skip or '________________'),x+9,y+54,size=10.3)
    b.label('BEST: __________',x+9,y+77,size=10.3,font=BOLD)

def render_21(b,w):
    start(b,w,0)
    offers(b,b.y)
    q(b,w,'21.1')
    b.table([['Days taken','Battery spent','Points'],['','',''],['','',''],['','','']],
            widths=[264,130,130],row_height=[26,29,29,29],size=11);b.y+=12
    q(b,w,'21.2')
    y=b.y
    for x,title in [(44,'TAKE WHEN POSSIBLE'),(314,'BIGGEST REWARD FIRST')]:
        b.box(x,y,254,91,fill=None,radius=4);b.label(title,x+10,y+10,size=9.5,font=BOLD,color=TEAL)
        b.label('days: ____________________',x+10,y+35,size=10.5)
        b.label('battery: ____    points: ____',x+10,y+61,size=10.5)
    b.y=y+104
    q(b,w,'21.3');b.box(44,b.y,524,54,label='MY BEST PLAN / WHY I THINK IT IS BEST');b.y+=64
    start(b,w,1)
    q(b,w,'21.4');y=b.y
    for x,title,history in [(44,'ROBOT X','day 1 TAKE  /  day 2 SKIP'),(314,'ROBOT Y','day 1 SKIP  /  day 2 TAKE')]:
        b.box(x,y,254,87,fill=PALE,radius=4)
        b.label(title,x+10,y+9,size=10,font=BOLD,color=TEAL);b.label(history,x+10,y+31,size=10)
        b.label('battery: ____    earned: ____',x+10,y+57,size=10.5)
    b.y=y+99;blank_lines(b,2)
    q(b,w,'21.5')
    b.table([['battery','0','1','2','3','4','5'],['best extra','','','','','','']],
            widths=[110]+[69]*6,row_height=[29,39],size=11);b.y+=8;blank_lines(b,1)
    q(b,w,'21.6');y=b.y
    for x,title in [(44,'TAKE DAY 3'),(314,'SKIP DAY 3')]:
        b.box(x,y,254,120,fill=None,stroke=LIGHT,radius=5)
        b.label(title,x+9,y+8,size=10.5,font=BOLD,color=TEAL)
        b.label('points now: ____',x+9,y+32,size=10.5)
        b.label('battery before day 4: ____',x+9,y+54,size=10.5)
        b.label('best later score: ____',x+9,y+76,size=10.5)
        b.label('TOTAL: ____',x+9,y+98,size=10.5,font=BOLD)
    b.y=y+133;blank_lines(b,1)
    start(b,w,2)
    q(b,w,'21.7');y=b.y
    for i,e in enumerate([1,3,5]):comparebox(b,44+i*179,y,166,103,f'DAY 3 / BATTERY {e}')
    b.y=y+115
    q(b,w,'21.8');y=b.y
    comparebox(b,44,y,254,103,'(a) DAY 2 / BATTERY 3')
    comparebox(b,314,y,254,103,'(b) DAY 2 / BATTERY 5')
    b.y=y+113;y=b.y
    comparebox(b,44,y,254,103,'(c) DAY 1 / BATTERY 5')
    b.box(314,y,254,103,fill=None,radius=5);b.label('(d) TRACE YOUR PLAN',324,y+8,size=10.5,font=BOLD,color=TEAL)
    b.label('days: ___________________',324,y+38,size=10.5);b.label('points: ____   battery: ____',324,y+69,size=10.5)
    b.y=y+116
    q(b,w,'21.9');blank_lines(b,4,spacing=21)

def track(b,y,n=4,prices=False,ferry=False):
    x0=78;dx=456/n
    b.line(x0,y,x0+n*dx,y,width=1.6)
    for i in range(n+1):
        x=x0+i*dx;b.circle(x,y,15,fill=PALE if i in [0,n] else WHITE)
        b.label(str(i),x,y-8,size=12,font=BOLD,align='center')
        if prices:b.label(('0' if i==0 else str(n) if i==n else '____')+' prize price',x,y+25,size=9.5,align='center')
    if not ferry:
        b.label('TAILS ←',240,y-38,size=10.5,align='center',color=GRAY)
        b.label('→ HEADS',385,y-38,size=10.5,align='center',color=GRAY)
    else:
        # Two ferry paths deliberately occupy separate top lanes; small outgoing
        # arrows for normal sites live below, away from the price labels.
        for end,label,yy in [(0,'T',y-53),(4,'H',y-78)]:
            x2=x0+end*dx;mid=x0+2*dx
            b.poly([(mid,y-17),(mid,yy),(x2,yy),(x2,y-20)],stroke=TEAL,width=1.4)
            b.arrow(x2,y-31,x2,y-18,color=TEAL,width=1.4)
            b.label('ferry '+label,(mid+x2)/2,yy-16,size=10,align='center',color=TEAL)
        for i,j,label,yy in [(1,0,'T',y+30),(1,2,'H',y+48),(3,2,'T',y+30),(3,4,'H',y+48)]:
            xx=x0+i*dx;xx2=x0+j*dx
            b.poly([(xx,y+17),(xx,yy),(xx2,yy),(xx2,y+18)],stroke=GRAY,width=.9)
            b.arrow(xx2,yy,xx2,y+18,color=GRAY,width=.9)
            b.label(label,(xx+xx2)/2,yy+2,size=9,align='center',color=GRAY)
    b.y=y+(69 if not ferry else 94)

def render_01(b,w):
    start(b,w,0)
    track(b,b.y+45,prices=False)
    q(b,w,'01.1')
    b.table([['Start','A short path / toss record','Shore'],['','',''],['','',''],['','',''],['','','']],
            widths=[75,374,75],row_height=[26,25,25,25,25],size=10.5);b.y+=12
    q(b,w,'01.2');track(b,b.y+32,prices=True);blank_lines(b,1)
    q(b,w,'01.3');blank_lines(b,3)
    start(b,w,1)
    q(b,w,'01.4');y=b.y+3
    b.box(244,y,124,29,label='HERE = ____',fill=PALE)
    b.arrow(257,y+31,181,y+72);b.arrow(354,y+31,431,y+72)
    b.label('half',208,y+39,size=10);b.label('half',390,y+39,size=10)
    b.box(130,y+74,103,29,label='a');b.box(379,y+74,103,29,label='b')
    b.y=y+119
    q(b,w,'01.5');y=b.y
    # Square graph with generous spaces for plotting and equal-gap annotations.
    gx=142;gy=y+10;gw=296;gh=184
    b.grid(gx,gy,gw,gh,4,4)
    for i in range(5):
        b.label(str(i),gx+i*gw/4,gy+gh+8,size=10,align='center')
        b.label(str(4-i),gx-12,gy+i*gh/4-7,size=10,align='right')
    b.circle(gx,gy+gh,4,fill=INK);b.circle(gx+gw,gy,4,fill=INK)
    b.label('price',gx-32,gy-21,size=10,color=GRAY);b.label('place',gx+gw+20,gy+gh+8,size=10,color=GRAY)
    b.y=gy+gh+35
    q(b,w,'01.6');y=b.y
    for i in range(4):b.label(f'gap {i+1}: ____',44+i*138,y,size=10.5)
    b.y=y+26
    for i in range(1,4):b.label(f'chance from {i}: ______',44+(i-1)*181,b.y,size=10.5)
    b.y+=26;blank_lines(b,2)
    start(b,w,2)
    q(b,w,'01.7');track(b,b.y+96,prices=False,ferry=True)
    for i in range(1,4):b.label(f'price at {i}: _____',64+(i-1)*177,b.y,size=10.5)
    b.y+=29
    q(b,w,'01.8');blank_lines(b,2)
    q(b,w,'01.9');track(b,b.y+42,n=6,prices=False);blank_lines(b,1)

def icon(b,s,x,y,r=10):
    if s=='A':b.poly([(x,y-r),(x-r,y+r),(x+r,y+r)],closed=True,fill=WHITE,stroke=INK)
    elif s=='B':b.circle(x,y,r,fill=WHITE)
    elif s=='C':b.box(x-r,y-r,2*r,2*r,fill=WHITE,stroke=INK)
    else:
        pts=[(x+(r if i%2==0 else r*.43)*math.sin(i*math.pi/5),y-(r if i%2==0 else r*.43)*math.cos(i*math.pi/5)) for i in range(10)]
        b.poly(pts,closed=True,fill=WHITE,stroke=INK)
    b.label(s,x,y+r+3,size=9,align='center')

def strip(b,message,y,blank=False):
    for i,s in enumerate(message):
        x=66+i*66
        b.box(x-20,y,40,47,fill=None,stroke=LIGHT)
        if not blank:icon(b,s,x,y+17,9)
    b.y=y+58

def bits(b,y,n=16):
    # Thin boundaries between bits do not suggest where symbols end.
    for i in range(n):b.box(44+i*524/n,y,524/n,25,fill=None,stroke=LIGHT,width=.45)
    b.y=y+37

def treeframe(b,x,y,w,h):
    b.box(x,y,w,h,fill=None,stroke=LIGHT,radius=5)
    mid=x+w/2;b.circle(mid,y+17,3,fill=INK)
    b.line(mid,y+20,mid-28,y+48,width=.8);b.line(mid,y+20,mid+28,y+48,width=.8)
    b.label('0',mid-24,y+22,size=10);b.label('1',mid+17,y+22,size=10)

def render_29(b,w):
    start(b,w,0)
    q(b,w,'29.1');strip(b,'ABACABDA',b.y);bits(b,b.y)
    b.label('Receiver pictures: __________________________________________',44,b.y,size=10.5);b.y+=26
    q(b,w,'29.2');y=b.y
    for x in [44,314]:
        b.box(x,y,254,64,fill=None,radius=4)
        b.label('0  1  0',x+127,y+9,size=16,font=BOLD,align='center')
        b.label('pictures: _________________',x+10,y+38,size=10.5)
    b.y=y+78
    q(b,w,'29.3');y=b.y
    treeframe(b,44,y,327,172)
    for i,s in enumerate('ABCD'):b.label(s+' = ______________',396,y+13+i*28,size=11)
    b.label('TOTAL BITS: _____',396,y+149,size=10.5,font=BOLD);b.y=y+185
    start(b,w,1)
    q(b,w,'29.4');y=b.y
    # Deliberately only a two-leaf toy; no answer shape for main problem.
    b.circle(132,y+6,3,fill=INK);b.line(132,y+9,132,y+35)
    b.circle(132,y+38,3,fill=INK);b.line(132,y+41,96,y+72);b.line(132,y+41,168,y+72)
    b.label('0',144,y+17,size=10);b.label('0',101,y+46,size=10);b.label('1',155,y+46,size=10)
    b.label('A',96,y+77,size=10,align='center');b.label('B',168,y+77,size=10,align='center')
    b.label('SHORTEN IT HERE',347,y+3,size=9.5,font=BOLD,color=GRAY)
    b.box(274,y+20,254,82,fill=None,radius=4)
    b.y=y+116
    q(b,w,'29.5');y=b.y
    treeframe(b,44,y,254,165);treeframe(b,314,y,254,165)
    for x in [44,314]:b.label('root split: ____ + ____',x+10,y+139,size=10.5)
    b.y=y+177
    q(b,w,'29.6');y=b.y
    b.label('Shape 1 total: __________',44,y,size=10.5);b.label('Shape 2 total: __________',314,y,size=10.5)
    b.y=y+24;blank_lines(b,4)
    start(b,w,2)
    q(b,w,'29.7');strip(b,'ABCDABCD',b.y)
    y=b.y;b.label('balanced total: ______',44,y,size=11);b.label('long-branch total: ______',314,y,size=11);b.y=y+27
    q(b,w,'29.8');strip(b,'ABCDAA',b.y,blank=True)
    y=b.y
    for x,title in [(44,'BALANCED'),(314,'LONG BRANCH')]:
        b.box(x,y,254,126,fill=None,radius=4);b.label(title,x+10,y+8,size=10,font=BOLD,color=TEAL)
        for i,s in enumerate('ABCD'):b.label(s+' = __________',x+10+(i%2)*124,y+34+(i//2)*29,size=10.5)
        b.label('total bits: ______',x+10,y+99,size=11)
    b.y=y+139
    q(b,w,'29.9');bits(b,b.y);blank_lines(b,2)

def render_students(book,family_id):
    w=FAMILIES[family_id]
    {'AP-23':render_23,'AP-21':render_21,'AP-01':render_01,'AP-29':render_29}[family_id](book,w)


def render_facilitator(book,family_id):
    w=FAMILIES[family_id];f=w['facilitator']
    book.new_page(family_id,w['title'],'Facilitator notes • exact worksheet answers • not classroom-piloted')
    book.flow_p(w['verdict'])
    book.flow_h('Prerequisites and honest stopping points')
    for k,v in w['prerequisites'].items():book.flow_p(k.replace('_',' ').capitalize()+': '+v)
    book.flow_p('Materials: '+w['materials'])
    book.flow_p(f"Preparation: about {w['prep_minutes']} minutes. "+w['timing'])
    book.flow_p('Stop: '+f['stop'])
    book.flow_h('Staged hints')
    for h in f['hints']:book.flow_p(f"{h['stage']}. For {h['for']}: {h['text']}")
    book.flow_h('Checked solutions to every prompt')
    for key,value in f['solutions'].items():
        book.flow_h(key)
        book.flow_p(value)
    book.flow_h('What this really teaches')
    book.flow_p(f['adult_math']);book.flow_p('Prior use: '+f['prior_use'])
    book.flow_p('Source adaptation: '+f['source_note'])
    for s in w['sources']:
        book.flow_p(s['title']+'. '+s['locator']+'. '+s['url']+'\nEvidence status: '+s['checked'])
    book.flow_p('Verification: plans/atlas/worksheet-trial/decisions-checks.py; exact enumeration and rational calculations in decisions-checks-results.json. Full battery state tables are in that checked data; they are deliberately absent from the student work.')
