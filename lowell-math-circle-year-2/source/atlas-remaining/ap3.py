"""Eight final applied-math investigations: student-owned constructions and exact diagrams."""
import math
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from sheet import FONT, BOLD, TEAL, GRAY, INK, LIGHT, PALE, WHITE, text_markup
from common import start, question, family_data

FAMILIES = family_data('ap3')


def ph(text):
    s=ParagraphStyle('ap3-measure',fontName=FONT,fontSize=11.5,leading=15.18)
    return Paragraph(text_markup(text),s).wrap(524,1000)[1]+8


def space(b,x,y,w,h,label='Your construction / certificate'):
    b.box(x,y,w,h,label=label)
    if h>76:
        for yy in range(int(y+48),int(y+h-9),27):
            b.line(x+10,yy,x+w-10,yy,LIGHT,.45)


def region(b,f,page,drawers,weights=None):
    start(b,f,page)
    qs=f['pages'][page-1]['prompts']; weights=weights or [1]*len(qs)
    free=738-b.y-sum(ph(q['id']+'. '+q['text']) for q in qs)-12*len(qs)
    assert free>140,(f['id'],page,free)
    for q,draw,weight in zip(qs,drawers,weights):
        question(b,f,q['id']);y=b.y;h=free*weight/sum(weights)
        (draw or space)(b,44,y,524,h)
        b.y=y+h+12


def side(figure,label='Work / explanation',left=225):
    def draw(b,x,y,w,h):
        figure(b,x,y,left-13,h)
        space(b,x+left,y,w-left,h,label)
    return draw


def graph(b,x,y,w,h,xmax=1,ymax=1,xlabel='x',ylabel='y',xticks=None,yticks=None):
    lx=x+31;ty=y+18;ww=w-51;hh=h-45
    def at(a,c):return lx+ww*a/xmax,ty+hh*(1-c/ymax)
    xticks=xticks if xticks is not None else [i*xmax/4 for i in range(5)]
    yticks=yticks if yticks is not None else [i*ymax/4 for i in range(5)]
    for a in xticks:
        xx,_=at(a,0);b.line(xx,ty,xx,ty+hh,LIGHT,.4)
        b.label(f'{a:g}',xx,ty+hh+5,size=8,align='center',color=GRAY)
    for c in yticks:
        _,yy=at(0,c);b.line(lx,yy,lx+ww,yy,LIGHT,.4)
        b.label(f'{c:g}',lx-6,yy-5,size=8,align='right',color=GRAY)
    b.line(lx,ty,lx,ty+hh,GRAY,.8);b.line(lx,ty+hh,lx+ww,ty+hh,GRAY,.8)
    b.label(xlabel,lx+ww+8,ty+hh-10,size=10)
    b.label(ylabel,lx-20,ty-15,size=10)
    return at


def channel(b,x,y,w,h):
    mid=x+w/2;yy=y+30
    b.line(x+5,yy,x+w-5,yy,TEAL,1.5)
    b.box(x+5,yy+9,w-10,38,fill=PALE,stroke=LIGHT)
    b.label('BED HIDDEN / NOT TO SCALE',mid,yy+21,size=8.5,align='center',color=GRAY)
    b.line(mid,yy+3,mid,yy+48,GRAY,.7,dash=[3,3])
    for t,xx in [('0',x+5),('6',mid),('12',x+w-5)]:
        b.line(xx,yy-4,xx,yy+4,TEAL);b.label(t,xx,yy-21,size=10,align='center')
    b.label('depth H₁',x+w/4,yy+58,size=10,align='center')
    b.label('depth H₂',x+3*w/4,yy+58,size=10,align='center')
    if h>119:
        b.label('end time 5',mid,yy+83,size=10,align='center')


def receivers(b,x,y,w,h):
    yy=y+43;b.line(x+10,yy,x+w-10,yy,TEAL,1.4)
    for t in [0,3,6,9,12]:
        xx=x+10+(w-20)*t/12;b.circle(xx,yy,3,WHITE,TEAL)
        b.label(str(t),xx,yy+12,size=10,align='center')
    b.label('Choose / mark a receiver.',x+w/2,y+8,size=10,align='center')
    b.label('launch',x+10,yy-20,size=9)
    b.label('end',x+w-10,yy-20,size=9,align='right')
    if h>120:space(b,x,y+91,w,h-91,'My extra information')


