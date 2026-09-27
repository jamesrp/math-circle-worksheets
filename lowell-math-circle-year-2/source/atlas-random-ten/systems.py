"""Custom student layouts and complete facilitator key for GA-11/AP-26/AP-07."""
from math import exp, sqrt
from html import escape
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from sheet import *

D=data('systems-data.json')
F={x['id']:x for x in D['investigations']}


def prompt(f,pid):
    return next(p['text'] for page in f['student_pages'] for p in page['prompts'] if p['id']==pid)


def ask(b,f,pid,y,text=None,x=44,width=524):
    b.label(pid,x,y+1,size=11.5,font=BOLD,color=TEAL)
    return b.p(text or prompt(f,pid),x=x+29,y=y,width=width-29,size=11.7,leading=15.1)+7


def blank(b,y,h,label='',x=44,w=524):
    b.box(x,y,w,h,label=label,stroke=LIGHT)
    return y+h+10


def line_space(b,y,n=2):
    b.lines(49,y+15,514,n=n,spacing=22)
    return y+22*n+10


def start(b,f,page,gate):
    p=f['student_pages'][page-1]
    y=b.new_page(f['id'],p['title'],gate,part=f'{page} / {len(f["student_pages"])}')
    return b.rule(p['lede'],y=y)+12


def pairboxes(b,y,labels,count=7,initial='(a, b)',height=44):
    gap=7;ww=(524-(count-1)*gap)/count
    for i in range(count):
        x=44+i*(ww+gap)
        b.box(x,y,ww,height)
        if labels:b.label(str(labels[i]),x+ww/2,y+5,size=9.5,align='center',color=GRAY)
        if i==0 and initial:b.label(initial,x+ww/2,y+height-22,size=12,align='center')
        if i<count-1:b.arrow(x+ww+1,y+height/2,x+ww+gap-1,y+height/2,head=3,color=GRAY)
    return y+height+11


def numberline(b,x,y,w,lo,hi,step=1):
    b.line(x,y,x+w,y,color=GRAY)
    for k in range(round((hi-lo)/step)+1):
        v=lo+k*step;xx=x+w*(v-lo)/(hi-lo)
        b.line(xx,y-5,xx,y+5,color=GRAY)
        b.label(f'{v:g}',xx,y+9,size=10,align='center')


def two_dials(b,x,y,w,title):
    b.box(x,y,w,131,stroke=LIGHT)
    b.label(title,x+12,y+9,size=13,font=BOLD,color=TEAL)
    b.box(x+12,y+35,45,32,label='a')
    b.box(x+68,y+35,45,32,label='b')
    b.arrow(x+119,y+51,x+147,y+51,color=GRAY)
    b.box(x+154,y+35,w-166,32,label='output')
    b.label('Formula:',x+12,y+80,size=11.5)
    b.line(x+62,y+96,x+w-12,y+96,color=LIGHT)
    b.label('Why it obeys addition:',x+12,y+106,size=10.5,color=GRAY)