def intervals(b,x,y,w,h):
    for j,title in enumerate(['x=3, reported time 3/2','x=6, reported time 3']):
        xx=x+j*(w+14)/2;ww=(w-14)/2
        b.box(xx,y,ww,h,label=title)
        for k,name in enumerate(['u','v']):
            yy=y+50+k*min(45,(h-70)/2)
            b.label(name,xx+10,yy-7,size=11)
            b.line(xx+31,yy,xx+ww-14,yy,GRAY,.7)
        if h>160:b.label('Record endpoints and how u, v are linked.',xx+10,y+h-29,size=9,color=GRAY)


def recipes(b,x,y,w,h):
    for j,(name,colors,value) in enumerate([('A',['R','R','B'],3),('B',['R','B','B'],4)]):
        yy=y+14+j*63
        b.label(name,x+7,yy+12,size=12,font=BOLD)
        for k,c in enumerate(colors):
            xx=x+46+k*30;b.circle(xx,yy+19,11,PALE if c=='R' else WHITE,TEAL)
            b.label(c,xx,yy+12,size=10,align='center')
        b.label('→ '+str(value)+' points',x+125,yy+12,size=10)


def audit_prices(b,x,y,w,h):
    for j,name in enumerate(['one red: r =','one blue: b =']):
        yy=y+13+j*62;b.box(x+5,yy,w-10,48,label=name)


def stock_choices(b,x,y,w,h):
    for j,title in enumerate(['add RED','add BLUE']):
        xx=x+j*(w+14)/2;ww=(w-14)/2
        space(b,xx,y,ww,h,title+' / plan / upper bound / gain')


def payoff(b,x,y,w,h):
    b.label('Column pays Row',x+w/2,y+4,size=10,align='center')
    cell=42;lx=x+(w-3*cell)/2;ty=y+28
    for j,s in enumerate(['','L','R']):
        for i,r in enumerate(['','U','D']):
            b.box(lx+j*cell,ty+i*28,cell,28,stroke=LIGHT)
            txt=s if i==0 else r if j==0 else [['2','0'],['0','1']][i-1][j-1]
            b.label(txt,lx+j*cell+cell/2,ty+i*28+7,size=11,align='center')
    if h>145:b.label('My bag: __________________',x+7,ty+101,size=10)


def guarantees(b,x,y,w,h):
    graph(b,x,y,250,h,1,2,'p','pay',xticks=[0,.25,.5,.75,1],yticks=[0,.5,1,1.5,2])
    space(b,x+269,y,w-269,h,'Opponent comparisons / optimality proof')


def bag(b,x,y,w,h):
    b.poly([(x+24,y+16),(x+w-24,y+16),(x+w-5,y+89),(x+w-21,y+109),(x+21,y+109),(x+5,y+89),(x+24,y+16)],stroke=TEAL)
    b.label('Design your randomizer',x+w/2,y+39,size=10,align='center')
    b.label('P(L) = __________',x+w/2,y+68,size=11,align='center')


def probability_ranges(b,x,y,w,h):
    for j,name in enumerate(['Row p','Column q']):
        yy=y+30+j*min(66,(h-55)/2)
        b.label(name,x,y+2+j*min(66,(h-55)/2),size=10)
        b.line(x+40,yy,x+w-8,yy,GRAY)
        for val in [0,.5,1]:
            xx=x+40+(w-48)*val;b.line(xx,yy-4,xx,yy+4,GRAY)
            b.label(str(val),xx,yy+8,size=9,align='center')


def history(b,x,y,w,h):
    gap=18;ww=(w-gap)/2;rh=(h-26)/4
    for j,title in enumerate(['A color is lost','Always mixed so far']):
        xx=x+j*(ww+gap);b.label(title,xx+ww/2,y,size=10,align='center')
        for n in range(4):
            yy=y+24+n*rh;b.label('n='+str(n),xx+2,yy+4,size=9)
            for k in range(2):
                cx=xx+71+k*72;b.circle(cx,yy+9,10,WHITE,TEAL)
                if n==0:b.label(['R','B'][k],cx,yy+3,size=10,align='center')
                if n>0:
                    b.label('parent ___',cx,yy+23,size=8,align='center',color=GRAY)


def offspring(b,x,y,w,h):
    b.label('OLD parents',x+w/2,y,size=10,align='center')
    for k,s in enumerate(['R','B']):
        xx=x+w*(k+1)/3;b.circle(xx,y+32,12,WHITE,TEAL);b.label(s,xx,y+25,size=11,align='center')
    b.label('Each child draws from OLD.',x+w/2,y+59,size=9,align='center',color=GRAY)
    for k in range(2):
        xx=x+w*(k+1)/3;b.box(xx-30,y+84,60,31,label='child '+str(k+1))


def transitions(b,x,y,w,h):
    b.label('Fill each row; check its sum.',x,y,size=10,color=GRAY)
    cols=[54]+[(w-54)/4]*4;labels=['from','to 0','to 1','to 2','to 3'];xx=x
    for cw,s in zip(cols,labels):b.box(xx,y+24,cw,28);b.label(s,xx+cw/2,y+32,size=10,align='center');xx+=cw
    rh=min(43,(h-54)/2)
    for j in range(2):
        xx=x
        for k,cw in enumerate(cols):
            b.box(xx,y+52+j*rh,cw,rh)
            if k==0:b.label(str(j+1),xx+cw/2,y+63+j*rh,size=11,align='center')
            xx+=cw


def reaction(b,x,y,w,h):
    b.label('one legal forward firing',x+w/2,y+3,size=10,align='center')
    yy=y+43
    for xx,s in [(x+18,'A'),(x+57,'B'),(x+87,'B')]:
        b.circle(xx,yy,12,WHITE,TEAL);b.label(s,xx,yy-7,size=10,align='center')
    b.arrow(x+109,yy,x+155,yy,TEAL)
    b.box(x+168,yy-13,27,27,stroke=TEAL);b.label('C',x+181,yy-7,size=10,align='center')
    b.label('Only fire when ingredients exist.',x+w/2,yy+30,size=9,align='center',color=GRAY)


def weights(b,x,y,w,h):
    for j,title in enumerate(['Weight system I','Weight system II']):
        xx=x+j*(w+14)/2;ww=(w-14)/2;b.box(xx,y,ww,h,label=title)
        b.label('A: ____   B: ____   C: ____',xx+12,y+35,size=11)
        b.label('Total before / after:',xx+12,y+66,size=10)


def state_chain(b,x,y,w,h):
    b.box(x,y,w,h,label='Arrange your states and draw legal arrows; use more space if needed.')


def tanks(b,x,y,w,h):
    for j,s in enumerate(['a','b']):
        xx=x+15+j*(w/2);ww=w/2-24
        b.box(xx,y+18,ww,65,fill=PALE,stroke=GRAY)
        b.label(s+' hidden',xx+ww/2,y+40,size=10,align='center')
    b.label('No drawn fill levels are data.',x+w/2,y+99,size=9,align='center',color=GRAY)
    if h>144:
        b.label('sensor: sum only',x+w/2,y+124,size=11,align='center')


def reading_cone(b,x,y,w,h):
    graph(b,x,y,255,h,8,5,'y₀','y₁',xticks=[0,2,4,6,8],yticks=[0,1,2,3,4,5])
    space(b,x+272,y,w-272,h,'All feasible readings / include boundaries')


def delay_record(b,x,y,w,h):
    b.box(x,y,w,h,label='Choose trial delays; then explain what happens for all later delays.')
    for j,label in enumerate(['chosen k','reconstruction / evidence','error bound']):
        b.label(label,x+[12,145,352][j],y+33,size=10,color=GRAY)
    for yy in range(int(y+64),int(y+h-8),30):b.line(x+10,yy,x+w-10,yy,LIGHT,.5)


def bits(b,x,y,word='',n=5,cell=25,label=None):
    if label:b.label(label,x-11,y+7,size=10,align='right')
    for k in range(n):
        b.box(x+k*cell,y,cell,cell,stroke=GRAY)
        if word:b.label(word[k],x+k*cell+cell/2,y+6,size=11,align='center')