def render_ga11(b,f):
    y=start(b,f,1,'Core: signed fractions, symbolic algebra, and rational versus irrational numbers.')
    y=ask(b,f,'G1',y,text='For each claim, mark IMPOSSIBLE or FORCED. Certify your verdict using two addition routes to the same input. Do not assume a formula for f.')
    cards=[('f(0) = 1',''),('f(−1) = −3',''),('f(2/3) = 21/10',''),('f(5/6) = 5/2','')]
    for i,(claim,_) in enumerate(cards):
        xx=44+(i%2)*270;yy=y+(i//2)*143
        b.box(xx,yy,254,133)
        b.label(claim,xx+12,yy+9,size=14,font=BOLD)
        b.label('Verdict: __________________',xx+12,yy+33,size=11)
        b.label('Route A:',xx+12,yy+59,size=10.5,color=GRAY)
        b.label('Route B:',xx+12,yy+91,size=10.5,color=GRAY)
        b.line(xx+62,yy+83,xx+242,yy+83,color=LIGHT)
        b.line(xx+62,yy+115,xx+242,yy+115,color=LIGHT)
    y+=290
    y=ask(b,f,'G2',y,text='Choose a new awkward rational input and a tempting wrong output. Trade with a partner: expose the contradiction using the addition promise.')
    b.box(44,y,524,95)
    b.label('Input: __________________    Proposed output: __________________',56,y+10,size=11.5)
    b.label('Certificate:',56,y+38,size=11.5,color=GRAY)
    b.lines(116,y+61,432,n=1)

    y=start(b,f,2,'A proof for a whole set of inputs; then one new kind of input.')
    y=ask(b,f,'G3',y)
    for label in ['First: zero and integer inputs','Then: n copies of m/n','Therefore: every rational input']:
        y=blank(b,y,53,label)
    y=ask(b,f,'G4',y)
    y=line_space(b,y,n=2)
    y=ask(b,f,'G5',y,text='Now accept exactly a+b√2 with rational a,b. You may use: each input has exactly one pair (a,b). Invent pair addition. Test it on (1+2√2)+(−3+√2/2).')
    b.box(44,y,524,83)
    b.label('(a, b) + (c, d) =',56,y+10,size=13)
    b.line(181,y+30,550,y+30,color=LIGHT)
    b.label('Our example:',56,y+45,size=11.5)
    b.line(135,y+66,550,y+66,color=LIGHT)

    y=start(b,f,3,'Full core: invent and verify two different functions on the same domain.')
    y=ask(b,f,'G6',y,text='Make Machine A send √2 to 0 and Machine B send √2 to 5. Give formulas in a,b. Prove each obeys addition for two arbitrary input pairs.')
    two_dials(b,44,y,254,'MACHINE A');two_dials(b,314,y,254,'MACHINE B');y+=142
    y=blank(b,y,75,'Addition proof for arbitrary pairs')
    y=ask(b,f,'G7',y,text='Give an input where they disagree. Prove they agree on EVERY rational input. Why does the uniqueness of (a,b) matter?')
    y=line_space(b,y,n=2)
    y=ask(b,f,'G8',y,text='Optional continuity challenge. For B, compare outputs at 1.4142 and √2; you may use 1.4142<√2<1.4143. Does one close pair prove discontinuity? What happens for rational inputs arbitrarily close to √2? Which extra promise rules B out?')
    y=line_space(b,y,n=2)


def tri_grid(b,x,y,w,h):
    points={}
    scale=min(w/9,h/(3*sqrt(3)))
    cx=x+w/2;cy=y+h/2
    for a in range(-3,4):
        for c in range(-3,4):
            points[(a,c)]=(cx+scale*(a-c/2),cy-scale*sqrt(3)*c/2)
    for (a,c),p in points.items():
        for da,dc in [(1,0),(0,1),(1,1)]:
            q=points.get((a+da,c+dc))
            if q:b.line(*p,*q,color=LIGHT,width=.4)
    for p in points.values():b.circle(*p,r=1.25,fill=GRAY,stroke=GRAY,width=.2)
    b.circle(cx,cy,3,fill=INK)
    b.label('(0,0)',cx+5,cy+3,size=9)
    for pair,label,offset in [((1,0),'+1 OLD',(0,4)),((0,1),'+1 CURRENT',(-55,-20))]:
        xx,yy=points[pair];b.arrow(cx,cy,xx,yy,color=TEAL,width=1.6)
        b.label(label,xx+offset[0],yy+offset[1],size=9.5,color=TEAL)


def render_ap26(b,f):
    p=f['student_pages'][0]
    y=b.new_page(f['id'],p['title'],'Core: signed subtraction; track two cards in the right order.',part='1 / 4')
    y=b.rule('Start OLD=1 and CURRENT=1. Each tick: command = −OLD; new position = CURRENT + command. Then replace BOTH cards: OLD becomes the position before the move, CURRENT becomes the new position.',y=y)+10
    b.box(44,y,250,40,label='OLD REPORT = 1',fill=PALE);b.box(312,y,256,40,label='CURRENT POSITION = 1',fill=PALE);y+=56
    numberline(b,56,y,500,-6,6);y+=36
    y=ask(b,f,'D1',y,text='Play until you think the story repeats. Record enough ticks to convince a partner. Circle every visit to zero. Does reaching zero mean staying there?')
    y=pairboxes(b,y,list(range(9)),count=9,initial='1',height=44)
    y=line_space(b,y,n=1)
    y=ask(b,f,'D2',y,text='Instead use CURRENT to make the command. Start at 1 again. What happens, and exactly what did the delayed report change?')
    y=line_space(b,y,n=2)
    y=ask(b,f,'D3',y,text='Restore the delayed rule. Choose (old,current) that makes the NEXT position zero. Find every pair that stays at zero forever. Explain the difference.')
    b.box(44,y,254,70,label='Next position is zero');b.box(314,y,254,70,label='Stays zero forever')

    y=start(b,f,2,'A repeated reading and a repeated complete state are different.')
    y=ask(b,f,'D4',y)
    b.box(44,y,254,54,label='A: (1,1) →');b.box(314,y,254,54,label='B: (−1,1) →');y+=63
    y=ask(b,f,'D5',y)
    y=blank(b,y,201,'Our pair-state map: draw the states and tick arrows')
    y=ask(b,f,'D6',y)
    y=blank(b,y,83,'Previous pair: (________, ________) → (c,d)')

    y=start(b,f,3,'Algebra continuation: letters stand for any starting pair. Picture proof is optional.')
    y=ask(b,f,'D7',y,text='Start at (a,b). Apply (old,current) → (current,current−old) until the pair returns. Explain why your calculation works for every real a,b.')
    y=pairboxes(b,y,list(range(7)),initial='(a,b)',height=59)
    y=ask(b,f,'D8',y,text='Does every nonzero pair FIRST return on the same tick? Rule out return in 1, 2, or 3 ticks. Why are those the only shorter periods you need to check?')
    b.box(44,y,524,102)
    for xx,label in [(56,'1 tick'),(230,'2 ticks'),(405,'3 ticks')]:
        b.label(label,xx,y+7,size=10.5,color=GRAY)
    y+=112
    y=ask(b,f,'D9',y,text='Optional geometry. Plot the orbit of (1,1), then (1,2), on this triangular grid. One OLD unit points right; one CURRENT unit points up-left. What rigid motion does one tick make? Can the two unit directions prove it for all pairs?')
    tri_grid(b,60,y+4,480,180)
    b.label('Start from the center. Follow the two arrow directions to locate a pair.',44,y+191,size=10.5,color=GRAY)

    y=start(b,f,4,'Optional extension: fractions and algebra. Plan for another session if useful.')
    y=ask(b,f,'D10',y,text='Start at (1,1). Predict whether this gentler correction helps. Run four ticks and compare the WHOLE pair with the start. Then test four more if needed.')
    y=pairboxes(b,y,list(range(5)),count=5,initial='(1,1)',height=57)
    y=pairboxes(b,y,list(range(5,9)),count=4,initial='',height=57)
    y=ask(b,f,'D11',y,text='Now start at (a,b). Work out four ticks and use the result to prove whether EVERY pair approaches (0,0).')
    y=pairboxes(b,y,list(range(5)),count=5,initial='(a,b)',height=62)
    y=blank(b,y,96,'Why all four types of tick approach zero')
    y=ask(b,f,'D12',y,text='Starting at (1,1), certify a tick after which BOTH cards always have magnitude at most 1/100. It need not be the earliest. Why is a small current value alone insufficient?')
    y=blank(b,y,75,'A certified tick and reason')


def cooling_graph(b,x,y,w,h):
    t0,t1=0,3.1;v0,v1=-17,9
    def at(t,v):return (x+w*(t-t0)/(t1-t0),y+h*(v1-v)/(v1-v0))
    for t in [0,.5,1,1.5,2,2.5,3]:
        xx,_=at(t,0);b.line(xx,y,xx,y+h,color=LIGHT,width=.4)
        b.label(f'{t:g}',xx,y+h+5,size=9,align='center')
    for v in [-16,-12,-8,-4,0,4,8]:
        _,yy=at(0,v);b.line(x,yy,x+w,yy,color=LIGHT,width=.4)
        b.label(str(v),x-9,yy-5,size=9,align='right')
    b.line(*at(0,0),*at(3.1,0),color=GRAY,width=.9)
    points=[at(3.1*i/160,8*exp(-3.1*i/160)) for i in range(161)]
    b.poly(points,stroke=TEAL,width=1.9)
    b.circle(*at(0,8),r=2.5,fill=TEAL,stroke=TEAL)
    b.label('exact y = 8e^(−t)',x+w-130,y+15,size=10,color=TEAL)
    b.label('elapsed time t',x+w-10,y+h+19,size=10,align='right',color=GRAY)
    b.label('y',x-17,y-10,size=11,color=GRAY)


def render_ap07(b,f):
    y=start(b,f,1,'Calculus core: derivatives as slopes, exponentials, algebra. Calculator welcome.')
    y=ask(b,f,'C1',y,text='Check the supplied solution using its derivative and initial value. What must remain true about its sign and direction of change for every finite t≥0?')
    y=line_space(b,y,n=2)
    y=ask(b,f,'C2',y,text='At (t,y), follow slope −y for a duration h>0. Derive the next value. From (0,8), draw ONE step for h=1/2, 3/2, and 3; label endpoints by actual time. Which violate the model’s behavior?')
    b.label('Update rule: ___________________________________________',44,y+2,size=11.5);y+=31
    cooling_graph(b,80,y+3,472,182);y+=218
    y=ask(b,f,'C3',y,text='Does a negative simulated y mean negative absolute temperature? Explain its actual meaning and why it is still wrong for this model and start.')
    y=line_space(b,y,n=2)

    y=start(b,f,2,'Classify a parameter; then test a claim about accuracy.')
    y=ask(b,f,'C4',y,text='Express an update as multiplication by one number. Classify ALL h>0 in the table. Include every boundary value.')
    b.label('Multiplier: __________________',44,y,size=12);y+=28
    y=b.table([['Behavior','Values of h'],['Strictly positive, decreasing',''],['Hits zero in one step',''],['Alternates and settles',''],['Bounded, persistent oscillation',''],['Magnitude grows','']],y=y,widths=[338,186],size=11.5,row_height=31)+13
    y=ask(b,f,'C5',y,text='Disprove: “If it settles, its answers are accurate.” Compare at the SAME elapsed time. Calculate relative error |approximate−exact|/exact.')
    y=b.table([['h','time','approximate','exact','relative error'],['','','','','']],y=y,widths=[62,65,128,128,141],size=11.5,row_height=31)+13
    y=ask(b,f,'C6',y,text='Change the physics to y′=−2y. Find all positive h that make the simulator settle, and all that keep EVERY value strictly positive. Explain without a long sequence.')
    y=blank(b,y,78,'New multiplier and two parameter ranges')

    y=start(b,f,3,'A design problem: optimize where to spend a limited number of updates.')
    y=ask(b,f,'C7',y,text='Try two split times h. Derive the final value as a function of h. Both estimates must finish at t=1.')
    for i in range(2):
        yy=y+i*39;b.line(70,yy+8,548,yy+8,color=GRAY)
        b.line(70,yy+2,70,yy+14);b.line(548,yy+2,548,yy+14)
        b.label('0',70,yy+17,size=10,align='center');b.label('1',548,yy+17,size=10,align='center')
        b.label('mark your split',302,yy+15,size=10,align='center',color=GRAY)
    y+=88
    y=blank(b,y,47,'Final value formula')
    y=ask(b,f,'C8',y,text='Which h gives the closest answer to 8/e? Prove it beats EVERY two-step choice. Why does maximizing the simulated value minimize the error here?')
    y=blank(b,y,148,'Optimal choice and proof')
    y=ask(b,f,'C9',y,text='Replace one duration H by positive u,v with u+v=H. Compare the two multipliers algebraically. What improves for 0<H≤1? What exact-model comparison is needed to claim improved accuracy?')
    y=blank(b,y,80,'One step versus split step')

    y=start(b,f,4,'Advanced continuation: choose a schedule and prove its cost is minimal.')
    y=ask(b,f,'C10',y,text='Find a schedule meeting the target. Equal steps are worth trying, but unequal ones are allowed. Give durations, estimate, and relative error.')
    y=blank(b,y,111,'Schedule / final estimate / relative error')
    y=ask(b,f,'C11',y,text='Prove fewer updates than your proposed minimum cannot meet the target. You may use: among nonnegative factors with a fixed sum, the equal factors give the largest product. Identify the factors and sum; include schedules with still fewer updates.')
    y=blank(b,y,143,'A lower bound for every shorter schedule')
    y=ask(b,f,'C12',y,text='Optional repair: choose the END slope, so y_new=y_old−h·y_new. Solve for y_new. Is it positive and settling for every h>0? Does that buy 10% accuracy with one step to t=1?')
    y=blank(b,y,88,'New update rule, behavior, and accuracy test')


def render_students(book,family_id):
    f=F[family_id]
    {'GA-11':render_ga11,'AP-26':render_ap26,'AP-07':render_ap07}[family_id](book,f)


def measured(text,size=11):
    style=ParagraphStyle('measured',fontName=FONT,fontSize=size,leading=size*1.35)
    return Paragraph(text_markup(text),style).wrap(524,1000)[1]


def section(b,title,paras):
    total=27+sum(measured(p)+9 for p in paras)
    # Keep a short prompt and its full answer together. Long overview sections
    # can flow paragraph by paragraph while the shared helper keeps headings.
    need=total if 'prompt and solution' in title and total<570 else 27+(measured(paras[0]) if paras else 0)+9
    if b.y+need>725:b.new_page(b.family_id,b.page_title,part='continued')
    b.flow_h(title)
    for text in paras:b.flow_p(text,size=11)


def render_facilitator(b,family_id):
    f=F[family_id]
    b.new_page(family_id,f['title'],'Facilitator key • independently checked mathematics; not classroom-piloted.')
    section(b,'Assessment and satisfying core',[f['potential'],f['satisfactory_core']])
    section(b,'Prerequisites and setup',[f['prerequisites']['core'],f['prerequisites']['extension'],f['prerequisites']['honest_stop'],f"Materials: {f['materials']} Preparation: about {f['preparation_minutes']} minutes.",f['suggested_timing']])
    section(b,'Launching and choosing an endpoint',[f['launch']]+f['facilitator']['satisfying_stops'])
    section(b,'What to watch for',f['facilitator']['common_pitfalls'])
    for page in f['student_pages']:
        section(b,f"Student page {page['page']}: {page['title']}",[page['lede']])
        for p in page['prompts']:
            pid=p['id']
            section(b,pid+' — prompt and solution',[p['text'],f['solutions'][pid]])
            section(b,pid+' — delayed hints',f['staged_hints'][pid])
    section(b,'Further problems with solutions', [p['prompt']+' '+p['solution'] for p in f['facilitator']['extensions']])
    section(b,'Sources and scope',[s['title']+'. '+s['locator']+' '+s['checked']+' '+s['url'] for s in f['sources']])
    section(b,'Prior-use and design distinction',[f['facilitator']['novelty'],'Exact checks: plans/atlas/worksheet-trial/systems-checks.py. The universal arguments above, not finite examples alone, support the general claims.'])