def design_code(b,x,y,w,h):
    for j,name in enumerate(['A','B','C','D']):
        xx=x+27+(j%2)*260;yy=y+16+(j//2)*min(62,(h-41)/2)
        bits(b,xx,yy,label=name,cell=31)
    if h>153:b.label('Use the rest for revisions or an ambiguous received strip.',x+9,y+h-24,size=9,color=GRAY)


def audit_code(b,x,y,w,h):
    for j,(s,word) in enumerate([('A','00000'),('B','11100'),('C','10011'),('D','01111')]):
        bits(b,x+19+(j%2)*140,y+12+(j//2)*40,word,cell=20,label=s)
    space(b,x+288,y,w-288,h,'Pair distances / decode / rule')
    if h>132:b.label('Keep the at-most-one-flip promise.',x+10,y+112,size=9,color=GRAY)


def received_words(b,x,y,w,h):
    b.box(x,y,w,h,label='An outside word / evidence / a two-flip deception')
    for j,name in enumerate(['outside','sent','received']):
        bits(b,x+75+j*149,y+39,n=5,cell=21)
        b.label(name,x+125+j*149,y+70,size=9,align='center',color=GRAY)
    if h>137:b.line(x+12,y+117,x+w-12,y+117,LIGHT,.5)


def three_bit(b,x,y,w,h):
    for j,name in enumerate(['A','B','C','D']):
        bits(b,x+26+(j%2)*126,y+14+(j//2)*46,n=3,cell=24,label=name)
    space(b,x+269,y,w-269,h,'Detection proof / correction ambiguity')


def resistor(b,x1,y1,x2,y2,label):
    # The circuit uses unambiguous rectangular resistor symbols.
    if x1==x2:
        mid=(y1+y2)/2;b.line(x1,y1,x1,mid-14,TEAL,1.2);b.box(x1-7,mid-14,14,28,stroke=TEAL);b.line(x1,mid+14,x2,y2,TEAL,1.2)
        b.label(label,x1+12,mid-7,size=10)
    else:
        mid=(x1+x2)/2;b.line(x1,y1,mid-15,y1,TEAL,1.2);b.box(mid-15,y1-7,30,14,stroke=TEAL);b.line(mid+15,y1,x2,y2,TEAL,1.2)
        b.label(label,mid,y1-25,size=10,align='center')


def circuit(b,x,y,w,h,meters=1,value='R'):
    # All branches share the same explicitly marked node and ground rail.
    top=y+18;mid=y+78;bottom=min(y+h-24,y+149)
    cx=x+35;right=x+w-22
    b.label('6 V',cx-10,top-15,size=10,align='right')
    resistor(b,cx,top,cx,mid,'2 Ω');b.circle(cx,top,2.5,TEAL,TEAL)
    resistor(b,cx,mid,cx,bottom,'1 Ω')
    b.circle(cx,mid,3,TEAL,TEAL);b.label('X',cx-11,mid-6,size=11,align='right')
    b.line(cx,bottom,right,bottom,TEAL,1.2);b.label('0 V / ground',cx+8,bottom+8,size=9)
    if meters:
        b.line(cx,mid,right,mid,TEAL,1.2)
        for i in range(meters):
            xx=cx+(right-cx)*(i+1)/meters
            resistor(b,xx,mid,xx,bottom,value)
            b.circle(xx,mid,2.5,TEAL,TEAL);b.circle(xx,bottom,2.5,TEAL,TEAL)


def power_record(b,x,y,w,h):
    b.box(x,y,w,h,label='Power audit / then treat the ideal wire separately')
    for j,s in enumerate(['source','2 Ω','1 Ω','meter']):
        xx=x+12+j*127;b.label(s,xx,y+34,size=10)
        b.line(xx,y+66,xx+105,y+66,LIGHT,.6)


DRAWERS={
 'AP-19':[[side(channel,'Chosen depths / verify total time'),None],
          [side(receivers,'Recover / explain new information'),None],[intervals,None]],
 'AP-20':[[side(recipes,'Plan / ingredients used / leftovers'),None],[side(audit_prices,'Check recipes / prove universal bound'),None],[None,stock_choices]],
 'AP-22':[[side(payoff,'My bag / expected payments / revision'),guarantees],[side(bag,'Upper bound / uniqueness'),None],[side(probability_ranges,'Endpoints / necessity / sufficiency'),None]],
 'AP-24':[[history,side(offspring,'Ordered choices / probabilities / mean')],[None,None],[transitions,None]],
 'AP-25':[[side(reaction,'My target / legal firings / count change'),weights],[None,state_chain],[None,None]],
 'AP-27':[[side(tanks,'Two hidden starts / entire record'),None],[None,reading_cone],[None,delay_record]],
 'AP-28':[[design_code,None],[audit_code,None],[received_words,three_bit]],
 'AP-30':[[side(lambda *a:circuit(*a,meters=0),'Trial voltage / balance / uniqueness'),side(circuit,'My R / voltage / three currents')],
          [side(circuit,'Formulas / finite R / ideal limit'),None],[power_record,side(lambda *a:circuit(*a,meters=2,value='R'),'Two readings / m branches / design bound')]]
}


def render_students(book,family_id):
    f=FAMILIES[family_id]
    for i,drawers in enumerate(DRAWERS[family_id],1):
        weights=[1,1]
        if family_id=='AP-24' and i==1:weights=[1.18,1]
        if family_id=='AP-30' and i==3:weights=[.8,1.2]
        region(book,f,i,drawers,weights)


def render_key_figures(b,family_id):
    if family_id not in ['AP-19','AP-24','AP-28','AP-30']:return
    b.new_page(family_id,FAMILIES[family_id]['title'],'Worked visual / facilitator only')
    if family_id=='AP-19':
        b.p('A single end reading leaves a whole positive line of slowness pairs. The endpoints are excluded: they would require an infinite depth.',size=11)
        y=b.y+20;at=graph(b,70,y,440,280,1,1,'u','v')
        b.line(*at(0,5/6),*at(5/6,0),TEAL,2)
        for u,v in [(0,5/6),(5/6,0)]:b.circle(*at(u,v),4,WHITE,TEAL)
        b.circle(*at(.5,1/3),4,TEAL,TEAL)
        px,py=at(.5,1/3);b.label('(1/2, 1/3): depths (4, 9)',px-27,py-25,size=10)
        b.y=y+300;b.flow_p('For x=6, the interior reading S=3 fixes u=S/6=1/2 and v=(5−S)/6=1/3. Under |e|≤1/20, the two recovered slowness errors have equal magnitude and opposite signs; they do not independently fill a rectangle.',size=11)
    elif family_id=='AP-24':
        b.p('The two-parent count chain has only one transient state. Its outgoing probabilities explain both the unchanged mean and the vanishing chance of a mixed population.',size=11)
        y=b.y+110
        for x,label in [(115,'0 red'),(305,'1 red'),(495,'2 red')]:
            b.circle(x,y,31,PALE,TEAL);b.label(label,x,y-7,size=12,align='center')
        b.arrow(272,y,150,y,TEAL);b.label('1/4',207,y-24,size=11,align='center')
        b.arrow(338,y,460,y,TEAL);b.label('1/4',401,y-24,size=11,align='center')
        b.poly([(284,y-27),(284,y-69),(328,y-69),(328,y-28)],stroke=TEAL)
        b.arrow(328,y-49,328,y-29,TEAL);b.label('1/2',306,y-92,size=11,align='center')
        b.label('absorbing',115,y+44,size=10,align='center');b.label('absorbing',495,y+44,size=10,align='center')
        b.y=y+97;b.flow_p('Starting in the middle: P(X_k=1)=2^(−k). The two absorbing probabilities are each (1−2^(−k))/2. Hence E[X_k]=1 for every finite k, even when almost all histories have lost a color.',size=11)
    elif family_id=='AP-28':
        b.p('Six distance checks certify the supplied construction. Every allowed received strip has exactly one codeword within distance one.',size=11)
        y=b.y+20
        for j,(name,word) in enumerate([('A','00000'),('B','11100'),('C','10011'),('D','01111')]):bits(b,95,y+j*47,word,label=name,cell=32)
        pairs=[('AB',3),('AC',3),('AD',4),('BC',4),('BD',3),('CD',3)]
        for j,(pair,d) in enumerate(pairs):b.label(pair+': '+str(d),350+(j%2)*80,y+(j//2)*46+15,size=12)
        b.y=y+211;b.flow_p('Each length-five codeword has 1+5=6 allowed received words. The four disjoint neighborhoods cover 24 of the 32 possible strips. The outside word 00110 has distances 2, 3, 3, 2; a promise-respecting transmission cannot produce it.',size=11)
        b.flow_p('For the extension, the five single-bit syndromes are (1,0), (1,1), (0,1), (1,0), (0,1). All single flips are detected, but repeated columns prevent unique correction. More generally, exactly the 24 error patterns with nonzero syndrome are detected.',size=11)
    elif family_id=='AP-30':
        b.p('Loaded circuit with R=2 Ω. The listed I values are currents, while X is a voltage. All branches meet at the filled junctions.',size=11)
        y=b.y+28;circuit(b,62,y,230,242,meters=1,value='2 Ω')
        b.label('X = 3/2 V',330,y+40,size=12)
        b.label('I_in = 9/4 A',330,y+76,size=12)
        b.label('I_lower = 3/2 A',330,y+112,size=12)
        b.label('I_meter = 3/4 A',330,y+148,size=12)
        b.y=y+246;b.flow_p('Source power: 6·(9/4)=27/2 W. Dissipation: upper 81/8 W, lower 9/4 W, meter 9/8 W; these sum to 27/2 W. The voltage 3/2 V is smaller than the unloaded 2 V even though the meter reports its own loaded voltage exactly.',size=11)
